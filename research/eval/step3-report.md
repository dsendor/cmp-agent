# Step 3 report: what MARG's recall is made of, and what to borrow

*Claude-judged, provisional. Every verdict below is Gemini 4 Argon matching review points to
referee concerns (U5 in `../eval.md`); no physicist has rated any of it. Written 2026-10-28 for
David. It builds on `../eval.md` rows P11 to P13; every number comes from the saved judge files
through `step3_analysis.py`, whose full output is `api/results/2026-10-28-step3-analysis.md`.
Producing it cost nothing. The follow-up tests below ran afterwards and cost $50.90.*

## Follow-up tests: read this first

David approved the three tests at the end of this report and asked for a fourth, a
CMP checklist. They ran on 2026-10-28; full tables in `api/results/2026-10-28-step3-followup.md`
(`step3_analysis.py followup`), rows P14 to P17 in `../eval.md`. Tests B, C and D use the
`marg10` papers with three runs each (C one run); test A uses all 30 dev papers.

| Test | What changed | Recall | Change (95% CI) | Top-11 | Precision | Words | Cost per review |
|---|---|---|---|---|---|---|---|
| Plain (base for C) | | 44% | | 26% | 16% | 2,513 | $0.54 |
| **C** | Plain prompt, "raise at least 70 concerns" | **61%** | +17 (11 to 24), p 0.002 | 24% | 15% | 4,334 | $0.74 |
| MARG-S-NR | multi-agent, one run | 62% | +17 (9 to 27) | 26% | 16% | 6,408 | $10.75 |
| Liang et al. (base for B, D) | | 45% | | 28% | 23% | 2,449 | $0.50 |
| **B** | Liang et al. + MARG claims-to-experiments, hidden assumptions, figure check, triage tiers | 47% | +2 (−3 to 5) | 28% | 19% | 2,536 | $0.54 |
| **D** | B + the CMP checklist | 49% | +4 (−1 to 9), p 0.11 | 29% | 19% | 2,594 | $0.58 |
| Liang et al., dev30 (base for A) | one run | 42% | | 31% | 20% | 2,414 | $0.50 |
| **A** | three Liang et al. runs merged by one call | **53%** | +11 (9 to 13), p < 0.001 | 31% | 21% | 3,122 | about $1.40 |

What they settle:

1. **MARG's recall is length, and length is cheap.** The plain prompt asked for 70 concerns
   matches MARG-S-NR (61% against 62%) at a fourteenth of the cost, with the same top-11 and
   precision. MARG's multi-agent machinery adds nothing that a longer single call does not. The
   price of length is noise: 15.1 major points per paper that no referee raised, against 7.8 for
   the ordinary plain review and 11.8 for MARG.
2. **Merging runs keeps all of the extra recall at a fraction of the reading.** The merged
   review keeps the full three-run union (53%, the same as pooling the three reviews), in 3,122
   words against 7,242 for the three separate reviews, with precision unchanged. This is the
   strongest result: a significant +11 points; the merged review beats the single-run mean on 25 of 30 papers, ties on 4 and trails on 1.
3. **The borrowed MARG method helps a little; the CMP checklist a little more.** B adds 2
   points and D 4, neither significant on 10 papers, and both lose some precision (19% against
   23%). D is the best single short review measured so far (49% recall, 48% at 30 points).
4. **Triage works, ranking does not.** Tier A holds about 36% of each review's points and 64 to
   70% of the referees' major concerns the review caught: twice the concentration of an untiered
   list, so a Brief or Standard view (tier A, or A and B) keeps most of what matters. But the
   order within the list still does not improve: top-11 recall stays at 28 to 31% for every
   variant, triaged or not.

What changes in the plan (`step4-plan.md`):

- **Base prompt: D** (Liang et al. + MARG method + CMP checklist + triage tiers), pending a test
  on more papers, since its gain is not yet significant.
- **Exhaustive depth:** two cheap routes now, both far below MARG's price: ask for more concerns
  in one call (61%, $0.74, noisier) or merge three runs (+11 points, about $1.40, as precise as
  one run). The next test combines them: D asked for more, run three times and merged.
- **Ranking is the open problem.** A separate triage call that sees the paper and the full list
  is the next thing to try, measured by top-11 recall and tier-A concentration.
- **MARG is retired** as a candidate; it stays in the record as the reference that showed length
  was the lever.

## The question

MARG-S-NR (the multi-agent reviewer, one run) found 62% of the referees' eligible concerns on
10 dev papers. Plain found 44% and Liang et al. 45% on the same papers. Is that worth $10.75 a
review against about $0.50? Where does it help, how much of it overlaps with what the cheap
reviewers already find, and which parts of MARG can we take without paying for MARG?

## Short answer

