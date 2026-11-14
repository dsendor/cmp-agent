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

        d = json.loads(run(rec, "dictate", "lab-record", "--text",
                           "Cooldown 3. Swept the gate on D7 from minus two to half a volt.", cwd=proj).stdout)
        photo = json.loads(run(rec, "add", "lab-record", "notebook-page.jpg", cwd=proj).stdout)[0]
        again = json.loads(run(rec, "add", "lab-record", "notebook-page.jpg", cwd=proj).stdout)[0]
        assert again["new"] is False and again["path"] == photo["path"], "same file stored twice"
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
        open(os.path.join(ed, eid + ".md"), "w").write("# D7\n\n12 mK[^f1], aborted[^f2], see[^f8].\n")

        p = run(ver, "lab-record", "--json", cwd=proj, ok=False)
        out = json.loads(p.stdout)
        failed = {i["fact"] for i in out["items"] if i["result"] == "fail"}
        person = {i["fact"] for i in out["items"] if i["result"] == "person"}
        assert p.returncode == 1, "verify should exit 1 on failures"
        assert failed == {"e1", "e2", "e3", "f8"}, "expected planted failures, got %s" % failed
        assert person == {"f5"}, person
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
        print("all lab-notes tests passed")
    finally:
        shutil.rmtree(proj, ignore_errors=True)


if __name__ == "__main__":
    main()
