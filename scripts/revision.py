#!/usr/bin/env python3
"""Merge a version comparison into a review and write the revision record.

    python3 revision.py <folder> --old-review <old review.json> [--old-label L] [--new-label L]
        [--records DIR] [--public]

<folder> holds the blind review of the new version (review.json) and the comparison
lane's files:
  inferred.json     changes, inferred_requests, issue_status, unaddressed_major, verdict
  overlay.json      inferred referee concerns matched to items of the new review
  walkthrough.json  per concern: verdict, asked, response, judgment, still_open, ...
  comparison.json   (optional) the Version comparison page

It writes:
  - review.json's "demo" overlay with inferred: true and the walkthrough, so the
    dashboard shows a Referee feedback view (docs/dashboard.md);
  - revision.json in the folder: the revision record (docs/revisions.md), with metrics;
  - a copy of the record in --records (default ~/.referee-preview/revisions/), named
    <old id>--<new id>.json. Only with --public is the record meant for the repository:
    then both versions must be public (an arXiv id each) and it says so.
Prints the metrics and every problem found; exits 1 on a missing or invalid file.
"""
import argparse
import datetime
import json
import sys
from collections import Counter
from pathlib import Path

VERDICTS = {"addressed", "partly", "not_addressed", "unclear"}
STATUSES = {"addressed", "partly", "not_addressed", "moot"}
SCHEMA = "referee-preview/revision@1"


def load(path, problems):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, json.JSONDecodeError) as e:
        problems.append(f"{path}: {e}")
        return None


def metrics(old_review, inferred, walk):
    """Numbers that let us learn from a revision without the referee reports."""
    old = {i["id"]: i for i in old_review["issues"]}
    reqs = inferred["inferred_requests"]
    anticipated = [q for q in reqs if q.get("anticipated_by")]
    by_tier = {}
    for s in inferred["issue_status"]:
        i = old.get(s["issue_id"])
        if not i or i["lane"] == "copy":
            continue
        by_tier.setdefault(i["tier"], Counter())[s["status"]] += 1
    return {
        "inferred_requests": len(reqs),
        "anticipated_by_old_review": len(anticipated),
        "anticipation_rate": round(len(anticipated) / len(reqs), 2) if reqs else None,
        "missed_by_old_review": [q["id"] for q in reqs if not q.get("anticipated_by")],
        "high_confidence_requests": sum(q["confidence"] == "high" for q in reqs),
        # how the old review's items fared, by tier: are A items the ones authors act on?
        "old_items_by_tier": {t: dict(c) for t, c in sorted(by_tier.items())},
        "verdicts": dict(Counter(c["verdict"] for c in walk)),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder")
    ap.add_argument("--old-review", required=True)
    ap.add_argument("--old-label")
    ap.add_argument("--new-label")
    ap.add_argument("--records", default=str(Path.home() / ".referee-preview" / "revisions"))
    ap.add_argument("--public", action="store_true")
    a = ap.parse_args()
    folder = Path(a.folder).resolve()
    problems = []
    review = load(folder / "review.json", problems)
    old_review = load(a.old_review, problems)
    inferred = load(folder / "inferred.json", problems)
    overlay = load(folder / "overlay.json", problems)
    walk_file = load(folder / "walkthrough.json", problems)
    if problems:
        print("\n".join(problems))
        sys.exit(1)

    ids = {i["id"] for i in review["issues"]}
    old_ids = {i["id"] for i in old_review["issues"]}
    reqs = {q["id"]: q for q in inferred["inferred_requests"]}
    walk = walk_file["concerns"]
    for s in inferred["issue_status"]:
        if s["issue_id"] not in old_ids:
            problems.append(f"issue_status: {s['issue_id']} is not in the old review")
        if s["status"] not in STATUSES:
            problems.append(f"issue_status {s['issue_id']}: status {s['status']!r}")
    have = {s["issue_id"] for s in inferred["issue_status"]}
    for i in old_review["issues"]:
        if i["lane"] != "copy" and i["id"] not in have:
            problems.append(f"issue_status: old item {i['id']} has no status")
    for c in overlay["referee_concerns"]:
        for m in c.get("matches", []):
            if m["issue"] not in ids:
                problems.append(f"overlay {c['id']}: {m['issue']} is not in the new review")
    for c in walk:
        if c["id"] not in reqs:
            problems.append(f"walkthrough: {c['id']} is not an inferred request")
            continue
        if c.get("verdict") not in VERDICTS:
            problems.append(f"walkthrough {c['id']}: verdict {c.get('verdict')!r}")
        c.setdefault("title", reqs[c["id"]]["title"])
        c.setdefault("confidence", reqs[c["id"]]["confidence"])
        c["blind"] = [x for x in c.get("blind", []) if x in ids]
    missing = set(reqs) - {c["id"] for c in walk}
    if missing:
        problems.append("walkthrough: no verdict for " + ", ".join(sorted(missing)))

    review["demo"] = {"inferred": True, "note": overlay.get("note", ""),
                      "referee_concerns": overlay["referee_concerns"], "walkthrough": walk}
    (folder / "review.json").write_text(json.dumps(review, ensure_ascii=False, indent=1))

    old_paper, new_paper = old_review["paper"], review["paper"]
    if a.public and not (old_paper.get("arxiv") and new_paper.get("arxiv")):
        problems.append("--public: both versions need an arXiv id; keep this record private")
        a.public = False
    m = metrics(old_review, inferred, walk)
    record = {
        "schema": SCHEMA,
        "date": datetime.date.today().isoformat(),
        "public": bool(a.public),
        "old": {"id": old_paper.get("id"), "arxiv": old_paper.get("arxiv"), "label": a.old_label or old_paper.get("title"),
                "review": old_review.get("id"), "reviewer": old_review.get("reviewer")},
        "new": {"id": new_paper.get("id"), "arxiv": new_paper.get("arxiv"), "label": a.new_label or new_paper.get("title"),
                "review": review.get("id"), "reviewer": review.get("reviewer")},
        "verdict": inferred.get("verdict"),
        "metrics": m,
        "changes": inferred["changes"],
        "inferred_requests": inferred["inferred_requests"],
        "issue_status": inferred["issue_status"],
        "unaddressed_major": inferred.get("unaddressed_major", []),
        "walkthrough": walk,
    }
    text = json.dumps(record, ensure_ascii=False, indent=1)
    (folder / "revision.json").write_text(text)
    out = Path(a.records).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    name = f"{record['old']['id']}--{record['new']['id']}.json".replace("/", "_")
    (out / name).write_text(text)

    print(f"{folder / 'review.json'}: demo overlay with {len(walk)} inferred concerns")
    print(f"{folder / 'revision.json'} (also {out / name}){'' if a.public else ', private'}")
    print(f"anticipated {m['anticipated_by_old_review']}/{m['inferred_requests']} inferred requests; "
          f"verdicts {m['verdicts']}; old items by tier {m['old_items_by_tier']}")
    for p in problems:
        print("problem:", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
