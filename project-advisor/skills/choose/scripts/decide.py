#!/usr/bin/env python3
"""Turn the researcher's own estimates into a decision summary. Standard library only.

  python3 decide.py <folder>/advisor.json      writes <folder>/decision.json, prints a summary

What it computes, all from the estimates in advisor.json (format: docs/advisor-format.md):

- The value of each idea, sampled over the researcher's ranges (triangular: low, best guess,
  high). value = p_success * impact + (1 - p_success) * fallback, on the researcher's 0 to 10
  scale. With "utility": "per_year" the value is divided by the years of effort.
- How often each idea comes out on top across those ranges.
- The Pareto front of likelihood of success against impact if it works (Alon 2009;
  Fischbach and Walsh 2024): ideas no other idea beats on both.
- Robustness: does the top pick survive moving any one estimate by 20% either way?
- The value of information: which single estimate, if the researcher knew it, would most
  often change the pick, and by how much on average (expected value of partial perfect
  information, computed by Monte Carlo). This is what the cheapest test should resolve.
- Red flags from the assumption tables: a high-risk assumption that reads out late, several
  high-risk assumptions in one idea, work past the time horizon, estimates the model made.

Nothing here is a judgment by the model. If the estimates are the researcher's, so are the
results; the output says which estimates were not.
"""
import json
import math
import random
import sys
from pathlib import Path

PARAMS = ("p_success", "impact", "fallback", "months")
LABEL = {"p_success": "odds of success", "impact": "impact if it works",
         "fallback": "value if it fails", "months": "months of work"}
N = 20000      # joint samples
K = 40         # values of the parameter being learned (EVPPI)
N_INNER = 2000  # samples of the other parameters for each of those values
SEED = 20261121


def tri_ppf(u, lo, mode, hi):
    """Inverse CDF of the triangular distribution."""
    if hi <= lo:
        return lo
    c = (mode - lo) / (hi - lo)
    if u < c:
        return lo + math.sqrt(u * (hi - lo) * (mode - lo))
    return hi - math.sqrt((1 - u) * (hi - lo) * (hi - mode))


def bounds(est, name, scale=1.0):
    e = est[name]
    lo, hi = float(e["low"]), float(e["high"])
    if lo > hi:
        lo, hi = hi, lo
    mode = float(e["best"]) if e.get("best") is not None else (lo + hi) / 2
    mode = min(max(mode, lo), hi)
    lo, mode, hi = lo * scale, mode * scale, hi * scale
    if name == "p_success":
        lo, mode, hi = (min(max(x, 0.0), 1.0) for x in (lo, mode, hi))
    if name == "months":
        lo, mode, hi = (max(x, 0.5) for x in (lo, mode, hi))
    return lo, mode, hi


def value(p, impact, fallback, months, per_year):
    v = p * impact + (1 - p) * fallback
    return v * 12.0 / months if per_year else v


class Idea:
    def __init__(self, raw, per_year, rng):
        self.raw, self.id, self.per_year = raw, raw["id"], per_year
        self.b = {k: bounds(raw["estimates"], k) for k in PARAMS}
        self.u = [[rng.random() for _ in PARAMS] for _ in range(N)]  # common random numbers

    def samples(self, b=None):
        b = b or self.b
        return [value(*(tri_ppf(u[j], *b[k]) for j, k in enumerate(PARAMS)), self.per_year)
                for u in self.u]

    def mean(self, b=None):
        s = self.samples(b)
        return sum(s) / len(s)

    def mid(self, k):
        return self.b[k][1]


def pareto(ideas):
    front = []
    for a in ideas:
        ax, ay = a.mid("p_success"), a.mid("impact")
        beaten = any((b.mid("p_success") >= ax and b.mid("impact") >= ay) and
                     (b.mid("p_success") > ax or b.mid("impact") > ay) for b in ideas if b is not a)
        if not beaten:
            front.append(a.id)
    return front


def flags(raw, horizon):
    out = []
    a = raw.get("assumptions") or []
    late = [x for x in a if x.get("risk", 0) >= 4 and x.get("readout_months", 0) > 18]
    for x in late:
        out.append({"kind": "late_high_risk", "text": "High-risk assumption reads out only after "
                    "%s months: %s" % (x["readout_months"], x["text"])})
    high = [x for x in a if x.get("risk", 0) >= 4]
    if len(high) > 2:
        out.append({"kind": "multiple_miracles",
                    "text": "%d assumptions rated risk 4 or 5: it needs several things to go right."
                    % len(high)})
    if a:
        worst = max(a, key=lambda x: (x.get("risk", 0), -x.get("readout_months", 0)))
        if worst.get("risk", 0) >= 4 and worst.get("readout_months", 99) <= 6:
            out.append({"kind": "early_go_no_go", "good": True,
                        "text": "The riskiest assumption reads out within %s months."
                        % worst["readout_months"]})
    m = raw["estimates"]["months"]
    if horizon and float(m["high"]) > horizon:
        out.append({"kind": "past_horizon", "text": "Could take up to %s months; the horizon is %s."
                    % (m["high"], horizon)})
    by_model = [LABEL[k] for k in PARAMS if raw["estimates"][k].get("by", "researcher") != "researcher"]
    if by_model:
        out.append({"kind": "model_estimates",
                    "text": "Estimated by the model, not by you: " + ", ".join(by_model) + "."})
    return out


