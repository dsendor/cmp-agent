# Run notes: arXiv 2607.11721v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes). Read once with skill/SKILL.md and skill/report-template.md at the start.
- Date: 2026-10-24. Label: AI only.

## What I read

- Extracted text of the paper (main text pp. 1 to 16 and SI pp. 17 to about 45), from the file the task named. Per the task I did not fetch the abstract page, PDF or HTML. Title taken from the first line of the text; I couldn't confirm it against the arXiv abstract page. Figures not seen; figure details come from captions and text.
- No ancillary figure data; read_mtx.py not used. Data availability: "available from the corresponding author upon reasonable request" (p. 16), so no repository to count from.
- I did not recognize this paper (dated 13 Jul 2026).

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Ballistic, phase-coherent transport: Fabry-Pérot oscillations in RN and Ic in the Dirac band and in the hole minibands; Fraunhofer pattern | Fig. 1c to g; Fig. S5 to S9, S12 | GH1 (also GH2) | RN at 10 K, Ic at 2 K; Fraunhofer at n/ns ∼ 1.6, 100 mK; period 2.2 ± 0.3 mT |
| Long-ballistic regime: Ic(T) exponential, δE ∝ 1/L, IcRN ∝ 1/L | Fig. S8 | GH1 to GH4 | δE at n/ns ∼ 1.3; IcRN at n/ns ∼ 1.2 |
| High-field supercurrent pockets in minibands up to ∼6 T, beyond 2rc = L | Fig. 2a, b, e; Fig. 3e | GH1 | 100 mK; Ic up to 48 ± 2 nA at 2.5 T, n/ns ∼ 1.8; Fig. 2e at 4.1 T |
| Phase coherence at high field: irregular Ic(B) oscillations | Fig. 2c (4.3 T), Fig. S10, S11 (2.5, 3.5, 4.5 T, two consecutive sweeps each) | GH1; GH2 Fig. S13c (3.5 T) | GH1 at n/ns ∼ 1.8; GH2 at 1.6; periods 2.3 to 3.4 mT (GH1), 1.7 to 2.0 mT (GH2) |
| Not quantum Hall edge transport: no Landau levels in normal state at 200 nA bias where pockets are | Fig. S14 | GH1, GH2 | 200 nA bias |
| Moiré needed: non-aligned junction shows no SC beyond 2rc = L | Fig. S15 | one non-moiré junction (L ∼ 300 nm) | densities < 5 × 10^12 cm^-2 |
| Pockets coincide with high calculated ⟨v²⟩/vF² from Hofstadter bands | Fig. 3c to e; Fig. S18 to S21 | GH1, GH2 | θ = 0.2° and 0.38° in model; fluxes 1/3 to 1/20; 1/R cutoff 20 mS (Fig. S18) |

Device counts: four moiré junctions fabricated and measured (GH1 to GH4, Table S1), two show high-field SC (GH1, GH2), two do not (GH3, GH4, attributed to length); one non-moiré control. Missing: cooldowns, number of datasets or density cuts, how GH1 and the interference cuts were chosen. Main text says "multiple additional devices"; SI shows one additional device with the high-field effect. Gate up to ± 80 V (gate leaks beyond), magnet up to 8 T, 100 mK to 10 K.

## Entries matched, adapted, skipped

- Matched: fine-tuning-and-selection (always).
- Adapted: field-enhanced-supercurrent-resonances (signature is field-growing supercurrent read as triplet; here high-field supercurrent read as Hofstadter-band transport; the mechanism, finite-bias resonances shaping the extracted switching current, carries over). series-resistance-subtraction (signature is conductance near 2e^2/h; here a 3447 Ω subtraction underlies "vanishing resistance" and the 1/R map).
- Skipped as not applicable (no zero-bias peak, quantization, nonlocal, island, Shapiro, charge, chiral QAH, Kitaev or diode claim): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer, diode-vortex-screening.
- Considered and not used: protocol-parameter-sensitivity. The Fig. 3 comparison uses display thresholds (colorbar limits, 20 mS cutoff, ⟨v²⟩/vF² > 0.1 versus the 0.17 conjecture), but it is not a pass/fail protocol; I folded the threshold point into the series-resistance question.
- Checks: the library has check lists for zbp, shapiro, kitaev, charge and practice only. I applied the three practice checks.

## Sources held out

None. No library source cites this paper.

## Outside rows (library gaps)

