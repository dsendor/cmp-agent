# Lookalike check: Suppressing Majorana hybridization in Cr chains on β-Bi2Pd (arXiv 2610.29446v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is STM on chains built atom by atom, so I adapted the nanowire entries: tip height stands in for barrier gates, the chain-center gap versus length for the nonlocal gap, and trivial Yu-Shiba-Rusinov end states for unintended dots.

**The claim, as I read it.** Cr chains on β-Bi2Pd show a length-driven closing and reopening of the in-gap spectrum (Cr4 to Cr12, Fig. 2(a)) and, in one Cr12 chain, zero-bias weight at both ends around a 204 ± 50 µeV gap (Fig. 4(b), Fig. S3). The electron-hole exchange (Fig. 3), the 16.8 µeV splitting and ξM ≃ 10.5 Å (Eq. 1) come from the Green-function calculation.

One note: your summary calls five items a "combined observation" (p. 4), and two of them, the electron-hole exchange and the splitting behind ξM, are calculated. Saying so in that sentence would help a reader.

## Checks a careful reader will look for

1. Look for trivial bound states at the chain ends (adapted from the dot search) : Not done.
2. Show the peak over wide parameter ranges, including where it is absent : Partly. "Spatially resolved differential-conductance maps acquired along Crx chains with x = 4, 5, 8, 12" (Fig. 2 caption, p. 3); field and tip height are not varied.
3. Measure both ends at the same settings : Done. "showing spectral weight localized near the two ends and a reduced signal in the central region" (Fig. 4(b) caption, p. 4).
4. Show the peak stays as the junction changes (adapted: tip height or setpoint) : Not done.
5. Show a gap that closes and reopens where the end peaks appear (adapted: chain-center gap versus length) : Partly. "the experimental resolution does not allow us to resolve a clear mini-gap" for Cr4, and "for Cr12 a gap centered at zero energy is recovered at the chain center" (p. 2).
6. State the background subtracted and show the raw data (adapted from series resistance) : Done. "The red curve is the full conductance clearly showing the topological gap." (Fig. S3 caption, p. S4).
7. Report devices and datasets measured, how many showed the effect, and why others were set aside : Not done.
8. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "VRF = 0.22 mV corresponds to the largest applied ac modulation" (Fig. S5 caption, p. S6); lengths beyond the four shown are not given.
9. Give the processing steps from raw data to figures, with data and code : Partly. "we subtract the dI/dV of the pristine surface from the middle of the chain dI/dV" (p. S4); no data or code.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Quasi-Majorana states from smooth confinement | Tested in part | Gap closing and reopening (equivalent: chain-center gap vs length): part; correlated zero modes at both ends: part | "for Cr12 a gap centered at zero energy is recovered at the chain center and two zero-bias resonances appear at the chain ends" (p. 2); the Cr4 gap is unresolved and the end correlation is untested. | From the Fig. 2(a) data, plot both end peaks' energy and height for every length you built, including the lengths between 5 and 12. |
| Disorder-induced zero modes | Tested in part | End-to-end correlation: part; gap closing and reopening: part; insensitivity to parameters that should not matter (tip, chain site): no | "a small variation of the local coupling to the superconducting substrate is sufficient to account for the measured asymmetry" (p. 3) | Build a second Cr12 chain in another region and compare its end imbalance and end-peak energies with Fig. 4(b). |
| Crowded trivial subgap states | Tested in part | Length range compared with the predicted range: part; subband model: part | "Calculations further predicted that chains longer than approximately eight atoms should enter a regime in which the in-gap spectrum reopens near zero energy" (p. 2); the model uses "a single compact orbital per site" (p. S1), so several YSR channels per atom are outside it. | Show how many in-gap states the single Cr adatom has here, and the full length series, so a reader can see where zero-bias weight appears and where it doesn't. |
| Trivial Andreev band mimicking gap reopening | Tested in part | Same analysis on a trivial model or device: part; parameters outside the analysis varied (field, tip height, chain direction): no | "We can see that the Rashba coupling is instrumental in closing an reopening the gap" (p. S2, Fig. S2); the length series at small αR is not shown. | Run the Fig. 2(b) length series at αR near zero, and measure a length series of 2a-spaced chains, which your earlier work found trivial on this surface. |
| End state at one end only | Ruled out for the claim | Both ends compared at the same settings: all; nonlocal conductance: no | "spectral weight localized near the two ends" (Fig. 4(b), p. 4); zero-bias weight at both ends of the same chain is enough, since this lookalike leaves the far end empty. | None needed |
| Local-probe loophole (overlap not measured) | Tested in part | Nonlocal measurement: part (both ends read, their correlation untested); overlap estimated through a dot: no (the overlap comes from the calculation) | "From the residual splitting of the calculated zero-energy mode we extract a localization length" (p. 2) | Use the atom-by-atom history: show whether the untouched end responds when atoms are added at the other end. |
| Fine-tuning and selection | Tested in part | Counts: no; how the shown data were chosen: part; second device: no | "Figure 1(c–f) shows representative Cr4, Cr5, Cr8, and Cr12 chains." and "The chains were constructed in defect-free regions" (p. 2) | A short table: chains built per length, chains that ruptured, chains that showed end modes, tips and cooldowns. |
| Trivial end states in a trivial minigap (not in library) | Tested in part | End-state energy followed after a local perturbation at one chain end, compared with the other end: part (the measured end imbalance acts as an uncontrolled perturbation); magnetic order of the chain determined: no | "a small variation of the local coupling to the superconducting substrate is sufficient to account for the measured asymmetry while preserving the zero-energy character of the end state [18, 31]" (p. 3) | Place a defect or extra atom at one end of a Cr12 chain and follow both end peaks, as in Schneider et al. (arXiv 2211.00561). |

