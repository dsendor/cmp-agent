# Lookalike check: Spin-singlet 2/3 edges by interferometry (arXiv 2609.01233v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper, "Interferometry reveals spin-singlet fractional quantum Hall edges in graphene", against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is quantum Hall interferometry of edge spin structure, which the library reaches only through its interferometer and practice entries, so I adapted the Fabry-Perot entry and the charge-family checks to your Mach-Zehnder geometry.

**The claim, as I read it.** In one graphene p-n junction device, whether Aharonov-Bohm oscillations appear with spin-selected integer probe channels shows that the νN = 2/3 interface channel is spin unpolarized below about 9.5 T and spin-down polarized near 11 T (Figs. 2, 3a, ED2, ED3). At (νP, νN) = (−2, 2/3) near 8.4 T the oscillations hold combination frequencies fnm = n f10 + m f01, including f11, which you read as two-electron interference through spin-charge separation, supported by faster thermal and bias decay of f10 and f01 (Figs. 3b to 3e, ED4).

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime (Aharonov-Bohm or Coulomb-dominated) they are in : Partly. Every configuration has a B-gate map with a 2D FFT, and the area check rests on an inferred arm spacing: "Given the 700 nm arm length set by electron-beam lithography, we extract a separation of approximately 170 nm between the two arms" (pp. 2 to 3).
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. "In contrast to the low-field regime, the AB oscillations exhibit a regular pattern with a single frequency (Fig. 2d)" (p. 3), and the integer (−2, 2) map shows only two fundamentals (Fig. 1f); charge traps and gate leakage are not discussed.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. "Temperature dependence of the AB oscillations under the same conditions as in b" (Fig. 3d caption, p. 5) repeats the Fig. 3b window ten times; the other maps have no repeats.
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. Supplementary Note 1 says "The devices were fabricated" (p. 13), and the data appear to come from one device, with no counts.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The junction transmission exhibits AB oscillations throughout the νN = 2/3 plateau (Fig. 2b)" (p. 3); the other windows are 0.1 to 1.1 T wide, with no reason given.
6. Give the processing steps from raw data to figures, with data and code : Partly. The visibility fits are described, "after excluding the three lowest-temperature data points" (p. 19); the step from T to δT and the FFT windowing are not, and the data are "available from the corresponding author upon reasonable request" (p. 8).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Coulomb-dominated interferometer (adapted from Fabry-Perot to Mach-Zehnder) | Tested in part | Field and gate map with stripe slope and spacing: all; Regime and charging parameters reported: no | "Consequently, the AB period is set by the electron charge." (p. 3) | Compare the flux-period areas of (−2, 1), (−2, 2), (−1, 2/3) and (−2, 2/3) with channel positions computed as in your ref. 36, and say whether localized charge can sit between the arms. |
| Fine-tuning and data selection | Tested in part | Devices and datasets measured, and how many showed the effect: no; How the shown data were chosen: no; A second device or dataset shown: part (multi-frequency maps in Figs. 2b, 2c, 3b, all from one device) | "The interference pattern displays multiple frequencies." (Fig. 2c caption, p. 4) | Give device and cooldown counts, and run the Fig. 3c FFT analysis on the wider Fig. 2c window. |
| Coulomb coupling of the copropagating integer probe channels (not in library) | Tested in part | Same analysis with the same νP = −2 probe edge where no spin-singlet edge is expected: all (Figs. 1f, 2d, 3e grey, ED4b); Bias-dependent visibility analysed for interaction-induced oscillations: part (ED4 shows the data, unanalysed for this); Probe-side interchannel interaction in the model: no | "Both f10 and f01 exhibit enhanced thermal decay and bias-voltage dependence (Extended Data Fig. ED4), compared with the spin-polarized regime." (p. 6) | Add the interaction between the two νP = −2 channels to your model and see whether it changes f11 or the fitted decay rates; measure the temperature dependence of the two (−2, 2) frequencies. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the multi-frequency pattern at νN = 2/3? Supplementary Note 1 refers to "The devices" (p. 13), and every figure seems to come from one device and one cooldown.
2. Why were the other devices set aside?
3. Which ranges of B, Vleft, Vright and VSi did you measure beyond the windows shown, for example around the 0.25 T by 55 mV window of Fig. 3b?
4. What does the second-best dataset look like? The wider Fig. 2c window (7.7 to 8.8 T) would be a natural place to repeat the Fig. 3c analysis.
5. The Fig. 3b window sets an FFT resolution of about 0.017 µm² in Φ0/ΔB and about 19 V⁻¹ in 1/ΔVleft, while f10 and f01 differ by 0.005 µm² and 52 V⁻¹. How stable are the assignments of f11, f02 and the higher peaks when you change the window, and does a longer field window separate f10 and f01 along B?
6. Does the Fig. 3c spectrum show weight at the difference frequency f10 − f01, near (−0.005 µm², 52 V⁻¹)? Single-particle paths that connect the two loops, or capacitive mixing between them, would generally add difference frequencies as well as sums, so its size helps separate those cases from your two-electron process.
7. How is δT obtained from the measured transmission (background subtraction, filtering), how are the visibilities in Fig. 3e extracted from the maps in Fig. 3d, and how do the decay rates B10, B01 and B11 change if the three lowest-temperature points are kept in the fits (p. 19)?
8. Have you measured the temperature dependence of the two (−2, 2) frequencies of Fig. 1f? There both probe spins interfere through integer channels, so the comparison would separate decay set by the copropagating probe channels from decay in the fractional channel.

## Related work

- Wei et al. 2017, "Mach-Zehnder interferometry using spin- and valley-polarized quantum Hall edge states in graphene", <https://arxiv.org/abs/1703.00110>. Shows beam splitters formed by scattering between same-spin channels along the physical graphene edge, the principle behind your spin access.
- Shimizu et al. 2024, "Mach-Zehnder interference of fractionalized electron-spin excitations", <https://arxiv.org/abs/2407.11490>. In an interferometer whose paths are copropagating spin-up and spin-down integer channels, interchannel Coulomb interaction fractionalizes the electron and gives interference beyond the single-particle first order.
- Levkivskyi and Sukhorukov 2008, "Dephasing in the electronic Mach-Zehnder interferometer at filling factor 2", <https://arxiv.org/abs/0801.2338>. A model where Coulomb coupling between the two ν = 2 channels sets the temperature dependence of the visibility and the lobe period in bias.
- Werkmeister et al. 2023, "Strongly coupled edge states in a graphene quantum Hall interferometer", <https://arxiv.org/abs/2312.03150>. In a graphene Fabry-Perot interferometer, strong repulsion between spin-split ν = 2 channels plus charge quantization gives phase jumps and AB frequency doubling.
- Song and Myoung 2025, "Asymmetric-gate Mach--Zehnder interferometry in graphene: Multi-path conductance oscillations and visibility characteristics", <https://arxiv.org/abs/2508.07380>. Single-particle simulations of graphene p-n interferometers where extra interface channels form nested loops and beat frequencies, with a weak peak at the summed loop area.

Happy to rerun this if you share the raw maps behind Figs. 2c and 3b.
