# Run notes: arXiv 2608.27444v1

- Library: lookalikes.yaml, meta.version 0.5 (updated 2026-10-24). It has 28 lookalike entries.
- What I read: SKILL.md, report-template.md, lookalikes.yaml (all entries, tests and checks), and the extracted paper text with the main text, Methods and Supplementary Sections D to M. I collapsed the whitespace into a working copy under the scratchpad work folder.
- What I couldn't open: there was no PDF or abstract page, by instruction. Figure details come from captions only, so I could not see the stripe slope signs, the DC-bias diamond shapes or the histograms. The title comes from the paper text and matches the arXiv API listing for 2608.27444v1, which appeared in a search result; I did not open the paper's own page. Data are "upon reasonable request", so no repository was used. There were no ancillary files, so read_mtx.py was not used.
- Page numbers: taken from the page markers in the extracted text (main text pp. 1 to 10, supplement pp. 13 to 31). The marker sits at the top of each page's text in this extraction.
- Recognition: I did not recognize the paper or know of any later history.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| e/4 charge addition at ν = −5/2, −1/2, 3/2 (ΔV/ΔV1 = 0.27, 0.24, 0.25 ± 0.03) | Fig. 2a,b,d, 2e,f,h; Fig. 4b; Figs. S8, S9, S11 | One device (Methods: "The device was measured") | B = 14 T; ΔV 56 to 63 mV; ΔB = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT (p ≈ 10, 2, 6); field step 1 mT, NB ≈ 101 points; Iac 0.2 to 1 nA; T base about 10 mK, electron T 30 to 50 mK stated |
| e/3 at ν = 2/3 (0.32 ± 0.03), validated by repeated sweeps | Fig. 2c,g; Figs. S10, S13 to S15 | Same | 20 repetitions at fixed B; several fields |
| Calibration: ν = −1 at 10 T as reference (ΔV1 = 233 ± 14.3 mV, ΔB1 = 40.3 ± 6.7 mT); −4/3 gives 0.37 ± 0.04; ν = −2 gives e | Fig. 1e to h; Figs. S3, S4, S5 | Same | Four data points in Fig. S3 (ν = −1 at 10 T and 14 T, ν = −2 at 10 T, ν = −4/3 at 14 T) |
| Crossover to doubled gate period with side-gate coupling at −5/2, −1/2, 2/3, 3/2; none at −4/3, −1/3 | Fig. 3, Fig. 4; Figs. S6, S7 | Same | Vsg 0.2, 2, 5 V at −4/3; −2 and 0 V at −1/3; safe limit about 6 V (5 V max used) |
| Temperature dependence | Figs. S16, S17 | Same | T = 16, 30, 50, 70, 95, 120 mK (12.7 to 70 mK for panel a); B = 13.95 T |

Missing counts: devices fabricated (the author contributions say "devices"), devices measured, cooldowns, ADG and B ranges beyond those shown, side-gate settings tried, and why the developing states +1/2 and +5/2 were not measured.

## Entries matched, adapted, skipped

- Matched: coulomb-dominated-interferometer (adapted), charge-trap-fractional-shift (adapted), and fine-tuning-and-selection (always applies).
- Adapted:
  - coulomb-dominated-interferometer: the paper is an antidot, and the reading runs the other way (CD is claimed, AB or mixed is the alternative). I took the tests from the entry unchanged.
  - charge-trap-fractional-shift: the claim is a period ratio, not a fractional shift. I treated the integer-filling electron period as the "absent where not expected" test.
- Skipped:
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: there is no superconductor, zero-bias peak, Josephson junction, QAH film or dot chain.
  - local-probe-loophole: it concerns Majorana separation.
  - protocol-parameter-sensitivity: there is no pass/fail protocol. The FFT and Gaussian-fit choices are covered under report-processing and the questions.
- Checks walked: charge (charge-regime-map, charge-control-regime, charge-repeat-sweeps) and practice (report-counts, report-ranges, report-processing).

## Hold-out

No library source cites 2608.27444, its title or its authors (searched the library for "2608.27444", "Di Luca" and "antidot"). No sources were skipped.

## Related work checks

All five were checked through the arXiv API abstract (id_list query), confirming ID, title, first author and abstract content. I did not read any full text.
- 1201.1600 Kou: abstract.
- 2509.04209 Di Luca: abstract. This is the authors' earlier paper, listed for its own results.
- 2412.11401 Hata: abstract. It is also the source for the outside row.
- 2412.19886 Kim: abstract.
- 1010.4598 Halperin: abstract. It is also a library source.

I also considered cond-mat/0007383 (Kataoka et al., h/2e from compressible rings around an antidot) and checked its abstract. I dropped it as an outside row because the paper's own ν = −2 data (electron gate period, p = 2) already match the two-ring CD picture, and the mechanism does not predict a quarter gate period.

## Library gaps

- Filling-dependent antidot area or gate lever arm (Hata et al. 2024, arXiv 2412.11401). A charge read from a normalized gate period assumes the same lever arm and area at the reference and at the state. I built its tests from that paper's approach (area compared through the field period; an assumption of constant gate capacitance).
- The library has no antidot-specific entry. coulomb-dominated-interferometer covers interferometers only.
- There is no entry for quasiparticle bunching or doubled periodicity. The authors themselves leave that open.

## Unsure

- Stripe slope test marked "part": I can't see the figures, and the text gives both periods but not the slope sign.
- Gate leakage marked "no": the only statement is that two-probe resistance was monitored during fabrication etching, and no data are shown.
- The second-dataset test for fine-tuning-and-selection is marked "part" because of the temperature series (Fig. S16) and the doubled-regime maps from the same device. No extracted e/4 ratio is given from a second dataset.
- Possible text inconsistencies (Fig. 3 panel assignments on p. 6, "ν = −2/3" on p. 7, three different e/4 suppression temperatures) are put to the authors as one question. I did not use them to change any status.
- The capacitance model predicts about 330 mV against a measured 235 mV, and the paper calls this agreement (p. 14). I noted it and did not raise it.

## Skill issues

- The skill says to read the abstract page and PDF. This run supplied text only, so the title could not come from the abstract page.
- The charge family's lookalike entries assume interferometers or dots. Antidot experiments that claim CD charge addition invert the usual reading, and the skill does not say how to phrase an inverted lookalike name.
- In step 3, the "evidence presented" for a check like charge-control-regime is ambiguous: it is unclear whether calibration states (integer, −4/3) count as evidence for the e/4 claim.
- The template has no slot for the outside-row source URL inside the table. I cited the source in Related work.
- The skill gives a word target (600 to 900 outside the table) but does not say whether added commentary paragraphs are allowed beyond the template sections. I added a short "notes on the table" paragraph after the questions.
