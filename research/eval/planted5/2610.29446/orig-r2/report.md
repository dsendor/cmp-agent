# Lookalike check: Suppressing Majorana hybridization in Cr chains on β-Bi2Pd (arXiv 2610.29446v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. The library is written for nanowire transport, so I adapted its zero-bias entries to STM spectroscopy of an atomic chain: "both ends" means the two chain ends in one map, "bulk gap" means the gap at the chain center, and "transparency" means tip height.

**The claim, as I read it.** You assemble Cr chains atom by atom on β-Bi2Pd and report that the in-gap spectrum closes and reopens with length (Cr4, Cr5, Cr8, Cr12; Fig. 2a). In Cr12 you see zero-bias modes at both ends (Figs. 2a, 4b, S1) and a reopened gap of 204 ± 50 µeV at the center (Fig. S3). From a residual splitting of 16.8 µeV in the calculation you derive ξM ≈ 10.5 Å, about three sites (Eq. 1). The electron-hole exchange (Figs. 3, S2) comes from the calculation, and the 44 GHz data (Figs. S4, S5) come from the same Cr12 chain.

## Checks a careful reader will look for

1. Search for trivial bound states (adapted: end-atom and single-atom YSR states, resonances that cross and recross) : Partly. "This controlled length series allows us to follow the evolution from coupled Yu–Shiba–Rusinov (YSR) states to end-localized zero-energy modes" (p. 2, Fig. 2a); the single-adatom spectrum is cited from Ref. [23] and not shown here.
2. Peak over wide ranges, including where it is absent : Partly. You show four lengths, including lengths without end modes (Fig. 2a); no magnetic field is applied.
3. Both ends at the same settings : Done. "The spectral weight is concentrated near the two ends and is strongly reduced in the central region" (p. 3, Fig. 4b).
4. Peak stable as the junction changes (adapted: tip height or setpoint) : Not done. The setpoints for the spectroscopy maps aren't given.
5. Bulk gap closes and reopens where end peaks appear : Partly. "Upon adding a fifth atom, the dominant in-gap feature shifts to negative energy, indicating the closing of the low-energy gap" (p. 2, Fig. 2a); for Cr4 "the experimental resolution does not allow us to resolve a clear mini-gap" (p. 2).
6. Raw data and processing of the conductance (adapted: substrate subtraction) : Partly. Fig. S3 shows the raw curve next to the curve after subtracting "the dI/dV of the pristine surface" (p. S4); the maps' normalization isn't stated.
7. Counts of devices and datasets : Not done. Fig. 1 shows "representative" chains (p. 2), with no counts.
8. Full parameter ranges : Partly. "a lock-in amplifier using a 30 µV excitation at 330 Hz" and T = 30 mK (p. S1); lengths, field and the reasons for each range aren't stated.
9. Processing steps, data and code : Partly. The model parameters and the subtraction are described (pp. S1, S4); I found no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Trivial YSR or Andreev end state (adapted from abs-quantum-dot) | Tested in part | Trivial bound-state signatures: part; zero bias at both ends: all | "Zero-bias end states can also arise from trivial Andreev or YSR bound states [14–18]" (p. 1); both ends in Fig. 4b | Show end-atom spectra next to a single Cr adatom, plus Cr11 and Cr13 ends, from your growth sequence |
| Quasi-Majorana from a slowly varying coupling | Tested in part | Gap closing and reopening: part; correlated zero modes at both ends: part | "the experimental profile in (b) displays a clear imbalance between the two edge amplitudes" (p. 3, Fig. 4b) | Compare energy and width at both ends in Fig. S1(a); run your code on a trivial chain with a smooth J gradient |
| Disorder or strain states (adapted from disorder-induced-zbp) | Tested in part | End-to-end correlation: part; gap closing and reopening: part; insensitivity to irrelevant knobs: no | "the interaction will be local and will keep the topology of the perfect chain" (p. S4) | Rebuild Cr12 at a second site; model larger J variations to find where the zero mode leaves zero |
| Crowded trivial subgap states (several YSR channels per atom) | Tested in part | Lengths with peaks compared with prediction: part; orbital model: part | Model uses "a single compact orbital per site" (p. S1); "For Cr4, the spectral weight is concentrated near zero bias" (p. 2) | Show Cr4 to Cr12 end spectra on one bias axis; say whether Cr d-orbital channels change Fig. 2b |
| State at one end only | Ruled out for the claim | Both ends compared: all; nonlocal conductance: no | "two zero-bias resonances appear at the chain ends" (p. 2, Fig. 2a); one map covers both ends, which by itself shows the partner | None needed |
| Trivial Shiba band mimicking closing and reopening | Tested in part | Criterion run on a trivial model: part; unused parameters varied: no | "the Rashba coupling is instrumental in closing an reopening the gap" (p. S2, Fig. S2) | Run the Fig. 2b length series in a trivial parameter set and give the invariant for the parameters you used |
| Local-probe loophole | Tested in part | Both ends: all; overlap measured: no | Signal-to-noise prevents "a more precise determination of the residual offset of the edge mode from zero bias" (p. S4) | Give an experimental bound on the splitting from the end spectra, with the lock-in and thermal widths |
| Fine-tuning and selection | Tested in part | Counts: no; how chosen: part; second dataset: no | "The chains were constructed in defect-free regions" and "representative" chains (p. 2, Fig. 1) | Give chain counts per length and show a second Cr12 |
| Trivial end states in a chain that isn't ferromagnetic (not in library) | Not tested (data bear on it) | Local defect at one end with both ends followed: no | Not discussed; Fig. S1(a) shows both ends of a chain whose ends differ | Add a defect atom at one end and follow both end energies, per Schneider et al. |

