#!/usr/bin/env python3
"""Score API runs: judge agreement, the referee agreement ceiling, and arms against a baseline.

    python3 research/eval/api/score.py ceiling --set referee16
    python3 research/eval/api/score.py agree   --set referee16 --judges sonnet,opus
    python3 research/eval/api/score.py metrics --set referee16 --judge sonnet --base legacy.plain --arms legacy.assistant
    python3 research/eval/api/score.py labels  --set rec20

Every result is Claude-judged, provisional (U2 in ../../eval.md) until a non-Claude judge reruns it.

Definitions (U1 and U3 in ../../eval.md; the Notion plan's Step 4 for the false-alarm rate):
  eligible   first-round concerns outside presentation and novelty, minus those the experiment 11
             judge (judge.json) marked fixed in v1. The same list for every arm, so arms pair.
  recall     eligible concerns judged "raised", pooled over concerns: each paper contributes its
             mean over runs of concerns raised, divided by all eligible concerns in the set.
  top-k      matched-length recall: a concern counts if a review point ranked 1..k (the reviewer
             model's own ranking, rank step) matches it; k = median eligible concern count in the set.
  precision  of a review's points the judge rates substantive, the share matching at least one
             referee concern (full match); pooled the same way as recall.
  false alarms  major points rated substantive that match no referee concern, even partly: mean
             per clean paper (all referees accept or minor). For contested papers the same count
             is shown as unmatched major points per paper.
  unique     substantive points matching no referee concern that the base arm did not raise in
             any run (overlap step), mean over runs, summed over papers.
  severity   Spearman correlation over papers between the review's recommendation (stated, or
             assigned by the judge) and the mean of the referees' first-round recommendations,
             coded accept 1, minor 2, major 3, reject 4.
  intervals  95% bootstrap over papers, pooled statistic in every resample. Paired gains use the
             same resampled papers for both arms; p is a one-sided sign-flip test on per-paper
             differences in concerns raised.
  ceiling    for papers with two or more referees: for each ordered pair of referees, the share
             of one referee's eligible concerns the other also raised; mean over pairs.
"""
import argparse
import json
import random
import statistics
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REF = HERE.parent / "referee"
EXCLUDED = ("presentation or clarity", "novelty, significance or prior work")
LEGACY = {"legacy.assistant": "assistant-r1/report.md", "legacy.plain": "plain/review.txt"}
LEVELS = ["raised", "partly", "not raised"]
CODE = {"accept": 1, "minor revision": 2, "major revision": 3, "reject": 4}
BOOT = 2000


def paper_set(name):
    return json.loads((HERE / "sets.json").read_text())[name]


def load(p):
    return json.loads(p.read_text()) if p.exists() else None


def eligible(pid):
    ref = load(REF / pid / "referee.json")
    old = load(REF / pid / "judge.json")
    fixed = {m["concern"] for m in old["matches"] if m.get("fixed_in_v1")} if old else set()
    # Papers judged before 2026-10-28 use judge.json's fixed_in_v1; later papers drop concerns the
    # extractor marked as about material absent from v1 (in_v1 false).
    return [c for c in ref["concerns"] if c["category"] not in EXCLUDED and c["id"] not in fixed
            and (old or c.get("in_v1") is not False)]


def label(pid):
    rec = (load(REF / pid / "referee.json") or {}).get("recommendations")
    return rec["label"] if rec else "unlabeled"


def referee_code(pid):
    rec = (load(REF / pid / "referee.json") or {}).get("recommendations")
    codes = [CODE[r["recommendation"]] for r in (rec or {}).get("first_round", []) if r["recommendation"] in CODE]
    return sum(codes) / len(codes) if codes else None


def review_file(pid, arm, k):
    return REF / pid / LEGACY[arm] if arm in LEGACY else REF / pid / "api" / arm / f"r{k}.txt"


def kappa(pairs):
    n = len(pairs)
    po = sum(a == b for a, b in pairs) / n
    pa = {lv: sum(a == lv for a, _ in pairs) / n for lv in LEVELS}
    pb = {lv: sum(b == lv for _, b in pairs) / n for lv in LEVELS}
    pe = sum(pa[lv] * pb[lv] for lv in LEVELS)
    return po, (po - pe) / (1 - pe) if pe < 1 else 1.0


