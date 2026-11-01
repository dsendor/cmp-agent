# Lookalike check: Flux-tunable superconductivity in a TI nano-SQUID (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library has no ordered checks for diode or nonlocal signals, so I used its zero-bias-peak checks and its data-practice checks, and I added one lookalike for the diode signal that is not in the library.

**The claim, as I read it.** In devices A, B and C, Ic(Bx) oscillates with period h/2e, and the diode efficiency changes sign at half-integer flux (Fig. 1e, 3a, S2a, S4). You read this as a flux-driven global transition into topological superconductivity. Local and nonlocal tunnelling spectra jump at the same fields (Fig. 1f-g, 3b-e, S2b-e), and a ZBP appears at the transition in device A. In devices B and C, ZBPs appear in both the expected topological and the expected trivial regimes (Fig. 4, S3), which you report as a lack of correlation with the global signatures.

## Checks a careful reader will look for

1. Unintended dots near the barrier : Not done. I found no search for Coulomb resonances or even-odd patterns in the gate maps of Fig. 4a-h.
2. Wide gate, field and angle ranges, with peak heights : Partly. "we observe these even in theoretically trivial windows and notably even at zero Bx" (p. 5, Fig. 4). The paper reports gate and field ranges, but no field-angle series and no peak heights.
3. Both ends at the same settings : Partly. "simultaneously detected at both ends of the TINW" (p. 4, Fig. 3b-c). This covers B and C; device A has one probe.
4. Peak stability against barrier transparency : Not done. The ALD barrier is fixed and has no gate of its own.
5. Nonlocal gap closing and reopening : Partly. "jumps at the boundaries where the phase transition is supposed to occur" (p. 4, Fig. 3d-e). These are jumps, not a gap that closes and reopens, and the paper also reports "jumps at Bx values that do not correspond to the Ic features" (p. 5).
6. Series resistance stated and raw data shown : Partly. "the known filter resistance was subtracted from the recorded data" (p. 6). The values are not given and no raw maps are shown.
7. Device counts and why devices were set aside : Partly. "observed in all examined devices" (p. 4). The number of devices examined is not given.
8. Full ranges and why the shown ones were chosen : Partly. "the gating range was limited due to a leaky gate dielectric" (Suppl. p. 3). No reason is given for VG = 10 V in Fig. 1f.
9. Processing steps, data and code : Partly. Data are "available at the online depository zenodo" (p. 7), and Suppl. S1.C describes the circuit correction. The correlation code is not mentioned.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | counts: part; how chosen: no; second device: all | "observed in all examined devices" (p. 4) | Give device and cooldown counts, and say why VG = 10 V was chosen for Fig. 1f |
| Diode from vortex barriers and Meissner screening | Tested in part | plain Nb control: no; versus field and width: all | "the cross-section is larger than for device A and multiple oscillations of Ic are observed" (Fig. 3a) | Plot the η period against cross-section for A, B and C, and measure a plain Nb junction near zero field |
| Trivial SQUID diode from asymmetric junctions with skewed CPRs (not in library) | Tested in part | asymmetry tuned and η tracked: part; CPR harmonics: no | "it is also necessary to break inversion symmetry, which in the experiment is achieved through gating" (p. 6) | Use Fig. S4 to show how η near Φ0/2 follows the VG-tuned asymmetry, and fit Ic(Φ) with a two-junction model |
| Andreev states in an unintended dot | Tested in part | dot search: no; both ends: part | "Both ends show a rich spectrum of ABSs evolving with the field" (p. 4, Fig. 3b-c) | Look for Coulomb resonances above the gap in the Fig. 4a-h gate maps |
| Quasi-Majoranas from smooth confinement | Tested in part | nonlocal gap: part; correlated ends: part | "some features correspond to the boundaries of the expected topological regimes" (Fig. 3d-e) | Show where each end's ZBP first appears relative to the nonlocal jumps |
| Disorder-induced zero-bias peaks | Tested in part | end-to-end: part; nonlocal gap: part; gate sensitivity: all | "at least some of these ZBPs are driven by disorder effects" (p. 5) | Report ZBP heights and gate widths for each flux regime |
| Crowded trivial subgap states | Tested in part | range compared: all; subband model: part | "both showing a large number of ZBPs at both ends" (p. 5, Fig. 4l) | Model the subbands at the measured chemical potentials, and compare with Fig. 4l |
| Kondo resonance | Not tested (data bear on it) | even-odd: no; temperature: no; Zeeman: no | "the zero field ZBPs largely have a strong dependence on VG" (p. 5, Fig. 4a-b) | Check whether the zero-field ZBPs alternate between gate valleys, and take a temperature series |
| Weak antilocalization | Tested in part | Pikulin test: no; channel number: part (the VG sweep crosses the Dirac point but is not analysed by channel count) | "even over a region of VG that includes the Dirac point (Fig. 4j-k)" (p. 5) | Sort ZBP occurrence by surface subband count across the Dirac point |
| Peak at one end only | Tested in part | both ends: part; nonlocal: part | "we observe a jump in the spectrum and the appearance of a zero-bias peak (ZBP) within the predicted topological window" (p. 3, device A, one probe) | Show the Fig. 1f signature in a two-probe device |
| Local-probe loophole | Tested in part | nonlocal: part; dot overlap: no | "both regimes contain ZBPs on either end" (p. 5, Fig. 4c,f,i,l) | Compare the nonlocal magnitude at zero bias with each end's ZBP |
| Spin-orbit length pinning | Tested in part | non-field parameters: all | "very stable over the examined gate-voltage range" (Suppl. p. 3, Fig. S1) | Compare devices with different TI lengths beyond the tunnel probe |
| Exceptional-point zero mode | Not tested (data bear on it) | overlap: no | "we can measure the nonlocal conductance through the length of the nanowire" (p. 4) | Estimate the Majorana overlap from the nonlocal data in the odd lobe |
| Accidental crossing at phase π in a transparent junction | Tested in part | density tuned: all | "the abrupt appearance of the zero-bias conductance anomaly at half-flux quantum, is very stable" (Suppl. p. 3) | Report the junction transparency, for example from the excess current, at each VG |
| Trivial Andreev band mimicking a bulk transition | Tested in part | trivial model: no; other parameters: part | "the low-bias nonlocal conductance exhibits frequent sign changes as the gate voltage is varied" (Suppl. p. 6, Fig. S5) | Simulate nonlocal G for a trivial disordered wire under the same phase jump |

