# Lookalike check: Flux-tunable superconductivity in a TI nano-SQUID (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first.

**The claim, as I read it.** Your evidence for a flux-driven topological phase comes from three devices (A, B, C):
- Global signatures: h/2e oscillations of Ic and a diode sign reversal at half-integer flux (Figs. 1e, 3a, S2a, S4).
- Matching spectral jumps in local and nonlocal conductance (Figs. 1f-g, 3b-e, S2b-e).

You read this as a phase that "is successfully realised" (p. 5). You also report zero-bias peaks in both the predicted topological and trivial regimes, and at zero field (Fig. 4, Fig. S3), and you don't offer those peaks as Majorana evidence. So most entries below bear on the global reading and on the device A peak in Fig. 1f.

## Checks a careful reader will look for

The library has no check list for diode or nonlocal signals, so these are the zero-bias-peak checks and the practice checks.

1. Look for unintended quantum dots : Not done. Your zero-field gate maps (Fig. 4a,b; Fig. S3a,b) are where dots would show. The paper doesn't look for them there.
2. Wide gate, field and angle ranges, with peak heights : Partly. "we do not see a significant difference between the VG dependence of ZBPs in the expected topological or trivial regimes (Fig. 4d-e & g-h) even over a region of VG that includes the Dirac point (Fig. 4j-k)" (p. 5). The paper shows no field-angle series and no table of peak heights.
3. Tunneling at both ends : Partly. "we analysed the correlation of local states at opposite ends of the nanowire" (p. 5, Fig. 4c,f,i,l). This covers devices B and C. The Fig. 1f peak in device A comes from one end only.
4. Peak stability against junction transparency : Not done. The tunnel barriers are fixed ALD layers, and the paper shows no barrier-gate series.
5. Nonlocal gap closing and reopening : Partly. "the nonlocal conductance reveals features that align with the Ic oscillations, such as jumps at the boundaries where the phase transition is supposed to occur (see Fig. 3d-e)" (p. 4).
6. Series resistance and raw data : Partly. "the known filter resistance was subtracted from the recorded data" (p. 6). The paper doesn't give the value, and it shows no raw curves.
7. Device and dataset counts : Partly. "observed in all examined devices" (p. 4). The paper doesn't say how many devices that is.
8. Full parameter ranges : Partly. "the gating range was limited due to a leaky gate dielectric" (p. 12). The paper doesn't say why each shown range was chosen, and every measurement is at base temperature.
9. Processing from raw data to figures : Partly. "corrected for the effects of measurement circuit arising from finite line impedance using the formalism developed in Ref. [2]" (p. 11). The data are on Zenodo (p. 7). The paper doesn't describe the steps of the correlation analysis.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Trivial supercurrent-interferometer diode (not in library) | Not addressed | Not discussed. Fig. 2 models only the topological junction. | Fit Figs. 1e, 3a and S2a with a trivial two-junction model that uses skewed current-phase relations and unequal transparencies, tune the asymmetry with VG, and show which features the model misses. |
| Vortex and screening diode (diode-vortex-screening) | Partly addressed | "the reversal of the SDE exactly at half-integer flux quanta" (p. 2, Fig. 1e). The data bear on it; the paper doesn't discuss it. | Show η near zero field in fine steps for both sweep directions, and compare with a plain Nb strip or a Nb-only junction. |
| Accidental zero crossing at phase π in a transparent junction | Partly addressed | "we do not see a significant difference between the VG dependence of ZBPs in the expected topological or trivial regimes" (p. 5, Fig. 4). The data bear on it; the paper doesn't discuss it. | Extract the JJ1 and JJ2 transparencies from the excess current or IcRN (Fig. 4j), and check whether the features at half-integer flux open into anticrossings as VG lowers them. |
| Trivial Andreev band mimicking a bulk transition | Partly addressed | "there are also nonlocal conductance jumps at Bx values that do not correspond to the Ic features" (p. 5) | Count the nonlocal jumps at half-integer flux and elsewhere, field by field, across the VG range of Fig. S5. |
| Flux-tunable Andreev levels in the junction region | Partly addressed | "present both within the predicted topological range of magnetic fields and in theoretically trivial regimes, including at zero magnetic field" (p. 1). The data bear on it. | Compare the tunnel-junction geometry of devices A, B and C (C mostly lacks peaks), and look for dot levels in gate scans at each junction. |
| Quantum dot Andreev states (abs-quantum-dot) | Partly addressed | "the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5). The data bear on it; the paper doesn't discuss it. | Extend the Fig. 4a,b and S3a,b bias range above the gap, and look for Coulomb diamonds or for peaks that split and recross. |
| Kondo resonance | Partly addressed | "the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5). The data bear on it; the paper doesn't discuss it. | Check whether the zero-field peaks occupy alternating gate windows, and take a temperature series at zero field. |
| Disorder-induced zero-bias peaks | Partly addressed | "suggests that at least some of these ZBPs are driven by disorder effects" (p. 5). The paper names disorder as the likely origin and doesn't test it. | Report peak heights across VG and Bx from the Fig. 4 data, and add disorder to the tight-binding model. |
| Crowded trivial subgap states | Partly addressed | "both showing a large number of ZBPs at both ends" (p. 5). The paper doesn't model multiple subbands. | Model the nanowire's surface subbands at your W and d, and compare the predicted field range with where the peaks appear. |
| Quasi-Majorana states | Partly addressed | "We find that both regimes contain ZBPs on either end (see Fig. 4c,f,i,l) the majority of the time." (p. 5) | Set the two-end correlation against the nonlocal spectra at the same VG and Bx. |
| Weak antilocalization | Not addressed | Not discussed. | Compare peak height with tunnel-contact conductance across devices and gate settings. |
| Exceptional-point zero mode | Not addressed | Not discussed. | Use the correlated two-end peaks to estimate how much the end states overlap, for example through splittings that appear at one end and not the other. |
| Peak at one end only | Partly addressed | "we analysed the correlation of local states at opposite ends of the nanowire" (p. 5). This covers devices B and C only. | For Fig. 1f, say that device A had no second probe, and show the B and C correlation over the first predicted topological lobe on its own. |
| Local-probe loophole | Partly addressed | "a conclusive demonstration will also require the development of advanced probes of Majorana physics" (p. 5) | Pair the correlated two-end peaks with the zero-bias nonlocal conductance at the same settings. |
| Analysis outcome set by data choices (adapted to the correlation analysis) | Not addressed | Not discussed. The smoothing, derivative step and bias window behind Fig. 4l are not given. | Rerun Fig. 4l and Fig. S3l with different smoothing, bias windows and resolution, and release the code. |
| Fine-tuning and selection | Partly addressed | "a zero-bias conductance peak was mostly absent in this device" (p. 13, device C) | State how many devices and cooldowns you measured and how you chose Fig. 1f. |

