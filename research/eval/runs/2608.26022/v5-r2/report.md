# Lookalike check: Field-free superconducting diode in CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is a superconducting diode measurement on exfoliated flakes. The library has one diode entry and no diode-specific checks, so I used that entry, the practice checks that apply to every paper, and two lookalikes from outside the library.

**The claim, as I read it.** Encapsulated CsV3Sb5 flakes show no diode (Device 1 in Fig. 1, Devices 2 to 10 in Figs. S1, S2 and Table S1). Oxidation (Device 11, Fig. 2, eta up to 83.61%) or asymmetric etching (Devices 13 and 14, Fig. 3, Figs. S6, S7) produces a field-free diode whose sign and size change from sweep to sweep. An out-of-plane field of 0.1 to 0.2 T fixes it (Fig. 4, Fig. S11). Ti-doped flakes (Devices 15 and 16, Figs. S13, S14) show none. You read this as time-reversal-breaking domains inherited from the CDW.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories (Figs. S1 and S2 and Table S1)." (p. 4). The pristine count is complete; the number of oxidized or etched devices, and how many showed a diode, is not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature." (Fig. 3 caption, p. 15). Sweep counts per setting are given; reasons for the field and temperature ranges, and the temperature for Device 14, are not.
3. Give the processing steps from raw data to figures, with data and code : Partly. Ic is "defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5). The onset threshold is not stated, and data are "available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Asymmetric vortex edge barriers and Meissner screening | Tested in part | Plain film or junction of the parent superconductor: part (pristine flakes, and Ti-doped Devices 15 and 16 at zero field only); field, width or edge quality: part (Devices 13 and 14 at 0.1 T steps) | "demonstrating that the field stabilization is not related to the vortex physics" (SI p. 13, Fig. S10); the Hc1 estimate covers the in-plane field only. | Null the magnet, sweep the out-of-plane field through zero in sub-millitesla steps on Device 13 and Device 16, and give eta(B) with its zero crossing. |
| Fine-tuning and selection | Tested in part | Devices and datasets, and how many showed it: part; how the shown data were chosen: part; a second device or dataset: all | "During the second oxidation stage, three consecutive measurements were performed, and only the second exhibited a field-free SDE, corresponding to Fig. 2(c) in the main text." (SI p. 2) | One table per device with eta for every sweep, zeros included, plus the count of processed devices. |
| Trapped vortices pinned in the processed flake (not in library) | Tested in part | Flux trapped or removed on purpose, with eta tracked: part (Device 14, 1 T field cooling of one sign); bias configuration changed: no | "The stochastic SDE still persists under this protocol." (SI p. 11, Fig. S8) | Field-cool at +1 T and at -1 T, and warm above Tc between sweeps, then compare mean eta; swap the current leads. |
| Phase-slip switching statistics (not in library) | Tested in part | Per-polarity switching distributions over many sweeps: part (six to nine sweeps, shown as eta only); width compared with the spread in the Ic difference: no; fixed-bias time traces: part (Device 14, two sweeps) | "Control measurements presented in Fig. S12 further rule out ordinary time-dependent fluctuation near the critical current as the origin of the observed stochasticity." (p. 6) | Histograms of Ic+ and Ic- from 100 or more sweeps on Device 13, pristine Device 1 and Device 16, set against the spread in the Ic difference. |

A few notes on the rows. Hou et al. find a screening-current diode in plain Nb and V films at fields near 1 Oe. Your Fig. 4 steps from 0 to 0.1 T, so it cannot show where eta(B) crosses zero or how big the remanent field is at "B = 0". At plus and minus 0.2 T, eta takes the sign of the field (Fig. 4). A screening-current diode does the same, so the low-field sweep would separate the two pictures. Your Ti-doped etched Device 16 is the closest control you have, and it would be most useful under the same field series as Device 13.

Golod and Krasnov switch a zero-field diode on and off by trapping and removing a single vortex. A resistive excursion in each sweep could re-pin flux in your oxidized or etched flakes, so a warm-up reset between sweeps would test this directly.

For the statistics row, a reader will want to compare the scatter in Ic for each polarity with the size of the asymmetry. In Fig. S6, Ic in Device 13 runs from about 35 to 46 uA across six sweeps.

## Questions about devices and data

1. How many CsV3Sb5 devices did you oxidize or etch, and how many showed a field-free diode? The text names Devices 11 to 14, and panels in Figs. S13 and S14 carry the labels Device 19 and Device 20, which suggests more devices were made.
2. Why were the other processed devices set aside, if there were any?
3. Which ranges did you measure beyond the ones shown (out-of-plane field steps near zero, temperatures for Device 14, sweep rates), and how many sweeps did each pristine device and each Ti-doped stage get?
4. What does the second-best oxidized device look like, and which device is which? The Fig. S3 caption calls Device 12 the Fig. 2 device while the main text names Device 11, and the Fig. S4 caption gives the 17.07% to -30.86% sweeps to Device 13 while the main text gives them to Device 12.
5. What was the residual field of the magnet at nominal zero field after the 1 T field cooling and the 0.2 T series, and could you sweep the out-of-plane field through zero in sub-millitesla steps on Device 13 and on Ti-doped Device 16?
6. Which threshold defines the onset current in a smeared, multi-peak transition such as Fig. 2c, and how does eta change with that threshold and with the 10 uA ac excitation listed in Fig. S3?
7. How do Ti-doped Devices 15 and 16 compare with Devices 13 and 14 in thickness, Tc, critical current and transition shape, and did they get the same field and temperature series?
8. Did you ever warm above Tc between sweeps, and does the eta distribution change when you do?

Question 3 matters for the baseline. Processed devices show a diode in only some sweeps: one of three at the second oxidation stage (SI p. 2) and three of six in Fig. S4. A pristine baseline built from a single sweep per device could miss a diode that appears only now and then.

## Related work

- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. Reports a field-free diode in intrinsic CsV3Sb5 flakes whose polarity changes with thermal history, read as chiral superconducting domains.
- Ge et al. 2025, "Nonreciprocal superconducting critical currents with normal state field trainability in kagome superconductor CsV3Sb5", <https://arxiv.org/abs/2506.04601>. Zero-field Ic asymmetry in CsV3Sb5 nanodevices whose polarity changes randomly over thermal cycles to 300 K and follows a field applied above the CDW transition.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. A zero-field diode and second-harmonic signals that appear as flakes get thinner, together with a 3D to 2D crossover in the upper critical field.
- Rog et al. 2026, "Direct Observation of Channelised Supercurrents in a Kagome Superconductor", <https://arxiv.org/abs/2606.20157>. SQUID microscopy of CsV3Sb5-xSnx flakes shows a network of narrow supercurrent channels that acts like linked Josephson junctions, weaker in undoped samples; it bears on the path weights in your Eq. 2.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A diode effect in plain Nb and V films at fields as small as 1 Oe, traced to asymmetric vortex edge barriers and Meissner screening.

Outside-library sources in the table: Golod and Krasnov 2022, <https://arxiv.org/abs/2205.12196>; Murphy et al. 2013, <https://arxiv.org/abs/1303.2620>.

Happy to rerun this if you share the per-sweep critical currents for Devices 13, 14 and 16.
