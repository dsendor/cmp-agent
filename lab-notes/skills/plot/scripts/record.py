#!/usr/bin/env python3
"""Housekeeping for the lab record (see docs/record-format.md). Standard library only.

  record.py init     ROOT [--lab NAME] [--project NAME]
  record.py add      ROOT FILE [FILE ...]      copy inputs into originals/, print path + sha256
  record.py dictate  ROOT [--text TEXT]        save dictated text (or stdin) as an original
  record.py attachment ROOT --name NAME [--text TEXT]
                                               save the transcription of a chat attachment that
                                               has no file (the image itself can't be kept)
  record.py new-id   ROOT TITLE                print a fresh entry id: YYYY-MM-DD-HHMM-slug
  record.py index    ROOT                      rebuild index.json from entry sidecars
  record.py inbox    ROOT                      list files waiting in inbox/

ROOT is the lab-record folder. Originals are append-only: add never overwrites.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

README = """# Lab record

Written and kept by the lab-notes plugin. Plain files: read them without any tool.

- `originals/`: photos, dictation, notes and files exactly as they came in. Never edited.
- `entries/`: one entry per session, idea or meeting. The `.md` is for reading; the `.json`
  beside it lists every fact and the original it came from.
- `inbox/`: drop files here (from a phone, a shared folder) to be turned into entries.
- `devices/`, `timeline.md`, `open-questions.md`: pages for browsing (open this folder in
  Obsidian), rebuilt from the entries. Don't edit them.
- `index.json`, `authorship.json`: kept by the plugin. `authorship.json` records which
  paragraphs the AI wrote, so its text is marked and a person's edits are noticed.

