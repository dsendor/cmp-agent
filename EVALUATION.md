# How well does it anticipate referees?

*Measured October 2026. Every number here is judged by an AI model and is provisional: no
physicist has yet rated the reviews, and the held-out test papers have not been run.*

## The question

Given a condensed matter paper as first submitted, how many of the concerns its real referees
raised does the review raise too?

## Method

- **Papers and referees.** Condensed matter papers whose journals publish the peer review
  file (mostly Nature Communications), reviewed as their first arXiv version. Each referee
  report's first-round concerns were extracted one by one. Concerns about material that is
  not in the first version were dropped. 30 papers form the development set; 22 more are
  held out for a final test.
- **Reviews.** Claude Opus 5.5 through the API, with the paper given as the PDF.
- **Judging.** For each referee concern, a judge model reads the paper, the concerns and one
  review and decides whether the review raised the concern, partly raised it, or did not.
  The judge is Gemini 4 Argon, a different model family from the reviewer; on 426 calls it
  agreed with Claude Opus 5.5 as a second judge 90% of the time (Cohen's kappa 0.84).
- **Recall** is the share of all referee concerns a review raised, pooled over papers, with
  95% intervals from resampling papers.

## Results on the development papers

| Reviewer | Papers | Recall | Change |
|---|---|---|---|
| The plain prompt "Review this paper." | 30 | 42% | |
| Liang et al. review prompt | 30 | 42% | |
| Three Liang et al. runs, merged into one prioritized list | 30 | 53% | +11 points (95% CI 9 to 13) |
| Liang et al. on the 10-paper subset | 10 | 45% | |
| **Reviewer v1.0** (Liang et al. + MARG's claims-to-experiments method + condensed matter checklist + importance tiers), one run | 10 | **49%** | +4 points (−1 to 9), not yet significant |
| MARG multi-agent reviewer, without refinement | 10 | 62% | at about 20 times the cost |
| The plain prompt asked for at least 70 concerns | 10 | 61% | matches MARG; length is what MARG adds |

What this settled:

1. **Merging independent runs is the cheapest reliable gain.** Three runs merged raise 11
   points more of the referees' concerns, in a list only 1.3 times as long as one review.
   This plugin merges three runs of reviewer v1.0 by default. That exact combination has not
   been measured yet.
2. **Importance tiers work for triage.** The *must address* tier holds about a third of a
   review's points and two thirds of the referees' major concerns the review caught.
3. **Order within a tier did not improve** with any variant tried. The dashboard lets you
   sort and filter for that reason.
4. **A catalog of known artifacts is not a substitute for a general review.** An earlier
   version that reviewed through a library of known lookalike effects (ordinary physics that
   mimics a topological signal) raised far fewer concerns than the plain prompt. Reviewer
   v1.0 keeps the general review and adds the condensed matter checklist as a last pass.

## Stage 1: accepted versions, tier precision and inference (November 2026)

*Measured 2026-11-22 on 54 more papers, 32 of them with the version the journal accepted. Reviews
ran as Claude Code subagents, not through the API, so these numbers do not mix with the table
above. Details: [`research/eval/stage1/README.md`](research/eval/stage1/README.md).*

| Metric | Reviewer v1.0 | Candidate v1.1 (not adopted) |
|---|---|---|
| Recall, three runs merged (dev2, 22 papers) | 55% (81% with partial matches) | |
| Recall, one run (held-out test2, 21 papers) | 50% (75%) | 45% (73%) |
| *Must address* items matching a real referee concern (test2) | 86% | 82% |
| ***Must address* items on the accepted version** (test2, 15 papers) | **3.3** | **0.7** |
| … on the first version of the same papers | 3.9 | 2.3 |
| Accepted versions with no *must address* item | 0 of 15 | 7 of 15 |

- **What "must address" means today.** v1.0's *must address* items are accurate (most match a
  real referee concern), but it raises as many on a paper the journal accepted as on the first
  draft. Its tiers rank concerns within a paper; they do not say a paper is not yet ready.
- **v1.1** makes the tier absolute ("a referee at a top-tier journal would require this") and
  adds a verdict. It brings accepted versions near zero at a cost of a few points of recall.
  The verdict line itself is not yet reliable.
- **Inferring the referees' requests** from what changed between versions, with the reports
  hidden: 77% of inferred requests are real, and 64% of real concerns are found (80% of those
  answered with new data). This is what the revision comparison (`/referee-preview:compare`)
  rests on.

## What the numbers do not tell you

- **Usefulness.** Recall only counts concerns the referees raised. About four of five review
  points match no referee concern; some are real problems the referees missed, some are
  noise, and only a physicist can tell which. The dashboard's decisions are how that will be
  measured.
- **The held-out papers.** The prompt was developed on the 30 development papers, so its gain
  could be smaller on new ones. The 22 test papers will be run once, with the reviewer frozen.
- **Clean papers.** Accepted versions (stage 1, above) are the closest proxy for a sound
  paper; whether the *must address* items they still get are real gaps or false alarms needs a
  physicist.
- **Other models and settings.** Measured with Claude Opus 5.5 at high effort through the API.
  Running inside Claude Code with another model is not measured.
- **Presentation and copy lanes** are newer and not yet measured.

## The full record

Everything behind these numbers is in [`research/`](research/): the referee concerns for each
paper, every review and judge call, the scoring scripts and the API harness that ran them
(`research/eval/api/`, keys read from environment variables), and the running log of what was
tried and why (`research/eval.md`). Step-by-step reports: `research/eval/step3-report.md` and
`research/eval/step4-plan.md`. A sample dashboard on a published paper, with its real
referees' concerns overlaid: `research/eval/sample/2601.01843/dashboard.html`.

## References

- Liang et al., "Can large language models provide useful feedback on research papers? A
  large-scale empirical analysis", arXiv:2310.01783.
- D'Arcy et al., "MARG: Multi-Agent Review Generation for Scientific Papers", arXiv:2401.04259.
