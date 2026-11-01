# Run notes: arXiv 2608.26022v1

## Library and inputs

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalike entries, checks for families zbp, shapiro, kitaev, charge and practice.
- Skill: cmp-assistant/skill/SKILL.md and skill/report-template.md, read once at the start.
- Paper: extracted text only (paper.txt, main text pp. 1 to 16 plus supplement pp. S1 to S17) and the saved arXiv abstract page (abs.html). Version v1, submitted 26 Aug 2026, 33 pages, 18 figures. No PDF, so figure details come from captions and the extracted axis text. Page numbers follow the "Page N of 16" markers in the main text and the bottom page numbers in the supplement.
- Ancillary files: none listed on the abstract page. Data repository: none ("available from the corresponding author upon reasonable request", p. 9). read_mtx.py not used (no .mtx files).
- Not opened: the paper's own arXiv pages (by instruction). One arXiv API search result listed 2608.26022 by ID and title; I did not open it.
- Recognition: I did not recognize this paper (it postdates my training data). No knowledge of later history was used.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges | Missing |
|---|---|---|---|---|
| Pristine encapsulated CsV3Sb5 has no field-free diode | Fig. 1 (p. 13), Figs. S1, S2, Table S1 (pp. S3 to S5) | Device 1 plus Devices 2 to 10 (ten) | 1.8 K, B = 0; thickness 21 to 76 nm; Ic 81 to 496.5 μA; η upper bounds 0 to 0.48% (Table S1); top- and bottom-electrode fabrication | Repeated sweeps per device; temperatures below 1.8 K; dilution-fridge data for pristine devices |
| Oxidation turns on a field-free diode | Fig. 2 (p. 14), Figs. S3, S5 | Device 11 (Fig. 2), Device 12 (Fig. S3 per caption) | 1.8 K, B = 0, sweeps 0 to ±300 μA; Ic 115 to 37 μA after first oxidation; η 83.61% at second oxidation; four or more oxidation steps; AFM after three steps | Onset criterion; number of sweeps per oxidation step; how many devices were oxidized |
| Etching turns on a field-free diode | Fig. 3a to c (p. 15), Fig. S7 | Devices 13, 14 | Zig-zag etch (Device 13), second etched device (Device 14), sweep rate 0.05 μA/s for Device 14 | How many devices were etched; Device 13 sweep rate (S12 implies about 3 minutes over 8 μA) |
| Diode is stochastic in sign and size | Fig. 3d,e; Figs. S4, S6, S12 | Devices 13, 12 (S4 labeled 13), 14 | 0.25 to 1.5 K in 0.25 K steps, six sweeps per temperature; Device 12 η from -30.86% to 17.07% over six sweeps; S12 time traces 68 to 74 μA, about 20 minutes | Total zero-field sweeps; histograms for other devices |
| Small out-of-plane field stabilizes the diode | Fig. 4 (p. 16); Figs. S8 to S11 | Devices 13, 14 | -0.2 to 0.2 T out of plane, nine sweeps per field (Device 13); 0.1 T out of plane and 0.3 T in plane fix Device 14, 0.2 T in plane does not; 1 T field-cooling, out of plane and in plane, then removed: stochastic diode persists | Field steps; residual field at nominal zero; how the magnet was zeroed; sign of η versus sign of B |
| Ti-doped (x = 0.24) devices without long-range CDW show no diode | Figs. S13, S14 (pp. S16, S17) | Device 15 (oxidized, three steps), Device 16 (etched) | Upper bound of η about 0.1%; one slower-sweep run (S14f); single doping level | Tc, Ic, thickness, measurement temperature; field data; number of sweeps |

Other counts: 16 devices named in total (1 to 10 pristine, 11 and 12 oxidized, 13 and 14 etched, 15 and 16 Ti-doped). Cooldowns are not counted. Two cryostats (PPMS, Triton dilution refrigerator); which device was measured in which is only implied by temperature.

## Matching (step 2)

