# Run notes: arXiv 2608.26022v1

AI only. Lookalike assistant run on 2026-10-23.

## Library
- lookalikes.yaml, meta.version 0.4 (updated 2026-10-23). 28 lookalike entries. Checks sections exist for zbp, shapiro, kitaev, charge and practice. There are none for diode.

## What I read
- The arXiv abstract page as provided (abs.html): title "Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV$_3$Sb$_5$", 17 authors, first author Xin-Jie Liu, dated 2026-08-26, comments "33 pages,18 figures".
- The extracted full text (paper.txt): main text pp. 1 to 16 and supplementary pp. 1 to 17, including the SI text, Table S1 and the captions of Figs. S1 to S14.
- Page numbers: main-text quotes use the "Page N of 16" footers. SI quotes use the SI page numbers and are labelled "SI p.".
- No PDF was provided. Figure content comes from captions and text only, and the axis-tick debris in the extraction was ignored. Per the instructions I did not fetch the paper itself.
- Data repository: none linked. The paper says data are "available from the corresponding author upon reasonable request" (p. 9), so no data were used to count devices. No ancillary figure data, so read_mtx.py was not run.
- I did not recognize the paper. arXiv 2608 is after my training data, so I have no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges | Missing |
|---|---|---|---|---|
| Pristine encapsulated CsV3Sb5 shows no field-free SDE | Fig. 1 (p. 13), Figs. S1, S2, Table S1 | Device 1 plus Devices 2 to 10 ("ten", p. 4) | Thickness 21 to 76 nm, Ic 81 to 496.5 μA, Tc 3.80 to 4.36 K; eta upper bounds 0 to 0.4806% (Table S1); T = 1.8 K; in-plane field magnetoresistance only | Out-of-plane field data for the pristine devices; number of sweeps per device |
| Oxidation activates a field-free SDE | Fig. 2 (p. 14), Figs. S3, S5 | Device 11 (p. 5); Fig. S3 says Device 12 is "Fig. 2 in the main text" | eta = 83.61% at the second oxidation step (p. 5). Ic fell from about 115 to about 37 μA. Bias 0 to ±300 μA, 1.8 K, B = 0. SI p. 2: stage 2, 1 of 3 sweeps showed SDE; stage 3, 0 of 3; stage 4, 1 of 3; final stage, no Ic. Each oxidation stage means warming to 300 K and venting, so it is a separate cooldown. Fig. S3: Iac = 10 μA, steps 0.2 or 0.5 μA | Total number of oxidized devices; onset criterion; sweep rate |
| Asymmetric etching activates a field-free SDE | Fig. 3a to c (p. 15), Fig. S7 | Device 13 (zig-zag), Device 14 | Device 14 sweep rate 0.05 μA/s (Fig. S7) | Total number of etched devices; Device 13 sweep rate |
| Stochastic sign and size | Fig. 3d,e, Figs. S4, S6 | Device 13; "Device 12" per p. 5 | 0.25 to 1.5 K in 0.25 K steps, six sweeps each (Fig. 3 caption). Fig. S4: six sweeps, 3 with SDE, eta 17.07%, -30.86% and -14.07%. Device 14: Ic window about 66 to 74 μA (Fig. S12) | Separate Ic+ and Ic- histograms; the device-label conflict between p. 5, Fig. S3 and Fig. S4 |
| Field training stabilizes the SDE | Fig. 4 (p. 16), Figs. S8 to S11 | Device 13, Device 14 | Out-of-plane -0.2 to 0.2 T, nine sweeps per field (Fig. 4). 0.1 T fixes the polarity; 0.2 T fixes polarity and amplitude (p. 6). Device 14: in-plane 0.3 T stabilizes, 0.2 T is still stochastic (Fig. S10); out-of-plane 0.1 T (Fig. S11). Field cooling at 1 T out of plane and in plane, then field removed: stochastic SDE persists (Figs. S8, S9) | Field step values; temperature; residual field; whether eta is odd in B |
| Not time-dependent fluctuation | Fig. S12 | Device 14 | Fixed bias at 68, 70, 72 and 74 μA, about 20 min traces, sweeps #A and #B | Temperature; only two sweeps |
| Ti-doped (x = 0.24, no long-range CDW) shows no SDE after the same processing | Figs. S13, S14 | Device 15 (oxidized three times), Device 16 (etched) | Upper bound about 0.1% (Fig. S14). No CDW kink in R-T (Fig. S13b) | Number of Ti-doped devices; their thickness, Ic and Tc; field-trained data |

## Entries matched, skipped or adapted (step 2)
- Matched: diode-vortex-screening (diode family) and fine-tuning-and-selection (always included).
- Adapted: fine-tuning-and-selection, read as selection of sweeps and oxidation stages within a device as well as across devices. diode-vortex-screening applied as written; it fits thin films. Scope sentence in "What this is": critical-current nonreciprocity, not tunneling.
- Skipped:
  - protocol-parameter-sensitivity: no automated pass/fail protocol.
  - local-probe-loophole: specific to Majorana and local probes.
  - field-enhanced-supercurrent-resonances: needs a Josephson supercurrent that grows with field, which is not claimed.
  - All zbp, quantization, nonlocal, island, shapiro, charge, chiral and kitaev entries: no tunneling peak, quantized conductance, Shapiro step, island, fractional charge, QAH plateau or dot chain in this device.

