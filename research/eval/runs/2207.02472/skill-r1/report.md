# Lookalike check: InAs-Al hybrid devices passing the topological gap protocol (arXiv 2207.02472v4)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v4, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library's ordered checks are modeled on your protocol's stages, so several are done by design.

**The claim, as I read it.** Devices A to D pass the topological gap protocol (TGP; Figs. 11 to 19, Table III): cutter-stable zero-bias peaks at both ends, inside a B-Vp region whose boundary shows a bulk gap closing in the antisymmetrized non-local conductance, with maximum gaps of 17 to 61 µeV. Device A passes in three measurements over two cooldowns; simulations (Table II) put the false discovery rate below about 8%.

## Checks a careful reader will look for

1. Look for unintended quantum dots near the barrier and in the junction : Partly. "sub-gap states may appear in the local spectroscopy, which we interpret as localized bound states at the junction" (p. 50); no dot search is shown.
2. Show the peak over wide gate, field and field-angle ranges : Partly. "We focus our Stage 1 scans on a Vp range of 30 mV above this value." (p. 16, Fig. 10); field angle is described without data (p. 19).
3. Measure tunneling at both ends at the same settings : Done. "In SOI2 , there are ZBPs exhibiting this type of stability at both junctions." (p. 22).
4. Show the peak stays as the junction transparency changes : Done. "the ZBPs remain stable with respect to these perturbations" (p. 22, Fig. 15).
5. Measure non-local conductance for a gap that closes and reopens : Done. "There is a clear bulk transport gap closing and re-opening visible in A(GRL ) at B ≈ 1.5 T." (p. 17, Fig. 11).
6. State the series resistance, its calibration, and the raw data : Partly. Lead resistances "are extracted independently from the linear I-V response in DC measurements" (p. 49); values sit in Ref. 98, and the 1-6% bias corrections are not applied (p. 50).
7. Report devices measured, how many showed the effect, and why others were set aside : Partly. "we report on data from two of them, which have been named devices E and F." (p. 3); the total is not given.
8. Disclose the full ranges measured and why each shown range was chosen : Partly. "makes it prudent to narrow the measured parameter range" (p. 13); ranges beyond the Stage 2 windows are not listed.
9. Give the processing steps, with data and code : Done. "The full source code of the TGP and raw data sets are available in Ref. 98." (p. 12).

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| One-end-only trivial state | Ruled out | "In SOI2 , there are ZBPs exhibiting this type of stability at both junctions." (p. 22) | None needed |
| Local-probe loophole | Ruled out | "Next, we use bias scans of the non-local conductances A(GRL ), A(GLR ) to determine the bulk transport gap at each point in the phase diagram." (p. 17) | None needed |
| Quasi-Majorana states from smooth confinement | Ruled out | "Quasi-MZMs do not appear after a gap closing/re-opening." (p. 31); the SOI2 requires a gapped interior. | None needed |
| Spin-orbit length pinning | Ruled out | "They are similarly stable with respect to changes in Vp" (p. 22, Fig. 14), and to cutters (Fig. 15). | None needed |
| Andreev states in an unintended junction dot | Partly addressed | "we observe that all of our devices have trivial ZBPs, even the ones that pass the TGP." (p. 30); no dot search shown. | Scan the cutters toward pinch-off at B = 0 and in field for Coulomb resonances; show finite-bias Stage 2 maps for levels that cross zero. |
| Kondo resonance | Partly addressed | At B = 0, "the zero-bias conductance was comparable to the noise floor" (p. 50); the data bear on it; the paper doesn't discuss it. | Show B = 0 local spectra at each SOI2's cutter and Vp settings. |
| Disorder-induced zero-bias peaks | Partly addressed | "However, this scenario does not entail a gap closing and re-opening in the non-local signal, from which we conclude that it does not apply to devices A, B, C, and D." (p. 31) | Vary gates the protocol leaves fixed (outer plungers, helper gates) inside each SOI2. |
| Crowded trivial subgap states | Partly addressed | "Often, they occur at only one junction, but they sometimes occur at both junctions" (p. 30) | Report how often ZBPs occur across every Stage 1 map, per device. |
| Weak antilocalization peak | Partly addressed | "Note that the ZBP height is of the order of e2 /h for all left cutter gate settings." (Fig. 15, p. 23); the data bear on it; the paper doesn't discuss it. | Track the peak as the junction opens past e²/h. |
| Exceptional-point zero mode | Partly addressed | "simultaneous zero-bias conductance peaks at both ends of the devices that withstand changes in the junction transparencies" (p. 1); the data bear on it; the paper doesn't discuss it. | Estimate the overlap of the two end states from the non-local data. |
| Trivial Andreev band mimicking gap reopening | Partly addressed | "Of course, we cannot rule this out completely." (p. 31); the bound rests on simulations. | Run the released code on simulated trivial wires built to mimic reopening; vary field angle and outer gates inside each SOI2. |
| Protocol outcome set by data choices | Partly addressed | "When we restrict the magnetic field to B ⩽ 2.5 T, we find one false positive for an SLG-β device" (p. 41, simulations). | Rerun the code on each measured dataset with field, bias and Vp windows, resolution and cutter subsets varied. |
| Fine-tuning and selection | Partly addressed | "It regularly passed the TGP, but also failed sometimes." (p. 22) | Give run and device counts, pass and fail, and show a failing run. |
| Circuit voltage-divider effects in three-terminal data (not in library) | Ruled out | "GLR and GRL may receive contributions from line impedances in the measurement circuit, which we account for by taking the full impedance network into account [156]." (p. 38) | None needed |

