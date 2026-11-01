# Lookalike check: Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper measures critical-current nonreciprocity in flakes, away from the tunneling experiments most entries cover, so I used the library's one diode entry and its practice checks, and added two lookalikes from papers I opened.

**The claim, as I read it.** Encapsulated CsV3Sb5 flakes show no field-free diode (Fig. 1, Table S1); oxidation (Device 11, Fig. 2) or etching (Device 13, Fig. 3) switches one on, with a sign and size that vary by sweep and settle under small out-of-plane fields (Fig. 4). Ti-doped devices without long-range CDW order (Figs. S13, S14) show none, which you read as a CDW-linked time-reversal-breaking domain texture.

## Checks a careful reader will look for

The library has no ordered checks for diode signals, so these are its three practice checks.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories (Figs. S1 and S2 and Table S1)." (p. 4). The counts of oxidized, etched and Ti-doped devices are missing.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature." (Fig. 3 caption, p. 15). Field steps, sweep rates for Devices 11 to 13 and the residual field at nominal zero are missing.
3. Give the processing steps from raw data to figures, with data and code : Partly. The critical currents in Eq. 1 are "defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5); the onset criterion is missing and data are "available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Asymmetric vortex barriers and Meissner screening in an ordinary film | Partly addressed | "This means that ordinary vortex entry into the superconducting layer is not expected under the in-plane training condition, demonstrating that the field stabilization is not related to the vortex physics." (Fig. S10 caption, SI p. 13); this covers the in-plane 0.3 T field only. | Run the etched Ti-doped Device 16 and one pristine device through the same out-of-plane series as Fig. 4, with fine field steps through zero. |
| Fine-tuning and data selection | Partly addressed | "During the second oxidation stage, three consecutive measurements were performed, and only the second exhibited a field-free SDE, corresponding to Fig. 2(c) in the main text." (SI p. 2) | Show every sweep for each oxidized and etched device as eta histograms, in the form of Fig. 3d,e. |
| Trapped vortex or residual magnet field (not in library) | Partly addressed | "The stochastic SDE still persists under this protocol." (Fig. S8 caption, SI p. 11); the data bear on it; the paper doesn't discuss trapped flux or the magnet's residual field. | Measure or null the residual field at nominal zero, then test whether the sign of eta follows the field history; Golod and Krasnov switch a niobium diode's polarity by trapping or removing one vortex. |
| Switching-current statistics in an inhomogeneous film (not in library) | Partly addressed | "Control measurements presented in Fig. S12 further rule out ordinary time-dependent fluctuation near the critical current as the origin of the observed stochasticity." (p. 6) | Plot separate histograms of Ic+ and Ic- from many same-direction sweeps and compare the spread of eta with what independent draws would give; Murphy et al. (<https://arxiv.org/abs/1303.2620>) measure switching currents as distributions. |

On the last two rows: each sweep in Fig. 2 starts at zero and drives the flake normal (Fig. 2 caption, p. 14), so flux can re-trap differently each time, and switching in a multi-peaked film (Fig. 2b) can itself be random. Your Ti-doped devices bear on both, with an upper bound of "approximately 0.1%" (Fig. S14 caption, SI p. 17), most strongly if they match Devices 11 to 14 in thickness, critical current and field history.

## Questions about devices and data

1. How many oxidized, etched and Ti-doped devices did you measure, and how many showed a field-free diode? The pristine count of ten is on p. 4.
2. Why were the others set aside, if any were?
3. Which ranges did you measure beyond the ones shown: more sweeps per condition, field values between those in Fig. 4, and temperatures for Device 14?
4. What does the second-best device look like? Device 14 (Figs. S7 to S11) partly answers this; could you show its eta statistics as in Figs. 3d,e and 4?
5. What is the magnet's residual field at nominal zero after the Fig. 4 series and the 1 T field cooling (Figs. S8, S9), and was it measured?
6. Did you measure Device 16, or a pristine device, at the 0.1 to 0.2 T out-of-plane fields that fix the polarity in Device 13?
7. How is the onset current picked in multi-peak curves such as Fig. 2b, and what excitation and sweep rate were used? Fig. S3 lists "Iac = 10 μA" against a critical current near 37 μA (p. 5).
8. Which device is which? Page 5 gives eta from −30.86% to 17.07% for Device 12, Fig. S3 calls Device 12 "Fig. 2 in the main text" (Device 11 on p. 5), and Fig. S4 gives those values for "Device 13 after successive oxidation stages".

## Related work

- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. Reports a field-free diode in intrinsic CsV3Sb5 flakes with polarity modulated by thermal history.
- Ge et al. 2025, "Nonreciprocal superconducting critical currents with normal state field trainability in kagome superconductor CsV3Sb5", <https://arxiv.org/abs/2506.04601>. Reports a zero-field critical-current asymmetry with random polarity after thermal cycling, set by a perpendicular field applied above the CDW transition.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. Reports a zero-field diode and second-harmonic signals that appear as CsV3Sb5 flakes get thinner.
- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Shows diodes in plain niobium and vanadium films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Shows zero-field niobium junction diodes whose polarity switches as an Abrikosov vortex is trapped or removed.

Happy to rerun this if you share the sweep-by-sweep critical currents.
