# Lookalike check: Stacked vortices with number controllable Majorana zero modes in Bi2Te3/FeTe (arXiv 2610.17701v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper reports scanning tunneling spectroscopy of vortex cores, which the transport library wasn't built for. So I adapted its zero-bias-peak entries and checks to a vortex probed by an STM tip, and I added three vortex-specific lookalikes from the STM literature, marked "(not in library)". I worked from the extracted text, so I cite quotes by section, caption or figure. I couldn't give page numbers, and I didn't have the Methods or Supplementary figures.

**The claim, as I read it.** In a defect-free region of a 1QL-Bi2Te3/FeTe island at 0.4 K and 1.0 T, the vortex core shows a zero-bias conductance peak (FWHM about 0.5 meV). The peak stays unsplit away from the core and sits among finite-energy levels that you read as an integer-quantized CdGM sequence (Fig. 2I, Fig. 3B-I). You attribute it to a Majorana zero mode in the FeTe layer. Zero-energy maps taken at several fields show one, two and three such vortices in an island (Fig. 4B-D).

## Checks a careful reader will look for

1. Search for trivial bound states near the core (adapted from the unintended-dot search) : Partly. "we extract five discrete states ... from the spectra by multi-peak fitting" (Fig. 3G). You resolve the finite-energy levels, but you show no spectra at defects or at sites nearby.
2. Peak over wide ranges, including where it is absent : Partly. "Abrikosov vortices of 1QL-Bi2Te3/FeTe heterojunction measured under different perpendicular magnetic field at zero energy" (Fig. 4B-D caption). Spectra appear at 1.0 T only, and the fields for Fig. 4 aren't given.
3. Both ends : Not done. The other end of the vortex line, in the FeTe film, is out of the tip's reach. The island edge and neighboring vortices are the accessible analogues.
4. Peak stable as tunnel coupling changes (tip height, adapted from barrier transparency) : Not done. The ZBCP appears at the 500 pA (Fig. 2I) and 1 nA (Fig. 3B-E) setpoints, but you show no tip-height series.
5. Independent evidence of a topological bulk (adapted from nonlocal gap closing) : Partly. "a Dirac cone like dispersion emerges near the Fermi level (Figure S7)" ('Origin of Majorana zero modes'). This is ARPES on Te-annealed FeTe, without Bi2Te3 on top.
6. Raw spectra and processing (adapted; STM has no series resistance) : Partly. Raw dI/dV spectra appear in Fig. 2I and 3B-E. The constraints on the multi-peak and multi-Lorentzian fits aren't stated in the main text.
7. Counts : Partly. "MZMs are observed in all measured vortices" (Abstract). No number is given.
8. Full ranges : Not done. Only the settings of the shown data are stated.
9. Processing with data and code : Not done. "Source data will be provided with this paper." (Data availability). Code is available on request.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Counts: part; how data were chosen: part; second dataset: part | "To minimize possible defect-related effects, we performed the measurements in a defect-free region" ('Anisotropic Abrikosov vortex'); the vortices in Fig. 4B-D appear as zero-energy maps only | Give counts of samples, islands, vortices and cooldowns; show core spectra for every vortex in Fig. 4B-D |
| Local-probe loophole | Not tested (data bear on it) | Nonlocal measurement: no; overlap via a dot: no | "measured under different perpendicular magnetic field at zero energy" (Fig. 4B-D caption); the multi-vortex maps could show hybridization | Spectra along the line joining two vortices, and the ZBCP as a function of vortex separation and distance to the island edge |
| Kondo resonance (adapted: magnetic excess Fe) | Not tested (not mentioned) | Even-odd occupancy: no (no dot); temperature: no; Zeeman: no | Not discussed. | Temperature series of the ZBCP width from 0.4 K up, and a field series at the same vortex |
| Trivial quantum-limit CdGM levels, half-integer series with the lowest level unresolved (not in library) | Tested in part | Integer versus half-integer fit: part; lowest level against resolution: part; levels stable in space: all | "approximately follow an integer quantized sequence (Fig. 3G)" ('Double sets of vortex bound states'); you don't show the half-integer alternative | Fit Fig. 3G with both sequences and report E2/E1 with errors; compare the ZBCP width with a pair at the lowest half-integer level broadened by 0.37 meV |
| Anisotropic non-split zero-energy CdGM states (not in library) | Tested in part | Several radial angles: part; quasi-classical calculation: no; resolution below level spacing: no | "in sharp contrast to the pronounced anisotropic Fermi surface of Bi2Te3 and the star-shaped morphology of the Bi2Te3 derived vortex bound states" (Fig. 3H-I); you show two directions | Radial cuts along and between the star rays, an angle plot on a circle, and a quasi-classical calculation with your measured contour |
| Impurity-induced near-degenerate Yu-Shiba-Rusinov states (not in library) | Tested in part | Superconducting tip: no; field series: part; tip-height series: no | "red line for 0T at clean surface and black line for 1.0T at vortex core center" (Fig. 2I caption); it's unclear whether the two spectra share a site | Take the 0 T spectrum at the later core site, follow the ZBCP in field and tip height, and use higher resolution if you can |

