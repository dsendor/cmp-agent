# Run notes: arXiv 2610.17701v1

## Library and inputs
- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 entries plus the checks section. Read once at the start, with skill/SKILL.md and skill/report-template.md.
- Paper: extracted text only (the scratchpad paper.txt given in the prompt). No PDF, no abstract page, no supplementary material (Figs. S2 to S11 are cited but not available). No page numbers, so quotes cite sections and figure captions. Figure details come from the captions only.
- The title is taken from the text. An arXiv API search for related work happened to return 2610.17701v1 itself. Its title matches the text, and I used nothing else from that hit.
- Data: "Source data will be provided with this paper"; no repository is linked. read_mtx.py was not used (no .mtx files).
- I didn't recognize this paper and used no knowledge of its later history.

## Claims table (step 1)
| Claim | Figures | Source | Counts and ranges |
|---|---|---|---|
| Interfacial superconductivity only on 1QL-Bi2Te3, with gaps modulated at the moiré period | Fig. 1D-I, S3, S4 | 1QL-Bi2Te3/FeTe (20 UC FeTe), MBE | Gap peaks at ±1.85 and ±2.92 meV, dip near ±4.4 meV; Fig. 1 taken at 1.6 K; one line profile shown |
| Star-shaped vortex with QPI-like modulation (pair-breaking QPI) | Fig. 2A-H, S8 | One vortex, 1.0 T, 0.4 K, "defect-free region" | Energies 0, ±3 meV; 50 nm field of view |
| Dispersive Bi2Te3-derived branch (X-shape) | Fig. 3B, 3F, S8A, S10 | Fig. 3A vortex | 10 to 20 nm from center; kF ~0.3 nm^-1, EF ~300 meV; spacing ~0.03 meV against ~0.37 meV resolution |
| ZBCP plus integer CdGM ladder (the MZM claim) | Fig. 2I, 3B-E, 3G-I | One vortex in an island (Fig. 3A); Fig. 2I may be the same vortex or another one, which is unclear | FWHM ~0.5 meV, height ~2x the above-gap conductance; levels -2.1, -0.93, 0.003, 0.79, 1.96 meV; text says spacing "about 0.7 meV"; setpoints 500 pA (Fig. 2I) and 1 nA (Fig. 3); spectra along two directions |
| FeTe layer is the topological origin | Fig. S6, S7 (ARPES) | Separate as-grown and Te-annealed FeTe samples | Not measured on the heterostructure |
| One, two and three Majorana vortices controlled by field and island size | Fig. 4B-D (zero-energy maps), 4E schematic | Islands at "different perpendicular magnetic field" | Field values not given; no spectra; island-size dependence not shown in any figure |
| Missing counts | | | Samples, islands, tips, cooldowns, vortices measured, vortices with ZBCP: none stated |

## Scope adaptation
- This is STM/STS of vortex cores, outside the library's transport scope; I said so under "What this is".
- Checks adapted: zbp-dot-search (trivial core bound states: CdGM ladder and off-center splitting), zbp-transparency (tip-sample distance or setpoint), zbp-nonlocal-gap (evidence of bulk topology where the peak appears), zbp-raw-conductance (no series resistance in STM; I judged setpoint, modulation, resolution and raw spectra), zbp-both-ends (the other end of the vortex line).
- Entries adapted: kondo-resonance (magnetic impurity such as interstitial Fe under the core; the even-odd occupancy test has no analog here and is marked "no"), local-probe-loophole (applied as written; STM is a local probe).

