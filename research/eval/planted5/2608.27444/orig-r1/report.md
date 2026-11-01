# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library's charge entries are written for interferometers and quantum dots, so I adapted them to your antidot, where the reading runs the other way: you take the oscillations to be Coulomb-dominated, and the question is whether an Aharonov-Bohm or mixed regime could produce the same gate period.

**The claim, as I read it.** Your claim is that at ν = −5/2, −1/2 and 3/2 the antidot-gate period, normalized to the ν = −1 electron period, is about 0.25, so the localized charge changes in steps of e/4. You report "∆V/∆V1 = 0.27 ± 0.03 for ν = −5/2, ∆V/∆V1 = 0.24 ± 0.03 for ν = −1/2 and ∆V/∆V1 = 0.25 ± 0.03 for ν = 3/2" (p. 4, Fig. 2), with e/3 at ν = 2/3. All of it comes from one gate-defined antidot device at B = 14 T, and the reference is ν = −1 at 10 T.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in: Done. Vadg versus B maps and 2D-FFTs are shown for every state (Fig. 2a-h), and "The corresponding magnetic-field periods ... are consistent with measurements in the CD regime." (p. 4)
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage: Partly. The integer states give the electron period: "we further find that the ν = −2 gate-voltage periodicity is consistent with electron charge" (p. 15, Fig. S3). Gate separation was monitored only during fabrication (p. 9).
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps: Partly. Repeats are shown at ν = 2/3 only: "Raw data from 20 consecutive repetitions of the same measurement, at a fixed magnetic field of B = 14 T." (p. 25, Fig. S13)
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside: Partly. "The device was measured in a Leiden wet dilution refrigerator" (p. 9), and "The white circles indicate the regions where we have measured the oscillations." (p. 3, Fig. 1d). There is no count of devices fabricated or of cooldowns.
5. Disclose the full parameter ranges measured and why each shown range was chosen: Partly. The side-gate limit is stated ("in our case of approximately 6 V", p. 13), as are the temperature steps and the field step (p. 10, p. 28). The ADG and field ranges measured beyond each map are not stated.
6. Give the processing steps from raw data to figures, with data and code: Partly. "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper." (p. 10). The data are "available from the corresponding author upon reasonable request" (p. 10), and no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Aharonov-Bohm or mixed regime read as Coulomb-dominated charge addition (adapted from coulomb-dominated-interferometer) | Tested in part | Field and gate map with stripe slope and spacing: part (both periods are given for all states, the slope sign is not stated); Regime and charging parameters reported: part (the regime is stated, no charging energy) | "For several of the other oscillations, including the minimal excitation oscillations of the even-denominator states, the amplitude is suppressed too rapidly with temperature for a reliable extraction." (p. 30, Fig. S17) | State the stripe slope sign in Fig. 2a-d against the ν = −1 reference, and extract a charging energy from the minimal-excitation DC-bias maps (Figs. S8c to S11c) |
| Integer charges in a nearby trap or side region (charge-trap-fractional-shift) | Tested in part | Shifts absent where the exotic state is not expected: all; Gate leakage checked: no; Map of where in two-gate space the shifts occur: no (ADG versus TG maps exist only for ν = −1 and −4/3) | "we further find that the ν = −2 gate-voltage periodicity is consistent with electron charge" (p. 15, Fig. S3) | Repeat ADG sweeps at fixed field for the e/4 states as in Fig. S13, show ADG versus TG maps at one e/4 filling, and report leakage at base temperature |
| Non-representative example after fine-tuning (fine-tuning-and-selection) | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: part (temperature series and side-gate series, one device) | "The device was measured in a Leiden wet dilution refrigerator with a base temperature of approximately 10 mK." (p. 9) | Give device and cooldown counts and the side-gate settings tried, and show e/4 at a second field or cooldown with its extracted ratio |
| Filling-dependent antidot area or gate lever arm (not in library; Hata et al. 2024) | Tested in part | Gate lever arm calibrated at the field and filling of interest: part (ν = −1 and −4/3 at 14 T, none at an even-denominator filling); Antidot area at each filling compared through the field period: part (an 8 % area change is estimated, not measured) | "Applying the ν = −1 reference periods to our ν = −4/3 data yields results consistent with both p = 4 and charge e/3." (p. 15, Fig. S3) | Renormalize Fig. 4b with ν = −1 at 14 T, and report the area the field period gives at each even-denominator filling |