Entries are drafted by AI. Each file's `author` and `checked` properties say who wrote it and
whether a person has checked it; in a file with both, the AI's text sits between `🤖 AI` and
`🤖 end` lines.
"""


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def slug(s, n=40):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].rstrip("-") or "entry"


def cmd_init(a):
    root = a.root
    for d in ("originals", "entries", "inbox"):
        os.makedirs(os.path.join(root, d), exist_ok=True)
    cfg = os.path.join(root, "config.json")
    if not os.path.exists(cfg):
        json.dump({
            "lab": a.lab or "", "project": a.project or "", "people": [],
            "qcodes_dbs": [], "data_dirs": [], "eln": None, "auto_commit": False,
            "notes": "Edit freely. qcodes_dbs and data_dirs are paths relative to the project.",
        }, open(cfg, "w"), indent=2)
    rd = os.path.join(root, "README.md")
    if not os.path.exists(rd):
        open(rd, "w").write(README)
    gi = os.path.join(root, "inbox", ".gitkeep")
    open(gi, "a").close()
    print(json.dumps({"root": os.path.abspath(root), "config": cfg}))


def add_original(root, src, name=None):
    digest = sha256(src)
    base = name or os.path.basename(src)
    day = datetime.now().strftime("%Y-%m-%d")
    dest = os.path.join(root, "originals", "%s-%s-%s" % (day, digest[:8], slug(os.path.splitext(base)[0], 60) + os.path.splitext(base)[1].lower()))
    # Same content already stored? Reuse it.
    for f in os.listdir(os.path.join(root, "originals")):
        if digest[:8] in f:
            p = os.path.join(root, "originals", f)
            if sha256(p) == digest:
                return {"path": os.path.relpath(p, os.path.dirname(os.path.abspath(root))), "sha256": digest, "new": False}
    if os.path.exists(dest):
        sys.exit("refusing to overwrite %s" % dest)
    shutil.copy2(src, dest)
    os.chmod(dest, 0o444)
    return {"path": os.path.relpath(dest, os.path.dirname(os.path.abspath(root))), "sha256": digest, "new": True}


def cmd_add(a):
    out = []
    for f in a.files:
        if not os.path.isfile(f):
            sys.exit("not a file: %s" % f)
        out.append(dict(add_original(a.root, f), source=f))
    print(json.dumps(out, indent=1))


def cmd_dictate(a):
    text = a.text if a.text is not None else sys.stdin.read()
    if not text.strip():
        sys.exit("no text")
    stamp = datetime.now().strftime("%H%M%S")
    tmp = os.path.join(a.root, "inbox", ".dictation-%s.txt" % stamp)
    with open(tmp, "w") as f:
        f.write(text.rstrip() + "\n")
    try:
        r = add_original(a.root, tmp, name="dictation-%s.txt" % stamp)
    finally:
        os.remove(tmp)
    print(json.dumps(r))


def cmd_attachment(a):
    text = a.text if a.text is not None else sys.stdin.read()
    if not text.strip():
        sys.exit("no text")
    stamp = datetime.now().strftime("%H%M%S")
    tmp = os.path.join(a.root, "inbox", ".attachment-%s.txt" % stamp)
    with open(tmp, "w") as f:
        f.write("Transcription of a chat attachment (the image itself was not kept): %s\n\n" % a.name)
        f.write(text.rstrip() + "\n")
    try:
        r = add_original(a.root, tmp, name="attachment-%s-%s.txt" % (slug(a.name, 30), stamp))
    finally:
        os.remove(tmp)
    print(json.dumps(r))


def cmd_new_id(a):
    eid = "%s-%s" % (datetime.now().strftime("%Y-%m-%d-%H%M"), slug(a.title))
    n, base = 2, eid
    while os.path.exists(os.path.join(a.root, "entries", eid + ".json")):
        eid = "%s-%d" % (base, n); n += 1
    print(eid)


def cmd_index(a):
    ed = os.path.join(a.root, "entries")
    entries, devices, runs, questions, unconfirmed = [], {}, [], [], 0
    for f in sorted(os.listdir(ed)):
        if not f.endswith(".json"):
            continue
        try:
            e = json.load(open(os.path.join(ed, f)))
        except ValueError as err:
            print("skipping unreadable %s: %s" % (f, err), file=sys.stderr)
            continue
        eid = e.get("id", f[:-5])
        confirmed = {c.get("fact") for c in e.get("confirmed", [])}
        facts = e.get("facts", [])
        unconfirmed += sum(1 for x in facts if x.get("id") not in confirmed and x.get("status") in ("stated", "inferred"))
        entries.append({"id": eid, "kind": e.get("kind"), "created": e.get("created"),
                        "title": e.get("title"), "devices": e.get("devices", []),
                        "facts": len(facts), "failures": len(e.get("failures", [])),
                        "open_questions": len(e.get("questions", []))})
        for d in e.get("devices", []):
            devices.setdefault(d, []).append(eid)
        for r in e.get("runs", []):
            runs.append(dict(r, entry=eid))
        for q in e.get("questions", []):
            questions.append({"entry": eid, "question": q})
    idx = {"rebuilt": datetime.now().isoformat(timespec="seconds"), "entries": entries,
           "devices": devices, "runs": runs, "open_questions": questions,
           "facts_awaiting_confirmation": unconfirmed}
    json.dump(idx, open(os.path.join(a.root, "index.json"), "w"), indent=1)
    skipped = hub_pages(a.root, entries, devices, questions)
    import authorship
    led = authorship.load(os.path.abspath(a.root))
    for k in sorted(led["files"]):
        authorship.mark_file(os.path.abspath(a.root), led, k)
    authorship.save(os.path.abspath(a.root), led)
    print("%d entries, %d devices, %d runs, %d open questions, %d facts awaiting confirmation" % (
        len(entries), len(devices), len(runs), len(questions), unconfirmed))
    for f in skipped:
        print("not overwritten (a person edited it): %s" % f)


def tldr_of(root, eid):
    """The entry's TL;DR line, without the label, or ''."""
    p = os.path.join(root, "entries", eid + ".md")
    if not os.path.exists(p):
        return ""
    m = re.search(r"\*\*TL;DR:?\*\*:?\s*(.+)", open(p, encoding="utf-8").read())
    return re.sub(r"\[\^f\d+\]", "", m.group(1)).strip() if m else ""


