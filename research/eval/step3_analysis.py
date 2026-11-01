#!/usr/bin/env python3
"""Step 3 follow-up analysis: where MARG's recall comes from, from the saved judge files only.

    python3 research/eval/step3_analysis.py > research/eval/api/results/2026-10-28-step3-analysis.md

No API calls. Papers: marg10 (the 10 dev papers MARG-S-NR ran on). Judge: gemini (Argon).
Recall here is the concern-level verdict "raised" over eligible concerns (score.py's definition);
recall at k uses the judge's point-level matches among the reviewer's top k ranked points.
Claude-judged, provisional (Gemini 4 Argon judge).
"""
import collections
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "api"))
import score  # noqa: E402

PIDS = score.paper_set("marg10")
ARMS = ["plain.opus", "liang.opus", "openaireview.opus", "margnr.opus"]
FOLLOW = ["liangplus.opus", "liangplus_cmp.opus", "plain70.opus"]
NAME = {"plain.opus": "Plain", "liang.opus": "Liang et al.", "openaireview.opus": "OpenAIReview",
        "margnr.opus": "MARG-S-NR"}
# Mean cost per review on these papers (review + rank + judge), from costs.csv.
COST = {}
SET_NAME = {"experiments_proofs": "experiments and claims", "novelty_impact": "novelty and impact",
            "clarity_reproducibility": "clarity and reproducibility"}


def costs():
    import csv
    tot = collections.defaultdict(float)
    n = collections.Counter()
    for r in csv.DictReader(open(HERE / "costs.csv")):
        f = r["request"].split("|")
        if len(f) < 3 or f[1] not in PIDS or not r["cost_usd"]:
            continue
        if f[0] == "review" and len(f) == 5:
            arm = f"{f[2]}.{f[3]}"
            tot[arm] += float(r["cost_usd"])
            n[arm] += 1
        elif f[0] in ("rank", "judge") and "cancelled-batch" not in r["request"] and r["stop"] != "max_tokens":
            tot[f[2]] += float(r["cost_usd"])
        elif f[0] == "marg" and "refine" not in r["request"] and "probe" not in r["request"]:
            tot["margnr.opus"] += float(r["cost_usd"])
    for arm in ARMS + FOLLOW:
        runs = n[arm] or (len(PIDS) if arm == "margnr.opus" else 1)
        COST[arm] = tot[arm] / runs


def runs_of(pid, arm):
    """Per run: {concern: verdict}, points with rank and matches."""
    ids = {c["id"] for c in score.eligible(pid)}
    out = []
    d = score.REF / pid / "api" / arm
    for jf in sorted(d.glob("r*.judge.gemini.json")):
        j = json.loads(jf.read_text())
        v = {c: "not raised" for c in ids}
        v.update({m["concern"]: m["verdict"] for m in j["matches"] if m["concern"] in ids})
        pr = j.get("_points_rank", {})
        pts = [dict(p, rank=pr.get(p["id"], 999), m=set(p.get("matches", [])) & ids) for p in j["points"]]
        out.append({"k": jf.name.split(".")[0], "v": v, "pts": sorted(pts, key=lambda p: p["rank"])})
    return ids, out


def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "n/a"