## Entries skipped and why
- abs-quantum-dot: no tunnel barrier or nanowire segment. The vortex-core analog (trivial Andreev or CdGM states) is covered by the outside row, which has a better-fitting control.
- quasi-majorana-smooth-confinement, one-end-only, spin-orbit-length-pinning, disorder-induced-zbp, crowded-trivial-subgap-states, weak-antilocalization, exceptional-point-zero-mode: these are nanowire end-state or nanowire disorder mechanisms. Unresolved dense vortex states (the closest analog of crowded states) are covered by the outside row.
- fine-tuned-plateau, series-resistance-subtraction: no quantized conductance claimed.
- micromagnet-stray-field (field is applied, no magnets), full-shell-flux-andreev (no full-shell wire), trivial-andreev-band-gap-reopening and protocol-parameter-sensitivity (no gap protocol), and the chiral, island, shapiro, supercurrent, charge, kitaev, diode and interferometer entries: different signatures.

## Status judgments
- Evidence presented: spectra for one vortex (Figs. 2I and 3; possibly two vortices) and zero-energy maps of the vortices in Figs. 4B-D, offered as the "number controllable" evidence. Those Fig. 4 vortices are part of the presented evidence for "Majorana vortices", so tests shown only for the Fig. 3 vortex are marked "part". Missing counts and other islands are counted only under fine-tuning-and-selection and the questions.
- Outside CdGM row, ladder test "part": shown for one vortex. The fitted ratio (about 2.4) sits between integer and half-odd-integer, and the text's "about 0.7 meV" spacing doesn't match the fits.
- Outside CdGM row, spatial test "part": shown along two directions for the Fig. 3 vortex only.
- kondo-resonance: "argued, not tested". The defect-free-region choice is the argument. The 0 T spectrum in Fig. 2I was taken at a different spot ("at clean surface"), so it doesn't test this.
- zbp-raw-conductance "done": unsure. Fig. 2I is described as "Typical dI/dV spectra" with setpoints. I couldn't see whether it is normalized.

## Sources held out
- None. No library source cites 2610.17701 or this author group's paper. A grep of the library for the ID and "Bi2Te3/FeTe" found nothing.

## Related work checks
Each was opened on its arxiv.org/abs page (citation_title and first author confirmed), and each one-line description was checked against the abstract (abstract only, not full text):
- 1709.09401, Chen, Mingyang: abstract confirms half-odd-integer levels, and "rather a symmetric peak appears at zero-bias at the vortex center".
- 1901.02293, Kong, Lingyuan: abstract confirms two vortex classes, the half-integer shift tied to the ZBP, and the integer versus half-odd-integer ratios.
- 1312.7110, Xu, Jin-Peng: abstract confirms the ZBP "splits right off the vortex center in conventional superconductors", and that the mode is destroyed as vortex distance shrinks.
- 1812.08995, Machida, T.: abstract confirms some vortices host the ZVBS, with a fraction that decreases with field.
- 1904.06124, Zhu, Shiyu: abstract confirms the plateau with tunnel coupling for the zero mode and none for CdGM states or the continuum.
- arXiv API calls were spaced 3 s apart; no rate limit was hit.

## Library gaps
- STM vortex lookalikes are missing: ordinary CdGM states in the quantum limit (half-odd-integer ladder; unresolved, they give a zero-bias peak at the center), sources 1709.09401 and 1901.02293. A vortex-pinned magnetic impurity (Kondo or YSR) state is also missing; I adapted kondo-resonance for it.
- There are no vortex checks: integer versus half-odd-integer ladder fit with resolution, tunnel-coupling (tip height) series, fraction of vortices with a ZBP against field (1812.08995), and vortex-vortex distance splitting (1312.7110).

## Skill issues
- The report template asks for page numbers. Text-only input has none; I used sections and figure captions.
- The skill doesn't say how to treat evidence that is shown but has a different kind of data. Here Fig. 4 vortices appear in maps without spectra. I counted it as "part" of the presented evidence; another reader might count it under selection only.
- For adapted entries, it is unclear whether test text may be reworded. I kept the library wording and explained adaptations in cells and notes.
- The skill lists exactly four questions that must always be asked. Here the "devices" question is about vortices and islands; I reworded it to fit.
- The flags schema has one `source` per outside row; my row rests on two papers (1709.09401 for the lookalike, 1901.02293 for the ratio test). I listed the first.
