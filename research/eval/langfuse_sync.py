#!/usr/bin/env python3
"""Mirror the evaluation into Langfuse: the paper sets as datasets, and runs with their scores.

    pip install -r research/corpus/requirements.txt
    python3 research/eval/langfuse_sync.py datasets          # create or update the datasets
    python3 research/eval/langfuse_sync.py baselines         # recall of the API-run arms on dev30
    python3 research/eval/langfuse_sync.py reviews DIR NAME  # a folder of review folders as one run
    python3 research/eval/langfuse_sync.py stage1            # stage 1 datasets, runs and inference test

Keys come from the environment (LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_BASE_URL),
or from `.env` in this checkout or the main checkout (gitignored; names in `.env.example`).

Needs the Langfuse Python SDK v5 (Python 3.10+): Langfuse Cloud removed its v3 API on
2026-11-19. Langfuse is a mirror for browsing, comparing runs and collecting labels; the files in
research/ and the corpus (research/corpus/) stay the source of truth. Dataset items have fixed ids, so
`datasets` is idempotent; each `reviews` or `baselines` call logs a new experiment run.

`reviews DIR NAME` reads every folder under DIR that has a `science.json` (and optionally
`novelty.json`) and logs one experiment item per folder, with scores: must_address,
should_address, minor, items, strengths and, when present, novelty_must / novelty_should /
novelty_minor. A folder is matched to a dataset item by its arXiv id, and by version when the
folder is named `v1` or `accepted` (research/eval/stage1/runs/<engine>/<id>/<version>/).
"""
import argparse
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REF = HERE / "referee"
ROOT = HERE.parent.parent


def load_env():
    if os.environ.get("LANGFUSE_PUBLIC_KEY"):
        return
    places = [ROOT / ".env"]
    try:
        common = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--git-common-dir"],
                                capture_output=True, text=True).stdout.strip()
        if common:
            places.append((ROOT / common).resolve().parent / ".env")
    except OSError:
        pass
    for p in places:
        if p.exists():
            for line in p.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
            return
    sys.exit("No Langfuse keys: set LANGFUSE_* or put them in .env (see .env.example)")


def retry(fn, *args, **kw):
    """Call the Langfuse API, waiting out its rate limit (Hobby: 100 dataset calls a minute)."""
    import time
    from langfuse.api.core.api_error import ApiError
    for attempt in range(8):
        try:
            return fn(*args, **kw)
        except ApiError as e:
            if e.status_code != 429 or attempt == 7:
                raise
            wait = ((e.body or {}).get("details") or {}).get("retryAfterSeconds", 30) if isinstance(e.body, dict) else 30
            print(f"  rate limited; waiting {wait} s", flush=True)
            time.sleep(wait + 1)


def tiers_from_review(md):
    """Tier counts from a merged science review, for folders not yet structured into science.json:
    concerns are numbered across the headings A. Must address, B. Should address, C. Minor."""
    import re
    heads = [(m.start(), m.group(1)) for m in re.finditer(r"(?m)^[#*\s]*([ABC])\.\s+(?:Must|Should|Minor)", md)]
    out = Counter()
    for k, (start, tier) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(md)
        out[tier] = len(re.findall(r"(?m)^[#*\s]*\d+\.\s", md[start:end]))
    return out


def client():
    load_env()
    os.environ.setdefault("LANGFUSE_HOST", os.environ.get("LANGFUSE_BASE_URL", ""))
    from langfuse import Langfuse
    lf = Langfuse()
    if not lf.auth_check():
        sys.exit("Langfuse refused the keys")
    return lf


def paper_meta():
    pool = json.loads((REF / "pool.json").read_text())
    meta = {}
    for k in ("papers", "borderline", "pending"):
        for r in pool[k]:
            meta.setdefault(r["arxiv_id"], r)
    return meta


