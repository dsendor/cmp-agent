# Lookalike check: Chiral Majorana edge state in a quantum anomalous Hall insulator-superconductor structure (arXiv 1606.05712v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Two library entries written for nanowire peaks (fine-tuned plateaus, and how a
conductance value is extracted) are adapted here to a field-swept conductance plateau.

**The claim, as I read it.** During each magnetization reversal, the four-terminal
conductance σ12 of a Nb-covered (Cr0.12Bi0.26Sb0.62)2Te3 film shows plateaus near
0.5 e²/h at the shoulders of the σ12 valleys (Fig. 2b at 350 mK for devices I, II and III;
Fig. 2c and Fig. 3a at 20 mK). These sit between σ12 near e²/h at saturation and near
zero in the normal-insulator dips, and are read as transport through a single chiral
Majorana edge mode (𝒩 = ±1).

## Checks a careful reader will look for

The library has no ordered checks for half-quantized chiral plateaus yet, so this list holds
the general practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. Fig. 2b shows "three representative TSC devices" (p. 19); how many were made and measured, and why these three, isn't stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Fig. 3 gives the temperature series, "Traces are offset for clarity, except for the lowest traces at 20 mK in (a), 350 mK in (b), and 350 mK in (c) with 10-mK steps." (p. 20); the number of sweeps, sweep rate, excitation and the reason for each field window aren't given.
3. Give the processing steps from raw data to figures, with data and code : Not done. How σ12 is computed from V12 and I12, and how plateau values and their uncertainties were read off, aren't described; no data or code are linked.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Superconducting strip with a transparent contact acting as an electrical short | Partly addressed | "Any backscattering processes from the TSC𝒩=±2 or the NSC𝒩=0 phase would only involve a considerably small Andreev scattering, which cannot explain the half-integer conductance observed in this experiment." (p. 10); an argument, and the Nb-film contact isn't measured. | Measure the Nb-film interface resistance with the Nb bar's own leads (Isc, Vsc in Fig. 1b), and sweep σ12 to fields above the Nb critical field. |
| Plateau from fine-tuning, found by a dedicated search (adapted) | Partly addressed | "The pertinent data obtained from other two TSC devices (II and III) exhibit 0.52(±0.06) and 0.48(±0.07) e2/h conductance plateaus at similar magnetic field ranges." (p. 8, Fig. 2b) | Show every sweep, both field directions, for all three devices at 20 mK, and report any plateau-like features at other values. |
| How the conductance value is extracted (adapted from series-resistance subtraction) | Partly addressed | "obtained by passing an alternating current (I12 in Fig. 1b) through the outer two probes and measuring the potential drop across the inner two probes" (p. 6); the four-terminal setup avoids lead resistance, and the conversion to σ12 isn't stated. | Give the formula from V12 to σ12, show raw V12, and explain the saturated σ12 at 350 mK. |
| Fine-tuning and selection | Partly addressed | "of three representative TSC devices as functions of perpendicular magnetic fields at 350 mK" (p. 19, Fig. 2b) | State devices made, measured and showing plateaus, cooldowns, and what the next-best device looks like. |
| Barkhausen-like discrete jumps at the Chern transition (not in library; Liu et al. 2016, https://arxiv.org/abs/1603.02311) | Partly addressed | "the half-integer plateaus can be well repeated with clear temperature traces (Fig. 3a)" (p. 10); argued, and successive sweeps at one temperature aren't shown. | Overlay successive sweeps at fixed temperature and at two sweep rates, with the control Hall bar at the same temperatures. |

Some notes on the rows.

**The superconducting short.** A strip that couples strongly to the chiral edges can, on its
own, hold the two-terminal conductance at half of e²/h wherever the magnetization is
aligned. Your 20 mK data bear on this: "Outside the half-plateau regimes, when the
magnetization is fully saturated, the conductance reaches to a quantized value of
0.98(±0.04) e2/h" (p. 8, Fig. 2c). The paper doesn't discuss the strip as a possible short,
and the contact transparency isn't reported. Your device already has leads on the Nb bar,
so sending current from a film probe into the Nb bar would give the interface resistance
directly. At 350 mK, σ12 at the highest fields in Fig. 2b and Fig. 3b appears to sit near
0.7 e²/h, which is worth explaining next to the 0.49 e²/h plateau. Magnetic disorder near
the coercive field can also give plateau-like features through percolating edges; a wider
device set and the control bar at 20 mK would show this.

**Selection and fine-tuning.** Three devices, four plateau values between 0.48 and
0.52 e²/h, and the temperatures where the plateaus vanish ("400, 470, and 390 mK for device I
(Fig. 3b), II, and III", p. 9) are a good start. Devices II and III appear only at 350 mK, on
the positive-field side of one sweep, and the Fig. 2b caption notes that only device I shows
the sudden increase at the high-field shoulder. Showing II and III at 20 mK in both sweep
directions would let a reader judge how typical device I is.

**Barkhausen-like jumps.** You raise this yourself (pp. 9 to 10) and argue from
reproducibility and from the high-field shoulder. Liu et al. report jumps in a magnetic
topological insulator that are stochastic yet partly reproducible over successive scans.
Successive sweeps at one temperature, with the abstract's "many magnetic reversal sweeps"
(p. 2) counted, would test this directly.

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed the 0.5 e²/h plateaus? Fig. 2b calls devices I, II and III "representative".
2. Why were the others set aside?
3. Which field ranges, field directions and temperatures did you measure beyond the ones shown, in particular the negative-field side for Fig. 2b and fields above the Nb critical field?
4. What do devices II and III look like at 20 mK, over full sweeps in both directions?
5. What is the resistance of the Nb-film interface, and could you measure it through the Nb bar's own leads (Isc, Vsc in Fig. 1b)?
6. How many reversal sweeps did you take at a fixed temperature, at what sweep rate, and do the plateau fields and values repeat from sweep to sweep?
7. How is σ12 computed from V12 and I12, how were the plateau values and uncertainties (for example 0.49 and ±0.05 e²/h) read off, and why does σ12 at the highest fields in Fig. 2b sit near 0.7 e²/h at 350 mK?
8. Fig. 3c shows the control Hall bar from 350 mK up; what does its σ12 look like at 20 mK, next to Fig. 2c?

## Related work

- Wang, Zhou, Lian and Zhang 2015, "Chiral topological superconductor and half-integer conductance plateau from quantum anomalous Hall plateau transition", <https://arxiv.org/abs/1507.00788>. Proposes the 𝒩 = 1 chiral phase in a magnetic topological insulator film next to an s-wave superconductor and predicts a half-integer conductance plateau at the coercive field.
- Ji and Wen 2018, "A mechanism of e²/2h conductance plateau without 1D chiral Majorana fermions", <https://arxiv.org/abs/1708.06214>. Shows that a half-quantized σ12 is a general feature of good electrical contact between a quantum Hall film and a superconducting film on top of it, with or without chiral Majorana modes, and models the contact with percolation.
- Liu et al. 2016, "Large discrete jumps observed in the transition between Chern states in a ferromagnetic Topological Insulator", <https://arxiv.org/abs/1603.02311>. Reports large jumps in Hall and longitudinal resistance as a magnetic topological insulator leaves its metastable Chern state; the jumps are stochastic yet partly reproducible over successive scans.
- Lachman et al. 2015, "Visualization of superparamagnetic dynamics in magnetic topological insulators", <https://arxiv.org/abs/1506.05114>. NanoSQUID imaging of a Cr-doped (Bi,Sb)2Te3 film shows the Hall plateau transition proceeds through random reversals of domains a few tens of nanometers across.
- Uday et al. 2024, "Induced superconducting correlations in the quantum anomalous Hall insulator", <https://arxiv.org/abs/2307.08578>. Detects crossed Andreev reflection across a narrow Nb electrode on a quantum anomalous Hall edge through a negative downstream nonlocal voltage, a way to probe how a Nb contact couples to the edge.

Happy to rerun this if you share the raw sweeps for devices I to III.
