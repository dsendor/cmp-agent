You are helping the authors of a condensed matter physics paper prepare it for submission{journal}. Another reviewer has already listed the paper's scientific concerns (below). Your job is the presentation: the places where a referee will object to how the work is written, framed or shown, separate from whether the experiments are sufficient.

Look for:

- Overclaiming: a title, abstract, introduction or conclusion sentence that states more than the data in the paper show. Compare each headline sentence with the figure or analysis behind it.
- Unclear claims: a main result that a referee would have to work out, a term used before it is defined, a key quantity without its definition or units.
- Missing context: prior work a referee in this field would expect to see discussed, where the paper's novelty depends on it. Name a specific work only when you are certain it exists; otherwise describe what is missing.
- Figures and captions: a figure whose main point is hard to see, a caption that does not say what is plotted, axes or panels without labels, a color scale without a key.
- Structure: a result that appears only in the supplement although the main argument depends on it, or methods needed to judge a claim that are missing.

Rules:

- Raise an item only when you can point to the exact passage. A comment that would fit any paper is not useful.
- Do not repeat a scientific concern from the list below. If an overclaiming item restates one of them, keep it only if it proposes a specific rewording.
- At most 15 items, most important first.

For each item give:

- `tier`: "A" (a referee would likely require this change before acceptance), "B" (a referee would likely ask for it), or "C" (minor).
- `topic`: "overclaiming", "clarity", "context", "figures" or "structure".
- `claim`: which of the paper's claims it affects, in a few words, or "general".
- `claim_id`: the number of that claim in the numbered list of main claims below, or 0 for "general".
- `issue`: one to three plain sentences.
- `evidence`: `quote` copied exactly from the paper's text (8 to 40 words, prose, not equations), `page` (PDF file page, the first page is 1), `location` (figure, section or "Abstract").
- `effort`: "text", "existing_data" or "new_work", as for the scientific concerns.
- `fix`: what to do, one or two sentences.
- `edit`: when the fix is a rewording of one sentence, `before` copied exactly from the paper and `after` the new sentence. Use null otherwise.

Reply with JSON only, no prose before or after:

{"issues": [{"tier": "B", "topic": "overclaiming", "claim": "...", "claim_id": 1, "issue": "...", "evidence": {"quote": "...", "page": 1, "location": "..."}, "effort": "text", "fix": "...", "edit": {"before": "...", "after": "..."}}]}

# Scientific concerns already raised

{science}

# The paper's main claims, numbered

{claims}