## Questions about devices and data

1. How many devices did you fabricate and measure, and in how many did you see the Ic oscillations, the diode sign reversal and the spectral jumps? Your text says the global signatures "are also observed in all examined devices" (p. 4); a number would help.
2. Why were the other devices set aside? You note that "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5); did devices with one or no working probe still show the global signatures, and are they in the Zenodo set?
3. Which ranges did you measure beyond the ones shown? For example, Fig. S4 maps device B over a wider gate range than the ±30 V of Fig. 4, and all data are at base temperature; were field angle or temperature series taken?
4. What does the second-best device look like for the device A result, where a ZBP appears at the half-flux jump (Fig. 1f-g)? Did any other device show a ZBP that appears at the transition and leaves at the next one?
5. For device C, Table S1 (16 nm by 80 nm) puts one flux quantum near 1.6 T, so 3Φ0/2 would sit near 2.4 T, yet Fig. S3d-e at Bx = 2.5 T is described as "within the expected first topological regime". Which flux period did you use for device C, and where does 2.5 T fall on it?
6. How does the end-to-end correlation in Fig. 4l and Fig. S3l treat small curvatures: is there a threshold on the size of the second derivative of G, and how were the gate points and bias resolution chosen? Relatedly, device C's ZBP "was mostly absent" in Fig. S2b-c while Fig. S3l reports "a strong increase of correlated zero-bias conductance peaks" in the first topological regime; which gate voltage is Fig. S2 taken at?
7. For the diode data, was the field swept in both directions, given that the high-field jumps show a "strong dependence on the magnetic-field sweep direction" (p. 4)? And does the size or sign of η around half a flux quantum track the top-bottom asymmetry you tune with VG (Fig. S4), as an ordinary two-junction interferometer diode would?
8. What were the filter and line resistances subtracted in the two-terminal dV/dI and in the nonlocal correction (Supplementary S1.C), and could you show one nonlocal map before correction?

## Related work

- Dartiailh et al. 2021, "Phase signature of topological transition in Josephson Junctions", <https://arxiv.org/abs/1906.01179>. Two gate-tunable Al/InAs junctions in a loop show a π-jump of the junction phase with in-plane field, together with a critical current minimum. This is a close analog of your global signature in a planar platform.
- Seoane Souto, Leijnse and Schrade 2022, "The Josephson diode effect in supercurrent interferometers", <https://arxiv.org/abs/2205.04469>. In theory, two junctions with non-sinusoidal current-phase relations in a loop give a diode effect from flux alone, with efficiency up to about 40%. The effect vanishes at integer multiples of half a flux quantum.
- Ciaccia et al. 2023, "Gate Tunable Josephson Diode in Proximitized InAs Supercurrent Interferometers", <https://arxiv.org/abs/2304.00484>. In experiment, a SQUID of two trivial InAs junctions gives a gate-tunable diode efficiency up to about 30%, whose sign mirrors about half a flux quantum when the junction asymmetry changes sign.
- Yu et al. 2021, "Non-Majorana states yield nearly quantized conductance in superconductor-semiconductor nanowire devices", <https://arxiv.org/abs/2004.08583>. Two-end tunnelling on InSb wires finds peaks at one end with dips at the other, and the paper sets out procedures for assessing end-to-end nonlocality.
- Valentini et al. 2021, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", <https://arxiv.org/abs/2008.02348>. Flux-tunable Andreev levels in dots in the junction region give robust ZBPs that look like Majorana modes but have no link to topology.

Happy to rerun this with the Zenodo data, which would let me count devices and gate ranges directly.
