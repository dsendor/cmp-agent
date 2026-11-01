#!/usr/bin/env python3
"""Assemble review.json from the structured lanes, assign ids and risk, validate.

    python3 assemble.py <review-folder> --paper-id ID --mode exhaustive|standard \
        [--runs 3] [--model NAME] [--journal NAME] [--source DIR] [--arxiv ID]

Reads from the folder: science.json (required), presentation.json and copy.json
(optional). Writes review.json. Prints a summary and every problem found; exits 1
if science.json is missing or unreadable.
"""
import argparse
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parent.parent / "engine"
TIERS = {"A", "B", "C"}
EFFORTS = {"text", "existing_data", "new_work"}
SCIENCE_TOPICS = {"samples", "null_control", "apparatus", "heating", "calibration", "dependences", "fits",
                  "inhomogeneity", "direct_evidence", "theory", "consistency", "other"}
PRESENTATION_TOPICS = {"overclaiming", "clarity", "context", "figures", "structure"}
COPY_TOPICS = {"consistency", "notation", "references", "language"}
HEDGES = re.compile(r"\b(significant\w*|demonstrat\w*|evidenc\w*|suggest\w*|consistent with|prov\w*|confirm\w*|"
                    r"establish\w*|show\w*|indicat\w*|clear\w*|unambiguous\w*|first)\b", re.I)


def load(folder, name, problems, required=False):
    p = folder / name
    if not p.exists():
        if required:
            sys.exit(f"{p} is missing")
        return None
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as e:
        if required:
            sys.exit(f"{p} is not valid JSON: {e}")
        problems.append(f"{name}: not valid JSON ({e}); lane skipped")
        return None


def copy_risk(item):
    """Copy edits are low risk unless the change touches a number, symbol, unit, citation or hedge word."""
    before, after = item.get("before") or "", item.get("after") or ""
    if re.findall(r"\d", before) != re.findall(r"\d", after):
        return "medium"
    for pat in (r"\$[^$]*\$", r"\\cite\w*\{[^}]*\}", r"\\ref\{[^}]*\}", r"\\(SI|si|unit)\{[^}]*\}"):
        if re.findall(pat, before) != re.findall(pat, after):
            return "medium"
    if sorted(m.lower() for m in HEDGES.findall(before)) != sorted(m.lower() for m in HEDGES.findall(after)):
        return "medium"
    return "low"


def evidence(item, problems, iid):
    ev = item.get("evidence") or {}
    page = ev.get("page")
    if not isinstance(page, int):
        try:
            page = int(page)
        except (TypeError, ValueError):
            problems.append(f"{iid}: no page number")
            page = None
    return {"quote": (ev.get("quote") or "").strip(), "page": page, "location": ev.get("location") or ""}


def claim_id(item, n_claims):
    """1-based index into the paper's claims, 0 for the paper in general, None when missing or out of range."""
    c = item.get("claim_id")
    return c if isinstance(c, int) and 0 <= c <= n_claims else None


def edit_of(e, file=None):
    if not e or not e.get("before") or e.get("after") is None:
        return None
    return {"file": e.get("file", file), "before": e["before"], "after": e["after"]}


def engine_hash():
    h = hashlib.sha256()
    for f in sorted(ENGINE.glob("*.md")):
        h.update(f.name.encode() + b"\0" + f.read_bytes())
    return h.hexdigest()[:12]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--paper-id", required=True)
    ap.add_argument("--mode", choices=["standard", "exhaustive"], required=True)
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--model", default="")
    ap.add_argument("--journal", default="")
    ap.add_argument("--source", default="")
    ap.add_argument("--arxiv", default="")
    a = ap.parse_args()
    folder = Path(a.folder)
    problems = []

    sci = load(folder, "science.json", problems, required=True)
    pres = load(folder, "presentation.json", problems) or {"issues": []}
    cop = load(folder, "copy.json", problems) or {"issues": []}

    n_claims = len(sci.get("claims", []))
    issues = []
    for n, it in enumerate(sci.get("issues", []), 1):
        iid = f"S{n:02d}"
        tier = it.get("tier") if it.get("tier") in TIERS else "B"
        if it.get("tier") not in TIERS:
            problems.append(f"{iid}: tier {it.get('tier')!r} set to B")
        issues.append({
            "id": iid, "lane": "science", "tier": tier, "rank": it.get("rank", n),
            "topic": it.get("topic") if it.get("topic") in SCIENCE_TOPICS else "other",
            "claim": it.get("claim", ""), "claim_id": claim_id(it, n_claims), "issue": it.get("issue", ""),
            "evidence": evidence(it, problems, iid),
            "effort": it.get("effort") if it.get("effort") in EFFORTS else "existing_data",
            "fix": it.get("fix", ""), "fix_scoped": it.get("fix_scoped"),
            "edit_scoped": edit_of(it.get("edit_scoped")), "edit": None,
            "risk": "high", "runs": it.get("runs") or ["r1"],
        })
    for n, it in enumerate(pres.get("issues", []), 1):
        iid = f"P{n:02d}"
        issues.append({
            "id": iid, "lane": "presentation", "tier": it.get("tier") if it.get("tier") in TIERS else "B", "rank": n,
            "topic": it.get("topic") if it.get("topic") in PRESENTATION_TOPICS else "clarity",
            "claim": it.get("claim", ""), "claim_id": claim_id(it, n_claims), "issue": it.get("issue", ""),
            "evidence": evidence(it, problems, iid),
            "effort": it.get("effort") if it.get("effort") in EFFORTS else "text",
            "fix": it.get("fix", ""), "fix_scoped": None, "edit_scoped": None,
            "edit": edit_of(it.get("edit")), "risk": "medium", "runs": [],
        })
    for n, it in enumerate(cop.get("issues", []), 1):
        iid = f"K{n:02d}"
        ed = edit_of(it, it.get("file"))
        if ed is None:
            problems.append(f"{iid}: copy item without before and after; skipped")
            continue
        issues.append({
            "id": iid, "lane": "copy", "tier": None, "rank": n,
            "topic": it.get("topic") if it.get("topic") in COPY_TOPICS else "language",
            "claim": "", "claim_id": None, "issue": it.get("issue", ""), "evidence": evidence(it, problems, iid),
            "effort": "text", "fix": "", "fix_scoped": None, "edit_scoped": None,
            "edit": ed, "risk": copy_risk(it), "runs": [],
        })
    for i in issues:
        i["evidence_found"] = "unchecked"
        i["found_page"] = None

    review = {
        "schema": "referee-preview/review/1",
        "id": f"{a.paper_id}-{datetime.date.today().isoformat()}-{a.mode}",
        "paper": {"id": a.paper_id, "title": sci.get("title", ""), "arxiv": a.arxiv or None,
                  "pdf": "paper.pdf", "source": a.source or None},
        "reviewer": {"version": (ENGINE / "VERSION").read_text().split()[0] if (ENGINE / "VERSION").exists() else "",
                     "engine_hash": engine_hash()},
        "model": a.model, "mode": a.mode, "runs": a.runs, "date": datetime.date.today().isoformat(),
        "target_journal": a.journal or None,
        "claims": sci.get("claims", []), "summary": sci.get("summary", ""),
        "issues": issues,
    }
    (folder / "review.json").write_text(json.dumps(review, indent=1, ensure_ascii=False))
    count = {lane: sum(i["lane"] == lane for i in issues) for lane in ("science", "presentation", "copy")}
    print(f"{folder / 'review.json'}: " + ", ".join(f"{k} {v}" for k, v in count.items()))
    for p in problems:
        print("  problem:", p)


if __name__ == "__main__":
    main()
