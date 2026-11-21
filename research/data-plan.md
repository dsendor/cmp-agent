# Data and evaluation plan: learning from how papers change

*AI-written plan, 2026-11-21. Nothing here has run yet. Builds on `eval.md` (the referee
match), `eval/proxies.md` (which sources publish reports) and `../docs/revisions.md` (the
revision record).*

## Why

Two lessons from the first author to use the plugin on their own paper:

1. **The first review was valuable.** It found the points the paper had not backed up, and
   the authors fixed most of them before submitting.
2. **The review of the revision felt like it was "trying to find something".** It still had
   five *must address* items, some of which the author judged wrong or already answered in
   the text. The author asked: once everything is fixed, will it ever say the paper is ready?

The reviewer has no stopping rule. Its tiers are relative: about a third of any review is
*must address*, however strong the paper. This plan builds the data to set an absolute
standard, defines "enough" from what referees actually accepted, and measures every change to
the reviewer against it.

## What "better" means: the metrics

| Metric | Question | Data |
|---|---|---|
| **Recall** | Of the referees' concerns about a first version, how many did the review raise? | Stage 1 |
| **Tier A precision** | Of the *must address* items, how many match a referee's major concern or a change the authors made? | Stages 1, 2 |
| **A rate on accepted versions** | How many *must address* items does the reviewer raise on the version the journal accepted? That version was enough for its referees, so this should be near zero. | Stages 1, 2 |
| **Response judgment** | In revision mode, does the reviewer agree with the referees on which responses settled a concern? | Stage 1 |
| **Inference accuracy** | When the reports are hidden, how well do the concerns inferred from what changed match the real ones? | Stage 1 |
| **Provenance** | Is every quote in the paper, and does every item resting on a figure name the panel? | All |
| **Author verdicts** | Which items do authors mark *Will fix*, *Already in the paper* or *Disagree*? | Stage 3 |

Recall alone rewards long reviews. The A rate on accepted versions is the counterweight, and
it is the measured answer to "what is enough".

## Defining "enough"

- **A paper is ready when it would get through referees at its target journal**, not when no
  objection can be raised. The accepted version of a published paper is a real example of
  "enough" for that journal.
- **Tier A becomes absolute:** an item a referee at the target journal would likely require
  before acceptance. A review may have no tier A items. Calibrate the tiers so that recall on
  first versions holds and the A rate on accepted versions falls to about one per paper or
  less.
- **Each review ends in an overall verdict:** *ready*, *minor revision* or *major revision*,
  like a referee's recommendation. Check it against what actually happened to the paper.
- **Revision mode judges the response.** For a concern answered with new data, a reanalysis,
  a narrower claim or a rebuttal, the question is "would a referee accept this?". The
  resolution labels in stage 1 give examples of answers referees accepted.
- **Authors can answer back.** *Already in the paper* or *Disagree* triggers a re-check that
  either withdraws the item or quotes the passage that keeps it open. How often items are
  withdrawn is a precision signal.

## Tools

**Langfuse Cloud** for runs, experiments and labels, plus a **separate corpus database** as
the source of truth.

MLflow 3 is a real alternative. It has GenAI tracing, a prompt registry, LLM-judge
evaluation, and labeling sessions where experts rate traces. Either would work. Langfuse is
chosen because:
- its hosted cloud is ready for public data now, and annotation queues are on every plan,
  which is what physicists will label in;
- its core is MIT-licensed and self-hostable, which stage 3 needs;
- MLflow's expert-review tools are strongest on Databricks.

The decision is easy to revisit: both take OpenTelemetry traces, and the corpus does not
live in either.

How the pieces fit:

- **Corpus database: DuckDB, exported as Parquet.** It holds the research data: papers,
  versions, reports, concerns, responses, changes, reviews, items, matches and labels. Public
  snapshots go to a Hugging Face dataset or a release asset. Only the schema and the
  scripts live in this repository.
- **Langfuse holds the runs:**
  - one **dataset** per paper set (dev, test, accepted versions);
  - one **dataset item** per paper version, with its referee concerns as the expected output;
  - one **experiment run** per reviewer version;
  - **scores** for the metrics above;
  - **annotation queues** for physicists to rate items.
