# Lookalike check: Heavy fermions and local moments in MATBG via planar tunneling (arXiv 2503.17875v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is a tunneling and thermodynamic measurement on a moiré flat band, outside the library's families, so I used the practice checks, adapted two entries and added three explanations from papers outside the library.

**The claim, as I read it.** From one graphite/hBN/MATBG planar tunnel junction, you extract dμ/dn from dI/dVb and dI/dVg (Eq. 3, Fig. 2a), read swings of m* from about 0.6 me below to about 0.06 me above positive integer fillings as the heavy and light charge-one excitations of the topological heavy fermion model (Fig. 3a, b, d), and read two plateaus in the Maxwell-relation entropy near 10 K and 20 K as 4-fold and 8-fold isospin local moment states (Fig. 4c, Extended Fig. 4c).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. The paper presents one junction and gives no count; the Author Contributions mention "devices" (p. 16).
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "a 3He refrigerator at a base temperature of 0.3 K, with a maximum perpendicular magnetic field of 8 T" (p. 22); the shown ranges are stated; the choice of Vb = ±42 mV and of the 4.2 to 36 K entropy window is not explained.
3. Give the processing steps from raw data to figures, with data and code : Partly. Methods Eqs. 1 to 13 lay out the chain, and "The entropy values and corresponding errors are obtained by performing a linear fit using three adjacent temperature points" (p. 26); the T(n) fit and quantum capacitance correction sit in an SI not in this PDF, no code is given, and data are "available from the corresponding author upon reasonable request" (p. 16).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Selection of the shown device and data (fine-tuning-and-selection) | Not tested (not mentioned) | Devices and datasets measured, and how many showed the effect: no; How the shown data were chosen: no; A second device or dataset shown: no | Not discussed. | State how many junctions and cooldowns you measured, and show the second-best one next to Fig. 3a and Fig. 4c. |
| Background normalization and capacitances shape the extracted dμ/dn (adapted from series-resistance-subtraction) | Tested in part | Series resistance calibrated independently, with its value (here T(n), Cb, Cg): part; Raw data before subtraction (here before division by T(n)): part | "we divide I by the transmission coefficient background, T(n) ∝ exp(0.258 ∙ n/n0), arising from the dependence of the barrier on carrier density (SI and Extended Figure 1a)" (p. 6); raw dI/dVb is in Fig. 1b, and dI/dVg appears only after normalization (Extended Fig. 1b). | Rerun Eq. 3 on data you have with the exponent, Cb/Cg and the dropped Eq. 7 factor ρ(EF)/ρ(EF + eVb) varied, and see where dμ/dn stays negative. |
| Carrier confinement under the planar probe (not in library; Tilak et al. 2021) | Tested in part | Filling of the probed region checked against the global electrostatic model: part; 0.3 K maps examined for Coulomb-diamond-like features: no | "The dμ/dn peaks at n/n0 = 0, 2, 4 align well with dark vertical lines in the top panel indicating low DOS." (Fig. 2f caption, p. 9) | Look in the 0.3 K maps (Fig. 1b, Extended Fig. 2a, b) for extra charging lines spaced by a charging energy, and report the CNP offset under the probe. |
| Twist-angle inhomogeneity across the ~1 µm² junction (not in library; Uri et al. 2020) | Tested in part | Twist angle from independent features compared: part; Spread across the probed area bounded: no | "The twist angle, 1.06° ± 0.02°, is determined by calibrating the carrier density n using high magnetic field Landau levels (LLs) and Chern insulators (CIs) (Methods)." (p. 3) | Fit n0 separately from the CNP fan, each Chern insulator line and the ±4 gaps, and use the feature widths to bound the angle spread alongside the 0.2 filling correction (p. 7). |
| Exchange-correlation contribution to dμ/dn read as mass (not in library; Larentis et al. 2014) | Left open by the authors | Mass measured independently at the fillings where it swings: no; dμ/dn compared with the inverse DOS from Methods Eq. 6: no | "While this expression is valid for weakly-correlated excitations with doping-independent degeneracy, we use it to qualitatively estimate the carriers’ effective mass" (p. 11) | Compare dμ/dn with 1/ρ from Eq. 6 on the same data; the difference estimates the interaction term that Eq. 4 assigns to m*. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the heavy-to-light dμ/dn swings and the two entropy plateaus? The twist angle reads 1.06° ± 0.02° (p. 3), 1.08° (Fig. 1b caption, p. 6) and 1.07° (Methods, p. 22); are these one device?
2. Why were the other devices or cooldowns set aside?
3. Which ranges did you measure beyond the ones shown: other bias voltages for the dμ/dn extraction besides ±42 mV, the hole side for the temperature series and entropy, and fields above 6 T for the dμ/dn map?
4. What does the second-best device or dataset look like for Fig. 3a and Fig. 4c?
5. How was the exponent 0.258 in T(n) obtained, what is its uncertainty, and how do the negative dμ/dn dips in Fig. 2a and the masses in Fig. 3a change when it is varied over that range? Could you show the raw dI/dVg next to Extended Fig. 1b?
6. Eq. 3 is an approximation of Methods Eq. 7. How large is ρ(EF) compared with ρ(EF + eVb) at Vb = ±42 mV across the flat bands (Eq. 6 gives it from your data), how does the ~20 meV phonon offset enter the probed energy, and does dμ/dn keep its shape at other bias voltages?
7. For the entropy, the chemical potential at the CNP is set to 0 at every temperature (Extended Fig. 4a). How do Fig. 4c and Extended Fig. 4c change if μ at the CNP is allowed to drift with temperature, and if the fit uses more than three adjacent temperature points?
8. Do high-resolution dI/dVb(Vb, Vg) maps at 0.3 K show Coulomb-diamond-like features of the kind your group reported in a planar MATBG junction (arXiv 2106.11333), and what doping offset does the graphite probe induce in the region beneath it?

## Related work

- Zondiner et al. 2020, "Cascade of Phase Transitions and Dirac Revivals in Magic Angle Graphene", <https://arxiv.org/abs/1912.06150>. Local compressibility shows asymmetric jumps near integer fillings, read as flavor resets.
- Rozen et al. 2021, "Entropic evidence for a Pomeranchuk effect in magic angle graphene", <https://arxiv.org/abs/2009.01836>. Electronic entropy rises to about 1 kB per moiré cell near filling one and is quenched by an in-plane field, a field test you could apply to your plateaus.
- Saito et al. 2021, "Isospin Pomeranchuk effect and the entropy of collective excitations in twisted bilayer graphene", <https://arxiv.org/abs/2008.10830>. Entropy of order unity per cell near ν = -1, with a measurable fraction suppressed by in-plane field.
- Tilak et al. 2021, "Flat band carrier confinement in magic-angle twisted bilayer graphene", <https://arxiv.org/abs/2106.11333>. STM and a planar tunneling junction on MATBG show Coulomb diamonds from carriers confined in a potential well about the size of the tunneling electrode.
- Uri et al. 2020, "Mapping the twist angle and unconventional Landau levels in magic angle graphene", <https://arxiv.org/abs/1908.04595>. NanoSQUID maps find local twist-angle spans close to 0.1° in devices with good global transport.

Happy to rerun this if you share the dI/dVb and dI/dVg data behind Fig. 2a and Fig. 4.
