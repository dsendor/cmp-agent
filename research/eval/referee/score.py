#!/usr/bin/env python3
"""Score the referee-match test in eval/referee/.

    python3 research/eval/referee/score.py           # prints markdown tables
    python3 research/eval/referee/score.py --json    # also writes eval/referee/scores.json

Each paper folder holds:
  referee.json        first-round referee concerns, extracted from the journal's peer review file
  assistant-r1/       the lookalike assistant on arXiv v1 (flags.json, report.md, notes.md)
  plain/review.txt    a plain "Review this paper." prompt on the same v1
  judge.json          a blind judge's mapping of each eligible concern to Review A and Review B

papers.json says which of A and B is the assistant. The judge scores only concerns outside
the presentation and novelty categories. A concern counts as eligible when the judge did not
mark it fixed_in_v1 (some v1 texts already carry the revision). Recall is eligible concerns
raised over eligible concerns, pooled over papers, with "raised or partly" as a looser second
number. The interval is a bootstrap over papers (2000 draws, seed 7) of the pooled difference.
"""
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
METHODS = ["assistant", "plain"]


def load(p):
    return json.loads(p.read_text()) if p.exists() else None


def side(paper, method):
    """Which judge letter (A or B) holds this method's review."""
    want = "assistant-r1/report.md" if method == "assistant" else "plain/review.txt"
    return "A" if paper["judge_A"] == want else "B"


def rows():
    out = []
    for p in load(ROOT / "papers.json")["papers"]:
        j = load(ROOT / p["id"] / "judge.json")
        if not j:
            continue
        ref = load(ROOT / p["id"] / "referee.json") or {}
        for m in j["matches"]:
            if m.get("fixed_in_v1"):
                continue
            r = {"paper": p["id"], "tier": p["tier"], "scope": "in" if p["scope_rank"] <= 4 else "out",
                 "category": m["category"], "severity": m.get("severity", ""),
                 "matches_v1": ref.get("reviewed_matches_v1", "")}
            for meth in METHODS:
                r[meth] = m[side(p, meth)]
            out.append(r)
    return out


def extras():
    out = []
    for p in load(ROOT / "papers.json")["papers"]:
        j = load(ROOT / p["id"] / "judge.json")
        if not j:
            continue
        e = {"paper": p["id"]}
        for meth in METHODS:
            lst = j.get(side(p, meth) + "_extra") or []
            e[meth] = {k: sum(x.get("kind") == k for x in lst) for k in ("substantive", "generic")}
        out.append(e)
    return out


def recall(rs, meth, loose=False):
    ok = ("raised", "partly") if loose else ("raised",)
    return sum(r[meth] in ok for r in rs), len(rs)


def pct(a, n):
    return f"{a}/{n} ({100 * a / n:.0f}%)" if n else "0/0"


def boot(rs, loose=False, n=2000):
    by = defaultdict(list)
    for r in rs:
        by[r["paper"]].append(r)
    papers = list(by)
    rnd = random.Random(7)
    diffs = []
    for _ in range(n):
        s = [r for p in (rnd.choice(papers) for _ in papers) for r in by[p]]
        if s:
            a, k = recall(s, "assistant", loose)
            b, _ = recall(s, "plain", loose)
            diffs.append((a - b) / k)
    diffs.sort()
    return diffs[int(0.025 * len(diffs))], diffs[int(0.975 * len(diffs)) - 1]


def table(title, groups):
    print(f"\n## {title}\n")
    print("| Group | Papers | Concerns | Assistant raised | Plain raised | Assistant raised or partly | Plain raised or partly |")
    print("|---|---|---|---|---|---|---|")
    for name, rs in groups:
        if not rs:
            continue
        cells = [pct(*recall(rs, m)) for m in METHODS] + [pct(*recall(rs, m, True)) for m in METHODS]
        print(f"| {name} | {len({r['paper'] for r in rs})} | {len(rs)} | " + " | ".join(cells) + " |")


def main():
    rs = rows()
    if not rs:
        print("No judged papers yet.")
        return
    out = {"concerns": rs}
    table("Recall of eligible first-round referee concerns", [("all", rs)])
    table("By tier (A clean, B caveats, C reports public before the model's training cutoff)",
          [(t, [r for r in rs if r["tier"] == t]) for t in "ABC"])
    table("By library scope", [("in scope (rank 1 to 4)", [r for r in rs if r["scope"] == "in"]),
                               ("out of scope (rank 5 to 6)", [r for r in rs if r["scope"] == "out"])])
    table("By category", [(c, [r for r in rs if r["category"] == c]) for c in sorted({r["category"] for r in rs})])
    table("By severity", [(s, [r for r in rs if r["severity"] == s]) for s in ("major", "minor")])
    table("By whether the reviewed manuscript matches v1",
          [(v, [r for r in rs if r["matches_v1"] == v]) for v in sorted({r["matches_v1"] for r in rs})])

    lo, hi = boot(rs)
    lo2, hi2 = boot(rs, True)
    a, n = recall(rs, "assistant")
    b, _ = recall(rs, "plain")
    a2, _ = recall(rs, "assistant", True)
    b2, _ = recall(rs, "plain", True)
    print(f"\nAssistant minus plain, raised: {100 * (a - b) / n:+.0f} points (95% interval {100 * lo:+.0f} to {100 * hi:+.0f}). "
          f"Raised or partly: {100 * (a2 - b2) / n:+.0f} points ({100 * lo2:+.0f} to {100 * hi2:+.0f}).")
    both = sum(r["assistant"] == "raised" and r["plain"] == "raised" for r in rs)
    either = sum("raised" in (r["assistant"], r["plain"]) for r in rs)
    print(f"Raised by both: {both}. Raised by either: {pct(either, n)}.")

    print("\n## Per paper (raised / eligible)\n")
    print("| Paper | Tier | Scope | Eligible | Assistant | Plain |")
    print("|---|---|---|---|---|---|")
    wins = defaultdict(int)
    for pid in dict.fromkeys(r["paper"] for r in rs):
        prs = [r for r in rs if r["paper"] == pid]
        x, y = recall(prs, "assistant")[0], recall(prs, "plain")[0]
        wins["assistant" if x > y else "plain" if y > x else "tie"] += 1
        print(f"| {pid} | {prs[0]['tier']} | {prs[0]['scope']} | {len(prs)} | {x} | {y} |")
    print(f"\nPapers where the assistant raised more: {wins['assistant']}; plain more: {wins['plain']}; tie: {wins['tie']}.")

    ex = extras()
    print("\n## Issues no referee raised (judge's count)\n")
    print("| Method | Substantive | Generic |")
    print("|---|---|---|")
    for m in METHODS:
        print(f"| {m} | {sum(e[m]['substantive'] for e in ex)} | {sum(e[m]['generic'] for e in ex)} |")
    out["extras"] = ex
    out["totals"] = {"eligible": n, "assistant_raised": a, "plain_raised": b, "assistant_loose": a2,
                     "plain_loose": b2, "diff_ci": [lo, hi], "diff_ci_loose": [lo2, hi2]}

    if "--json" in sys.argv:
        (ROOT / "scores.json").write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
