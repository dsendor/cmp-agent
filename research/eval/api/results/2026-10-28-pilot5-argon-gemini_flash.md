Claude-judged, provisional. Judge gemini_flash; base plain.opus; k = 12 (median eligible concerns per paper); labels: clean 1, contested 4

**All papers (5)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 0 | | | | | | | | | | | | |
| plain.gemini | 5 | 5 | 3% (0 to 7) | 8% | 3% | 4% | 1.0 |  | -0.15 (n 5) | 1307 | 9.2 |  |  |
| legacy.plain | 5 | 5 | 39% (26 to 53) | 46% | 28% | 12% | 9.0 |  | undefined: every review major revision | 3264 | 45.4 |  |  |

**Clean papers (1)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | False alarms per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 0 | | | | | | | | | | | | |
| plain.gemini | 1 | 1 | 0% (0 to 0) | 10% | 0% | 0% | 1.0 |  |  | 1399 | 11.0 |  |  |
| legacy.plain | 1 | 1 | 60% (60 to 60) | 60% | 50% | 16% | 6.0 |  |  | 2997 | 45.0 |  |  |

**Contested papers (4)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 0 | | | | | | | | | | | | |
| plain.gemini | 4 | 4 | 4% (0 to 8) | 8% | 4% | 6% | 1.0 |  | 0.54 (n 4) | 1284 | 8.8 |  |  |
| legacy.plain | 4 | 4 | 35% (23 to 49) | 43% | 24% | 11% | 9.8 |  | undefined: every review major revision | 3331 | 45.5 |  |  |
