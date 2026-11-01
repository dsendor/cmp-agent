# Lookalike check: Josephson diode effect in FeTe0.55Se0.45 van der Waals junctions (arXiv 2610.29124v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a diode and Shapiro-step study of a vertical van der Waals junction. The library has no ordered checks for diode signals or half-integer steps, so I adapted its thin-film diode entry to a junction, added three lookalikes from papers I opened, and used the general practice checks.

**The claim, as I read it.** You report a zero-field Josephson diode in one FTS vdW junction: "|Ic+| = 35.2 μA and |Ic−| = 28.9 μA", η = 9.8% (p. 7, Fig. 2a-b). You also report an η(Bx) that is antisymmetric about Bx = −8 G (Fig. 2c-d), a hysteretic Fraunhofer pattern and a field-independent 170 μV feature (Fig. 3), and asymmetric half-integer Shapiro steps at Bx = 75 G (Fig. 4, Supplementary Figs. 6-7). You trace all of these to coupling between interfacial magnetization and the Josephson current, reproduced with RCSJ + LLG simulations.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. The abstract says "Our devices exhibit a robust zero-field diode response with asymmetric switching currents" (p. 2), but every dataset I could trace is from "the same junction" (p. 7, also p. 31), and no count is given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. You give the reason for the Shapiro field: "We therefore performed Shapiro-step measurements at Bx = 75 G, near the first Fraunhofer node, where the JDE remains pronounced while the MR induced voltage feature is strongly suppressed." (p. 12). The shown ranges are stated: Bx to ±100 G (Fig. 2c), ±200 G (Fig. 3), 0 to 5 K (Supplementary Fig. 1b) and four frequencies at 75 G. The field-sweep history before each dataset and any ranges beyond these are not.
3. Give the processing steps from raw data to figures, with data and code : Partly. You describe the switching criterion ("a threshold of 10 μV", p. 16), the voltage binning (p. 16) and the FFT filter (p. 28). Data are "available from the corresponding authors upon reasonable request" (p. 17), and no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Meissner screening and asymmetric vortex barriers in the electrodes (library entry for films, adapted to a junction) | Tested in part | Same measurement on a plain film or junction of the parent superconductor: no; Effect followed against field, sample width or edge quality: all (field, Fig. 2c-d; temperature, Supplementary Fig. 1b) | "the observed zero-field diode response is unlikely to originate from the bulk crystal alone" (p. 7) | Measure Ic± versus Bx on a single FTS flake or a constriction on the same chip, and compare its η(Bx) with Fig. 2d. |
| Self-field from nonuniform bias, shifted to zero field by trapped flux (not in library; Golod and Krasnov 2022) | Tested in part | Diode polarity compared for another bias configuration: no; Nonreciprocity with trapped flux removed and deliberately trapped: part (one zero-field-cooled state, no comparison) | "show similar overall patterns symmetric around Bx = −8 G" (p. 7, Fig. 2c) | Bias through another contact pair and see whether η flips; warm above Tc,FTS, cool at a compensated true zero, and see whether B0 and the zero-field η stay. |
| Trapped vortices from remanent field or field history (not in library; Zhu et al. 2025) | Not tested (argued, not tested) | Half-integer steps compared across thermal cycles above Tc: no; Steps compared after field sweeps from opposite directions: no; Remanent field at the sample measured: no | "revealing a hysteretic response that is absent in conventional non-magnetic Josephson junctions" (pp. 9-10, Fig. 3a) | Repeat the 75 G Shapiro map after a thermal cycle and after approaching 75 G from the other side; report the magnet's remanent field at the sample. |
| Interference with a second current path (not in library; Kalashnikov et al. 2025) | Not tested (data bear on it) | Shapiro step asymmetry followed in field for oscillation with the second path's period: no | "This feature may arise from an additional transport channel operating in parallel with the dominant Josephson current across the vdW interface" (p. 8) | Take Shapiro maps at a few fields across one 11 G period near 75 G and see whether the ±1/2 asymmetry follows that period. |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: no; How the shown data were chosen: part (the 75 G choice is explained); A second device or dataset shown: part (other frequencies and Bx = 0 on the same junction, no second junction) | "measured at 4.348, 7.580, and 9.680 GHz consistently exhibit integer and asymmetric half-integer Shapiro step structures" (p. 35, Supplementary Fig. 6) | State how many junctions were made and measured, and show the second-best junction's Fig. 2c-d. |

## Questions about devices and data

1. How many junctions did you fabricate and measure, and how many showed the zero-field diode, the hysteretic Fraunhofer pattern, the 170 μV feature and the asymmetric half-integer steps? The abstract says "Our devices", and the figures appear to come from one junction.
2. Why were the others set aside?
3. Which ranges of field (sweep amplitude and direction), temperature, microwave frequency and power did you measure beyond the ones shown, and over how many cooldowns?
4. What does the second-best junction or dataset look like?
5. What is the remanent field of the vector magnet at the sample after the sweeps you used, and does the symmetry point B0 = −8 G of η(Bx) (Fig. 2c, Supplementary Fig. 1b) stay where it is after warming above Tc,FTS and cooling at a compensated zero field? At Bx = 0 the junction sits 8 G from B0, so this tells a reader how much of the zero-field η = 9.8% comes from an offset field.
6. Which contacts carry the bias current into the top and bottom flakes, and does the diode polarity change when you feed the current through another contact pair?
7. Which field history preceded the Bx = 75 G Shapiro data, and do the half-integer steps and their ±1/2 asymmetry survive a thermal cycle above Tc,FTS or an approach to 75 G from the opposite field direction?
8. Near 75 G, does the ±1/2 asymmetry change with field on the roughly 11 G period of the fast Fraunhofer component?

## Related work

- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Conventional Nb planar junctions give a zero-field diode from the self-field of nonuniform bias plus stray fields of a trapped Abrikosov vortex; polarity switches with bias configuration and with trapping or removing the vortex.
- Zhu et al. 2025, "Manipulating fractional Shapiro steps in twisted cuprate Josephson junctions", <https://arxiv.org/abs/2512.01586>. In stacked vdW cuprate junctions, half-integer steps vanish with thermal cycling and return after small-field training, with field-sweep hysteresis the authors tie to trapped vortices.
- Kalashnikov et al. 2025, "Diode effect in Shapiro steps in an asymmetric SQUID with a superconducting nanobridge", <https://arxiv.org/abs/2510.15526>. Strong Shapiro step asymmetry with only a weak critical-current diode, oscillating with the SQUID period, from two parallel paths with ordinary current-phase relations.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A diode effect in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex barriers and Meissner screening.
- Qiu et al. 2023, "Concurrent Ferromagnetism and Superconductivity in Fe(Te,Se) van der Waals Josephson Junctions", <https://arxiv.org/abs/2303.00966>. FTS vdW junctions with magnetic hysteresis only below Tc and a stochastic field-free diode, read as interfacial ferromagnetism.

Happy to rerun this if you share the switching-current and Shapiro data together with the field-sweep log.
