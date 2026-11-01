# Lookalike check: Majorana parity qubit in coupled minimal Kitaev chains (arXiv 2607.09511v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your evidence is time-domain qubit data, so I adapted two entries written for tunneling
spectroscopy (quasi-Majoranas, the local-probe loophole) to parity oscillations.

**The claim, as I read it.** Coherent parity oscillations in both global parity manifolds of
two coupled two-site Kitaev chains in one InSb nanowire device, with frequencies that
agree to about 5% at the sweet spot (Fig. 2a,b, Fig. 3a,b,h) and that depend on coupler
detuning, flux and dot detuning as the model predicts (Fig. 2c,e, Fig. 3c-j, Fig. 4). Main
data: one cooldown at B|| = 150 mT, about 20 mK (p. 4); Fig. ED9 is from another cooldown.

## Checks a careful reader will look for

1. How sweet spots were found and how many were kept : Partly. Methods III gives the procedure, Fig. ED4 and ED5 show the maps, and "We verify this condition before every measurement presented in the main text." (p. 31). The number of tune-ups tried and kept isn't stated.
2. Extend the chain and test whether the state survives : Not done. "Future experiments with longer chains will enable direct tests of the predicted protection scaling" (p. 9).
3. Device and dataset counts : Partly. "The data shown in Fig. ED6 and Fig. ED9 were acquired in a different cooldown" (p. 24); the number of devices fabricated and measured isn't given.
4. Full parameter ranges : Partly. You give the acquisition order (p. 24) and the fit window, "only data with VC < 11.25 mV were included in this fit" (p. 26); other parallel fields, temperatures and dot orbitals aren't reported.
5. Processing from raw data to figures, with data and code : Done. "All raw data measured on the device presented in this work at the time of writing, the data processing and plotting code, and the code used for the theory calculations are available" (p. 9), with fit details in Methods VI (pp. 26-27).

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| False poor man's Majoranas (imperfect PMMs that turn into trivial states in longer chains) | Partly addressed | "a careful study of detuning individual chain parameters described by Eq. (5), as is done in the main text, is necessary to get evidence for spatial separation." (p. 29); the dot-detuning tests bear on localization, and the chain isn't extended. | Place your sweet spot on an ABS-mediated microscopic model (as in Luethi et al.) using your measured couplings, Zeeman energy and dot orbitals, and say whether it sits where false PMMs are common; compare with the Fig. ED9 orbitals. |
| Decoupled but overlapping Majorana components (quasi-Majorana entry, adapted) | Partly addressed | "quasi-Majorana states could yield a similar Hamiltonian with little unwanted Majorana coupling, despite the effective Majorana components not spatially separated in this case" (p. 29); Fig. 4a-d is your test of it. | From Fig. 4a-d and ED7a-d, extract the longitudinal splitting against single-dot detuning for each of the four dots and test whether it grows quadratically, as sweet-spot protection predicts, or linearly. |
| Local-probe loophole (adapted: one global readout and one frequency comparison) | Partly addressed | "the observation of very small frequency differences in Fig. 3b strongly hints at well-decoupled Majorana states in at least one of the chains." (p. 34) | Repeat the φ ≈ π test of Methods XI in the main cooldown, detuning the outer dot of each chain in turn in both manifolds, to bound each chain's overlap on its own (ED6i-n come from the other cooldown). |
| Fine-tuning and selection | Partly addressed | "coherent parity oscillations measured in a different tuning configuration (Fig. ED9)" (p. 8); device and tune-up counts aren't stated. | You retuned before every 2D sweep, so you could tabulate the frequency mismatch and contrast at each retuning, plus every tune-up that failed the both-manifold criterion. |
| Conventional charge qubit oscillations (not in library) | Partly addressed | "provides a direct comparison to a conventional charge qubit [32, 33], for which no coherent oscillations are resolved under the same measurement conditions" (p. 9, Fig. 4g,h); shown at one VC with 25 ns ramps, where a charge qubit with nanosecond coherence (Petersson et al.) could go unresolved. | Compare dephasing against detuning in the charge-qubit and sweet-spot configurations at matched oscillation frequency, and state the shortest coherence time your pulse scheme can resolve. |

## Questions about devices and data

1. How many devices did you fabricate and cool down, and how many showed parity oscillations at the both-manifold sweet spot? The paper presents one device and two cooldowns (pp. 9, 24).
2. Why were the others set aside, if there were others?
3. Which ranges did you measure beyond those shown: parallel fields other than 150 mT, temperatures above base, coupler amplitudes above 11.25 mV, and other dot orbitals in the main cooldown?
4. What does the second-best dataset look like? Fig. ED9 was never checked in the odd manifold (p. 24); how many retunings in the main cooldown passed the both-manifold check, and what spread of (fodd - feven)/(fodd + feven) did they give?
5. Page 8 says the even–odd degeneracy "is protected against detuning of either QD individually", and page 9 says detuning a single QD "removes the sweet spot protection and suppresses the oscillations". Could you say which you mean, and quantify the splitting against single-dot detuning?
6. Fig. 3b bounds the product of the two chains' overlaps (p. 34). Do you have φ ≈ π data in both manifolds from the main cooldown that bound each chain on its own?
7. For the charge-qubit configuration in Fig. 4g,h, what is the shortest coherence time you could have resolved with 25 ns ramps, and so what does "no coherent oscillations are resolved" bound?
8. Fig. 2e was measured after a phase jump and a charge jump that left the device with "increased instability" (p. 24). How did you check each of the nine retunings, and were the crossings in both manifolds verified at each field?

## Related work

- Luethi et al. 2025, "Properties and prevalence of false poor man's Majoranas in two- and three-site artificial Kitaev chains", <https://arxiv.org/abs/2504.06732>. In a microscopic model, the most stable two-site PMMs sit where false PMMs are common.
- Luethi et al. 2024, "Fate of poor man's Majoranas in the long Kitaev chain limit", <https://arxiv.org/abs/2408.10030>. Some PMMs become trivial states in long chains, with no conductance signature to tell them apart.
- Luethi et al. 2024, "From perfect to imperfect poor man's Majoranas in minimal Kitaev chains", <https://arxiv.org/abs/2408.03071>. In realistic models the sweet spot is only approximated, giving states that are "highly, but not perfectly, localized".
- Pan, Das Sarma and Liu 2024, "Rabi and Ramsey oscillations of a Majorana qubit in a quantum dot-superconductor array", <https://arxiv.org/abs/2407.16750>. Simulations with charge noise predict longer dephasing for larger-gap Majorana qubits than for quantum dot charge qubits.
- Petersson et al. 2010, "Quantum Coherence in a One-Electron Semiconductor Charge Qubit", <https://arxiv.org/abs/1008.3089>. A GaAs double-dot charge qubit driven by gate pulses, with coherence up to about 7 ns.

Happy to rerun this with the Zenodo data if you can share it somewhere I can reach; I couldn't open the record from here.
