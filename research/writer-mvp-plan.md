# Writer-mode reviewer skill: MVP plan

*AI only. Written 2026-10-29 for David. It replaces Bill's Notion page "Claude instructions:
lock the reviewer, run ship checks, build the review dashboard" where the two differ, and
keeps the rest of it. Background: `eval/step3-report.md`, `eval/step4-plan.md`, `eval.md`.*

## Decisions (David, 2026-10-29)

- **Writer mode first.** The user is an author checking their own paper before submission.
  Reviewer mode is parked (journals restrict uploading manuscripts under review to AI tools).
- **Claude Code only** for the MVP. ChatGPT is parked.
- **David sees a sample dashboard before any test spend.** The ship checks run after his
  review of it.
- **The reviewing engine stays prompt D, frozen.** Writer mode lives in the passes added around
  it and in the dashboard. That keeps the eval numbers true of what ships.
- **Three runs as subagents, merged,** is the writer-mode default; one run is the quick option.
- **A single HTML file** for the dashboard, with the PDF beside it at the cited page, and
  decisions saved by export.

## The workflow, six stages

| Stage | What the user gets | Built from |
|---|---|---|
| 1. Find | every issue, in three lanes: science, presentation, copy | prompt D (science), two new passes |
| 2. Sort | each issue placed by importance (tier) and by effort to fix | structuring step |
| 3. Walk through | a triage view and a page-by-page view, with the PDF beside them | dashboard |
| 4. Apply | accepted edits written into the LaTeX source, compiled, committed; the rest a revision plan | Claude Code, from the exported decisions |
| 5. Re-check | after revising, each open issue checked against the new draft: resolved, partly, open | one cheap call per issue |
| 6. Learn | a personal record that tunes the skill, a scorecard once real referee reports arrive, an opt-in contribution to the shared skill | local files |

David's four steps are stages 1, 2, 3 and 6. Stages 4 and 5 are added: an accepted edit is
only useful once it is in the source, and an author who revises needs to know which issues the
revision closed.

### 1. Find: three lanes

| Lane | Covers | Engine | Measured? |
|---|---|---|---|
| Science | does the evidence support the conclusions: controls, samples, artifacts, fits, alternative explanations (the 11 CMP themes) | prompt D v1.0, unchanged | yes on dev (49% of referee concerns, one run; 53% for three Liang et al. runs merged); test22 pending |
| Presentation | overclaiming, claims stated more strongly than the data, missing citations and prior work, unclear figures and captions, framing for the target journal | new pass | no; the referee concerns already extracted include 78 presentation and 44 novelty concerns on 20 dev papers, so a `score.py` change can measure it at no API cost |
| Copy | numbers that differ between text, figures and tables; units and notation; undefined acronyms; figure, equation and reference numbering; spelling and grammar | new pass, plus checks a script can do exactly (LaTeX log: undefined references, duplicate labels) | no |

The copy lane is collapsed by default and shows a count, so eighty comma fixes never sit above
a tier A science issue. Spelling and grammar are table stakes (Overleaf and Grammarly do them);
the copy items worth most here are the consistency ones, theme 11 of the CMP list.

**Inputs.** The paper's source, the compiled PDF, and the supplementary information. Without
the SI the skill asks for things the SI already contains. Two source formats (David,
2026-10-29: assume both until we know what authors use):

- **LaTeX** (built first): the source folder, an Overleaf project cloned with git or its
  download zip.
- **Word** (built second): the `.docx`. Accepted edits go back as tracked changes and comments,
  so the author's own Word review pane becomes a second walk-through.

PDF only also works, with suggestions and no edits applied. The target journal is optional and
feeds the presentation lane only.

### 2. Sort: importance and effort

Importance is the tier from prompt D: A (the conclusion does not follow without it), B (a claim
is weaker), C (minor). Copy items have no tier.

Effort is one of three classes, set by the structuring step:

| Effort | Means | Typical time |
|---|---|---|
| Text | reword, add a caveat or limitation, cite, fix a label | minutes |
| Existing data | reanalysis, a new plot or panel, error bars, report fit parameters | hours to days |
| New work | a new measurement, sample, device or calculation | weeks |

**Two routes for hard issues.** For a tier A or B issue that needs existing data or new work,
the skill offers two fixes side by side: do the work, or scope the claim down to what the data
supports, with the exact rewording. Often the second is what a referee would accept, and it
turns a weeks-long issue into a text edit.

The overview shows a grid of tier against effort. The "quick wins" cell (tier A or B, text
effort) is where an author starts.

### 3. Walk through

**Triage view.** Issues sorted by lane, then tier, then effort. One decision per issue, with
keyboard shortcuts:

- Science and presentation: *Will fix*, *Fix by scoping the claim*, *Already in the paper*,
  *Disagree*, *Not worth it*, plus a note.
- Copy: *Accept*, *Reject*, *Edit*.

