# Run notes: arXiv 2610.29446v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries plus the checks section.
- Skill read: skill/SKILL.md and skill/report-template.md. read_mtx.py not used (no figure data).
- Paper read: the extracted text only (paper.txt): main text pp. 1-4 and supplement pp. S1-S8, including captions of Figs. 1-4 and S1-S5. No PDF or abstract page was given, and I fetched neither, as instructed. The title comes from the text header. Figure details come from the captions only; I could not see any panel, so bias ranges, color scales and how many spatial points each map has are unknown.
- Data repository: none linked in the text. None used.
- Recognition: I did not recognize this paper (dated October 2026, after my training data). No knowledge of its later history was used.

## Claims table (step 1)

| Claim | Figures | Device(s) | Counts and ranges |
|---|---|---|---|
| Chain-length-driven closing and reopening of the in-gap spectrum | Fig. 2(a) (exp), 2(b) (theory), Fig. 1(c-f) topographs | One "representative" chain each of Cr4, Cr5, Cr8, Cr12 (p. 2). Atoms were added "sequentially to one end"; unclear whether this is one chain grown in steps or separate chains | Chains assembled: missing. Lengths built beyond 4, 5, 8, 12: missing. Regions, tips, cooldowns: missing. One crystal, Tc = 5.2 K. T = 30 mK only. No magnetic field data. Lock-in 30 µV at 330 Hz. Spectroscopy setpoint: missing (imaging 3 mV, 50 pA). Cr4: "experimental resolution does not allow us to resolve a clear mini-gap" (p. 2) |
| Zero-bias modes at both chain ends | Fig. 2(a), Fig. 4(a,b), Fig. S1(a,c) | One Cr12 chain | End amplitudes are clearly imbalanced (p. 3, Fig. S1c). The theory reproduces this only with a linear J variation (Fig. 4d) or a 1% cumulative perturbation (Fig. S1e) |
| Reopened gap Δtopo = 204 ± 50 µeV | Fig. S3 | Cr12 chain center | From a pristine-surface subtraction, with the raw curve shown. Model gives 84 µeV (αR = 1.8) and 146 µeV (αR = 2.5) (p. S4) |
| Exchange of electron-hole character, spin texture | Fig. 3, Fig. S2 | Calculation only | Tip was non-magnetic PtIr. No spin-polarized data. The summary lists it among "the combined observation" (p. 4) |
| ξM ≃ 10.5 Å (about three sites) from the residual splitting | Eq. (1), Sec. S5 | Calculation for Cr12 at ΓD = 5 µeV | δϵ = 16.8 µeV is calculated; the experiment cannot resolve the offset ("signal-to-noise ratio is lower", p. S4). The 16.8 µeV is below the 30 µV excitation. cos(kF L) ≈ 1 is assumed from the absence of moiré |
| RF (44 GHz) response consistent with compact modes | Fig. S4, S5 (main text cites S5 with stray asterisks "Cr ∗ 12", "V ∗ RF") | Cr12, third and sixth atoms (S4), profile along the chain (S5) | One frequency only. VRF up to 0.22 mV in S5, larger in S4 (value not given). Sec. S8 refers to "the microwave study of Fig. 4", but Fig. 4 has no RF data |

My arithmetic check of Eq. (1) with the free electron mass, kF = 0.18/a0 = 0.340 Å^-1 and L = 57 Å: δϵ(ξ = 10.5 Å) is about 9.5 µeV, and 16.8 µeV needs ξ of about 11.1 Å. cos(kF L) = cos(19.4) is about 0.86. 10.5 Å / 4.75 Å is about 2.2 spacings, against "three lattice sites" (p. 3). These are small, and they went into question 6. Theory parameters are inconsistent: Sec. S4 says "we have increased the coupling to ... αR = 3.6 eV-Å", while S2 gives the DFT value 1.8 eV·Å. Which value Figs. 2(b), 3 and 4 use is not stated.

## Adaptation (scope)

