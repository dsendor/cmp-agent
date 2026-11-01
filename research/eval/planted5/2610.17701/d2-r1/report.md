# Lookalike check: Stacked vortex structure with number-controllable Majorana zero modes in Bi2Te3/FeTe (arXiv 2610.17701v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is STM vortex spectroscopy, so I adapted the zero-bias-peak checks from nanowire transport to a vortex core probed by a tip. The library has no vortex-specific entries, so two rows below come from papers outside it. The extracted text has no page numbers, so quotes cite the section and figure.

**The claim, as I read it.** In the vortex core on a 1QL-Bi2Te3 island over FeTe, you see a zero-bias conductance peak (ZBCP) that stays unsplit away from the center, sitting among discrete levels you read as an integer sequence (Fig. 2I, Fig. 3B-I). You assign it to a Majorana zero mode from the FeTe layer, and you show that the number of vortices on an island changes with field (Fig. 4B-D).

## Checks a careful reader will look for

1. Search for trivial bound states at the core (adapted from the dot search) : Partly. "we extract five discrete states ... which approximately follow an integer quantized sequence (Fig. 3G)" (Double sets of vortex bound states). Impurity states at the core aren't checked.
2. Peak over wide field, temperature and setpoint ranges, with heights reported : Partly. Fig. 4B-D are vortex maps "measured under different perpendicular magnetic field at zero energy"; the ZBCP spectra are shown at 1.0 T only, with no temperature series.
3. Partner mode compared (adapted from both ends: island edge or a second vortex) : Not done.
4. Peak followed as the tunnel coupling changes (adapted from transparency: tip-sample distance) : Not done.
5. Independent evidence of a topological band structure in the same heterostructure (adapted from the nonlocal gap check) : Partly. "In samples with reduced interstitial Fe (Te annealed), a Dirac cone like dispersion emerges near the Fermi level (Figure S7)" (Origin of Majorana zero modes). That ARPES is on annealed FeTe, not under the Bi2Te3.
6. Processing from raw dI/dV (adapted from series resistance) : Partly. Raw waterfalls with setpoints appear in Fig. 3B-E; the fits behind the level values and decay lengths aren't described in the main text.
7. Counts of devices and datasets, and why others were set aside : Not done. "MZMs are observed in all measured vortices" (Abstract), with no number.
8. Full parameter ranges and why each shown range was chosen : Not done. The captions for Fig. 3 and Fig. 4B-D give no field, and the vortex spectra give no temperature.
9. Processing steps, data and code : Partly. "The code used for STM analysis is available from the corresponding author upon reasonable request." (Code available)

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Counts and how many showed it: no; how the shown data were chosen: no; second dataset: part (Fig. 2I and Fig. 3 may be one vortex) | "Notably, MZMs are observed in all measured vortices" (Abstract) | Give the vortex, island and sample counts, and spectra at each vortex in Fig. 4B-D. |
| Trivial CdGM vortex-core states (not in library) | Tested in part | Level ratios integer versus half-odd-integer: part (ratios 2.3 and 2.5); ZBCP followed off center: all | "the ZBCP remains unsplit along different directions from the core center" (Fig. 3B-E) | Fit integer and half-integer sequences to Fig. 3G with your resolution and compare. |
| Interstitial excess-Fe zero-energy bound state (not in library) | Tested in part | Zero field at the same spot: part (0 T spectrum is at another spot); ZBCP tracked to vortex positions: part (maps only) | "red line for 0T at clean surface and black line for 1.0T at vortex core center" (Fig. 2I) | Take a zero-field spectrum at the same core location and register cores to topography. |
| Local-probe loophole | Not tested (data bear on it) | Nonlocal measurement: no; overlap estimate: no | Fig. 4B-D show two- and three-vortex islands as zero-energy maps only. | Take spectra versus vortex spacing in Fig. 4B-D and look for splitting; probe the island edge. |

