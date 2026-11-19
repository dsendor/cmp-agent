# The lab record: format

The record is a folder of plain files inside the researcher's project, under git. Anyone can
read it without the plugin. The plugin never changes or deletes an original: photos, voice
transcripts and instrument files are copied in once and hashed, and everything the agent
writes is derived from them.

```
lab-record/
  README.md            what this folder is (written by setup)
  config.json          lab, project, people, where instrument data lives, optional eLabFTW
  inbox/               drop zone: phone photos, voice memo transcripts, files to process
  originals/           copied inputs, never edited; named <date>-<sha8>-<name>
  entries/             one entry per session, idea or meeting
    2026-11-14-1530-d7-gate-sweep.md     the readable entry
    2026-11-14-1530-d7-gate-sweep.json   its sidecar: every fact and where it came from
  procedures/          step-by-step manuals, revised each time someone does them
  lab-guide.md         how this lab loads, corrects and plots data
  devices/D7.md        browsing pages, rebuilt by record.py index: one per device,
  timeline.md            every entry newest first,
  open-questions.md      and every open question, each linking to its entry
  index.json           rebuilt by record.py: entries, devices, runs, open questions
  authorship.json      which paragraphs the AI wrote, by fingerprint (scripts/authorship.py)
```

Open `lab-record/` as a vault in Obsidian, or read it in any Markdown viewer or on GitHub:
links are ordinary relative Markdown links.

## The entry (`.md`)

Readable by a person, in the lab's own words. It opens with frontmatter and a TL;DR:

```
---
title: D7 gate sweeps and field map
date: 2026-11-12
kind: session            # session | idea | meeting
devices: [D7]
cooldown: 3
runs: [1, 2, 3, 4]
checked: ai              # ai = AI only; human = a person read it and stands behind it
tags: [ai, d7]
author: ai               # set by the plugin: ai | person | mixed
---
# D7 gate sweeps and field map

**TL;DR:** Two gate sweeps at 0 and 0.5 T and an overnight map; run 2 crashed. The peak
near -0.6 V moves with field. Open: the line resistance and run 3's time constant.
```

The TL;DR is at most 60 words; the prose after it aims for under 300 (`verify.py` fails a
missing TL;DR and warns past 300 words). Then sections, each optional:

- **What was done**, **What was seen**, **Ideas**, **Problems and failed runs**,
  **Open questions** (things the record does not hold and someone should answer).
- Every number, setting, device or run mentioned carries a footnote marker `[^f3]` pointing
  to fact `f3` in the sidecar. Text with no marker is narrative, not a fact.
- Who wrote it and whether a person checked it is in the frontmatter (below), not in the
  text.

## The sidecar (`.json`)

```json
{
  "id": "2026-11-14-1530-d7-gate-sweep",
  "kind": "session",
  "created": "2026-11-14T15:30:00-05:00",
  "author": "who was at the bench (as given)",
  "drafted_by": "lab-notes plugin (AI)",
  "devices": ["D7"],
  "runs": [{"source": "qcodes", "db": "data/experiments.db", "run_id": 214, "guid": "..."}],
  "facts": [
    {
      "id": "f3",
      "field": "mixing chamber temperature",
      "value": 12,
      "unit": "mK",
      "source": {
        "type": "qcodes",
        "path": "data/experiments.db",
        "sha256": "...",
        "locator": {"run_id": 214, "parameter": "fridge.T_mc"}
      },
      "status": "instrument"
    },
    {
      "id": "f4",
      "field": "gate voltage range",
      "value": "-2 to 0.5",
      "unit": "V",
      "source": {
        "type": "dictation",
        "path": "originals/2026-11-14-a1b2c3d4-dictation.txt",
        "sha256": "...",
        "quote": "swept the gate from minus two to half a volt"
      },
      "status": "stated"
    }
  ],
  "failures": [{"what": "run 213 aborted after 40 points", "fact": "f7"}],
  "questions": ["Which cooldown is this? The notebook page doesn't say."],
  "confirmed": [{"fact": "f4", "by": "name", "at": "2026-11-14T16:02:00-05:00"}]
}
```

### Source types and how each is checked

| `type` | `locator` | Checked by `verify.py` |
|---|---|---|
| `qcodes` | `run_id`, and `parameter` (`instrument.param` in the snapshot) or a run field (`name`, `sample_name`, `completed`, `points`) | yes: re-reads the database |
| `file` (CSV, TSV) | `row` (1-based, header is row 1), `column` (name or 1-based number), and `unit` if the file stores the value in a different unit from the fact (file in A, fact in nA) | yes: re-reads the cell |
| `json` | `pointer` (JSON pointer, `/a/b/0`) | yes |
| `dictation`, `text` | `quote`: the exact words in the transcript or note | yes: the quote must appear in the file |
| `attachment` | `quote`: the exact words in the transcription of an image attached in the chat with no file (the image itself isn't kept) | partly: the quote must be in the transcription; then listed for a person |
| `photo`, `pdf` | `page`, `region` (words, e.g. "top right, under 'cooldown 3'") and `quote` (what the page says, transcribed) | no: listed for a person to check against the crop |
| `inferred` | `from`: the fact ids it was inferred from, and `reason` | the facts it rests on are checked |
| `person` | who said it, when (answered an open question) | no |

`status` is one of `instrument` (read from an instrument file), `stated` (written or said by
a person, transcribed), `inferred` (the agent's inference, never shown as a fact), or
`not recorded` (asked for, not in any source; `value` is null).

Units are required for every number that has one. A number with no unit and no source is
not written.

## Who wrote what

Only the AI marks anything; people never tag their own text.

- `author`: `ai` (every paragraph is the AI's), `person`, or `mixed`. Set by
  `authorship.py mark`, which `record.py index` runs.
- `checked`: `ai` until a person says the file is right (`authorship.py check`, with
  `checked_by` and `checked_on`). Any later change, by anyone, returns it to `ai`.
- The tag `ai` while any AI text remains, so "everything still AI only" is one search.
- In a `mixed` file, each run of AI paragraphs sits between a line `🤖 AI YYYY-MM-DD` and a
  line `🤖 end`. Text outside them is a person's.

How it knows: `authorship.json` holds a fingerprint (sha256) of every paragraph the AI
wrote, recorded as it writes (`authorship.py write`, or a Claude Code hook around its own
edits). A paragraph with no AI fingerprint is a person's, so an edit is noticed with nobody
saying so, and the AI never takes its own text for a person's. Marker lines and frontmatter
are not fingerprinted, so marking changes nothing.

Git: `authorship.py commit` commits only files whose new paragraphs are all the AI's, with
the message starting `🤖 lab-notes:` and the trailer `AI-Generated: lab-notes plugin`. A file
a person edited is left for them to commit. So git history and the fingerprints agree, and
nothing depends on the AI remembering to commit.

## What is never done

- No original is edited, renamed in place or deleted. `originals/` is append-only.
- No value is smoothed over. If the notebook and the instrument disagree, both facts are
  kept and the disagreement goes in **Open questions**.
- No instrument is controlled. The plugin reads files the lab's software already saved.
