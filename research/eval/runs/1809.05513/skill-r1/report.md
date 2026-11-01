# Lookalike check: Flux-induced Majorana modes in full-shell nanowires (arXiv 1809.05513v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** Tunneling into the core of device 1 shows a zero-bias peak
throughout the first Little-Parks lobe, a hard gap in the zeroth lobe and subgap states
away from zero in the second lobe (Fig. 2, Figs. S2, S3). In device 2, six full-shell
islands from 210 nm to 970 nm on one wire show even-odd Coulomb peak spacing in the first
lobe, and the even-odd energy falls exponentially with island length, with ξ = 180 nm
(Figs. 3, 4, S4 to S9, Table S1).

## Checks a careful reader will look for

1. Search for unintended dots near the barrier : Partly. "The resonance at VBG ∼ −1.2 V is likely due to a resonance in the barrier." (p. 3, Fig. 2C); the bare segment isn't examined as a dot.
2. Peak over wide gate, field and angle ranges, including where absent : Partly. "the first lobes show zero-bias peak, the second lobes show non-zero subgap states." (p. 2, Fig. 2 caption); one gate window, axial field only, no peak heights.
3. Tunneling at both ends at the same settings : Not done. Device 1 has one tunnel probe.
4. Peak stays as transparency changes : Partly. "the sweep of VBG showed a zero-energy state throughout the tunneling regime (Fig. 2E)." (p. 3); one global gate sets the barrier and the bare segment together.
5. Nonlocal conductance for a bulk gap closing and reopening : Not done. The closing at 55 mT and reopening at 65 mT (p. 3) is local and tracks the shell's destructive regime.
6. Series resistance and raw data : Partly. "adding a line resistance RLine = 6.7 kΩ" (p. 7); subtraction isn't stated, a small matter with no quantized value claimed.
7. Device and dataset counts : Partly. "Two device geometries, measured in three devices each, showed similar results." (p. 2); how many showed the peak isn't given.
8. Full parameter ranges and why each was chosen : Partly. "full data sets for other lengths reported in [44]" (p. 4); ranges beyond those shown aren't stated.
9. Processing from raw data to figures : Partly. "using separately measured level arms for each segment" (p. 4, Fig. 4F caption); no data or code are linked.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Andreev states in an unintended dot near the barrier | Partly addressed | "presumably due to gate-dependent charge motion in the barrier." (p. 3, Fig. 2C, E); the bare segment isn't discussed as a dot. | Report the bare segment length; show finite-bias scans over a wider VBG range at 0 and 110 mT for dot resonances. |
| Flux-tunable Andreev levels in a dot in the junction (full shell) | Not addressed | Not discussed; junction length isn't reported or varied. | Compare the tunneling devices you have by junction length, and whether each shows the first-lobe peak. |
| Quasi-Majorana states from smooth confinement | Partly addressed | "evolves into a zero-bias dip at strong coupling, in qualitative agreement with theory supporting MZMs [43]." (p. 3, Fig. S3B) | Give the dip value in units of 2e^2/h at strong coupling; a quantized dip is the distinguishing feature in Vuik et al. |
| Disorder-induced subgap states | Partly addressed | "not bound to impurities or local potential fluctuations" (p. 4, Fig. 4F); this comes from one island series. | Show the spread of A over the gate configurations per island, and the same series on a second wire. |
| Crowded trivial subgap states from many subbands | Partly addressed | "Note that Majorana zero modes are expected to appear only when the superconducting phase winding number is odd [12]." (p. 8, Fig. S2) | Report how often the first-lobe peak appears across devices and gate settings, against the subband occupancy your model predicts. |
| Kondo resonance | Partly addressed | "a narrow zero-bias conductance peak was observed throughout the first gapped lobe" (p. 3, Fig. 2B); the data bear on it; the paper doesn't discuss it. | Show the peak's temperature dependence and whether it splits in field across the lobe. |
| Andreev state pinned by the spin-orbit length of a normal segment | Partly addressed | "The Al shell was removed at the end of the wire" (p. 3); the data bear on it; the paper doesn't discuss it. | Report the bare segment length and compare devices with different lengths. |
| Exceptional-point zero mode from coupling to the lead | Partly addressed | "Hybridization of MZMs can be measured in Coulomb islands of finite length" (p. 3, Fig. 4); the data bear on it; the paper doesn't discuss it. | An overlap estimate on the tunneling wire itself, for example a second probe or an island cut from it. |
| Peak at one end only | Partly addressed | "implying that the low-energy modes are located at the ends of the wire" (p. 4, Fig. 4F); from islands, separate from the tunneling wire. | Tunnel into both ends of one wire, or into an island in its open regime. |
| Local-probe loophole | Partly addressed | "Hybridization of MZMs can be measured in Coulomb islands of finite length from the spacing of Coulomb blockade conductance peaks" (p. 3) | Combine both measurements on one wire, so the local peak and the island overlap come from the same device. |
| Confined island states giving even-odd spacing | Partly addressed | "featuring zero-bias peaks at the degeneracy points for each island." (p. 9, Figs. S4 to S8) | Open one island's junctions and show tunneling spectra in the first lobe on that same island. |
| Fine-tuning and selection | Partly addressed | "Data from two devices are presented" (p. 2); "several different gate configurations for each island" (p. 9) | State how many devices showed each signature and show the second-best tunneling device. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the first-lobe zero-bias peak or the even-odd length dependence? Page 2 says the six devices "showed similar results"; how many showed each signature, over how many cooldowns?
2. Why were the other four devices set aside?
3. Which ranges did you measure beyond the ones shown: back-gate voltage outside −1.2 V to −0.8 V at 110 mT, field angles (you had a three-axis magnet), and temperature for the zero-bias peak?
4. What do the second-best tunneling device and the second-best island series look like?
5. How long is the bare InAs segment between the barrier and the end of the shell in device 1, and do finite-bias scans of it show dot resonances at zero field?
6. At strong coupling in Fig. S3B, what is the zero-bias dip value in units of 2e^2/h, and was the 6.7 kΩ line resistance subtracted before plotting conductance?
7. For each island, how many gate configurations went into Table S1, how widely did A vary between them, and how was the plunger window for the averages in Fig. 4E chosen?
8. Did you tunnel into the other end of the device 1 wire, or into any device 2 island with its junctions opened?

