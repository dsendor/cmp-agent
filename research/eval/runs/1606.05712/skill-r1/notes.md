# Run notes: arXiv 1606.05712v1

- Run: lookalike-assistant skill, run skill-r1, 2026-10-23. Library `meta.version` 0.4 (updated 2026-10-23, 28 lookalike entries, `checks` for families zbp, shapiro, kitaev, charge, practice).
- Output written to eval/runs/1606.05712/skill-r1/ as asked by the caller, not to reports/<id>.md and reports/<id>.notes.md as the skill says.

## What I read
- Local copies only, no fetch of the paper: abs.html (title, 19 authors, submitted 2016-06-18, v1 only, "20 pages, 3 figures", journal DOI 10.1126/science.aag2792 listed), paper.txt (full extracted text), and paper.pdf (figure pages 16 to 20 rendered to PNG to read axes and labels).
- Supplementary material: none in the PDF (text runs pp. 1 to 10, references pp. 11 to 14, acknowledgments p. 15, figures pp. 16 to 20). No arXiv ancillary files and no data repository linked, so read_mtx.py wasn't used.
- Page numbers are the printed page numbers, which match the PDF pages.
- I recognized the paper (He et al., later published in Science) and know its later history. I didn't use that knowledge in the report.

## Claims table (step 1)

| Claim | Figures | Device(s) | Counts and ranges |
|---|---|---|---|
| σ12 plateaus near 0.5 e²/h at the shoulders of the σ12 valleys during reversal | Fig. 2b (350 mK), Fig. 2c (20 mK), Fig. 3a | I, II, III (Fig. 2b); Fig. 2c device not named, Fig. 3a is device I | Device I at 350 mK: 0.49 e²/h at ±80 mT (low-field), kinks 0.51(±0.05) (high-field); II 0.52(±0.06); III 0.48(±0.07); 20 mK: 0.50(±0.06) at both shoulders (p. 8). Fig. 2b spans about -40 to 290 mT, one sweep direction only. |
| σ12 = 0.98(±0.04) e²/h at saturation (𝒩 = ±2), about 0.05 e²/h in NI dips | Fig. 2c, Fig. 3a | presumably I | 20 mK; field ±350 mT (Fig. 2c), ±400 mT (Fig. 3a). At 350 mK the high-field σ12 reads about 0.7 e²/h (Fig. 2b, Fig. 3b lowest trace, read by eye). |
| Plateaus narrow with temperature and vanish above 400, 470, 390 mK | Fig. 3a, 3b (device I only) | I, II, III | 20 to 340 mK (Fig. 3a), 350 to 520 mK in 10 mK steps (Fig. 3b, 3c); II and III temperature data not shown. |
| Repeatable over "many magnetic reversal sweeps" (p. 2) | none shown as repeats | not stated | Number of sweeps not given; sweep rate not given. |
| Control QAHI Hall bar shows zero Hall plateau at Hc = ±150 mT and no half plateau | Fig. 2d (σxy, 20 mK), Fig. 3c (σ'12, 350 to 520 mK) | 1 control bar, same wafer (p. 6) | σ'12 of the control at 20 mK not shown. |
| Nb bar Hc2 far above QAHI Hc | Fig. 2a | Nb bar | R(T) at 0 to 2.8 T in 200 mT steps; Hc2 points from about 2.3 to 6.5 K, extrapolated by GL fit. |

Missing counts: devices fabricated, devices measured, devices showing the effect (3 shown as "representative"), cooldowns, number of sweeps, sweep rate, excitation current and frequency, how σ12 is computed from V12, how plateau values and errors were extracted, and the wafers for II and III. Field is perpendicular only. There are no gates ("without the assistance of electric field tuning", p. 6). The film is 6 QL; the bar is 2 mm × 1 mm; the Nb bar is 8 mm × 0.6 mm (200 nm Nb, 5 nm Au).

## Entries matched, adapted, skipped (step 2)
- Matched: `chiral-plateau-superconductor-short` (direct family match) and `fine-tuning-and-selection` (always).
- Adapted: `fine-tuned-plateau` (its signature is a zero-bias peak near 2e²/h; adapted to a half-quantized σ12 plateau vs field, keeping the control of wider ranges, other devices and values above or below the quantized value). `series-resistance-subtraction` (no subtraction is reported; adapted to "how the conductance value is extracted" in this four-terminal circuit, since the plateau value depends on that conversion).
- Skipped as not applicable: all `zbp` entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode), because there is no tunneling spectroscopy or zero-bias peak. Also skipped: the `nonlocal` entries (one-end-only, trivial-andreev-band-gap-reopening), for nanowire ends and the bulk gap, which don't apply here. `local-probe-loophole`, because there are no local probes of separated zero modes. `protocol-parameter-sensitivity`, because there is no automated protocol. `island-states-coulomb-spacing`, the shapiro entries, `transparent-junction-pi-crossing`, `switching-jump-blind-region`, `field-enhanced-supercurrent-resonances`, `charge-trap-fractional-shift`, `coulomb-dominated-interferometer`, `false-poor-mans-majorana` and `diode-vortex-screening`, because the device and signal differ.
- Checks walked: `practice` only (report-counts partly, report-ranges partly, report-processing not done). There is no `checks` block for the chiral family.

