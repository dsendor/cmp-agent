# Lookalike check: Reversible field-free superconducting diode effect controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is a superconducting diode measurement in a film, so I used the library's diode entry and practice checks, plus three lookalikes from papers I opened. I worked from the text and figure captions.

**The claim, as I read it.** At zero applied field, a 5 µm by 180 µm CuMnAs/AlAs/Al bar along [010] switches at unequal currents in the two directions (η about 7% after zero-field cooling, Fig. 3a), and the sign of η follows the sign of a preparation field along [100] (up to about ±20%, Fig. 3b,d) with a weak, unreversed response along [010] (Fig. 3e). You tie this to the Néel state through the same anisotropy in the nonlinear resistance of a separate CuMnAs bar at 5 K (Fig. 4) and in XMLD-PEEM (Extended Data Fig. 5).

## Checks a careful reader will look for

The library has no ordered checks for diode signals yet, so these are its three practice checks; the diode-specific controls are in the table.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. You show two superconducting bars: "The response shows the same qualitative dependence on the preparation-field axes as the [010]-oriented bar" (p. 11, Extended Data Fig. 4). The number of bars, chips and cooldowns measured isn't stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. The preparation ranges show on the axes (±1 T along [100] in Fig. 3d, ±4 T along [010] in Fig. 3e), and for the reference bar "ranging from −5 to 5 T, Reven shows pronounced hysteresis" (p. 5, Fig. 4c). The diode data are all taken "at a base temperature of 20 mK" (p. 8); η against temperature or small applied field isn't shown, nor why the ranges were chosen.
3. Give the processing steps from raw data to figures, with data and code : Partly. Methods give the criterion, "defined as the bias current at which the measured voltage first exceeded a threshold of 50 µV" (p. 8), and the averaging. I found no data or code availability statement.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Fine-tuning and selection | Partly addressed | "Repeated current sweeps yield well-separated switching-current distributions for the two current directions (inset of Fig. 3a)" (p. 3); bar and cooldown counts are missing. | State how many bars and chips you measured at 20 mK, and show the [100] bar's histograms and raw sweeps as the second-best dataset. |
| Vortex barriers and Meissner screening in the Al film | Partly addressed | "the anisotropic remanence itself originates in CuMnAs rather than from spurious flux trapping or vortex dynamics" (p. 6); no plain Al control is shown. | Run the same preparation protocol on an Al/AlAs film without CuMnAs at the same 5 µm width, and map η against a small out-of-plane field near zero. |
| Trapped flux set by the preparation field (not in library; Jiang et al. 2025) | Partly addressed | "Neither mechanism is naturally expected to track the Néel-vector anisotropy observed here." (p. 6) | After preparing, warm above the Al Tc (for example to 1 K, far below the 480 K Néel temperature), recool in nulled field and remeasure η. |
| Residual field of the magnet after the excursion (not in library; Jiang et al. 2025) | Partly addressed | "suggesting that the anisotropy is not determined simply by the relative orientation of the applied field and current" (p. 11, Extended Data Fig. 4); the data bear on it; the paper doesn't discuss it. | Measure and null the field at the sample after each excursion with an in situ sensor (Jiang et al. used graphene), and remount the chip rotated by 90°. |
| Stray field from a small uncompensated moment (not in library; Li et al. 2025) | Partly addressed | "this also disfavors a stray-field mechanism associated with uncompensated magnetization" (p. 6), from a sample-averaged SQUID bound (Fig. 2b). | Measure the SQUID remanent moment after the same ±[100] preparations and compare the edge field it implies with the 1 Oe scale in Hou et al. |

## Questions about devices and data

1. How many bars did you measure at 20 mK, on how many chips and cooldowns, and how many showed a polarity that reversed with [100] preparation? The paper shows two.
2. Why were the others set aside, if any were?
3. Which ranges did you measure beyond the ones shown: preparation fields above ±1 T along [100], temperatures above base, and small applied fields around zero after each preparation?
4. What does the second-best dataset look like, for example the [100] bar with histograms like Fig. 3a and 3b, or a second cooldown of the [010] bar?
5. What residual field, including its out-of-plane part, does your magnet leave at the sample after the ±1 T and ±4 T excursions along each axis, and was it measured or nulled?
6. Were both bars on the same chip in one mounting, with the [100] and [010] fields from different coils of a vector magnet? A chip tilt relative to each coil could give the same anisotropy in both bars; a 90° remount would separate crystal and magnet axes.
7. Do the preparation fields at which η changes sign in Fig. 3d match the switching fields of Reven in Fig. 4c, given that the reference bar comes from a CuMnAs wafer "with 3 nm fully oxidized Al cap" (p. 8) and was measured at 5 K?
8. How does η change with the 50 µV threshold and the 0.2 s step delay, which "was chosen empirically to minimize premature switching associated with faster current ramping" (p. 8), and what is the offset of the current-to-voltage converter?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a diode effect at fields as small as 1 Oe from asymmetric vortex barriers and Meissner screening; a field tilted 0.01° out of the film plane can fake an in-plane diode.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. A zero-field diode whose sign follows a ±1 T poling field, attributed to trapped flux; the magnet's own hysteresis (about ±15 mT) is calibrated with graphene.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Conventional Nb junctions act as zero-field diodes whose polarity is switched by trapping or removing an Abrikosov vortex.
- Li et al. 2025, "Field-Free Superconducting Diode Enabled by Geometric Asymmetry and Perpendicular Magnetization", <https://arxiv.org/abs/2506.17651>. Stray fields from a magnetized Co layer, with engineered geometric asymmetry, give a field-free diode in Nb through asymmetric vortex entry and pinning.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. A zero-field diode in Nb on compensated Mn3Pt, whose field and temperature dependence the authors say hints at several contributing mechanisms.

Happy to rerun this if you share the switching-current data and the magnet's residual-field calibration.
