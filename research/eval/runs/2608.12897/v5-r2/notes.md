# Run notes: arXiv 2608.12897v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes, checks for zbp, shapiro, kitaev, charge, practice).
- Run date: 2026-10-24. Report is AI only.

## What I read
- Abstract page (local abs.html): title "Observation of Time-Domain Braiding of Non-Abelian Anyons at $\nu = 5/2$ State", Alkalay, Park, Oh et al., dated 2026-08-13, v1, "15 pages, 3 figures".
- Full text (local paper.txt, 41 pages), all of it: main text pp. 1-7, Methods pp. 8-12, references pp. 13-15, Supplementary Notes pp. 16-41 (Note 1 datasets, Note 2 theory, Note 3 heating model).
- PDF pages rendered and looked at: p. 4 (Fig. 2), p. 6 (Fig. 3), pp. 18-21 (Figs. S1-S4), p. 39 (Fig. S9). I read approximate R values off Figs. S1 to S4 panels (a) and (e) by eye.
- Data: no arXiv ancillary files. The paper says "Source data are provided with this paper" and "All other data related to this paper are available from the corresponding author upon reasonable request" (p. 13). I found no data repository link, so I counted devices and datasets from the text only. read_mtx.py not used.
- I did not fetch the paper itself; I used only the local copies.
- Could not open: nothing needed was blocked.

## Claims table (step 1)

| Claim | Figures | Devices / datasets | Counts and ranges |
|---|---|---|---|
| e/4 charge at each QPC (as injector) | Fig. 1b; Figs. S1-S4 (b), (f) | all 4 datasets | R about 0.05 to 0.25 (read from panels a, e) |
| Charge Fano factor above 1, matching PH-Pf (Abelian time-domain braiding) | Fig. 2b (data set 4, device C, second cooldown); Figs. S1-S4 (c), (d) | 4 datasets, 3 devices | F_charge = 1.54 at e*V_S/2k_BT = 4.6 vs PH-Pf 1.49, A-Pf 0.94 (p. 12) |
| Neutral Fano factor matching M_n = 0 (non-Abelian braiding) | Fig. 3b (data set 3, device C, first cooldown); Figs. S1-S4 (g), (h) | 4 datasets | F_neutral = 2.37 at 5.0 vs PH-Pf 2.33, A-Pf 2.0 (p. 12) |
| Incoherent heating excluded | Note 3, Fig. S9 | data set 4 only | heating model about a factor of two below data (Fig. S9 caption); main text p. 7 says "far smaller" |
| PH-Pf favored over A-Pf | Figs. 2b, 3b, S1-S4 | all | no fitting parameters; theory uses reduction factors C_rd of about 0.47, 0.44, 0.09, 0.59 set by numerical comparison (pp. 28) |

Counts:
- Devices fabricated: not stated.
- Devices measured: 3 (A, B, C). QPC gaps 1.2 µm on two and 1.3 µm on one. QPC separation 1.4 µm in all.
- Devices showing the effect: 3 of 3, per the authors.
- Cooldowns: 4 (device C twice, the second with 0.3 V on the gates during cooldown).
- Datasets: 4.
- Ranges:
  - Magnetic field and plateau position: not stated.
  - Bulk filling: 5/2. The active channel is ν = 1/2 with conductance e^2/2h.
  - Electron temperature: 10 mK only. How it was determined is not stated.
  - Bias: |e*V_S/2k_BT| up to about 5 to 6. My own estimate is about ±40 µV.
  - Noise detection at 720 and 690 kHz; conductance lock-in at 17 Hz.
  - Density 3.16e11 cm^-2, mobility 1e7 cm^2/Vs.
  - Dilution: one setting per dataset.
- Missing: devices fabricated, field, plateau, QPC gate voltages, why these transmissions, error bars or uncertainty values ("within experimental uncertainty" is not quantified).

## Entries matched, skipped, adapted
- Matched from the library: fine-tuning-and-selection (always).
- Skipped:
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: no such signal or device.
  - charge-trap-fractional-shift: no Coulomb blockade or interference pattern shifts.
  - coulomb-dominated-interferometer: no interferometer.
  - local-probe-loophole: Majorana-specific.
  - protocol-parameter-sensitivity: no pass/fail protocol.
