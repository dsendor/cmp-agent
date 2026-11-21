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

## Referee overlay (`review.json` → `demo`)

An optional `demo` object in `review.json` tags review cards with referee concerns and adds a
box under the summary. It has `note` (string), `referee_concerns` (list of `{id, severity,
summary, raised, matches}`, where `raised` is `yes`, `partly` or `no` and `matches` is a list
of `{issue, raised}` naming review issue ids) and `inferred` (boolean).

- `inferred: false` or absent: the concerns come from real referee reports (the sample
  dashboard). The box says "Demo only" and lists the concerns the review missed.
- `inferred: true`: the concerns were inferred by AI from what changed between two versions
  of the paper; no referee report was seen. The box and tags say so, and the box lists every
  inferred concern. Use this with a `comparison.json` built from the same two versions.
- `walkthrough` (with `inferred: true`): a list of `{id, title, confidence, verdict, asked,
  response, judgment, still_open, changes, earlier, blind}`, written by `scripts/revision.py`
  (format in `engine/compare.md`, step 3). It adds a **Referee feedback** view: one card per
  inferred concern with its verdict (looks addressed, partly, not addressed, can't tell),
  what changed between versions with page links, and a button that lists the blind review's
  items on the same point. **Start here** then opens with a line saying the paper is a
  revision, and the summary box above is not shown.

**Start here** and **Referee feedback** hide the claim grid, lane and filter controls; the
item views show them.

## Ask Claude (published artifacts only)

In a page published with `/referee-preview:publish`, an **Ask Claude** button opens a chat
about the review. It uses the artifact's `sample` capability, so it runs as the viewer, on
their own Claude account, after a consent prompt. It works with base Claude; Claude Code is
not needed. The button shows only where the capability is granted. Declare
`"sample": {}` alongside the shared-review capabilities (`docs/shared-review.md`).

Claude answers through tools that read the page's own data:
- the review items;
- the paper's and the supplement's text by page (`paper.pages.json` and `si.pages.json`,
  embedded by `build_dashboard.py --artifact`);
- the inferred referee feedback and the version comparison, when present;
- `analysis.md`, a written analysis in the review folder, when present.

A menu in the panel picks the model: *Best available* (the host's strongest, the default), Claude Opus 5.5, Fable 5.2, Sonnet 5.5 or Haiku 5.5. The choice is kept in the browser. The host may refuse a named model and fall back, so each answer says which model gave it. It is told to check claims against the paper text, and to say which figure panel an item
rests on, since it cannot see figures. Conversations are not saved.
