#!/usr/bin/env python3
"""Reviewer, judge, extractor and recognition runs through the model APIs.

    python3 research/eval/api/run.py inputs  --set referee16
    python3 research/eval/api/run.py review  --set pilot5 --arm plain --model opus --runs 1
    python3 research/eval/api/run.py rank    --set pilot5 --arm plain.opus            # ranker = the reviewer model
    python3 research/eval/api/run.py judge   --set pilot5 --arm plain.opus --judge sonnet
    python3 research/eval/api/run.py overlap --set pilot5 --arm v1.opus --base plain.opus --judge sonnet
    python3 research/eval/api/run.py merge   --set dev30 --arm liang.opus --out liangx3       # runs merged into one review
    python3 research/eval/api/run.py extract --set tierC --model opus
    python3 research/eval/api/run.py recommend --set rec20 --model opus
    python3 research/eval/api/run.py apply-recommend --set rec20 --model opus   # into referee.json
    python3 research/eval/api/run.py recognize --set tierC --model opus
    python3 research/eval/api/run.py collect          # fetch every finished batch
    python3 research/eval/api/run.py collect --wait   # every minute until done; exits 3 on a stall
    python3 research/eval/api/run.py status           # progress of every pending batch; flags stalls
    python3 research/eval/api/run.py rescue --batch <id>   # cancel a stalled batch; collect keeps what finished
    python3 research/eval/api/run.py cost             # spend so far, from costs.csv

Add --sync to call the API directly (twice the price, no waiting; --parallel N runs N calls at
once) and --dry-run to print the requests without sending. Batches are recorded in batches.json
until collected.

Batch watch (config.json batch_watch). Each submit also sends a one-request canary batch to the
same model. status and collect poll every pending batch and append a row to batch_log.csv
(time, batch, state, done of total, age), so a slow batch leaves a record of when its requests
finished. A batch is flagged STALLED when it is older than stall_minutes and has finished
nothing new for no_progress_minutes. The canary tells the two causes apart: a canary that is
also slow means the provider's queue; a canary that finished in minutes points at the batch's
own requests (size, very long outputs). rescue cancels a batch; collect then saves whatever
finished, and the next run of the same step, with --sync, sends only what is still missing.
Every response cut off at its token limit is reported as TRUNCATED; config.json is read when
a run starts, so a raised limit needs a new run.

An arm is a folder name: <variant>.<model> for API reviews (plain.opus), or legacy.assistant and
legacy.plain for the experiment 11 reviews (assistant-r1/report.md, plain/review.txt), which are
ranked and judged in place. Judge calls use prompts/judge_v2.md: one review per call, the review
blinded (blind.py), referee concerns and the review's ranked points each in a seeded random
order, with the point ids mapped back to ranks in the saved file (_points_rank).

Where things go, under eval/referee/<id>/api/:
  <arm>/r<k>.txt                           a review (API arms; raw model output, kept as .txt so the docs style check skips it)
  <arm>/r<k>.rank.<model>.json             the reviewer model's own ranked list of its concerns
  <arm>/r<k>.judge.<judge>.json            the judge's verdicts on that review (judge v2)
  <arm>/r<k>.overlap.<base>.<judge>.json   which of its unmatched substantive points the base arm also raised
  extract.<model>.json                     extracted referee concerns (copied to referee.json by hand)
  recommend.<model>.json                   each referee's first-round recommendation (apply-recommend copies it)
  recognize.<model>.json                   the recognition probe
Every call's tokens and cost go to eval/costs.csv.
"""
import argparse
import csv
import datetime
import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import providers  # noqa: E402
from blind import blind, shuffled  # noqa: E402

HERE = Path(__file__).resolve().parent
EVAL = HERE.parent
REF = EVAL / "referee"
CFG = json.loads((HERE / "config.json").read_text())
WATCH = CFG.get("batch_watch", {})
BATCHES = HERE / "batches.json"
COSTS = EVAL / "costs.csv"
BATCH_LOG = HERE / "batch_log.csv"
V1 = providers.CACHE / "v1"
EXCLUDED = ("presentation or clarity", "novelty, significance or prior work")
LEGACY = {"legacy.assistant": "assistant-r1/report.md", "legacy.plain": "plain/review.txt"}
SCALE = ("accept", "minor revision", "major revision", "reject")