## Sources held out
- https://arxiv.org/abs/1904.06463 (Kayyalha et al.): its ref. [23] is He et al., Science 357, 294 (2017), the published version of this paper. Held out.
- https://arxiv.org/abs/1708.06752 (Huang, Setiawan and Sau): its abstract cites "Science 357, 294 (2017)" and ref. [14] is He et al. Held out.
- Together these are every source of `chiral-plateau-superconductor-short`. I used the entry's own lookalike, mechanism, control and data text, quoted neither source, and left both out of related work.
- Checked and kept: https://arxiv.org/abs/2309.09368 (Frolov et al.; no mention of He et al., chiral Majorana or anomalous Hall) and https://arxiv.org/abs/2501.18631 (Akrap et al.; cites Kayyalha et al. as ref. [46] among praised replications, but doesn't cite He et al. by title, authors or ID). Neither is quoted in the report. Also grep-checked, with no mention found: 2101.11456 and 2502.19560.

## Related work, how checked
For every listed paper I opened https://arxiv.org/abs/<id> and confirmed the ID, title and first author, and read the abstract through the arXiv API.
- 1507.00788 Wang et al. 2015: abstract.
- 1708.06214 Ji and Wen 2018: abstract and full text (pp. 1 to 2, the contact-resistance argument). It was written in response to the published version of this experiment and refers to data (σ13, "Fig. 4C in Ref. 10") that aren't in v1. I described only its own result.
- 1603.02311 Liu et al. 2016: abstract and full text (jumps between about 65 and 145 mK, "stochastic, yet systematic"; first two jumps reproducible over four successive scans, with HJ varying by about 10%).
- 1506.05114 Lachman et al. 2015: abstract.
- 2307.08578 Uday et al. 2024: abstract.
- Seen in searches but not listed: 1608.00237 (Chen et al., domain walls; discusses this experiment), 1709.05558 (Lian et al., disorder and critical scaling; discusses this experiment), 1904.12396 (Zhang, Pan, Yin, He 2019, a repeat by the same group), 1809.04752 (Shen et al. 2019, Andreev spectroscopy on the same alloy).

## Library gaps
- Barkhausen-like discrete jumps or avalanches at the Chern-state transition of magnetic TIs (source: Liu et al. 2016, https://arxiv.org/abs/1603.02311). The paper raises it itself; the library has no entry.
- Magnetic-domain inhomogeneity and percolation near the coercive field appear only in the data field of `chiral-plateau-superconductor-short`, and only with a held-out source. A separate entry with a non-held-out source (for example Lachman et al. 2015 for superparamagnetic domains) would help.
- There is no `checks` block for the chiral family. Candidates: contact transparency measured, sweeps above the superconductor's critical field, control bar at the same temperature, repeated sweeps.

## Unsure
- The 0.7 e²/h saturated σ12 at 350 mK is read by eye from Fig. 2b and the unoffset lowest trace of Fig. 3b; I wrote "appears to".
- Whether the Fig. 2c device is device I isn't stated; I assumed so from Fig. 3a.
- Chiral row: I chose "partly addressed" over "not addressed" because the paper gives an argument about Andreev scattering from a trivial superconductor (p. 10) and shows saturated data (p. 8) that bear on it, even though it never names the strip as a short.
- The Barkhausen row is "partly addressed" because the paper argues the point, but shows no successive sweeps at a fixed temperature.

## Skill issues
1. **Hold-out can remove every source of the one entry that matches.** The rule doesn't say whether the entry's own text (lookalike, mechanism, control) can still be used. I used it without citing the sources; a stricter reading would drop the entry entirely.
2. **Related work can undo the hold-out.** Step 5 allows later papers that discuss the paper under review, as long as I describe "what they show". This lets held-out content back in (Ji and Wen make the same argument as the held-out entry). It is also unclear whether held-out library sources may be listed as related work; I excluded them.
3. **Indirect citations.** The hold-out rule doesn't cover a source that cites a critique of the paper without citing the paper itself (Akrap et al. citing Kayyalha et al.). I kept it.
4. **No family checks.** Step 3 assumes a `checks` block exists for the paper's family; the chiral family has none. I walked only the practice checks and said so in the report.
5. **Output paths.** The skill names reports/<id>.md and reports/<id>.notes.md; the caller named eval/runs/.../report.md and notes.md. I followed the caller.
6. **Adapting in-scope papers.** The "Scope" sentence under "What this is" is meant for out-of-scope measurements. It is unclear whether in-scope papers with adapted entries should say so; I added one sentence.
7. **No slot for extra explanation.** The template's table allows one quote and one clause per cell, with no place for things like the saturated-conductance data that bear on a lookalike. I added a short "Some notes on the rows" section below the table.
8. **Author-raised alternatives.** It is unclear whether an alternative the authors raise themselves (Barkhausen) that isn't in the library counts as "an explanation you think of". I treated it as a "(not in library)" row with an opened source.
9. **Missing counts in the standard questions.** The four standard questions overlap with ranges the paper partly gives. The skill says to note "where" the paper answers them, but the template has no slot for a partial answer; I put the partial answer in the question text.
10. **Word target.** It is unclear whether "600 to 900 words outside the table" includes questions and related work. With them, the report runs a little over 900.
11. **Harness, not skill.** The subagent Write tool blocks .md report files, so a subagent can't produce report.md or notes.md as the skill and caller expect.
