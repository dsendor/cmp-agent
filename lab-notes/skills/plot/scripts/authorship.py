#!/usr/bin/env python3
"""Who wrote what in the lab record: the AI or a person. Standard library only.

The AI never relies on remembering. Every paragraph it writes is fingerprinted (sha256 of
the paragraph) in lab-record/authorship.json. A paragraph whose fingerprint the AI recorded
is the AI's; anything else is a person's (or was changed by one). So a person's edit is
noticed even if nobody says so, and the AI never mistakes its own text for a person's, as
long as its writes go through this script (or the Claude Code hook, which calls it).

Only the AI marks anything. People never tag their own text.

  authorship.py write  FILE [--text TEXT]   write FILE (content from --text or stdin) and
                                            record the paragraphs that are new as the AI's
  authorship.py before FILE                 snapshot FILE before the AI edits it another way
  authorship.py after  FILE                 record the paragraphs the AI just added
  authorship.py hook                        Claude Code PreToolUse/PostToolUse hook (stdin)
  authorship.py status ROOT [--json]        per file: ai, person or mixed; checked or not
  authorship.py mark   ROOT                 refresh the visible marks (below)
  authorship.py check  ROOT FILE --by NAME  a person read FILE and stands behind it
  authorship.py commit ROOT -m MESSAGE      git commit only what the AI wrote, as AI

ROOT is the lab-record folder. Visible marks, kept up to date by `mark`:
  - frontmatter `author: ai | person | mixed`, `checked: ai | human` (+ checked_by,
    checked_on), and the tag `ai` while any AI text remains;
  - in a mixed file only, each run of AI paragraphs sits between a line
    `🤖 AI YYYY-MM-DD` and a line `🤖 end`. Text outside those lines is a person's.
Marker lines and frontmatter never count toward a fingerprint, so marking changes nothing.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import date

LEDGER = "authorship.json"
MARK_RE = re.compile(r"^🤖 (AI \d{4}-\d{2}-\d{2}|end)\s*$")
TRAILER = "AI-Generated: lab-notes plugin"


# ---------- paragraphs and fingerprints ----------

def split_frontmatter(lines):
    """(frontmatter lines without the --- fences, or None; index of the first body line)."""
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[1:i], i + 1
    return None, 0


def blocks(text):
    """Paragraphs of the body as (first line, last line, fingerprint). Marker lines and
    frontmatter are skipped, so adding or removing marks never changes a fingerprint."""
    lines = text.split("\n")
    _, start = split_frontmatter(lines)
    out, cur = [], []

    def flush():
        if cur:
            body = "\n".join(lines[j].rstrip() for j in cur)
            out.append((cur[0], cur[-1], hashlib.sha256(body.encode()).hexdigest()[:16]))
            cur.clear()

    for i in range(start, len(lines)):
        ln = lines[i]
        if MARK_RE.match(ln.strip()):
            flush()
        elif ln.strip() == "":
            flush()
        else:
            cur.append(i)
    flush()
    return out


def hashes_of(path):
    if not os.path.exists(path):
        return []
    return [h for _, _, h in blocks(open(path, encoding="utf-8").read())]


# ---------- ledger ----------

def find_root(path):
    """The lab-record folder that contains path, or None."""
    d = os.path.dirname(os.path.abspath(path))
    while True:
        if os.path.basename(d) == "lab-record":
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def rel(root, path):
    return os.path.relpath(os.path.abspath(path), os.path.dirname(root))


def load(root):
    p = os.path.join(root, LEDGER)
    if os.path.exists(p):
        return json.load(open(p))
    return {"about": "Which paragraphs the AI wrote, by fingerprint. Kept by lab-notes; "
                     "see scripts/authorship.py.", "files": {}, "pending": {}}


def save(root, led):
    p = os.path.join(root, LEDGER)
    tmp = p + ".tmp"
    json.dump(led, open(tmp, "w"), indent=1, sort_keys=True)
    os.replace(tmp, p)


def entry(led, key):
    return led["files"].setdefault(key, {"ai": {}, "seen": [], "checked": None})


def claim(root, path, before, warn_if_guess=False):
    """Record paragraphs in path that were not in `before` as the AI's, today."""
    led = load(root)
    key = rel(root, path)
    e = entry(led, key)
    if before is None:  # no snapshot: best guess is everything changed since we last looked
        before = e["seen"]
        if warn_if_guess:
            print("authorship: no snapshot before this write to %s; paragraphs changed since the "
                  "last stamp are counted as the AI's" % key, file=sys.stderr)
    now = hashes_of(path)
    today = date.today().isoformat()
    new = [h for h in now if h not in set(before)]
    for h in new:
        e["ai"].setdefault(h, today)
    e["seen"] = now
    led["pending"].pop(key, None)
    save(root, led)
    return new


def classify(e, hs):
    ai = [h for h in hs if h in e["ai"]]
    if not hs:
        return "ai" if e["ai"] else "person"
    if len(ai) == len(hs):
        return "ai"
    return "mixed" if ai else "person"


