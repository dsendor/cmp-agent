# Lookalike check: High-field Josephson effect enabled by a moiré Hofstadter spectrum (arXiv 2607.11721v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper reports a high-field supercurrent in a moiré graphene junction, which is outside the library's topological scope, so I adapted the supercurrent and series-resistance entries and added two explanations from the graphene Josephson literature that the library lacks.

**The claim, as I read it.** In device GH1 (L ∼ 200 nm, θ ∼ 0.21°), pockets of vanishing two-probe resistance with a finite critical current appear in the moiré minibands up to ∼6 T (Fig. 2a, b, e), with irregular Ic(B) oscillations (Fig. 2c, Fig. S11), well beyond the 2rc = L limit; GH2 repeats this up to 5 T (Fig. S13). You read this as bulk Andreev transport carried by dispersive Hofstadter bands, matched to the calculated ⟨v²⟩/vF² (Fig. 3d, e).

## Checks a careful reader will look for

The library has no check list for supercurrent claims, so only the practice checks apply.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "No high field superconductivity nor clear Fabry-Pérot oscillations were observed for the other two devices GH3 and GH4." (SI p. 33). Cooldowns and datasets aren't counted, and p. 3 speaks of "multiple additional devices".
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The maximum voltage we can typically apply in our devices with the Si gate is ± 80 V" (SI p. 20); the reason for the interference cuts at n/ns ∼ 1.8 (GH1) and 1.6 (GH2) isn't given.
3. Give the processing steps from raw data to figures, with data and code : Partly. "a finite known in-series resistance of 3447 Ω was subtracted from the data" (SI p. 19), and the Ic and Fabry-Pérot extraction is described (SI pp. 22 to 23); data are "available from the corresponding author upon reasonable request" (p. 16), with no code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets counted: part; how the shown data were chosen: no; second device or dataset shown: all | "The principal observations reported here were reproduced across multiple additional devices with different twist angles and geometries (see Supplementary Information), however in the following we focus on device GH1" (p. 3); GH2 in SI Section F. | Count cooldowns and datasets, say why GH1 and the n/ns ∼ 1.8 cut were chosen, and show a pocket from another density range. |
| Field-dependent finite-bias resonances setting the switching current (adapted from triplet claims) | Tested in part | Finite-bias dV/dI with the switching current: part (cuts at n/ns ∼ 1.8 and 4.1 T only); effect across gate and devices: all | "These superconducting features manifest as scattered pockets of vanishing resistance R, that are visible as dark-blue specks in Fig. 2a, and which respectively show non-linear dV /dI characteristics in Fig. 2b." (p. 4) | Plot dV/dI versus I across a pocket edge of Fig. 2a, marking finite-bias peaks next to the extracted Ic, so a reader sees Ic tracks the zero-voltage branch. |
| Series resistance subtraction (adapted to the zero-resistance criterion) | Not tested (data bear on it) | Calibration with value: no (value stated, method not); raw data before subtraction: no | "In measurements with a two-probe scheme, a finite known in-series resistance of 3447 Ω was subtracted from the data." (SI p. 19) | Show raw R for Fig. 2a and how 3447 Ω was found, and check the pocket map against a few tens of ohms change, since the 20 mS cutoff of Fig. S18 is 50 Ω. |
| Chiral Andreev edge-state supercurrent (not in library) | Ruled out for the claim | Normal-state fan checked for plateaus where pockets sit: all (Fig. S14, both devices); interference periodicity checked: all (Fig. 2c, S11, S13c) | "The absence of these LLs proves that the superconducting proximity effect in our JJs does not occur in the quantum Hal regime." (SI p. 33); the fan alone separates it, since a chiral edge supercurrent needs a quantum Hall plateau. | None needed. |
| Supercurrent carried by Andreev states near the graphene edges (not in library) | Not tested (data bear on it) | High-field current-density profile: no (Fig. S9c is near zero field); high-field pattern compared with an edge pattern: no | "The irregular variation in the amplitude and periodicity of these oscillations, ranging from ∼ 2.3 ± 0.2 mT to ∼ 3.4 ± 0.4 mT (see also SI), can be associated with a chaotic billboard of Andreev-pair trajectories" (p. 5) | Run the Dynes-Fulton reconstruction of Fig. S9c on Fig. 2c or Fig. S11 data, or compare with an edge (SQUID-like) pattern. |

