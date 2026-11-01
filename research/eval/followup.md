# Follow-up record for the new papers

*AI only. Recorded 2026-10-23, the day the reports were written. Nothing here is
human-checked.*

Check back in 6 to 12 months (April to October 2027) for new versions, comments, replies,
corrections and publication, and compare with the flags in `ratings/<id>.md`. Run:

```bash
python3 research/scripts/followup.py
```

It prints, per paper, the latest arXiv version and its comments field, the journal DOI and
venue if OpenAlex has one, the citation count, and any citing work whose title looks like a
comment, reply, erratum, correction or retraction. A flag that a later version addresses, or
that a comment raises, is worth noting next to the physicist's rating; a flag nobody ever
raises is not evidence either way.

Two cautions. OpenAlex lags arXiv by weeks to months: one run found a September 2026 paper
(arXiv 2609.25223) whose abstract names 2607.09511, while OpenAlex still lists 0 citations
today. And a title search misses replies posted under ordinary titles, so also read the
list of citing works for each paper.

## State on 2026-10-23 (output of followup.py)

### 2607.09511
- latest arXiv version: v1; comments: none
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2607.09511; cited by 0

### 2608.12897
- latest arXiv version: v1; comments: 15 pages, 3 figures
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2608.12897; cited by 0

### 2610.18817
- latest arXiv version: v1; comments: none
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2610.18817; cited by 0

### 2608.17404
- latest arXiv version: v1; comments: Main text: 8 pages, 4 figures. SM: 7 pages, 5 figures
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2608.17404; cited by 0

### 2608.27444
- latest arXiv version: v1; comments: none
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2608.27444; cited by 0

### 2608.26022
- latest arXiv version: v1; comments: 33 pages,18 figures
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2608.26022; cited by 0

### 2609.38003
- latest arXiv version: v1; comments: 14 pages, 4+5 figures
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2609.38003; cited by 0

### 2609.01233
- latest arXiv version: v1; comments: none
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2609.01233; cited by 0

### 2610.29124
- latest arXiv version: v1; comments: 39 pages, including 20 pages of main text with 4 figures and 19 pages of Supplementary Information with 8 figures
- venue: arXiv (Cornell University); DOI: https://doi.org/10.48550/arxiv.2610.29124; cited by 0

