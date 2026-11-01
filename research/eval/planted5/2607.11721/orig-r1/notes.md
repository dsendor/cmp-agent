# Run notes: arXiv 2607.11721v1

- Library: lookalikes.yaml meta.version 0.5 (updated 2026-10-24), 28 entries. Read once at the start with SKILL.md and report-template.md.
- Paper read: the extracted text only (paper.txt, main text p. 1-16 and SI p. 17-51), as the run prompt required. I did not fetch the abstract page or PDF. The title comes from the paper text, not the abstract page. Figure details come from captions only; I could not look at any figure. No ancillary data files; read_mtx.py not used. The data statement says data are available on request; no repository was reached.
- Recognition: I did not recognize the paper (dated 13 Jul 2026) and used no outside knowledge of its history.
- Scope: the paper is a high-field Josephson effect in moiré graphene, not a topological claim. I adapted entries from the supercurrent, quantization and practice families. No zbp, nonlocal, island, shapiro, charge, chiral, kitaev or diode checks apply.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Ballistic, phase-coherent transport (Fabry-Pérot in Ic and RN in Dirac band and minibands) | Fig. 1c-e, S5-S7, S12 | GH1 (main), GH2 (S12) | Ic at 2 K, RN at 10 K; n/ns about -2 to +2.7; bias-voltage FP check at 10 K |
| Uniform Fraunhofer near zero field | Fig. 1g, S9 | GH1 (n/ns ∼ 1.6), GH2 (n/ns ∼ 1.5) | period 2.2 ± 0.3 mT (GH1), 1.7 ± 0.3 mT (GH2) |
| Long-ballistic regime | Fig. S8 | GH1-GH4 | δE ∝ 1/L at n/ns ∼ 1.3; IcRN at n/ns ∼ 1.2 |
| Zero-resistance pockets up to ∼6 T in minibands, beyond 2rc = L | Fig. 2a, 2b, 2e, 3e | GH1; GH2 to 5 T (S13) | 100 mK; Fig. 2b at n/ns ∼ 1.8, several B; Fig. 2e at 4.1 T; field range of Fig. 2a not stated in text |
| Phase-coherent Ic oscillations at high field | Fig. 2c, S10, S11, S13c | GH1 at n/ns ∼ 1.8 (2.5, 3.5, 4.3, 4.5 T); GH2 at n/ns = 1.6, ∼3.5 T | periods 2.3 to 3.4 mT; S11 shows two consecutive sweeps per field; Ic up to 48 ± 2 nA |
| Not quantum Hall edge transport | Fig. S14 | GH1, GH2 | normal-state fan at 200 nA |
| Moiré needed (control) | Fig. S15 | one non-aligned graphene JJ, L ∼ 300 nm | same densities (< 5e12 cm-2) |
| Hofstadter band dispersion explains pockets | Fig. 3a-e, S18-S22 | GH1 (θ = 0.2°), GH2 (θ = 0.38°) | p/q from 1/3 to 1/20, 205 fields, cutoff 8 T; 1/R cutoff 20 mS; ⟨v²⟩/vF² > 0.1 level |

Counts: 4 moiré devices (GH1-GH4) plus 1 non-moiré; 2 of 4 moiré devices show high-field SC; GH3/GH4 set aside with a reason (length, low Ic). Missing: devices fabricated, junctions per chip, cooldowns, number of datasets, Fig. 2a field range, high-field data on the hole-side minibands. Main text says "reproduced across multiple additional devices" while the SI shows one (GH2).

## Entries matched, adapted, skipped

