# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper measures fractional charge with a quantum Hall antidot, so I adapted the library's interferometer and charge-trap entries to an antidot read through gate-period ratios. I worked from the extracted text and figure captions only.

**The claim, as I read it.** In one bilayer graphene antidot at B = 14 T, the antidot-gate period normalized to ν = −1 at 10 T is about 0.25 at ν = −5/2, −1/2 and 3/2 (Fig. 2a,b,d) and 0.32 at ν = 2/3 (Fig. 2c). You read these as localized charges of e/4 and e/3 in the Coulomb-dominated regime. Stronger side-gate coupling roughly doubles the gate period (Fig. 3). You leave the origin of that doubling open.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Partly. You map Vadg against B for all four states and state the regime: "The corresponding magnetic-field periods ... are consistent with measurements in the CD regime" (p. 4). The text does not give the stripe slope sign, and at ν = 2/3 the 2D-FFT periods are "not considered reliable" (Fig. S10, p. 22).
2. Show the effect is absent where it is not expected, and rule out charge traps and gate leakage : Partly. "The ν = −1 measurements at both 10 T and 14 T are consistent with electron charge periodicity and with p = 1" (p. 15). ν = −4/3 gives e/3 (Fig. S6). Charge traps are not discussed, and gate leakage is described only as a fabrication step (p. 9).
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. "Raw data from 20 consecutive repetitions of the same measurement" (Fig. S13, p. 25) covers ν = 2/3 only.
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The device was measured in a Leiden wet dilution refrigerator" (p. 9). You do not give the number of devices fabricated or cooldowns.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The white circles indicate the regions where we have measured the oscillations" (Fig. 1d, p. 3). The side-gate limit and the excitation choice are explained (pp. 9, 13). The gate windows measured beyond each map are not given.
6. Give the processing steps from raw data to figures, with data and code : Partly. "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper" (p. 9). The data are "available from the corresponding author upon reasonable request" (p. 10), and no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Aharonov-Bohm or mixed regime setting the gate period (library: Coulomb-dominated interferometer, adapted to an antidot) | Tested in part | Field and gate map with stripe slope and spacing: part; Regime and charging parameters reported: part | "a magnetic field period ratio of ∆B1 /∆B = 2.32 ± 0.93, compatible with q = e/3 and p = 2" (p. 4); "Although the fits cannot therefore identify the transport regime" (p. 30) | State the slope sign of each minimal-regime map against the CD and AB expectations, and report charging energies from the DC-bias data in Figs. S8 to S11 |
| Charge trap or side dot capacitively coupled to the antidot | Tested in part | Shifts absent where the exotic state is not expected: all; Gate leakage checked: no; Map of where in two-gate space the shifts occur: part | "In our case the instability cannot be related to quasiparticles entering and leaving the AD-bulk." (p. 25) | Repeat sweeps like Fig. S13 at the even-denominator fillings, show gate leakage currents from the cooldown, and map ADG against TG at one even-denominator state |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: part | "The device was measured in a Leiden wet dilution refrigerator" (p. 9); a second e/4 dataset at "B = 13.95 T" (Fig. S16, p. 28) | Give device and cooldown counts, and show a second weak-coupling map per even-denominator state |
| Coulomb island in a constriction (not in library) | Tested in part | Location of the oscillating localized state identified: part; Loop area from the field period compared with the antidot size at each filling: part | "∆B1 gives access to the antidot diameter, which we find to be D = 361 ± 30 nm" (p. 4); "This agreement confirms that the ADG oscillations are area oscillations rather than density oscillations." (p. 14) | Compare the area from ∆B with the antidot size at each fractional filling, and compare ADG and side-gate lever arms there |

## Questions about devices and data

1. How many devices did you fabricate and measure (the author contributions mention "the devices"), and how many showed the e/4 period?
2. Why were the others set aside?
3. Which ADG, top-gate, bottom-gate and side-gate ranges, and which fields, did you measure at ν = −5/2, −1/2 and 3/2 beyond the windows in Fig. 2, and did any weak-coupling setting give a normalized period other than about 0.25?
4. What does the second-best minimal-regime map at each even-denominator filling look like, and did you try the developing states at ν = +1/2 and +5/2?
5. What is the sign of the stripe slope in each minimal-regime Vadg versus B map (Fig. 2a-d), and at ν = 2/3, where ∆B1/∆B = 2.32 ± 0.93, what in the data separates the Coulomb-dominated reading from the Aharonov-Bohm value of 1?
6. Did you measure gate leakage during the cooldown, and do repeated sweeps like Fig. S13 at the even-denominator fillings show the hysteresis seen at ν = 2/3?
7. How much do the extracted charges move if the reference is ν = −1 at 14 T or ν = −2 at 10 T, given the stronger fluctuations you report for ν = −1 at 14 T?
8. Could you share the raw maps and the analysis code (background subtraction, choice of the 2D-FFT line, Gaussian fits), so readers can rerun the period extraction?

## Related work

- Halperin, Stern, Neder and Rosenow 2011, "Theory of the Fabry-Perot Quantum Hall Interferometer", <https://arxiv.org/abs/1010.4598>. Shows that the Aharonov-Bohm and Coulomb-dominated regimes give stripes with different spacings and slopes of opposite sign in the B and gate plane, with a superposition at intermediate coupling.
- Kou, Marcus, Pfeiffer and West 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. Uses field and gate periods in GaAs antidots to find Coulomb-type oscillations and a tunneling charge of (2/3)e at ν = 2/3.
- Di Luca et al. 2025, "Quantum Hall Antidot as a Fractional Coulombmeter", <https://arxiv.org/abs/2509.04209>. A gate-defined bilayer graphene antidot in the Coulomb-dominated regime gives e/3 at several fillings and 2e/3 at ν = 2/3 from the gate period and oscillation slope.
- Kim et al. 2024, "Aharonov-Bohm Interference in Even-Denominator Fractional Quantum Hall States", <https://arxiv.org/abs/2412.19886>. Fabry-Perot interferometry in bilayer graphene at even-denominator states shows a two-flux-quantum period, read as e/2 interference or thermally smeared e/4 interference.
- Hackens et al. 2010, "Imaging Coulomb Islands in a Quantum Hall Interferometer", <https://arxiv.org/abs/1010.4494>. Scanning gate microscopy locates Coulomb islands that shape magnetoresistance oscillations in a quantum Hall interferometer.

Happy to rerun this if you share the figure data.
