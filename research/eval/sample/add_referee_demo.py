#!/usr/bin/env python3
"""Add the demo-only referee overlay to a sample review.json.

    python3 add_referee_demo.py review.json referee_map.json

referee_map.json is the matching of the paper's real first-round referee concerns
(eligible ones only) to the review's issues, made with the eval judge's definitions:
{"referee_concerns": [{"id": "C1", "severity": "major", "summary": "...",
  "raised": "yes" | "partly" | "no", "matches": [{"issue": "S03", "raised": "yes" | "partly"}]}]}
Only sample dashboards made from development papers carry this; a user's review never does.
"""
import json
import sys
from pathlib import Path

review_path, map_path = map(Path, sys.argv[1:3])
review = json.loads(review_path.read_text())
ids = {i["id"] for i in review["issues"]}
m = json.loads(map_path.read_text())
for c in m["referee_concerns"]:
    c["matches"] = [x for x in c.get("matches", []) if x["issue"] in ids]
    if not c["matches"]:
        c["raised"] = "no"
review["demo"] = {
    "note": "This sample is a published paper whose referee reports are public, so the dashboard can show which of "
            "the referees' concerns the review anticipated.",
    "referee_concerns": m["referee_concerns"],
}
review_path.write_text(json.dumps(review, indent=1, ensure_ascii=False))
rc = m["referee_concerns"]
print(f"{len(rc)} referee concerns: {sum(c['raised'] == 'yes' for c in rc)} raised, "
      f"{sum(c['raised'] == 'partly' for c in rc)} partly, {sum(c['raised'] == 'no' for c in rc)} missed")
