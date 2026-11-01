# Run notes: 1606.05712v1

AI only. Run on 2026-10-24.

## Library and inputs
- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries; checks for zbp, shapiro, kitaev, charge and practice).
- Read: skill/SKILL.md, skill/report-template.md, the full library.
- Paper: the local abs.html (title "Chiral Majorana edge state in a quantum anomalous Hall insulator-superconductor structure", v1 only, submitted 2016-06-18, "20 pages, 3 figures"), the local paper.txt in full, and PDF pages 16 to 20 as images to read Figs. 1 to 3. I did not fetch the paper.
- Supplementary material: none in the v1 PDF. No ancillary figure data, no data repository linked, so read_mtx.py was not used.
- Could not open: nothing failed.
- I recognized this paper and know some of its later history. I did not use that knowledge in the report and judged the v1 text as written. It did make the hold-out check below matter more, and it made the choice of related work delicate (see Skill issues).

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| σ12 plateau near 0.5 e2/h at the low-field shoulder of each σ12 valley (N = ±1) | Fig. 2b (350 mK), Fig. 2c (20 mK), Fig. 3a | I, II, III | 350 mK: 0.49 (I), 0.52(±0.06) (II), 0.48(±0.07) (III), "at ± 80 mT" (p. 8). 20 mK: 0.50(±0.06) at both shoulders (p. 8). Fig. 2b covers about -40 to 290 mT, one sweep direction. Fig. 2c covers ±300 mT, both directions. |
| High-field-shoulder kinks | Fig. 2b, 2c | I (Fig. 2b caption: "Only device I exhibits a sudden increase...") | 0.51(±0.05) e2/h at 350 mK (p. 8) |
| σ12 ≈ e2/h at saturation (N = ±2), about 0.05 e2/h in the NI dips | Fig. 2c, 3a | I | 0.98(±0.04) e2/h (p. 8) |
| Plateau repeats over sweeps and narrows with T | Fig. 3a (20 to 340 mK), Fig. 3b (350 to 520 mK, 10 mK steps) | I shown; II, III in text only | Disappears above 400, 470 and 390 mK for I, II, III (p. 9). Number of sweeps: "many" (p. 2), not counted. Sweep rate not given. |
| Bare QAHI Hall bar: zero Hall plateau, no half plateau | Fig. 2d (σxy, 20 mK, ±300 mT), Fig. 3c (σ12', 350 to 520 mK) | 1 control bar, same wafer | Hc = ±150 mT (p. 7). σ12' at 20 mK is not shown. |
| Nb Hc2 perpendicular far above Hc | Fig. 2a | Nb bar | Inset 0 to 2.8 T in 200 mT steps. The extrapolated Hc2 at T = 0 is about 4 T. |
| Not Barkhausen | p. 9 to 10, argued from reproducibility and the high-field kink | | Argument plus Fig. 3a |

Missing counts: devices fabricated and measured (only "three representative TSC devices", p. 19), cooldowns, wafers for II and III, number of sweeps, sweep rate, excitation current and frequency, Nb to film contact resistance, whether the Nb was floating or grounded during σ12. Field direction: perpendicular only. No gate ("without the assistance of electric field tuning", p. 6). Fig. 2c's caption does not name the device. I took it to be device I because the lowest 20 mK trace of Fig. 3a (device I) matches it; this is an inference. Small inconsistencies: the Fig. 2 and Fig. 3 axes read "σ12 (h/e2)", and the text has "0.5 h/e2" (p. 8), where e2/h is meant.

## Entries matched, adapted and skipped
- Matched: chiral-plateau-superconductor-short (direct match), fine-tuning-and-selection (always).
- Adapted: fine-tuned-plateau. Its signature is a zero-bias peak at 2e2/h. I matched it on the physics: a plateau at a quantized value over a field range, offered as proof. Its test "Same peak over wider gate and field ranges" was applied as field and temperature ranges, since the device has no gate.
- Outside the library: Barkhausen-type domain jumps, from Liu et al. 2016 (arXiv 1603.02311, full text opened). Its tests come from that paper's own controls: successive scans at fixed T and sweep rate (their Fig. 6), simultaneous separated voltage-contact pairs (their Fig. 5), and temperature and sweep-rate dependence. The paper under review raises this explanation itself (p. 9 to 10).
- Skipped: all zbp entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode). The paper has no tunneling spectroscopy and no zero-bias peak; it lists Kondo, Andreev states and weak antilocalization only as issues for other experiments (p. 3 to 4).
- Also skipped:
  - series-resistance-subtraction: four-terminal measurement, no subtraction described, signature is near 2e2/h. Processing is covered by the report-processing check.
  - one-end-only, trivial-andreev-band-gap-reopening and local-probe-loophole: no end-mode tunneling.
  - protocol-parameter-sensitivity: no automated protocol.
  - island, shapiro, supercurrent, charge, kitaev and diode entries: not this measurement.
