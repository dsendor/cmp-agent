# Lookalike check: Field-free diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library's diode section is small, so I added three lookalikes from the diode literature, each tied to a paper I opened.

**The claim, as I read it.** You report a field-free superconducting diode in a 5 µm by 180 µm CuMnAs/AlAs(2 nm)/Al bar. Efficiency is "approximately 7% in the ZFC state" (p. 3, Fig. 3a). After field preparation it reaches "values approaching ±20%" (p. 4, Fig. 3d). The polarity reverses with the sign of a preparation field along [100] and responds weakly along [010] (Figs. 3b, 3d, 3e; Extended Data Fig. 4 for a second, [100]-oriented bar). You assign the polarity to the remanent Néel state. Two things support that: matching remanence in the even nonlinear resistance of a separate CuMnAs bar at 5 K (Fig. 4), and a SQUID bound on the net moment (Fig. 2b).

## Checks a careful reader will look for

The library has no ordered checks for diode papers, so these are the practice checks, which apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. You name two bars ("An orthogonal bar patterned along [100] displays the same qualitative dependence", p. 4 to 5). Totals, cooldowns and any set-aside bars are not given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Ranges appear on axes and in text ("ranging from −5 to 5 T", p. 5). Preparation along [100] spans ±1 T (Fig. 3d) and along [010] spans ±4 T (Fig. 3e), with no stated reason. No η is shown at nonzero measurement field or above 20 mK.
3. Give the processing steps from raw data to figures, with data and code : Partly. Methods give the switching criterion, "a threshold of 50 µV" (p. 8), and the averaging over eight sweeps. I found no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Asymmetric vortex barriers and Meissner screening in the Al film | Tested in part | Same protocol on a plain Al film or junction: no; effect followed against field, width or edges: part (preparation field and two bar orientations only) | "the anisotropic remanence itself originates in CuMnAs rather than from spurious flux trapping or vortex dynamics" (p. 6) | Run the Fig. 3c protocol on a bare Al bar, and show η against small measurement fields around zero. |
| Trapped flux set by the preparation field (not in library) | Not tested (argued, not tested) | Critical currents mapped against measurement field near zero after each preparation sign: no; in-plane against out-of-plane preparation: no | Same sentence (p. 6); the Fig. 3b axis spans about 16 to 23 µA, below the 27 to 31 µA of the Fig. 3a inset | After preparing, warm above TC ≈ 350 mK at H = 0 and cool back: trapped flux leaves, while a Néel state with a Néel temperature of 480 K would stay. |
| Remanent field of the superconducting magnet at nominal H = 0 (not in library) | Not tested (not mentioned) | Zero field calibrated in situ with a non-hysteretic sensor: no | Not discussed. | Calibrate zero field after the ±1 T and ±4 T excursions with a Hall probe or an on-chip sensor, and rotate the chip 90° in a later cooldown so [100] and [010] swap magnet axes. |
| Stray fields from remanent magnetic domains (not in library) | Tested in part | Spacer that cuts proximity but keeps stray fields: no; domain axis along and across the current: all (both bars, both axes) | "this also disfavors a stray-field mechanism associated with uncompensated magnetization" (p. 6) | Turn the SQUID bound (Fig. 2b) into a local field at the bar edges, and add a thicker-barrier sample where proximity is gone and stray fields remain. |
| Selection of the shown device and data | Tested in part | Counts: part; how the data were chosen: no; second device: part (η only, Extended Data Fig. 4) | "An orthogonal bar patterned along [100] displays the same qualitative dependence" (p. 4 to 5) | State totals, and show the [100] bar's zero-field-cooled distributions and Fig. 3b readout. |

Two points tie these rows to your figures. First, both bars sit on the same chip in the same magnet. The [100] axis is therefore both a crystal axis and a fixed magnet axis, so the test across two bar orientations cannot tell the two apart. A rotated cooldown or an in-situ field sensor would. Second, the Fig. 4 reference bar comes from "a CuMnAs wafer with 3 nm fully oxidized Al cap" (p. 8), measured at 5 K. It shows how CuMnAs keeps memory of the protocol. It does not show whether the Al in the diode bar traps flux. A warm-above-TC test on the diode bar itself bears on the trapped-flux and screening rows at once, and you can run it with your present setup.

## Questions about devices and data

1. How many bars did you measure on the 2.0 nm wafer, over how many cooldowns, and how many showed the field-free diode and the [100] reversal?
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown: preparation fields beyond ±1 T along [100] (Fig. 3d), measurement fields near zero, and temperatures above 20 mK?
4. What does the second-best device look like, for example the [100] bar's zero-field-cooled switching distributions and the Fig. 3b readout?
5. Does a prepared polarity survive warming the bar above TC at H = 0 and cooling back, and why do the switching currents after preparation (Fig. 3b axis, about 16 to 23 µA) sit below those after zero-field cooling (Fig. 3a inset, about 27 to 31 µA)?
6. How did you set and check H = 0 after the ±1 T and ±4 T excursions, and did [100] and [010] fields come from different magnet coils for both bars?
7. What local field at the Al does the SQUID bound allow? By my estimate, 3×10−3 µB/Mn is about 0.6 emu/cm3 (4πM near 8 G), so fields of order a gauss near edges or domain walls seem possible, the scale at which Hou et al. see diodes in plain films.
8. Why does the Fig. 4 reference come from a different wafer ("a CuMnAs wafer with 3 nm fully oxidized Al cap", p. 8) measured at 5 K, and could Reven or XMLD-PEEM be measured on the diode wafer itself?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", https://arxiv.org/abs/2205.09276. Diodes in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening, plus a non-volatile diode with a EuS layer.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", https://arxiv.org/abs/2512.05427. A zero-field diode whose sign follows a ±1 T poling field, traced to trapped flux; they calibrate zero field with a graphene sensor to exclude magnet remanence.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", https://arxiv.org/abs/2205.12196. Nb planar junctions where a trapped Abrikosov vortex gives a zero-field diode, with polarity switched by trapping or removing the vortex.
- Li et al. 2025, "Field-Free Superconducting Diode Enabled by Geometric Asymmetry and Perpendicular Magnetization", https://arxiv.org/abs/2506.17651. A field-free diode in Pt/Co/Nb driven by stray fields of a magnetized layer through asymmetric vortex entry and pinning.
- Zapata et al. 2026, "Field-free superconducting diode and tunable vortex dynamics in NbN/FePt stripe-domain heterostructures", https://arxiv.org/abs/2610.30556. A field-free diode from remanent stripe-domain stray fields that persists through an insulating AlN spacer and depends on domain orientation relative to the current.

Happy to rerun this if you share the figure data.
