# advisor.json

One file per session, in `project-choice/<YYYY-MM-DD>/`. The skill writes it;
`decide.py` reads it and writes `decision.json`; `build_dashboard.py` reads both. A full
example is `tests/example/advisor.json` in the plugin.

```json
{
 "schema": 1,
 "created": "YYYY-MM-DD",
 "researcher": {"stage": "postdoc", "horizon_months": 24, "goal": "...", "setup": "..."},
 "utility": "total",
 "ideas": [
  {
   "id": "short-id",
   "title": "Short title",
   "summary": "Two-line restatement",
   "heilmeier": {"what": "", "today": "", "new": "", "who_cares": "", "risks": "",
                 "cost": "", "time": "", "midterm": "", "final": ""},
   "estimates": {
    "p_success": {"low": 0.2, "best": 0.35, "high": 0.55, "by": "researcher"},
    "impact":    {"low": 6, "best": 8, "high": 9, "by": "researcher"},
    "fallback":  {"low": 2, "best": 3, "high": 4, "by": "researcher"},
    "months":    {"low": 12, "best": 16, "high": 22, "by": "researcher"}
   },
   "assumptions": [
    {"text": "...", "kind": "nature", "risk": 4, "readout_months": 6, "scariest": true}
   ],
   "prior_work": {"...": "the prior-work/<id>.json written by the search, copied in"},
   "cheapest_test": {"text": "...", "resolves": "p_success", "months": 1},
   "inversion": "What you'd still have if it fails"
  }
 ],
 "pi_questions": ["..."]
}
```

| Field | Meaning |
|---|---|
| `utility` | `total`: value = odds × impact + (1 − odds) × fallback. `per_year`: the same, per year of work. |
| `estimates.*` | `low` and `high` required, `best` optional (defaults to the middle). Odds between 0 and 1; impact and fallback on the researcher's 0 to 10 scale; months positive. |
| `estimates.*.by` | `researcher` (default) or `model`. Anything not the researcher's is flagged on the dashboard. |
| `assumptions[].kind` | `nature` or `capability`. |
| `assumptions[].risk` | 1 (very likely true) to 5 (very unlikely), given by the researcher. |
| `cheapest_test.resolves` | Which estimate the test would change: `p_success`, `impact`, `fallback` or `months`. |

`decision.json` is written by `decide.py` and never edited by hand.
