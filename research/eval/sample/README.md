# Sample dashboard (M1)

*AI only, made 2026-10-29 for David to review before any test spend (`../../writer-mvp-plan.md`, M1).*

Open `2601.01843/dashboard.html` in Chrome or Safari. The paper (arXiv 2601.01843v1, pressurized
UTe2 point-contact spectroscopy, one of the `marg10` development papers) loads from arXiv in the
right-hand pane; to work offline, save `https://arxiv.org/pdf/2601.01843v1` as `paper.pdf` next
to the dashboard and rebuild with `python3 ../../../scripts/build_dashboard.py 2601.01843`.

How it was made, following the plugin's `review` skill:

| Step | Made by | File |
|---|---|---|
| Three science reviews, prompt D | the existing API runs (P16, Opus 5.5, batch) | `runs/r1.md` to `r3.md` |
| Merge, with which runs raised each concern | `review-merger`, in Claude Code | `science-review.md` (31 concerns) |
| Structure, quotes, effort, scoped claims | `issue-structurer`, with the LaTeX source | `science.json` |
| Presentation pass | `presentation-reviewer` | `presentation.json` (15) |
| Copy pass, on the LaTeX source | `copy-checker` | `copy.json` (60) |
| Assemble, quote check, dashboard | `assemble.py`, `check_evidence.py`, `build_dashboard.py` | `review.json`, `dashboard.html` |
| Demo-only referee overlay | a matching agent with the eval judge's definitions; `add_referee_demo.py` | `referee_map.json` |

Results on this one paper, AI-judged:

- **Quotes found in the paper:** science 31 of 31, presentation 15 of 15, copy 54 of 60 (the 6
  misses are equations and a table row the copy pass retyped; the dashboard flags them).
- **Edits that apply to the LaTeX source exactly once:** copy 58 of 60 (two involve dashes stored
  in a non-UTF-8 encoding that vanish from the PDF, a real error the pass caught), presentation
  7 of 8, scoped claims 14 of 14.
- **Referee overlay:** of the referees' 33 first-round concerns, the review raised 15 and 9 in
  part; all 13 major concerns were raised (10) or partly raised (3). The 9 missed are minor.

The first structuring took scoped-claim edits from the PDF text and only 3 of 14 matched the
source; the `issue-structurer` now takes them from the LaTeX source, and the sample uses that
version.

Dashboard v0.2 (2026-10-30) links each objection to a main claim. The structuring step now records the
claim number; for this sample, made before that change, Claude added the links afterwards from each
item's claim text (`review.json`, `claim_ids_note`).
