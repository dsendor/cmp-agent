# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library centers on superconducting hybrid devices, so I adapted its
fractional-charge and data-practice entries to a quantum Hall antidot.

**The claim, as I read it.** In one gate-defined bilayer graphene antidot at B = 14 T, the
antidot-gate (ADG) period at weak coupling, normalized to the ν = −1 electron period, is
about 0.25 at ν = −5/2, −1/2 and 3/2 (Fig. 2a,b,d; Fig. 4b), read as addition of localized
e/4 quasiparticles in the Coulomb-dominated regime, with e/3 at ν = 2/3 (Fig. 2c). A
second claim is a crossover to a doubled gate period as the side gates raise the coupling
(Fig. 3), which you leave open between bunching and an Aharonov-Bohm or mixed regime.

## Checks a careful reader will look for

1. Regime map (Aharonov-Bohm or Coulomb-dominated) : Partly. "are consistent with measurements in the CD regime" (p. 4, Fig. 2e–h); temperature and DC bias are not decisive, since "the two models are not strongly distinguishable" (p. 30).
2. Control regime, and traps or leakage ruled out : Partly. ν = −4/3 gives a ratio "in agreement with the value q/e = 1/3 expected for CD antidot oscillations previously reported" (p. 4, Fig. 1g–h); traps and gate leakage during measurement aren't discussed.
3. Repeated sweeps : Partly. "The first 6 repetitions show substantial shifts between successive traces, consistent with significant gate hysteresis at this filling factor." (p. 25, Fig. S13); done at ν = 2/3 only.
4. Device and dataset counts : Not done. The paper describes one device and doesn't say how many were made, measured or set aside.
5. Full parameter ranges : Partly. "with typically NB ≈ 101 points per scan" (p. 10); ranges explored beyond the shown windows, and why each was chosen, aren't given.
6. Processing from raw data to figures : Partly. "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper." (p. 9); data are on request and no code is shared.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Aharonov-Bohm or mixed regime, where the gate period stops tracking the localized charge (adapted from the interferometer entry) | Partly addressed | "are consistent with measurements in the CD regime" (p. 4, Fig. 2e–h); the regime rests on field periods with large errors. | Report the stripe slope sign in each Vadg–B map (Halperin et al.), and add top-gate periods at the e/4 fillings as in Fig. S5. |
| Charge traps or stochastic switching that shift or add periodicities | Partly addressed | "The first 6 repetitions show substantial shifts between successive traces, consistent with significant gate hysteresis at this filling factor." (p. 25, Fig. S13) | Repeat fixed-field ADG sweeps at ν = −5/2, −1/2 and 3/2 and show the spacing histogram per repetition; report gate leakage during the runs. |
| Fine-tuning and selection | Partly addressed | "Within the uncertainty, all three filling factors yield the same gate-voltage period ratio" (p. 4); the data bear on it; the paper doesn't discuss how tunings were chosen. | State devices, cooldowns and tunings tried per filling, and show the second-best map for each. |
| Period extraction set by data choices (window, background, fit) (adapted from the protocol entry) | Partly addressed | "we instead use the uncertainty obtained from the corresponding histogram analysis in order to avoid underestimating the error" (p. 10) | Rerun the 2D-FFT with other background orders, field windows and no moving average, and share data and code. |
| Period halving from several antidot-bound modes, h/2e type (not in library; Kataoka et al., https://arxiv.org/abs/cond-mat/0007383) | Partly addressed | "while its magnetic-field periodicity is consistent with p = 2, corresponding to ϕ0 /2, as expected for two edge states in the CD regime" (p. 15, Fig. S3); tested at ν = −2 only. | Count the antidot-bound modes expected at each filling and compare with the measured p, as Kou et al. do for integer edges. |

## Questions about devices and data

1. How many devices did you fabricate and measure, over how many cooldowns, and how many showed the e/4 gate period at each of ν = −5/2, −1/2 and 3/2?
2. Why were the other devices, cooldowns or tunings set aside, and were there settings at these fillings where the weak-coupling period ratio came out near 1/3 or 1/2?
3. Which ranges of ADG voltage, magnetic field (beyond the roughly 100 mT windows), side-gate voltage and displacement field did you measure beyond the ones shown?
4. What does the second-best dataset at each even-denominator filling look like, and what ΔV/ΔV1 does it give?
5. Could you extract top-gate periods at ν = −5/2, −1/2 and 3/2, as you did at ν = −4/3 in Fig. S5, to give a charge estimate that does not rely on the ADG lever arm?
6. Did you repeat ADG sweeps at fixed field at the e/4 fillings, as in Fig. S13 for ν = 2/3, and is the e/4 period free of hysteresis or switching there?
7. How does the 0.37 ± 0.04 calibration at ν = −4/3 (about 11% above 1/3), and the use of a 10 T reference for 14 T data, enter the separation of e/4 from e/3 at ν = −5/2, where you find 0.27 ± 0.03?
8. On p. 7, does "ν = −2/3" refer to the ν = 2/3 data, and could you release the raw data and the period-extraction code, which are currently available on request?

Question 5 matters most: the slope method is set aside because "In our geometry the ADG mainly controls the AD potential, so this approach is not applicable here" (p. 3), so the charge reading rests on the ADG period ratio. At ν = −5/2 you set the gate-period error by hand to 5.6 mV (Fig. S8, p. 20), and e/3 sits about two standard errors from 0.27.

## Related work

- Di Luca et al. 2025, "Quantum Hall Antidot as a Fractional Coulombmeter", https://arxiv.org/abs/2509.04209. A bilayer graphene antidot in the Coulomb-dominated regime giving e/3 at ν = 4/3, 5/3, 7/3 and 2e/3 at ν = 2/3.
- Kou et al. 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", https://arxiv.org/abs/1201.1600. Identifies the Coulomb regime from how the field period scales with the number of edges bound to the antidot; finds 2e/3 at ν = 2/3.
- Franklin et al. 1995, "The Aharonov-Bohm Effect in the Fractional Quantum Hall Regime", https://arxiv.org/abs/cond-mat/9509116. Antidot resonances at ν = 1/3 consistent with charge e* and also with any charge at or above e*.
- Halperin et al. 2011, "Theory of the Fabry-Perot Quantum Hall Interferometer", https://arxiv.org/abs/1010.4598. Aharonov-Bohm and Coulomb-dominated periodicities give stripes of different spacing and opposite slope in the field and gate plane.
- Kim et al. 2024, "Aharonov-Bohm Interference in Even-Denominator Fractional Quantum Hall States", https://arxiv.org/abs/2412.19886. A bilayer graphene interferometer with a 2Φ0 period at even-denominator states and bulk quasiparticles of charge e/4.

Happy to rerun this if you share the figure data.
