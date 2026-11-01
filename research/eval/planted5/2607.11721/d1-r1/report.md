# Lookalike check: High-field Josephson effect enabled by a moiré Hofstadter spectrum (arXiv 2607.11721v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a high-field Josephson measurement with no topological claim, so I
adapted the library's supercurrent and conductance entries to it and added three
explanations from the graphene Josephson literature that the library does not hold.

**The claim, as I read it.** In device GH1 (θ ∼ 0.21°, L ∼ 200 nm), pockets of zero
resistance with oscillating Ic persist up to about 6 T in the electron moiré minibands
(n/ns > 1), well past the 2rc = L boundary (Fig. 2a-c, e);
GH2 shows the same trend up to 5 T (Fig. S13). You attribute this to dispersive Hofstadter
bands, supported by the overlap of the measured 1/R map with the calculated ⟨v²⟩/vF²
(Fig. 3c-e).

## Checks a careful reader will look for

The library has no ordered checks for supercurrent signals, so the three general practice
checks apply.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "No high field superconductivity nor clear Fabry-Pérot oscillations were observed for the other two devices GH3 and GH4." (SI p. 33). Devices are counted (Table S1); cooldowns and datasets are not.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The maximum voltage we can typically apply in our devices with the Si gate is ± 80 V" (SI p. 20); the Fig. 2c settings are not explained and hole-miniband data at high field are not shown.
3. Give the processing steps from raw data to figures, with data and code : Partly. Ic criterion, series resistance and fits are described (p. 3; SI pp. 19, 22-23), but "The data that support the findings of this study are available from the corresponding author upon reasonable request." (p. 16), and no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets counted: part; how the shown data were chosen: no; second device or dataset: all | "The principal observations reported here were reproduced across multiple additional devices with different twist angles and geometries (see Supplementary Information), however in the following we focus on device GH1" (p. 3) | Give the number of junctions, cooldowns and high-field maps taken, say how the Fig. 2c settings were picked, and show the second-best high-field pattern. |
| Finite-bias resonances setting the switching current (adapted from the field-enhanced supercurrent entry) | Tested in part | Finite-bias dV/dI shown with the switching current: part; effect followed across gate and in other devices: all | "These superconducting features manifest as scattered pockets of vanishing resistance R, that are visible as dark-blue specks in Fig. 2a, and which respectively show non-linear dV/dI characteristics in Fig. 2b." (p. 4) | Show dV/dI(I) for a grid of pockets across Fig. 2a, including those nearest 6 T, marking the zero-resistance branch and any finite-bias peaks; the Fig. 2a pockets come from zero-bias R alone. |
| Series resistance subtraction (adapted to the zero-resistance pockets) | Not tested (data bear on it) | Calibration with its value: no; raw data before subtraction: no | "In measurements with a two-probe scheme, a finite known in-series resistance of 3447 Ω was subtracted from the data." (SI p. 19) | Show raw dV/dI for Fig. 2b before subtraction and say how 3447 Ω was measured; a true supercurrent branch sits at the same raw level at every field. |
| Chiral Andreev edge-state supercurrent (not in library) | Ruled out for the claim | Normal-state map at dc bias above Ic checked for quantum Hall plateaus: all; Ic against the nA edge-state scale: part; period regularity: part | "Landau levels are absent in the former at the same regions in the B–n phase map where superconductivity is observed in the latter." (SI p. 33, Fig. S14) | None needed: an edge-state supercurrent needs a quantum Hall plateau beneath it, and Fig. S14 shows none in either device. |
| Edge-localized Andreev states (not in library) | Tested in part | Current distribution across the width in the regime of the claim: part (zero field only, Fig. S9) | "The agreement with the standard Fraunhofer pattern confirms a uniform supercurrent distribution across the device." (p. 3, Fig. 1g) | Apply the Dynes-Fulton analysis of Fig. S9, or a test for SQUID-like lobes, to the high-field patterns in Fig. 2c and Fig. S11. |
| Brown-Zak normal-state conduction in the 1/R map (not in library) | Not tested (data bear on it) | Same map above the leads' Tc or at bias above Ic, compared with ⟨v²⟩: no | "we use the base-temperature zero-bias conductance 1/R as a proxy for the onset of the superconducting phase" (p. 7) | Run the Fig. 3c-d comparison on the 200 nA map of Fig. S14 or on a 10 K field map, where Brown-Zak conduction survives and superconductivity does not. |

Your Fig. S14 is the strongest control here: it shows the pockets do not sit on quantum
Hall plateaus. The open points are where the supercurrent flows at 4 T (your uniform profile
is shown near zero field only) and whether the Fig. 3e overlap holds with superconductivity
suppressed, since ⟨v²⟩ also governs normal-state conduction. You have the data for both.

## Questions about devices and data

1. Table S1 lists four moiré devices and Section F shows high-field supercurrent in GH1 and GH2. How many junctions did you fabricate and cool down in total, and does "reproduced across multiple additional devices" (p. 3) refer to GH2 alone for the high-field result?
2. Section F sets GH3 and GH4 aside for their length. Were other junctions on the same mesas measured (Fig. S1a shows several contacts), and how did they behave at high field?
3. Which ranges did you measure beyond the ones shown, in particular the hole minibands (n/ns < -1) at high field and fields between 6 T and the 8 T magnet limit?
4. What does the second-best high-field interference pattern look like, and how were n/ns ∼ 1.8 and B ∼ 4.3 T chosen for Fig. 2c?
5. How was the 3447 Ω series resistance calibrated, and could you show the raw two-terminal dV/dI for Fig. 2b and the 1/R map of Fig. 3e before subtraction?
6. How does the correlation between 1/R and <v^2>/vF^2 in Fig. 3c-e look when you use the 200 nA map of Fig. S14 or a field map at 10 K, where superconductivity is suppressed?
7. Can you extract a current distribution, or test for SQUID-like lobes, from the high-field patterns in Fig. 2c and Fig. S11, as you did at zero field in Fig. S9?
8. How often did the field-cycling procedure of SI Sec. A.2 fail to give a reproducible pattern, and could you share the raw data and the analysis code for the Ic extraction and the <v^2> maps?

## Related work

- Ben Shalom et al. 2015, "Quantum oscillations of the critical current and high-field superconducting proximity in ballistic graphene", <https://arxiv.org/abs/1504.03286>. Random superconducting pockets above 1 T with Ic near the quantum limit, attributed to near-edge Andreev states.
- Amet et al. 2015, "Supercurrent in the quantum Hall regime", <https://arxiv.org/abs/1512.09083>. Supercurrent through a graphene quantum Hall region up to 2 T, with plateaus revealed by a dc bias.
- Indolese et al. 2018, "Signatures of van Hove singularities probed by the supercurrent in a graphene - hBN superlattice", <https://arxiv.org/abs/1805.10184>. In a graphene/hBN superlattice junction, interference patterns point to enhanced edge supercurrent near the van Hove singularity.
- Krishna Kumar et al. 2017, "High-temperature quantum oscillations caused by recurring Bloch states in graphene superlattices", <https://arxiv.org/abs/1705.11170>. Oscillations without Landau quantization at simple flux fractions per moiré cell, persisting above room temperature.
- Barrier et al. 2024, "One-dimensional proximity superconductivity in the quantum Hall regime", <https://arxiv.org/abs/2402.14451>. Domain walls in twisted bilayer graphene carry a non-oscillatory supercurrent at quantizing fields.

Happy to rerun this if you share the figure data.
