# Revisions: tracking what changes from version to version

Journals rarely publish referee reports, but authors' revisions show what the referees
pushed on. `/referee-preview:compare` turns each pair of versions into a **revision record**:
what changed, what the referees most likely asked, whether the new version answers it, and
how an earlier review fared. Records add up to data on which concerns referees actually
raise, without needing the reports.

## The record (`revision.json`, schema `referee-preview/revision@1`)

Written by `scripts/revision.py` from the comparison lane's files (`engine/compare.md`).

| Field | What it holds |
|---|---|
| `old`, `new` | `{id, arxiv, label, review, reviewer}`: the two versions and the reviews made of them |
| `public` | true only if both versions are on arXiv |
| `verdict` | How the paper changed and what referees most likely pushed on |
| `metrics` | Below |
| `changes` | Every substantive change, kind, old and new page, whether it looks referee-driven |
| `inferred_requests` | What referees most likely asked, with confidence and the old review items that anticipated it |
| `issue_status` | Each old review item: addressed, partly, not addressed or moot in the new version |
| `unaddressed_major` | Major old items left alone, judged not raised or rebutted |
| `walkthrough` | Per request: verdict, what was asked, the response, the judgment, what could come up again, the blind review items on it |

## Metrics

- **Anticipation**: the share of inferred referee requests the old review raised. The
  closest thing to recall against referees we can get without the reports.
- **Missed**: the requests no old item anticipated. Each is a candidate gap in the reviewer.
- **Tier calibration** (`old_items_by_tier`): how the old review's A, B and C items fared.
  If tiers mean what they say, A items should be addressed far more often than C items.
- **Verdicts**: how many requests the new version looks to answer.

These rest on AI inference twice over (what was asked, then whether it was answered), so
they are signals until the inference is validated (below).

## Where records live

- **Private** (default): `~/.referee-preview/revisions/<old id>--<new id>.json`. Any record
  with an unpublished version stays here. It never enters this repository, and nor does
  anything from the author or their correspondence.
- **Public**: `research/eval/revisions/<old arXiv id>--<new arXiv id>.json`, only when both
  versions are on arXiv (`revision.py --public` checks for the ids). A private record can
  move here once its revision is posted, after the authors agree.

## Validating the inference

Before using the metrics to change the reviewer, check the inference against real reports.
The papers in `research/eval/referee/` have public referee reports. For each with an arXiv
v1 and a later version: run `/referee-preview:compare` with no reports, then score the
inferred requests against the actual first-round concerns (precision and recall, as in
experiment 11 of `research/eval.md`). Record it there as a new experiment. To grow the set,
`research/scripts/followup.py` finds arXiv papers that gained a new version.
