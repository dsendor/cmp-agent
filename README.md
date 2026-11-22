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
**[Shared knowledge for condensed matter physics](https://cmp.sendorai.com/)**.

Referee preview is the first step: a tool that is useful to a working physicist today, built
on what the field already knows about how claims fail. The major next step is a shared record
of what has been tried: experiments, controls and dead ends, recorded as they happen and
shared, so that the next lab starts from what the field has already learned. Feedback that
authors choose to share from this plugin (see below) is the first small piece of that record.

## Also in this repository

**[Lab notes](lab-notes/)**: an AI lab notebook. Dictate notes, drop in notebook photos and
instrument runs, and get a record where every number cites its source; procedure manuals from
dictation; plots the lab's way. `/plugin install lab-notes@cmp-agent`.

## Install

In Claude Code:

```text
/plugin marketplace add dsendor/cmp-agent
/plugin install referee-preview@cmp-agent
```

To try it for one session from a clone, without installing: `claude --plugin-dir <path to this repository>`.

**Without Claude Code (claude.ai).** A basic version runs as a claude.ai skill: one Claude
does every lane in turn, and you download the dashboard. Install steps, written for someone
who has never installed a skill: [claude-ai/README.md](claude-ai/README.md). It is untested
in claude.ai so far; Claude Code is the tested route. After changing `engine/`, the scripts or
the dashboard template, rebuild the committed zip with `bash scripts/package_skill.sh`.

Needs Python 3. `pdftotext` (poppler) is optional; without it, quotes are not checked against
the paper. The review is written for Claude Opus; other models work but are not measured.

## Use

```text
/referee-preview:review path/to/paper.pdf
/referee-preview:review path/to/latex-folder --journal "Physical Review B"
/referee-preview:review 2601.01843 quick
/referee-preview:publish                             # share the dashboard as a private claude.ai link
/referee-preview:compare <old review folder> new.pdf  # a revision: what changed, what referees likely asked
```

The review runs three independent scientific reviews in parallel and merges them (about 10 to
25 minutes on your Claude Code plan); say "quick" for one review. It writes a folder
`referee-preview/<paper>-<date>/` next to the paper and opens `dashboard.html`.

It looks at the paper in four lanes:

- **Science:** does the evidence support the conclusions (controls, samples, artifacts,
  heating, calibration, fits, alternative explanations, theory).
- **Presentation:** overclaiming, unclear claims, missing context, figures and captions.
- **Novelty:** checks the paper's "first" and "has not been shown" statements against its own
  references and an arXiv search, lists the closest prior papers, and grades each claim:
  *precedent exists*, *extends close prior work*, or *no precedent found in the searches*. It
  needs network access.
- **Copy:** numbers that disagree between text and figures, notation, numbering, language.

In the dashboard:

- **Start here** opens with what the paper does well, the major points, where the paper sits
  in the literature, and each claim with two routes: narrow the wording, or support it as
  written.
- **By importance** sorts by *must address* (the conclusion does not follow without it),
  *should address* (a claim is weaker), *minor*. **In page order** follows the paper page by
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

**Sharing it as a link.** `/referee-preview:publish` publishes the dashboard and `paper.pdf` as
a private Claude artifact, which you can then share from its page on claude.ai. It needs a
client with Claude artifacts, such as the Claude desktop app, and asks before uploading
anything. Co-authors you share it with mark items under their own names and see each other's
choices; you and any editors set the agreed decision for each item, and Discuss opens a
claude.ai comment thread on it. `/referee-preview:apply` then reads the agreed decisions from
the artifact. In the published page arXiv opens in a new tab rather than the PDF pane. Details
in [docs/shared-review.md](docs/shared-review.md).

**After peer review.** `/referee-preview:compare` takes the reviewed version and the revision.
It reviews the revision blind, infers from what changed what the referees most likely asked
(referee reports are rarely available), and judges whether the revision answers each point.
The dashboard's **Referee feedback** view walks through them, and **Version comparison**
lists every change. Each comparison leaves a revision record in `~/.referee-preview/revisions/`
so changes can be tracked from version to version. See [docs/revisions.md](docs/revisions.md).

## Your data

- Your paper is read by Claude Code on your machine and sent only to the model, as in any
  Claude Code session. The plugin has no server and sends nothing anywhere else, unless you
  choose to publish a dashboard as a Claude artifact (`/referee-preview:publish`).
- Your house style, standing rules and a history of reviews and decisions live in
  `~/.referee-preview/`, outside the plugin, so updates never touch them.

## How it works

| | |
|---|---|
| `skills/review/`, `skills/apply/`, `skills/publish/`, `skills/compare/`, `skills/contribute/` | the five commands |
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

Version 0.3, an early release for feedback from working physicists. Known limits: Word
documents are not supported yet (use a PDF); the presentation and copy lanes are not yet
measured; the measurements so far are judged by an AI model, not yet by physicists.

## License

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE), which credits the published work
the review prompt builds on.
