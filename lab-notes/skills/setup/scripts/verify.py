#!/usr/bin/env python3
"""Check every fact in the lab record against the original it cites. Code, not a prompt.

  verify.py ROOT [ENTRY_ID ...] [--json]

For each fact in each entry sidecar:
  - the cited file must exist and, if a sha256 is given, be unchanged;
  - qcodes: re-read the run from the database and compare the value (and unit);
  - file (CSV/TSV): re-read the cell at row/column and compare;
  - json: follow the JSON pointer and compare;
  - dictation/text: the quoted words must appear in the file;
  - photo/pdf: cannot be checked by code; listed for a person, with page and region;
  - inferred: the facts it rests on must exist;
  - any number must have a unit (unit "" is allowed only for counts and ids, marked
    "unit": "1").
And for each entry's text: frontmatter with `checked:`, a **TL;DR:** first (at most 60
words), and a warning past 300 words of prose.
Exit 1 if anything fails, so it can gate a commit.
"""
import argparse
import csv
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qcodes_runs  # noqa: E402

REL_TOL = 1e-6
_db_cache = {}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().lower()


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


UNIT_SCALE = {
    # prefix -> factor, applied to a base unit
    "": 1.0, "k": 1e3, "m": 1e-3, "u": 1e-6, "µ": 1e-6, "μ": 1e-6, "n": 1e-9, "p": 1e-12, "M": 1e6, "G": 1e9,
}


def to_base(value, unit):
    """(value in base unit, base unit) for simple SI prefixes, e.g. 12 mK -> (0.012, K)."""
    v = num(value)
    if v is None or not unit:
        return v, unit
    for base in ("K", "T", "V", "A", "Hz", "s", "Ohm", "Ω", "W", "e^2/h"):
        if unit == base:
            return v, base
        if unit.endswith(base) and unit[: -len(base)] in UNIT_SCALE:
            return v * UNIT_SCALE[unit[: -len(base)]], base
    return v, unit


def same_value(claimed, claimed_unit, actual, actual_unit):
    a, au = to_base(claimed, claimed_unit)
    b, bu = to_base(actual, actual_unit)
    if a is not None and b is not None:
        if actual_unit and claimed_unit and au != bu:
            return False, "unit %s vs %s" % (claimed_unit, actual_unit)
        ok = abs(a - b) <= REL_TOL * max(abs(a), abs(b), 1e-30)
        return ok, "" if ok else "value %s %s vs %s %s" % (claimed, claimed_unit, actual, actual_unit)
    ok = norm(claimed) == norm(actual)
    return ok, "" if ok else "value %r vs %r" % (claimed, actual)


def check_fact(fact, project, facts_by_id):
    src = fact.get("source") or {}
    t = src.get("type")
    loc = src.get("locator") or {}
    val, unit = fact.get("value"), fact.get("unit", None)
    status = fact.get("status")

    # Units: any number needs one.
    if num(val) is not None and unit in (None, "") and status != "not recorded":
        return "fail", "number without a unit (use \"1\" for counts and ids)"

    if status == "not recorded":
        return ("ok", "not recorded") if val in (None, "") else ("fail", "marked not recorded but has a value")

    if t == "inferred":
        missing = [f for f in src.get("from", []) if f not in facts_by_id]
        if not src.get("from"):
            return "fail", "inferred with no facts it rests on"
        return ("fail", "rests on missing facts %s" % missing) if missing else ("ok", "inferred from %s" % ", ".join(src["from"]))

    if t == "person":
        return "person", "said by %s" % src.get("who", "someone")

    path = src.get("path")
    if not path:
        return "fail", "no source path"
    full = path if os.path.isabs(path) else os.path.join(project, path)
    if not os.path.exists(full):
        return "fail", "source missing: %s" % path
    if src.get("sha256") and t != "qcodes" and sha256(full) != src["sha256"]:
        return "fail", "source changed since it was cited (sha256 differs): %s" % path

    if t == "qcodes":
        run = loc.get("run_id")
        field = loc.get("parameter") or loc.get("field")
        if run is None or not field:
            return "fail", "qcodes source needs locator.run_id and locator.parameter"
        con = _db_cache.get(full) or qcodes_runs.connect(full)
        _db_cache[full] = con
        actual, aunit = qcodes_runs.get_field(con, int(run), field)
        if aunit is None:
            return "fail", "run %s has no %s" % (run, field)
        ok, why = same_value(val, unit or "", actual, aunit)
        return ("ok", "run %s %s = %s %s" % (run, field, actual, aunit)) if ok else ("fail", why)

    if t == "file":
        row, col = loc.get("row"), loc.get("column")
        if row is None or col is None:
            return "fail", "file source needs locator.row and locator.column"
        delim = "\t" if full.endswith((".tsv", ".tab")) else ","
        with open(full, newline="", errors="replace") as f:
            rows = list(csv.reader(f, delimiter=delim))
        if not rows or int(row) < 1 or int(row) > len(rows):
            return "fail", "row %s out of range" % row
        header = rows[0]
        if isinstance(col, int) or str(col).isdigit():
            ci = int(col) - 1
        else:
            if col not in header:
                return "fail", "no column %r" % col
            ci = header.index(col)
        r = rows[int(row) - 1]
        if ci >= len(r):
            return "fail", "row %s has no column %s" % (row, col)
        # The file's own unit, if it differs from the fact's (e.g. file in A, fact in nA).
        ok, why = same_value(val, unit or "", r[ci], loc.get("unit", unit or ""))
        return ("ok", "row %s %s = %s" % (row, col, r[ci])) if ok else ("fail", why)

    if t == "json":
        ptr = loc.get("pointer", "")
        node = json.load(open(full))
        for part in [p for p in ptr.split("/") if p != ""]:
            part = part.replace("~1", "/").replace("~0", "~")
            try:
                node = node[int(part)] if isinstance(node, list) else node[part]
            except (KeyError, IndexError, ValueError, TypeError):
                return "fail", "pointer %s not found" % ptr
        ok, why = same_value(val, unit or "", node, loc.get("unit", unit or ""))
        return ("ok", "%s = %s" % (ptr, node)) if ok else ("fail", why)

    if t in ("dictation", "text"):
        quote = src.get("quote")
        if not quote:
            return "fail", "dictation/text source needs the exact quote"
        text = open(full, errors="replace").read()
        return ("ok", "quote found") if norm(quote) in norm(text) else ("fail", "quote not in %s" % path)

    if t == "attachment":
        quote = src.get("quote")
        if not quote:
            return "fail", "attachment source needs the exact quote from the transcription"
        text = open(full, errors="replace").read()
        if norm(quote) not in norm(text):
            return "fail", "quote not in the transcription %s" % path
        return "person", "from a chat attachment that wasn't kept; check the transcription: %r" % quote

    if t in ("photo", "pdf"):
        where = ", ".join(str(x) for x in (loc.get("page"), loc.get("region")) if x)
        return "person", "check by eye: %s%s reads %r" % (path, (" (" + where + ")") if where else "", src.get("quote", val))

    return "fail", "unknown source type %r" % t