def model_cfg(name):
    m = CFG["models"][name]
    if not m["id"]:
        sys.exit(f"model {name}: id not set in config.json (check the provider's official model list first)")
    return m


def paper_set(name):
    return json.loads((HERE / "sets.json").read_text())[name]


# ---------- inputs ----------

def v1_pdf(pid):
    p = V1 / f"{pid}v1.pdf"
    if not p.exists():
        V1.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(f"https://arxiv.org/pdf/{pid}v1", headers={"User-Agent": "cmp-assistant-eval"})
        p.write_bytes(urllib.request.urlopen(req, timeout=120).read())
        time.sleep(3.2)
    if p.stat().st_size > 30e6:
        # Claude takes PDFs up to 32 MB: images downsampled to 150 dpi, text untouched.
        small = V1 / f"{pid}v1.small.pdf"
        if not small.exists():
            import pymupdf
            d = pymupdf.open(p)
            d.rewrite_images(dpi_threshold=200, dpi_target=150, quality=75)
            d.save(small, garbage=3, deflate=True)
        return small
    return p


def v1_text(pid):
    t = V1 / f"{pid}v1.txt"
    if not t.exists():
        subprocess.run(["pdftotext", str(v1_pdf(pid)), str(t)], check=True)
    return t.read_text(errors="ignore")


def peer_review_url(pid):
    cands = json.loads((REF / "candidates.json").read_text())
    pool = REF / "pool.json"
    rows = cands["candidates"] + cands["early_candidates"] + (json.loads(pool.read_text())["papers"] if pool.exists() else [])
    return next(r["peer_review_url"] for r in rows if r["arxiv_id"] == pid)


def peer_review_pdf(pid):
    p = providers.CACHE / "peer_review" / f"{pid}.pdf"
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(urllib.request.urlopen(urllib.request.Request(peer_review_url(pid), headers={"User-Agent": "cmp-assistant-eval"}),
                                             timeout=120).read())
    return p


