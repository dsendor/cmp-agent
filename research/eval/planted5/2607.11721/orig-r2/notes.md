# Run notes: arXiv 2607.11721v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes). Skill and template read once at the start.
- Date: 2026-10-24.

## What I read

- The paper's extracted text only (main text, figure captions, Supplementary Information pp. 17-51), as instructed. I did not fetch the abstract page or the PDF. The title comes from the first line of the text. Figure details come from captions only; I saw no images.
- Page numbers come from the page markers in the extracted text (main text pp. 1-16, SI pp. 17-51).
- No ancillary figure data. Data are "available from the corresponding author upon reasonable request" (p. 16). I did not use read_mtx.py.
- I don't recognize this paper; it postdates my training data. I used no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Phase-coherent ballistic Andreev transport: Fabry-Pérot oscillations in Ic and RN in the Dirac band and the hole minibands | Fig. 1c-e, S5-S7, S12 | GH1 (main), GH2 (S12), non-aligned control (S15) | Ic at 2 K, RN at 10 K; FP in minibands shown on the hole side (n/ns < -1) only |
| Uniform current at low field (Fraunhofer, Dynes-Fulton) | Fig. 1g, S9 | GH1 (n/ns ∼ 1.6), GH2 (n/ns ∼ 1.5) | Period 2.2 ± 0.3 mT (GH1), 1.7 ± 0.3 mT (GH2) |
| Long-ballistic regime | Fig. S8 | GH1-GH4 | Ic(T) at several densities for GH1-2; δE and IcRN vs 1/L at n/ns ∼ 1.3 and 1.2 |
| Zero-resistance pockets up to ∼6 T in the electron minibands, beyond 2rc = L | Fig. 2a, 2b, 2e, 3e, S18 | GH1; GH2 up to 5 T (S13a) | Fig. 2a range shown approx. 0 < n/ns < 2.5ish (from caption: Dirac band and n/ns > 1); 100 mK; R from lock-in with 1 nA ac; 3447 Ω series subtracted; 1/R cutoff 20 mS (S18) |
| Oscillating Ic in the pockets (phase coherence at high field) | Fig. 2c (n/ns ∼ 1.8, 4.3 T), 2e (4.1 T), S11 (2.5, 3.5, 4.5 T, two consecutive sweeps each), S13c (GH2, n/ns 1.6, 3.5 T) | GH1, GH2 | Periods 2.3-3.4 mT (GH1), 1.7-2.0 mT (GH2); Ic up to 48 ± 2 nA at 2.5 T |
| Not quantum Hall edge transport | Fig. S14 | GH1, GH2 | Landau fans at dc bias 200 nA |
| Pockets coincide with high Hofstadter band velocity | Fig. 3a-e, S18-S21 | GH1, GH2 (calculation at θ = 0.2° and 0.38°) | 205 rational fluxes p/q from 1/3 to 1/20; linecuts at 5.3, 4.1, 3.6 T |
| Moiré needed: a non-aligned junction stays below 2rc = L | Fig. S15 | 1 non-aligned junction (L ∼ 300 nm) | Densities < 5 × 10^12 cm^-2 |

Counts: 4 moiré junctions listed (Table S1), 2 show high-field pockets (GH1, GH2), 2 do not (GH3, GH4, explained by length, SI p. 33), plus 1 non-aligned control. The paper doesn't say how many junctions were fabricated (Fig. S1a shows multiple contacts per stack), how many cooldowns there were, or how many interference datasets were taken. The main text (p. 3) says "reproduced across multiple additional devices", while the SI shows one additional device with the high-field effect.

## Entries matched, adapted, skipped

- Family: closest is `supercurrent` (unusual supercurrent read as an exotic mechanism). The library has no `checks` for that family, so I walked only the `practice` checks.
- Adapted (scope rule):
  - field-enhanced-supercurrent-resonances: the signature is supercurrent growing with field, read as exotic pairing; here it is supercurrent persisting at high field, read as a Hofstadter-band mechanism. The finite-bias resonance mechanism still bears on how the switching current is read.
  - series-resistance-subtraction: the signature is conductance near 2e^2/h. Here the "vanishing resistance" pockets and the 1/R map (20 mS cutoff) depend on a 3447 Ω subtraction.
  - fine-tuning-and-selection: applies as written.
- Skipped, because they can't apply to a graphene Josephson junction with no tunnel probe, no microwaves, no island and no topological claim: all zbp entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode); fine-tuned-plateau; one-end-only and trivial-andreev-band-gap-reopening (nonlocal); island-states-coulomb-spacing; all shapiro entries (shapiro-landau-zener, shapiro-nonlinear-resistance, transparent-junction-pi-crossing, switching-jump-blind-region); charge-trap-fractional-shift and coulomb-dominated-interferometer; chiral-plateau-superconductor-short; false-poor-mans-majorana; diode-vortex-screening (no diode claim); local-probe-loophole (no Majorana claim); protocol-parameter-sensitivity (no automated pass/fail protocol, although the 20 mS cutoff in Fig. S18 is a related thresholding choice; I raised it in the questions).

