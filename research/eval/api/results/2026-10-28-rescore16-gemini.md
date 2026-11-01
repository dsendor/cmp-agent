Claude-judged, provisional. Judge gemini; base legacy.plain; k = 12 (median eligible concerns per paper); labels: clean 2, contested 14

**All papers (16)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 16 | 16 | 42% (34 to 51) | 65% | 30% | 17% | 8.1 |  | undefined: every review major revision | 3061 | 42.1 |  |  |
| legacy.assistant | 16 | 16 | 15% (9 to 20) | 30% | 14% | 19% | 1.8 |  | undefined: every review major revision | 1483 | 11.6 | -28 pts (-35 to -21), p 1.000 | -16 pts (-22 to -10), p 1.000 |

**Clean papers (2)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | False alarms per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 2 | 2 | 67% (60 to 100) | 75% | 42% | 11% | 8.5 |  |  | 3087 | 47.0 |  |  |
| legacy.assistant | 2 | 2 | 0% (0 to 0) | 33% | 0% | 0% | 1.5 |  |  | 1414 | 11.5 | -67 pts (-100 to -60), p 1.000 | -42 pts (-50 to -40), p 1.000 |

**Contested papers (14)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 14 | 14 | 41% (31 to 49) | 64% | 29% | 18% | 8.1 |  | undefined: every review major revision | 3057 | 41.4 |  |  |
| legacy.assistant | 14 | 14 | 15% (9 to 22) | 30% | 15% | 22% | 1.8 |  | undefined: every review major revision | 1493 | 11.6 | -25 pts (-31 to -20), p 1.000 | -14 pts (-20 to -9), p 1.000 |
