# Lookalike check: Majorana parity qubit in coupled minimal Kitaev chains (arXiv 2607.09511v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper reports time-domain qubit data and the library is written for transport
signatures, so I adapted its Kitaev-chain and practice entries to Rabi oscillations and
added one ordinary explanation from outside the library.

**The claim, as I read it.** Two two-site Kitaev chains in one InSb nanowire device,
coupled through a central dot, show coherent oscillations between parity states in both
global parity manifolds (Fig. 2a, Fig. 3a), with nearly equal even and odd frequencies at
the sweet spot (Fig. 3h), a coupling that vanishes near φ = π (Fig. 2e), and a detuning
dependence that follows the partial protection of poor man's Majoranas (Fig. 3c to 3j, Fig. 4).

## Checks a careful reader will look for

1. Report how sweet spots were found, how many were found and how many were kept, with the surrounding charge stability maps : Partly. "We verify this condition before every measurement presented in the main text." (Methods IX, p. 31; maps in Fig. ED4, Fig. ED5). How many tunings were found and kept isn't stated.
2. Add a site or extend the chain and test whether the state survives : Not done. "Future experiments with longer chains will enable direct tests of the predicted protection scaling" (p. 9).
3. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "The data shown in Fig. ED6 and Fig. ED9 were acquired in a different cooldown before the measurement protocol for the global odd parity manifold had been developed." (Methods III, p. 24). One device is presented; devices fabricated or set aside aren't given.
4. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "only data with VC < 11.25 mV were included in this fit" (Methods VI, p. 26). B|| is fixed at 150 mT and temperature at base.
5. Give the processing steps from raw data to figures, with data and code : Done. "All raw data measured on the device presented in this work at the time of writing, the data processing and plotting code, and the code used for the theory calculations are available" (p. 9). I did not open the repository.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| False poor man's Majoranas (pass local tests at a two-site sweet spot, become trivial in longer chains) | Partly addressed | "Detuning one QD at a time gradually reduces oscillation visibility, with the signal decaying toward p(ee\|ee) ≈ 0.5 (Fig. 4a–d), consistent with increased dephasing and no sizable longitudinal splitting." (p. 8); the data bear on it, though the paper doesn't discuss false PMMs and Luethi et al. find local signatures can't separate them. | Place the sweet spot in a microscopic model of the hybrid segments (ABS energies behind VLH and VRH, excitation gap from the outer lines in Fig. ED5); in a later device, add a third site. |
| Fine-tuning and selection | Partly addressed | "A successful tuning is indicated by oscillations with similar frequencies and contrast in both manifolds, together with a decay of the conditional probabilities toward 0.5." (Methods III, p. 23); the procedure is disclosed, but tunings tried and rejected aren't counted, and the acceptance test overlaps the headline result. | From the raw data you released, list every tuning attempt with its even and odd frequencies, rejected ones included, and give device counts. |
| Quasi-Majorana or overlapping Majorana components (adapted from the nanowire entry) | Partly addressed | "any conclusions obtained from comparing to this effective Hamiltonian can only make statements about effectively decoupled Majorana states, but not whether these are spatially separated" (Methods VIII, p. 29); Fig. 4 and the φ ≈ π data bear on separation, and the outer versus inner dot comparison at φ ≈ π (Fig. ED6i,j) comes from the earlier cooldown. | In the main tuning at φ ≈ π, measure return probability versus pulse duration while detuning outer and inner dots separately, and fit λL and λR with Eqs. (23) to (25). |
| Ordinary charge-qubit oscillations of one electron moving between the chains (not in library) | Ruled out | "Detuning one QD in each chain (Fig. 4g,h) reduces the coupled chains to an effective double QD and provides a direct comparison to a conventional charge qubit [32, 33], for which no coherent oscillations are resolved under the same measurement conditions." (p. 9), set against the single-dot robustness of Fig. 4a to 4d. | None needed. |

## Questions about devices and data

1. How many devices did you fabricate and measure with this layout, and how many showed coherent parity oscillations? The paper presents one device.
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown, for example B|| values other than 150 mT, temperatures above base, and other dot orbitals or hybrid-segment Andreev states?
4. What does the second-best dataset look like where both parity manifolds were compared? Fig. ED9 is from an earlier cooldown without the odd-manifold check.
5. Matching even and odd frequencies is both your acceptance test for a tuning (Methods III) and a headline result: how many tunings did you try, how many passed, and what frequency differences did the rejected ones show?
6. At φ ≈ π in the main tuning, could you show the return probability versus pulse duration while detuning the outer dot and the inner dot of each chain, and fit λL and λR from Eqs. (23) to (25)? Fig. ED6i,j shows this only as pulsed charge-stability diagrams from the earlier cooldown.
7. For the odd manifold, how well does the parity-switching pulse map |eo⟩ and |oe⟩ onto the even manifold for readout, and how much of the 5% leakage in Fig. 2b comes from readout error and how much from parity switching?
8. Can you place your sweet spots relative to where Luethi et al. predict false poor man's Majoranas are common, for example with a microscopic model of the hybrid segments, or by adding a third site?

## Related work

- Luethi et al. 2024, "Fate of poor man's Majoranas in the long Kitaev chain limit", <https://arxiv.org/abs/2408.10030>. Some PMMs evolve into trivial localized states in long chains, and no clear conductance signature separates them.
- Luethi et al. 2025, "Properties and prevalence of false poor man's Majoranas in two- and three-site artificial Kitaev chains", <https://arxiv.org/abs/2504.06732>. The PMMs most stable to chemical-potential changes, with the largest gaps, sit where false PMMs are common.
- Luethi et al. 2024, "From perfect to imperfect poor man's Majoranas in minimal Kitaev chains", <https://arxiv.org/abs/2408.03071>. In realistic models the sweet-spot conditions can only be approximated, and classifying the resulting states rests on thresholds.
- Tsintzis et al. 2023, "Roadmap towards Majorana qubits and nonabelian physics in quantum dot-based minimal Kitaev chains", <https://arxiv.org/abs/2306.16289>. Proposes coupling two PMM systems into a qubit, and finds two-site chains need extra care and modified protocols.
- Pan, Das Sarma and Liu 2024, "Rabi and Ramsey oscillations of a Majorana qubit in a quantum dot-superconductor array", <https://arxiv.org/abs/2407.16750>. Simulates Rabi and Ramsey oscillations with charge noise and leakage; larger-gap Majorana qubits outperform smaller-gap ones and quantum dot charge qubits.

Happy to rerun this if you share the counts of devices and tunings, or point me to the parts of the data repository that hold them.
