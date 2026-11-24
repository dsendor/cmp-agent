#!/usr/bin/env python3
"""Re-merge existing runs with a different merge prompt, without new reviews: finding and tiering
measured separately (recall comes from the runs, tiers from the merge).

    python3 research/eval/stage1/remerge.py v1.2 --from v1.0 --engine research/eval/stage1/engine-v1.2
    python3 research/eval/stage1/remerge.py v1.2p --from v1.0 --engine research/eval/stage1/engine-v1.2 --paper

For each runs/<from>/<id>/<v1|accepted>/ with runs/r1.md to r3.md, a headless Claude Code session
(`claude -p`) merges the three runs with <engine>/merge.md and writes
runs/<arm>/<id>/<version>/science-review.md. The runs are read in place, not copied.

The merge prompt's {paper_check} is empty by default: the merger works from the reviews alone, as
agents/review-merger.md says. With --paper it may also read the paper, for the last check of the
A items only (does the paper already give evidence a reasonable referee would accept?).
"""
import argparse
import datetime
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
from drive import body, claude  # noqa: E402

PAPER_CHECK = (" For this check only, read the paper (its PDF path is in the dispatch) to see what evidence it"
               " gives. Never add a concern from the paper, and never drop or reword one because of it.")


def job(src, dst, engine, paper, model, log):
    out = dst / "science-review.md"
    runs = [src / "runs" / f"r{k}.md" for k in (1, 2, 3)]
    if out.exists() or not all(r.exists() for r in runs):
        return
    dst.mkdir(parents=True, exist_ok=True)
    prompt_file = dst / "merge-prompt.md"
    prompt_file.write_text((engine / "merge.md").read_text().replace("{paper_check}", PAPER_CHECK if paper else ""))
    agent = body("review-merger.md")
    if paper:
        agent = agent.replace("Work from the reviews alone; do not read the paper.",
                              "Work from the reviews; read the paper only for the check the prompt names.")
    prompt = (agent + f"\n\n# This dispatch\n\n- Reviews: r1 {runs[0]}, r2 {runs[1]}, r3 {runs[2]}\n"
              f"- Merge prompt: {prompt_file}\n- Output: {out}\n"
              + (f"- Paper PDF: {src / 'paper.pdf'}\n" if paper else ""))
    claude(prompt, HERE / "runs", model, log)  # one folder that holds both the runs and the output
    prompt_file.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arm")
    ap.add_argument("--from", dest="src", default="v1.0")
    ap.add_argument("--set", default="dev2")
    ap.add_argument("--engine", required=True)
    ap.add_argument("--paper", action="store_true")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--parallel", type=int, default=10)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    engine = (ROOT / a.engine).resolve()
    ids = set(json.loads((HERE.parent / "referee" / "split.json").read_text())[a.set])
    srcs = [d for d in sorted((HERE / "runs" / a.src).glob("*/*")) if d.parent.name in ids and (d / "runs").is_dir()
            and (not a.only or f"{d.parent.name}/{d.name}" in a.only)]
    base = HERE / "runs" / a.arm
    base.mkdir(parents=True, exist_ok=True)
    (base / "drive.json").write_text(json.dumps({
        "runs_from": a.src, "engine": str(engine.relative_to(ROOT)), "merge_reads_paper": a.paper, "model": a.model,
        "runner": "claude -p (Claude Code headless, maintainer's plan)", "date": datetime.date.today().isoformat()},
        indent=1) + "\n")
    log = base / "drive.log"
    print(f"{len(srcs)} merges", flush=True)
    with ThreadPoolExecutor(a.parallel) as ex:
        list(ex.map(lambda s: job(s, base / s.parent.name / s.name, engine, a.paper, a.model, log), srcs))
    left = [f"{s.parent.name}/{s.name}" for s in srcs if not (base / s.parent.name / s.name / "science-review.md").exists()]
    print("not finished:", left or "none", flush=True)


if __name__ == "__main__":
    sys.exit(main())