## Questions about devices and data

1. How many nano-SQUID devices did you measure in total, including those where only the Josephson junctions worked, and how many showed the Ic oscillations, the diode sign reversal and zero-bias peaks? The paper names devices A, B and C and says the global signatures appear "in all examined devices" (p. 4).
2. Why were the other devices set aside, in particular the rest of the "series of devices with two functioning tunnel contacts" (p. 4), and what did they show?
3. Which ranges did you measure beyond the ones shown: temperatures above the 30 mK base, field angles away from the nanowire axis, and, for device A, gate voltages outside -10 to 20 V?
4. What does the second-best dataset look like? Device C answers this in part (pp. 12-13); is there a second case like Fig. 1f, where a zero-bias peak appears at half-integer flux and persists over a wide field range?
5. Would a trivial two-junction interferometer model, with skewed current-phase relations and unequal JJ1 and JJ2 transparencies fitted to your data, reproduce Ic(Φ) and η(Φ) in Figs. 1e, 3a and S2a, and which features would it miss?
6. What are the transparencies of JJ1 and JJ2 (for example from the excess current, or IcRN in Fig. 4j), and how do they change with VG?
7. For the end-to-end correlation in Fig. 4l and Fig. S3l, which smoothing, derivative step and bias window did you use, how did you classify points where neither end shows a clear peak or dip, and how do the fractions change when you vary these choices?
8. At zero field, do the tunnel spectra show Coulomb diamonds or resonances above the gap, or zero-bias peaks that alternate between gate-voltage windows, and how do the zero-field peaks depend on temperature?

## Related work

- Souto, Leijnse and Schrade 2022, "The Josephson diode effect in supercurrent interferometers", <https://arxiv.org/abs/2205.04469>. In theory, two junctions with non-sinusoidal current-phase relations in a loop form a flux-tunable diode, up to about 40% efficient, with no Zeeman splitting or spin-orbit coupling. The effect vanishes at integer multiples of Φ0/2 and needs unequal transmissions.
- Dartiailh et al. 2021 (arXiv 2019), "Phase signature of topological transition in Josephson Junctions", <https://arxiv.org/abs/1906.01179>. Two Al/InAs junctions in a loop show a π jump in junction phase together with a critical-current minimum in in-plane field, read as a topological transition. This is a close analogue of your global signatures.
- Valentini et al. 2021, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", <https://arxiv.org/abs/2008.02348>. Subgap states follow the tunnel-junction region. Quantum dots there host flux-tunable Andreev levels that give robust trivial zero-bias peaks.
- Hess, Legg, Loss and Klinovaja 2023, "Trivial Andreev band mimicking topological bulk gap reopening in the non-local conductance of long Rashba nanowires", <https://arxiv.org/abs/2210.03507>. A trivial bulk Andreev band gives an apparent gap reopening in nonlocal conductance, alongside trivial end peaks.
- Chen et al. 2019, "Ubiquitous non-Majorana Zero-Bias Conductance Peaks in Nanowire Devices", <https://arxiv.org/abs/1902.02773>. At finite field, Majorana-like peaks with zero-bias pinning become ubiquitous in InSb-Al devices. A multiband model traces them to crowded trivial subgap states.

Happy to rerun this if you share the figure data or the code for the correlation analysis.