def referee_summary(aid):
    f = REF / aid / "referee.json"
    if not f.exists():
        return None
    r = json.loads(f.read_text())
    recs = [x.get("recommendation") for x in (r.get("recommendations") or {}).get("first_round", [])]
    first = r.get("concerns") or []
    return {"referees": r.get("referees"), "first_round_concerns": len(first),
            "major": sum(c.get("severity") == "major" for c in first), "recommendations": recs}


def datasets(lf):
    split = json.loads((REF / "split.json").read_text())
    meta = paper_meta()
    sets = {
        "referee-dev30": ("Development set: tune prompts here.", split["dev"]),
        "referee-test22": ("Held out: run once per reviewer change, never tune.", split["test"]),
        "referee-dev2": ("Develop the new metrics (data-plan.md, stage 1).", split.get("dev2", [])),
        "referee-test2": ("Held out for the new metrics.", split.get("test2", [])),
    }
    jc = json.loads((HERE / "jclub" / "selections.json").read_text())
    sets["jclub"] = ("Papers the Journal Club for Condensed Matter Physics recommended (in scope).",
                     [a for a, m in jc["papers"].items() if m.get("in_scope")])
    for name, (desc, ids) in sets.items():
        retry(lf.create_dataset, name=name, description=desc + " Mirrored from research/; AI-generated evaluation.")
        for aid in ids:
            m = meta.get(aid) or jc["papers"].get(aid) or {}
            retry(lf.create_dataset_item,
                dataset_name=name, id=f"{name}--{aid}",
                input={"arxiv_id": aid, "title": m.get("title"), "journal": m.get("journal")},
                expected_output=referee_summary(aid),
                metadata={k: m.get(k) for k in ("subfield", "pub_date", "accepted", "primary_category") if m.get(k)})
        print(f"{name}: {len(ids)} items")
    pilot = HERE / "stage1" / "pilot"
    if pilot.exists():
        name = "stage1-pilot"
        retry(lf.create_dataset, name=name, description="Stage 1 pilot: each paper's arXiv v1 and the version posted "
                          "after acceptance, to measure must-address items on accepted papers.")
        n = 0
        for d in sorted(p for p in pilot.iterdir() if p.is_dir()):
            for ver in ("v1", "accepted"):
                if (d / ver).exists():
                    m = meta.get(d.name, {})
                    retry(lf.create_dataset_item,
                        dataset_name=name, id=f"{name}--{d.name}--{ver}",
                        input={"arxiv_id": d.name, "version": ver, "title": m.get("title"), "journal": m.get("journal")},
                        expected_output=referee_summary(d.name), metadata={"accepted": m.get("accepted")})
                    n += 1
        print(f"{name}: {n} items")
    lf.flush()


def items_of(lf, dataset_name):
    return {it.id: it for it in retry(lf.get_dataset, dataset_name).items}


def log_experiment(lf, dataset_name, run_name, description, results):
    """Log precomputed results as one Langfuse experiment (SDK v5).

    results: {dataset item id: {"output": ..., "scores": {name: number}}}. The task returns the
    stored output and the evaluator turns its scores into Langfuse scores; nothing is recomputed.
    Run-level means are added for every score."""
    from langfuse import Evaluation
    items = items_of(lf, dataset_name)
    data = [items[i] for i in results if i in items]
    missing = [i for i in results if i not in items]
    if missing:
        print(f"  no dataset item for {len(missing)}: {missing[:3]}")

    def task(*, item, **kwargs):
        return results[item.id]

    def scores(*, input, output, expected_output, metadata, **kwargs):
        return [Evaluation(name=k, value=v, data_type="CATEGORICAL" if isinstance(v, str) else None)
                for k, v in output["scores"].items()]

    def means(*, item_results, **kwargs):
        names = sorted({k for r in results.values() for k in r["scores"]})
        out = []
        for n in names:
            vals = [r["scores"][n] for r in results.values() if isinstance(r["scores"].get(n), (int, float))]
            if not vals:
                continue
            out.append(Evaluation(name=f"mean_{n}", value=sum(vals) / len(vals)))
        return out

    lf.run_experiment(name=run_name, run_name=run_name, description=description, data=data, task=task,
                      evaluators=[scores], run_evaluators=[means], max_concurrency=2)
    lf.flush()
    print(f"{run_name}: {len(data)} items logged to {dataset_name}")


