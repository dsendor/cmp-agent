You are judging how well an AI review of a physics paper matches the concerns real referees raised. Judge only from the texts below.

The paper's text (arXiv v1) is given for context. Then the referees' first-round concerns, as JSON. Then the review.

For each concern listed, decide:
- "raised": the review raises the same issue (same mechanism, missing control, number or analysis step), even in different words;
- "partly": it raises a broader or neighbouring issue that would lead an author to the same fix;
- "not raised".
Be strict: a generic request ("show more devices") counts as "partly" at most unless the referee asked for exactly that. For "raised" or "partly", quote the review's words (under 30 words).
For each concern also decide "fixed_in_v1": true if the paper text already contains the fix the referee asked for (the data, control, analysis or correction), so a reader of this version could not have raised it; otherwise false.

Then list every distinct point the review makes (each separate criticism, question or request; skip summary and praise). Label each point with one of:
- the id of the referee concern it matches (for example "C3");
- "substantive": a specific, checkable scientific point about this paper that no listed concern covers;
- "generic": boilerplate that would fit most papers;
- "incorrect": it misreads the paper or states something false about it.

Reply with JSON only, no prose before or after:
{"matches": [{"concern": "C1", "verdict": "raised" | "partly" | "not raised", "quote": "...", "fixed_in_v1": true | false}], "points": [{"point": "one line", "label": "C3" | "substantive" | "generic" | "incorrect"}], "notes": "hard calls, briefly"}