## Sources held out

None. The library sources I relied on predate the paper (13 Jul 2026): Frolov et al. 2309.09368 (2023), Zhang et al. 2101.11456 (2021), and Akrap et al. 2501.18631, whose v2 is dated 25 Mar 2026 (checked on its abstract page).

## Related work: how each link was checked

All IDs, titles and first authors were confirmed on the arXiv abstract pages.
- 1504.03286 Ben Shalom: abstract plus full text (Secs. 7-9 on near-edge Andreev states, the 2rc = L cutoff, and Fraunhofer-based current distribution). This is the source of the outside row's tests.
- 1512.09083 Amet: abstract plus full text, searched (IS = 0.5 nA; plateaus revealed with IDC = 3-6 nA; period 0.5 mT close to the low-field Fraunhofer period). This is the source of the outside row's tests.
- 2503.15384 Villani: abstract.
- 2402.14451 Barrier: abstract.
- 1705.11170 Krishna Kumar: abstract (oscillations "persist well above room temperature"). This is the source of the outside row's test.
- Also opened, not listed: 1801.01447 Draelos (abstract), 1504.07630 Allen (abstract).

## Library gaps

- No checks for the `supercurrent` family (for example: show I-V against voltage at the claimed pockets, the current distribution at the relevant field, and the normal-state map at the same settings).
- Missing entries for high-field supercurrent in graphene junctions: chiral quantum Hall edge supercurrent (Amet 2016), near-edge mesoscopic Andreev states (Ben Shalom 2016), 1D channels along domain walls (Barrier 2024), and normal-state Brown-Zak conductance confounding conductance-based maps (Krishna Kumar 2017).
- series-resistance-subtraction is written for quantized conductance only. A broader signature ("any zero-resistance or conductance threshold set after subtracting a series resistance") would cover two-probe junction maps.

## Unsure, or worth the authors' attention (not in the report)

- p. 6, garbled sentence: "ranging from ETh ∼ 2.6 meV at the main Dirac band, to ETh ∼ 1.6 meV at the moiré minibands is ETh ∼ 2.6 meV". The numbers check out (ℏvF/L with 0.8 and 0.5 × 10^6 m/s and L = 200 nm), but the tail repeats the Dirac-band value.
- The miniband vF from Ic(T) is 0.34 ± 0.05 × 10^6 m/s (SI p. 28), called "in good agreement" with 0.5 ± 0.1; the main-text ETh uses 0.5.
- Fig. 3 text threshold: the conjecture needs ⟨v²⟩/vF² of about 0.17, while the text quotes the range where it exceeds 0.1.
- Fig. S18: the caption puts band velocity in (a,b) and 1/R in (c,d); the text says velocity in (a) and (c), resistance in (b) and (d).
- SI p. 20 writes the density as "6.0 × 10−12 cm-2" (exponent sign). SI p. 30: "∆B = 2.2 ± 0.4 mT, corresponds to one and two units of superconducting flux quanta" reads garbled.
- Fabry-Pérot evidence for ballistic transport in the minibands comes from the hole side (n/ns < -1), while the high-field claim is on the electron side; Ic(T) at n/ns ∼ 1.3 covers the electron side.
- Fig. 2b: the main text cites a 2.5 T trace with Ic ∼ 48 nA; the caption doesn't list the fields shown. I couldn't see whether any trace is at 5-6 T, which is why it is question 4.
- I computed consistency checks (moiré wavelength about 13.6 nm giving Φ0 per cell at about 25.6 T; ∆Bphys values; IQ = e∆/h ∼ 54 nA; B* values). All agree with the text.
- Chiral QH row: marked "ruled out" on the strength of the Fig. S14 Landau-fan test alone. One caveat: a 200 nA bias could smear Landau levels, but the text says levels are absent "at the same regions" where pockets appear, which implies they are visible elsewhere in the same map.

## Skill issues

- The scope rule covers "a different kind of measurement" but not a non-topological claim in a related device. I applied it ("adapt the matching entries") and said so in "What this is".
- A family with entries but no `checks` (supercurrent) leaves step 3 with only the practice checks. The skill doesn't say whether to improvise family checks; I did not.
- Step 7 says to use the title on the arXiv abstract page. This run was text-only and forbade fetching it, so I took the title from the text.
- Test "Series resistance calibrated independently, with its value": it's unclear how to score a value given without its calibration. I used "part".
- For an outside row where the paper concludes against the explanation with its own argument and data, the skill doesn't say whether the paper's own tests or only the cited paper's control count. I took the tests from the cited paper's control (Amet), and they match what the paper shows.
- The skill says to write reports/<id>.md and .notes.md; this run asked for them in the reply. I followed the run instructions.
