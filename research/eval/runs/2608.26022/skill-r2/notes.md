# Run notes: arXiv 2608.26022v1

AI only. Lookalike assistant run on 2026-10-23. Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalike entries.

## What I read
- skill/SKILL.md, skill/report-template.md and library/lookalikes.yaml, including its `checks` section. I read each once, at the start.
- The paper's extracted text (eval/blind/k3/paper.txt): the main text, the 16 page numbers, the figure captions, and the supplement (Supp. pp. 1 to 17, which includes Table S1).
- The arXiv abstract page (eval/blind/k3/abs.html). It gives the title, 17 authors, the date 2026-08-26 and the abstract. It has no ancillary files and no comments.
- I did not fetch the paper in any form, as the prompt required. One arXiv API search ("superconducting diode" AND "stochastic") returned 2608.26022v1 as a hit, and I did not open it.
- There is no PDF. Figure details come only from the captions. The figure tick labels in the text extraction are scrambled, so I could not read curve shapes, the field steps in Fig. 4 or the full histograms.
- Data repository: none. The paper says the data are "available from the corresponding author upon reasonable request" (p. 9). There are no ancillary files, so I did not use read_mtx.py.
- Page numbers come from the "Page N of 16" footers in the text: the text above a footer is on that page. The supplement has its own page numbers, written "Supp. p. N".

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges | Missing |
|---|---|---|---|---|
| Pristine hBN-encapsulated CsV3Sb5 shows no field-free diode | Fig. 1, Figs. S1, S2, Table S1 | Devices 1 to 10 (top and bottom electrodes) | 10 devices; 21 to 76 nm thick; Ic 81 to 496.5 μA; 1.8 K; η upper bounds 0 to 0.4806% (Table S1 lists Devices 2 to 10) | Device 1 is not in Table S1; it is not stated whether these devices were measured under out-of-plane field |
| Oxidation activates a field-free diode | Fig. 2, Figs. S3, S5 | Device 11 (and Device 12 per p. 5) | Device 11: Ic about 115 to 37 μA after exposure; η = 83.61% in one of three sweeps at stage 2, zero of three at stage 3, one of three at stage 4; 1.8 K, B = 0; bias 0 to plus or minus 300 μA; ac 10 μA with 0.2 μA steps (Fig. S3 labels) | Number of oxidized devices made; device labels conflict (see below) |
| Asymmetric etching activates a field-free diode | Fig. 3, Fig. S7 | Devices 13 and 14 | Zig-zag etched pattern; Device 14 sweep rate 0.05 μA/s | Number of etched devices made; Device 13 sweep rate |
| Stochastic sign and size | Fig. 3d,e, Figs. S4, S6 | Devices 13, 12, 14 | 0.25 to 1.5 K in 0.25 K steps, 6 sweeps per temperature; Fig. S4: η = 17.07%, -30.86%, -14.07% in 3 of 6 sweeps | Total sweeps; the content of Fig. S6 beyond its caption |
| Field training | Fig. 4, Figs. S10, S11 | Device 13 (out of plane, -0.2 to 0.2 T, 9 sweeps per field); Device 14 (in plane 0.2 and 0.3 T; out of plane 0.1 T) | Hc2 perpendicular about 0.85 T; estimated parallel Hc1 0.59 T for d about 40 nm | Field step values; whether the remanent field was nulled; in-plane alignment |
| Field cooling does not remove the stochasticity | Figs. S8, S9 | Device 14 | Cooled at 1 T (out of plane and in plane), then field removed | Remanent field after removal |
| Not time-dependent fluctuations | Fig. S12 | Device 14 | Window 66 to 74 μA, 2 μA steps, about 20 min traces | |
| No diode without long-range CDW (Ti, x = 0.24) | Figs. S13, S14 | Device 15 (oxidized 3 times), Device 16 (etched) | η upper bound about 0.1%; one slower sweep (Fig. S14f) | Thickness, Tc, Ic and geometry next to Devices 11 to 14; measurements under field |

Instruments: PPMS (1.8 K) and a Triton dilution refrigerator (from 0.25 K). The number of cooldowns is not given; each oxidation cycle warms the device to 300 K (Fig. S3).

## Entries matched, skipped and adapted
- Matched: diode-vortex-screening (family diode) and fine-tuning-and-selection (always included).
- Adapted: the signature of diode-vortex-screening reads the diode as "finite-momentum or other exotic pairing". This paper reads it as CDW-inherited time-reversal symmetry breaking domains, and I applied the entry to that reading. The scope sentence sits under "What this is".
- Skipped: all zbp, quantization, nonlocal, island, shapiro, chiral and kitaev entries. The paper has no tunneling spectroscopy, quantized conductance, Majorana claim, Shapiro steps, chiral edge or dot chain.
- Also skipped:
  - field-enhanced-supercurrent-resonances: no supercurrent that grows with field is claimed.
  - charge-trap-fractional-shift and coulomb-dominated-interferometer: no fractional charge.
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol, although the onset criterion for Ic raises a related question (Q6).
  - local-probe-loophole: it is specific to Majorana modes.
  - micromagnet-stray-field: its signature is a zero-bias peak. The physics is similar (stray fields breaking time-reversal symmetry), and the outside row covers it.
- Checks walked: only the `practice` checks (report-counts, report-ranges, report-processing). The library's `checks` section has no diode family.

