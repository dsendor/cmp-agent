# Stage 1: must-address items on accepted papers

*AI-generated. Run 2026-11-22. Nothing here is human-checked. Plan: `../../data-plan.md`.*

**Question.** A version a journal accepted was "enough" for its referees. Does the reviewer
still raise *must address* items on it, and fewer than on the first version?

## Pilot: six dev2 papers, first and accepted version

Six of the 27 dev2 papers (`../referee/split.json`) have an arXiv version posted after the
journal accepted them. That version is the accepted text, and arXiv allows using it; the other
21 would need the journal's PDF. Each version was reviewed by reviewer v1.0 in exhaustive mode:
three independent runs merged (`engine/science.md`, `engine/merge.md`), as Claude Code
subagents (Claude Opus 5.5). Tier counts come from the merged review (`science-review.md`). The
runs are in `pilot/<arXiv id>/<v1|accepted>/`; the PDFs are not committed.

| Paper | Journal | v1 must / should / minor | Accepted must / should / minor |
|---|---|---|---|
| 2501.13446 | Communications Materials | 5 / 11 / 8 | 6 / 9 / 11 |
| 2504.19361 | Communications Physics | 4 / 8 / 9 | 4 / 10 / 9 |
| 2508.16491 | Communications Materials | 4 / 12 / 8 | 4 / 13 / 11 |
| 2511.02448 | Communications Materials | 4 / 7 / 13 | 4 / 9 / 7 |
| 2512.00737 | Nature Communications | 4 / 11 / 8 | 4 / 9 / 9 |
| 2512.12439 | Communications Physics | 6 / 8 / 9 | 4 / 12 / 10 |
| **Mean** | | **4.5** / 9.5 / 9.2 | **4.3** / 10.3 / 9.5 |

**Result: the accepted versions get as many *must address* items as the first versions**
(4.3 against 4.5 per paper; five of six papers have the same count or one more). The papers the
Journal Club recommended got 4.2 (`../jclub/results.md`). Across the 24 reviews here and in that
run, the count stays at 3 to 6 whatever the state of the paper. The tiers rank concerns within
a paper; they do not say whether a referee would require them.

This is the baseline for the "enough" metric. The prototype in `../../data-plan.md` (absolute
tiers, an overall verdict, a review may have no tier A items) should bring the count on accepted
versions near zero while recall on first versions holds.

## Caveats

- Six papers, mostly from Communications Materials and Communications Physics.
- Only the count is measured, not which items: an accepted version's tier A items may be the same
  concerns as before, left alone, or new ones. Matching them, and matching both versions' items
  to the referees' concerns (not yet extracted for dev2), is the next step.
- The version posted after acceptance can differ from the journal's in copy-editing. Several arXiv
  PDFs lack the supplementary material they cite, and the reviews ask for some of it.
- Subagent runs use the session's model and effort, not the API harness's fixed settings.

## In Langfuse

Dataset `stage1-pilot` (12 items), experiment `stage1-pilot-reviewer-v1.0-cc` with scores
`must_address`, `should_address`, `minor`, `items` and their means. Synced with
`../langfuse_sync.py`.