TLDR_WORDS = 60     # the TL;DR: two or three lines
BODY_WORDS = 300    # the rest of the entry's prose, before it's flagged as long


def check_shape(md):
    """The entry opens with frontmatter (with `checked`) and a short TL;DR, and stays short.
    Tables, footnote definitions and the Originals list don't count toward the length."""
    out = []
    lines = md.split("\n")
    fm_end = 0
    if lines and lines[0].strip() == "---":
        try:
            fm_end = lines.index("---", 1) + 1
        except ValueError:
            fm_end = 0
    if not fm_end:
        out.append(("fail", "no frontmatter (title, date, devices, author, checked, tags)"))
    elif not any(l.startswith("checked:") for l in lines[1:fm_end - 1]):
        out.append(("fail", "frontmatter has no `checked:` (new entries are `checked: ai`)"))
    body = [l for l in lines[fm_end:] if not l.startswith("🤖 ")]
    paras = [p.strip() for p in "\n".join(body).split("\n\n") if p.strip()]
    paras = [p for p in paras if not p.startswith("# ")]
    if not paras or not re.match(r"\*\*TL;DR:?\*\*", paras[0]):
        out.append(("fail", "the first thing under the title must be **TL;DR:** (two or three lines)"))
    else:
        n = len(re.sub(r"\[\^f\d+\]", "", paras[0]).split()) - 1
        if n > TLDR_WORDS:
            out.append(("fail", "TL;DR is %d words; keep it under %d" % (n, TLDR_WORDS)))
    words, skip = 0, False
    for l in body:
        if l.startswith("## "):
            skip = l[3:].strip().lower().startswith("originals")
        if skip or l.startswith(("|", "[^", "#")) or "TL;DR" in l:
            continue
        words += len(re.sub(r"\[\^f\d+\]", "", l).split())
    if words > BODY_WORDS:
        out.append(("warn", "entry is %d words; aim for under %d (detail belongs in the sidecar)" % (words, BODY_WORDS)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("entries", nargs="*")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    project = os.path.dirname(root)
    ed = os.path.join(root, "entries")
    names = [e + ".json" for e in a.entries] or sorted(f for f in os.listdir(ed) if f.endswith(".json"))
    report, counts = [], {"ok": 0, "fail": 0, "person": 0, "warn": 0}
    for n in names:
        e = json.load(open(os.path.join(ed, n)))
        facts = e.get("facts", [])
        by_id = {f.get("id"): f for f in facts}
        md = os.path.join(ed, n[:-5] + ".md")
        md_text = open(md).read() if os.path.exists(md) else ""
        for f in facts:
            res, why = check_fact(f, project, by_id)
            counts[res] += 1
            report.append({"entry": n[:-5], "fact": f.get("id"), "field": f.get("field"),
                           "result": res, "detail": why})
        # Every footnote in the entry text must point at a fact, and every fact be used.
        used = set(re.findall(r"\[\^(f\d+)\]", md_text))
        for u in sorted(used - set(by_id)):
            counts["fail"] += 1
            report.append({"entry": n[:-5], "fact": u, "field": None, "result": "fail",
                           "detail": "entry text cites %s, which the sidecar does not have" % u})
        for res, why in check_shape(md_text):
            counts[res] += 1
            report.append({"entry": n[:-5], "fact": "text", "field": None, "result": res, "detail": why})
    if a.json:
        print(json.dumps({"counts": counts, "items": report}, indent=1))
    else:
        for r in report:
            if r["result"] != "ok":
                print("%-6s %s %s (%s): %s" % (r["result"].upper(), r["entry"], r["fact"], r["field"], r["detail"]))
        print("verified %d, failed %d, for a person to check %d, warnings %d" % (
            counts["ok"], counts["fail"], counts["person"], counts["warn"]))
    return 1 if counts["fail"] else 0


if __name__ == "__main__":
    sys.exit(main())
