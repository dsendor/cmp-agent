# Lookalike check: Suppressing Majorana hybridization in atomically assembled Cr chains on β-Bi2Pd (arXiv 2610.29446v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. Your paper is scanning tunnelling spectroscopy on atom-built Shiba chains, so I adapted the nanowire entries: chain length stands in for gate and field, the chain center stands in for nonlocal conductance, and the two chain ends stand in for two tunnel probes.

**The claim, as I read it.** Cr chains built atom by atom on β-Bi2Pd show a length-driven closing and reopening of the in-gap spectrum (Fig. 2, Cr4, Cr5, Cr8, Cr12) and zero-bias modes at both ends of a Cr12 chain (Figs. 2(a), 4(b)). From the splitting of the calculated zero-energy mode (16.8 µeV at ΓD = 5 µeV) you extract ξM ≃ 10.5 Å and conclude that finite-size hybridization is strongly suppressed.

## Checks a careful reader will look for

1. Search for trivial bound states that could sit at zero (adapted from the dot search) : Partly. "This controlled length series allows us to follow the evolution from coupled Yu–Shiba–Rusinov (YSR) states to end-localized zero-energy modes" (p. 2); four lengths shown.
2. Wide ranges, including where the effect is absent (adapted: chain length, field) : Partly. Cr4, Cr5 and Cr8 appear without end modes (Fig. 2(a)); no field data and no lengths between those shown.
3. Both ends at the same settings : Done. "showing spectral weight localized near the two ends and a reduced signal in the central region" (Fig. 4(b), p. 4).
4. Junction transparency (adapted: tip height or setpoint) : Not done. No spectra at different setpoints are shown.
5. Bulk gap closing and reopening where the end peaks appear (adapted: chain-center spectra versus length) : Partly. "From the conductance minimum in the central region of the Cr12 chain, we estimate a reopened low-energy gap of ∆topo = 204 ± 50 µeV" (p. 2); the closing is read from a shift at Cr5, and for Cr4 "the experimental resolution does not allow us to resolve a clear mini-gap" (p. 2).
6. Raw conductance (adapted: STM has no series resistance; setpoint, normalization, raw spectra) : Partly. "a 30 µV excitation at 330 Hz" (p. S1) and "The red curve is the full conductance" (Fig. S3, p. S4); the spectroscopy setpoint and any normalization are not stated.
7. Report counts of devices and datasets : Not done. The chains are "representative" (p. 2) with no count.
8. Report full ranges : Partly. "VRF = 0.22 mV corresponds to the largest applied ac modulation" (Fig. S5, p. S6); other lengths built are not stated.
9. Processing steps with data and code : Not done. No data or code linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Quasi-Majorana (partially separated) bound states | Tested in part | Gap closing and reopening (chain center for nonlocal): part; correlated zero modes at both ends: part | "From the conductance minimum in the central region of the Cr12 chain, we estimate a reopened low-energy gap of ∆topo = 204 ± 50 µeV" (p. 2); end amplitudes differ and end energies are not compared. | Fit the peak energy at each Cr12 end with your resolution, and show chain-center spectra at every length you built. |
| Disorder-induced zero-bias states | Tested in part | End-to-end correlation: part; gap closing and reopening: part; insensitivity to parameters that should not matter: no (modeled only) | "the experimental profile in (b) displays a clear imbalance between the two edge amplitudes" (p. 3) | Show a second Cr12 chain and compare its end amplitudes and center gap with Fig. 4(b). |
| Trivial bound state at a chain end (adapted from the quantum dot entry) | Tested in part | Trivial resonances followed as atoms are added: part (four lengths); both ends compared: all | "Zero-bias end states can also arise from trivial Andreev or YSR bound states [14–18], so a convincing interpretation requires more than the observation of a localized zero-bias peak." (p. 1) | Show full-bias spectra on the end atoms for each length, so readers can see end states approach zero and whether they split and recross. |
| Zero mode at one end only | Ruled out for the claim | Both ends compared at the same settings: all; nonlocal conductance: no | "spectral weight localized near the two ends" (Fig. 4(b), p. 4); one map covering both ends shows a partner at the far end, which is what this lookalike lacks. | None needed |
| Local-probe loophole (overlap not measured) | Tested in part | Both ends measured: all; overlap measured: no (calculated only) | "Using the calculated splitting yields ξM ≃ 10.5 Å" (p. 3); "preventing a more precise determination of the residual offset of the edge mode from zero bias" (p. S4) | State the upper bound on the splitting that the measured Cr12 end spectra set, next to the calculated 16.8 µeV. |
| Trivial Andreev band mimicking gap reopening | Tested in part | Tested on trivial models: part (Fig. S2 varies αR for Cr12 only); unused parameters varied: no | "Together with the gap closing and reopening observed in Fig. 2, this evolution supports the assignment of the long chains to a topological Shiba-chain regime." (p. 2) | Run the same length series in the model in the trivial regime (small αR), and measure a chain in field or along another direction. |
| Fine-tuning and selection | Not tested (data bear on it) | Counts: no; how shown data were chosen: no; second dataset: no | "Figure 1(c–f) shows representative Cr4 , Cr5 , Cr8 , and Cr12 chains." (p. 2) | Report how many chains of each length were built and measured, and show a second Cr12. |
| Length-oscillating end-mode splitting (not in library) | Tested in part | End energy followed length by length past the onset: part (only Cr12 has end modes); splitting resolved against resolution: no | "Since no moiré pattern is observed for Cr chains on Bi2 Pd [20], we take cos(kF L) ≃ 1." (p. 3) | Show end-state energies at both ends for Cr9 to Cr13 and longer, atom by atom; that tests cos(kF L) ≃ 1 directly. |
| Trivial end states in a wide trivial minigap (not in library) | Not tested (argued, not tested) | Local defect at one end, far end watched: no | "a small variation of the local coupling to the superconducting substrate is sufficient to account for the measured asymmetry while preserving the zero-energy character of the end state [18, 31]" (p. 3), shown in calculation (Fig. 4(d)) | Move or remove the end atom at one end of a long chain and show whether the other end's mode stays at zero, as Schneider et al. do. |

