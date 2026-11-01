# Lookalike check: Quantum Hall Antidot as a Fractional Coulombmeter (arXiv 2509.04209v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library is built mostly around superconducting hybrid devices, so I adapted its
fractional-charge entries to a quantum Hall antidot and added two rows from antidot papers
I opened.

**The claim, as I read it.** In the bilayer graphene antidot AD #2, the top-gate and field periods of Coulomb-dominated oscillations give a tunneling charge q/e close to 1/3 at ν = 4/3, 5/3 and 7/3 and for the small-period oscillation at ν = 8/3 (Fig. 4e, Fig. 3, Figs. S15 to S18). Integer fillings in AD #1 and AD #2 give q/e close to 1 (Fig. 2h, Fig. 4d-e), and ν = 2/3 and the large 8/3 oscillation give about 2e/3.

## Checks a careful reader will look for

1. Map the oscillations in the field and gate plane and say which regime they are in : Done. Every filling has a B-Vtg map, and "The oscillations exhibit a slope corresponding to the filling factor ν." (Fig. 5 caption, p. 7)
2. Show the effect is absent where the exotic state is not expected, and rule out charge traps and gate leakage : Partly. "As expected for the IQHE, filling factors ν = −2, 1, 2, 3, and 4 consistently fall around the q/e = 1 line, independently of the magnetic field at which they are measured." (p. 5, Fig. 4d); traps and leakage are not addressed.
3. Repeat sweeps to separate reproducible shifts from stochastic charge jumps : Partly. Several maps per fraction at other D and B (Figs. S13 to S16, S18); none at identical settings, and 7/3 has one map (Fig. S17).
4. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "For this part of the study, we fabricated a second device (AD #2) that showed a richer set of fractional quantum Hall states." (p. 4); totals fabricated and cooldowns are not given.
5. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Plateaus "typically extend over a limited range (∼ 200 mT and ∼ 50 mV)" (p. 15) and "Oscillations are consistently measured at the center of the fractional plateau, where Rxx = 0 and Gxy is constant." (p. 23)
6. Give the processing steps from raw data to figures, with data and code : Partly. The FFT windowing and error rules are in Sec. E (p. 15), and a current factor "is chosen such that the ν = 2 quantum Hall plateau is properly quantized" (p. 12); data are "available from the corresponding author upon reasonable request" (p. 10), with no code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Aharonov-Bohm or mixed regime read as Coulomb-dominated (library: coulomb-dominated-interferometer, adapted) | Tested in part | Field and gate map with stripe slope and spacing: all; Regime and charging parameters reported: part | "This behavior suggests a phase shift in the oscillation pattern, which is consistent with an Aharonov–Bohm–like mechanism rather than a purely Coulomb-dominated regime." (p. 23, Fig. S15) | Fourier-analyse the 4/3 maps (Fig. S15a-b) for an opposite-slope stripe family and give its amplitude; add a temperature series at one fraction. |
| Charge trap or side dot adding extra periods or jumps (library: charge-trap-fractional-shift, adapted) | Tested in part | Shifts absent where the exotic state is not expected: all; Gate leakage checked: no; Map of where in two-gate space the shifts occur: part | "However, since this occurs only in certain regions, we have decided to retain both points." (p. 4, small 8/3 oscillation) | Resweep the Fig. S18a window; follow the small-period stripes in bottom-gate sweeps; report leakage; mark the jumps in Figs. S11c and S17a. |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: part | "In these cases, the periodicity is estimated from the spacing between multiple consecutive peaks in the original conductance signal." (p. 15) | List every device, cooldown and fraction tried; show a second 7/3 dataset and the regions without the small 8/3 period. |
| Antidot area that changes with filling factor (not in library) | Tested in part | Area at each filling determined independently of the charge or N assignment: part; Integer and fractional gate periods compared in the same gate-voltage range: no | "confirming that the assumption of a nearly constant area across filling factors is reasonable." (p. 5, Fig. 4d-e) | Show the unrounded ratios 2ΔB2/ΔB with errors, and compare integer and fractional periods at the same gate voltages, as Hata et al. do. |
| Field period set by the number of charged edges (not in library) | Tested in part | Field period compared with the number of edges bound to the antidot at each filling: part; Gate-voltage and field periods combined to give charge and number of charged edges: all | "The edge-counting, in contrast, would only imply 2 edges for ν = 4/3, leading to an estimated AD diameter far larger than lithographic size between the two side gates (∼ 450 nm)." (p. 6) | Give the side-gate separation next to the N = 2 diameter at 4/3, and run the same argument at 5/3, 7/3 and 8/3. |

