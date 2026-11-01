# Lookalike check: Field-free diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a superconducting diode measurement. The library has one diode entry and no diode-specific checks, so I used the practice checks and adapted one stray-field entry written for zero-bias peaks.

**The claim, as I read it.** A 5 µm by 180 µm CuMnAs/AlAs(2 nm)/Al bar along [010] shows a zero-field diode effect after zero-field cooling, with η of about 7% (Fig. 3a). The polarity reverses with the sign of a [100] preparation field, reaching about ±20%, and barely responds to [010] preparation (Fig. 3b, d, e). A [100] bar behaves the same way (Extended Data Fig. 4). You tie this to the Néel state using the even nonlinear resistance of a separate CuMnAs bar at 5 K (Fig. 4) and XMLD-PEEM (Extended Data Fig. 5).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. You name the two diode bars and the 1.5 nm reference stack, but not how many bars or cooldowns there were in total.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. The field ranges are given, "For H100 prep ranging from −5 to 5 T, Reven shows pronounced hysteresis" (p. 5), and one setting is explained, "this value was chosen empirically to minimize premature switching" (p. 8). All diode data are at 20 mK, and you don't say why the [100] diode preparation stops at ±1 T.
3. Give the processing steps from raw data to figures, with data and code : Partly. The switching criterion is stated: "defined as the bias current at which the measured voltage first exceeded a threshold of 50 µV" (p. 8). So are the eight-sweep averaging and the Reven formula. I found no statement on data or code availability.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Meissner screening and asymmetric vortex edge barriers in the Al film (diode-vortex-screening) | Tested in part | Same measurement on a plain film or junction of the parent superconductor: no; Effect followed against field, sample width or edge quality: part (preparation-field history only, with readout always at H = 0) | "the anisotropic remanence itself originates in CuMnAs rather than from spurious flux trapping or vortex dynamics, both known to generate SDE28,29" (p. 6) | Sweep a few mT, in plane and out of plane, through zero at readout, and measure a bare Al bar from a matched growth. |
| Stray field from uncompensated moments (adapted from micromagnet-stray-field) | Tested in part | Magnet switching (hysteresis in field): all (no loop in the CuMnAs M(H), Fig. 2b); Stray field mapped or bounded: part (a wafer-averaged bound, with no figure for the field at the bar); Comparison with devices without magnets: no | "this also disfavors a stray-field mechanism associated with uncompensated magnetization30" (p. 6) | Bound the moment on the patterned bar itself, for example from its normal-state Hall signal, and compare with an Al bar without CuMnAs. |
| Selection and fine-tuning (fine-tuning-and-selection) | Tested in part | Devices and datasets measured, and how many showed the effect: no; How the shown data were chosen: no; A second device or dataset shown: part (Extended Data Fig. 4 covers the remanent control only) | "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)" (pp. 4-5) | Report the counts. Show the [100] bar after zero-field cooling, and Fig. 3d from a second cooldown. |
| Trapped flux set by the preparation field (not in library; Jiang et al. 2025) | Tested in part | Switching currents mapped against applied field through zero after each preparation field: no; Preparation-field direction compared, in plane and out of plane: part (two in-plane axes only); Trapped flux imaged directly: no | "Neither mechanism is naturally expected to track the Néel-vector anisotropy observed here." (p. 6) | Between preparation and readout, warm above 350 mK at H = 0 and recool. That releases trapped flux and leaves the Néel state (480 K) in place. |
| Residual field of the superconducting magnet at nominal H = 0 (not in library; Jiang et al. 2025) | Not tested (not mentioned) | Field at the sample after each excursion calibrated with a hysteresis-free sensor: no | Not discussed. | Calibrate the field at the sample for each magnet axis after each excursion (a Hall sensor works), or demagnetize the magnet before readout. |

## Questions about devices and data

1. How many CuMnAs/AlAs/Al bars did you fabricate and measure, over how many cooldowns, and how many showed a zero-field diode and the remanent reversal of Fig. 3d?
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown: temperatures above 20 mK, current ramps other than the 0.2 s step delay, and diode preparation fields along [100] beyond ±1 T (your Fig. 4c goes to ±5 T)?
4. What does the second-best device or dataset look like, for example the zero-field-cooled switching distributions of the [100] bar, or Fig. 3d repeated in a second cooldown?
5. What is the field at the sample at nominal H = 0 after each excursion, for each magnet axis, and how does η respond to a small applied field (a few mT, in plane and out of plane) swept through zero?
6. Did you warm above the 350 mK transition at H = 0 between preparation and readout, and does the diode polarity survive that? Relatedly, what sets the drop from about 27 and 31 µA after zero-field cooling (Fig. 3a inset) to about 17 to 21 µA after the ±1 T preparations (Fig. 3b)?
7. Your η reverses within about 0.1 T of preparation field (Fig. 3d), while Reven reverses near ±1.3 T (Fig. 4c), measured at 5 K on a bar from a different wafer. Could you comment on the different field scales, and on Extended Data Fig. 4a, where η after +1 T sits near −4%?
8. Were the [010] and [100] bars on the same chip and mounting, so that [100] lies along the same magnet coil for both, and have you repeated Fig. 3d with the chip rotated relative to the magnet axes?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a strong diode effect at fields as small as 1 Oe, from Meissner screening and asymmetric vortex barriers.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. In a nonmagnetic superconductor, the sign of a zero-field diode follows a ±1 T poling field through trapped flux. The authors also correct for a magnet hysteresis of about ±15 mT.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. In conventional Nb junctions, a trapped Abrikosov vortex together with the bias self-field gives a zero-field diode whose polarity can be switched.
- Li et al. 2025, "Field-Free Superconducting Diode Enabled by Geometric Asymmetry and Perpendicular Magnetization", <https://arxiv.org/abs/2506.17651>. In Pt/Co/Nb, stray fields from a perpendicular magnet plus geometric asymmetry give a field-free diode through vortex entry and pinning.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. Nb on compensated Mn3Pt shows a zero-field diode, with efficiencies up to 50%, that depends on the magnetic phase.

Happy to rerun this if you share the switching-current data behind Fig. 3 and Extended Data Fig. 4.