def spearman(x, y):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for t in range(i, j + 1):
                r[order[t]] = (i + j) / 2 + 1
            i = j + 1
        return r
    if len(x) < 3:
        return None
    rx, ry = ranks(x), ranks(y)
    mx, my = sum(rx) / len(rx), sum(ry) / len(ry)
    sxy = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    sxx, syy = sum((a - mx) ** 2 for a in rx), sum((b - my) ** 2 for b in ry)
    return sxy / (sxx * syy) ** 0.5 if sxx and syy else None


# ---------- ceiling and judge agreement ----------

def ceiling(pids):
    vals, papers = [], 0
    for pid in pids:
        cs = eligible(pid)
        refs = sorted({r for c in cs for r in c["referees"]})
        if len(refs) < 2:
            continue
        papers += 1
        for a in refs:
            for b in refs:
                if a != b:
                    mine = [c for c in cs if b in c["referees"]]
                    if mine:
                        vals.append(sum(a in c["referees"] for c in mine) / len(mine))
    m = sum(vals) / len(vals)
    print(f"Referee agreement ceiling: {100 * m:.0f}% ({papers} papers with 2+ referees, {len(vals)} referee pairs)")
    return m


def verdicts(pids, source):
    """{(pid, arm, concern): verdict} for the experiment 11 reviews; source 'old' is judge.json."""
    out = {}
    papers = {p["id"]: p for p in load(REF / "papers.json")["papers"]}
    for pid in pids:
        ids = {c["id"] for c in eligible(pid)}
        old = load(REF / pid / "judge.json")
        for arm, f in LEGACY.items():
            if source == "old":
                if not old:
                    continue
                side = "A" if papers[pid]["judge_A"] == f else "B"
                for m in old["matches"]:
                    if m["concern"] in ids:
                        out[(pid, arm, m["concern"])] = m[side]
            else:
                j = load(REF / pid / "api" / arm / f"r1.judge.{source}.json")
                if not j:
                    continue
                got = {m["concern"]: m["verdict"] for m in j["matches"]}
                for c in ids:
                    out[(pid, arm, c)] = got.get(c, "not raised")
    return out


def agree(pids, judges):
    sources = ["old"] + judges
    data = {s: verdicts(pids, s) for s in sources}
    print("Judge agreement on raised / partly / not raised, experiment 11 reviews (Claude-judged, provisional)\n")
    print("| Pair | Calls | Agreement | Cohen's kappa | Assistant kappa | Plain kappa |\n|---|---|---|---|---|---|")
    names = {"old": "judge.json"}
    for i, a in enumerate(sources):
        for b in sources[i + 1:]:
            keys = sorted(set(data[a]) & set(data[b]))
            if not keys:
                print(f"| {names.get(a, a)} vs {names.get(b, b)} | 0 | | | | |")
                continue
            po, k = kappa([(data[a][x], data[b][x]) for x in keys])
            by = []
            for arm in LEGACY:
                ps = [(data[a][x], data[b][x]) for x in keys if x[1] == arm]
                by.append(f"{kappa(ps)[1]:.2f}" if ps else "")
            print(f"| {names.get(a, a)} vs {names.get(b, b)} | {len(keys)} | {100 * po:.0f}% | {k:.2f} | {by[0]} | {by[1]} |")
    for j in judges:
        keys = sorted(set(data["old"]) & set(data[j]))
        if not keys:
            continue
        print(f"\nOld judge (rows) against {j} (columns):\n\n| Old \\ {j} | " + " | ".join(LEVELS) + " |\n|---|---|---|---|")
        for a in LEVELS:
            print(f"| {a} | " + " | ".join(str(sum(data['old'][x] == a and data[j][x] == b for x in keys))
                                         for b in LEVELS) + " |")
    print()
    for s in sources:
        for arm in LEGACY:
            v = [x for k_, x in data[s].items() if k_[1] == arm]
            if v:
                print(f"{names.get(s, s):10} {arm:17} recall {100 * sum(x == 'raised' for x in v) / len(v):.0f}% "
                      f"({len(v)} concerns)")