## Questions about devices and data

1. How many antidot devices did you fabricate and measure, and in how many did you resolve fractional oscillations? Your p. 4 introduces AD #2 as a device "that showed a richer set of fractional quantum Hall states"; were there others beyond AD #1 and AD #2?
2. Why were the other devices, cooldowns or fractional states set aside? For example, at which fractions did you look for oscillations without resolving them (p. 6 mentions the 2/5 derivative states and 11/3)?
3. Which field, gate and displacement-field ranges did you measure beyond the windows shown in Fig. 3 and Figs. S13 to S18, and how did you pick each window inside a plateau?
4. What does the second-best dataset look like at ν = 7/3, where Fig. S17 shows a single map, and which other maps at ν = 8/3 show the small-period oscillation?
5. N comes from the field-period ratio to ν = 2 under a constant area (Fig. 4b), and the diameters in Fig. 4c use those same N values. Could you show the unrounded ratios with errors, an area estimate that does not use N (for example integer and fractional periods taken in the same gate-voltage range), and, for the edge-counting reading at ν = 4/3, the side-gate separation next to the diameter N = 2 would imply, with the same argument for 5/3, 7/3 and 8/3?
6. At ν = 4/3 the bias data suggest "an Aharonov–Bohm–like mechanism" (p. 23). Do the 2D-FFTs at 4/3 show any stripe family with the opposite slope, and do you have a temperature series at any fractional filling?
7. Do the small-period stripes at ν = 8/3 (Fig. S18a) and the jumps visible in Figs. S11c and S17a repeat when you resweep the same window, do the small-period stripes appear in the bottom-gate sweeps of Fig. S9, and did you check gate leakage?
8. Could you confirm which device the fractional bottom-gate data in Fig. S9g-l come from (the p. 20 text says AD #1, the caption says AD #2), and which device the "many well-developed fractional Hall states at B = 8 T" on p. 3 refers to, given the p. 11 note on "the absence of fractional quantum Hall states at a field of B = 8 T"?

A note on why question 5 matters most. Your Eq. 2 (p. 7) gives q/e = ν/N, and Fig. 5 shows the slope tracks ν at every filling. Once the slope is fixed, the charge depends on N alone, which is your own point on p. 7: "This may lead to a misinterpretation of the calculated value, with it being ascribed to the tunneling quasiparticle charge rather than to the slope of the oscillations determined by the filling factor." Your independent cross-check, ΔV/ΔVe in Fig. 4d, also assumes the same area and gate coupling at every filling. A measurement of the area that does not depend on N would make the e/3 values at 4/3, 5/3 and 7/3 hard to question. The bottom-gate repeat in Fig. S10 is a good start, since it reaches the same charges with a different gate.

## Related work

- Kou, Marcus, Pfeiffer and West 2012, "Coulomb Oscillations in Antidots in the Integer and Fractional Quantum Hall Regimes", <https://arxiv.org/abs/1201.1600>. GaAs antidots where field and gate periods give a tunneling charge e with two charged edges at ν = 2, and (2/3)e with a single charged edge at ν = 2/3.
- Hata et al. 2024, "Coulomb oscillations of a quantum antidot formed by an airbridged pillar gate in the integer and fractional quantum Hall regime", <https://arxiv.org/abs/2412.11401>. Finds the antidot area at ν = 2/3 significantly smaller than at ν = 2 and 1, and an effective charge of about 2/3 at 2/3 when a constant gate capacitance is assumed.
- Mills, Averin and Du 2020, "Localizing fractional quasiparticles on graphene quantum hall antidots", <https://arxiv.org/abs/2010.11394>. Graphene antidots with quasiparticle charges of approximately ±e/3 measured at ν = ±1/3.
- Kataoka et al. 2000, "Coulomb blockade of tunnelling through compressible rings formed around an antidot: an explanation for h/2e Aharonov-Bohm oscillations", <https://arxiv.org/abs/cond-mat/0007383>. A charging model in which compressible rings around an antidot give resonances twice per h/e period.
- Halperin, Stern, Neder and Rosenow 2011, "Theory of the Fabry-Perot Quantum Hall Interferometer", <https://arxiv.org/abs/1010.4598>. Aharonov-Bohm and Coulomb-dominated regimes give stripes with different spacings and opposite slopes, and intermediate coupling superposes the two.

Happy to rerun this if you share the figure data.
