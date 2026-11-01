# Lookalike check: Quantized Majorana conductance (arXiv 1710.10701v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** A zero-bias peak whose height stays at 2e^2/h (a plateau) as
field, tunnel-gate and super-gate voltages change, in InSb-Al nanowire device A (Figs. 1
to 3) and device B (Fig. 4), measured by one tunnel probe at one end of the wire, offered
as evidence of a Majorana zero mode. Device C (Fig. 5) is the trivial Andreev bound state
comparison.

## Checks a careful reader will look for

1. Look for unintended quantum dots near the barrier : Partly. "No localization effect (conductance resonances or quantum dot induced Coulomb blockade) is observed." (p. 22, Ext. Data Fig. 4b), for device C only.
2. Show the peak over wide gate, field and field-angle ranges, with heights everywhere : Partly. "Magnetic field direction is aligned with the nanowire axis for all measurements." (p. 12, Fig. 1); field and gate windows are shown, angle is not varied.
3. Measure tunneling at both ends at the same settings : Not done. "The right contact is used to drain the current to ground." (p. 3, Fig. 1a)
4. Show the peak stays as the junction transparency changes : Done, over the windows shown. "the above-gap conductance measured at |V| = 0.2 meV varies by more than 50%" (p. 5, Fig. 2c), and device B in Fig. 4b.
5. Nonlocal conductance for a bulk gap closing and reopening : Not done. "The gap re-opening is not visible in a measurement of the local density-of-states" (p. 4).
6. State the series resistance subtracted, its calibration, and the raw data : Not done. The paper doesn't mention series resistance.
7. Report devices and datasets, how many showed the effect, and why others were set aside : Partly. "only 2 devices (presented in the manuscript, Figs. 1,2,3 for device A and Fig.4 for device B) show a quantized ZBP-plateau" (p. 26, Ext. Data Fig. 7); cooldowns and datasets are not counted.
8. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Each figure's settings are stated, for example "Super- (tunnel-) gate voltage is fixed at -6.5 V (-7.7 V)" (p. 12, Fig. 1b); the ranges explored around them are not.
9. Give the processing steps from raw data to figures, with data and code : Not done. Only the Fig. 4e normalization (p. 15) and a background estimate (p. 7) are named; no data or code are linked.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Fine-tuned plateau from trivial states | Partly addressed | "from a rough estimate of this background contribution that the net ZBP-height (above background) never exceeds 2e2/h" (p. 7, Fig. 4b); how the plateau settings were found is not stated. | Show zero-bias height over the full tunnel-gate, super-gate and back-gate ranges you have for A and B, including regions above 2e^2/h, and say how the Fig. 1b settings were found. |
| Series resistance subtraction | Not addressed | Not discussed. | Report the subtracted resistance and its calibration, and show Figs. 2b and 4b before subtraction. |
| Andreev bound states in an unintended dot | Partly addressed | "The two different behaviours between back-gate and tunnel-gate are expected for ABSs that are localized near the tunnel barrier" (p. 9, Fig. 5); shown for device C only. | Show zero-field tunnel-gate and super-gate maps for A and B over wide bias, as in Ext. Data Fig. 4b, to look for dot resonances. |
| Quasi-Majorana from smooth confinement | Partly addressed | "ZBPs can also arise from local and non-topological Andreev bound states (ABS)16,31-34" (p. 8); ref. 31 is the smooth-confinement case, and the tunnel-gate test is argued for a dot near the barrier. | Run your Fig. 2f model with a smooth potential at the barrier end; in a new device, add a probe at the other end. |
| Disorder-induced subgap states | Partly addressed | "We have recently solved all these dissipation and disorder issues21" (p. 3); no device statistics on peak heights. | Show back-gate dependence for A and B (held at 0 V in Figs. 1 and 2) and peak heights across the 11 devices. |
| Crowded trivial subgap states | Partly addressed | "While most of these devices show ZBPs after tuning gate voltages and magnetic field, only 2 devices (presented in the manuscript, Figs. 1,2,3 for device A and Fig.4 for device B) show a quantized ZBP-plateau." (p. 26, Ext. Data Fig. 7); the data bear on it; the paper doesn't discuss it. | Compare where ZBPs appear in the 11 devices with the field and gate window your model predicts for the topological phase. |
| Kondo resonance | Partly addressed | "As B increases, two levels detach from the gap edge (at ~0.2 meV), merge at zero bias, and form a robust ZBP." (p. 3, Fig. 1b); the data bear on it; the paper doesn't discuss it. | Show zero-field data for A and B across the tunnel-gate range of Figs. 2a and 4b, to confirm no zero-bias peak at B = 0. |
| Weak antilocalization | Not addressed | Cited as ref. 33 (p. 8); not discussed. | Compare peaks in the single-channel (device A) and multi-channel (device B, Fig. 4b) regimes against the tests in Pikulin et al. |
| Spin-orbit length pinning | Partly addressed | "Fig. 3a shows a nearly-quantized ZBP that remains non-split over a large range in the super-gate voltage." (p. 6, Fig. 3a); the data bear on it; the paper doesn't discuss it. | Report the normal-segment length in A and B and show tunnel-gate sweeps at several fields. |
| Exceptional-point zero mode | Not addressed | Not discussed. | A second probe or a dot-assisted measurement in a new device, to estimate the overlap of the two Majorana components. |
| One end only | Not addressed | Not discussed; one probe per wire. | A device with tunnel probes at both ends, compared at the same field and gates. |
| Local-probe loophole | Partly addressed | "Only a stable quantized tunnel-conductance plateau, robust against variations in all gate voltages and magnetic field strength, can uniquely identify a topological Majorana zero-mode as far as tunnelling spectroscopy is concerned." (p. 9) | Nonlocal conductance or a second probe; until then, state the limit of a one-end measurement in the claim. |
| Fine-tuning and selection | Partly addressed | "We fabricated and tested many (>60) devices out of which we selected 11 devices" (p. 26, Ext. Data Fig. 7); the second-best dataset isn't shown. | Show the best data from the nine devices without a plateau, and count cooldowns and datasets per device. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the quantized plateau? Ext. Data Fig. 7 (p. 26) answers this (more than 60 fabricated, 11 measured, 2 with a plateau); how many cooldowns and datasets does that cover?
2. Why were the others set aside? Ext. Data Fig. 7 gives working gates and "good basic transport" as the criterion for the 11; did any of the others show zero-bias peaks?
3. Which ranges of field, field angle and the three gates did you measure beyond those in Figs. 1 to 4, and what does the zero-bias conductance do there?
4. What does the second-best device or dataset look like, for example the best of the nine devices without a plateau?
5. What series resistance, if any, did you subtract in Figs. 1 to 4, how was it calibrated, and what do Figs. 2b and 4b look like raw?
6. How did you find the gate settings of Figs. 1b and 2a, and do other settings in device A give peaks that level off above or below 2e^2/h?
7. For device B, how did you estimate the second-channel background, and what is the net peak height across Fig. 4b?
8. Did you look for dot resonances above the gap in devices A and B, as Ext. Data Fig. 4b does for device C?