def main():
    costs()
    data = {pid: {arm: runs_of(pid, arm) for arm in ARMS} for pid in PIDS}
    elig = {pid: score.eligible(pid) for pid in PIDS}
    n_all = sum(len(e) for e in elig.values())
    sev = {(pid, c["id"]): c.get("severity") for pid in PIDS for c in elig[pid]}
    cat = {(pid, c["id"]): c["category"] for pid in PIDS for c in elig[pid]}
    text = {(pid, c["id"]): c["summary"] for pid in PIDS for c in elig[pid]}
    print("# Step 3 follow-up analysis (marg10)\n")
    print(f"Claude-judged, provisional (judge Gemini 4 Argon). {len(PIDS)} papers, {n_all} eligible referee "
          f"concerns ({sum(s == 'major' for s in sev.values())} major).\n")

    # 1. Recall at k
    ks = [5, 11, 20, 30, 43, 60, 999]
    print("## 1. Recall at k (point-level matches among the top k ranked points, mean over runs)\n")
    print("| Reviewer | Points per review | " + " | ".join("all" if k == 999 else f"k={k}" for k in ks) + " | Concern-level recall |")
    print("|---|---|" + "---|" * (len(ks) + 1))
    for arm in ARMS:
        row, npts = [], []
        for k in ks:
            hits = 0
            for pid in PIDS:
                _, rs = data[pid][arm]
                hits += sum(len(set().union(*([p["m"] for p in r["pts"] if p["rank"] <= k] or [set()]))) for r in rs) / len(rs)
            row.append(pct(hits, n_all))
        for pid in PIDS:
            _, rs = data[pid][arm]
            npts.append(sum(len(r["pts"]) for r in rs) / len(rs))
        cl = sum(sum(sum(x == "raised" for x in r["v"].values()) for r in data[pid][arm][1]) / len(data[pid][arm][1]) for pid in PIDS)
        print(f"| {NAME[arm]} | {sum(npts) / len(npts):.1f} | " + " | ".join(row) + f" | {pct(cl, n_all)} |")

    # 1b. Word-matched: MARG cut to the words of a Plain review
    print("\n**Word-matched.** Each MARG-S-NR review cut to its top k points, k chosen per paper so the points "
          "kept are about as long as that paper's mean Plain review (MARG points average more words):\n")
    hits, ksum = 0, 0
    for pid in PIDS:
        _, rs = data[pid]["margnr.opus"]
        mw = len((score.REF / pid / "api" / "margnr.opus" / "r1.txt").read_text().split())
        _, ps = data[pid]["plain.opus"]
        pw = sum(len((score.REF / pid / "api" / "plain.opus" / f"{r['k']}.txt").read_text().split()) for r in ps) / len(ps)
        k = round(len(rs[0]["pts"]) * pw / mw)
        ksum += k
        hits += len(set().union(*([p["m"] for p in rs[0]["pts"] if p["rank"] <= k] or [set()])))
    print(f"MARG-S-NR at Plain's length: {pct(hits, n_all)} (mean k {ksum / len(PIDS):.0f}); Plain: "
          f"{pct(sum(sum(sum(x == 'raised' for x in r['v'].values()) for r in data[pid]['plain.opus'][1]) / 3 for pid in PIDS), n_all)}.")

    # 2. Unions of runs and of reviewers
    print("\n## 2. Union of runs: what more draws of a cheap reviewer buy\n")
    print("A concern counts if any review in the combination raised it (concern-level verdict).\n")
    print("| Combination | Reviews | Recall | Major concerns | Cost (reviews, rank, judge) | Words to read |")
    print("|---|---|---|---|---|---|")
    words = {arm: sum(len((score.REF / pid / "api" / arm / f"{r['k']}.txt").read_text().split())
                      for pid in PIDS for r in data[pid][arm][1]) / sum(len(data[pid][arm][1]) for pid in PIDS)
             for arm in ARMS}
    combos = [("Plain, 1 run", [("plain.opus", [0])]), ("Plain, 2 runs", [("plain.opus", [0, 1])]),
              ("Plain, 3 runs", [("plain.opus", [0, 1, 2])]), ("Liang et al., 1 run", [("liang.opus", [0])]),
              ("Liang et al., 3 runs", [("liang.opus", [0, 1, 2])]),
              ("Plain 1 + Liang et al. 1", [("plain.opus", [0]), ("liang.opus", [0])]),
              ("Plain 3 + Liang et al. 3", [("plain.opus", [0, 1, 2]), ("liang.opus", [0, 1, 2])]),
              ("MARG-S-NR, 1 run", [("margnr.opus", [0])]),
              ("MARG-S-NR + Plain 1", [("margnr.opus", [0]), ("plain.opus", [0])]),
              ("Everything", [(a, [0, 1, 2]) for a in ARMS])]
    caught = {}
    for label, parts in combos:
        hit, maj, nrev, cost, w = 0, 0, 0, 0.0, 0.0
        for pid in PIDS:
            got = set()
            for arm, idx in parts:
                rs = data[pid][arm][1]
                for i in idx:
                    if i < len(rs):
                        got |= {c for c, x in rs[i]["v"].items() if x == "raised"}
            caught[(label, pid)] = got
            hit += len(got)
            maj += sum(sev[(pid, c)] == "major" for c in got)
        for arm, idx in parts:
            r = min(len(idx), 1 if arm == "margnr.opus" else 3)
            nrev += r
            cost += r * COST[arm]
            w += r * words[arm]
        n_maj = sum(s == "major" for s in sev.values())
        print(f"| {label} | {nrev} | {pct(hit, n_all)} | {pct(maj, n_maj)} | ${cost:.2f} | {w:,.0f} |")

    # 2b. Paper bootstrap for the key differences
    import random
    def diff(a, b, seed=7, n=10000):
        per = [(len(caught[(a, pid)]) - len(caught[(b, pid)]), len(elig[pid])) for pid in PIDS]
        point = sum(x for x, _ in per) / n_all
        rng = random.Random(seed)
        ds = []
        for _ in range(n):
            smp = [rng.choice(per) for _ in per]
            ds.append(sum(x for x, _ in smp) / sum(y for _, y in smp))
        ds.sort()
        return f"{100 * point:+.0f} pts (95% CI {100 * ds[int(.025 * n)]:+.0f} to {100 * ds[int(.975 * n)]:+.0f})"
    print("\nPaper-bootstrap differences in recall: "
          f"MARG-S-NR minus Plain 3 runs {diff('MARG-S-NR, 1 run', 'Plain, 3 runs')}; "
          f"MARG-S-NR minus Liang et al. 3 runs {diff('MARG-S-NR, 1 run', 'Liang et al., 3 runs')}; "
          f"Plain 3 + Liang et al. 3 minus MARG-S-NR {diff('Plain 3 + Liang et al. 3', 'MARG-S-NR, 1 run')}; "
          f"MARG-S-NR minus Plain 1 run {diff('MARG-S-NR, 1 run', 'Plain, 1 run')}.")

    # 3. Overlap: MARG against three plain runs
    print("\n## 3. Overlap: MARG-S-NR (1 run) against Plain (3 runs) and Liang et al. (3 runs)\n")
    m_only, p_only, both, neither = [], [], [], []
    for pid in PIDS:
        m = caught[("MARG-S-NR, 1 run", pid)]
        o = caught[("Plain 3 + Liang et al. 3", pid)]
        for c in elig[pid]:
            key = (pid, c["id"])
            (both if c["id"] in m and c["id"] in o else m_only if c["id"] in m else p_only if c["id"] in o else neither).append(key)
    print("| Raised by | Concerns | Major | Share of all eligible |")
    print("|---|---|---|---|")
    for lab, xs in [("Both", both), ("MARG-S-NR only", m_only), ("Plain or Liang et al. only (any of 6 reviews)", p_only),
                    ("Nobody", neither)]:
        print(f"| {lab} | {len(xs)} | {sum(sev[x] == 'major' for x in xs)} | {pct(len(xs), n_all)} |")
    print("\nBy referee category:\n")
    print("| Category | Eligible | MARG-S-NR (1) | Plain (3 runs) | Liang et al. (3 runs) | MARG-S-NR only |")
    print("|---|---|---|---|---|---|")
    for ct in sorted(set(cat.values())):
        keys = [k for k in cat if cat[k] == ct]
        f = lambda lab: sum(k[1] in caught[(lab, k[0])] for k in keys)
        print(f"| {ct} | {len(keys)} | {pct(f('MARG-S-NR, 1 run'), len(keys))} | {pct(f('Plain, 3 runs'), len(keys))} "
              f"| {pct(f('Liang et al., 3 runs'), len(keys))} | {sum(k in m_only for k in keys)} |")
    print("\nThe concerns only MARG-S-NR raised, against all six Plain and Liang et al. reviews:\n")
    for k in m_only:
        print(f"- {k[0]} {k[1]} ({sev[k]}, {cat[k]}): {text[k]}")

    # 4. Which MARG agent group produced the hits
    print("\n## 4. Which MARG-S-NR agent group raised each matched concern\n")
    per_set = collections.Counter()
    hits_set = collections.defaultdict(set)
    only_set = collections.Counter()
    pts_set = collections.Counter()
    unk = 0
    for pid in PIDS:
        d = score.REF / pid / "api" / "margnr.opus"
        mj = json.loads((d / "r1.marg.json").read_text())
        comments = [(s, c) for s, v in mj["by_set"].items() for c in v["final"]]
        for s, _ in comments:
            per_set[s] += 1
        rank = json.loads((d / "r1.rank.opus.json").read_text())["concerns"]
        norm = lambda t: re.sub(r"[^a-z0-9]+", " ", str(t).lower()).strip()
        def owner(rc):
            q = norm(rc.get("quote", ""))[:80]
            for s, c in comments:
                if q and q in norm(c):
                    return s
            words = set(norm(rc["concern"]).split())
            best = max(comments, key=lambda sc: len(words & set(norm(sc[1]).split())) / (len(words) or 1))
            return best[0]
        ownr = {rc["rank"]: owner(rc) for rc in rank}
        _, rs = data[pid]["margnr.opus"]
        for p in rs[0]["pts"]:
            s = ownr.get(p["rank"])
            if s is None:
                unk += 1
                continue
            pts_set[s] += 1
            for c in p["m"]:
                hits_set[s].add((pid, c))
    for s in hits_set:
        only_set[s] = len(hits_set[s] & set(m_only))
    print("| Agent group | Comments | Ranked points | Eligible concerns matched | of them MARG-only |")
    print("|---|---|---|---|---|")
    for s in ["experiments_proofs", "novelty_impact", "clarity_reproducibility"]:
        print(f"| {SET_NAME[s]} | {per_set[s]} | {pts_set[s]} | {len(hits_set[s])} | {only_set[s]} |")
    allh = set().union(*hits_set.values())
    print(f"\nMatched by one group only: " + ", ".join(
        f"{SET_NAME[s]} {len(hits_set[s] - set().union(*[hits_set[t] for t in hits_set if t != s]))}" for s in hits_set)
        + f"; by any group: {len(allh)}." + (f" {unk} ranked points could not be traced." if unk else ""))

    # 5. Per paper
    print("\n## 5. Per paper\n")
    print("| Paper | Eligible | Chunks | Plain (mean of 3) | Plain (3-run union) | Liang et al. (mean) | MARG-S-NR | MARG-S-NR only |")
    print("|---|---|---|---|---|---|---|---|")
    for pid in PIDS:
        n = len(elig[pid])
        mean_hit = lambda arm: sum(sum(x == "raised" for x in r["v"].values()) for r in data[pid][arm][1]) / len(data[pid][arm][1])
        ch = json.loads((score.REF / pid / "api" / "margnr.opus" / "r1.marg.json").read_text())["chunks"]
        print(f"| {pid} | {n} | {ch} | {pct(mean_hit('plain.opus'), n)} | {pct(len(caught[('Plain, 3 runs', pid)]), n)} "
              f"| {pct(mean_hit('liang.opus'), n)} | {pct(mean_hit('margnr.opus'), n)} | {sum(k[0] == pid for k in m_only)} |")

    # 6. Quality of the extra volume
    print("\n## 6. What the extra volume is made of (judge ratings of every ranked point)\n")
    print("| Reviewer | Points | Substantive | Generic | Incorrect | Substantive matching a referee | Major unmatched substantive per review |")
    print("|---|---|---|---|---|---|---|")
    for arm in ARMS:
        q = collections.Counter()
        sm, um, nr = 0, 0, 0
        for pid in PIDS:
            for r in data[pid][arm][1]:
                nr += 1
                for p in r["pts"]:
                    q[p.get("quality")] += 1
                    if p.get("quality") == "substantive":
                        sm += bool(p["m"])
                        um += (not p["m"] and not p.get("partly") and p.get("severity") == "major")
        tot = sum(q.values())
        print(f"| {NAME[arm]} | {tot / nr:.1f} | {pct(q['substantive'], tot)} | {pct(q['generic'], tot)} | "
              f"{pct(q['incorrect'], tot)} | {pct(sm, q['substantive'])} | {um / nr:.1f} |")
    print("\nCost per review on these papers (review, rank and judge): " +
          ", ".join(f"{NAME[a]} ${COST[a]:.2f}" for a in ARMS) + ".")


