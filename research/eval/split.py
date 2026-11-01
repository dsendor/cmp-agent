#!/usr/bin/env python3
"""Count the paper pool and draw the dev, test and reserve split (U3), seeded.

    python3 research/eval/split.py                     # counts and a proposed split, printed
    python3 research/eval/split.py --write             # also write referee/split.json
    python3 research/eval/split.py --borderline        # let borderline-scope papers into the draw
    python3 research/eval/split.py --keep --write      # keep dev and test, new papers to the reserve

Dev is the 16 judged papers plus about 14 post-cutoff papers drawn at random; test is about 50
post-cutoff papers drawn at random from the rest; every other post-cutoff paper is the reserve.
Post-cutoff means published (peer review file public) from 2026-07-01, after the June 2026
training cutoff of every Claude model in config.json. Early papers (published 2026-01-01 to
06-30) and tier C papers can top up dev only, and are reported apart. The draw shuffles the
sorted arXiv ids with a fixed seed, so it is reproducible. No concerns are extracted here.
"""
import argparse
import json
import random
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REF = HERE / "referee"
SEED = 20261028


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dev-extra", type=int, default=14)
    ap.add_argument("--test", type=int, default=50)
    ap.add_argument("--borderline", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--keep", action="store_true", help="keep the dev and test in split.json; add new post-cutoff papers to the reserve")
    a = ap.parse_args()
    pool = json.loads((REF / "pool.json").read_text())
    sets = json.loads((HERE / "api" / "sets.json").read_text())
    judged = sets["referee16"]
    rows = [dict(r, scope="core") for r in pool["papers"]]
    if a.borderline:
        rows += [dict(r, scope="borderline") for r in pool["borderline"] if r.get("peer_review_url")]
    post = sorted(r["arxiv_id"] for r in rows if r["window"] == "post" and r["arxiv_id"] not in judged)
    early = sorted(r["arxiv_id"] for r in rows if r["window"] == "early")
    flagged = {r["arxiv_id"]: r["flags"] for r in rows}

    print(f"Pool retrieved {pool['retrieved']}; draw from {'core and borderline' if a.borderline else 'core'} papers")
    print("\n| Window | Journal | Papers |\n|---|---|---|")
    for (w, j), n in sorted(Counter((r["window"], r["journal"]) for r in rows).items()):
        print(f"| {w} | {j} | {n} |")
    bl = Counter(r["window"] for r in pool["borderline"] if r.get("peer_review_url"))
    pend = Counter(r["window"] for r in pool["pending"])
    print(f"\nPost-cutoff available for the draw: {len(post)} (plus the 16 judged papers); early: {len(early)}; "
          f"tier C (dev only): {len(sets['tierC'])}")
    print(f"Borderline with a file: post {bl['post']}, early {bl['early']}; pending (no file yet): "
          f"post {pend['post']}, early {pend['early']}")

    order = post[:]
    random.Random(SEED).shuffle(order)
    need = a.dev_extra + a.test
    dev_extra = order[:a.dev_extra]
    test = order[a.dev_extra:need]
    reserve = order[need:]
    if a.keep:
        old = json.loads((REF / "split.json").read_text())
        dev_extra, test = old["dev_new"], old["test"]
        reserve = [p for p in order if p not in set(dev_extra) | set(test)]
        print(f"Kept dev and test from split.json; reserve {len(old['reserve'])} -> {len(reserve)}")
    short = max(0, need - len(post))
    print(f"\nProposed split (seed {SEED}): dev {len(judged)} + {len(dev_extra)} = {len(judged) + len(dev_extra)}, "
          f"test {len(test)}, reserve {len(reserve)}" + (f"; short by {short} post-cutoff papers" if short else ""))
    n_flag = sum(any("days after submission" in f or "transfer" in f for f in flagged[p]) for p in test)
    print(f"Test papers whose v1 may carry revisions or whose earlier rounds are missing: {n_flag} of {len(test)}")
    if a.write:
        out = {"seed": SEED, "pool_retrieved": pool["retrieved"], "borderline_included": a.borderline,
               "dev": judged + sorted(dev_extra), "dev_judged": judged, "dev_new": sorted(dev_extra),
               "dev_topup_candidates": {"early": early, "tierC": sets["tierC"]},
               "test": sorted(test), "reserve": sorted(reserve),
               "note": "Dev and test as approved by David (U5); papers found later go to the reserve."
               if a.keep else "Proposed; not final until David approves. No concerns extracted."}
        (REF / "split.json").write_text(json.dumps(out, indent=1))
        print("wrote referee/split.json")


if __name__ == "__main__":
    main()
