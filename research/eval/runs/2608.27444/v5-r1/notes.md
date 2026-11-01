# Run notes: arXiv 2608.27444v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes, checks for zbp, shapiro, kitaev, charge, practice).
- Date: 2026-10-24. Version reviewed: v1 (given). AI only.

## What I read
- The local abstract page (abs.html): title "Trapping $e/4$ quasiparticles in bilayer graphene", authors Di Luca, Hajigeorgiou, Ma, Waldherr, Watanabe, Taniguchi, Banerjee, dated 2026-08-27.
- All of paper.txt, the extracted text of the 31-page PDF including the supplement (Secs. D to M).
- PDF pages 4, 5, 18 and 20 rendered to images, to read figure axes and ranges (Fig. 2, Fig. 3, Fig. S6, Fig. S8). Other figure pages I read only from captions.
- I did not fetch the paper online. It has no ancillary figure data, so read_mtx.py was not used. Data are "available from the corresponding author upon reasonable request" (p. 10), so I used no data repository.
- Opened without problems. Nothing failed to open.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| e/4 localized charge at ν = −5/2, −1/2, 3/2 from ΔV/ΔV1 = 0.27 ± 0.03, 0.24 ± 0.03, 0.25 ± 0.03 | Fig. 2a,b,d,e,f,h (p. 4); Figs. S8, S9, S11 | one gate-defined BLG antidot with air-bridge ADG (lithographic diameter ~210 nm, extracted 361 ± 30 nm) | ΔV 56–63 mV. ΔB = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT, read as p ≈ 10, 2, 6. Fig. 2a: B 13.930–13.965 T, Vadg −3.60 to −2.90 V. Fig. 2b: 13.90–14.00 T, −3.30 to −2.90 V. Fig. 2d: 13.93–14.00 T, 0.55–1.05 V |
| e/3 at ν = 2/3 | Fig. 2c,g; Figs. S10, S13–S15 | same | ΔV/ΔV1 = 0.32 ± 0.03, ΔB1/ΔB = 2.32 ± 0.93. 20 repeated sweeps (Fig. S13). Fig. 2c: 13.90–14.00 T, Vadg 2.74–3.44 V |
| Calibration and controls | Fig. 1e–h, Figs. S3–S5 | same | ΔV1 = 233 ± 14.3 mV and ΔB1 = 40.3 ± 6.7 mT from ν = −1 at 10 T. ν = −1 at 14 T, ν = −2 at 10 T, ν = −4/3 at 14 T (0.37 ± 0.04, p = 3.47 ± 0.79). ADG vs TG at ν = −1 and −4/3 |
| Crossover to doubled gate period at −5/2, −1/2, 2/3, 3/2 with stronger side-gate coupling, absent at −4/3 and −1/3 | Fig. 3, Fig. 4, Figs. S6–S11 | same | ν = −4/3 at side gates 0.2, 2, 5 V. ν = −1/3 at −2 and 0 V. Side gates limited to ~5–6 V. ΔVdouble/ΔVminimal ≈ 2 for all four states; ΔB ratio scattered (Fig. 3q,s) |
| Temperature dependence | Figs. S16, S17 | same | T = 16, 30, 50, 70, 95, 120 mK (−5/2 minimal: 12.7–70 mK), at B = 13.95 T. e/4 suppressed by ~50–70 mK |
| Experimental settings | Methods | same | Base ~10 mK, electron T 30–50 mK, I_ac 0.2–1 nA at 17.777 Hz, 1 mT field step, typically ~101 points per scan |

Missing counts: devices fabricated, measured and showing the effect; cooldowns; tunings tried before the minimal regime; ADG and field windows explored beyond those shown. The paper only ever refers to "the device". Fig. 1b says "a device with the air-bridge".

