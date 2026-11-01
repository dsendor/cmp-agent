# Run notes: arXiv 2610.29446v1

AI only. Run date 2026-10-24. Library version 0.5 (meta.version), 28 lookalike entries.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all entries, tests and the checks section). Nothing else under cmp-assistant/ was opened. read_mtx.py not used (no figure data).
- The paper as extracted text only (scratchpad planted2/blind/t66/paper.txt): main text pp. 1-4 and Supplementary pp. S1-S8, including captions of Figs. 1-4 and S1-S5. Figures themselves were not seen; figure details come from captions and text.

## What I could not open
- Per the task, I did not fetch the arXiv abstract page, PDF or HTML of 2610.29446. The report title is taken from the paper text (lightly shortened in the header: "Suppressing Majorana Hybridization in Atomically Assembled Cr Chains on β-Bi2Pd").
- No data repository or code is linked in the paper, so nothing was used to count devices or ranges.
- Text extraction loses subscripts and adds spaces (for example "Cr4 ," for Cr subscript 4). I normalized that whitespace inside quotes; words are verbatim.

## Recognition
I do not recognize this paper (dated 21 Oct 2026). No later history used.

## Claims table (step 1)
| Claimed signal | Figures | Measured or calculated | Device(s) | Counts and ranges |
|---|---|---|---|---|
| Chain-length-driven closing and reopening of the in-gap spectrum | Fig. 2(a) exp, Fig. 2(b) calc | Both | Cr4, Cr5, Cr8, Cr12 (one chain each shown, "representative") | Lengths 4, 5, 8, 12 only; lengths 6, 7, 9-11 and >12 not shown; Cr4 mini-gap unresolved (p. 2); built by adding atoms at one end (p. 2) |
| Zero-bias modes localized at both chain ends | Fig. 2(a), Fig. 4(b), Fig. S1(a,c) | Measured | One Cr12 chain | Clear end imbalance; attributed to a 6% J variation in calc (Fig. 4(d), S1(e)) |
| Reopened gap Δtopo = 204 ± 50 µeV | Fig. S3 | Measured, after subtraction of clean-surface dI/dV | Cr12 center | How ±50 µeV was obtained is not stated |
| Exchange of electron-hole character across the transition; spin texture | Fig. 3, Fig. S2 | Calculated only | Model chains | αR: 1.8 eV Å from DFT (p. S1) vs "increased the coupling ... αR = 3.6 eV-Å" (p. S2) |
| Residual splitting 16.8 µeV and ξM ≃ 10.5 Å | Eq. (1), Sec. S5 | Calculated (Dynes Γ reduced to 5 µeV) | Model Cr12 | cos(kF L) set to 1 |
| Compact real-space end profiles | Fig. 4(b) exp, 4(c,d) calc | Both | One Cr12 chain | |
| RF response consistent with broadening | Figs. S4, S5 | Measured + Tien-Gordon / Dynes simulation | Cr12, 3rd and 6th atoms, profiles | 44 GHz only; VRF up to 0.22 mV (Fig. S5) |
Missing counts: chains built per length, chains that ruptured (S6 mentions strain-driven rupture), chains showing end modes, tips, cooldowns, crystals (one "selected crystal", Tc = 5.2 K). Fixed parameters: T = 30 mK, no magnetic field, lock-in 30 µV at 330 Hz, setpoints for spectra not given (topography 3 mV, 50 pA).

## Scope adaptation
The paper is STM on atomic Shiba chains, outside the library's nanowire transport focus. Adapted: zbp checks (dot search -> search for trivial end-atom YSR states; transparency -> tip height or setpoint; nonlocal gap -> chain-center gap versus chain length; raw conductance/series resistance -> clean-surface background subtraction and raw curve). Adapted lookalike entries: quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, trivial-andreev-band-gap-reopening, one-end-only, local-probe-loophole (tests reinterpreted for STM on chains; length used as the tuning parameter).

