# Lookalike check: Suppressing Majorana Hybridization in Atomically Assembled Cr Chains on β-Bi2Pd (arXiv 2610.29446v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library is written for transport in hybrid nanowires, and your paper is scanning tunnelling spectroscopy of chains built atom by atom, so I adapted the zero-bias and gap-reopening entries: the two chain ends stand in for the two wire ends, the length series for a gate sweep, and tip height for barrier transparency.

**The claim, as I read it.** Cr chains on Bi-terminated β-Bi2Pd show a length-driven closing and reopening of the in-gap spectrum across Cr4, Cr5, Cr8 and Cr12 (Fig. 2(a)), and in Cr12 zero-bias modes at both ends inside a reopened gap of 204 ± 50 µeV (Fig. 2(a), Fig. 4(b), Fig. S3). A localization length of about 10.5 Å, read as three sites, comes from the residual splitting of the calculated end mode (Eq. 1, Sec. S5) and is offered as the reason hybridization stays small.

## Checks a careful reader will look for

1. Look for trivial bound states at the chain ends (resonances above zero, levels that split and recross) : Not done. The four-length series follows the in-gap levels, with no end-atom spectrum over the full bias range and no tracking of end-state energy over consecutive lengths.
2. Show the peak over wide ranges, including where it is absent : Partly. "Figure 2(a) shows the measured in-gap spectra for Cr4, Cr5, Cr8, and Cr12" (p. 2) shows the short chains where it is absent; there is no field or temperature series.
3. Measure both ends at the same settings : Done. Fig. 4(b) shows "spectral weight localized near the two ends and a reduced signal in the central region" (p. 4, Fig. 4 caption).
4. Show the peak stays as the junction transparency changes (here, tip height or setpoint) : Not done.
5. Bulk gap closing and reopening where the end peaks appear : Partly. "Upon adding a fifth atom, the dominant in-gap feature shifts to negative energy, indicating the closing of the low-energy gap" (p. 2); the closing is inferred from one feature, and for Cr4 "the experimental resolution does not allow us to resolve a clear mini-gap" (p. 2).
6. State any subtraction and show the raw data : Partly. Fig. S3 shows the raw curve and "the red curve after subtraction of a dI/dV curve taken in the clean base superconductor" (p. S4, Fig. S3), for the gap estimate only.
7. Report chains built and measured, how many showed the effect, and why others were set aside : Not done.
8. Disclose the full parameter ranges and why each shown range was chosen : Partly. "Conductance spectra were acquired with a lock-in amplifier using a 30 µV excitation at 330 Hz" (p. S1); the lengths built and the reason for the four shown are not given.
9. Processing from raw data to figures, with data and code : Partly. The gap subtraction is described in Sec. S7 (p. S4); no data or code are linked, and the processing behind the Fig. 2(a) maps is not described.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Trivial Andreev or YSR state at a chain end (adapted from the dot entry) | Tested in part | Dot signatures searched: no; zero-bias state at both ends: all | "Fig. 4(b) shows the corresponding zero-bias conductance profile along the same chain. The spectral weight is concentrated near the two ends" (p. 3) | Plot the end-state energy at both ends for each length from Cr8 up, and show end-atom spectra over the full bias range. |
| Quasi-Majorana from smooth confinement | Tested in part | Gap closing and reopening: part; correlated zero modes at both ends: part (one chain, with "a clear imbalance", no parameter varied) | "for Cr12 a gap centered at zero energy is recovered at the chain center and two zero-bias resonances appear at the chain ends" (p. 2) | Show the chain-center spectrum for every length built near Cr5 and Cr8, and compare the two end-mode energies in Fig. S1(a). |
| Disorder or inhomogeneity along the chain | Tested in part | End-to-end correlation: part; gap closing and reopening: part; insensitivity to parameters that should not matter: no | "the accumulation of strain can be inhomogeneous in the chain leading to small geometrical distortion" (p. S3 to S4) | Repeat on a second Cr12 chain, or rebuild one at another site, and check the end modes stay at zero. |
| Kondo resonance at an end atom | Not tested (not mentioned) | Even-odd occupancy: no; temperature dependence: no; Zeeman splitting: no | Not discussed. | A small field series within the superconducting range and a temperature series of the end peak. |
| Trivial Andreev band mimicking gap reopening | Tested in part | Tested on a trivial model: part (Rashba sweep of Cr12 only, Fig. S2); parameters outside the protocol varied: no | "We can see that the Rashba coupling is instrumental in closing an reopening the gap, leading to a topological quantum phase transition." (p. S2) | Run the length series in your model with αR set to zero, and compute an invariant for the infinite chain at the fitted parameters. |
| State at one end only | Ruled out for the claim | Both ends compared: all; nonlocal conductance: no | "spectral weight localized near the two ends" (p. 4, Fig. 4(b)); zero-bias weight at both ends is enough by itself against a one-sided state | None needed |
| Local-probe loophole (overlapping components) | Tested in part | Both ends measured: all; overlap estimated: no | "The experimental signal-to-noise ratio is lower than in previous microwave-assisted tunnelling studies, preventing a more precise determination of the residual offset of the edge mode from zero bias" (p. S4) | Bound the splitting from the measured spectra (for example with a superconducting tip), and fit the decay of the Fig. 4(b) profile to get ξM from data. |
| Fine-tuning and selection | Tested in part | Counts: no; how data were chosen: no; second dataset: part (the "No RF" profile in Fig. S5(a) may be the same chain) | "Figure 1(c–f) shows representative Cr4, Cr5, Cr8, and Cr12 chains." (p. 2) | Report counts per length and show a second Cr12 chain. |
| Oscillating splitting that is near zero at the chosen length (not in library) | Not tested (argued, not tested) | Energy over consecutive lengths at both ends: no; splitting measured or bounded: no | "Since no moiré pattern is observed for Cr chains on Bi2Pd [20], we take cos(kF L) ≃ 1." (p. 3) | Build Cr9 to Cr14 and plot end-mode energy against length; with kF ≈ 0.34 Å⁻¹ and 4.75 Å spacing, cos(kF L) changes sign about every two atoms. |
| Trivial end states in a trivial minigap (not in library) | Not tested (data bear on it) | Defect at one end, end energies compared: no | "the experimental profile in (b) displays a clear imbalance between the two edge amplitudes" (p. 3) | Place one defect atom at one end of a Cr12 chain and compare the two end-state energies. |

