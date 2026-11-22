#!/usr/bin/env python3
"""Tests for the project-advisor scripts. Standard library only.

  python3 project-advisor/tests/run_tests.py             offline tests on the made-up example
  python3 project-advisor/tests/run_tests.py --network   also one live arXiv search and count

The example (tests/example/advisor.json) is invented: four ideas with known properties.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "skills", "choose", "scripts")


def run(script, *args, ok=True):
    p = subprocess.run([sys.executable, os.path.join(SCRIPTS, script)] + list(args),
                       capture_output=True, text=True)
    if ok and p.returncode != 0:
        raise SystemExit("FAILED: %s %s\n%s%s" % (script, " ".join(args), p.stdout, p.stderr))
    return p


def check(cond, msg):
    if not cond:
        raise SystemExit("FAILED: " + msg)
    print("ok   " + msg)


def main():
    tmp = tempfile.mkdtemp(prefix="project-advisor-test-")
    try:
        shutil.copy(os.path.join(HERE, "example", "advisor.json"), tmp)
        adv = os.path.join(tmp, "advisor.json")
        run("decide.py", adv)
        d = json.load(open(os.path.join(tmp, "decision.json")))
        flags = {i["id"]: {f["kind"] for f in i["flags"]} for i in d["ideas"]}

        check(d["top"] == "thermal-mag", "top pick is the idea with the highest expected value")
        check(abs(sum(i["p_top"] for i in d["ideas"]) - 1) < 0.01, "shares on top sum to 1")
        check({"late_high_risk", "multiple_miracles", "past_horizon"} <= flags["trilayer-sc"],
              "trilayer idea gets late-high-risk, several-miracles and past-horizon flags")
        check("model_estimates" in flags["stack-auto"], "a model's estimate is flagged")
        check("early_go_no_go" in flags["thermal-mag"], "early go/no-go is recognized")
        check(len(d["pareto_front"]) == 4, "all four example ideas trade odds against impact")
        check(d["evpi"] >= max(v["evppi"] for v in d["value_of_information"]) - 1e-9,
              "value of perfect information bounds each partial value")

        first = open(os.path.join(tmp, "decision.json")).read()
        run("decide.py", adv)
        check(first == open(os.path.join(tmp, "decision.json")).read(), "results are reproducible")

        # A close call: make the second idea nearly as good and check the robustness test sees it.
        doc = json.load(open(adv))
        doc["ideas"][1]["estimates"]["impact"] = {"low": 6, "best": 7.5, "high": 9}
        close = os.path.join(tmp, "close")
        os.mkdir(close)
        json.dump(doc, open(os.path.join(close, "advisor.json"), "w"))
        run("decide.py", os.path.join(close, "advisor.json"))
        c = json.load(open(os.path.join(close, "decision.json")))
        check(not c["robust"] and c["flips"], "a close call is reported as not robust")
        check(c["value_of_information"][0]["p_changes_pick"] > 0.1,
              "a close call has an estimate worth learning")

        bad = json.load(open(adv))
        bad["ideas"][0]["estimates"]["p_success"]["high"] = 1.5
        del bad["ideas"][1]["estimates"]["months"]
        json.dump(bad, open(os.path.join(close, "advisor.json"), "w"))
        p = run("decide.py", os.path.join(close, "advisor.json"), ok=False)
        check(p.returncode != 0 and "between 0 and 1" in p.stderr and "months needs" in p.stderr,
              "bad estimates are rejected with a clear message")

        run("build_dashboard.py", tmp)
        page = open(os.path.join(tmp, "dashboard.html")).read()
        check("Local thermal transport" in page and "<svg" in page, "dashboard builds with the chart")
        check("model's guess" in page, "dashboard marks the model's estimates")
        check("AI-drafted" in page and "not judged by the model" in page, "dashboard labels AI work")
        check("\u2014" not in page, "no em dashes on the page")
        check("novel" not in page.lower(), "the page never calls an idea novel")
    finally:
        shutil.rmtree(tmp)

    if "--network" in sys.argv:
        p = run("search.py", "papers", 'abs:altermagnet AND abs:"anomalous Hall"', "--max", "3")
        res = json.loads(p.stdout)
        check(res["papers"] and res["papers"][0]["arxiv"], "arXiv search returns papers")
        p = run("search.py", "counts", "abs:altermagnet", "--from", "2023", "--to", "2024")
        res = json.loads(p.stdout)
        check(res["per_year"]["2024"] > res["per_year"]["2023"] > 0, "arXiv counts per year")
    print("all tests passed")


if __name__ == "__main__":
    main()
