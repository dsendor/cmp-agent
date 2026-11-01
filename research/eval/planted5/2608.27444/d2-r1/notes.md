# Run notes: arXiv 2608.27444v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes). I read the skill, the report template and the library once, at the start.
- What I read: the extracted text of v1 only (main text, Methods, Supplementary Sections D to M), as the run instructions required. I did not fetch the abstract page, PDF or HTML of the paper under review. The title comes from the text header. Figure details come from captions only, so I could not read axis ranges or stripe slopes off the figures.
- Could not open: no figure images and no data repository. The data are "available from the corresponding author upon reasonable request" (p. 10), so I had no figure data and did not run read_mtx.py.
- Recognition: I did not recognize this paper or know of any later history.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| e/4 localized charge at ν = −5/2, −1/2, 3/2 (∆V/∆V1 = 0.27, 0.24, 0.25 ± 0.03) | Fig. 2a,b,d,e,f,h; Figs. S8, S9, S11 | one gate-defined BLG antidot with an air-bridge gate | ADG periods 56 to 63 mV; ∆B = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT; stated p = 10, 2, 6; B = 14 T |
| e/3 at ν = 2/3 (∆V/∆V1 = 0.32 ± 0.03, ∆B1/∆B = 2.32 ± 0.93) | Fig. 2c,g; Figs. S10, S13 to S15 | same | 20 repeated sweeps (Fig. S13); histogram ∆B = 19.6 ± 4 mT (minimal), 30.4 ± 10 mT (doubled) |
| Calibration: ν = −1 at 10 T gives ∆V1 = 233 ± 14.3 mV, ∆B1 = 40.3 ± 6.7 mT; −4/3 gives 0.37 ± 0.04 and 3.47 ± 0.79; −2 consistent | Fig. 1e to h; Figs. S3 to S5 | same | ν = −1 at 10 T and 14 T, ν = −2 at 10 T, −4/3 at 14 T |
| Doubled gate period with stronger side-gate coupling at −5/2, −1/2, 2/3, 3/2; none at −4/3, −1/3 | Fig. 3; Fig. 4; Figs. S6, S7 | same | −4/3 at Vsg = 0.2, 2, 5 V; −1/3 at −2, 0 V; Vsg limit about 6 V (p. 13) or 5 V (Fig. S6) |
| Temperature dependence | Figs. S16, S17 | same | 16 to 120 mK (12.7 to 70 mK for panel a), B = 13.95 T |

- Other parameters: AC excitation 0.2 to 1 nA at 17.777 Hz; base temperature about 10 mK; field step 1 mT with about 101 points per scan (about 100 mT windows); top hBN 46 nm (Methods) and 50 nm (Supp. E); antidot diameter 361 ± 30 nm from ∆B1 (I checked this: h/e over 40.3 mT gives 361 nm).
- Missing counts: devices fabricated ("the devices"), cooldowns, number of side-gate settings tried per filling, ADG voltage ranges, and how each minimal-regime setting was found.
- Internal inconsistencies I found (these went into the questions):
  - ν = −1/2: 40.3/13 ≈ 3.1, while the text states p = 2.
  - The e/4 suppression temperature is given three ways: ~60 mK (p. 8), 50 to 70 mK (p. 28), and 30 to 50 mK (p. 30).
  - The Vsg limit is given as 6 V (p. 13) and as 5 V (Fig. S6).
  - For ν = −1/3, data are shown only up to 0 V, against the claim of no doubling at the "largest side-gate voltage".
  - Fig. 3 panel labels in the p. 6 text conflict with the caption.
  - "ν = −2/3" appears on p. 7 where the data are at ν = 2/3.
  - On the other numbers I checked (lB = 6.9 nm, the 8% area term, the capacitance factor of about 10, the 1 GΩ bias current), the arithmetic is consistent.

## Entries matched, skipped and adapted

- Matched:
  - coulomb-dominated-interferometer, adapted from the Fabry-Perot interferometer to an antidot. The lookalike runs in the other direction here: an AB or mixed regime would make the gate period stop measuring the charge. The authors discuss this themselves.
  - charge-trap-fractional-shift, adapted from fractional shifts to fractional or doubled periods and to the ν = 2/3 hysteresis.
  - fine-tuning-and-selection (always).
- Checks walked: charge family (charge-regime-map, charge-control-regime, charge-repeat-sweeps) and practice (report-counts, report-ranges, report-processing).
- Skipped:
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: these are hybrid superconductor, Josephson, QAH or dot-chain devices, so the signatures cannot apply to a QH antidot.
  - series-resistance-subtraction: the claim rests on period ratios, and no conductance value is read as quantized.
  - local-probe-loophole: specific to Majorana modes.
  - protocol-parameter-sensitivity: there is no pass/fail protocol, although the FFT line-selection rule is an algorithmic choice.
- Outside row: constriction-modulated charging energy, from Hajigeorgiou et al. 2026 (arXiv 2606.19187, abstract checked). Its tests come from that paper's control: charging energy tracked against field and coupling, and correlated with the constriction conductance. The paper says "cannot exclude", so the status is "Left open by the authors". Library gap: there is no entry for charging energy or lever arm changing with coupling or field, which also bears on transferring the 10 T calibration to 14 T. Hata et al. 2024 (2412.11401) shows the constant-capacitance assumption at work in antidots.

## Sources held out

- None. No library source cites this paper; the library sources all predate it.

## Related work verification

- All five were checked through the arXiv API abstract and the arXiv abstract page, which confirmed the title and first author for each. The one-line descriptions are checked against the abstracts only, not the full text.
- 1010.4598 Halperin (library source); 1201.1600 Kou; 2412.11401 Hata; 2509.04209 Di Luca; 2606.19187 Hajigeorgiou.
- Considered and not listed: 2010.11394 Mills et al. (abstract checked; e/3 on graphene antidots) and 2602.08468 Alkalai et al. (title only).

## Unsure

- charge-regime-map: I set it to "partly" because the doubled-regime regime is left open and the field periods match the CD expectation only loosely. A reader who judges only the e/4 claim might call it "done".
- coulomb-dominated-interferometer: I kept it at "tested in part". The AB limit predicts ∆V/∆V1 = ν and p = 1, and the weak-coupling data differ from both, which argues for a stronger status. Against that, ν = 2/3 (2.32 ± 0.93) is within about 1.5 sigma of p = 1, and the authors call temperature and DC-bias inconclusive.
- Gate leakage: I marked it "no". The only evidence is a fabrication-time two-probe check stated in a sentence, with no data shown.

## Skill issues

- The checks and tests are written for interferometers and quantum dots. For an antidot where the claim is a fractional period (not a shift), mapping "Shifts absent where the exotic state is not expected" onto calibration controls needed judgment.
- When a paper presents a main claim plus a secondary result whose mechanism is explicitly left open (here the doubled period), it is unclear whether a check counts as "done" for the main claim alone or must cover all the evidence presented.
- The skill asks me to open the arXiv abstract page and PDF of the paper under review. The run instructions forbade this, so I took the title from the text header.
- Step 5 says to open each related paper's "arXiv abstract page". It does not say whether the API abstract counts. I used both.
