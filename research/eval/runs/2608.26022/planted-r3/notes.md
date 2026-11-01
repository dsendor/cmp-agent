# Run notes: arXiv 2608.26022v1

- Date: 2026-10-23. Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes.
- Read once at the start: skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml including the `checks` section.
- Paper: worked from the supplied extracted text (paper.txt: main text pp. 1 to 16 plus Supplementary Materials pp. 1 to 17) and the supplied abstract page (abs.html; title, 17 authors, submitted 2026-08-26, "33 pages,18 figures"). Per the task prompt I did not fetch the paper's abs, PDF or HTML. No figures were seen; figure details come from the captions and the scattered axis labels in the text (for example "Iac = 10 μA, step: 0.2 μA" in Fig. S3, and the |Ic| and η values printed in Fig. S4).
- Page citations: main text "p. N" follows the "Page N of 16" footers; supplement "SM p. N" follows its own page numbers.
- Ancillary data: none. scripts/read_mtx.py not used. The data repository: none; data are "available from the corresponding author upon reasonable request" (p. 9), so I did no counting from data.
- Recognition: I did not recognize this paper. I knew Hou et al. and Le et al. from training; I opened both abstract pages anyway.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Pristine encapsulated CsV3Sb5 shows no field-free diode | Fig. 1 (p. 13), Figs. S1, S2, Table S1 | Device 1, Devices 2 to 10 | 10 devices; thickness 21 to 76 nm; Ic 81 to 496.5 μA; η upper bounds 0 to 0.4806% (Table S1); 1.8 K; Device 1 Tc onset 4.08 K, zero 3.39 K; Device 1 not in Table S1 |
| Oxidation activates a field-free diode | Fig. 2 (p. 14), Figs. S3 to S5 | Device 11 (Fig. 2), Device 12 (Figs. S3 to S5) | 1.8 K, B = 0; sweeps 0 to ±300 μA; Ic 115 to 37 μA after first exposure; η = 83.61% after second oxidation (single sweep shown, count missing); Device 12 η from −30.86% to 17.07% over 6 sweeps |
| Asymmetric etching activates a field-free diode | Fig. 3 (p. 15), Figs. S6, S7 | Device 13, Device 14 | 0.25 to 1.5 K in 0.25 K steps, 6 sweeps each (Fig. 3d,e); sweep rate 0.05 μA/s for Device 14; rates for Devices 11 to 13 missing |
| Polarity and size are stochastic, not fixed by structure | Fig. 3, Figs. S4, S6, S8, S9, S12 | Devices 12, 13, 14 | Field-cooling at 1 T (out-of-plane, S8; in-plane, S9; one sign stated); time traces at 68 to 74 μA, about 20 min, two sweeps (S12) |
| Out-of-plane field stabilizes polarity then amplitude | Fig. 4 (p. 16), Figs. S10, S11 | Devices 13, 14 | −0.2 to 0.2 T, 9 sweeps per field (step size missing); in-plane 0.2 T still stochastic, 0.3 T stable (S10) |
| CDW-suppressed Ti-doped control shows no diode | Figs. S13, S14 | Device 15 (oxidized, three stages), Device 16 (etched) | x = 0.24; η upper bound about 0.1% (S14); Tc, Ic, thickness, sweep counts missing |

Missing everywhere: devices fabricated in total, processed CsV3Sb5 devices without a diode (if any), cooldowns, total sweeps per condition, residual field at "B = 0", magnet history.

Possible labeling inconsistencies: Fig. S3 caption says "Device 12 (Fig. 2 in the main text)" but Fig. 2 is Device 11; Fig. S4 is titled "Device 13 after successive oxidation stages" but holds the η values (17.07%, −30.86%) that p. 5 assigns to Device 12. Raised as question 4.

## Matching (step 2)

- Matched: diode-vortex-screening (adapted: its signature says "finite-momentum or other exotic pairing"; here the reading is internal TRS-breaking order tied to CDW; the mechanism and control carry over), fine-tuning-and-selection (always included).
- Skipped, with reason:
  - All zbp, quantization, nonlocal, island, kitaev and chiral entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode, island-states-coulomb-spacing, false-poor-mans-majorana, chiral-plateau-superconductor-short): no tunneling spectroscopy, zero-bias peaks, quantized conductance, islands, dot chains or QAH films.
  - shapiro entries (shapiro-landau-zener, shapiro-nonlinear-resistance, transparent-junction-pi-crossing, switching-jump-blind-region): no microwave irradiation and no Josephson junction.
  - field-enhanced-supercurrent-resonances: the claim is not a supercurrent growing with field.
  - charge entries (charge-trap-fractional-shift, coulomb-dominated-interferometer): no fractional shifts.
  - local-probe-loophole: Majorana-specific.
  - protocol-parameter-sensitivity: no automated pass/fail protocol. Your "sequential symmetry test" is qualitative; I covered its data-window sensitivity under the report-ranges and report-processing checks.
- Adapted for scope: diode-vortex-screening (signature wording), and the practice checks, used alone because the library has no diode check family.

## Checks (step 3)

