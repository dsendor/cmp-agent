# Run notes: arXiv 2610.29446v1

AI only.

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 entries). Skill: cmp-assistant/skill/SKILL.md and report-template.md, read once at the start.
- What I read: the extracted text of 2610.29446v1 (main text pp. 1-4, supplement pp. S1-S8, references), given as paper.txt. The prompt barred me from fetching the abstract page or the PDF. I took figure content from the captions and the main text only, because the extracted text holds no figure images. I took the title from the paper text. I normalized subscript spacing from the PDF extraction in quotes (for example "Cr4 , Cr5" becomes "Cr4, Cr5").
- Not opened: the figures themselves. The paper links no data repository, and there are no ancillary files, so I did not run read_mtx.py.
- Recognition: I did not recognize this paper (it is dated 21 Oct 2026, after my training data).

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| In-gap spectrum closes and reopens with chain length | Fig. 2a (exp), 2b (theory) | Cr4, Cr5, Cr8, Cr12, called "representative" (Fig. 1c-f) | Chains built: not stated. Chains per length: not stated. Lengths 6, 7, 9-11 and >12: not shown. One crystal (Tc = 5.2 K). T = 30 mK only. No field. Lock-in 30 µV at 330 Hz. Bias range: only in the figures (not readable). Spectroscopy setpoint: not stated (topography V = 3 mV, I = 50 pA) |
| Zero-bias modes at both ends of Cr12 | Figs. 2a, 4b, S1a/c | One Cr12 chain | One chain. Amplitude imbalance between the ends |
| Reopened gap 204 ± 50 µeV | Fig. S3 (after subtracting the pristine-surface dI/dV) | Cr12 center | One curve |
| Electron-hole exchange and spin texture | Figs. 3, S2 | Calculation only | PtIr tip is not spin-polarized. Rashba coupling: 1.8 eV·Å (S2), 3.6 eV·Å (S4), and 2.5 eV·Å mentioned (S7) |
| ξM ≈ 10.5 Å from the residual splitting | Eq. 1, S5 | Calculation with ΓD = 5 µeV, δϵ = 16.8 µeV; "agreement" with Fig. 4b | Splitting not resolved experimentally (S8) |
| End asymmetry from a 6% J gradient | Figs. 4c/d, S1d/e | Calculation | Linear 1% per atom over half the chain |
| RF response consistent with broadening | Figs. S4, S5 | Cr12, third and sixth atoms, plus profiles | 44 GHz. VRF up to 0.22 mV (S5), larger in S4 |

## Scope adaptation

The paper is an STM study of an atomic chain on a superconductor. The library is written for transport. I used the zbp and practice checks and adapted them as follows: dot search becomes end-atom or single-atom YSR states; both ends becomes both chain ends in one map; transparency becomes tip height and setpoint; nonlocal gap becomes the gap at the chain center versus length; series resistance becomes subtraction and normalization. Adapted entries: abs-quantum-dot (as trivial YSR or Andreev end states), quasi-majorana-smooth-confinement (smooth J or strain gradient), disorder-induced-zbp (strain or inhomogeneous coupling), crowded-trivial-subgap-states (several Shiba bands or orbital channels), trivial-andreev-band-gap-reopening (trivial Shiba band with length), one-end-only and local-probe-loophole (both chain ends in an STM map).

## Entries skipped

- kondo-resonance: its tests (even-odd dot occupancy) do not map onto adatoms whose YSR states sit inside a 0.76 meV gap. A field series would still be worth asking for (question 3).
- weak-antilocalization: about disorder-averaged multichannel transport. It does not apply to local tunneling into an atomic chain.
- fine-tuned-plateau and series-resistance-subtraction: the paper claims no quantized conductance value.
- micromagnet-stray-field: no magnets.
- full-shell-flux-andreev: no full-shell wire.
- spin-orbit-length-pinning: needs a normal segment and a field sweep. Neither exists here.
- exceptional-point-zero-mode: the subgap bath is the gapped superconductor and the tip is in weak tunneling, so the non-Hermitian lead coupling it needs does not apply.
- protocol-parameter-sensitivity: no automated protocol.
- All shapiro, supercurrent, charge, chiral, island, kitaev and diode entries: other signatures.

## Sources held out

None. All library sources predate the paper (posted 21 Oct 2026). I judged this from their dates and titles and did not open them to check whether they cite it.

## Related work checks

All five were checked on the arXiv abstract page (title, first author, abstract text), not the full text: 2104.11503 (Schneider, Mn on Nb, length-dependent splitting), 2211.00561 (Schneider, antiferromagnetic chains, one-end defect test), 2112.05708 (Küster, trivial end modes in diluted chains), 2204.02324 (Hess, prevalence of trivial zero states in helical chains, which they find low), 1709.09224 (Choi, Cr dimer ferromagnetic or antiferromagnetic order on β-Bi2Pd). I found the arXiv ID for Choi 2017 through OpenAlex (DOI 10.1103/PhysRevLett.120.167001).

## Library gaps

- Trivial end states in atomic chains whose magnetic order is not ferromagnetic, separated by a local defect at one end (Schneider et al., arXiv 2211.00561). Added as an outside row.
- No STM-specific family: tip-height dependence, lock-in and thermal resolution against claimed splittings, spin-polarized tips, and chain length as the tuning knob.
- No entry for theory-derived quantities, here ξM from a calculated splitting, presented next to the measurement.

## Unsure

- Rashba coupling: S2 says αR ≈ 1.8 eV·Å from DFT, and S4 says "we have increased the coupling ... αR = 3.6 eV-Å". It is unclear which value Figs. 2-4 use (question 6).
- Arithmetic: Eq. 1 with the free-electron mass, kF = 0.18/a0 and L = 57 Å gives δϵ ≈ 9.5 µeV at ξM = 10.5 Å (cos taken as 1). Solving with δϵ = 16.8 µeV gives about 11.2 Å. This is a small difference, but ξM depends only logarithmically on δϵ (question 8). The true cos(kF L) is about 0.86.
- "Both ends: all" rests on the zero-bias profile (Fig. 4b) and the map in S1. I could not see the figures to check whether the weaker end shows a resolved peak at zero bias.
- How the shown data were chosen: I marked this "part" on the strength of "defect-free regions" plus "representative". A strict reading could mark it "no".
- Outside row note: I chose "data bear on it" because Fig. S1(a) shows a chain with unequal ends. "Not mentioned" is also defensible.

## Skill issues

- The skill says to use the title on the arXiv abstract page, but this run barred fetching it. I used the title from the paper text.
- The skill says to write reports/<id>.md and .notes.md. This run asked for them inline, so I wrote neither file.
- Adapting nanowire tests to STM chains is left to judgment. For example, it is unclear whether "both ends compared" counts for one-end-only and local-probe-loophole when both ends appear in one STM map. I counted it.
- The skill does not say how to treat claims that rest on calculation (spin texture, ξM). Tests are defined as measurements or analyses the paper shows, so a calculation counts as an analysis. Whether it should count for a lookalike about the sample is unclear.
- Under the judge-the-evidence rule, range gaps go only under fine-tuning-and-selection. But zbp-wide-ranges is itself a range check, and the rule does not say whether "Partly" there counts the same gap twice.
