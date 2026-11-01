# Lookalike check: Field-free superconducting diode in CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

Title on the arXiv abstract page: "Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV$_3$Sb$_5$".

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your signal is a field-free diode read as internal time-reversal-breaking order, which sits next to the library's topological signals, so I adapted its one diode entry (written for finite-momentum or exotic pairing) and its practice checks to your claim.

**The claim, as I read it.** In CsV3Sb5 flakes whose inversion symmetry is broken by oxidation (Devices 11 and 12; Fig. 2, Figs. S3 to S5) or by asymmetric etching (Devices 13 and 14; Fig. 3, Figs. S6, S7), the critical current differs between the two directions at zero applied field. The sign and size change from sweep to sweep, and an out-of-plane field of 0.1 to 0.2 T stabilizes them (Fig. 4, Figs. S10, S11). Ten encapsulated pristine devices (Figs. S1, S2, Table S1) and two processed Ti-doped devices (Figs. S13, S14) show no diode, which you read as tying the time-reversal breaking to CDW-related order.

## Checks a careful reader will look for

The library holds no ordered checks for diode signals yet, so these are its practice checks, which apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories" (p. 4); four diode-active devices are shown, and the number of oxidized or etched CsV3Sb5 devices made, and of cooldowns, is not stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature." (Fig. 3 caption, p. 15); the total number of zero-field sweeps per device, the sweep rates for Devices 11 to 13, and fields between 0 and 0.1 T are not given.
3. Give the processing steps from raw data to figures, with data and code : Partly. The critical currents are "defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5); how the onset is picked in multi-peak curves is not stated, and the data are "available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Asymmetric vortex barriers and Meissner screening in a small residual field (Hou et al., https://arxiv.org/abs/2205.09276) | Partly addressed | "the Ti-doped samples do not show a field-free superconducting diode effect" (p. 6); the data bear on it; the paper doesn't discuss it. | Step B through zero in about 1 Oe steps on Device 13 or 14, find where the mean η crosses zero, and report the magnet's residual field at "B = 0". |
| Non-representative example after fine-tuning and selection | Partly addressed | "including a second etched sample (Device 14; Fig. S7)" (p. 5); total processed devices and sweeps are not given. | Report every processed device and every zero-field sweep, and show the η distribution behind the 83.61% of Fig. 2c. |
| Trapped magnetic flux or vortices set the zero-field diode (not in library; Jiang et al., https://arxiv.org/abs/2512.05427) | Partly addressed | "The stochastic SDE still persists under this protocol." (Fig. S8, SM p. 11); the data bear on it; the paper doesn't discuss trapped flux. | Field-cool at +1 T and at −1 T and compare zero-field signs, as Jiang et al. do with a poling field; repeat with sweeps that stop just above Ic, or with a warm-up above Tc between sweeps. |
| Stochastic phase-slip switching makes η random (not in library; Sahu et al., https://arxiv.org/abs/0804.2251) | Partly addressed | "Control measurements presented in Fig. S12 further rule out ordinary time-dependent fluctuation near the critical current as the origin of the observed stochasticity." (p. 6); shown for Device 14, two sweeps. | Plot the |Ic+| and |Ic−| switching histograms separately for each zero-field set, with their temperature dependence, and give the mean signed η with its standard error. |

## Questions about devices and data

1. How many oxidized or etched CsV3Sb5 devices did you make, and how many showed a diode? You list ten pristine devices (Table S1), four diode-active ones (Devices 11 to 14) and two Ti-doped ones (Devices 15 and 16); the total processed count and the number of cooldowns would complete the picture.
2. Why were any others set aside, and why is Device 1, the device of Fig. 1, absent from Table S1?
3. Which ranges did you measure beyond those shown: how many zero-field sweeps per device in total, which sweep rates for Devices 11 to 13, temperatures above 1.5 K for Device 13, and fields between 0 and 0.1 T?
4. What does the second-best dataset look like, for example the zero-field η distribution of Device 14 with as many sweeps as Fig. 3, and of Devices 11 and 12 at each oxidation step? Fig. S3's caption calls Device 12 "Fig. 2 in the main text", which shows Device 11, and Fig. S4 is titled Device 13 while carrying the Device 12 values quoted on p. 5; which device is in each figure?
5. What is the residual field at the sample when the magnet reads zero, in the PPMS and in the Triton, and was the magnet reset before the zero-field sweeps? When you step the field through zero in fine steps, where does the mean η cross zero?
6. Each sweep in Fig. 2 runs to ±300 μA, far above Ic. Does the η distribution change if sweeps stop just above Ic, or if you warm above Tc between sweeps, and does field-cooling at +1 T and at −1 T (Fig. S8) give opposite zero-field signs?
7. For Fig. 3d,e and Fig. 4, what is the mean signed η at zero field with its standard error, and what do the |Ic+| and |Ic−| histograms look like separately? How is the onset picked when dV/dI has several peaks, and how does the 10 μA ac excitation labeled in Fig. S3 compare with the 16.8 to 36 μA critical currents in Fig. S4?
8. For the Ti-doped Devices 15 and 16, what are the thickness, Tc and Ic, how many sweeps went into Figs. S13 and S14, and did oxidation produce the same multi-peak transition as in Device 11?

Questions 5 and 6 bear on the two field-related lookalikes: your Ti-doped control (Figs. S13, S14) already speaks to them, and a fine field sweep through zero plus a two-sign field-cooling run on Device 13 or 14 would let a reader see it directly. Question 7 bears on stochastic switching: your Fig. 3d,e and Fig. 4 data likely already hold the separate |Ic+| and |Ic−| histograms.

## Related work

- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. Reports a field-free diode in intrinsic CsV3Sb5 flakes, with polarity modulated by thermal history.
- Ge et al. 2025, "Nonreciprocal superconducting critical currents with normal state field trainability in kagome superconductor CsV3Sb5", <https://arxiv.org/abs/2506.04601>. Zero-field critical-current asymmetry in CsV3Sb5 whose polarity changes randomly on thermal cycling to 300 K and follows a perpendicular field applied above the CDW transition.
- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Strong diode in plain Nb and V films at fields as small as 1 Oe, traced to asymmetric vortex edge or surface barriers and Meissner screening.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Zero-field diode in conventional Nb junctions from self-field and a trapped Abrikosov vortex, with polarity switched by trapping or removing the vortex.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi$_2$", <https://arxiv.org/abs/2512.05427>. Zero-field diode whose sign is set by a poling field applied before the measurement, attributed to trapped flux.

Happy to rerun this if you share the sweep-by-sweep critical currents.
