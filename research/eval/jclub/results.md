# Journal Club papers: results

*AI-generated, run 2026-11-22. Nothing here is human-checked. How the run was made:
`README.md`.*

Twelve condensed matter papers that experts recommended in the Journal Club for Condensed
Matter Physics over the last 12 months, each reviewed by reviewer v1.0 in exhaustive mode
(three runs, merged), structured with strengths, and checked for novelty.

## 1. The reviewer does not recognize an important paper

| Paper | Must address | Should address | Minor | Novelty (overall) | Novelty items (A/B/C) |
|---|---|---|---|---|---|
| 2505.12131 UTe2 strange metal at high field | 5 | 8 | 9 | incremental | 1/1/0 |
| 2505.22488 Raman optical activity, ferroaxial NiTiO3 | 3 | 10 | 12 | incremental | 0/1/1 |
| 2510.25767 Fermi liquid and BCS in overdoped cuprates | 5 | 14 | 8 | incremental | 0/2/0 |
| 2512.06265 Twist-angle superconductivity in tWSe2 | 4 | 12 | 11 | incremental | 1/1/0 |
| 2603.11162 Selective anyon braiding, bilayer graphene | 3 | 11 | 11 | incremental | 0/2/0 |
| 2603.11182 Controlled anyon localization, graphene | 6 | 11 | 8 | incremental | 0/1/1 |
| 2604.19870 Quantum fluctuations shift melting temperatures | 3 | 10 | 11 | incremental | 0/1/1 |
| 2604.23162 Fermi pockets in multilayer cuprates | 5 | 10 | 9 | incremental | 0/2/0 |
| 2605.13303 Reconfigurable chiral superconductivity | 4 | 13 | 9 | incremental | 0/2/3 |
| 2605.30316 Orbital magnetism, rhombohedral graphene | 3 | 13 | 12 | incremental | 2/1/0 |
| 2606.19426 3D foliated fractional quantum Hall phases | 3 | 8 | 10 | no precedent found | 0/1/0 |
| 2607.13127 3D non-foliated fractional quantum Hall phases | 6 | 11 | 10 | no precedent found | 0/0/2 |

Four novelty checks were rerun in sequence after arXiv rate-limited the first run (section 4).

**Every paper got 3 to 6 *must address* items: 50 in all, 4.2 per paper.** For comparison, an
ordinary preprint reviewed the same way (arXiv 2507.20647v1) got 5. Must-address items are 17%
of all items here (50 of 301). Papers the field singled out are graded like any draft.
This is the stage 1 finding of `../../data-plan.md` seen from the other side: tiers are relative
to the paper in front of the reviewer, not set against what referees or experts accept. A
must-address item on a recommended paper is either a real gap the experts let pass or a sign
that the bar is too strict. Telling which needs a physicist; the reviews are kept here for that.

**Strengths:** every review listed four. Whether they match why each paper was recommended is
not yet compared: the commentaries carry no licence, so the comparison needs a reader with the
commentaries in hand, not stored text.

## 2. The novelty lane finds a recurring pattern

Three papers have a *must address* novelty item, four in all, and in three of the four the
contradicting work is **cited by the paper itself**:
- 2505.12131 says T-linear resistivity "has not previously been associated with a spin-triplet
  superconductive state"; T-linear resistivity in UCoGe under pressure (arXiv:1608.01949, not
  cited) weighs against it.
- 2512.06265 says the twist angle's effect on superconductivity in tWSe2 "remains unknown"; its
  own ref. [28] (arXiv:2508.02662) studied it.
- 2605.30316 says studies have been "limited to the electronic transport response" (its own
  ref. [34], arXiv:2605.13303, imaged it) and claims a "first real-space imaging" that its ref.
  [20] (arXiv:2201.06901) did in another system.

The same pattern turned up when the lane was first tried, on arXiv 2507.20647v1 (a "has been
lacking" statement contradicted by the paper's own ref. [46]). A broad priority word in the introduction,
contradicted by a paper in the reference list, looks like the most common and cheapest-to-fix
novelty problem. Checked: the quoted sentences are in the papers on the pages given, and the
cited arXiv papers exist with the titles given; whether each contradicts the claim is the AI's
judgment.

Ten papers came out "incremental" and two (the 3D fractional quantum Hall theory pair) "no
precedent found" for their headline claim.

## 3. Problems in the run

- **Companion papers.** Two pairs of recommended papers are companions, posted days apart
  (2603.11162/2603.11182; 2605.13303/2605.30316). In the first, rate-limited run one check asked a
  paper to cite its same-day companion while the other listed it as context. With full searches
  both list a same-day companion as context only, so the inconsistency came mostly from weak
  coverage. A companion posted two weeks earlier (2605.13303 for 2605.30316) is prior work and
  rightly counts. The prompt could still say so explicitly.
- **Missing supplements.** Several arXiv PDFs lack the supplementary material they cite
  (2505.12131, 2510.25767, 2604.23162). Some items ask for what may be there.

## 4. Search coverage

Eight novelty checks ran at once, and arXiv rate-limited them (HTTP 429): the script waits
3 seconds between its own calls, but parallel agents do not share the wait. Four checks
(2510.25767, 2603.11162, 2603.11182, 2604.19870) fell back on the paper's references and web
search, so they were rerun one at a time with 8 to 11 arXiv queries each and no failures. The
verdicts held (all incremental), but the evidence changed: two checks gained a should-address
item (an uncited earlier paper each), and one replaced its companion-paper item with an
inaccurately described earlier experiment. A rate-limited novelty check under-reports, so it
should be rerun, not trusted. For the plugin: a review runs one novelty check, so this only bites
batch runs; a batch runner should run novelty checks in sequence.

Across all twelve papers the novelty lane wrote 27 items: 4 must address, 15 should address and
8 minor.

## Next

1. A physicist rates the must-address items on two or three of these papers in their field:
   real gap, or too strict? About 30 items settles it (`../../data-plan.md`, "Physicists").
2. Say in `engine/novelty.md` that a same-day companion paper is context, not prior work.
3. Load these into the corpus (`journal_club` and, with a reviews loader, `reviews`).