# ---------- metrics ----------

def load_arm(pids, arm, judge, base=None):
    """pid -> list of runs; each run a dict of per-review counts."""
    out = {}
    for pid in pids:
        ids = {c["id"] for c in eligible(pid)}
        d = REF / pid / "api" / arm
        runs = []
        for jf in sorted(d.glob(f"r*.judge.{judge}.json")) if d.exists() else []:
            k = jf.name.split(".")[0][1:]
            j = load(jf)
            v = {c: "not raised" for c in ids}
            v.update({m["concern"]: m["verdict"] for m in j["matches"] if m["concern"] in ids})
            pr = j.get("_points_rank", {})
            pts = [dict(p, rank=pr.get(p["id"], 999), matches=set(p.get("matches", [])) & ids,
                        partly=set(p.get("partly", [])) & ids) for p in j["points"]]
            subst = [p for p in pts if p.get("quality") == "substantive"]
            unmatched = [p for p in subst if not p["matches"] and not p["partly"]]
            uniq = None
            if base:
                ov = load(d / f"r{k}.overlap.{base}.{judge}.json")
                if ov:
                    uniq = sum(not a["in_b"] for a in ov["a"])
                elif not unmatched:
                    uniq = 0
            rec = (j.get("recommendation") or {}).get("value")
            rf = review_file(pid, arm, k)
            runs.append({"n": len(ids), "hit": sum(x == "raised" for x in v.values()),
                         "loose": sum(x in ("raised", "partly") for x in v.values()),
                         "points": pts, "subst": len(subst), "subst_matched": sum(bool(p["matches"]) for p in subst),
                         "fa": sum(p.get("severity") == "major" for p in unmatched), "unique": uniq,
                         "verdict": CODE.get(rec), "words": len(rf.read_text().split()) if rf.exists() else None})
        if runs:
            out[pid] = runs
    return out


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def topk_hits(run, k):
    return len(set().union(*([p["matches"] for p in run["points"] if p["rank"] <= k] or [set()])))


def paper_means(runs, k):
    return {"n": runs[0]["n"], "hit": mean([r["hit"] for r in runs]), "loose": mean([r["loose"] for r in runs]),
            "topk": mean([topk_hits(r, k) for r in runs]), "subst": mean([r["subst"] for r in runs]),
            "subst_matched": mean([r["subst_matched"] for r in runs]), "fa": mean([r["fa"] for r in runs]),
            "unique": mean([r["unique"] for r in runs]) if all(r["unique"] is not None for r in runs) else None,
            "verdict": mean([r["verdict"] for r in runs]), "words": mean([r["words"] for r in runs]),
            "concerns": mean([len(r["points"]) for r in runs]), "runs": len(runs)}


def ratio(pm, ps, num, den):
    d = sum(pm[p][den] for p in ps)
    return sum(pm[p][num] for p in ps) / d if d else None


def boot(ps, f, seed=7):
    rnd = random.Random(seed)
    vals = []
    for _ in range(BOOT):
        v = f([rnd.choice(ps) for _ in ps])
        if v is not None:
            vals.append(v)
    vals.sort()
    return (vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]) if vals else (None, None)


def signflip(diffs, seed=11, n=20000):
    obs = sum(diffs)
    rnd = random.Random(seed)
    ge = sum(sum(d if rnd.random() < 0.5 else -d for d in diffs) >= obs - 1e-12 for _ in range(n))
    return (ge + 1) / (n + 1)


def pct(x):
    return "" if x is None else f"{100 * x:.0f}%"


def ci(lo, hi):
    return "" if lo is None else f" ({100 * lo:.0f} to {100 * hi:.0f})"


