# Lookalike check: Field-free superconducting diode effect in CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with lookalike library version 0.4. A person hasn't checked it.*

Paper title on arXiv: "Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV$_3$Sb$_5$".

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library has one entry for superconducting diodes and no diode-specific checks, so I walked its general practice checks and added one lookalike from outside the library, with its source.

**The claim, as I read it.** Ten pristine hBN-encapsulated CsV3Sb5 devices show no field-free diode (Fig. 1, Figs. S1 and S2, Table S1). Oxidation (Device 11, Fig. 2) or asymmetric etching (Devices 13 and 14, Fig. 3, Fig. S7) turns on a field-free diode whose sign and size change from sweep to sweep, small out-of-plane fields fix it (Fig. 4), and Ti-doped devices with suppressed long-range CDW show none after the same processing (Devices 15 and 16, Figs. S13 and S14). You read this as metastable TRS-breaking domains tied to CDW order.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices with different thicknesses and fabrication histories (Figs. S1 and S2 and Table S1)." (p. 4). The pristine set is counted; for oxidized and etched CsV3Sb5 the paper names Devices 11 to 14 without saying how many were processed in total or whether any stayed diode-free.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Measurements were performed from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature." (Fig. 3 caption, p. 15). The field steps in Fig. 4, the residual field at nominal zero, and the total number of zero-field sweeps per device aren't given, and the pristine baseline is shown at 1.8 K only (Fig. 1e, Figs. S1 and S2).
3. Give the processing steps from raw data to figures, with data and code : Partly. Eq. (1) defines η, and the switching currents "are defined as the onset currents of the superconducting-to-resistive transition in the forward and backward sweeps" (p. 5). The onset criterion for multi-peak curves isn't stated, and the data are "available from the corresponding author upon reasonable request" (p. 9).

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Asymmetric vortex edge or surface barriers and Meissner screening (diode-vortex-screening) | Partly addressed | "After deliberately introducing inversion-symmetry breaking with the same fabrication protocol used for the pristine devices, the Ti-doped samples do not show a field-free superconducting diode effect." (p. 6); edges, vortices and residual field aren't discussed. | Report the residual field at nominal zero, plot η against field near zero for both signs from your Fig. 4 data, and measure Device 16 at ±0.1 T and ±0.2 T. |
| Trapped Abrikosov vortex giving a zero-field diode with switchable polarity (not in library) | Partly addressed | "it is not eliminated by field-cooling followed by removal of the external field" (p. 5; Figs. S8 and S9); the data bear on it; the paper doesn't discuss vortices. | Warm above Tc in a nulled field between sweeps, and compare sweeps that stop just past switching with sweeps to 300 μA. |
| Fine-tuning and selection (fine-tuning-and-selection) | Partly addressed | "The effect is reproducible across devices, including a second etched sample (Device 14; Fig. S7)" (p. 5); counts of processed devices and of sweeps set aside are missing. | State how many devices were oxidized or etched and how many showed the effect, and show Devices 12 and 14 in the Fig. 3d,e format. |

A note on the two vortex rows. Your Ti-doped etched control is the closest thing to the library's control (the same geometry in a related superconductor), and the field-cooling runs in Figs. S8 and S9 bear on trapped flux. What a reader will still ask is how large the field is at nominal zero, especially after a 1 T excursion in a superconducting magnet, and whether the polarity that Fig. 4 fixes simply follows the sign of the applied field, as an ordinary field-induced diode in a film with asymmetric edges would. Your etched zig-zag geometry (Fig. 3a inset) and the oxidized, inhomogeneous films (Fig. 2b, "multi-peak structure", p. 5) are the kind of samples where edge barriers and vortex pinning differ between the two current directions. Each sweep to 300 μA drives the film normal, which could also release or re-pin vortices between sweeps. The Ti-doped devices would separate these readings most directly if they were measured at the same temperature, T/Tc and fields as Device 13.

## Questions about devices and data

1. How many CsV3Sb5 devices did you oxidize or etch in total, and how many showed a field-free diode? Your pristine set is counted (ten devices, Table S1); for the inversion-broken set the paper names Devices 11 to 14.
2. Why were the others set aside, if any were?
3. Which ranges did you measure beyond the ones shown: the total number of zero-field sweeps per device, the field steps in Fig. 4, and temperatures below 1.8 K for the pristine devices?
4. What does the second-best device or dataset look like? For example, Devices 12 and 14 at zero field in the format of Fig. 3d,e.
5. What was the residual field at nominal B = 0 in the PPMS and in the dilution refrigerator, how was the magnet zeroed (in particular after the 1 T field-cooling in Figs. S8 and S9), and how does η depend on fields of a few mT of either sign?
6. For the Ti-doped Devices 15 and 16, what are the thickness, Tc, critical current and measurement temperature, and do they show a diode at ±0.1 T and ±0.2 T out of plane, as Device 13 does?
7. How did you pick the onset currents in multi-peak curves such as Fig. 2c,d (a voltage or resistance threshold, which peak), and how much does η change with that choice?
8. Which device is which in the supplement? Fig. S3 is captioned as Device 12 "(Fig. 2 in the main text)", while the main text gives Fig. 2 as Device 11, and Fig. S4 is captioned Device 13 but shows the η values (17.07% and -30.86%) that page 5 gives for Device 12.

## Related work

- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Strong diode effects in plain Nb and V films at fields as small as 1 Oe, traced to asymmetric vortex edge or surface barriers and Meissner screening currents.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Conventional Nb junctions give a zero-field diode above 70% efficiency from self-field plus a trapped Abrikosov vortex, with polarity switched by trapping or removing the vortex.
- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. A field-free diode in intrinsic CsV3Sb5 flakes whose polarity changes with thermal history.
- Ge et al. 2025, "Nonreciprocal superconducting critical currents with normal state field trainability in kagome superconductor CsV3Sb5", <https://arxiv.org/abs/2506.04601>. Zero-field nonreciprocal critical currents in CsV3Sb5 nanodevices, with polarity random over thermal cycles to 300 K and set by a field applied above the CDW transition.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. A zero-field diode and second-harmonic signals that appear as CsV3Sb5 flakes get thinner, alongside a crossover to two-dimensional superconductivity.

Happy to rerun this if you share the sweep data behind Figs. 3, 4 and S14.
