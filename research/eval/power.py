#!/usr/bin/env python3
"""Simulated power to detect a recall gain between two reviewer variants.

    python3 research/eval/power.py                  # the plan's table, default settings
    python3 research/eval/power.py --sensitivity    # also vary repeat rate and gain spread
    python3 research/eval/power.py --repeat 0.62    # rerun with a measured repeat rate
    python3 research/eval/power.py --stat paper     # the 2026-10-27 statistic, per-paper means

Model. Each paper gets a number of eligible concerns drawn from the 16 judged papers in
referee/scores.json. Each concern has a latent ease z = a_paper + e_concern, and a run raises
it with probability Phi(z), independently across runs. Three settings are calibrated:
mean recall (46%, the plain prompt), the run-to-run repeat rate P(raised in run 2 | raised in
run 1) = E[p^2]/E[p], and the paper-to-paper spread of single-run recall (0.20 observed on the
16 papers, which includes binomial noise). The variant shifts every z by delta plus a paper
term g_paper ~ N(0, gain_sd), so the gain varies by paper; delta is set so mean recall rises
by the target. Both arms run R times on the same papers.

The test (U1, 2026-10-28) is on pooled recall: per paper, d = the difference in concerns raised
(mean over runs), and the pooled gain is sum(d) / sum(n). A paired one-sided t-test over papers
on d, alpha 0.05, so papers count by their number of concerns. --stat paper gives the earlier
test on per-paper recall (d / n), where every paper counts the same. Concern counts are the full
distribution of eligible concerns on the 16 judged papers (2 to 24, including the three papers
the removed five-concern minimum had cut). Cells more than 10 points from the plan's table are
flagged. Needs numpy and scipy.
"""
import argparse
import json
from pathlib import Path

import numpy as np
from scipy import optimize, stats

ROOT = Path(__file__).resolve().parent
BASE = 0.46
SIMS = 4000


def counts():
    rs = json.loads((ROOT / "referee" / "scores.json").read_text())["concerns"]
    c = {}
    for r in rs:
        c[r["paper"]] = c.get(r["paper"], 0) + 1
    return np.array(sorted(c.values()))


def moments(mu, sd, nodes=np.polynomial.hermite_e.hermegauss(80)):
    """E[p] and E[p^2] for p = Phi(z), z ~ N(mu, sd)."""
    x, w = nodes
    w = w / w.sum()
    p = stats.norm.cdf(mu + sd * x)
    return (w * p).sum(), (w * p * p).sum()


def calibrate(repeat, spread, ns, rng):
    """Find mu, tau (paper sd) and s (concern sd) that hit mean, repeat rate and spread."""
    def total_sd(rep):
        # Total latent sd that gives this repeat rate at mean BASE.
        def f(sd):
            mu = optimize.brentq(lambda m: moments(m, sd)[0] - BASE, -5, 5)
            m1, m2 = moments(mu, sd)
            return m2 / m1 - rep
        sd = optimize.brentq(f, 0.01, 10)
        mu = optimize.brentq(lambda m: moments(m, sd)[0] - BASE, -5, 5)
        return mu, sd

    mu, sd = total_sd(repeat)
    # Split the latent variance between paper and concern to match the observed spread.
    def sim_spread(frac):
        tau, s = sd * np.sqrt(frac), sd * np.sqrt(1 - frac)
        out = []
        for _ in range(400):
            a = rng.normal(mu, tau, len(ns))
            rec = [rng.binomial(1, stats.norm.cdf(rng.normal(ai, s, n))).mean() for ai, n in zip(a, ns)]
            out.append(np.std(rec, ddof=1))
        return np.mean(out)
    lo, hi = 0.0, 0.95
    if sim_spread(lo) > spread:
        frac = 0.0
    else:
        for _ in range(14):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if sim_spread(mid) < spread else (lo, mid)
        frac = (lo + hi) / 2
    return mu, sd * np.sqrt(frac), sd * np.sqrt(1 - frac)


