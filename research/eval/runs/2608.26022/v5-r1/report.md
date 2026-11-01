# Lookalike check: Field-free diode in CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

Paper: "Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV$_3$Sb$_5$", Liu et al., https://arxiv.org/abs/2608.26022v1

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first.

**The claim, as I read it.** Pristine hBN-covered CsV3Sb5 flakes show no field-free diode (Fig. 1, Figs. S1 and S2). Oxidized or etched flakes (Devices 11 to 14) show a zero-field diode whose sign and size change from sweep to sweep (Figs. 2 and 3). A small out-of-plane field fixes the polarity (Fig. 4). Ti-doped flakes processed the same way show none (Figs. S13 and S14). You read this as CDW-linked time-reversal-breaking domains coupling to an extrinsic polar axis.

## Checks a careful reader will look for

The library has no ordered checks for the diode family, so these are the practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories" (p. 4). The total number of oxidized or etched CsV3Sb5 devices, and whether any of them stayed diode-free, isn't given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature" (Fig. 3 caption, p. 15). The field grid near zero, the temperature of Fig. 4 and the temperature of the Ti-doped controls aren't stated.
3. Give the processing steps from raw data to figures, with data and code : Partly. Your p. 5 says the critical currents are "defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps". The onset criterion isn't given, and the data are "available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Vortex edge barriers and Meissner screening in a small residual field (`diode-vortex-screening`) | Tested in part | Same measurement on a plain film or junction of the parent superconductor: part (the Ti-doped Devices 15 and 16 went through the same processing, one device per route, with a lower Tc); Effect followed against field, sample width or edge quality: part (five out-of-plane fields in 0.1 T steps on Device 13, and Device 14 in Figs. S10 and S11) | "demonstrating that the field stabilization is not related to the vortex physics" (SI p. 13, Fig. S10) | Measure or null the magnet's remanent field at the sample. Then sweep the out-of-plane field through zero in Oe steps on Device 13 or 14 and on etched Device 16, and check whether η is odd about an offset field. Your Fig. 4 polarity follows the sign of B, which this mechanism also produces. |
| Trapped vortex plus self-field from nonuniform bias (not in library; Golod and Krasnov) | Tested in part | Sweeps repeated after trapped flux is removed (warming above Tc in a nulled field) and after flux is trapped on purpose: part (1 T field cooling then removal in Figs. S8 and S9, with no flux-free reference); Polarity compared with the bias configuration changed (current leads swapped): no | "it is not eliminated by field-cooling followed by removal of the external field" (p. 5) | Warm above Tc in a nulled field before each of several zero-field sweeps and see whether the sign still scatters. Swap the current leads and see whether the polarity follows the bias configuration. You could also stop sweeps just above the switching current to limit flux entry. |
| A chosen example from many patterns (`fine-tuning-and-selection`) | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part (the sweep choice is stated for Fig. 2c and 2d only); A second device or dataset shown: all (Devices 11 to 14, and controls 15 and 16) | "During the second oxidation stage, three consecutive measurements were performed, and only the second exhibited a field-free SDE" (SI p. 2) | Give the full count of oxidized or etched devices. Show every sweep per condition, with η and both switching currents, for example as a table in the supplement. |

## Questions about devices and data

1. How many oxidized or etched CsV3Sb5 devices did you make, and how many showed a field-free diode? Your p. 4 and Table S1 cover ten pristine devices, all diode-free, and Devices 11 to 14 show the effect; the total number of inversion-broken devices isn't stated.
2. Why were any others set aside?
3. Which ranges did you measure beyond the ones shown, in particular out-of-plane fields between 0 and 0.1 T, other sweep rates, and the temperatures of Fig. 4 and of the Ti-doped devices?
4. What does the second-best dataset look like, for example the third oxidation stage of the Fig. 2 device, where you write "none of which showed SDE" (SI p. 2)?
5. What was the residual out-of-plane field at the sample during the "B = 0" sweeps, after the ±10 T magnetoresistance sweeps of Figs. S1 and S2 and the 1 T field cooling of Figs. S8 and S9, and was it measured or nulled?
6. With many sweeps per direction at zero field (a few hundred, say), how do the switching-current histograms for positive and negative bias compare, and is the mean η different from zero? In Fig. S7 both |Ic+| and |Ic−| move by a few μA between sweeps, about the size of their difference.
7. For the Ti-doped controls (Devices 15 and 16), at what temperature and T/Tc were they measured, how many sweeps per condition did you take, and did Device 16 get the same etch pattern as Device 13? Since the Fig. 2 device showed a diode in one of three sweeps per oxidation stage, how many diode-free sweeps would you need before the null is clear?
8. Which device is which in Figs. 2, S3 and S4? Fig. S3 is captioned "Device 12 (Fig. 2 in the main text)" while Fig. 2 names Device 11; Fig. S4 calls the oxidized device Device 13, whose η values p. 5 gives for Device 12; and panels in Figs. S13 and S14 read Device 19 and 20. Also, what criterion sets the onset current, given Fig. S3 lists "Iac = 10 μA" while |Ic−| in Fig. 2c is a few μA?

## Related work

- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. Reports a field-free diode in CsV3Sb5 flakes whose polarity changes with thermal history, read as chiral superconducting domains.
- Ge et al. 2025, "Nonreciprocal superconducting critical currents with normal state field trainability in kagome superconductor CsV3Sb5", <https://arxiv.org/abs/2506.04601>. Zero-field critical-current asymmetry whose polarity changes randomly on thermal cycling to 300 K and follows a perpendicular field applied above the CDW transition.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. A zero-field diode and second-harmonic signals that appear as CsV3Sb5 flakes get thinner.
- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A strong diode in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening currents.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. A zero-field diode in conventional Nb junctions from self-field and a trapped Abrikosov vortex. Changing the bias configuration or trapping and removing a vortex switches the polarity or turns the diode on and off.

Happy to rerun this if you share the sweep-by-sweep data for Devices 13, 14 and 16.
