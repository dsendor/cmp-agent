# Lookalike check: Spin-singlet 2/3 edges by interferometry (arXiv 2609.01233v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**Paper.** "Interferometry reveals spin-singlet fractional quantum Hall edges in graphene", Ayache, Kim, Kuiri et al., https://arxiv.org/abs/2609.01233

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library is built mostly around Majorana-type transport, so I adapted its interferometer and practice entries to a Mach-Zehnder measurement of edge spin structure, and I added two explanations from papers outside the library.

**The claim, as I read it.** In one graphene p-n junction device, the presence or absence of AB oscillations against integer probe channels of known spin shows that the νN = 2/3 interface channel is spin unpolarized below about 9.5 T (single frequency at (−1, 2/3), Fig. 3a; combination frequencies fnm = n f10 + m f01 at (−2, 2/3), Fig. 3b,c) and spin polarized near 11 T (single frequency, Fig. 2d; no oscillations at (−1, 2/3), Fig. ED3). The f11 component and the faster thermal decay of f10 and f01 (Fig. 3e) are read as spin-charge separation and a two-electron spin swap.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Partly. Every key regime has a B and gate map with a 2D FFT, "showing multiple frequencies that are linear combinations of two frequencies" (Fig. 3c). The AB reading rests on the area argument for the integer case (p. 2 to 3). The Coulomb-dominated alternative isn't discussed, and Fig. 2c has no FFT.
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. The integer and high-field controls are there: "By contrast, no AB oscillation is observed at (νP , νN ) = (−1, 1) (Extended Data Fig. ED2)" (p. 3), and Fig. 2d shows a single frequency. Charge traps and gate leakage aren't discussed.
3. Repeat sweeps to separate reproducible features from stochastic jumps : Not done. Fig. 3d is taken "under the same conditions as in b" at ten temperatures, which comes close, but no repeat at base temperature is shown or stated.
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. Supplementary Note 1 says "The devices were fabricated" in the plural; all data shown come from one device, with no count of devices or cooldowns.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The junction transmission exhibits AB oscillations throughout the νN = 2/3 plateau (Fig. 2b)" (p. 3). The 0.25 T by about 50 mV window of Fig. 3b, where the fnm analysis is done, isn't explained.
6. Give the processing steps from raw data to figures, with data and code : Partly. The visibility fits are described: "We fit log Visnm linearly as a function of temperature after excluding the three lowest-temperature data points" (SI p. 7). How δT is obtained from T isn't described, and "The data supporting the findings of this study are available from the corresponding author upon reasonable request" (p. 8).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection of a representative example | Tested in part | Devices and datasets counted: no; how shown data were chosen: no; second device or dataset: part (Fig. 2c is a second low-field map of the same device, with no FFT) | "The interference pattern displays multiple frequencies." (Fig. 2c caption, p. 4) | State devices, cooldowns and how many showed fnm; add a 2D FFT of Fig. 2c and of the ED4a dataset |
| Coulomb-dominated oscillations (adapted from the Fabry-Perot entry) | Tested in part | Field and gate map with stripe slope and spacing: all; regime and charging parameters: part (AB named, no charging estimate) | "Given the 700 nm arm length set by electron-beam lithography, we extract a separation of approximately 170 nm between the two arms." (p. 2 to 3, Fig. 1e) | From maps you have, report the stripe slope sign for f10 and f01 and check that the B areas stay fixed across the plateau; bound the charging energy of the region between the arms |
| Single-particle multi-path loops (not in library) | Tested in part | Two-loop configuration without the fractional channel checked for a summed-area peak: all (Fig. 1f); noninteracting multi-path model of the (−2, 2/3) geometry: no | "as only a single winding is allowed in the noninteracting MZI of the integer QH regime in Fig. 1." (p. 4) | Quote the upper bound on a summed-area peak in Fig. 1f and compare it with the f11 to f10 ratio in Fig. 3c; run a noninteracting scattering model of the nested (−2, 2/3) loops |
| Valley-isospin selection at the beam splitters (not in library) | Tested in part | Valley pairing held fixed between coupling and no-coupling configurations: part (integer calibration only, Figs. ED1a and ED2a); beam-splitter transmission across gate settings with no oscillations: all (Figs. ED2d to f, ED3d to f) | "Spin is conserved during this scattering, while the valley degree of freedom changes [34, 35]" (p. 2) | State the expected valley content of the 2/3 channel in both regimes and of the νP = −1 and −2 probes, so the (−1, 2/3) blocking near 11 T reads as spin alone |

## Questions about devices and data

1. How many devices did you measure, and how many showed the multi-frequency pattern at νN = 2/3 below about 9.5 T?
2. Why were the others set aside?
3. Which ranges of B, Vleft, Vright and VSi did you measure in the low-field (−2, 2/3) regime beyond the 0.25 T by about 50 mV window of Fig. 3b, and does the fnm = n f10 + m f01 pattern hold across them?
4. What does the second-best dataset look like, for example a 2D FFT of the Fig. 2c map or of a second cooldown?
5. In Fig. 3c the B areas of f10 and f01 differ by 0.005 µm², while a 0.25 T window gives an FFT resolution in Φ0/ΔB of about 0.017 µm². Does the spin-up and spin-down assignment rest on the gate frequencies, and how does it hold up with a wider field window?
6. In the integer (−2, 2) map of Fig. 1f, how large could a peak at the summed frequency be, relative to the two primary peaks, and how does that bound compare with the f11 to f10 amplitude ratio in Fig. 3c?
7. What valley content do you expect for the 2/3 interface channel in each regime, and for the probe channels at νP = −1 and −2, so a reader can see that the absence of oscillations at (−1, 2/3) near 11 T follows from spin alone?
8. How is δT obtained from the raw transmission (background subtraction, filtering, FFT windowing), and could you show a raw T map for Fig. 3b?

## Related work

- Amet et al. 2014, "Selective equilibration of spin and valley polarized quantum Hall edge states in graphene", https://arxiv.org/abs/1307.4408. In dual-gated graphene, edge states with opposite spins propagate without mixing, so equilibration reveals the spin polarization of each filling factor.
- Wei et al. 2017, "Mach-Zehnder interferometry using spin- and valley-polarized quantum Hall edge states in graphene", https://arxiv.org/abs/1703.00110. P-n junction MZIs with visibilities up to 98%, with beam splitters formed by scattering between same-spin channels along the physical edge.
- Jo et al. 2021, "Quantum Hall valley splitters and tunable Mach-Zehnder interferometer in graphene", https://arxiv.org/abs/2011.04958. Beam splitters couple channels of opposite valley, and their transmission can be tuned from zero to near unity.
- Trifunovic and Brouwer 2019, "Valley isospin of interface states in a graphene pn junction in the quantum Hall regime", https://arxiv.org/abs/1902.07975. Edge-to-interface scattering at the corners is governed by valley isospin conservation, which sets the junction conductance.
- Song and Myoung 2025, "Asymmetric-gate Mach--Zehnder interferometry in graphene: Multi-path conductance oscillations and visibility characteristics", https://arxiv.org/abs/2508.07380. A noninteracting model in which extra interface channels give multiple MZ loops, beat patterns, and a weak higher-order loop at the summed area.

Happy to rerun this if you share the figure data or the raw transmission maps.
