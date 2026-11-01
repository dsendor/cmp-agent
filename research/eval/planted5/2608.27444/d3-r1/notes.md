# Run notes: arXiv 2608.27444v1

- Library: lookalikes.yaml meta.version 0.5 (28 lookalike entries, checks for zbp, shapiro, kitaev, charge, practice).
- Date: 2026-10-24. Paper version: v1 (given).

## What I read
- The skill (SKILL.md), report-template.md, the full library. I did not use read_mtx.py because there are no figure data.
- The paper: only the extracted text supplied (paper.txt), main text, Methods and Supplementary Sections D to M. I took figure details from the captions. I did not fetch the abstract page, PDF or HTML, as the run instructions said. I took the title from the first line of the text, not from an abstract page.
- Page numbers come from the page markers in the extracted text. Main text pp. 1 to 10. Supplement starts on p. 13: S1 p. 13, Section E p. 14, Section F p. 15, Fig. S5 p. 17, Fig. S8 p. 20, Section K and Fig. S13 p. 25, Section L p. 28, temperature fit discussion p. 30. They may be off by one where a marker falls mid-column.
- Data repository: none linked ("available from the corresponding author upon reasonable request", p. 10). Not used.
- Not opened: anything else in cmp-assistant, per the run instructions.
- I did not recognize the paper. It postdates my training data.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| ∆V/∆V1 ≈ 0.25 (0.27 ± 0.03, 0.24 ± 0.03, 0.25 ± 0.03) at ν = −5/2, −1/2, 3/2, read as e/4 | Fig. 2a,b,d,e,f,h; Figs. S8, S9, S11 | one device (the text says "The device"; "M.D.L. fabricated the devices") | Devices fabricated: not given. Devices measured: one presented. Cooldowns: not given. ADG periods 56 to 63 mV. B = 14 T (temperature series at 13.95 T). Field step 1 mT, about 101 points per scan. ADG and B windows per map: not stated in the text. |
| Field periods ∆B = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT, read as p ≈ 10, 2, 6 | Fig. 2e,f,h | same | Reference ∆B1 = 40.3 ± 6.7 mT at ν = −1, 10 T. From these numbers ∆B1/∆B ≈ 6.8, 3.1, 7.6. |
| ∆V/∆V1 = 0.32 ± 0.03 at ν = 2/3, read as e/3 | Fig. 2c,g; Figs. S10, S13, S14 | same | 20 repeated sweeps at fixed B; histogram ∆B = 19.6 ± 4 mT |
| Calibration: ν = −4/3 gives 0.37 ± 0.04 and ∆B1/∆B = 3.47 ± 0.79 | Fig. 1e to h; Figs. S3 to S5 | same | ν = −1 at 10 T and 14 T; ν = −2 at 10 T; ν = −4/3 at 14 T |
| Doubled period at stronger side-gate coupling (left open, context only) | Figs. 3, 4, S6, S7, S16, S17 | same | Side gates up to about 6 V; ν = −4/3 at Vsg = 0.2, 2, 5 V; ν = −1/3 at −2, 0 V |
| Temperature dependence | Figs. S16, S17 | same | T = 16 to 120 mK (12.7 to 70 mK for one panel) |
Missing: devices fabricated or measured, cooldowns, gate and field windows per map, excitation current per state (only the range 0.2 to 1 nA is given), displacement field per state (only marked as circles in Fig. 1d).

## Matching (step 2)
- Family: charge, plus practice.
- Matched:
  - coulomb-dominated-interferometer, adapted. The library entry reads interferometer oscillations as AB with CD as the lookalike. Here the paper claims CD in an antidot, and the lookalike is an AB or mixed contribution setting the gate period. The paper itself raises this possibility (p. 7).
  - charge-trap-fractional-shift. The signal is a fractional periodicity, and the ν = 2/3 data show gate hysteresis.
  - fine-tuning-and-selection (always).
- Skipped:
  - zbp entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode): no superconductor and no zero-bias peak.
  - quantization (fine-tuned-plateau, series-resistance-subtraction): no conductance value is claimed; the claim uses period ratios.
  - nonlocal entries, island-states-coulomb-spacing, shapiro entries, transparent-junction-pi-crossing, switching-jump-blind-region, field-enhanced-supercurrent-resonances, chiral-plateau-superconductor-short, false-poor-mans-majorana, diode-vortex-screening: different device class.
  - local-probe-loophole: about Majorana separation.
  - protocol-parameter-sensitivity: there is no pass/fail protocol. The analysis-choice concerns (polynomial background, picking the FFT line with the largest amplitude, error inflation at ν = −5/2, histogram used in place of FFT in some cases) go under the report-processing and report-ranges checks.
- Adapted: coulomb-dominated-interferometer (interferometer to antidot, direction reversed). I stated this in one sentence under "What this is".

