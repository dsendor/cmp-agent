# Run notes: arXiv 2608.26022v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalikes.
- Skill and template: cmp-assistant/skill/SKILL.md and skill/report-template.md. Both were read once at the start.
- Run date: 2026-10-24.

## What I read
- The extracted text of the paper (main text p. 1 to 16 plus the Supplementary Materials p. 1 to 17), from the provided paper.txt. Per the run instructions I did not open the arXiv abstract page, the PDF or the HTML. The title comes from the paper text: "Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV3Sb5". The report shortens it in the header.
- Figures: only the captions, plus the axis text the extraction kept for Figs. S1 to S4 and S12. Figs. 1 to 4, S5 to S11, S13 and S14 have captions only. All figure detail comes from captions and running text.
- Data repository: none linked. The data are "available from the corresponding author upon reasonable request" (p. 9). There are no ancillary files, so read_mtx.py was not used.
- An arXiv API search (abs:"diode" AND abs:CsV3Sb5) listed the paper's own entry (2608.26022v1, title only) among the results. I did not open it.
- I did not recognize the paper and used no knowledge of its later history.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Pristine hBN-encapsulated CsV3Sb5 shows no field-free diode | Fig. 1d-f; Figs. S1, S2; Table S1 | Devices 1 to 10 (top and bottom electrodes) | 10 devices, all null; thickness 21.06 to 75.56 nm; Ic 81.4 to 496.5 μA; Tc 3.80 to 4.36 K; η upper bounds 0 to 0.48%; 1.8 K; in-plane field to ±10 T for magnetoresistance. Repeated sweeps per pristine device: not stated |
| Oxidation activates a field-free diode | Fig. 2a-d; Fig. S3 (supp. text) | Device 11 (main text); the S3 caption calls it Device 12 | 1.8 K, B = 0, bias 0 to ±300 μA; Ic about 115 to 37 μA after the first oxidation; η 83.61% in one of 3 sweeps at stage 2; stage 3, 0 of 3; stage 4, 1 of 3; final stage, no Ic. Iac 10 μA, steps 0.2 or 0.5 μA |
| Etching activates a field-free diode | Fig. 3a-c; Fig. S6; Fig. S7 | Device 13 (zig-zag etched); Device 14 (etched) | Device 13 in the dilution refrigerator; Device 14 sweep rate 0.05 μA/s |
| The diode is stochastic in sign and size | Fig. 3d,e; Figs. S4, S6, S12 | Device 13; Device 12 (main text) or Device 13 (S4 caption); Device 14 (S12) | 0.25 to 1.5 K in 0.25 K steps, 6 sweeps each; S4: 6 sweeps at 1.8 K, 3 with SDE (η 17.07%, -30.86%, -14.07%; I checked these against the listed Ic values); S12: fixed-bias time traces at 68 to 74 μA for about 20 min, stochastic window 66 to 74 μA |
| Out-of-plane field stabilizes the diode | Fig. 4; Figs. S10, S11 | Device 13; Device 14 | Fig. 4: -0.2 to 0.2 T out of plane, 9 sweeps per field, field step not stated; S10: in-plane 0.2 T still stochastic, 0.3 T stable; S11: out-of-plane 0.1 T |
| Diode persists after field cooling | Figs. S8, S9 | Device 14 | Field-cooled at 1 T out of plane or in plane, then the field removed |
| Ti-doped (x = 0.24) devices show no diode | Figs. S13, S14 | Device 15 (oxidized, 3 stages); Device 16 (etched) | No CDW kink in R-T; η upper bound about 0.1% (S14); Tc, Ic and thickness not given; number of sweeps not stated |

Missing counts: total devices fabricated, oxidized or etched; how many showed the diode; why any were set aside; residual field at 0 T; field step in Fig. 4; onset threshold; repeated sweeps on pristine devices.

## Matching (step 2)
- Matched: diode-vortex-screening (diode family) and fine-tuning-and-selection (always).
- Skipped: every zbp, quantization, nonlocal, island, shapiro, kitaev, chiral and charge entry. The device has no tunnel probe, no zero-bias peak, no Josephson junction under irradiation, no quantum dot and no quantized signal.
- Skipped field-enhanced-supercurrent-resonances: the paper does not claim a supercurrent that grows with field.
- Skipped protocol-parameter-sensitivity: there is no automated pass/fail protocol.
- Skipped local-probe-loophole: it is specific to Majorana claims.
- Adapted: the scope sentence under "What this is" notes the paper is a diode study in a kagome superconductor. The library family exists, so no entry needed adapting beyond that.
- Checks: the library has no `checks` block for the diode family. I walked only the practice checks (report-counts, report-ranges, report-processing).