- **Prompts stay in `engine/`** as the source of truth. Each run records `engine/VERSION`
  and the git commit. Langfuse's prompt manager mirrors the prompts for display but is not
  where they are edited.
- **The harness:** `research/eval/api/` gains a Langfuse client. Reviewer and judge calls
  become traces tagged with paper id, version, set and engine version. Scores are written
  back to both stores.

### Corpus schema (first cut)

| Table | Key fields |
|---|---|
| `papers` | id, title, field, journal, published DOI, licence |
| `versions` | paper id, kind (arXiv v1, arXiv vN, accepted), arXiv id, date, text location |
| `reports` | paper id, round, referee, source (peer review file, SciPost) |
| `concerns` | report id, text, kind, major or minor, version it is about |
| `responses` | concern id, type (new data, reanalysis, narrowed claim, rebuttal, ignored), accepted by referee, text |
| `changes` | version pair, kind, summary, old and new page, referee-driven |
| `inferred_requests` | version pair, text, confidence, matched concern id (stage 1 only) |
| `reviews` | version id, engine version, model, mode, run ids |
| `items` | review id, lane, tier, topic, effort, text, quote found |
| `matches` | item id, concern id, raised (yes, partly), judge, judge model |
| `labels` | item id, labeller (physicist, author), label, note |

The revision record (`revision.json`, `docs/revisions.md`) maps onto `changes`,
`inferred_requests` and the item statuses, so `/referee-preview:compare` output loads
directly.

## Stage 1: papers with public referee reports

**Goal:** a gold set where the reports, the authors' responses and every version are all
known. Use it to measure the reviewer, test the inference and learn what "enough" looks like.

**Sources:**
- Nature Communications peer review files (reports and rebuttals, through Europe PMC; nearly
  every paper since 2024);
- Nature (since June 2025);
- SciPost Physics, whose reports are public, including some on rejected submissions;
- Communications Physics and npj Quantum Materials where they publish reports.

The 73 papers in `eval/referee/` are the start. Target: about 200 condensed matter papers.

**Steps:**
1. **Assemble triples:** arXiv v1, reports with responses, and the accepted version (the
   last arXiv version, or the open-access journal version). Load the corpus. Keep the
   existing dev/test split. New papers go to a test set dated after the model's training
   cutoff.
2. **Extract concerns and resolutions.** Reuse the experiment 11 extraction, adding a
   response type per concern and whether the referee accepted it in the next round. A
   physicist checks a 10% sample.
3. **Measure the current reviewer:** recall on v1 (the baseline exists), tier A precision,
   and the A rate on accepted versions. That last one is new and is the key number.
4. **Test the inference.** Run `/referee-preview:compare` with the reports hidden, then score
   the inferred requests against the real concerns. This tells us how far to trust stage 2.
5. **Prototype the fixes:** absolute tiers, the overall verdict and revision mode, in a new
   `engine/` version. Accept it only if recall holds and the A rate on accepted versions
   falls. Then run the held-out set once and record the result in `eval.md` (an `engine/VERSION`
   bump, per `AGENTS.md`).

**Done when:** baseline and new numbers for every stage 1 metric are in `EVALUATION.md`, and
inference precision and recall are known.

## Stage 2: the larger arXiv-to-published corpus

**Goal:** volume. Thousands of condensed matter papers whose versions show what changed in
review, with no reports, for base rates and calibration by kind of concern.

**Steps:**
1. **Match versions.** For cond-mat papers with a journal DOI (arXiv metadata, then Crossref
   and OpenAlex title search, as `scripts/followup.py` does), take arXiv v1 and the last
   version posted after acceptance. Keep pairs where that version is dated after acceptance.
   Target: 2,000 pairs over several journals, PRB/PRL/PRX included, since their changes
   reflect their referees.
2. **Infer and weight.** Run the change and inference steps of `engine/compare.md` (step 1
   only, cheaper) and weight each inferred concern by the stage 1 precision for its kind and
   confidence.
