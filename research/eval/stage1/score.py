#!/usr/bin/env python3
"""Stage 1 metrics for one reviewer version on one set.

    python3 research/eval/stage1/score.py dev2 v1.0
    python3 research/eval/stage1/score.py dev2 v1.0 --json > out.json

Per paper, from runs/<arm>/<id>/{v1,accepted}/science-review.md and v1/judge.gemini.json:
- A, B, C counts on v1 and on the accepted version, and the verdict line if there is one;
- recall: eligible referee concerns (api/score.py's definition: first round, about content in
  v1, not presentation or novelty) judged "raised" (strict) or "raised"/"partly" (lenient);
- tier A precision: the share of tier A items the judge matched (fully or partly) to any
  first-round referee concern, presentation and novelty included.

Papers whose arXiv v1 is not the manuscript the referees first saw (reviewed_matches_v1 "no"
in referee.json) are listed but left out of recall and precision: their v1 may already contain
the fixes.
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVAL = HERE.parent
sys.path.insert(0, str(HERE))
from judge import items  # noqa: E402

EXCLUDED = ("presentation or clarity", "novelty, significance or prior work")
VERDICT = re.compile(r"(?i)\b(ready|minor revision|major revision)\b")


def counts(md):
    c = {"A": 0, "B": 0, "C": 0}
    for t, _, _ in items(md):
        c[t] += 1
    i = md.lower().rfind("verdict")
    v = VERDICT.search(md[i:i + 300]) if i >= 0 else None
    c["verdict"] = v.group(1).lower() if v else None
    return c


def paper(arm, pid, review="science-review.md"):
    d = HERE / "runs" / arm / pid
    ref = json.loads((EVAL / "referee" / pid / "referee.json").read_text())
    out = {"id": pid, "matches_v1": ref.get("reviewed_matches_v1")}
    for ver in ("v1", "accepted"):
        f = d / ver / review
        if f.exists():
            out[ver] = counts(f.read_text())
    j = d / "v1" / ("judge.gemini.json" if review == "science-review.md" else f"judge.{Path(review).stem}.gemini.json")
    if j.exists():
        jd = json.loads(j.read_text())
        elig = {c["id"] for c in ref["concerns"] if c["category"] not in EXCLUDED and c.get("in_v1") is not False}
        fixed = {m["concern"] for m in jd["matches"] if m.get("fixed_in_v1")}
        elig -= fixed
        verdict = {m["concern"]: m["verdict"] for m in jd["matches"]}
        out["eligible"] = len(elig)
        out["raised"] = sum(verdict.get(c) == "raised" for c in elig)
        out["raised_or_partly"] = sum(verdict.get(c) in ("raised", "partly") for c in elig)
        pts = {p["id"]: p for p in jd["points"]}
        a = [pid_ for pid_, key in jd["_points"].items() if key.startswith("A")]
        hit = [p for p in a if pts.get(p) and (pts[p].get("matches") or pts[p].get("partly"))]
        out["A_judged"] = len(a)
        out["A_matched"] = len(hit)
        out["A_full_match"] = sum(bool(pts.get(p, {}).get("matches")) for p in a)
        out["A_incorrect"] = sum(pts.get(p, {}).get("quality") == "incorrect" for p in a)
        allp = list(jd["_points"])
        out["items_judged"] = len(allp)
        out["items_matched"] = sum(bool(pts.get(p) and (pts[p].get("matches") or pts[p].get("partly"))) for p in allp)
        out["recommendation"] = (jd.get("recommendation") or {}).get("value")
    return out


def summarize(rows):
    ok = [r for r in rows if r["matches_v1"] == "yes" and "eligible" in r]
    s = {}
    if ok:
        el = sum(r["eligible"] for r in ok)
        s["papers_judged"] = len(ok)
        s["recall_strict"] = round(100 * sum(r["raised"] for r in ok) / el, 1)
        s["recall_lenient"] = round(100 * sum(r["raised_or_partly"] for r in ok) / el, 1)
        a = sum(r["A_judged"] for r in ok)
        s["A_precision"] = round(100 * sum(r["A_matched"] for r in ok) / a, 1) if a else None
        s["A_precision_full"] = round(100 * sum(r["A_full_match"] for r in ok) / a, 1) if a else None
        it = sum(r["items_judged"] for r in ok)
        s["all_items_precision"] = round(100 * sum(r["items_matched"] for r in ok) / it, 1) if it else None
    for ver in ("v1", "accepted"):
        rs = [r[ver] for r in rows if ver in r]
        if rs:
            s[f"{ver}_papers"] = len(rs)
            for t in "ABC":
                s[f"{ver}_{t}_mean"] = round(sum(r[t] for r in rs) / len(rs), 2)
            s[f"{ver}_zero_A"] = sum(r["A"] == 0 for r in rs)
            vs = [r["verdict"] for r in rs if r["verdict"]]
            if vs:
                s[f"{ver}_verdicts"] = {v: vs.count(v) for v in sorted(set(vs))}
    both = [r for r in rows if "v1" in r and "accepted" in r]
    if both:
        s["paired_papers"] = len(both)
        s["paired_A_v1"] = round(sum(r["v1"]["A"] for r in both) / len(both), 2)
        s["paired_A_accepted"] = round(sum(r["accepted"]["A"] for r in both) / len(both), 2)
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("set")
    ap.add_argument("arm")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--review", default="science-review.md", help="runs/r1.md scores standard mode (one run)")
    a = ap.parse_args()
    pids = json.loads((EVAL / "referee" / "split.json").read_text())[a.set]
    rows = [paper(a.arm, p, a.review) for p in pids if (HERE / "runs" / a.arm / p).exists()]
    s = summarize(rows)
    if a.json:
        print(json.dumps({"set": a.set, "arm": a.arm, "summary": s, "papers": rows}, indent=1))
        return
    print(f"{a.set} {a.arm}: {len(rows)} papers")
    for r in rows:
        v1, ac = r.get("v1", {}), r.get("accepted", {})
        rec = f"{r['raised']}/{r['eligible']}" if "eligible" in r else "-"
        pa = f"{r['A_matched']}/{r['A_judged']}" if "A_judged" in r else "-"
        print(f"  {r['id']} matches_v1={r['matches_v1']:<7} v1 A/B/C={v1.get('A','-')}/{v1.get('B','-')}/{v1.get('C','-')} "
              f"{v1.get('verdict') or ''}  acc A/B/C={ac.get('A','-')}/{ac.get('B','-')}/{ac.get('C','-')} {ac.get('verdict') or ''}"
              f"  recall {rec}  A matched {pa}")
    for k, v in s.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
