# Lookalike check: Flux-tunable global and local superconductivity in a topological insulator nano-SQUID (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library has entries for diode effects and nonlocal conductance but no ordered checks for them, so the checks below are the zero-bias-peak list and the practice list. The diode and nonlocal claims are covered in the table.

**The claim, as I read it.** Your global data are read as a flux-driven transition into a topological phase in three devices (A, B, C). Those data are the h/2e critical current oscillations and the diode sign reversals at half-integer flux (Figs. 1e, 3a, S2a, S4), together with jumps in local and nonlocal conductance at the same fluxes (Figs. 1f-g, 3b-e, S2). You read the zero-bias peaks with care. Device A's ZBP appears inside the predicted window (Fig. 1f-g, S1). Devices B and C show ZBPs at both ends in predicted topological and trivial windows, including zero field (Fig. 4, S3), and you attribute these at least in part to disorder.

## Checks a careful reader will look for

1. Look for unintended dots near the barrier and in the junction : Not done. No search for Coulomb resonances, split-and-recross peaks or even-odd patterns is reported.
2. Show the peak over wide gate, field and angle ranges, with heights : Partly. "we do not see a significant difference between the VG dependence of ZBPs in the expected topological or trivial regimes (Fig. 4d-e & g-h)" (p. 5). Field angle is not varied, and peak heights are not reported across ranges.
3. Measure both ends at the same settings : Partly. "Both ends show a rich spectrum of ABSs evolving with the field" (p. 4, Fig. 3b-c) for B and C. Device A has one probe.
4. Show the peak stays as junction transparency changes : Not done. The barrier is a fixed ALD layer, and no barrier gate is described.
5. Nonlocal bulk gap at the end-peak fields : Partly. "the nonlocal conductance reveals features that align with the Ic oscillations, such as jumps at the boundaries where the phase transition is supposed to occur (see Fig. 3d-e)" (p. 4). This covers B and C only.
6. Series resistance and raw data : Partly. "The line resistances required were determined from two-terminal resistance measurements of the cryostat lines." (SM p. 2). The values and the raw local spectra are not shown.
7. Report device counts : Partly. "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5). Totals are not given.
8. Report full ranges and why : Partly. "in this device A, the gating range was limited due to a leaky gate dielectric" (SM p. 3). The reasons for the fields in Fig. 4 and S3 are not given.
9. Processing from raw data to figures : Partly. "the known filter resistance was subtracted from the recorded data" (p. 6). Data are on Zenodo. The derivative and correlation steps are not described.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Trivial Andreev states in an unintended dot near the barrier | Tested in part | Dot signatures searched: no; both ends compared: part (B, C; A has one probe) | "We find that both regimes contain ZBPs on either end (see Fig. 4c,f,i,l) the majority of the time." (p. 5) | Look in the zero-field gate maps (Fig. 4a-b, S3a-b) and Fig. S1 for resonances above the gap and peaks that split and recross. |
| Quasi-Majorana states from smooth confinement | Tested in part | Nonlocal bulk signature: part (jumps at boundaries, the expected bulk signature here, in B and C); correlated zero modes at both ends: part (B, C) | "there are also nonlocal conductance jumps at Bx values that do not correspond to the Ic features, especially at large values of magnetic flux" (p. 5) | Plot the correlated-peak fraction of Fig. 4l against whether the nonlocal data jump at each window's boundary. |
| Disorder-induced subgap states | Tested in part | End-to-end correlation: part (B, C); bulk gap signature: part (B, C); gate sensitivity: all (Figs. S1, 4, S3) | "suggests that at least some of these ZBPs are driven by disorder effects" (p. 5) | From the Fig. 4 and S3 maps, report ZBP heights and the VG width each peak survives over, split by flux window. |
| Crowded trivial subgap states from many subbands | Tested in part | Field and gate range vs predicted range: all (Figs. 1f, 4l, S3l); subband model: part (clean model, L = 150 nm) | "there is no clear distinction between expected topological regions and trivial regions, with both showing a large number of ZBPs at both ends" (p. 5) | Run the Kwant model at device dimensions, or with disorder, and count zero-energy end states in even-flux windows. |
| Kondo resonance in a dot | Not tested (data bear on it) | Even-odd occupancy: no; temperature: no; Zeeman splitting: no | "Although the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5) | Check whether the zero-field ZBPs alternate between gate valleys and split at small Bx; add one temperature series. |
| Weak antilocalization | Not tested (data bear on it) | Pikulin et al. test: no; channel number or disorder: no | "even over a region of VG that includes the Dirac point (Fig. 4j-k)" (p. 5) | Compare ZBP height and width on the two sides of the Dirac point, where the number of surface channels changes. |
| Peak at one end only | Tested in part | Both ends at the same settings: part (B, C; A's ZBP is one-ended); nonlocal: part (B, C) | "In Fig. 1 we present the data from a first-generation device (device A) featuring a single functional tunnel contact." (p. 2) | Say near Fig. 1g that A's ZBP is one-ended, and show B's two-end data near A's Dirac-point gate voltage. |
| Trivial Andreev band mimicking a bulk transition | Tested in part | Trivial reference: part (even-flux windows of B, C); unused parameters varied: part (nonlocal vs VG, Fig. S5, field not stated) | "This likely indicates the complex interplay of effects local to the tunnel contacts, such as local phase instabilities, and global properties of the full device that impact the nonlocal conductance." (p. 5) | Add nonlocal Bx maps at two or three more VG and check that the boundary jumps stay fixed in flux. |
| Flux-tunable Andreev levels in the junction region (adapted) | Not tested (not mentioned) | Short and long junction regions compared: no | Not discussed. | Describe the TI segment under each probe, and compare ZBP rates across probes or devices with different segment lengths. |
| Accidental zero-energy crossing in a transparent junction | Tested in part | Density tuned through the crossing: all (Figs. S1, 4, S3) | "The phenomenology remains qualitatively identical for different chemical potentials, as tuned by the global back gate voltage" (p. 3) | Show odd-flux line cuts across VG to see whether the zero crossing opens into an anticrossing anywhere. |
| Local-probe loophole | Tested in part | Nonlocal measurement: part (B, C); overlap through a dot: no | "a conclusive demonstration will also require the development of advanced probes of Majorana physics" (p. 5) | Compare Fig. 4l with the fraction expected if the two ends were independent (the product of each end's ZBP rate). |
| Meissner and vortex-barrier diode in the Nb films | Tested in part | Plain Nb control: no; followed against field and width: all (A, B, C differ in cross-section) | "Ic exhibits strong oscillations with a periodicity corresponding to one flux quantum Φ0 = h/2e threading the effective cross-sectional area of the nanowire" (p. 2) | Bound the film's own diode with a Nb-only bridge on the same chip at the same Bx. |
| Trivial SQUID interference diode (not in library) | Tested in part | Diode followed as junction asymmetry is tuned: part (VG maps for B, C, Fig. S4); trivial two-junction model compared: no | "the reversal of the SDE exactly at half-integer flux quanta, all fit the expected theoretical global signatures of a ground-state phase experiencing a phase jump across the junction" (p. 2) | Fit Ic±(Φ) of device B with a trivial two-junction model (fitted harmonics and asymmetry), and show what it cannot reproduce. |
| Fine-tuning and selection | Tested in part | Devices measured and how many showed it: part; how shown data were chosen: no; second device: all (A, B, C) | "making devices with two decent tunnel probes to be comparatively rare" (p. 5) | Add a short table of every device: working probes, gate range, ZBP seen or not. |

Ciaccia et al. find for a trivial InAs SQUID that "for Φext/Φ0 = 0.5, which equals φext = π, η = 0 independent on any other parameters" (https://arxiv.org/abs/2304.00484, p. 6, Fig. 3). That is why the trivial interferometer row is in the table.

## Questions about devices and data

1. How many nano-SQUIDs did you fabricate and measure in total, how many showed the global signatures, and how many showed ZBPs? You write that the global signatures "are also observed in all examined devices" (p. 4); the number examined would help.
2. Why were the other devices set aside, for example devices with one working tunnel probe besides device A?
3. Which ranges of VG, Bx and field angle did you measure beyond the ones shown, and why were Bx = 0, 1 and 2 T (Fig. 4) and 0, 2.5 and 4 T (Fig. S3) chosen for the gate maps?
4. What does the second-best dataset look like, for example another cooldown of device B, or device A at gate voltages beyond the three in Fig. S1?
5. In the correlation analysis (Fig. 4c, f, i, l), what threshold separates "correlated" from "no correlation", was the data smoothed before taking third derivatives, and how do the fractions in Fig. 4l move with that threshold?
6. Do the zero-field ZBPs in Fig. 4a-b show dot or Kondo features, such as alternation between gate valleys, splitting at small Bx, or a temperature dependence?
7. Could a trivial two-junction SQUID model with your measured asymmetry reproduce the Ic and η curves of Figs. 1e and 3a, and which feature, if any, would it miss?
8. Which field-sweep direction do Figs. 1f, 3 and S2 show, and do the jumps at half-integer flux sit at the same fields in both directions?

## Related work

- Valentini et al. 2021, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", <https://arxiv.org/abs/2008.02348>. In a flux-threaded hybrid wire, Andreev levels in a junction dot give robust ZBPs that follow the flux.
- Hess, Legg, Loss and Klinovaja 2023, "Trivial Andreev band mimicking topological bulk gap reopening in the non-local conductance of long Rashba nanowires", <https://arxiv.org/abs/2210.03507>. A trivial Andreev band mimics a bulk reopening in nonlocal conductance, alongside trivial end ZBPs.
- Banerjee et al. 2023, "Local and Nonlocal Transport Spectroscopy in Planar Josephson Junctions", <https://arxiv.org/abs/2205.09419>. In a phase-biased InAs/Al junction, gap reopening was strongly correlated end to end and local ZBCPs were weakly correlated.
- Ciaccia et al. 2023, "Gate Tunable Josephson Diode in Proximitized InAs Supercurrent Interferometers", <https://arxiv.org/abs/2304.00484>. A SQUID of two trivial InAs junctions gives a gate-tunable diode up to about 30%, with η = 0 at half a flux quantum.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a diode effect from vortex barriers and Meissner screening at fields as small as 1 Oe.

Happy to rerun this if you share the figure data or the Zenodo record.
