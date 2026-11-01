# Lookalike check: Stacked vortices and number controllable Majorana zero modes in Bi2Te3/FeTe (arXiv 2610.17701v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is scanning tunnelling spectroscopy of vortex cores, and the library is built for transport, so I adapted the zero-bias-peak checks and entries to an STM vortex. Two vortex-specific explanations come from papers outside the library. Your text came without page numbers, so I cite sections and figures.

**The claim, as I read it.** In 1QL-Bi2Te3/FeTe islands at 0.4 K and 1.0 T, one vortex core shows a zero-bias conductance peak (FWHM about 0.5 meV) that stays unsplit off center, with finite-energy levels you read as an integer CdGM ladder (Figs. 2I, 3B-I). You read it as a Majorana zero mode from the FeTe layer. Zero-energy maps at several fields (Figs. 4B-D) show islands with one, two and three vortices, which you present as a controllable number of Majorana vortices.

## Checks a careful reader will look for

1. Look for trivial bound states in the core (adapted from the quantum-dot search: the CdGM ladder and peaks that split off center) : Partly. "Five discrete integer energy bound states are extracted, with no obviously dispersion" (Fig. 3G caption). That covers the Fig. 3 vortex; the vortices in Figs. 4B-D appear only in zero-energy maps.
2. Show the peak over wide parameter ranges, including where it is absent : Not done. The core spectrum is shown at 1.0 T, next to a 0 T spectrum "at clean surface" (Fig. 2I caption). There is no field, temperature or setpoint series of the peak, and the fields used in Figs. 4B-D aren't given.
3. Measure both ends at the same settings : Not done. The tip reaches only the top end of each vortex line.
4. Show the peak stays as the tunnel coupling changes (adapted from barrier transparency to tip-sample distance) : Not done. Fig. 2I uses 500 pA and Figs. 3B-E use 1 nA, with no comparison between the two.
5. Show bulk topology where the peak appears (adapted from a nonlocal gap closing) : Not done. "a Dirac cone like dispersion emerges near the Fermi level (Figure S7)" (section "Origin of Majorana zero modes"). That is in separately Te-annealed FeTe, not under the Bi2Te3.
6. Raw conductance and processing parameters (adapted: STM has no series resistance) : Done. "Vbias = 10 mV, ITunnel = 500 pA, Vmod = 0.1 mV" (Fig. 2I caption), with resolution "~0.37 meV at 0.4 K" (section "Double sets of vortex bound states").
7. Report counts of samples and datasets, how many showed the effect, and why others were set aside : Not done.
8. Disclose full parameter ranges and why each shown range was chosen : Partly. "To minimize possible defect-related effects, we performed the measurements in a defect-free region at 0.4 K under a perpendicular magnetic field of 1.0 T" (section "Anisotropic Abrikosov vortex").
9. Processing from raw data to figures, with data and code : Partly. The fits are named ("multi-peak fitting", "multi-Lorentzian fitting"), but "Source data will be provided with this paper" and the code is "available from the corresponding author upon reasonable request" (Data and Code availability).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Ordinary CdGM vortex states (not in library; Chen et al., arXiv 1709.09401) | Tested in part | Discrete ladder compared with the half-odd-integer ladder: part; levels followed off center: part | "whereas the ZBCP remains unsplit along different directions from the core center" (section "Double sets", Figs. 3B-E). This is the Fig. 3 vortex only. Fitted levels give ratios between integer and half-odd-integer, and the text gives a spacing of "about 0.7 meV". | Fit the Fig. 3 core spectrum with both ladders, convolved with your 0.37 meV resolution, and compare. Show spectra through the Fig. 4B-D vortices. |
| Kondo resonance (adapted: a magnetic impurity such as interstitial Fe under the core) | Not tested (argued, not tested) | Even-odd occupancy: no (no charge states here); temperature dependence: no; Zeeman splitting in field: no | "To minimize possible defect-related effects, we performed the measurements in a defect-free region" (section "Anisotropic Abrikosov vortex") | Show the peak at the same spot as the vortex moves (different field), plus a temperature series. Subsurface Fe isn't visible in topography. |
| Local-probe loophole | Not tested (not mentioned) | Nonlocal measurement: no; overlap through a dot in series: no | Not discussed. | Use the multi-vortex islands of Fig. 4. Peak splitting against vortex spacing, or against FeTe thickness, gives an overlap estimate from data you may already have. |
| Fine-tuning and selection | Tested in part | Counts measured and showing the effect: no; how the shown data were chosen: part; second dataset: part | "we performed the measurements in a defect-free region" (section "Anisotropic Abrikosov vortex"). Figs. 4B-D show other vortices as zero-energy maps only. | State the vortex, island and sample counts and show the second-best vortex spectrum. |

