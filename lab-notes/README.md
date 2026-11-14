# Lab notes

An AI lab notebook for experimental physics, as a Claude Code plugin. You talk, type, or drop
in photos and files; it keeps a record in your project where every number says where it came
from. Version 0.1, early: built to try with a few researchers and improve from what they say.

| Command | What you do | What you get |
|---|---|---|
| `/lab-notes:setup` | once per project | a `lab-record/` folder; it finds your notebooks and data |
| `/lab-notes:note` | dictate or type what you did or saw; drop in a notebook photo, a screenshot, a data file | an entry where each number, setting and run cites its source, with failed runs and missing details listed as questions |
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

- **At the desk:** use dictation. On a Mac, press the dictation key (or `fn` twice) in the
  message box and talk; on Windows, `Win + H`. Talk as you would to a labmate. It saves your
  words exactly as you said them, then structures them.
- **At the bench, on your phone:** take photos and record a voice memo (the iPhone Voice
  Memos app shows a transcript). Save them into `lab-record/inbox/` (AirDrop, iCloud Drive,
  Dropbox, any synced folder works), and later say "process my inbox".
- **Photos of notebook pages and screenshots:** drop them into `lab-record/inbox/` or give
  the path. It transcribes what it can read, marks what it can't as `[illegible]` and asks,
  and never guesses a digit or a unit.

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
  never controls an instrument.
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
| `skills/` | the five commands |
| `scripts/record.py` | the record: set up, save originals, entry ids, index |
| `scripts/qcodes_runs.py` | read a QCoDeS database read-only: list runs, show settings, diff two runs, flag aborted runs |
| `scripts/verify.py` | check every fact against its source |
| `docs/record-format.md` | the record's format, for people and other tools |
| `tests/run_tests.py` | end-to-end test on a simulated database (`python3 lab-notes/tests/run_tests.py`) |
| `tests/make_test_db.py` | makes that database with QCoDeS's simulated instruments |
