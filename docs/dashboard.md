# Dashboard data

`scripts/build_dashboard.py <review-folder>` fills `dashboard/template.html` with the folder's
data and writes `dashboard.html`, one self-contained file.

## Files in a review folder

| File | Needed | What it is |
|---|---|---|
| `review.json` | yes | The review: paper, claims, issues, evidence check. Written by `scripts/assemble.py`. |
| `paper.pdf` | no | Shown in the PDF pane, loaded by relative path, so it must stay beside `dashboard.html`. A paper with an arXiv id loads from arXiv instead. |
| `comparison.json` | no | Adds a Version comparison page (below). |
| Markdown change log | no | Named by `comparison.json`'s `changelog_file`, included in full. |

## `comparison.json`

Compares two versions of a paper, for example an arXiv version and a newer draft. Every field
is optional except `old` and `new`. Text is plain, except `changelog`, which is Markdown.

| Field | Shape | Shown as |
|---|---|---|
| `page_title`, `heading` | string | Tab name and page heading. |
| `verdict` | string | The opening summary. |
| `caveat` | string | The AI-only notice. Say what was and was not checked. |
| `old`, `new` | `{label, short}` | The two versions. `old` may add `arxiv` (an id with version, such as `2406.13799v2`), `supplement_first_page` and `warning`; the PDF pane can then switch to that arXiv PDF, with the warning as a banner. |
| `counts` | list of `[row label, old value, new value]` | Review counts table. |
| `counts_note` | string | A note under the table. |
| `changed`, `improved`, `worse`, `unresolved` | list of items | The four sections. |
| `si_note` | string | Introduces the supplement checks. |
| `si_mismatches` | list of `{says, result, refs}` | What the draft says the supplement holds, and whether it does. |
| `si_disagreements` | list of items | Where the draft and the supplement disagree. |
| `issue_supplement_links` | `{issue id: [{label, page}]}` | Extra links on review cards that open the arXiv PDF at a page. |
| `changelog_file` | string | A Markdown file in the folder, inlined as `changelog`. |
| `changelog_summary` | string | The collapsed change log's label. |

An **item** is `{title, text, points?, refs?, issues?}`: `points` is a list of bullet strings,
`issues` a list of review issue ids (shown as chips that jump to the card), and `refs` a list
of `{src, page, note?}` where `src` is `"old"` or `"new"`. Check every page in `refs` against
the PDF text before building.
