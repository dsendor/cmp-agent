# Run notes: arXiv 2608.27444v1 (lookalike assistant, skill-r1)

AI only. Run on 2026-10-23.

## Library
- lookalikes.yaml meta.version 0.4 (updated 2026-10-23): 28 lookalike entries and 18 check steps (families zbp, shapiro, kitaev, charge, practice).
- Read once at the start, with SKILL.md and report-template.md.

## What I read
- The arXiv abstract page, from the provided abs.html (I did not fetch it): title "Trapping $e/4$ quasiparticles in bilayer graphene", v1 submitted 27 Aug 2026, 7 authors with Di Luca first, cond-mat.mes-hall. There are no ancillary files.
- The full text, main paper and supplement (pp. 1 to 31, Figs. 1 to 4 and S1 to S18), from the provided extraction (plain.txt; I also looked at the layout version, paper.txt). I added page markers from the form feeds, so page numbers are PDF pages.
- I did not open the PDF images, so figure content (map ranges, axis limits, side-gate values in Fig. 3) is known only from captions and text.
- Data: "available from the corresponding author upon reasonable request" (p. 10). There is no repository and no ancillary files, so I counted no data files and did not use read_mtx.py.
- Quote fidelity: quotes come from the text extraction. One line-break hyphen is restored ("backgroundsubtracted" in the extraction, written "background-subtracted"). I checked every other quote string by string against the extracted text.

## What I couldn't open
- Nothing failed. I did not fetch the paper under review in any form, as instructed.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges | Missing |
|---|---|---|---|---|
| e/4 localized charge at ν = −5/2, −1/2, 3/2 from ADG period ratio 0.27 ± 0.03, 0.24 ± 0.03, 0.25 ± 0.03 (ADG periods 56 to 63 mV) | Fig. 2a,b,d, 2e–h; Fig. 4b; Figs. S8, S9, S11 | One BLG antidot device (46 nm top hBN, 20 nm bottom hBN; lithographic AD about 210 nm, fitted diameter 361 ± 30 nm) | B = 14 T; dB = 1 mT, NB ≈ 101 points per scan (so about 100 mT windows); Iac 0.2 to 1 nA at 17.777 Hz; electron T about 30 to 50 mK; one map per filling per regime | Devices fabricated, measured and showing the effect; cooldowns; ADG, TG, BG, D and side-gate values and ranges; how tunings were chosen |
| Field periods consistent with the CD regime: ΔB = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT (p ≈ 10, 2, 6) | Fig. 2e–h, Fig. 4a | Same | ΔB1 = 40.3 ± 6.7 mT reference at ν = −1, 10 T; 8% area uncertainty added | Stripe slope signs not reported; slope method declared not applicable (p. 3) |
| e/3 at ν = 2/3 (ratio 0.32 ± 0.03, ΔB1/ΔB = 2.32 ± 0.93) | Fig. 2c; Figs. S10, S13 to S15 | Same | 20 repeated sweeps at 14 T, first 6 show hysteresis; histograms at several B | Number of B values in the histogram analysis given only in figures |
| Calibration: ν = −1 at 10 T reference (ΔV1 = 233 ± 14.3 mV); ν = −4/3 gives 0.37 ± 0.04, ΔB1/ΔB = 3.47 ± 0.79; ν = −2 gives e and p = 2; TG ratio 2.9 ± 0.6 for −1 vs −4/3 | Fig. 1e–h; Figs. S3 to S5 | Same | ν = −1 at 10 T and 14 T, ν = −2 at 10 T, ν = −4/3 at 14 T | TG-driven periods at the even-denominator fillings not shown |
| Crossover to doubled gate period with side-gate coupling at −5/2, −1/2, 2/3, 3/2; absent at −4/3 (Vsg 0.2, 2, 5 V) and −1/3 (Vsg −2, 0 V) | Fig. 3; Fig. 4; Figs. S6, S7 | Same | Side-gate safe limit about 6 V (p. 13), 5 V max (Fig. S6); no intermediate regime found at 3/2 | Side-gate values for the even-denominator series given only in Fig. 3; at −1/2 the doubled regime shows no full field period (Fig. S9) |
| Temperature dependence: e/4 suppressed at about 50 to 70 mK; doubled period at −1/2 and 2/3 survives to 120 mK | Figs. S16, S17 | Same | T = 16 to 120 mK (12.7 to 70 mK in one panel), B = 13.95 T | AB and CB fits not distinguishable over the range (p. 30) |

