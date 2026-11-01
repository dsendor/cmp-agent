# Lookalike check: Flux-induced Majorana modes in full-shell nanowires (arXiv 1809.05513v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** In a full-shell InAs/Al nanowire in the destructive Little-Parks regime, tunneling into the core shows a hard gap in the zeroth lobe and a discrete zero-bias peak throughout the first lobe (device 1, Fig. 2, Figs. S2, S3, S9). Six full-shell Coulomb islands, 210 nm to 970 nm long on a single wire, show even-odd peak spacing in the first lobe that falls exponentially with length, with ξ = 180 nm (device 2, Figs. 3, 4, S4 to S9, Table S1). You read both as Majorana modes at the wire ends.

## Checks a careful reader will look for

1. Look for unintended quantum dots near the barrier and in the junction : Partly. Your Fig. 2C and 2E show back-gate maps at 0 and 110 mT, and you note "The resonance at VBG ∼ −1.2 V is likely due to a resonance in the barrier" (p. 3); no dot analysis of the bare segment is shown.
2. Show the peak over wide gate, field and field-angle ranges, including where it is absent : Partly. The field range covers every lobe: "The second lobe closes at 250 mT, above which only normal-state behavior was observed" (p. 3). The back gate spans 0.4 V, and the field was only axial: "Magnetic field was applied parallel to the nanowire using three-axis vector magnet" (p. 2).
3. Measure tunneling at both ends of the wire at the same settings : Not done. Device 1 has one tunneling probe (Fig. 2A).
4. Show the peak stays as the junction transparency changes : Done. "In the first lobe, at B = 110 mT, the sweep of VBG showed a zero-energy state throughout the tunneling regime (Fig. 2E)" (p. 3), with the evolution into the open regime in Fig. S3B.
5. Measure nonlocal conductance for a bulk gap that closes and reopens : Not done. The gap closing you show is local and belongs to the shell's destructive regime: "the superconducting gap in the core closed at |B| = 55 mT and reopened at 65 mT, separated by a gapless destructive regime" (p. 3).
6. State the series resistance subtracted and show raw data : Partly. The line resistance is given, "adding a line resistance RLine = 6.7 kΩ" (p. 7). The paper doesn't say whether it was subtracted, and no raw data are shown.
7. Report devices and datasets measured, how many showed the effect, and why others were set aside : Partly. "Two device geometries, measured in three devices each, showed similar results. Data from two devices are presented" (p. 2).
8. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. The field ranges are full, but the island data come from "several different gate configurations for each island" (p. 9), with no count or reason given.
9. Give the processing steps from raw data to figures, with data and code : Partly. The lever-arm conversion is described, "using the slopes of the Coulomb diamonds [8, 52]" (p. 4), and Table S1 lists η and A. No data or code are linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Flux-tunable Andreev levels in a dot in the junction (full-shell) | Not tested (data bear on it) | Short and long junction regions compared: no | "The Al shell was removed at the end of the wire and the tunnel barrier was controlled by the global back-gate" (p. 3); the bare segment where such a dot would sit is not characterized. | Compare the three tunneling devices if their bare-segment lengths differ, and scan VBG wider for dot resonances above the gap. |
| Andreev bound states in an unintended dot near the barrier | Tested in part | Dot signatures searched: part; both ends compared: no | "Several switches in data occurred at the same gate voltages in Fig. 2, C and E, presumably due to gate-dependent charge motion in the barrier" (p. 3) | Show finite-bias VBG maps over the full range at 110 mT and say whether any Coulomb diamonds appear. |
| Spin-orbit length resonance pinning an Andreev state | Tested in part | Pinning against parameters other than field: part (only the back gate, which also sets the barrier) | "the sweep of VBG showed a zero-energy state throughout the tunneling regime (Fig. 2E)" (p. 3) | Report the bare-segment length and compare devices where it differs. |
| Quasi-Majoranas from smooth confinement | Tested in part | Nonlocal gap closing and reopening: no; correlated zero modes at both ends: part (island length dependence on device 2, not the ends of device 1) | "the zero bias peak splits and eventually evolves into a zero-bias dip at strong coupling, in qualitative agreement with theory supporting MZMs [43]" (p. 3) | Give the dip depth in Fig. S3B in units of 2e^2/h, since a quantized dip is the open-regime test in your ref. [43]. |
| Disorder-induced subgap states | Tested in part | End-to-end correlation: part (islands only); bulk gap: no; insensitivity to gates: part (one gate) | "implying that the low-energy modes are located at the ends of the wire, not bound to impurities or local potential fluctuations" (p. 4) | Show how the island peak spacing responds to the side gates, and the spread of A across gate configurations. |
| Crowded trivial subgap states from several subbands | Tested in part | Field and gate range vs predicted topological range: part (field only); subband model: no | "the first lobes show zero-bias peak, the second lobes show non-zero subgap states" (Fig. 2B caption, p. 2) | Compare the VBG range of the peak with the range ref. [24]'s model predicts for this wire's density and subband filling. |
| State at one end only | Not tested (argued, not tested) | Both ends at same settings: no; nonlocal conductance: no | "implying that the low-energy modes are located at the ends of the wire" (p. 4), drawn from device 2 | Add a probe at the far end of a tunneling wire, or measure the ends of an existing device if contacts allow. |
| Local-probe loophole (overlapping components) | Tested in part | Nonlocal measurement: no; overlap estimated through a series dot: part (estimated through Coulomb islands) | "Within a Majorana picture, the energy scale A(L) reflects the length dependent hybridization energy of MZMs." (p. 4) | Same as the row above for the tunneling device. |
| Kondo resonance | Tested in part | Even-odd occupancy: no; temperature dependence: no; Zeeman splitting: part (field series shown, splitting not discussed) | "At zero field, a hard superconducting gap was observed throughout the zeroth superconducting lobe (Fig. 2, B and D)." (p. 3) | Show the temperature dependence of the first-lobe peak at 110 mT. |
| Exceptional-point zero mode | Not tested (data bear on it) | Overlap of the two components measured: no | Not discussed; Fig. S3B shows how the peak changes with lead coupling. | Read Fig. S3B for how the peak's position and width change with coupling. |
| Weak antilocalization | Not tested (data bear on it) | Pikulin et al. test: no; channel-number dependence: no | Not discussed; Fig. S3B tracks the peak as the junction opens. | Track the peak height and width against the above-gap conductance in Fig. S3B. |
| Confined island states giving even-odd spacing | Not tested (argued, not tested) | Tunneling spectroscopy on the same island with junctions opened: no | "The data are well described by an exponential length dependence, implying that the low-energy modes are located at the ends of the wire" (p. 4) | Open the side-gate barriers of one device 2 island at 110 mT and look for a zero-bias peak. |
| Fine-tuning and selection | Tested in part | Counts: part; how data were chosen: no; second dataset: part (six islands and a 140 mT set; one tunneling device) | "Two device geometries, measured in three devices each, showed similar results." (p. 2) | State, per device, whether it showed each signature, and show a second tunneling device. |

