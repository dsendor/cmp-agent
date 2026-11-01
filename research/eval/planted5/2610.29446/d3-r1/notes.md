# Run notes: arXiv 2610.29446v1

- Library: lookalikes.yaml meta.version 0.5 (28 entries). Read SKILL.md, report-template.md and lookalikes.yaml once at the start.
- Date: 2026-10-24.

## What I read
- The extracted text of 2610.29446v1 (main text, pp. 1 to 4, and Supplementary pp. S1 to S8, including the reference list), from the local file supplied by the caller. Per the caller's instructions I did not fetch the abstract page, PDF or HTML. The title comes from the paper text, not the abstract page. Figure details come from captions only; the figures themselves were not available, so judgments about what a figure shows rest on captions and main text.
- No data repository or ancillary files are mentioned in the text; none used. read_mtx.py not needed.
- Page numbers follow the page markers in the extracted text (p. 1 to 4, S1 to S7). Fig. S4 caption sits on p. S5, Fig. S5 caption on p. S6.

## What I couldn't open
- The paper's figures (text only). Nothing else failed.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Length-driven closing and reopening of the in-gap spectrum | Fig. 2(a) measured, 2(b) calculated; Fig. S1, S3 | Cr chains along <110> on Bi-terminated β-Bi2Pd; lengths 4, 5, 8, 12 shown | Chains built per length: missing. Chains measured: missing. Tips: missing. Lengths between 5 and 8, 8 and 12, and above 12: not stated. Cr4 mini-gap unresolved (p. 2). |
| Zero-bias modes localized at both chain ends | Fig. 2(a) Cr12, Fig. 4(a,b), Fig. S1(c) | One Cr12 chain (as presented) | One Cr12 profile shown; amplitudes asymmetric. No field data. T = 30 mK, lock-in 30 µV at 330 Hz, PtIr tip. Spectroscopy setpoint not stated (topography V = 3 mV, I = 50 pA). |
| Reopened gap Δtopo = 204 ± 50 µeV | Fig. S3, p. 2 | Cr12 center | Single value; how the ±50 µeV was set not stated. Calculated 84 µeV (αR = 1.8) and 146 µeV (αR = 2.5). |
| Residual splitting 16.8 µeV and ξM ≃ 10.5 Å (about three sites) | Eq. (1), S5 | Calculation only, ΓD = 5 µeV | L = 57 Å, kF ≃ 0.18/a0, cos(kF L) set to 1 by citing absence of moiré [20]. My check: free-electron mass gives 9.5 µeV at ξ = 10.5 Å and ξ ≈ 11.1 Å for 16.8 µeV; kF L ≈ 19.4 rad, cos ≈ 0.86; 10.5/4.75 ≈ 2.2 sites. Small differences only, raised as question 8. |
| Electron-hole exchange and spin texture | Fig. 3, Fig. S2 | Calculation only | No spin-polarized measurement. S4 states αR = 3.6 eV·Å used ("increased the coupling"), against 1.8 eV·Å from DFT in S2. Which αR fed Figs. 2(b), 3, 4 not stated. |
| RF response supports compact modes | Fig. S4, S5 | Cr12 (written "Cr ∗ 12" on p. 4) | 44 GHz; VRF up to 0.22 mV (Fig. S5). Third and sixth atoms (Fig. S4). Whether this is the same Cr12 as Fig. 4 is unclear. |

## Checks walked
- Family: zbp checks (adapted to STM chains) and practice checks. The nonlocal family has no checks section; zbp-nonlocal-gap covers gap reopening.
- zbp-transparency adapted as tip setpoint dependence; zbp-raw-conductance adapted as setpoint, normalization and raw spectra (no series resistance in an STM junction).