## Questions about devices and data

1. How many vortices, islands, samples and cooldowns did you measure with spectroscopy, and how many showed the zero-bias peak together with the integer ladder of Fig. 3G?
2. Why were the others set aside, and how did you pick the "defect-free region" and the vortex shown in Figs. 2 and 3 (are they the same vortex)?
3. Which fields, temperatures and setpoints did you measure beyond the 1.0 T, 0.4 K data shown, and which field values do Figs. 4B-D correspond to?
4. What does the second-best vortex look like? Spectra through the vortices of Figs. 4B-D, and through vortices in other islands, would answer this directly.
5. Your text gives a level spacing of "about 0.7 meV", while the fitted levels in Fig. 3G differ by about 0.8 to 1.2 meV. How many peaks did the multi-peak fit allow, and how well does a half-odd-integer ladder (no level at zero) fit the same core spectrum?
6. Does the zero-bias peak height or width change with tunnel coupling (your Fig. 2I uses 500 pA and Fig. 3B-E uses 1 nA), with temperature, or with field?
7. In the two- and three-vortex islands of Fig. 4, what are the vortex spacings, and does the zero-bias peak stay at zero or split as vortices come closer?
8. Your text says vortex number is set by "the lateral size of Bi2Te3 islands" as well as by field. Which data show the island-size dependence, given that the Fig. 4 caption lists only field?

A note on question 5. With your inner gap of about 1.85 meV and a spacing near 0.85 meV, a conventional ladder would put its lowest pair near ±0.43 meV. At 0.37 meV resolution, that pair would look wider than the 0.5 meV peak you report. So a direct two-ladder fit could separate the two readings with data you already have. Your fitted levels (0.79, -0.93, 1.96, -2.1 meV) give a ratio of about 2.4 between the second and first pair. That sits between the integer value of 2 and the half-odd-integer value of 3, so the fit would help.

The "number controllable" part of the claim rests on zero-energy maps (Figs. 4B-D). Any vortex core raises the zero-bias LDOS, so readers will look for a spectrum through each vortex before counting them as Majorana vortices.

## Related work

- Chen et al. 2017, "Discrete energy levels of Caroli-de Gennes-Martricon states in quantum limit due to small Fermi energy in FeTe0.55Se0.45", <https://arxiv.org/abs/1709.09401>. Ordinary quantum-limit CdGM levels sit at half-odd-integer multiples of Δ²/E_F, and when unresolved they give a symmetric zero-bias peak at the vortex center.
- Kong et al. 2019, "Observation of half-integer level shift of vortex bound states in an iron-based superconductor", <https://arxiv.org/abs/1901.02293>. Two classes of vortices in one crystal differ by a half-integer level shift, which goes with the presence or absence of the zero-bias peak and changes the higher level ratios from integer to half-odd-integer.
- Xu et al. 2013, "Majorana mode in vortex core of Bi2Te3/NbSe2 topological insulator-superconductor heterostructure", <https://arxiv.org/abs/1312.7110>. In conventional superconductors the zero-bias peak splits right off the vortex center. Reducing the distance between vortices destroys the zero mode and the peak splits again.
- Machida et al. 2018, "Zero-energy vortex bound state in the superconducting topological surface state of Fe(Se,Te)", <https://arxiv.org/abs/1812.08995>. At high energy resolution, some vortices host the zero-energy state and others don't, and that fraction falls as the field rises.
- Zhu et al. 2019, "Nearly quantized conductance plateau of vortex zero mode in an iron-based superconductor", <https://arxiv.org/abs/1904.06124>. Variable tunnel coupling gives a conductance plateau for the zero-energy vortex state, and no plateau for finite-energy CdGM states or the continuum.

Happy to rerun this if you share the figure data.