This paper is STM tunneling spectroscopy of atomically assembled Shiba chains, not transport in nanowires. Adapted entries:
- abs-quantum-dot: read as trivial YSR/Andreev states localized at the chain ends. "Dot signatures" means end states that split off zero and recross.
- quasi-majorana-smooth-confinement: read as a smooth variation along the chain (the paper itself models a linear J gradient). "Nonlocal gap closing" means the chain-center gap versus length.
- disorder-induced-zbp: read as an inhomogeneous exchange or adsorption. "Gates" means tip height, region or tip change.
- crowded-trivial-subgap-states: read as several YSR orbitals per Cr. "Field and gate range" means the length range against the model prediction (end modes predicted beyond about eight atoms).
- one-end-only, local-probe-loophole: "both ends" means the two chain ends probed by the tip.
- trivial-andreev-band-gap-reopening: the "protocol" is the paper's criterion of length-driven closing and reopening plus end modes.
- Checks zbp-dot-search, zbp-wide-ranges, zbp-transparency (tip height or setpoint), zbp-nonlocal-gap and zbp-raw-conductance (the Fig. S3 background subtraction) were adapted the same way.

## Entries skipped and why

- kondo-resonance: the zero-bias feature sits inside a 0.76 meV gap at 30 mK, and the single Cr adatoms are fit as YSR states [23]. The entry's mechanism needs a Kondo temperature well above the gap, which would leave no YSR states.
- weak-antilocalization: needs a many-channel disordered transport wire; STM tunnels into a local density of states.
- fine-tuned-plateau, series-resistance-subtraction: the paper makes no claim of a quantized conductance. The background subtraction is covered by the adapted checks zbp-raw-conductance and report-processing.
- micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning (no normal segment, no field data), exceptional-point-zero-mode (tip weakly coupled; no normal reservoir lead into the chain), protocol-parameter-sensitivity (no automated pass/fail protocol).
- Families chiral, island, shapiro, supercurrent, charge, kitaev, diode: a different signal. false-poor-mans-majorana: considered because the chains are short, but the signature is quantum-dot sweet spots, so skipped.

## Sources held out

None. No library source cites this paper (none could: all library sources predate October 2026, and grep found no match for 2610.29446 or Bi2Pd in the library).

## Related work: how each was checked

- 2104.11503 (Schneider et al.): ID, title, first author and abstract confirmed from the arXiv abstract page.
- 2112.05708v3 (Küster et al.): abstract page confirmed. I also read the full text (PDF): the perturbation tests in Fig. 3c-d, and the supplement passage "This closing and reopening, however, does not indicate a phase transition from trivial to topological."
- 2211.00561 (Schneider et al.): abstract page confirmed (found via the arXiv website search).
- 2204.02324 (Hess et al.): abstract page confirmed.
- 1412.0151 (Peng et al.): abstract page confirmed.
- Also opened, not listed: 2104.11497 (Schneider et al., topological Shiba bands by quasiparticle interference).

## Library gaps

- Finite-size gap closing and reopening in short trivial spin chains (Küster et al. 2022, arXiv 2112.05708, supplement). It is used here as an outside row. Its tests come from that paper: a topological invariant or longer model chains, and robustness of the end modes to added adatoms or defects.
- Atomic-chain (STM Shiba chain) family: no checks exist for it. A local-defect test at one end (Schneider et al. 2022, arXiv 2211.00561) and a spin-polarized-tip test would fit there.
- Calculated quantities presented as measured: Fig. 3 and the splitting behind ξM are calculated, but the summary lists them among observations. No entry or check covers this "theory-as-evidence" pattern.

## Unsure

- Whether a calculation counts as "shown" for a test: I counted Fig. S2 (the αR sweep in the model) as part of "Protocol tested on trivial models".
- local-probe-loophole, "Nonlocal measurement (both ends ...)": I marked it all, because both chain ends are probed. A stricter reading would mark it part, since energies at the two ends are not correlated over lengths.
- crowded-trivial-subgap-states, range compared with prediction: I marked it all for the four lengths shown.
- one-end-only: I marked it ruled out, even though the ends are imbalanced; both ends do show zero-bias weight.
- Whether the four lengths are one chain grown in steps or separate chains is unclear from the text.

## Skill issues

- Several adapted tests ("Nonlocal conductance", "Overlap through a quantum dot in series", "gates") have no STM analogue. The skill does not say whether to mark these "no" or treat them as not applicable. I marked them "no", which pulls statuses toward "Tested in part".
- The skill does not say whether theory figures can satisfy a test.
- The outside-row rule overlaps with adapted entries. Schneider et al. 2211.00561 (trivial end states in a large minigap) could be an outside row or the adapted abs-quantum-dot. I folded it into the abs-quantum-dot suggested check to avoid a double count.
- Step 7 says to write reports/<id>.md and use the arXiv abstract-page title. This run forbade both (title taken from the paper text, outputs returned inline).
- The word target (600 to 900 outside the table) is tight once the template boilerplate and eight questions are included. This report is about 960 words outside the table.
