# Lookalike check: Facet-selective ballistic supercurrent in a weak topological insulator (arXiv 2607.00683v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is Josephson interferometry on a 3D crystal, which the library's signal families (zero-bias peaks, Shapiro steps, Kitaev chains and others) don't cover, so only the practice entries apply and the other rows come from papers I opened outside the library.

**The claim, as I read it.** In Al/ZrTe5 and NbN/ZrTe5 junctions the supercurrent flows mainly along two side facets that host weak topological insulator surface states. The evidence is SQUID-like, flux-quantum-periodic Ic(B) with two-peaked Js(x) (Fig. 4, Dev 1 and Dev 2; Fig. 5b, Dev 3), a different pattern for in-plane By (Fig. 5c, Dev 3), and ballistic transport read from an exponential Ic(T) (Fig. 3d, three devices) and from sharp lobes (Fig. 5b,c).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "three independent devices suggests that our results originate from intrinsic properties of ZrTe5" (p. 8); the text doesn't say how many junctions were made or measured.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. The text says the reconstruction is limited by the field range (p. 7) but doesn't give the ranges measured or why the shown ones were chosen.
3. Give the processing steps from raw data to figures, with data and code : Partly. "see Supplementary Note 6 for details" (p. 6); the main text gives no Ic criterion and no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: part | "This facet selectivity is robust across multiple devices and two different superconductors (Al and NbN)" (p. 2); the By pattern and the sharp lobes come from Dev 3 alone. | Give the number of junctions made and measured, and show By data and lobe shape for Dev 1 or Dev 2, or for a second NbN junction. |
| Trivial edge channels from band bending (not in library; de Vries et al., https://arxiv.org/abs/1709.03727) | Not tested (argued, not tested) | Edge and bulk weight followed with a gate: no; Same interferometry on a trivial junction: no | "our results are inconsistent with this picture based on the following three observations" (p. 7); the trivial InAs edge junctions in de Vries et al. were also quasi-ballistic. | Follow Js(x) against density with a back gate, and say whether the partially merged By channels at the gapped a–c surfaces (Fig. 5c) could come from band bending at the substrate and contacts. |
| Diffusive long-junction Ic(T) that looks exponential (not in library; Dubos et al., https://arxiv.org/abs/cond-mat/0008146) | Not tested (argued, not tested) | Usadel fit over the full temperature range: no; eIcRN compared with the Thouless energy: no | "is incompatible with a trivial diffusive transport scenario" (p. 7); Dubos et al. find the diffusive form close to a simple exponential over a limited range (p. 3). | Fit Fig. 3d with both forms over the full range, and give RN, eIcRN and the Thouless energy next to the fitted δE. |
| Triangular lobes from loop or kinetic inductance (not in library; Friedrich et al., https://arxiv.org/abs/1908.11067) | Not tested (not mentioned) | Inductance and screening parameter estimated: no; Modulation depth compared with what the screening parameter predicts: no | Not discussed; the sharp lobes are read as a sawtooth current-phase relation (p. 7, Fig. 5f). | Estimate loop and kinetic inductance of the NbN and Al leads, compare the modulation depth with the screening parameter, and show lobe shape against temperature. |
| Aspect-ratio dependent pattern of a uniform junction (not in library; Chiodi et al., https://arxiv.org/abs/1201.3509) | Tested in part | Uniform-current model with the junction aspect ratio: part (compared with a uniform profile in your model, Fig. 5f, whose aspect ratio the main text doesn't give); Junctions of different aspect ratio compared: no | "a homogeneous supercurrent producing a pattern like that shown in the bottom panel of Fig. 5f is therefore expected" (p. 7) | Give the length, width and flake thickness of Dev 3, and compare Fig. 5c with a uniform-current 2D model at that aspect ratio, where a narrow junction decays monotonically. |

## Questions about devices and data

1. How many ZrTe5 junctions did you fabricate and measure, and how many showed SQUID-like patterns?
2. Why were the others set aside, if any were?
3. Which field ranges, field directions and temperatures did you measure beyond the ones shown, for example By on Dev 1 and Dev 2, or interference patterns above 20 mK?
4. What does the second-best junction or cooldown look like, for example one with a more Fraunhofer-like pattern?
5. In your Fig. 5c the two partially merged channels sit at the top and bottom a–c surfaces, which are gapped in a WTI. Can you tune the Fermi level with the Si substrate as a back gate, and follow the edge and bulk weight in Js(x) with density, to separate these from band bending at the substrate and contact interfaces?
6. Does the diffusive long-junction form fit your Fig. 3d as well as the ballistic exponential, and what are RN, eIcRN and the fitted δE next to the Thouless energy?
7. What are the estimated loop and kinetic inductances of the NbN and Al leads (the screening parameter), and do the lobes in your Fig. 5b,c round off as temperature lowers Ic?
8. What are the length, width and flake thickness of Dev 3, how was Ic extracted from the V(I) curves, and how does a uniform-current model at the Dev 3 aspect ratio compare with your Fig. 5c?

## Related work

- de Vries et al. 2018, "h/e superconducting quantum interference through trivial edge states in InAs", <https://arxiv.org/abs/1709.03727>. Non-topological InAs Josephson junctions show a SQUID pattern from edge transport, with Fermi-level pinning and band bending at the etched edge.
- Allen et al. 2016, "Spatially resolved edge currents and guided-wave electronic states in graphene", <https://arxiv.org/abs/1504.07630>. Fourier reconstruction of interferometry in graphene junctions shows edge currents near charge neutrality, which the authors read as guided waves confined by band bending.
- Dubos et al. 2001, "The Josephson critical current in a long mesoscopic S-N-S junction", <https://arxiv.org/abs/cond-mat/0008146>. In diffusive Nb-Cu-Nb junctions the high-temperature Ic(T) is numerically close to a simple exponential, as one would expect from a ballistic junction.
- Chiodi et al. 2012, "Geometry-related magnetic interference patterns in long SNS Josephson junctions", <https://arxiv.org/abs/1201.3509>. Changing the normal wire's geometry tunes Ic(Φ) from a monotonic Gaussian-like decay to a Fraunhofer-like pattern.
- Friedrich et al. 2019, "Onset of phase diffusion in high kinetic inductance granular aluminum micro-SQUIDs", <https://arxiv.org/abs/1908.11067>. A large kinetic loop inductance reduces the switching-current modulation and distorts it toward a triangular shape.

Happy to rerun this with the Supplementary Information or the figure data.