1. **The recall is real, and it comes from MARG writing more good points, at the same density
   per word as Plain.** Point for point, MARG keeps finding concerns long after Plain has run
   out (56% against 44% at 43 points each). Word for word it ties Plain (44% each at Plain's
   length). It ranks no better: the top 11 points tie at 26%.
2. **Three cheap runs buy almost all of it.** The union of three Plain runs reaches 57%, and
   three Liang et al. runs 56%, at $1.50 to $1.63 a paper. MARG-S-NR is 5 to 6 points higher
   (95% CI about −5 to +15, so not distinguishable on 10 papers) at about 6.6 times the cost.
   Six cheap runs together reach 67% for $3.13, above MARG.
3. **MARG's distinct contribution is small and specific.** Of 133 eligible concerns, 9 were
   raised by MARG and by none of six Plain and Liang et al. reviews; 6 of the 9 are major, and
   8 are missing controls or theory and model assumptions. The six cheap reviews caught 16
   concerns MARG missed.
4. **One MARG agent group earns most of it.** The "experiments and claims" group matched 56 of
   MARG's 82 concerns, 33 of them raised by no other MARG group, and 6 of the 9 MARG-only
   concerns. Its method fits in one prompt.
5. **Recommendation, revised.** Keep Liang et al. as the Step 4 base, and add two borrowed
   pieces to it: MARG's claims-to-experiments protocol inside the single prompt (no added cost)
   and, where recall matters most, two or three independent runs merged into one ranked list
   (about three times the cost of one run, a sixth of MARG). MARG itself stays a reference
   arm. Three cheap tests below settle whether the borrowing works, for about $30 in total.

My earlier summary to you said MARG's gain was "volume, not ranking". Section 1 refines that: it
is volume of useful points at ordinary density, which is a better thing than padding.

## 1. Recall as a function of length

Each reviewer's points are ranked by the reviewer model itself (the `rank` step). Recall at k
counts the referee concerns matched by the top k points.

| Reviewer | Points per review | k=5 | k=11 | k=20 | k=30 | k=43 | all |
|---|---|---|---|---|---|---|---|
| Plain | 43.1 | 15% | 26% | 36% | 43% | 44% | 44% |
| Liang et al. | 30.7 | 16% | 28% | 37% | 44% | 45% | 45% |
| OpenAIReview | 22.4 | 15% | 24% | 28% | 29% | 29% | 29% |
| MARG-S-NR | 70.6 | 12% | 26% | 35% | 48% | 56% | 62% |

Read across a row and the curves tell the story. Plain and Liang et al. climb fast and flatten
by about 30 points: the last dozen points add almost nothing. MARG climbs at the same rate and
keeps climbing to 70 points. Its top of the list is no better (26% at k=11, against 26% and 28%),
so MARG's advantage lives entirely in the lower half of a long list.

MARG's points are also longer (about 91 words each against Plain's 58). Cut each MARG review
to the length of that paper's Plain review (its top 28 points on average) and it scores 44%,
exactly Plain's figure. So per word read, the two are equally productive; MARG simply does not
stop.

## 2. What more draws of a cheap reviewer buy

Two runs of the same prompt raise different concerns, so the union of several runs grows.

| Combination | Reviews | Recall | Major concerns caught | Cost per paper | Words to read |
|---|---|---|---|---|---|
| Plain, 1 run | 1 | 47% | 58% | $0.54 | 2,513 |
| Plain, 2 runs | 2 | 55% | 67% | $1.09 | 5,026 |
| Plain, 3 runs | 3 | 57% | 69% | $1.63 | 7,539 |
| Liang et al., 3 runs | 3 | 56% | 69% | $1.50 | 7,346 |
| Plain 1 + Liang et al. 1 | 2 | 53% | 64% | $1.04 | 4,962 |
| MARG-S-NR, 1 run | 1 | 62% | 72% | $10.75 | 6,408 |
| Plain 3 + Liang et al. 3 | 6 | 67% | 78% | $3.13 | 14,886 |
| All 10 reviews | 10 | 74% | 86% | $15.43 | 30,114 |

(Plain's first run happens to score 47% against its three-run mean of 44%: run-to-run spread is
a few points, and MARG has only one run.)

Paper-bootstrap differences: MARG minus three Plain runs, +5 points (95% CI −5 to +14); MARG
minus three Liang et al. runs, +6 (−5 to +15); six cheap runs minus MARG, +5 (−2 to +15). MARG
against a single Plain run, +14 (+6 to +24), is the only clear difference.

The words column is the catch for the unions: three runs repeat each other, so a reader would
need a merge step that removes duplicates and ranks the rest. That step is one cheap call and
is untested (test A below).

## 3. Overlap: who catches what

