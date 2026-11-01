# Lookalike check: Flux-tunable global and local superconductivity in a topological insulator nano-SQUID (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your main evidence is global (critical current and diode effect), which the library
covers only lightly, so I adapted a few entries and added one lookalike from outside the
library.

**The claim, as I read it.** In three BiSbTeSe2 nano-SQUIDs (devices A, B, C), you report
h/2e oscillations of Ic and a diode-effect sign reversal at half-integer flux (Figs. 1e, 3a,
S2a, S4), which you read as consistent with a flux-driven transition into a topological
regime, plus spectral jumps in local and nonlocal conductance that line up with them
(Figs. 1f-g, 3b-e, S2). You also report that zero-bias peaks appear at both ends in the
expected topological and trivial flux windows alike, including zero field (Figs. 3b-c, 4,
S3), so the local peaks do not track the global features.

## Checks a careful reader will look for

1. Unintended dots near the barrier : Not done. Your zero-field gate maps (Fig. 4a-b, S3a-b) are the data that would show dot resonances; the text doesn't look for them.
2. Wide ranges, including where the peak is absent : Partly. "we do not see a significant difference between the VG dependence of ZBPs in the expected topological or trivial regimes (Fig. 4d-e & g-h) even over a region of VG that includes the Dirac point (Fig. 4j-k)" (p. 5). Field angle and peak heights across the maps are not reported.
3. Both ends at the same settings : Partly. "We find that both regimes contain ZBPs on either end (see Fig. 4c,f,i,l) the majority of the time." (p. 5). Device A has one working probe.
4. Peak stable as junction transparency changes : Not done. There is no tunnel-barrier gate; the back gate tunes the whole wire.
5. Nonlocal gap closing and reopening : Partly. "the nonlocal conductance reveals features that align with the Ic oscillations, such as jumps at the boundaries where the phase transition is supposed to occur (see Fig. 3d-e)" (p. 4). These are jumps; a closing and reopening gap is not analysed.
6. Series resistance stated and raw data shown : Partly. "the known filter resistance was subtracted from the recorded data" (p. 6). The resistance values are not given.
7. Device and dataset counts : Partly. "the yield of functional tunnel junctions fabricated on top remains below 50%, making devices with two decent tunnel probes to be comparatively rare." (p. 5). Totals fabricated and measured are not given.
8. Full parameter ranges : Partly. "Note that, in this device A, the gating range was limited due to a leaky gate dielectric" (p. S3). Measured ranges beyond the figures are not stated.
9. Processing from raw data to figures : Partly. "The data that support the findings of this study are available at the online depository zenodo" (p. 7). The derivative and smoothing behind Fig. 4l are not described, and code is not mentioned.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Andreev states in an unintended dot (`abs-quantum-dot`) | Partly addressed | "the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5). The data bear on it; the paper doesn't discuss it. | Look in Fig. 4a-b and S3a-b for resonances above the gap and peaks that split and recross with VG. |
| Kondo resonance (`kondo-resonance`) | Not addressed | Not discussed. | Check whether zero-field peaks sit in alternating gate windows and split with Bx; add a temperature series of one peak. |
| Disorder-induced states (`disorder-induced-zbp`) | Partly addressed | "suggests that at least some of these ZBPs are driven by disorder effects" (p. 5). You raise it yourselves. | Say which peaks, if any, you see as outside this reading, and what in your data would separate them. |
| Crowded trivial subgap states (`crowded-trivial-subgap-states`) | Partly addressed | "both showing a large number of ZBPs at both ends" (p. 5). The data bear on it; the paper doesn't discuss subbands. | Estimate occupied surface subbands per VG from Table S1 and compare with the peak fractions in Fig. 4l. |
| Quasi-Majorana states (`quasi-majorana-smooth-confinement`) | Partly addressed | "If these ZBPs originated from Majorana bound states, we would expect a positive correlation" (p. 5). Done for B and C; device A's peak is one-ended. | For device A, compare the peak onset field with the Ic minimum in Fig. 1e at finer field steps. |
| Spin-orbit length pinning (`spin-orbit-length-pinning`) | Partly addressed | "is very stable over the examined gate-voltage range" (p. S3, Fig. S1). Three gate values only. | Add a finer VG sweep at fixed Bx inside the device A lobe. |
| Flux-tunable Andreev levels in the junction (`full-shell-flux-andreev`, adapted) | Partly addressed | "disorder effects frequently mimic topological signatures [11, 12]" (p. 1). Cited in the introduction; no test in the data. | Compare devices with different probe-to-junction spacing; Table S1 already spans L = 1.3 to 2.5 µm. |
| Weak antilocalization (`weak-antilocalization`) | Not addressed | Not discussed. | Track zero-field peak width with Bx and VG against the number of open subbands. |
| Accidental crossing at phase π (`transparent-junction-pi-crossing`, adapted) | Partly addressed | "even over a region of VG that includes the Dirac point (Fig. 4j-k)" (p. 5). The data bear on it; the paper doesn't discuss it. | Use RN(VG) in Fig. 4j as a transparency proxy and plot peak occurrence against it in each lobe. |
| State at one end only (`one-end-only`) | Partly addressed | "We find that both regimes contain ZBPs on either end (see Fig. 4c,f,i,l) the majority of the time." (p. 5). Not possible for device A. | State in the text that the device A peak is from one end; show GLL and GRR of B at matched settings near its onset. |
| Local-probe loophole (`local-probe-loophole`) | Partly addressed | "a conclusive demonstration will also require the development of advanced probes of Majorana physics" (p. 5). | Compare zero-bias nonlocal sign changes (Fig. S5) with C_LR at the same VG and Bx. |
| Trivial Andreev band in nonlocal (`trivial-andreev-band-gap-reopening`) | Partly addressed | "there are also nonlocal conductance jumps at Bx values that do not correspond to the Ic features" (p. 5). | Show nonlocal maps against Bx at several VG to see whether the jumps track flux lobes at each gate setting. |
| Vortex and screening diode (`diode-vortex-screening`, adapted) | Partly addressed | "Their strong dependence on the magnetic-field sweep direction points to a vortex dynamics and flux trapping origin within the Nb electrodes." (p. 4). Stated for conductance jumps. | Compare η(Bx) for up and down sweeps, and its response to a small added Bz. |
| Analysis choices behind a classifier (`protocol-parameter-sensitivity`, adapted to Fig. 4l) | Partly addressed | "we evaluated the end-to-end correlation using the relative signs of the third derivative of the current at zero bias" (p. 5). No threshold or smoothing stated. | Rerun Fig. 4l with varied bias window, smoothing and VG step, and with a "no correlation" threshold; release the code. |
| Selection among devices and settings (`fine-tuning-and-selection`) | Partly addressed | "although a zero-bias conductance peak was mostly absent in this device" (p. S4, device C). | Give totals: devices fabricated, measured, cooldowns, and one-probe devices besides A. |
| Diode in an ordinary two-arm interferometer (not in library; Souto et al., https://arxiv.org/abs/2205.04469) | Not addressed | Not discussed. | Fit Fig. 1e with a trivial SQUID of two skewed, unequal current-phase relations and say which features need TI surface states. |

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed the global features and the zero-bias peaks? The paper names A, B and C and says "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5), and that the global signatures appear "in all examined devices" (p. 4), without a total.
2. Why were the others set aside, for example devices with one working probe besides A?
3. Which ranges of Bx, field angle, VG and temperature did you measure beyond the ones shown, especially for device A, where the gate range was limited?
4. What does the second-best device or dataset look like? Device C (Figs. S2, S3) partly answers this; are there other cooldowns of A or B?
5. For Fig. 4l, which bias window, smoothing and VG step set the sign of the third derivative, and how do the fractions move if you change them or add a threshold?
6. Do the zero-field peaks in Fig. 4a-b come with resonances above the gap, splitting with Bx, or an alternation between gate windows, and how do they change with temperature?
7. Does η(Bx) in Figs. 1e and 3a change with the field sweep direction or with a small out-of-plane field, and how much of Fig. 2b would a trivial two-arm SQUID with skewed current-phase relations reproduce?
8. What filter and line resistance values did you subtract (p. 6, p. S2), and how large is the correction to GLL, GRR and the nonlocal terms?

## Related work

- Souto, Leijnse and Schrade 2022, "The Josephson diode effect in supercurrent interferometers", <https://arxiv.org/abs/2205.04469>. Theory: two-junction interferometers with skewed current-phase relations give a diode effect from flux alone, which vanishes at integer multiples of the half flux quantum.
- Ciaccia et al. 2023, "Gate Tunable Josephson Diode in Proximitized InAs Supercurrent Interferometers", <https://arxiv.org/abs/2304.00484>. Experiment: a trivial InAs SQUID with two junctions shows a gate-tunable diode efficiency up to about 30% at finite flux.
- Valentini et al. 2021, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", <https://arxiv.org/abs/2008.02348>. Robust zero-bias peaks from flux-tunable Andreev levels in a dot in the junction region.
- Hess, Legg, Loss and Klinovaja 2023, "Trivial Andreev band mimicking topological bulk gap reopening in the non-local conductance of long Rashba nanowires", <https://arxiv.org/abs/2210.03507>. A trivial Andreev band gives a reopening signature in nonlocal conductance alongside trivial end peaks.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a strong diode effect at fields near 1 Oe from vortex barriers and Meissner screening.

Happy to rerun this if you share the figure data or the code behind Fig. 4l.
