# Run notes: arXiv 2609.38003v1

AI only. Lookalike library version 0.4 (meta.updated 2026-10-23). Run date 2026-10-23.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all 28 entries and the full checks section), each read once at the start.
- The paper's extracted text (paper.txt, 14 pages with Methods and Extended Data Figs. 1 to 5) and the arXiv abstract page (abs.html: title, 22 authors, submitted 2026-09-29, "14 pages, 4+5 figures"). No PDF was available, so all figure details come from the captions and the garbled axis labels in the extracted text.
- No ancillary files, so read_mtx.py was not used. The paper links no data repository and has no data availability statement, so I used no data repository.
- I did not fetch the paper itself. One arXiv API search ("superconducting diode" AND "remanent") listed the paper under review among its hits (title and metadata only). I did not open it.
- Page numbers come from the page headers in the extracted text. Page 1 has no number. Methods are on pp. 6 to 8 and the Extended Data on pp. 9 to 12; Extended Data Figs. 3 and 4 are on p. 11.

## What I couldn't open
- Nothing failed. I could not see the figures themselves, so the axis ranges below are read from tick labels in the extracted text and may be incomplete.

## Claims table (step 1)

| Claim | Figure | Device | Counts and ranges |
|---|---|---|---|
| Field-free diode after zero-field cooling, η about 7% | Fig. 3a (with switching histograms in the inset) | Bar along [010], 5 µm by 180 µm, four-terminal, 2.0 nm AlAs heterostructure | 50 sweeps per polarity; 20 mK base; switching defined at a 50 µV threshold with a 0.2 s step delay. Device count not stated. |
| A preparation field along [100] reverses the polarity; η approaches ±20% | Fig. 3b, c, d | Same bar | Preparation ±1 T along [100] (Fig. 3d axis); each point averages 8 sweeps per polarity |
| A preparation field along [010] gives a weak response with no systematic reversal | Fig. 3e | Same bar | Preparation ±4 T along [010] (axis) |
| A bar along [100] shows the same anisotropy | Extended Data Fig. 4 | Second superconducting bar | Same axis ranges (±1 T along [100], ±4 T along [010]); no histograms or I-V shown |
| Reven is hysteretic for fields along [100] and weak along [010]; the remanent Reven reverses with the preparation sign | Fig. 4a, b, c | Reference CuMnAs bar, 20 µm by 10 µm, from a different wafer "with 3 nm fully oxidized Al cap"; 5 K; ±4 mA | Field sweeps ±4 T along [100] and about ±2 T along [010] (axes); preparation "−5 to 5 T" in the text against ±4 T ticks in Fig. 4c |
| Easy axis along [100] | Extended Data Fig. 5 | A 10 µm by 10 µm region of the epilayer, about 100 K | Two polarization angles |
| Net moment below 3×10^-3 µB/Mn | Fig. 2b | 3 mm by 5 mm wafer pieces, "a series of samples" from edge to centre | Number of pieces and measurement temperature not stated |
| Proximity tuning: 2.0 nm barrier gives Tc ≈ 350 mK; 1.5 nm barrier stays normal to 20 mK | Fig. 2c, Extended Data Fig. 3 | Two heterostructures | Model gives a crossover at about 6 spacer layers |

Counts missing: bars fabricated and measured, chips, cooldowns, how the preparation fields are applied (vector magnet or rotation), any temperature dependence of η, and whether the two superconducting bars share a chip and a mounting.

## Entries matched, skipped and adapted
- Matched: fine-tuning-and-selection (always included) and diode-vortex-screening.
- Adapted: diode-vortex-screening. Its signature reads the diode as "finite-momentum or other exotic pairing". This paper reads it as time-reversal breaking imprinted by an antiferromagnet. The physics of the lookalike (Meissner screening and vortex barriers in an ordinary film under a small field) applies unchanged. I adapted the control to an Al/AlAs film without CuMnAs.
- Skipped:
  - micromagnet-stray-field: its signature is a zero-bias peak from Andreev states in a dot. I carried the stray-field idea through an outside row instead.
  - protocol-parameter-sensitivity: the paper has no pass/fail protocol. Its threshold and delay choices became question 8.
  - field-enhanced-supercurrent-resonances: there is no claim of supercurrent growing with field; the diode is measured at H = 0.
  - series-resistance-subtraction: there is no quantized value.
  - local-probe-loophole: it is specific to Majorana modes.
  - All zbp, quantization, nonlocal, island, shapiro, chiral, kitaev and charge entries: the paper reports none of those signals.
- Checks: the library has no checks for the diode family, so I walked only the three practice checks (report-counts, report-ranges, report-processing). All three came out partly done.