## Checks walked (step 3)
- There is no diode checks family, so only the practice checks were walked:
  - report-counts: partly.
  - report-ranges: partly.
  - report-processing: partly.
- fine-tuning-and-selection is addressed by report-counts and report-ranges, both partly, so it is partly addressed.
- diode-vortex-screening has no addressing check in the library. I judged it against the entry's control (a control sample of the parent superconductor, plus tracking against field, width and edges).
  - It is partly addressed through the in-plane vortex argument in the Fig. S10 caption and the Ti-doped control.
  - The out-of-plane 0.1 to 0.2 T training sits in the vortex state of a film with an estimated out-of-plane Hc2 of about 0.85 T (Fig. S10 caption). The paper's vortex argument covers only the in-plane field.

## Sources held out
- None. No library source cites this paper by title, authors or arXiv ID. I searched the library for kagome, CsV3Sb5, 2608.26022 and the title and found no hits. Hou et al. 2205.09276 is cited by the paper (ref. 8), but it does not discuss it.

## Related work and outside sources: how checked
All six abstract pages were opened at arxiv.org/abs/<id>. ID, title and first author were confirmed, and each one-line description was checked against the abstract only. No full texts were read.
- 2309.00264, Le et al., abstract: field-free SDE in intrinsic flakes, polarity modulated by thermal history.
- 2506.04601, Ge et al., abstract: zero-field Ic asymmetry with random polarity on thermal cycling to 300 K; polarity follows a perpendicular field applied above the CDW transition.
- 2605.29665, Zhang et al., abstract: zero-field SDE and second-harmonic signals emerging with decreasing thickness.
- 2205.09276, Hou et al., abstract: SDE in Nb and V films at fields as small as 1 Oe, from vortex barriers and Meissner screening.
- 2205.12196, Golod and Krasnov, abstract: zero-field diode in Nb junctions; polarity switched by trapping or removing an Abrikosov vortex.
- 1303.2620, Murphy et al., abstract: switching-current distributions from phase slips in nanowire and graphene weak links. Used only as the source for the switching-statistics row.
- Found by searching and not used: 2508.15266, 2606.20157, 2505.22274, 2609.38003, 2610.30556, 2610.16972, 2210.16827, 2610.04446.
- arXiv API calls were spaced 3 to 4 s apart. Two queries came back empty, and there was no "Rate exceeded" message.

## Library gaps
1. No `checks` family for diode signals. Suggested steps:
   - a control film or junction of the parent material, measured under the same field history;
   - eta(B) in fine steps through zero, with the residual field measured;
   - separate Ic+ and Ic- distributions over many sweeps;
   - the onset criterion and excitation amplitude stated.
2. Trapped vortex or residual magnet field as a field-free, polarity-switchable diode (source: Golod and Krasnov, https://arxiv.org/abs/2205.12196). The current diode entry covers small applied fields, not trapped flux or memory.
3. Switching-current statistics: random-sign eta from independent stochastic switching in each direction, especially in inhomogeneous films (source: Murphy et al., https://arxiv.org/abs/1303.2620). The source shows switching distributions in general. It does not show a diode lookalike directly, so this gap is weaker.
4. Control-sample comparability: a doped or otherwise altered control changes more than the one order parameter. Not entered as a lookalike; raised in the report text.

## Unsure
- Device labels are inconsistent. Main text p. 5 gives Device 11 for Fig. 2 and Device 12 for Figs. S3 to S5. The Fig. S3 caption says Device 12 is Fig. 2, and Fig. S4 gives the p. 5 "Device 12" eta values for "Device 13 after successive oxidation stages". I raised this as question 8 and did not resolve it.
- Sweep protocol: both the forward and backward branches start at zero (Fig. 2 caption), so both are switching currents. I therefore left out heating and retrapping hysteresis as a lookalike.
- Iac = 10 μA appears in the Fig. S3 panels. Whether it is rms or peak, and whether the same value applies to Devices 13 and 14, is not stated.
- Status choice for diode-vortex-screening: I picked partly addressed over ruled out because the vortex argument covers the in-plane field only.
- Status choice for switching statistics: I picked partly addressed over ruled out because Fig. S12 tests fixed-bias telegraph switching on one device and does not show Ic distributions.
- Word count outside the table is about 910, slightly over the 600 to 900 aim, because of the template's fixed boilerplate.

## Skill issues
1. Step 3 assumes a checks family exists for every signature. There is none for diode, so only the practice checks could be walked, and flags.json can only hold library check IDs. The skill doesn't say what to do when a family has no checks.
2. Step 3 sets lookalike status from the addressing checks, but diode-vortex-screening is addressed by no check. I fell back on the entry's `control`; the skill could say so explicitly.
3. Outside lookalikes need a source URL, but table cells are limited to "one quote and one clause". It is unclear where the outside source URL goes in the report. I put it in the suggested-check cell or the related-work list.
4. Step 7 says to write `reports/<id>.md` and `.notes.md`. This run's instructions overrode that with inline output. The skill could allow an output-path argument.
5. The hold-out rule covers library sources only. It doesn't say whether related-work papers that cite the paper under review should be excluded. None did here.
6. "Read the supplementary material if it is in the PDF": with text-only input, the SI figures are known only from captions. The skill could tell runs to flag caption-only figure reads.
7. The "What this is" scope sentence plus the template boilerplate takes about 120 of the 600 to 900 word budget.
