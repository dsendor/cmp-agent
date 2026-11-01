# Lookalike check: Facet-selective ballistic supercurrent in ZrTe5 (arXiv 2607.00683v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library has no entries for edge-localized supercurrent seen in interference patterns, so I used its practice checks and its selection entry, and I added two lookalikes from papers I opened, marked "(not in library)". I worked from the extracted main text only, without the PDF or the Supplementary Information, so figure details come from the captions.

**The claim, as I read it.** Your Al/ZrTe5 junctions (Dev 1 and Dev 2, Fig. 4a,b) and the NbN/ZrTe5 junction (Dev 3, Fig. 5b) show SQUID-like Ic(B) at 20 mK, which you read as supercurrent confined to two side facets that host weak topological insulator surface states. Two further results support this reading: the By pattern of Dev 3 (Fig. 5c) differs from its Bz pattern, and you read the exponential Ic(T) in Fig. 3d and the sharp lobes in Fig. 5b,c as ballistic transport.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "three independent devices" (p. 8). The text doesn't say how many junctions were fabricated or measured.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. You note that the Js(x) widths depend on "the finite magnetic-field range of the measured interference pattern" (p. 7), but the text gives no measured field range.
3. Give the processing steps from raw data to figures, with data and code : Partly. The Js(x) extraction is deferred: "see Supplementary Note 6 for details" (p. 6). The main text has no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; how the shown data were chosen: no; a second device or dataset shown: part | "First, SQUID-like patterns appear for two separate Al/ZrTe5 devices." (p. 7, Fig. 4a,b). The By contrast and the sharp lobes come from Dev 3 alone. | State how many junctions you measured, and show a second junction in the By orientation. |
| Trivial edge accumulation from band bending (not in library; de Vries et al. 2018) | Not tested (argued, not tested) | Fermi level tuned through the bulk-to-edge transition: no; same measurement on a reference junction where no topological state is expected: no | "Although the observed surface-dominated supercurrent can in principle arise from trivial boundary channels due to local doping or band bending near the edges, our results are inconsistent with this picture based on the following three observations." (p. 7) | Sweep the Si back gate while you follow the Dev 1 or Dev 2 pattern. The By data of Dev 3 (Fig. 5c) already bear on it. |
| Quasi-exponential Ic(T) of a long diffusive junction (not in library; Dubos et al. 2001) | Tested in part | Diffusive long-junction form fitted next to the ballistic one: no; fitted energy compared with an independent estimate: part (the mean free path estimate is in Supplementary Note 2, which I didn't have) | "In a purely bulk scenario, the estimated mean free path is too short to support ballistic transport over the junction length (Supplementary Note 2)" (p. 6, Fig. 3d) | Fit Fig. 3d with both forms over the same range, and compare the fitted level spacing with hbar v_F / L. |

## Questions about devices and data

1. How many ZrTe5 junctions did you fabricate and measure, and how many showed SQUID-like interference? The text names three (Dev 1, Dev 2, Dev 3).
2. Why were any others set aside, and how did you choose which datasets of Dev 1, Dev 2 and Dev 3 to show?
3. Which field ranges (Bz, By and other angles) and temperatures did you measure beyond those in Figs. 3 to 5, and how wide was the field range used for the Js(x) reconstruction in Fig. 4d,e?
4. What does the second-best device or dataset look like, in particular a second junction measured with By as in Fig. 5c?
5. How does the diffusive long-junction form of Dubos et al. fit Fig. 3d over the same temperature range as your ballistic fit, and how do the fitted level spacings compare with hbar v_F / L for each device?
6. Could you sweep the Si back gate under the SiO2 to move the Fermi level and follow the SQUID-like pattern of Dev 1 or Dev 2, to see whether the edge peaks track band bending at the etched edges?
7. The Fourier reconstruction of Js(x) assumes a sinusoidal current-phase relation and near-longitudinal Andreev trajectories; how do these assumptions hold in long junctions where you report a sawtooth current-phase relation, and does a reconstruction with a sawtooth kernel move the edge peaks in Fig. 4d,e?
8. How did you align the vector magnet for the Bz and By sweeps of Dev 3, and how much does a small misaligned field component change the patterns in Fig. 5b,c?

A few notes on why I ask these. Edge accumulation from band bending is the explanation a reader will reach for first, and you raise it yourself on p. 7. De Vries et al. saw a SQUID pattern in plain InAs junctions as they tuned the Fermi level toward the bulk gap. Your three counterarguments are reproducibility, the By contrast and ballistic Ic(T). None of them moves the Fermi level, and your devices sit on SiO2/Si, so a back gate may already be available. Your own text says the By pattern shows "the appearance of edge channels is puzzling" (p. 7). That makes the By data the dataset readers will look at most closely for this question.

The ballistic argument rests on Fig. 3d. Dubos et al. show that a diffusive long junction gives a temperature dependence that is, over a limited range, "numerically very close to a simple exponential dependence". A fit of both forms to the same points, with the fitted energies placed next to independent estimates, would let the ballistic reading stand on the data. The same applies to the lobe shape: comparing the measured lobes with simulations in Fig. 5e,f is a good start, and a reader will also want to know whether the reconstruction in Fig. 4d,e stays valid with a non-sinusoidal kernel.

## Related work

- de Vries et al. 2018, "h/e superconducting quantum interference through trivial edge states in InAs", <https://arxiv.org/abs/1709.03727>. A SQUID pattern from supercurrent along trivial, band-bent edges in non-topological InAs junctions, with a gate-tuned crossover from bulk to edge transport.
- Dubos et al. 2001, "The Josephson critical current in a long mesoscopic S-N-S junction", <https://arxiv.org/abs/cond-mat/0008146>. A quantitative Ic(T) study of diffusive Nb-Cu-Nb junctions, scaled by the Thouless energy. Over a limited range the diffusive curve looks like the ballistic exponential.
- Suominen et al. 2017, "Anomalous Fraunhofer Interference in Epitaxial Superconductor-Semiconductor Josephson Junctions", <https://arxiv.org/abs/1611.00190>. In trivial InAs junctions, flux focusing makes the node spacing aperiodic, and an in-plane field strengthens higher nodes, which looks like current flowing along the edges.
- Allen et al. 2016, "Spatially resolved edge currents and guided-wave electronic states in graphene", <https://arxiv.org/abs/1504.07630>. Fourier reconstruction of interference patterns in graphene shows edge-guided supercurrent near charge neutrality, interpreted as states confined by band bending.
- Frolov et al. 2023, ""Smoking gun" signatures of topological milestones in trivial materials by measurement fine-tuning and data postselection", <https://arxiv.org/abs/2309.09368>. Trivial devices reproduce accepted topological signatures through fine-tuning and data selection.

Happy to rerun this if you share the Supplementary Information and the figure data.