## Entries skipped and why
- abs-quantum-dot: no semiconductor segment or tunnel-barrier region; vacuum STM junction. Its physics (trivial end bound states) is covered by the outside row.
- kondo-resonance: judgment call. Single Cr adatoms here show YSR states near the Fermi level (per the paper's refs), and the Cr12 center shows a gap (Fig. S4(c)); a site-local Kondo resonance would not give end-only weight. Flagging as uncertain.
- weak-antilocalization: a transport interference effect in many-channel wires; does not apply to STM LDOS.
- fine-tuned-plateau, series-resistance-subtraction: no conductance quantization claim.
- spin-orbit-length-pinning: needs a normal segment and a field sweep; neither present.
- exceptional-point-zero-mode: tip coupling is weak (tunneling setpoints of tens of MΩ), so lead-induced non-Hermitian locking is negligible; skipped.
- micromagnet-stray-field, full-shell-flux-andreev, island-states-coulomb-spacing, protocol-parameter-sensitivity (no automated protocol), chiral, Shapiro (4 entries), supercurrent, charge (2), kitaev, diode: different signal families or device types.

## Sources held out
None skipped. Library sources were used only as quoted in the library; I did not open their full texts. All library sources are earlier than this Oct 2026 paper or are comments on other papers; none appears to discuss it.

## Related work: how checked
Each found via the arXiv API (export.arxiv.org, 3 s between calls), abstract read from the API summary, then the arXiv abstract page fetched to confirm ID, title and first author (from citation meta tags). Abstract only for all five:
- 2104.11503 Schneider et al., abstract checked.
- 2211.00561 Schneider et al., abstract checked (also the source of the outside row; it is the paper's own ref. [18], published as Nat. Commun. 14, 2742).
- 2112.05708 Küster et al., abstract checked.
- 2204.02324 Hess et al., abstract checked.
- 2104.06171 Mier et al., abstract checked (same group's earlier work).
A search for Peng et al. 2015 returned nothing via the API; not listed.

## Library gaps
- No Shiba-chain / STM family: trivial end states in trivial minigaps (Schneider 2022, arXiv 2211.00561, control: perturb one end and follow both end states; magnetic order), trivial Shiba boundary modes (Küster 2021). Added as one outside row.
- No check for evidence that is calculation-only (here the electron-hole exchange and ξM). A check like "separate measured from modeled evidence; show model sensitivity to fitted or chosen parameters" would fit.
- No STM-specific checks (tip setpoint dependence, energy resolution versus claimed splittings, superconducting-tip resolution).

## Arithmetic and consistency notes (not all in report)
- Eq. (1) with ħ²/m = 7.62 eV Å², kF = 0.18/a0 = 0.340 Å⁻¹, L = 57 Å, δε = 16.8 µeV and cos = 1 gives ξM ≈ 11.1 Å (10.5 Å gives ≈ 9.5 µeV). cos(kF L) = cos(19.4) ≈ 0.86, not 1. 10.5 Å / 4.75 Å ≈ 2.2 sites, versus "three lattice sites". L = 12 × 4.75 Å counts 12 spacings for 12 atoms (11 spacings would be 52 Å). Q6 carries the main point.
- Sec. S8 refers to "the microwave study of Fig. 4", which seems to mean Fig. S5; Sec. S6 cites "Fig. 3" for the edge difference, which seems to mean Fig. 4. Fig. S5 says 0.22 mV is the largest VRF applied, while S8 says the Fig. S4 mid-gap peak appears at "much larger VRF values".
- Main text describes "a variation of 6% between one end atom and the central atom ... keeping the other half of the chain unperturbed"; S3 says 1% per atom over the second half to J12 = 2.35 eV. Consistent in total, wording differs.
- 44 GHz photon energy ≈ 182 µeV, close to Δtopo; not used in the report.

## Unsure
- one-end-only marked "ruled out for the claim" on the single-test route (zero-bias weight at both ends of the same chain). Its second test (nonlocal conductance) has no STM equivalent here.
- local-probe-loophole first test marked "part": both ends are read, but the read is local at each end and no correlation is shown.
- Outside row test 1 marked "part" because the measured end imbalance acts as an uncontrolled one-end perturbation with both end peaks reported at zero bias; a stricter reading would give "no".
- fine-tuning-and-selection "How the shown data were chosen: part" rests on "constructed in defect-free regions" and "representative"; a stricter reading would give "no" and "Not tested (not mentioned)" is not right either since the word "representative" implies other chains.
- zbp-raw-conductance marked Done because the only subtraction described (Fig. S3) shows the raw curve; normalization of the Fig. 2(a) and 4(b) maps is not stated.
- Report runs about 950 words outside the table including template boilerplate, a bit over the 600 to 900 target.

## Skill issues
- Scope: the skill allows adapting entries, but gives no guidance on adapting checks (zbp checks to STM) or on which tuning parameter replaces gate and field (here chain length).
- Theory evidence: the skill does not say whether a calculation counts as a test being "shown" ("the paper shows the measurement or analysis"). I counted model calculations as part at most, never as all.
- "Not tested" notes: when the paper argues against a lookalike in general terms and data also bear on it, the skill does not say which note wins.
- Title: the skill says to use the abstract-page title; the task forbade fetching it. Used the paper text.
- Overlapping entries (one-end-only, local-probe-loophole, quasi-majorana's both-ends test) all hinge on the same both-ends data; the skill could say how to keep them consistent.
- Step 7 says write reports/<id>.md and notes; the task redirected output to the reply, which I followed.
