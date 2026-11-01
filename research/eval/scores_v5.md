## Status of every lookalike row, careful papers against the others

Each cell counts rows over all runs of that scale. Careful papers: 2608.17404, 2608.27444, 2608.26022, 2609.38003. Others: 2607.09511, 2608.12897, 2610.18817, 2609.01233, 2610.29124.

| Scale | Group | Rows | ruled out for the claim | tested in part | left open by the authors | not tested |
|---|---|---|---|---|---|---|
| v0.5 | careful | 52 | 0 (0%) | 42 (81%) | 1 (2%) | 9 (17%) |
| v0.5 | other | 41 | 1 (2%) | 32 (78%) | 0 (0%) | 8 (20%) |

| Scale | Group | Rows | ruled out | partly addressed | not addressed |
|---|---|---|---|---|---|
| v0.4 | careful | 86 | 0 (0%) | 77 (90%) | 9 (10%) |
| v0.4 | other | 50 | 1 (2%) | 44 (88%) | 5 (10%) |

## Per paper (v0.5 runs)

| Paper | Group | Runs | Rows per run | Ruled out for the claim | Not tested | Checks done | Flag Jaccard (v0.5) | Flag Jaccard (v0.4) |
|---|---|---|---|---|---|---|---|---|
| 2607.09511 | other | 2 | [5, 4] | [0, 1] | [0, 0] | 1/5, 1/5 | 0.60 | 0.60 |
| 2608.12897 | other | 2 | [4, 3] | [0, 0] | [2, 0] | 1/6, 1/6 | 0.40 | 0.31 |
| 2610.18817 | other | 2 | [3, 3] | [0, 0] | [0, 1] | 0/6, 0/6 | 0.50 | 0.83 |
| 2608.17404 | careful | 2 | [14, 14] | [0, 0] | [4, 3] | 0/9, 0/9 | 1.00 | 0.74 |
| 2608.27444 | careful | 2 | [4, 3] | [0, 0] | [0, 0] | 1/6, 1/6 | 0.75 | 0.54 |
| 2608.26022 | careful | 2 | [3, 4] | [0, 0] | [0, 0] | 0/3, 0/3 | 0.40 | 0.78 |
| 2609.38003 | careful | 2 | [5, 5] | [0, 0] | [1, 1] | 0/3, 0/3 | 1.00 | 0.78 |
| 2609.01233 | other | 2 | [3, 4] | [0, 0] | [0, 0] | 0/6, 0/6 | 0.40 | n/a |
| 2610.29124 | other | 2 | [5, 7] | [0, 0] | [2, 3] | 0/3, 1/7 | 0.20 | n/a |

## Tests shown, careful papers against the others (v0.5)

Every test of every lookalike row, marked all, part or no. Library rows only (outside rows set their own tests).

| Group | Tests | all | part | no |
|---|---|---|---|---|
| careful | 96 | 17 (18%) | 46 (48%) | 33 (34%) |
| other | 59 | 14 (24%) | 28 (47%) | 17 (29%) |

## Checks marked done, careful papers against the others

| Scale | Group | Checks | done | partly | not done |
|---|---|---|---|---|---|
| v0.5 | careful | 42 | 2 (5%) | 33 (79%) | 7 (17%) |
| v0.5 | other | 56 | 5 (9%) | 39 (70%) | 12 (21%) |
| v0.4 | careful | 63 | 0 (0%) | 55 (87%) | 8 (13%) |
| v0.4 | other | 62 | 4 (6%) | 46 (74%) | 12 (19%) |

## Known-outcome papers (v0.5): recall and precision against the answer key

A key explanation counts as found when the run gives it any status except ruled out for the claim.

| Paper | Recall | Precision (floor) | Statuses of the key explanations |
|---|---|---|---|
| 1710.10701 | 4 of 4 | 6 of 11 | fine-tuned-plateau: tested in part; disorder-induced-zbp: tested in part; quasi-majorana-smooth-confinement: not tested; one-end-only: not tested |
| 1204.4212 | 4 of 5 | 4 of 6 | shapiro-landau-zener: tested in part; shapiro-nonlinear-resistance: tested in part; switching-jump-blind-region: tested in part; heating: absent; fine-tuning-and-selection: tested in part |
| 1606.05712 | 1 of 2 | 1 of 4 | chiral-plateau-superconductor-short: tested in part; percolation: absent |
| 2207.02472 | 3 of 3 | 3 of 7 | protocol-parameter-sensitivity: tested in part; trivial-andreev-band-gap-reopening: tested in part; fine-tuning-and-selection: tested in part |
| 1809.05513 | 2 of 2 | 2 of 13 | full-shell-flux-andreev: not tested; abs-quantum-dot: tested in part |
