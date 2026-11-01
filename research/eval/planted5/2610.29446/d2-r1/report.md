# Lookalike check: Suppressing Majorana hybridization in Cr chains on β-Bi2Pd (arXiv 2610.29446v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is STM spectroscopy of atom chains, so I adapted the nanowire entries: "both ends" means the two chain ends, "bulk gap" means the gap at the chain center, and "gates" means local knobs such as tip height or an added atom.

**The claim, as I read it.** In Cr chains built atom by atom on β-Bi2Pd, the in-gap spectrum closes near Cr5 and reopens by Cr12, with zero-bias weight at both ends (Fig. 2(a), Fig. 4(b)); with calculated electron-hole character (Fig. 3) and a calculated splitting of 16.8 µeV giving ξM ≃ 10.5 Å, you read this as a topological Shiba chain with weakly hybridized end modes. The evidence is one chain at each of four lengths.

## Checks a careful reader will look for

1. Search for trivial end states (states that split off zero and recross as length or the local environment changes) : Not done. End modes appear only at Cr12.
2. Wide ranges, including where the effect is absent : Partly. "Figure 2(a) shows the measured in-gap spectra for Cr4, Cr5, Cr8, and Cr12" (p. 2); no other lengths, fields or temperatures.
3. Both ends at the same settings : Done. "two zero-bias resonances appear at the chain ends" (p. 2, Fig. 2(a), Fig. 4(b)).
4. Stability against junction transparency (here, tip height or setpoint) : Not done.
5. Bulk gap closing and reopening where the end modes appear : Partly. Shown in local spectra across four lengths, and for Cr4 "the experimental resolution does not allow us to resolve a clear mini-gap" (p. 2).
6. Processing before the key number, with the raw curve : Done. "The blue curve is the red curve after subtraction of a dI/dV curve taken in the clean base superconductor." (Fig. S3, p. S4), with the raw red curve shown.
7. Counts of devices and datasets, and why others were set aside : Not done. "Figure 1(c–f) shows representative Cr4, Cr5, Cr8, and Cr12 chains." (p. 2)
8. Full ranges measured and why each shown range was chosen : Not done. Sec. S6 says strain "will limit the achievable length of the chain" (p. S3) without giving the lengths reached.
9. Processing from raw data to figures, with data and code : Partly. "a 30 µV excitation at 330 Hz" (p. S1) and the Fig. S3 subtraction are given; the spectroscopy setpoint and a data statement are missing.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Trivial bound states at the chain ends (adapted from unintended quantum dot) | Tested in part | Trivial-state signatures searched: no; both ends compared: all | "two zero-bias resonances appear at the chain ends" (p. 2, Fig. 2(a)) | Add one atom or a defect at one end of Cr12 and follow both end states, as in Schneider et al. 2022 |
| Quasi-Majorana from smooth confinement (adapted: smooth variation along the chain) | Tested in part | Gap closing and reopening: part; correlated modes at both ends: part | "the experimental profile in (b) displays a clear imbalance between the two edge amplitudes" (p. 3, Fig. 4(b)) | Show full bias spectra at both ends of Cr12 and of any longer chain, and how the imbalance tracks length |
| Disorder-induced zero-bias states (adapted: inhomogeneous exchange or adsorption) | Tested in part | End-to-end correlation: part; gap closing and reopening: part; insensitivity to knobs that shouldn't matter: no | "Calculated zero-energy LDOS including a weak linear variation of the local exchange coupling J." (Fig. 4(d)) | Repeat Cr12 in a second surface region or with a second tip; vary tip height |
| Crowded trivial subgap states (adapted: several YSR orbitals per Cr) | Tested in part | Range compared with prediction: all; subband model: no | "with a single compact orbital per site" (p. S1) | Say how many YSR resonances a single Cr shows and whether the model needs more than one orbital |
| State at one end only | Ruled out for the claim | Both ends compared: all; nonlocal conductance: no | "two zero-bias resonances appear at the chain ends" (p. 2); zero-bias weight at both ends separates a one-end state on its own | None needed |
| Trivial Andreev band mimicking gap reopening | Tested in part | Criteria tried on a trivial model: part; parameters outside the length series varied: no | "Together with the gap closing and reopening observed in Fig. 2, this evolution supports the assignment of the long chains to a topological Shiba-chain regime." (p. 2); "At low coupling, the spin-down structure is confined to positive-valued energies." (p. S2) | Run the length series of Fig. 2(b) at low αR and with αR = 0, and show the end modes vanish there |
| Local-probe loophole | Tested in part | Both ends probed: all; overlap measured: no | "Using the calculated splitting yields ξM ≃ 10.5 Å" (p. 3); "preventing a more precise determination of the residual offset of the edge mode from zero bias" (p. S4) | Report an upper bound on the measured end-mode offset from Fig. S1 or S4, next to the 30 µV excitation |
| Fine-tuning and selection | Not tested (not mentioned) | Counts: no; how chosen: no; second dataset: no | Not discussed. | Give the number of chains built and kept, and show a second long chain |
| Finite-size gap closing in short trivial chains (not in library) | Not tested (argued, not tested) | Invariant or longer model chains: no; end modes under added adatoms or a defect: no | "The evidence does not rely on a single zero-bias peak, but on the combined observation of a chain-length-driven gap closing and reopening, end-localized zero-energy modes, exchange of electron–hole character across the transition" (p. 4) | Compute the invariant, or extend the model to long chains, to show the Cr5 closing is a trivial-to-topological transition (Küster et al. 2022) |

