# Lookalike check: Field-free superconducting diode effect in CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a superconducting diode study. The library's diode family has one entry and no ordered checks, so I used the checks that apply to every paper and added one lookalike from outside the library.

**The claim, as I read it.** Your hBN-encapsulated CsV3Sb5 devices show no field-free diode (Fig. 1, Figs. S1 and S2, Table S1, ten devices). Oxidation (Device 11, Fig. 2) or asymmetric etching (Device 13, Fig. 3) turns on a field-free diode whose sign and size change from sweep to sweep. Small out-of-plane fields stabilize it (Fig. 4, Figs. S10 and S11). Ti-doped devices without long-range CDW order show none after the same processing (Figs. S13 and S14). You read this as CDW-linked time-reversal-breaking domains coupled to extrinsic inversion breaking.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. You count the pristine devices: "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices" (p. 4). You also count sweeps per oxidation stage: "During the second oxidation stage, three consecutive measurements were performed, and only the second exhibited a field-free SDE" (Supplementary Text, p. 2). I could not find the total number of oxidized or etched devices, or how many of them showed the diode.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature" (Fig. 3 caption). The paper does not state the field steps in Fig. 4, the residual field at nominal 0 T, or why each range was chosen.
3. Give the processing steps from raw data to figures, with data and code : Partly. The onset currents "are defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5). The onset threshold is not given, and the data "are available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Asymmetric vortex edge barriers and Meissner screening current | Tested in part | Same measurement on a plain film or junction of the parent superconductor: part (the Ti-doped Devices 15 and 16 went through the same processing, Figs. S13 and S14, but their superconducting parameters are not compared with the CsV3Sb5 devices); effect followed against field, sample width or edge quality: part (field series for the etched Devices 13 and 14 only, Fig. 4, Figs. S10 and S11) | "demonstrating that the field stabilization is not related to the vortex physics" (Fig. S10 caption; the estimate covers the in-plane field only) | Measure the residual field at the sample at nominal 0 T. Then take η against out-of-plane field in steps of about 1 Oe around zero, for Device 13 and Ti-doped Device 16 in the same cooldown. |
| Trapped vortex from field history (not in library; Golod and Krasnov 2022) | Tested in part | Field history before each zero-field dataset reported, with zero-field cooling in a nulled field: no; diode compared with and without trapped flux (field-cooled versus zero-field-cooled): part (Device 14 only, Figs. S8 and S9) | "The stochastic SDE still persists under this protocol." (Fig. S8 caption) | Warm above Tc and null the magnet's remanent field. Cool in zero field and repeat the zero-field sweeps of Fig. 3 before applying any field. Report the order of the field series. |
| Fine-tuning and data selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; how the shown data were chosen: part (disclosed for the Fig. 2 sweeps, not for Fig. 3a to c); a second device or dataset shown: all (Devices 12 and 14 in the SI) | "only the second exhibited a field-free SDE, corresponding to Fig. 2(c) in the main text" (Supplementary Text, p. 2) | List every CsV3Sb5 and Ti-doped device you processed. Give η for every sweep at each oxidation stage, including the sweeps with no diode. |

## Questions about devices and data

1. How many CsV3Sb5 devices did you oxidize or etch, and how many showed a field-free diode? Your ten pristine devices are counted (p. 4, Table S1); I could not find the same count for processed devices, or for Ti-doped devices beyond Devices 15 and 16.
2. Why were the other processed devices, if any, set aside?
3. Which field steps, temperatures, sweep rates and numbers of sweeps did you measure beyond the ones shown, in particular the field step in Fig. 4 and any fields between 0 and 0.1 T?
4. What does the second-best dataset look like? Devices 12 and 14 appear in the SI; it would help to see the pristine devices with the same number of repeated sweeps, so the baseline spread of η sits on the same footing as Fig. 3d,e.
5. What is the residual field at the sample at nominal 0 T in the PPMS and in the dilution refrigerator, how was it measured, and what field history (the Fig. 4 series, the 1 T field cooling of Figs. S8 and S9) preceded each zero-field dataset?
6. The SI labels seem to differ from the main text: Fig. S3 calls the Fig. 2 device "Device 12", and Fig. S4 and the Supplementary Text give η = 17.07%, -30.86% and -14.07% for an oxidized "Device 13", while p. 5 gives "between −30.86% and 17.07%" for Device 12 and describes Device 13 as etched. Which device is which?
7. For Ti-doped Devices 15 and 16, what are the thickness, Tc, critical current and transition shape after each processing step, and how many sweeps did you take per step? Did oxidation give the same multi-peak transition you show in Fig. 2b?
8. What dV/dI threshold defines the onset current, and how do you apply it when the transition has several peaks? Switching-current histograms for each direction would show how far the sweep-to-sweep spread of η exceeds ordinary switching statistics.

## Related work

- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. Reports a field-free diode in intrinsic CsV3Sb5 flakes, with polarity modulated by thermal history, and reads it as chiral superconducting domains.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. Reports a zero-field diode and second-harmonic nonreciprocal signals that appear as CsV3Sb5 flakes get thinner.
- Hou et al. 2022 (Phys. Rev. Lett. 131, 027001, 2023), "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Shows a strong diode in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Shows a zero-field diode in conventional Nb junctions from a trapped Abrikosov vortex. Trapping or removing the vortex switches the polarity or turns the diode on and off.
- Rog et al. 2026, "Direct Observation of Channelised Supercurrents in a Kagome Superconductor", <https://arxiv.org/abs/2606.20157>. SQUID microscopy shows networks of narrow supercurrent channels in CsV3Sb5-xSnx flakes, much weaker in undoped samples.

Happy to rerun this if you share the figure data or the full sweep sets.
