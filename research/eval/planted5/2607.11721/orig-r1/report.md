# Lookalike check: High-field Josephson effect in moiré graphene (arXiv 2607.11721v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper reports a non-topological supercurrent, so I adapted the library's supercurrent, series-resistance and data-window entries and added two explanations from the graphene Josephson literature that the library lacks.

**The claim, as I read it.** In ballistic graphene/hBN moiré Josephson junctions, pockets of zero resistance with oscillating critical current survive up to about 6 T once the Fermi level enters the moiré minibands (Fig. 2a-c, e; device GH1, with GH2 in Fig. S13), well beyond the 2rc = L limit that bounds them in the main Dirac band and in a non-moiré control junction (Fig. S15). You link these pockets to dispersive Hofstadter bands by comparing the zero-bias 1/R map with calculated ⟨v²⟩/vF² (Fig. 3c-e).

## Checks a careful reader will look for

The library has no checks for the supercurrent family, so only the practice checks apply.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "No high field superconductivity nor clear Fabry-Pérot oscillations were observed for the other two devices GH3 and GH4." (SI F, p. 33). Devices are counted in Table S1; datasets and cooldowns are not.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "The maximum voltage we can typically apply in our devices with the Si gate is ± 80 V" (SI B, p. 20). No reason is given for the cuts at n/ns ∼ 1.8 and 4.3 T.
3. Give the processing steps from raw data to figures, with data and code : Partly. "a finite known in-series resistance of 3447 Ω was subtracted from the data" (SI A.2, p. 19); the Ic criterion and the Fabry-Pérot background fits are described (SI C, p. 22-23), and data are "available from the corresponding author upon reasonable request" (p. 16), with no code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and datasets counted: part; how shown data were chosen: no; second device shown: all | "No high field superconductivity nor clear Fabry-Pérot oscillations were observed for the other two devices GH3 and GH4." (SI F, p. 33) | Count datasets and cooldowns, and say why n/ns ∼ 1.8 and 4.3 T were picked for Fig. 2b-c. |
| Series resistance subtraction (adapted: zero resistance in a two-probe map) | Not tested (data bear on it) | Calibrated independently, with value: no; raw data before subtraction: no | "In measurements with a two-probe scheme, a finite known in-series resistance of 3447 Ω was subtracted from the data." (SI A.2, p. 19) | Show raw two-probe R for Fig. 2a and redraw Fig. 3e with the resistance moved by ±50 Ω. |
| Field-moved finite-bias resonances changing the switching current (adapted) | Tested in part | Finite-bias dV/dI with switching current: part; across gate and other devices: all | "dV /dI map vs I and vs n/ns at B = 4.1 T, where superconducting pockets with oscillating Ic are observed." (Fig. 2e, p. 10) | Plot full-range dV/dI vs I and B at a pocket and mark any resonance next to Ic. |
| Data-window and threshold choices (adapted from protocol sensitivity) | Tested in part | Code and data published: no; reason for each range: part; rerun with ranges varied: no | "The lower and upper colorbar limits correspond to the limits imposed by the Thouless energy." (Fig. 3d, p. 11) | Rerun the Fig. 3d-e comparison for several 1/R cutoffs and ⟨v²⟩ levels. |
| Chiral quantum Hall edge supercurrent (not in library) | Ruled out for the claim | Normal-state fan vs pockets: all; Ic size and period vs chiral form: part | "The absence of these LLs proves that the superconducting proximity effect in our JJs does not occur in the quantum Hal regime." (SI G, p. 33, Fig. S14) | None needed. |
| Edge-localized high-field Andreev states (not in library) | Not tested (data bear on it) | Jc(x) at high field: no; edge vs bulk interference form at high field: no | "The agreement with the standard Fraunhofer pattern confirms a uniform supercurrent distribution across the device." (p. 3, Fig. 1g; near zero field only) | Run the Dynes-Fulton analysis of Fig. S9 on Fig. 2c and Fig. S11. |

A few notes on the table. The chiral edge row is ruled out by one test that separates it by itself: Fig. S14 shows no Landau levels at 200 nA where the pockets sit, in both GH1 and GH2, and a chiral edge supercurrent needs a quantum Hall plateau. Your Ic of ∼48 nA and the irregular periods (p. 5) add to that.