## Questions about devices and data

1. How many chains did you assemble (per length, region, tip and cooldown), and how many showed the Cr12 pattern of a central gap with zero-bias weight at both ends?
2. Why were the others set aside, for example chains broken by the strain of Sec. S6?
3. Which other lengths did you measure (Cr6, Cr7, Cr9 to Cr11, beyond 12), and any spectra in field or at other temperatures?
4. What does the second-best long chain look like?
5. Which end of Cr12 received the last atoms, and does the stronger end in Fig. 4(b) follow it? Have you tried a defect or extra atom at one end while following both end states?
6. The 16.8 µeV splitting and ξM ≃ 10.5 Å are calculated. Which αR (1.8, 2.5 or 3.6 eV·Å) and mass m in Eq. (1) did you use, and how does ξM change if the model reproduces the measured 204 ± 50 µeV gap?
7. Fig. 3 (electron-hole exchange, spin texture) is calculated and the tip was non-magnetic PtIr. Could the summary mark which items are measured and which calculated, and is a spin-polarized tip possible?
8. What setpoint did the spectra in Figs. 2(a), 4(b) and S1 use, constant height or feedback re-stabilized per point, and which figure holds the microwave data called Fig. S5 in the main text and Fig. 4 in Sec. S8?

## Related work

- Schneider et al. 2021, "Controlled length-dependent interaction of Majorana modes in Yu-Shiba-Rusinov chains", <https://arxiv.org/abs/2104.11503>. Mn chains on Nb, end-mode splitting measured from both ends versus length; it reaches zero only at periodic lengths.
- Küster et al. 2022, "Non-Majorana modes in diluted spin chains proximitized to a superconductor", <https://arxiv.org/abs/2112.05708>. Zero-energy end modes in assembled chains identified as trivial Shiba states; its supplement shows a gap closing and reopening in short chains that is not a trivial-to-topological transition.
- Schneider et al. 2022, "Testing the topological nature of end states in antiferromagnetic atomic chains on superconductors", <https://arxiv.org/abs/2211.00561>. Near-zero end states in a large minigap; a defect at one end splits only that end's state off zero, ruling out a Majorana origin there.
- Hess et al. 2022, "Prevalence of trivial zero-energy sub-gap states in non-uniform helical spin chains on the surface of superconductors", <https://arxiv.org/abs/2204.02324>. Finds trivial zero-energy states far less common in non-uniform helical chains than in nanowires.
- Peng et al. 2015, "Strong localization of Majorana end states in chains of magnetic adatoms", <https://arxiv.org/abs/1412.0151>. Velocity renormalization localizes Majorana end states far below the host coherence length, the mechanism you invoke for ξM.

Happy to rerun this if you share the figure data, especially the full Cr12 map behind Fig. S1.
