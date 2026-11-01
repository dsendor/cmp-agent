# Lookalike check: Stacked vortex structure with number controllable Majorana zero mode in Bi2Te3/FeTe (arXiv 2610.17701v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is scanning tunneling spectroscopy of vortex cores, while the library was written for nanowire devices, so I adapted its zero-bias-peak entries and checks to an STM vortex and added two outside rows from STM vortex papers. I read the extracted main text only, so Figs. S1 to S11 and the Supplementary Materials were not available to me. Quotes are located by section and figure because the text has no page numbers.

**The claim, as I read it.** In one vortex on a 1QL-Bi2Te3 island over 20 unit cells of FeTe, measured at 0.4 K and 1.0 T, you report a spatially unsplit zero-bias conductance peak (FWHM about 0.5 meV). It sits with discrete CdGM levels that "approximately follow an integer quantized sequence" (Figs. 2I, 3B-I), and you read it as a Majorana zero mode from topological FeTe. You also report that field and island size set how many such vortices an island holds (Fig. 4B-D), and that "MZMs are observed in all measured vortices" (Abstract).

## Checks a careful reader will look for

1. Search for local trivial states at the peak site (adapted from dot search to impurities or defects) : Partly. "we performed the measurements in a defect-free region at 0.4 K" (Anisotropic Abrikosov vortex section), and Fig. 2I shows a 0 T spectrum "at clean surface"; you show no impurity spectra or 0 T spectrum at the same spot.
2. Peak over wide field ranges, including where it is absent : Partly. Fig. 4B-D shows zero-energy maps "under different perpendicular magnetic field"; you show vortex-core spectra only at 1.0 T.
3. Both ends compared (adapted to the two ends of the vortex line) : Not done. STM reaches only the top surface.
4. Peak followed as the tunnel coupling changes (adapted to tip-sample distance) : Not done. Setpoints differ between figures (500 pA, 1 nA), and you show no systematic series.
5. Bulk gap closing and reopening : Not done. The band-topology argument rests on ARPES of FeTe films (Figs. S6, S7), and you show no transition in the heterostructure.
6. Raw data and processing of the peak (adapted from series resistance to normalization and fitting) : Partly. You show raw dI/dV line cuts (Fig. 3B-E), and you name the fits ("multi-peak fitting", "multi-Lorentzian fitting") without their settings.
7. Report counts of devices and datasets : Not done. "MZMs are observed in all measured vortices" (Abstract), with no number.
8. Report full parameter ranges : Partly. You give setpoints, ±10 mV, 0.4 K and 1.0 T; the field values for Fig. 4B-D are missing.
9. Processing steps, data and code : Partly. "Source data will be provided with this paper" and code "available from the corresponding author upon reasonable request" (Data and Code availability).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Counts: part; how data were chosen: part; second dataset: part | "Notably, MZMs are observed in all measured vortices" (Abstract); "in a defect-free region" (vortex section) | Give the number of vortices, islands and samples, and show full level fits for a second vortex, including one from Fig. 4. |
| Local-probe loophole | Not tested (not mentioned) | Nonlocal measurement: no; overlap via dot: no | Not discussed. | Estimate how the zero mode would split for a vortex line through a 20 unit cell film, and compare with the 0.5 meV width. |
| Kondo resonance (adapted: magnetic impurity such as interstitial Fe) | Not tested (argued, not tested) | Even-odd occupancy: no; temperature: no; Zeeman splitting: no | "To minimize possible defect-related effects, we performed the measurements in a defect-free region" (vortex section) | Show 0 T and 1.0 T spectra at the same core site, and a temperature series of the peak. |
| Disorder-induced zero-bias peak (adapted: moiré and interface inhomogeneity) | Not tested (argued, not tested) | End-to-end correlation: no; gap closing: no; insensitivity to irrelevant parameters: no | "distinct from alloyed Fe(Te,Se) systems in which chemical inhomogeneity can obscure the microscopic origin" (Summary) | Compare vortices pinned at different moiré positions and local gap sizes (Fig. 1I) for peak energy and width. |
| Trivial quantum-limit CdGM levels with half-odd-integer sequence (not in library) | Tested in part | Levels compared with integer and half-odd-integer: part; vortices with and without peak compared: no | "five discrete states at −2.1 ± 0.13 meV (L-2), −0.93 ± 0.14 meV (L-1), 0.003 ± 0.11 meV (L0), 0.79 ± 0.17 meV (L1), and 1.96 ± 0.22 meV (L2)" (Fig. 3G) | Plot EL/ΔE against both sequences per vortex; the ratios of about 2.3 and 2.5 sit between them. |
| Non-split zero-energy vortex states in a trivial superconductor (not in library) | Tested in part | Level spacing vs resolution: all; spatial profile vs trivial quasi-classical model: part | "The decay length of the ZBCP is nearly identical along different high symmetry directions (Fig. 3H-I)" | Run a trivial-vortex quasi-classical calculation with your measured Bi2Te3 Fermi contour and compare it with Fig. 3H-I. |

