# Step 4 plan: two tools, depth on demand, triage, CMP topics and checklists

*AI only, written 2026-10-28 for David, updated with the follow-up test results the same day. It
answers his questions on the Step 3 report (`step3-report.md`) and sets up Step 4. Test results
are in `step3-report.md`, "Follow-up tests"; rows P14 to P17 in `../eval.md`.*

## 1. Two versions, one engine

The reviewing step is the same for both readers; what changes is the framing, what is shown and
how much. Both start from prompt D (Liang et al. with the MARG protocol, the CMP checklist and
triage tiers), the best short review in the follow-up tests (49% recall against 45%).

| | Reviewer mode | Writer mode |
|---|---|---|
| Reader | a referee with the manuscript in hand | an author before submission or resubmission |
| Question it answers | does the evidence support the conclusions, and what must the authors do | what will referees object to, and how do I fix it first |
| Output | short summary, concerns in tiers A to C, questions for the authors | anticipated objections in tiers A to C, each with a concrete fix: the experiment, control, analysis or rewrite |
| Extra content | nothing about style unless it hides the science | clarity, overclaiming, missing citations and framing for the journal (categories the eval does not score yet) |
| Default depth | Standard | Thorough |
| What the eval scores | top-k recall and precision: the first items must be the right ones | recall over the whole list, then actionability |

**Depth, chosen by the user:**

| Depth | Shows | Built from | Cost per paper (Opus batch) |
|---|---|---|---|
| Brief | tier A only, at most 5 items | one run | about $0.40 |
| Standard | tiers A and B, about 15 items | one run | about $0.40 |
| Thorough | all tiers | one run | about $0.40 |
| Exhaustive | all tiers, more concerns per run, merged from three runs | three long runs plus a merge call (tests A and C) | about $2 |

Brief, Standard and Thorough are the same review cut at a different tier, so changing depth
costs nothing and never re-runs the model. Tier A holds about a third of a review's points and
two thirds of the referees' major concerns it caught, so Brief keeps most of what matters.
Exhaustive is the only mode that pays for more. The follow-up tests found two cheap levers, each
reaching MARG territory on its own: asking one call for 70 concerns (61%, $0.74, but twice the
unmatched major points) and merging three runs (+11 points with precision unchanged). Exhaustive
combines them; that combination is the next test.

Writer mode needs an eval of its own before it ships. The current metric drops presentation and
novelty concerns, which are much of what an author wants to hear. The referee concerns already
extracted carry those categories, so scoring them is a change to `score.py`, with no new data.

## 2. Triage and ranking

Yes, and it works for grouping. Tests B and D put triage into the prompt: every concern goes
under A (the conclusion does not follow without it), B (a claim is weaker without it) or C
(minor), numbered in priority order; test A's merge call does the same across three reviews.
Tier A ends up with 35 to 37% of the points and 64 to 70% of the referees' major concerns that
the review caught. What did not improve is the order inside the list: top-11 recall stayed at 28
to 31% for every variant.

Ranking has been the weak point of every reviewer: plain, Liang et al., MARG and every follow-up
variant sit at 24 to 31% top-11 recall whatever their total recall. Prompt-level triage did not
move it, so the next thing to try is a separate triage call that sees the paper and the full
list and has only one job.

## 3. CMP topics the referees raise

Read from the 352 referee concerns on the 20 dev papers outside `marg10` (so tests B and D are
scored on papers the topic list never saw; the test set stays untouched). Eleven themes recur
across techniques:

1. **How many samples or devices.** Single device, single film thickness, device-to-device
   spread, survival after thermal cycling (twisted graphene, CrSBr, NbSe2 resonators, gate-tuned
   films).
2. **The null control.** A geometry or sample where the effect should vanish: a 0 degree SQUID,
   a reference resonator, a bare device without the WSe2 layer, a nonmagnetic tip, a metal with
   the opposite spin Hall sign.
3. **Apparatus artifacts.** Contacts and filters shifting a resonance, illumination of contacts
   by a large THz beam, the NV laser itself, tip changes, trapped flux, switching-current
   fluctuations, frequency-dependent extrinsic RF signals.
4. **Heating.** Electron against lattice temperature, phonon contributions to transport or
   thermal conductivity, Joule and optical heating, whether the sample temperature is known.
5. **Calibration and conversions.** Gate voltage to density and filling (nonlinear conversion,
   where filling zero sits), twist and alignment angles and their uncertainty, beam fluence and
   spot size, oxygen stoichiometry.
6. **Missing dependences.** A result at one temperature, two temperatures where a transition is
   claimed, no field, power or frequency dependence, comparisons at mismatched temperatures.