# ---------- commands ----------

def cmd_write(a):
    root = find_root(a.file)
    if not root:
        sys.exit("not inside a lab-record folder: %s" % a.file)
    text = a.text if a.text is not None else sys.stdin.read()
    before = hashes_of(a.file)
    os.makedirs(os.path.dirname(os.path.abspath(a.file)), exist_ok=True)
    with open(a.file, "w", encoding="utf-8") as f:
        f.write(text if text.endswith("\n") else text + "\n")
    new = claim(root, a.file, before)
    print(json.dumps({"file": rel(root, a.file), "ai_paragraphs_added": len(new)}))


def cmd_before(a):
    root = find_root(a.file)
    if not root:
        return
    led = load(root)
    led["pending"][rel(root, a.file)] = hashes_of(a.file)
    save(root, led)


def cmd_after(a):
    root = find_root(a.file)
    if not root:
        return
    led = load(root)
    before = led["pending"].get(rel(root, a.file))
    claim(root, a.file, before, warn_if_guess=True)


def cmd_hook(_a):
    """Claude Code hook: PreToolUse snapshots, PostToolUse claims. Never blocks a tool."""
    try:
        ev = json.load(sys.stdin)
        path = (ev.get("tool_input") or {}).get("file_path") or ""
        if not path.endswith(".md") or not find_root(path):
            return
        ns = argparse.Namespace(file=path)
        if ev.get("hook_event_name") == "PreToolUse":
            cmd_before(ns)
        elif ev.get("hook_event_name") == "PostToolUse":
            cmd_after(ns)
    except Exception as err:  # a broken hook must never stop the work
        print("authorship hook: %s" % err, file=sys.stderr)


def file_status(root, led, key):
    path = os.path.join(os.path.dirname(root), key)
    if not os.path.exists(path):
        return None
    e = led["files"][key]
    hs = hashes_of(path)
    ai = sum(1 for h in hs if h in e["ai"])
    unseen = sum(1 for h in hs if h not in e["ai"] and h not in set(e["seen"]))
    ck = e.get("checked")
    checked = "human" if ck and sorted(ck.get("hashes", [])) == sorted(hs) else "ai"
    return {"file": key, "author": classify(e, hs), "ai_paragraphs": ai,
            "other_paragraphs": len(hs) - ai, "changed_since_last_look": unseen,
            "checked": checked, "checked_by": ck.get("by") if ck and checked == "human" else None,
            "changed_since_checked": bool(ck) and checked == "ai"}


def cmd_status(a):
    root = os.path.abspath(a.root)
    led = load(root)
    rows = [s for s in (file_status(root, led, k) for k in sorted(led["files"])) if s]
    if a.json:
        print(json.dumps(rows, indent=1))
        return
    for s in rows:
        extra = []
        if s["changed_since_last_look"]:
            extra.append("%d paragraph(s) changed by someone since the AI last looked" % s["changed_since_last_look"])
        if s["changed_since_checked"]:
            extra.append("changed since a person checked it")
        print("%-7s %-6s %s%s" % (s["author"], "human" if s["checked"] == "human" else "AI only",
                                  s["file"], ("  (" + "; ".join(extra) + ")") if extra else ""))


def set_frontmatter(lines, fields, tag_ai):
    fm, start = split_frontmatter(lines)
    fm = list(fm) if fm is not None else []
    keys = [l.split(":", 1)[0].strip() for l in fm]
    for k, v in fields.items():
        line = "%s:" % k if v is None else "%s: %s" % (k, v)
        if k in keys:
            fm[keys.index(k)] = line
        else:
            fm.append(line)
            keys.append(k)
    tags = []
    if "tags" in keys:
        raw = fm[keys.index("tags")].split(":", 1)[1].strip()
        tags = [t.strip() for t in raw.strip("[]").split(",") if t.strip()]
    tags = [t for t in tags if t != "ai"]
    if tag_ai:
        tags.insert(0, "ai")
    line = "tags: [%s]" % ", ".join(tags)
    if "tags" in keys:
        fm[keys.index("tags")] = line
    else:
        fm.append(line)
    return ["---"] + fm + ["---"] + lines[start:]


def squeeze(lines):
    """No more than one blank line in a row, so adding and removing marks never piles up
    empty lines."""
    out = []
    for l in lines:
        if l.strip() == "" and out and out[-1].strip() == "":
            continue
        out.append(l)
    return out


