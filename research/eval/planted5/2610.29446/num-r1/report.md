# Lookalike check: Majorana hybridization in Cr chains on β-Bi2Pd (arXiv 2610.29446v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is scanning tunnelling spectroscopy of atom-by-atom chains, so I adapted
the nanowire entries: chain length stands in for the gate or field sweep, the chain center
for the nonlocal bulk-gap measurement, and tip height for junction transparency.

**The claim, as I read it.** Cr chains on β-Bi2Pd show a chain-length-driven closing and
reopening of the in-gap spectrum (Fig. 2(a), Cr4, Cr5, Cr8, Cr12), followed by zero-bias
modes at both ends of a Cr12 chain (Fig. 4(b), Fig. S1) inside a reopened gap of
204 ± 50 µeV (Fig. S3). A Green-function calculation (Figs. 2(b), 3, 4(c,d)) reproduces
the evolution and, from a calculated splitting of 16.8 µeV, gives ξM ≃ 10.5 Å.

## Checks a careful reader will look for

1. Look for trivial bound states (adapted: end peaks that split and recross as the chain grows) : Partly. "Figure 2(a) shows the measured in-gap spectra for Cr4, Cr5, Cr8, and Cr12." (p. 2); zero-bias end modes appear only at Cr12, so their energy over neighbouring lengths isn't shown.
2. Show the peak over wide ranges, including where it is absent : Partly. The length series shows where end modes are absent (Fig. 2(a)); there is no magnetic-field or tip-height dependence.
3. Compare both ends at the same settings : Done. "spectral weight localized near the two ends and a reduced signal in the central region" (Fig. 4(b) caption, p. 4).
4. Show the peak stays as the junction transparency changes (adapted: tip height or setpoint) : Not done.
5. Bulk gap that closes and reopens where the end peaks appear (adapted: chain center versus length) : Done, with length as the tuning parameter. "for Cr12 a gap centered at zero energy is recovered at the chain center and two zero-bias resonances appear at the chain ends" (p. 2).
6. Processing from raw conductance (adapted: no series resistance in STM; substrate subtraction) : Done. "The red curve is the full conductance clearly showing the topological gap." (Fig. S3, p. S4).
7. Report devices and datasets measured, how many showed the effect, and why others were set aside : Not done.
8. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. "Conductance spectra were acquired with a lock-in amplifier using a 30 µV excitation at 330 Hz." (p. S1); spectroscopy setpoints and unshown lengths aren't given.
9. Give the processing steps from raw data to figures, with data and code : Partly. Sec. S7 describes the subtraction and Sec. S2 the model parameters; I found no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Trivial Andreev or YSR end states (adapted from abs-quantum-dot) | Tested in part | Trivial-state signatures (end peaks that split and recross with length): part; zero-bias state at both ends: all | "Zero-bias end states can also arise from trivial Andreev or YSR bound states [14–18]" (p. 1); four lengths shown, end modes only at Cr12 | Plot end-state energy for Cr9 to Cr11 and Cr13; in a mirror-symmetric chain trivial states also appear at both ends |
| Quasi-Majorana states from smooth confinement | Tested in part | Gap closing and reopening (chain center versus length, equivalent): part; correlated zero modes at both ends: part | "the asymmetry originates from a local or slowly varying microscopic perturbation that modifies the spatial distribution of the end-mode spectral weight without removing the zero-energy state [31]" (p. 3) | In the Fig. 4(d) model with the J gradient, report the splitting and the Majorana polarization at each end |
| Disorder-induced zero-energy states | Tested in part | End-to-end correlation: part; gap closing and reopening: part; insensitivity to local perturbations (adapted from gates): no | "a small variation of the local coupling to the superconducting substrate is sufficient to account for the measured asymmetry while preserving the zero-energy character of the end state [18, 31]" (p. 3) | Run the model over random site-to-site J and U variations of a few percent and report how often trivial zero-energy end states appear |
| Trivial Andreev band mimicking gap reopening | Tested in part | Criteria tested on trivial models: part (Fig. S2 αR series, no invariant); parameters outside the criteria varied: no | "The critical value of the Rashba coupling is difficult to determine from these calculations." (Sec. S4, p. S2) | Compute a topological invariant for the Fig. S2 couplings and show the length series for a set you consider trivial |
| State at one end only | Ruled out for the claim | Both ends compared at the same settings: all; nonlocal conductance: no | "showing spectral weight localized near the two ends" (Fig. 4(b), p. 4); the two-end profile alone separates a one-end state | None needed |
| Local-probe loophole (overlapping Majorana components) | Tested in part | Both ends measured: all; overlap estimated: no | "preventing a more precise determination of the residual offset of the edge mode from zero bias [39, 41]" (Sec. S8, p. S4) | Resolve the end-mode splitting in experiment at both ends, with a lock-in excitation below 30 µV |
| Kondo resonance on the magnetic adatoms (adapted) | Not tested (not mentioned) | Even-odd occupancy: no; temperature dependence: no; Zeeman splitting in field: no | Not discussed. | A temperature or small-field series at a chain end with the same tip |
| Fine-tuning and selection | Not tested (not mentioned) | Chains built, measured and showing the effect: no; how shown data were chosen: no; second chain shown: no | Fig. 1 shows "representative Cr4, Cr5, Cr8, and Cr12 chains" (p. 2); no counts | State how many chains of each length were built, measured and broke, and show a second Cr12 |
| Trivial end states that react to a local perturbation at one end (not in library) | Not tested (data bear on it) | Defect placed at one end, both end states followed in energy: no | "the experimental profile in (b) displays a clear imbalance between the two edge amplitudes" (p. 3) | Compare the two end-state energies in Fig. S1(a), then add a defect at one end of a Cr12 and follow both ends, per Schneider et al. |

