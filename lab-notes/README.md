# Lab notes

An AI lab notebook for experimental physics, as a Claude Code plugin. You talk, type, or drop
in photos and files; it keeps a record in your project where every number says where it came
from. Version 0.1, early: built to try with a few researchers and improve from what they say.

| Command | What you do | What you get |
|---|---|---|
| `/lab-notes:setup` | once per project | a `lab-record/` folder; it finds your notebooks and data |
| `/lab-notes:note` | dictate or type what you did or saw; attach a notebook photo, a screenshot, a data file | an entry where each number, setting and run cites its source, with failed runs and missing details listed as questions |
| `/lab-notes:procedure` | talk through a procedure while you do it | a step-by-step manual for the next student, with your tips, revised each time someone does it |
| `/lab-notes:learn` | point it at the lab's good example notebooks | a lab guide: how this lab loads, corrects and plots its data |
| `/lab-notes:plot` | "plot run 214" or "plot yesterday's sweep on D7" | the figure, the script that made it, and the plotted numbers as CSV, ready for a paper's data deposit |

You don't need to type the commands: say what you want ("log this", "let me walk you through
the cooldown", "plot the last run") and Claude picks the skill.

## Install

In Claude Code (the desktop app's Code tab, or the terminal):

```text
/plugin marketplace add dsendor/cmp-agent
/plugin install lab-notes@cmp-agent
```

Then open your project folder and say "set up lab notes here". Needs Python 3. QCoDeS isn't
needed to read QCoDeS databases; the plugin reads them directly.

## Talking to it

- **Dictate in the Claude desktop app.** Click the microphone in the message box and talk as
  you would to a labmate. It saves your words exactly as you said them, then structures them.
- **Attach photos and files in the chat**: a notebook page, a screenshot, a data file. Drag
  the file in from Finder or Explorer if you can: then the photo itself is kept in the record.
  Pasted images work too; it transcribes them, but the image isn't kept, and it says so.
- **Lots of files at once, or from your phone without opening Claude:** save them into
  `lab-record/inbox/` (any synced folder works) and later say "process my inbox".

Unreadable handwriting is marked `[illegible]` and asked about; it never guesses a digit or
a unit.

## Who wrote what, and keeping it short

- **AI text is marked, by code.** Every file has `author` (ai, person or mixed) and
  `checked` (ai until a person says it's right) properties. Where a file has both, the AI's
  paragraphs sit between `🤖 AI <date>` and `🤖 end` lines. You never tag anything: the
  plugin fingerprints what the AI writes, so your edits are noticed on their own.
- **Git, if you want it:** the AI commits only its own writing, marked as AI, and leaves any
  file you edited for you.
- **TL;DR first** in every file, and entries stay under about 300 words; the detail is in the
  sources, linked.

## Browsing it

Open `lab-record/` as a vault in [Obsidian](https://obsidian.md) (or any Markdown viewer).
Entries have properties (date, device, runs, checked), and the plugin rebuilds a page per
device, a `timeline.md` and an `open-questions.md` each time it writes. Search `tag:#ai` for
everything a person hasn't checked yet.

## What it promises

- **Originals are never changed.** Photos, dictation and files are copied into
  `lab-record/originals/` once, read-only, with a fingerprint (sha256).
- **Every fact points to its source,** and `scripts/verify.py` checks that in code, not by
  asking the AI: it re-reads every cited database run, CSV cell and quote and fails on any
  mismatch, missing unit, or a source changed since it was cited. Photo transcriptions are
  listed for you to check by eye.
- **Failures are kept.** Aborted runs (QCoDeS records the crash), dead devices and
  disagreements between your notes and the instrument are written down, not smoothed over.
- **Read only on instruments.** It reads files your measurement software already saved. It
  never controls an instrument. Plots load a copy of a QCoDeS database, because QCoDeS can
  rewrite a file it opens.
- **AI-drafted, and it says so.** Each entry shows which items a person has confirmed. You
  confirm only what it flags, not every line.

## Your data

Files stay in your project. What Claude reads to write an entry (your words, the photo, the
run's settings) is sent to the model, as in any Claude Code session. Nothing is shared
anywhere else. The record is plain files (markdown and JSON) you can read, copy or delete
without the plugin. Put the project under git and you get its history for free.

If your lab or institution restricts sending unpublished data to an AI service, check before
using it on that data.

## Claude Science

The skills use the open Agent Skills format and can be imported into Claude Science from
GitHub (Settings, Skills, Import from GitHub). That route is untested so far; Claude Code is
the tested one.

## Files

| | |
|---|---|
| `skills/` | the five commands; each folder carries copies of `scripts/` and `docs/record-format.md` so it works when imported on its own |
| `scripts/record.py` | the record: set up, save originals, entry ids, index |
| `scripts/qcodes_runs.py` | read a QCoDeS database read-only: list runs, show settings, diff two runs, flag aborted runs |
| `scripts/verify.py` | check every fact against its source, and that each entry has a TL;DR and stays short |
| `scripts/authorship.py` | who wrote what: fingerprints the AI's paragraphs, marks AI text, records a person's check, commits only the AI's writing |
| `hooks/hooks.json` | in Claude Code, runs `authorship.py` around the AI's own edits in `lab-record/` |
| `docs/record-format.md` | the record's format, for people and other tools |
| `tests/run_tests.py` | end-to-end test on a simulated database (`python3 lab-notes/tests/run_tests.py`) |
| `tests/sync_skills.py` | refreshes those copies after a script changes (`--check` fails if they've drifted; the tests run it) |
| `tests/make_test_db.py` | makes that database with QCoDeS's simulated instruments |
| `tests/build_test_kit.py` | builds a test kit for trying the skills by hand: a fake lab project with planted problems, the skills packaged for Claude Science upload, published data (Riggert et al. 2025, CC BY 4.0), and prompts with what a good answer does |
