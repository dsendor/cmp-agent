# Lookalike check: Facet-selective ballistic supercurrent in ZrTe5 (arXiv 2607.00683v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper uses supercurrent interferometry to locate where current flows. The library is built around zero-bias peaks, Shapiro steps and similar signals, so only its general entry on data selection applies directly. The other two rows below come from papers I opened, and they are marked "(not in library)".

**The claim, as I read it.** You show SQUID-like Ic(B) oscillations with flux-quantum period in two Al/ZrTe5 junctions (Fig. 4a,b, Dev 1 and 2) and one NbN/ZrTe5 junction (Fig. 5b, Dev 3), and you read them as supercurrent confined to the a–b side facets that carry the weak topological insulator's surface states. You support this with a different pattern for in-plane field (Fig. 5c), an exponential Ic(T) read as ballistic transport (Fig. 3d), and sharp lobes read as a sawtooth current-phase relation (Fig. 5b,c).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. You name three junctions, "three independent devices" (p. 8), and earlier "robust across multiple devices" (p. 2). The text gives no number for the junctions fabricated or measured, and none for cooldowns.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. The captions for Figs. 4 and 5 give no field range. The text notes the reconstruction "is limited by the finite magnetic-field range of the measured interference pattern" (p. 7), so the range you measured matters to the reader.
3. Give the processing steps from raw data to figures, with data and code : Partly. The Js(x) extraction is described in "Supplementary Note 6" (p. 6), and Fig. 2b,c show ΔRxx "after background subtraction" (Fig. 2 caption). I found no statement in the text about data or code availability.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection of a non-representative example | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: all | "SQUID-like patterns appear for two separate Al/ZrTe5 devices" (p. 7), plus Dev 3 in Fig. 5b | State how many junctions were made and measured, and how many gave SQUID-like or Fraunhofer-like patterns |
| Trivial edge accumulation channels (not in library; de Vries et al. 2018) | Not tested (argued, not tested) | Fermi level tuned with a gate while following the edge supercurrent: no; Same interferometry on a trivial reference junction made the same way: no | "our results are inconsistent with this picture based on the following three observations" (p. 7) | Make a junction on a trivial reference crystal with the same ion milling and Pd/Al process, or add a gate and follow Js(x) as the bulk density changes |
| Diffusive long junction with a quasi-exponential Ic(T) (not in library; Dubos et al. 2001) | Tested in part | Ic(T) fitted with the diffusive long-junction form next to the ballistic fit: no; Fitted energy scale checked against independent parameters: part (mean free path estimate in Supp. Note 2, which is not in the text I had) | "is incompatible with a trivial diffusive transport scenario" (p. 7); "the estimated mean free path is too short to support ballistic transport over the junction length" (p. 6) | Fit the Fig. 3d data with both forms over the whole temperature range and compare the δE or Thouless energy you get with the junction lengths in Table S1 |

## Questions about devices and data

1. How many Josephson junctions did you fabricate and measure, and how many showed SQUID-like patterns? The text says "multiple devices" (p. 2) and "three independent devices" (p. 8); if three were measured and three showed it, saying so would settle this.
2. If any junctions were set aside, why?
3. Which field ranges and field angles did you measure beyond those shown in Figs. 4 and 5, and did you measure the in-plane orientation (By) on Dev 1 and Dev 2 as well?
4. What does the second-best junction look like, and did any junction show a Fraunhofer-like pattern?
5. Without a gate, how do you tell topological facet states from accumulation layers at the ion-milled flake edges? A junction made the same way on a trivial reference crystal, or a gated device that depletes the bulk, would separate the two.
6. In Fig. 5c the two partly merged channels lie along the thickness, which places them near the top and bottom a–c faces that you expect to be gapped. Could the substrate interface and the Pd contact interface carry them?
7. For Fig. 3d, how does the diffusive long-junction form fit over the full temperature range, and what junction lengths, δE values and mean free path (Supplementary Note 2) go into the comparison, given that your SdH data show a bulk electron pocket?
8. The text gives the STM edge-state width as "≈ 6 µm" (p. 5), with a 5 nm scale bar in Fig. 2g, and then calls the 0.7-1.5 µm Js half-widths "substantially larger" (p. 7). Which value is intended?

A note on questions 5 and 6. Your three arguments against trivial boundary channels are reproducibility across devices, the contrast between field orientations, and ballistic Ic(T). Accumulation layers at etched edges would also repeat from device to device, and they can be ballistic, so the field-orientation contrast is the argument that bears most directly on them. You describe the edge channels in Fig. 5c as "puzzling" (p. 7) and write that "on the basis of superconducting quantum interference measurements alone, we cannot unambiguously distinguish between hinge modes and surface states" (p. 8). A trivial reference junction, or gate control, would let readers place that result.

A note on question 8. As written, the STM width is several times larger than the Js widths it is compared with, and it is far larger than the image it is measured on. One of the two numbers or units probably needs a fix. The comparison on p. 7 depends on it.

## Related work

- de Vries et al. 2018, "h/e superconducting quantum interference through trivial edge states in InAs", <https://arxiv.org/abs/1709.03727>. Non-topological InAs junctions show SQUID-like interference from band-bending edge states, and the authors conclude that edge supercurrent and SQUID patterns alone cannot separate trivial from topological edges.
- Allen et al. 2016, "Spatially resolved edge currents and guided-wave electronic states in graphene", <https://arxiv.org/abs/1504.07630>. Fourier-reconstructed supercurrent density in graphene junctions shows edge currents that the authors attribute to guided-wave states confined by band bending.
- Aharon-Steinberg et al. 2021, "Long-range nontopological edge currents in charge-neutral graphene", <https://arxiv.org/abs/2012.02842>. Scanning SQUID imaging shows that charge accumulation at graphene edges produces narrow, nontopological conducting channels.
- Hart et al. 2014, "Induced Superconductivity in the Quantum Spin Hall Edge", <https://arxiv.org/abs/1312.2559>. Edge-confined supercurrent appears in 7.5 nm HgTe wells as the bulk is depleted, and it cannot be told apart from bulk supercurrent in trivial 4.5 nm wells. This is a trivial reference control of the kind suggested above.
- Dubos et al. 2001, "The Josephson critical current in a long mesoscopic S-N-S junction", <https://arxiv.org/abs/cond-mat/0008146>. In diffusive long junctions Ic(T) is numerically close to a simple exponential over a limited temperature interval, as expected in the ballistic limit.

Happy to rerun this if you share the figure data and the supplement.
