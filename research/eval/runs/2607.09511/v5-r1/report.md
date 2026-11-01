# Lookalike check: Majorana parity qubit in coupled minimal Kitaev chains (arXiv 2607.09511v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your evidence is time-domain qubit data, not transport, so I used the library's Kitaev-chain and practice entries and adapted two zero-bias entries (quasi-Majoranas and the local-probe loophole) to a parity qubit read out by quantum capacitance.

**The claim, as I read it.** In one InSb nanowire device with two two-site Kitaev chains joined by a coupler dot, you report coherent parity oscillations between |ee⟩ and |oo⟩ (Fig. 2a-d), suppressed near φ = π (Fig. 2e), with matching frequencies in the even and odd manifolds at the sweet spot (Fig. 3a,b,h: 113.4 and 117.7 MHz), and a detuning response that follows the partial protection of poor man's Majoranas (Fig. 3c-j, Fig. 4).

## Checks a careful reader will look for

1. Report how sweet spots were found, how many were found and kept, with the surrounding charge stability maps : Partly. You describe the procedure and show the maps (Fig. 1f,g, Fig. ED4, ED5): "Following the procedure described in Ref. [30], we tune both Kitaev chains to a Majorana sweet spot." (p. 23). The device "is retuned before each two-dimensional sweep" (p. 24), and the number of tunings tried and kept is not given.
2. Add a site or extend the chain and test whether the state survives : Not done. You name it as future work: "Future experiments with longer chains will enable direct tests of the predicted protection scaling" (p. 9).
3. Report devices and datasets measured, how many showed the effect, and why others were set aside : Partly. One device and a second cooldown are named: "The data shown in Fig. ED6 and Fig. ED9 were acquired in a different cooldown" (p. 24). The total number of devices is not given.
4. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. You give the acquisition order, the retuning fields and one range choice: "In Fig. 2 and Fig. 3, only data with VC < 11.25 mV were included in this fit" (p. 26). Measured ranges beyond the figures (other B||, temperature) are not stated.
5. Give the processing steps from raw data to figures, with data and code : Done. Methods IV to VI give thresholds, conditional probabilities and fits, and "All raw data measured on the device presented in this work at the time of writing, the data processing and plotting code" are on Zenodo (p. 9).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| False poor man's Majoranas (trivial states that pass the same local tests) | Tested in part | Chain extended or a site added: no; Microscopic model of the device: part (Eq. 5 is the ideal two-site Kitaev model with noise widths "chosen to qualitatively reproduce the experimental data", p. 28, so it cannot produce false PMMs) | "Our theoretical modeling assuming quasistatic charge noise reproduces the main observations (Fig. ED10, Fig. ED11)." (p. 9) | Place your sweet spot in a microscopic QD-ABS model (charging energy, ABS energy, g factor at 150 mT) per Luethi et al., and report the stability of the sweet spot to plunger detuning from Fig. 4a-d. |
| Quasi-Majorana states (adapted: overlapping trivial components that mimic decoupled Majoranas) | Tested in part | Bulk gap closing and reopening in nonlocal conductance: no (a two-site chain has no bulk); Correlated zero modes at both ends: part (equivalent: single-dot versus two-dot detuning, Fig. 4a-h and ED9e-l, read through total chain parity) | "quasi-Majorana states could yield a similar Hamiltonian with little unwanted Majorana coupling" (p. 29) | From Fig. 4a-d and ED9e-h, extract frequency and return probability versus single-dot detuning and compare the quadratic splitting expected for separated PMMs with the linear one for overlapping components. |
| Local-probe loophole (adapted: overlap of the Majorana components not measured) | Tested in part | Nonlocal measurement (both ends or nonlocal conductance): no (transport tune-up of Ref. [30] not shown); Overlap estimated through a quantum dot in series: part (the even/odd comparison via the coupler bounds only the product of both chains' overlaps) | "the observation of very small frequency differences in Fig. 3b strongly hints at well-decoupled Majorana states in at least one of the chains." (p. 34) | Use the time-domain data near φ ≈ π (Fig. 2e, ED6i-n), where overlap enters linearly, or detune one outer dot at a time at φ ≈ 0, to bound each chain's overlap separately. |
| Fine-tuning and selection | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part; A second device or dataset shown: part (ED9 is a second tuning of the same device, without the odd-manifold comparison) | "A successful tuning is indicated by oscillations with similar frequencies and contrast in both manifolds" (p. 23) | State how many tunings and cooldowns were tried and how many met this criterion, and show a tuning that failed it. |
| Conventional charge qubit in the same dots (not in library) | Tested in part | Same Rabi measurement in a charge-qubit configuration, coherence and visibility compared: part (reached by detuning at fixed VC = 9.8 mV, so a charge-qubit resonance at other coupler settings is not searched) | "provides a direct comparison to a conventional charge qubit [32, 33], for which no coherent oscillations are resolved under the same measurement conditions." (p. 9) | Repeat the Fig. 2a coupler sweep in the double-dot configuration of Fig. 4g,h and report T2Rabi and Q next to the sweet-spot values. |

## Questions about devices and data

1. How many devices did you fabricate and measure, and how many showed coherent parity oscillations?
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown, for example other in-plane fields than B|| = 150 mT, higher temperatures, coupler amplitudes above 11.25 mV, and longer pulse durations?
4. What does the second-best device or dataset look like? Fig. ED9 is a second tuning of the same device; is there a second device with even and odd manifolds compared?
5. Methods III says "A successful tuning is indicated by oscillations with similar frequencies and contrast in both manifolds." How many tunings did you try, and how many were set aside because the even and odd frequencies or contrasts differed?
6. Since the frequency difference in Fig. 3b bounds only the product of the two chains' overlaps, can you bound each chain separately, for example from the time-domain data near phi = pi (Fig. 2e) or by detuning one outer dot at a time?
7. For the charge-qubit comparison in Fig. 4g,h, did you sweep the coupler amplitude in the double-dot configuration, and would oscillations decaying within a few ns be resolved with your pulse timing?
8. Fig. 3h-j are described as "Separate representative measurements", and a charge jump preceded Fig. 2e: how were these traces chosen, and were any datasets set aside because of the jump or drift?

## Related work

- Luethi, Legg and Loss 2024, "Fate of poor man's Majoranas in the long Kitaev chain limit", <https://arxiv.org/abs/2408.10030>. A microscopic model shows some two-site PMMs evolve into trivial localized states in long chains, with no clear conductance signature to tell them apart.
- Luethi, Legg and Loss 2025, "Properties and prevalence of false poor man's Majoranas in two- and three-site artificial Kitaev chains", <https://arxiv.org/abs/2504.06732>. Many false PMMs trace back to zero-energy states present without superconductivity, and the most stable sweet spots sit where false PMMs are common.
- Pan, Das Sarma and Liu 2024, "Rabi and Ramsey oscillations of a Majorana qubit in a quantum dot-superconductor array", <https://arxiv.org/abs/2407.16750>. Simulates Rabi and Ramsey oscillations with charge noise and compares minimal Majorana qubits with conventional double-dot charge qubits, which also oscillate with shorter coherence.
- Tsintzis, Souto, Flensberg et al. 2023, "Roadmap towards Majorana qubits and nonabelian physics in quantum dot-based minimal Kitaev chains", <https://arxiv.org/abs/2306.16289>. Proposes coupling two PMM pairs into a qubit and measuring its coherence, with a realistic interacting, spinful dot model.
- Mishmash, Bauer, von Oppen et al. 2019, "Dephasing and leakage dynamics of noisy Majorana-based qubits: Topological versus Andreev", <https://arxiv.org/abs/1911.02582>. A time-domain protocol, via the dependence of dephasing on tunable parameters, separates a Majorana qubit from one built of semilocal Andreev states that mimic it in local probes.

Happy to rerun this if you share how many tunings and devices sit behind the figures; I could not reach the Zenodo record.
