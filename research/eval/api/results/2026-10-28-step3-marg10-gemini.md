Claude-judged, provisional. Judge gemini; base plain.opus; k = 11 (median eligible concerns per paper); labels: clean 1, contested 9

**All papers (10)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 10 | 30 | 44% (34 to 54) | 69% | 26% | 16% | 7.8 |  | undefined: every review major revision | 2513 | 43.1 |  |  |
| liang.opus | 10 | 30 | 45% (36 to 54) | 69% | 28% | 23% | 6.1 |  | undefined: every review major revision | 2449 | 30.7 | +1 pts (-3 to 6), p 0.462 | +2 pts (-2 to 4), p 0.195 |
| openaireview.opus | 10 | 30 | 29% (22 to 38) | 47% | 24% | 20% | 2.7 |  | undefined: every review major revision | 2940 | 22.4 | -16 pts (-23 to -8), p 1.000 | -2 pts (-8 to 3), p 0.831 |
| margnr.opus | 10 | 10 | 62% (50 to 73) | 81% | 26% | 16% | 11.8 |  | undefined: every review major revision | 6408 | 70.6 | +17 pts (9 to 27), p 0.013 | +0 pts (-10 to 9), p 0.516 |

**Clean papers (1)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | False alarms per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 1 | 3 | 100% (100 to 100) | 100% | 100% | 5% | 9.0 |  |  | 2680 | 49.3 |  |  |
| liang.opus | 1 | 3 | 100% (100 to 100) | 100% | 67% | 9% | 8.0 |  |  | 2717 | 37.0 | +0 pts (0 to 0), p 1.000 | -33 pts (-33 to -33), p 1.000 |
| openaireview.opus | 1 | 3 | 100% (100 to 100) | 100% | 100% | 12% | 2.3 |  |  | 3017 | 22.0 | +0 pts (0 to 0), p 1.000 | +0 pts (0 to 0), p 1.000 |
| margnr.opus | 1 | 1 | 100% (100 to 100) | 100% | 0% | 5% | 19.0 |  |  | 6419 | 69.0 | +0 pts (0 to 0), p 1.000 | -100 pts (-100 to -100), p 1.000 |

**Contested papers (9)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 9 | 27 | 44% (32 to 53) | 69% | 25% | 17% | 7.7 |  | undefined: every review major revision | 2494 | 42.4 |  |  |
| liang.opus | 9 | 27 | 44% (35 to 52) | 68% | 27% | 25% | 5.9 |  | undefined: every review major revision | 2419 | 30.0 | +1 pts (-4 to 6), p 0.458 | +2 pts (-0 to 5), p 0.099 |
| openaireview.opus | 9 | 27 | 28% (21 to 36) | 46% | 23% | 20% | 2.8 |  | undefined: every review major revision | 2932 | 22.4 | -16 pts (-24 to -8), p 1.000 | -2 pts (-8 to 3), p 0.830 |
| margnr.opus | 9 | 9 | 61% (50 to 73) | 81% | 27% | 18% | 11.0 |  | undefined: every review major revision | 6407 | 70.8 | +18 pts (9 to 27), p 0.014 | +2 pts (-6 to 10), p 0.421 |