def peer_review_part(pid):
    """The peer review file as a request part: the PDF, or for a web page (SciPost) its text."""
    url = peer_review_url(pid)
    if not url.lower().split("?")[0].endswith(".pdf") and "scipost.org" in url:
        t = providers.CACHE / "peer_review" / f"{pid}.txt"
        if not t.exists():
            import html
            page = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "cmp-assistant-eval"}),
                                          timeout=120).read().decode("utf-8", "ignore")
            page = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", page)
            text = html.unescape(re.sub(r"(?s)<[^>]+>", " ", page))
            t.parent.mkdir(parents=True, exist_ok=True)
            t.write_text(re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n\n", text)).strip())
        return {"text": "# Peer review page (" + url + ")\n\n" + t.read_text()}
    f = peer_review_pdf(pid)
    if f.read_bytes()[:2] == b"PK":  # a Word file served under a .pdf name
        import zipfile
        xml = zipfile.ZipFile(f).read("word/document.xml").decode("utf-8", "ignore")
        xml = re.sub(r"</w:p>", "\n", xml)
        text = re.sub(r"<[^>]+>", "", xml)
        import html
        return {"text": "# Peer review file (Word document, converted to text)\n\n" + html.unescape(text)}
    return {"pdf": str(f)}


# ---------- requests ----------

def review_requests(pids, arm, model, runs):
    # Third-party prompts kept verbatim are .txt (outside the docs style check); our own are .md.
    f = HERE / "arms" / f"{arm}.md"
    prompt = (f if f.exists() else f.with_suffix(".txt")).read_text().strip()
    reqs = []
    for pid in pids:
        for k in range(1, runs + 1):
            out = REF / pid / "api" / f"{arm}.{model}" / f"r{k}.txt"
            if out.exists():
                continue
            reqs.append({"id": f"review|{pid}|{arm}|{model}|{k}", "max_tokens": CFG["max_tokens"]["review"],
                         "parts": [{"pdf": str(v1_pdf(pid)), "cache": True}, {"text": prompt}]})
    return reqs


def update_batches(fn):
    """Read, change and write batches.json under a file lock, so two runs (a background collect and
    a status check) never overwrite each other's records. fn takes the list and returns the new one."""
    import fcntl
    with open(BATCHES.with_suffix(".lock"), "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        recs = json.loads(BATCHES.read_text()) if BATCHES.exists() else []
        recs = fn(recs)
        BATCHES.write_text(json.dumps(recs, indent=1))
        return recs


def _merge_seen(polled):
    """For update_batches: copy the progress marks of polled records onto the current file."""
    seen = {r["batch"]: r.get("seen") for r in polled if r.get("seen")}
    def fn(recs):
        for r in recs:
            if r["batch"] in seen:
                r["seen"] = seen[r["batch"]]
        return recs
    return fn


def merge_requests(pids, arm, model, out_arm):
    """One call per paper: the arm's reviews merged into one deduplicated, prioritized review."""
    tmpl = (HERE / "prompts" / "merge.md").read_text()
    reqs = []
    for pid in pids:
        rs = reviews(pid, arm)
        if len(rs) < 2 or (REF / pid / "api" / f"{out_arm}.{model}" / "r1.txt").exists():
            continue
        body = "\n\n".join(f"=== Review {i} ===\n{f.read_text()}" for i, (_, f) in enumerate(rs, 1))
        reqs.append({"id": f"review|{pid}|{out_arm}|{model}|1", "max_tokens": CFG["max_tokens"]["review"],
                     "parts": [{"text": tmpl.format(n=len(rs), reviews=body)}]})
    return reqs


def reviews(pid, arm):
    """(k, path) for every review of this arm on this paper."""
    if arm in LEGACY:
        f = REF / pid / LEGACY[arm]
        return [("1", f)] if f.exists() else []
    d = REF / pid / "api" / arm
    return [(f.stem[1:], f) for f in sorted(d.glob("r*.txt")) if f.stem[1:].isdigit()] if d.exists() else []


def arm_dir(pid, arm):
    return REF / pid / "api" / arm


def default_ranker(arm):
    """The reviewer model ranks its own review; the experiment 11 reviews are ranked by opus."""
    return "opus" if arm in LEGACY else arm.rsplit(".", 1)[1]


def rank_requests(pids, arm, ranker):
    prompt = (HERE / "prompts" / "rank.md").read_text().strip()
    reqs = []
    for pid in pids:
        for k, f in reviews(pid, arm):
            if (arm_dir(pid, arm) / f"r{k}.rank.{ranker}.json").exists():
                continue
            reqs.append({"id": f"rank|{pid}|{arm}|{k}|{ranker}", "max_tokens": CFG["max_tokens"]["rank"],
                         "parts": [{"text": prompt.replace("{review}", f.read_text())}]})
    return reqs


def concerns_for_judge(pid):
    """Eligible first-round concerns; fixed_in_v1 taken from the earlier judge where it exists."""
    ref = json.loads((REF / pid / "referee.json").read_text())
    fixed = set()
    old = REF / pid / "judge.json"
    if old.exists():
        fixed = {m["concern"] for m in json.loads(old.read_text())["matches"] if m.get("fixed_in_v1")}
    return [{k: c[k] for k in ("id", "category", "severity", "quote", "summary")}
            for c in ref["concerns"] if c["category"] not in EXCLUDED and c["id"] not in fixed
            and (old.exists() or c.get("in_v1") is not False)]


def ranked_points(pid, arm, k, ranker):
    """The ranked concerns in a seeded random order, as P ids, and the map from P id to rank."""
    r = json.loads((arm_dir(pid, arm) / f"r{k}.rank.{ranker}.json").read_text())
    items = shuffled(sorted(r["concerns"], key=lambda c: c["rank"]), f"{pid}|{arm}|{k}")
    pts = [{"id": f"P{i}", "point": c["concern"]} for i, c in enumerate(items, 1)]
    return pts, {f"P{i}": c["rank"] for i, c in enumerate(items, 1)}


def judge_requests(pids, arm, judge, ranker):
    prompt = (HERE / "prompts" / "judge_v2.md").read_text().strip()
    reqs = []
    for pid in pids:
        for k, f in reviews(pid, arm):
            if (arm_dir(pid, arm) / f"r{k}.judge.{judge}.json").exists():
                continue
            if not (arm_dir(pid, arm) / f"r{k}.rank.{ranker}.json").exists():
                print(f"  skip {pid} {arm} r{k}: no rank.{ranker} yet")
                continue
            pts, _ = ranked_points(pid, arm, k, ranker)
            shared = (f"{prompt}\n\n# Paper text (arXiv v1)\n\n{v1_text(pid)}\n\n# Referee concerns\n\n"
                      + json.dumps(shuffled(concerns_for_judge(pid), pid), indent=1))
            reqs.append({"id": f"judge|{pid}|{arm}|{k}|{judge}|{ranker}", "max_tokens": CFG["max_tokens"]["judge"],
                         "parts": [{"text": shared, "cache": True},
                                   {"text": "# Review\n\n" + blind(f.read_text())
                                    + "\n\n# Review points\n\n" + json.dumps(pts, indent=1)}]})
    return reqs


def overlap_requests(pids, arm, base, judge, ranker_base):
    """For each review of arm: its substantive points no referee raised, against every point the base arm made."""
    prompt = (HERE / "prompts" / "overlap.md").read_text().strip()
    reqs = []
    for pid in pids:
        b = []
        for k, _ in reviews(pid, base):
            rf = arm_dir(pid, base) / f"r{k}.rank.{ranker_base}.json"
            if rf.exists():
                b += [c["concern"] for c in json.loads(rf.read_text())["concerns"]]
        if not b:
            continue
        b_list = json.dumps([{"id": f"B{i}", "concern": c} for i, c in enumerate(b, 1)], indent=1)
        for k, _ in reviews(pid, arm):
            jf = arm_dir(pid, arm) / f"r{k}.judge.{judge}.json"
            out = arm_dir(pid, arm) / f"r{k}.overlap.{base}.{judge}.json"
            if out.exists() or not jf.exists():
                continue
            j = json.loads(jf.read_text())
            ranker = j["_meta"].get("ranker", default_ranker(arm))
            pts, _ = ranked_points(pid, arm, k, ranker)
            text = {p["id"]: p["point"] for p in pts}
            a = [{"id": p["id"].replace("P", "A"), "concern": text[p["id"]]} for p in j["points"]
                 if p.get("quality") == "substantive" and not p.get("matches") and not p.get("partly") and p["id"] in text]
            if not a:
                continue
            reqs.append({"id": f"overlap|{pid}|{arm}|{k}|{base}|{judge}", "max_tokens": CFG["max_tokens"]["judge"],
                         "parts": [{"text": prompt.replace("{a}", json.dumps(a, indent=1)).replace("{b}", b_list)}]})
    return reqs


def recommend_requests(pids, model):
    prompt = (HERE / "prompts" / "recommend.md").read_text().strip()
    return [{"id": f"recommend|{pid}|{model}", "max_tokens": CFG["max_tokens"]["recommend"],
             "parts": [peer_review_part(pid), {"text": prompt}]}
            for pid in pids if not (REF / pid / "api" / f"recommend.{model}.json").exists()]


def apply_extract(pids, model):
    """Copy extract.<model>.json to referee.json for papers that have none (never overwrites)."""
    for pid in pids:
        src, dst = REF / pid / "api" / f"extract.{model}.json", REF / pid / "referee.json"
        if not src.exists():
            print(f"{pid}: no extract.{model}.json")
            continue
        if dst.exists():
            print(f"{pid}: referee.json exists, left as is")
            continue
        d = json.loads(src.read_text())
        meta = d.pop("_meta", {})
        out = {"paper": pid, **d, "source": f"api/extract.{model}.json", "extracted": meta.get("date"),
               "model": meta.get("model"), "checked": "ai"}
        dst.write_text(json.dumps(out, indent=1, ensure_ascii=False))
        n = len(d.get("concerns", []))
        el = sum(c.get("category") not in EXCLUDED for c in d.get("concerns", []))
        print(f"{pid}: {n} first-round concerns, {el} outside presentation and novelty")


def apply_recommend(pids, model):
    """Copy recommend.<model>.json into referee.json and label the paper clean or contested."""
    for pid in pids:
        src = REF / pid / "api" / f"recommend.{model}.json"
        if not src.exists():
            print(f"{pid}: no recommend.{model}.json")
            continue
        rec = json.loads(src.read_text())
        rf = REF / pid / "referee.json"
        ref = json.loads(rf.read_text())
        rows = [{k: r.get(k) for k in ("referee", "recommendation", "explicit", "quote")} for r in rec["referees"]]
        bad = [r for r in rows if r["recommendation"] not in SCALE]
        label = "unclear" if bad or not rows else (
            "clean" if all(r["recommendation"] in ("accept", "minor revision") for r in rows) else "contested")
        ref["recommendations"] = {"first_round": rows, "note": rec.get("note", ""), "label": label,
                                  "source": f"api/recommend.{model}.json", "checked": "ai"}
        rf.write_text(json.dumps(ref, indent=1, ensure_ascii=False))
        print(f"{pid}: {label} ({', '.join(r['recommendation'] or '?' for r in rows)})")


def extract_requests(pids, model):
    prompt = (HERE / "prompts" / "extract.md").read_text().strip()
    return [{"id": f"extract|{pid}|{model}", "max_tokens": CFG["max_tokens"]["extract"],
             "parts": [peer_review_part(pid), {"pdf": str(v1_pdf(pid))}, {"text": prompt}]}
            for pid in pids if not (REF / pid / "api" / f"extract.{model}.json").exists()]


def recognize_requests(pids, model):
    prompt = (HERE / "prompts" / "recognize.md").read_text().strip()
    meta = {p["id"]: p for p in json.loads((REF / "papers.json").read_text())["papers"]}
    reqs = []
    for pid in pids:
        if (REF / pid / "api" / f"recognize.{model}.json").exists():
            continue
        m = meta[pid]
        desc = f"Title: {m['title']}\nJournal: {m['journal']}, published {m['pub_date']}\narXiv: {pid}"
        reqs.append({"id": f"recognize|{pid}|{model}", "max_tokens": CFG["max_tokens"]["recognize"],
                     "parts": [{"text": prompt.replace("{paper}", desc)}]})
    return reqs


# ---------- results ----------

def out_path(rid):
    f = rid.split("|")
    kind, pid = f[0], f[1]
    d = REF / pid / "api"
    if kind == "review":
        return d / f"{f[2]}.{f[3]}" / f"r{f[4]}.txt"
    if kind == "rank":
        return d / f[2] / f"r{f[3]}.rank.{f[4]}.json"
    if kind == "judge":
        return d / f[2] / f"r{f[3]}.judge.{f[4]}.json"
    if kind == "overlap":
        return d / f[2] / f"r{f[3]}.overlap.{f[4]}.{f[5]}.json"
    return d / f"{kind}.{f[2]}.json"


def parse_json(text):
    s = text.strip()
    if s.startswith("```"):
        s = s.split("\n", 1)[1].rsplit("```", 1)[0]
    s = s[s.find("{"): s.rfind("}") + 1]
    try:
        return json.loads(s)
    except ValueError:
        # LaTeX in quoted strings (\phi, \Delta) is not a valid JSON escape: double those backslashes.
        return json.loads(re.sub(r'\\(?!["\\/bfnrtu])', r"\\\\", s))


def save(rid, res, model_name, batch, sync):
    path = out_path(rid)
    log_cost(rid, res, model_name, batch, sync)
    if str(res.get("stop") or "").upper().endswith("MAX_TOKENS"):
        print(f"  TRUNCATED {rid}: output hit its token limit (max_tokens in config.json)")
    if res.get("error") or not res["text"]:
        print(f"  failed {rid}: {res.get('error') or 'empty'}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".json":
        try:
            data = parse_json(res["text"])
        except ValueError:
            path.with_suffix(".raw.txt").write_text(res["text"])
            print(f"  unparsed JSON {rid}: kept {path.with_suffix('.raw.txt').name}")
            return
        data["_meta"] = {"model": CFG["models"][model_name]["id"], "settings": CFG["models"][model_name].get("settings", {}),
                         "date": datetime.date.today().isoformat(), "stop": res.get("stop"), "usage": res["usage"]}
        f = rid.split("|")
        if f[0] == "judge":
            data["_meta"].update(prompt="judge_v2.md", ranker=f[5], blinded=True)
            data["_points_rank"] = ranked_points(f[1], f[2], f[3], f[5])[1]
        path.write_text(json.dumps(data, indent=1))
    else:
        path.write_text(res["text"])


def log_cost(rid, res, model_name, batch, sync):
    u = res.get("usage") or {}
    price = CFG["models"][model_name]["batch_price"]
    cost = ""
    if price and u:
        cost = sum(u.get(k, 0) * price[k] for k in price) / 1e6 * (2 if sync else 1)
        cost = f"{cost:.5f}"
    new = not COSTS.exists()
    with COSTS.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["time", "request", "model", "settings", "mode", "batch", "input", "cache_write", "cache_read",
                        "output", "stop", "cost_usd", "error"])
        w.writerow([datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), rid,
                    CFG["models"][model_name]["id"], json.dumps(CFG["models"][model_name].get("settings", {})),
                    "sync" if sync else "batch", batch,
                    u.get("input", ""), u.get("cache_write", ""), u.get("cache_read", ""), u.get("output", ""),
                    res.get("stop") or "", cost, (res.get("error") or "")[:200]])


def send(reqs, model_name, sync, dry, parallel=1):
    pending = {i for b in (json.loads(BATCHES.read_text()) if BATCHES.exists() else []) for i in b["ids"]}
    reqs = [r for r in reqs if r["id"] not in pending]  # already waiting in a batch
    if not reqs:
        print("nothing to do")
        return
    if dry:
        for r in reqs:
            parts = [("pdf:" + Path(p["pdf"]).name) if "pdf" in p else f"text:{len(p['text'])} chars" for p in r["parts"]]
            print(r["id"], parts)
        print(f"{len(reqs)} requests (dry run)")
        return
    cap = CFG["models"][model_name].get("max_output")
    if cap:
        reqs = [dict(r, max_tokens=cap) for r in reqs]
    prov = providers.make(model_cfg(model_name))
    if sync:
        def one(r):
            print("sync", r["id"], flush=True)
            try:
                res = prov.sync(r)
            except Exception as e:  # keep going; the error lands in costs.csv
                res = {"text": "", "usage": None, "error": repr(e)[:300]}
            save(r["id"], res, model_name, "", True)
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max(1, parallel)) as ex:
            list(ex.map(one, reqs))
        return
    try:
        bid = prov.submit(reqs)
    except Exception as e:  # out of credit, quota, bad request: stop loudly so a driver script stops too
        print(f"SUBMIT FAILED for {len(reqs)} {model_name} requests: {e!r}"[:600])
        sys.exit(4)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    new = [{"batch": bid, "model": model_name, "ids": [r["id"] for r in reqs], "submitted": now}]
    if WATCH.get("canary", True):
        cid = prov.submit([{"id": f"canary|{bid}", "max_tokens": 1024, "parts": [{"text": "Reply with the word OK."}]}])
        new.append({"batch": cid, "model": model_name, "ids": [f"canary|{bid}"], "submitted": now, "canary_for": bid})
    update_batches(lambda b: b + new)
    print(f"submitted {bid}: {len(reqs)} requests (plus a canary); run `status` or `collect` later")


