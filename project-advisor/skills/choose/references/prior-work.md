# Prior-work search loop

Modelled on the novelty check in Si et al.'s AI-Researcher (`src/novelty_check.py`,
https://github.com/NoviScl/AI-Researcher, MIT), with facet comparison from the
Idea Novelty Checker, SDP 2025 (https://aclanthology.org/2025.sdp-1.9; method only, no code used).
Rewritten for physics and for arXiv.

The goal is the closest papers, not a verdict. "Someone did this, here's the paper" can be
checked; "nobody did this" can't. Never write that an idea is novel.

## Facets

Compare each paper with the idea on three facets, separately:
- **Question:** the physical question or quantity (local thermal conductance; the
  anomalous Hall response; the size of the gap).
- **System:** the material or object (magic-angle twisted bilayer graphene; MnTe films; a
  type of galaxy).
- **Method:** the measurement or technique (nanoSQUID thermometry; Johnson noise; ARPES;
  a survey and its depth).

A paper matching all three is a direct precedent. Two of three is close. One is context.

## The loop (at most three rounds)

1. **Queries.** Write two or three arXiv queries from the idea, each pairing two facets
   (question with system, system with method, question with method). Expand synonyms and
   spellings with OR, because arXiv matches words, not meanings:
   - `(abs:moire OR abs:"moiré" OR abs:"twisted bilayer" OR abs:"magic-angle")`
   - `(abs:altermagnet OR abs:altermagnetism OR abs:altermagnetic)`
   - `(abs:"Johnson noise" OR abs:"noise thermometry" OR abs:"shot noise")`
   Use `abs:` for terms and `"..."` for phrases. Add `--cat cond-mat` (or `astro-ph`) when
   a term is used in other fields.
2. **Search.** `python3 search.py papers '<query>' --max 15` for each query.
3. **Score.** For each paper returned, read the title and abstract and score similarity
   1 to 10 from the facets (10 = same question, system and method). Keep anything at 5 or
   above.
4. **Refine.** If the best hits match only one facet, or a hit points to a term you didn't
   search (a name the community uses for the same thing), write new queries with it and go
   again. Stop after three rounds or when a round adds nothing at 5 or above.
5. **Trend.** Run `python3 search.py counts '<query>' --from 2019` once, on the idea's core
   question-and-system query. It gives papers per year: how crowded the area is and whether
   it is growing. Report it as a fact, not a score. The current year is partial.

You may also use web search for a hit's published version or for a term's synonyms. Cite
arXiv identifiers where they exist.

## Output

Write JSON to the path you were given:

```json
{
 "id": "<idea id>",
 "searched": "YYYY-MM-DD",
 "sources": ["arXiv API"],
 "queries": ["..."],
 "closest": [
  {"arxiv": "2301.00323", "title": "...", "year": 2023, "similarity": 6,
   "facets": {"question": true, "system": true, "method": false},
   "overlap": "one line: what is the same", "difference": "one line: what is not"}
 ],
 "counts": {"query": "...", "per_year": {"2019": 20}, "note": "2026 is a partial year."},
 "summary": "one line for the researcher"
}
```

Three to five papers in `closest`, best first. If nothing scored 5 or above, `closest` is
empty and `summary` says so plainly. Copy titles and years from the search output; never
type an arXiv identifier from memory.
