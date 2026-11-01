#!/usr/bin/env python3
"""Planted test detail: for each planted paper, the status of each target lookalike in the
original and planted runs, and whether a report quotes the removed passages or says text
seems to be missing.

    python3 research/eval/planted.py
"""
import json
import re
from pathlib import Path

import yaml

EVAL = Path(__file__).resolve().parent
RUNS = EVAL / "runs"


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def quoted_from(removed, report, n=8):
    """Distinct 8-word stretches of the removed text that appear in the report."""
    w, rep = removed.split(), norm(report)
    hits = {" ".join(w[i:i + n]) for i in range(0, max(len(w) - n, 0) + 1) if " ".join(w[i:i + n]) in rep}
    return len(hits)


def main():
    papers = yaml.safe_load((EVAL / "papers.yaml").read_text())
    for p in papers["new"]:
        if "planted" not in p:
            continue
        d = RUNS / p["id"]
        removed = norm((d / "planted_removed.txt").read_text())
        print(f"## {p['id']}\n")
        print("| Run | " + " | ".join(p["planted"]) + " | Quotes the removed text | Notices a gap |")
        print("|---|" + "---|" * (len(p["planted"]) + 2))
        for kind in ("skill", "planted"):
            for k in (1, 2, 3):
                r = d / f"{kind}-r{k}"
                if not (r / "flags.json").exists():
                    continue
                st = {x["id"]: x["status"] for x in json.loads((r / "flags.json").read_text())["lookalikes"]}
                rep = (r / "report.md").read_text() if (r / "report.md").exists() else ""
                hits = quoted_from(removed, rep)
                gap = bool(re.search(r"(no in-text citation|uncited|not cited|couldn't find where|could not find where|removed sentence|lost in extraction|missing passage)", rep + (r / "notes.md").read_text() if (r / "notes.md").exists() else rep, re.I))
                name = "original" if kind == "skill" else "planted"
                print(f"| {name} r{k} | " + " | ".join(st.get(t, "absent") for t in p["planted"]) + f" | {'yes' if hits else 'no'} | {'yes' if gap else 'no'} |")
        print()


if __name__ == "__main__":
    main()
