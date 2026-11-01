# Lookalike check: High-field Josephson effect in moiré graphene/hBN (arXiv 2607.11721v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper makes no topological claim, so I adapted the two entries that fit a supercurrent measurement and added three explanations from the graphene literature, marked "(not in library)".

**The claim, as I read it.** In device GH1 (L = 0.2 µm, θ = 0.21°), pockets of vanishing resistance with oscillating Ic persist up to about 6 T once the Fermi level enters the moiré minibands (n/ns > 1), well past the 2rc = L bound that ends them in the main Dirac band (Fig. 2a to 2c, 2e); GH2 shows the same up to 5 T (Fig. S13). You attribute this to dispersive Hofstadter bands, from the match between the measured 1/R map and the calculated ⟨v²⟩ (Fig. 3c to 3e).

## Checks a careful reader will look for

The library has no ordered checks for supercurrent claims, so these are the practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "Table S1 summarizes the main geometrical parameters of the four devices presented in this work" (SI p. 20); high-field maps appear for GH1 and GH2 only, and the number fabricated isn't given.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "in our devices we can only reach about Vg ∼ 80 V with our Si gate before it leaks" (SI p. 32) explains the density limit; the choice of the cuts at n/ns ∼ 1.8 and 4.3 T (Fig. 2c) isn't explained.
3. Give the processing steps from raw data to figures, with data and code : Partly. The Fabry-Pérot extraction is spelled out ("These are extracted by fitting the data to a fifth degree polynomial", SI p. 23); data are "available from the corresponding author upon reasonable request" (p. 16), with no code linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Selection of devices and datasets (fine-tuning-and-selection) | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: no; A second device or dataset shown: all | "This section shows data at high magnetic fields from a second device GH2" (SI p. 31, Fig. S13) | Say whether GH3 and GH4 went above 1 T, and how the Fig. 2c cut was picked. |
| Finite-bias resonances that move the switching current (field-enhanced-supercurrent-resonances, adapted) | Tested in part | Finite-bias differential resistance plotted with the switching current: part; Effect followed across gate voltage and in other devices: all | "which respectively show non-linear dV /dI characteristics in Fig. 2b" (p. 4) | Plot dV/dI against voltage out to 2Δ/e for pockets spread over Fig. 2a, including near 6 T, and check whether Ic follows a moving finite-bias peak. |
| Choice of subtracted series resistance (series-resistance-subtraction, adapted) | Not tested (data bear on it) | Series resistance calibrated independently, with its value: no; Raw data before subtraction: no | "a finite known in-series resistance of 3447 Ω was subtracted from the data" (SI p. 19) | Check 3447 Ω against the two-terminal quantum Hall plateaus in Fig. S3, and show Fig. 2a and 3e before subtraction. |
| Edge supercurrent from near-edge Andreev states (not in library) | Tested in part | Supercurrent distribution from Josephson interferometry across the densities and fields of the claim: part | "The agreement with the standard Fraunhofer pattern confirms a uniform supercurrent distribution across the device." (p. 3, Fig. 1g) | Run the Dynes-Fulton analysis of Fig. S9 as a function of n/ns through the minibands, including near the van Hove singularities. |
| Flux creep in the MoRe leads (not in library) | Tested in part | Interference pattern reproduced on repeated up and down field sweeps: part | "The top and bottom panels show two consecutive measurements at the same fields." (SI p. 30, Fig. S11) | Show an up and a down sweep for Fig. 2c and Fig. S13c, with the time between them. |
| Chiral Andreev edge states in the quantum Hall regime (not in library) | Ruled out for the claim | Normal-state map at a suppressing d.c. bias checked for plateaus under the pockets: all; Ic magnitude compared with the nA scale of edge-state supercurrent: all; Ic(B) period compared with the low-field Fraunhofer period: all | "The absence of these LLs proves that the superconducting proximity effect in our JJs does not occur in the quantum Hal regime." (SI p. 33, Fig. S14) | None needed. |

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed high-field pockets? Table S1 lists four moiré junctions, but high-field maps appear for GH1 and GH2 only. Were GH3 and GH4 taken above 1 T?
2. Why were the others set aside? If GH3 and GH4 showed no pockets, or weren't measured, could the SI say so?
3. Which ranges did you measure beyond the ones shown? In particular, did you map the hole minibands (n/ns < -1) at high field, where Fig. 1c shows Fabry-Pérot oscillations in the supercurrent?
4. What does the second-best device or dataset look like? GH2 (Fig. S13) partly answers this; how were the cuts at n/ns ∼ 1.8 and 4.3 T in Fig. 2c chosen, and do other pockets give similar Ic(B) patterns?
5. How was the 3447 Ω series resistance calibrated, does it put the two-terminal quantum Hall plateaus in Fig. S3 at h/νe², and could you show Fig. 2a before subtraction? How was the 20 mS cutoff in Fig. S18 chosen?
6. Were the patterns in Fig. 2c and Fig. S13c reproduced on up and down field sweeps, and how much time passed between repeats?
7. Have you mapped the supercurrent distribution (the Dynes-Fulton analysis of Fig. S9) as a function of n/ns through the minibands and near the van Hove singularities? GH2's high-field periods of 1.7 to 2.0 mT sit close to its zero-field period; how do you read that?
8. Fig. 3e uses base-temperature 1/R as a proxy for superconductivity. Does the normal-state map at 200 nA bias (Fig. S14) track ⟨v²⟩ in Fig. 3d in the same way, since dispersive magnetic Bloch bands also raise normal-state conductance?

## Related work

- Ben Shalom et al. 2016, "Quantum oscillations of the critical current and high-field superconducting proximity in ballistic graphene", <https://arxiv.org/abs/1504.03286>. Random pockets with Ic near the single-mode limit survive to about 1 T in ballistic graphene, attributed to near-edge Andreev states; up and down sweeps separate them from flux creep.
- Amet et al. 2016, "Supercurrent in the quantum Hall regime", <https://arxiv.org/abs/1512.09083>. A supercurrent of about 0.5 nA sits on quantum Hall plateaus near 1 T, with a regular period close to the low-field Fraunhofer period.
- Indolese et al. 2018, "Signatures of van Hove singularities probed by the supercurrent in a graphene - hBN superlattice", <https://arxiv.org/abs/1805.10184>. In a MoRe-contacted graphene/hBN superlattice junction, Josephson interferometry across the gate range finds a larger share of edge supercurrent near the van Hove singularities.
- Barrier et al. 2024, "One-dimensional proximity superconductivity in the quantum Hall regime", <https://arxiv.org/abs/2402.14451>. Domain walls in minimally twisted bilayer graphene carry a non-oscillatory supercurrent at quantizing fields.
- Krishna Kumar et al. 2018, "High-order fractal states in graphene superlattices", <https://arxiv.org/abs/1804.09476>. Delocalized magnetic Bloch states at unit fractions of the flux quantum per cell straighten electron trajectories and show up in the normal-state resistance above 100 K.

Happy to rerun this if you share the raw Fig. 2a data and the series-resistance calibration.