## Questions about devices and data

1. How many samples, islands and vortices did you take full spectra on, and how many showed the ZBCP? Your abstract says "MZMs are observed in all measured vortices"; the count behind "all" would help readers.
2. Were any vortices or islands set aside (for example vortices near island edges or steps, or at higher field), and why?
3. Which fields, temperatures and tip setpoints did you measure beyond those shown? The captions of Fig. 3 and Fig. 4B-D don't give the field, and the vortex spectra in Figs. 2 and 3 don't give a temperature.
4. What do the spectra look like at your second-best vortex, and at each vortex in the two- and three-vortex configurations of Fig. 4B-D?
5. How were the five levels in Fig. 3G fitted? Your values give |L2/L1| of about 2.5 and |L-2/L-1| of about 2.3, between the integer ratio (2) and the half-odd-integer ratio (3), and the text gives a spacing of "about 0.7 meV" while the fitted spacings are about 0.8 to 0.9 meV and 1.2 meV. How does a half-integer fit compare at your resolution?
6. Did you measure the same core location at zero field, and does the core sit on an interstitial Fe or other defect in topography? The zero-field spectrum in Fig. 2I is "at clean surface", and the short, isotropic decay you report also describes the excess-Fe bound state of Yin et al.
7. How does the ZBCP height change with tip-sample distance? Fig. 3B-E use a 1 nA setpoint and the maps use 500 pA.
8. What are the fitted decay lengths along the white and orange arrows in Fig. 3H-I and for the Bi2Te3-derived states you compare them with, and did you measure other directions?

A few notes on the table. Your strongest piece is the unsplit ZBCP away from the center (Fig. 3B-E). That is the test Xu et al. use to separate a vortex Majorana mode from the zero-bias peak of merged CdGM states, which splits right off center. The level sequence is the second test in that row. As fitted, its ratios sit between the two cases Kong et al. tell apart, which is why I marked it "part". Your paper also notes that excess interstitial Fe changes the FeTe band structure. Yin et al. found an isotropic, short-range zero-energy state at such Fe sites that survives to 8 T, so a zero-field spectrum at the same spot would settle that row quickly. The "number controllable" claim rests on vortex counts in zero-energy maps. Machida et al. found that only some vortices host a zero mode, and that the fraction falls with field. Spectra at every vortex in Fig. 4B-D would let your data speak to that directly.

## Related work

- Kong et al. 2019, "Observation of half-integer level shift of vortex bound states in an iron-based superconductor", <https://arxiv.org/abs/1901.02293>. Two classes of vortices in FeTe0.55Se0.45: integer level ratios with a zero-bias peak, half-odd-integer ratios without one.
- Chen et al. 2017, "Discrete energy levels of Caroli-de Gennes-Martricon states in quantum limit due to small Fermi energy in FeTe0.55Se0.45", <https://arxiv.org/abs/1709.09401>. In most superconductors, unresolved CdGM states show up as a symmetric zero-bias peak at the vortex center; in FeTe0.55Se0.45 the discrete levels are resolved.
- Yin et al. 2014, "Observation of a Robust Zero-energy Bound State in Iron-based Superconductor Fe(Te,Se)", <https://arxiv.org/abs/1403.1027>. An isotropic zero-energy state at interstitial excess Fe sites, with a decay length of about 10 Å, stable to 8 T.
- Machida et al. 2018, "Zero-energy vortex bound state in the superconducting topological surface state of Fe(Se,Te)", <https://arxiv.org/abs/1812.08995>. Some vortices host the zero-energy state and others don't; the fraction decreases with field.
- Zhu et al. 2019, "Nearly quantized conductance plateau of vortex zero mode in an iron-based superconductor", <https://arxiv.org/abs/1904.06124>. Tunnel-coupling-dependent STM shows a plateau for the zero-energy vortex state and none for finite-energy CdGM states.

Happy to rerun this if you share the source data and fit code.
