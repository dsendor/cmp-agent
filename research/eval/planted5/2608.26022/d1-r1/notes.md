# Run notes: arXiv 2608.26022v1

AI only. Lookalike assistant, 2026-10-24.

## Library
- lookalikes.yaml meta.version 0.5 (updated 2026-10-24); 28 lookalike entries.
- The diode family has one entry (diode-vortex-screening) and no `checks` block. Only the practice checks (report-counts, report-ranges, report-processing) applied.

## What I read
- The extracted text only, as instructed: /tmp/.../planted2/blind/r63/paper.txt. It holds the main text (pp. 1 to 16, with figure captions on pp. 12 to 16) and the supplement (supp. pp. 1 to 17: Supplementary Text, Table S1, captions of Figs. S1 to S14). Figure panels come through only as scattered axis labels and inset numbers. I could not see any figure image.
- I read pages from the "Page N of 16" footers. Text before each marker sits on page N.
- No PDF and no abstract page, as instructed. The arXiv title comes from an arXiv API search listing that returned the paper's own entry as a side effect of a related-work query: 2608.26022v1, "Symmetry Origins of the Field-Free Superconducting Diode Effect in the Kagome Superconductor CsV$_3$Sb$_5$", first author Xin-Jie Liu. It matches the title in the text. I did not open that entry's page.
- No ancillary figure data and no repository. The paper says data are "available from the corresponding author upon reasonable request" (p. 9). I did not run read_mtx.py.
- Could not open: nothing failed. Two arXiv API queries came back empty: diode + "switching current distribution" + statistic, and "remanent field" / "trapped flux" + diode.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Pristine hBN-encapsulated CsV3Sb5 shows no field-free diode | Fig. 1 (p. 13), Figs. S1, S2, Table S1 | Device 1 (Fig. 1); Devices 2 to 10 (Table S1) | Text says ten devices (p. 4); Table S1 lists nine (2 to 10). Thickness 21 to 76 nm; Ic 81 to 496.5 μA; Tc 3.80 to 4.36 K; η upper bounds 0 to 0.4806%; measured at 1.8 K. Number of sweeps per device not stated. Top- and bottom-electrode types. |
| Oxidation activates a field-free diode | Fig. 2 (p. 14), Figs. S3 to S5 | Device 11 (Fig. 2); Device 12 (Figs. S3 to S5) | Device 11: 1.8 K, 0 T, bias 0 to ±300 μA, four oxidation steps; Ic about 115 to 37 μA; η = 83.61% after the second step. Device 12: η from −30.86% to 17.07% (p. 5). Labels conflict: Fig. S3 says "Device 12 (Fig. 2 in the main text)"; Fig. S4 says Device 13 "after successive oxidation stages", six sweeps, and its panel labels carry the −30.86% and 17.07% values. |
| Asymmetric etching activates a field-free diode | Fig. 3 (p. 15), Figs. S6, S7 | Device 13 (zig-zag); Device 14 | Device 13: 0.25 to 1.5 K in 0.25 K steps, six sweeps per temperature. Device 14: sweep rate 0.05 μA/s; Ic window about 66 to 74 μA (Fig. S12). |
| The diode is stochastic in sign and size | Fig. 3, Figs. S4, S6, S12 | Devices 12, 13, 14 | Six to nine sweeps per setting. Fixed-bias time traces about 20 min in 2 μA steps, two sweeps (Device 14). |
| Field cooling does not remove the stochasticity | Figs. S8, S9 | Device 14 | 1 T out of plane and in plane, field removed before measuring. |
| Small fields stabilize the polarity | Fig. 4 (p. 16), Figs. S10, S11 | Devices 13, 14 | Device 13: −0.2 to 0.2 T, nine sweeps per field, field step not stated; 0.1 T fixes polarity, 0.2 T fixes amplitude. Device 14: 0.1 T out of plane stabilizes; in plane, 0.2 T still stochastic and 0.3 T stable. |
| No diode in Ti-doped CsV3−xTixSb5 (x = 0.24) after the same processing | Figs. S13, S14 | Device 15 (oxidized, three steps); Device 16 (etched) | R-T shows no CDW; η upper bound about 0.1%; slower sweep rate tried on Device 16 (Fig. S14f). Geometry and Ic beside Devices 12 and 13 not given. |
- Missing counts: total devices fabricated (numbering runs 1 to 16); oxidized or etched CsV3Sb5 devices made versus shown; cooldowns; total sweeps per device; field step near zero; residual magnet field. Instruments: PPMS and Oxford Triton dilution refrigerator.

