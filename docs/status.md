# Status: what is in progress and what is next

Agents keep this page current. Update it at the end of a piece of work: move finished items
out, add what you learned that the next session needs. History belongs in git, not here.

## Released

- Version 0.2.0 (`.claude-plugin/plugin.json`): review, apply and contribute commands; the
  dashboard with triage, walk-through, PDF pane, and an optional version comparison page.

## In progress

- Publishing a dashboard as a Claude artifact, as an option after the review, so it can be
  shared as a link. The local `dashboard.html` stays the default.

## Next

- Physicists rate the reviews; run the held-out test papers (`EVALUATION.md`).
- Measure the presentation and copy lanes.
- Word (`.docx`) input.
- A shared record of what has been tried (see the README, "Why this exists").

## Known limits

- An installed plugin keeps its cached version until the version number changes, so a
  dashboard rebuilt with an old install loses newer features.
- Opening `dashboard.html` straight from disk is less tested than serving it locally.