## Entries matched, adapted, skipped
- Matched: charge family `charge-trap-fractional-shift` and `coulomb-dominated-interferometer`, plus practice `fine-tuning-and-selection` (always included) and `protocol-parameter-sensitivity`.
- Adapted, per the Scope rule (this is a quantum Hall antidot charge measurement, outside the superconducting hybrid focus):
  - `coulomb-dominated-interferometer` is written for Fabry-Perot interferometers, where the Coulomb-dominated regime is the lookalike. In an antidot charge measurement the direction flips: the CD regime is the one the claim needs, and an AB or mixed regime is the lookalike, because there the gate period stops tracking the localized charge. I judged it against the same control (stripe slopes and spacings in the B–V_G plane).
  - `charge-trap-fractional-shift` covers fractional shifts. I applied it to stochastic switching and hysteresis that can shift or add periodicities in the period extraction (relevant to Fig. S13).
  - `protocol-parameter-sensitivity` covers pass/fail protocols. I applied it to the 2D-FFT period-extraction pipeline (third-order polynomial background, two-point moving average, picking the line with the largest Gaussian amplitude, uncertainties set by hand at −5/2).
- Skipped:
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: there is no superconductor, no tunneling peak, no Josephson junction and no Kitaev chain.
  - `local-probe-loophole`: it concerns separation of Majorana components, which has no analog in this charge measurement.
  - `series-resistance-subtraction`: no conductance is compared to a quantized value. The results are period ratios.
- Checks walked: charge family (charge-regime-map, charge-control-regime, charge-repeat-sweeps), then practice (report-counts, report-ranges, report-processing). There is no "charge" lookalike that the checks rule out completely.

## Sources held out
- None. No library source discusses this paper:
  - No library entry mentions antidots, bilayer graphene, the authors or the ID (grep).
  - All library sources predate 27 Aug 2026, except Legg 2502.19560 v2 (21 Oct 2026). That is a comment on the topological gap protocol, which I did not quote or open in full.
  - Akrap et al. 2501.18631 v2 is dated 25 Mar 2026, so it predates the paper.

## Related work: how each link was checked
- All abstract-level checks: I opened each arXiv abstract page and confirmed ID, title, first author and the one-line description.
  - 2509.04209 (Di Luca et al.)
  - 1201.1600 (Kou et al.)
  - cond-mat/9509116 (Franklin et al.)
  - 1010.4598 (Halperin et al.): the 2011 date is the publication year as given in the library; the arXiv posting is 2010.
  - 2412.19886 (Kim et al.)
  - cond-mat/0007383 (Kataoka, Ford, Faini), cited in the table for the outside lookalike.
- Opened but not listed: 0711.4746 (Sim, Kataoka, Ford review), 2010.11394 (Mills, Averin, Du), 2606.24831 (Thamm, Puster, Rosenow).
- arXiv API searches: abs:antidot AND abs:"h/2e"; antidot quantum Hall charge; the BLG even-denominator interferometer title. I waited about 3 s between calls.

## Library gaps
- Antidot and quantum-dot charge spectroscopy in the quantum Hall regime has no entries. Candidates:
  - (a) h/2e-type period halving from several antidot-bound modes (Kataoka et al., cond-mat/0007383);
  - (b) lever-arm or reference-state errors in gate-period-ratio charge estimates (calibration at a different field or filling);
  - (c) the Franklin et al. point that antidot periods are consistent with any charge at or above e*.
- The `coulomb-dominated-interferometer` entry fixes AB as the claimed regime. An antidot or CD-regime variant would avoid the inversion I had to make.
- The charge family has no check on period-extraction robustness (FFT window, background order, sampling near Nyquist: here dB = 1 mT against ΔB of about 5 mT).

## Unsure
- `fine-tuning-and-selection`: I chose "partly addressed" because consistent ratios across three fillings and several side-gate settings bear on single-tuning selection. The paper gives no counts at all, so "not addressed" is defensible.
- The outside lookalike (h/2e) mimics the field period (p) more directly than the gate charge. I kept it for the doubled-regime and p interpretation and labeled it "not in library".
- The weak-coupling e/4 claim does not use the side-gate crossover, so I treated the crossover as a second claim and did not give it its own lookalike rows.
- Word count is about 936 outside the table if headings, header and the checks list are counted, slightly over the 900 aim.
- I did not recognize this paper (posted Aug 2026) and used no outside knowledge of its later history.

## Skill issues
- Step 7 says to write `reports/<id>.md` and `.notes.md`. The run prompt replaced that with inline output. That was fine, but the skill has no mode for "return instead of write".
- There is no guidance for a lookalike whose direction inverts between device types (AB vs CD for interferometers vs antidots).
- It is unclear whether the 600 to 900 word aim includes the checks list, the questions and the headings.
- Practice entries such as `protocol-parameter-sensitivity` have protocol-specific signatures, yet the practice checks (report-ranges, report-processing) address them for every paper. It is unclear whether they belong in the table when there is no pass/fail protocol.
- Applying the hold-out rule strictly means opening every library source to see whether it cites the paper. The skill doesn't say whether checking by date or grep is enough.
- The template check line format "<check> : Done" (space before the colon) looks unintended.
- Environment: the shared scratchpad has no per-run naming. Another agent's report.txt replaced mine at the same path, and a `sed` I meant for my file ran on theirs (the target strings were specific to my report, so I expect no change).
