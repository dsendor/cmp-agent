# Lookalike check: Boundary-Bulk Interplay in Nonlinear Topological Transport (arXiv 2512.07017v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper measures second-harmonic transport in a magnetic topological insulator sandwich with no superconductor. The library's signal families are built around hybrid superconducting devices and don't cover this, so only the general data-selection entry applies as written. I added three ordinary second-harmonic mechanisms from the literature, each marked "(not in library)".

**The claim, as I read it.** In Sample S1 at 25 mK, the second-harmonic longitudinal voltages on the two sides of the Hall bar, V2ω_xx,L and V2ω_xx,R, have opposite signs. Their antisymmetric part V2ω_xx,A exceeds the electrode-independent part V2ω_xx,S, and V2ω_yx tracks V2ω_xx,R (Figs. 1e, 1f, 2, 3). You read this electrode dependence, together with its dependence on magnetic order and carrier type, as boundary modes dominating the nonlinear response. A C2z symmetry argument and nonlinear Landauer-Büttiker simulations support the reading (Fig. 4).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "Samples S1 to S4 are used in our electrical transport measurements, with Samples S1 and S2 measured in the dilution refrigerator and all samples measured in the PPMS." (p. 4). The paper doesn't say how many of the four show the effect, or why S1 leads.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. You show wide gate, field, temperature, frequency and current ranges ("over -200 V ≤ (Vg-Vg0) ≤ 200 V", p. 7; Extended Data Figs. 4 to 6). The reasons for the five field-sweep gate voltages in Fig. 2, and for 2 μA at 25 mK, go no further than the heating remark on p. 6.
3. Give the processing steps from raw data to figures, with data and code : Partly. "All magneto-transport results shown in this work are symmetrized or anti-symmetrized as a function of the magnetic field to eliminate the influence of the electrode misalignment." (p. 14). The data "are openly available" (p. 19, Zenodo). The paper doesn't say how the hysteretic branches are paired, which lock-in phase is used, or where the simulation code is.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: all | "This transport property shows reproducibility and consistency across multiple samples (Extended Data Figs. 9 and 10, and Figs. S3 and S4)." (p. 13); S2 appears in Extended Data Figs. 9 and 10 | State how many of S1 to S4 show the sign-reversed pair, and put S3 and S4 at the gate voltages of Fig. 2 into the PDF |
| Gate-voltage oscillation from the AC channel potential (not in library) | Tested in part | Source and drain ground swapped: part (one gate voltage, 1.7 K); Hall electrodes grounded one at a time: no; Gate oscillation applied on purpose: no | "we exclude the possibility that the second-harmonic voltages observed in our samples arise from gate oscillations" (p. 6); Extended Data Fig. 3 at (Vg-Vg0) = -5 V, T = 1.7 K | Repeat the ground swap at 25 mK at (Vg-Vg0) = -5 V and 10 V, and add the one-at-a-time Hall-electrode grounding of Xu et al. |
| Back-gate self-gating by the Hall and longitudinal voltages (not in library) | Not tested (argued, not tested) | Control device without a back gate: no; Second harmonic compared with the prediction from linear coefficients and gate capacitance: no | The same p. 6 sentence cites this work. A ground swap leaves the position-dependent density modulation in place, so Extended Data Fig. 3 doesn't separate it. | Compute the Iwakiri et al. model from your measured ρxx and ρyx versus Vg and H with the gate capacitance; measure the second Hall pair (3 and 5) |
| Joule-heating thermoelectric voltages at 2ω (not in library) | Not tested (argued, not tested) | Thermoelectric part separated by its symmetry and field dependence: no; Control where heating remains and the claimed mechanism is absent: no | "An AC current I = 2 μA is applied to enhance the signal-to-noise ratio and minimize heating effects and other higher-order contributions." (p. 6) | Estimate the temperature rise from ρxx versus current and versus temperature at 2 μA, and compare the 2ω field shape with the dissipated power times a Nernst-like term |

One note on the symmetry argument. Your p. 11 sentence says it "does not rely on the microscopic model". The same reasoning seems to apply to any voltage that is even in the current, including the gate and heating mechanisms above. A reader may ask what in the data separates them from boundary transport. That is why the three outside rows are here, and the checks in the right column use data you mostly already have.

## Questions about devices and data

1. You list Samples S1 to S4 (p. 4). How many Hall bars did you measure in all, and how many showed the opposite-sign second-harmonic voltages on the two sides?
2. Why does the main text use Sample S1, and why were S3 and S4 measured only in the PPMS?
3. Which ranges did you measure beyond the ones shown: currents other than 2 μA at 25 mK, field sweeps at gate voltages other than the five in Fig. 2, other cooldowns, and any tilted field?
4. What does the second-best device look like at 25 mK? S2 appears at two gate voltages and 1 μA (Extended Data Fig. 9); how do S3 and S4 compare at the gate voltages of Fig. 2?
5. How were the hysteretic second-harmonic sweeps antisymmetrized in field (which up and down branches were paired), which lock-in phase did you record, and could you show the raw left and right voltages behind Fig. 1e?
6. What is the capacitance per area of the SrTiO3 back gate at 25 mK, did you repeat the ground swap of Extended Data Fig. 3 at 25 mK and other gate voltages, and did you measure the second Hall pair (electrodes 3 and 5)?
7. What temperature rise do you estimate at 2 μA (25 mK) and at 5 μA (1.7 K)?
8. You describe the C2z symmetry of your Hall bars as approximate (p. 11). What are the resistances of the pressed indium contacts, and how symmetric are the scratched Hall bars in shape and contact placement?

## Related work

- Xu et al. 2024, "Second harmonic generation induced by gate voltage oscillation in few layer MnBi2Te4", <https://arxiv.org/abs/2401.00679>. In gated MnBi2Te4 devices, large second-harmonic signals come from gate voltage oscillation and reverse when the ground moves between source and drain. The paper also gives a grounding method that suppresses them.
- Iwakiri et al. 2023, "Nonlinear response of 2DEG in the quantum Hall regime", <https://arxiv.org/abs/2306.09907>. A back-gated GaAs 2DEG shows a voltage that goes as current squared next to the quantum Hall plateaus. It depends on field and contact configuration, and it is absent in a sample without a back gate.
- Avci et al. 2014, "Interplay of spin-orbit torque and thermoelectric effects in ferromagnet/normal metal bilayers", <https://arxiv.org/abs/1412.0865>. Joule-heating thermal gradients give second-harmonic transverse signals of comparable symmetry and magnitude to the effect under study, and the paper gives a method to separate them.
- Li et al. 2023, "Observation of giant nonreciprocal charge transport from quantum Hall states in a topological insulator", <https://arxiv.org/abs/2307.08917>. Nonreciprocal transport mediated by quantum Hall states in Sn-Bi1.1Sb0.9Te2S devices, a similar boundary-state signature.
- Wang et al. 2023, "Quantum metric-induced nonlinear transport in a topological antiferromagnet", <https://arxiv.org/abs/2306.09285>. Nonlinear Hall and nonreciprocal longitudinal responses in MnBi2Te4 reverse with antiferromagnetic order and with carrier type, and are assigned to the bulk quantum metric.

Happy to rerun this if you share the figure data or the Supplementary Information.