## Status reasoning
- diode-vortex-screening: Partly addressed. The paper's vortex argument (Fig. S10) covers only the in-plane 0.3 T training. The out-of-plane 0.1 to 0.2 T stabilization in Fig. 4 is not discussed against the Meissner and edge-barrier mechanism. Hou et al. show that mechanism is odd in field and larger with a serrated edge, which resembles the zig-zag Device 13. The Ti-doped etched control (Device 16) and the pristine devices also bear on this row, but I could quote only one item per cell.
- fine-tuning-and-selection: Partly addressed. The paper discloses the sweep fractions for Device 11 and Device 13 (Fig. S4: 3 of 6) and the ten pristine devices. The number of treated devices made is not stated.
- outside, trapped flux or vortices: Partly addressed. The paper never discusses trapped flux. The field-cooling data (Figs. S8, S9) and the Ti-doped control bear on it. I picked the weaker status because of how the skill words it ("the data bear on it; the paper doesn't discuss it").

## Sources held out
None. I checked the submission history of every library source and related paper I used: Hou v5 2023-02, Akrap v2 2026-03-25, Ge v2 2026-05-04, Le v2 2024-05, Zhang 2026-05 (opened, not listed), Golod 2022, Jiang 2025-12, and Frolov 2309.09368 v1 2023. All predate 2026-08-26, so none can cite the paper. I did not open Frolov or Akrap full texts.

## Related-work checks
- 2205.09276 Hou et al.: opened the abstract page and the full text (v5 PDF). Confirmed the ID, title, first author (Hou, Yasen), the sub-1 Oe diode, the serrated-edge result (~50% versus 21%) and the false in-plane diode at 0.01 degrees. The 0.5 Oe figure in Q5 is my own arithmetic: 0.3 T times sin(0.01 degree).
- 2512.05427 Jiang et al.: abstract page. Confirmed the title, first author (Jiang, Nan) and the poling-field sign control attributed to trapped flux. This is the source for the outside lookalike.
- 2205.12196 Golod and Krasnov: abstract page and full text (v1 PDF). Confirmed the trapped vortex plus nonuniform bias, and the vortex "controllably introduced and removed by short current pulses".
- 2309.00264 Le et al.: abstract page. Confirmed the title, first author (Le, Tian) and "polarity modulated by thermal histories".
- 2506.04601 Ge et al.: abstract page. Confirmed the title, first author (Ge, Jun), the random polarity across thermal cycles to 300 K, and the polarity following a field applied above the CDW transition.
- Opened and not listed (limit of five): 2605.29665 (Zhang et al., thickness-driven zero-field diode in CsV3Sb5) and 2301.07121 (Gutfreund et al., vortex diode).

## Library gaps
- No `checks` for the diode family. Suggested steps:
  - null the remanent field and sweep through zero in fine steps;
  - run a control sample of the same geometry;
  - calibrate the in-plane tilt;
  - log field and current history, and pole or reset between sweeps;
  - state the Ic criterion against the ac excitation.
- No entry for trapped flux or vortices giving a zero-field diode with a sign set by history (Jiang 2512.05427, Golod 2205.12196). I added it as an outside row.
- No entry for a misaligned "in-plane" field acting as an out-of-plane field (Hou 2205.09276, Supp.). It could be a source on diode-vortex-screening.
- No entry for confounds in a "removed ingredient" control: a doped control sample can differ in Tc, disorder, pinning and geometry, as well as the ingredient removed.

## Unsure
- The device labels conflict. Fig. S3 says "Device 12 (Fig. 2 in the main text)" while Fig. 2 is Device 11. Fig. S4 says Device 13 oxidized, while p. 5 gives the same η values to Device 12. I asked about this (Q8) and did not resolve it.
- The sign of η for sweep #5: the supplement text gives +30.86%, while the Fig. S4 panel and p. 5 give -30.86%.
- Whether the vortex row should be "not addressed" for the out-of-plane training. I kept "partly" because the in-plane argument and the doped etched control are partial controls.
- I did not recognize this paper (posted after my training data) and used no knowledge of its later history.

## Skill issues
- Step 3 says to walk the checks "for the paper's family", but the diode family has no checks. The skill does not say whether to build ad hoc steps from the entry's `control`. I walked only `practice` and said so.
- Step 7 says to write reports/<id>.md and .notes.md. This run's prompt forbade .md writes, and I followed the prompt.
- The Scope paragraph is about measurement type (for example qubit data). It is unclear whether a different reading of a matched family (time-reversal symmetry breaking domains in place of exotic pairing) counts as "adapting"; I treated it as adapting.
- Step 3 ties lookalike statuses to the checks, but an outside lookalike has no checks to walk. The skill could say to judge it against the cited paper's control directly; that is what I did.
- Verbatim quoting from a text extraction hits artifacts: lost hyphenation ("sweep-tosweep") and garbled math. The skill could say how to handle them. I chose quotes without artifacts.
- The template's "<short title>" conflicts with step 7's "Use the title on the arXiv abstract page". I used the full abstract-page title.
- The rule never to fetch the paper is not covered for arXiv API search results that list it.
- The 600 to 900 word target is hard to meet with the template's fixed boilerplate plus eight questions and five related-work lines. I landed at about 890 words outside the table.
