#!/usr/bin/env python3
"""Validate the lookalike library and the text files around it.

    python3 research/scripts/check.py            # fields, ids, URLs, labels, style
    python3 research/scripts/check.py --quotes   # also fetch each arXiv source and
                                                      # confirm every quote appears in it

Fails on: a missing field, a duplicate id, a source with no URL or no quote, a Notion URL
as a source, `checked` other than `ai` or `human`, an em dash anywhere in research/,
and contrast phrasing outside quotes. --quotes needs network access to arxiv.org and
`pdftotext` (poppler); fetched text is cached in ~/.cache/cmp-assistant.
"""
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library" / "lookalikes.yaml"
CACHE = Path.home() / ".cache" / "cmp-assistant"

FIELDS = ["id", "family", "signature", "lookalike", "mechanism", "control", "tests",
          "data_that_reveals_it", "sources", "checked"]
SOURCE_FIELDS = ["url", "title", "where", "quote"]
# Writing rules from the brief: no contrast phrasing in our own words.
CONTRAST = [r"\brather than\b", r"\binstead of\b", r"\bnot\s+\w+(\s+\w+)?\s+but\b"]

errors = []


def err(msg):
    errors.append(msg)


def check_library():
    data = yaml.safe_load(LIBRARY.read_text())
    families = set(data["meta"]["families"])
    seen = set()
    for i, e in enumerate(data["lookalikes"]):
        where = e.get("id", f"entry {i}")
        for f in FIELDS:
            if not e.get(f):
                err(f"{where}: missing {f}")
        if where in seen:
            err(f"{where}: duplicate id")
        seen.add(where)
        if e.get("family") not in families:
            err(f"{where}: unknown family {e.get('family')}")
        if e.get("checked") not in ("ai", "human"):
            err(f"{where}: checked must be ai or human")
        for s in e.get("sources") or []:
            for f in SOURCE_FIELDS:
                if not s.get(f):
                    err(f"{where}: source missing {f}")
            url = s.get("url", "")
            if not url.startswith("https://"):
                err(f"{where}: source URL must be https: {url}")
            if "notion." in url:
                err(f"{where}: a Notion page is not a source: {url}")
        if not isinstance(e.get("tests"), list) or not all(isinstance(t, str) and t for t in e.get("tests") or []):
            err(f"{where}: tests must be a list of short strings")
        for f in ("signature", "lookalike", "mechanism", "control", "tests", "data_that_reveals_it"):
            for pat in CONTRAST:
                if re.search(pat, str(e.get(f, "")), re.I):
                    err(f"{where}: contrast phrasing in {f}")
    check_checks(data, families | {"practice"}, seen)
    return data


def check_source(where, s):
    for f in SOURCE_FIELDS:
        if not s.get(f):
            err(f"{where}: source missing {f}")
    url = s.get("url", "")
    if not url.startswith("https://") or "notion." in url:
        err(f"{where}: source URL must be https and not Notion: {url}")


def check_checks(data, families, entry_ids):
    """Ordered checks per family: known family, unique step ids, known lookalikes, sources."""
    step_ids = set()
    for c in data.get("checks") or []:
        fam = c.get("family")
        if fam not in families:
            err(f"checks: unknown family {fam}")
        if c.get("note") and not c.get("note_source"):
            err(f"checks {fam}: note needs note_source")
        if c.get("note_source"):
            check_source(f"checks {fam} note", c["note_source"])
        for st in c.get("steps") or []:
            sid = st.get("id", "?")
            if sid in step_ids:
                err(f"check {sid}: duplicate id")
            step_ids.add(sid)
            for f in ("check", "addresses", "sources"):
                if not st.get(f):
                    err(f"check {sid}: missing {f}")
            for a in st.get("addresses") or []:
                if a not in entry_ids:
                    err(f"check {sid}: unknown lookalike {a}")
            for s in st.get("sources") or []:
                check_source(f"check {sid}", s)
            for pat in CONTRAST:
                if re.search(pat, st.get("check", ""), re.I):
                    err(f"check {sid}: contrast phrasing")


def all_sources(data):
    """Every (label, source) pair in the library: entries, checks and check notes."""
    for e in data["lookalikes"]:
        for s in e["sources"]:
            yield e["id"], s
    for c in data.get("checks") or []:
        if c.get("note_source"):
            yield f"checks {c['family']} note", c["note_source"]
        for st in c.get("steps") or []:
            for s in st.get("sources") or []:
                yield f"check {st['id']}", s


def check_style():
    for path in ROOT.rglob("*"):
        if path.is_dir() or path.suffix not in (".md", ".yaml", ".py", ".sh") or "dist" in path.parts:
            continue
        text = path.read_text()
        if "\u2014" in text:
            err(f"{path.relative_to(ROOT)}: em dash")
        if path.suffix == ".md":
            # Quoted text (in quotation marks or blockquotes) is the source's words.
            own = re.sub(r'"[^"\n]*"|“[^”]*”', "", text)
            own = "\n".join(l for l in own.splitlines() if not l.lstrip().startswith(">"))
            for pat in CONTRAST:
                for m in re.finditer(pat, own, re.I):
                    line = own[: m.start()].count("\n") + 1
                    err(f"{path.relative_to(ROOT)}:{line}: contrast phrasing '{m.group(0)}'")


def norm(s):
    s = s.replace("-\n", "")
    return re.sub(r"[^a-z0-9]", "", s.lower())


def arxiv_text(arxiv_id):
    CACHE.mkdir(parents=True, exist_ok=True)
    txt = CACHE / f"{arxiv_id}.txt"
    if not txt.exists():
        pdf = CACHE / f"{arxiv_id}.pdf"
        req = urllib.request.Request(f"https://arxiv.org/pdf/{arxiv_id}",
                                     headers={"User-Agent": "cmp-assistant-check"})
        pdf.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        subprocess.run(["pdftotext", str(pdf), str(txt)], check=True)
        abs_req = urllib.request.Request(f"https://arxiv.org/abs/{arxiv_id}",
                                         headers={"User-Agent": "cmp-assistant-check"})
        abs_html = urllib.request.urlopen(abs_req, timeout=60).read().decode("utf8", "ignore")
        m = re.search(r'<meta name="citation_abstract" content="(.*?)"', abs_html, re.S)
        if m:
            import html
            with txt.open("a") as f:
                f.write("\n" + html.unescape(m.group(1)))
    return txt.read_text(errors="ignore")


def check_quotes(data):
    checked = 0
    for label, s in all_sources(data):
        m = re.match(r"https://arxiv\.org/(?:abs|pdf|html)/([0-9.]+)", s["url"])
        if not m:
            print(f"  skip (not arXiv, check by hand): {label} {s['url']}")
            continue
        text = arxiv_text(m.group(1))
        if norm(s["quote"]) not in norm(text):
            err(f"{label}: quote not found in {s['url']}: {s['quote'][:60]}...")
        checked += 1
    print(f"  {checked} quotes checked against their sources")


if __name__ == "__main__":
    data = check_library()
    check_style()
    if "--quotes" in sys.argv:
        check_quotes(data)
    n = len(data["lookalikes"])
    if errors:
        print("\n".join(errors))
        print(f"FAILED: {len(errors)} problems")
        sys.exit(1)
    k = sum(len(c.get("steps") or []) for c in data.get("checks") or [])
    print(f"OK: {n} lookalikes and {k} checks, every one sourced and labeled")