def delta_for(gain, mu, sd_total, gain_sd):
    return optimize.brentq(lambda d: moments(mu + d, np.hypot(sd_total, gain_sd))[0] - (BASE + gain), -1, 5)


PLAN = {"16x1": (27, 64, 90), "30x1": (40, 84, 99), "50x1": (53, 96, 100), "80x1": (72, 99, 100),
        "120x1": (85, 100, 100), "16x3": (53, 92, 100), "30x3": (72, 99, 100), "50x3": (90, 100, 100)}


def power(n_papers, runs, gain, cal, gain_sd, ns, rng, stat="pooled"):
    mu, tau, s = cal
    d = delta_for(gain, mu, np.hypot(tau, s), gain_sd)
    tcrit = stats.t.ppf(0.95, n_papers - 1)
    hits = 0
    for _ in range(SIMS):
        n = rng.choice(ns, n_papers)
        paper = np.repeat(np.arange(n_papers), n)
        z = rng.normal(mu, tau, n_papers)[paper] + rng.normal(0, s, paper.size)
        pa = stats.norm.cdf(z)
        pb = stats.norm.cdf(z + d + rng.normal(0, gain_sd, n_papers)[paper])
        ka = rng.binomial(runs, pa)
        kb = rng.binomial(runs, pb)
        diffs = (np.bincount(paper, kb, n_papers) - np.bincount(paper, ka, n_papers)) / runs
        if stat == "paper":
            diffs = diffs / n
        sdv = diffs.std(ddof=1)
        if sdv > 0 and diffs.mean() / (sdv / np.sqrt(n_papers)) > tcrit:
            hits += 1
    return hits / SIMS


DESIGNS = [(16, 1), (30, 1), (50, 1), (80, 1), (120, 1), (16, 3), (30, 3), (50, 3)]
GAINS = [0.05, 0.10, 0.15]


def table(repeat, spread, gain_sd, seed=7, stat="pooled"):
    rng = np.random.default_rng(seed)
    ns = counts()
    cal = calibrate(repeat, spread, ns, rng)
    print(f"\nStatistic {stat}; repeat rate {repeat:.2f}, single-run paper spread {spread:.2f}, gain sd {gain_sd:.2f} "
          f"(latent: mu {cal[0]:.2f}, paper sd {cal[1]:.2f}, concern sd {cal[2]:.2f}); {SIMS} simulations per cell")
    print(f"Concern counts per paper ({len(ns)} papers, {ns.sum()} concerns): {', '.join(map(str, ns))}\n")
    print("| Papers × runs | Paper-runs | Detect 5 pts | Detect 10 pts | Detect 15 pts | Plan's table | Flag |")
    print("|---|---|---|---|---|---|---|")
    out = {}
    for n, r in DESIGNS:
        cells = [power(n, r, g, cal, gain_sd, ns, rng, stat) for g in GAINS]
        out[f"{n}x{r}"] = cells
        plan = PLAN[f"{n}x{r}"]
        flag = ", ".join(f"{int(100 * g)} pts moved {100 * c - q:+.0f}" for g, c, q in zip(GAINS, cells, plan)
                         if abs(100 * c - q) > 10)
        print(f"| {n} × {r} | {n * r} | " + " | ".join(f"{100 * c:.0f}%" for c in cells)
              + f" | {', '.join(map(str, plan))} | {flag} |")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repeat", type=float, default=0.70)
    ap.add_argument("--spread", type=float, default=0.20)
    ap.add_argument("--gain-sd", type=float, default=0.25, help="paper-to-paper sd of the gain, latent scale")
    ap.add_argument("--sensitivity", action="store_true")
    ap.add_argument("--stat", choices=["pooled", "paper"], default="pooled")
    a = ap.parse_args()
    table(a.repeat, a.spread, a.gain_sd, stat=a.stat)
    if a.sensitivity:
        for rep in (0.65, 0.77):
            table(rep, a.spread, a.gain_sd, stat=a.stat)
        table(a.repeat, a.spread, 0.5, stat=a.stat)
        table(a.repeat, a.spread, 0.0, stat=a.stat)


if __name__ == "__main__":
    main()