## Questions about devices and data

1. How many samples (growths), islands and vortices did you measure, over how many cooldowns, and how many vortices showed the ZBCP? Your abstract says "MZMs are observed in all measured vortices", and the number would let readers weigh that.
2. Were any vortices or regions set aside, for example vortices sitting near defects or island edges, and why?
3. Which fields, temperatures and tip setpoints did you measure beyond the 1.0 T, 0.4 K, 500 pA and 1 nA shown, and which fields do Fig. 4B-D correspond to?
4. What does the second-best vortex look like, for example the core spectrum of each vortex in the two- and three-vortex maps of Fig. 4B-D? Is the vortex in Fig. 2 the same one as in Fig. 3?
5. In Fig. 3G, how did you fit the five levels (number of peaks fixed or free, peak widths, and the Δ and E_F you use for the FeTe branch), and how well does a half-integer sequence fit next to the integer one? From the listed energies, the ratio of the second to the first level is about 2.5 on the positive side and 2.3 on the negative side.
6. Along which directions relative to the six star rays do the white and orange arrows of Fig. 3A run, and does the ZBCP stay unsplit between the rays as well as along them?
7. Was the 0 T spectrum in Fig. 2I taken at the same spot as the 1.0 T core spectrum?
8. Does the ZBCP change as two vortices approach each other, or as a vortex sits closer to the island edge, given that a partner mode would sit at the island edge or at the bottom of the 20 unit cell FeTe film?

## Related work

- Kim et al. 2021, "Anisotropic non-split zero-energy vortex bound states in a conventional superconductor", <https://arxiv.org/abs/2105.01354>. In topologically trivial La(0001), an anisotropic Fermi surface gives spatially non-split zero-energy vortex states alongside X-shaped split branches.
- Chen et al. 2017, "Discrete energy levels of Caroli-de Gennes-Martricon states in quantum limit due to small Fermi energy in FeTe0.55Se0.45", <https://arxiv.org/abs/1709.09401>. Resolves trivial quantum-limit CdGM levels at half-integer multiples of Δ²/E_F, and notes that unresolved levels appear as a zero-bias peak at the core.
- Kong et al. 2019, "Observation of half-integer level shift of vortex bound states in an iron-based superconductor", <https://arxiv.org/abs/1901.02293>. Two classes of vortices in FeTe0.55Se0.45 differ by a half-integer level shift tied to the presence or absence of a zero-bias peak, with integer or half-odd-integer level ratios.
- Machida et al. 2018, "Zero-energy vortex bound state in the superconducting topological surface state of Fe(Se,Te)", <https://arxiv.org/abs/1812.08995>. At high energy resolution, some vortices host a zero-energy state and others don't, and the fraction falls as field increases.
- Li et al. 2026, "Distinguishing impurity-induced bound states from Majorana-like zero-energy peaks in strained CsCa2Fe4As4F2 by scanning tunneling microscopy", <https://arxiv.org/abs/2603.27217>. A sharp zero-energy peak at defects is traced to nearly degenerate Yu-Shiba-Rusinov states, using a superconducting tip and field and transmissivity series.

Happy to rerun this if you share the source data and the Supplementary figures.