## Status reasoning
- AB or mixed regime: Tested in part. The maps and period spacings are shown for all four states. The stripe slope is not analyzed: the paper says the slope method "is not applicable here" (p. 3). The regime is stated, but there is no charging energy: DC bias is inconclusive (p. 8), and the temperature fits are "not strongly distinguishable" (p. 30). I judged the field periods away from ϕ0 and the gate ratios away from ν or νLL to be strong but argued through the model, so I did not apply the single-test "ruled out" route.
- Charge trap: Tested in part.
  - The integer controls (ν = −1, −2, same device and gate) count as "all" for "shifts absent where not expected".
  - Gate leakage is "no". The fabrication-time monitoring of gate-to-contact resistance (p. 9) is a sentence, not shown data, and the air-bridge came later.
  - The two-gate map is "part": ADG versus TG maps exist only for ν = −1 and −4/3.
- Selection: Tested in part. Fig. 1d circles and the current-selection sentence count as "part" for how the data were chosen. The temperature series and the Fig. 3 minimal-regime traces are second datasets from the same device ("part").

## Sources held out
- None skipped. No library source cites 2608.27444, as far as titles, abstracts and dates show.
- Legg 2502.19560v2 was updated 2026-10-21, after this paper. It is a comment on the topological gap protocol, and I did not open its full text to confirm that it does not cite this paper. Akrap et al. 2501.18631v2 (2026-03-25) predates the paper.

## Related work checks
I opened each arXiv abstract page and confirmed the ID, title and first author, and that the abstract supports the one-line description. All were checked from the abstract, not the full text.
- 2509.04209: Di Luca, "Quantum Hall Antidot as a Fractional Coulombmeter".
- 1201.1600: Kou.
- 2010.11394: Mills.
- 2412.19886: Kim.
- 1010.4598: Halperin. This is also a library source.

## Library gaps
- No antidot entries. The CD versus AB regime question for antidots runs opposite to the interferometer entry. An antidot-specific entry with tests would help, for example: slope sign, charging energy from DC-bias diamonds, field period against ϕ0 and ϕ0/p.
- No entry for reference-calibration or lever-arm lookalikes. A gate-period ratio relies on a reference state taken at a different field, displacement field or Landau level.
- No entry for excitation or heating relative to kT and the level spacing. Here the current is 0.2 to 1 nA through a fractional state.

## Things I was unsure of, and text issues worth a look (not in the report, which has no slot for them)
- Fig. 3 panel references on p. 6: "As shown in Fig. 3d,e for ν = 2/3, and similarly for ν = −1/2 in Fig. 3g,i" conflicts with the caption, where d to f is ν = −1/2 and g to i is ν = 2/3.
- p. 7: "magnetic field periodicities at ν = −2/3 and ν = 3/2" probably means ν = 2/3.
- p. 6: the sentence "the ADG period doubles ... at ν = −5/2, −1/2, 2/3 and 3/2" is followed by a gap in the extracted text, so text may be missing.
- Temperature values disagree: 60 mK (p. 8), 50 to 70 mK and 50 mK (p. 28), and 30 to 50 mK (p. 30).
  - The ν = 2/3 doubled period persisting to 120 mK (p. 28) is not mentioned where p. 8 singles out ν = −1/2.
  - The Fig. S17 caption fits "the e/4 oscillations at ν = −1/2", while p. 30 says the minimal-excitation even-denominator amplitudes were suppressed too rapidly to fit.
- Supp. E (p. 14) uses a 50 nm top hBN against the measured 46 nm, and calls a predicted 330 mV against a measured 235 mV an "agreement".
- AD diameter 361 ± 30 nm against a lithographic 210 nm plus 46 nm hBN, described as consistent (p. 4).
- ν = −1/2: ∆B1/∆B from the quoted numbers is about 3.1 ± 0.6, against the stated p ≈ 2.
- Excitation of 0.2 to 1 nA across a resistance of order h/e² gives tens of µV against kT of about 2.6 µV at 30 mK. I folded this into question 3.

## Skill issues
- The template has no place for internal inconsistencies in the paper (figure labels, conflicting numbers). I put one into question 8 and left the rest in the notes.
- Step 7 says to write reports/<id>.md and notes files. This run forbids .md writes, so both went into the reply.
- For an adapted entry whose direction is reversed (here AB as the lookalike, where the library entry treats CD as the lookalike), the skill does not say whether to keep the library test text verbatim. I kept it verbatim in flags.json.
- "Say which regime" in charge-regime-map: it is unclear whether a regime stated from period ratios alone counts as done. I marked it done and carried the gap into the lookalike's tests.
- Page numbers are hard to give reliably from extracted text alone. The skill assumes the PDF.
- The step 6 standard questions ask about "parameter ranges", and step 1 asks for the figure ranges. With text only, map windows (ADG and B axes) cannot be read, so they are recorded as missing.
