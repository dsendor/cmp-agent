Claude-judged, provisional. Judge gemini_flash; base legacy.plain; k = 12 (median eligible concerns per paper); labels: clean 2, contested 14

**All papers (16)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 16 | 16 | 40% (31 to 50) | 53% | 28% | 14% | 8.4 |  | undefined: every review major revision | 3061 | 42.1 |  |  |
| legacy.assistant | 16 | 16 | 14% (9 to 20) | 24% | 14% | 17% | 2.6 |  | undefined: every review major revision | 1483 | 11.6 | -26 pts (-34 to -19), p 1.000 | -14 pts (-22 to -7), p 1.000 |

**Clean papers (2)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | False alarms per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 2 | 2 | 67% (60 to 100) | 67% | 50% | 10% | 8.0 |  |  | 3087 | 47.0 |  |  |
| legacy.assistant | 2 | 2 | 8% (0 to 50) | 25% | 8% | 5% | 3.5 |  |  | 1414 | 11.5 | -58 pts (-60 to -50), p 1.000 | -42 pts (-50 to 0), p 1.000 |

**Contested papers (14)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| legacy.plain | 14 | 14 | 39% (29 to 48) | 52% | 26% | 14% | 8.5 |  | undefined: every review major revision | 3057 | 41.4 |  |  |
| legacy.assistant | 14 | 14 | 14% (9 to 20) | 24% | 14% | 19% | 2.4 |  | undefined: every review major revision | 1493 | 11.6 | -24 pts (-32 to -17), p 1.000 | -12 pts (-19 to -6), p 1.000 |
