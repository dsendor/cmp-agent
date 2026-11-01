# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. I adapted the library's interferometer entry to your antidot, where the regime question runs the other way: could an Aharonov-Bohm or mixed contribution set the gate period you read as Coulomb-dominated?

**The claim, as I read it.** In one bilayer graphene antidot driven by an air-bridge antidot gate (ADG), the gate period normalized to the ν = −1 electron period is ∆V/∆V1 ≈ 0.25 at ν = −5/2, −1/2 and 3/2 (Fig. 2a,b,d, p. 4), read as e/4 charge addition with field periods near p = 10, 2 and 6, and 0.32 ± 0.03 at ν = 2/3, read as e/3 (Fig. 2c). You leave the doubled period (Figs. 3, 4) open, so I treat it as context.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime : Done. Maps and 2D-FFTs for all four states (Fig. 2a to h); field periods "are consistent with measurements in the CD regime" (p. 4).
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. "the ν = −2 gate-voltage periodicity is consistent with electron charge" (p. 15); no ADG leakage data.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. ν = 2/3 only: "Raw data from 20 consecutive repetitions of the same measurement" (Fig. S13, p. 25).
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. "M.D.L. fabricated the devices" (p. 9), with no counts.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Side-gate limit "approximately 6 V" (p. 13); ranges around each Fig. 2 window are not given.
6. Give the processing steps from raw data to figures, with data and code : Partly. "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper" (p. 9); data on request, no code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Aharonov-Bohm or mixed regime setting the gate period (coulomb-dominated-interferometer, adapted to an antidot) | Tested in part | Field and gate map with stripe slope and spacing: part (spacings for all four states, slope not analyzed); Regime and charging parameters reported: part (regime stated, no charging energy) | "The DC-bias dependence reported in the Supp. Material also does not provide conclusive information" (p. 8) | Read the stripe slope sign in the existing Fig. 2 maps against the ν = −1 reference, and extract a charging energy from the DC-bias maps at the minimal-excitation settings |
| Charge trap or gate leakage shifting the oscillations (charge-trap-fractional-shift) | Tested in part | Shifts absent where the exotic state is not expected: all (ν = −1, −2); Gate leakage checked: no; Map of where in two-gate space the shifts occur: part (ADG versus TG for ν = −1 and −4/3 only, Fig. S5) | "In our case the instability cannot be related to quasiparticles entering and leaving the AD-bulk." (Supp. K, p. 25) | Fixed-field repeat sweeps at ν = −5/2, −1/2 and 3/2 as in Fig. S13, ADG leakage at base temperature, and one ADG versus TG map at an even-denominator state |
| Selection and fine-tuning (fine-tuning-and-selection) | Tested in part | Devices and datasets measured, and how many showed the effect: no; How the shown data were chosen: part; A second device or dataset shown: part (Fig. S16 and Fig. 3d,j, same device) | "The white circles indicate the regions where we have measured the oscillations." (Fig. 1d, p. 3) | State device and cooldown counts and the side-gate range where the e/4 period holds, and show a second map per state |

## Questions about devices and data

1. How many devices did you fabricate and measure (the author contributions mention "devices"), and how many showed the e/4 gate period?
2. Why were the others set aside, and over how many cooldowns was this device measured?
3. Which side-gate, displacement-field and field ranges did you measure at ν = −5/2, −1/2 and 3/2 beyond the Fig. 2 windows, over what side-gate range does the e/4 period hold, and which excitation current did you use at each state?
4. What does the second-best dataset at each even-denominator state look like, for example a repeat of the faint ν = −5/2 map (Fig. S8, p. 20)?
5. Could you repeat fixed-field gate sweeps at ν = −5/2, −1/2 and 3/2 as in Fig. S13, and report the air-bridge gate leakage at base temperature?
6. ∆V1 comes from ν = −1 at 10 T, while the half-filled states sit at 14 T, in the N = 1 level and at other displacement fields (Fig. 1d); how does the ADG lever arm depend on D and Landau level, and could a reference state at each state's D and field confirm it?
7. Can you identify the regime independently of the period ratios, from the stripe slope sign in the Fig. 2 maps or a charging energy from the DC-bias maps (Figs. S8c to S11c)?
8. The e/4 suppression temperature reads "approximately 60 mK" (p. 8), "between 50 mK and 70 mK" (p. 28) and "30 mK to 50 mK" (p. 30), and the doubled period at ν = 2/3 also survives to 120 mK (p. 28); which values hold, and does that change the p. 8 argument singling out ν = −1/2?

## Related work

- Di Luca et al. 2025, "Quantum Hall Antidot as a Fractional Coulombmeter", <https://arxiv.org/abs/2509.04209>. The same bilayer graphene antidot approach in the Coulomb-dominated regime, with gate period and slope giving q = e/3 at ν = 4/3, 5/3 and 7/3 and q = 2e/3 at ν = 2/3.
- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. GaAs antidots where the field period scaling with the number of bound edges identifies Coulomb-type oscillations, with a tunneling charge of 2e/3 at ν = 2/3.
- Mills et al. 2020, "Localizing fractional quasiparticles on graphene quantum hall antidots", <https://arxiv.org/abs/2010.11394>. Graphene antidots that give quasiparticle charges near ±e/3 at ν = ±1/3.
- Kim et al. 2024, "Aharonov-Bohm Interference in Even-Denominator Fractional Quantum Hall States", <https://arxiv.org/abs/2412.19886>. Bilayer graphene Fabry-Perot interferometry at half-filled states: a 2Φ0 period (e/2, or thermally smeared e/4), halved periods at hole-conjugate states, and bulk quasiparticles of charge e/4.
- Halperin et al. 2011, "Theory of the Fabry-Perot Quantum Hall Interferometer", <https://arxiv.org/abs/1010.4598>. Aharonov-Bohm and Coulomb-dominated regimes give stripes with different spacings and opposite slopes in the field and gate plane, superposed at intermediate coupling.

Happy to rerun this if you share the figure data.
