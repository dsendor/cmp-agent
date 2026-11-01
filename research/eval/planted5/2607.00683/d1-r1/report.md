# Lookalike check: Facet-selective ballistic supercurrent in a weak topological insulator (arXiv 2607.00683v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport. A lookalike is an ordinary effect that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper measures supercurrent interference in a three-dimensional crystal. That is at the edge of the library's scope, which is built around Majorana and fractional Josephson signatures in hybrid devices. So only the library's selection entry and its general practice checks apply directly. I added two ordinary explanations from papers I opened, marked "(not in library)". I worked from the extracted text, so figure details come from the captions. Page numbers follow the page markers in that text.

**The claim, as I read it.** Your Figs. 4a,b and 5b show SQUID-like critical current oscillations with flux-quantum spacing in two Al/ZrTe5 junctions (Dev 1, Dev 2) and one NbN/ZrTe5 junction (Dev 3). You read these as supercurrent confined to the two conducting side facets of a weak topological insulator. Three further observations support that reading:
- Dev 3 shows a different pattern for in-plane By (Fig. 5c).
- All three junctions show an exponential Ic(T) (Fig. 3d), which you read as ballistic transport.
- The lobes are sharp (Fig. 5b,c), which you read as a sawtooth current-phase relation.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "All three junctions exhibit this exponential temperature dependence." (p. 6). Three junctions are shown. The text doesn't say how many were made, or whether any were set aside.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. You note the reconstruction "is limited by the finite magnetic-field range of the measured interference pattern" (p. 7). The text doesn't give the field or temperature ranges measured, or why the shown ranges were chosen.
3. Give the processing steps from raw data to figures, with data and code : Partly. "we extract the supercurrent density profile Js (x) across the junction width from the interference patterns (see Supplementary Note 6 for details)" (p. 6). The text I read has no data or code availability statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection of a non-representative example | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: part | "Fig. 4a,b present the interference patterns of two Al/ZrTe5 junctions" (p. 6). The By contrast comes from Dev 3 alone (Fig. 5c). | State how many junctions were made and measured in each field orientation, and show the By pattern for a second junction if you have one. |
| Trivial edge channels from band bending or edge doping (not in library) | Tested in part | Edge and bulk supercurrent followed with carrier density (gate voltage): no; Same interference measurement in a reference configuration where no topological boundary state should carry the edge current: part (your By orientation, Dev 3 only, where you expect a homogeneous current) | "Such a field-orientation contrast is difficult to reconcile with a trivial mechanism." (p. 7). For By you also find that "the appearance of edge channels is puzzling" (p. 7). | Compare the edge peak weight in Js(x) across your junctions of different width or edge preparation (Supplementary Table S1). A gated or trivial-reference junction would settle it. |
| Quasi-exponential Ic(T) in a diffusive long junction (not in library) | Not tested (argued, not tested) | Ic(T) fitted with the diffusive long-junction form in Thouless-energy units: no; Fitted energy scale compared with the Thouless energy from junction length and diffusion constant: no | "the ballistic nature of the supercurrent, as evidenced by the exponential temperature dependence of Ic (Fig. 3d), is incompatible with a trivial diffusive transport scenario" (p. 7) | Fit the Fig. 3d data with Ic proportional to T^3/2 exp(-L/LT) as well. Compare the fitted energy scales with hbar vF/L and with the Thouless energy from your mean free path. |

## Questions about devices and data

1. How many ZrTe5 junctions did you fabricate and measure, and how many showed SQUID-like interference? The text shows three (Dev 1 to Dev 3, Figs. 3 to 5) and points to Supplementary Table S1 for their dimensions.
2. Why were the others set aside, if any were?
3. Which field ranges did you measure beyond the ones shown in Figs. 4 and 5, and how did you choose the range that feeds the Js(x) reconstruction?
4. What does the second-best junction look like, especially for the in-plane By orientation, which appears for Dev 3 only (Fig. 5c)?
5. On p. 7 you list "three observations" against trivial boundary channels, and the text I read shows the second and third. What is the first, and which figure carries it?
6. How were the side edges of the junction flakes formed? Methods describes Ar+ ion milling for the Hall bars; if the junction edges were milled too, a comparison of milled and as-exfoliated edges would help separate edge damage or doping from the facet picture.
7. Do the Fig. 3d data fit the diffusive long-junction form, Ic proportional to T^3/2 exp(-L/LT), as well as the ballistic form, and how do the fitted level spacings compare with hbar vF/L from your Fermi-surface data and with the Thouless energy from the mean free path in Supplementary Note 2?

## Related work

- Hart et al. 2014, "Induced Superconductivity in the Quantum Spin Hall Edge", <https://arxiv.org/abs/1312.2559>. In 7.5 nm HgTe wells, supercurrent becomes confined to the edges as the bulk is depleted. In 4.5 nm wells, which are trivial, edge supercurrents can't be told apart from the bulk. This is a reference sample measured alongside the topological one.
- Allen et al. 2016, "Spatially resolved edge currents and guided-wave electronic states in graphene", <https://arxiv.org/abs/1504.07630>. A Fourier reconstruction finds edge-dominated supercurrent near charge neutrality in graphene, which the authors attribute to band-bending guided modes. Gate tuning brings the device back to uniform flow and a Fraunhofer pattern.
- de Vries et al. 2018, "h/e superconducting quantum interference through trivial edge states in InAs", <https://arxiv.org/abs/1709.03727>. Non-topological InAs junctions show SQUID patterns and edge-only Js(x), from electron accumulation at etched mesa edges. The authors conclude that superconducting edges alone don't prove topological edge states.
- Dubos et al. 2001, "The Josephson critical current in a long mesoscopic S-N-S junction", <https://arxiv.org/abs/cond-mat/0008146>. In diffusive Nb-Cu-Nb junctions, Ic proportional to T^3/2 exp(-L/LT) is, over a limited temperature interval, numerically very close to the simple exponential expected in the ballistic limit.
- Meier, Fal'ko and Glazman 2016, "Edge effects in the magnetic interference pattern of a ballistic SNS junction", <https://arxiv.org/abs/1603.08567>. Theory: in a wide ballistic junction, trajectories reflected from the side edges lift the zeros of Ic(flux) and shift its minima. So a uniform ballistic junction already departs from a Fraunhofer pattern.

Happy to rerun this if you share the supplementary notes and the figure data.
