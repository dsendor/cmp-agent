# Lookalike check: High-field Josephson effect enabled by a moiré Hofstadter spectrum (arXiv 2607.11721v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport. A lookalike is an ordinary effect that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper reports high-field supercurrent in a moiré graphene junction, which is outside the library's topological focus. So I adapted three entries to it (supercurrent, series resistance and practice) and added three explanations from the graphene literature, marked "(not in library)".

**The claim, as I read it.** In device GH1 (θ ∼ 0.21°, L ∼ 200 nm, W ∼ 1.5 µm), the electron moiré minibands (n/ns > 1) show pockets of zero resistance up to about 6 T, well past the 2rc = L limit. In those pockets Ic oscillates with field and density (Fig. 2a-e), and the pockets line up with regions of high calculated band velocity in the Hofstadter spectrum (Fig. 3c-e). GH2 shows the same up to 5 T (Fig. S13). A non-aligned graphene junction stays below 2rc = L (Fig. S15d).

## Checks a careful reader will look for

The library has no ordered checks for unusual supercurrents, so these are the practice checks, which apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "No high field superconductivity nor clear Fabry-Pérot oscillations were observed for the other two devices GH3 and GH4." (SI p. 33). The main text says the observations "were reproduced across multiple additional devices" (p. 3), and it gives no counts of cooldowns or datasets.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. You give the gate and density limits ("The maximum voltage we can typically apply in our devices with the Si gate is ± 80 V", SI p. 20). You don't explain why you chose n/ns ∼ 1.8 or the fields of the interference patterns.
3. Give the processing steps from raw data to figures, with data and code : Partly. You describe the Ic criterion, the smoothing and the series subtraction (SI pp. 19, 22-23). Data are "available from the corresponding author upon reasonable request" (p. 16), and no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Supercurrent shaped by finite-voltage resonances (adapted from field-enhanced-supercurrent-resonances) | Tested in part | Finite-bias dV/dI with the switching current: part (plotted against current only); across gate and other devices: all (Fig. 2e, Fig. S13) | "these states show phase-coherent Josephson transport, as evidenced by the oscillating Ic with both magnetic field (see Fig. 2c), and carrier density (Fig. 2e)." (p. 4) | Plot the pocket curves of Fig. 2b and 2e against measured voltage, next to a zero-field curve, so the zero-voltage branch and any resonance near switching are visible. |
| Subtracted series resistance (adapted from series-resistance-subtraction) | Tested in part | Calibrated value: part (value given, calibration not described); raw data before subtraction: no | "In measurements with a two-probe scheme, a finite known in-series resistance of 3447 Ω was subtracted from the data." (SI p. 19) | Show raw two-probe R for Fig. 2a, and redo the 20 mS cutoff of Fig. S18 with the series value moved by 1 to 2%. |
| Fine-tuning and selection | Tested in part | Devices and how many showed it: part (devices yes, datasets no); how shown data were chosen: no; second device: all (GH2, Figs. S12-S13) | "The principal observations reported here were reproduced across multiple additional devices with different twist angles and geometries (see Supplementary Information)" (p. 3) | Say in the main text that two of four moiré junctions showed the pockets, and give the number of cooldowns and interference datasets. |
| Chiral quantum Hall edge supercurrent (not in library) | Ruled out for the claim | Normal-state Landau levels with bias above Ic: all (Fig. S14, GH1 and GH2); Ic size and period: part (GH2 values not stated in text) | "The absence of these LLs proves that the superconducting proximity effect in our JJs does not occur in the quantum Hal regime." (SI p. 33) | None needed; the Landau-fan test is enough on its own, because edge supercurrent needs a quantum Hall state where the pockets sit. |
| Near-edge mesoscopic Andreev states (not in library) | Tested in part | Current distribution at high field: no (Fig. S9 is near zero field); cutoff compared with 2rc = L: all (Figs. 2a, S13a, S15d) | "We find that the onset of this phase cannot be explained within a semiclassical picture built on the zero-field Fermi surface, even when magnetic breakdown between neighboring Fermi contours is included." (p. 7) | Run the Dynes-Fulton reconstruction of Fig. S9 on the high-field patterns of Fig. 2c and Fig. S11. |
| Normal-state Brown-Zak conductance in the 1/R map (not in library) | Not tested (data bear on it) | Normal-state map compared with zero-bias 1/R: no | "we use the base-temperature zero-bias conductance 1/R as a proxy for the onset of the superconducting phase" (p. 7) | Overlay or subtract the 200 nA map of Fig. S14 (or a map above 9 K) on Fig. 3e, to mark regions that stay bright without supercurrent. |