**Walk-through view.** The same issues in paper order, page by page, with the PDF in a frame
opened at the cited page (`paper.pdf#page=7`). This is the editing pass: an author fixes a
paper top to bottom, and decides priorities in tier order.

Every card shows the claim it affects, the quote from the paper with page and figure, a
"quote found" badge from `check_evidence.py`, the proposed fix, and for edits a before and
after diff.

**What can be accepted in bulk.**

| Risk | Which items | How |
|---|---|---|
| Low | copy edits that touch prose only | accept a whole section at once, after a diff preview |
| Medium | presentation rewordings, including scoping a claim | one at a time, diff shown, editable |
| High | science issues | never applied as edits; each becomes a to-do with its fix. A caveat or limitation sentence can be drafted on request and accepted one at a time |

A copy edit that would change a number, symbol, unit, citation or a hedge word ("significant",
"demonstrate", "evidence", "suggest", "consistent with") moves to medium automatically. Those
words carry scientific meaning.

### 4. Apply

The dashboard exports `decisions.json` (a download; in Chrome, after one permission click, it
can save straight into the review folder). The user tells Claude Code "apply my decisions".
Claude Code then:

1. commits the current source as a checkpoint, so one command undoes everything;
2. applies accepted low and medium edits to the `.tex` files, or for Word writes them into the
   `.docx` as tracked changes;
3. compiles, and reverts any edit that breaks the build or changes the page count unexpectedly;
4. commits, and writes `revision-plan.md`: the science to-dos grouped by effort, each with its
   fix and the user's note.

### 5. Re-check

After the author revises, "re-check" sends the new draft and the open issues, one short call per
issue: resolved, partly resolved, or open, with the evidence. It costs a fraction of a new
review. A fresh full review is a separate option, for issues the revision introduced.

### 6. Learn

**Personal record, across projects.** Each paper's review folder keeps its own `review.json`,
`decisions.json` and dashboard. One user-level folder, `~/.cmp-reviewer/`, holds what carries
across papers:

- `my-style.md`: house style (spelling variant, "we", notation) and the user's standing rules;
- `history/`: a copy of every review and decision file, with an index by paper and date;
- `contributions/`: the opt-in files for the shared skill.

The folder sits outside the skill (`~/.claude/skills/...`), so updating the skill never touches
the user's data. The skill reads `my-style.md` at the start of every run and writes to
`history/` at the end. Claude Code asks once for permission to read and write the folder; the
skill's setup step adds it to the user's allowed directories. A user who works on two machines
can make the folder a private git repository or keep it in a synced drive.

**Learning from decisions: the user sets the rules.** Every decision on a paper is final for
that paper; a dismissed issue stays dismissed. Rules for future papers come from the user
explicitly: "stop flagging British spelling", "don't raise sample counts for my STM papers". The
skill can propose a rule when it sees a pattern, and the user accepts or rejects it. In the copy
lane, proposed rules are low stakes. In the science lane, the skill does not infer a rule from
dismissals on its own: a dismissal on one paper can be specific to that paper (the data exist,
the referees for that journal never ask), and a silent rule would remove the issue from every
later paper without the author ever choosing that. A user who wants a science topic muted mutes
it, in one step.

**Referee scorecard.** When the real referee reports arrive, the user drops them in. The skill
matches them to its own issues with the eval's judge prompt and reports what it predicted, what
it missed, and which dismissed issues the referees raised. This is the eval's metric on real
drafts, and the best data the project can collect: it shows which dismissals were right.

**Shared skill, opt-in, through GitHub (David, 2026-10-29).** Nothing leaves the machine by
default; drafts are unpublished work. Contributions go to a private feedback repository as pull
requests, so David reviews each one before it joins the shared data. The skill itself ships from
a separate repository, which Claude Code can install as a plugin, so feedback and code never mix
and the code can go public later without the feedback.

The `contribute` step walks the user through redaction before anything is sent:

1. **Choose a level**, for the whole review, with per-item overrides:

   | Level | What is shared per issue |
   |---|---|
   | 0. Labels | lane, topic, tier, effort, decision, reason and, after a scorecard, whether a referee raised it. No text |
   | 1. Generalized | level 0 plus the issue rewritten without specifics: no materials, sample or device names, numbers, figure or section numbers. The user approves each rewrite |
   | 2. Issue text | level 0 plus the issue as written, with paper quotes removed |
   | 3. Full | everything, quotes included; offered only once the paper is public (arXiv or published) |

2. **Automatic scrub.** A script searches the contribution for anything that identifies the
   paper: its title, author names, arXiv or DOI identifiers, any run of six or more words that
   also appears in the paper, numbers with units, chemical formulas, and names from the user's
   own block list in `my-style.md`. Every hit blocks the contribution until the user removes,
   generalizes or explicitly allows it.
3. **Preview.** The dashboard shows the exact file that will be sent, item by item, with hits
   highlighted.
4. **Send.** The skill commits the file to a branch of the feedback repository and opens a pull
   request, using the user's own GitHub login. A user without GitHub, or who prefers not to be
   named, saves the file and emails it to David; David commits it without their name.