## Questions about devices and data

1. How many devices did you measure (the author contributions mention "devices"), how many cooldowns, and how many devices showed the 0.25 gate-period ratio at the even-denominator states?
2. Why were the other devices, and the developing states at ν = +1/2 and +5/2 marked in Fig. 1d, set aside?
3. Which ranges of ADG voltage, magnetic field and side-gate voltage did you measure at each filling beyond those in Fig. 2, and how did you pick the side-gate setting you call the weak-coupling regime?
4. What does the second-best dataset for each e/4 state look like, for example the same state at another field, side-gate setting or cooldown, with its extracted ΔV/ΔV1?
5. What is the sign of the stripe slope in Fig. 2a-d compared with the ν = −1 reference, and can you extract a charging energy from the DC-bias maps of the minimal-excitation data (Figs. S8c to S11c)?
6. How do the ratios in Fig. 4b change if you normalize with ν = −1 at 14 T (Fig. S3) in place of 10 T, and what antidot area do the field periods give at each even-denominator filling?
7. Did you repeat ADG sweeps at fixed field for the e/4 states, as in Fig. S13 for ν = 2/3, and did you check gate leakage at base temperature?
8. Could you reconcile a few cross-references: p. 6 assigns Fig. 3d,e to ν = 2/3 and Fig. 3g,i to ν = −1/2 while the caption assigns d-f to ν = −1/2 and g-i to ν = 2/3; p. 7 mentions ν = −2/3; and the e/4 suppression temperature reads about 60 mK (p. 8), 50 to 70 mK (p. 28) and 30 to 50 mK (p. 30)?

**A few notes on the table.** The gate-period ratio is the heart of your claim, so the regime question carries the most weight. You already note that the AB limit predicts ∆V/∆V1 = ν, or νLL in the BLG interferometers, and either gives values well away from 0.25. Stating the stripe slope sign and a charging energy for the minimal-excitation maps would close the loop with data already in hand. The temperature fits can't separate the two regimes for the e/4 oscillations, which you say clearly on p. 30.

The normalization uses a reference at a different field (10 T against 14 T). Your ν = −4/3 and ν = −1 checks at 14 T support the transfer. Hata et al. found the antidot area changes with filling, so a short table of ΔV/ΔV1 under both references, plus the area implied at each even-denominator filling, would show how much the 0.25 depends on that choice. Your field periods give p ≈ 10, 2 and 6, which makes this worth spelling out.

Your repeated-sweep analysis at ν = 2/3 (Figs. S13 to S15) is a good model. The same analysis on one e/4 state would answer the charge-trap and hysteresis question directly.

## Related work

- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. From field and gate periods in GaAs antidots, it finds Coulomb-type oscillations and a tunneling charge of 2e/3 at ν = 2/3.
- Di Luca et al. 2025, "Quantum Hall Antidot as a Fractional Coulombmeter", <https://arxiv.org/abs/2509.04209>. It uses a BLG antidot in the Coulomb-dominated regime to read charge from the gate period and slope, finding e/3 at ν = 4/3, 5/3, 7/3 and 2e/3 at ν = 2/3.
- Hata et al. 2024, "Coulomb oscillations of a quantum antidot formed by an airbridged pillar gate in the integer and fractional quantum Hall regime", <https://arxiv.org/abs/2412.11401>. In an air-bridged antidot, it finds a smaller area at ν = 2/3 than at ν = 2 and 1, and it infers the effective charge by assuming a constant gate capacitance.
- Kim et al. 2024, "Aharonov-Bohm Interference in Even-Denominator Fractional Quantum Hall States", <https://arxiv.org/abs/2412.19886>. BLG Fabry-Perot interferometers show a 2Φ0 period at even-denominator states (e/2 interfering, or e/4 smeared) and half-expected periods at hole-conjugate states.
- Halperin et al. 2011, "Theory of the Fabry-Perot Quantum Hall Interferometer", <https://arxiv.org/abs/1010.4598>. It shows that AB-dominated and Coulomb-dominated oscillations give stripes in the B-V_G plane with different spacings and slopes of opposite sign, superposed at intermediate coupling.

Happy to rerun this if you share the figure data.