## Questions about devices and data

1. How many chains of each length did you assemble and measure, and how many of the long chains showed zero-bias end modes?
2. Why were the others set aside, for example chains that broke or developed stacking faults from the strain you describe in Sec. S6?
3. Which chain lengths beyond Cr4, Cr5, Cr8 and Cr12 did you build (Cr6, Cr7, Cr9 to Cr11, longer than Cr12), and which bias, setpoint, temperature and field ranges did you measure beyond the ones shown?
4. What does the second-best Cr12 chain look like, and is the "Cr*12" chain in the RF data the same chain as in Fig. 4?
5. The 16.8 µeV splitting comes from the calculation with ΓD = 5 µeV. What is your experimental energy resolution with a PtIr tip at 30 mK and a 30 µV lock-in excitation, and can the measured Cr12 spectra bound the splitting? By my estimate Eq. (1) with ξM = 10.5 Å, L = 57 Å, kF = 0.18 a0^-1 and the free-electron mass gives about 9.5 µeV, and 16.8 µeV gives ξM of about 11 Å; which mass and kF did you use, and how is "three lattice sites" counted, given that 10.5 Å is about 2.2 spacings of 4.75 Å?
6. Which Rashba coupling produces Fig. 2(b), Fig. 3, Fig. 4(c,d) and the 16.8 µeV splitting? Sec. S2 gives αR ≈ 1.8 eV·Å, Sec. S4 says 3.6 eV·Å, and Sec. S7 reports calculated gaps of 84 and 146 µeV next to the measured 204 ± 50 µeV.
7. Adding atoms leaves the bulk Hamiltonian unchanged, so how does the length series separate a phase transition from the Shiba band filling in as levels are added? A topological invariant for the infinite chain at your fitted parameters would help.
8. Did you measure the end modes in a magnetic field, or after placing a defect atom at one end of a Cr12 chain? Both would help separate trivial end states from Majorana-like ones.

## Related work

- Schneider et al. 2021, "Controlled length-dependent interaction of Majorana modes in Yu-Shiba-Rusinov chains", <https://arxiv.org/abs/2104.11503>. Mn chains on Nb built atom by atom: the end-mode splitting, measured from both ends, goes to zero only at periodic lengths.
- Schneider et al. 2022, "Testing the topological nature of end states in antiferromagnetic atomic chains on superconductors", <https://arxiv.org/abs/2211.00561>. Near-zero end states in a large minigap; a defect at one end shifts only that end's state, which rules out a Majorana origin.
- Küster et al. 2021, "Non-Majorana modes in diluted spin chains proximitized to a superconductor", <https://arxiv.org/abs/2112.05708>. Chains built atom by atom show boundary modes that mimic Majorana signatures and are identified as trivial Shiba states.
- Hess et al. 2022, "Prevalence of trivial zero-energy sub-gap states in non-uniform helical spin chains on the surface of superconductors", <https://arxiv.org/abs/2204.02324>. Non-uniform helical chains can host near-zero trivial states, which they find far less common on a 3D superconductor than in equivalent nanowires.
- Peng et al. 2014, "Strong localization of Majorana end states in chains of magnetic adatoms", <https://arxiv.org/abs/1412.0151>. Velocity renormalization localizes Majorana end states on a scale far below the host coherence length, the mechanism you invoke for ξM.

Happy to rerun this if you share the figure data.