- Matched: diode-vortex-screening (signature: nonreciprocal supercurrent read as exotic pairing; the paper reads it as TRS-breaking CDW-derived domains, which is the same kind of claim), fine-tuning-and-selection (always included).
- Outside the library: trapped Abrikosov vortex (Golod and Krasnov 2022, arXiv 2205.12196, abstract checked). Control from that paper: trapping or removing a vortex switches the nonreciprocity on and off and changes its polarity, so a field-nulled warm-up above Tc and correlation of polarity changes with excursions to the normal state test it.
- Skipped, with reason: all zbp, quantization, nonlocal, island, kitaev and chiral entries (no tunneling spectroscopy, quantized conductance or Majorana claim); shapiro entries (no microwave data); field-enhanced-supercurrent-resonances (no claim of supercurrent growing with field); charge entries (no fractional charge claim); micromagnet-stray-field (signature is zero-bias peaks; the stray-field idea is covered by the residual-field question under the diode row); protocol-parameter-sensitivity (no automated pass/fail protocol); local-probe-loophole (no Majorana or local-probe claim).
- Adapted: none in the sense of the scope rule (the diode family is listed in the library). Checks: the library has no diode checks, so only the practice checks (report-counts, report-ranges, report-processing) were walked.

## Statuses, with the reason for each borderline call

- diode-vortex-screening: partly addressed. The Ti-doped etched control and the pristine devices bear on it, and the paper rules out "a trivial by-product of surface processing" (p. 6). Not ruled out, because the library control also asks for tracking against field near zero, width and edge quality, and residual field, which the paper doesn't report.
- Trapped vortex (outside): partly addressed; the field-cooling runs (Figs. S8, S9) and the Ti-doped control bear on it without discussing vortices. Picked the weaker status since nothing addresses a remanent field after the 1 T excursion.
- fine-tuning-and-selection: partly addressed; pristine counts are given, the inversion-broken counts and sweep totals are not.
- Checks: all three "partly". report-processing could be read as "not done" (no data or code released); I gave "partly" because Eq. (1) and the onset definition are stated.

## Hold-out

- Searched the library for "kagome", "CsV3Sb5", "2608.26022" and the first author: no matches. No library source was held out. Hou et al. (2205.09276) is cited by the paper (ref. 8) but predates it and does not discuss it, so it stays.

## Related work, how each was checked

All five abstract pages fetched from arxiv.org/abs; ID, title, first author and the one-line description checked against the abstract (abstract only, no full text):
- 2205.09276, Hou et al., abstract.
- 2205.12196, Golod and Krasnov, abstract.
- 2309.00264, Le et al., abstract (this is the paper's ref. 17).
- 2506.04601, Ge et al., abstract (the paper's ref. 39).
- 2605.29665, Zhang et al., abstract. Earlier than the paper under review, so it cannot discuss it.
arXiv API searches used: abs:CsV3Sb5 AND abs:diode; diode AND trapped AND vortex; title "diode-with-memory"; kagome AND nonreciprocal AND trainability; superconducting diode AND remanent; superconducting diode AND stochastic. Waited 3 s between calls; no rate limiting.

## Library gaps

- No checks section for the diode family. Candidate checks: report the residual field at nominal zero and how it was nulled; show η against small fields of both signs; run the same geometry in a control superconductor; test for trapped flux (field-nulled warm-up above Tc).
- No entry for trapped vortices or remanent magnet field giving a zero-field diode (source: Golod and Krasnov 2022, arXiv 2205.12196).
- No entry for switching-current statistics in inhomogeneous films (stochastic premature switching or heating producing sweep-to-sweep scatter in η). The paper addresses time-dependent fluctuations itself (Fig. S12); I found no paper to cite for this, so it is not in the report.

## Unsure

- Whether Fig. 4's fixed polarity follows the sign of B. The caption says "The field fixes the diode polarity", which suggests it, but I can't read the figure. The report asks.
- Device labeling in the supplement (Fig. S3 says Device 12 is Fig. 2; Fig. S4 labeled Device 13 shows Device 12's η values). Asked as question 8.
- Page numbers for supplementary figures are taken from the bottom page numbers in the extracted text.

## Skill issues

- The checks section has no diode family, so flags.json carries only the practice checks. The skill doesn't say whether to draft family checks when none exist; I didn't.
- The scope rule covers "a different kind of measurement" but not an in-scope family with a single entry. I put one sentence in "What this is" saying so; unclear if that is wanted.
- The template header asks for a short title while step 7 says "Use the title on the arXiv abstract page". I used a short title in the header and gave the full arXiv title on the next line.
- Step 5's outside-library rule asks me to "judge it against the control that paper describes"; with only the abstract checked, the control is inferred from one sentence ("by trapping/removing a vortex"). The skill doesn't say whether abstract-level checking is enough for an outside row.
- Step 7 says to write reports/<id>.md and .notes.md; in this run the report and notes go in the reply per the prompt.
- Adding a short prose note under the Lookalikes table is not in the template; I added one paragraph to reach the word target and explain the vortex rows.
- An arXiv API search can return the paper under review; the skill could say to skip it in result listings.