## Questions about devices and data

1. How many samples, islands and vortices did you measure? The abstract says "MZMs are observed in all measured vortices"; could you give the number of vortices behind "all"?
2. If some regions or vortices were set aside (for example regions with defects, given your choice of "a defect-free region"), how many, and why?
3. Which fields, temperatures and setpoints did you measure beyond the ones shown? In particular, what fields were used in Fig. 4B-D, and do you have vortex-core spectra at fields other than 1.0 T or at temperatures above 0.4 K?
4. What does the second-best vortex look like? A full line cut and level fit for another vortex, ideally one from the two- and three-vortex islands of Fig. 4, would help.
5. Your Fig. 3G energies give level ratios E2/E1 of about 2.5 (positive bias, 1.96/0.79) and 2.3 (negative bias, 2.1/0.93), and spacings of 0.79 to 1.17 meV, while the text gives "an energy spacing of about 0.7 meV". Could you plot EL/ΔE against integer and half-odd-integer lines, per vortex, and say which spacing is intended?
6. For the Bi2Te3 branch, the text gives a level spacing of "~0.03 µeV". With Δ of 1.85 to 2.92 meV and EF of about 300 meV, Δ²/EF comes to roughly 11 to 28 µeV (about 0.01 to 0.03 meV). Which value and which Δ did you intend?
7. Did you vary the tip-sample distance (setpoint conductance) at the vortex center, and does the zero-bias peak height behave differently from the finite-energy CdGM peaks?
8. Could you show spectra at the same vortex-core location at 0 T and 1.0 T, and the topography there, to exclude a magnetic impurity such as interstitial Fe, and the peak's temperature dependence?

## Related work

- Kong et al. 2019, "Observation of half-integer level shift of vortex bound states in an iron-based superconductor", <https://arxiv.org/abs/1901.02293>. In FeTe0.55Se0.45 it finds two classes of vortex: integer-quantized levels with a zero-bias peak, and half-odd-integer levels without one.
- Kim et al. 2021, "Anisotropic non-split zero-energy vortex bound states in a conventional superconductor", <https://arxiv.org/abs/2105.01354>. It reports non-split zero-energy vortex states in trivial La(0001), set by the surface Fermi contour.
- Machida et al. 2019, "Zero-energy vortex bound state in the superconducting topological surface state of Fe(Se,Te)", <https://arxiv.org/abs/1812.08995>. Some vortices host the zero-energy state and others do not, and the fraction falls as field rises.
- Zhu et al. 2020, "Nearly quantized conductance plateau of vortex zero mode in an iron-based superconductor", <https://arxiv.org/abs/1904.06124>. Varying the tip-sample coupling gives a plateau for the zero-energy vortex state and none for the CdGM states.
- Wang et al. 2018, "Evidence for Majorana bound state in an iron-based superconductor", <https://arxiv.org/abs/1706.06074>. It shows a sharp, non-split zero-bias peak in FeTe0.55Se0.45 vortices, followed across field, temperature and tunneling barrier.

Happy to rerun this if you share the Supplementary Materials and the figure data.