def reviews(lf, folder, run_name, dataset_name, description):
    folders = sorted({p.parent for p in Path(folder).rglob("science.json")} |
                     {p.parent for p in Path(folder).rglob("science-review.md")})
    results = {}
    for d in folders:
        ver = d.name if d.name in ("v1", "accepted") else None
        aid = d.parent.name if ver else d.name
        iid = f"{dataset_name}--{aid}" + (f"--{ver}" if ver else "")
        sj = d / "science.json"
        if sj.exists():
            s = json.loads(sj.read_text())
            tiers = Counter(i.get("tier") for i in s.get("issues", []))
        else:
            s = {"issues": [], "strengths": []}
            tiers = tiers_from_review((d / "science-review.md").read_text())
        sc = {"must_address": tiers.get("A", 0), "should_address": tiers.get("B", 0), "minor": tiers.get("C", 0),
              "items": sum(tiers.values())}
        if s.get("strengths"):
            sc["strengths"] = len(s["strengths"])
        out = {"arxiv_id": aid, "version": ver, "tiers": dict(tiers),
               "must_address": [i.get("headline") or i.get("issue", "")[:140] for i in s.get("issues", []) if i.get("tier") == "A"],
               "source": str(d.resolve().relative_to(ROOT))}
        nf = d / "novelty.json"
        if nf.exists():
            nv = json.loads(nf.read_text())
            nt = Counter(i.get("tier") for i in nv.get("issues", []))
            sc.update({"novelty_must": nt.get("A", 0), "novelty_should": nt.get("B", 0), "novelty_minor": nt.get("C", 0)})
            out["novelty"] = (nv.get("overall") or {}).get("grade")
        results[iid] = {"output": out, "scores": sc}
    log_experiment(lf, dataset_name, run_name, description, results)


STAGE1_RUNS = [  # (set, arm folder, review file, run name, description)
    ("dev2", "v1.0", "science-review.md", "stage1-v1.0-exhaustive", "Reviewer v1.0, three runs merged."),
    ("dev2", "v1.0", "runs/r1.md", "stage1-v1.0-r1", "Reviewer v1.0, one run (the first exhaustive run)."),
    ("dev2", "v1.0", "runs/r2.md", "stage1-v1.0-r2", "Reviewer v1.0, a second single run: run-to-run noise."),
    ("dev2", "v1.1", "runs/r1.md", "stage1-v1.1", "Reviewer v1.1 (absolute tier A, verdict), one run."),
    ("dev2", "v1.1", "science-review.md", "stage1-v1.1-merged",
     "Reviewer v1.1, three runs merged with the v1.1 merge prompt (r2, r3 and the merge headless via claude -p)."),
    ("dev2", "v1.2", "science-review.md", "stage1-v1.2-retiered",
     "v1.0's three runs re-merged with engine-v1.2/merge.md: every concern kept, tiers against v1.1's absolute bar."),
    ("dev2", "v1.2p", "science-review.md", "stage1-v1.2p-retiered-paper",
     "As v1.2, with the merger allowed to read the paper for the last check of the A items."),
    ("test2", "t1.0", "runs/r1.md", "stage1-test2-v1.0", "Held out. Reviewer v1.0, one run."),
    ("test2", "t1.1", "runs/r1.md", "stage1-test2-v1.1", "Held out, run once after v1.1 was fixed. One run."),
]


