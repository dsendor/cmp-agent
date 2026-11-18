---
name: deposit
description: Packages a paper's figures, the code that made each one and the data behind them as an RO-Crate, ready to upload to Zenodo or an institutional data repository, including which measurements no figure uses. Use when someone asks to prepare a data deposit, share the data behind a paper or its figures, make a Zenodo upload, a data availability statement or an RO-Crate, or invokes /lab-notes:deposit. Never uploads anything itself.
---

# Lab notes: package the data behind a paper

Journals and funders increasingly want the data behind each figure. Most labs assemble it by
hand, late. If the figures were made with the `plot` skill, each one already has its script,
its exact numbers and a record of which runs it used, so the deposit is mostly bookkeeping.

Scripts: paths below use `${CLAUDE_PLUGIN_ROOT}`, the plugin's folder. If it isn't set (for example in Claude Science), use the copies in `scripts/` and `docs/` in this skill's own folder, next to this file. If you can't find them, tell the person the skill was imported without its scripts and ask them to re-import it; don't rebuild the record by hand, because the scripts catch things a hand-built record misses, such as runs that crashed.

**Replying.** Short: what changed, then at most three questions, then a one-line TL;DR at the
very end.

Invoking this skill is the go-ahead to build the package in the project. Uploading it is
always the researcher's step: never upload, publish or send anything.

## 1. Which figures

Ask which figures are in the paper and their numbers ("Fig. 2a"), or read them off the
draft if they share it. Match each to a folder in `lab-record/figures/`. A figure with no
folder, or a folder without `figure.json`: say so; offer to remake it with the `plot` skill
so its sources are recorded. Never guess which run a figure used.

## 2. Build the crate

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/rocrate.py build lab-record <name> \
  lab-record/figures/<folder> ... --label <folder>="Fig. 2a" ... \
  --title "<paper title>: data and code for the figures" --license <URL>
```

Ask the license (CC BY 4.0 is the usual default for data; the lab or journal may require
another). Add `--no-data` if the databases are too large or not theirs to share; the crate
then references them by path.

It writes `lab-record/deposits/<name>/`: the figures, scripts and CSVs, a consistent copy of
each database cited, `ro-crate-metadata.json` (which code and runs made each figure) and a
`README.md`. It checks the crate's structure and reports problems; fix them and rebuild.

## 3. Show what it says, especially what isn't shown

Report: the figures and the runs each used, and the **measured but not shown** list from
the README (runs in the databases no figure uses, aborted ones marked). That list is a
strength, not an embarrassment: it is what lets a reader see a figure isn't the one good
try. If a run in it looks like one a reader would expect to see (a repeat of a shown
measurement), say so plainly and let the researcher decide whether to add it or explain it.

## 4. Hand over

Tell them how to upload, without doing it: zip the folder, then Zenodo, New upload, add the
zip (Zenodo keeps `ro-crate-metadata.json` inside it), fill in authors, and link the paper's
DOI once it has one. Suggest a data availability sentence for the paper with the Zenodo DOI
left as a placeholder. Mark that sentence as AI-drafted.

## Rules

- Nothing private goes in without asking: notes, entries and originals stay out of the crate
  unless the researcher asks for them by name.
- Only data the lab may share. If a database holds other people's runs, ask before
  including it.
