# Lookalike check: Field-free superconducting diode in CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper reads a superconducting diode as a probe of time-reversal symmetry breaking tied to the CDW. That is not a topological signature, so I used the library's diode entry and its practice checks, applied to that reading.

**The claim, as I read it.** In pristine hBN-encapsulated CsV3Sb5 there is no diode (ten devices, Fig. 1, Table S1). Oxidized Devices 11 and 12 and etched Devices 13 and 14 show a field-free diode whose sign and size change from sweep to sweep (Figs. 2, 3, S3, S4, S6, S7). An out-of-plane field of 0.1 to 0.2 T fixes the polarity (Fig. 4, Figs. S10, S11). Ti-doped devices with the CDW suppressed show no diode after the same processing (Figs. S13, S14). From this you conclude that time-reversal symmetry breaking domains linked to the CDW couple to an inversion breaking supplied from outside.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. You give "ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories (Figs. S1 and S2 and Table S1)" (p. 4), and sweep counts for the oxidation series: "three consecutive measurements were performed, and only the second exhibited a field-free SDE" (Supp. p. 2). The paper doesn't say how many oxidized or etched devices were made, and the device labels for Figs. S3 and S4 don't match the main text.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature." (Fig. 3 caption, p. 15). The field steps near zero, and why each range was chosen, aren't given.
3. Give the processing steps from raw data to figures, with data and code : Partly. "|Ic+| and |Ic−| are defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5). The paper doesn't say how the onset is located in multi-peak curves, and the data are "available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Asymmetric vortex barriers and Meissner screening (diode-vortex-screening) | Tested in part | Same measurement on a plain film of the parent superconductor: part; effect followed against field, width or edge quality: part | "ordinary vortex entry into the superconducting layer is not expected under the in-plane training condition" (Fig. S10 caption, Supp. p. 13); pristine and Ti-doped controls are shown at nominal zero field only | Measure η against out-of-plane field (0 to 0.2 T, fine steps) on a pristine device and on etched Ti-doped Device 16. The training fields sit at 12 to 24% of μ0Hc2⊥ ≈ 0.85 T, where vortices are present |
| Fine-tuning and selection (fine-tuning-and-selection) | Tested in part | Devices and datasets measured, and how many showed the effect: part; how the shown data were chosen: part; a second device or dataset shown: all | "only the second exhibited a field-free SDE, corresponding to Fig. 2(c) in the main text" (Supp. p. 2) | Give device and sweep counts for every inversion-broken device, and show every sweep behind Figs. 2c and 2d |
| Trapped Abrikosov vortex or remanent field at nominal zero field (not in library) | Tested in part | Field at the sample measured or compensated: no; field history varied and polarity checked: part; trapped flux cleared before each sweep: no | "it is not eliminated by field-cooling followed by removal of the external field (Figs. S8 and S9)" (p. 5) | Measure the remanent field (Hall sensor, or locate the zero crossing of η(B) in steps of about 1 mT). Then repeat the zero-field statistics after warming above Tc in compensated zero field before each sweep |

## Questions about devices and data

1. How many oxidized or etched CsV3Sb5 devices did you make beyond Devices 11 to 14, and did any of them show no field-free diode response? (The ten pristine devices are counted in Table S1 and the Ti-doped Devices 15 and 16 in Figs. S13 and S14.) Could you also confirm the device labels: p. 5 gives the -30.86% and 17.07% sweeps as Device 12 (Figs. S3 to S5), Fig. S4 labels them Device 13, and Fig. S3 calls Device 12 "Fig. 2 in the main text" while Fig. 2 shows Device 11.
2. Your supplementary text (p. 2) says only one sweep in three showed a diode at the second and fourth oxidation stages. Were any sweeps, cooldowns or devices set aside from the statistics in Figs. 3d&e and 4, and why?
3. Which ranges did you measure beyond the ones shown: field steps near zero in Fig. 4, fields beyond 0.2 T, temperatures other than 1.8 K for the oxidized devices, and temperatures below 1.8 K for the pristine devices?
4. What do the zero-field statistics of your second-best device (Device 14, or the oxidized Device 12) look like next to Fig. 3d&e?
5. What is the residual field at the sample at nominal zero in the PPMS and in the Triton, after the in-plane sweeps to 10 T (Figs. S1, S2) and the 1 T field cools (Figs. S8, S9), and was it measured or compensated?
6. The training fields of 0.1 to 0.2 T are a sizable fraction of the out-of-plane critical field of about 0.85 T (Fig. S10), where vortices and Meissner screening currents are present. Did you measure the diode efficiency against out-of-plane field on a pristine device and on the etched Ti-doped Device 16?
7. For the null results, how many sweeps did you take per condition on the pristine devices and on Devices 15 and 16, at which temperatures relative to their Tc, and what are the Tc and critical current of the Ti-doped devices? With a diode in one sweep out of three in Device 11, a few sweeps could miss it.
8. At zero field, is the mean signed efficiency (with its uncertainty) different from zero, and how do the separate distributions of |Ic+| and |Ic-| compare? In Fig. S4, |Ic+| alone ranges from 16.8 to 36 μA between sweeps, and it would help to know how the onset was located in multi-peak curves such as Fig. 2c.

A few notes on the questions. Questions 5 and 6 come from the two vortex rows. Your Fig. S10 estimate rules out vortex entry for the in-plane field. Fig. 4 and Fig. S11 use out-of-plane fields, where a thin flake holds vortices well below 0.2 T. There, an etched zig-zag edge gives a field-odd diode in ordinary films (Hou et al., below). A trapped vortex can also give a zero-field diode whose polarity changes when the vortex moves or leaves (Golod and Krasnov, below). Each excursion into the resistive state could reset that. Your field-cool runs (Figs. S8, S9) bear on this. A measured remanent field and flux-cleared repeats would settle most of it.

Question 8 is one no library entry raises. Each η pairs one forward and one backward sweep taken at different times. If |Ic| jitters by tens of percent between sweeps in both directions, η takes either sign with a mean near zero. Fig. 3d&e reports the average amplitude, and the signed mean would separate the two readings. Your Fig. S12 time traces test telegraph switching at fixed bias. They don't address this sweep-to-sweep jitter.

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A strong diode in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex edge barriers and Meissner screening.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. A zero-field diode in conventional Nb junctions from a trapped Abrikosov vortex, with polarity switched by trapping or removing the vortex.
- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. A field-free diode in CsV3Sb5 flakes with polarity modulated by thermal history, read as dynamical superconducting domains.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. A zero-field diode and second-harmonic signals that emerge as CsV3Sb5 flakes are thinned.
- Rog et al. 2026, "Direct Observation of Channelised Supercurrents in a Kagome Superconductor", <https://arxiv.org/abs/2606.20157>. SQUID microscopy showing narrow supercurrent channels in CsV3Sb5-xSnx flakes, weaker in undoped samples, consistent with a Josephson network.

Happy to rerun this if you share the figure data.