MARG-S-NR (one run) against all six Plain and Liang et al. reviews, over the 133 eligible
concerns:

| Raised by | Concerns | Major |
|---|---|---|
| Both | 73 (55%) | 54 |
| MARG-S-NR only | 9 (7%) | 6 |
| Plain or Liang et al. only | 16 (12%) | 11 |
| Nobody | 35 (26%) | 12 |

By the referees' own category of concern:

| Category | Eligible | MARG-S-NR | Plain, 3 runs | Liang et al., 3 runs | MARG only |
|---|---|---|---|---|---|
| Missing control or measurement | 31 | 68% | 52% | 52% | 5 |
| Theory or modelling | 36 | 67% | 53% | 56% | 3 |
| Alternative explanation | 27 | 63% | 67% | 59% | 1 |
| Analysis or numbers | 29 | 55% | 55% | 55% | 0 |
| Data selection or reproducibility | 10 | 40% | 70% | 60% | 0 |

MARG's edge is concentrated where its experiments agent is aimed: controls a paper should have
run and assumptions its model leans on. Its weak spot is data selection and reproducibility,
oddly the subject of one of its three agent groups. A likely cause: MARG's agents read the
paper as extracted text, without figures, while the other reviewers read the PDF.

The nine MARG-only concerns, for you to judge whether they are the kind a referee assistant
must catch:

- 2601.01843 C1 (major): the analysis assumes triplet p-wave BTK throughout without showing that
  singlet s- or d-wave pairing cannot explain the spectra.
- 2602.11302 C9 (major): the link between the speckle pattern and the metallic and insulating
  domains is asserted, never shown with representative data.
- 2603.03092 C13 and C14 (minor): roughness judged by RMS amplitude alone; edge and bulk disorder
  not separated.
- 2512.19052 C2 (major): temperature-dependent retention is needed to test for Arrhenius
  activation matching the dielectric peak.
- 2512.19052 C11 (major): no check of how AlOx thickness sets vacancy concentration and carrier
  density.
- 2508.17861 C7 (major): the Kondo exclusion uses a single-impurity model although 13% of sites
  host the peak.
- 2508.17861 C8 (minor): all data on 0.5% Se-doped crystals; unclear whether it holds in pristine
  4Hb-TaS2.
- 2508.17861 C24 (major): the 1T zero-bias dip is called superconducting without a vortex map or
  field and temperature fits.

These are good physics concerns, mostly "you have not run the control that would rule this
out". They cluster in three of the ten papers.

## 4. Which part of MARG did the work

MARG-S-NR runs three agent groups with different instructions. Tracing each ranked point back
to the group that wrote it (by quoted text; approximate):

| Agent group | Ranked points | Eligible concerns matched | Matched by this group alone | MARG-only concerns |
|---|---|---|---|---|
| Experiments and claims | 284 | 56 | 33 | 6 |
| Novelty and impact | 237 | 34 | 17 | 4 |
| Clarity and reproducibility | 185 | 16 | 9 | 2 |

The experiments-and-claims group carries MARG. Its instruction, in short, is a three-step method:
list the paper's claims; design the experiments and analyses you would need to support each one;
compare that list with what the paper did and write a comment for every gap. The novelty group
adds value through its skeptical expert, whose brief is to find hidden assumptions behind the
claims (the Kondo-lattice point is one). The clarity group adds the least.

## 5. Where MARG helped, paper by paper

| Paper | Eligible | Plain (mean of 3) | Plain (3-run union) | Liang et al. (mean) | MARG-S-NR | MARG only |
|---|---|---|---|---|---|---|
| 2512.05873 | 7 | 33% | 57% | 38% | 29% | 0 |
| 2511.21968 | 8 | 42% | 50% | 62% | 75% | 0 |
| 2601.01843 | 24 | 61% | 71% | 58% | 71% | 1 |
| 2602.11302 | 12 | 36% | 50% | 36% | 50% | 1 |
| 2512.04975 | 9 | 44% | 44% | 52% | 44% | 0 |
| 2503.17875 | 2 | 100% | 100% | 100% | 100% | 0 |
| 2603.03092 | 13 | 54% | 77% | 51% | 100% | 2 |
| 2512.19052 | 24 | 51% | 67% | 43% | 67% | 2 |
| 2508.17861 | 24 | 22% | 29% | 26% | 50% | 3 |
| 2603.02450 | 10 | 37% | 60% | 37% | 40% | 0 |

MARG's lead over the three-run union comes from three papers: 2508.17861 (an STM study whose
referees raised 24 concerns, many about alternative explanations of a spectral feature),
2603.03092 and 2511.21968. On two papers it trails the three-run union by 20 points or more, and
on the other five it ties. Nothing about paper length predicts
it: MARG split the papers into 3 to 8 chunks, and the gains do not follow the chunk count.