3. **Use it for:**
   - base rates, meaning which kinds of concern authors are made to fix, by journal and
     subfield;
   - tier calibration, meaning which kinds of item belong in tier A for a given journal;
   - the A rate on accepted versions at scale;
   - a larger held-out set for regression tests of each engine version.
4. **Mind the noise:**
   - changes made for editors, length or new data are not referee-driven, and stage 1
     measures that rate;
   - only published papers appear, so add rejected-then-resubmitted pairs where a v1 and a
     different journal's version can be matched.

**Licences:** many arXiv papers do not allow redistribution. Store derived data (changes,
concerns, short quotes, scores) publicly, and full text only in a working cache that is not
redistributed.

**Cost:** estimate on 50 pairs first. At current API prices, a step-1 comparison costs a
fraction of a full review. Batch it.

## Stage 3: sensitive data and learning from use

**Goal:** learn from the people using the plugin on unpublished work (drafts, private
reports, response letters, their decisions on each item) without that work ever becoming
public.

### Sources

- **Dashboard decisions.** *Will fix*, *Scope the claim*, *Already in the paper*, *Disagree*
  and the notes. `/referee-preview:contribute` already sends these at the level the author
  picks (labels only up to full text), redacted, to a private inbox.
- **Revision records** from `/referee-preview:compare` on private revisions, which stay in
  `~/.referee-preview/revisions/` today.
- **Private referee reports and responses** an author chooses to share. Those are the most
  valuable data: the only way to see the papers that were rejected.
- **Rebuttals from the re-check flow:** which items were withdrawn after the author answered.

### Privacy tiers

| Tier | What | Where | Who sees it |
|---|---|---|---|
| Public | Published papers, public reports, derived data | Langfuse Cloud, public corpus | Anyone |
| Shared | Contributions at levels 0 to 2: labels, generalized or item text, no quotes | Private corpus, private Langfuse project | Maintainers |
| Private | Drafts, unpublished reports, full text | The author's machine. A private store only with a signed agreement. | The author, or named maintainers under the agreement |

### What stage 3 needs before any sensitive data comes in

1. **Self-hosted Langfuse** (MIT core), in an account we control, with encryption at rest,
   single sign-on, audit logs and a retention limit. Or Langfuse Cloud's region and DPA, if
   that is acceptable to the people sharing. The public project and the sensitive project
   are kept apart.
2. **Consent per contribution**, as `contribute` does now: what is shared, who sees it, how
   to withdraw it. Plus a short data policy in `README.md`.
3. **Deletion on request**, by contribution id, from the corpus, traces and backups.
4. **Aggregates only out.** Results from sensitive data are published as counts and rates,
   never examples, and only above a minimum count so no paper can be identified.
5. **Evals on sensitive data run only in the private environment.** Prompt changes are still
   tested first on public data, so no private example is needed to justify a change.

### Learning from use

- **Precision proxy:** the share of tier A items authors mark *Disagree* or *Already in the
  paper*, by topic and engine version. Track it in Langfuse.
- **Calibration:** items authors fix versus items referees later raise, joined where an author
  shares both.
- **Regression set:** contributed items the reviewer got wrong (with the author's consent,
  generalized) become test cases that each engine version must not repeat.

## Order of work

1. Corpus schema in DuckDB, a loader for `eval/referee/` and the revision record, and a
   Langfuse project with the harness writing traces.
2. Stage 1 steps 1 to 3: the baseline, including the A rate on accepted versions.
3. Stage 1 step 4: inference accuracy. That decides whether stage 2 is worth its cost.
4. The absolute-tier, verdict and revision-mode engine version, measured on stage 1.
5. Stage 2 on 50 pairs, then scale.
6. Stage 3 infrastructure, before the first sensitive contribution is accepted.

## Open questions

- Which target journal does "enough" calibrate to when the author names none? Probably the
  journal the paper ended up in, for corpus papers, and a stated default for users.
- Are physicist labels needed on the A rate on accepted versions, to tell "referees missed it"
  from "too strict"? A sample of 30 items probably settles it.
- Does revision mode need the old version and the response letter, or can it work from the
  new version alone?
