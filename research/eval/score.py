#!/usr/bin/env python3
"""Score the evaluation runs in eval/runs/ against eval/papers.yaml.

    python3 research/eval/score.py            # prints markdown tables
    python3 research/eval/score.py --json     # also writes eval/scores.json

Inputs, per paper folder eval/runs/<id>/:
  skill-r<k>/flags.json          lookalike assistant runs (k = 1, 2, 3)
  planted-r<k>/flags.json        runs on the planted text (passages removed)
  openaireview/mapped.json       baseline 1, mapped to library ids by the judge
  plain/mapped.json              baseline 2, mapped to library ids by the judge
  judge.json                     the judge's mapping of baseline comments and outside rows

A flag is a lookalike marked "partly addressed" or "not addressed". mapped.json has
{"flags": [<library id or short name>, ...]}, the explanations a review raised as open.
"""
import difflib
import itertools
import json
import sys
from pathlib import Path

import yaml

EVAL = Path(__file__).resolve().parent
RUNS = EVAL / "runs"
OPEN = {"partly addressed", "not addressed"}


def load(p):
    return json.loads(p.read_text()) if p.exists() else None


def outside_canon(paper_dir):
    """Map each outside-row name in a paper's runs to one canonical label: the judge's
    library id when it found one (judge.json), else the first similar name (difflib >= 0.6)."""
    judge = load(paper_dir / "judge.json") or {}
    jmap = {k.strip().lower(): v for k, v in (judge.get("outside") or {}).items()}
    canon, labels = {}, []
    for f in sorted(paper_dir.glob("*-r*/flags.json")):
        for r in load(f)["lookalikes"]:
            if not r["id"].startswith("outside"):
                continue
            name = r["id"].split(":", 1)[-1].strip()
            if name in canon:
                continue
            if jmap.get(name.lower()):
                canon[name] = jmap[name.lower()]
                continue
            match = next((l for l in labels if difflib.SequenceMatcher(None, l.lower(), name.lower()).ratio() >= 0.6), None)
            if match is None:
                labels.append(name)
                match = name
            canon[name] = "outside: " + match
    return canon


def skill_flags(run_dir):
    """Lookalikes a run left open, with outside rows given one label per paper."""
    f = load(run_dir / "flags.json")
    if not f:
        return None
    canon = outside_canon(run_dir.parent)
    flags = set()
    for r in f["lookalikes"]:
        if r["status"] not in OPEN:
            continue
        if r["id"].startswith("outside"):
            flags.add(canon.get(r["id"].split(":", 1)[-1].strip(), r["id"]))
        else:
            flags.add(r["id"])
    return flags


def statuses(run_dir):
    f = load(run_dir / "flags.json")
    return {r["id"]: r["status"] for r in f["lookalikes"]} if f else {}


def jaccard(a, b):
    return len(a & b) / len(a | b) if a | b else 1.0


def stability(runs):
    """Mean pairwise Jaccard of flag sets, and how many flags appear in every run."""
    sets = [s for s in runs if s is not None]
    if len(sets) < 2:
        return None, None, len(sets)
    pairs = [jaccard(a, b) for a, b in itertools.combinations(sets, 2)]
    return sum(pairs) / len(pairs), len(set.intersection(*sets)), len(sets)


def key_ids(key):
    """Each answer-key explanation as a set of acceptable ids."""
    return [{k["explanation"], *k.get("also", [])} for k in key]


def recall_precision(flags, key):
    if flags is None:
        return None
    keys = key_ids(key)
    hits = sum(1 for k in keys if k & flags)
    in_key = sum(1 for f in flags if any(f in k for k in keys))
    return hits, len(keys), in_key, len(flags)


def main():
    papers = yaml.safe_load((EVAL / "papers.yaml").read_text())
    out = {"new": {}, "known": {}}
    print("## New papers: stability over repeated runs\n")
    print("| Paper | Runs | Flags per run | Mean pairwise Jaccard | Flags in every run | Ruled out per run |")
    print("|---|---|---|---|---|---|")
    for p in papers["new"]:
        d = RUNS / p["id"]
        runs = [skill_flags(d / f"skill-r{k}") for k in (1, 2, 3)]
        j, common, n = stability(runs)
        sizes = [len(s) for s in runs if s is not None]
        ruled = [sum(1 for s in statuses(d / f"skill-r{k}").values() if s == "ruled out") for k in (1, 2, 3)
                 if (d / f"skill-r{k}" / "flags.json").exists()]
        out["new"][p["id"]] = {"runs": n, "sizes": sizes, "jaccard": j, "common": common, "ruled_out": ruled}
        print(f"| {p['id']} | {n} | {sizes} | {j:.2f} | {common} | {ruled} |" if j is not None
              else f"| {p['id']} | {n} | {sizes} | n/a | n/a | {ruled} |")

    print("\n## Planted test: status of the removed point, original runs vs planted runs\n")
    print("| Paper | Lookalike | Original runs | Planted runs |")
    print("|---|---|---|---|")
    for p in papers["new"]:
        for target in p.get("planted", []):
            d = RUNS / p["id"]
            orig = [statuses(d / f"skill-r{k}").get(target, "absent") for k in (1, 2, 3) if (d / f"skill-r{k}").exists()]
            plant = [statuses(d / f"planted-r{k}").get(target, "absent") for k in (1, 2, 3) if (d / f"planted-r{k}").exists()]
            out["new"][p["id"]].setdefault("planted", {})[target] = {"original": orig, "planted": plant}
            print(f"| {p['id']} | {target} | {', '.join(orig)} | {', '.join(plant)} |")

    print("\n## Known-outcome papers: recall and precision against the answer key\n")
    print("| Paper | Method | Recall | Precision (floor) |")
    print("|---|---|---|---|")
    for p in papers["known"]:
        d = RUNS / p["id"]
        methods = {
            "assistant": skill_flags(d / "skill-r1"),
            "OpenAIReview prompt": set((load(d / "openaireview" / "mapped.json") or {"flags": None})["flags"] or []) if (d / "openaireview" / "mapped.json").exists() else None,
            "plain prompt": set((load(d / "plain" / "mapped.json") or {"flags": None})["flags"] or []) if (d / "plain" / "mapped.json").exists() else None,
        }
        for name, flags in methods.items():
            r = recall_precision(flags, p["key"])
            out["known"].setdefault(p["id"], {})[name] = r
            if r:
                print(f"| {p['id']} | {name} | {r[0]} of {r[1]} | {r[2]} of {r[3]} |")
            else:
                print(f"| {p['id']} | {name} | not run | not run |")

    print("\n## New papers: what the baselines raised that the assistant also raised\n")
    print("| Paper | Assistant flags (any run) | OpenAIReview prompt | Plain prompt | Shared with OpenAIReview | Shared with plain |")
    print("|---|---|---|---|---|---|")
    for p in papers["new"]:
        d = RUNS / p["id"]
        a = set().union(*[s for s in (skill_flags(d / f"skill-r{k}") for k in (1, 2, 3)) if s] or [set()])
        o = set((load(d / "openaireview" / "mapped.json") or {}).get("flags", []))
        pl = set((load(d / "plain" / "mapped.json") or {}).get("flags", []))
        out["new"][p["id"]].update({"assistant_any": sorted(a), "openaireview": sorted(o), "plain": sorted(pl)})
        print(f"| {p['id']} | {len(a)} | {len(o)} | {len(pl)} | {len(a & o)} | {len(a & pl)} |")

    if "--json" in sys.argv:
        (EVAL / "scores.json").write_text(json.dumps(out, indent=2, default=list))


if __name__ == "__main__":
    main()
