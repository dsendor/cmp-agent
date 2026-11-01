# Step 3 follow-up tests A to D

Claude-judged, provisional (judge Gemini 4 Argon). Recall is the concern-level verdict "raised" over eligible concerns; top-11 uses point-level matches among the reviewer's top 11 ranked points.

## Tests B, C, D on marg10 (the 10 MARG papers)

10 papers, 133 eligible concerns (83 major).

| Reviewer | Reviews | Recall | Top-11 | Top-30 | Union of runs | Words | Points | Tier A points | Referee majors caught in tier A |
|---|---|---|---|---|---|---|---|---|---|
| Plain | 30 | 44% | 26% | 43% | 57% | 2,513 | 43.1 |  |  |
| Liang et al. | 30 | 45% | 28% | 44% | 56% | 2,449 | 30.7 |  |  |
| B: Liang et al. + MARG protocol | 30 | 47% | 28% | 44% | 58% | 2,536 | 39.3 | 14.4 | 41% |
| D: B + CMP checklist | 30 | 49% | 29% | 48% | 61% | 2,594 | 40.5 | 14.3 | 42% |
| C: Plain asked for 70 | 10 | 61% | 24% | 40% | 61% | 4,334 | 90.3 |  |  |
| MARG-S-NR | 10 | 62% | 26% | 48% | 62% | 6,408 | 70.6 |  |  |

## Test A on dev30 (30 dev papers)

30 papers, 355 eligible concerns (227 major).

| Reviewer | Reviews | Recall | Top-11 | Top-30 | Union of runs | Words | Points | Tier A points | Referee majors caught in tier A |
|---|---|---|---|---|---|---|---|---|---|
| Liang et al. | 90 | 42% | 29% | 42% | 53% | 2,414 | 30.2 |  |  |
| A: 3 Liang et al. runs merged | 30 | 53% | 30% | 51% | 53% | 3,122 | 37.9 | 14.0 | 41% |
| Plain | 90 | 42% | 28% | 41% | 55% | 2,467 | 40.9 |  |  |

Cost per review on marg10 (review, rank and judge): B: Liang et al. + MARG protocol $0.54, D: B + CMP checklist $0.58, C: Plain asked for 70 $0.74.