## Sources held out
None. No library source used here (Hou et al. 2022, Frolov et al. 2023, Akrap et al. 2026) cites this paper by title, authors or arXiv ID, judging from the library quotes and titles. I did not reopen library sources.

## Related work: how each was checked
All five were checked from the arXiv API abstract (id_list query), confirming ID, title, first author and the abstract statement used:
- 2309.00264v2, Tian Le et al.
- 2605.29665v1, Wei Zhang et al.
- 2205.09276v5, Yasen Hou et al. (also a library source)
- 2205.12196v1, T. Golod and V. M. Krasnov
- 2606.20157v1, Matthijs Rog et al.

None of these abstracts discusses the paper under review. Searches on switching-current histograms or stochastic switching in diodes, remanent field and phase slips gave nothing I could cite for an outside row, so I did not add one.

## Outside lookalike (library gap)
- Trapped Abrikosov vortex giving a zero-field diode whose polarity changes as vortices are trapped or removed (Golod and Krasnov 2022, https://arxiv.org/abs/2205.12196).
  - Tests come from that paper's control (trapping or removing the vortex): field history with nulled-field zero-field cooling, and field-cooled versus zero-field-cooled comparison.
  - Relevance: Devices 13 and 14 saw ±0.2 T out-of-plane series and 1 T field cooling, and each switching event heats the device.

## Library gaps
- The diode family has no `checks` block. Candidates: residual-field calibration at nominal zero field; field history and zero-field cooling; a control sample of the parent superconductor in the same geometry; switching-current statistics per direction.
- No entry for a trapped-vortex zero-field diode (Golod and Krasnov 2022).
- No entry for ordinary switching-current statistics or multi-path switching in inhomogeneous films as a source of sweep-to-sweep sign changes. I found no citable paper in this run, so I raised it as a question only.
- No entry for "a control sample differs in more than the intended variable" (here, Ti doping changes disorder and superconducting parameters as well as the CDW).

## Unsure
- The Fig. 4 field step and whether η changes sign with the sign of B. The caption gives only "-0.2 and 0.2 T" with nine sweeps per field.
- Device numbering conflicts:
  - Main text: Fig. 2 is Device 11; Device 12 is oxidized with η from -30.86% to 17.07%, citing Figs. S3 to S5; Device 13 is etched.
  - SI: the S3 caption calls the Fig. 2 device "Device 12"; the S4 caption and the Supplementary Text call the oxidized six-sweep device "Device 13".
  - I followed the main text in the report and raised the conflict as question 6.
- Main text p. 5 says the out-of-plane evolution is also seen in Device 14 "(Figs. S10 and S11)", but the S10 caption describes an in-plane field.
- Fig. S10's Hc1 argument uses d of about 40 nm. Device 14's thickness is not given, and the argument covers in-plane fields only; the main-text training field is out of plane.
- Fig. S12 axes read nV for some traces and mV (about 46 to 48 mV) for others. That suggests a normal-state resistance of hundreds of ohms, while other dV/dI plots read a few ohms. These are extraction artifacts or device differences I could not resolve, so I left them out of the report.
- Ti-doped etched Device 16 as a "plain film" equivalent: marked part, because its superconducting parameters are not compared.

## Skill issues
- The skill says to walk "the checks for the paper's family", but the diode family has none. It does not say whether to adapt checks from another family or use the practice checks only. I used the practice checks only.
- The template's "What this is" frames the library as "topological transport". For a diode paper the scope sentence carries the adaptation, but the template line still reads slightly off.
- The flags format has a `note` field for every status. The skill only defines notes for "Not tested", so I set note to null for "Tested in part".
- For outside rows, the skill says to take tests "from the control that paper describes". When the paper is a device demonstration (Golod and Krasnov) with no stated control, the test wording is my adaptation.
- The Input section expects the abstract page and PDF. This run supplied text only, so the title came from the paper text.
