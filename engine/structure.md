Below is a review of a condensed matter physics paper. The paper itself is provided separately. Turn the review into structured data an author can work through. You are a careful clerk: you do not add concerns, drop concerns, or change what a concern says.

From the paper:

- `title`: the paper's title.
- `claims`: the paper's main claims, three to six, each one sentence in plain words.
- `summary`: two sentences on what the paper reports.

From the review, one item per numbered concern, in the review's order:

- `tier`: "A", "B" or "C", from the heading the concern sits under (A must address, B should address, C minor).
- `rank`: the concern's number in the review.
- `topic`: the one that fits best: "samples" (how many samples or devices, spread, thermal cycling), "null_control" (a sample or geometry where the effect should vanish), "apparatus" (contacts, filters, probes, illumination, tip, trapped flux), "heating" (Joule, optical, electron against lattice temperature), "calibration" (gate to density, angles, fluence, stoichiometry), "dependences" (temperature, field, power, frequency or angle dependence missing), "fits" (free and fixed parameters, extrapolation, error bars), "inhomogeneity" (disorder, strain, domains, interfaces, terminations), "direct_evidence" (direct evidence for the headline property, uniqueness of the signature), "theory" (model assumptions, parameters, convergence, quantitative comparison), "consistency" (between figures, text and figures, earlier data, literature), or "other".
- `claim`: which of the paper's claims the concern affects, in a few words.
- `claim_id`: the number of that claim in your `claims` list (1 for the first), or 0 when the concern is about the paper in general.
- `issue`: the concern in one to three plain sentences, understandable on its own.
- `evidence`: the passage of the paper the concern is about.
  - `quote`: copied exactly, character for character, from the paper's text, 8 to 40 words. Copy prose, not equations. If the concern is about something missing, quote the sentence that makes the claim the missing item would support.
  - `page`: the page of the PDF file where the quote appears, counting the first page of the file as 1.
  - `location`: the figure, table, equation or section, for example "Fig. 3b" or "Methods".
- `effort`: what fixing it takes: "text" (reword, add a caveat or limitation, cite, fix a label), "existing_data" (reanalysis, a new plot or panel, error bars, report fit parameters, using data the authors already have), or "new_work" (a new measurement, sample, device or calculation).
- `fix`: what the authors should do, from the review, one to three sentences.
- `fix_scoped`: only for tier A or B with effort "existing_data" or "new_work". The other route: how the claim could be narrowed to what the data already support, as the exact new wording of the claim's sentence. Use null otherwise.
- `edit_scoped`: when `fix_scoped` is given, the text change that makes it: `before` copied exactly from the paper (one sentence), `after` the reworded sentence. Use null otherwise.
- `runs`: the labels on the concern's "Raised by:" line, for example ["r1", "r3"]. If there is no such line, ["r1"].

Reply with JSON only, no prose before or after:

{"title": "...", "claims": ["..."], "summary": "...", "issues": [{"tier": "A", "rank": 1, "topic": "...", "claim": "...", "claim_id": 1, "issue": "...", "evidence": {"quote": "...", "page": 1, "location": "..."}, "effort": "text", "fix": "...", "fix_scoped": null, "edit_scoped": null, "runs": ["r1"]}]}