if __name__ == "__main__" and sys.argv[1:] != ["followup"]:
    main()


# ---------------------------------------------------------------------------------------------
# Follow-up tests A to D (step3-report.md, "Follow-up tests"):
#     python3 research/eval/step3_analysis.py followup > research/eval/api/results/2026-10-28-step3-followup.md

TIER = re.compile(r"(?im)^[#*\s]*([ABC])[.)]\s*(must|should|minor)")


def tiers_of(text):
    """[(position, tier)] for the tier headings in a review."""
    return [(m.start(), m.group(1).upper()) for m in TIER.finditer(text)]


def point_tier(pid, arm, k, rank_no, cache={}):
    """Tier (A, B, C) of a ranked point, found by locating its quote in the review text."""
    key = (pid, arm, k)
    if key not in cache:
        d = score.REF / pid / "api" / arm
        text = (d / f"{k}.txt").read_text()
        rk = json.loads((d / f"{k}.rank.opus.json").read_text())["concerns"]
        norm = lambda t: re.sub(r"\s+", " ", str(t)).strip().lower()
        nt = norm(text)
        # Headings found on the whitespace-normalized text, so positions match the quotes.
        heads = [(m.start(), m.group(1).upper()) for m in
                 re.finditer(r"\b([abc])[.)]\s*\**\s*(must address|should address|minor)", nt)]
        out = {}
        for rc in rk:
            q = norm(rc.get("quote", ""))[:60]
            pos = nt.find(q) if q else -1
            t = None
            if pos >= 0:
                before = [h for h in heads if h[0] <= pos]
                t = before[-1][1] if before else None
            out[rc["rank"]] = t
        cache[key] = out
    return cache[key].get(rank_no)


