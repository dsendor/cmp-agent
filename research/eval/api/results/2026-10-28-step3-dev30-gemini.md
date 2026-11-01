Claude-judged, provisional. Judge gemini; base plain.opus; k = 12 (median eligible concerns per paper); labels: clean 3, contested 27

**All papers (30)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 30 | 90 | 42% (36 to 48) | 68% | 28% | 15% | 8.2 |  | 0.16 (n 30) | 2467 | 40.9 |  |  |
| openaireview.opus | 30 | 90 | 29% (24 to 34) | 49% | 25% | 18% | 2.2 |  | undefined: every review major revision | 2825 | 20.4 | -14 pts (-18 to -9), p 1.000 | -3 pts (-6 to 0), p 0.970 |
| liang.opus | 30 | 90 | 42% (36 to 48) | 68% | 31% | 20% | 6.1 |  | -0.18 (n 30) | 2414 | 30.2 | -0 pts (-3 to 3), p 0.576 | +3 pts (1 to 5), p 0.015 |

**Clean papers (3)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | False alarms per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 3 | 9 | 62% (17 to 100) | 74% | 48% | 8% | 11.8 |  | undefined: every review major revision | 2470 | 44.9 |  |  |
| openaireview.opus | 3 | 9 | 50% (0 to 100) | 67% | 48% | 15% | 1.8 |  | undefined: every review major revision | 2847 | 18.7 | -12 pts (-17 to 0), p 1.000 | +0 pts (0 to 0), p 1.000 |
| liang.opus | 3 | 9 | 50% (0 to 100) | 67% | 33% | 10% | 9.8 |  |  | 2572 | 35.6 | -12 pts (-17 to 0), p 1.000 | -14 pts (-33 to 0), p 1.000 |

**Contested papers (27)**

| Arm | Papers | Runs | Recall (95% CI) | Raised or partly | Top-k recall | Precision | Unmatched major per paper | Unique | Severity rho | Words | Concerns | Recall gain vs base (CI, p) | Top-k gain (CI, p) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| plain.opus | 27 | 81 | 42% (36 to 48) | 68% | 28% | 16% | 7.8 |  | 0.15 (n 27) | 2467 | 40.5 |  |  |
| openaireview.opus | 27 | 81 | 28% (23 to 33) | 49% | 25% | 18% | 2.2 |  | undefined: every review major revision | 2823 | 20.6 | -14 pts (-19 to -10), p 1.000 | -3 pts (-6 to 0), p 0.967 |
| liang.opus | 27 | 81 | 42% (36 to 48) | 68% | 31% | 22% | 5.7 |  | -0.07 (n 27) | 2397 | 29.6 | +0 pts (-3 to 3), p 0.443 | +3 pts (2 to 5), p 0.002 |