## Questions about devices and data

1. How many chains did you assemble at each length, and how many showed the gap closing, the reopening and the end modes?
2. Why were the others set aside, for example chains that ruptured from the strain in Sec. S6?
3. Which ranges did you measure beyond the ones shown: other chain lengths, tip setpoints, magnetic field, temperature?
4. What does the second-best Cr12 chain, or the same chain with a different tip, look like?
5. You added atoms at one end only (p. 2). Does the untouched end change as atoms are added, and do the two Cr12 end peaks sit at the same bias?
6. Which Rashba coupling did you use for Figs. 2 to 4 (1.8 eV Å on p. S1, 3.6 eV Å on p. S2), and how does ξM change across that range? With your inputs to Eq. (1) I get ξM near 11 Å, and 10.5 Å is about 2.2 sites of 4.75 Å.
7. What is your energy resolution with the 30 µV lock-in excitation at 30 mK, and how was the ±50 µeV on Δtopo obtained?
8. Did you measure the magnetic order of the chains (spin-polarized tip or field dependence)? The spin texture in Fig. 3 is calculated.

## Related work

- Schneider et al. 2021, "Controlled length-dependent interaction of Majorana modes in Yu-Shiba-Rusinov chains", <https://arxiv.org/abs/2104.11503>. Mn chains on Nb, end-mode splitting measured from both ends versus length; it reaches zero within resolution only at periodic lengths.
- Schneider et al. 2022, "Testing the topological nature of end states in antiferromagnetic atomic chains on superconductors", <https://arxiv.org/abs/2211.00561>. A defect at one end splits that end state off zero while the other end stays, which rules out a Majorana origin there.
- Küster et al. 2021, "Non-Majorana modes in diluted spin chains proximitized to a superconductor", <https://arxiv.org/abs/2112.05708>. Atom-by-atom chains show ubiquitous boundary modes, identified as trivial Shiba states.
- Hess et al. 2022, "Prevalence of trivial zero-energy sub-gap states in non-uniform helical spin chains on the surface of superconductors", <https://arxiv.org/abs/2204.02324>. Theory: trivial zero-energy states in non-uniform helical chains are far less prevalent than in equivalent nanowires.
- Mier et al. 2021, "Atomic Manipulation of In-gap States on the β-Bi2Pd Superconductor", <https://arxiv.org/abs/2104.06171>. Cr chains on this surface: only the √2a-spaced chain is non-trivial, so 2a-spaced chains give a trivial control.

Happy to rerun this if you share the Fig. 2(a) maps for every chain you built.