## Questions about devices and data

1. How many chains did you build and measure at each length, and how many Cr12 chains showed zero-bias end modes? Is the Cr4 to Cr12 series one chain grown atom by atom, or separate chains?
2. Why were the others set aside? Sec. S6 mentions "stacking fault and rupture of the spin chains" as length increases; how many chains broke, and at which length?
3. Which chain lengths, bias ranges, setpoints and tips did you measure beyond the ones shown, for example Cr6, Cr7, Cr9 to Cr11, or chains longer than Cr12?
4. What does the second-best Cr12 chain, or the next-longest chain with end modes, look like?
5. The main text gives "L = 12 × 4.75 = 114 Å" (p. 3) and Sec. S5 gives "L = 12 × 4.75 = 57 Å" (p. S3). Which value gives ξM ≃ 10.5 Å? With 57 Å and cos(kF L) = 1 I get about 11 Å, and with 114 Å about 24 Å. And since 10.5 Å is about 2.2 spacings of 4.75 Å, how did you count "three lattice sites"?
6. Which Rashba coupling did Figs. 2(b), 3 and 4 use: "αR ≈ 1.8 eV·Å" (p. S1) or "αR = 3.6 eV-Å" (p. S2)? Which one gives the 16.8 µeV splitting?
7. In Fig. S1(a), does the weaker end state sit at the same bias as the stronger one within your resolution, and is a deliberate defect at one end feasible?
8. Is the "Cr ∗ 12" chain of the RF measurement (p. 4) the same chain as in Fig. 4, and what does the asterisk mark?

## Related work

- Schneider et al. 2021, "Controlled length-dependent interaction of Majorana modes in Yu-Shiba-Rusinov chains", <https://arxiv.org/abs/2104.11503>. Measures the end-mode splitting at both ends of Mn chains on Nb as atoms are added and finds lengths where it vanishes within resolution.
- Schneider et al. 2022, "Testing the topological nature of end states in antiferromagnetic atomic chains on superconductors", <https://arxiv.org/abs/2211.00561>. Places a defect at one chain end; the end state on that side splits off zero energy while the other stays, which rules out a Majorana origin.
- Küster et al. 2021, "Non-Majorana modes in diluted spin chains proximitized to a superconductor", <https://arxiv.org/abs/2112.05708>. Atom-by-atom chains show ubiquitous end modes that mimic Majorana signatures and are identified as trivial Shiba states.
- Hess et al. 2022, "Prevalence of trivial zero-energy sub-gap states in non-uniform helical spin chains on the surface of superconductors", <https://arxiv.org/abs/2204.02324>. Non-uniform helical chains host near-zero trivial states for some profiles, far less often than equivalent nanowires.
- Peng et al. 2014, "Strong localization of Majorana end states in chains of magnetic adatoms", <https://arxiv.org/abs/1412.0151>. Velocity renormalization localizes Majorana end states far below the host coherence length, the mechanism you invoke for ξM.

Happy to rerun this if you share the figure data or the model code.
