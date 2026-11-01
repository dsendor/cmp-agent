# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport. A lookalike is an ordinary effect that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper measures charge with a quantum Hall antidot. The library's charge entries were written for interferometers and quantum dots, so I adapted the two that apply.

**The claim, as I read it.** In one gate-defined bilayer graphene antidot at B = 14 T, the antidot-gate period of δRt oscillations, normalized to the ν = −1 period at 10 T, gives ∆V/∆V1 ≈ 0.25 at ν = −5/2, −1/2 and 3/2. You read this as charge-e/4 addition in the Coulomb-dominated regime (Fig. 2a, b, d; p. 4). You also report e/3 at ν = 2/3 (Fig. 2c) and a side-gate-driven crossover to a doubled period (Fig. 3).

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Done. "Variation of the transmitted resistance oscillations δRt as a function of the ADG voltage Vadg and the magnetic field B for filling factors ν = −5/2, −1/2, 2/3 and 3/2" (p. 4, Fig. 2), "consistent with measurements in the CD regime" (p. 4).
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. The same gate gives the expected periods at reference states: "∆V /∆V1 = 0.37 ± 0.04, in agreement with the value q/e = 1/3" at ν = −4/3 (p. 4). Charge traps and gate leakage during measurement are not discussed.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. Done at ν = 2/3 only: "Raw data from 20 consecutive repetitions of the same measurement" (p. 25, Fig. S13).
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. The text describes one device ("The device was measured in a Leiden wet dilution refrigerator", p. 9) and gives no counts.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The white circles indicate the regions where we have measured the oscillations" (p. 3, Fig. 1d). The side-gate limit is stated (p. 13). The ADG and field windows of Fig. 2 are not explained.
6. Give the processing steps from raw data to figures, with data and code : Partly. "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper" (p. 9). The data are "available from the corresponding author upon reasonable request" (p. 10). No code is given.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Aharonov-Bohm or mixed regime setting the period (adapted from coulomb-dominated-interferometer) | Tested in part | Field and gate map with stripe slope and spacing: all; regime and charging parameters reported: part | "Although the fits cannot therefore identify the transport regime, they still constrain the electron temperature of our setup." (p. 30, Fig. S17) | Report the charging energy and lever arm from the DC-bias maps (Figs. S8 to S11c), and the stripe slope sign in Fig. 2a to d next to ν = −1 |
| Charge trap or side dot adding resonances (adapted from charge-trap-fractional-shift) | Tested in part | Shifts absent where not expected: all; gate leakage checked: no; two-gate map: part | "∆V /∆V1 = 0.37 ± 0.04, in agreement with the value q/e = 1/3 expected for CD antidot oscillations" (p. 4, Fig. 1g–h) | Repeat sweeps at ν = −5/2, −1/2, 3/2 as in Fig. S13; show gate leakage at base temperature; one ADG versus TG map at an e/4 filling |
| Fine-tuning and selection | Tested in part | Devices and datasets counted: no; how shown data were chosen: part; second dataset: part | "For each filling factor, we selected a current sufficiently low to avoid merging distinct features" (p. 9); the temperature series is a second dataset: "All measurements are performed at B = 13.95 T." (p. 28, Fig. S16) | State device and cooldown counts; show a second minimal-excitation map per filling |
| Multiple charged rings around the antidot (not in library; Kataoka et al. 2000) | Tested in part | Gate and field periods compared with the number of charged edges, integer control: part | "the ν = −2 gate-voltage periodicity is consistent with electron charge, while its magnetic-field periodicity is consistent with p = 2" (p. 15, Fig. S3) | Repeat the ν = −2 control at 14 T, and at ν = −3 for the −5/2 state, with the same ADG |

## Questions about devices and data

1. How many devices did you measure, and how many showed the e/4 period? The text describes one device ("The device was measured in a Leiden wet dilution refrigerator", p. 9), while the author contributions say "M.D.L. fabricated the devices" (p. 9).
2. If other devices or cooldowns were measured, why were they set aside, and how many cooldowns do the data in Figs. 2 and 3 span?
3. Which ranges of ADG voltage, magnetic field and side-gate voltage did you measure beyond the windows in Figs. 2 and 3, and how were the Fig. 2 windows chosen?
4. What does the second-best dataset at each even-denominator filling look like, for example a minimal-excitation map at another side-gate setting or field?
5. On p. 4 you give ADG periods "in the range 112 mV to 126 mV" for the e/4 states, but with "∆V1 = 233 ± 14.3 mV" (p. 15) the ratios 0.24 to 0.27 correspond to about 56 to 63 mV, and 112 to 126 mV matches the doubled-period regime (∆V/∆V1 ≈ 1/2, p. 7). Which periods went into the ratios? While checking numbers I also noticed "ν = −2/3" on p. 7 where the data are at 2/3, Fig. 3 panel references on p. 6 ("Fig. 3d,e for ν = 2/3", "ν = −1/2 in Fig. 3g,i") that are swapped relative to the caption, and suppression temperatures given as "approximately 60 mK" (p. 8), "between 50 mK and 70 mK" (p. 28) and "30 mK to 50 mK" (p. 30).
6. Your reference ∆V1 comes from ν = −1 at 10 T while the e/4 data are at 14 T. What ADG period do you get at ν = −1 at 14 T, and does the e/4 ratio hold if you normalize to that value or to ν = −4/3 at 14 T?
7. Could you report the charging energy and ADG lever arm from the DC-bias maps (Figs. S8 to S11, panels c) for the minimal-excitation data, and the sign of the stripe slope in Fig. 2a to d next to the ν = −1 reference, so the Coulomb-dominated reading rests on more than the period ratios?
8. Did you check gate leakage at base temperature, and did you repeat sweeps at ν = −5/2, −1/2 and 3/2 as you did at 2/3 (Fig. S13), to separate reproducible resonances from charge rearrangements?

## Related work

- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. GaAs antidots: Coulomb-type oscillations identified from how the field period scales with the number of bound edges; tunneling charge (2/3)e at ν = 2/3.
- Mills, Averin and Du 2020, "Localizing fractional quasiparticles on graphene quantum hall antidots", <https://arxiv.org/abs/2010.11394>. Graphene antidots with quasiparticle charge of about ±e/3 at ν = ±1/3.
- Di Luca et al. 2025, "Quantum Hall Antidot as a Fractional Coulombmeter", <https://arxiv.org/abs/2509.04209>. Bilayer graphene antidot in the Coulomb-dominated regime: e/3 at 4/3, 5/3, 7/3, 2e/3 at 2/3, and both e/3 and 2e/3 signatures at 8/3.
- Henzinger et al. 2026, "Controlled localization of anyons in a graphene quantum Hall interferometer", <https://arxiv.org/abs/2603.11182>. Bilayer graphene interferometer with an embedded dot/antidot: at half filling the interfering edge appears to carry e/2 while e/4 charges stay localized.
- Kim et al. 2026, "Selective braiding of different anyons in the even-denominator fractional quantum Hall effect", <https://arxiv.org/abs/2603.11162>. Interferometer with an embedded antidot, braiding phases π and π/2 attributed to e/2 quasiparticles encircling e/2 or e/4, plus switching of antidot occupancy over time.

Happy to rerun this if you share the figure data.
