# Lookalike check: Trapping e/4 quasiparticles in bilayer graphene (arXiv 2608.27444v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your signal is a gate-period ratio in a quantum Hall antidot, so I adapted the library's fractional-charge entries to period ratios and added two antidot lookalikes the library lacks.

**The claim, as I read it.** In one bilayer graphene antidot near 14 T, the air-bridge gate period at ν = −5/2, −1/2 and 3/2 is about a quarter of the single-electron period at ν = −1 and 10 T (ΔV/ΔV1 = 0.27, 0.24, 0.25; Fig. 2, p. 4), read as e/4 added per resonance in the Coulomb-dominated (CD) regime; ν = 2/3 gives e/3. A second result is a crossover to a doubled gate period at stronger antidot-edge coupling (Fig. 3), left open between bunching and an Aharonov-Bohm (AB) or mixed regime.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Partly. Every state has a B versus Vadg map (Fig. 2a–d, 3l–o), but the temperature fits "cannot therefore identify the transport regime" (p. 30), and the stripe slope sign isn't reported.
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. At ν = −4/3 the same analysis gives "∆V /∆V1 = 0.37 ± 0.04, in agreement with the value q/e = 1/3" (p. 4); charge traps and leakage aren't discussed.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. Done at ν = 2/3 only: "Raw data from 20 consecutive repetitions of the same measurement" (p. 25, Fig. S13).
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. "The device was measured in a Leiden wet dilution refrigerator" (p. 9); no device, cooldown or dataset counts.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The white circles indicate the regions where we have measured the oscillations." (p. 3, Fig. 1d). The Fig. 2 windows (35 to 100 mT, a different Vadg range per state) aren't explained.
6. Give the processing steps from raw data to figures, with data and code : Partly. Methods C gives each step, and data are "available from the corresponding author upon reasonable request" (p. 10); no code is linked.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| AB or mixed regime, where the gate period stops measuring charge (adapted from the CD-versus-AB interferometer entry) | Partly addressed | "are consistent with measurements in the CD regime" (p. 4, Fig. 2e–h) | Report the stripe slope sign in Fig. 2a–d next to the ν = −1 and −4/3 maps of Fig. 1e–f; add finer low-temperature steps for the e/4 series. |
| Charge trap or side dot coupled to the antidot | Partly addressed | "consistent with significant gate hysteresis at this filling factor" (p. 25, Fig. S13, ν = 2/3 only) | Repeat fixed-field sweeps at ν = −5/2, −1/2 and 3/2 as in Fig. S13; check the Fig. 2 stripes for jumps; report ADG leakage. |
| Fine-tuning and selection of the shown example | Partly addressed | "Both the raw and background-subtracted data are shown in the Supp. Material for all data included in the paper." (p. 9) | Give device and cooldown counts, list the gate, side-gate and field windows tried at each half filling, and show the second-best e/4 dataset. |
| Filling- or gate-dependent antidot area and lever arm (not in library; Hata et al., https://arxiv.org/abs/2412.11401) | Partly addressed | "This agreement provides an independent check that the reference periods determined at 10 T can be applied to the 14 T measurements." (p. 15) | Measure an integer reference period at 14 T inside each Vadg window of Fig. 2, at the same BG and TG; carry a lever-arm term into ΔV/ΔV1, as you do (8%) for ΔB1/ΔB. |
| Two charged edges bound to the antidot that resonate in turn and shorten the apparent period (not in library; Kataoka et al., https://arxiv.org/abs/cond-mat/0007383) | Partly addressed: the data bear on it; the paper doesn't discuss it | "these periods correspond approximately to p = 10, 2, and 6 quasiparticles transferred per flux quantum" (p. 4) | State how many edges are bound at each half filling and check that count against p, as Kou et al. do; look for alternating peak heights in the Fig. 2 line cuts. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the e/4 period? The author contributions say "M.D.L. fabricated the devices".
2. Why were the others set aside?
3. Which ranges of ADG voltage, field and side-gate voltage did you measure at the half fillings beyond the Fig. 2 windows, and did you try ν = +1/2 and +5/2?
4. What does the second-best e/4 dataset look like?
5. The ν = −1 reference (Fig. 1e) spans Vadg = 0 to 2.6 V at 10 T, while ν = −5/2 and −1/2 sit near Vadg = −3 V at 14 T. Is the single-electron ADG period the same at those gate settings?
6. In the Fig. 2 maps, do the stripes slope the same way as in the CD reference maps of Fig. 1e–f?
7. At the half fillings, did repeated fixed-field sweeps show the hysteresis seen at ν = 2/3 (Fig. S13), and what is the ADG leakage?
8. How many edges are bound to the antidot at each half filling, and how do p ≈ 10, 2 and 6 (p. 4) follow from that count?

## Related work

- Halperin, Stern, Neder and Rosenow 2011, "Theory of the Fabry-Perot Quantum Hall Interferometer", <https://arxiv.org/abs/1010.4598>. AB and CD regimes give stripes in the field and gate plane with different spacings and opposite slopes.
- Kou, Marcus, Pfeiffer and West 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. Field and gate periods together give the tunneling charge and the number of charged edges; 2e/3 and one edge at ν = 2/3.
- Kataoka et al. 2000, "Coulomb blockade of tunnelling through compressible rings formed around an antidot: an explanation for h/2e Aharonov-Bohm oscillations", <https://arxiv.org/abs/cond-mat/0007383>. With two bound spin states, resonances through the outer states occur twice per h/e period.
- Hata et al. 2024, "Coulomb oscillations of a quantum antidot formed by an airbridged pillar gate in the integer and fractional quantum Hall regime", <https://arxiv.org/abs/2412.11401>. An air-bridged antidot whose area at ν = 2/3 is significantly smaller than at ν = 2 and 1; its charge estimate assumes a constant gate capacitance.
- Kim et al. 2024, "Aharonov-Bohm Interference in Even-Denominator Fractional Quantum Hall States", <https://arxiv.org/abs/2412.19886>. A bilayer graphene interferometer shows a 2Φ0 period at two half-filled states, with e/4 bulk quasiparticles inferred from filling deviations.

Happy to rerun this if you share the figure data.
