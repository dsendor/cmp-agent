# Lookalike check: Topological phase in monolayer Si2Te2 on HfTe2 (arXiv 2508.07351v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport. A lookalike is an ordinary effect that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper uses scanning tunneling spectroscopy of edge states, which is a different measurement from the device transport the library was built for. So I adapted one library entry and added two lookalikes from papers outside the library.

**The claim, as I read it.** Monolayer Si2Te2 grown on HfTe2 is a quantum spin Hall insulator. The evidence is a bulk gap of about 300 meV in dI/dV (Fig. 4(a) inset). There is also an in-gap edge state: a dI/dV peak near EF that appears within 2 to 3 nm of the island edge. It is seen in point spectra and a line cut on one island (Fig. 5(a) to (c)), and as a ring in a +7 mV dI/dV map of a second island (Fig. 5(d), (e)). DFT supports both (Figs. 1, 2).

## Checks a careful reader will look for

The library has no check list for STM edge-state signatures, so these are its practice checks, which apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. For the gap you give a count: "corroborated by systematic measurements on 20 ML-Si2Te2 islands (See Ref. 35)" (p. 4). For the edge state the main text says only "multiple ML-Si2Te2 islands and step geometries, see Fig. S11" (p. 4). Fig. S11 is not in this version.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Not done. The edge spectra in Fig. 5(b), (c) cover -0.1 to +0.1 V, and Fig. 5(e) is a single map energy (+7 mV). The paper doesn't say what else was measured or why these windows were chosen.
3. Give the processing steps from raw data to figures, with data and code : Not done. The caption of each panel gives the acquisition settings, but processing, data and code are deferred to Ref. 35. Ref. 35's description says the material covers "image processing procedures and large area scans showing the coexistence of three stripe orientations" (p. 6). The stripe wording may come from another manuscript, so it is worth checking.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Shown islands and edges picked from a larger set (fine-tuning-and-selection) | Tested in part | Devices and datasets measured, and how many showed the effect: part; how the shown data were chosen: no; a second device or dataset shown: all | "These features are reproducibly observed across multiple ML-Si2Te2 islands and step geometries, see Fig. S11" (p. 4); Fig. 5(d), (e) is a second island. | State how many islands and edges you measured and how many showed the peak, and show the second-best edge in the main text. |
| A local probe can't tell a helical edge from a trivial edge mode (local-probe-loophole, adapted) | Not tested (argued, not tested) | Nonlocal measurement (here, edge conduction): no; overlap through a quantum dot: no (does not apply to this system) | "The observed spatial extent and robustness of the edge states provide strong evidence for their topological origin." (p. 4) | Measure step edges of your semiconducting ML-Si2Te2 on Sb2Te3 the same way, and if possible probe edge conduction directly (multi-tip STM or microwave impedance). |
| Trivial edge states from band bending or in-gap states (not in library; Shi et al. 2018) | Tested in part | Edge signal across the whole bulk gap with no gap of its own: part; suppressed by magnetic field: no | "the edge spectrum displays a pronounced peak at EF within the same energy range" (p. 4, Fig. 5(b)) | Take edge and center spectra from -0.1 to +0.4 V at one set-point, and edge maps at several energies inside the gap. |
| Set-point (feedback) contrast at the 7 Å island step (not in library; Scarfato et al. 2024) | Tested in part | Map at constant height or a second set-point: no; edge feature as a narrow peak in fixed set-point spectra: part | "Spatially dependent dI/dV spectra recorded along the origin line in (a) with 0.36 nm spacing." (Fig. 5(c) caption) | Repeat the Fig. 5(e) map at constant height or with Vstab outside the gap, and compare tip paths that climb onto the island with paths that step down from it. |

A few notes on the table. Your line cut in Fig. 5(c) helps a lot: a narrow peak that appears only near the edge is hard to get from set-point rescaling alone. That is why the last row counts as tested in part, though so far on one line of one island. For the band bending row, your Fig. 5(b) spans about a third of the gap. Within that window the peak sits close to the valence band edge you place at about -10 meV, and above roughly +20 mV the edge curve drops below the center curve. Showing the edge spectra up to the conduction band edge near 290 meV would speak directly to this lookalike. Shi et al. used the same reasoning when they saw no gap in the edge signal. For the local probe row, your earlier Si2Te2 on Sb2Te3 samples are a ready-made trivial control. Edges there measured with similar tips and set-points would show what a non-topological Si2Te2 edge looks like in your hands. Leis et al. found an in-gap STS edge state without ballistic edge conduction, which is why a conduction probe carries weight when you can get one.

## Questions about devices and data

1. How many islands and step edges did you measure with STS, and how many showed the edge peak near EF? The 20 islands on p. 4 refer to the band gap, and Fig. S11 is not in this version.
2. Were any islands or edges set aside, and why?
3. Which bias ranges, map energies, set-points and island sizes did you measure beyond the -0.1 to +0.1 V spectra and the single +7 mV map in Fig. 5?
4. What does the second-best island or edge look like, in point spectra and in a map?
5. Does the edge enhancement extend across the whole gap up to the conduction band edge near 290 meV? In your Fig. 5(b) the peak sits within about 10 meV of the valence band edge you place at about -10 meV, and the edge curve falls below the center curve above about +20 mV.
6. How does the "V-shaped dip between ±50 mV" in the center spectrum of Fig. 5(b) relate to the gap from about -10 to 290 meV in the Fig. 4(a) inset, and how large were the islands used for each?
7. Did you measure step edges of the semiconducting ML-Si2Te2 on Sb2Te3 from your Refs. 29 and 30 with similar tips and set-points, and do they show a similar peak?
8. Was the Fig. 5(e) map taken with the feedback set at Vstab = 0.2 V at each pixel, and does the ring persist in a constant-height map or at a set-point outside the gap?

## Related work

- Leis et al. 2022, "Probing edge state conductance in ultra-thin topological insulator films", <https://arxiv.org/abs/2204.03753>. Reports an in-gap STS edge state at step edges of few-layer (Bi,Sb)2Te3 films with no ballistic edge conduction in four-tip STM transport. It also rules out a feedback artifact by comparing tip paths that climb and descend the step.
- Shi et al. 2018, "Imaging Quantum Spin Hall Edges in Monolayer WTe2", <https://arxiv.org/abs/1807.09342>. Images edge conduction in WTe2 by microwave impedance microscopy. The edge signal shows no gap with gate voltage and is suppressed by magnetic field, which the authors use to rule out band bending and in-gap states.
- Maximenko et al. 2020, "Electric field effects on the band gap and edge states of monolayer 1T'-WTe2", <https://arxiv.org/abs/2011.10096>. STM on back-gated WTe2 on graphene reports clear edge states that span the bulk gap.
- Scarfato et al. 2024, "Feedback loop dependent charge density wave imaging by scanning tunneling spectroscopy", <https://arxiv.org/abs/2406.03294>. Shows that constant-current STS maps depend on the set-point, and that only constant-height maps track the intrinsic LDOS.
- Huang et al. 2022, "Epitaxial growth of a two-dimensional topological insulator candidate: monolayer Si2Te2", <https://arxiv.org/abs/2206.00919>. Your group's ML-Si2Te2 on Sb2Te3, semiconducting by STS and DFT. It is a natural trivial reference for edge spectra.

Happy to rerun this if you share the supplementary material and the Fig. 5 grid data.
