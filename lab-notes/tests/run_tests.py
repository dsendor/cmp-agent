#!/usr/bin/env python3
"""End-to-end test of the lab-notes scripts on a simulated QCoDeS database. Standard library only.

  python3 lab-notes/tests/run_tests.py

Builds a throwaway project with fixtures/simulated.db (made by make_test_db.py: three gate
sweeps on a pretend device D7, run 2 aborted), a dictation, a CSV and a photo, writes an
entry with three planted errors, and checks the verifier finds exactly those.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")


def run(*args, cwd, ok=True):
    p = subprocess.run([sys.executable] + list(args), cwd=cwd, capture_output=True, text=True)
    if ok and p.returncode != 0:
        raise SystemExit("FAILED: %s\n%s%s" % (" ".join(args), p.stdout, p.stderr))
    return p


def main():
    run(os.path.join(HERE, "sync_skills.py"), "--check", cwd=HERE)
    proj = tempfile.mkdtemp(prefix="lab-notes-test-")
    try:
        os.makedirs(os.path.join(proj, "data"))
        shutil.copy(os.path.join(HERE, "fixtures", "simulated.db"), os.path.join(proj, "data", "experiments.db"))
        with open(os.path.join(proj, "data", "iv.csv"), "w") as f:
            f.write("V_bias,I\n0.0,0.0\n0.001,2.5e-9\n")
        with open(os.path.join(proj, "notebook-page.jpg"), "wb") as f:
            f.write(b"\xff\xd8 not really a photo")

        rec = os.path.join(SCRIPTS, "record.py")
        ver = os.path.join(SCRIPTS, "verify.py")
        qc = os.path.join(SCRIPTS, "qcodes_runs.py")

        run(rec, "init", "lab-record", cwd=proj)
        listing = run(qc, "list", "data/experiments.db", cwd=proj).stdout
        assert "ABORTED" in listing and listing.count("gate_sweep") == 3, listing
        diff = json.loads(run(qc, "diff", "data/experiments.db", "1", "3", "--json", cwd=proj).stdout)
        assert {c["setting"] for c in diff} >= {"magnet.B", "lockin.time_constant"}, diff
        assert not os.path.exists(os.path.join(proj, "data", "experiments.db-wal")), "reader wrote to the database"
        before = open(os.path.join(proj, "data", "experiments.db"), "rb").read()
        cp = run(qc, "copy", "data/experiments.db", "--to", os.path.join(proj, "tmpcopy"), cwd=proj).stdout.strip()
        assert "ABORTED" in run(qc, "list", cp, cwd=proj).stdout, "copy lost the runs"
        assert open(os.path.join(proj, "data", "experiments.db"), "rb").read() == before, "copy changed the original"
        assert run(qc, "copy", "data/experiments.db", "--to", os.path.join(proj, "tmpcopy"), cwd=proj, ok=False).returncode != 0, "copy overwrote"

        d = json.loads(run(rec, "dictate", "lab-record", "--text",
                           "Cooldown 3. Swept the gate on D7 from minus two to half a volt.", cwd=proj).stdout)
        photo = json.loads(run(rec, "add", "lab-record", "notebook-page.jpg", cwd=proj).stdout)[0]
        again = json.loads(run(rec, "add", "lab-record", "notebook-page.jpg", cwd=proj).stdout)[0]
        assert again["new"] is False and again["path"] == photo["path"], "same file stored twice"
        att = json.loads(run(rec, "attachment", "lab-record", "--name", "notebook page 2", "--text",
                             "Cooldown 3, D7, Vg sweep -2..0.5 V, B = 0.5 T", cwd=proj).stdout)
        eid = run(rec, "new-id", "lab-record", "D7 gate sweeps", cwd=proj).stdout.strip()

        db = {"type": "qcodes", "path": "data/experiments.db"}
        dic = {"type": "dictation", "path": d["path"], "sha256": d["sha256"]}
        facts = [
            {"id": "f1", "field": "T_mc", "value": 12, "unit": "mK", "status": "instrument",
             "source": dict(db, locator={"run_id": 1, "parameter": "fridge.T_mc"})},
            {"id": "f2", "field": "run 2 aborted", "value": True, "unit": "1", "status": "instrument",
             "source": dict(db, locator={"run_id": 2, "parameter": "aborted"})},
            {"id": "f3", "field": "gate range", "value": "-2 to 0.5", "unit": "V", "status": "stated",
             "source": dict(dic, quote="from minus two to half a volt")},
            {"id": "f4", "field": "current at 1 mV", "value": 2.5, "unit": "nA", "status": "instrument",
             "source": {"type": "file", "path": "data/iv.csv", "locator": {"row": 3, "column": "I", "unit": "A"}}},
            {"id": "f5", "field": "sample on page", "value": "D7", "status": "stated",
             "source": {"type": "photo", "path": photo["path"], "sha256": photo["sha256"],
                        "locator": {"page": 1, "region": "top left"}, "quote": "D7"}},
            {"id": "f8", "field": "field on page 2", "value": 0.5, "unit": "T", "status": "stated",
             "source": {"type": "attachment", "path": att["path"], "sha256": att["sha256"], "quote": "B = 0.5 T"}},
            {"id": "f6", "field": "lock-in amplitude", "value": None, "status": "not recorded",
             "source": {"type": "dictation", "path": d["path"]}},
            {"id": "f7", "field": "base temperature, K", "value": 0.012, "unit": "K", "status": "inferred",
             "source": {"type": "inferred", "from": ["f1"], "reason": "unit conversion"}},
            # Planted errors:
            {"id": "e1", "field": "time constant run 3", "value": 100, "unit": "ms", "status": "instrument",
             "source": dict(db, locator={"run_id": 3, "parameter": "lockin.time_constant"})},
            {"id": "e2", "field": "cooldown", "value": 3, "unit": "1", "status": "stated",
             "source": dict(dic, quote="Cooldown three")},
            {"id": "e3", "field": "field", "value": 0.5, "status": "instrument",
             "source": dict(db, locator={"run_id": 3, "parameter": "magnet.B"})},
        ]
        ed = os.path.join(proj, "lab-record", "entries")
        json.dump({"id": eid, "kind": "session", "devices": ["D7"], "facts": facts,
                   "questions": ["Lock-in amplitude?"]}, open(os.path.join(ed, eid + ".json"), "w"))
        open(os.path.join(ed, eid + ".md"), "w").write(
            "---\ntitle: D7\nchecked: ai\ntags: [d7]\n---\n# D7\n\n**TL;DR:** Two sweeps; run 2 crashed.\n\n"
            "12 mK[^f1], aborted[^f2], see[^f9].\n")

        p = run(ver, "lab-record", "--json", cwd=proj, ok=False)
        out = json.loads(p.stdout)
        failed = {i["fact"] for i in out["items"] if i["result"] == "fail"}
        person = {i["fact"] for i in out["items"] if i["result"] == "person"}
        assert p.returncode == 1, "verify should exit 1 on failures"
        assert failed == {"e1", "e2", "e3", "f9"}, "expected planted failures, got %s" % failed
        assert person == {"f5", "f8"}, person
        assert out["counts"]["ok"] == 6, out["counts"]

        # Changing an original after it was cited must be caught.
        orig = os.path.join(proj, d["path"])
        os.chmod(orig, 0o644)
        open(orig, "a").write("edited later\n")
        out2 = json.loads(run(ver, "lab-record", "--json", cwd=proj, ok=False).stdout)
        assert any("changed since" in i["detail"] for i in out2["items"] if i["fact"] == "f3"), "edit not caught"

        run(rec, "index", "lab-record", cwd=proj)
        idx = json.load(open(os.path.join(proj, "lab-record", "index.json")))
        assert idx["devices"] == {"D7": [eid]} and len(idx["open_questions"]) == 1

        authorship_tests(proj, eid)
        print("all lab-notes tests passed")
    finally:
        shutil.rmtree(proj, ignore_errors=True)


def authorship_tests(proj, eid):
    au = os.path.join(SCRIPTS, "authorship.py")
    ver = os.path.join(SCRIPTS, "verify.py")
    rec = os.path.join(SCRIPTS, "record.py")
    root = os.path.join(proj, "lab-record")
    md = os.path.join("lab-record", "entries", eid + ".md")
    status = lambda: {r["file"]: r for r in json.loads(run(au, "status", "lab-record", "--json", cwd=proj).stdout)}

    # Hub pages for browsing: one per device, a timeline, the open questions; marked as AI.
    for page in ("devices/D7.md", "timeline.md", "open-questions.md"):
        text = open(os.path.join(root, page)).read()
        assert "**TL;DR:**" in text and "author: ai" in text and "tags: [ai" in text, page
    assert "entries/%s.md" % eid in open(os.path.join(root, "devices", "D7.md")).read()

    # The entry was written by hand above (not through the script): the AI writes it again
    # through authorship.py, so its paragraphs are the AI's.
    text = open(os.path.join(proj, md)).read()
    os.remove(os.path.join(proj, md))  # rewriting identical text would (rightly) claim nothing
    run(au, "write", md, "--text", text, cwd=proj)
    assert status()[md]["author"] == "ai"

    # A person adds a line. Nobody tags it; it is noticed.
    open(os.path.join(proj, md), "a").write("\nContact 3 is flaky again, use 1 and 4.\n")
    s = status()[md]
    assert s["author"] == "mixed" and s["changed_since_last_look"] == 1, s

    # Marks: AI text between robot lines, the person's line unmarked, fingerprints unchanged.
    run(au, "mark", "lab-record", cwd=proj)
    marked = open(os.path.join(proj, md)).read()
    assert "🤖 AI " in marked and "🤖 end" in marked and "author: mixed" in marked
    after_ai = marked.split("🤖 end")[-1]
    assert "Contact 3 is flaky" in after_ai, "the person's line should be outside the AI block"
    assert status()[md]["author"] == "mixed"
    run(au, "mark", "lab-record", cwd=proj)
    assert open(os.path.join(proj, md)).read() == marked, "marking twice must change nothing"

    # The Claude Code hook: snapshot before, claim after.
    hook = lambda ev: subprocess.run([sys.executable, au, "hook"], cwd=proj, text=True, capture_output=True,
                                     input=json.dumps({"hook_event_name": ev, "tool_input": {"file_path": os.path.join(proj, md)}}))
    hook("PreToolUse")
    open(os.path.join(proj, md), "a").write("\nThe peak may track the field.\n")
    hook("PostToolUse")
    s = status()[md]
    assert s["ai_paragraphs"] >= 4 and s["other_paragraphs"] == 1, s

    # Checked by a person; any later change returns it to AI only.
    run(au, "check", "lab-record", md, "--by", "Matan", cwd=proj)
    assert status()[md]["checked"] == "human" and "checked: human" in open(os.path.join(proj, md)).read()
    open(os.path.join(proj, md), "a").write("\nOne more thing.\n")
    s = status()[md]
    assert s["checked"] == "ai" and s["changed_since_checked"], s

    # The verifier wants frontmatter and a short TL;DR first.
    bad = os.path.join(root, "entries", eid + ".md")
    keep = open(bad).read()
    open(bad, "w").write("# D7\n\n12 mK[^f1], aborted[^f2].\n")
    out = json.loads(run(ver, "lab-record", eid, "--json", cwd=proj, ok=False).stdout)
    why = " ".join(i["detail"] for i in out["items"] if i["fact"] == "text")
    assert "frontmatter" in why and "TL;DR" in why, why
    open(bad, "w").write(keep)

    # git: the AI commits only what it wrote, marked as AI; a person's edit is left alone.
    if shutil.which("git"):
        g = lambda *a: subprocess.run(["git", "-C", proj] + list(a), capture_output=True, text=True)
        g("init", "-q"); g("config", "user.email", "t@example.org"); g("config", "user.name", "Tester")
        g("add", "-A"); g("commit", "-qm", "start")
        other = os.path.join("lab-record", "entries", "idea.md")
        run(au, "write", other, "--text", "---\nchecked: ai\n---\n# Idea\n\n**TL;DR:** Try a back gate.\n", cwd=proj)
        open(os.path.join(proj, md), "a").write("\nA person wrote this.\n")
        res = json.loads(run(au, "commit", "lab-record", "-m", "idea", cwd=proj).stdout)
        assert other in res["committed"] and md in [x["file"] for x in res["left_for_the_person"]], res
        msg = g("log", "-1", "--format=%B").stdout
        assert msg.startswith("🤖 lab-notes: idea") and "AI-Generated: lab-notes plugin" in msg, msg
        assert md in g("status", "--porcelain").stdout, "the person's edit should stay uncommitted"

    # A hub page a person edited is not overwritten.
    page = os.path.join(root, "timeline.md")
    open(page, "a").write("\nMy own note on the timeline.\n")
    out = run(rec, "index", "lab-record", cwd=proj).stdout
    assert "not overwritten" in out and "My own note" in open(page).read(), out


if __name__ == "__main__":
    main()
