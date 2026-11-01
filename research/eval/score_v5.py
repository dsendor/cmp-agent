#!/usr/bin/env python3
"""Score the runs made with the library v0.5 status scale (run folders v5-r<k>).

    python3 research/eval/score_v5.py           # prints markdown tables
    python3 research/eval/score_v5.py --json    # also writes eval/scores_v5.json

The v0.5 statuses are "ruled out for the claim", "tested in part", "left open by the
authors" and "not tested". A flag is any status except "ruled out for the claim". The
same tables for the v0.4 runs (skill-r<k>, statuses "ruled out", "partly addressed",
"not addressed") sit next to them for comparison. Outside rows get one label per paper,
as in score.py.
"""
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

from score import RUNS, EVAL, load, outside_canon, jaccard, recall_precision

V5 = ["ruled out for the claim", "tested in part", "left open by the authors", "not tested"]
V4 = ["ruled out", "partly addressed", "not addressed"]
CHECKS = ["done", "partly", "not done"]


def rows(run_dir):
    f = load(run_dir / "flags.json")
    return f["lookalikes"] if f else None


def checks(run_dir):
    f = load(run_dir / "flags.json")
    return [c["status"] for c in f["checks"]] if f else None


def flags(run_dir, ruled):
    rs = rows(run_dir)
    if rs is None:
        return None
    canon = outside_canon(run_dir.parent)
    out = set()
    for r in rs:
        if r["status"] == ruled:
            continue
        rid = r["id"]
        if rid.startswith("outside"):
            rid = canon.get(rid.split(":", 1)[-1].strip(), rid)
        out.add(rid)
    return out


def runs(d, prefix):
    return sorted(p for p in d.glob(f"{prefix}-r*") if (p / "flags.json").exists())


def group_counts(paper_ids, prefix, scale):
    c, n = Counter(), 0
    for pid in paper_ids:
        for r in runs(RUNS / pid, prefix):
            for row in rows(r):
                c[row["status"]] += 1
                n += 1
    return c, n


def pct(a, b):
    return f"{a} ({100 * a / b:.0f}%)" if b else "0"


def main():
    papers = yaml.safe_load((EVAL / "papers.yaml").read_text())
    new = papers["new"]
    careful = [p["id"] for p in new if p.get("careful")]
    other = [p["id"] for p in new if not p.get("careful")]
    out = {"groups": {}, "papers": {}, "known": {}}

    print("## Status of every lookalike row, careful papers against the others\n")
    print("Each cell counts rows over all runs of that scale. Careful papers: "
          + ", ".join(careful) + ". Others: " + ", ".join(other) + ".\n")
    print("| Scale | Group | Rows | " + " | ".join(V5) + " |")
    print("|---|---|---|" + "---|" * len(V5))
    for name, ids in (("careful", careful), ("other", other)):
        c, n = group_counts(ids, "v5", V5)
        out["groups"][f"v5 {name}"] = {"rows": n, **{s: c[s] for s in V5}}
        print(f"| v0.5 | {name} | {n} | " + " | ".join(pct(c[s], n) for s in V5) + " |")
    print("\n| Scale | Group | Rows | " + " | ".join(V4) + " |")
    print("|---|---|---|" + "---|" * len(V4))
    for name, ids in (("careful", careful), ("other", other)):
        c, n = group_counts(ids, "skill", V4)
        out["groups"][f"v4 {name}"] = {"rows": n, **{s: c[s] for s in V4}}
        print(f"| v0.4 | {name} | {n} | " + " | ".join(pct(c[s], n) for s in V4) + " |")

    print("\n## Per paper (v0.5 runs)\n")
    print("| Paper | Group | Runs | Rows per run | Ruled out for the claim | Not tested | Checks done | Flag Jaccard (v0.5) | Flag Jaccard (v0.4) |")
    print("|---|---|---|---|---|---|---|---|---|")
    for p in new:
        d = RUNS / p["id"]
        r5 = runs(d, "v5")
        if not r5:
            continue
        nrows = [len(rows(r)) for r in r5]
        ruled = [sum(1 for x in rows(r) if x["status"] == V5[0]) for r in r5]
        nott = [sum(1 for x in rows(r) if x["status"] == "not tested") for r in r5]
        cdone = [f"{checks(r).count('done')}/{len(checks(r))}" for r in r5]
        f5 = [flags(r, V5[0]) for r in r5]
        f4 = [flags(r, "ruled out") for r in runs(d, "skill")]
        j5 = [jaccard(a, b) for a, b in itertools.combinations(f5, 2)]
        j4 = [jaccard(a, b) for a, b in itertools.combinations(f4, 2)]
        j5s = f"{sum(j5) / len(j5):.2f}" if j5 else "n/a"
        j4s = f"{sum(j4) / len(j4):.2f}" if j4 else "n/a"
        grp = "careful" if p.get("careful") else "other"
        out["papers"][p["id"]] = {"group": grp, "rows": nrows, "ruled_out": ruled, "not_tested": nott,
                                  "checks_done": cdone, "jaccard_v5": j5s, "jaccard_v4": j4s}
        print(f"| {p['id']} | {grp} | {len(r5)} | {nrows} | {ruled} | {nott} | {', '.join(cdone)} | {j5s} | {j4s} |")

    print("\n## Tests shown, careful papers against the others (v0.5)\n")
    print("Every test of every lookalike row, marked all, part or no. Library rows only (outside rows set their own tests).\n")
    print("| Group | Tests | all | part | no |")
    print("|---|---|---|---|---|")
    for name, ids in (("careful", careful), ("other", other)):
        c = Counter(t["shown"] for pid in ids for r in runs(RUNS / pid, "v5") for x in rows(r)
                    if not x["id"].startswith("outside") for t in x.get("tests") or [])
        n = sum(c.values())
        out["groups"][f"v5 tests {name}"] = dict(c)
        print(f"| {name} | {n} | {pct(c['all'], n)} | {pct(c['part'], n)} | {pct(c['no'], n)} |")

    print("\n## Checks marked done, careful papers against the others\n")
    print("| Scale | Group | Checks | " + " | ".join(CHECKS) + " |")
    print("|---|---|---|" + "---|" * len(CHECKS))
    for prefix, label in (("v5", "v0.5"), ("skill", "v0.4")):
        for name, ids in (("careful", careful), ("other", other)):
            c = Counter(s for pid in ids for r in runs(RUNS / pid, prefix) for s in checks(r))
            n = sum(c.values())
            print(f"| {label} | {name} | {n} | " + " | ".join(pct(c[s], n) for s in CHECKS) + " |")

    print("\n## Known-outcome papers (v0.5): recall and precision against the answer key\n")
    print("A key explanation counts as found when the run gives it any status except ruled out for the claim.\n")
    print("| Paper | Recall | Precision (floor) | Statuses of the key explanations |")
    print("|---|---|---|---|")
    for p in papers["known"]:
        d = RUNS / p["id"] / "v5-r1"
        f = flags(d, V5[0])
        if f is None:
            print(f"| {p['id']} | not run | not run | |")
            continue
        r = recall_precision(f, p["key"])
        st = {x["id"]: x["status"] for x in rows(d)}
        keyst = "; ".join(f"{k['explanation']}: {st.get(k['explanation'], 'absent')}" for k in p["key"])
        out["known"][p["id"]] = r
        print(f"| {p['id']} | {r[0]} of {r[1]} | {r[2]} of {r[3]} | {keyst} |")

    if "--json" in sys.argv:
        (EVAL / "scores_v5.json").write_text(json.dumps(out, indent=2, default=list))


if __name__ == "__main__":
    main()
