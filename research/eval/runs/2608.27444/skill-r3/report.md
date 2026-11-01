# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your experiment is quantum Hall antidot charge spectroscopy, so I adapted the
library's Fabry-Perot interferometer entry (Coulomb-dominated versus Aharonov-Bohm
oscillations) to an antidot.

**The claim, as I read it.** In one bilayer graphene antidot, the air-bridge gate (ADG)
period normalized to the ν = −1 electron period is about 0.25 at ν = −5/2, −1/2 and 3/2
(Fig. 2, p. 4), read as localized e/4 charge in the Coulomb-dominated (CD) regime, with
e/3 at ν = 2/3. The side-gate crossover to a doubled period (Fig. 3) is secondary.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Partly. Every state is mapped and called CD from its periods; the slope method is set aside ("In our geometry the ADG mainly controls the AD potential, so this approach is not applicable here", p. 3) and the temperature fits "cannot therefore identify the transport regime" (p. 30).
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. Integer and odd-denominator states give the expected periods ("∆V /∆V1 = 0.37 ± 0.04, in agreement with the value q/e = 1/3", p. 4; Figs. S3 to S7); gates were checked for shorts at fabrication (p. 9); charge traps are not discussed.
3. Repeat sweeps to separate reproducible periods from stochastic charge jumps : Partly. At ν = 2/3 only: "repeated the same sweep multiple times" (p. 25, Fig. S13).
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The device was measured in a Leiden wet dilution refrigerator" (p. 9); devices fabricated and cooldowns are not given.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The white circles indicate the regions where we have measured the oscillations." (Fig. 1d, p. 3); gate ranges explored beyond the figures are not given.
6. Give the processing steps from raw data to figures, with data and code : Partly. Methods C gives each step and raw maps are shown (p. 9); data are "available from the corresponding author upon reasonable request" (p. 10), with no code linked.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Aharonov-Bohm or mixed regime, where the gate period does not read the localized charge (library: Coulomb-dominated interferometer, adapted to an antidot) | Partly addressed | "are consistent with measurements in the CD regime" (p. 4, Fig. 2e to h); the regime rests on the period values, since the temperature and dc-bias data are inconclusive by your account (p. 8, p. 30). | A short B against top-gate map at each even-denominator filling, as in Fig. S5 for ν = −4/3, to read the stripe slope sign and get a charge estimate that does not use the ADG lever arm. |
| Charge trap or side dot coupled to the antidot | Partly addressed | "The first 6 repetitions show substantial shifts between successive traces, consistent with significant gate hysteresis at this filling factor." (Fig. S13, p. 25); the data bear on it at ν = 2/3, and the paper doesn't discuss traps at the e/4 fillings. | Repeated fixed-field ADG sweeps with spacing histograms at ν = −5/2, −1/2 and 3/2, and the full 2D-FFTs with any secondary peaks marked. |
| Fine-tuning and selection | Partly addressed | "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper." (p. 9); one device, with the tuning history and other settings not described. | State the devices, cooldowns and gate tunings tried, and show the second-best e/4 map per filling. |

## Questions about devices and data

1. How many devices did you fabricate and measure, over how many cooldowns, and how many showed the e/4 period?
2. If other devices or cooldowns were measured, why were they set aside?
3. Which gate, side-gate, displacement-field and magnetic-field ranges did you measure beyond the ones shown? Did you look for oscillations at ν = +1/2 and +5/2?
4. What does the second-best e/4 dataset look like at each even-denominator filling?
5. Besides the period values, what places the e/4 oscillations in the CD regime? Your numbers give ∆B1/∆B near 6.8, 3.1 and 7.6 for ν = −5/2, −1/2 and 3/2; how did you assign p ≈ 10, 2 and 6?
6. ∆V1 comes from ν = −1 at 10 T. How much could the ADG lever arm change between that reference and the 14 T states, and should the 8% area allowance used for ∆B1/∆B also enter ∆V/∆V1?
7. Did you repeat fixed-field sweeps at the e/4 fillings, and do their 2D-FFTs show secondary peaks besides the line you select?
8. At ν = −1/2 in the doubled regime the field window holds less than one period (Fig. S9); did you measure a wider range there?

## Related work

- Halperin, Stern, Neder and Rosenow 2011, "Theory of the Fabry-Perot Quantum Hall Interferometer", <https://arxiv.org/abs/1010.4598>. AB and CD oscillations give stripes in the field and gate plane with different spacings and opposite slopes.
- Levy Schreier, Stern and Rosenow 2015, "Thermodynamic properties of a quantum Hall anti-dot interferometer", <https://arxiv.org/abs/1510.05241>. Antidot interferometers also feel Coulomb coupling between edges, and reach the AB regime more easily than dots.
- Kou, Marcus, Pfeiffer and West 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. Coulomb-type antidot oscillations, identified from field-period scaling, with a (2/3)e tunneling charge at ν = 2/3.
- Kim et al. 2024, "Aharonov-Bohm Interference in Even-Denominator Fractional Quantum Hall States", <https://arxiv.org/abs/2412.19886>. Bilayer graphene interferometers at even-denominator states show a two-flux-quantum period, while added bulk quasiparticles carry e/4.
- Werkmeister et al. 2024, "Anyon braiding and telegraph noise in a graphene interferometer", <https://arxiv.org/abs/2403.18983>. Random telegraph noise traced to fluctuations in localized quasiparticle number.

Happy to rerun this if you share the figure data. Two labels to check: p. 6 cites Fig. 3d,e for ν = 2/3, where the caption has ν = −1/2, and p. 7 mentions ν = −2/3.
