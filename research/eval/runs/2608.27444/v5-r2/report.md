# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper measures fractional charge with a quantum Hall antidot, so I used the
library's fractional-charge entries and adapted the one written for Fabry-Perot
interferometers to your antidot.

**The claim, as I read it.** Your Fig. 2a, b and d show antidot oscillations against
the air-bridge gate and field at ν = −5/2, −1/2 and 3/2 near 14 T in one device, with gate
periods 0.27, 0.24 and 0.25 of the ν = −1 reference, read as e/4 added per resonance in
the Coulomb-dominated regime; Fig. 2c gives e/3 at ν = 2/3. Fig. 3 adds a doubled gate
period at stronger antidot-edge coupling, with two explanations left open.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Done. Fig. 2a to d are field and gate maps for all four states, and the field periods "are consistent with measurements in the CD regime" (p. 4).
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. The integer and odd-denominator controls are there ("the ν = −2 gate-voltage periodicity is consistent with electron charge", p. 15; Fig. 4b), and traps and leakage at base temperature aren't discussed.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. Done at ν = 2/3 only: "Raw data from 20 consecutive repetitions of the same measurement" (Fig. S13, p. 25).
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. One device is implied ("The device was measured in a Leiden wet dilution refrigerator", p. 9); cooldowns and datasets per state aren't given.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The white circles indicate the regions where we have measured the oscillations." (Fig. 1d, p. 3); the gate and field ranges explored beyond the maps aren't stated.
6. Give the processing steps from raw data to figures, with data and code : Partly. "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper." (p. 9); data come on request (p. 10) and no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Aharonov-Bohm or mixed regime, where the gate period no longer gives the charge (adapted from the interferometer entry) | Tested in part | Field and gate map with stripe slope and spacing: all (field period compared with the AB value of one flux quantum; the slope method is not usable here, p. 3); Regime and charging parameters reported: part (regime stated, temperature fits inconclusive, p. 30) | "are consistent with measurements in the CD regime" (p. 4, Fig. 2e to h) | Report the charging energy and level spacing from the DC-bias maps (Fig. S8c to S11c) in the minimal regime, and set each state's two periods against the AB and CD entries of Fig. S18. |
| Integer charge moving in a capacitively coupled trap or side region | Tested in part | Shifts absent where the exotic state is not expected: all; Gate leakage checked: no; Map of where in two-gate space the shifts occur: part (side-gate series for ν = −1/2 and 3/2 only, Fig. 3d to k) | "e/4 at the even-denominator filling factors ν = −5/2, −1/2 and 3/2, and e/3 at the odd-denominator and hole-conjugate FQH states" (p. 6, Fig. 4b) | Repeat fixed-field gate sweeps at the three e/4 fillings as in Fig. S13, and show an antidot-gate versus top-gate map at ν = −5/2 to look for a second family of charging lines. |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: part (second tunings in Fig. 3 and temperature series in Fig. S16, one device) | "We therefore use ν = −1 at 10 T as the integer reference." (p. 15) | State device and cooldown counts, list every setting where you looked for the e/4 period, and show a second full map per state. |

On the first row: a field period far from one flux quantum argues against the pure
Aharonov-Bohm limit, and on its own it leaves a mixed regime open, which you raise
yourself for Fig. 3: "We cannot, however, exclude a second interpretation in which the
system crosses over away from the CD regime toward an AB-dominated or mixed transport
regime." (p. 7). A charging energy from your DC-bias maps would be the most direct addition.

## Questions about devices and data

1. How many devices did you measure, and how many showed the e/4 gate period? Is the device in Fig. 1b the one measured, and over how many cooldowns?
2. If other devices or cooldowns were measured, why were they set aside?
3. Which ranges of antidot gate, side gate, displacement field and magnetic field did you measure beyond the ones shown, and did you look at the "developing states at ν = +1/2 and +5/2" (p. 2)?
4. What does the second-best dataset look like at each even-denominator filling, for example a second map at ν = −5/2, where the oscillations are weakest (Fig. S8)?
5. What are the ratios ∆V/∆V1 at ν = −5/2, −1/2 and 3/2 when you normalize to ν = −1 at 14 T, the field of the fractional data (Fig. S3)?
6. Your text gives "p = 10, 2, and 6" (p. 4), while Fig. 4a seems to show about 7, 3 and 7.5. How were the text values obtained, and how many field periods does each map hold at the 1 mT step (Fig. 2a spans about 35 mT)?
7. Did you repeat fixed-field gate sweeps at the three even-denominator fillings, as at ν = 2/3 (Fig. S13), and measure gate leakage at base temperature?
8. Can you extract a charging energy and a level spacing from the DC-bias maps (Fig. S8c to S11c) in the minimal regime, and say what in them places the e/4 oscillations in the Coulomb-dominated regime?

## Related work

- Di Luca et al. 2025, "Quantum Hall Antidot as a Fractional Coulombmeter", <https://arxiv.org/abs/2509.04209>. A bilayer graphene antidot in the Coulomb-dominated regime gives e/3 at ν = 4/3, 5/3 and 7/3 and 2e/3 at ν = 2/3 from gate period and slope.
- Di Luca et al. 2025, "Tunable inter-edge interactions in a bilayer graphene quantum Hall antidot", <https://arxiv.org/abs/2504.16750>. At ν = 2 and 4, stronger antidot-edge coupling doubles the gate period and moves the field period to φ0, read as a crossover to the Aharonov-Bohm regime.
- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. GaAs antidots where field and gate periods together fix regime and charge: e at ν = 2, 2e/3 at ν = 2/3.
- Kim et al. 2024, "Aharonov-Bohm Interference in Even-Denominator Fractional Quantum Hall States", <https://arxiv.org/abs/2412.19886>. A bilayer graphene interferometer at half filling shows a 2Φ0 period, while added bulk quasiparticles carry e/4.
- Halperin et al. 2011, "Theory of the Fabry-Perot Quantum Hall Interferometer", <https://arxiv.org/abs/1010.4598>. Bulk-edge coupling sets Aharonov-Bohm, Coulomb-dominated or mixed periodicities, told apart by stripe spacing and slope.

Happy to rerun this if you share the figure data.