The edge row comes from Ben Shalom et al., your Ref. [20], who attribute high-field supercurrent in ballistic graphene to Andreev states near the edges, and from Indolese et al., who find edge supercurrent in a graphene/hBN superlattice at the van Hove singularities, where the bulk Fermi velocity drops. That second mechanism is specific to moiré bands, so your non-moiré control (Fig. S15) doesn't separate it from your bulk picture. A current-density profile from data you already have would.

On the series resistance: your zero-resistance pockets and the 1/R map in Fig. 3e both rest on the 3447 Ω subtraction. Your Fig. 2b and 2c show a flat zero-voltage branch and Ic oscillations, which help a lot; a reader will still want the raw two-probe trace and the calibration, because the edges of the pockets in Fig. 3e and Fig. S18 move with that number.

## Questions about devices and data

1. How many devices did you measure, and how many showed the high-field supercurrent? Your SI answers this for devices (GH1 and GH2 of GH1 to GH4, plus one non-moiré junction, SI pp. 33 and 34); could you add the number of cooldowns and datasets, and square it with "multiple additional devices" on p. 3?
2. Why were the others set aside? Your SI gives junction length as the reason for GH3 and GH4 (SI p. 33). Were other junctions on these stacks fabricated and not measured, and what made GH1 the main device?
3. Which ranges of density, field and temperature did you measure beyond those in Fig. 2a and Fig. S13a, and at which densities besides n/ns ∼ 1.8 (GH1) and n/ns = 1.6 (GH2) did you take high-field interference patterns?
4. What does the second-best dataset look like? GH2 (SI Section F) answers this at the device level; could you also show a high-field pocket of GH1 from another density range, for example near n/ns ∼ 2.2 or below 1.5?
5. How was the 3447 Ω series resistance obtained (SI p. 19), was it checked at high field and in each cooldown, and could you show Fig. 2a before subtraction, together with the threshold that marks a region as superconducting in Fig. 3e and the 20 mS cutoff of Fig. S18?
6. Could you reconstruct the current density across the width, as in Fig. S9c, from a high-field pattern such as Fig. 2c or Fig. S11, to tell bulk trajectories from Andreev states near the edges?
7. Two numbers disagree with others in the text: the single-mode limit reads IQ = e∆/h ∼ 106 ± 2 nA on p. 5 and ∼ 53 ± 1 nA on SI p. 31 (with ∆ ∼ 1.4 meV, e∆/h is about 54 nA), and SI p. 20 gives n/ns ∼ ±2.7 at 6.0 × 10^12 cm^-2, while your moiré formula with θ = 0.21° gives ns ≈ 2.5 × 10^12 cm^-2 and so n/ns ≈ 2.4. Which values are right, and which IQ did you compare with the 48 ± 2 nA of Fig. 2b?

## Related work

- Ben Shalom et al. 2015, "Quantum oscillations of the critical current and high-field superconducting proximity in ballistic graphene", <https://arxiv.org/abs/1504.03286>. Ballistic graphene junctions where supercurrent pockets appear and vanish with field and density above 1 T, attributed to mesoscopic Andreev states near the edges.
- Indolese et al. 2018, "Signatures of van Hove singularities probed by the supercurrent in a graphene - hBN superlattice", <https://arxiv.org/abs/1805.10184>. A graphene/hBN superlattice junction whose field dependence shows edge supercurrent at the van Hove singularities.
- Amet et al. 2015, "Supercurrent in the quantum Hall regime", <https://arxiv.org/abs/1512.09083>. Supercurrent through a graphene quantum Hall region at fields up to 2 T.
- Vignaud et al. 2023, "Evidence for chiral supercurrent in quantum Hall Josephson junctions", <https://arxiv.org/abs/2305.01766>. Chiral edge supercurrent up to 8 T with a regular 2φ0 periodicity on a quantum Hall plateau.
- Barrier et al. 2024, "One-dimensional proximity superconductivity in the quantum Hall regime", <https://arxiv.org/abs/2402.14451>. Domain walls in minimally twisted bilayer graphene carry a non-oscillating supercurrent up to fields near the electrodes' upper critical field.

Happy to rerun this if you share the figure data.