## Questions about devices and data

1. Your p. 2 says "Two device geometries, measured in three devices each, showed similar results." For each of the six devices, did the tunneling devices show the zero-bias peak in the first lobe, and did the island devices show the even-odd spacing that shrinks with length?
2. Why were the other four devices set aside, and how were device 1 and device 2 chosen for the paper?
3. Which ranges did you measure beyond the ones shown: back-gate voltage outside -1.2 V to -0.8 V in Fig. 2C and 2E, field angles away from the wire axis, and temperatures for the first-lobe zero-bias peak?
4. What does the second-best tunneling device look like in the first lobe, for example its version of Fig. 2B and 2E?
5. How long is the bare InAs segment between the tunnel barrier and the end of the Al shell in device 1, and did the other tunneling devices have different segment lengths?
6. Was the 6.7 kOhm line resistance (p. 7) subtracted from the conductance in Fig. 2 and Fig. S3, and how deep is the zero-bias dip in Fig. S3B in units of 2e^2/h?
7. Did you measure tunneling spectroscopy on any device 2 island with its side-gate barriers opened, at B = 110 mT?
8. For Fig. 4F and Table S1, how many gate configurations went into each island's value of A, how were they chosen, and how widely do the single-configuration values spread?

## Related work

- Albrecht et al. 2016, "Exponential Protection of Zero Modes in Majorana Islands", <https://arxiv.org/abs/1603.03217>. Coulomb-blockade spectroscopy of partially covered InAs/Al islands, where the even-odd splitting falls exponentially with wire length: the same signature as your Fig. 4F, in a different shell geometry.
- Chiu, Sau and Das Sarma 2017, "Conductance of a superconducting Coulomb blockaded Majorana nanowire", <https://arxiv.org/abs/1702.04357>. A theory of peak-spacing oscillations in hybrid islands, which reproduces the observed field trends only when ordinary Andreev bound states and several subbands are included.
- Liu, Sau, Stanescu and Das Sarma 2017, "Andreev bound states versus Majorana bound states in quantum dot-nanowire-superconductor hybrid structures", <https://arxiv.org/abs/1705.02035>. Shows that dot-induced Andreev states coalesce into near-zero-energy states, mostly in the trivial regime, which bears on a bare segment next to the barrier.
- Vuik, Nijholt, Akhmerov and Wimmer 2018, "Reproducing topological properties with quasi-Majorana states", <https://arxiv.org/abs/1806.02801>. Quasi-Majoranas from smooth confinement mimic most Majorana signatures, and a quantized conductance dip in the open regime separates true Majoranas.
- Chen et al. 2019, "Ubiquitous non-Majorana Zero-Bias Conductance Peaks in Nanowire Devices", <https://arxiv.org/abs/1902.02773>. Zero-bias peaks with pinning become common at finite field in InSb/NbTiN devices and trace back to crowded trivial subgap states.

Happy to rerun this if you share the figure data or the other four devices.
