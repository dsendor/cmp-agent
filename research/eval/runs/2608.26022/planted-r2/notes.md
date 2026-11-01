# Run notes: arXiv 2608.26022v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalike entries.
- Skill files read: skill/SKILL.md, skill/report-template.md, and the library including `checks`. I did not run scripts/read_mtx.py because there are no figure data.
- Date of run: 2026-10-23.

## What I read

- The extracted text of the paper: main text pp. 1 to 16 plus the supplementary material (its own pages 1 to 17, cited here as Supp. p. N), at scratchpad/eval/blind/m7/paper.txt.
- The arXiv abstract page at scratchpad/eval/blind/m7/abs.html. Title "Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV$_3$Sb$_5$". First author Liu, Xin-Jie; 17 authors. Submitted 2026-08-26 as v1, 33 pages, 18 figures.
- I fetched no version of the paper itself, per the caller's instructions. There was no PDF. Figure details come from the captions only, because the axis labels in the extracted text are jumbled.
- Data repository: none. The paper says "available from the corresponding author upon reasonable request" (p. 9). There are no ancillary files.
- Page numbers come from the "Page N of 16" markers in the text, and from the bare page numbers in the supplement.

## Claims table (step 1)

| # | Claimed signal | Figures | Devices | Counts and ranges | Missing |
|---|---|---|---|---|---|
| C1 | Pristine hBN-encapsulated CsV3Sb5 shows no field-free diode | Fig. 1, Figs. S1, S2, Table S1 | Devices 1 to 10 (Device 1 in Fig. 1; 2 to 10 in Table S1) | 10 devices, top and bottom electrodes, 21 to 76 nm, Ic 81 to 496.5 μA, 1.8 K, B = 0. Table S1 η upper bounds 0 to 0.48% | Whether any pristine device was measured below 1.8 K in the dilution fridge; number of sweeps |
| C2 | Oxidation activates a field-free diode | Fig. 2, Figs. S3 to S5 | Device 11 (Fig. 2); Device 12 (S3 to S5; device labels conflict, see uncertainties) | Device 11: Ic about 115 to about 37 μA after first oxidation; η 83.61% at the second step; 1.8 K, B = 0, sweeps 0 to ±300 μA; 4+ oxidation steps; Iac 10 μA, steps 0.2 or 0.5 μA | Number of sweeps per step; which sweep is shown; how many oxidized devices in total |
| C3 | Asymmetric etching activates a field-free diode | Fig. 3a to c, Fig. S7 | Device 13 (zig-zag), Device 14 | Device 14 sweep rate 0.05 μA/s | Number of etched devices in total |
| C4 | Diode polarity and size are stochastic from sweep to sweep | Fig. 3, Fig. S6, Figs. S3 to S5, S7 | 12, 13, 14 | Device 13: 0.25 to 1.5 K in 0.25 K steps, 6 sweeps per temperature; Device 12: η from −30.86% to 17.07%; Fig. S4 shows 6 sweeps | Total zero-field sweeps |
| C5 | Not removed by field-cooling | Figs. S8, S9 | 14 | 1 T out-of-plane and 1 T in-plane, field then removed | Residual field after removal |
| C6 | A small field trains the diode | Fig. 4, Figs. S10, S11 | 13, 14 | Device 13: −0.2 to 0.2 T out-of-plane, 9 sweeps per field; 0.1 T fixes polarity, 0.2 T fixes size. Device 14: 0.3 T in-plane stabilizes it, 0.2 T in-plane still stochastic; 0.1 T out-of-plane stabilizes it | Field step; temperature for Fig. 4 |
| C7 | Not caused by time-dependent fluctuation | Fig. S12 | 14 | Fixed-bias traces at 68 to 74 μA in 2 μA intervals, about 20 min each; stochastic window 66 to 74 μA | Switching statistics at each bias |
| C8 | Ti-doped (x = 0.24, no long-range CDW) processed devices show no diode | Figs. S13, S14 | Device 15 (oxidized 3 times), Device 16 (etched) | Device 16 η upper bound about 0.1%; slower sweep also shown | Tc, Ic, temperature, number of sweeps, and field series for Devices 15 and 16 |

## Matching (step 2)

- Matched `diode-vortex-screening` (family diode). I adapted it: the entry's signature reads a diode as "finite-momentum or other exotic pairing", while this paper reads it as a CDW-derived time-reversal-breaking texture. The physics is the same: an ordinary diode needs only a small field plus asymmetric barriers.
- Matched `fine-tuning-and-selection`, which applies to every paper.
- Skipped every entry in the zbp, quantization, nonlocal, island, shapiro, kitaev, chiral and charge families. The paper has no tunneling spectroscopy, Majorana claim, Shapiro steps, dot chain, QAH plateau or fractional charge.
- Skipped `field-enhanced-supercurrent-resonances`. Its signature is a supercurrent that grows with field, read as triplet pairing. This paper claims nonreciprocity and does not claim Ic growing with field.
- Skipped `protocol-parameter-sensitivity`. There is no automated pass/fail protocol. The onset criterion for η is covered by the `report-processing` check.
- Skipped `local-probe-loophole`, which is specific to Majorana claims.
- Scope: the paper falls inside the library's scope through the diode family, so I added no scope sentence beyond noting that there are no diode checks.

