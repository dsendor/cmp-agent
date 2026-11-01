# Lookalike check: Electrically controllable superconducting memory in UTe2 (arXiv 2603.02450v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper reports bulk critical current transport in a multiphase superconductor, which sits outside the library's main scope. So I adapted the one vortex entry that fits, and I added three ordinary explanations, two from vortex matter and one from heating, taken from papers I opened and marked "(not in library)".

**The claim, as I read it.** In UTe2 crystals at 50 mK, with B near the b axis, an abrupt drop of a large dc current leaves the crystal in a state with a higher Jc that lasts for hours. A slow ramp-down erases that state. The data are Fig. 1b (sample S1 at 20 T), and Fig. 1c and Figs. 2 to 4 (sample S2). You read this as an intrinsic effect of competing SC1 and SC2 vortex species, in a region you call SC1.5.

## Checks a careful reader will look for

The library has no ordered checks for this kind of signal, so only the practice checks apply.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "Each of the three samples investigated in this study had 𝐽 sourced along the [100] direction" (Methods, p. 23). You show the pulse protocol on S1 and S2. S3 appears only in the ac data of Fig. 4h, and the paper doesn't say whether S3 shows the memory effect.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "as a function of magnetic field strength and rotation angle up to 30 T at 50 mK" (p. 9). Rotation covers b toward c only. The reasons behind the shown fields (7, 9, 14, 15, 20 T) and the sample cross-sections behind J aren't given.
3. Give the processing steps from raw data to figures, with data and code : Partly. "Δ𝐽 is calculated here at a nominal fixed value of 𝑉 = 1 µV" (Extended Data Fig. 1, p. 27). The instrument code is a supplement, and "The datasets supporting the findings of this study will be uploaded to the University of Cambridge Apollo Repository prior to publication" (pp. 25 to 26).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: all | "In Fig. 1c we show data measured on a second sample (labelled S2)." (p. 7, Fig. 1c) | Say how S3 behaves under the pulse protocol and how the shown fields were picked; show the S1 counterpart of Fig. 4e. |
| Vortex edge barriers and Meissner screening (adapted from the diode entry) | Tested in part | Same measurement on a plain film or junction of the parent superconductor: part (the SC1-only and SC2-only regimes of S2 act as in-sample controls); Effect followed against field, sample width or edge quality: part (field and angle for S2 only) | "At high 𝐵 around 30 T the material is then fully in the SC2 phase, and the memory effect is no longer exhibited (Fig 4c)." (p. 9) | Repeat the pump and erase sequence of Fig. 2 on a crystal cut to a different width, or after re-polishing its edges. |
| Supercooled disordered vortex phase near a peak effect (not in library) | Tested in part | Field-cooled and zero-field-cooled states compared at the same B and T: no; Memory region placed against a rise of Jc with field or temperature: part (Fig. 4b and Extended Data Fig. 9 show a non-monotonic Jc(B) that the paper doesn't compare to a peak effect) | "An anomalous non-monotonic kink in 𝑉 (𝐵) at high 𝐽 is observed at the boundary of the memory region." (Fig. 4b caption, p. 11) | Field cool S2 to 9 to 14 T and compare the first Jc with the pumped state; overlay the Jc(B) from Fig. 4b on the ΔJ window of Fig. 4e. |
| Edge contamination through surface barriers (not in library) | Not tested (argued, not tested) | Current distribution across the sample width measured: no; Ac and dc critical currents compared, with frequency dependence, in the same sample: no | "this should be insensitive to how the current is turned off, depending only on the total energy imparted" (p. 13) | Compare ac Jc at a few frequencies with dc Jc in S2 at 14 T; in NbSe2, edge-injected disorder makes the two differ and gives a ramp-rate-dependent Ic. |
| Joule heating during pulses (not in library) | Tested in part | Sample temperature measured directly during and after the pulses: part (the plot sits in the Supplementary Information, which isn't in the v1 PDF) | "In the Supplementary Information we plot the measured temperature as a function of time during the current pulse measurement protocols" (p. 12) | Put the temperature traces in the main PDF, with the thermometer's location, the contact resistances and the power during the 40 mA reset. |

A note on the vortex rows: your relaxation-rate result (Fig. 2c) is your main argument against ordinary pinning. Xiao et al. report a ramp-speed-dependent critical current in an ordinary NbSe2 vortex lattice, so that test by itself may not separate the two readings. In both samples the memory window also sits next to a field range where Jc rises with field: in S2 between about 10 and 14 T (Fig. 4b), and in S1 above 20 T ("𝐽𝑐 is minimal around 20 T, and is actually higher at 28 T than it is at 9 T", Extended Data Fig. 9, p. 35). In NbSe2 that is where metastable vortex states show up. You could address this directly with the field-cooling comparison.

## Questions about devices and data

1. How many UTe2 crystals did you measure with the pulse protocol, and how many showed the memory effect? In particular, does S3 (RRR 395), which appears only in the ac data of Fig. 4h, show it?
2. Why were the others set aside, if any were?
3. Which ranges did you measure beyond the ones shown, for example rotation toward the a axis, pulse maps of S1 away from 20 T, excitations above 20 A cm^-2, and the waiting times behind "persists over a timescale of at least several hours" (p. 7)?
4. What does the second-best dataset look like, for example a map of ΔJ against B for S1 like your Fig. 4e?
5. How was each field reached: swept at 50 mK, or field cooled? Does a field-cooled state at 9 to 14 T start in the high-Jc state before any pump?
6. What are the sample cross-sections and the contact resistances, how much power do the 40 mA reset and the pumps dissipate in the contacts and the sample, and where is the thermometer behind the Supplementary temperature traces?
7. ΔJ is read at V = 1 µV, and the memory region ends where ΔJ "reaches zero within the resolution of the measurement" (Fig. 4g caption, p. 11). How do the boundaries in Fig. 4e and 4f move for other voltage criteria and other Jex, and what is the ΔJ resolution?
8. In S2 at 0°, ΔJ starts near 7 T and peaks near 10 T (Fig. 4e), while the low-Jc coexistence region you cite lies at about 15 to 20 T (p. 5). What sets the lower edge of the memory region, and does it move with sample quality the way the upper edge does?

## Related work

- Henderson, Andrei, Higgins and Bhattacharya 1996, "Metastability and Glassy Behavior of a Driven Flux-Line Lattice", <https://arxiv.org/abs/cond-mat/9606074>. In 2H-NbSe2 they find two vortex states with different order and history-dependent dc and pulsed transport near the peak effect, and current anneals the metastable state.
- Xiao, Andrei and Higgins 1999, "Flow Induced Organization and Memory of a Vortex Lattice", <https://arxiv.org/abs/cond-mat/9904141>. In NbSe2 the vortices freeze in place when the current is turned off. There is a regime where a driving current can raise or lower the critical current, and Ic depends on the ramp speed.
- Paltiel et al. 2000, "Dynamic instabilities and memory effects in vortex matter", <https://arxiv.org/abs/cond-mat/9912157>. NbSe2 remembers the direction, amplitude, duration and frequency of the previous current. Hall sensor arrays trace this to disorder injected at the sample edges.
- Ravikumar et al. 2000, "Stable and Metastable vortex states and the first order transition across the peak effect region in weakly pinned 2H-NbSe_2", <https://arxiv.org/abs/cond-mat/0007436>. Each metastable vortex state has its own Jc, set by thermomagnetic history, and small field cycling brings it to the stable state.
- Courtois, Meschke, Peltonen and Pekola 2008, "Origin of Hysteresis in a Proximity Josephson Junction", <https://arxiv.org/abs/0805.4524>. A direct measurement of the electron temperature shows that the I-V hysteresis in SNS junctions comes from heating once the junction switches to the resistive state.

Happy to rerun this if you share the Supplementary Information and the figure data.
