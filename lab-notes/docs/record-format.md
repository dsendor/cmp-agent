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
  index.json           rebuilt by record.py: entries, devices, runs, open questions
```

## The entry (`.md`)

Readable by a person, in the lab's own words. Sections, each optional:

- **What was done**, **What was seen**, **Ideas**, **Problems and failed runs**,
  **Open questions** (things the record does not hold and someone should answer).
- Every number, setting, device or run mentioned carries a footnote marker `[^f3]` pointing
  to fact `f3` in the sidecar. Text with no marker is narrative, not a fact.
- The first line under the title says the entry is AI-drafted, and which items a person has
  confirmed.

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
| `photo`, `pdf` | `page`, `region` (words, e.g. "top right, under 'cooldown 3'") and `quote` (what the page says, transcribed) | no: listed for a person to check against the crop |
| `inferred` | `from`: the fact ids it was inferred from, and `reason` | the facts it rests on are checked |
| `person` | who said it, when (answered an open question) | no |

`status` is one of `instrument` (read from an instrument file), `stated` (written or said by
a person, transcribed), `inferred` (the agent's inference, never shown as a fact), or
`not recorded` (asked for, not in any source; `value` is null).

Units are required for every number that has one. A number with no unit and no source is
not written.

## What is never done

- No original is edited, renamed in place or deleted. `originals/` is append-only.
- No value is smoothed over. If the notebook and the instrument disagree, both facts are
  kept and the disagreement goes in **Open questions**.
- No instrument is controlled. The plugin reads files the lab's software already saved.
