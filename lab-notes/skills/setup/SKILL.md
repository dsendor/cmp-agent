---
name: setup
description: Sets up a lab record in the researcher's project folder so the other lab-notes skills can capture notes, procedures and plots there. Use when someone starts using lab-notes, asks to set up a lab notebook, lab record or lab-notes in a folder, or invokes /lab-notes:setup. Asks a few short questions, creates the folder, and finds the lab's existing notebooks and data.
---

# Lab notes: set up a lab record

You set up `lab-record/` in the researcher's project and learn where things are. Keep it
short: the researcher should be capturing notes within five minutes. Invoking this skill is
the go-ahead.

Scripts: paths below use `${CLAUDE_PLUGIN_ROOT}`, the plugin's folder. If it isn't set (for example when this skill was imported on its own into Claude Science), the scripts are in `scripts/` next to this file or two levels above it; find them before starting. The same goes for `docs/record-format.md`.

Everything this plugin writes is AI-drafted and says so. Originals (photos, dictation, data
files) are never changed or deleted.

## 1. Where

Use the current folder unless the researcher names another. If it already has
`lab-record/config.json`, say so and offer to update it instead.

## 2. Create it

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/record.py init lab-record --lab "<lab>" --project "<project>"
```

Ask only what you can't find, in one message: the lab or PI, the project, and who works on
it. If they'd rather skip, leave the fields empty.

## 3. Find what the lab already has (read only)

Look around the project, without changing anything:

- Jupyter notebooks (`*.ipynb`) and Python files: note the ones that load or plot data.
- QCoDeS databases (`*.db` with a `runs` table: check with
  `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/qcodes_runs.py list <db>`), HDF5, CSV, `.dat`,
  LabVIEW `.lvm` or `.tdms` files: note the folders.

Write what you found into `lab-record/config.json` (`qcodes_dbs`, `data_dirs`), with paths
relative to the project. Don't copy data.

## 4. Git

If the project isn't under git, offer to run `git init` in it (it gives the record a history
for free). If it is, offer to add `lab-record/` in a commit. Never add large data files: if a
data folder is inside the project, suggest adding it to `.gitignore`.

## 5. Tell them what they can do now

Three short lines, in their terms, not the plugin's:

- "Tell me what you did or saw, or drop in a photo of your notebook page" (`/lab-notes:note`).
- "Talk me through a procedure while you do it, and I'll write a manual for the next
  student" (`/lab-notes:procedure`).
- "Let me learn how this lab loads and plots data, so 'plot run 214' just works"
  (`/lab-notes:learn`, then `/lab-notes:plot`).

Suggest `learn` first if the project has notebooks: it makes everything else faster.
