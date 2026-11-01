Claude-judged, provisional. Judge sonnet; base plain.opus; k = 12 (median eligible concerns per paper); labels: clean 1, contested 4

**All papers (5)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 5 | 5 | 34% (20 to 54) | 62% | 25% | 13% | 3.2 |  | undefined: every review major revision | 2400 | 38.0 |  |  |
| plain.gemini | 5 | 5 | 3% (0 to 7) | 21% | 3% | 7% | 0.4 |  | undefined: every review minor revision | 1307 | 9.2 | -31 pts (-52 to -18), p 1.000 | -21 pts (-35 to -12), p 1.000 |
| legacy.plain | 5 | 5 | 34% (25 to 43) | 57% | 28% | 13% | 2.6 |  | undefined: every review major revision | 3264 | 45.4 | +0 pts (-16 to 11), p 0.589 | +3 pts (-4 to 10), p 0.370 |

**Clean papers (1)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | False alarms per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 1 | 1 | 70% (70 to 70) | 80% | 50% | 19% | 4.0 |  |  | 2866 | 45.0 |  |  |
| plain.gemini | 1 | 1 | 0% (0 to 0) | 20% | 0% | 0% | 1.0 |  |  | 1399 | 11.0 | -70 pts (-70 to -70), p 1.000 | -50 pts (-50 to -50), p 1.000 |
| legacy.plain | 1 | 1 | 40% (40 to 40) | 70% | 40% | 11% | 4.0 |  |  | 2997 | 45.0 | -30 pts (-30 to -30), p 1.000 | -10 pts (-10 to -10), p 1.000 |

**Contested papers (4)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 4 | 4 | 27% (15 to 40) | 59% | 20% | 11% | 3.0 |  | undefined: every review major revision | 2284 | 36.2 |  |  |
| plain.gemini | 4 | 4 | 4% (0 to 8) | 22% | 4% | 8% | 0.2 |  | undefined: every review minor revision | 1284 | 8.8 | -24 pts (-32 to -15), p 1.000 | -16 pts (-20 to -12), p 1.000 |
| legacy.plain | 4 | 4 | 33% (22 to 43) | 55% | 25% | 13% | 2.2 |  | undefined: every review major revision | 3331 | 45.5 | +6 pts (-4 to 15), p 0.254 | +6 pts (0 to 12), p 0.254 |