def _age_min(iso, now):
    return (now - datetime.datetime.fromisoformat(iso)).total_seconds() / 60


def watch(records, quiet=False):
    """Poll each pending batch, log it to batch_log.csv, print and return the stalled batch ids."""
    now = datetime.datetime.now(datetime.timezone.utc)
    canary = {r["canary_for"]: r for r in records if r.get("canary_for")}
    new = not BATCH_LOG.exists()
    stalled = []
    with BATCH_LOG.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["time", "batch", "model", "kind", "state", "done", "total", "age_min"])
        for r in records:
            try:
                p = providers.make(model_cfg(r["model"])).progress(r["batch"])
            except Exception as e:
                p = {"state": f"error: {e!r}"[:120], "done": None, "total": None}
            age = _age_min(r["submitted"], now)
            kind = "canary" if r.get("canary_for") else r["ids"][0].split("|")[0]
            w.writerow([now.isoformat(timespec="seconds"), r["batch"], r["model"], kind, p["state"],
                        p["done"], p["total"], f"{age:.1f}"])
            seen = r.setdefault("seen", {"t": r["submitted"], "done": 0})
            if p["done"] is not None and p["done"] != seen["done"]:
                r["seen"] = {"t": now.isoformat(timespec="seconds"), "done": p["done"]}
            if quiet or r.get("canary_for"):
                continue
            # Gemini reports a state but no per-request counts: there, idle is the batch's age.
            idle = _age_min(r["seen"]["t"], now) if p["done"] is not None else age
            finished = any(x in str(p["state"]).upper() for x in ("ENDED", "SUCCEEDED", "FAILED", "CANCEL", "EXPIRED", "COMPLETED"))
            flag = ""
            if not finished and age > WATCH.get("stall_minutes", 30) and idle > WATCH.get("no_progress_minutes", 15):
                c = canary.get(r["batch"])
                cs = f"canary still pending ({_age_min(c['submitted'], now):.0f} min): queue side" if c \
                    else "canary finished: look at this batch's requests (size, output length)"
                stalled.append(r["batch"])
                flag = f"  STALLED: nothing new for {idle:.0f} min; {cs}; `rescue --batch {r['batch']}` to cancel"
            print(f"{r['batch']} [{kind}, {r['model']}] {p['state']}: {p['done']} of {p['total']} done, "
                  f"{age:.0f} min old{flag}")
    return stalled


