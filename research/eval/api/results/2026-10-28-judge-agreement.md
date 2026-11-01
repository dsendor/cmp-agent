Judge agreement on raised / partly / not raised, experiment 11 reviews (Claude-judged, provisional)

| Pair | Calls | Agreement | Cohen's kappa | Assistant kappa | Plain kappa |
|---|---|---|---|---|---|
| judge.json vs sonnet | 426 | 76% | 0.62 | 0.70 | 0.51 |
| judge.json vs opus | 426 | 85% | 0.77 | 0.78 | 0.71 |
| judge.json vs gemini_flash | 426 | 77% | 0.63 | 0.64 | 0.57 |
| judge.json vs gemini | 426 | 83% | 0.73 | 0.73 | 0.68 |
| sonnet vs opus | 426 | 81% | 0.69 | 0.74 | 0.62 |
| sonnet vs gemini_flash | 426 | 77% | 0.61 | 0.63 | 0.56 |
| sonnet vs gemini | 426 | 78% | 0.65 | 0.67 | 0.60 |
| opus vs gemini_flash | 426 | 85% | 0.74 | 0.74 | 0.71 |
| opus vs gemini | 426 | 90% | 0.84 | 0.83 | 0.82 |
| gemini_flash vs gemini | 426 | 87% | 0.78 | 0.78 | 0.75 |

Old judge (rows) against sonnet (columns):

| Old \ sonnet | raised | partly | not raised |
|---|---|---|---|
| raised | 90 | 37 | 3 |
| partly | 3 | 68 | 44 |
| not raised | 0 | 17 | 164 |

Old judge (rows) against opus (columns):

| Old \ opus | raised | partly | not raised |
|---|---|---|---|
| raised | 114 | 16 | 0 |
| partly | 2 | 75 | 38 |
| not raised | 0 | 8 | 173 |

Old judge (rows) against gemini_flash (columns):

| Old \ gemini_flash | raised | partly | not raised |
|---|---|---|---|
| raised | 113 | 13 | 4 |
| partly | 3 | 34 | 78 |
| not raised | 0 | 0 | 181 |

Old judge (rows) against gemini (columns):

| Old \ gemini | raised | partly | not raised |
|---|---|---|---|
| raised | 117 | 13 | 0 |
| partly | 4 | 61 | 50 |
| not raised | 0 | 7 | 174 |

judge.json legacy.assistant  recall 15% (213 concerns)
judge.json legacy.plain      recall 46% (213 concerns)
sonnet     legacy.assistant  recall 12% (213 concerns)
sonnet     legacy.plain      recall 31% (213 concerns)
opus       legacy.assistant  recall 14% (213 concerns)
opus       legacy.plain      recall 41% (213 concerns)
gemini_flash legacy.assistant  recall 14% (213 concerns)
gemini_flash legacy.plain      recall 40% (213 concerns)
gemini     legacy.assistant  recall 15% (213 concerns)
gemini     legacy.plain      recall 42% (213 concerns)
