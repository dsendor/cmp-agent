# Lookalike check: Stacked vortices and Majorana zero modes in 1QL Bi2Te3/FeTe (arXiv 2610.17701v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport. A lookalike is an ordinary effect that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is scanning tunnelling spectroscopy of vortex cores, which the library's transport entries don't cover. So I adapted its zero-bias peak checks and entries to vortex spectra, and I added two vortex lookalikes from papers I opened. I worked from the extracted text without page numbers, so I locate quotes by section and figure.

**The claim, as I read it.** At the vortex core center in 1QL Bi2Te3/FeTe, at 1.0 T and 0.4 K, there is a zero-bias conductance peak about 0.5 meV wide. It comes with finite-energy levels spaced about 0.7 meV apart, read as integer quantized, and its profile stays unsplit and isotropic (Figs. 2I, 3). You read it as a Majorana zero mode from the FeTe layer. You also read the zero-energy maps with one, two and three vortices (Figs. 4B-D) as Majorana zero modes whose number can be controlled.

## Checks a careful reader will look for

1. Trivial bound states at the core (adapted from the search for quantum dots) : Partly. "Away from the vortex center, the intensity of the finite-energy peaks decreases and disappears at about 10 nm, whereas the ZBCP remains unsplit along different directions from the core center" (Fig. 3B-E). This is shown for one vortex, and there is no check for an impurity at the core spot.
2. Peak over wide ranges, including where it is absent : Partly. There are spectra at 0 T and 1.0 T (Fig. 2I). Figs. 4B-D are zero-energy maps without spectra, and no temperature series is shown.
3. Both ends (adapted: the partner mode at the far end of the vortex line) : Not done. STM reaches only the top surface.
4. Peak stable as the coupling changes (adapted: tip-sample coupling) : Not done. Spectra were taken at two setpoints, 500 pA (Fig. 2I) and 1 nA (Fig. 3B-E), with no series.
5. Bulk topology of the host layer (adapted from the nonlocal gap check) : Not done in the heterostructure. You show ARPES on a separate sample: "In samples with reduced interstitial Fe (Te annealed), a Dirac cone like dispersion emerges near the Fermi level (Figure S7)" (section "Origin of Majorana zero modes").
6. Raw conductance : Partly. Fig. 2I shows "Typical dI/dV spectra". Whether spectra are normalized is not stated.
7. Counts of devices and datasets : Partly. "MZMs are observed in all measured vortices" (Abstract). The number of vortices, islands and samples is missing.
8. Full parameter ranges : Partly. "we performed the measurements in a defect-free region at 0.4 K under a perpendicular magnetic field of 1.0 T" (section on Fig. 2). The fields of Figs. 4B-D are not stated.
9. Processing from raw data to figures : Partly. You name the "multi-Lorentzian fitting" (Fig. 3H-I) and state "Source data will be provided with this paper" (Data availability). The code is "available from the corresponding author upon reasonable request".

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: part | "MZMs are observed in all measured vortices" (Abstract); "we performed the measurements in a defect-free region" (Fig. 2 section) | State the number behind "all", and add spectra for the Fig. 4B-D vortices. |
| Local probe loophole | Not tested (not mentioned) | Nonlocal measurement: no; Overlap estimated through a quantum dot in series: no | Not discussed. | Estimate the overlap with the partner at the far end of the vortex line, for example from the Fig. 3H-I decay length against the 20 unit cell FeTe thickness. |
| Disorder-induced zero-energy states (adapted: interstitial excess Fe) | Not tested (argued, not tested) | End-to-end correlation: no; Bulk gap closing and reopening: no; Insensitivity to gates that should not matter: no | "To minimize possible defect-related effects, we performed the measurements in a defect-free region" (Fig. 2 section) | Take a 0 T spectrum at the core spot, and check that the peak follows the vortex across fields. Interstitial Fe can sit below the Bi2Te3 surface. |
| Half-odd-integer CdGM levels in a trivial vortex (not in library) | Tested in part | Level sequence resolved and shown integer with a zero level: part; Level sequence compared vortex by vortex: no | "two pairs of low-energy symmetric peaks appear near the zero energy, with an energy spacing of about 0.7 meV, suggestive of integer quantized CdGM states" (Figs. 2I, 3G) | Fit both sequences to Fig. 3G at your 0.37 meV resolution, and tabulate the sequence for each vortex measured. |
| Merged CdGM states giving a peak at the core center (not in library) | Tested in part | Spatial profile of where the peak splits off center: part; Peak followed as vortex spacing shrinks: no | "the ZBCP remains unsplit along different directions from the core center" (Fig. 3B-E) | Show the same line cuts for the two- and three-vortex configurations in Figs. 4B-D. |