- Adapted per the scope rule (time-domain shot-noise braiding is outside the library's signatures). I used the charge-family checks:
  - charge-regime-map: from "field and gate map, AB vs CD regime" to "bias, dilution and temperature, and name the regime".
  - charge-control-regime: to "same two-QPC noise at a filling with no anyons".
  - charge-repeat-sweeps: to "repeat measurements, including cooldowns".
- Practice checks were used unchanged.

## Outside rows (library gaps)
- Incoherent heating of the upstream neutral mode.
  - Source: Bid et al. 2010, arXiv 1005.5724, full text opened. It reports neutral-mode-induced noise at a QPC at 5/2, 2/3 and 3/5, and measures the apparent quasiparticle temperature from rounding near zero bias.
  - Tests taken from that paper's control plus the authors' own heating model.
  - Park et al. 2018 (1810.06871) supports the heat-diffusion noise picture; I opened only its abstract.
- Bunched tunneling charge at weak backscattering and low energy.
  - Source: Dolev et al. 2009, arXiv 0911.3023, full text opened. At 5/2 with t about 0.9 and a "mound-like" transmission, the charge is well above e/4, and it returns to e/4 at higher energy or temperature.
  - Tests: charge at the working transmission and temperature, and charge versus transmission and temperature.
- Suggested additions to the library:
  - A family for noise-based braiding (anyon collider, time-domain braiding).
  - The two entries above.
  - An integer-filling control check.

## Hold-out
- The library sources I used were Frolov et al. 2309.09368, Akrap et al. 2501.18631 (fine-tuning-and-selection and the practice checks), and the charge-check sources 1010.4598 and 2101.11456. I did not re-open them for this run.
  - 2309.09368 and 1010.4598 predate the paper.
  - The library entries for 2501.18631 and 2101.11456 are about other experiments.
  - I found no sign that any of them cites 2608.12897, and held out none.
- Related-work papers all predate the paper and do not discuss it.
- I did not recognize this paper (dated after my training data). I know its predecessor at ν = 1/3 (Lee et al., Nature 2023), and I used none of that knowledge beyond what the cited abstract says.

## Related-work checks
- 2209.15461: abstract page opened; ID, title and first author (June-Young M. Lee) confirmed; description checked against the abstract.
- 2202.03649: abstract page opened; ID, title, first author (Lee) confirmed; abstract checked.
- 1005.5724: abstract page and full text opened; Bid confirmed; abstract and text checked.
- 0911.3023: abstract page and full text opened; Dolev confirmed; text pp. 6-7 checked.
- 1810.06871: abstract page opened; Park confirmed; abstract checked.

## Unsure
- R values read off small plots. QPC1 is about 0.2 in Fig. S1a and about 0.1 in Fig. S1e. That reading is the basis of question 5 and the "part" in the bunching row.
- Whether "four data sets" is all data taken. I marked report-counts "done" because the paper states counts, shows all four and says all behave the same. The gap goes under fine-tuning-and-selection and the questions.
- Fig. S9 (data set 4) versus main-text "far smaller" for heating. I quoted the Fig. S9 caption and did not call it a discrepancy in the report.
- Whether the Fig. 2b "trivial" curve counts as a control. I treated it as computed, so charge-control-regime is "not done".

## Skill issues
- The checks have no "not applicable" status. Adapted checks that only partly fit force a "partly" or "not done" that reads like a gap. I adapted all three charge checks; another run might drop charge-regime-map.
- Step 6 says "always ask" the four standard questions "unless the paper already answers them (then say where)". The template has no slot for an answered question. I folded the answer into question 1 and asked a narrower follow-up.
- The outside rows rule ("take its tests from the control that paper describes") is hard when the source paper's control was aimed at a different question. Bid et al. test whether neutral modes exist, not heating versus braiding. I took only their apparent-temperature measurement and added the authors' own heating comparison as a test.
- The 600 to 900 word target is tight once the fixed "What this is" text and eight questions are in. This report is about 940 words outside the table.
- A shared scratchpad "work" folder is not namespaced per run. I overwrote a file there before noticing (see the summary).
