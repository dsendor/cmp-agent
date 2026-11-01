# Lookalike check: Magnetization and Josephson current coupling drives the Josephson diode effect in FeTe0.55Se0.45 van der Waals junctions (arXiv 2610.29124v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library has no ordered checks for diode signals and its Shapiro entries are written for missing odd steps, so I adapted the Shapiro checks and one Shapiro entry to your half-integer steps, and added three lookalikes from outside the library, each with a paper I opened.

**The claim, as I read it.** One FTS vdW junction shows unequal switching currents at zero applied field (|Ic+| = 35.2 μA, |Ic−| = 28.9 μA, η = 9.8%, Fig. 2a-b, p. 7), which you trace to interfacial magnetization coupled to the Josephson current. The supporting signals are a Fraunhofer pattern that depends on sweep direction (Fig. 3a), a voltage feature near 170 μV read as magnetic resonance (Fig. 3b, Supp. Fig. 4), and asymmetric ±1/2 Shapiro steps at Bx = 75 G read as a second harmonic plus a magnetization-induced phase shift (Fig. 4, Supp. Figs. 6-7).

## Checks a careful reader will look for

1. Dc curve without irradiation at the Shapiro settings, adapted to half-integer steps : Partly. "under this condition the difference between the n-p and p-n sweeps is negligible and the I − V hysteresis is essentially absent" (Supp. p. 35); the undriven edge of Fig. 4a carries it, with no separate dV/dI versus V marked at ±hf/4e.
2. Full frequency and power maps : Done. "Both the dV/dI maps and the bin-count maps measured at 4.348, 7.580, and 9.680 GHz consistently exhibit integer and asymmetric half-integer Shapiro step structures." (Supp. p. 35, Supp. Fig. 6)
3. Same measurement where the proposed mechanism should be absent (a non-magnetic control junction, or a regime with no interfacial magnetization) : Not done. The comparison without magnetization is a simulation (Supp. Fig. 8).
4. Junction transparency measured and tuned : Not done. Argued from other junctions (p. 13).
5. Devices and datasets measured, and how many showed the effect : Not done. "Our devices exhibit a robust zero-field diode response" (p. 2); every figure I could trace is from one junction.
6. Full parameter ranges and why each shown range was chosen : Partly. Bx to ±200 G, By to ±400 G, 0 to 5 K and "microwave power in the range of -60~10 dBm" (p. 15) are given, and the 75 G choice is explained (p. 12); out-of-plane field and other Shapiro fields are not mentioned.
7. Processing from raw data to figures, with data and code : Partly. The switching threshold (p. 16), FFT filtering (Supp. p. 28) and binning (p. 16) are described; "available from the corresponding authors upon reasonable request" (p. 17), no code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Vortex barriers and Meissner screening in the parent superconductor (`diode-vortex-screening`) | Tested in part | Plain film or junction of the parent superconductor: no; effect followed against field: all | "the observed zero-field diode response is unlikely to originate from the bulk crystal alone" (p. 7); Fig. 2c-d and Supp. Fig. 1b follow η over ±100 G. | Run the same switching statistics on a single-flake FTS bridge on this chip, and plot η against B − B0 with the magnet's residual field calibrated. |
| Self-field from nonuniform bias plus trapped-vortex stray fields (not in library; Golod and Krasnov) | Not tested (data bear on it) | Current through other contacts: no; with and without trapped vortices: no | "show similar overall patterns symmetric around Bx = −8 G" (p. 7, Fig. 2c), with main lobes at −6 G and +22 G for opposite sweeps (Fig. 3a). | Swap current leads; compare zero-field η after a thermal cycle above 13.5 K in compensated zero field and after excursions to ±200 G. |
| Finite-voltage resonances (MAR, Andreev states, self-induced steps), adapted to the 170 μV feature (`field-enhanced-supercurrent-resonances`) | Tested in part | Finite-bias dV/dI with switching current: all; across gates and other devices: no | "this feature remains concentrated around a nearly field-independent characteristic voltage" (p. 10, Fig. 3b). | Follow V_MR with temperature in data you may already have (Supp. Fig. 1b runs to 5 K), and compare 170 μV with the interface gap and circuit resonances. |
| Nonmonotonic dc resistance shaping step features, adapted to half-integer steps (`shapiro-nonlinear-resistance`) | Tested in part | Undriven dV/dI: part (map edge only); frequency and power maps: all; other regimes: part (Bx = 0 G map, with another stated origin) | "weaker but reproducible enhanced counts at n = ±1/2" (p. 12, Fig. 4b). | Show the ±1/2 counts at all four frequencies on one hf/2e-scaled axis; a fixed dc feature cannot sit at ±hf/4e for every f. |
| Skewed CPR from a transparent junction (not in library; Ueda et al.) | Not tested (argued, not tested) | Half-integer steps versus temperature: no; transmission estimated or tuned: no | "This value exceeds the second harmonic typically expected from highly transparent Josephson junctions" (p. 13). | Estimate transmission from the excess current at high bias, and track the ±1/2 widths with temperature. |
| Trapped vortices giving half-integer steps (not in library; Zhu et al.) | Not tested (not mentioned) | Across thermal cycles: no; after field training: no | Not discussed. | Repeat the 75 G map after a thermal cycle and after approaching 75 G from both sweep directions. |
| Fine-tuning and selection (`fine-tuning-and-selection`) | Tested in part | Counts: no; how data were chosen: part; second device or dataset: part (same junction only) | "near the first Fraunhofer node, where the JDE remains pronounced while the MR induced voltage feature is strongly suppressed" (p. 12). | State device and cooldown counts, and show Fig. 2a-d for a second junction. |