## Related work

- Liu et al. 2017, "Andreev bound states versus Majorana bound states in quantum dot-nanowire-superconductor hybrid structures: Trivial versus topological zero-bias conductance peaks", <https://arxiv.org/abs/1705.02035>. Dot-induced Andreev states stick together near zero energy, mostly in the trivial regime, with tunneling signatures hard to tell from Majorana ones.
- Kells et al. 2012, "Near-zero-energy end states in topologically trivial spin-orbit coupled superconducting nanowires with a smooth confinement", <https://arxiv.org/abs/1207.3067>. A smooth confinement potential gives trivial end states with exponentially small energy, even in a clean single-channel wire.
- Yu et al. 2020, "Non-Majorana states yield nearly quantized conductance in superconductor-semiconductor nanowire devices", <https://arxiv.org/abs/2004.08583>. With probes at both ends of InSb wires, nearly quantized peaks appear at one end only, with dips at the other end.
- Wang et al. 2022, "Plateau regions for zero-bias peaks within 5% of the quantized conductance value $2e^2/h$", <https://arxiv.org/abs/2205.06736>. Plateaus near 2e^2/h over gate and field sweeps in an InAs-Al wire where disorder and quantum dots are present.
- Frolov et al. 2023, "\"Smoking gun\" signatures of topological milestones in trivial materials by measurement fine-tuning and data postselection", <https://arxiv.org/abs/2309.09368>. Trivial devices show near-2e^2/h plateaus, with similar plateaus above 2e^2/h in other regimes, attributed to fine-tuning and data selection.

Happy to rerun this if you share the figure data.