## Questions about devices and data

1. How many vortices, islands and samples did you take spectra on, and how many showed the zero-bias peak? Your abstract says "MZMs are observed in all measured vortices", and the number behind "all" would help a reader a lot.
2. Were any vortices, islands or regions set aside (for example vortices near defects or island edges), and why?
3. Which ranges of field, temperature and tunnelling setpoint did you measure beyond the spectra shown at 0 T and 1.0 T, 0.4 K, 500 pA and 1 nA? Which fields do Figs. 4B-D correspond to?
4. What does the second-best vortex look like? Line cuts of spectra through the vortices in Figs. 4B-D would show whether each one carries the zero-bias peak, and it would help to know whether Figs. 2 and 3 show the same vortex.
5. Was the 0 T spectrum in Fig. 2I taken at the same spot as the 1.0 T vortex-core spectrum, and does the zero-bias peak move with the vortex when the field changes?
6. With an energy resolution of about 0.37 meV and a level spacing of about 0.7 meV, how well does a half-odd-integer sequence (lowest levels near ±0.35 meV) fit the peak positions in Fig. 3G, compared with the integer sequence?
7. Which data show the vortex number tuned by island size, and which island sizes did you measure?
8. Does the zero-bias peak height hold as you change the tip-sample coupling, as Zhu et al. did for vortex zero modes in FeTe0.55Se0.45?

## Related work

- Kong et al. 2019, "Observation of half-integer level shift of vortex bound states in an iron-based superconductor", <https://arxiv.org/abs/1901.02293>. In FeTe0.55Se0.45 they find two classes of vortex in the same crystal. A half-integer level shift separates them and is tied to whether a zero-bias peak is present.
- Chen et al. 2017, "Discrete energy levels of Caroli-de Gennes-Martricon states in quantum limit due to small Fermi energy in FeTe0.55Se0.45", <https://arxiv.org/abs/1709.09401>. They report discrete CdGM levels at half-odd-integer multiples of Δ²/E_F. They note that most type-II superconductors show a single zero-bias peak at the vortex center.
- Xu et al. 2013, "Majorana mode in vortex core of Bi2Te3/NbSe2 topological insulator-superconductor heterostructure", <https://arxiv.org/abs/1312.7110>. They use where the zero-bias peak splits off the vortex center, and how it changes as vortices crowd, to tell a Majorana mode from CdGM states.
- Yin et al. 2014, "Observation of a Robust Zero-energy Bound State in Iron-based Superconductor Fe(Te,Se)", <https://arxiv.org/abs/1403.1027>. They find an isotropic zero-energy bound state at interstitial excess Fe sites, with a decay length of about 10 Å, that stays robust in fields up to 8 T.
- Zhu et al. 2019, "Nearly quantized conductance plateau of vortex zero mode in an iron-based superconductor", <https://arxiv.org/abs/1904.06124>. They use variable tunnel coupling in STM. Zero-energy vortex states show conductance plateaus near 2e²/h, and CdGM states do not.

Happy to rerun this if you share the figure data or the supplementary figures.
