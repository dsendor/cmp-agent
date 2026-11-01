# Run notes: 2607.11721v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes, checks for families zbp, shapiro, kitaev, charge, practice).
- Skill read: skill/SKILL.md and skill/report-template.md, once, at the start. I did not use scripts/read_mtx.py because no figure data came with the paper.
- Paper read: the extracted text only (main text pp. 1 to 16, SI pp. 17 to 51), per the test prompt. I did not fetch the arXiv abstract page, PDF or HTML for 2607.11721. The title comes from the paper text: "High-field Josephson effect enabled by a moiré Hofstadter spectrum". Figure details come from the captions only. Panels drawn as images in the PDF (Fig. S17 to S22 plots) could not be seen.
- Data repository: none linked ("available from the corresponding author upon reasonable request", p. 16), so nothing was counted beyond the text.
- Recognition: I did not recognize the paper. It is dated 13 Jul 2026, after my training data, and I used no outside knowledge of what happened to it later.
- Word count: about 925 words outside the table, slightly over the 600 to 900 target.

## Claims table (step 1)

| Claim | Figures | Device(s) | Counts and ranges |
|---|---|---|---|
| Ballistic, phase-coherent Josephson transport across the main Dirac band and the moiré minibands (Fabry-Pérot oscillations in Ic and RN) | Fig. 1c to 1e; SI Fig. S5 to S7; GH2 Fig. S12; non-aligned control Fig. S15a,b | GH1 (main), GH2 (SI) | Ic at 2 K, RN at 10 K; FP for n/ns from about -2 to 0 (GH1); normal-state FP vs Vb at 10 K (Fig. S7) |
| Uniform current distribution at low field (Fraunhofer) | Fig. 1g; Fig. S9 | GH1 at n/ns ∼ 1.6, GH2 at n/ns ∼ 1.5 | Low field only, period 2.2 ± 0.3 mT (GH1), 1.7 ± 0.3 mT (GH2) |
| Long-ballistic regime | Fig. S8 | GH1 to GH4 | δE ∝ 1/L across 4 lengths (0.2 to 0.6 µm); IcRN ∝ 1/L at n/ns ∼ 1.2 |
| Main claim: superconducting pockets with oscillating Ic up to ∼6 T in the minibands, beyond 2rc = L | Fig. 2a to 2c, 2e; Fig. S10, S11 | GH1 | 100 mK; field perpendicular only; Ic up to 48 ± 2 nA at 2.5 T; Ic(B) periods 2.3 to 3.4 mT near 4.3 T; Fig. S11 at about 2.5, 3.5 and 4.5 T at n/ns ∼ 1.8 |
| Same trend in a second device | Fig. S13 | GH2 | Up to 5 T; cut at n/ns ∼ 1.8 and re-emergence at ∼2.0; periods 1.7 to 2.0 mT |
| Pockets are not quantum Hall edge supercurrent | Fig. S14 (normal state at 200 nA dc) | GH1, GH2 | 200 nA bias |
| Non-moiré control stays below 2rc = L | Fig. S15d | One non-aligned junction, L ∼ 300 nm | Densities < 5 × 10^12 cm^-2 |
| Mechanism: pockets coincide with high ⟨v²⟩ in Hofstadter bands | Fig. 3; Fig. S18 to S21 | GH1 (main), GH2 (S18) | Calculations at 205 flux values from p/q = 1/3 (8.54 T) to 1/20 (1.28 T); 1/R cutoff 20 mS (Fig. S18) |

Counts and gaps: 4 moiré devices presented (GH1 to GH4, all W = 1.5 µm) plus 1 non-aligned device. The number fabricated is not given. Cooldowns are not given. High-field data appear for GH1 and GH2 only; GH3 and GH4 appear only at zero field (Fig. S2, S4, S8). Gate range: ±80 V possible, ±70 V in Fig. S2, n/ns up to about ±2.0 to 2.7 depending on twist. Temperatures: 100 mK base, 2 K (FP Ic), 10 K (RN). Field sweep rate about 0.2 mT/s, with three back-and-forth sweeps before each interference pattern. Measurement: ac 1 nA at 17.777 Hz, dc current step 2 nA, two-probe with 3447 Ω subtracted. Field angle: perpendicular only.

## Entries matched, adapted and skipped

- Matched: fine-tuning-and-selection (always applies).
- Adapted:
  - field-enhanced-supercurrent-resonances. Its signature is a supercurrent that grows with field, read as exotic pairing. Here the supercurrent reappears and persists at high field and is read as Hofstadter-band transport. The finite-bias resonance mechanism carries over.
  - series-resistance-subtraction. Its signature names 2e²/h. Here the "vanishing resistance" and the 1/R maps in a two-probe measurement depend on the 3447 Ω subtraction.