def followup():
    costs()
    for arm in ["liangplus.opus", "liangplus_cmp.opus", "plain70.opus", "liangx3.opus"]:
        NAME.setdefault(arm, arm)
    NAME.update({"liangplus.opus": "B: Liang et al. + MARG protocol", "liangplus_cmp.opus": "D: B + CMP checklist",
                 "plain70.opus": "C: Plain asked for 70", "liangx3.opus": "A: 3 Liang et al. runs merged"})
    print("# Step 3 follow-up tests A to D\n")
    print("Claude-judged, provisional (judge Gemini 4 Argon). Recall is the concern-level verdict \"raised\" "
          "over eligible concerns; top-11 uses point-level matches among the reviewer's top 11 ranked points.\n")

    def table(pids, arms, title):
        elig = {pid: score.eligible(pid) for pid in pids}
        n_all = sum(len(e) for e in elig.values())
        majors = {(pid, c["id"]) for pid in pids for c in elig[pid] if c.get("severity") == "major"}
        print(f"## {title}\n")
        print(f"{len(pids)} papers, {n_all} eligible concerns ({len(majors)} major).\n")
        print("| Reviewer | Reviews | Recall | Top-11 | Top-30 | Union of runs | Words | Points | Tier A points | Referee majors caught in tier A |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for arm in arms:
            hit = t11 = t30 = 0.0
            union = 0
            words = pts = ta = 0.0
            maj_a, maj_any = 0.0, 0.0
            nrev = 0
            for pid in pids:
                ids, rs = runs_of(pid, arm)
                if not rs:
                    continue
                nrev += len(rs)
                hit += sum(sum(x == "raised" for x in r["v"].values()) for r in rs) / len(rs)
                at = lambda r, k: len(set().union(*([p["m"] for p in r["pts"] if p["rank"] <= k] or [set()])))
                t11 += sum(at(r, 11) for r in rs) / len(rs)
                t30 += sum(at(r, 30) for r in rs) / len(rs)
                union += len(set().union(*[{c for c, x in r["v"].items() if x == "raised"} for r in rs]))
                for r in rs:
                    words += len((score.REF / pid / "api" / arm / f"{r['k']}.txt").read_text().split()) / len(rs)
                    pts += len(r["pts"]) / len(rs)
                    tiered = arm in ("liangplus.opus", "liangplus_cmp.opus", "liangx3.opus")
                    if tiered:
                        a_pts = [p for p in r["pts"] if point_tier(pid, arm, r["k"], p["rank"]) == "A"]
                        ta += len(a_pts) / len(rs)
                        got_a = set().union(*([p["m"] for p in a_pts] or [set()]))
                        maj_a += len({(pid, c) for c in got_a} & majors) / len(rs)
            np_ = len([p for p in pids if runs_of(p, arm)[1]])
            tiered = arm in ("liangplus.opus", "liangplus_cmp.opus", "liangx3.opus")
            print(f"| {NAME.get(arm, arm)} | {nrev} | {pct(hit, n_all)} | {pct(t11, n_all)} | {pct(t30, n_all)} | "
                  f"{pct(union, n_all)} | {words / np_:,.0f} | {pts / np_:.1f} | "
                  f"{(f'{ta / np_:.1f}' if tiered else '')} | {(pct(maj_a, len(majors)) if tiered else '')} |")
        print()

    table(PIDS, ["plain.opus", "liang.opus", "liangplus.opus", "liangplus_cmp.opus", "plain70.opus", "margnr.opus"],
          "Tests B, C, D on marg10 (the 10 MARG papers)")
    table(score.paper_set("dev30"), ["liang.opus", "liangx3.opus", "plain.opus"], "Test A on dev30 (30 dev papers)")
    print("Cost per review on marg10 (review, rank and judge): " + ", ".join(
        f"{NAME.get(a, a)} ${COST.get(a, 0):.2f}" for a in ["liangplus.opus", "liangplus_cmp.opus", "plain70.opus"]) + ".")


if __name__ == "__main__" and sys.argv[1:] == ["followup"]:
    followup()
