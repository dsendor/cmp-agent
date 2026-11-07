---
name: apply
description: Applies the decisions an author made in the Referee preview dashboard. Accepted copy edits and accepted rewordings go into the LaTeX source, the paper is recompiled where possible, and the change is committed so it can be undone in one step; then Claude works through each item the author marked Will fix, offering concrete help guided by the author's notes. Use when the user says "apply my decisions", "apply the edits", or invokes /referee-preview:apply, usually with the decisions file name the dashboard's Send to Claude button copied.
---

# Referee preview: apply decisions

## 1. Find the files

- **The review.** The most recent `referee-preview/*/review.json` under the current directory, unless the user names one.
- **The decisions.** Decisions pasted in the message (a JSON object with `"schema": "referee-preview/decisions/1"`, which the dashboard published as an artifact copies): save them as `decisions-<review id>.json` in the review folder and use that. Otherwise, the file named in the command (the dashboard's Send to Claude button copies `/referee-preview:apply decisions-<review id>.json`), or `decisions-<review id>.json` for the most recent review. Look in the current directory, the review folder, `~/Downloads`, `~/Desktop` and `~/Documents`, in that order. If several match, take the newest and say which. If none, ask the user to click Send to Claude in the dashboard and say where it saved the file.
- **The source.** `review.json` field `paper.source`, or ask for the LaTeX folder. Without source (PDF only), skip to step 4: nothing can be applied, and the revision plan lists the accepted edits for the author to make by hand. Word is not supported yet.

Copy the decisions file into the review folder as `decisions.json` and `~/.referee-preview/history/<review id>.decisions.json`.

## 2. What gets applied

| Decision | Item | Applied |
|---|---|---|
| `accept` | copy edit | `edit.before` to `edit.after` |
| `edit` | copy edit | `edit.before` to the user's `after` |
| `will_fix` | presentation item with an `edit` | `edit.before` to `edit.after` |
| `scope_claim` | science item with an `edit_scoped` | `edit_scoped.before` to `edit_scoped.after` |
| anything else | | nothing: it goes to the revision plan |

Science items marked `will_fix` are work for the authors and are never edited into the paper.

## 3. Apply

1. **Checkpoint.** If the source folder is a git repository with uncommitted changes, ask the user to commit or stash first, and stop. If it is a repository, note the current commit. If it is not, copy the folder to `<folder>.before-referee-preview-<timestamp>` and say where.
2. **Edit.** For each item, find `before` in the named `.tex` file (or in any `.tex` file of the project when `file` is null). Replace it only when it occurs exactly once; when it occurs zero or several times, skip the item and record why. Never edit inside math unless the item is a copy edit whose `before` is math.
3. **Compile**, when `latexmk` or `pdflatex` is available. If the build fails, read the log, find the edit responsible, revert that one edit, record it, and build again.
4. **Commit** (git projects): one commit, "Referee preview: apply N accepted edits", listing the item ids. Tell the user that `git revert <commit>` undoes all of it.

## 4. Revision plan

Write `revision-plan.md` into the review folder:

- **To do**, the science and presentation items marked `will_fix` with no edit, grouped by effort (text, existing data, new work), each with its fix and the user's note.
- **Applied**, each applied edit by id.
- **Not applied**, each skipped edit and why, for the author to make by hand.
- **Set aside**, items marked already in the paper, disagree, not worth it or reject, with notes.
- **Undecided**, the count.

## 5. Report what was applied

In a few lines: how many edits were applied, skipped and reverted, whether the paper compiled, where the plan is, and how to undo.

## 6. Help with the items the author will fix

Go through the items marked `will_fix` that were not applied as edits, most important first (must address, then should address, then minor). For each one:

1. Say in one or two sentences what the item asks for, and quote the author's note if there is one: the note is the author's instruction and takes precedence over the item's suggested fix.
2. Offer the help that fits its effort:
   - **Text edit:** draft the change (a caveat, a limitation sentence, a citation, a clarified definition) as a diff to the source, and apply it only when the author says yes.
   - **Reanalysis:** propose the analysis, and offer to write the script or notebook that does it if the author points you to the data.
   - **New experiment:** outline the measurement or calculation that would settle it, and draft the sentence the paper can carry until it is done.
3. Ask whether to go on, skip, or stop. The author decides the pace; never change the paper without a yes.

Record what was done for each item in `revision-plan.md`. When the author stops, offer the next step: after revising, run the review again on the new draft.
