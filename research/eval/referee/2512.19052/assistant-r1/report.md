# Lookalike check: Gate-imprinted memory and light-induced erasure of superconductivity at KTaO3-based interfaces (arXiv 2512.19052v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is outside the library's field, so only its general entries apply; I
added three ordinary explanations from papers I opened, marked "(not in library)".

**The claim, as I read it.** Back-gate cycles between -50 V and +50 V raise Tc of the
AlOx/KTaO3(111) 2DEG (at Vg = 0, from about 1.02 K to about 1.09 K, Supp. Fig. 1e) and
Rs, and red light at 10 K resets both (Fig. 2c, h, i). You read this as polar-nanoregion
(PNR) reorientation and oxygen-vacancy (OV) charge switching, from two dielectric loss
peaks (Fig. 3b, c), a slope change of loop size against ε near 35 K (Fig. 3d) and
dark-relaxation maxima at 35 K and 95 K (Fig. 4b, c). All data come from one sample.

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Not done. One sample is described: "the transport measurements were conducted in van der Pauw (vdP) method on the square-shape sample" (Methods, p. 10).
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Gate cycles are conducted at multiple temperatures from 5 K to 180 K" (Supp. p. 2), and 10 K is explained (p. 3); the ±50 V range and the single LED wavelength and drive carry no stated reason.
3. Give the processing steps from raw data to figures, with data and code : Partly. "Sheet resistance Rs was calculated from R by performing finite-element modelling (FEM)" (Methods, p. 10), with Tc and ε defined; there is no data or code statement, and the reading of peak positions in Fig. 3b is not described.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Selection of a non-representative example after fine-tuning | Tested in part | Devices and datasets measured, and how many showed the effect: no; How the shown data were chosen: part (stated for Supp. Fig. 2 only); A second device or dataset shown: part (repeat runs on the same sample, Supp. Fig. 4) | "Supplementary Figure 2 plots the data measured in the fourth cycle at each temperature to ensure the memory effect is fully imprinted." (Supp. p. 2) | State the number of samples and cooldowns, and show the Tc memory and its erasure in a second sample or cooldown. |
| Electrons irreversibly leaving the well into substrate traps above a filling threshold (not in library; Biscaras et al.) | Tested in part | Reversibility checked against the largest gate voltage applied before: part (±40 V against ±50 V at 10 K, Rs only, Supp. Fig. 4); Resistance relaxation after a gate step: part (Rs traces in Supp. Fig. 4 are plotted and not analysed); Warm-up at zero gate after cycling, showing where the state resets: no | "It indicates a field-driven irreversible charge exchange between the 2DEG and the embedding lattice near the interface" (p. 3, Supp. Fig. 3a) | From a fresh cooldown, sweep to growing negative Vg and record Tc each time, then warm at Vg = 0 and log Rs(T) for release steps; comparing the Hall change in n with C·ΔVg/e from your ε shows how much memory is left for a polarization term. |
| Tc set by the gate-tuned disorder level, read through mobility (not in library; Chen et al.) | Tested in part | Tc compared with Hall μ and n measured in the same states: part (gate cycles in Supp. Fig. 1; no Hall data for states L0 to L4 of Fig. 2i); Superconducting layer thickness tracked across states: no | "Despite these mobility and density enhancements, it is striking that illumination reduces Tc, apparently contradicting the expected trend." (p. 6) | Plot Tc against μ for every gate-cycled and illuminated state; Tc is highest where μ is lowest in Supp. Fig. 1, and light raises μ and lowers Tc in Fig. 2, so one curve would tie the Tc memory to the mobility memory. |
| Maxwell-Wagner relaxation from contacts or internal interfaces (not in library; Lunkenheimer et al.) | Not tested (data bear on it) | Different sample geometries or thicknesses: no; Different contact configurations: no; Equivalent-circuit analysis of the frequency response: no; Light-intensity dependence of the relaxation frequency: no | "By neglecting the stray resistance, capacitance, and inductance along the contact wirings, we have" (Methods, p. 10) | Fit the Fig. 3a, b spectra with an equivalent circuit that includes the 2DEG and contact resistances, measure a bare KTaO3(111) substrate, and repeat the loss scan after illumination to see whether Peak 2 moves. |

## Questions about devices and data

1. How many heterostructures did you measure, and how many showed the gate memory, the light erasure and the two loss peaks?
2. If some samples or cooldowns did not show them, why were they set aside?
3. Which ranges did you measure beyond the ones shown: gate voltages past ±50 V, other LED wavelengths or drive levels, and dielectric frequencies below 0.1 Hz?
4. What does the second-best sample or cooldown look like, for example its Tc trajectory under the cycles of Fig. 1e?
5. The 35 K and 95 K traces in Fig. 4a are noisier and larger than their neighbours, while those in Supp. Fig. 5a look like the curves next to them. Are they from the same run as the rest, and were these temperatures, and a few kelvin either side, repeated? Each maximum in Fig. 4b rests on one point.
6. From 0.1 to 4001 Hz, Peak 1 moves from about 29 K to 47 K and Peak 2 from about 89 K to 139 K (my reading of Fig. 3c). At what frequency should they be compared with the 35 K and 95 K features? Extending your Arrhenius lines to the τ of about 10^3 s in Fig. 4c would put them near 25 K and 75 K.
7. Fig. 2b shows LED heating at 2 K. What is the sample temperature during illumination at 10 K, does a warming excursion of that size in the dark lower Tc the same way, and does the erased state of Fig. 2i return to the pre-gating Tc?
8. For the gate current in Supp. Fig. 3a, what was the sweep rate, how much is displacement current from your measured ε and how much is leakage, and how does the integrated charge compare with the Hall change in n?

## Related work

- Zhang et al. 2025, "Universally enhanced superconductivity and coexisting ferroelectricity at oxide interfaces", <https://arxiv.org/abs/2506.16298>. Gating and poling raise Tc at LaAlO3/KTaO3 by 0.2 to 0.6 K with hysteresis, attributed to switchable ferroelectric polarization.
- Biscaras et al. 2012, "Irreversibility and time relaxation in electrostatic doping of oxide interfaces", <https://arxiv.org/abs/1206.1198>. At SrTiO3 interfaces electrons escape the well irreversibly above a filling threshold, giving gating hysteresis and slow relaxation; the original state returns only on warming.
- Chen et al. 2020, "Electric field control of disorder-tunable superconductivity and the emergence of quantum metal at an oxide interface", <https://arxiv.org/abs/2009.05896>. At LaAlO3/KTaO3(111) a back gate tunes Tc along a dome while the density barely changes and the mobility falls, read as gate control of disorder.
- Liu et al. 2022, "Tunable superconductivity at the oxide-insulator/KTaO3 interface and its origin", <https://arxiv.org/abs/2203.05867>. Tc at KTaO3(111) interfaces depends linearly on carrier density over nearly a decade.
- Lunkenheimer et al. 2002, "Materials with Colossal Dielectric Constant: Do They Exist?", <https://arxiv.org/abs/cond-mat/0201146>. Contact and interface layers give Maxwell-Wagner loss peaks that shift with temperature like thermally activated dipolar relaxation.

Happy to rerun this if you share the figure data or a second sample's measurements.
