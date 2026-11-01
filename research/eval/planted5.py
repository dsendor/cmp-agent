#!/usr/bin/env python3
"""Score the larger planted test (library v0.5) in eval/planted5/.

    python3 research/eval/planted5.py           # prints markdown tables
    python3 research/eval/planted5.py --json    # also writes eval/planted5/scores.json

Each paper folder holds key.json (what was removed, from which run folder) and runs:
  orig-r1, orig-r2   the full text, run twice (the noise baseline)
  d<k>-r1            the text with deletion k removed: the passages where the paper tests
                     one library lookalike
  num-r1, num-plain  a planted numeric inconsistency, read by the assistant and by a plain
                     "Review this paper." prompt (scored by numeric.json, from the judge)

A deletion counts as detected at the status level when the target lookalike's status in
the cut run is lower than in both original runs, and at the test level when its test
score is lower than in both. Status rank: ruled out 3, tested in part 2, left open 1,
not tested 0, row absent -1. Test score: all 2, part 1, no 0, summed over the row's tests.
The same comparison between orig-r1 and orig-r2, over every library row, gives the rate
at which a row drops by chance.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "planted5"
RANK = {"ruled out for the claim": 3, "tested in part": 2, "left open by the authors": 1, "not tested": 0}
TEST = {"all": 2, "part": 1, "no": 0}
NOTICE = re.compile(r"(missing|absent|cut off|truncated|orphan|refers to .{0,40}not (?:in|shown)|"
                    r"no (?:such|corresponding) (?:passage|section|figure|text)|text (?:appears|seems) to be missing)", re.I)


def load(p):
    return json.loads(p.read_text()) if p.exists() else None


def row(run, lid):
    f = load(run / "flags.json")
    if not f:
        return None
    for r in f["lookalikes"]:
        if r["id"] == lid:
            return r
    return {}


def rank(r):
    if r is None:
        return None
    return RANK.get(r.get("status"), -1) if r else -1


def tscore(r):
    if r is None:
        return None
    return sum(TEST.get(t.get("shown"), 0) for t in (r.get("tests") or [])) if r else -1


def lib_rows(run):
    f = load(run / "flags.json")
    return {r["id"]: r for r in f["lookalikes"] if not r["id"].startswith("outside")} if f else {}


def main():
    out = {"deletions": [], "noise": {}}
    print("## Deletions: status and test score of the target lookalike\n")
    print("| Paper | Run | Target | Original runs (status, tests) | Cut run (status, tests) | Status dropped | Tests dropped | Notes a gap |")
    print("|---|---|---|---|---|---|---|---|")
    n = s_drop = t_drop = noticed = unmatched = 0
    noise_pairs = noise_s = noise_t = 0
    for kf in sorted(ROOT.glob("*/key.json")):
        key = load(kf)
        d = kf.parent
        o1, o2 = d / "orig-r1", d / "orig-r2"
        # noise: every library row present in both original runs
        r1, r2 = lib_rows(o1), lib_rows(o2)
        for lid in set(r1) & set(r2):
            noise_pairs += 1
            a, b = (rank(r1[lid]), rank(r2[lid])), (tscore(r1[lid]), tscore(r2[lid]))
            noise_s += a[0] != a[1]
            noise_t += b[0] != b[1]
        for run, v in sorted(key["variants"].items()):
            if not run.startswith("d") or not (d / run / "flags.json").exists():
                continue
            targets = v["info"]["lookalike"]
            targets = targets if isinstance(targets, list) else [targets]
            for t in targets:
                orig = [(rank(row(o, t)), tscore(row(o, t))) for o in (o1, o2) if (o / "flags.json").exists()]
                cut = (rank(row(d / run, t)), tscore(row(d / run, t)))
                sd = bool(orig) and all(cut[0] < o[0] for o in orig)
                td = bool(orig) and all(cut[1] < o[1] for o in orig)
                rep = (d / run / "report.md").read_text() if (d / run / "report.md").exists() else ""
                nt = bool(NOTICE.search(rep))
                if orig and all(o[0] == -1 for o in orig):
                    unmatched += 1
                n += 1
                s_drop += sd
                t_drop += td
                noticed += nt
                out["deletions"].append({"paper": key["id"], "run": run, "target": t, "orig": orig, "cut": cut,
                                         "status_dropped": sd, "tests_dropped": td, "notes_gap": nt})
                fmt = lambda x: f"{x[0]}, {x[1]}"
                print(f"| {key['id']} | {run} | {t} | {'; '.join(fmt(o) for o in orig)} | {fmt(cut)} | "
                      f"{'yes' if sd else 'no'} | {'yes' if td else 'no'} | {'yes' if nt else 'no'} |")
    print(f"\nDeletions scored: {n}. Status dropped: {s_drop}. Test score dropped: {t_drop}. "
          f"Report mentions missing text: {noticed}. Target row absent from both original runs "
          f"(the skill never matched it, so it cannot drop): {unmatched}.")
    if noise_pairs:
        print(f"\nNoise baseline (orig-r1 against orig-r2, {noise_pairs} library rows): status differs in "
              f"{noise_s} ({100 * noise_s / noise_pairs:.0f}%), test score differs in {noise_t} "
              f"({100 * noise_t / noise_pairs:.0f}%). A difference can go either way, so about half of these "
              f"are drops.")
    out["noise"] = {"pairs": noise_pairs, "status_differs": noise_s, "tests_differ": noise_t}
    out["totals"] = {"deletions": n, "target_unmatched": unmatched, "status_dropped": s_drop, "tests_dropped": t_drop, "notes_gap": noticed}

    judged = [r for g in "abc" for r in (load(ROOT / f"judge-{g}.json") or [])]
    if judged:
        kinds = ["noticed", "asked", "lowered", "no"]
        print("\n## Judge: did the cut run register the deletion?\n")
        print("noticed: says text seems missing, or asks for exactly what was cut. asked: asks a question "
              "the cut passage would have answered. lowered: marks drop, no request. no: nothing.\n")
        print("| Removed passage | Deletions | " + " | ".join(kinds) + " |")
        print("|---|---|" + "---|" * len(kinds))
        for kind in ["test", "mixed", "statement", "all"]:
            rows = [r for r in judged if kind == "all" or r["removed_kind"] == kind]
            print(f"| {kind} | {len(rows)} | " + " | ".join(str(sum(r['cut_flagged'] == k for r in rows)) for k in kinds) + " |")
        print(f"\nCopies of the cut evidence left elsewhere in the paper: {sum(bool(r['copies_left']) for r in judged)}. "
              f"Original runs relied on the cut passage: {sum(bool(r['orig_cited']) for r in judged)}. "
              f"Cut runs that suspected a test: {sum(bool(r['guessed_test']) for r in judged)}.")
        out["judge"] = judged

    num = load(ROOT / "numeric.json")
    if num:
        print("\n## Planted numeric errors\n")
        print("| Paper | Change | Assistant caught it | Plain prompt caught it |")
        print("|---|---|---|---|")
        for r in num:
            print(f"| {r['paper']} | {r['change']} | {r['assistant']} | {r['plain']} |")
        out["numeric"] = num

    if "--json" in sys.argv:
        (ROOT / "scores.json").write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
