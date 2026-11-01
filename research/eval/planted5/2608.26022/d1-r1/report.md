# Lookalike check: Field-free superconducting diode in CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. I applied the library's diode entry, written for exotic pairing, to your
CDW-linked reading, working from the text and captions only.

**The claim, as I read it.** Encapsulated CsV3Sb5 devices show equal |Ic+| and |Ic−| at
zero field (Fig. 1, Figs. S1 and S2, Table S1), while oxidized (Devices 11 and 12) and
etched (Devices 13 and 14) devices show a field-free diode whose sign and size change from
sweep to sweep (Figs. 2 and 3, Figs. S3 to S7). Fields of 0.1 to 0.2 T
stabilize it (Fig. 4, Figs. S10, S11); Ti-doped devices with suppressed CDW show none
(Figs. S13, S14). You read this as time-reversal-breaking domains linked to the CDW.

## Checks a careful reader will look for

The library has no diode checks yet, so these are the practice checks.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories" (p. 4); processed-device totals are not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature." (Fig. 3, p. 15); field steps, total sweeps and reasons for ranges are not given.
3. Give the processing steps from raw data to figures, with data and code : Partly. Eq. 1 uses currents "defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5); no onset criterion, and data are "available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Asymmetric vortex barriers and Meissner screening in an ordinary film, driven by a small residual field (diode-vortex-screening) | Tested in part | Plain film of the parent superconductor: part (Ti-doped Devices 15 and 16, one per route; geometry and Ic not compared with Devices 12 and 13); field, width or edge quality: part (field in Fig. 4 and Figs. S10, S11; oxidation steps in Fig. 2; no Oe-scale steps near zero) | "These observations are difficult to reconcile with a single fixed structural diode axis or with a static fabrication artifact." (p. 6) | Measure the residual field at the sample after the 1 T and 0.2 to 0.3 T ramps, then step through zero in Oe-scale steps on Device 13 or 14; put Device 16's geometry and Ic beside Device 13's. |
| Non-representative example chosen after tuning (fine-tuning-and-selection) | Tested in part | Devices and datasets counted: part (pristine counted, processed not); how shown data were chosen: no; second device shown: all (Devices 12 and 14) | "The effect is reproducible across devices, including a second etched sample (Device 14; Fig. S7)" (p. 5) | State how many oxidized or etched CsV3Sb5 devices you made and how the Fig. 2c sweep was picked; show every zero-field sweep per device. |
| Trapped Abrikosov vortex plus self-field from nonuniform bias (not in library) | Tested in part | Vortex trapped and removed: part (field cooling, Device 14 only); bias configuration changed: no | "it is not eliminated by field-cooling followed by removal of the external field (Figs. S8 and S9)" (pp. 5 to 6) | From existing sweeps, test whether each polarity follows the sign of the previous excursion into the normal state; warm above Tc in zero field between sweeps; swap current leads. |
| Stochastic switching from thermal or quantum fluctuations (not in library) | Tested in part | Ic+ and Ic− magnitude distributions with signed mean η: part (η spreads from six or nine sweeps, Figs. 3 and 4); sweep rate and temperature: part (temperature only); fixed-bias time traces: part (Device 14, Fig. S12) | "Control measurements presented in Fig. S12 further rule out ordinary time-dependent fluctuation near the critical current as the origin of the observed stochasticity." (p. 6) | From existing sweeps, give the signed mean η with its standard error at zero field and separate histograms of the two critical-current magnitudes; repeat at two or three sweep rates on Device 14. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the effect? Your p. 4 and Table S1 answer this for the ten encapsulated devices; for oxidized or etched CsV3Sb5, Devices 11 to 14 appear, and I couldn't find how many were made in total or whether any stayed symmetric.
2. Why were the others set aside? The numbering runs from Device 1 to Device 16; is that every device you made, and were any lost or excluded?
3. Which ranges of field, temperature and sweep count did you measure beyond the ones shown, for example the field step in Fig. 4 and the total number of zero-field sweeps per device?
4. What does the second-best device or dataset look like? Devices 12 and 14 are in the supplement; what do repeated sweeps of Device 11 at the second oxidation step look like, and how was the sweep with η = 83.61% (Fig. 2c) chosen?
5. What is the residual field at the sample at nominal zero field, after the ramps to 1 T (Figs. S8 and S9) and to 0.2 to 0.3 T (Fig. 4, Figs. S10 and S11), and was it measured or compensated?
6. At zero field, what are the signed mean η and its standard error for Devices 12, 13 and 14, do the |Ic+| and |Ic−| distributions differ, and does a sweep's polarity follow the sign of the sweep before it?
7. Were repeated sweeps taken on the pristine devices, and on Devices 13 and 14 before etching, at the temperatures of Fig. 3, and how do the geometry, critical current and number of sweeps of Ti-doped Devices 15 and 16 compare with Devices 12 and 13?
8. Which device does each supplementary figure show, and how was the onset current defined in the multi-peak traces? Fig. S3 calls Device 12 "Fig. 2 in the main text" while Fig. 2 shows Device 11, Fig. S4 is labelled Device 13 "after successive oxidation stages" yet appears to carry the −30.86% and 17.07% values p. 5 gives for Device 12, and Table S1 lists Devices 2 to 10.

## Related work

- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. Field-free diode in CsV3Sb5 flakes, polarity changing with thermal history.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. Zero-field diode that emerges as CsV3Sb5 flakes are thinned.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Diode effects in plain Nb and V films at fields near 1 Oe, from vortex barriers and Meissner screening.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Zero-field diode in Nb junctions from a trapped vortex and nonuniform bias; trapping or removing the vortex switches it.
- Vedin and Lidmar 2024, "Switching current distributions in superconducting nanostrips", <https://arxiv.org/abs/2406.19024>. Fluctuations make the switching current random, with a distribution set by sweep rate, temperature and geometry.

Happy to rerun this if you share the sweep-by-sweep critical currents.
