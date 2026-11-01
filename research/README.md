> **About this folder.** The research behind the Referee preview plugin: the first lookalike
> assistant, every evaluation run, the referee data and the scripts. It was developed as
> `cmp-assistant/` in a private project repository and moved here in November 2026; paths in
> older run notes still say `cmp-assistant/`. The plugin it led to is the root of this
> repository. Referee text is reused under CC BY 4.0; see `../NOTICE`.

# Lookalike assistant (proof of concept)

*AI only. Built 2026-10-23 from Bill's Notion brief ("Claude Code brief: condensed matter
lookalike assistant (POC)"). Nothing here is human-checked yet.*

A small proof of concept of phase 1 on the condensed matter site
(https://reproducible-cmp.vercel.app/): an assistant that knows the known lookalikes in one
subfield, topological transport, and writes a one-page report on a paper. The question to
put to physicists: would this have helped you?

It is model-agnostic: plain markdown instructions and a YAML library, packaged as an Agent
Skill so it also loads into Claude Code or Claude Science. It doesn't touch the site.

## Status

Library and skill v0.5. **In testing it did not beat a plain "Review this paper."
prompt.** Against journal referees on 16 papers, it raised 15% of their concerns and the
plain prompt 46%. Assistant runs are paused. From 2026-10-27 the work follows a data-driven eval plan
(`eval.md`, Eval plan), with every run scripted through the model APIs (`eval/api/`).
`eval.md` is the single record of what was tried, what worked and what didn't.

## What's here

| | |
|---|---|
| `writer-mvp-plan.md` | The plan for the writer-mode MVP: six stages, three lanes, build order. |
| The plugin | The Claude Code plugin built from that plan (reviewer v1.0) is the root of this repository. Sample dashboard in `eval/sample/`. |
| `eval.md` | **Start here.** Every experiment (11 of them), its result and verdict, what worked, what didn't and why, and the eval plan with its Step 0 checks. |
| `library/lookalikes.yaml` | The library: ordinary effects that can produce a claimed topological signal, each with mechanism, discrete tests, what fuller data would show, and verbatim quotes from sources with URLs. |
| `skill/SKILL.md` | The workflow, seven steps from claims to report. Plain markdown, usable as a prompt in any model. |
| `skill/report-template.md` | The one-page report layout. |
| `eval/` | Data behind `eval.md`: the test set (`papers.yaml`), runs (`runs/<id>/`), the larger planted test (`planted5/`), the referee match (`referee/`), scoring scripts and their generated tables (`scores.md`, `planted.md`, `scores_v5.md`), proxy research (`proxies.md`, `proxies/`), physicist rating sheets (`ratings/`), the 2027 follow-up record (`followup.md`), the API harness for the eval plan (`api/`), the power simulation (`power.py`) and the judge audit sheet (`judge-audit.md`). |
| `reports/2004.08583.md` | The figure-data test report (Yu et al. 2021) and its run notes. |
| `sample-report.md` | A v0.4 report made for showing physicists (the Kitaev parity-qubit paper). Made before the referee match. |
| `sample-report-anonymized.md` | The same report with title, ID, links and searchable quotes removed. |
| `demo/claude-science.md` | How to load and run the skill in Claude Science (untested), and a table to record the result. |
| `scripts/check.py` | Validates the library and the style rules. `--quotes` fetches every arXiv source and confirms each quote appears in it. |
| `scripts/read_mtx.py` | Summarizes Spyview `.mtx` figure data (axes, ranges, grid size) for step 1. Needs numpy. |
| `scripts/followup.py` | Checks the new test papers for later versions, comments, replies and publication (OpenAlex and arXiv, no keys). |
| `scripts/package.sh` | Builds `dist/lookalike-assistant/` and a zip for loading as a skill (generated, not committed). |
| `prior-work.md` | Existing tools and papers checked for reuse, and how the topological gap protocol compares with the library. |

## Run it

**In Claude Code**, from this repository:

```bash
bash research/scripts/package.sh                         # check, then build the package
cp -r research/dist/lookalike-assistant ~/.claude/skills/ # install it as a personal skill
```

Then in a new Claude Code session: "Run the lookalike-assistant skill on arXiv
2607.09511v1." It writes `reports/<id>.md` and `reports/<id>.notes.md`. Without
installing, you can also say "Follow `research/skill/SKILL.md` on arXiv <id>".

**In ChatGPT, Gemini or any chat model:** paste `skill/SKILL.md`,
`skill/report-template.md` and `library/lookalikes.yaml`, attach the paper's PDF, and ask
for the report. If the model can't open links, it marks related work "links not checked".

**In Claude Science:** see `demo/claude-science.md`.

## Change the library

Edit `library/lookalikes.yaml` by hand, then run:

```bash
python3 research/scripts/check.py --quotes
```

Every new entry starts `checked: ai`, and only David changes that. Each source needs a URL
and a passage copied exactly from it; the check fails on a quote it can't find in the
arXiv text, so nothing gets in from model memory alone. Sources off arXiv are skipped by
the quote check and listed so you can confirm them by hand. The check needs PyYAML and
`pdftotext` (poppler).

## Rules

House rules for this work: no em dashes, every source with a URL and labeled AI only. The brief adds: no contrast phrasing
("not X but Y", "rather than", "instead of"). `check.py` enforces both outside quotes.