Most rows come back to one point. Your measured spectra show end-localized zero-bias weight and a reopened center gap; the residual splitting, and so ξM ≃ 10.5 Å and the suppression of hybridization, come from the calculation at ΓD = 5 µeV. The measured spectra bound the splitting only to your energy resolution. A stated experimental bound, and end energies over more lengths, would let readers see how much of the headline claim rests on data.

Two smaller things a reader may trip on. The calculation in S4 uses αR = 3.6 eV·Å, twice the 1.8 eV·Å from DFT quoted in S2, and the measured gap (204 µeV) exceeds both calculated values (84 and 146 µeV, p. S4). Cross-references also drift: S8 calls the RF data "the microwave study of Fig. 4", and S6 points to "Fig. 3" for the edge asymmetry.

## Questions about devices and data

1. How many Cr chains did you assemble and measure at each length, and how many of the long chains showed zero-bias modes at both ends? Is the chain used for the RF data (written "Cr ∗ 12" on p. 4) the same chain as in Fig. 4?
2. Why were the other chains set aside, for example chains that ruptured or faulted from the strain you describe in S6, or chains without end modes?
3. Which lengths did you build and measure beyond Cr4, Cr5, Cr8 and Cr12 (Cr6, Cr7, Cr9 to Cr11, longer than 12), and did you take any spectra in magnetic field?
4. What does the second-best long chain, or a second Cr12, look like?
5. What is your energy resolution (30 µV lock-in excitation, effective electron temperature), and what upper bound on the end-mode splitting do the measured Cr12 end spectra set, next to the calculated 16.8 µeV?
6. Which Rashba coupling produced Figs. 2(b), 3, 4 and the 16.8 µeV splitting: the 1.8 eV·Å from DFT or the 3.6 eV·Å of S4? How do the splitting and ξM change between the two, given the measured 204 µeV gap against the calculated 84 and 146 µeV?
7. Could you perturb one end of a long chain (move or remove the end atom, or add a defect) and show whether the far end's mode stays at zero energy?
8. Which mass enters Eq. (1), and how does ξM shift if you keep cos(kF L) with kF L of about 19.4 rad? With a 4.75 Å spacing, 10.5 Å is about 2.2 sites; how did you arrive at three?

## Related work

- Schneider et al. 2021, "Controlled length-dependent interaction of Majorana modes in Yu-Shiba-Rusinov chains", <https://arxiv.org/abs/2104.11503>. Mn chains on Nb(110) built atom by atom; end-mode splitting measured from both ends at each length, reaching zero only at periodic lengths within the energy resolution.
- Schneider et al. 2022, "Testing the topological nature of end states in antiferromagnetic atomic chains on superconductors", <https://arxiv.org/abs/2211.00561>. Near-zero end states in a large minigap; a defect at one end splits that end's state off zero while the other end's stays, ruling out a Majorana origin.
- Küster et al. 2021, "Non-Majorana modes in diluted spin chains proximitized to a superconductor", <https://arxiv.org/abs/2112.05708>. Atom-built spin chains whose end modes mimic Majorana signatures and are identified as trivial Shiba states.
- Jeon et al. 2017, "Distinguishing a Majorana zero mode using spin resolved measurements", <https://arxiv.org/abs/1710.04662>. Spin-polarized STM on Fe chains on Pb, proposed as a measured test that separates Majorana modes from trivial in-gap states.
- Peng et al. 2014, "Strong localization of Majorana end states in chains of magnetic adatoms", <https://arxiv.org/abs/1412.0151>. Theory: velocity renormalization localizes Majorana end states far below the host coherence length.

Happy to rerun this if you share the figure data.