- Matched and adapted: fine-tuning-and-selection (always); series-resistance-subtraction (adapted from a quantized value to zero resistance and a 1/R cutoff in a two-probe measurement); field-enhanced-supercurrent-resonances (adapted from "supercurrent grows with field, read as triplet" to "large supercurrent at high field, read as Hofstadter-band transport"); protocol-parameter-sensitivity (adapted from an automated pass/fail protocol to the threshold-based map comparison of Fig. 3d-e).
- Skipped, can't apply: all zbp entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode): no tunneling spectroscopy or zero-bias peak. fine-tuned-plateau, one-end-only, trivial-andreev-band-gap-reopening, local-probe-loophole: no quantized peak or Majorana claim. chiral-plateau-superconductor-short: no QAH film or half-quantized plateau. island-states-coulomb-spacing, charge-trap-fractional-shift, coulomb-dominated-interferometer: no islands or fractional charge. Shapiro entries (shapiro-landau-zener, shapiro-nonlinear-resistance, transparent-junction-pi-crossing, switching-jump-blind-region): no microwave irradiation or 4pi claim. false-poor-mans-majorana: no dot chain. diode-vortex-screening: no nonreciprocity claim.
- Outside rows (not in library): chiral quantum Hall edge supercurrent (source Vignaud et al. 2023, tests taken from its described signature: supercurrent on a QH plateau with 2ϕ0 period at constant filling); edge-localized high-field Andreev states (sources Ben Shalom et al. 2016 and Indolese et al. 2018; tests from Indolese's use of the field dependence of the supercurrent to locate edge currents and from the paper's own Dynes-Fulton method).

## Status reasoning

- Chiral edge: ruled out by Fig. S14 alone, shown for both devices that carry the claim; the paper concludes against it (SI G, p. 33).
- Series resistance: the value is stated, its calibration is not; a stated value is a sentence, so I marked the calibration test "no". Fig. 2b nonlinear dV/dI and RN data bear on it.
- Field-moved resonances: finite-bias dV/dI maps exist at selected cuts (Fig. 2b, 2c, 2e, S11, S13), so "part"; the paper does not discuss resonances.
- Protocol sensitivity: reason given for Fig. 3d colorbar limits (Thouless energy) but not for the 20 mS cutoff, so "part".
- Fine-tuning: devices counted, datasets not, so "part"; GH2 shown, so second device "all".

## Hold-out

No library source was skipped: none of the matched entries' sources (library text) cites this paper by title, authors or arXiv ID. I did not fetch the library sources' full texts to confirm.

## Related work, how checked

All five opened on their arXiv abstract pages (fetched 2026-10-24) after an arXiv API title search (3 s between calls). Confirmed ID, title and first author, and each one-line description against the abstract text: 1504.03286 (Ben Shalom, abstract), 1805.10184 (Indolese, abstract), 1512.09083 (Amet, abstract), 2305.01766 (Vignaud, abstract), 2402.14451 (Barrier, abstract). None was read in full text.

## Library gaps

- No checks for the supercurrent family (high-field or field-enhanced supercurrent in graphene and similar junctions).
- No entry for chiral quantum Hall edge supercurrent as an explanation of high-field supercurrent.
- No entry for edge-localized Andreev states or edge supercurrent (Ben Shalom 2016; Indolese 2018), with a Jc(x) test.
- No entry for 1D channels (domain walls, defects) carrying high-field supercurrent (Barrier 2024).
- No entry for a normal-state quantity used as a proxy for superconductivity (here zero-bias 1/R correlated with band velocity, which normal-state conductance may also track).

## Unsure

- Whether field-enhanced-supercurrent-resonances and protocol-parameter-sensitivity match closely enough; both are adapted, and a stricter reading would skip them.
- Figure ranges (field axis of Fig. 2a, current range of Fig. 2b-c) are not in the text, so tests marked "part" for finite-bias maps rest on captions.
- Page numbers are the printed page numbers in the extracted text.

## Skill issues

- Step 3 says to walk "the checks for the paper's family", but the supercurrent family has no checks; the skill does not say what to do then.
- Scope rule says adapt entries for a different kind of measurement, but gives no guidance on how far a signature can be stretched (for example "grows with field, read as triplet" vs "survives at high field, read as band-structure transport").
- It is unclear whether a stated but uncalibrated value (series resistance) counts as "part" for a test that names both the calibration and the value.
- For outside rows, "take its tests from the control that paper describes" fails when the cited abstract describes no control (Ben Shalom); I combined Indolese's approach with the paper's own Dynes-Fulton method.
- The skill asks to write reports/<id>.md and notes; this run returned them in the reply per the run prompt. The skill also asks for the abstract-page title, which this run could not fetch.
- "Tested in part" vs "Not tested (argued)" for low-field evidence offered as general support (uniform Fraunhofer near zero field) when the claim is at high field is not covered.
