# Status: what is in progress and what is next

Agents keep this page current. Update it at the end of a piece of work: move finished items
out, add what you learned that the next session needs. History belongs in git, not here.

## Released

- Version 0.2.0 (`.claude-plugin/plugin.json`): review, apply and contribute commands; the
  dashboard with triage, walk-through, PDF pane, and an optional version comparison page.

## In progress

- Publishing a dashboard as a Claude artifact, as an option after the review, so it can be
  shared as a link. The local `dashboard.html` stays the default.

- Comparing versions after peer review (`/referee-preview:compare`, `docs/revisions.md`):
  a blind review of the revision, inferred referee requests, a Referee feedback view and a
  revision record. Tried once, on a private revision. Next: validate the inference on the
  papers in `research/eval/referee/` whose reports are public, then collect public records
  in `research/eval/revisions/`.

- **Stage 1 corpus** (`research/corpus/`): built and checked against `EVALUATION.md` (recall
  reproduces). The reserve is split into dev2 and test2 (27 each, `split.py --split-reserve`);
  test2 is held out for the new metrics. `eval/recheck_pending.py` rechecks the pending pool
  papers for a peer review file: on 2026-11-22, 0 of 94 had one (the checker found the known
  file for three control papers, on Springer and in PMC), so the pending papers most likely
  never opted in. The reserve gets no new papers from them; new ones come from new publications. `eval/jclub/selections.json` lists the Journal Club's last 12
  months (links and DOIs only: the commentaries carry no licence); 12 papers are in scope.
  Next: Langfuse in the harness, then the stage 1 baseline on dev2.
- **How evals run from now on** (maintainer's decision, 2026-11-22): Claude reviews and Claude
  judging run as Claude Code subagents on the maintainer's plan, not through the API, to save
  money; Gemini (`gemini-4-argon`, through the API) is the second, non-Claude judge. Keys are in
  `.env` in the main checkout (gitignored; names in `.env.example`); all four were checked
  working on 2026-11-22. Subagent runs use the session's model and effort, which differ from the
  API harness's fixed settings: record them, and don't mix their numbers with API-run numbers in
  one comparison.
- **Novelty lane** (`engine/novelty.md`, `agents/novelty-checker.md`): tried once, on a
  public arXiv paper, where it found a cited reference contradicting a priority statement that
  the science review missed. Not yet measured against referees. The project advisor's
  `search.py` and `scripts/arxiv_search.py` are the same script; keep them in step.
- **claude.ai skill bundle** (`skill-bundle/`, `scripts/package_skill.sh`, install guide in
  `claude-ai/README.md`): built, not yet run in claude.ai. The zip in `claude-ai/` is
  committed so users can download it: rebuild it after changing `engine/`, the scripts it
  copies or the dashboard template (`--check` tells you if it is stale).

## Next

- **Data and evaluation plan** (`research/data-plan.md`): stage 1 first: a corpus of papers
  with public referee reports, the baseline including the *must address* rate on accepted
  versions, and Langfuse for runs and labels.

- **Lab notes plugin** (`lab-notes/`, v0.1.0): setup, note, procedure, learn, plot. Not yet tried on a real
  lab's data. Next: his feedback; eLabFTW export; a hand-annotated messy lab day as the
  benchmark (`lab-notes/docs/record-format.md` is the format).

- Physicists rate the reviews; run the held-out test papers (`EVALUATION.md`).
- Measure the presentation and copy lanes.
- Word (`.docx`) input.
- A shared record of what has been tried (see the README, "Why this exists").

## Known limits

- An installed plugin keeps its cached version until the version number changes, so a
  dashboard rebuilt with an old install loses newer features.
- Opening `dashboard.html` straight from disk is less tested than serving it locally.
