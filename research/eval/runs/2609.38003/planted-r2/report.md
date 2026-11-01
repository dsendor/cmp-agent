# Lookalike check: Reversible field-free superconducting diode effect controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library has no ordered checks for diode experiments yet, so I adapted its diode entry to your claim of antiferromagnetic control and used the general practice checks. I worked from the v1 text, with figure details from the captions.

**The claim, as I read it.** A CuMnAs/AlAs/Al bar along [010] shows a zero-field diode efficiency of about 7% after zero-field cooling (Fig. 3a); a preparation field along [100] sets its sign, up to about ±20% (Fig. 3d), and one along [010] does not (Fig. 3e). A second bar behaves the same (Extended Data Fig. 4), and a separate CuMnAs bar shows matching anisotropy and history in its nonlinear resistance at 5 K (Fig. 4), which you read as the Néel state controlling the diode.

## Checks a careful reader will look for

1. Report devices and datasets, how many showed the effect, and why others were set aside : Partly. For the second bar, "The response shows the same qualitative dependence on the preparation-field axes as the [010]-oriented bar" (p. 11, Extended Data Fig. 4); two bars are shown, with no counts of bars or cooldowns.
2. Disclose the full parameter ranges and why each was chosen : Partly. Diode data are taken "at a base temperature of 20 mK using a four-terminal configuration" (p. 8); preparation ranges are shown (Fig. 3d,e), while η versus temperature or small applied field is not.
3. Give the processing steps from raw data to figures, with data and code : Partly. The switching current is "defined as the bias current at which the measured voltage first exceeded a threshold of 50 µV" (p. 8); I found no data or code statement.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Meissner screening and asymmetric vortex barriers in a small field (diode-vortex-screening) | Partly addressed | "applying the resetting and preparation fields along the orthogonal [010] direction produces a substantially weaker response which shows no systematic reversal of the sign of the diode effect" (p. 4, Fig. 3e); the data bear on it; the paper doesn't discuss it. | Measure η versus small applied fields, in-plane and out-of-plane, a few mT either side of zero after each preparation, and run the protocol on a plain Al bar of the same width and thickness. |
| Residual field of the superconducting magnet at nominal H = 0 (not in library; Jiang et al. 2025, https://arxiv.org/abs/2512.05427) | Partly addressed | "This suggests that the anisotropy is not determined by the relative orientation of the applied field and current, but is instead tied to the underlying crystallographic axes of CuMnAs." (p. 5, Extended Data Fig. 4); a coil fixed along [100] would also follow the crystal axis. | Measure the true field at the sample with a Hall sensor or a field-symmetric reference, as Jiang et al. did, and rotate the chip 90° relative to the magnet axes. |
| Flux trapped in the Al film by the preparation field (not in library; Jiang et al. 2025, https://arxiv.org/abs/2512.05427) | Partly addressed | "Preparation along [100] reverses the diode polarity, whereas preparation along [010] produces a weaker response and leaves η predominantly of the same sign." (p. 4, Fig. 3 caption); the data bear on it; the paper doesn't discuss it. | After preparing, warm above Tc ≈ 350 mK, far below the 480 K Néel temperature, recool in a nulled field and remeasure η: this erases trapped flux and keeps the Néel state. |
| Stray field from uncompensated moments in the CuMnAs layer (micromagnet-stray-field, adapted) | Partly addressed | "which place an upper bound of (3×10−3 µB /Mn), more than an order of magnitude below that expected from a uniformly uncompensated interfacial Mn plane" (p. 3, Fig. 2b); the bound covers the average moment only. | Turn the bound into a field at the Al edges and domain walls, and measure the remanent moment by SQUID after ±1 T along [100] and [010] to see whether it switches with η. |
| A non-representative example (fine-tuning-and-selection) | Partly addressed | "Repeated current sweeps yield well-separated switching-current distributions for the two current directions (inset of Fig. 3a)" (p. 3); this covers switching noise in one bar and one state. | Report bars, chips and cooldowns, repeat the Fig. 3d loop, and show the second bar's raw switching currents. |

The most useful single check is likely a thermal cycle: Al loses superconductivity at 350 mK while CuMnAs stays ordered to 480 K (p. 3), so a prepared η that survives warming above Tc and recooling in a measured zero field would answer both flux rows at once. Jiang et al. had to correct for about 15 mT of magnet hysteresis after ±1 T, so the field calibration matters for any "H = 0" protocol. By my rough arithmetic your SQUID bound still allows µ0M of about 0.8 mT, while Hou et al. see a diode in plain films at 1 Oe. Your reference list includes refs. 28 to 30 (Hou, Jiang, Li), but I couldn't find where the v1 text cites them; a short discussion there would answer much of this table.

## Questions about devices and data

1. How many CuMnAs/Al bars did you measure, on how many chips and in how many cooldowns, and how many showed the remanent reversal of Fig. 3d?
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown: η versus temperature, η versus small applied field, larger preparation fields along [100], and repeated loops?
4. What does the second-best device or dataset look like, for example the Fig. 3d loop after a new cooldown?
5. What is your magnet's residual field at nominal H = 0 after the ±1 T and ±4 T excursions, how was zero calibrated, and is the crystal [100] axis along the same coil for both bars?
6. At what temperature was the preparation field applied, and does the prepared η survive warming above 350 mK and recooling in a nulled field?
7. Could you read out the Néel state on the superconducting heterostructure itself, since Fig. 4 uses a separate wafer at 5 K?
8. After preparation along [010], η stays predominantly of one sign (Fig. 3e): what sets that sign, and does it match the 7% after zero-field cooling?

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A diode in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. A zero-field diode whose sign is set by a poling field applied before measurement, attributed to trapped flux.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Zero-field diodes in Nb junctions from self-field plus a trapped Abrikosov vortex, switched by trapping or removing it.
- Li et al. 2025, "Field-Free Superconducting Diode Enabled by Geometric Asymmetry and Perpendicular Magnetization", <https://arxiv.org/abs/2506.17651>. A field-free diode in Pt/Co/Nb from geometric asymmetry and a magnetic layer's stray fields.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. A zero-field diode in Nb on compensated Mn3Pt, with field and temperature dependence hinting at several mechanisms.

Happy to rerun this if you share the figure data.