## Entries matched, adapted, skipped
- Matched and adapted (charge family; antidot in place of quantum dot or Fabry-Perot): charge-trap-fractional-shift (claim is a fractional period ratio, not a fractional shift; adapted to traps or side states adding or shifting resonances), coulomb-dominated-interferometer (antidot in place of Fabry-Perot; the concern runs the other way: a claimed CD reading that could be AB or mixed), fine-tuning-and-selection (always).
- Checks walked: charge-regime-map, charge-control-regime, charge-repeat-sweeps, then report-counts, report-ranges, report-processing.
- Skipped, because the device has no superconductor, no Majorana claim, no Josephson junction, no Kitaev chain and no diode: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, all shapiro entries, field-enhanced-supercurrent-resonances, spin-orbit-length-pinning, exceptional-point-zero-mode, false-poor-mans-majorana, local-probe-loophole, diode-vortex-screening.
- Also skipped: series-resistance-subtraction (no quantized conductance value is claimed) and protocol-parameter-sensitivity (no pass/fail protocol; the analysis choices, such as the 2D-FFT line with the largest amplitude and the inflated −5/2 error, fall under report-processing).

## Sources held out
- None. No library source cites 2608.27444 by title, authors or ID. I judged this from titles and dates: every source predates August 2026, and I did not open the two 2026 v2 sources (Legg 2502.19560, Akrap 2501.18631) to confirm. Their topics are the topological gap protocol and reproducibility.

## Related work, how each was checked
- 2504.16750, 2509.04209, 1201.1600, 2412.19886, 2602.08468, and 2606.19187 (outside row): ID and title confirmed on the arxiv.org/abs page; first author confirmed from citation_author; abstract text read through the export.arxiv.org API. Each one-line description is checked against the abstract only, not the full text.
- All are earlier than the paper under review. 2504.16750, 2509.04209, 2606.19187 and 2602.08468 share authors with it.

## Library gaps
- Field-dependent charging energy from constriction coupling (Hajigeorgiou et al. 2026, https://arxiv.org/abs/2606.19187): used as an outside row. Its tests come from the abstract's control (correlate charging energy modulation with constriction magnetoconductance; the effect appears only at strong coupling). It bears on the doubled-period regime, not on the weak-coupling e/4 claim.
- No antidot-specific entry. Two candidates: CD to AB crossover in antidots giving period doubling with no bunching (Di Luca et al. 2025, 2504.16750, integer ν = 2 and 4), and lever-arm or reference calibration for gate-period charge ratios (ΔV1 taken at another field, filling and ADG window).
- The charge family has no check for the reference calibration behind a period ratio.

## Unsure
- Whether charge-trap-fractional-shift is a fair match: its signature is fractional shifts, and the paper's signal is a period ratio.
- "Gate leakage checked" marked no. Methods (p. 9) say the gate-to-contact resistance was monitored during fabrication etching, which is a sentence about fabrication and shows no measurement.
- coulomb-dominated-interferometer kept at tested in part: the maps fit the CD limit, and the ΔB uncertainties (up to 44%) and the lack of a charging energy leave a mixed regime unseparated. A reader could argue the map alone separates the extreme AB limit (p = 1, ΔV/ΔV1 = ν).
- The p ≈ 10 assignment at ν = −5/2: ΔB1/ΔB = 40.3/5.9 ≈ 6.8 before the 8% area correction. I did not raise this separately; question 7 covers the field sampling.
- Fig. 3 panel labels and caption disagree about which filling d–f and g–i show; p. 7 writes "ν = −2/3". I noted both as a small thing.
- I did not recognize the paper. It postdates my training data, so I used no knowledge of its later history.

## Skill issues
- The skill expects one status per lookalike. Here the same lookalike (AB or mixed regime) bears on two claims, the e/4 claim and the doubled-period crossover, and the statuses differ. It is unclear whether to split the row or describe the second claim in the cell. I kept one row and named the doubled regime in the suggested check.
- Scope adaptation: the charge entries' signatures say "shifts" and "interferometer". For period-ratio charge measurements in antidots, the skill does not say how close a match has to be.
- Outside-row tests: "Take its tests from the control that paper describes" does not say whether the abstract is enough. I used only the abstract.
- Step 5 says "open its arXiv abstract page"; with the API also allowed, it is unclear whether the API abstract counts. I did both.
- Hold-out rule: a library source can't be checked for citing the paper without opening it, and the skill does not say whether title and date screening is enough.
- Report length: 600 to 900 words is hard to hit with six checks, eight questions and five related papers. This report runs about 1000 words outside the table, counting symbols.
- Step 7 says to write reports/<id>.md; this run returned the text in the reply, as the prompt instructed.
