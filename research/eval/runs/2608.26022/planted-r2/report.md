# Lookalike check: Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library has no diode-specific checks yet, so the checks below are the general reporting ones.

**The claim, as I read it.** A field-free superconducting diode appears in CsV3Sb5 flakes only after oxidation (Device 11, Fig. 2; Device 12, Figs. S3 to S5) or asymmetric etching (Devices 13 and 14, Fig. 3, Fig. S7), with a polarity and size that change from sweep to sweep until a small out-of-plane field fixes them (Fig. 4). It is absent in ten pristine encapsulated devices (Fig. 1, Table S1) and in two processed Ti-doped devices without long-range CDW order (Figs. S13, S14), which you read as CDW-derived time-reversal breaking.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories" (p. 4) counts the baseline; for processed flakes I couldn't find how many were made, how many cooldowns there were, or whether any showed no diode.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature" (Fig. 3 caption, p. 15); the field step in Fig. 4, the total zero-field sweeps per device, and which sweep Fig. 2c shows are not stated.
3. Give the processing steps from raw data to figures, with data and code : Partly. Critical currents are "defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5), with no onset threshold given, and data are "available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Asymmetric vortex edge barriers and Meissner screening current in a small residual field | Partly addressed | "the Ti-doped samples do not show a field-free superconducting diode effect" (p. 6, Figs. S13, S14); the paper doesn't discuss this mechanism or the residual field at nominal zero. | Report the residual field at the sample and sweep B through zero in steps of about 1 Oe; run the Fig. 4 field series on etched Ti-doped Device 16 for comparison. |
| Fine-tuning and selection of the shown sweeps and devices | Partly addressed | "consecutive current sweeps at the same temperature and nominally identical conditions produce different diode efficiencies" (p. 5, Fig. 3); counts of processed devices and total sweeps are missing. | Show every zero-field sweep per device as a histogram of η, and list all oxidized or etched devices, including any with no diode. |
| Trapped Abrikosov vortex plus self-field from nonuniform bias (not in library; Golod and Krasnov 2022, https://arxiv.org/abs/2205.12196) | Partly addressed | "it is not eliminated by field-cooling followed by removal of the external field" (p. 5, Figs. S8, S9); the data bear on it; the paper doesn't discuss it. | Swap the current leads, and stop sweeps just above the critical current so the flake doesn't go fully normal each time; see whether the polarity statistics change. |

## Questions about devices and data

1. How many oxidized or etched CsV3Sb5 devices did you measure, and how many showed a field-free diode? (The ten pristine devices are counted on p. 4.)
2. Why were any others set aside?
3. Which temperatures, fields and sweep counts did you measure beyond the ones shown, including the total zero-field sweeps per device and the field step in Fig. 4?
4. What does the second-best device or dataset look like, for example the other sweeps at the oxidation step where Fig. 2c gives η = 83.61%?
5. What is the residual field at the sample at nominal B = 0 in each cryostat, after the 1 T field-cooling (Figs. S8, S9) and the ±0.2 T series (Fig. 4), and was the magnet reset? Each sweep well past the critical current drives the flake normal, so flux trapped on re-entry could differ between sweeps.
6. How do Ti-doped Devices 15 and 16 compare with Devices 11 to 14 in Tc, critical current, multi-peak dV/dI after processing, measurement temperature and sweep count?
7. What threshold defines the onset current, and how does the 10 μA ac excitation in Fig. S3 compare with critical currents of about 17 to 37 μA (Fig. 2b, Fig. S4)?
8. Which device is in Fig. 2 and in Fig. S4? The main text names Device 11 for Fig. 2 and Device 12 for the −30.86% to 17.07% sweeps, while the captions read "Device 12 (Fig. 2 in the main text)" (Fig. S3) and "Device 13 after successive oxidation stages" (Fig. S4).

## Related work

- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A strong diode in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. A zero-field diode in conventional Nb junctions from bias self-field plus a trapped vortex, with polarity set by bias configuration and vortex trapping.
- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. A field-free diode in intrinsic CsV3Sb5 flakes, with polarity modulated by thermal history.
- Ge et al. 2025, "Nonreciprocal superconducting critical currents with normal state field trainability in kagome superconductor CsV3Sb5", <https://arxiv.org/abs/2506.04601>. A zero-field asymmetry whose polarity changes randomly with thermal cycling and follows a field applied above the CDW transition.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. A zero-field diode that emerges as CsV3Sb5 flakes get thinner.

Happy to rerun this if you share the raw sweeps and a residual-field calibration.
