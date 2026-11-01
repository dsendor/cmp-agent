You are judging how well a review of a physics paper matches the concerns real referees raised. Judge only from the texts below, and judge the content of each point, not its style or length.

The paper's text (arXiv v1) is given for context. Then the referees' first-round concerns, as JSON (ids C1, C2, ...). Then the review, and the review's points as a JSON list (ids P1, P2, ..., in no particular order).

Part 1. For each referee concern, decide:
- "raised": the review raises the same issue (same mechanism, missing control, number or analysis step), even in different words;
- "partly": it raises a broader or neighbouring issue that would lead an author to the same fix;
- "not raised".
Be strict: a generic request ("show more devices") counts as "partly" at most unless the referee asked for exactly that. For "raised" or "partly", quote the review's words (under 30 words).
Also decide "fixed_in_v1": true if the paper text already contains the fix the referee asked for (the data, control, analysis or correction), so a reader of this version could not have raised it; otherwise false.

Part 2. For each review point (P ids), give:
- matches: ids of referee concerns this point raises in the Part 1 sense (empty list if none);
- partly: ids of referee concerns this point only partly raises (empty list if none);
- quality, judged on its own whether or not a referee raised it: "substantive" (a specific, checkable scientific point about this paper), "generic" (boilerplate that would fit most papers) or "incorrect" (it misreads the paper or states something false about it);
- severity: "major" if, were it right, it would undermine or seriously qualify a main claim; otherwise "minor".
Keep Part 1 and Part 2 consistent: a concern judged "raised" in Part 1 should appear in the matches of at least one point.

Part 3. The review's overall recommendation on the scale "accept", "minor revision", "major revision", "reject". If the review states one, report it with source "stated". If not, assign the one its points imply, with source "assigned".

Reply with JSON only, no prose before or after:
{"matches": [{"concern": "C1", "verdict": "raised" | "partly" | "not raised", "quote": "...", "fixed_in_v1": true | false}], "points": [{"id": "P1", "matches": ["C3"], "partly": [], "quality": "substantive" | "generic" | "incorrect", "severity": "major" | "minor"}], "recommendation": {"value": "accept" | "minor revision" | "major revision" | "reject", "source": "stated" | "assigned"}, "notes": "hard calls, briefly"}
