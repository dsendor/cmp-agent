# Lookalike check: Stacked vortices and number-controllable Majorana zero modes in 1QL-Bi2Te3/FeTe (arXiv 2610.17701v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is scanning tunneling spectroscopy of vortex cores, which sits outside the library's transport scope, so I adapted the zero-bias-peak entries and checks to an STM tip over a vortex and added two lookalikes from the vortex literature. I worked from the extracted text, which has no page numbers, so each quote cites its section heading or figure.

**The claim, as I read it.** In 1QL-Bi2Te3 on 20 unit cell FeTe, the FeTe-derived branch of vortex bound states gives a spatially unsplit zero-bias conductance peak (FWHM about 0.5 meV) with flanking levels that "approximately follow an integer quantized sequence" (Fig. 2I, Fig. 3B-I), read as a Majorana zero mode. Zero-energy maps at several fields (Fig. 4B-D) support MZMs "in all measured vortices", with their number set by field and island size. Data are at 0.4 K and 1.0 T perpendicular.

## Checks a careful reader will look for

1. Look for trivial bound states near the core (adapted from the dot search) : Partly. "To minimize possible defect-related effects, we performed the measurements in a defect-free region at 0.4 K" ('Anisotropic Abrikosov vortex' section); this is stated for the Fig. 2 vortex from surface topography, and subsurface FeTe sites are not mapped.
2. Peak over wide field ranges, including where absent, with heights : Partly. "red line for 0T at clean surface and black line for 1.0T at vortex core center" (Fig. 2I caption); spectra are at one field, and the Fig. 4B-D maps give no field values.
3. Both ends of the Majorana pair (adapted: partner mode or vortex-vortex overlap) : Not done.
4. Peak versus junction transparency (adapted: tip height or setpoint series) : Not done. Fig. 2I uses 500 pA and Fig. 3B-E uses 1 nA on different vortices, with no series on one vortex.
5. Bulk topological transition (adapted from nonlocal gap closing) : Not done. The Dirac-like ARPES dispersion is on Te-annealed FeTe (Fig. S7), apart from the heterostructure.
6. Raw conductance and processing behind the peak height (adapted from series resistance) : Partly. Setpoints are given, "Vbias = 10 mV, ITunnel = 500 pA, Vmod = 0.1 mV" (Fig. 2I caption); normalization, if any, is not stated.
7. Report devices and datasets, and how many showed the effect : Partly. "Notably, MZMs are observed in all measured vortices" (Abstract); the numbers of samples, islands and vortices are not given.
8. Disclose full parameter ranges : Not done.
9. Processing steps, data and code : Partly. Fitting methods are named (multi-peak, multi-Lorentzian, Dynes), and "The code used for STM analysis is available from the corresponding author upon reasonable request." (Code available).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection of the shown vortex | Tested in part | Counts measured and with the effect: part; how shown data were chosen: part; second dataset shown: part | "Notably, MZMs are observed in all measured vortices" (Abstract); two vortex-core spectra appear (Fig. 2I, Fig. 3). | Give the numbers of samples, islands and vortices, and show a full line cut for a second vortex. |
| Crowded trivial subgap states (adapted: dense Bi2Te3-branch CdGM states merging into a core peak) | Tested in part | Field and gate range vs predicted topological range: no; subband model: part (BdG fit of the Bi2Te3 branch, plus the spatial symmetry and decay-length comparison of Fig. 3H-I as an equivalent test) | "This distinct spatial symmetry, together with the shorter characteristic decay length, indicates that the second set of vortex bound states has a different microscopic origin." ('Double sets' section, Fig. 3H-I) | Compute the Bi2Te3-branch core spectrum from your BdG parameters at 0.37 meV resolution, and compare the decay along all six star arms. |
| Local-probe loophole (adapted: STM tip over one vortex) | Not tested (data bear on it) | Nonlocal measurement: no; overlap estimate: no | "Abrikosov vortices of 1QL-Bi2Te3/FeTe heterojunction measured under different perpendicular magnetic field at zero energy" (Fig. 4B-D caption) | Take spectra on the vortex pairs and triplets of Fig. 4B-D versus vortex spacing and look for splitting of the zero-bias peak. |
| Half-integer CdGM levels in a conventional quantum-limit vortex (not in library) | Tested in part | Level sequence and ratios resolved, resolution below spacing: part (one vortex, Fig. 3G); vortices surveyed for both classes: no | "we extract five discrete states ... which approximately follow an integer quantized sequence (Fig. 3G)" ('Double sets' section) | Fit every vortex core spectrum to both sequences, report the fitted spacing with uncertainties, and count vortices with and without the peak. |
| Impurity-bound zero-energy state at interstitial excess Fe (not in library) | Tested in part | Zero-field spectrum at the same spot: no; peak followed as the vortex moves: part (zero-energy maps only, Fig. 4B-D) | "To minimize possible defect-related effects, we performed the measurements in a defect-free region" ('Anisotropic Abrikosov vortex' section) | Take a spectrum at the same spot at 0 T and after the vortex moves with field, and check whether the peak follows the vortex. |

