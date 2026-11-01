# Run notes: 2608.26022v1

- Library: lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 entries. Read SKILL.md, report-template.md and the full library once at the start.
- Paper: I read paper.txt (the full text, with the supplement, 33 PDF pages) and abs.html, which gives the title, the 17 authors, a submission date of 26 Aug 2026 and no ancillary files. I rendered PDF pages 13 to 33 to images and looked at Figs. 2, 3 and 4 and Figs. S6 to S14 to read field values, sweep counts and panel labels. I did not fetch the paper. The paper folder also holds other files (paper_planted.txt, prompt_*.txt and others). I did not open them.
- Data repository: none. Data are "available from the corresponding author upon reasonable request" (p. 9). There are no figure data files, so I did not run read_mtx.py.
- I did not recognize the paper. It postdates my training.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| No diode in pristine encapsulated flakes | Fig. 1d-f; Figs. S1, S2; Table S1 | Devices 1 to 10 (top and bottom electrodes) | Ten devices, 21 to 76 nm thick, Ic 81 to 496.5 uA, 1.8 K, zero field; eta upper bounds 0 to 0.48%; in-plane R(B) to 10 T. Sweeps per device: not stated |
| Oxidation activates a field-free diode | Fig. 2 (Device 11); Figs. S3, S4, S5 | Device 11; Device 12 (S3, whose caption says it is the "Fig. 2" device); S4 caption says Device 13 | Fig. 2: 1.8 K, 0 T, 0 to +/-300 uA, stages pristine, 1st, 2nd, 4th; eta 83.61%. SI p. 2: three sweeps per stage, the diode only in sweep 2 of stage 2 and sweep 2 of stage 4, none in stage 3, Ic lost at the final stage. S3: Iac 10 uA, steps 0.2 to 0.5 uA. S4: six sweeps, diode in #1, #5, #6 (17.07%, -30.86%, -14.07%) |
| Etching activates a field-free diode | Fig. 3a-c; Figs. S6, S7 | Devices 13, 14 | Device 13: Ic about 35 to 46 uA. Device 14: Ic about 67 to 77 uA, 0.05 uA/s, six sweeps |
| Diode is stochastic | Fig. 3d,e; Figs. S4, S6, S7, S12 | Devices 13 (T series), 14 | 0.25 to 1.5 K in 0.25 K steps, six sweeps each; S12: fixed bias 68 to 74 uA for about 20 min, two sweeps (#A, #B) |
| Persists after field cooling | Figs. S8, S9 | Device 14 | 1 T out of plane and 1 T in plane, field removed, six sweeps each; one field sign only |
| Field stabilizes the diode | Fig. 4; Figs. S10, S11 | Devices 13, 14 | Fig. 4: B out of plane at -0.2, -0.1, 0, 0.1, 0.2 T, nine sweeps each. S10: in plane 0.2 and 0.3 T, six sweeps each. S11: out of plane 0.1 T, six sweeps |
| No diode in Ti-doped control | Figs. S13, S14 | Device 15 (panels labeled Device 19 and Device #20), Device 16 (panel labeled Device 20) | x = 0.24; EDS and R-T without a CDW kink. Device 15: pristine plus three oxidation stages, Ic about 12 uA, Tc about 2 K. Device 16 (etched): five sweeps at 0.05 uA/s, one at 0.025 uA/s, eta upper bound about 0.1%. Zero field only; temperature not stated |

Missing counts: the total devices fabricated, the number processed by oxidation or etching, cooldowns, the temperature for the Device 14 data and the Ti-doped data, and the sweeps per pristine device.

Inconsistencies noted: device numbering across the main text, the Fig. S3 and S4 captions and the Fig. S13 and S14 panel labels (question 4 and question 1).

## Matching (step 2)

- Matched: diode-vortex-screening (family diode) and fine-tuning-and-selection (always).
- Adapted: diode-vortex-screening. Its source studies plain films and junctions. I applied it to exfoliated flakes and counted the pristine flakes and the processed Ti-doped flakes as partial equivalents of "a plain film of the parent superconductor" (part, because the Ti-doped devices were measured at zero field only and their superconducting parameters differ).
- Skipped: every zbp, quantization, nonlocal, island, shapiro, chiral, kitaev and charge entry (a different signal: no tunneling peak, quantization, Shapiro steps or fractional shifts); field-enhanced-supercurrent-resonances (the signal there is a supercurrent that grows with field, and this paper does not claim that); protocol-parameter-sensitivity (no automated pass/fail protocol); local-probe-loophole (no local probe of Majorana modes).
- Checks: the library has no `checks` for the diode family, so I walked only the three practice checks.

## Outside rows (library gaps)

- Trapped vortices: Golod and Krasnov 2022, https://arxiv.org/abs/2205.12196 (abstract page opened). A zero-field diode in Nb junctions from the stray field of a trapped Abrikosov vortex plus the self-field, with polarity switched by trapping or removing the vortex or by changing the bias configuration. Tests taken from that control: flux trapped or removed on purpose; bias configuration changed. Proposed library gap: a diode entry for trapped flux, with field-cool sign reversal and a warm-up reset as tests.
- Phase-slip switching statistics: Murphy et al. 2013, https://arxiv.org/abs/1303.2620 (abstract page opened). Switching current distributions from thermal and quantum phase slips in weak links. Tests: per-polarity switching distributions, their width against the spread in the Ic difference, plus the paper's own fixed-bias time traces (S12) as an equivalent test. Proposed library gap: a sweep-to-sweep stochasticity entry for diode and switching-current claims.

## Hold-out

No library source was held out. All the sources I used (Hou 2205.09276, Frolov 2309.09368 v1 from 2023, Akrap 2501.18631 v2 from 25 Mar 2026) predate 26 Aug 2026, so none can cite this paper.

## Related work verification

All checked against the abstract only (arXiv abstract page fetched for the title and first author; the API abstract was read for content): Le 2309.00264, Ge 2506.04601, Zhang 2605.29665, Rog 2606.20157, Hou 2205.09276, Golod 2205.12196, Murphy 1303.2620. All opened, and none dropped.

## Unsure

- Whether the Ti-doped processed devices count as the "plain film" test. I marked it part.
- The scatter of Ic per polarity is shown only as individual sweep panels (S4, S6, S7) and eta bars. I marked the distribution test part, because the paper never shows per-polarity histograms.
- Fig. 4 field values were read from the figure axis (five fields). The text names only 0.1 T and 0.2 T.
- The 10 uA ac excitation is listed only on the Fig. S3 panels. I do not know whether it applies to Devices 13 and 14.

## Skill issues

- The template's "What this is" hard-codes "topological transport". A diode paper on a bulk superconductor sits in the library's diode family but outside topological transport. The skill does not say whether this counts as in scope or as adapted.
- There is no `checks` block for the diode family, and the skill does not say whether to walk only the practice checks or to build family checks. I walked only the practice checks.
- For outside rows, the skill says to take the tests "from the control that paper describes". It does not say whether the paper's own equivalent test (here Fig. S12) may be added as a test row. I added it.
- "Judge the evidence the paper presents" is unclear for a multi-part claim (baseline, activation, stochasticity, training, doped control). The denominator for "all" versus "part" is ambiguous. I used the processed devices that carry the diode claim.
- Step 7 says to write reports/<id>.md. The run prompt overrode this, so I wrote no .md files.
