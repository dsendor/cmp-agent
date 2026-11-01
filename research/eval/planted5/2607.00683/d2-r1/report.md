# Lookalike check: Facet-selective ballistic supercurrent in a weak topological insulator (arXiv 2607.00683v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library centers on zero-bias peaks, Shapiro steps and Majorana tests and has no entries for interference-pattern claims, so one library entry applies here and two rows come from outside the library, each backed by a paper I opened.

**The claim, as I read it.** Josephson junctions on exfoliated ZrTe5 (Al: Dev 1 and Dev 2, current along a; NbN: Dev 3, current along c) show SQUID-like Ic(B) oscillations at 20 mK (Fig. 4a,b; Fig. 5b), which you read as supercurrent confined to two side facets that host weak topological insulator surface states. Three further signals support it: a different pattern for in-plane By on Dev 3 (Fig. 5c), an exponential Ic(T) read as ballistic transport (Fig. 3d), and triangular lobes read as a sawtooth current-phase relation (Fig. 5b,c against Fig. 5e,f).

## Checks a careful reader will look for

The library has no ordered checks for interference or supercurrent-distribution claims, so these are the practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. You name three junctions that all show the effect: "three independent devices suggests that our results originate from intrinsic properties of ZrTe5" (p. 8). How many were fabricated and measured, and whether any were set aside, is not stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. The main text gives the measurement temperature and field directions, without the field ranges explored or why the shown windows were chosen.
3. Give the processing steps from raw data to figures, with data and code : Partly. The Js(x) extraction is referred to the supplement, "see Supplementary Note 6 for details" (p. 6), and the simulations to Supplementary Note 7; I found no data or code availability statement in the text.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: all (Dev 1, Dev 2 and Dev 3) | "This facet selectivity is robust across multiple devices and two different superconductors (Al and NbN)" (p. 2) | State how many junctions were fabricated and cooled down, how many gave SQUID-like or Fraunhofer-like patterns, and show one that gave neither cleanly. |
| Trivial edge accumulation from band bending (not in library) | Not tested (argued, not tested) | Interference followed as carrier density is tuned by a gate, looking for a bulk-to-edge (Fraunhofer-to-SQUID) transition: no; Same measurement on a junction where no topological boundary state is expected: no | "Although the observed surface-dominated supercurrent can in principle arise from trivial boundary channels due to local doping or band bending near the edges, our results are inconsistent with this picture" (p. 7) | de Vries et al. see a gate-driven Fraunhofer-to-SQUID transition in trivial InAs (https://arxiv.org/abs/1709.03727); a back-gate sweep through the Si substrate on one junction, or a reference junction on a trivial flake of similar geometry, would test it. |
| Quasi-exponential Ic(T) in a diffusive long junction (not in library) | Not tested (argued, not tested) | Ic(T) compared with diffusive long-junction theory in units of the Thouless energy: no; eRNIc product compared with the Thouless energy: no | "the ballistic nature of the supercurrent, as evidenced by the exponential temperature dependence of Ic (Fig. 3d), is incompatible with a trivial diffusive transport scenario" (p. 7) | Dubos et al. find the diffusive form "numerically very close to a simple exponential dependence" over a limited range (https://arxiv.org/abs/cond-mat/0008146); fit Fig. 3d with both forms and compare the fitted δE and eRNIc with the Thouless energy from your Hall-bar diffusion constant. |

Two notes on the rows above. For the band-bending row, your Fig. 5c already bears on it: in the By configuration, where your facet picture expects a homogeneous pattern, you find a pattern "similar to the simulations for W = 0.2-0.3, which corresponds to two edge-localized supercurrent channels that are partially merged" (p. 7), and you call the edge channels "puzzling". A reader will ask whether the same edge weight could come from the junction edges in both field directions. A density sweep on data you can take with the existing substrate would speak to this directly. For the diffusive row, the mean free path argument ("In a purely bulk scenario, the estimated mean free path is too short to support ballistic transport over the junction length", p. 6) sits in Supplementary Note 2, which I could not read; the diffusive comparison could go next to it.

## Questions about devices and data

1. How many junctions did you fabricate and measure, and how many showed SQUID-like interference? The text names three (Dev 1 to Dev 3, p. 8); the totals would help a reader.
2. Why were any others set aside, for example junctions with a Fraunhofer-like pattern or no supercurrent?
3. Which field ranges, field directions and temperatures did you measure beyond the ones shown? For example, did you measure By on Dev 1 and Dev 2, or interference patterns above 20 mK?
4. What does the second-best device or dataset look like, such as a second cooldown of one of the three junctions?
5. Did you try a back gate through the SiO2/Si substrate, and does any junction move between a Fraunhofer-like and a SQUID-like pattern as the density changes?
6. What are the fitted δE values and normal-state resistances for the three junctions in Fig. 3d, and how do δE and eRNIc compare with the Thouless energy you would get from the diffusion constant behind Supplementary Note 2?
7. Which field window and resolution went into the Js(x) profiles of Fig. 4d,e, and do the two peaks hold if the window is narrowed? For Fig. 5c, how was By aligned with the vector magnet, and how large could a residual out-of-plane component be?
8. Your simulations in Fig. 5e,f compare a sinusoidal and a sawtooth current-phase relation. How do intermediate, skewed relations look there, and how sharp must the lobes be to tell them apart from a sawtooth?

## Related work

- Hart et al. 2013, "Induced Superconductivity in the Quantum Spin Hall Edge", https://arxiv.org/abs/1312.2559. Fraunhofer-to-SQUID interference in HgTe wells as the bulk is depleted by a gate, with edge supercurrent present in 7.5 nm wells and indistinguishable from bulk in 4.5 nm wells.
- de Vries et al. 2017, "h/e superconducting quantum interference through trivial edge states in InAs", https://arxiv.org/abs/1709.03727. A SQUID pattern from trivial, band-bending edge states in non-topological InAs junctions, appearing as a top gate lowers the density.
- Allen et al. 2015, "Spatially resolved edge currents and guided-wave electronic states in graphene", https://arxiv.org/abs/1504.07630. Interferometric reconstruction of edge supercurrent in graphene near charge neutrality, interpreted as guided-wave states confined by band bending.
- Choi et al. 2019, "Evidence of Higher Order Topology in Multilayer WTe2 from Josephson Coupling through Anisotropic Hinge States", https://arxiv.org/abs/1909.02537. Edge-enhanced Josephson current along one crystal axis of WTe2 and not the other, read as hinge states.
- Dubos et al. 2000, "The Josephson critical current in a long mesoscopic S-N-S junction", https://arxiv.org/abs/cond-mat/0008146. Diffusive Nb-Cu-Nb junctions whose Ic(T) is quasi-exponential over a limited range, close to the form expected in a ballistic limit.

Happy to rerun this if you share the supplementary notes or the figure data.
