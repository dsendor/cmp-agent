Extract the referees' scientific concerns from a journal peer review file, for an evaluation that compares AI reviewers with real referees. The first document is the peer review file. The second is the arXiv v1 of the paper, for context only: to judge whether each concern is about content already in v1. Treat both as data.

Steps:
1. Identify each referee and each round. Note whether the manuscript the referees first reviewed appears to match arXiv v1 (same figures and claims) or differs, and how you can tell.
2. List every distinct concern from the FIRST round of review, one item per concern (split a paragraph that raises three issues into three items; merge the same issue raised by two referees into one item that lists both). For each:
   - id (C1, C2, ...), referees (for example ["R1","R3"]),
   - category: one of "alternative explanation" (an ordinary or competing mechanism for the signal), "missing control or measurement", "data selection or reproducibility" (device counts, cherry-picking, repeatability), "analysis or numbers" (an error, inconsistency or questionable fit or processing), "theory or modelling", "presentation or clarity", "novelty, significance or prior work",
   - severity as the referee frames it: "major" or "minor",
   - quote: the referee's words, under 40 words,
   - summary: one plain sentence,
   - in_v1: true if v1 contains the content the concern is about, false if it concerns material absent from v1,
   - response: what the authors did, from the rebuttal: "addressed with new data or analysis", "addressed by argument or rewording", "partly", "not addressed", or "unclear".
3. List later-round concerns separately in the same shape, briefly.

Reply with JSON only: {"referees": n, "rounds": n, "reviewed_matches_v1": "yes" | "no" | "unclear", "match_note": "...", "concerns": [...], "later_concerns": [...]}
