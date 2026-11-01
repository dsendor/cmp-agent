---
name: contribute
description: Shares an author's Referee preview decisions to improve the shared plugin, after a redaction step the author controls. Builds a contribution at the level the author picks (labels only, generalized text, item text, or full with quotes for public papers), scrubs it for anything that identifies the paper, shows exactly what will be sent, and sends it only on the author's yes. Use when the user says "share my feedback", "contribute", or invokes /referee-preview:contribute.
---

# Referee preview: share feedback

Nothing leaves the machine unless the author says yes to the exact file. Drafts are
unpublished work: when in doubt, share less.

## 1. Find the review

The most recent `referee-preview/*/review.json` under the current directory, unless the user
names one, and `decisions.json` beside it (the apply step copies it there; otherwise find the
exported decisions file as the `apply` skill does and copy it in). Only decided items are shared.

## 2. Choose a level

Explain the four levels in one short table and ask which one, for the whole review:

| Level | What is shared for each decided item |
|---|---|
| 0. Labels | lane, topic, importance, effort, the decision. No text at all |
| 1. Generalized | level 0 plus the item rewritten with no materials, sample or device names, numbers, figure or section numbers |
| 2. Item text | level 0 plus the item as reviewed and the author's note, with no quote from the paper |
| 3. Full | everything, quotes included; only for a paper that is already public |

Level 0 is the default. Offer level 3 only if the paper is on arXiv or published.

## 3. Level 1: write the rewrites

For each decided science or presentation item, rewrite its `issue` as one sentence a reader
could not trace to this paper: keep the kind of concern (a missing control, heating, a fit with
too many free parameters), drop every material, number, sample name, figure, section and
technique detail that narrows it to one paper. Write them to `<folder>/rewrites.json` as
`{"S01": "...", ...}`, show them to the author, and change any the author asks to change.

## 4. Build and scrub

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/contribute.py <folder> --level <n> [--rewrites <folder>/rewrites.json]
```

If it lists hits (the title, the arXiv id, words copied from the paper, numbers with units,
formulas, or anything in the author's "## Never share" list in `~/.referee-preview/my-style.md`),
fix each one: rewrite it (level 1), drop the item, or, only when the author says the hit is
fine to share, pass its id with `--allow`. Run the script again until it reports no hits.

## 5. Show, then send

Show the author `<folder>/contribution.json`: the level, the number of items, and every text
field in full. Ask: "Send this?" Only on a clear yes:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/contribute.py <folder> --level <n> [--rewrites ...] [--allow ...] --send
```

It goes to the maintainer's feedback inbox, where each contribution is reviewed before it is
used. If no endpoint is configured or sending fails, tell the author the file is saved at
`<folder>/contribution.json` and that the plugin's README says where to email it.