def stage1(lf, only=None):
    """Stage 1 (research/eval/stage1/README.md): datasets stage1-dev2 and stage1-test2 with one item per
    paper and version (v1, accepted), every reviewer run as an experiment with tier counts, verdict,
    recall and tier A precision (Gemini judge), and the inference test as one experiment.
    Langfuse's run means average papers (and mix v1 with accepted items for the tier counts);
    the pooled figures in stage1/README.md come from stage1/score.py."""
    sys.path.insert(0, str(HERE / "stage1"))
    import score as s1
    split = json.loads((REF / "split.json").read_text())
    meta = paper_meta()
    manifest = json.loads((HERE / "stage1" / "manifest.json").read_text())
    runs = HERE / "stage1" / "runs"
    for st in ("dev2", "test2"):
        name = f"stage1-{st}"
        retry(lf.create_dataset, name=name, description=(
            f"Stage 1, {st}: each paper's arXiv v1 and, where available, the version the journal accepted. "
            "Mirrored from research/eval/stage1; AI-generated evaluation."))
        n = 0
        for aid in split[st]:
            m = meta.get(aid, {})
            for ver in ("v1", "accepted"):
                if not any((runs / arm / aid / ver).exists() for arm in ("v1.0", "v1.1", "t1.0", "t1.1")):
                    continue
                mf = manifest.get(aid) or {}
                src = mf.get("accepted_source") if ver == "accepted" else "arXiv v1"
                retry(lf.create_dataset_item, dataset_name=name, id=f"{name}--{aid}--{ver}",
                      input={"arxiv_id": aid, "version": ver, "title": m.get("title"), "journal": m.get("journal"),
                             "source": src, "doi": mf.get("doi")},
                      expected_output=referee_summary(aid) if ver == "v1" else {"accepted": True},
                      metadata={"accepted": m.get("accepted")})
                n += 1
        print(f"{name}: {n} items")
    lf.flush()

    for st, arm, review, run_name, desc in STAGE1_RUNS:
        if only and run_name not in only:
            continue
        results = {}
        for aid in split[st]:
            if not (runs / arm / aid).exists():
                continue
            r = s1.paper(arm, aid, review)
            for ver in ("v1", "accepted"):
                if ver not in r:
                    continue
                c = r[ver]
                sc = {"must_address": c["A"], "should_address": c["B"], "minor": c["C"],
                      "items": c["A"] + c["B"] + c["C"]}
                if c.get("verdict"):
                    sc["verdict"] = c["verdict"]
                if ver == "v1" and r["matches_v1"] == "yes" and r.get("eligible"):
                    sc["recall_strict"] = r["raised"] / r["eligible"]
                    sc["recall_lenient"] = r["raised_or_partly"] / r["eligible"]
                    if r.get("A_judged"):
                        sc["a_precision"] = r["A_matched"] / r["A_judged"]
                f = runs / arm / aid / ver / review
                results[f"stage1-{st}--{aid}--{ver}"] = {
                    "output": {"arxiv_id": aid, "version": ver, "tiers": {t: c[t] for t in "ABC"},
                               "verdict": c.get("verdict"), "matches_v1": r["matches_v1"],
                               "review": f.read_text()[:20000], "source": str(f.relative_to(ROOT))},
                    "scores": sc}
        log_experiment(lf, f"stage1-{st}", run_name, desc + " Claude Code subagents (Claude Opus 5.5); "
                       "Gemini judge. AI-generated.", results)

    if only and "stage1-inference" not in only:
        return
    import infer_judge as ij
    results = {}
    for d in sorted((HERE / "stage1" / "inference").glob("*/judge.gemini.json")):
        aid = d.parent.name
        ref, cs = ij.concerns(aid)
        if ref.get("reviewed_matches_v1") != "yes":
            continue
        j = json.loads(d.read_text())
        reqs = j.get("requests", [])
        hit = [q for q in reqs if q.get("matches") or q.get("partly")]
        cm = {c["id"]: c.get("matched") for c in j.get("concerns", [])}
        found = sum(cm.get(c["id"]) in ("yes", "partly") for c in cs)
        walk = {}
        wf = d.parent / "walkthrough.json"
        if wf.exists():
            walk = {c["id"]: c.get("verdict") for c in json.loads(wf.read_text()).get("concerns", [])}
        judged = [walk[q["id"]] for q in hit if walk.get(q["id"])]
        sc = {"inferred": len(reqs), "precision": len(hit) / len(reqs) if reqs else 0.0,
              "recall": found / len(cs) if cs else 0.0}
        if judged:
            sc["response_agreement"] = sum(v in ("addressed", "partly") for v in judged) / len(judged)
        results[f"stage1-dev2--{aid}--accepted"] = {
            "output": {"arxiv_id": aid, "inferred": json.loads((d.parent / "inferred.json").read_text()),
                       "source": str(d.parent.relative_to(ROOT))}, "scores": sc}
    log_experiment(lf, "stage1-dev2", "stage1-inference", "Referee requests inferred from v1 vs the accepted "
                   "version (engine/compare.md steps 1 and 3), reports hidden; Gemini matched them to the real "
                   "concerns. AI-generated.", results)