def metrics(pids, judge, base, others):
    k = int(round(statistics.median([len(eligible(p)) for p in pids])))
    arms = [base] + others
    pm = {a: {p: paper_means(r, k) for p, r in load_arm(pids, a, judge, None if a == base else base).items()}
          for a in arms}
    labels = {p: label(p) for p in pids}
    print(f"Claude-judged, provisional. Judge {judge}; base {base}; k = {k} (median eligible concerns per paper); "
          f"labels: " + ", ".join(f"{v} {sum(x == v for x in labels.values())}" for v in sorted(set(labels.values()))))
    for split in ("all", "clean", "contested"):
        sel = [p for p in pids if split == "all" or labels[p] == split]
        if not sel:
            continue
        print(f"\n**{split.capitalize()} papers ({len(sel)})**\n")
        print("| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | "
              + ("False alarms per paper" if split == "clean" else "Unmatched major per paper")
              + " | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |")
        print("|" + "---|" * 14)
        for a in arms:
            ps = [p for p in sel if p in pm[a]]
            if not ps:
                print(f"| {a} | 0 |" + " |" * 12)
                continue
            m = pm[a]
            rec = ratio(m, ps, "hit", "n")
            lo, hi = boot(ps, lambda s: ratio(m, s, "hit", "n"))
            sev = [(referee_code(p), m[p]["verdict"]) for p in ps]
            sev = [(x, y) for x, y in sev if x is not None and y is not None]
            rho = spearman([x for x, _ in sev], [y for _, y in sev]) if sev else None
            uq = [m[p]["unique"] for p in ps]
            gains = ["", ""]
            if a != base:
                common = [p for p in ps if p in pm[base]]
                b = pm[base]
                for gi, key in enumerate(("hit", "topk")):
                    def g(s, key=key):
                        r1, r0 = ratio(m, s, key, "n"), ratio(b, s, key, "n")
                        return None if r1 is None or r0 is None else r1 - r0
                    if common and g(common) is not None:
                        glo, ghi = boot(common, g)
                        pv = signflip([m[p][key] - b[p][key] for p in common])
                        gains[gi] = f"{100 * g(common):+.0f} pts{ci(glo, ghi)}, p {pv:.3f}"
            print(f"| {a} | {len(ps)} | {sum(m[p]['runs'] for p in ps)} | {pct(rec)}{ci(lo, hi)} | "
                  f"{pct(ratio(m, ps, 'loose', 'n'))} | {pct(ratio(m, ps, 'topk', 'n'))} | "
                  f"{pct(ratio(m, ps, 'subst_matched', 'subst'))} | {mean([m[p]['fa'] for p in ps]):.1f} | "
                  f"{'' if a == base or None in uq else f'{sum(uq):.0f}'} | "
                  f"{sev_cell(rho, sev)} | {mean([m[p]['words'] for p in ps]):.0f} | "
                  f"{mean([m[p]['concerns'] for p in ps]):.1f} | {gains[0]} | {gains[1]} |")


def sev_cell(rho, sev):
    if rho is not None:
        return f"{rho:.2f} (n {len(sev)})"
    if len(sev) >= 3 and len({y for _, y in sev}) == 1:
        inv = {v: k for k, v in CODE.items()}
        return f"undefined: every review {inv.get(sev[0][1], sev[0][1])}"
    return ""


def labels_cmd(pids):
    print("| Paper | Label | First-round recommendations |\n|---|---|---|")
    for pid in pids:
        rec = (load(REF / pid / "referee.json") or {}).get("recommendations")
        rows = ", ".join(f"{r['referee']} {r['recommendation']}{'' if r.get('explicit') else ' (inferred)'}"
                         for r in rec["first_round"]) if rec else ""
        print(f"| {pid} | {label(pid)} | {rows} |")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["ceiling", "agree", "metrics", "labels"])
    ap.add_argument("--set", required=True)
    ap.add_argument("--judge")
    ap.add_argument("--judges", default="sonnet,opus")
    ap.add_argument("--base", default="plain.opus")
    ap.add_argument("--arms", default="")
    a = ap.parse_args()
    a.judge = a.judge or json.loads((HERE / "config.json").read_text()).get("main_judge")
    pids = paper_set(a.set)
    if a.cmd == "ceiling":
        ceiling(pids)
    elif a.cmd == "agree":
        agree(pids, [j for j in a.judges.split(",") if j])
    elif a.cmd == "labels":
        labels_cmd(pids)
    else:
        metrics(pids, a.judge, a.base, [x for x in a.arms.split(",") if x])


if __name__ == "__main__":
    main()
