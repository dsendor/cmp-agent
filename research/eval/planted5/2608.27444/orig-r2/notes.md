# Run notes: arXiv 2608.27444v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries plus the checks section. Skill and report-template read once, at the start.
- Run date: 2026-10-24. Run tag: orig-r2.

## What I read
- Only the extracted text of the paper (main text pp. 1-12, Methods pp. 9-10, Supplementary pp. 13-31), from the provided paper.txt. Following the run instructions, I did not use a PDF or the abstract page, and I did not fetch the paper. Figure details come from the captions only; I could not see the figures. Page numbers follow the page markers in the extracted text (the page N marker comes before the text of page N).
- The title is taken from the first line of the paper text, because the abstract page was not available.
- Data repository: none linked ("available from the corresponding author upon reasonable request", p. 10). No ancillary figure data, so read_mtx.py was not used.
- I don't recognize this paper and know nothing of its later history. I know the group's earlier antidot paper (ref. 30) only from its arXiv abstract, which I opened for related work.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Localized charge e/4 at ν = −5/2, −1/2, 3/2 from ∆V/∆V1 = 0.27 ± 0.03, 0.24 ± 0.03, 0.25 ± 0.03 | Fig. 2a,b,d, e,f,h (p. 4); full data in Fig. S8, S9, S11 | One gate-defined BLG antidot with an air-bridge antidot gate (ADG), lithographic diameter about 210 nm, top hBN 46 nm | B = 14 T; ADG periods 56 to 63 mV; ∆B = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT, read as p ≈ 10, 2, 6; field step 1 mT, typically about 101 points per scan (p. 10); excitation 0.2 to 1 nA; base about 10 mK, electron temperature about 30 to 50 mK claimed (p. 5). Devices fabricated, cooldowns and datasets set aside: missing. |
| Localized charge e/3 at ν = 2/3 | Fig. 2c,g; Fig. S10, S13 to S15 | Same | ∆V/∆V1 = 0.32 ± 0.03, ∆B1/∆B = 2.32 ± 0.93; gate instability, 20 repeated sweeps (Fig. S13); histogram method gives ∆B = 19.6 ± 4 mT |
| Calibration: ν = −1 at 10 T as the reference (∆V1 = 233 ± 14.3 mV, ∆B1 = 40.3 ± 6.7 mT); ν = −4/3 gives 0.37 ± 0.04 and 3.47 ± 0.79; ν = −2 gives e and p = 2 | Fig. 1e to h; Fig. S3 to S5 | Same | 10 T and 14 T; ADG versus TG check (2.9 ± 0.6) |
| Crossover to a doubled gate period with increasing side-gate coupling at ν = −5/2, −1/2, 2/3, 3/2, absent at −4/3 and −1/3; interpretation left open (bunching, or an AB or mixed regime) | Fig. 3, Fig. 4; Fig. S6, S7 | Same | Side gate up to about 5 V (−4/3); −1/3 only at −2 V and 0 V; safe limit about 6 V (p. 13) |
| Temperature dependence | Fig. S16, S17 | Same | B = 13.95 T; steps 16 to 120 mK (12.7 to 70 mK for one panel) |

## Entries matched, adapted, skipped
- Matched: coulomb-dominated-interferometer (adapted), charge-trap-fractional-shift (adapted), fine-tuning-and-selection (always).
- Adapted: coulomb-dominated-interferometer. The entry is written for a Fabry-Perot interferometer read as AB, where the lookalike is a CD regime. Here the paper claims the CD regime, and the alternative that matters is an AB or mixed regime, where the gate period stops counting the localized charge. I used the same two tests. charge-trap-fractional-shift: the entry's signature is fractional shifts. I applied it to traps or side dots adding jumps or extra periods to the antidot pattern. This fits the gate hysteresis and switching the paper reports at ν = 2/3, which it attributes to two near-degenerate configurations.
- Checks used: the charge family (charge-regime-map, charge-control-regime, charge-repeat-sweeps) and the practice family (report-counts, report-ranges, report-processing).
- Skipped: every zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entry, because there is no superconductor, tunnel probe or Josephson junction in this device. local-probe-loophole is specific to Majorana separation. protocol-parameter-sensitivity does not apply because no pass/fail protocol is used.

## Sources held out
- None. No matched-entry source (Halperin et al. 2011; Frolov et al. 2023; Zhang et al. 2021; Akrap, Frolov et al. 2026 v2) is likely to discuss this August 2026 paper. I did not open the full texts to confirm, so this is unverified for Akrap et al. v2.

## Related work checks
- All five, plus Halperin et al. 1010.4598, were found through the arXiv API, with the abstract text read from the API record. I then opened each arXiv abstract page to confirm the title and first author from its citation meta tags. Checked at the abstract level only, no full texts: 2509.04209 (Di Luca), 1201.1600 (Kou), 2603.11182 (Henzinger), 2603.11162 (Kim), 2412.16316 (Ghosh). Each one-line description matches its abstract.

## Library gaps
- No antidot-specific entry. The CD versus AB entry is written for interferometers, and its slope test assumes a side gate that changes the area. Here the ADG is argued to change the antidot area (p. 14).
- Lever-arm transfer: the charge comes from a ratio to a reference taken at another field and filling (10 T, ν = −1). The paper checks the transfer at ν = −4/3. A library entry on reference-calibration transfer would help. I found no cited demonstration, so there is no outside row.
- Superposed or harmonic periods read as a single fractional period by a 2D-FFT. The paper itself shows superposed periods in the intermediate regime (Fig. 3e,h). I have no opened source to cite.
- Quasiparticle bunching (Ghosh et al. 2412.16316) changes the measured period. It bears on the doubled regime, which the authors leave open, so I did not add an outside row.

## Unsure, and noticed but kept out of the report
- The CD-regime row could arguably be "ruled out for the claim", because ∆B1/∆B sits well above the AB value of 1 at −5/2 and 3/2. I kept it at "tested in part" for three reasons: at −1/2 the ratio (about 3.1 ± 0.7) sits between the expected values, the slope sign and charging energy are not reported, and the paper says its temperature fits "cannot therefore identify the transport regime" (p. 30).
- The e/4 and e/3 gate ratios (0.25 ± 0.03 versus 0.33) are separated by about 2.7 sigma at each filling.
- Possible text errors, left out of the report because the template has no place for them:
  - p. 6 says "Fig. 3d,e for ν = 2/3, and similarly for ν = −1/2 in Fig. 3g,i", while the caption has d to f at ν = −1/2 and g to i at ν = 2/3.
  - p. 7 mentions "ν = −2/3", a filling not measured; probably 2/3.
  - p. 14 calls a predicted 330 mV against a measured 235 mV an "agreement", and uses a 50 nm top hBN against the 46 nm in the Methods.
- The report runs about 1100 words outside the table, above the 600 to 900 target, mainly because of the quotes in the questions.

## Skill issues
- The report template has no slot for internal inconsistencies (mislabelled panels, conflicting numbers). Only one could go in, as question 7.
- Adapting an entry whose claim direction is reversed (the paper claims CD, and the entry treats CD as the lookalike) is not covered. The scope rule says "adapt" without saying how to restate the tests.
- For a one-device paper it is unclear whether report-counts is "partly" (one device named) or "not done" (no counts of devices made, cooldowns or datasets set aside). I chose partly.
- The hold-out rule needs knowing whether each library source cites the paper. That can't be checked without opening every source, and the skill doesn't say how far to go.
- The title rule assumes the abstract page. This run had text only.
- "Open its arXiv abstract page": I used the API record and the abstract page meta tags. It is unclear whether this counts as "abstract" checking.