def hub_pages(root, entries, devices, questions):
    """Pages for browsing in Obsidian or anywhere markdown renders: one per device, a
    timeline and every open question. Generated, so never edited by hand; a page a person
    did edit is left alone and reported."""
    import authorship
    root = os.path.abspath(root)
    led = authorship.load(root)
    newest = sorted(entries, key=lambda e: e.get("created") or e["id"], reverse=True)
    by_id = {e["id"]: e for e in entries}
    head = "*Generated by lab-notes from the entries; rebuilt each time, so don't edit it.*"

    def link(eid, up):
        e = by_id.get(eid, {})
        return "[%s](%sentries/%s.md)" % (e.get("title") or eid, up, eid)

    def fm(title, tag):
        return "---\ntitle: %s\ngenerated: true\ntags: [%s]\n---\n" % (title, tag)

    pages = {}
    for d, eids in sorted(devices.items()):
        es = [by_id[x] for x in eids if x in by_id]
        es.sort(key=lambda e: e.get("created") or e["id"], reverse=True)
        qs = [q for q in questions if q["entry"] in eids]
        dates = sorted((e.get("created") or "")[:10] for e in es if e.get("created"))
        span = (" from %s to %s" % (dates[0], dates[-1])) if dates else ""
        body = [fm(d, "device"), "# %s" % d, "", head, "",
                "**TL;DR:** %d entr%s%s; %d open question%s." % (
                    len(es), "y" if len(es) == 1 else "ies", span, len(qs), "" if len(qs) == 1 else "s"),
                "", "## Entries", ""]
        body += ["- %s %s%s" % ((e.get("created") or "")[:10], link(e["id"], "../"),
                                (": " + tldr_of(root, e["id"])) if tldr_of(root, e["id"]) else "") for e in es]
        if qs:
            body += ["", "## Open questions", ""] + ["- %s (%s)" % (q["question"], link(q["entry"], "../")) for q in qs]
        pages[os.path.join(root, "devices", "%s.md" % slug(d, 60))] = "\n".join(body)
    tl = [fm("Timeline", "index"), "# Timeline", "", head, "",
          "**TL;DR:** %d entries, newest first. Devices: %s." % (
              len(entries), ", ".join("[%s](devices/%s.md)" % (d, slug(d, 60)) for d in sorted(devices)) or "none"),
          ""]
    tl += ["- %s %s%s" % ((e.get("created") or "")[:10], link(e["id"], ""),
                          (": " + tldr_of(root, e["id"])) if tldr_of(root, e["id"]) else "") for e in newest]
    pages[os.path.join(root, "timeline.md")] = "\n".join(tl)
    oq = [fm("Open questions", "index"), "# Open questions", "", head, "",
          "**TL;DR:** %d open, across %d entr%s. Answer any of them in a note and they close." % (
              len(questions), len({q["entry"] for q in questions}),
              "y" if len({q["entry"] for q in questions}) == 1 else "ies"), ""]
    for e in newest:
        qs = [q["question"] for q in questions if q["entry"] == e["id"]]
        if qs:
            oq += ["## %s" % link(e["id"], ""), ""] + ["- %s" % q for q in qs] + [""]
    pages[os.path.join(root, "open-questions.md")] = "\n".join(oq)

    skipped = []
    for path, text in pages.items():
        key = authorship.rel(root, path)
        if os.path.exists(path):
            e = led["files"].get(key)
            if not e or any(h not in e["ai"] for h in authorship.hashes_of(path)):
                skipped.append(key)
                continue
        before = authorship.hashes_of(path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(text + "\n")
        authorship.claim(root, path, before)
        led = authorship.load(root)
    return skipped


def cmd_inbox(a):
    ib = os.path.join(a.root, "inbox")
    files = [f for f in sorted(os.listdir(ib)) if not f.startswith(".")]
    print(json.dumps([{"path": os.path.join(ib, f), "bytes": os.path.getsize(os.path.join(ib, f))} for f in files], indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init"); p.add_argument("root"); p.add_argument("--lab"); p.add_argument("--project"); p.set_defaults(fn=cmd_init)
    p = sub.add_parser("add"); p.add_argument("root"); p.add_argument("files", nargs="+"); p.set_defaults(fn=cmd_add)
    p = sub.add_parser("dictate"); p.add_argument("root"); p.add_argument("--text"); p.set_defaults(fn=cmd_dictate)
    p = sub.add_parser("attachment"); p.add_argument("root"); p.add_argument("--name", required=True); p.add_argument("--text"); p.set_defaults(fn=cmd_attachment)
    p = sub.add_parser("new-id"); p.add_argument("root"); p.add_argument("title"); p.set_defaults(fn=cmd_new_id)
    p = sub.add_parser("index"); p.add_argument("root"); p.set_defaults(fn=cmd_index)
    p = sub.add_parser("inbox"); p.add_argument("root"); p.set_defaults(fn=cmd_inbox)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