def render(text, e, checked_fields):
    """Frontmatter fields, and 🤖 markers around AI paragraphs when the file is mixed."""
    lines = squeeze([l for l in text.split("\n") if not MARK_RE.match(l.strip())])
    hs = blocks("\n".join(lines))
    kind = classify(e, [h for _, _, h in hs])
    if kind == "mixed":
        out, i, n = [], 0, len(lines)
        idx = 0
        _, start = split_frontmatter(lines)
        out = lines[:start]
        i = start
        while idx < len(hs):
            a0, a1, h = hs[idx]
            out.extend(lines[i:a0])
            if h in e["ai"]:
                run_end, day = idx, e["ai"][h]
                while run_end + 1 < len(hs) and hs[run_end + 1][2] in e["ai"]:
                    run_end += 1
                    day = min(day, e["ai"][hs[run_end][2]])
                last = hs[run_end][1]
                out.extend(["", "🤖 AI %s" % day, ""] + lines[a0:last + 1] + ["", "🤖 end", ""])
                i, idx = last + 1, run_end + 1
            else:
                out.extend(lines[a0:a1 + 1])
                i, idx = a1 + 1, idx + 1
        out.extend(lines[i:n])
        lines = out
    fields = dict(author=kind, **checked_fields)
    lines = set_frontmatter(squeeze(lines), fields, tag_ai=kind != "person")
    return "\n".join(lines)


def mark_file(root, led, key):
    path = os.path.join(os.path.dirname(root), key)
    if not os.path.exists(path):
        return False
    e = led["files"][key]
    st = file_status(root, led, key)
    ck = e.get("checked") or {}
    fields = {"checked": st["checked"],
              "checked_by": ck.get("by") if st["checked"] == "human" else None,
              "checked_on": ck.get("on") if st["checked"] == "human" else None}
    old = open(path, encoding="utf-8").read()
    new = render(old, e, fields)
    if new != old:
        open(path, "w", encoding="utf-8").write(new)
    e["seen"] = hashes_of(path)
    return new != old


def cmd_mark(a):
    root = os.path.abspath(a.root)
    led = load(root)
    changed = [k for k in sorted(led["files"]) if mark_file(root, led, k)]
    save(root, led)
    print("marks refreshed in %d file(s)" % len(changed))


def cmd_check(a):
    root = os.path.abspath(a.root)
    led = load(root)
    key = rel(root, a.file)
    e = entry(led, key)
    e["checked"] = {"by": a.by, "on": date.today().isoformat(), "hashes": hashes_of(a.file)}
    mark_file(root, led, key)
    e["checked"]["hashes"] = hashes_of(a.file)
    save(root, led)
    print("%s checked by %s" % (key, a.by))


def git(project, *args, ok=True):
    p = subprocess.run(["git", "-C", project] + list(args), capture_output=True, text=True)
    if ok and p.returncode != 0:
        sys.exit("git %s failed: %s" % (" ".join(args), p.stderr.strip()))
    return p


def cmd_commit(a):
    """Stage only what the AI wrote and commit it marked as AI. A Markdown file with any
    paragraph the AI didn't write since the last commit is left for the person."""
    root = os.path.abspath(a.root)
    project = os.path.dirname(root)
    if git(project, "rev-parse", "--show-toplevel", ok=False).returncode != 0:
        sys.exit("not a git repository; nothing committed")
    top = git(project, "rev-parse", "--show-toplevel").stdout.strip()
    led = load(root)
    out = git(project, "status", "--porcelain=v1", "-uall", "--", root).stdout.splitlines()
    take, hold = [], []
    for line in out:
        code, path = line[:2], line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        full = os.path.join(top, path)
        key = rel(root, full)
        if "D" in code:
            hold.append((key, "deleted"))
            continue
        if not full.endswith(".md"):
            take.append(full)
            continue
        e = led["files"].get(key)
        if not e:
            hold.append((key, "not written by the AI"))
            continue
        head = git(project, "show", "HEAD:%s" % os.path.relpath(full, top), ok=False)
        before = set(h for _, _, h in blocks(head.stdout)) if head.returncode == 0 else set()
        foreign = [h for h in hashes_of(full) if h not in before and h not in e["ai"]]
        if foreign:
            hold.append((key, "%d paragraph(s) by a person" % len(foreign)))
        else:
            take.append(full)
    if take:
        git(project, "add", "--", *take)
        git(project, "commit", "-q", "-m", "🤖 lab-notes: %s\n\n%s" % (a.message, TRAILER), "--", *take)
    print(json.dumps({"committed": [rel(root, t) for t in take],
                      "left_for_the_person": [{"file": k, "why": w} for k, w in hold]}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("write"); p.add_argument("file"); p.add_argument("--text"); p.set_defaults(fn=cmd_write)
    p = sub.add_parser("before"); p.add_argument("file"); p.set_defaults(fn=cmd_before)
    p = sub.add_parser("after"); p.add_argument("file"); p.set_defaults(fn=cmd_after)
    p = sub.add_parser("hook"); p.set_defaults(fn=cmd_hook)
    p = sub.add_parser("status"); p.add_argument("root"); p.add_argument("--json", action="store_true"); p.set_defaults(fn=cmd_status)
    p = sub.add_parser("mark"); p.add_argument("root"); p.set_defaults(fn=cmd_mark)
    p = sub.add_parser("check"); p.add_argument("root"); p.add_argument("file"); p.add_argument("--by", required=True); p.set_defaults(fn=cmd_check)
    p = sub.add_parser("commit"); p.add_argument("root"); p.add_argument("-m", "--message", required=True); p.set_defaults(fn=cmd_commit)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