## Entries matched, adapted, skipped
- Matched: diode-vortex-screening and fine-tuning-and-selection.
- Adapted: diode-vortex-screening is written for a diode "read as finite-momentum or other exotic pairing". I applied it to the paper's reading, TRS-breaking domains inherited from CDW order. I read "plain film of the parent superconductor" as the Ti-doped CsV3Sb5 devices processed the same way, and marked that test "part" because their geometry and Ic are not compared. Scope: this is a supercurrent-diode study in a kagome superconductor flake, outside topological transport proper. One sentence under "What this is" says so.
- Skipped, wrong signal: every zbp, quantization, nonlocal, island, shapiro, charge, chiral and kitaev entry. The paper has no tunneling spectroscopy, conductance value, microwave irradiation, Coulomb blockade, QAH film or dot chain.
- Skipped, specific reasons:
  - field-enhanced-supercurrent-resonances: no supercurrent-growing-with-field claim.
  - micromagnet-stray-field: no magnets in the device. The residual magnet field is folded into the diode-vortex-screening row.
  - protocol-parameter-sensitivity: no automated pass/fail protocol. The η extraction is covered under report-processing.
  - series-resistance-subtraction: no conductance value claimed.
  - local-probe-loophole: specific to Majorana modes.
  - charge-trap-fractional-shift: considered for the sweep-to-sweep jumps, but its signature is fractional shifts in dots.

## Sources held out
- None. No library source cites 2608.26022, its title or its authors (grep of the library).

## Related work, how checked
- I opened every arXiv abstract page and confirmed ID, title, first author and that the abstract supports the one-line description. I checked abstracts only, no full texts.
- 2309.00264 (Le): abstract says field-free diode with "polarity modulated by thermal histories".
- 2605.29665 (Zhang): zero-field diode emerging with decreasing thickness.
- 2205.09276 (Hou, also a library source): diode in Nb and V films at about 1 Oe from vortex barriers and Meissner screening.
- 2205.12196 (Golod): zero-field diode in Nb junctions from a trapped vortex plus self-field; polarity switched by trapping or removing a vortex or by changing bias configuration.
- 2406.19024 (Vedin): random switching current, with a distribution that depends on sweep rate, temperature and geometry.
- Also opened, not listed: 2210.11256 (Ghosh, "High-temperature Josephson diode"). Its abstract reports asymmetry in switching currents and their distributions, induced by small fields, in a vortex-based picture.

## Library gaps
- No `checks` for the diode family. Suggested steps:
  - residual field measured or nulled, with Oe-scale sweeps through zero;
  - signed mean η with its uncertainty over many sweeps;
  - a control sample with the same geometry;
  - current leads swapped.
- Outside row 1, trapped Abrikosov vortex plus self-field from nonuniform bias (Golod and Krasnov 2022, arXiv 2205.12196). Tests come from that paper's control (polarity changed by trapping or removing a vortex and by changing bias configuration).
- Outside row 2, stochastic switching-current distributions (Vedin and Lidmar 2024, arXiv 2406.19024). Tests come from that paper's dependence on sweep rate and temperature. I added the paper's own fixed-bias time traces (Fig. S12) as an equivalent test.
- The residual field of a superconducting magnet after ramps has no entry; it fits under diode-vortex-screening.

## Unsure
- Fig. S4 attribution: the text says Device 12; the caption says Device 13.
- Whether Fig. 3d,e reports a signed mean. The caption says "average diode amplitude", which I took as a magnitude.
- Whether the Ti-doped devices are fair plain-film controls for the vortex mechanism. I marked the test part.
- The field step in Fig. 4.
- I parsed Table S1 from flattened text and matched columns by order. The nine devices line up.
- Recognition: I did not recognize this paper and know nothing of its later history.

## Skill issues
1. The diode family has no `checks`, but the template's checks section and step 3 assume family checks exist. I used the practice checks only and said so in the report.
2. "Partly" is defined by evidence coverage ("one of the three devices"). It is unclear for a check done only in part across all the evidence (report-processing: η is defined, but there is no onset criterion and no data or code). I marked it partly.
3. Step 7 says write reports/<id>.md and notes.md. This environment refuses .md writes, so both are in the reply, per the prompt.
4. The Input section requires the abstract page and PDF, and "use the title on the arXiv abstract page". This test forbids both. The title came from an API search listing, and the skill does not say whether seeing the paper's own listing during a search is acceptable.
5. The diode test "plain film or junction of the parent superconductor" is ambiguous when the claimed order belongs to the parent itself. A doped control seems the natural equivalent; the skill could say so.
6. Outside rows: no guidance on how many tests to derive or how to word them, or on whether the paper's own extra controls (Fig. S12) count as tests.
7. Length: with template boilerplate and eight long questions, 600 to 900 words outside the table is tight. The report came out at about 914 words.
8. The hold-out rule covers library sources only. It says nothing about related-work searches that return the paper itself or later papers discussing it.