The contributor's GitHub username is visible to David on the pull request; the merged data stores
a random contributor id. David curates contributions into the shared skill (checklist items,
per-technique checklists, new lookalikes), each starting `checked: ai`.

## Data files

`review.json`, top level: paper id and title, source and PDF paths, reviewer version, model,
mode (one run or three), date, target journal, the paper's main claims. Per issue:

| Field | Content |
|---|---|
| `id` | stable, for example `S07`, `P03`, `K41` (science, presentation, copy) |
| `lane` | science, presentation, copy |
| `tier` | A, B, C (none for copy) |
| `effort` | text, existing data, new work |
| `topic` | one of the 11 CMP themes, or `other` |
| `claim` | the paper's claim it affects |
| `issue` | one to three sentences |
| `evidence` | exact quote from the paper, page, figure or section |
| `evidence_found` | result of `check_evidence.py` |
| `fix` | the fix; for tier A or B with effort above text, also `fix_scoped`, the claim rewording |
| `edit` | for applicable items: file, line, before, after |
| `risk` | low, medium, high |
| `runs` | which runs raised it (three-run mode) |

`decisions.json`: per issue, the decision, the reason, any edited text, a note, a timestamp.
`score.py` can read it later as human ratings.

## Build order

| Step | What | Cost | Gate |
|---|---|---|---|
| M0 | Freeze the engine in `referee-preview/engine/` (the plugin, to become its own open-source repository), tagged v1.0, hashes in `eval.md` (U6): prompt D; the structuring prompt (new, based on `prompts/rank.md`, adding the paper quote, page, claim, effort and edit); `merge.md` with one change, keeping which runs raised each concern | none | |
| M1 | **Sample dashboard for David.** One `marg10` paper with arXiv LaTeX source. Uses its three existing prompt D reviews, merged, structured, plus the presentation and copy passes on the source. Because it is a dev paper, a demo-only marker shows which issues the real referees raised. | about $2 | **David reviews it and adds missing steps** |
| M2 | Skill end to end in Claude Code: one command on a PDF, one run, dashboard opens with no manual steps | a few dollars | |
| M3 | Source mode: copy and presentation lanes on LaTeX, the apply loop, checkpoints, compile check | a few dollars | |
| M3b | Word: read the `.docx`, write accepted edits back as tracked changes and comments | a few dollars | |
| M4 | Three runs as subagents, merged; the writer-mode default | a few dollars | |
| M5 | Re-check | small | |
| M6 | Personal record, `my-style.md`, referee scorecard | small | |
| M7 | Contribution flow: redaction levels, scrub script, preview, pull request to the feedback repository. Creating the two repositories is David's call | none | David creates or approves the repositories |

**Ship checks** (Bill's Part 2, without ChatGPT), after M1 and before any physicist uses it,
capped at $100:

- test22, run once: plain, prompt D one run, prompt D three runs merged;
- the skill in Claude Code on 5 `marg10` papers with default settings, against the API runs of D;
- `check_evidence.py`: share of quotes found in the paper;
- overlap step on dev30: science issues from D that neither plain nor any referee raised, with
  10 examples for David;
- the `score.py` change that measures the presentation lane against referee presentation concerns.

**Author trial** after M4: two or three physicists run it on a draft of their own, and their
decisions are the first human ratings. Who to ask is David's call.

## Parked

Reviewer mode, ChatGPT, the local server view, a separate triage call, prompt D asked for more
concerns, per-technique checklists (these return through the contribution loop), Ai2 tools,
full MARG-S, several co-authors deciding on one review.

## Pushback, for David

1. **Bulk accept stays in the copy lane.** A presentation rewording can change what a paper
   claims, and a science issue is work, so neither is accepted in bulk.
2. **Science rules come from the user, never inferred from dismissals.** The user decides
   everything about their own paper and can mute any topic. What the skill avoids is muting a
   science topic for future papers on its own, from a pattern of dismissals. See stage 6.
3. **Effort and ordering inside a tier are untested AI estimates.** No prompt variant improved
   the order within a list. Keep effort to three classes, show it, let the user sort, and spend
   nothing on ranking until users say it is wrong.
4. **The new lanes are unmeasured.** The dashboard labels presentation and copy items as such
   until the `score.py` check and the author trial say otherwise.

## Answered by David (2026-10-29)

- **Source format:** both LaTeX and Word; David will find out which authors use. LaTeX is
  built first (M3), Word second (M3b).
- **Personal record:** across projects, in `~/.cmp-reviewer/` (stage 6).
- **Sample paper:** a `marg10` dev paper with the referee marker. Pick one with LaTeX source on
  arXiv. The `marg10` papers were left out when the CMP checklist was built, so the sample is
  fair to prompt D.
- **Contributions:** pull requests to a private GitHub feedback repository, after a redaction
  step the user controls (stage 6).