A note on the two adapted entries. In Fig. 2b and 2e, a switching transition from a flat low-resistance branch up to RN is hard to fake with a constant offset. The wide maps are different: Fig. 2a, Fig. 3e and the 20 mS cutoff in Fig. S18 set the reported ∼6 T extent, and they sit on top of a 3447 Ω subtraction. The questions below ask for the curves at the highest fields for that reason.

## Questions about devices and data

1. How many junctions did you fabricate and measure in total, over how many cooldowns, and how many showed the high-field pockets? Table S1 and SI Sec. F (p. 33) give two of the four moiré junctions; could the main text say so where it reads "reproduced across multiple additional devices" (p. 3)?
2. Fig. S1a shows several MoRe contacts on one stack: were other junctions on the GH1 to GH4 stacks measured, and if so, why were they set aside? (GH3 and GH4 are explained by their length on p. 33.)
3. Which field and density ranges did you measure beyond those shown, in particular the hole-side minibands (n/ns < -1) at high field and fields between 6 T and the 8 T magnet limit?
4. What does the second-best high-field dataset look like: could you show dV/dI against I at the highest fields that Fig. 2a and Fig. 3e mark as superconducting (5 to 6 T), in GH1 and GH2?
5. How was the 3447 Ω series resistance (SI p. 19) determined, and how do the pockets in Fig. 2a and the 20 mS cutoff of Fig. S18 change if it is off by 1 to 2%?
6. How much of the bright 1/R region in Fig. 3e survives with a dc bias above Ic (as in Fig. S14) or above the leads' Tc, where normal-state Brown-Zak conductance would remain and supercurrent would not?
7. Could you reconstruct the supercurrent distribution, as in Fig. S9, from the high-field interference patterns of Fig. 2c and Fig. S11, to see whether the pockets carry current through the bulk or near the edges?
8. How did you choose n/ns ∼ 1.8 and the fields 2.5, 3.5, 4.3 and 4.5 T for the interference patterns, and how many pockets did you measure in total compared with the number shown?

## Related work

- Ben Shalom et al. 2016, "Quantum oscillations of the critical current and high-field superconducting proximity in ballistic graphene", <https://arxiv.org/abs/1504.03286>. In ballistic graphene junctions, superconducting pockets appear at random above 1 T with Ic close to the single-mode limit, and the authors attribute them to mesoscopic Andreev states near the graphene edges.
- Amet et al. 2016, "Supercurrent in the quantum Hall regime", <https://arxiv.org/abs/1512.09083>. Supercurrent flows through a quantum Hall weak link at fields up to 2 T, with a sub-nA switching current on top of the quantum Hall plateaus.
- Villani et al. 2025, "Quasi-Φ0-periodic supercurrent at quantum Hall transitions", <https://arxiv.org/abs/2503.15384>. In an hBN-encapsulated graphene junction, superconducting pockets persist past the quantum Hall onset up to 2.4 T, with roughly h/2e periodicity in field.
- Barrier et al. 2024, "One-dimensional proximity superconductivity in the quantum Hall regime", <https://arxiv.org/abs/2402.14451>. Domain walls in minimally twisted bilayer graphene carry a non-oscillatory supercurrent at quantizing fields close to the electrodes' upper critical field.
- Krishna Kumar et al. 2017, "High-temperature quantum oscillations caused by recurring Bloch states in graphene superlattices", <https://arxiv.org/abs/1705.11170>. Graphene superlattices show conductance oscillations at simple fractions of the flux quantum per unit cell (Brown-Zak oscillations), and these persist above room temperature.

Happy to rerun this if you share the raw two-probe maps or the figure data.
