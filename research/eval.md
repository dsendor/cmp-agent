# Evaluation record: what we tried, what worked, what didn't

*AI only. Every run, score and judgment here was made by the same model between
2026-10-23 and 2026-10-25. No physicist has checked any of it. This file is the single
record of the evaluation; the folders under `eval/` hold the runs and data behind it.*

## Status

The lookalike assistant (library v0.5, `skill/SKILL.md`) **does not beat a plain "Review
this paper." prompt.** Against real journal referees on 16 papers, the plain prompt raised
46% of first-round concerns and the assistant 15%, and the plain prompt raised more on
every paper. Further assistant runs are paused.

From 2026-10-27 the work follows a data-driven eval plan (Notion: "Claude instructions:
data-driven eval plan for the CMP reviewer"), changed by David on 2026-10-28 (see
[Plan changes](#plan-changes)). Pick the best existing reviewer, improve it against
held-out referee concerns, and add the library as a layer only if it earns its place. See
[Eval plan](#eval-plan-from-2026-10-27). **A new session starts at
[Next session: start here](#next-session-start-here).** The first API runs were on
2026-10-28 (rows P1 to P6 under [Plan runs](#plan-runs), $13.37 in all), until the Claude
API refused new requests at a Console spending limit.

## Every experiment at a glance

| # | Date | Library | Question | Result | Verdict |
|---|---|---|---|---|---|
| 1 | 10-23 | v0.2 | Pilot: can it write a usable report? | Three reports, readable. Superseded by experiment 3. | Worked, as a demo |
| 2 | 10-23 | v0.3 | Does released figure data add anything? (Yu et al. 2021, 65 files) | Sharper questions, a gap in the data release, a bug in `read_mtx.py` found and fixed. No status changed. | Worked, one paper |
| 3 | 10-23 | v0.4 | Is it stable, and does its status column separate careful papers from others? (9 new papers, 3 runs on 7) | Stable core flags (overlap 0.31 to 0.83). Nearly every row "partly addressed" on careful and other papers alike. | Stable; **no separation** |
| 4 | 10-23 | v0.4 | Planted test: does deleting a paper's control change the status? (2 papers) | No status changed. Cut-text runs lost the quotes; on one paper all three runs noticed a gap. | **Didn't work** |
| 5 | 10-23 | v0.4 | Known-outcome papers: does it flag what later work showed? (5 papers) | Assistant 14 of 16, OpenAIReview prompt 12, plain prompt 10. Answer key partly circular. | Weak positive |
| 6 | 10-23 | v0.4 | Against two baselines on the new papers, what does each catch? | Baselines catch calculation and consistency errors the assistant skips. Assistant asks device and selection questions they skip. | Mixed |
| 7 | 10-24 | v0.5 | Does a finer, test-based status scale separate careful papers? | 81% of careful rows and 78% of other rows "tested in part". | **Didn't work** |
| 8 | 10-24 | v0.5 | Larger planted test (9 papers, 24 deletions) | Status dropped in 1 of 26 targeted rows, about run-to-run noise. Prose noticed 9 deletions. | **Didn't work** |
| 9 | 10-24 | v0.5 | Planted number errors (7), assistant against plain prompt | Both caught 7 of 7. | No advantage |
| 10 | 10-24 | none | Research: what can stand in for "less careful" papers? | Unpublished preprints are a weak proxy. Open referee reports are the best one. | Led to experiment 11 |
| 11 | 10-25 | v0.5 | Referee match: does it raise what real referees raised? (16 papers, 213 concerns) | Assistant 15%, plain prompt 46%. Plain prompt ahead on all 16 papers. | **Didn't work** |

## What worked

- **Stable core flags.** Selection and the one or two lookalikes closest to the claim recur
  in every run of the same paper (experiment 3).
- **Device and selection questions.** How many devices, why others were set aside, the
  second-best dataset. The assistant asks them on every paper; the baselines mostly don't
  (experiment 6).
- **Checked related work.** The skill has each related-work link opened and its ID, title
  and first author confirmed, and the run notes record how each was checked. The library's
  quote check (`scripts/check.py --quotes`) keeps model memory out of the library.
- **Figure data.** With a paper's raw files, the assistant read off plateau values,
  undid a series-resistance correction and found gaps in the release (experiment 2).
- **Known-outcome recall.** 14 of 16 answer-key explanations, ahead of both baselines,
  with the caveat that the key overlaps the library's sources (experiment 5).

## What didn't work, and why

- **The status column never discriminated.** In v0.4 nearly every row was "partly
  addressed", because each entry's control bundled several tests and the skill said to
  pick the weaker status when unsure. v0.5 split controls into tests and still put about
  80% of rows on "tested in part" for careful and other papers alike (experiments 3, 7).
- **Removing evidence barely moved the marks.** Most deleted passages were statements,
  which v0.5 does not count as tests, and most cut evidence survived in a caption or the
  supplement. The signal that did appear was in the prose, which a score cannot read
  without a judge (experiments 4, 8).
- **No edge on consistency checks.** The plain prompt caught every planted number error
  the assistant caught (experiment 9).
- **Referees raise paper-specific physics, and the assistant is built to skip it.** The
  misses are fit models, reference baselines, theory assumptions and alternative
  explanations unique to one device. No library of known lookalikes can hold these, and
  the skill tells the assistant not to judge whether the result is right, caps the report
  near 900 words and limits questions to devices and data. It lost even on its home
  ground: alternative explanations 26% against 52% (experiment 11).
- **Most real papers fall outside the library.** 11 of the 16 referee papers were outside
  topological transport. On the 5 inside it, the assistant still trailed, 17% against 48%.

## The experiments in detail

### 1. Pilot (v0.2)

Three reports on 1710.10701, 1204.4212 and 2607.09511, written before the checks, the
hold-out rule and repeat runs existed. The reports were deleted once experiment 3 replaced
them; the runs in `eval/runs/` are the current versions.

### 2. Figure-data test (v0.3): Yu et al. 2021, arXiv 2004.08583v1

Report and notes in `reports/2004.08583.md` and `.notes.md`. Not scored: the paper argues
its own peaks are not Majorana, and four library sources cite it.

- The barrier "plateau" is 7 of 17 gate points within 0.90 to 1.04 × 2e²/h. Of five gate
  settings scanned in field, two peak below 0.95 × 2e²/h. Undoing the 4 kΩ series
  correction puts the 1 T peak near 0.75 × 2e²/h.
- No right-end file shows a zero-bias peak above 0.05 × 2e²/h, which confirms the
  paper's one-end result.
- The release has gaps: four pairs of identical arrays, two panels with no file, about 31
  two-sided scans for "about 7000 useful datasets".
- Tool fixes: `read_mtx.py` had the axis order wrong (fixed and checked against the
  authors' reader); mapping instrument labels to figure axes is a step the skill doesn't
  describe.

The notes list problems in a named group's public data release. A person should check
them before anyone outside sees them.

### 3 to 6. Main test on library v0.4

**Test set** (`eval/papers.yaml`, with reasons and answer keys):

| Group | Papers | Runs |
|---|---|---|
| New, main | 2607.09511, 2608.12897, 2610.18817, 2608.17404 (careful), 2608.27444 (careful) | assistant ×3, both baselines |
| New, careful, planted | 2608.26022, 2609.38003 | assistant ×3 on full text, ×3 on cut text, both baselines |
| New, secondary | 2609.01233, 2610.29124 | assistant ×1, both baselines |
| Known outcome | 1710.10701, 1204.4212, 1606.05712, 2207.02472, 1809.05513 | assistant ×1, both baselines |

"Careful" means the paper shows the controls a referee would ask for. An agent picked
them; a physicist hasn't checked the choice. New papers were all posted after the model's
training data.

**Method.** A fresh agent per run read only the skill, template, library and paper, and
wrote a report, run notes and `flags.json`. Baseline 1 is the OpenAIReview zero-shot prompt
([github.com/ChicagoHAI/OpenAIReview](https://github.com/ChicagoHAI/OpenAIReview), MIT,
`src/reviewer/prompts.py`), verbatim. Baseline 2 is "Review this paper." A blind judge
mapped baseline comments to library ids (`runs/<id>/judge.json`). Stability is the mean
pairwise Jaccard overlap of flag sets (SPOT, [arXiv 2505.11855](https://arxiv.org/abs/2505.11855)).
`eval/score.py` and `eval/planted.py` reproduce the tables in `eval/scores.md` and
`eval/planted.md`.

**Stability** (experiment 3):

| Paper | Flags per run | Mean overlap | In every run |
|---|---|---|---|
| 2607.09511 | 3, 5, 4 | 0.60 | 2 |
| 2608.12897 | 6, 5, 4 | 0.31 | 2 |
| 2610.18817 | 3, 3, 4 | 0.83 | 3 |
| 2608.17404 | 16, 15, 16 | 0.74 | 13 |
| 2608.27444 | 5, 5, 3 | 0.54 | 3 |
| 2608.26022 | 3, 2, 3 | 0.78 | 2 |
| 2609.38003 | 2, 2, 3 | 0.78 | 2 |

**Statuses** (experiment 3):

| | Rows | Ruled out | Partly addressed | Not addressed |
|---|---|---|---|---|
| Careful papers (12 runs) | 86 | 0 | 77 | 9 |
| Other new papers (11 runs) | 50 | 1 | 44 | 5 |

**Planted test** (experiment 4). Removing the passages where 2608.26022 and 2609.38003
address a lookalike left every target status at "partly addressed". Full-text runs quoted
the removed passages (6 of 6); cut-text runs couldn't. On 2609.38003 the cut left three
references cited nowhere, and all three cut-text runs asked whether a passage was missing.

**Known-outcome papers** (experiment 5). Recall against the answer key, precision floor in
brackets:

| Paper | Assistant | OpenAIReview prompt | Plain prompt |
|---|---|---|---|
| 1710.10701 (retracted) | 4 of 4 (6 of 13) | 3 of 4 (5 of 7) | 3 of 4 (4 of 6) |
| 1204.4212 | 4 of 5 (4 of 6) | 4 of 5 (4 of 5) | 2 of 5 (2 of 3) |
| 1606.05712 (retracted) | 1 of 2 (1 of 5) | 2 of 2 (2 of 4) | 2 of 2 (2 of 4) |
| 2207.02472 | 3 of 3 (3 of 9) | 2 of 3 (2 of 7) | 2 of 3 (2 of 7) |
| 1809.05513 | 2 of 2 (2 of 12) | 1 of 2 (1 of 2) | 1 of 2 (1 of 6) |
| **Total** | **14 of 16** | **12 of 16** | **10 of 16** |

Read as a sanity check only. The library was built partly from the papers that answer
these; the hold-out rule removes those sources but not the entries' wording. The plain
prompt recalled the later history of three papers from memory. One run each. 1204.4212
stands in for Frolov et al.'s "four cases", which are the authors' own trivial devices and
have no claim paper of their own.

**Baselines** (experiment 6). Lookalikes raised per paper, on the same library ids:

| Paper | Assistant | OpenAIReview | Plain | Raised by a baseline only |
|---|---|---|---|---|
| 2607.09511 | 5 | 4 | 5 | analysis-choice sensitivity; dot Andreev states |
| 2608.12897 | 10 | 3 | 2 | none |
| 2610.18817 | 4 | 3 | 2 | analysis-choice sensitivity |
| 2608.17404 | 20 | 3 | 8 | none |
| 2608.27444 | 7 | 1 | 4 | heating |
| 2608.26022 | 3 | 4 | 3 | heating, percolation, analysis choices |
| 2609.38003 | 3 | 2 | 3 | heating |
| 2609.01233 | 4 | 2 | 5 | heating, percolation, analysis choices |
| 2610.29124 | 5 | 4 | 5 | circuit and Fiske resonances, heating, analysis choices |

The baselines checked the paper against itself (wrong factors, unit conversions,
contradictions between text and supplement). The assistant asked the device and selection
questions and named subfield lookalikes the baselines rarely did. On the most-discussed
alternatives all three converged.

### 7 to 9. Follow-up on library v0.5

**What v0.5 changed.** Each lookalike lists discrete tests (60 across 28 entries), marked
all, part or no. Four statuses: ruled out for the claim, tested in part, left open by the
authors, not tested (argued, data bear on it, not mentioned). A sentence alone no longer
counts as a test. `eval/score_v5.py` writes `eval/scores_v5.md`.

**Status scale** (experiment 7), two runs on each of the nine new papers:

| Group | Rows | Tested in part | Not tested | Tests marked "all" | Checks done |
|---|---|---|---|---|---|
| Careful | 52 | 81% | 17% | 18% | 5% |
| Others | 41 | 78% | 20% | 24% | 9% |

**Larger planted test** (experiment 8, `eval/planted5/`, scored by `eval/planted5.py`).
Nine careful papers (the four above plus 2607.00683, 2607.11721, 2608.19099, 2610.17701,
2610.29446); full text run twice as a noise baseline, 24 deletions run once each.

- The targeted row's status dropped below both original runs in 1 of 26 rows, its test
  score in 3. Between two full-text runs, status differs in 3% of rows and test score in
  17%. So the drops are at noise level.
- A judge read each cut run (`judge-*.json`, one call corrected with the reason recorded):

| Removed passage | Deletions | Noticed | Asked | Lowered | Nothing |
|---|---|---|---|---|---|
| Shown evidence | 4 | 1 | 1 | 1 | 1 |
| Mixed | 5 | 2 | 1 | 0 | 2 |
| Statement | 15 | 6 | 1 | 1 | 7 |
| All | 24 | 9 | 3 | 2 | 10 |

- Every run that noticed missing text blamed text extraction; none suspected a test.

**Planted number errors** (experiment 9). Seven single-number changes, each contradicting
another number in the same paper. The assistant and the plain prompt each caught all
seven (`eval/planted5/numeric.json`).

**Slips found in the papers as posted.** While checking numbers, runs flagged apparent
inconsistencies in the unmodified text of 2607.11721, 2610.29446, 2610.17701, 2608.17404,
2608.27444 and 2608.26022 (details in the run notes under `eval/planted5/`). AI readings
of extracted text; unchecked.

### 10. Proxies for less careful papers

`eval/proxies.md` has the research and sources. Preprints that are never published are a
weak proxy: 9 of 136 in one subfield, often for reasons unrelated to quality. Open peer
review is better: Nature Communications posts referee reports for nearly every paper since
2024, so comparing the assistant's output with the referees' concerns needs no physicist
up front.

### 11. Referee match (v0.5)

**Setup** (`eval/referee/`). Papers whose peer review files became public after the
model's training cutoff. The assistant and the plain prompt each read the same arXiv v1
(PDF and text, no web access to the paper, the journal version or the reviews). An agent
extracted the first-round referee concerns from each review file (`<id>/referee.json`). A
blind judge mapped each concern to Review A and Review B (order randomized) as raised,
partly or not raised (`<id>/judge.json`). `score.py` writes `scores.json`. Presentation and
novelty concerns are left out, as are concerns already fixed in v1 (some v1 texts are the
revised manuscript). That leaves 213 concerns on 16 papers.

| | Assistant | Plain prompt |
|---|---|---|
| Raised | 32 of 213 (15%) | 98 of 213 (46%) |
| Raised or partly raised | 80 (38%) | 165 (77%) |
| Papers where it raised more | 0 of 16 | 16 of 16 |
| Concerns only it raised | 1 | 67 |
| Issues no referee raised (judge: substantive) | 91 | 289 |
| Mean length | about 1,500 words | about 3,000 words |

The gap in "raised" is 31 points (95% bootstrap interval over papers, 24 to 39).

| Split | Assistant raised | Plain raised |
|---|---|---|
| Papers in the library's scope (5) | 17% | 48% |
| Papers outside it (11) | 14% | 45% |
| Alternative explanation (42 concerns) | 26% | 52% |
| Missing control or measurement (41) | 12% | 41% |
| Data selection or reproducibility (20) | 20% | 50% |
| Analysis or numbers (47) | 15% | 60% |
| Theory or modelling (63) | 8% | 33% |
| Major concerns (133) | 17% | 54% |

**Coverage.** 31 papers qualified (`papers.json`, with tiers and caveats; 3 more excluded
and listed there). 16 were run and judged, all from tiers A and B, whose reports went
public after the cutoff. Tier C (reports public before the cutoff, a contamination risk)
was not reached: the run hit the usage limit and was then paused. Of the 15 unrun papers,
four have folders with the extracted concerns only (2503.13213, 2506.04601, 2506.16869,
2509.02063), and 2509.02063 also has a complete but unjudged assistant run. Partial
outputs from runs cut off by the limit were deleted.

**Caveats.** Five of the 16 papers were reviewed in a version that differs from v1, and
2503.17875 has only two scorable concerns. Referees are one reading of a paper; both
reviews raised many issues no referee did, which this test cannot score. One model
throughout, as assistant, plain reviewer, extractor and judge.

## Eval plan (from 2026-10-27)

The plan (Notion, "Claude instructions: data-driven eval plan for the CMP reviewer") aims
for an MVP reviewer that beats the plain prompt on held-out referee concerns within four
weeks. Pass bar on the test set: recall at least 8 points above the plain prompt (and also
ahead on matched-length recall), precision no lower, at least 10 unique substantive
concerns, and a false-alarm rate on clean papers no higher than the plain prompt's. Equal
recall with fewer false alarms counts as a win. Steps: 0 verify the analysis, 1 expand the
dataset, 2 validate the judge, 3 pick a base reviewer among existing ones, 4 improve it on
dev, 5 add the lookalike library as a layer, 6 test set, 7 physicist check. The v0.6 idea
from experiment 11 (a full referee read first, the library second) is one candidate
inside step 4. The Notion page is the source of truth for anything the changes below
don't cover.

### Plan changes

| # | Date | Change | Source |
|---|---|---|---|
| U1 | 10-28 | Keep every paper (the five-concern minimum is removed, restoring 2509.04209, 2606.31267, 2503.17875). Record each referee's recommendation; label papers clean (all accept or minor) or contested. Recall pooled over concerns, bootstrap and paired tests by resampling papers. New metrics: false-alarm rate on clean papers, severity agreement (Spearman, reviewer verdict against referee recommendations). Every metric reported for clean and contested papers separately. Pass bar adds the false-alarm condition. Power rerun with pooled recall. | David, 2026-10-28 |
| U2 | 10-28 | Claude only: Opus 5.5 reviews, runs the plain baseline and extracts; Sonnet 5.5 is the main judge; Opus 5.5 second judge for Step 2 only; Fable 5.1 optional ceiling check. Judge blind (no model names or formatting cues, random order). Step 2 kappa among Sonnet, Opus and the old judge.json, at least 0.6 before Step 3. Judge audit grows to 50 calls, at least 15 on the final candidate. Every result labeled "Claude-judged, provisional"; the MVP claim needs a non-Claude judge rerun on the test set. Step 0 contamination probe on Claude only; Step 3 candidates plain, OpenAIReview, Liang et al., MARG (10 dev papers first), all on Opus 5.5; Step 6 final variant and plain only. Budget about $420 to $600, Claude only, replaced by measured cost after the 5-paper check. | David, 2026-10-28 |
| U3 | 10-28 | Answers to the Step 0 questions. Definitions of precision and unique concerns replaced (below). Every comparison reports mean words and mean concerns per review, and matched-length recall: each reviewer ranks its concerns and recall is scored on its top k, k the median referee concern count; a variant wins on recall only if it also wins on matched-length recall. Split: dev is the 16 judged papers plus about 14 post-cutoff (about 30, early papers added if needed and reported apart); test about 50 post-cutoff picked at random; the rest a reserve for a second test. Final counts before any extraction. | David, 2026-10-28 |
| U4 | 10-28 | David reports Gemini working and asks for it as a comparison. The 2026-10-28 session found the key (`GEMINI_API_KEY`) and exact IDs (`gemini-4-argon`, `gemini-3.8-flash`, now in `api/config.json` with batch prices), and, once David added credit later that day, ran it as a second-family judge (P8) and a pilot comparator (P9). David's call on its role (comparison reviewer only, or also judge) is still open. | David, 2026-10-28 |
| U5 | 10-28 | Gemini 4 Argon is the main judge: a different model family from the Opus 5.5 reviewer, and the judge that agreed best with Opus 5.5 (kappa 0.84, P8). Opus 5.5 stays the reviewer. Sonnet 5.5 is no longer the main judge. Use nature.com if reachable; otherwise accept the data available and go on: dev 30 (16 judged + 14 drawn) and test 22, from `referee/split.json` (seed 20261028), with any papers reached later added to the reserve. Go-ahead to extract concerns. | David, 2026-10-28 |
| U6 | 10-29 | Writer mode first, in a Claude Code plugin (`referee-preview/`); plan in `writer-mvp-plan.md`. Reviewer frozen as v1.0 in `referee-preview/engine/`: `science.md` is prompt D (`arms/liangplus_cmp.md`) byte for byte (sha256 f8d027247d57); `merge.md` is `prompts/merge.md` plus one line recording which runs raised each concern (44c5b6715c6b); `structure.md` (dcac00a4662a; 6f0fad120a70 from 10-30, adding a claim number to each issue), `presentation.md` (6841121471d4; 77dedced210c from 10-30, the same) and `copy.md` (8026381026a7) are new and unmeasured. Recall tuning on dev is paused. The ship checks (test22 once, the plugin in Claude Code on 5 marg10 papers, quote check, overlap) follow David's review of the sample dashboard, capped at $100. Any reviewer change after the test22 run goes to a reserve set. | David, 2026-10-29 |

**Definitions now in force (U3), and how they differ from the 2026-10-27 ones.**

- *Precision:* the share of a review's substantive concerns that match at least one
  referee concern. Before: points matching a referee concern *or* rated substantive, over
  all points. The new one counts substantive concerns no referee raised against
  precision, where the old one counted them for it.
- *Unique concerns:* substantive concerns the candidate raises that neither the plain
  prompt nor any referee raised. Before: referee concerns the candidate raised that the
  baseline did not. The new one is about concerns outside the referees' list; the old one
  was about concerns inside it.
- *Recall (U1):* pooled over concerns, with paper resampling for intervals and paired
  tests. Before: pooled for the headline, but `api/score.py` took per-paper means for the
  gain and its interval. That code still needs changing.

**Harness** (`eval/api/`). Every reviewer, judge, extraction and recognition call is a
script call to the Claude, Gemini or OpenAI API (`run.py`, `providers.py`), batch by
default, with the paper sent as the arXiv v1 PDF and cached. Settings are pinned in
`config.json`; every call's tokens and cost go to `eval/costs.csv`. `score.py` gives
recall, precision, unique concerns, a paired bootstrap interval and judge agreement.
Precision counts review points the judge labels as a referee concern or "substantive",
over all points; "referee precision" counts only the first kind. Unique concerns are
referee concerns an arm raised in some run that the baseline raised in none. The
experiment 11 reviews came from Claude Code agents with file access, so they are kept as
history and the baseline is rerun through the API.

### Plan runs

Every row is Claude-judged, provisional (U2). Model settings: effort high on every call;
batch mode. Recall and the other metrics as defined in `api/score.py`; full tables in
`eval/api/results/`.

| # | Date | Variant | Model | Papers | Runs | Recall | Top-k recall | Precision | False alarms (clean) | Unique | Cost | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 10-28 | Contamination probe (`recognize`), all31 | claude-opus-5-5 | 31 | 1 | | | | | | $0.13 | "Topic only" on all 31, tier C included; no authors or review history named. Self-report, so weak evidence |
| P2 | 10-28 | Referee recommendations (`recommend`), rec20 | claude-opus-5-5 | 20 | 1 | | | | | | $3.40 | 2 clean (2501.06460, 2503.17875), 18 contested |
| P3 | 10-28 | Rank step on the experiment 11 reviews | claude-opus-5-5 | 16 | 1 per arm | | | | | | $1.76 | Plain review splits into 42.1 concerns, v0.5 into 11.6 |
| P4 | 10-28 | Rescore experiment 11, judge v2: plain | judge claude-sonnet-5-5 | 16 | 1 | 31% (25 to 39) | 24% | 13% | 5.0 (2 papers) | | $1.81 both arms | Sonnet is stricter than judge.json (46%) |
| P4 | 10-28 | Rescore experiment 11, judge v2: v0.5 | judge claude-sonnet-5-5 | 16 | 1 | 12% (8 to 17) | 12% | 18% | 0.5 (2 papers) | not run | | 19 points below plain (14 to 26) |
| P5 | 10-28 | Rescore experiment 11, judge v2: plain | judge claude-opus-5-5 | 16 | 1 | 41% (33 to 49) | 30% | 15% | 5.0 (2 papers) | | $3.97 both arms | Second judge, Step 2 only |
| P5 | 10-28 | Rescore experiment 11, judge v2: v0.5 | judge claude-opus-5-5 | 16 | 1 | 14% (9 to 19) | 13% | 21% | 2.5 (2 papers) | not run | | 27 points below plain (21 to 34) |
| P6 | 10-28 | Cost check: plain prompt on pilot5 (API) | claude-opus-5-5; judge claude-sonnet-5-5 | 5 | 1 | 34% (20 to 54) | 25% | 13% | | | $2.71 | $0.54 per paper-run with one run (review $0.39, rank $0.07, judge $0.08). Recall equals the experiment 11 plain reviews on the same papers (34%) |
| P7 | 10-28 | Unique concerns of v0.5 against plain (`overlap`) | judges claude-sonnet-5-5, claude-opus-5-5 | 16 | 1 | | | | | 9 (Sonnet), 16 (Opus) | $0.30 | Substantive v0.5 points that neither plain nor any referee raised, summed over 16 papers |
| P8 | 10-28 | Rescore experiment 11, judge v2: plain | judge gemini-3.8-flash | 16 | 1 | 40% (31 to 50) | 28% | 14% | | | $1.87 both arms (two sync test calls included) | Second judge family |
| P8 | 10-28 | Rescore experiment 11, judge v2: v0.5 | judge gemini-3.8-flash | 16 | 1 | 14% (9 to 20) | 14% | 17% | | | | 26 points below plain |
| P8 | 10-28 | Rescore experiment 11, judge v2: plain | judge gemini-4-argon | 16 | 1 | 42% (34 to 51) | 30% | 17% | | | $2.89 both arms | Agrees best with Opus (kappa 0.84) |
| P8 | 10-28 | Rescore experiment 11, judge v2: v0.5 | judge gemini-4-argon | 16 | 1 | 15% (9 to 20) | 14% | 19% | | | | 27 points below plain |
| P9 | 10-28 | Gemini 4 Argon as plain-prompt reviewer, pilot5 | gemini-4-argon; judges claude-sonnet-5-5, claude-opus-5-5, gemini-3.8-flash | 5 | 1 | 2 to 3% (all three judges) | 2 to 3% | 3 to 7% | | | $0.30 reviews, about $1 rank and judges | Short, mostly positive reviews (1,300 words, 9 concerns); the Opus plain prompt is at 34 to 39% on the same papers. Five papers, one run: a probe only |
| P10 | 10-28 | Concern and recommendation extraction (`extract`, `recommend`), new36 (dev 14 + test 22) | claude-opus-5-5 | 36 | 1 | | | | | | $17.95 | 696 first-round concerns, 418 eligible (142 dev, 276 test; 14 dropped as about material absent from v1). 1 clean, 35 contested. 8 papers reviewed in a version that differs from v1 |
| P11 | 10-28 | Step 3 base reviewer: plain prompt ("Review this paper."), dev30 | claude-opus-5-5; rank claude-opus-5-5; judge gemini-4-argon | 30 | 3 | 42% (36 to 48) | 28% | 15% | 11.8 (3 papers) | not run | $50.01 | Base. 2,467 words, 40.9 concerns per review; 8.2 unmatched major points per paper |
| P11 | 10-28 | Step 3: OpenAIReview zero-shot prompt, verbatim (`arms/openaireview.txt`), dev30 | same | 30 | 3 | 29% (24 to 34) | 25% | 18% | 1.8 (3 papers) | not run | $48.18 | 14 points below plain (9 to 18). Fewer, longer concerns (20.4 per review), 2.2 unmatched major points per paper. Deviation: the paper goes in as the attached PDF, with the prompt's paper-text slot holding a placeholder |
| P11 | 10-28 | Step 3: Liang et al. prompt (`arms/liang.md`), dev30 | same | 30 | 3 | 42% (36 to 48) | 31% | 20% | 9.8 (3 papers) | not run | $46.48 | Ties plain on recall (+0, -3 to 3); top-k recall +3 points (1 to 5, p 0.015) and precision 20% against 15%, with 30.2 concerns per review. Deviation: venue changed from an ML conference to a top-tier physics journal, ChatGPT system line dropped |
| P12 | 10-28 | Step 3: MARG-S cost probe (`api/marg.py`, prompts verbatim in `arms/marg_s.json`), 1 paper of `marg10` | claude-opus-5-5, synchronous | 1 | 1 | | | | | | $7.44 | Drafts: 46 comments over the three sets ($5.06, plus $0.35 to recover JSON lists that the reference's 2,048-token turn cut off). Refinement measured on 3 comments: $0.64 and about 90 s each, so about $35 per 3-chunk paper and $350 or more for 10 papers. Stopped for David's decision |
| P13 | 10-28 | Step 3: MARG-S-NR (MARG-S without the refinement stage, as in the MARG paper; `marg.py --no-refine`), `marg10` | claude-opus-5-5, synchronous; rank claude-opus-5-5; judge gemini-4-argon | 10 | 1 | 62% (50 to 73) | 26% | 16% | | not run | $112.68 (reviews $103.09 with the P12 probe, rank $6.93, judge $2.66) | Recall +17 points over plain on the same 10 papers (9 to 27, p 0.013), from 70.6 concerns and 6,408 words per review against 43.1 and 2,513. At 43 points each MARG leads (56% against 44%); cut to plain's word count it ties (44%); top-k recall (26%) and precision (16%) tie. Three plain runs pooled reach 57% for $1.63 (`eval/step3-report.md`); 11.8 unmatched major points per paper against 7.8. About $10 per review against $0.55 for plain. Same papers: plain 44%, Liang et al. 45% (top-k 28%, precision 23%), OpenAIReview 29%. One run against three; the agents read pdftotext text, the other arms the PDF |
| P14 | 10-28 | Follow-up test A: three Liang et al. runs merged into one prioritized review (`run.py merge`, `prompts/merge.md`), dev30 | claude-opus-5-5 merge; rank claude-opus-5-5; judge gemini-4-argon | 30 | 1 | 53% (46 to 59) | 31% | 21% | | | $9.83 (merge, rank, judge; the three runs already existed) | +11 points over one Liang et al. run (9 to 13, p < 0.001), the full three-run union, in 3,122 words against 7,242; better on 25 of 30 papers. Tier A holds 37% of points and 64% of the referee majors caught |
| P15 | 10-28 | Follow-up test B: Liang et al. plus MARG's claims-to-experiments protocol, hidden assumptions, figure check and triage tiers (`arms/liangplus.md`), marg10 | claude-opus-5-5; judge gemini-4-argon | 10 | 3 | 47% (37 to 56) | 28% | 19% | | | $16.26 | +2 points over Liang et al. (−3 to 5), not significant; precision 19% against 23%. Tier A: 37% of points, 70% of referee majors caught |
| P16 | 10-28 | Follow-up test D: B plus the CMP checklist from 20 dev papers outside marg10 (`arms/liangplus_cmp.md`), marg10 | claude-opus-5-5; judge gemini-4-argon | 10 | 3 | 49% (40 to 58) | 29% | 19% | | | $17.37 | +4 points over Liang et al. (−1 to 9, p 0.11); best short single review so far. Tier A: 35% of points, 70% of referee majors caught |
| P17 | 10-28 | Follow-up test C: the plain prompt asked for at least 70 concerns (`arms/plain70.md`), marg10 | claude-opus-5-5; judge gemini-4-argon | 10 | 1 | 61% (49 to 74) | 24% | 15% | | | $7.43 | +17 points over plain (11 to 24, p 0.002), equal to MARG-S-NR (62%) at $0.74 a review against $10.75: MARG's recall is length. 15.1 unmatched major points per paper |

### Step 0 and Step 2 results (2026-10-28)

Claude-judged, provisional, except rows P8 and P9 (Gemini). Tables:
`eval/api/results/2026-10-28-*.md`.

**Harness.** Built as planned: the `rank` step, judge prompt v2 (`api/prompts/judge_v2.md`),
blinding (`api/blind.py`: model, product and company names, the provenance line and
markdown cues stripped; one review per call; referee concerns and review points in a seeded
random order), `recommend` and `apply-recommend`, an `overlap` step for unique concerns,
`score.py metrics` (every U1 and U3 metric, split clean and contested), `split.py` and
`judge_audit.py --judge`. A bug from 2026-10-27 is fixed: Claude batch `custom_id` must
match `[a-zA-Z0-9_-]`, so no batch could have been sent before. Blinding removes names and
formatting; a v0.5 report still reads as a lookalike table, so its structure is a cue the
judge can see.

**Judge agreement** on raised, partly or not raised, 426 concern calls (213 concerns × 2
reviews), five judges: judge.json (experiment 11), Sonnet 5.5, Opus 5.5, Gemini 3.8 Flash
and Gemini 4 Argon. Every pair clears the 0.6 bar overall.

| Pair | Agreement | Kappa | On v0.5 | On plain |
|---|---|---|---|---|
| Opus 5.5 vs Gemini 4 Argon | 90% | 0.84 | 0.83 | 0.82 |
| Gemini 3.8 Flash vs Gemini 4 Argon | 87% | 0.78 | 0.78 | 0.75 |
| judge.json vs Opus 5.5 | 85% | 0.77 | 0.78 | 0.71 |
| Opus 5.5 vs Gemini 3.8 Flash | 85% | 0.74 | 0.74 | 0.71 |
| judge.json vs Gemini 4 Argon | 83% | 0.73 | 0.73 | 0.68 |
| Sonnet 5.5 vs Opus 5.5 | 81% | 0.69 | 0.74 | 0.62 |
| Sonnet 5.5 vs Gemini 4 Argon | 78% | 0.65 | 0.67 | 0.60 |
| judge.json vs Gemini 3.8 Flash | 77% | 0.63 | 0.64 | 0.57 |
| judge.json vs Sonnet 5.5 | 76% | 0.62 | 0.70 | 0.51 |
| Sonnet 5.5 vs Gemini 3.8 Flash | 77% | 0.61 | 0.63 | 0.56 |

Sonnet 5.5, the U2 main judge, is the outlier: the strictest judge and the lowest
agreement with every other judge. Of 130 concerns judge.json called raised, it calls 37
partly. Plain recall is 46% under judge.json, 40 to 42% under Opus and both Gemini models,
31% under Sonnet. Opus 5.5 and Gemini 4 Argon, from different model families, agree best
(0.84), which makes either a better main judge than Sonnet on this evidence. Changing the
main judge is David's call (U2). The 50-call audit (`judge-audit.md`, Sonnet calls, method
key at the end) lets David check the disputed calls by hand.

**Rescore of the 16 papers under U1 and U3.** The direction holds under all four new
judges, Gemini included: v0.5 is 19 (Sonnet), 26 (Gemini Flash), 27 (Opus, Gemini Argon)
points below plain on pooled recall; the Claude-judged numbers are and 13 or 16 below on
top-k recall (k = 12). v0.5 has the higher precision (18% against 13% with Sonnet), since
it makes fewer points (11.6 against 42.1 per review). Plain makes about 5 major
substantive points per paper that match no referee concern, v0.5 about 1. On the 2 clean
papers that count is the false-alarm rate: 5.0 per paper for plain, 0.5 (Sonnet) or 2.5
(Opus) for v0.5. Two clean papers are too few to read anything from. Severity agreement is
undefined: every review, plain and v0.5, recommends major revision, so the reviewer
verdict has no spread to correlate. Unique concerns (P7): v0.5 raised 9 (Sonnet) or 16
(Opus) substantive concerns that neither plain nor any referee raised, across the 16
papers.

**Clean and contested.** 2 of the 16 judged papers are clean, 14 contested; with the 4
concern-only papers, 2 of 20. The extractor inferred most recommendations (Nature
Communications referees rarely use the four words), so the label rests on its reading;
`score.py labels --set rec20` lists each referee's level and whether it was explicit.

**Power with pooled recall** (`power.py`, default settings). Pooled recall gives more power
than per-paper recall on single-run designs. Five cells move more than 10 points from the
plan's table, all upward: 16 × 1 detects 10 points 76% of the time (plan 64%), 30 × 1 96%
(84%), 50 × 1 detects 5 points 71% (53%), 80 × 1 87% (72%), 120 × 1 96% (85%). The
three-run designs stay within 10 points (30 × 3: 81%, 100%, 100%). The concern counts are
the full 16-paper distribution, 2 to 24 per paper. The sensitivity tables are in
`api/results/2026-10-28-power-pooled.md`.

**Contamination.** Opus 5.5 recognized none of the 31 papers, tier C included. The plan's
second check, plain recall on tier C against tiers A and B, needs plain reviews of tier C
papers, which only 4 have concerns for so far.

**Cost.** Measured per call, batch prices:

| Call | Measured | Tokens in / out |
|---|---|---|
| Opus 5.5 plain review | $0.39 mean (one read the paper from cache at $0.12; the others $0.42 to $0.53) | 73K / 16K |
| Opus 5.5 rank, plain review | $0.08 | 7K / 6K |
| Sonnet 5.5 judge v2 | $0.06 | 34K / 2K |
| Opus 5.5 judge v2 | $0.12 | 34K / 2K |
| Opus 5.5 recommend | $0.17 | 80K / 1K |

A plain paper-run (review, rank, Sonnet judge) is about $0.53 with one run per paper. With
three runs the paper is written to the cache once and read twice, which brings the review
to about $0.26 and the paper-run to about $0.40. Thinking at high effort is most of the
output. The plan assumed $0.25.

**Budget, replaced** (Claude only, measured cost, three runs per paper):

| Step | Plan | Measured basis |
|---|---|---|
| 0 to 2 | $20 | $13.37 spent; about $10 left (pilot judge, overlap, tier C plain runs) |
| 3 bake-off | $165 to $225 | 3 one-call reviewers × 30 papers × 3 runs × $0.40 = $108, plus MARG on 10 papers ($60 to $120): $170 to $230 |
| 4 loop | $135 to $270 | 3 to 5 rounds × 90 paper-runs × $0.40: $110 to $180 |
| 5 library | $30 | about $40 |
| 6 test | $70 | 2 arms × 3 runs × 50 papers × $0.40 = $120 (fewer papers if the test set stays near 22) |
| **Total** | **$420 to $600** | **about $450 to $580** |

### Step 0: checks of the plan (2026-10-27)

**Power.** `eval/power.py` reimplements the simulation without Bill's code: per-concern
latent ease with a paper effect, calibrated to 46% recall, a 70% run-to-run repeat rate
and the observed paper-to-paper spread of 0.20, a gain that varies by paper (latent sd
0.25), and a paired one-sided t-test over papers. Every cell is within 6 points of the
plan's table, so none is flagged.

| Papers × runs | Detect 5 pts | Detect 10 pts | Detect 15 pts | Plan's table |
|---|---|---|---|---|
| 16 × 1 | 27% | 63% | 88% | 27, 64, 90 |
| 30 × 1 | 38% | 85% | 99% | 40, 84, 99 |
| 50 × 1 | 56% | 97% | 100% | 53, 96, 100 |
| 80 × 1 | 72% | 100% | 100% | 72, 99, 100 |
| 120 × 1 | 86% | 100% | 100% | 85, 100, 100 |
| 16 × 3 | 47% | 92% | 100% | 53, 92, 100 |
| 30 × 3 | 70% | 99% | 100% | 72, 99, 100 |
| 50 × 3 | 87% | 100% | 100% | 90, 100, 100 |

Sensitivity (`--sensitivity`): for 30 papers × 3 runs, power to detect 5 points is 63%
at a 65% repeat rate, 81% at 77%, 52% when the gain varies twice as much by paper, and 79%
when it doesn't vary. One correction to the plan: papers and runs buy the same power only
when the gain is the same on every paper. With a gain that varies by paper, extra runs
help less than extra papers (16 × 3 gives 32% against 49% for 50 × 1 at 5 points), which
strengthens the plan's advice to prefer papers.

**Prices and credits.** Claude prices match the official page (checked 2026-10-27): Opus
5.5 batch $2 in and $10 out per million tokens, so 50K in and 10K out is $0.20; Sonnet
5.5 batch $1 and $5, $0.10. Cache reads on both are 5% of the input price. Max 5x gets $100
and Max 20x $200 of monthly API credit; credits don't roll over, require seven days on an
eligible plan (an upgrade from 5x to 20x gives prorated credit at once), go to one linked
Console organization, and API use stops when they run out unless other credit exists. The
Gemini and OpenAI pricing pages were not reachable from this session, so those prices and
model IDs are unchecked. Third-party pages suggest the flagship models cost more than the
plan's $0.05 to $0.10 per review: GPT-5.5 is listed at $5 in and $30 out (about $0.28 per
review at batch rates), Gemini 3.1 Pro at about $2 in and $12 out (about $0.11). A
flagship non-Claude judge reading the paper text, the concerns and one review would be
nearer $0.10 to $0.20 a call than $0.05.

**Model snapshots.** Claude 5 models have no dated IDs; `claude-opus-5-5` is the full ID.
Pinning means recording it with its settings and the run date.

**Referee agreement ceiling.** On the 15 judged papers with two or more referees, one
referee raised on average 12% of another referee's eligible concerns (76 referee pairs,
`score.py ceiling`). Referees overlap little, so recall against the pooled concerns of
three referees is a high bar, and 46% is already well above what one referee matches.

**Five-concern minimum.** 13 of the 16 judged papers have at least 5 eligible concerns;
2509.04209, 2606.31267 and 2503.17875 fall below it.

**Judge audit.** `eval/judge-audit.md` has 30 random judge calls from experiment 11 (12
raised, 6 partly, 12 not raised), method hidden, for a hand check. `judge_audit.py`
regenerates it.

### Step 1: the pool, counted (2026-10-27)

`eval/referee/pool.json` lists new experimental condensed matter papers, beyond the 31 in
`papers.json`, that have a public peer review file and an arXiv v1 posted before
acceptance. Subject sorting was by an agent from titles and, for 46 unclear ones,
abstracts, so it needs a spot-check.

| Journal | Post-cutoff (Jul 1 to Oct 27) | Early (Jan 1 to Jun 30) |
|---|---|---|
| Nature Communications | 31 | 87 |
| Nature | 3 | 5 |
| Communications Materials | 1 | 1 |
| Nature Physics | 0 | 3 |
| Communications Physics | 0 | 2 |
| Nature Nanotechnology | 0 | 1 |
| SciPost Physics | 0 | 2 |
| **Total** | **35** | **101** |

- With the 16 post-cutoff papers already judged, 51 post-cutoff papers have files now.
  About 14 more Nature Communications papers should reach PMC within weeks.
- 77 post-cutoff papers in Communications Physics, Nature Physics, Communications
  Materials, Nature Materials, Nature and Nature Nanotechnology are not in PMC, and
  nature.com returns 403 here, so their peer review files are out of reach for now.
- Flags: 30 papers have a v1 posted more than 30 days after submission (it may carry
  revisions), and 12 are transfers whose earlier rounds are missing. 12 files with only a
  sign-off were rejected. Looser filters would add about 52 borderline papers (qubit
  hardware, devices, soft matter, nanophotonics) and about 25 whose v1 came after
  acceptance.
- SciPost: both qualifying papers are early. scipost.org returns 403 here, so the reports
  themselves can't be read yet.
- Concerns are not yet extracted, so the five-concern minimum will cut these numbers.

Proposed split: the 16 judged papers go to dev, since their misses were already read in
experiment 11. The 35 new post-cutoff papers, plus the Nature Communications ones as they
reach PMC, are the test set (about 45 to 49 before the five-concern cut). Dev is topped
up from tier C and the early window, reported separately.

**Not done yet.** Measured cost per paper-run (step 0.2), the contamination probe on tier C
(step 0.4) and judge re-runs (step 2) all need API keys.

## Next session: start here

State on 2026-10-28, end of the fourth session that day. Branch
`claude/youthful-mendel-hww024`, PR #34 (PRs #31 to #33 merged). Spend so far $343.96, of which
Step 3 is $308.25; every call in `eval/costs.csv`.

**Keys and access.** `CMP_EVAL_ANTHROPIC_KEY` works; `ANTHROPIC_API_KEY` not set.
`GEMINI_API_KEY` works for `gemini-4-argon` and `gemini-3.8-flash`. Gemini counts thinking in
its output limit, so `config.json` gives each Gemini model its own `max_output`. Gemini Tier 1
allows 5M tokens of active batch requests per model; a larger submission gets 429, and
`run.py send` resubmits the rest on the next pass. David allowed nature.com and
static-content.springer.com on 2026-10-28; nature.com sends automated requests to its login
page, and its peer review files are on springer, which answers.

**Batch watch.** Every batch on 2026-10-28 took 1.6 to 8.1 min except one 10-request Opus
rank batch for MARG: 0 of 10 done at 61 min. It was cancelled by hand and dropped from
`batches.json`, so the 8 requests that had finished by then were never collected (their cost
is logged since, $1.40) and were paid for again as synchronous calls. `run.py` now guards
against both: each submit adds a one-request canary batch; `status` and `collect` log every
poll to `api/batch_log.csv` and flag a batch STALLED past 30 min with nothing new for 15
(canary still pending: provider queue; canary done: this batch's requests); `rescue --batch`
cancels and leaves the record for `collect`, which saves what finished; `collect --wait`
polls each minute and exits 3 at a stall, for a background runner; `--sync --parallel N`
reruns what is missing. Responses cut off at their token limit print TRUNCATED.

**Decided by David (U5).** Gemini 4 Argon is the main judge (`config.json` `main_judge`,
the default for `run.py judge` and `score.py`); Opus 5.5 stays the reviewer. The split is
dev 30 (`sets.json` `dev30`: the 16 judged + `dev14`) and test 22 (`test22`). Concerns and
recommendations for all 36 new papers are extracted into `referee.json` (P10). Papers found
after the split go to the reserve.

**Step 3 result (P11 to P17).** On 30 dev papers × 3 runs, judged by Argon: plain 42%, Liang et
al. 42%, OpenAIReview 29%. MARG-S-NR on 10 of those papers reaches 62%, and the plain prompt asked
for 70 concerns reaches 61% at $0.74 a review: MARG's recall is length. Merging three Liang et
al. runs keeps their full union (+11 points on dev30) in 1.3 times one review's length. Liang et
al. with MARG's protocol and the CMP checklist (D) is the best short review (49% against 45%,
not yet significant). Triage tiers put 64 to 70% of the referee majors caught into tier A; the
order of points (top-11 recall) did not improve under any variant. Analysis and plan:
`eval/step3-report.md`, `eval/step4-plan.md`. Step 3 cost $308.25 (P11 $144.67, P12 and P13
$112.68, P14 to P17 $50.90).

**Still open.**
1. Full MARG-S (with refinement) was not run: about $35 per paper (P12).
2. Only 3 of 52 papers are clean (2501.06460, 2503.17875 and one new paper), so the
   false-alarm rate and every clean-paper figure rest on very few papers.
3. The overlap step (unique concerns) has not run for Step 3.

**Eligible concerns for new papers.** Papers without an experiment 11 `judge.json` have no
fixed-in-v1 marks; their eligible concerns drop the ones the extractor marked `in_v1: false`
(14 of 696). The judge's per-review `fixed_in_v1` is recorded but not used for eligibility.

**Pool** (`referee/pool.json`, retrieved 2026-10-28). 228 core papers with a usable file, 90
post-cutoff and 138 early; 73 borderline; 94 pending; 535 rejected. The springer recheck
moved 116 pending papers: 91 to core (54 post-cutoff, 37 early), 21 to borderline and 4 to
rejected (Nature Communications files holding only a one-page transfer sign-off). The 94 still
pending have no peer review file at MOESM1 to MOESM12, mostly a Supplementary Information file
only, so their authors probably did not opt in to published peer review. A missing springer
file answers 403 AccessDenied from Google Cloud Storage. `split.py --keep --write` keeps dev
30 and test 22 and puts the 54 new post-cutoff papers in the reserve (`referee/split.json`).

**In flight.** Nothing. API reviews are saved as `r<k>.txt`; `reviews()` only counts files
named `r<number>.txt`.

**Next steps, in order:**
1. Step 4 base: prompt D (`arms/liangplus_cmp.md`). Next tests (`eval/step4-plan.md`): D asked
   for more concerns, run three times and merged (exhaustive depth); a separate triage call for
   ranking; D on the other 20 dev papers to confirm its gain.
2. With David's OK, top test up toward the plan's 50 from the reserve (no test paper has been
   run yet), then extract concerns for the added papers (about $0.34 per paper).
3. Overlap step for Liang and OpenAIReview against plain (`run.py overlap`, Argon).
4. David checks `judge-audit.md`; regenerate it from Argon on Step 3 runs
   (`judge_audit.py --judge gemini --n 50`).

## Still open

- **No physicist ratings.** `eval/ratings/<id>.md` lists every flag and question from
  experiment 3 with blank columns for a physicist to rate. Until someone does,
  "reasonable" is unmeasured.
- **Follow-up in 2027.** `eval/followup.md` records each new paper's state on 2026-10-23;
  `scripts/followup.py` checks for new versions, comments and replies, due April to
  October 2027.
- **Sample report.** `sample-report.md` and `sample-report-anonymized.md` were made with
  v0.4 for showing physicists, before the referee match. Worth replacing with a report
  from the MVP if it passes.

## Limitations

- One model throughout, as assistant, baselines and judge. Judge calls are judgment calls;
  their notes list the hard ones.
- "Careful" papers were chosen by an agent.
- The v0.4 planted pair and all of experiment 8 ran on extracted text only.
- In experiment 8 the paper paths seen by the runs included a parent folder named
  `planted2`, though no run mentioned it.