## Questions about devices and data

1. How many chains of each length did you assemble and measure, and how many Cr12 (or longer) chains showed zero-bias end modes?
2. Why were the others set aside, for example chains that broke or distorted from the strain you describe in Sec. S6, or chains near defects?
3. Since you grew each chain one atom at a time, which other lengths did you measure beyond Cr4, Cr5, Cr8 and Cr12 (Cr6, Cr7, Cr9 to Cr11, or longer than Cr12), and did you take any spectra in a magnetic field?
4. What does the second-best Cr12 chain or dataset look like?
5. In Fig. S1(a), do the end states at the stronger and the weaker end sit at the same energy, and how do their widths compare with the 30 µV lock-in excitation and the 16.8 µeV calculated splitting?
6. Which Rashba coupling did you use for the calculations in Figs. 2 to 4: the DFT value of about 1.8 eV·Å (Sec. S2) or 3.6 eV·Å (Sec. S4)? For those parameters, what is the topological invariant, and does the same length series in a trivial parameter set also give a gap closing, a reopening and end peaks?
7. What were the spectroscopy setpoints (bias and current) for the maps in Figs. 2(a) and 4(b), how were the maps normalized, and do the end peaks stay at zero bias at other tip heights?
8. With the free-electron mass, Eq. (1) gives δϵ of about 9.5 µeV for ξM = 10.5 Å, and ξM of about 11 Å for δϵ = 16.8 µeV; it also moves only from about 9 Å to 15 Å as δϵ goes from 1.7 µeV to 168 µeV. Could you state the inputs you used and how sensitive ξM is to the calculated δϵ?

## Related work

- Schneider et al. 2021, "Controlled length-dependent interaction of Majorana modes in Yu-Shiba-Rusinov chains", <https://arxiv.org/abs/2104.11503>. Mn chains on Nb(110) built atom by atom, with the splitting of the end modes measured from both ends as the chain grows; the splitting reaches zero within resolution only at periodic lengths.
- Schneider et al. 2022, "Testing the topological nature of end states in antiferromagnetic atomic chains on superconductors", <https://arxiv.org/abs/2211.00561>. In antiferromagnetic Mn chains, a defect at one end moves only that end's state off zero energy, which rules out a Majorana origin; their model needs unrealistically large spin-orbit coupling to reach the topological phase.
- Küster et al. 2021, "Non-Majorana modes in diluted spin chains proximitized to a superconductor", <https://arxiv.org/abs/2112.05708>. Chains assembled atom by atom show end modes almost everywhere that mimic Majorana signatures and are identified as trivial Shiba states.
- Hess et al. 2022, "Prevalence of trivial zero-energy sub-gap states in non-uniform helical spin chains on the surface of superconductors", <https://arxiv.org/abs/2204.02324>. Non-uniform helical chains can host trivial near-zero states, though these are far less common than in nanowires, and the authors find none for a 1D chain on a 3D superconductor.
- Choi et al. 2017, "Probing magnetic interactions between Cr adatoms on the β-Bi2Pd superconductor", <https://arxiv.org/abs/1709.09224>. On this surface, Cr dimers couple ferromagnetically or antiferromagnetically depending on their arrangement, and this shows up in their intra-gap spectra.

Happy to rerun this if you share the figure data.
