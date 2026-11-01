# Run notes: 2608.26022v1

**Library version:** 0.5 (meta.updated 2026-10-24), 28 lookalike entries.

## What I read
- The skill (SKILL.md), report-template.md and library/lookalikes.yaml, all in full, including `checks`.
- paper.txt in full (main text, methods, references, figure captions, supplementary text and the S1 to S14 captions, and Table S1).
- abs.html: title, authors and date (2026-08-26) from its meta tags, and the abstract. The page lists no ancillary files.
- PDF (33 pages): I rendered and looked at pp. 14 to 16 (Figs. 2, 3 and 4) and pp. 26, 27, 30, 32 and 33 (Figs. S7, S8, S11, S13 and S14) to read field values, device labels and sweep ranges.
- I did not fetch the paper itself in any form.

## What I couldn't open
- There is no data repository: "available from the corresponding author upon reasonable request" (p. 9). There are no ancillary files, so read_mtx.py wasn't used.
- The paper's folder also held other files (paper_planted.txt, plain.txt, prompt_*.txt, planted_removed.txt). I only listed their names and didn't open them, per the task instructions.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Pristine hBN-covered CsV3Sb5 shows no field-free diode | Fig. 1e,f; Figs. S1, S2; Table S1 | Devices 1 to 10 | 10 devices, thickness 21 to 76 nm, Ic 81 to 496.5 μA, η upper bound 0 to 0.48% (Table S1), 1.8 K, B = 0; R(B) to ±10 T in-plane |
| Oxidation turns on a field-free diode | Fig. 2; Fig. S3; Fig. S5 (AFM) | Device 11 (Fig. 2); Fig. S3 caption says Device 12 is Fig. 2 | η = 83.61% after 2nd oxidation; 3 sweeps per stage, diode in 1 of 3 at stages 2 and 4, 0 of 3 at stage 3, no Ic at final stage; 1.8 K; 0 to ±300 μA; Iac = 10 μA, steps 0.2 to 0.5 μA |
| Etching turns on a field-free diode | Fig. 3a-c; Fig. S7 | Device 13 (zig-zag), Device 14 | Device 14 sweep rate 0.05 μA/s; Ic about 66 to 76 μA |
| The diode is stochastic | Fig. 3d,e; Figs. S4, S6, S7, S8, S9, S12 | Device 13 (and the "Device 12" values in Fig. S4, captioned Device 13), Device 14 | 0.25 to 1.5 K in 0.25 K steps, 6 sweeps each; η from −30.86% to 17.07% (3 of 6 sweeps with a diode); fixed-bias time traces at 68 to 74 μA for about 20 min (Fig. S12); field cooling at 1 T out-of-plane and in-plane (Figs. S8, S9) |
| A small field trains the polarity | Fig. 4; Figs. S10, S11 | Device 13, Device 14 | Fig. 4: B = −0.2, −0.1, 0, 0.1, 0.2 T out-of-plane, 9 sweeps each, temperature not stated; Device 14: 0.1 T out-of-plane, 0.2 and 0.3 T in-plane |
| No diode once CDW is suppressed (Ti, x = 0.24) | Figs. S13, S14 | Device 15 (oxidized; panels read Device 19 and #20), Device 16 (etched; panel reads Device 20) | 3 oxidation stages with 2 sweeps each after the pristine sweep; 5 sweeps at 0.05 μA/s plus 1 at 0.025 μA/s; η bound about 0.1%; temperature not stated; Tc about 2 K from the Fig. S13 R(T) |

Missing counts: the total number of oxidized or etched CsV3Sb5 devices fabricated and measured, cooldowns, the temperature for Fig. 4 and for the Ti-doped data, the field steps between 0 and 0.1 T, and the residual field of the magnet.

## Entries matched, skipped, adapted
- Matched: `diode-vortex-screening` (diode family) and `fine-tuning-and-selection` (always).
- Skipped as not applicable: every zbp, quantization, nonlocal, island, shapiro, chiral and kitaev entry, because there is no tunneling spectroscopy, conductance quantization, Majorana claim, microwave drive or quantum-dot chain. Also skipped:
  - `field-enhanced-supercurrent-resonances`: the claim isn't a supercurrent that grows with field.
  - `charge-trap-fractional-shift` and `coulomb-dominated-interferometer`: no fractional-charge claim.
  - `protocol-parameter-sensitivity`: no automated pass/fail protocol.
  - `local-probe-loophole`: no local-probe Majorana claim.
- Adapted: none. The paper is in the library's diode family, so I didn't add a scope sentence. The library has no `checks` for the diode family, so only the three practice checks were walked.

## Sources held out
None. Every library source predates 2608.26022 (August 2026). The two 2026 revisions (Legg arXiv 2502.19560v2 and Akrap et al. arXiv 2501.18631v2) are on other topics, and I judged them unlikely to cite this paper. I didn't fetch them to confirm.

## Related-work checks
I fetched each arXiv abstract page and confirmed the ID, title, first author and that the abstract supports my one-line description. All five were checked from the abstract only:
- 2309.00264 (Le et al.)
- 2506.04601 (Ge et al.)
- 2605.29665 (Zhang et al.)
- 2205.09276 (Hou et al.)
- 2205.12196 (Golod and Krasnov)

I also opened 2310.10337 (Mehrnejat et al., flux-pinning-mediated diode in NbSe2/CrGeTe3) and didn't list it, since it relies on a magnetic layer.

The searches used the arXiv API with 3 s waits. Queries covered "superconducting diode" with CsV3Sb5, trapped vortex, remanent field, trapped flux, switching current and self-field.

## Library gaps
- Zero-field diode from trapped vortices plus self-field in ordinary superconductors (Golod and Krasnov, arXiv 2205.12196). I added it as an outside row. Its tests come from the abstract's control: trapping and removing a vortex, and changing the bias configuration.
- Ordinary switching-current statistics: sweep-to-sweep scatter in |Ic+| and |Ic−| gives an η whose sign scatters when only a few sweeps are taken. I didn't open a paper that shows this in a diode measurement, so it isn't in the table. It appears as question 6 (the one question the paper invites).
- Remanent field of superconducting magnets after high-field sweeps. I folded it into the `diode-vortex-screening` suggestion and question 5. A dedicated entry with a source would help.
- No `checks` for the diode family. Candidates: a near-zero field map with the residual field calibrated, a control film or device of a conventional superconductor with the same geometry, and switching histograms per direction.

## Judgment calls and uncertainty
- I counted the Ti-doped etched and oxidized devices as an equivalent of "a plain film of the parent superconductor" and marked that test "part". They have a different Tc, an unstated temperature, possibly a different etch pattern, and one device per route.
- For `diode-vortex-screening`, I marked the field-dependence test "part". Fig. 4 has five fields in 0.1 T steps, there is no Oe-scale sweep, and the SI vortex argument (Fig. S10) covers only in-plane fields.
- For the outside row, field cooling then field removal (Figs. S8, S9) deliberately traps flux. I marked that test "part" because no flux-free reference is shown.
- Page numbers: main-text pages follow the "Page X of 16" footers. SI pages follow the SI's own numbering (SI p. 2 is the supplementary text, SI p. 13 is Fig. S10).
- Device labels are inconsistent between Fig. 2, Figs. S3 and S4, and Figs. S13 and S14 (question 8). Where they conflict I took device identities from the main text.
- I didn't recognize the paper and used no knowledge of its later history.

## Skill issues
- The skill says to write `reports/<id>.md` and `.notes.md`. This run delivered them inline per the task, because the environment refuses .md writes.
- The template's "What this is" sentence says "topological transport", which reads oddly for a diode paper that makes no topological claim. The scope rule only covers "a different kind of measurement", so it's unclear whether a non-topological claim in a listed family needs the scope sentence.
- `checks` has no diode family even though `meta.families` lists it. The skill doesn't say what to do when a family has no checks; I walked only the practice checks and said so in the report.
- The test "plain film or junction of the parent superconductor" is ambiguous when the material under test is itself the parent compound. It isn't clear whether a doped or differently processed control counts as equivalent.
- "Ruled out" requires that "the paper concludes against the lookalike", but nothing says whether a general conclusion ("extrinsic polarity, fabrication disorder, and inhomogeneous switching are not sufficient", p. 8) counts as concluding against a specific lookalike.
- The hold-out rule can't be checked without fetching every source's full text. The skill doesn't say whether judging by date is acceptable.
- The cap of eight questions, the four standard questions, paper-specific questions and one invited question pull against each other. I merged the label and onset-criterion questions into question 8 to stay within eight.
