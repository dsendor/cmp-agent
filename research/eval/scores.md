## New papers: stability over repeated runs

| Paper | Runs | Flags per run | Mean pairwise Jaccard | Flags in every run | Ruled out per run |
|---|---|---|---|---|---|
| 2607.09511 | 3 | [3, 5, 4] | 0.60 | 2 | [1, 0, 0] |
| 2608.12897 | 3 | [6, 5, 4] | 0.31 | 2 | [0, 0, 0] |
| 2610.18817 | 3 | [3, 3, 4] | 0.83 | 3 | [0, 0, 0] |
| 2608.17404 | 3 | [16, 15, 16] | 0.74 | 13 | [0, 0, 0] |
| 2608.27444 | 3 | [5, 5, 3] | 0.54 | 3 | [0, 0, 0] |
| 2608.26022 | 3 | [3, 2, 3] | 0.78 | 2 | [0, 0, 0] |
| 2609.38003 | 3 | [2, 2, 3] | 0.78 | 2 | [0, 0, 0] |
| 2609.01233 | 1 | [4] | n/a | n/a | [0] |
| 2610.29124 | 1 | [5] | n/a | n/a | [0] |

## Planted test: status of the removed point, original runs vs planted runs

| Paper | Lookalike | Original runs | Planted runs |
|---|---|---|---|
| 2608.26022 | fine-tuning-and-selection | partly addressed, partly addressed, partly addressed | partly addressed, partly addressed, partly addressed |
| 2608.26022 | diode-vortex-screening | partly addressed, partly addressed, partly addressed | partly addressed, partly addressed, partly addressed |
| 2609.38003 | diode-vortex-screening | partly addressed, partly addressed, partly addressed | partly addressed, partly addressed, partly addressed |
| 2609.38003 | micromagnet-stray-field | absent, absent, partly addressed | partly addressed, partly addressed, absent |

## Known-outcome papers: recall and precision against the answer key

| Paper | Method | Recall | Precision (floor) |
|---|---|---|---|
| 1710.10701 | assistant | 4 of 4 | 6 of 13 |
| 1710.10701 | OpenAIReview prompt | 3 of 4 | 5 of 7 |
| 1710.10701 | plain prompt | 3 of 4 | 4 of 6 |
| 1204.4212 | assistant | 4 of 5 | 4 of 6 |
| 1204.4212 | OpenAIReview prompt | 4 of 5 | 4 of 5 |
| 1204.4212 | plain prompt | 2 of 5 | 2 of 3 |
| 1606.05712 | assistant | 1 of 2 | 1 of 5 |
| 1606.05712 | OpenAIReview prompt | 2 of 2 | 2 of 4 |
| 1606.05712 | plain prompt | 2 of 2 | 2 of 4 |
| 2207.02472 | assistant | 3 of 3 | 3 of 9 |
| 2207.02472 | OpenAIReview prompt | 2 of 3 | 2 of 7 |
| 2207.02472 | plain prompt | 2 of 3 | 2 of 7 |
| 1809.05513 | assistant | 2 of 2 | 2 of 12 |
| 1809.05513 | OpenAIReview prompt | 1 of 2 | 1 of 2 |
| 1809.05513 | plain prompt | 1 of 2 | 1 of 6 |

## New papers: what the baselines raised that the assistant also raised

| Paper | Assistant flags (any run) | OpenAIReview prompt | Plain prompt | Shared with OpenAIReview | Shared with plain |
|---|---|---|---|---|---|
| 2607.09511 | 5 | 4 | 5 | 3 | 3 |
| 2608.12897 | 10 | 3 | 2 | 3 | 2 |
| 2610.18817 | 4 | 3 | 2 | 2 | 1 |
| 2608.17404 | 20 | 3 | 8 | 3 | 8 |
| 2608.27444 | 7 | 1 | 4 | 1 | 3 |
| 2608.26022 | 3 | 4 | 3 | 2 | 2 |
| 2609.38003 | 3 | 2 | 3 | 1 | 2 |
| 2609.01233 | 4 | 2 | 5 | 1 | 2 |
| 2610.29124 | 5 | 4 | 5 | 2 | 2 |