- Family checks: none exist for `diode`. Practice checks walked: report-counts (partly), report-ranges (partly), report-processing (partly).
- Status reasoning:
  - diode-vortex-screening: partly. The pristine devices (no diode) and the etched Ti-doped Device 16 (no diode, same geometry route) bear on it. The paper cites Hou et al. (ref. 8) only as an example of field-requiring diodes and doesn't discuss the mechanism or the residual field. The field-training data (polarity fixed by sign of B) also fit this mechanism. The Ti-doped devices differ in more than CDW (Tc, Ic, disorder), so I picked the weaker status.
  - fine-tuning-and-selection: partly. Device counts are given for pristine and processed devices, but there is no total-made count and no sweep count for the headline 83.61%.
  - trapped flux (outside): partly. Field-cooling at 1 T (Figs. S8, S9) bears on it; one field sign is stated and trapped flux is not discussed.
  - stochastic switching (outside): partly. Fig. S12 addresses fixed-bias fluctuations for Device 14 over two sweeps. Separate switching histograms and the mean signed η are not shown. Weaker status chosen because the control covers one device.

## Hold-out

- No library source skipped. I grepped the library for "CsV3Sb5", "kagome" and "2608.26022": no hits. Every library source predates 2026-08-26 (latest: Akrap et al. PRB 113, 2026; Legg v2, 2026), and none is on kagome diodes.

## Related work (step 5), how each was checked

All checks used the arXiv abstract page (https://arxiv.org/abs/<id>), abstract only, no full text. I confirmed ID, title and first author on each, and checked that the one-line description matches the abstract.
- 2309.00264: Le, Tian (first author); title confirmed; abstract: field-free diode "with polarity modulated by thermal histories". Found via arXiv API ti:diode AND ti:CsV3Sb5. Cited by the paper as ref. 17.
- 2506.04601: Ge, Jun; title confirmed; abstract: polarity "changes randomly in repeated thermal cycling to 300 K" and follows a field applied above the CDW transition. Cited by the paper as ref. 39.
- 2205.09276: Hou, Yasen; title confirmed; abstract: diode in Nb and V films at "as small as 1 Oe", from asymmetric vortex barriers and Meissner screening. Also a library source.
- 2205.12196: Golod, T.; title confirmed; abstract: zero-field diode from self-field and a "trapped Abrikosov vortex", polarity switched by trapping or removing the vortex.
- 2512.05427: Jiang, Nan; title confirmed; abstract: zero-field diode with sign "controlled by the poling magnetic field", attributed to trapped flux. Used as the source for the trapped-flux row.
- 0804.2251: Sahu, Mitrabhanu; title on page: "Probing individual topological tunnelling events of a quantum field via their macroscopic consequences"; abstract: switching-current distributions from thermal and quantum phase slips. Used as the source for the stochastic-switching row only (not in the related-work list, to keep it at five).
- arXiv API calls spaced by about 3 s; no rate-limit replies.

## Library gaps

1. No `checks` family for `diode`. Suggested steps: fine field sweep through zero with the residual field reported; a control film or junction of the parent superconductor; trapped-flux tests (poling with both signs, warm-up above Tc); separate switching histograms and the mean signed η.
2. Trapped magnetic flux or vortices as a zero-field diode source (Golod and Krasnov 2205.12196; Jiang et al. 2512.05427). Not in the library.
3. Stochastic switching (phase slips) making sweep-to-sweep η random when the true asymmetry is below the switching width (Sahu et al. 0804.2251 for switching distributions). Not in the library.
4. diode-vortex-screening's signature names only "finite-momentum or other exotic pairing". Claims of TRS-breaking order (loop currents, chiral CDW) inferred from a diode would match more cleanly if the signature named them.
5. Possibly: residual field of superconducting magnets at nominal zero as its own practice check (it applies to any "field-free" claim).

## Unsure

- Whether the Ti-doped etched device counts as the "equivalent" of the entry's control (a plain film of the parent superconductor). I treated it as partial because Ti doping changes more than CDW order.
- Whether Fig. S12 should count as ruling out stochastic switching for Device 14 alone. I kept it at partly.
- Fig. S4 versus main-text device labels (see above).
- The "upper bound of the SDE efficiency η" in Table S1 has nonzero values up to 0.48%. The paper calls these "no discernible" diode; I didn't treat it as a finding.

## Skill issues

1. Step 3 assumes a check family exists for the paper's signal. `diode` has none, so only practice checks applied. The skill doesn't say what to do then; I said so in the report.
2. Step 7 says to write reports/<id>.md and reports/<id>.notes.md. The task prompt asked for the text in the reply and flags.json in out-r3/, so I followed the prompt.
3. The Input section says to read the PDF at arxiv.org. The prompt forbids fetching the paper, so I worked from the extracted text and captions. The skill has no rule for text-only input (for example how to cite pages when the main text and the supplement are numbered separately); I used "p. N" and "SM p. N".
4. The hold-out rule covers library sources only. It doesn't say whether related-work papers that cite or are cited by the paper (here refs. 17 and 39) need any handling.
5. The template's question list shows five numbered items while step 6 allows up to eight. It is unclear whether the four standard questions must come first verbatim when the paper partly answers them. I kept them first and noted where the paper answers.
6. Step 2 says "Skip entries that can't apply". It doesn't say whether a family-level skip (all zbp entries) can be noted as a group; I grouped them.
7. Outside rows: the template table has no column for the outside source's URL. I put the URL in the Lookalike cell.
8. "Every 'ruled out' and 'partly addressed' needs a short verbatim quote": the extracted text has math-italic glyphs and merged hyphenations (for example "fieldfree"), so I chose quotes that avoid those spans.
9. The scope sentence goes under "What this is", but the template's "What this is" paragraph is fixed text. I appended the sentence to it.
