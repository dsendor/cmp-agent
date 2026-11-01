# Lookalike check: Majorana parity qubit in coupled minimal Kitaev chains (arXiv 2607.09511v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your evidence is time-domain qubit data, so I adapted the Kitaev-chain and practice entries, written for transport signatures, to parity oscillations.

**The claim, as I read it.** Two two-site Kitaev chains in one InSb nanowire, coupled through a quantum dot, show coherent oscillations between |ee⟩ and |oo⟩ and between |eo⟩ and |oe⟩, with nearly equal frequencies in both global parity manifolds at the sweet spot (Fig. 2a, Fig. 3a,b,h), a coupling that vanishes near φ = π (Fig. 2e), and detuning patterns matching the partial protection of poor man's Majoranas (Fig. 3c-j, Fig. 4).

## Checks a careful reader will look for

1. Report how sweet spots were found, how many were found, and how many were kept, with the surrounding charge stability maps : Partly. "We verify this condition before every measurement presented in the main text" (p. 31; Fig. 1f,g, Fig. ED4, Fig. ED5). How many sweet spots you found, tried and kept isn't stated.
2. Add a site or extend the chain and test whether the state survives : Not done. You name it as the next step: "Future experiments with longer chains will enable direct tests of the predicted protection scaling" (p. 9).
3. Report devices and datasets measured, how many showed the effect, and why the others were set aside : Partly. "All raw data measured on the device presented in this work at the time of writing" are released (p. 9), which covers this device; other devices aren't mentioned.
4. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. For example, "only data with VC < 11.25 mV were included in this fit, as the oscillations become too rapid at higher pulse amplitudes" (p. 26). B|| stays at 150 mT (p. 4), with no other values.
5. Give the processing steps from raw data to figures, with data and code : Done. Fit model and settings (Methods VI, p. 26), thresholds "obtained by fitting a Gaussian mixture model" (Fig. ED3, p. 13), virtual-gate corrections (Methods V, p. 25), and "the data processing and plotting code" on Zenodo (p. 9).

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| False poor man's Majoranas: sweet-spot states that pass two-site tests and turn trivial in longer chains | Tested in part | Chain extended or a site added: no; Microscopic model of the device: part (the Eq. 5 model takes t and Δ as inputs and leaves out the spinful, interacting levels where Luethi et al. find false PMMs) | "Our theoretical modeling assuming quasistatic charge noise reproduces the main observations (Fig. ED10, Fig. ED11)." (p. 9) | With your transport tune-up data, place the sweet spot in a spinful, interacting dot model (Zeeman, charging and Andreev bound state energies); on a next device, add a third site. |
| Overlapping Majorana components read as separated ones (local-probe loophole, adapted; covers quasi-Majoranas) | Tested in part | Nonlocal measurement: part (each chain's parity is read as a whole; Fig. 4 detunes every site, but no measurement resolves the Majorana weight at each end); Overlap estimated through a dot in series: part (the even/odd frequency match through QDC bounds only the product λLλR, per Eq. 22, and is absent for Fig. ED9) | "For example, quasi-Majorana states could yield a similar Hamiltonian with little unwanted Majorana coupling, despite the effective Majorana components not spatially separated in this case [49]." (p. 29) | Fit the φ ≈ π data you already have (Fig. 2e, Fig. ED6i-n) with Eqs. 23-24 to bound λL and λR one at a time; repeat the even/odd comparison for the Fig. ED9 tuning. |
| Selection from many tunings (fine-tuning and selection) | Tested in part | Devices and datasets measured, and how many showed the effect: part; How the shown data were chosen: part (measurement order on p. 24; Fig. 3h-j called "representative", p. 6); A second device or dataset shown: part (second cooldown, same device) | "The data shown in Fig. ED6 and Fig. ED9 were acquired in a different cooldown before the measurement protocol for the global odd parity manifold had been developed." (p. 24) | State devices fabricated, cooled and measured, and sweet-spot attempts per cooldown; show the second-best main-cooldown tuning in both manifolds. |
| Ordinary double-dot charge qubit (not in library) | Ruled out for the claim | Same Rabi experiment in a charge-qubit configuration, compared: all (Fig. 4g,h; Fig. ED9k,l); Dephasing time and quality factor reported: part (Fig. 2d, Fig. ED7n, Fig. ED8i; Fig. ED9 not fitted) | "Detuning one QD in each chain (Fig. 4g,h) reduces the coupled chains to an effective double QD and provides a direct comparison to a conventional charge qubit [32, 33], for which no coherent oscillations are resolved under the same measurement conditions." (p. 9) | None needed: the double-dot comparison is enough by itself, since the same dots set up as a charge qubit show no resolved oscillations under the same conditions. |

## Questions about devices and data

1. How many devices did you fabricate and cool down, how many reached a sweet spot in both chains, and how many showed coherent parity oscillations?
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown, for example B|| other than 150 mT, hybrid-gate detuning beyond the 0.5 mV windows of Fig. 3d-g, and pulse durations beyond 80 ns?
4. What does the second-best tuning in the main cooldown look like in both parity manifolds?
5. How many sweet spots (QD orbitals and Andreev bound state configurations) did you find and try in each cooldown, and how many gave matching even and odd frequencies?
6. What are the Zeeman, charging and Andreev bound state energies at the sweet spot, so a reader can place it in the microscopic models where false poor man's Majoranas appear?
7. The even and odd frequencies "typically agree" to about 5% (p. 6): over how many tunings, and can the φ ≈ π data (Fig. 2e, Fig. ED6i-n) bound λL and λR separately?
8. Fig. 2e followed "a charge jump" and "increased instability" (p. 24), with retuning at nine fields: were any sweeps repeated or set aside, and how does it compare with Fig. ED7o?

## Related work

- Luethi et al. 2024, "Fate of poor man's Majoranas in the long Kitaev chain limit", <https://arxiv.org/abs/2408.10030>. Some two-site PMMs evolve into trivial localized states in long chains, and no conductance signature tells them apart.
- Luethi et al. 2025, "Properties and prevalence of false poor man's Majoranas in two- and three-site artificial Kitaev chains", <https://arxiv.org/abs/2504.06732>. The PMMs most stable to chemical-potential changes and with the largest gaps sit where false PMMs are common.
- Tsintzis et al. 2023, "Roadmap towards Majorana qubits and nonabelian physics in quantum dot-based minimal Kitaev chains", <https://arxiv.org/abs/2306.16289>. Proposes the coupled-PMM qubit and the even/odd frequency difference as "a time-domain measurement of the Majorana quality" (p. 13), and notes that a coherence measurement on its own "is not sensitive to ζ" (p. 13).
- Pan, Das Sarma and Liu 2024, "Rabi and Ramsey oscillations of a Majorana qubit in a quantum dot-superconductor array", <https://arxiv.org/abs/2407.16750>. Compares simulated Majorana qubits with a charge qubit; the system "is equivalent to semiconductor charge qubits if all superconductivity is removed from considerations" (p. 5).
- Samuelson et al. 2025, "Quantifying robustness and locality of Majorana bound states in interacting systems", <https://arxiv.org/abs/2510.20538>. Shows how the locality of many-body Majorana bound states limits their coupling to an environment.

Happy to rerun this with the Zenodo files; I couldn't reach the record, so the counts come from the paper alone.
