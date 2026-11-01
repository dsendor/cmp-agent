# Lookalike check: Field-free diode controlled by an antiferromagnet (arXiv 2609.38003v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your claim is magnetic control of a diode in a conventional superconductor, so I used the library's diode and practice entries, adapted one stray-field entry, and added two lookalikes from outside it. I worked from the text and captions only.

**The claim, as I read it.** A 5 µm by 180 µm CuMnAs/AlAs/Al bar along [010] shows a zero-field diode efficiency of about 7% after zero-field cooling (Fig. 3a). After a preparation field along [100], the sign of η at H = 0 follows that field and approaches ±20% (Fig. 3b,d); [010] preparation gives a weak, non-reversing response (Fig. 3e). You tie this to the Néel state through the matching anisotropy and hysteresis of Reven in a reference CuMnAs bar at 5 K (Fig. 4) and XMLD-PEEM (Extended Data Fig. 5).

## Checks a careful reader will look for

The library has no diode checks yet, so its general practice checks apply.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "An orthogonal bar patterned along [100] displays the same qualitative dependence" (p. 4, Extended Data Fig. 4). The number of bars, chips and cooldowns measured isn't stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Preparation ranges appear in Fig. 3d,e, and for Reven "ranging from −5 to 5 T, Reven shows pronounced hysteresis" (p. 5). η appears at base temperature only and never against small applied fields; the reasons for each range aren't given.
3. Give the processing steps from raw data to figures, with data and code : Partly. The switching current is "defined as the bias current at which the measured voltage first exceeded a threshold of 50 µV" (p. 8), and sweep counts are given; I found no data or code availability statement.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Vortex barriers and Meissner screening in the Al film (diode-vortex-screening) | Partly addressed | "the anisotropic remanence itself originates in CuMnAs rather than from spurious flux trapping or vortex dynamics" (p. 6); the data bear on the remanence, and a plain Al control isn't shown. | Measure η against small applied fields near zero along [100], [010] and out of plane, and run a plain Al bar through the Fig. 3c protocol. |
| Flux trapped by the preparation field (not in library; Jiang et al., https://arxiv.org/abs/2512.05427) | Partly addressed | "Neither mechanism is naturally expected to track the Néel-vector anisotropy observed here." (p. 6) | After each excursion, warm above Tc (about 350 mK, far below the 480 K Néel temperature), cool at H = 0, then read η; a sign that survives points away from flux in the Al. |
| Remanent field of the superconducting magnet (not in library; Jiang et al., https://arxiv.org/abs/2512.05427) | Not addressed | Not discussed. | Calibrate the field at nominal H = 0 after each excursion with a Hall sensor or a field-even reference, and check whether η(H) curves after ±1 T are shifted copies of each other. |
| Stray fields from residual or domain magnetization in CuMnAs (micromagnet-stray-field, adapted) | Partly addressed | "this also disfavors a stray-field mechanism associated with uncompensated magnetization" (p. 6, Fig. 2b) | Measure the SQUID moment at low temperature after the same ±1 T preparation, and estimate the local field from the domain texture in Extended Data Fig. 5. |
| Fine-tuning and data selection (fine-tuning-and-selection) | Partly addressed | "An orthogonal bar patterned along [100] displays the same qualitative dependence" (p. 4, Extended Data Fig. 4) | State how many bars and cooldowns you measured, show a repeat of the Fig. 3d loop, and show the [100] bar's switching-current distributions. |

## Questions about devices and data

1. How many bars, chips and cooldowns did you measure, and how many showed the zero-field diode and its reversal with preparation field? The paper shows two bars (Fig. 3 and Extended Data Fig. 4).
2. Why were any others set aside?
3. Which ranges did you measure beyond the ones shown: preparation fields above ±1 T along [100], η against small applied fields near zero, and temperatures between 20 mK and Tc? Does η change with the 50 µV threshold or the 0.2 s step delay?
4. What does the second-best dataset look like, for example a repeat of the Fig. 3d loop, or the switching-current distributions and Fig. 3b-type data for the [100] bar?
5. Did the bar stay below Tc between each preparation excursion and the readout at H = 0, and what happens to η if you warm above Tc and cool back at zero field before reading it?
6. What is the field at the sample at nominal H = 0 after the ±1 T and ±4 T excursions, and how did you calibrate it? Was the magnet in a known state before the zero-field cooldown of Fig. 3a?
7. Were the [010] and [100] bars on the same chip, so that the [100] axis lay along the same magnet coil in both? A cooldown with the chip turned by 90° would separate the crystal axis from the magnet axis.
8. At what temperature and field history was the SQUID bound of Fig. 2b taken, and does the 2 nm heterostructure itself show the Fig. 4 hysteresis? The reference bar came from "a CuMnAs wafer with 3 nm fully oxidized Al cap" (p. 8).

## Related work

- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a diode effect at fields as small as 1 Oe from asymmetric vortex barriers and Meissner screening.
- Jiang et al. 2025, "Zero-field superconducting diode effect induced by magnetic flux in a van der Waals superconductor trigonal PtBi2", <https://arxiv.org/abs/2512.05427>. In a nonmagnetic superconductor, a ±1 T in-plane poling field sets the sign of the zero-field diode, which they attribute to trapped flux; they correct a magnet hysteresis of about ±15 mT with a graphene reference.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. A trapped Abrikosov vortex in Nb planar junctions gives a zero-field diode whose polarity can be switched and remembered.
- Zapata et al. 2026, "Field-free superconducting diode and tunable vortex dynamics in NbN/FePt stripe-domain heterostructures", <https://arxiv.org/abs/2610.30556>. A field-free diode from remanent stripe-domain stray fields persists through an AlN spacer that reduces proximity coupling.
- Sachin et al. 2026, "Altermagnetic Superconducting Diode Effect in Mn3Pt/Nb Heterostructures", <https://arxiv.org/abs/2601.03366>. Nb on compensated and nearly compensated Mn3Pt shows a zero-field diode with efficiencies up to 50%.

Happy to rerun this if you share the figure data or the field-calibration runs.