## Questions about devices and data

1. How many devices did you measure with the TGP, and how many passed? You show six, four passing, and write "Indeed, we have measured devices in which we were not able to find a topological phase" (pp. 22 to 23).
2. Why were the others set aside? How many did the pinch-off health check (p. 12) or the n2D,int specification remove, and why were E and F the failing devices shown?
3. Which ranges did you measure beyond the ones shown: Vp outside the 30 mV Stage 1 window, Vp below −1.1580 V for device B (p. 25), fields above 2.5 T, and field angles off the wire axis (p. 19)?
4. What does the second-best device or dataset look like? Device A "regularly passed the TGP, but also failed sometimes" (p. 22): how many Stage 2 runs did each device get, and could you show a failing one?
5. Gth is set from the maximum non-local conductance found "scanning over all B for each Vp" (p. 39), and in simulation restricting the field to B ⩽ 2.5 T changed one outcome (p. 41). Could you rerun the released code on each measured dataset with the field, bias and Vp windows, resolution and cutter subsets varied, and report what changes?
6. Did you scan the cutters past the 0.1 to 1 e²/h window toward pinch-off, at zero and finite field, for Coulomb resonances of a junction dot, and do the SOI2 peaks survive changes of the outer plungers or helper gates?
7. Has the TGP been run on simulated trivial wires built to mimic a gap closing and reopening (smooth potentials, a bulk Andreev band), and did simulations and measurements use the same code version?

## Related work

- Pikulin et al. 2021, "Protocol to identify a topological superconducting phase in a three-terminal device", <https://arxiv.org/abs/2103.12217>. Defines the protocol and tests it on simulated data, including screening of false positives.
- Pan, Sau and Das Sarma 2021, "Three-terminal nonlocal conductance in Majorana nanowires: Distinguishing topological and trivial in realistic systems with disorder and inhomogeneous potential", <https://arxiv.org/abs/2009.11809>. Finds the non-local signal too weak to be decisive with disorder and inhomogeneous potential.
- Puglia et al. 2021, "Closing of the Induced Gap in a Hybrid Superconductor-Semiconductor Nanowire", <https://arxiv.org/abs/2006.01275>. Non-local conductance shows the gap closing before zero-bias peaks appear, then fluctuating signals and uncorrelated peaks.
- Pöschl et al. 2022, "Nonlocal conductance spectroscopy of Andreev bound states in gate-defined InAs/Al nanowires", <https://arxiv.org/abs/2204.02430>. In the same kind of gate-defined InAs/Al wire, Andreev bound states oscillate around zero energy with gate voltage.
- Martinez et al. 2021, "Measurement circuit effects in three-terminal electrical transport measurements", <https://arxiv.org/abs/2104.02671>. Gives exact corrections for voltage-divider effects from line impedances in three-terminal conductance.

Happy to rerun this on the released datasets if you point me to the files for each figure.