## Related work

- Liu, Sau, Stanescu and Das Sarma 2017, "Andreev bound states versus Majorana bound states in quantum dot-nanowire-superconductor hybrid structures: Trivial versus topological zero-bias conductance peaks", <https://arxiv.org/abs/1705.02035>. Dot-induced Andreev states stick together near zero energy, mostly in the trivial regime, with Majorana-like tunneling signatures.
- Moore, Stanescu and Tewari 2018, "Two terminal charge tunneling: Disentangling Majorana zero modes from partially separated Andreev bound states in semiconductor-superconductor heterostructures", <https://arxiv.org/abs/1711.06256>. Partially separated Andreev states mimic local signatures; correlated two-end spectra separate them.
- Vuik, Nijholt, Akhmerov and Wimmer 2019, "Reproducing topological properties with quasi-Majorana states", <https://arxiv.org/abs/1806.02801>. Quasi-Majorana states mimic most Majorana signatures; a quantized conductance dip in the open regime distinguishes true Majorana states.
- Chiu, Sau and Das Sarma 2017, "Conductance of a superconducting Coulomb blockaded Majorana nanowire", <https://arxiv.org/abs/1702.04357>. Peak spacing oscillations in Coulomb-blockaded wires depend on temperature, multiple subbands and ordinary Andreev bound states as well as Majorana overlap.
- Payá et al. 2026, "Absence of Quasi-Majorana False Positives in Full-Shell Hybrid Nanowires", <https://arxiv.org/abs/2604.24858>. Theory: in full-shell wires with smooth confinement, Caroli-de Gennes-Matricon analogs form a trivial end skin that hides quasi-Majorana states from a local probe.

Happy to rerun this if you share the figure data.