- Chiral Andreev edge-state supercurrent (quantum Hall Josephson effect). Source opened: Vignaud et al. 2023, arXiv 2305.01766 (abstract); also Amet et al., arXiv 1512.09083 (abstract). Tests taken from Vignaud's control: supercurrent on a quantum Hall plateau, regular 2φ0 periodicity. Paper shows Fig. S14 (both devices) and irregular periods (Fig. 2c, S11, S13c) and concludes against it. Ruled out for the claim; the normal-state fan alone separates it.
- Supercurrent carried by Andreev states near the graphene edges. Sources opened: Ben Shalom et al., arXiv 1504.03286 (abstract: "We attribute the high-field Josephson effect to mesoscopic Andreev states that persist near graphene edges."); Indolese et al., arXiv 1805.10184 (abstract: edge supercurrent at van Hove singularities in a graphene/hBN superlattice, found from the field dependence of the supercurrent). Tests from those controls: current-density profile at high field, comparison with an edge pattern. Paper shows Dynes-Fulton only near zero field (Fig. S9). Not tested (data bear on it).
- Library gap: no `supercurrent` check list; no entries for quantum Hall edge supercurrent or edge-guided Andreev states in graphene junctions; series-resistance-subtraction is written only for 2e^2/h.

## Related work checks

All five opened on arxiv.org/abs on 2026-10-24; ID, title and first author confirmed against the page; descriptions checked against the abstract only:
- 1504.03286 Ben Shalom (abstract)
- 1805.10184 Indolese (abstract)
- 1512.09083 Amet (abstract)
- 2305.01766 Vignaud (abstract)
- 2402.14451 Barrier (abstract)
arXiv API searched by title words with 3 s waits; no rate limit hit.

## Numerical consistency checks I ran (from the paper's own formulas)

- e∆/h with ∆ = 1.4 meV is 54 nA: matches SI p. 31 (53 ± 1 nA), not p. 5 (106 ± 2 nA). Flagged (question 7).
- ns from the SI moiré formula: θ = 0.21° gives λm = 13.6 nm, ns = 2.49 × 10^12 cm^-2, so 6.0 × 10^12 cm^-2 is n/ns ≈ 2.41; even θ = 0 gives at most 2.51. SI p. 20 says ∼2.7. Flagged (question 7). The 70 V figure (n/ns ∼ 2.0) is consistent.
- Consistent: ∆ = 1.764 kB Tc (1.37 meV); ∆Bphys = φ0/(W(L + Ls)) for GH1 to GH4 (2.12, 1.84, 1.45, 1.31 mT); ETh = ℏvF/L (2.6 and 1.6 meV); B* = ∆/(eLvF) (14 mT GH1, 9 mT GH2 versus quoted 13 and 8); Φ/Φ0 = 1/5 at 5.1 T and 6/29, 4/25, 5/36 at 5.3, 4.1, 3.6 T; vH ∼ 0.42 vF matches ⟨v²⟩/vF² ∼ 0.17; EJ/kB for 1 nA ≈ 24 mK (quoted ∼30 mK).
- Not flagged in the report: vF from δE (0.34 ± 0.05 × 10^6 m/s, SI p. 28) called "in good agreement" with 0.5 ± 0.1 × 10^6 m/s; main text gives vF ∼ 0.8 × 10^6 m/s in the Dirac cone, SI gives 0.7 ± 0.1. Eq. (4) has a factor 2 that depends on whether consecutive Vb extrema are counted as full or half periods. A garbled sentence on p. 6 ("to ETh ∼ 1.6 meV at the moiré minibands is ETh ∼ 2.6 meV").

## Unsure

- Whether field-enhanced-supercurrent-resonances should be matched at all: the claim is survival of supercurrent at high field, not growth. I kept it, adapted, because the interpretation relies on the extracted Ic magnitude and oscillations.
- Series resistance test 1: the value is stated but the calibration is not shown; I marked "no", following "a sentence alone doesn't count".
- Chiral edge row: Fig. S14 is a normal-state fan at 200 nA bias; bias heating could smear plateaus. I still treated it as shown, since the test is the measurement the source describes.
- Report length: about 900 words outside the table, at the top of the range.

## Skill issues

- The scope rule covers a "different kind of measurement" but not a non-topological claim; it is unclear whether to run the skill or how far to adapt. I adapted two entries and added two outside rows.
- The template's "What this is" text says "known lookalikes in topological transport", which reads oddly for a non-topological paper.
- No check list exists for the `supercurrent` family, so only practice checks apply; the skill doesn't say whether to adapt another family's checks (for example zbp-raw-conductance).
- "One question that no entry raises" forced me to merge two separate numerical inconsistencies into one question. The skill has no step for internal numerical consistency, though it is a natural referee check.
- Step 6 says to ask the standard questions "unless the paper already answers them (then say where)"; unclear whether to drop answered questions or keep them with the location. I kept them with the location and a follow-up.
- Step 7 says to write reports/<id>.md; the task overrode this. The arXiv abstract page title rule can't be met when only text is provided.
- "Ruled out" requires the paper to "conclude against" the lookalike; for an outside row it is unclear whether an argument against a related mechanism (here, quantum Hall edges in general) counts.