## Entries matched, adapted, skipped
- Adapted (scope rule, STM on atomic chains): quasi-majorana-smooth-confinement (chain-center spectra for nonlocal conductance), disorder-induced-zbp ("gates that should not matter" read as local perturbations; only modeled), abs-quantum-dot (read as a trivial YSR or Andreev bound state at a chain end; "dot signatures" read as end resonances followed with length), one-end-only, local-probe-loophole ("overlap through a dot" read as a measured overlap or splitting), trivial-andreev-band-gap-reopening (Fig. S2 counted as a partial trivial-model test), fine-tuning-and-selection (always).
- Skipped: kondo-resonance (end modes sit inside a superconducting gap at 30 mK with YSR physics established for these adatoms; considered, and a field series would address it, but no basis in the text to match it); crowded-trivial-subgap-states (multiband nanowire entry; the analogue, multiple Cr d-orbital YSR channels against a single-orbital model, is plausible but the signature does not match closely); spin-orbit-length-pinning (no field dependence claimed); exceptional-point-zero-mode (weak-tunnelling STM junction); weak-antilocalization (disordered multichannel wire); fine-tuned-plateau and series-resistance-subtraction (no quantization claim); micromagnet-stray-field, full-shell-flux-andreev, chiral, island, shapiro, supercurrent, charge, kitaev, diode, interferometer entries (different devices or signals); protocol-parameter-sensitivity (no automated protocol).
- Outside rows (library gaps):
  1. Length-oscillating end-mode splitting, source arXiv 2104.11503 (Schneider et al.; the paper cites it as ref. [33] and its published version as [11]). Control: splitting measured from both ends at each length, zero only at periodic lengths within resolution. Status tested in part: four lengths shown, only Cr12 has end modes; splitting not resolved.
  2. Trivial end states in a wide trivial minigap, source arXiv 2211.00561 (Schneider et al.; published as the paper's ref. [18]). Control: a defect at one end; if that end's state leaves zero while the other's stays, the end states are trivial. Status not tested (argued, not tested): the paper models a J gradient and keeps a zero mode in calculation only.
  Both are library gaps for STM Shiba-chain papers: atom-by-atom length series and single-end perturbation tests.

## Sources held out
- None. No library source cites this paper (the paper is dated 21 Oct 2026; library sources are earlier or are revisions of earlier comments and reports that cannot discuss it).

## Related work checks
- arXiv API query plus abstract page (arxiv.org/abs/<id>) opened for each; ID, title and first author confirmed against the abstract page meta tags; descriptions checked against the abstract text only.
  - 2104.11503 Schneider, Lucas: abstract.
  - 2211.00561 Schneider, Lucas: abstract.
  - 2112.05708 Küster, Felix: abstract.
  - 1710.04662 Jeon, Sangjun: abstract.
  - 1412.0151 Peng, Yang: abstract.
- arXiv API calls spaced 3 to 3.5 s; two title searches returned no entries and were replaced by broader searches.

## Unsure
- "Cr ∗ 12" and "V ∗ RF" on p. 4 may be extraction artifacts or may mark a different chain; asked as part of question 1. I marked "A second device or dataset shown" as no.
- Fig. S5 says increasing VRF reduces end conductance and fills the center; S8 says the RF data of "Fig. 4" sit near VRF ∼ 0.2 mV. Fig. 4 has no RF data; I read this as Fig. S5. S6 cites "Fig. 3" for the edge asymmetry, which is in Fig. 4 and S1. Noted in the report as cross-reference drift.
- One-end-only marked ruled out on the both-ends test alone, since one map over both ends shows a partner; the asymmetric amplitudes are carried under disorder and the outside defect row.
- Check 5 (gap closing and reopening) marked partly: reopening measured at Cr12, closing inferred from a shift at Cr5 with Cr4's mini-gap unresolved. Another reader could mark it done.
- Recognition: I did not recognize this paper or know any later history.

## Skill issues
- The skill says to read the abstract page and PDF; this run was text only by caller instruction, so the title comes from the paper text and figure judgments rest on captions. The skill has no instruction for this case.
- No checks section for the nonlocal family, and no STM-specific checks; adapting zbp checks (transparency, raw conductance) to STM needs judgment the skill does not guide. The status for a check that does not physically apply (series resistance in STM) is undefined: "not done" would penalize, "done" would overstate. I used partly with an adapted reading.
- Notes for "Not tested" ("data bear on it" versus "not mentioned") are ambiguous for fine-tuning-and-selection when the only hint is the word "representative".
- The skill does not say whether a calculation counts as "the paper shows the analysis" for a test whose physical meaning is a measurement (here the calculated splitting and the modeled J perturbation). I counted calculations as not showing a measured test.
- Step 7 asks to write report files; the caller asked for the report in the reply because subagent .md writes are refused.
