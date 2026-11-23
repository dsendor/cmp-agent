# Stage 1: referee-annotated papers, every metric

*AI-generated. Run 2026-11-22. Nothing here is human-checked: every extraction, review and
judgment was made by an AI model. Plan: `../../data-plan.md` (stage 1).*

## Summary

On 54 Nature-family papers with public peer review files (dev2 and test2, 27 each, all published
after the reviewer model's training cutoff):

1. **The current reviewer (v1.0) cannot tell an accepted paper from a first draft.** It raises
   4.5 *must address* items per accepted version (dev2, three runs merged) against 4.6 on the
   same papers' first versions. No review of an accepted version had zero.
2. **Its *must address* items are accurate.** 80% of them match a real referee concern (60% in
   full). Recall of the referees' concerns is 55% (81% counting partial matches).
3. **The candidate v1.1 fixes the first point and holds most of the second.** On the held-out
   test2 set (one run each): *must address* items on accepted versions 3.3 → 0.7, with 7 of 15
   accepted versions at zero; recall 50% → 45% (75% → 73% with partial matches); precision of
   *must address* items 86% → 82%.
4. **Referee requests can be inferred from what changed.** With the reports hidden, 77% of the
   requests the comparison lane inferred match a real concern, and it finds 64% of the real
   concerns (80% of those the authors answered with new data). It agrees with the referees that
   the accepted version answered the request in 81% of cases, and never says "not addressed".

## Data

- `fetch.py` assembled the triples: arXiv v1, the peer review file (Springer's static content),
  and the accepted version: the arXiv version posted after acceptance where there is one,
  otherwise the journal PDF from nature.com (downloaded with the maintainer's permission,
  2026-11-22). `manifest.json` records each source. 32 of the 54 papers have an accepted
  version (17 dev2, 15 test2); the rest are paywalled or Accelerated Article Previews without a
  final PDF. PDFs are not committed. Several PDFs lack the supplementary information.
- `../referee/<id>/referee.json`: the referees' concerns, extracted from each peer review file
  by a Claude Code subagent with `../api/prompts/extract.md` (the experiment 11 prompt): 54
  papers, 921 first-round concerns.
- For 10 of the 54 papers arXiv v1 is not the manuscript the referees first saw (already
  revised, or reviewed at another journal first). They are reviewed but left out of recall and
  precision (`reviewed_matches_v1` in `referee.json`).

Reviews ran as Claude Code subagents (Claude Opus 5.5, the session's default effort), not
through the API harness, so they are not directly comparable with the API-run numbers in
`EVALUATION.md`. The judge is Gemini (`gemini-4-argon`), with the prompt behind `EVALUATION.md`
(`../api/prompts/judge_v2.md`), the review blinded and its points in a seeded random order. The
judge sees each review's items with their tiers, so tier A precision is read off directly
(`judge.py`).

## Results

### Baseline: reviewer v1.0, exhaustive mode, dev2 (`runs/v1.0`)

| | |
|---|---|
| Recall, strict / with partial matches (22 papers) | 54.9% / 80.7% |
| Tier A precision, any match / full match | 80.4% / 59.8% |
| *Must address* per first version (27) | 4.33 |
| *Must address* per accepted version (17) | 4.53 (first versions of the same 17: 4.59) |
| Accepted versions with no *must address* item | 0 of 17 |

### The candidate: v1.1 (`engine-v1.1/`)

v1.1 changes two things in `science.md` and `merge.md`:
- Tier A is absolute: "a referee at a top-tier journal would require this before accepting the
  paper". The prompt says many good papers have no tier A item and a paper ready for publication
  has none, and asks for a last check that moves to B any A item the paper already answers with
  evidence a reasonable referee would accept.
- Every review ends with a verdict: ready, minor revision or major revision.

It was compared with v1.0 in standard mode (one run; v1.0's first exhaustive run, `runs/r1.md`,
is exactly that). A second v1.0 run (`runs/r2.md`) measures run-to-run noise.

| One run each | dev2 v1.0 r1 | dev2 v1.0 r2 | dev2 v1.1 | test2 v1.0 | test2 v1.1 |
|---|---|---|---|---|---|
| Recall, strict | 45.7% | 44.0% | 42.9% | 50.4% | 44.6% |
| Recall, with partial matches | 73.3% | 68.5% | 66.5% | 75.2% | 73.1% |
| Tier A precision (any match) | 82.1% | 82.2% | 83.3% | 86.1% | 82.4% |
| *Must address* per first version | 3.44 | 3.26 | 2.07 | 3.81 | 2.44 |
| *Must address* per accepted version | 3.29 | 3.12 | **1.29** | 3.27 | **0.67** |
| Accepted versions with none | 0/17 | 0/17 | 5/17 | 0/15 | **7/15** |

Recall and precision are on the papers whose v1 matches the reviewed manuscript (22 dev2, 21
test2). test2 was run once, after v1.1 was fixed on dev2.

**Reading.** The tier A rate on accepted versions falls to the plan's target (about one or
fewer) on both sets, and the gap between first and accepted versions opens (test2: 2.4 against
0.7). Tier A precision holds. Recall falls by 2 to 6 points strict and 2 to 7 points with partial
matches; two v1.0 runs differ by 2 to 5 points, so part of the fall is noise, but it is in the
same direction on both sets. v1.1 writes about 10% fewer items. Whether to adopt it is a choice
between those two numbers; it has not been adopted (`engine/` is unchanged).

**The verdict needs work.** v1.1 says "major revision" for 25 of 27 test2 first versions (right
direction) but also for 8 of 15 accepted versions. The tier A count separates the versions
better than the verdict line does.

### Inference test (`inference/`, `infer_judge.py`)

For the 13 dev2 papers with an accepted version and a matching v1, a subagent ran steps 1 and 3
of `engine/compare.md` on v1 and the accepted version with the referee reports hidden, and
Gemini matched the inferred requests to the real concerns.

| | |
|---|---|
| Inferred requests that match a real concern (precision) | 112 / 146 = 77% |
| Real concerns found (recall) | 146 / 228 = 64% |
| … answered with new data or analysis | 35 / 44 = 80% |
| … answered by argument or rewording | 96 / 153 = 63% |
| … partly answered | 14 / 25 = 56% |
| … not addressed | 1 / 6 = 17% |
| Response judgment: matched requests judged addressed or partly (referees accepted all) | 91 / 112 = 81% |

The other 19% are "unclear" (usually because the accepted version's supplement was missing),
never "not addressed". Concerns answered only in the response letter leave no trace in the paper,
so recall on them is low, as expected. This is the number stage 2 depends on: on papers without
public reports, about four in five inferred requests are real and about two in three real
concerns are recovered.

### Earlier: the pilot

The first six dev2 papers, reviewed before the rest, gave 4.5 *must address* items on first
versions and 4.3 on accepted versions; they are part of `runs/v1.0`.

## Caveats

- One reviewer model and one judge model; the judge has not been checked against physicists on
  these papers (`../judge-audit.md` covers the earlier set).
- Single runs for the v1.0/v1.1 comparison. Exhaustive mode was run for v1.0 only.
- Extractions are AI-made; for several papers the extractor had to infer severity, and some
  peer review files hold only later rounds or a transferred paper's second journal.
- Missing supplements: some items ask for what may be in the supplement, and some inferred
  requests are marked unclear for the same reason.

## Files

- `fetch.py`, `manifest.json`: inputs. `drive.py`: a headless runner for the same reviews
  (`claude -p`), unused here because the CLI's sign-in had expired.
- `runs/<v1.0|v1.1|t1.0|t1.1>/<id>/<v1|accepted>/`: `runs/r*.md` (single runs),
  `science-review.md` (merged, v1.0 dev2), `judge*.gemini.json`.
- `engine-v1.1/`: the candidate prompts.
- `inference/<id>/`: `changes.md`, `inferred.json`, `walkthrough.json`, `judge.gemini.json`.
- `judge.py`, `score.py`, `infer_judge.py`: the metrics.

```bash
python3 research/eval/stage1/score.py dev2 v1.0                          # exhaustive baseline
python3 research/eval/stage1/score.py test2 t1.1 --review runs/r1.md      # v1.1 on test2
python3 research/eval/stage1/infer_judge.py --score
```