- Checks: the library has no `checks` for the chiral family, so only the practice checks (report-counts, report-ranges, report-processing) were walked.

## Sources held out
I downloaded the full text of each library source I would use and searched it for "1606.05712", "Science 357, 294", the authors' names and the title.
- Held out: Kayyalha et al. 2020 (arXiv 1904.06463; ref. [23] is He et al., Science 357, 294 (2017)).
- Held out: Huang, Setiawan and Sau 2018 (arXiv 1708.06752; abstract line 16 cites "Science 357, 294 (2017)", and ref. [14]).
- These are the only two sources of chiral-plateau-superconductor-short. I still used the entry's own mechanism, control and tests, and the report cites neither source.
- Checked and kept: Frolov et al. 2309.09368, Akrap et al. 2501.18631, Prada et al. 1911.04512, Zhang et al. 2101.11456, Yu et al. 2004.08583, Aghaee et al. 2207.02472. None cites the paper.
- Borderline: Akrap et al. cites Kayyalha et al. (its ref. [46]) but not this paper. I kept it under the "title, authors or arXiv ID" rule.

## Related work: how each link was checked
- 1603.02311 (Liu et al.): abstract page opened, ID, title and first author (Minhao Liu) confirmed. Full text read; the reproducibility quote is on p. 3: "Despite the stochastic nature of the jumps, the overall pattern is systematic and reproducible, especially for the first two jumps in a trace." Material Cr-doped (Bi,Sb)2Te3, confirmed in the full text.
- 1708.06214 (Ji and Wen): abstract page opened, title and first author (Wenjie Ji) confirmed. The "general feature of a good electric contact" claim was confirmed in the abstract and full text. The arXiv title writes the fraction in LaTeX; I rendered it as e^2/2h.
- 1908.03303 (Zhang and Liu): abstract page opened, title and first author (Jian-Xiao Zhang) confirmed. Description checked against the abstract.
- 2307.08578 (Uday et al.): abstract page opened, title and first author (Anjana Uday) confirmed. Description checked against the abstract.
- Found and not listed because their main subject is this paper's result:
  - 1608.00237 (Chen et al., domain walls)
  - 1904.12396 (Zhang, Pan, Yin, note on the plateau; overlapping authors)
  - 2407.02761 (Huang et al. 2024, reproduction)
  - 1904.06463 (held out)

## Library gaps
- No entry for Barkhausen or discrete domain-reversal jumps in magnetic TI films (source: arXiv 1603.02311). Liu et al. report a reproducible jump pattern, which bears on reproducibility arguments.
- No entry for Andreev conversion from extra chiral or non-chiral metallic modes giving half transmission (arXiv 1908.03303). This is relevant wherever residual bulk conduction exists; the paper reports about 0.05 e2/h (p. 9).
- No `checks` list for the chiral family. Natural steps would be:
  - contact transparency
  - the Nb normal-state control
  - the bare-film σ12' at the same temperature
  - repeated sweeps
  - multiple voltage pairs
- The chiral entry's only two sources both discuss the paper reviewed here, so for this paper the entry has no usable citation.

## Unsure
- Test "Plateau checked across the full field range of aligned magnetization, including above the superconductor's critical field": marked part. Full loops to ±400 mT are shown for device I; nothing is shown above the Nb critical field or for II and III over a full loop.
- Successive-sweeps test for the Barkhausen row: marked part. Fig. 3a shows many successive traces, but at stepped temperatures, not repeats at fixed settings.
- Plateau heights test: marked part. Heights are given for I, II and III at 350 mK and for I at 20 mK, not for the other traces in Fig. 3.
- report-processing: marked not done. One could argue for partly, since the four-probe AC configuration is described (p. 6).

## Skill issues
- Hold-out of all of an entry's sources: the skill says to skip sources, and does not say whether to keep using the entry's text (mechanism, tests) when every source is held out. That text was written from the held-out papers, so the hold-out leaks.
- Cross-family adaptation: the Scope rule covers adapting entries to a different measurement kind. It does not say whether to adapt an in-scope entry from another family (fine-tuned-plateau for a 0.5 e2/h field plateau). I adapted it and said so.
- Families without checks: the skill does not say what to do when the paper's family has no checks. I used practice only and said so in "What this is".
- Related work after the paper: the skill allows later papers, but almost every later paper on this system cites or answers the paper under review. That sits uneasily with the hold-out spirit and the "don't use later history" rule. I excluded papers whose main subject is this result.
- Outside-row tests: the rule says to take tests "from the control that paper describes". Liu et al. is a measurement paper with no stated control for a lookalike, so I took its own methods as the tests.
- Template and word target: the template has no place for prose beyond one-clause table cells, while the 600 to 900 word target suggests more text. I kept to the template; the report runs about 750 words outside the table.
- flags.json `note`: null for every row, since none is "Not tested".
