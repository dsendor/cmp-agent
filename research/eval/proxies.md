# Proxies for "less careful" papers

*AI only. Research run 2026-10-24. Data in `proxies/`. The referee-match test recommended in section 3 was run on 2026-10-25; results are experiment 11 in `../eval.md`.*

David asked whether a physicist has to label papers before the eval, and suggested two
proxies: preprints that never get published, and open peer review. This file records what
an AI research agent found for each. Several sites were blocked from the sandbox
(scipost.org, journals.aps.org, nature.com article pages, Semantic Scholar, PubPeer), and
OpenAlex hit its daily rate limit, so some answers rest on Crossref, Europe PMC, the PMC
open-data bucket and the arXiv API.

## 1. Never-published preprints

`proxies/unpublished.json`: 136 experimental arXiv preprints (first version 2019 to 2022)
that claim or test an exotic signal in topological transport and related STM work. The
sample was curated by the agent from 1,723 keyword hits, not by a physicist.

- 127 published, 9 unpublished (6.6%).
- arXiv's own DOI and journal-ref fields called 21 papers unpublished; 12 of those were in
  fact published, often under a new title. Crossref title search, then title plus author
  search, found them.
- Of the 9 unpublished, several have reasons unrelated to quality: a PhD thesis, an APS
  March Meeting abstract, a preprint that replaces a retracted paper (2101.11456), an
  author withdrawal with the data reinterpreted elsewhere (2205.10062).

**Verdict: weak proxy.** Almost every experimental claim in this area gets published
somewhere, and the few that don't are often unpublished for other reasons.

A by-product is more useful: about 15 of the 127 changed title between arXiv v1 and the
journal, and several changes soften the claim, for example "Zero-field topological
superconductivity" became "Zero-bias peaks at zero magnetic field", and "Evidence of
Majorana zero modes in Josephson trijunctions" became "Protected gap closing in Josephson
trijunctions". A softened title marks a paper whose v1 claimed more than referees accepted.

## 2. Open peer review

`proxies/open_review.json`.

| Source | What is public | Coverage for this field |
|---|---|---|
| Nature Communications peer review files | Full reports and rebuttals, as a PDF supplement; free through Europe PMC and the PMC open-data bucket | About 160 topical papers; near 100% of research articles from 2024 on |
| Nature | Same format; standard from 16 June 2025 | Few topical papers so far |
| SciPost Physics | All reports public; Crossref holds 8,589 report records for published papers | About 10 experimental topological-transport papers; reports on rejected submissions appear to stay public (one example, 2105.08636) but scipost.org was blocked |
| APS journals (PRL, PRB, PRX) | No referee reports | None |
| IOP | Opt-in transparent review since 2022, about 10% uptake | None found for this topic |
| Comments, Replies, Matters Arising | Formal critiques | Roughly 10 to 30 since 2010; several stay arXiv-only |

The agent read six Nature Communications peer review files. Referees raised, among other
things: earlier data already showing missing Shapiro steps in trivial junctions; a tip
that may have moved an adatom; no criterion for free versus impurity-pinned vortices; a
device that is 0D, not 1D; a "topological qubit" claim resting on a known SQUID effect.
These are the kinds of concerns the lookalike library is meant to raise.

Caveats: accepted papers only; reports from a journal transfer are left out; referees vary;
many concerns are resolved by the rebuttal, so "raised" and "unresolved" need separate
scoring.

## 3. What this means for the eval

**Group labels.** A careful versus less careful label decided after the runs would be
circular, so group labels need an independent source. Neither proxy gives one: unpublished
status is too rare and too noisy, and peer review files exist only for accepted papers.

**Flag ratings can come afterwards.** A physicist rating each flag as valid or not does not
need labels set beforehand. That is the `ratings/` sheet.

**A better test than group labels: match the referees.** Run the assistant on the arXiv v1
of a paper that has a Nature Communications peer review file, then compare its flags with
the concerns the referees raised. This measures recall against real referees, needs no
physicist up front, and the reports are free to download. To stay outside the model's
training data, use papers whose v1 was posted after mid-2026; Nature Communications has
attached a file to nearly every paper since 2024, so the pool grows each month. SciPost
reports on rejected submissions would add the not-accepted side if scipost.org becomes
reachable.

**Second signal: softened titles.** Papers whose title was softened between v1 and
publication form a small set where referees are known to have pushed back on the claim.