## 6. What the extra length costs the reader

| Reviewer | Points | Generic | Incorrect | Substantive points matching a referee | Major unmatched points per review | Reading time (250 words a minute) |
|---|---|---|---|---|---|---|
| Plain | 43.1 | 0% | 0% | 16% | 7.8 | 10 min |
| Liang et al. | 30.7 | 0% | 0% | 23% | 6.1 | 10 min |
| MARG-S-NR | 70.6 | 2% | 2% | 16% | 11.8 | 26 min |

Length is not free. MARG is the only reviewer with points the judge rated generic or incorrect
(about 3 of 71 per review), and it raises 11.8 major points per paper that no referee raised.
Some of those may be real problems the referees missed (the plan's U3 unique-concerns check,
not yet run on MARG, would tell), but a physicist has to read them all to find out. Liang et
al. has the highest share of points that match a referee concern (23%).

## 7. What nobody catches

35 eligible concerns (26%, 12 of them major) were raised by none of the 10 reviews per paper; 22
of those were at least partly raised by someone. The major ones fall in two kinds:

- **Reading the figures closely**: fits that look poor at two angles of Fig. 3a; Fig. 4d
  apparently inconsistent with the claim in Fig. 4e; data-to-parameter ratios and goodness of
  fit in the structural refinements.
- **A specialist's alternative explanation**: phase slips with local heating; a Fano or Kondo
  line shape; interband singlet formation in a periodic Anderson model; overdoping on the KTO
  phase diagram.

Neither more runs nor more agents reach these. A figure-consistency instruction might reach the
first kind cheaply. The second kind is what the library of lookalike checks was built for.

## Where MARG makes sense

- **An exhaustive pre-submission audit**, where an author wants every plausible objection and
  will spend half an hour triaging a 70-point list. MARG is the single best reviewer here, though
  three merged cheap runs come close for a sixth of the price.
- **A ceiling and a source of ideas** for the eval: as a reference arm it shows how much a
  reviewer can find when it never stops.

Where it does not:

- **A referee's assistant** that has to surface the few concerns that matter. MARG's top 11 tie
  Plain's, and its tail carries generic and incorrect points.
- **Anything run at scale**: at $10.75 a review the test set (22 papers × 3 runs) alone would
  cost about $700.

## What to borrow, cheapest first

| Idea from MARG | Cost per review | Evidence it helps | How to test |
|---|---|---|---|
| Claims-to-experiments protocol (list claims; design the experiments each needs; comment on every gap) inside the single prompt | none | its agent group raised 56 of MARG's 82 matched concerns and 6 of the 9 MARG-only ones | test B |
| Skeptic's pass for hidden assumptions behind each claim, in the same prompt | none | source of the Kondo-lattice and pairing-symmetry concerns | test B |
| Several independent runs, merged and ranked | about 3× one run | three runs reach 56 to 57%, within noise of MARG | test A |
| A figure-consistency instruction (check each figure against the claims made about it) | none | the largest group of concerns nobody caught | test B |
| Paper split into chunks across agents | not worth borrowing | built for 2023 context limits; it drops the figures | none |
| Per-comment refinement groups | not worth borrowing | $0.64 a comment (P12); untested gain | none |

## Three tests that settle it (about $30; run, results at the top)

- **A. Merge three existing runs (about $5).** The 90 Liang et al. reviews on dev30 already
  exist. One Opus call per paper merges a paper's three reviews into one deduplicated, ranked
  list; judge the 30 merged lists. Question: does the merged list keep the union's recall (about
  56%) at one review's length, and does its top 11 improve?
- **B. Liang et al. plus borrowed protocol (about $15).** A new prompt: Liang et al.'s, plus the
  claims-to-experiments method, the hidden-assumptions pass and the figure check, in one call.
  Run it on marg10 × 3 runs. Question: does a single cheap call move toward MARG's 62%?
- **C. Length control (about $8 on marg10 × 1).** The Plain prompt asked for at least 70
  concerns. Question: is MARG's tail a product of its method or of length alone? If Plain asked
  for 70 points reaches 60%, MARG's architecture adds nothing beyond its stamina.

If B lifts single-call recall by 5 points or more without a drop in precision, it becomes the
Step 4 base. If A works, merged runs become the delivery format for the exhaustive mode.

## What this rests on

Ten papers, one MARG run, one AI judge whose agreement with Opus is kappa 0.84 and with no
person yet. Recall counts referee concerns, so a reviewer is never credited for a real problem
the referees missed. Union recall is an upper bound until test A shows a merge keeps it. The
agent-group attribution in section 4 matches ranked points to MARG comments by quoted text and
is approximate.