The edge-localized row comes from Ben Shalom et al., who saw random high-field pockets with Ic near the quantum limit in plain ballistic graphene and placed them near the edges, and from Indolese et al., who found edge supercurrent at the van Hove singularities of a graphene/hBN superlattice. Your non-moiré control (Fig. S15) bears on the first. A Jc(x) profile at the high-field pockets would speak to both.

For the series resistance, a 20 mS cutoff on 1/R (Fig. S18) is a residual of 50 Ω on top of 3447 Ω. So the outline of the "superconducting regions" in Fig. 3e depends on how well that value is known. The switching traces in Fig. 2b already show nonlinear dV/dI, which helps; the map is where the subtraction matters most.

## Questions about devices and data

1. How many devices did you measure, and how many showed high-field supercurrent? Table S1 and Section F list GH1 to GH4 plus one non-moiré junction, with GH1 and GH2 showing the effect; could you also give the number of junctions per chip (Fig. S1a shows several contacts on one mesa) and of cooldowns, and say whether "multiple additional devices" (p. 3) means more than GH2?
2. Why were the others set aside? You give a reason for GH3 and GH4 (SI F, p. 33); were any other junctions fabricated or measured and not reported?
3. Which ranges did you measure beyond the ones shown, in particular the hole-side minibands (n/ns < −1) at high field, the full field range of Fig. 2a, and negative fields?
4. What does the second-best dataset look like? GH2 appears in Fig. S13; how do interference patterns in GH1 at densities other than n/ns ∼ 1.8 compare with Fig. 2c and Fig. S11?
5. How was the 3447 Ω series resistance (SI A.2, p. 19) calibrated, and how much do the pockets in Fig. 2a and the 1/R map with its 20 mS cutoff (Fig. 3e, Fig. S18) change if that value moves by a few tens of ohms?
6. Do the dV/dI vs I maps at high field, over the full current range, show finite-bias resonances (multiple Andreev reflection or self-induced steps), and do they move with field together with the switching current?
7. Could you extract Jc(x) from the high-field interference patterns (Fig. 2c, Fig. S11), as you did near zero field in Fig. S9, to show whether the high-field supercurrent flows through the bulk or near the edges?
8. Does the normal-state map taken at 200 nA (Fig. S14) show the same correlation with ⟨v²⟩/vF² as the zero-bias 1/R map in Fig. 3e, and how were the 20 mS cutoff and the ⟨v²⟩/vF² > 0.1 level chosen?

## Related work

- Ben Shalom et al. 2016, "Quantum oscillations of the critical current and high-field superconducting proximity in ballistic graphene", <https://arxiv.org/abs/1504.03286>. In ballistic graphene junctions some proximity survives above 1 T, appearing and vanishing randomly with field and density with Ic near the quantum limit, attributed to mesoscopic Andreev states near the edges.
- Indolese et al. 2018, "Signatures of van Hove singularities probed by the supercurrent in a graphene - hBN superlattice", <https://arxiv.org/abs/1805.10184>. In a graphene/hBN superlattice junction, the field dependence of the supercurrent shows edge currents at the van Hove singularities.
- Amet et al. 2016, "Supercurrent in the quantum Hall regime", <https://arxiv.org/abs/1512.09083>. Supercurrent through a graphene quantum Hall weak link at fields up to 2 T.
- Vignaud et al. 2023, "Evidence for chiral supercurrent in quantum Hall Josephson junctions", <https://arxiv.org/abs/2305.01766>. Chiral supercurrent on a quantum Hall plateau up to 8 T in narrow graphene junctions, with a 2ϕ0 oscillation period at constant filling.
- Barrier et al. 2024, "One-dimensional proximity superconductivity in the quantum Hall regime", <https://arxiv.org/abs/2402.14451>. Domain walls in minimally twisted bilayer graphene carry a non-oscillatory supercurrent at quantizing fields close to the electrodes' upper critical field.

Happy to rerun this if you share the raw two-probe data and the high-field interference maps.