def baselines(lf):
    """Per-paper recall of the API-run arms on dev30, from the corpus (Gemini judge), one experiment per arm."""
    import duckdb
    db_path = ROOT / "research" / "corpus" / "corpus.duckdb"
    if not db_path.exists():
        sys.exit("Build the corpus first: python3 research/corpus/build.py")
    db = duckdb.connect(str(db_path), read_only=True)
    rows = db.execute("""
        WITH elig AS (SELECT arxiv_id, concern_id FROM concerns WHERE eligible),
        per_run AS (
          SELECT r.arxiv_id, r.arm, r.run, count(*) FILTER (WHERE m.verdict = 'raised') AS hit
          FROM reviews r JOIN elig e ON e.arxiv_id = r.arxiv_id
          LEFT JOIN matches m ON m.review_id = r.review_id AND m.judge = 'gemini' AND m.concern_id = e.concern_id
          WHERE r.review_id IN (SELECT review_id FROM matches WHERE judge = 'gemini')
          GROUP BY 1, 2, 3)
        SELECT p.arxiv_id, p.arm, avg(p.hit) AS hit, n.n
        FROM per_run p JOIN (SELECT arxiv_id, count(*) AS n FROM elig GROUP BY 1) n USING (arxiv_id)
        WHERE p.arxiv_id IN (SELECT arxiv_id FROM sets WHERE set_name = 'dev30')
        GROUP BY 1, 2, 4""").fetchall()
    by_arm = {}
    for aid, arm, hit, n in rows:
        by_arm.setdefault(arm, {})[f"referee-dev30--{aid}"] = {
            "output": {"arxiv_id": aid, "raised": hit, "eligible": n},
            "scores": {"recall": hit / n if n else 0.0, "concerns_raised": hit}}
    for arm, results in sorted(by_arm.items()):
        log_experiment(lf, "referee-dev30", f"api-{arm}",
                       "API harness run (eval.md), Gemini judge; mirrored from the corpus.", results)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["datasets", "baselines", "reviews", "stage1"])
    ap.add_argument("folder", nargs="?")
    ap.add_argument("run_name", nargs="?")
    ap.add_argument("--dataset")
    ap.add_argument("--description", default="")
    ap.add_argument("--only", nargs="*", help="stage1: log only these runs (names in STAGE1_RUNS, or stage1-inference)")
    a = ap.parse_args()
    lf = client()
    if a.command == "datasets":
        datasets(lf)
    elif a.command == "baselines":
        baselines(lf)
    elif a.command == "stage1":
        stage1(lf, a.only)
    else:
        if not (a.folder and a.run_name and a.dataset):
            sys.exit("reviews needs FOLDER RUN_NAME --dataset NAME")
        reviews(lf, a.folder, a.run_name, a.dataset, a.description)


if __name__ == "__main__":
    main()
