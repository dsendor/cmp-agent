# Lookalike check: Flux-tunable global and local superconductivity in a topological insulator nano-SQUID (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Two notes on scope. Your paper reads the global signals as evidence of a flux-driven transition and itself sets the zero-bias peaks aside as Majorana evidence, so the zero-bias rows below are about device A's peak in Fig. 1f and about how to sort the peaks in B and C. The library has no checks list for diode or SQUID signals, so I walked the zero-bias and practice checks and added one lookalike from outside the library for the global signals.

**The claim, as I read it.** In three BiSbTeSe2 nano-SQUIDs (A in Fig. 1, B in Figs. 3 and 4, C in Figs. S2 to S4), h/2e oscillations of Ic and a diode efficiency that reverses at half-integer flux quanta show a ground-state phase jump of pi, which your model (Fig. 2) ties to entering a topological phase; local and nonlocal spectral jumps line up with it. Zero-bias peaks appear in both the predicted topological and trivial flux windows, including at zero field.

## Checks a careful reader will look for

1. Look for unintended quantum dots near the barrier and in the junction : Not done. The Bx = 0 gate maps in Fig. 4a-b and Fig. S3a-b could show them; the text doesn't discuss dots.
2. Show the peak over wide gate, field and field-angle ranges : Partly. "we do not see a significant difference between the VG dependence of ZBPs in the expected topological or trivial regimes (Fig. 4d-e & g-h) even over a region of VG that includes the Dirac point (Fig. 4j-k)" (p. 5). Wide ranges in B and C; four gate values for A (Fig. S1); no field-angle data.
3. Measure tunneling at both ends at the same settings : Partly. "we analysed the correlation of local states at opposite ends of the nanowire" (p. 5), for B and C; A has one working probe.
4. Show the peak stays as the junction transparency changes : Not done. The Al2O3 tunnel barrier is fixed and has no barrier gate.
5. Nonlocal conductance for a bulk gap that closes and reopens : Partly. "the nonlocal conductance reveals features that align with the Ic oscillations, such as jumps at the boundaries where the phase transition is supposed to occur (see Fig. 3d-e)" (p. 4), for B and C.
6. State the series resistance and show raw data : Partly. "the known filter resistance was subtracted from the recorded data" (p. 6); the value and the raw data aren't given.
7. Report devices measured and how many showed the effect : Partly. "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5); totals fabricated and measured aren't given.
8. Disclose full parameter ranges and why each was chosen : Partly. "in this device A, the gating range was limited due to a leaky gate dielectric" (Suppl. p. 3); ranges measured beyond the figures aren't stated.
9. Give processing steps with data and code : Partly. "available at the online depository zenodo with the identifier 10.5281/zenodo.21988906" (p. 7); Methods and Suppl. S1.C describe the corrections; no code or derivative settings for the correlation analysis.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Trivial SQUID interference diode (not in library; Ciaccia et al., https://arxiv.org/abs/2304.00484) | Tested in part | Diode tracked as junction asymmetry is gated: part (Fig. S4 maps eta against VG in B and C, without relating VG to top-bottom asymmetry); trivial two-junction SQUID model compared: no | "all fit the expected theoretical global signatures of a ground-state phase experiencing a phase jump across the junction, which theoretically corresponds to the transition from trivial to topological superconductivity" (p. 2) | Fit Ic and eta versus flux with a trivial two-junction model from your measured Ic, RN and transparency, and say which feature it can't reproduce. |
| Vortex and Meissner screening diode in the Nb | Tested in part | Plain Nb control: no; effect against field and width: all | "the device in Fig. 3a (device B), which has an approximately 70% larger cross-section than the device in Fig. 1, exhibits multiple Ic oscillations and corresponding changes in the SDE" (p. 4) | Show eta at fine field steps near zero field, and on any plain Nb strip on the same chip. |
| Trivial Andreev band mimicking a bulk transition in nonlocal conductance | Not tested (data bear on it) | Trivial model of the nonlocal signal: no; other gates or field direction: no | "showing that some features correspond to the boundaries of the expected topological regimes" (Fig. 3 caption) | Follow the boundary jumps of Fig. 3d-e against VG and in both sweep directions. |
| Fine-tuning and selection | Tested in part | Counts: part; how data were chosen: no; second device: all | "are also observed in all examined devices and are largely robust against gate voltage" (p. 4) | State the totals and how the gate values in Figs. 1f, 3 and 4 were picked. |
| Disorder-induced zero-bias peaks | Tested in part | End-to-end correlation: part; nonlocal reopening: part; gate dependence: all | "suggests that at least some of these ZBPs are driven by disorder effects" (p. 5) | Add disorder to the Fig. 2c model and compare its zero-bias statistics with Fig. 4l. |
| Crowded trivial subgap states | Tested in part | Peak range against predicted windows: all; subband model: part (Fig. 2c is a clean model) | "there is no clear distinction between expected topological regions and trivial regions, with both showing a large number of ZBPs at both ends" (p. 5) | Include several surface subbands in the model and compare peak fractions per window with Fig. 4l and Fig. S3l. |
| Andreev states in an unintended quantum dot | Tested in part | Dot signatures: no; both ends: part | "Although the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5) | Look for diamonds and split-and-recross patterns in Fig. 4a-b and Fig. S3a-b at higher bias. |
| Accidental zero crossing at phase pi in a transparent junction | Tested in part | Density tuned through the crossing: all | "the abrupt appearance of the zero-bias conductance anomaly at half-flux quantum, is very stable over the examined gate-voltage range" (Suppl. p. 3) | Compare the odd-window zero-bias state across the Dirac point in B and C, where the gate range is wider. |
| Quasi-Majorana states from smooth confinement | Tested in part | Nonlocal reopening: part; correlated ends: part | "both regimes contain ZBPs on either end (see Fig. 4c,f,i,l) the majority of the time" (p. 5) | Mark where correlated peaks first appear in Bx relative to the nonlocal jumps. |
| One-end-only state | Tested in part | Both ends compared: part; nonlocal: part | "the boundary modes should be localised at the junctions without significant overlap in our devices" (p. 5) | For device A, say whether the second probe was measured at all. |
| Local-probe loophole | Tested in part | Nonlocal: part; overlap through a dot: no | "we estimate the experimental localisation length of the MBSs to be a few 100 nm, which is shorter than the 1.3 − 2.5µm length of our devices" (p. 5) | Use zero-bias GLR in the odd windows to bound end-to-end coupling. |
| Flux-tunable Andreev levels near the probe (adapted) | Not tested (not mentioned) | Probe regions of different size compared: no | Not discussed. | Compare probes whose uncovered TI segment differs in length. |
| Kondo resonance | Not tested (data bear on it) | Even-odd: no; temperature: no; Zeeman: no | "we observe these even in theoretically trivial windows and notably even at zero Bx" (p. 5) | Check zero-field peaks in Fig. 4a-b for alternation across resonances; take one temperature series. |
| Weak antilocalization | Not tested (not mentioned) | Pikulin test: no; channel number: no | Not discussed. | Compare peak heights and widths across the three cross-sections. |

## Questions about devices and data

1. How many nano-SQUID devices did you fabricate and cool down, and how many had working junctions with one or two working tunnel probes? You give the tunnel-probe yield as below 50% and show devices A, B and C; the totals would help.
2. Why were the others set aside? In particular, did any device with working junctions fail to show the Ic oscillations or the diode reversal (p. 4 says "all examined devices")?
3. Which ranges of field, field angle, back-gate voltage and temperature did you measure beyond the ones shown, and were the Bx sweeps in Figs. 1e, 3 and S2 also taken in the opposite sweep direction?
4. What does the second-best device or dataset look like: are there other single-probe devices like A, and did any show the abrupt zero-bias onset at half a flux quantum that Fig. 1f shows?
5. Could you compare Ic and eta versus flux, including how abrupt the reversal at Phi0(n + 1/2) is, with a trivial two-junction SQUID model built from your measured junction parameters, and say which feature of the global data that model could not produce?
6. Methods give tunnel-contact resistances "exceeding 100 kOhm", while the above-gap conductance in Fig. 1g and Fig. S2b is about 1 to 1.7 e^2/h (roughly 15 to 25 kOhm). What was each probe's resistance, and what filter resistance did you subtract, and how was it calibrated?
7. For the end-to-end correlation (Figs. 4c, f, i, l and S3), what threshold separates "correlated" from "no correlation", what bias step and smoothing go into the derivative, and how does Fig. 4l change when you vary them?
8. The Bx = 0 gate maps in Fig. 4a-b show resonances that cross zero bias. Did you look for Coulomb diamonds or even-odd patterns there, and at which field was Fig. S5 taken (its bias axes read in microvolts)?

## Related work

- Ciaccia et al. 2023, "Gate Tunable Josephson Diode in Proximitized InAs Supercurrent Interferometers", <https://arxiv.org/abs/2304.00484>. A SQUID of two trivial InAs junctions reaches about 30% diode efficiency, gate-tuned through the junction asymmetry, with eta = 0 at half a flux quantum whatever the other parameters.
- Souto, Leijnse and Schrade 2022, "The Josephson diode effect in supercurrent interferometers", <https://arxiv.org/abs/2205.04469>. Theory: interferometers of junctions with non-sinusoidal current-phase relations become diodes with only a flux, up to about 40% efficiency.
- Banerjee et al. 2022, "Local and Nonlocal Transport Spectroscopy in Planar Josephson Junctions", <https://arxiv.org/abs/2205.09419>. In a phase-biased planar junction with probes at both ends, gap reopening was strongly correlated end to end while local zero-bias peaks were weakly correlated.
- Hess, Legg, Loss and Klinovaja 2022, "Trivial Andreev band mimicking topological bulk gap reopening in the non-local conductance of long Rashba nanowires", <https://arxiv.org/abs/2210.03507>. A trivial bulk Andreev band can produce a reopening signature in nonlocal conductance alongside trivial end peaks.
- Pan and Das Sarma 2019, "Physical mechanisms for zero-bias conductance peaks in Majorana nanowires", <https://arxiv.org/abs/1910.11413>. Strong disorder generically gives trivial zero-bias peaks, and end-to-end correlation has limits in short wires.

Happy to rerun this if you share the figure data or the derivative settings behind Fig. 4l.
