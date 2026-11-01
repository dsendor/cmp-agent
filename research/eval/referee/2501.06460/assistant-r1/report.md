# Lookalike check: Multiband superconductivity in alternating twisted quadralayer graphene (arXiv 2501.06460v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper sits outside the library's main scope (moiré superconductivity read through critical currents, Landau fans and V-I curves), so I adapted one supercurrent entry, used the practice checks, and added three lookalikes from the moiré and 2D superconductor literature, marked "(not in library)".

**The claim, as I read it.** One 1.58° ATQG Hall bar shows D-tunable superconductivity with TBKT up to 1.6 K (Fig. 1, 3, 4; Supp. Fig. 5). Landau fans separate Dirac and flat band carriers (Fig. 2). Critical currents give a flat band velocity near 1700 m/s and a superfluid stiffness up to about 4 × 10^7 H^-1, one order above the conventional value, which you attribute to quantum metric (Fig. 5).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. The paper presents one device, "The ATQG sample" (p. 3), with no count of devices fabricated or measured.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Ranges can be read from the figures and Methods, for example "a DC signal (maximum ~ 650 nA)" (Supp. Note 1, p. 17); Landau fans appear only at D = 0 and 1.7 K and Ds only at νtot = 2.31, with no reason given.
3. Give the processing steps from raw data to figures, with data and code : Partly. Tc and Bc0 are defined (Supp. Note 3, p. 19); the Bc criterion at each temperature, the critical current criterion and the width used for js are not stated, and data are "available from the corresponding authors upon reasonable request" (p. 7).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets counted: no; how shown data were chosen: no; second device or dataset: part (other contact pairs of the same device, Supp. Fig. 1b; a second D-Idc map, Supp. Fig. 7a) | "Fig. 1d exhibits a typical longitudinal resistance (Rxx) map" (p. 3, Fig. 1d) | State how many devices you made and measured, and show a second pair's D-Idc map and Landau fan from data you already have. |
| Finite-bias resonances moving the switching current (adapted: critical current growing with D read as quantum-metric stiffness) | Tested in part | Finite-bias dV/dI plotted with the switching current: all (Fig. 5c, 4e); followed across gate voltage: part (Ic maps versus νtot at D = 0.26 and 0, Fig. 5a, Supp. Fig. 6a; Ds only at νtot = 2.31) | "the dV/dI curves in Fig. 4e show a higher critical current at finite D than that at zero D, suggesting a stronger coupling superconductivity" (p. 6, Fig. 4e) | Overlay the switching edge on the finite-bias ridges in Fig. 5c and say whether the Ds peak near D ≈ 0.2 to 0.25 V/nm sits where a ridge meets the edge; compute Ds(D) at a few other fillings. |
| Twist-angle disorder (not in library) | Tested in part | Local twist angle mapped or bounded: no; full-filling density and fans compared across contact pairs: part (Rxx(n) for four pairs at D = 0; fans from one pair) | "The transport curves between different bars in Supplementary Fig.1b suggest the uniform angle distribution" (Supp. Note 2, p. 18) | Extract n0 and θ for each pair in Supp. Fig. 1b, and show a second pair's fan to see whether the series from νtot ≈ 3 and 3.3 recur there. |
| Moiré-inhomogeneity Josephson network setting the switching current (not in library) | Not tested (data bear on it) | Switching-current distributions: no; BKT broadening by inhomogeneity checked: no | "we calculate the superfluid stiffness at zero temperature limit using the critical current density js in Fig. 5c" (p. 6, Fig. 5c); Fig. 5c and Supp. Fig. 7a differ about twofold in Ic at νtot = 2.31, and normal-state Rxx differs several-fold between pairs (Supp. Fig. 1b), which geometry or inhomogeneity could set | Measure switching distributions at νtot = 2.31 for a few D values, or compare with a kinetic inductance estimate as in Tanaka et al. and Banerjee et al. |
| Inhomogeneity mimicking BKT nonlinear V-I (not in library) | Not tested (data bear on it) | Exponent a(T) of V ∝ I^a followed through the transition: no; V-I compared with an inhomogeneity model: no | "the temperature-dependent voltage-current (V-I) curves show a clear Berezinskii–Kosterlitz–Thouless (BKT) transition at the critical temperature of TBKT = 1.1 K" (p. 3, Fig. 1g) | Plot a(T) from the Fig. 1g and Supp. Fig. 5 curves and compare its jump with an inhomogeneous model, as Venditti et al. did (https://arxiv.org/abs/1905.01221). |

## Questions about devices and data

1. How many ATQG devices did you fabricate and measure, and how many showed the superconductivity and the D-tunable critical current? The paper shows one device, at 1.58°.
2. Why were the others set aside, or was this the only device that worked?
3. Which ranges did you measure beyond the ones shown, for example Landau fans at D ≠ 0 or below 1.7 K, and critical current maps versus D at fillings other than νtot = 2.31?
4. What does the second-best dataset look like, for example the D-Idc map and the Landau fan from another contact pair in Supp. Fig. 1?
5. Which contact pair, temperature and cooldown are Fig. 5a and 5c from, and what width did you use to turn Idc into js and jn? Supp. Fig. 7a (ν = 2.31, 100 mK) shows a switching edge near 50 nA at D = 0, about half the value in Fig. 5c.
6. In Fig. 5c, does the switching-current peak near D ≈ 0.25 V/nm sit where a finite-bias dV/dI ridge meets the switching edge, and how does Fig. 5d change if that region is set aside?
7. What criterion sets Bc at each temperature in Supp. Fig. 2b, and how far do ξ × kF in Fig. 3c and 4c move with the Tc and Bc criteria (30 to 50%) and with n* taken as |νflat − 2| or from nH?
8. The universal BKT relation gives Ds(TBKT) = 8e²kBTBKT/(πħ²), about 1.3 × 10^8 H^-1 for TBKT = 1.6 K by my estimate, above the roughly 4 × 10^7 H^-1 in Fig. 5d. How do these two estimates of the stiffness compare in your analysis?

## Related work

- Tian et al. 2021, "Evidence for Flat Band Dirac Superconductor Originating from Quantum Geometry", <https://arxiv.org/abs/2112.13401>. In twisted bilayer graphene, uses Schwinger-limited nonlinear transport to get vF ~ 1000 m/s and a critical-current-based stiffness, the method your Fig. 5 follows.
- Tanaka et al. 2024, "Superfluid Stiffness and Flat-Band Superconductivity in Magic-Angle Graphene Probed by cQED", <https://arxiv.org/abs/2406.13740>. Measures stiffness directly through kinetic inductance in MATBG and finds it much larger than conventional Fermi liquid theory predicts.
- Banerjee et al. 2024, "Superfluid stiffness of twisted multilayer graphene superconductors", <https://arxiv.org/abs/2406.13742>. Kinetic inductance in twisted trilayer graphene gives a linear-in-T stiffness and nodal signatures, an independent route to the quantity in your Fig. 5d.
- Uri et al. 2020, "Mapping the twist angle and unconventional Landau levels in magic angle graphene", <https://arxiv.org/abs/1908.04595>. NanoSQUID imaging finds local twist-angle spans near 0.1° in devices that look uniform and superconducting in global transport.
- Mukherjee et al. 2025, "Superconducting magic-angle twisted trilayer graphene hosts competing magnetic order and moiré inhomogeneities", <https://arxiv.org/abs/2406.02521>. Switching statistics show a Josephson-network response from moiré inhomogeneity and a broadened BKT transition, with Js ~ 0.15 K.

Happy to rerun this if you share the figure data or a second contact pair's maps.
