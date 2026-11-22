# Journal Club papers

*AI-generated. Run 2026-11-22. Nothing here is human-checked.*

The [Journal Club for Condensed Matter Physics](https://www.condmatjclub.org/) recommends a few
papers a month, each with an expert's commentary. These are papers the field rated important.
`research/data-plan.md` uses them for two checks that referee data cannot give:

1. **Does the reviewer bury important papers?** How many *must address* (tier A) items does it
   raise on a paper experts singled out? A reviewer that raises as many on these as on any
   draft is ranking relative to the paper in front of it, not against an absolute bar.
2. **Does it see why they matter?** Do the strengths it lists, and the novelty lane's
   positioning, match why the paper was recommended?

## Files

- `fetch.py` builds `selections.json`: the last 12 months of commentaries with their DOIs and
  the arXiv papers they recommend, with arXiv metadata. `in_scope` marks a cond-mat primary
  category other than soft matter: 12 papers.
- `reviews/<arXiv id>/`: the AI review of each in-scope paper.
  - `runs/r1.md` to `r3.md`: three independent science reviews.
  - `science-review.md`: the three, merged.
  - `science.json`: structured, with strengths.
  - `novelty.json`: the novelty lane.
  - The PDF (`paper.pdf`) is downloaded locally and not committed.

**Licence.** The commentaries carry no licence (none on the site or in their Crossref
metadata, checked 2026-11-22), so only links and DOIs are stored, never commentary text. The
reviews quote short passages from the arXiv papers, as the other AI reviews in `research/` do.

## How this run was made

- **Reviewer:** v1.0 (`engine/science.md` and `engine/merge.md`), three runs merged, as the
  plugin's exhaustive mode.
- **Structuring and novelty:** `engine/structure.md` (with strengths) and `engine/novelty.md`
  from the branch of PR #20, commit a8b2f8b, which was not yet merged.
- **Where it ran:** as Claude Code subagents (Claude Opus 5.5, the session's default effort),
  not through the API harness. So these numbers are not directly comparable with the API-run
  numbers in `EVALUATION.md`.
- Run in three waves of four papers.