- Skipped, because they need a tunneling zero-bias peak, Majorana, island, Shapiro, charge, chiral QAH, Kitaev, diode or protocol context that this device does not have: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, protocol-parameter-sensitivity, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer, diode-vortex-screening.
- Checks: only the practice checks were walked (report-counts, report-ranges, report-processing), because the library has no checks for the supercurrent family.

## Sources held out

None. No library source I relied on discusses 2607.11721. The adapted entries' sources (Frolov 2309.09368, Zhang 2101.11456) predate the paper. I did not reopen them for this report.

## Related work: how each was checked

All five abstract pages were opened at arxiv.org/abs/<id> to confirm the title and first author, and abstracts were read through the export.arxiv.org API.
- 1504.03286 Ben Shalom et al.: abstract plus full text (main text p. 4 to 5, SI Sec. 5, 8, 9).
- 1512.09083 Amet et al.: abstract plus full text (p. 2 to 4).
- 1805.10184 Indolese et al.: abstract plus full text (p. 4 to 5).
- 2402.14451 Barrier et al.: abstract only.
- 1804.09476 Krishna Kumar et al.: abstract only.

## Outside rows (library gaps)

1. Edge supercurrent from near-edge Andreev states. Sources: Indolese et al. 1805.10184 (edge supercurrent in a MoRe/graphene-hBN superlattice junction, found by Josephson interferometry across the gate range) and Ben Shalom et al. 1504.03286 (high-field pockets attributed to near-edge Andreev states). Test taken from those controls: current distribution from Ic(B) across densities. flags.json carries only the Indolese URL because the schema allows one source.
2. Flux creep or vortex jumps in the leads producing changes in Ic(B). Source: Ben Shalom SI Sec. 5. Control there: reproducibility on up and down sweeps over hours.
3. Chiral Andreev edge-state supercurrent in the quantum Hall regime. Source: Amet et al. 1512.09083. Controls there: plateaus at a suppressing dc bias, Ic of order 0.5 nA, regular period close to the low-field Fraunhofer period.
- Library gap: there is no family of checks for supercurrent claims (high-field or field-enhanced supercurrent, Josephson interferometry).
- Library gap: the series-resistance-subtraction signature names only 2e²/h, but the same mechanism applies to "zero resistance" in two-probe Josephson data.

## Unsure

- Whether a stated series-resistance value counts as "shown". I treated it as a sentence only, so the test is "no" and the status is Not tested (data bear on it).
- The chiral edge-state row is "Ruled out" because every test is shown for both devices. However, GH2's high-field periods (1.7 to 2.0 mT) sit near its zero-field period, which is Amet's signature. I raised this in question 7 and left the status as the rule gives it.
- The edge row: the low-field Dynes-Fulton result (Fig. 1g, S9) covers part of the evidence. At high field a Fourier inversion is not standard, so "part" may be generous.
- Not used in the report:
  - The text sets the crossover at "vH ∼ 0.42vF" (p. 6). With Δ ∼ 1.4 meV and L = 0.2 µm, ħvH/L = Δ gives vH ≈ 0.53 vF; 0.42 vF corresponds to about 1.1 meV.
  - The threshold is quoted as ⟨v²⟩/vF² ∼ 0.17, while Fig. 3c-d discussion uses 0.1.
  - One sentence on p. 6 is garbled ("to ETh ∼ 1.6 meV at the moiré minibands is ETh ∼ 2.6 meV").
  - The density unit is printed as "10−12 cm-2" (SI p. 20).
- The field-enhanced entry is a loose fit. The paper's Ic is not shown to grow with field monotonically, only to reappear in pockets.

## Skill issues

- Step 7 says to use the title on the arXiv abstract page. This test forbade fetching it, so I took the title from the text.
- The skill does not say what to do when the paper's family (supercurrent) has no `checks`. I walked only the practice checks and said so in the report.
- The Scope rule allows adapting entries for a different kind of measurement. It does not say whether outside rows count toward that one-sentence scope note or need their own mention.
- The flags schema allows one source URL per outside row, while a row may rest on two papers.
- The status rules depend only on whether tests are shown, not on what they show. So "Ruled out" can hold when part of the evidence (GH2's periods) points the other way. The skill could say how to handle a test that is shown but does not separate the lookalike for part of the evidence.
- Step 6 says to skip a standard question "unless the paper already answers them (then say where)". For the second-best device the paper answers in part (GH2). I kept the question and pointed to Fig. S13; the rule for partial answers is unclear.
- The step 7 word target (600 to 900 outside the table) is hard to meet with six rows, three checks, eight questions and five references.