## Sources held out
- None. Every matched library source predates the paper (submitted 2026-09-29): Hou et al. 2205.09276 (latest version v5, February 2023), Frolov et al. 2309.09368 (v1, 2023) and Akrap et al. 2501.18631 (v2, 25 March 2026). For Akrap v2 I checked the date only, not the full text.
- The paper itself cites Hou et al. (its ref. 28). Being cited by the paper does not trigger the hold-out rule.

## Related work: how each link was checked
- 2205.09276, Hou et al.: abstract page (title and first author confirmed) and full text. The text is the source for the 1 Oe figure and for "a false “in-plane” magnetic field induced diode effect could easily be measured, with an offset between the magnetic field direction and the film plane by as small as 0.01˚" (p. 6). Fringing fields from an in-plane magnetized EuS layer are on p. 8.
- 2512.05427, Jiang et al.: abstract page and full text. Sources: "Such hysteresis can often arise from a stray magnetic field due to the superconducting magnet." (p. 4); the graphene calibration and the "≈ ±15 mT" shift (Appendix D, p. 10); out-of-plane poling (Appendix E); devices B to D (Appendix F).
- 2205.12196, Golod and Krasnov: abstract page only.
- 2506.17651, Li et al.: abstract page only.
- 2601.03366, Sachin et al.: abstract page only (the arXiv API id_list result matched it).
- Also opened but not listed: 2301.07121 (Gutfreund et al., abstract). Seen in search results only: 2206.00483 (Narita et al.), 2610.30556 and 2610.16972.
- The paper also cites Jiang (ref. 29), Li (ref. 30) and Sachin (ref. 10). I describe their own results only.

## Library gaps
1. The diode family has no checks section. Suggested checks:
   - a control film of the parent superconductor;
   - the residual field at the sample, measured and nulled with an in situ sensor, including its out-of-plane part;
   - a thermal cycle above Tc after preparation, to erase trapped flux;
   - a remount rotated relative to the magnet axes;
   - η against temperature and against a small applied field.
2. A zero-field diode from flux trapped by a poling field (Jiang et al. 2512.05427; Golod and Krasnov 2205.12196).
3. Remanence of the superconducting magnet, and misalignment of the field with the film plane (Jiang et al. Appendix D; Hou et al. p. 6).
4. Stray or fringing fields from a residual moment in an adjacent magnetic layer (Li et al. 2506.17651; Hou et al. on EuS).
   - The micromagnet-stray-field entry covers this physics only for zero-bias peaks.

## Things I was unsure of
- Status picks, each the weaker of two:
  - Residual magnet field: I chose partly addressed over not addressed. Extended Data Fig. 4 bears on an in-plane residual field, because field along current in the [100] bar should not give the in-plane diode. It does not bear on an out-of-plane part.
  - Trapped flux: I chose partly addressed over ruled out. The argument is correlational and rests on a bar from a different wafer measured at 5 K.
- Whether the dilution refrigerator has a vector magnet is not stated. The text says only that fields were applied "along [100]" and "along [010]". Question 6 rests on that point.
- My own estimate, kept out of the report: the SQUID bound of 3×10^-3 µB/Mn corresponds to µ0M of about 0.8 mT. I used a Mn density of 2 per a×a×c cell with a = 3.80 Å and c = 6.32 Å. The stray field at the bar edges would be much smaller for in-plane moments. This is unverified.
- The axis ranges (Fig. 3d ±1 T, Fig. 3e ±4 T, Fig. 4b about ±2 T) come from garbled tick labels.
- Recognition: I did not recognize this paper. Its ID is after my training data, and I used no outside knowledge of its history.
- Length: about 960 words outside the table, counting the fixed template boilerplate, a little over the 600 to 900 target.

## Skill issues
1. Step 3 assumes every family has checks. The diode family has none, and the skill doesn't say whether to derive checks from the entry's control. I used only the practice checks and put the diode controls in the table.
2. The template header asks for "<short title>", but step 7 says "Use the title on the arXiv abstract page". I used the full title.
3. Step 7 says to write reports/<id>.md and a notes file. It gives no fallback for an environment where .md writes are refused. I followed the run prompt.
4. The scope paragraph is unclear for a paper whose family is in the library but whose claim is not topological (the diode entry's signature says "exotic pairing"). I added one sentence under "What this is".
5. The word target of 600 to 900 "outside the table" doesn't say whether the fixed template text counts.
6. Step 5 sets no limit on outside rows and doesn't say whether one cited paper may support two rows (I used Jiang et al. for two).
7. Step 6 fixes four questions, asks for questions on each key figure's data choices, and caps the list at eight. That forced compound questions.
8. The rule "every partly addressed needs a quote" fits the "the data bear on it" case poorly. There the quote describes data that do not mention the lookalike.
9. There is no guidance on page numbers when working from extracted text, and no guidance on checking later versions of library sources for the hold-out rule beyond their dates.
10. The template's check line format "<check> : Done" has a space before the colon. I kept it.