def check(doc):
    """Return a list of problems that would make the numbers meaningless."""
    errs, seen = [], set()
    for n, r in enumerate(doc.get("ideas") or []):
        name = r.get("id") or "idea %d" % (n + 1)
        if not r.get("id"):
            errs.append("%s has no id" % name)
        elif r["id"] in seen:
            errs.append("duplicate id %s" % r["id"])
        seen.add(r.get("id"))
        est = r.get("estimates") or {}
        for k in PARAMS:
            e = est.get(k)
            if not e or e.get("low") is None or e.get("high") is None:
                errs.append("%s: estimate %s needs low and high" % (name, k))
                continue
            vals = [float(e[x]) for x in ("low", "best", "high") if e.get(x) is not None]
            if k == "p_success" and any(v < 0 or v > 1 for v in vals):
                errs.append("%s: p_success must be between 0 and 1" % name)
            if k in ("impact", "fallback") and any(v < 0 or v > 10 for v in vals):
                errs.append("%s: %s is on a 0 to 10 scale" % (name, k))
            if k == "months" and any(v <= 0 for v in vals):
                errs.append("%s: months must be positive" % name)
    return errs


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    doc = json.loads(path.read_text())
    errs = check(doc)
    if errs:
        sys.exit("advisor.json is not ready:\n  " + "\n  ".join(errs))
    per_year = doc.get("utility", "total") == "per_year"
    horizon = (doc.get("researcher") or {}).get("horizon_months")
    rng = random.Random(SEED)
    ideas = [Idea(r, per_year, rng) for r in doc["ideas"]]
    if len(ideas) < 2:
        sys.exit("Need at least two ideas to compare.")

    samples = {i.id: i.samples() for i in ideas}
    means = {k: sum(v) / N for k, v in samples.items()}
    best = max(means, key=means.get)
    wins = {i.id: 0 for i in ideas}
    best_per_draw = 0.0
    for n in range(N):
        top = max(ideas, key=lambda i: samples[i.id][n])
        wins[top.id] += 1
        best_per_draw += samples[top.id][n]
    evpi = best_per_draw / N - means[best]

    # Robustness: move one estimate of one idea by 20% either way.
    flips = []
    for i in ideas:
        for k in PARAMS:
            for s in (0.8, 1.2):
                b = dict(i.b)
                b[k] = bounds(i.raw["estimates"], k, s)
                m = dict(means)
                m[i.id] = i.mean(b)
                new = max(m, key=m.get)
                if new != best:
                    flips.append({"idea": i.id, "estimate": k, "change": "%+d%%" % round((s - 1) * 100),
                                  "new_top": new})

    # Value of partial perfect information, one estimate at a time.
    voi = []
    for i in ideas:
        others = max([means[j.id] for j in ideas if j is not i])
        other_best = max((j for j in ideas if j is not i), key=lambda j: means[j.id]).id
        for jk, k in enumerate(PARAMS):
            lo, mode, hi = i.b[k]
            if hi <= lo:
                continue
            gain, switch, switch_to = 0.0, 0, {}
            for q in range(K):
                theta = tri_ppf((q + 0.5) / K, lo, mode, hi)
                b = dict(i.b)
                b[k] = (theta, theta, theta)
                cond = sum(value(*(tri_ppf(u[j], *b[kk]) for j, kk in enumerate(PARAMS)), per_year)
                           for u in i.u[:N_INNER]) / N_INNER
                gain += max(cond, others)
                now = i.id if cond > others else other_best
                if now != best:
                    switch += 1
                    switch_to[now] = switch_to.get(now, 0) + 1
            evppi = gain / K - means[best]
            voi.append({"idea": i.id, "estimate": k, "label": LABEL[k], "range": [lo, hi],
                        "evppi": round(max(evppi, 0.0), 4),
                        "p_changes_pick": round(switch / K, 3),
                        "new_top": max(switch_to, key=switch_to.get) if switch_to else None})
    voi.sort(key=lambda x: (-x["evppi"], -x["p_changes_pick"]))

    out = {
        "computed_by": "decide.py from the estimates in advisor.json",
        "utility": "per_year" if per_year else "total",
        "samples": N, "seed": SEED,
        "ideas": [{
            "id": i.id,
            "expected_value": round(means[i.id], 3),
            "p_top": round(wins[i.id] / N, 3),
            "mid": {k: round(i.mid(k), 3) for k in PARAMS},
            "flags": flags(i.raw, horizon),
        } for i in sorted(ideas, key=lambda i: -means[i.id])],
        "top": best,
        "pareto_front": pareto(ideas),
        "robust": not flips,
        "flips": flips,
        "evpi": round(max(evpi, 0.0), 4),
        "value_of_information": voi[:8],
    }
    dst = path.with_name("decision.json")
    dst.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")

    title = {r["id"]: r.get("title", r["id"]) for r in doc["ideas"]}
    print("Top on expected value: %s (on top in %d%% of draws)" % (title[best], 100 * wins[best] / N))
    print("Pareto front: " + "; ".join(title[x] for x in out["pareto_front"]))
    print("Robust to 20%% moves: %s" % ("yes" if not flips else "no, %d move(s) change it" % len(flips)))
    if voi and voi[0]["evppi"] > 0:
        v = voi[0]
        print("Most valuable to learn: %s of %s (changes the pick %d%% of the time)"
              % (v["label"], title[v["idea"]], 100 * v["p_changes_pick"]))
    print("Wrote " + str(dst))


if __name__ == "__main__":
    main()
