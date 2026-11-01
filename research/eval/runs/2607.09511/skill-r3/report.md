# Lookalike check: Majorana parity qubit in coupled minimal Kitaev chains (arXiv 2607.09511v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your evidence is time-domain qubit data, so I adapted the library's Kitaev chain and local-probe entries from transport signatures to parity oscillations.

**The claim, as I read it.** In one InSb nanowire device with two two-site Kitaev chains and a coupler dot, you report coherent parity oscillations in both global parity manifolds (Fig. 2a,b; Fig. 3a) that match in frequency at the sweet spot (Fig. 3b,h), are suppressed near φ = π (Fig. 2e), and respond to dot detuning as poor man's Majoranas predict (Fig. 4), read as a qubit encoded in Majorana parity.

## Checks a careful reader will look for

1. How sweet spots were found, and how many were found and kept : Partly. You show the maps and the criterion: "We verify this condition before every measurement presented in the main text." (p. 31, Methods IX). The number of sweet spots found and kept isn't given.
2. Extend the chain and test whether the state survives : Not done. You name it as future work: "Future experiments with longer chains will enable direct tests of the predicted protection scaling" (p. 9).
3. Devices and datasets measured, and how many showed the effect : Partly. Datasets are traced to cooldowns: "The data shown in Fig. ED6 and Fig. ED9 were acquired in a different cooldown before the measurement protocol for the global odd parity manifold had been developed." (p. 24). The number of devices fabricated and measured isn't stated.
4. Full parameter ranges, and why each shown range was chosen : Partly. You give the acquisition order: "The measurements are acquired in the following order" (p. 24). The parallel field appears only at 150 mT and the temperature only at base.
5. Processing from raw data to figures, with data and code : Done. "All raw data measured on the device presented in this work at the time of writing, the data processing and plotting code, and the code used for the theory calculations are available at https://zenodo.org/records/21280458." (p. 9), with fit details in Methods VI. I couldn't open the record.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| False poor man's Majoranas: states that pass the sweet-spot tests in two sites and become trivial localized states in longer chains | Partly addressed | "Hence, the observation of very small frequency differences in Fig. 3b strongly hints at well-decoupled Majorana states in at least one of the chains." (p. 34, Methods XI) | Place your device's settings on a microscopic map of true and false PMMs (Luethi et al.), then add a third site; partly, because the chain is not extended. |
| Overlapping Majorana components that look decoupled in an effective description (adapted from the local-probe loophole) | Partly addressed | "any conclusions obtained from comparing to this effective Hamiltonian can only make statements about effectively decoupled Majorana states, but not whether these are spatially separated" (p. 29, Methods VIII) | Use φ ≈ π data in the main cooldown, where Methods XI says the overlap enters linearly, to bound each chain's outer-dot overlap separately. |
| Selection of a fine-tuned, non-representative example | Partly addressed | "Note that for this dataset, the chains were tuned using pulsed charge-stability diagrams but were not compared to the odd manifold." (p. 19, Fig. ED9) | State how many tunings and cooldowns gave oscillations, and show a second sweet spot with the full even and odd comparison. |
| Conventional charge-qubit oscillations in coupled dots (not in library) | Partly addressed | "provides a direct comparison to a conventional charge qubit [32, 33], for which no coherent oscillations are resolved under the same measurement conditions." (p. 9, Fig. 4g,h) | Bring the effective double dot to its own charge degeneracy and report its T2 and quality factor next to Fig. 2d (Petersson et al.; Pan et al.); partly, because the comparison is one configuration with no extracted numbers. |

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed coherent parity oscillations? The paper presents one device, in at least two cooldowns.
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown: other values or directions of the parallel field than 150 mT, higher temperatures, and hybrid-gate and dot detunings wider than in Fig. 3c-g and Fig. 4?
4. What does the second-best device or dataset look like? Fig. ED9 lacks the odd-manifold check; how many sweet spots did you find, and did any other pass the even and odd comparison?
5. Methods XI says the frequency difference in Fig. 3b depends on the product of both chains' overlaps. Can you bound each chain's overlap separately, for example from φ ≈ π data in the main cooldown?
6. How is "about 5%" defined for Fig. 3b, which VC points fall outside it, and was each even and odd pair measured right after the same retuning?
7. Fig. 2e follows a charge jump "after which the device displayed increased instability" (p. 24). Which other figures came after it, and does Fig. ED7o, taken before, show the same suppression near φ = π after the 2.5 mT shift?
8. For the charge-qubit comparison in Fig. 4g,h, what coherence time and frequency do you find for the effective double dot at its own charge degeneracy, with the same pulses and readout?

## Related work

- Luethi, Legg and Loss 2024, "Fate of poor man's Majoranas in the long Kitaev chain limit", <https://arxiv.org/abs/2408.10030>. Some poor man's Majoranas become trivial localized states as the chain grows, and no conductance signature tells the two kinds apart.
- Luethi, Legg and Loss 2025, "Properties and prevalence of false poor man's Majoranas in two- and three-site artificial Kitaev chains", <https://arxiv.org/abs/2504.06732>. The PMMs most stable to chemical-potential changes sit where false PMMs are common, which bears on reading Fig. 4 as protection.
- Tsintzis et al. 2023, "Roadmap towards Majorana qubits and nonabelian physics in quantum dot-based minimal Kitaev chains", <https://arxiv.org/abs/2306.16289>. Proposes the two-chain qubit and its coherence measurement, and notes it needs modified protocols.
- Pan, Das Sarma and Liu 2024, "Rabi and Ramsey oscillations of a Majorana qubit in a quantum dot-superconductor array", <https://arxiv.org/abs/2407.16750>. Simulates Rabi and Ramsey oscillations with charge noise and compares the Majorana qubit with conventional charge qubits.
- Petersson et al. 2010, "Quantum Coherence in a One-Electron Semiconductor Charge Qubit", <https://arxiv.org/abs/1008.3089>. Pulse-driven coherent charge oscillations in a GaAs double dot, coherence up to about 7 ns: the ordinary baseline for your Fig. 4g,h.

Happy to rerun this if you share the figure data or a reachable copy of the Zenodo record.
