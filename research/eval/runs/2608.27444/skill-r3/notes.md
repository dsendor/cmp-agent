# Run notes: arXiv 2608.27444v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes plus the checks section.
- Skill files read once at the start: skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml. scripts/read_mtx.py was not needed (no .mtx or ancillary files).
- Date of run: 2026-10-23.

## What I read

- arXiv abstract page (local copy, abs.html): title "Trapping $e/4$ quasiparticles in bilayer graphene", authors Di Luca, Hajigeorgiou, Ma, Waldherr, Watanabe, Taniguchi, Banerjee; v1 submitted 27 Aug 2026. Version used: v1, as given. No ancillary files are listed on the abstract page.
- Full text: local paper.txt (layout extraction), checked against the local paper.pdf (31 pages; I ran pdftotext without layout to confirm quotes broken up by the two-column layout). Main text pp. 1 to 12, Methods pp. 9 to 10, Supplementary Material pp. 13 to 31 (Figs. S1 to S18). I read all of it.
- Per the run instructions I did not fetch the paper itself from arXiv.
- Data repository: none. "The data supporting the findings of this study are available from the corresponding author upon reasonable request" (p. 10). So I counted devices, datasets and ranges from the text and captions only.
- Couldn't open: nothing I tried failed.

## Claims table (step 1)

| Claim | Figures | Device | Numbers given |
|---|---|---|---|
| Localized e/4 charge at ν = −5/2, −1/2, 3/2 (minimal-excitation, weak coupling) | Fig. 2a,b,d; 2e,f,h; Figs. S8, S9, S11 | the one device, B = 14 T | ∆V/∆V1 = 0.27 ± 0.03, 0.24 ± 0.03, 0.25 ± 0.03; ADG periods 56 to 63 mV; ∆B = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT; stated p ≈ 10, 2, 6 (p. 4) |
| Localized e/3 at ν = 2/3 | Fig. 2c,g; Figs. S10, S13 to S15 | same, 14 T | ∆V/∆V1 = 0.32 ± 0.03; ∆B1/∆B = 2.32 ± 0.93; histogram cross-check ∆B = 19.6 ± 4 mT; 20 repeated sweeps in Fig. S13, first 6 show hysteresis |
| Calibration of the ADG against integer and odd-denominator states | Fig. 1e to h; Figs. S3 to S5 | same, 10 T and 14 T | reference ν = −1 at 10 T: ∆V1 = 233 ± 14.3 mV, ∆B1 = 40.3 ± 6.7 mT; ν = −4/3: 0.37 ± 0.04 and ∆B1/∆B = 3.47 ± 0.79; TG ratio 2.9 ± 0.6; AD diameter 361 ± 30 nm against lithographic ~210 nm; ν = −2 gives e and p = 2 |
| Crossover to a doubled gate period with side gates at −5/2, −1/2, 2/3, 3/2, absent at −4/3 and −1/3 | Fig. 3; Fig. 4; Figs. S6, S7 | same | ratio ∆Vdouble/∆Vminimal ≈ 2; field ratios scattered; ν = −4/3 at Vsg = 0.2, 2, 5 V; ν = −1/3 at −2, 0 V; ν = −1/2 doubled ∆B estimated from a half period (Fig. S9) |
| Temperature dependence separates ν = −1/2 doubling | Figs. S16, S17 | same, 13.95 T | T = 16, 30, 50, 70, 95, 120 mK (12.7 to 70 mK in S16a); e/4 suppressed at 50 to 70 mK; doubled at −1/2 and 2/3 visible to 120 mK; AB and CD fits indistinguishable up to T ≈ 2 T0 |

Counts:
- Devices fabricated: not stated ("M.D.L. fabricated the devices", p. 9, plural).
- Devices measured: one implied ("The device was measured", p. 9). Showing the effect: that one.
- Cooldowns: not stated.
- Datasets: one ADG against B map per filling and regime, plus DC-bias, histogram and temperature series in the supplement. Full datasets are given per filling (Figs. S8 to S12).
- Ranges: B = 14 T main (13.95 T for the T series) and 10 T reference. Field scans typically 101 points at 1 mT. Side gates limited to about 6 V by the risk of shorting (5 V maximum used). Excitation 0.2 to 1 nA, chosen per filling. Electron temperature 30 to 50 mK stated. Displacement-field and ADG ranges appear only in the figure axes.
- Fillings measured are marked in Fig. 1d. Developing states +1/2 and +5/2 are mentioned (p. 2) with no oscillation data.
- Missing counts: devices fabricated or measured, cooldowns, number of gate tunings tried.

## Entries matched, skipped and adapted

Family: charge (fractional periodicity in a quantum Hall device). I walked the checks for charge (charge-regime-map, charge-control-regime, charge-repeat-sweeps), then practice (report-counts, report-ranges, report-processing).

Matched:
- coulomb-dominated-interferometer. Adapted: the entry is written for a Fabry-Perot interferometer read as AB interference. Here the risk runs the other way: the charge reading needs the CD regime, and an AB or mixed regime would break it. The paper itself frames the CD/AB question with Ref. [48], so the entry's control (stripe slopes and spacings in the B and gate plane) carries over.
- charge-trap-fractional-shift. Adapted from "fractional shifts" to a fractional period. A capacitively coupled trap or side dot charging along the ADG sweep would add jumps that distort peak-spacing histograms and the 2D-FFT. The ν = 2/3 instability data bear on it.
- fine-tuning-and-selection (always included).

