# Lookalike check: Field-free superconducting diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your claim concerns a superconducting diode, and it does not claim a topological state. The library has a single diode entry and no ordered diode checks, so I used the practice checks and added two lookalikes from papers I opened. I worked from the extracted text and the figure captions, with no PDF.

**The claim, as I read it.** A 5 µm by 180 µm CuMnAs/AlAs(2 nm)/Al bar along [010] shows a zero-field diode effect (η of about 7% after zero-field cooling, Fig. 3a). The sign of η reverses after ±1 T preparation fields along [100] and does not reverse systematically for [010] (Fig. 3b,d,e). A second bar along [100] shows the same axis dependence (Extended Data Fig. 4). You attribute the diode polarity to the remanent Néel state, which you support with R_even hysteresis in a separate CuMnAs bar at 5 K (Fig. 4) and with XMLD-PEEM (Extended Data Fig. 5).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside (report-counts) : Partly. "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)." (pp. 4 to 5). The paper does not give the totals for bars, chips and cooldowns.
2. Disclose the full parameter ranges measured and why each shown range was chosen (report-ranges) : Partly. "Measurements were performed in a cryogen-free dilution refrigerator at a base temperature of 20 mK" (Methods, p. 8). The prepared states are shown for ±1 T ([100]) and ±4 T ([010]). The paper shows no η(T) series and no near-zero field sweep, and it does not say why these ranges were chosen.
3. Give the processing steps from raw data to figures, with data and code (report-processing) : Partly. Switching currents are "defined as the bias current at which the measured voltage first exceeded a threshold of 50 µV" (Methods, p. 8). The averaging and the 0.2 s delay are stated. The paper has no data or code statement.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Asymmetric vortex barriers and Meissner screening in a small residual field (from the magnet, or from a small uncompensated moment) | Partly addressed | "suggesting that the anisotropy is not determined simply by the relative orientation of the applied field and current, but is instead tied to the underlying crystallographic axes of CuMnAs." (p. 11, Ext. Data Fig. 4); the data bear on it; the paper doesn't discuss it. | Measure the residual field at "H = 0" after each excursion, and run the same protocol on a plain Al film or on Al over a nonmagnetic layer. |
| Trapped flux set by the preparation field (not in library) | Partly addressed | "We therefore perform nonlinear magnetotransport measurements at 5 K using a reference CuMnAs bar without a superconducting Al layer." (p. 5, Fig. 4); the data bear on it; the paper doesn't discuss it. | After preparing a state, warm above the 350 mK transition, cool again at H = 0 and check that η keeps its sign. |
| Thermoelectric response with geometric asymmetry (not in library) | Partly addressed | "we observe that the ordering of the two switching currents is reversed" (p. 4, Fig. 3b); this bears on the reversible part, and the 7% ZFC offset remains. | Show η against current ramp rate and delay, and with the current leads swapped. |
| Fine-tuning and selection | Partly addressed | "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)." (pp. 4 to 5) | Give the number of bars, chips and cooldowns, and show the second bar's full data next to Fig. 3. |

**A note on the screening row.** Hou et al. find a diode effect in plain films at fields as small as 1 Oe. A superconducting magnet often keeps a residual field of that size after a 1 T excursion, and the sign of that field follows the preparation polarity, which is the same pattern as your Fig. 3d. Your [100] bar argues against a simple field-to-current geometry, because it keeps the crystal-axis dependence. A residual field or a misalignment specific to one coil would still follow the magnet axes. If both bars sat on one chip in one mounting, a 90° rotation of the chip would separate the crystal axes from the coil axes. Jiang et al. calibrated their magnet's residual field with a co-mounted graphene flake whose magnetoresistance is even in field and has no hysteresis. That approach would carry over here. I also ran a rough estimate: your SQUID bound of 3×10⁻³ µB/Mn corresponds to a magnetization of about 8 G (µ0M ≈ 0.8 mT) in the CuMnAs layer. That is above the 1 Oe scale, so it would help to report the remanent moment after ±1 T at low temperature.

**A note on trapped flux.** Jiang et al. see a zero-field diode whose sign is set by a ±1 T in-plane poling field. They see it with the field both perpendicular and parallel to the current, in a nonmagnetic superconductor. Your Fig. 4 shows that CuMnAs alone keeps a field-written memory, and that bears on this lookalike. The diode bar is still a superconductor that went through a 1 T excursion. Flux trapped in the Al would disappear above 350 mK. A Néel state would survive warming to 1 K, because the Néel temperature is 480 K. That one warm-up separates the two.

## Questions about devices and data

1. How many bars did you pattern and measure for the diode effect, on how many chips and in how many cooldowns, and how many showed the zero-field diode and its reversal? Your Fig. 3 and Extended Data Fig. 4 show two.
2. Why were any others set aside?
3. Which ranges did you measure beyond the ones shown: η versus temperature up to the 350 mK transition, preparation fields beyond ±1 T along [100], and η in small applied fields around zero?
4. What does the second-best device or dataset look like, for example the [100] bar's ZFC switching-current distributions next to the Fig. 3a inset?
5. What was the residual field at "H = 0" after a ±1 T or ±4 T excursion, and how did you measure or null it?
6. If you prepare a state, warm the sample above the Al transition (and far below the 480 K Néel temperature), and cool again at zero field, does η keep its sign?
7. Were the [010] and [100] bars measured on the same chip and in the same mounting relative to the magnet axes, and could you rotate the chip by 90° so that the crystal axes and the coil axes swap?
8. Did you run the same protocol on a control film (plain Al, or Al on a nonmagnetic layer), and could you measure R_even on the superconducting heterostructure itself, since Fig. 4 uses a bar from a different wafer at 5 K? In the text I read, refs. 28 to 30 appear in the reference list with no citation in the text; was a discussion of them planned?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a strong diode effect at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening. With a EuS layer the effect becomes non-volatile.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. A ±1 T poling field sets the sign of the zero-field diode through trapped flux, for in-plane fields both perpendicular and parallel to the current. The magnet's residual field was checked with graphene.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Conventional Nb junctions act as zero-field diodes, and trapping or removing an Abrikosov vortex switches their polarity.
- Nagata et al. 2024, "Field-free superconducting diode effect in layered superconductor FeSe", <https://arxiv.org/abs/2409.01715>. Controlled experiments trace a field-free diode to a thermoelectric response combined with geometric asymmetry.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. Nb on compensated Mn3Pt shows a zero-field diode with efficiencies up to 50%. Its field and temperature dependence hints at several contributing mechanisms.

Happy to rerun this if you share the switching-current data and the magnet's field log.
