# Lookalike check: Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper reads a diode as CDW-linked time-reversal symmetry breaking, so I adapted the library's one diode entry and walked only the general practice checks; the library has no diode checks yet.

**The claim, as I read it.** A field-free diode appears in CsV3Sb5 flakes only after oxidation (Device 11, Fig. 2) or asymmetric etching (Devices 13 and 14, Fig. 3, Fig. S7), with a sign and size that vary from sweep to sweep until a 0.1 to 0.2 T out-of-plane field fixes them (Fig. 4). Ten pristine devices (Table S1) and two Ti-doped devices without long-range CDW order (Figs. S13, S14) show none, which you read as CDW-tied time-reversal symmetry breaking domains.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories (Figs. S1 and S2 and Table S1)." (p. 4). The count of treated CsV3Sb5 devices made is missing.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature." (p. 15, Fig. 3). The field values in Fig. 4 are not given.
3. Give the processing steps from raw data to figures, with data and code : Partly. The critical currents "are defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5); the onset threshold isn't stated, and data are on request (p. 9).

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Asymmetric vortex edge barriers and Meissner screening in a small residual field | Partly addressed | "This means that ordinary vortex entry into the superconducting layer is not expected under the in-plane training condition, demonstrating that the field stabilization is not related to the vortex physics." (Supp. p. 13, Fig. S10); the argument covers the in-plane field only. | Measure η against out-of-plane field in fine steps through zero, with the remanent field nulled, on Device 13, one pristine device and etched Ti-doped Device 16, and calibrate the tilt for Fig. S10. |
| Fine-tuning and selection of sweeps and devices | Partly addressed | "During the second oxidation stage, three consecutive measurements were performed, and only the second exhibited a field-free SDE, corresponding to Fig. 2(c) in the main text." (Supp. p. 2) | Show every sweep per device and condition as an η histogram, zero-η sweeps included, and state how many treated devices were made. |
| Trapped magnetic flux or vortices set by field or current history (not in library) | Partly addressed | "The stochastic SDE still persists under this protocol." (Supp. p. 11, Fig. S8); the data bear on it; the paper doesn't discuss it. | Pole at plus and minus 1 T, return to a nulled zero field, and test whether the sign of η follows the poling sign or the previous sweep; warm above Tc between sweeps as a reset. |

## Questions about devices and data

1. How many oxidized or etched CsV3Sb5 devices did you make, and how many showed a field-free diode? The pristine and Ti-doped counts are given (Table S1, Figs. S13, S14).
2. Were any treated CsV3Sb5 devices set aside, and why?
3. Which ranges did you measure beyond the ones shown: total sweeps per condition, the field values in Fig. 4, and were any pristine devices measured at 0.1 to 0.2 T out of plane?
4. What does the second-best dataset look like, for example the other two stage-two sweeps of Device 11 beside the 83.61% sweep in Fig. 2c?
5. How was zero field set and checked after the field sweeps of Fig. 4 and the 1 T field cooling of Figs. S8 and S9, and how was the tilt calibrated for the in-plane fields of Fig. S10? Hou et al. (https://arxiv.org/abs/2205.09276) see a diode below 1 Oe and a false in-plane diode from a 0.01 degree tilt, which at 0.3 T is about 0.5 Oe out of plane.
6. What threshold defines the onset current, given the 10 μA ac excitation in Fig. S3 and critical currents of 17 to 36 μA in Fig. S4, and does η keep its sign if Ic is read at another dV/dI feature?
7. How do Ti-doped Devices 15 and 16 compare with Devices 11 to 14 in thickness, Tc, critical current and etched geometry, and does Device 16 show a diode at 0.1 to 0.2 T?
8. Which devices do Figs. S3 and S4 show? Fig. S3 is captioned "Device 12 (Fig. 2 in the main text)" (Supp. p. 6), though Fig. 2 shows Device 11; Fig. S4 is "Device 13 after successive oxidation stages" (Supp. p. 7), though p. 5 gives its η range to Device 12; and Supp. p. 2 lists "30.86% for sweep #5" where Fig. S4e reads η = -30.86%.

## Related work

- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Diodes in plain Nb and V films at out-of-plane fields below 1 Oe from Meissner screening and asymmetric edges, larger with a serrated edge.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. A zero-field diode whose sign follows a poling field applied beforehand, attributed to trapped flux.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. A zero-field diode in Nb junctions from a trapped vortex plus nonuniform bias, switched on and off by trapping or removing the vortex with short current pulses.
- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. A field-free diode in CsV3Sb5 flakes with polarity modulated by thermal history.
- Ge et al. 2025, "Nonreciprocal superconducting critical currents with normal state field trainability in kagome superconductor CsV3Sb5", <https://arxiv.org/abs/2506.04601>. Zero-field nonreciprocal critical currents in CsV3Sb5 whose polarity varies randomly between cycles to 300 K and follows a field applied above the CDW transition.

Happy to rerun this if you share the sweep-by-sweep data.
