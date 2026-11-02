# Referee preview

A Claude Code plugin that shows condensed matter physicists what referees will object to
before they submit. It reads your paper the way journal referees do, lists every likely
objection with a quote from the paper and a concrete fix, and opens a dashboard where you
decide what to do about each one. Accepted text edits go back into your LaTeX source, and
Claude then helps with the items you choose to fix.

Everything it produces is AI-generated and labeled so. It does not judge whether your result
is right; it lists what a careful referee would ask. How well it does that is in
[EVALUATION.md](EVALUATION.md).

## Why this exists

The goal is shared knowledge for condensed matter physics: what one lab learns should help
every other lab. Today a new signal is judged against the simple explanations a lab and its
referees happen to know, and what labs learn (failed runs, null results, the checks that ruled
an artifact out) mostly stays on lab drives. The vision, the pain points it addresses and the
phases to get there are set out at
**[Shared knowledge for condensed matter physics](https://reproducible-cmp.vercel.app/)**.

Referee preview is the first step: a tool that is useful to a working physicist today, built
on what the field already knows about how claims fail. The major next step is a shared record
of what has been tried: experiments, controls and dead ends, recorded as they happen and
shared, so that the next lab starts from what the field has already learned. Feedback that
authors choose to share from this plugin (see below) is the first small piece of that record.

## Install

In Claude Code:

```text
/plugin marketplace add dsendor/cmp-agent
/plugin install referee-preview@cmp-agent
```

To try it for one session from a clone, without installing: `claude --plugin-dir <path to this repository>`.

Needs Python 3. `pdftotext` (poppler) is optional; without it, quotes are not checked against
the paper. The review is written for Claude Opus; other models work but are not measured.

## Use

```text
/referee-preview:review path/to/paper.pdf
/referee-preview:review path/to/latex-folder --journal "Physical Review B"
/referee-preview:review 2601.01843 quick
```

The review runs three independent scientific reviews in parallel and merges them (about 10 to
25 minutes on your Claude Code plan); say "quick" for one review. It writes a folder
`referee-preview/<paper>-<date>/` next to the paper and opens `dashboard.html`.

It looks at the paper in three lanes:

- **Science:** does the evidence support the conclusions (controls, samples, artifacts,
  heating, calibration, fits, alternative explanations, theory).
- **Presentation:** overclaiming, unclear claims, missing context, figures and captions.
- **Copy:** numbers that disagree between text and figures, notation, numbering, language.

In the dashboard:

- **Triage** sorts by importance: *must address* (the conclusion does not follow without it),
  *should address* (a claim is weaker), *minor*. **Walk through** follows the paper page by
  page, with the PDF beside it (Show PDF).
- Each objection is linked to the main claim it affects; click a claim to see only its
  objections. Importance buttons show or hide each level, and the Tags menu sets which labels
  show.
- Each science or presentation item: *Will fix*, *Scope the claim* (accept a narrower wording
  where the data fall short), *Already in the paper*, *Disagree*, *Not worth it*, and a note.
- Copy edits: *Accept*, *Reject*, *Edit*. Low-risk ones (prose only) can be accepted in bulk;
  an edit that touches a number, symbol, unit, citation or hedge word is marked for a closer
  look.
- The grid of importance against effort to fix (text edit, reanalysis, new experiment) shows
  where the quick wins are. Press `?` for keyboard shortcuts.

Then click **Send to Claude** and paste the command it copies into Claude Code
(`/referee-preview:apply decisions-<review>.json`). It applies accepted edits to the LaTeX
source, recompiles, commits so one `git revert` undoes it, writes `revision-plan.md`, and then
works through each item you marked *Will fix*, using your note on it as the instruction.

**Sending a dashboard to someone.** `dashboard.html` is one self-contained file. For a paper on
arXiv it loads the paper from arXiv, so the file alone is enough; for a draft that is not on
arXiv, send `paper.pdf` with it, in the same folder.

## Your data

- Your paper is read by Claude Code on your machine and sent only to the model, as in any
  Claude Code session. The plugin has no server and sends nothing anywhere else.
- Your house style, standing rules and a history of reviews and decisions live in
  `~/.referee-preview/`, outside the plugin, so updates never touch them.

## How it works

| | |
|---|---|
| `skills/review/`, `skills/apply/`, `skills/contribute/` | the three commands |
| `agents/` | subagents: three science reviewers in parallel, the merger, the structurer, presentation and copy |
| `engine/` | the prompts. `science.md` and `merge.md` are the measured reviewer (`VERSION`); the others are newer and not yet measured |
| `scripts/` | `paper_text.py`, `assemble.py`, `check_evidence.py` (is each quote really in the paper), `build_dashboard.py`, `contribute.py` (redact, scrub, send) |
| `feedback-endpoint/` | the serverless function that files contributions in a private repository |
| `dashboard/template.html` | the dashboard: one self-contained file that works offline |

## Sharing your feedback

After a review, `/referee-preview:contribute` can share your decisions to improve the plugin.
You choose how much: labels only, generalized text, the item text, or everything for a paper that
is already public. A scrub step blocks anything that identifies your paper, you see the exact
file before it is sent, and nothing is sent without your yes. Contributions go to a private
inbox and are reviewed by the maintainer before they are used (`feedback-endpoint/`).

## Research

The evaluation, the referee data and every run are in [`research/`](research/), summarized in
[EVALUATION.md](EVALUATION.md). A sample dashboard on a published paper, with its referees'
real concerns overlaid: `research/eval/sample/2601.01843/dashboard.html`.

## Status

Version 0.2, an early release for feedback from working physicists. Known limits: Word
documents are not supported yet (use a PDF); the presentation and copy lanes are not yet
measured; the measurements so far are judged by an AI model, not yet by physicists.

## License

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE), which credits the published work
the review prompt builds on.
