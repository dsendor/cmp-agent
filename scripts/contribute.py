#!/usr/bin/env python3
"""Build a redacted contribution from a review and its decisions, scrub it, and optionally send it.

    python3 contribute.py <review-folder> --level 0|1|2|3 [--rewrites rewrites.json]
                          [--allow ID ...] [--send]

Levels: 0 labels only (lane, topic, tier, effort, decision); 1 adds each item's text as
rewritten without specifics (rewrites.json: {"S01": "...", ...}, written by the contribute
skill and approved by the user); 2 adds the item text as reviewed, without quotes; 3 adds the
quote from the paper (only for a paper that is already public).

The scrub looks for anything that identifies the paper: its title, arXiv id, any run of six
words that also appears in the paper, numbers with units, chemical formulas, and the lines
under "## Never share" in ~/.referee-preview/my-style.md. Every hit is listed, and the
contribution is not written while hits remain, unless the item is passed with --allow.

Writes <review-folder>/contribution.json. With --send, posts it to the feedback endpoint
(REFEREE_PREVIEW_FEEDBACK_URL, or the default below) and keeps a copy in
~/.referee-preview/contributions/. Exit codes: 0 done, 2 scrub hits remain, 3 send failed.
"""
import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ENDPOINT = os.environ.get("REFEREE_PREVIEW_FEEDBACK_URL",
                          "https://cmp-agent-feedback-dsendor-gmailcoms-projects.vercel.app/api/contribute")
HOME = Path.home() / ".referee-preview"
UNITS = r"(?:meV|eV|K|mK|T|mT|GPa|nm|um|μm|mm|Ω|ohm|kΩ|V|mV|Hz|kHz|MHz|GHz|THz|%|deg|°)"
NUMBER_UNIT = re.compile(r"\b\d+(?:\.\d+)?\s?" + UNITS + r"(?![A-Za-z])")
FORMULA = re.compile(r"\b(?:[A-Z][a-z]?\d*){2,}\b")


def words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def never_share():
    p = HOME / "my-style.md"
    if not p.exists():
        return []
    out, on = [], False
    for line in p.read_text().splitlines():
        if line.startswith("## "):
            on = line.strip().lower() == "## never share"
        elif on and line.strip().lstrip("-* ").strip():
            out.append(line.strip().lstrip("-* ").strip())
    return out


def build(review, decisions, level, rewrites):
    items = []
    for i in review["issues"]:
        d = decisions.get(i["id"]) or {}
        if not d.get("decision"):
            continue
        item = {"lane": i["lane"], "topic": i["topic"], "tier": i.get("tier"), "effort": i.get("effort"),
                "decision": d["decision"]}
        refs = [c for c in (review.get("demo") or {}).get("referee_concerns", [])
                if any(m["issue"] == i["id"] for m in c.get("matches", []))]
        if refs:
            item["referee_raised"] = True
        if level == 1 and i["id"] in rewrites:
            item["text"] = rewrites[i["id"]]
        elif level >= 2:
            item["text"] = i["issue"] + (" Author's note: " + d["note"] if d.get("note") else "")
        if level == 3:
            item["quote"] = i["evidence"]["quote"]
        items.append((i["id"], item))
    counts = {lane: sum(1 for _, it in items if it["lane"] == lane) for lane in ("science", "presentation", "copy")}
    meta = {"reviewer_version": review["reviewer"].get("version"), "mode": review.get("mode"),
            "model": review.get("model"), "runs": review.get("runs"), "counts": counts}
    return meta, items


def scrub(items, review, folder):
    """Return {item id: [reasons]} for every identifying string found in an item's text."""
    marks = [("the paper's title", review["paper"].get("title") or ""), ("the arXiv id", review["paper"].get("arxiv") or ""),
             ("the paper id", review["paper"].get("id") or "")]
    marks += [("your never-share list", s) for s in never_share()]
    six = set()
    pages = folder / "paper.pages.json"
    if pages.exists():
        ws = words(" ".join(json.loads(pages.read_text())["pages"]))
        six = {" ".join(ws[k:k + 6]) for k in range(len(ws) - 5)}
    hits = {}
    for iid, it in items:
        text = " ".join(str(it.get(k) or "") for k in ("text", "quote"))
        if not text.strip():
            continue
        found = [name for name, s in marks if s and s.lower() in text.lower()]
        tw = words(text)
        runs = {" ".join(tw[k:k + 6]) for k in range(len(tw) - 5)} & six
        if runs and "quote" not in it:
            found.append("words copied from the paper: \"" + sorted(runs)[0] + " ...\"")
        found += ["a number with units: " + m for m in NUMBER_UNIT.findall(text)]
        found += ["a formula or symbol: " + m for m in FORMULA.findall(text) if any(c.isdigit() for c in m) or len(m) > 3]
        if found:
            hits[iid] = found
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--level", type=int, choices=[0, 1, 2, 3], required=True)
    ap.add_argument("--rewrites")
    ap.add_argument("--allow", nargs="*", default=[])
    ap.add_argument("--send", action="store_true")
    a = ap.parse_args()
    folder = Path(a.folder)
    review = json.loads((folder / "review.json").read_text())
    dfile = folder / "decisions.json"
    if not dfile.exists():
        sys.exit(f"{dfile} is missing: export decisions from the dashboard first")
    decisions = json.loads(dfile.read_text()).get("decisions", {})
    rewrites = json.loads(Path(a.rewrites).read_text()) if a.rewrites else {}
    meta, items = build(review, decisions, a.level, rewrites)
    if not items:
        sys.exit("no decided items to contribute")

    hits = {k: v for k, v in scrub(items, review, folder).items() if k not in a.allow}
    for iid, reasons in hits.items():
        print(f"{iid}: " + "; ".join(reasons))
    if hits:
        print(f"{len(hits)} items still identify the paper. Rewrite or drop them, or pass --allow with their ids.")
        sys.exit(2)

    body = {"schema": "referee-preview/contribution/1", "level": a.level, "meta": meta, "items": [it for _, it in items]}
    out = folder / "contribution.json"
    out.write_text(json.dumps(body, indent=1, ensure_ascii=False))
    print(f"{out}: level {a.level}, {len(items)} items, no identifying text found")
    if not a.send:
        return
    if not ENDPOINT:
        sys.exit("no feedback endpoint configured (REFEREE_PREVIEW_FEEDBACK_URL); send the file by email instead")
    req = urllib.request.Request(ENDPOINT, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    try:
        reply = json.loads(urllib.request.urlopen(req, timeout=30).read())
    except Exception as e:
        print(f"send failed: {e}")
        sys.exit(3)
    (HOME / "contributions").mkdir(parents=True, exist_ok=True)
    (HOME / "contributions" / f"{review['id']}-{reply.get('id', 'sent')}.json").write_text(out.read_text())
    print(f"sent: contribution {reply.get('id')}")


if __name__ == "__main__":
    main()