## Questions about devices and data

1. How many devices (and cooldowns) did you measure, and how many showed the zero-field diode, the sweep-dependent Fraunhofer pattern, the feature near 170 μV and the asymmetric half-integer steps?
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown, for example out-of-plane field, Shapiro maps at fields other than 0 G and 75 G, and temperature series of the 170 μV feature and of the half-integer steps?
4. What does the second-best device or dataset look like?
5. What is the residual field of the vector magnet at nominal zero, which sweep direction and field history came before Fig. 2a-d and the 75 G Shapiro data, and does the symmetric point near −8 G move after warming above 13.5 K and cooling in a compensated zero field?
6. Does the zero-field diode keep its sign and size when you inject the current through a different pair of contacts?
7. How does V_MR change with temperature, and how does 170 μV compare with the interface gap and with resonances of the on-chip and bias circuitry near 82 GHz?
8. The simulations use different α for Supplementary Fig. 3c-d (Eq. S5), Fig. 3d (Eq. S7) and Fig. 4g-i (Eq. S10). Can one parameter set reproduce all three?

A note on question 5: η crosses zero near −8 G (Supp. Fig. 1b plots against B − B0), so the zero-field value of 9.8% sits about 8 G from the symmetric point. Your Fig. 3a shows that this point moves by tens of gauss with sweep direction. Knowing the field history would let a reader separate an interfacial moment from a remanent or trapped field.

## Related work

- Hou et al. 2022, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. A strong diode effect in plain Nb and V films at fields as small as 1 Oe, traced to asymmetric vortex barriers and Meissner screening.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. A zero-field diode in conventional Nb junctions from the self-field of nonuniform bias plus stray fields of a trapped vortex. The polarity changes with bias configuration and vortex state.
- Qiu et al. 2023, "Concurrent Ferromagnetism and Superconductivity in Fe(Te,Se) van der Waals Josephson Junctions", <https://arxiv.org/abs/2303.00966>. FTS vdW junctions with magnetic hysteresis below Tc and a stochastic field-free diode, read as interfacial ferromagnetism.
- Ueda et al. 2020, "Half-Integer Shapiro Steps in a Short Ballistic InAs Nanowire Josephson Junction", <https://arxiv.org/abs/2004.14039>. Half-integer steps that vanish as temperature rises or transmission falls, matched by a skewed CPR.
- Zhu et al. 2025, "Manipulating fractional Shapiro steps in twisted cuprate Josephson junctions", <https://arxiv.org/abs/2512.01586>. Half-integer steps in stacked cuprate junctions that change with thermal cycling and field training, which the authors attribute to trapped vortices.

Happy to rerun this if you share the switching-current and Shapiro data behind Figs. 2 and 4.
