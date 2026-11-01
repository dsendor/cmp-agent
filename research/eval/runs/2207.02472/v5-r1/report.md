# Lookalike check: InAs-Al Hybrid Devices Passing the Topological Gap Protocol (arXiv 2207.02472v4)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v4, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** Four gate-defined, 3 µm InAs-Al wires (devices A to D) pass the topological gap protocol: zero-bias peaks at both ends that survive changes of the cutter gates, inside a region of field and plunger voltage whose boundary shows a bulk gap closing in the antisymmetrized nonlocal conductance (Figs. 11, 13, 14 for device A; Figs. 16, 18, 19 for B, C, D), with maximum topological gaps of 17 to 61 µeV (Table III, p. 30).

## Checks a careful reader will look for

1. Search for unintended quantum dots : Partly. You follow one junction resonance in A2: "In addition to ZBPs, there is also a strong local resonance at the right junction which is evident in Fig. 13(d)." (p. 22). No junction charge-state scan is shown.
2. Wide gate, field and field-angle ranges : Partly. "We focus our Stage 1 scans on a Vp range of 30 mV above this value." (p. 16; Fig. 10, A1 only). Field angle is a sentence only (pp. 19, 22).
3. Both ends at the same settings : Done. "Find clusters of points in the B-Vp plane where there are stable ZBPs at both ends of the wire." (p. 14).
4. Stability to junction transparency : Done. "ZBPs that are stable with respect to changes of the cutter gate voltages is a mandatory requirement of the TGP." (p. 17; Figs. 15, 33, 34).
5. Nonlocal gap closing and reopening : Done. "There is a clear bulk transport gap closing and re-opening visible in A(GRL) at B ≈ 1.5 T." (p. 17).
6. Series resistance, calibration and raw data : Partly. Calibration parameters are in the repository (p. 49), and "the average magnitude of these corrections is 16% of the applied bias voltages" (p. 50), left unapplied.
7. Device and dataset counts : Partly. "We discard all devices in which one of the junctions cannot be completely closed at a pinch-off voltage > −3 V." (p. 12). Totals are not given.
8. Full ranges and why each was chosen : Partly. The Stage 1 window is explained (p. 13); "Stage 2 did not go to Vp lower than Vp = −1.1580 V" (p. 25). Ranges of failed runs are not given.
9. Processing steps, data and code : Done. "The full source code of the TGP and raw data sets are available in Ref. 98." (p. 12).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Andreev states in an unintended quantum dot | Tested in part | Dot signatures searched for in the same device: part (one resonance followed in A2 only); Zero-bias state compared at both ends: all | "However, as in the case of disorder-induced ZBPs, a trivial ABS need not be accompanied by a gap closing and re-opening in the non-local signal." (p. 31) | Show zero-field cutter and helper gate scans of each junction for Coulomb resonances above the gap, from data you already have. |
| Quasi-Majorana states from smooth confinement | Ruled out for the claim | Bulk gap closing and reopening in nonlocal conductance: all; Correlated zero modes at both ends: all | "By design, Stage 2 of the TGP weeds out stable ZBP clusters in which quasi-MZMs don’t evolve into true MZMs." (p. 31) | None needed |
| Disorder-induced subgap states | Ruled out for the claim | End-to-end correlation: all; Bulk gap closing and reopening: all; Insensitivity to gates that should not matter: all (cutter stability) | "However, this scenario does not entail a gap closing and re-opening in the non-local signal, from which we conclude that it does not apply to devices A, B, C, and D." (p. 31) | None needed |
| Crowded trivial subgap states | Ruled out for the claim | Field and gate range compared with the predicted topological range: all (Tables III and IV); Subband model of the device: all (Table I, Fig. 4) | "These are all trivial and fall outside the topological region because the observed bulk transport gap is zero." (p. 30) | None needed |
| Kondo resonance | Tested in part | Even-odd occupancy: no; Temperature dependence: no; Zeeman splitting in field: all (peaks at 1 to 2.5 T stay unsplit) | "In Fig. 14(c,d) one can see stable ZBPs at both junctions over a magnetic field range δB ≈ 0.5 T." (p. 22) | One sentence on the field range would cover it; zero-field junction gate scans would add the even-odd check. |
| Weak antilocalization | Tested in part | A distinguishing test from Pikulin et al.: no; Dependence on channel number or disorder: part (pass or fail listed against Hall-bar disorder; the peak itself is not followed) | "devices that have a narrow Al strip, zero-field induced gap to parent gap ratio in the required range, and weak disorder often pass the TGP while devices not meeting these requirements have never passed TGP, as expected from simulations." (p. 23) | Compare ZBP height and width across the cutter settings you already have, which change the open lead channels (Appendix H). |
| Peak at one end only | Ruled out for the claim | Both ends compared at the same settings: all; Nonlocal conductance: all | "A ZBP associated with an MZM must have a partner at the other end of the wire and should be stable to variations in the electric and magnetic fields in the device." (p. 2) | None needed |
| Trivial Andreev band mimicking a gap reopening | Tested in part | Protocol tested on trivial models or devices: part (349 disordered simulations; I can't tell whether any forms a bulk Andreev band); Parameters the protocol does not use varied: no | "Of course, we cannot rule this out completely." (p. 31) | Rotate the field or step the outer plungers through an SOI2; run the released code on a simulated wire with a trivial bulk Andreev band. |
| Protocol outcome set by data choices | Tested in part | Code and every dataset published: all; Reason given for each range and resolution: part (ranges explained, resolution not); Protocol rerun with ranges, resolution and gates varied: part (three cutter pairs for A1, Appendix F; field window varied in simulation only) | "When we restrict the magnetic field to B ⩽ 2.5 T, we find one false positive for an SLG-β device" (p. 41) | Rerun the released code on each measured dataset with field window, bias window, Vp step and cutter subset varied; Gth scales with the maximum over the field range (p. 39). |
| Local-probe loophole | Ruled out for the claim | Nonlocal measurement: all; Overlap estimated through a quantum dot in series: no | "This example once again reinforces the fact that local measurements alone cannot reliably detect a topological phase." (p. 44) | None needed (the entry names a nonlocal measurement as a control on its own) |
| Spin-orbit length pinning | Ruled out for the claim | Pinning tested against parameters other than field: all (cutters and Vp) | "Trivial ABS are not generically stable with respect to local perturbations whereas well-separated MZMs are." (p. 13) | None needed |
| Exceptional-point zero mode | Tested in part | Overlap of the two Majorana components measured: part (both-end correlation bounds it indirectly) | "ZBPs that occur at only one junction or for a small cutter gate fraction are likely to be due to trivial Andreev bound states." (Fig. 10, p. 17) | Report the ZBP splitting, or a bound on it, across each SOI2 as an overlap estimate. |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: all (A2, A3, B, C, D) | "It regularly passed the TGP, but also failed sometimes." (p. 22) | List every TGP run per device with its outcome, and show one failing run of device A. |

## Questions about devices and data

1. How many devices did you measure, and how many passed the TGP? Six are shown, and others are mentioned (pp. 22-23).
2. Why were the others set aside, beyond the pinch-off rule (p. 12)?
3. Which ranges did you measure beyond the ones shown, for example Stage 1 maps for devices B, C and D, and Vp below −1.1580 V for device B (p. 25)?
4. What does the second-best dataset look like, for example a run of device A that failed the TGP, and how many runs of each device passed?
5. Does each pass survive when you rerun the released code on the measured data with a narrower field window, a smaller bias window, coarser Vp steps, or another subset of cutter pairs?
6. What are the maximum topological gaps once the 16% bias correction (p. 50) is applied, and how much do nonlocal sign changes (p. 25) move them?
7. Do zero-field gate scans of the junctions show Coulomb resonances above the gap, and does the A2 right-junction resonance (Fig. 13(d)) recur in other runs?
8. Have you measured an SOI2 with the field rotated away from the wire, or with the outer plungers stepped, to see whether the gap closing follows?

## Related work

- Pikulin et al. 2021, "Protocol to identify a topological superconducting phase in a three-terminal device", <https://arxiv.org/abs/2103.12217>. Defines the protocol and tests it on simulated data.
- Puglia et al. 2020, "Closing of the Induced Gap in a Hybrid Superconductor-Semiconductor Nanowire", <https://arxiv.org/abs/2006.01275>. Nonlocal conductance shows the bulk gap closing before zero-bias peaks appear, then uncorrelated end peaks.
- Banerjee et al. 2022, "Signatures of a topological phase transition in a planar Josephson junction", <https://arxiv.org/abs/2201.03453>. Planar InAs/Al junctions show gap closing and reopening at both ends, while zero-bias peaks often differ between ends.
- Pan, Sau and Das Sarma 2020, "Three-terminal nonlocal conductance in Majorana nanowires: Distinguishing topological and trivial in realistic systems with disorder and inhomogeneous potential", <https://arxiv.org/abs/2009.11809>. Theory: with disorder, the nonlocal gap signal is too weak to be decisive.
- Pan and Das Sarma 2019, "Physical mechanisms for zero-bias conductance peaks in Majorana nanowires", <https://arxiv.org/abs/1910.11413>. Finds that strong disorder generically gives trivial zero-bias peaks in 1 and 3 µm wires.

Happy to rerun this if you share which runs of each device passed and which failed.