7. **Fits and extraction.** Free and fixed parameters, extrapolation to zero temperature, FFT
   resolution, how error bars were made, data-to-parameter ratios, normalization across field
   directions.
8. **Inhomogeneity.** Strain, disorder, domains, twist-angle variation, surface and interface
   states, terminations and reconstructions.
9. **Direct evidence for the headline property.** Zero resistance and Meissner response for
   superconductivity, spin resolution for spin splitting, a protection test for a topological
   edge state, and whether the signature is unique to the proposed state.
10. **Theory set-up.** Model symmetry against the real structure, fitted against independent
    parameters, functional and spin-orbit choices, relaxation and convergence, qualitative
    comparisons presented as agreement.
11. **Consistency.** Between figures, between text and figures, with the authors' earlier data
    and with literature values.

Test D adds these as a sixth step in the prompt (`api/arms/liangplus_cmp.md`).

## 4. More specific checklists

Worth adding, with one lesson from our own history: v0.5, which reviewed through the library of
lookalike checks, trailed the plain prompt by 19 to 27 points (P4, P5). It lost because the
catalog replaced the general review. Test D keeps the general review and adds the checklist as
a last pass, which is the safer design.

If D helps, the next layer is per-technique checklists, chosen by the techniques the paper
uses, each a short list drawn from dev-set referee concerns:

| Technique | Example items |
|---|---|
| Transport | four-terminal geometry, contact resistance, heating at the measurement current, gate-to-density conversion |
| STM and STS | setpoint effect, tip changes and convolution, matrix elements, surface termination |
| ARPES | surface against bulk bands, termination, photon-energy (kz) dependence, spin resolution |
| Optics, THz, NV | fluence and spot size at the sample, heating, illumination of contacts or substrate |
| Microwave resonators | reference-resonator spread, filters and bias lines, independent DC cross-checks |
| Thermal transport | phonon contribution, Wiedemann-Franz check, extrapolation to zero temperature |
| Magnetism and imaging | domains, strain maps, minor loops, probe-induced fields |
| DFT and models | functional and U, relaxation, convergence, symmetry of the model structure |
| Moiré devices | twist angle and its spread, alignment to hBN, displacement-field calibration, device comparison |

The library of lookalike checks stays what it is now, a set of specific trivial explanations for
specific claims (Majorana, Shapiro steps, quantization), applied when a paper makes one of those
claims.

The rule for building any of these: draw items from dev papers only, test on papers the list
never saw, and keep the 22 test papers for the final comparison.

## 5. Allen AI open-source tools

**Used:** the MARG-S prompts and agent protocol, and the Liang et al. prompt, both from Ai2's
`allenai/marg-reviewer` repository (`api/arms/marg_s.json`, `api/arms/liang.md`). MARG-S-NR, the
no-refinement variant we ran, is one of the configurations in that repository's paper
experiments.

**Assessed and set aside on 2026-10-23** (`../prior-work.md`): Ai2 ScholarQA
(`allenai/ai2-scholarqa-lib`), a literature-review pipeline over Semantic Scholar, judged too
heavy for a one-page report, and blocked from this sandbox.

**Worth a second look, for writer mode:**

- **Ai2 Paper Finder** (an open snapshot is on GitHub) and **ScholarQA**, for the novelty and
  missing-citation checks authors ask for. Referees raise these often (44 of the 352 concerns
  on the 20 dev papers are novelty or prior work, and 78 more are presentation), though the
  current recall metric leaves both out.
- **OpenScholar** (Ai2 and the University of Washington), retrieval-grounded answers over the
  literature, the same use.
- **ARIES** (Ai2), review comments paired with the edits authors made in response. It is
  computer-science papers, so not an eval set for us, but its comment-to-edit idea is how writer
  mode's actionability could be scored.
- **GROBID and s2orc-doc2json**, the PDF parsers in the MARG repository. We do not need them while
  the reviewers read the PDF directly.

All of the literature tools depend on Semantic Scholar. Its API still gave no response from this
sandbox on 2026-10-28, and github.com pages answer 403 here, so none of these can be tried from
this environment without a network change. These descriptions come from Ai2's own pages and
announcements, not from running the tools.

## 6. Order of work

1. Done: tests A to D ($50.90, P14 to P17). Base prompt D.
2. Next tests: D asked for more concerns, three runs merged (exhaustive depth); a separate
   triage call for ranking; D on the other 20 dev papers to confirm its 4-point gain.
3. Score presentation and novelty concerns for writer mode (`score.py` change, no API cost).
4. Per-technique checklists, built on dev and tested on unseen papers.
5. Then the planned Step 4 to 6 work in `../eval.md`, ending with one run on the 22 test papers.
