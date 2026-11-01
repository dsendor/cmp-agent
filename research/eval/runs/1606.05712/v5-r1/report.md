# Lookalike check: Chiral Majorana edge state in a QAHI-superconductor structure (arXiv 1606.05712v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library has no ordered checks for half-quantized chiral plateaus, so only its
general practice checks appear below.

**The claim, as I read it.** A four-terminal longitudinal conductance plateau near 0.5 e2/h at each magnetization reversal of a 6 nm (Cr0.12Bi0.26Sb0.62)2Te3 film crossed by a Nb bar, read as transport through a single chiral Majorana edge mode (the N = ±1 phase). It comes from device I at 20 mK to 520 mK (Fig. 2c, Fig. 3a, 3b), with devices II and III at 350 mK (Fig. 2b) and a bare Hall bar from the same wafer as reference (Fig. 2d, Fig. 3c).

## Checks a careful reader will look for

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "three representative TSC devices" (p. 19, Fig. 2b caption); the total measured is not stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "These features completely disappear above 400, 470, and 390 mK for device I (Fig. 3b), II, and III, respectively" (p. 9); field ranges beyond the figures and the reasons for each window are not given.
3. Give the processing steps from raw data to figures, with data and code : Not done. The measurement geometry is described (p. 6), with no processing steps, data or code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Superconducting strip acting as an electrical short for the film | Tested in part | Contact transparency measured directly: no; plateau checked across the full aligned-magnetization field range, including above the Nb critical field: part | "Outside the half-plateau regimes, when the magnetization is fully saturated, the conductance reaches to a quantized value of 0.98(±0.04) e2/h" (p. 8, Fig. 2c) | Report the Nb to film contact resistance from a separate contact, and show full loops with the Nb driven normal (above its critical field or temperature) |
| Fine-tuned plateau (adapted from the 2e2/h entry to a field plateau at 0.5 e2/h) | Tested in part | How the plateau was found: no; same plateau over wider field ranges: part (full loop for device I only); plateau heights from other regimes and devices: part | "The pertinent data obtained from other two TSC devices (II and III) exhibit 0.52(±0.06) and 0.48(±0.07) e2/h conductance plateaus at similar magnetic field ranges." (p. 8, Fig. 2b) | Say how each plateau window and value were picked, and list plateau heights for every trace in Fig. 3a and for II and III at 20 mK |
| Barkhausen-type domain jumps during reversal (not in library) | Tested in part | Successive sweeps at fixed temperature and rate: part (Fig. 3a steps the temperature between traces); separate voltage-contact pairs: no; temperature and sweep-rate dependence: part (temperature only) | "Thus, we claim that the half-plateau conductance is not due to Barkhausen effect." (p. 10) | Liu et al. report jump patterns that repeat across scans, so overlay several sweeps at 20 mK at a fixed, stated rate and add a second voltage pair |
| Fine-tuning and selection | Tested in part | Devices measured and how many showed it: part; how the shown data were chosen: no; second device shown: all | "The three devices all show conductance plateaus at the low-field shoulders of the σ12 valleys" (p. 19, Fig. 2b caption) | State how many devices were made and measured, and show II and III over the full loop at 20 mK |

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed the half plateau? Fig. 2b calls devices I to III "three representative TSC devices" (p. 19).
2. Why were the other devices set aside, if there were others?
3. Which field ranges, sweep directions, sweep rates and temperatures did you measure beyond the ones shown? For devices II and III, Fig. 2b shows one sweep from about -40 to 290 mT at 350 mK.
4. What do devices II and III look like over the full hysteresis loop at 20 mK, next to Fig. 2c?
5. During the σ12 measurements, was the Nb bar floating, grounded or wired to its own leads, and what is the contact resistance between the Nb and the film?
6. Did you measure σ12 with the Nb driven normal, above its critical field or temperature, or in a device with a normal metal strip, and what value does σ12 take there?
7. How did you extract the plateau values and their uncertainties, for example 0.50(±0.06) e2/h (p. 8): which field window was averaged, and how did dσ12/dB in Fig. 2c set its edges?
8. How many reversal sweeps did you take at a fixed temperature, and do the plateau field and value repeat from sweep to sweep? The abstract mentions "many magnetic reversal sweeps" (p. 2).

## Related work

- Liu et al. 2016, "Large discrete jumps observed in the transition between Chern states in a ferromagnetic Topological Insulator", <https://arxiv.org/abs/1603.02311>. Large discrete jumps in Hall and longitudinal resistance during magnetization reversal of Cr-doped (Bi,Sb)2Te3 near 65 to 145 mK, with a pattern that repeats across scans.
- Ji and Wen 2017, "A mechanism of e^2/2h conductance plateau without 1D chiral Majorana fermions", <https://arxiv.org/abs/1708.06214>. Theory: a half-quantized plateau as a general feature of good electric contact between a quantum Hall film and a superconducting film.
- Zhang and Liu 2019, "Disordered Quantum Transport in Quantum Anomalous Hall Insulator-Superconductor Junctions", <https://arxiv.org/abs/1908.03303>. Numerics: extra chiral or non-chiral metallic modes give strong Andreev conversion and half-electron half-hole transmission.
- Uday et al. 2023, "Induced superconducting correlations in the quantum anomalous Hall insulator", <https://arxiv.org/abs/2307.08578>. Crossed Andreev reflection across a narrow grounded Nb electrode on a QAHI chiral edge, a direct probe of Nb coupling to the edge.

Happy to rerun this if you share the figure data or the 20 mK loops for devices II and III.
