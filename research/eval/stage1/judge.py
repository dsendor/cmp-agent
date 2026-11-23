#!/usr/bin/env python3
"""Judge stage 1 reviews against the referees' concerns, item by item, with tiers kept.

    python3 research/eval/stage1/judge.py dev2 v1.0      # every runs/<arm>/<id>/v1/science-review.md
    python3 research/eval/stage1/judge.py dev2 v1.0 --parallel 4

A merged review (science-review.md) lists numbered items under "A. Must address",
"B. Should address" and "C. Minor". Each item becomes a review point with its tier. The judge
is api/prompts/judge_v2.md (the one behind EVALUATION.md), with the Gemini model in
api/config.json, the review blinded and the points in a seeded random order. Unlike the API
harness there is no separate ranking step: the merged review's own items are the points, so
tier A precision can be read off directly.

The judge sees every first-round concern about content in v1, including presentation and
novelty ones (so a tier A item about novelty that a referee also raised counts as a match).
Recall is reported on the eligible concerns only (api/score.py's definition), so it compares
with EVALUATION.md.

Output: runs/<arm>/<id>/v1/judge.gemini.json (judge.r1.gemini.json for --review runs/r1.md).
"""
import argparse
import datetime
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVAL = HERE.parent
sys.path.insert(0, str(EVAL / "api"))
sys.path.insert(0, str(EVAL))
import providers  # noqa: E402
import run  # noqa: E402
from blind import blind, shuffled  # noqa: E402
from langfuse_sync import load_env  # noqa: E402

TIER = re.compile(r"(?m)^[#*\s]*([ABC])\.\s+(?:Must|Should|Minor)[^\n]*$")
ITEM = re.compile(r"(?m)^[#*\s]*(\d+)\.\s+")


def items(md):
    """[(tier, number, text)] from a merged review."""
    heads = list(TIER.finditer(md))
    out = []
    for i, h in enumerate(heads):
        sec = md[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(md)]
        its = list(ITEM.finditer(sec))
        for j, m in enumerate(its):
            body = sec[m.end(): its[j + 1].start() if j + 1 < len(its) else len(sec)]
            body = re.sub(r"(?m)^Raised by:.*$", "", body).strip()
            out.append((h.group(1), int(m.group(1)), body))
    return out


def concerns(pid):
    ref = json.loads((run.REF / pid / "referee.json").read_text())
    return [{k: c[k] for k in ("id", "category", "severity", "quote", "summary")}
            for c in ref["concerns"] if c.get("in_v1") is not False]


def request(pid, review_md):
    its = items(review_md)
    pts = shuffled([(f"{t}{n}", txt) for t, n, txt in its], f"{pid}|stage1")
    ids = {f"P{i}": key for i, (key, _) in enumerate(pts, 1)}
    prompt = (run.HERE / "prompts" / "judge_v2.md").read_text().strip()
    shared = (f"{prompt}\n\n# Paper text (arXiv v1)\n\n{run.v1_text(pid)}\n\n# Referee concerns\n\n"
              + json.dumps(shuffled(concerns(pid), pid), indent=1))
    points = [{"id": p, "point": dict(pts)[k]} for p, k in ids.items()]
    body = "# Review\n\n" + blind(review_md) + "\n\n# Review points\n\n" + json.dumps(points, indent=1)
    return {"id": f"judge|{pid}|stage1", "max_tokens": run.CFG["max_tokens"]["judge"],
            "parts": [{"text": shared, "cache": True}, {"text": body}]}, ids


def judge_one(prov, model_name, pid, folder, review="science-review.md"):
    out = folder / ("judge.gemini.json" if review == "science-review.md" else f"judge.{Path(review).stem}.gemini.json")
    if out.exists():
        return
    req, ids = request(pid, (folder / review).read_text())
    cap = run.CFG["models"][model_name].get("max_output")
    if cap:
        req["max_tokens"] = cap
    try:
        res = prov.sync(req)
    except Exception as e:  # noqa: BLE001
        res = {"text": "", "usage": None, "error": repr(e)[:300]}
    run.log_cost(req["id"], res, model_name, "", True)
    if res.get("error") or not res["text"]:
        print(f"  failed {pid}: {res.get('error') or 'empty'}", flush=True)
        return
    try:
        data = run.parse_json(res["text"])
    except ValueError:
        (folder / "judge.gemini.raw.txt").write_text(res["text"])
        print(f"  unparsed {pid}", flush=True)
        return
    data["_points"] = ids  # P id -> tier and item number, e.g. "A3"
    data["_meta"] = {"model": run.CFG["models"][model_name]["id"], "prompt": "judge_v2.md", "blinded": True,
                     "date": datetime.date.today().isoformat(), "stop": res.get("stop"), "usage": res["usage"]}
    out.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"  judged {pid}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("set")
    ap.add_argument("arm")
    ap.add_argument("--parallel", type=int, default=3)
    ap.add_argument("--review", default="science-review.md",
                    help="the review to judge, relative to the version folder; runs/r1.md is standard mode")
    a = ap.parse_args()
    load_env()
    model_name = run.CFG.get("main_judge", "gemini")
    prov = providers.make(run.model_cfg(model_name))
    pids = json.loads((EVAL / "referee" / "split.json").read_text())[a.set]
    jobs = [(pid, HERE / "runs" / a.arm / pid / "v1") for pid in pids]
    jobs = [(p, f) for p, f in jobs if (f / a.review).exists() and (run.REF / p / "referee.json").exists()]
    print(f"{len(jobs)} reviews to judge", flush=True)
    with ThreadPoolExecutor(a.parallel) as ex:
        list(ex.map(lambda j: judge_one(prov, model_name, *j, review=a.review), jobs))


if __name__ == "__main__":
    main()