## Checks (step 3)

- The library `checks` section has no steps for the diode family, so I walked only the `practice` steps: report-counts, report-ranges and report-processing. All three came out partly done.

## Statuses

- **diode-vortex-screening: partly addressed.** The Ti-doped control and the pristine baseline bear on it. They are not the entry's control, which is a plain film of the parent superconductor processed the same way, tracked against field and geometry. The paper does not discuss the Meissner or vortex mechanism and does not report the residual field. It cites Hou et al. only as an example of SDEs that need an applied field. I picked partly over not addressed because the processed Ti-doped devices are a direct control sample.
- **fine-tuning-and-selection: partly addressed.** The paper uses repeated sweeps and shows distributions. Counts of processed devices and of total sweeps are missing.
- **Outside, "trapped Abrikosov vortex plus self-field" (Golod and Krasnov 2022, arXiv 2205.12196, abstract read): partly addressed.** The field-cooling tests (Figs. S8, S9) and the Ti-doped control bear on it, but the paper does not discuss it. It is judged against the control that source describes: polarity follows the bias configuration and vortex trapping or removal. Each sweep drives the flake normal and it re-enters superconductivity in the remanent field and the bias self-field, which could reset trapped flux from sweep to sweep. That is why I suggested swapping the leads and stopping sweeps just above Ic.

## Sources held out

- None. Every library source I used predates the paper (2026-08-26). Frolov 2309.09368 is from 2023. Akrap et al. 2501.18631 v2 is dated 2026-03-25, which I confirmed on its abstract page. Hou 2205.09276 is from 2022. None of them can discuss this paper.

## Related-work checks (step 5)

I found candidates with the export.arxiv.org API (`abs:"superconducting diode" AND abs:CsV3Sb5`, `ti:"diode-with-memory"`, `abs:"nonreciprocal" AND abs:CsV3Sb5`, and others), waiting 3 s between calls. I opened each arxiv.org/abs page and confirmed the ID, title, first author and that the abstract supports my line. I checked abstracts only, not full texts.

- 2205.09276 (Hou, Yasen, first author), abstract.
- 2205.12196 (Golod, T.), abstract.
- 2309.00264 (Le, Tian), abstract. The paper cites it as ref. 17.
- 2506.04601 (Ge, Jun), abstract. The paper cites it as ref. 39.
- 2605.29665 (Zhang, Wei), abstract. It predates the paper.

## Library gaps

1. There are no `checks` steps for the diode family. Candidates:
   - calibrate the residual field and sweep finely through zero;
   - process a conventional or control film identically;
   - swap the bias leads;
   - report full sweep statistics;
   - run the field series on the control sample.
2. Trapped Abrikosov vortex plus bias self-field as a zero-field diode lookalike (Golod and Krasnov 2022, https://arxiv.org/abs/2205.12196) is not in the library.
3. Possible gaps for which I opened no source, so I left them out of the table:
   - the remanent field of superconducting magnets after high-field excursions, as a general practice lookalike;
   - a control sample that differs in more than the target order (Ti doping can also change Tc, disorder and pinning);
   - ordinary switching-current statistics as a source of sweep-to-sweep spread in η, which the paper partly tests in Fig. S12.

## Uncertainties

- Device labels conflict. The text gives Device 11 for Fig. 2 and Device 12 for Figs. S3 to S5, but the Fig. S3 caption reads "Device 12 (Fig. 2 in the main text)". The Fig. S4 caption reads "Device 13 after successive oxidation stages" and carries the η values (17.07%, −30.86%, −14.07%) that the text assigns to Device 12. I raised this as question 8.
- The 17 to 37 μA critical-current range in question 7 combines the labels in Fig. S4 with the "approximately 37 μA" for Device 11 (p. 5).
- From the captions alone I can't tell the temperature of the Fig. 4 field series or whether the Ti-doped devices were measured below 1.8 K.
- I did not recognize the paper and used no knowledge of its later history.

## Skill issues

1. The skill says to walk "the checks for the paper's family", but the diode family has none. It doesn't say whether to adapt checks from the entry's `control` or to use only the practice checks. I used practice only.
2. The supplement restarts its page numbers at 1, and the skill doesn't say how to cite those pages. I wrote "Supp. p. N" in the notes and figure numbers in the report.
3. The template header says `<short title>`, but step 7 says "Use the title on the arXiv abstract page". I used the full abstract-page title with plain-text subscripts.
4. Step 6 says to ask the standard questions "unless the paper already answers them (then say where)". It is unclear what to do when the paper answers them partly: here the pristine count is given but the processed count is not. I asked and noted where the partial answer is.
5. The word target of 600 to 900 sits awkwardly with a template that has no discussion section. The reasoning behind the residual-field concern had to go into question 5 and the table cells.
6. Step 7 says to write the files to reports/. The caller overrode that, so these outputs went to the scratchpad and this reply.
