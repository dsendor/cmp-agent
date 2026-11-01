# Step 3 follow-up analysis (marg10)

Claude-judged, provisional (judge Gemini 4 Argon). 10 papers, 133 eligible referee concerns (83 major).

## 1. Recall at k (point-level matches among the top k ranked points, mean over runs)

| Reviewer | Points per review | k=5 | k=11 | k=20 | k=30 | k=43 | k=60 | all | Concern-level recall |
|---|---|---|---|---|---|---|---|---|---|
| Plain | 43.1 | 15% | 26% | 36% | 43% | 44% | 44% | 44% | 44% |
| Liang et al. | 30.7 | 16% | 28% | 37% | 44% | 45% | 45% | 45% | 45% |
| OpenAIReview | 22.4 | 15% | 24% | 28% | 29% | 29% | 29% | 29% | 29% |
| MARG-S-NR | 70.6 | 12% | 26% | 35% | 48% | 56% | 60% | 62% | 62% |

**Word-matched.** Each MARG-S-NR review cut to its top k points, k chosen per paper so the points kept are about as long as that paper's mean Plain review (MARG points average more words):

MARG-S-NR at Plain's length: 44% (mean k 28); Plain: 44%.

## 2. Union of runs: what more draws of a cheap reviewer buy

A concern counts if any review in the combination raised it (concern-level verdict).

| Combination | Reviews | Recall | Major concerns | Cost (reviews, rank, judge) | Words to read |
|---|---|---|---|---|---|
| Plain, 1 run | 1 | 47% | 58% | $0.54 | 2,513 |
| Plain, 2 runs | 2 | 55% | 67% | $1.09 | 5,026 |
| Plain, 3 runs | 3 | 57% | 69% | $1.63 | 7,539 |
| Liang et al., 1 run | 1 | 43% | 53% | $0.50 | 2,449 |
| Liang et al., 3 runs | 3 | 56% | 69% | $1.50 | 7,346 |
| Plain 1 + Liang et al. 1 | 2 | 53% | 64% | $1.04 | 4,962 |
| Plain 3 + Liang et al. 3 | 6 | 67% | 78% | $3.13 | 14,886 |
| MARG-S-NR, 1 run | 1 | 62% | 72% | $10.75 | 6,408 |
| MARG-S-NR + Plain 1 | 2 | 66% | 78% | $11.29 | 8,921 |
| Everything | 10 | 74% | 86% | $15.43 | 30,114 |

Paper-bootstrap differences in recall: MARG-S-NR minus Plain 3 runs +5 pts (95% CI -5 to +14); MARG-S-NR minus Liang et al. 3 runs +6 pts (95% CI -5 to +15); Plain 3 + Liang et al. 3 minus MARG-S-NR +5 pts (95% CI -2 to +15); MARG-S-NR minus Plain 1 run +14 pts (95% CI +6 to +24).

## 3. Overlap: MARG-S-NR (1 run) against Plain (3 runs) and Liang et al. (3 runs)

| Raised by | Concerns | Major | Share of all eligible |
|---|---|---|---|
| Both | 73 | 54 | 55% |
| MARG-S-NR only | 9 | 6 | 7% |
| Plain or Liang et al. only (any of 6 reviews) | 16 | 11 | 12% |
| Nobody | 35 | 12 | 26% |

By referee category:

| Category | Eligible | MARG-S-NR (1) | Plain (3 runs) | Liang et al. (3 runs) | MARG-S-NR only |
|---|---|---|---|---|---|
| alternative explanation | 27 | 63% | 67% | 59% | 1 |
| analysis or numbers | 29 | 55% | 55% | 55% | 0 |
| data selection or reproducibility | 10 | 40% | 70% | 60% | 0 |
| missing control or measurement | 31 | 68% | 52% | 52% | 5 |
| theory or modelling | 36 | 67% | 53% | 56% | 3 |

The concerns only MARG-S-NR raised, against all six Plain and Liang et al. reviews:

- 2601.01843 C1 (major, alternative explanation): The analysis assumes triplet p-wave BTK throughout without showing that singlet s- or d-wave pairing cannot explain the spectra.
- 2602.11302 C9 (major, missing control or measurement): The link between the measured speckle/diffraction pattern and the metallic/insulating domain distribution is asserted but not demonstrated with representative data.
- 2603.03092 C13 (minor, theory or modelling): The roughness analysis relies on RMS amplitude and does not systematically examine lateral correlation length or high-frequency components.
- 2603.03092 C14 (minor, theory or modelling): The separate contributions of edge-localized and bulk-distributed disorder to flat-band suppression are not distinguished.
- 2512.19052 C2 (major, missing control or measurement): Temperature-dependent retention/decay of the memory state is needed to test for Arrhenius activation matching the dielectric peak, distinguishing PNR relaxation from trap emission.
- 2512.19052 C11 (major, missing control or measurement): No verification of how AlOx thickness controls vacancy concentration and 2DEG carrier density.
- 2508.17861 C7 (major, theory or modelling): The Kondo exclusion uses a single-impurity Anderson model although 13% of sites host the peak, so a Kondo-lattice treatment may be needed.
- 2508.17861 C8 (minor, missing control or measurement): All data are on 0.5% Se-doped crystals; it is unclear whether the physics holds in pristine 4Hb-TaS2.
- 2508.17861 C24 (major, missing control or measurement): The 1T zero-bias dip is called superconducting without a vortex map or detailed temperature and field evolution with fits.

## 4. Which MARG-S-NR agent group raised each matched concern

| Agent group | Comments | Ranked points | Eligible concerns matched | of them MARG-only |
|---|---|---|---|---|
| experiments and claims | 138 | 284 | 56 | 6 |
| novelty and impact | 196 | 237 | 34 | 4 |
| clarity and reproducibility | 270 | 185 | 16 | 2 |

Matched by one group only: experiments and claims 33, novelty and impact 17, clarity and reproducibility 9; by any group: 82.

## 5. Per paper

| Paper | Eligible | Chunks | Plain (mean of 3) | Plain (3-run union) | Liang et al. (mean) | MARG-S-NR | MARG-S-NR only |
|---|---|---|---|---|---|---|---|
| 2512.05873 | 7 | 3 | 33% | 57% | 38% | 29% | 0 |
| 2511.21968 | 8 | 4 | 42% | 50% | 62% | 75% | 0 |
| 2601.01843 | 24 | 8 | 61% | 71% | 58% | 71% | 1 |
| 2602.11302 | 12 | 4 | 36% | 50% | 36% | 50% | 1 |
| 2512.04975 | 9 | 5 | 44% | 44% | 52% | 44% | 0 |
| 2503.17875 | 2 | 4 | 100% | 100% | 100% | 100% | 0 |
| 2603.03092 | 13 | 8 | 54% | 77% | 51% | 100% | 2 |
| 2512.19052 | 24 | 4 | 51% | 67% | 43% | 67% | 2 |
| 2508.17861 | 24 | 3 | 22% | 29% | 26% | 50% | 3 |
| 2603.02450 | 10 | 6 | 37% | 60% | 37% | 40% | 0 |

## 6. What the extra volume is made of (judge ratings of every ranked point)

| Reviewer | Points | Substantive | Generic | Incorrect | Substantive matching a referee | Major unmatched substantive per review |
|---|---|---|---|---|---|---|
| Plain | 43.1 | 99% | 0% | 0% | 16% | 7.8 |
| Liang et al. | 30.7 | 100% | 0% | 0% | 23% | 6.1 |
| OpenAIReview | 22.4 | 100% | 0% | 0% | 20% | 2.7 |
| MARG-S-NR | 70.6 | 96% | 2% | 2% | 16% | 11.8 |

Cost per review on these papers (review, rank and judge): Plain $0.54, Liang et al. $0.50, OpenAIReview $0.52, MARG-S-NR $10.75.
