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

## The loop (up to three rounds)

1. **Queries.** Write two or three arXiv queries from the idea. Each is **two OR-groups joined
   by AND**, one group per facet: question AND system, system AND method, question AND method.
   Three groups ANDed together usually return almost nothing. Expand synonyms and spellings
   inside each group, because arXiv matches words, not meanings:
   - `(abs:moire OR abs:"moiré" OR abs:"twisted bilayer" OR abs:"magic-angle")`
   - `(abs:altermagnet OR abs:altermagnetism OR abs:altermagnetic)`
   - `(abs:"Johnson noise" OR abs:"noise thermometry" OR abs:"shot noise")`
   - `(abs:nanoSQUID OR abs:"nano-SQUID" OR abs:"SQUID-on-tip" OR abs:"scanning SQUID")`
   Use `abs:` for terms and `"..."` for phrases. Add `--cat cond-mat` (or `astro-ph`) when
   a term is used in other fields.
2. **Search.** `python3 search.py papers '<query>' --max 15 --brief` for each query
   (`--brief` cuts abstracts to 300 characters; drop it to read a promising abstract in full).
3. **Landmarks.** arXiv's keyword ranking misses well-known papers whose abstracts use other
   words. Once per idea, run one or two **web searches in plain words**: the method with the
   question ("nanoscale thermal imaging of dissipation"), and the idea as a sentence. For
   each relevant published paper that turns up, find it on arXiv by title:
   `python3 search.py papers 'ti:"<three or four title words>"' --max 3 --brief`, and score
   it like the rest. If web search isn't available, say so in `summary`.
4. **Score.** For each paper, read the title and abstract and score similarity from the
   facets it shares with the idea:
   - all three (same question, system and method): **8 to 10**, a direct precedent;
   - two of three: **5 to 7**, close;
   - one: **2 to 4**, context.
   Within a band, score higher when the overlap is more specific. Keep anything at 5 or
   above.
5. **Refine.** If the best hits match only one facet, or a hit points to a term you didn't
   search (a name the community uses for the same thing), write new queries with it and go
   again. Stop after three rounds, or earlier when a round adds nothing at 5 or above.
6. **Trend.** Run `python3 search.py counts '<query>' --from 2019` once, on the idea's core
   question-and-system query, with the same `--cat` as that query used. Copy the script's
   JSON output unchanged into `counts`. It gives papers per year: how crowded the area is and
   whether it is growing. Report it as a fact, not a score. The current year is partial.

Cite arXiv identifiers where they exist. List every query you ran, web searches included
(prefix those with `web: `).

## Output

Write JSON to the path you were given:

```json
{
 "id": "<idea id>",
 "searched": "YYYY-MM-DD",
 "sources": ["arXiv API", "web search"],
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
