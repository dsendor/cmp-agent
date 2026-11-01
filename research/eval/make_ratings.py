#!/usr/bin/env python3
"""Write eval/ratings/<id>.md for each new paper: every flag and question the assistant
raised across runs, with blank columns for a physicist to rate.

    python3 research/eval/make_ratings.py

Flags are grouped by lookalike id; near-duplicate questions are merged (difflib ratio 0.55
or more) and listed once with the runs that asked them. Rerunning overwrites the sheets,
so copy a sheet before rating it, or rate in a copy named <id>.rated.md.
"""
import difflib
import json
import re
from pathlib import Path

import yaml

EVAL = Path(__file__).resolve().parent
RUNS = EVAL / "runs"
OPEN = {"partly addressed", "not addressed"}


def runs(d):
    return [r for r in sorted(d.glob("skill-r*")) if (r / "flags.json").exists()]


def main():
    papers = yaml.safe_load((EVAL / "papers.yaml").read_text())
    lib = {e["id"]: " ".join(str(e["lookalike"]).split())
           for e in yaml.safe_load((EVAL.parent / "library" / "lookalikes.yaml").read_text())["lookalikes"]}
    for p in papers["new"]:
        d = RUNS / p["id"]
        rs = runs(d)
        flags, qs = {}, []
        for r in rs:
            tag = r.name.replace("skill-", "")
            f = json.loads((r / "flags.json").read_text())
            for x in f["lookalikes"]:
                key = x["id"]
                e = flags.setdefault(key, {"runs": [], "status": []})
                e["runs"].append(tag)
                e["status"].append(x["status"])
            for q in f.get("questions", []):
                for c in qs:
                    if difflib.SequenceMatcher(None, c["text"].lower(), q.lower()).ratio() >= 0.55:
                        c["runs"].append(tag)
                        break
                else:
                    qs.append({"text": q, "runs": [tag]})
        out = [f"# Ratings: arXiv {p['id']} ({p['title']})", "",
               f"*AI only. The flags and questions the lookalike assistant raised in {len(rs)} run(s) "
               f"(library 0.4, 2026-10-23). For a physicist to rate. Rate each row R (reasonable), "
               f"O (off base) or ? (can't tell), with a comment if useful.*", "",
               "## Flags (lookalikes the assistant left open or ruled out)", "",
               "| # | Lookalike | Runs | Status per run | Rating | Comment |", "|---|---|---|---|---|---|"]
        for i, (k, e) in enumerate(sorted(flags.items(), key=lambda kv: -len(kv[1]["runs"])), 1):
            name = lib.get(k, k.replace("outside:", "(not in library)").strip())
            if k in lib:
                name = f"{name} (`{k}`)"
            out.append(f"| F{i} | {name} | {', '.join(e['runs'])} | {'; '.join(e['status'])} |  |  |")
        out += ["", "## Questions to the authors", "",
                "| # | Question (first run that asked it) | Runs | Rating | Comment |", "|---|---|---|---|---|"]
        for i, c in enumerate(sorted(qs, key=lambda c: -len(c["runs"])), 1):
            out.append(f"| Q{i} | {c['text'].replace('|', '/')} | {', '.join(sorted(set(c['runs'])))} |  |  |")
        out += ["", "Reports: " + ", ".join(f"`runs/{p['id']}/{r.name}/report.md`" for r in rs) + "."]
        (EVAL / "ratings" / f"{p['id']}.md").write_text("\n".join(out) + "\n")
        print(p["id"], len(flags), "flags,", len(qs), "questions")


if __name__ == "__main__":
    main()
