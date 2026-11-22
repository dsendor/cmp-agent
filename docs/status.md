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

## Next

- **Lab notes plugin** (`lab-notes/`, v0.1.0): setup, note, procedure, learn, plot. Not yet tried on a real
  lab's data. Next: his feedback; eLabFTW export; a hand-annotated messy lab day as the
  benchmark (`lab-notes/docs/record-format.md` is the format).

- **Project advisor plugin** (`project-advisor/`, v0.1.0): one skill, `/project-advisor:choose`.
  Tested only on a made-up example. Next: a blind comparison against a plain "help me choose
  between these" prompt with two or three early-career experimentalists on their own ideas,
  then a 3 to 6 month follow-up on what they picked. Protocol, forms and pass or stop
  criteria: `project-advisor/eval/README.md`. Later: Semantic Scholar and ADS as extra search sources.

- Physicists rate the reviews; run the held-out test papers (`EVALUATION.md`).
- Measure the presentation and copy lanes.
- Word (`.docx`) input.
- A shared record of what has been tried (see the README, "Why this exists").

## Known limits

- OpenAlex has required an API key since February 2026; an unkeyed request returned HTTP 429
  on 2026-11-21. `research/skill/SKILL.md` and `research/prior-work.md` still say it needs
  no key. Check any OpenAlex lookup before relying on it.

- An installed plugin keeps its cached version until the version number changes, so a
  dashboard rebuilt with an old install loses newer features.
- Opening `dashboard.html` straight from disk is less tested than serving it locally.
