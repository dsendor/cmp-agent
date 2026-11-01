# Run notes: arXiv 2608.19099v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 entries. Skill: cmp-assistant/skill/SKILL.md and report-template.md, read once at the start.
- Date of run: 2026-10-24. Output: AI only.

## What I read
- The extracted text of the paper only (main text, figure captions, references), as instructed. I had no PDF, no abstract page and no Supplementary Material. I took the title from the first lines of the text, since I could not use the abstract page.
- The paper does not link a data repository or code. There were no ancillary files, so I did not run read_mtx.py.
- I did not recognize the paper. It is dated 19 Aug 2026, after my training data.

## What I couldn't open
- The Supplementary Material (device #2, RMCD, micromagnetics, first-principles, sign-convention checks). Each item the paper says is "in SM" is marked shown in part.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| C1. Field-free diode, efficiency -15.2% after zero-field cooling, up to 35.7% in size after field training (45.3% at about -10 mT) | Fig. 1(c)-(e), Fig. 2(c), Fig. 3(b) | #1 | Current 0 to plus or minus 300 µA (Fig. 1(c)). Fig. 1 temperature not stated. Fig. 1(e) temperature series covers "the whole superconducting regime", values not in text. Sweeps per point not stated. |
| C2. Polarity programmable by field history | Fig. 2(a)-(c); Fig. 3(a) | #1 (Fig. 2), #3 (Fig. 3(a)) | Perpendicular field swept plus or minus 50 mT at 200 mK (#1). Training at plus or minus 6 T (#3), 705 µA excitation. No field sweep shown for #3. |
| C3. Nonmonotonic, hysteretic reversals with Bcf < 0 and Bcb > 0, read as inverted relative to ferromagnetic proximity | Fig. 2(c); SM | #1, "consistently" across devices; #2 in SM | Sign conventions checked in SM. Values of Bcf and Bcb not given in text. |
| C4. Mechanism: layered ferrimagnetism in CrBr3 plus a cubic odd-in-q GL term | Fig. 4(a)-(d); SM (RMCD, micromagnetics, DFT) | Simulation of a CrBr3 trilayer | CrBr3 and NbSe2 thicknesses not stated in the main text. |

Missing counts: devices fabricated; devices measured; how many showed the effect (at least #1, #2, #3 did); cooldowns (one zero-field cooling mentioned); datasets; field ranges beyond plus or minus 50 mT sweeps and 6 T training; in-plane field; sweep rates; the magnet's remanent field.

## Matching (step 2)
- Matched: diode-vortex-screening (family diode, the only diode entry) and fine-tuning-and-selection (always).
- Skipped:
  - All zbp, quantization, nonlocal, island, shapiro, charge, chiral and kitaev entries: no tunneling peaks, conductance quantization, Shapiro steps or charge signals in this paper.
  - field-enhanced-supercurrent-resonances: the claim is nonreciprocity at zero field, not supercurrent growing with field.
  - protocol-parameter-sensitivity: no automated protocol.
  - series-resistance-subtraction: no conductance value is claimed. The four-probe Ic is read from dV/dI peaks.
  - micromagnet-stray-field: it is written for Andreev states in dots giving zero-bias peaks. The physics that does carry over is a magnet's stray field breaking time reversal. I folded that into diode-vortex-screening, since Hou et al. include a ferromagnetic insulator (EuS), and put it in its suggested check and the report note.
- Entries adapted: none. The paper is in scope (diode family).
- Checks: the library has no `checks` block for the diode family, so I walked only the practice checks (report-counts, report-ranges, report-processing).

## Status reasoning
- diode-vortex-screening: field dependence is shown for device #1 only (Fig. 2). It is not shown for #3, and #2 is in the SM. No plain NbSe2 control is in the main text. The paper names the mechanism in the introduction but does not argue against it for its own devices. Status: tested in part.
- fine-tuning-and-selection: three devices are named, but totals and reasons are missing and selection is not described. Status: tested in part.
- Outside, trapped vortices (Golod and Krasnov 2022, ref. [23] of the paper): the test from that paper's control is removing or trapping a vortex and changing the bias configuration. The one zero-field-cooled value (Fig. 1(d), device #1) counts as part, because the magnet's zero is not calibrated. Status: tested in part.
- Outside, strain-induced field-free diode in NbSe2 (Li et al. 2025): the test from that paper's control is the B-odd versus B-even symmetry. The polarity reversal under opposite field history is shown for #1 (Fig. 2) and #3 (Fig. 3(a)), so I marked "all". The paper does not mention strain, so it cannot be "ruled out" (that needs the paper to conclude against it). I chose tested in part. That test alone also does not exclude a B-even part coexisting with the odd one.
- Question 5 (magnet remanence) is the one question no entry raises directly. It ties to diode-vortex-screening's data_that_reveals_it ("field sweeps near zero"). A remanent offset in a superconducting solenoid is opposite to the last excursion, which gives Bcf < 0 and Bcb > 0. That is the same pattern the paper reads as ferrimagnetic. I could not find an arXiv paper showing this for a diode measurement, so it is a question and not a table row.

## Hold-out
- No library source discusses this paper. Hou et al. 2023 (2205.09276) is cited by the paper as ref. [19]. That is the reverse direction, so I kept it. I did not open the 2026 versions of Akrap et al. (2501.18631v2) or Legg (2502.19560v2) to confirm they don't cite this paper. Both predate it in substance, and only Akrap is used (fine-tuning-and-selection).

## Related work: how each link was checked
All were checked against the arXiv abstract page (citation_title, citation_author and abstract), not the full text:
- 2205.09276: Hou, Yasen et al., title confirmed; abstract states the 1 Oe, Meissner screening and EuS 65% results.
- 2205.12196: Golod and Krasnov, title confirmed; abstract states the trapped Abrikosov vortex, self-field, above 70% efficiency and polarity switching.
- 2506.17651: Li, Jiaxu et al., title confirmed; abstract states Pt/Co/Nb, stray fields, vortex entry and pinning.
- 2610.30556: Zapata, Juan C. et al., title confirmed; abstract states 50 to 60%, AlN spacer, 35 to 40%, stray fields and vortex transport. It is later than the paper and is described for its own results.
- 2509.23707: Li, Jiajun et al., title confirmed; abstract states strain-induced field-free diode in NbSe2 with B-odd or B-even behavior.
- Opened, not listed: 2609.38003 (CuMnAs/Al), 2610.16972 (Mo2N/FePt), 2608.03072 (pressure-induced NbSe2 diode), 2402.16264 (NbSe2 nanobridge).
- arXiv API searches were spaced about 3 s apart. Several returned no entries.

## Library gaps
- No diode-family `checks` (for example: bare-superconductor control, calibrated zero field and magnet remanence, switching-current statistics, field-history protocol).
- No entry for trapped vortices or flux memory giving a history-dependent zero-field diode (Golod and Krasnov 2022, https://arxiv.org/abs/2205.12196).
- No entry for strain or structural asymmetry giving a field-free diode without a magnet (Li et al. 2025, https://arxiv.org/abs/2509.23707; Zhu et al. 2026, https://arxiv.org/abs/2608.03072).
- No entry for a magnet layer's stray field driving vortex entry, separable from exchange by a spacer (Zapata et al. 2026, https://arxiv.org/abs/2610.30556; Li et al. 2025, https://arxiv.org/abs/2506.17651). micromagnet-stray-field covers this only for zero-bias peaks.
- No entry for remanent field in the superconducting magnet shifting apparent zero-field crossings. I found no arXiv source.

## Unsure
- Page numbers are inferred from the page markers in the extracted text (p. 1 abstract and introduction, p. 2 Fig. 1 and the start of the results, p. 3 Fig. 2 and the Fig. 3(a) discussion).
- Whether the SM shows a bare NbSe2 control or a field calibration. If it does, the diode-vortex-screening tests would rise.
- The "all" mark for the strain test rests on polarity reversal with history in two devices. It is a judgment call.

## Skill issues
- The library has no `checks` for the `diode` family, although `meta.families` lists it. The skill does not say what to do when a family has no checks. I used the practice checks only.
- Step 3 says to judge "the evidence the paper presents" but doesn't say how to treat items the paper says are "in SM" when the SM is unavailable. I marked them part.
- The "Ruled out" rule needs the paper to "conclude against the lookalike". For an outside row the paper never mentions, a decisive test can only reach "tested in part". That is worth confirming as intended.
- The skill asks for the abstract-page title; this run forbade the abstract page, so the title came from the text.
- Outside rows need a cited paper, so a strong concern with no arXiv source (magnet remanence) can only appear as a question.
- Step 7 says to write reports/<id>.md and notes files. This run asked for them in the reply, which overrides that.
