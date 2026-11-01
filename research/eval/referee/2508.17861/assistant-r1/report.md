# Lookalike check: Mottness and superconductivity in 4Hb-TaS2 (arXiv 2508.17861v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is scanning tunneling spectroscopy of a correlated material and makes no topological claim. So I adapted the one entry that fits (a Kondo resonance on a site coupled to a superconductor) and the general practice checks, and I added two explanations from the 4Hb-TaS2 and STM literature that the library lacks.

**The claim, as I read it.** Filling rises across the Star of David clusters of the 1T termination, from about 0.2 electrons toward half filling. Along the way Hubbard bands emerge at a constant U ≈ 190 meV, and the central peak sharpens and vanishes as in the Brinkman-Rice picture (Figs. 2d and 3a to 3f). The linear temperature dependence of the peak width on one cluster (Fig. 3h) is offered as evidence against a Kondo reading. A proximity gap on the 1T layer closes as filling rises (Fig. 4).

## Checks a careful reader will look for

1. Track the zero-bias peak across fillings (adapted from the library's search for even-odd patterns across charge states) : Done. "The spectral weight of the central quasiparticle state with increasing electron filling" (Fig. 3e caption, p. 12), with the width in Fig. 3f.
2. Show the peak across the whole cluster population and the full temperature and field ranges (adapted from showing the peak over wide ranges) : Partly. Fig. 2d holds "more than one hundred typical dI/dV spectra" (p. 4) out of about four thousand clusters, and Fig. 3h follows one cluster ("ε = -76 meV").
3. State the setpoint and the normalization, and show raw spectra (adapted from the series resistance check) : Partly. Every caption gives setpoints, for example "Vs = -1000 mV, It = 2.5 nA, Vmod = 2 meV" (Fig. 2 caption, p. 11). The normalization is described in words, "their spectral weights offer a basis for normalizing the dI/dV spectra" (p. 4), without the exact procedure.
4. Report samples and datasets measured, how many showed the effect, and why others were set aside : Partly. Cluster counts are given: "approximately four thousand SoD clusters" and "approximately 12% of the clusters show a prominent zero-bias peak" (p. 3). Crystals, cleaves and fields of view are not counted.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. The width "decreases linearly with temperature from 4.2 to 0.3 K (Fig.3h)" (p. 5). The field range behind Supplementary Fig. 10 and the reason for each range are not in the main text.
6. Give the processing steps from raw data to figures, with data and code : Partly. The fit models are named ("Lorentzian fits to the peaks", Fig. 3b caption; "The FWHM is obtained via Fano fitting", Fig. 3f caption, p. 12). The data availability statement reads "The data supporting the findings of this study are available from the corresponding author upon reasonable request." (p. 15)

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Kondo resonance of a cluster moment screened by 1H electrons (library entry adapted: dot to SoD cluster, superconducting contact to 1H layer) | Tested in part | Even-odd occupancy, read as filling dependence: all (Figs. 3e, 3f); temperature dependence: part (one cluster, Fig. 3h); Zeeman splitting: part (Supplementary Fig. 10 is not in the v1 PDF) | "the HWHM of the central peak observed here is generally an order of magnitude smaller, does not saturate but decreases linearly with temperature from 4.2 to 0.3 K (Fig.3h)" (p. 5) | Repeat Fig. 3h on several clusters across ε, and compare with a Kondo curve whose T_K uses the 1T-1H hybridization |
| Fine-tuning and selection | Tested in part | Devices and datasets counted: part (clusters only); how the data were chosen: part ("typical"); second dataset: part (Supplementary Note 4 is not in the v1 PDF) | "In Fig. 2d, we have sorted more than one hundred typical dI/dV spectra according to the exact energy of the broad hump near -0.5 eV." (p. 4) | Show Fig. 2d for every cluster in one field of view, and the same plot from a second crystal |
| Extrinsic (thermal and modulation) broadening of the peak width (not in library) | Not tested (data bear on it) | Intrinsic width extracted with a lineshape that includes extrinsic broadening: no | "HWHM of the central quasiparticle peak at different temperatures (see SI Fig. S9)" (Fig. 3h caption, p. 12) | Refit the Fig. 3h spectra with a lineshape convolved with the Fermi and modulation broadening (Turco et al.) and plot the intrinsic width |
| Tip-induced switching between Kondo cluster and depleted flat-band states (not in library) | Not tested (not mentioned) | Same cluster at several tip heights or setpoint biases: no; hysteresis or low-frequency noise checked: no | Not discussed. | Repeat a few of the Fig. 2b clusters at two or three setpoints and look for jumps or hysteresis |

## Questions about devices and data

1. How many crystals, cleaves and fields of view did you measure, and how many showed the zero-bias-peak clusters and the 1T-layer gap?
2. Why were other fields of view or crystals set aside, and how were the "more than one hundred typical" spectra in Fig. 2d chosen from the roughly four thousand clusters in Fig. 2a?
3. Which ranges did you measure beyond the ones shown, for example temperature series on clusters other than the one at ε = -76 meV in Fig. 3h, and the field range and direction behind Supplementary Fig. 10?
4. What does the second-best dataset look like, for example Fig. 2d or Fig. 4e rebuilt from a second crystal or from the other STM system?
5. Were the widths in Figs. 3f and 3h corrected for thermal smearing (about 1.3 meV full width at 4.2 K) and for the lock-in modulation? The plotted HWHM runs from about 0.65 to 1.7 meV against about 2.4 meV for the Kondo line, a factor of about 1.5 to 4, so could you say how "an order of magnitude" follows, and which parameters set the gray line?
6. Which hybridization scale enters your T_K estimate? The formula uses the narrow-band width W0; how does T_K change if the 1T-1H hybridization is used, and could it fall into the 0.3 to 4.2 K window of Fig. 3h?
7. Did the spectrum of a given cluster change with setpoint bias, current or tip height? In 4Hb-TaS2 the tip has been reported to toggle clusters between a Kondo cluster state and a flat-band state, with hysteresis.
8. How exactly were the spectra in Fig. 2d normalized, do the trends in Figs. 3d and 3e hold in the raw spectra, and why are the fits Lorentzian in Fig. 3b and Fano for Fig. 3f? (The text cites "Fig. 3g" for the spectral weight, which the caption labels 3e.)

## Related work

- Vaňo et al. 2021, "Artificial heavy fermions in a van der Waals heterostructure", <https://arxiv.org/abs/2103.11989>. STM on 1T/1H-TaS2 reads the zero-bias resonance as a Kondo effect of localized moments coupled to 1H conduction electrons, the main alternative reading to yours.
- Crippa et al. 2023, "Heterogeneous Ta-dichalcogenide bilayer: heavy fermions or doped Mott physics?", <https://arxiv.org/abs/2302.14072>. First-principles work that quantifies the 1T-1H hybridization and places these bilayers closer to a doped Mott insulator; its hybridization value could feed your T_K estimate.
- Nayak et al. 2023, "First Order Quantum Phase Transition in the Hybrid Metal-Mott Insulator Transition Metal Dichalcogenide 4Hb-TaS2", <https://arxiv.org/abs/2303.01447>. In 4Hb-TaS2, a first-order transition between a Kondo cluster state and a depleted flat-band state, induced by electric field, temperature and the probe tip, with hysteresis and low-frequency noise.
- Wan et al. 2022, "Evidence for ground state coherence in a two-dimensional Kondo lattice", <https://arxiv.org/abs/2207.00096>. In 1T/1H-TaSe2 at 340 mK, two resonances near the Fermi energy and their nonlinear splitting in field are used to tell a screened Kondo lattice from magnetic order, a useful template for reading your field data.
- Turco et al. 2023, "Demonstrating Kondo behavior by temperature-dependent scanning tunneling spectroscopy", <https://arxiv.org/abs/2310.09326>. Shows how extrinsic broadening enters finite-temperature Kondo linewidths in STM and gives a lineshape for extracting the intrinsic width.

Happy to rerun this if you share the Fig. 3h spectra and the full cluster set behind Fig. 2a.
