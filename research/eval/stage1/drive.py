#!/usr/bin/env python3
"""Run exhaustive-mode reviews (three independent runs, then a merge) for stage 1, as headless
Claude Code sessions (`claude -p`) on the maintainer's plan, not through the API.

    python3 research/eval/stage1/drive.py v1.0 --set dev2 --engine engine
    python3 research/eval/stage1/drive.py v1.1 --set dev2 --engine research/eval/stage1/engine-v1.1 --parallel 8

For each paper version with a paper.pdf under runs/<arm>/<id>/<v1|accepted>/ (or, with --setup,
for each version in manifest.json, copying the PDF in), it writes runs/r1.md to r3.md, each
from a separate session that sees only the paper and the prompt, and then science-review.md
from a merge session that sees only the three runs. Existing files are skipped, so a stopped
run resumes. Each session follows the instructions in agents/science-reviewer.md and
agents/review-merger.md, with that version's science.md and merge.md.

The model and effort are those of the `claude` CLI's defaults unless --model is given; they are
recorded in runs/<arm>/drive.json.
"""
import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
AGENTS = ROOT / "agents"
LOCK = threading.Lock()


def body(agent_md):
    t = (AGENTS / agent_md).read_text()
    return re.sub(r"(?s)^---.*?---\s*", "", t)


def claude(prompt, cwd, model, log):
    cmd = ["claude", "-p", prompt, "--allowedTools", "Read", "Write", "Glob", "--permission-mode", "acceptEdits",
           "--add-dir", str(cwd), "--output-format", "text"]
    if model:
        cmd += ["--model", model]
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=3600)
        out = (r.stdout or "")[-500:] + (r.stderr or "")[-500:]
    except subprocess.TimeoutExpired:
        out = "TIMEOUT"
    with LOCK:
        with open(log, "a") as f:
            f.write(f"{datetime.datetime.now().isoformat(timespec='seconds')} {cwd.name}: {out.strip()[:300]}\n")
        print(f"  done {cwd.parent.name}/{cwd.name}: {out.strip()[:120]}", flush=True)


def review_job(vdir, k, engine, model, log):
    out = vdir / "runs" / f"r{k}.md"
    if out.exists():
        return
    prompt = (body("science-reviewer.md")
              + f"\n\n# This dispatch\n\n- Paper PDF: {vdir / 'paper.pdf'}\n- No supplementary information.\n"
              f"- Review prompt: {engine / 'science.md'}\n- Write your review to: {out}\n")
    claude(prompt, vdir, model, log)


def merge_job(vdir, engine, model, log):
    out = vdir / "science-review.md"
    runs = [vdir / "runs" / f"r{k}.md" for k in (1, 2, 3)]
    if out.exists() or not all(r.exists() for r in runs):
        return
    prompt = (body("review-merger.md")
              + f"\n\n# This dispatch\n\n- Reviews: r1 {runs[0]}, r2 {runs[1]}, r3 {runs[2]}\n"
              f"- Merge prompt: {engine / 'merge.md'}\n- Output: {out}\n")
    claude(prompt, vdir, model, log)


def setup(arm, set_name):
    man = json.loads((HERE / "manifest.json").read_text())
    for pid, v in sorted(man.items()):
        if v["set"] != set_name:
            continue
        for ver in ("v1", "accepted"):
            src = v.get(ver)
            if not src:
                continue
            d = HERE / "runs" / arm / pid / ver
            (d / "runs").mkdir(parents=True, exist_ok=True)
            if not (d / "paper.pdf").exists():
                shutil.copy(os.path.expanduser(src), d / "paper.pdf")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("arm")
    ap.add_argument("--set", default="dev2")
    ap.add_argument("--engine", default="engine")
    ap.add_argument("--model")
    ap.add_argument("--parallel", type=int, default=8)
    ap.add_argument("--setup", action="store_true", help="create folders and copy PDFs from manifest.json")
    ap.add_argument("--skip", nargs="*", default=[], help="id/version folders to leave alone (in progress elsewhere)")
    ap.add_argument("--only", nargs="*", help="id/version folders to run")
    a = ap.parse_args()
    engine = (ROOT / a.engine).resolve()
    if a.setup:
        setup(a.arm, a.set)
    ids = set(json.loads((HERE.parent / "referee" / "split.json").read_text())[a.set])
    base = HERE / "runs" / a.arm
    vdirs = [d for d in sorted(base.glob("*/*")) if d.parent.name in ids and (d / "paper.pdf").exists()
             and f"{d.parent.name}/{d.name}" not in a.skip
             and (not a.only or f"{d.parent.name}/{d.name}" in a.only)]
    meta = base / "drive.json"
    rec = json.loads(meta.read_text()) if meta.exists() else {}
    rec.update({"engine": str(engine.relative_to(ROOT)), "model": a.model or "claude CLI default",
                "runner": "claude -p (Claude Code headless, maintainer's plan)",
                "date": datetime.date.today().isoformat()})
    meta.write_text(json.dumps(rec, indent=1) + "\n")
    log = base / "drive.log"
    todo = [(d, k) for d in vdirs for k in (1, 2, 3) if not (d / "runs" / f"r{k}.md").exists()]
    print(f"{len(vdirs)} versions, {len(todo)} review runs to do", flush=True)
    with ThreadPoolExecutor(a.parallel) as ex:
        list(ex.map(lambda j: review_job(j[0], j[1], engine, a.model, log), todo))
    merges = [d for d in vdirs if not (d / "science-review.md").exists()]
    print(f"{len(merges)} merges to do", flush=True)
    with ThreadPoolExecutor(a.parallel) as ex:
        list(ex.map(lambda d: merge_job(d, engine, a.model, log), merges))
    left = [f"{d.parent.name}/{d.name}" for d in vdirs if not (d / "science-review.md").exists()]
    print("not finished:", left or "none", flush=True)


if __name__ == "__main__":
    sys.exit(main())