def status():
    if not BATCHES.exists() or not json.loads(BATCHES.read_text()):
        print("no pending batches")
        return
    records = json.loads(BATCHES.read_text())
    watch(records)
    update_batches(_merge_seen(records))


def rescue(batch_id):
    records = json.loads(BATCHES.read_text()) if BATCHES.exists() else []
    r = next((x for x in records if x["batch"] == batch_id), None)
    if not r:
        print(f"{batch_id} is not pending")
        return
    state = providers.make(model_cfg(r["model"])).cancel(batch_id)
    t = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    update_batches(lambda recs: [dict(x, cancel_requested=t) if x["batch"] == batch_id else x for x in recs])
    print(f"{batch_id}: cancel requested ({state}). `collect` saves what finished; then rerun the step with --sync")


def wait():
    """collect every minute until nothing is pending; exit 3 at the first stall, for a background runner."""
    while True:
        collect(poll=False)
        records = json.loads(BATCHES.read_text()) if BATCHES.exists() else []
        if not records:
            print("all batches collected")
            return
        stalled = watch(records)
        update_batches(_merge_seen(records))
        if stalled:
            print("stopping: stalled batch; see batch_log.csv")
            sys.exit(3)
        time.sleep(60)


def collect(poll=True):
    if not BATCHES.exists():
        print("no batches")
        return
    records = json.loads(BATCHES.read_text())
    if poll:
        watch(records, quiet=True)
    now = datetime.datetime.now(datetime.timezone.utc)
    pending = []
    for b in records:
        prov = providers.make(model_cfg(b["model"]))
        if not prov.done(b["batch"]):
            print(f"{b['batch']}: still running" + (" (canary)" if b.get("canary_for") else ""))
            pending.append(b)
            continue
        res = prov.results(b["batch"], b["ids"])
        if b.get("canary_for"):
            for rid, x in res.items():
                log_cost(rid, x, b["model"], b["batch"], False)
            print(f"{b['batch']}: canary for {b['canary_for']} done within {_age_min(b['submitted'], now):.0f} min")
            continue
        for rid in b["ids"]:
            save(rid, res.get(rid, {"text": "", "usage": None, "error": "missing from results"}), b["model"], b["batch"], False)
        print(f"{b['batch']}: collected {len(res)} of {len(b['ids'])} after {_age_min(b['submitted'], now):.0f} min")
    done = {b["batch"] for b in records} - {b["batch"] for b in pending}
    update_batches(lambda recs: [r for r in _merge_seen(records)(recs) if r["batch"] not in done])


