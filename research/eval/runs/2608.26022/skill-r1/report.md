# Lookalike check: Field-free superconducting diode in CsV3Sb5 (arXiv 2608.26022v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a superconducting diode measurement, which the library covers with one entry and no ordered diode checks, so I used the general practice checks, adapted the diode entry to a field-free claim in flakes, and added two lookalikes from outside the library.

**The claim, as I read it.** Ten hBN-protected CsV3Sb5 flakes show no zero-field diode (Fig. 1, Figs. S1, S2, Table S1). Oxidation (Device 11, Fig. 2) or asymmetric etching (Devices 13 and 14, Fig. 3, Fig. S7) gives a field-free diode whose sign and size change from sweep to sweep (Fig. 3d,e, Fig. S4), which 0.1 to 0.2 T out-of-plane fields fix (Fig. 4). Ti-doped devices without long-range CDW, processed the same way, show none (Devices 15 and 16, Figs. S13, S14). You read this as metastable TRS-breaking domains inherited from the CDW.

## Checks a careful reader will look for

1. Report devices and datasets, how many showed the effect, and why others were set aside : Partly. You give all ten pristine devices ("The same conclusion holds across ten hBN-encapsulated CsV3Sb5 devices", p. 4) and sweep counts per oxidation stage (SM p. 2); the number of oxidized or etched devices made, and how many showed a diode, is not stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Temperature and field ranges are given ("from 0.25 to 1.5 K in 0.25 K steps, with six consecutive sweeps taken at each temperature", Fig. 3 caption, p. 15); field steps, the residual field at nominal zero, and the total number of sweeps taken are not.
3. Give the processing steps from raw data to figures, with data and code : Partly. Eq. (1) defines η from "the onset currents of the superconducting-to-resistive transition" (p. 5); data are "available from the corresponding author upon reasonable request" (p. 9), and the onset criterion is not spelled out.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Vortex edge barriers and Meissner screening in a small residual field (diode-vortex-screening) | Partly addressed | "the Ti-doped samples do not show a field-free superconducting diode effect" (p. 6); the vortex argument in Fig. S10 covers in-plane fields only. | Measure or null the magnet's remanent field at "B = 0", scan η through zero in mT steps, and run the Fig. 4 field series on Devices 15 and 16. |
| Selection of a non-representative sweep (fine-tuning-and-selection) | Partly addressed | "only the second exhibited a field-free SDE, corresponding to Fig. 2(c) in the main text" (SM p. 2). | Show all sweeps per stage and device, with the share that showed a diode. |
| Trapped Abrikosov vortex plus self-field from nonuniform bias (not in library) | Partly addressed | "The stochastic SDE still persists under this protocol." (Fig. S8, SM p. 11); the data bear on it; the paper doesn't discuss trapped vortices. | Cap the sweep just above switching so the flake doesn't go fully normal, and compare polarity statistics with full ±300 μA sweeps and with zero-field cooling in a nulled field. |
| Stochastic switching-current distribution with no underlying diode (not in library) | Partly addressed | "we do not observe evidence of fluctuations that could account for the full stochastic variation of the diode polarity" (Fig. S12, SM p. 15). | Build |Ic+| and |Ic−| histograms over many sweeps and test whether their means differ; compare widths with Device 16. |

## Questions about devices and data

1. How many oxidized or etched CsV3Sb5 devices did you make and measure, and how many showed a field-free diode? Table S1 answers this for the ten pristine devices; Devices 11 to 14 are the inversion-broken ones shown.
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown: how many zero-field sweeps per condition in total, which field steps in Fig. 4, and were the Ti-doped Devices 15 and 16 also swept at the 0.1 to 0.2 T out-of-plane fields of Fig. 4?
4. What does the second-best dataset look like? For example, the first and third sweeps of Device 11 at the second oxidation stage (SM p. 2 says only the second showed a diode), and Device 14 next to Device 13.
5. What is the remanent field of the PPMS and Triton magnets at nominal B = 0, especially after the 1 T field-cooling runs (Figs. S8, S9) and the ±0.2 T sweeps of Fig. 4, and was it measured or nulled? A fine scan of η through zero field, a few mT each way, would show where the sign actually changes.
6. Could you show histograms of |Ic+| and |Ic−| from many sweeps (say a hundred each) at zero field for Device 13 or 14, and for Ti-doped Device 16, and say whether the two distributions differ in their means?
7. How was the onset current extracted from dV/dI with a 10 μA AC excitation and 0.2 to 0.5 μA steps (Fig. S3), when the critical currents in Fig. S4 are 17 to 36 μA, and how does η change with a smaller excitation or a different Ic criterion?
8. Which device is which? The main text calls the Fig. 2 device Device 11 and gives the −30.86% to 17.07% range for Device 12, while the Fig. S3 caption calls Device 12 the Fig. 2 device and those η values appear in Fig. S4, labeled Device 13. How do the thickness, Tc and Ic of Devices 15 and 16 compare with Devices 11 to 14?

A few notes on why these matter. Hou et al. find a strong diode in plain Nb and V films at fields "as small as 1 Oe", so a superconducting magnet's remanent field after a 1 T excursion is enough to matter in a flake with edges you have deliberately roughened. Your Ti-doped controls are the strongest answer to this family of explanations, and they become stronger still if Devices 15 and 16 match Devices 13 and 14 in thickness, Ic and geometry, were measured in the same cryostat after the same field history, and show no diode at the Fig. 4 fields too. At 0.1 to 0.2 T out of plane, a sizable fraction of your quoted 0.85 T out-of-plane critical field, any thin film sits in the vortex state, where a field-induced diode is expected; the Fig. 4 stabilization is most informative next to the same series on a Ti-doped device.

The stochastic sign is the heart of your interpretation, so the statistics deserve the most room. With six or nine sweeps per condition, and an η built from one forward and one backward sweep, the spread of switching currents alone sets a floor on |η|. Your Fig. S12 time traces show each state is stable at fixed bias, and they also show the switching current shifts between sweeps; whether that shift comes from domains, from flux re-trapped each time the flake is driven to 300 μA, or from current paths rearranging, is something the histograms and capped sweeps above could separate. Your own Ti-doped Device 16 bound of about 0.1% (Fig. S14) is a useful reference width for those histograms.

## Related work

- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Strong diode in conventional Nb and V films at fields as small as 1 Oe, traced to asymmetric vortex edge and surface barriers and Meissner screening currents.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Zero-field diode above 70% efficiency in conventional Nb junctions from self-field of nonuniform bias plus a trapped Abrikosov vortex; polarity switches by trapping or removing the vortex.
- Le et al. 2023, "Superconducting diode effect and interference patterns in Kagome CsV3Sb5", <https://arxiv.org/abs/2309.00264>. Field-free diode in intrinsic CsV3Sb5 flakes with polarity modulated by thermal history, read as chiral superconducting domains.
- Ge et al. 2025, "Nonreciprocal superconducting critical currents with normal state field trainability in kagome superconductor CsV3Sb5", <https://arxiv.org/abs/2506.04601>. Zero-field Ic asymmetry in CsV3Sb5 nanodevices whose polarity changes randomly with thermal cycling and follows a perpendicular field applied above the CDW transition.
- Zhang et al. 2026, "Thickness-driven crossover from conventional to chiral nonreciprocal superconductivity in kagome metal CsV3Sb5", <https://arxiv.org/abs/2605.29665>. Zero-field diode and second-harmonic signals that emerge with decreasing thickness in CsV3Sb5 flakes, alongside a 3D to 2D crossover in upper critical field.

Happy to rerun this if you share the figure data or the full sweep sets.
