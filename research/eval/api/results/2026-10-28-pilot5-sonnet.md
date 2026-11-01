Claude-judged, provisional. Judge sonnet; base legacy.plain; k = 12 (median eligible concerns per paper); labels: clean 1, contested 4

**All papers (5)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 5 | 5 | 34% (25 to 43) | 57% | 28% | 13% | 2.6 |  | undefined: every review major revision | 3264 | 45.4 |  |  |
| plain.opus | 5 | 5 | 34% (20 to 54) | 62% | 25% | 13% | 3.2 |  | undefined: every review major revision | 2400 | 38.0 | +0 pts (-11 to 16), p 0.600 | -3 pts (-10 to 4), p 0.879 |
| legacy.assistant | 5 | 5 | 8% (4 to 12) | 30% | 8% | 11% | 0.4 | 4 | undefined: every review major revision | 1446 | 11.4 | -26 pts (-35 to -18), p 1.000 | -20 pts (-31 to -9), p 1.000 |

**Clean papers (1)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | False alarms per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 1 | 1 | 40% (40 to 40) | 70% | 40% | 11% | 4.0 |  |  | 2997 | 45.0 |  |  |
| plain.opus | 1 | 1 | 70% (70 to 70) | 80% | 50% | 19% | 4.0 |  |  | 2866 | 45.0 | +30 pts (30 to 30), p 0.505 | +10 pts (10 to 10), p 0.505 |
| legacy.assistant | 1 | 1 | 0% (0 to 0) | 40% | 0% | 0% | 0.0 | 0 |  | 1406 | 11.0 | -40 pts (-40 to -40), p 1.000 | -40 pts (-40 to -40), p 1.000 |

**Contested papers (4)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 4 | 4 | 33% (22 to 43) | 55% | 25% | 13% | 2.2 |  | undefined: every review major revision | 3331 | 45.5 |  |  |
| plain.opus | 4 | 4 | 27% (15 to 40) | 59% | 20% | 11% | 3.0 |  | undefined: every review major revision | 2284 | 36.2 | -6 pts (-15 to 4), p 0.935 | -6 pts (-12 to 0), p 1.000 |
| legacy.assistant | 4 | 4 | 10% (7 to 14) | 27% | 10% | 13% | 0.5 | 4 | undefined: every review major revision | 1456 | 11.5 | -24 pts (-30 to -16), p 1.000 | -16 pts (-25 to -5), p 1.000 |