Skipped:
- All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries. There is no superconductor, Josephson junction, Majorana claim or nonreciprocity in this device.
- local-probe-loophole: about Majorana component separation; not applicable.
- protocol-parameter-sensitivity: the paper uses no pass/fail protocol. Its window and resolution point does bear on the FFT period extraction (the line of largest amplitude is selected, and ν = −1/2 doubled has less than one field period in the window). I raised that through questions 7 and 8 and the report-ranges check.

Statuses:
- All three lookalikes are "partly addressed".
- coulomb-dominated-interferometer: I weighed "ruled out" (the gate ratios 0.25 match neither the AB-limit ν nor the νLL = 1/2 interferometry value). I chose "partly" because the paper says its independent regime tests (temperature, DC bias) are inconclusive, and it set aside the slope test.
- report-counts: I picked "partly" over "not done" because the paper names one device and shows full datasets per filling. This is a judgment call.

## Sources held out

None. I checked each matched entry's source dates against the paper's submission (27 Aug 2026):
- 1010.4598 (2010)
- 2309.09368 (v1 2023, the version quoted)
- 2101.11456 (2021)
- 2501.18631 (v2 25 Mar 2026, abstract page opened)

None can cite this paper. I used submission dates as a proxy for "discusses the paper"; I did not full-text search them.

## Related work, how each was checked

All five abstract pages were opened on arxiv.org (abstract only, not full text). For each I confirmed the ID, title and first author, and that the abstract supports the one-line description.
- 1010.4598, Halperin et al. 2011 (also a library source): abstract.
- 1510.05241, Levy Schreier, Stern, Rosenow 2015: abstract. The abstract page lists three authors; the paper's Ref. [48] adds Halperin.
- 1201.1600, Kou et al. 2012: abstract.
- 2412.19886, Kim et al. 2024: abstract.
- 2403.18983, Werkmeister et al. 2024: abstract.

Considered and dropped:
- 2412.11401, Hata et al. 2024 (air-bridged pillar-gate antidot; finds a smaller antidot area at 2/3 and assumes a constant gate capacitance). Opened, abstract read; kept for the library gap below.
- 2010.11394, Mills et al. 2020 (graphene antidot e/3). Opened, abstract read.
- 2509.04209 and 2504.16750 (same group): seen in search results only, not opened, not used.

Searches: arXiv API, about 3 s between calls; no rate-limit replies.

## Library gaps

1. Lever-arm or area change between the reference state and the target state, when charge is read from a gate-period ratio (q/e = ∆V/∆V1). The antidot radius changes with filling and field, so the ratio can drift from the charge ratio. Hata et al. 2024 (https://arxiv.org/abs/2412.11401, abstract): "The area at ν = 2/3 is significantly smaller than that at ν = 2 and 1" and "By assuming a constant gate capacitance, the effective charge at ν = 2/3 is about 2/3". This shows the area change but not a false charge reading, so I did not add an outside row. I raised it as the one extra question (question 6). Candidate entry and check.
2. The charge checks have no step for antidot calibration (reference state at a different field, lever-arm constancy), nor for the DC-bias and temperature tests of regime. The paper shows both are weak below about 2 T0.
3. charge-control-regime bundles three tests (control regime, charge traps, gate leakage) into one status, which forces "partly" whenever one is missing.

## Unsure

- Whether charge-trap-fractional-shift should match a fractional-period claim at all. I matched it on the physics.
- My ∆B1/∆B values (6.8, 3.1, 7.6) are simple ratios of the paper's numbers, without the 8% area allowance. The paper states p ≈ 10, 2, 6 "within uncertainty"; I asked about it without asserting an error.
- "background-subtracted": the PDF breaks this word across a line; I kept the hyphen.
- I did not recognize the paper (submitted after my training data). I used no knowledge of its later history.

## Skill issues

- Step 7 says to write reports/<id>.md and .notes.md. This run required the report inline in the reply instead; not a skill problem, but the skill has no fallback when .md writes are refused.
- The hold-out rule needs a check of whether each source cites the paper, but it doesn't say how (full-text search or dates). I used submission dates.
- Scope rule: the template's "What this is" fixes the wording "topological transport". For a quantum Hall paper the adaptation sentence is the only place to say otherwise; unclear whether the boilerplate itself may change.
- Library entries are written one-directional (exotic reading against ordinary lookalike). Here the regime lookalike runs in reverse (CD is the claimed ordinary regime the charge reading depends on). The skill doesn't say how to phrase an adapted entry in the table; I renamed the row and cited the library id.
- "Every 'ruled out' and 'partly addressed' needs a short verbatim quote", and checks need "a short quote". Short quotes sometimes lose the point (check 1 needs two). The template's "one quote and one clause" per cell is hard to meet for the regime entry.
- The skill has no place for small labeling errors in the paper (figure panel mix-ups). I put them in the closing line.
- The library header suggests running check.py --quotes; the skill doesn't mention it, so I didn't run it.
- Concurrent runs share the scratchpad; another run overwrote my draft in a shared subfolder. The skill could advise a run-specific working folder.