## Questions about devices and data

1. How many samples, Bi2Te3 islands and vortices did you measure, and how many showed the zero-bias peak? Your abstract says "MZMs are observed in all measured vortices"; the numbers behind "all" would help.
2. Beyond choosing "a defect-free region", how did you pick the vortices shown in Figs. 2 and 3, and were any vortices, islands or samples set aside?
3. Which fields, temperatures and tunneling setpoints did you measure beyond the ones shown? In particular, which fields are used in Fig. 4B-D, and did you take spectra at more than one field or tip height?
4. What do the spectra of the other vortices look like, for example a line cut like Fig. 3B-E through each vortex in Fig. 4B-D?
5. The text gives a level spacing of "about 0.7 meV", while the fits in Fig. 3G give L1 = 0.79 meV, L-1 = -0.93 meV and L2 = 1.96 meV, L-2 = -2.1 meV, a ratio near 2.3 to 2.5. How do these compare with the integer (1:2) and half-odd-integer (1:3:5) sequences, and how do you separate L2 from the inner coherence peak at 1.85 meV?
6. With an energy resolution of about 0.37 meV and a peak width of about 0.5 meV, what values of the gap and Fermi energy do you use for the FeTe-derived branch, and would a pair of lowest levels at plus or minus half the level spacing be resolved?
7. Was the 0 T spectrum in Fig. 2I taken at the same spot as the 1.0 T vortex-core spectrum, and can you rule out a vortex pinned at a subsurface interstitial Fe site in the FeTe layer?
8. Which data show the vortex number tuned by island size? Fig. 4E is a schematic, and Fig. 4B-D vary the field.

## Related work

- Chen et al. 2018, "Discrete energy levels of Caroli-de Gennes-Martricon states in quantum limit due to small Fermi energy in FeTe0.55Se0.45", <https://arxiv.org/abs/1709.09401>. Resolves quantum-limit CdGM levels at half-odd-integer multiples of the spacing, and notes that with small gap-to-Fermi-energy ratio a symmetric zero-bias peak appears at a conventional vortex center.
- Kong et al. 2019, "Observation of half-integer level shift of vortex bound states in an iron-based superconductor", <https://arxiv.org/abs/1901.02293>. Finds two classes of vortices in one FeTe0.55Se0.45 crystal, with and without a zero-bias peak, told apart by integer versus half-odd-integer level ratios.
- Machida et al. 2019, "Zero-energy vortex bound state in the superconducting topological surface state of Fe(Se,Te)", <https://arxiv.org/abs/1812.08995>. Uses about 20 microeV resolution and finds that some vortices host the zero-energy state while others do not, with the fraction falling as field rises.
- Yin et al. 2015, "Observation of a Robust Zero-energy Bound State in Iron-based Superconductor Fe(Te,Se)", <https://arxiv.org/abs/1403.1027>. Shows an isotropic zero-energy bound state at interstitial excess Fe sites, with about 10 Å decay length, robust to fields up to 8 T.
- Wang et al. 2018, "Evidence for Majorana bound state in an iron-based superconductor", <https://arxiv.org/abs/1706.06074>. Reports a sharp, non-split vortex-core zero-bias peak in FeTe0.55Se0.45 and follows it versus field, temperature and tunneling barrier.

Happy to rerun this if you share the source data or the Supplementary Materials.