def cost():
    if not COSTS.exists():
        print("no costs yet")
        return
    rows = list(csv.DictReader(COSTS.open()))
    by = {}
    for r in rows:
        k = (r["request"].split("|")[0], r["model"])
        n, c = by.get(k, (0, 0.0))
        by[k] = (n + 1, c + float(r["cost_usd"] or 0))
    for (kind, m), (n, c) in sorted(by.items()):
        print(f"{kind:10} {m:24} {n:5} calls  ${c:8.2f}  (${c / n:.3f} per call)")
    print(f"total ${sum(c for _, c in by.values()):.2f}")
    # Per paper-run: a review call plus the rank and judge calls on that review.
    per = {}
    for r in rows:
        f = r["request"].split("|")
        if f[0] == "review":
            key = (f[1], f"{f[2]}.{f[3]}", f[4])
        elif f[0] in ("rank", "judge"):
            key = (f[1], f[2], f[3])
        else:
            continue
        per.setdefault(key, {}).setdefault(f[0], 0.0)
        per[key][f[0]] += float(r["cost_usd"] or 0)
    full = [v for v in per.values() if {"review", "rank", "judge"} <= set(v)]
    if full:
        avg = {k: sum(v[k] for v in full) / len(full) for k in ("review", "rank", "judge")}
        print(f"per paper-run ({len(full)} with review, rank and judge): review ${avg['review']:.3f}, "
              f"rank ${avg['rank']:.3f}, judge ${avg['judge']:.3f}, total ${sum(avg.values()):.3f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["inputs", "review", "rank", "judge", "overlap", "extract", "recommend",
                                    "apply-recommend", "apply-extract", "recognize", "collect", "cost", "status", "rescue", "merge"])
    ap.add_argument("--set")
    ap.add_argument("--arm", default="plain", help="review: the prompt in arms/; other steps: the folder, e.g. plain.opus")
    ap.add_argument("--model", default="opus", help="review, extract, recommend, recognize: the model; rank: the ranker")
    ap.add_argument("--judge")
    ap.add_argument("--base", default="plain.opus")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--sync", action="store_true")
    ap.add_argument("--parallel", type=int, default=1, help="with --sync: calls at once")
    ap.add_argument("--batch", help="rescue: the batch id")
    ap.add_argument("--wait", action="store_true", help="collect: poll until done, stop at a stall")
    ap.add_argument("--out", help="merge: the new arm's variant name")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    a.judge = a.judge or CFG.get("main_judge")
    if a.cmd == "collect":
        return wait() if a.wait else collect()
    if a.cmd == "cost":
        return cost()
    if a.cmd == "status":
        return status()
    if a.cmd == "rescue":
        return rescue(a.batch)
    pids = paper_set(a.set)
    if a.cmd == "inputs":
        for pid in pids:
            print(pid, v1_pdf(pid).stat().st_size // 1024, "KB", len(v1_text(pid).split()), "words")
        return
    if a.cmd == "review":
        reqs, m = review_requests(pids, a.arm, a.model, a.runs), a.model
    elif a.cmd == "rank":
        m = a.model if "--model" in sys.argv else default_ranker(a.arm)
        reqs = rank_requests(pids, a.arm, m)
    elif a.cmd == "judge":
        reqs, m = judge_requests(pids, a.arm, a.judge, default_ranker(a.arm)), a.judge
    elif a.cmd == "overlap":
        reqs, m = overlap_requests(pids, a.arm, a.base, a.judge, default_ranker(a.base)), a.judge
    elif a.cmd == "merge":
        reqs, m = merge_requests(pids, a.arm, a.model, a.out), a.model
    elif a.cmd == "recommend":
        reqs, m = recommend_requests(pids, a.model), a.model
    elif a.cmd == "apply-recommend":
        return apply_recommend(pids, a.model)
    elif a.cmd == "apply-extract":
        return apply_extract(pids, a.model)
    elif a.cmd == "extract":
        reqs, m = extract_requests(pids, a.model), a.model
    else:
        reqs, m = recognize_requests(pids, a.model), a.model
    send(reqs, m, a.sync, a.dry_run, a.parallel)


if __name__ == "__main__":
    main()
