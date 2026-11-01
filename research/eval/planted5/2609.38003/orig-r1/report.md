# Lookalike check: Field-free diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your signal is a superconducting diode. The library has one entry for it. I added three explanations from other diode papers, marked "(not in library)".

**The claim, as I read it.** A 5 µm by 180 µm CuMnAs/AlAs(2 nm)/Al bar along [010] switches at unequal currents at zero applied field, with η of about 7% after zero-field cooling (Fig. 3a). The sign of η follows the sign of a ±1 T preparation field along [100], read out at H = 0 (Fig. 3b,d). Preparation along [010] gives a weak response (Fig. 3e), and a [100] bar shows the same pattern (Extended Data Fig. 4). You tie this to the remanent Néel state through Reven on a separate CuMnAs bar at 5 K (Fig. 4) and through XMLD-PEEM (Extended Data Fig. 5).

## Checks a careful reader will look for

The library has no checks for diodes, so these are the practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. You give sweep counts, "50 sweeps were acquired for each polarity, whereas for the other magnetic-field-evolution measurements the switching current for each polarity was averaged over eight sweeps" (p. 8). You show two superconducting bars and one reference bar, with no totals for bars, chips or cooldowns.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. You state the ranges shown, for example "For H100prep ranging from −5 to 5 T, Reven shows pronounced hysteresis" (p. 5). You don't give what lies beyond them, or why the [100] diode sweep stops at ±1 T while the [010] sweep goes to ±4 T (Fig. 3d,e).
3. Give the processing steps from raw data to figures, with data and code : Partly. The switching current is "defined as the bias current at which the measured voltage first exceeded a threshold of 50 µV" (p. 8). I found no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Vortex barriers and Meissner screening in the Al film | Tested in part | Plain film of the parent superconductor: no; effect against field, width or edges: part (only against preparation field and axis, in two bars) | "Neither mechanism is naturally expected to track the Néel-vector anisotropy observed here." (p. 6) | Run the Fig. 3c protocol on a plain Al bar of the same size, and show η against a few mT of applied field after each preparation sign. |
| Selection of the shown bar and settings | Tested in part | Counts: no; how the data were chosen: no; second device: all (the [100] bar) | "An orthogonal bar patterned along [100] displays the same qualitative dependence on the preparation-field axes (Extended Data Fig. 4)." (p. 4 to 5) | State how many bars and cooldowns show the [100] sign reversal, and show the [100] bar's ZFC distributions. |
| Trapped flux from the preparation field (not in library) | Tested in part | η against applied field near zero after each preparation: no; a second geometry where trapping differs: part (two in-plane axes and two bar orientations, no out-of-plane preparation) | "the anisotropic remanence itself originates in CuMnAs rather than from spurious flux trapping or vortex dynamics, both known to generate SDE28,29" (p. 6) | After a preparation, warm above the Al transition at zero field (far below 480 K), cool, and remeasure η: a Néel memory should survive, trapped flux should not. |
| Remanent field of the superconducting magnet (not in library) | Not tested (not mentioned) | Field at the sample calibrated after each preparation: no; η against small applied fields around zero: no | Not discussed. | Measure the residual field at the sample after ±1 T excursions with a Hall sensor, then show η against that offset; Jiang et al. found about ±15 mT. |
| Stray field from residual magnetization (not in library) | Tested in part | Net moment: part (wafer pieces, SQUID temperature and history not stated); stray field of the remanent texture: no; texture parallel and perpendicular to the current: all (two bars) | "this also disfavors a stray-field mechanism associated with uncompensated magnetization30" (p. 6) | Turn the SQUID bound into a field scale: by my rough estimate 3×10−3 µB/Mn is µ0M near 0.8 mT, above the 1 Oe scale of Hou et al. |

## Questions about devices and data

1. How many bars, chips and cooldowns did you measure, and how many showed a field-free diode whose sign follows the [100] preparation field?
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown: [100] preparation fields beyond ±1 T for the diode (your Fig. 3e goes to ±4 T along [010]), temperatures above base, and small applied fields around zero?
4. What does the second-best bar or cooldown look like, beyond the [100] bar in Extended Data Fig. 4?
5. What is the field at the sample at the nominal H = 0 after a ±1 T excursion, and did you calibrate the magnet's remanent field with an independent sensor? Were both bars on one chip, aligned to the same magnet coils?
6. Does the prepared diode sign survive warming the bar above the Al transition (far below the 480 K Néel temperature) and cooling again at zero field?
7. Your Fig. 3b axis runs from 16 to 23 µA, while the ZFC distributions in Fig. 3a sit near 27 to 31 µA. If the switching currents after a 1 T excursion are lower than after zero-field cooling, what sets that drop?
8. Did you take an Reven readout, or any other Néel-state readout, on the CuMnAs/AlAs/Al bar itself, in the same cryostat and magnet as the diode data?

Question 5 matters for the anisotropy argument. If both bars sit on one chip, [100] maps onto the same magnet coil for both bars. A coil-specific remanent field would then also look tied to the crystal axes. Question 8 matters because the Reven link comes from a different wafer ("a CuMnAs wafer with 3 nm fully oxidized Al cap", p. 8), a different cryostat, and 5 K ("The data were taken at 5 K.", Fig. 4).

## Related work

- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Shows strong diode effects in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening, plus a non-volatile diode with a EuS layer.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. In a non-magnetic superconductor, the sign of the zero-field diode follows a ±1 T in-plane poling field, attributed to trapped flux. They correct a magnet offset of about ±15 mT after poling using a graphene sensor.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Zero-field diodes in Nb junctions from self-field plus the stray field of a trapped Abrikosov vortex, with polarity switched by trapping or removing the vortex.
- Zapata et al. 2026, "Field-free superconducting diode and tunable vortex dynamics in NbN/FePt stripe-domain heterostructures", <https://arxiv.org/abs/2610.30556>. A 1 to 2 nm AlN spacer cuts proximity coupling, yet stray fields from remanent domains still give diode efficiencies of about 35 to 40%, depending on the domain orientation relative to the current.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. Zero-field diode efficiencies up to 50% in Nb on compensated Mn3Pt, with field and temperature dependence that hints at several mechanisms at once.

Happy to rerun this if you share the switching-current data and the magnet calibration.
