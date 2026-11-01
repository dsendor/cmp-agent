# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library is built around hybrid superconducting devices; your antidot charge measurement sits closest to its fractional-charge entries, so I adapted the interferometer regime entry and the charge-trap entry to an antidot.

**The claim, as I read it.** In one gate-defined antidot in Bernal bilayer graphene at B = 14 T, the gate period driven by the air-bridge antidot gate, normalized to the ν = −1 electron period at 10 T, gives ∆V/∆V1 ≈ 0.25 at ν = −5/2, −1/2 and 3/2 (Fig. 2a,b,d, p. 4), read as a localized charge of e/4, with e/3 at ν = 2/3 (Fig. 2c). A second, more tentative claim is a crossover to a doubled gate period as the side gates raise the antidot-edge coupling (Fig. 3), for which you leave two interpretations open (pp. 6 to 7).

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Done. "At ν = −5/2, −1/2, and 3/2, we observe Coulomb-dominated (CD) oscillations corresponding to the addition of charge e/4" (p. 1), with a Vadg-B map and 2D-FFT for every state (Fig. 2a–h, p. 4).
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. Your integer controls behave as expected: "The ν = −1 measurements at both 10 T and 14 T are consistent with electron charge periodicity and with p = 1" (p. 15). No trap test or low-temperature leakage measurement is shown.
3. Repeat sweeps to separate reproducible periods from stochastic charge jumps : Partly. Done at ν = 2/3 only: "Raw data from 20 consecutive repetitions of the same measurement" (Fig. S13, p. 25).
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The device was measured in a Leiden wet dilution refrigerator" (p. 9); the number of devices made, cooldowns and datasets set aside are not given.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The white circles indicate the regions where we have measured the oscillations." (Fig. 1d, p. 3); side-gate and field ranges beyond the shown maps are not listed.
6. Give the processing steps from raw data to figures, with data and code : Partly. "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper." (p. 9); the data are "available from the corresponding author upon reasonable request" (p. 10) and no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Aharonov-Bohm or mixed regime, where the gate period no longer counts the localized charge (adapted from the Coulomb-dominated interferometer entry) | Tested in part | Field and gate map with stripe slope and spacing: all (Fig. 2a–h); regime and charging parameters reported: part (regime named, DC-bias maps in Fig. S8–S11, no charging energy or slope sign) | "Although the fits cannot therefore identify the transport regime, they still constrain the electron temperature of our setup." (p. 30) | Report the stripe slope sign in each Vadg-B map next to ν = −1, a charging energy from the DC-bias maps, and wider field scans. |
| Charge trap or side dot near the antidot that adds jumps or extra periods (adapted) | Tested in part | Shifts absent where the exotic state is not expected: all (ν = −1 and −2 give e, Fig. S4); gate leakage checked: no; map in two-gate space: part (ADG versus TG only at ν = −1 and −4/3, Fig. S5) | "In our case the instability cannot be related to quasiparticles entering and leaving the AD-bulk." (p. 25) | Repeated fixed-field sweeps like Fig. S13 at ν = −5/2, −1/2 and 3/2, leakage at base temperature, and ADG versus TG maps at those fillings. |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part (measured regions marked in Fig. 1d, no device or cooldown count); how the shown data were chosen: part; a second device or dataset shown: part (second e/4 datasets in Fig. 3d,j and Fig. S16, one device) | "For each filling factor, we selected a current sufficiently low to avoid merging distinct features or activating additional transport paths and unwanted excitations" (p. 9) | State device and cooldown counts and the side-gate settings tried per filling, and show a second e/4 map per filling. |

## Questions about devices and data

1. How many devices did you fabricate and measure, over how many cooldowns, and how many showed the e/4 gate period? The Methods describe "The device" (p. 9), while the author contributions say "M.D.L. fabricated the devices" (p. 9).
2. Why were the other devices or cooldowns set aside?
3. Which ranges of side-gate voltage, magnetic field and antidot-gate voltage did you measure at ν = −5/2, −1/2 and 3/2 beyond the ones shown, and in how many of those settings did the e/4 period appear?
4. What does the second-best e/4 dataset at each even-denominator filling look like, for example a Vadg-B map at a second side-gate setting within the minimal-excitation regime?
5. Most field scans have "typically NB ≈ 101 points per scan" at 1 mT steps (p. 10), about 2.5 periods of ∆B1 = 40.3 mT, and at ν = −1/2 in the doubled regime "there is no full magnetic field period present in the data" (Fig. S9, p. 21). Could you take wider field scans, and report the sign of the stripe slope in each map next to ν = −1, which Halperin et al. use to tell the two regimes apart?
6. Did you repeat fixed-field sweeps at the even-denominator states, as you did at ν = 2/3 (Fig. S13), and check gate leakage at base temperature? A nearby trap could add jumps that the 2D-FFT reads as a period.
7. The suppression temperature of the e/4 oscillations reads "approximately 60 mK" (p. 8), "between 50 mK and 70 mK" (p. 28) and "30 mK to 50 mK" (p. 30). Which applies? And since the doubled oscillations at ν = 2/3 "also remain finite up to 120 mK" (p. 28), how does that bear on reading the 120 mK persistence at ν = −1/2 as a different mechanism (p. 8)?
8. At ν = −1/3, Fig. S7 shows side-gate voltages of −2 V and 0 V, while p. 8 says "Even at the largest side-gate voltage accessible in our device, no period doubling is observed". What was the largest side-gate voltage reached at ν = −1/3?

## Related work

- Di Luca et al. 2025, "Quantum Hall Antidot as a Fractional Coulombmeter", <https://arxiv.org/abs/2509.04209>. Your earlier bilayer graphene antidot in the Coulomb-dominated regime, reporting e/3 at ν = 4/3, 5/3 and 7/3 and 2e/3 at ν = 2/3 from the gate period and oscillation slope.
- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. GaAs antidots where field and gate periods give a tunneling charge of e at ν = 2 and (2/3)e at ν = 2/3, with the field period scaling with the number of bound edges.
- Henzinger et al. 2026, "Controlled localization of anyons in a graphene quantum Hall interferometer", <https://arxiv.org/abs/2603.11182>. A gate-controlled dot or antidot inside a bilayer graphene interferometer; at half filling the interfering edge appears to carry e/2 while e/4 charges stay localized.
- Kim et al. 2026, "Selective braiding of different anyons in the even-denominator fractional quantum Hall effect", <https://arxiv.org/abs/2603.11162>. An interferometer with an embedded antidot resolving braiding phases attributed to e/2 quasiparticles encircling e/2 or e/4, and switching of the antidot occupancy over time.
- Ghosh et al. 2024, "Coherent Bunching of Anyons and their Dissociation in Interference Experiments", <https://arxiv.org/abs/2412.16316>. GaAs interferometers at ν = 2/3, 3/5 and 4/7 with flux periods of Φ0/ν read as bunched quasiparticles, which charging a central antidot gate dissociates.

Happy to rerun this if you share the figure data.
