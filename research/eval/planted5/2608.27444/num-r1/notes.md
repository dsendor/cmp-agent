# Run notes: arXiv 2608.27444v1

- Library: lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries.
- Skill files read once at the start: SKILL.md, report-template.md, lookalikes.yaml.
- Paper read: the extracted text only, scratchpad planted2/blind/b42/paper.txt. That covers the main text, Methods and Supplementary Sections D to M. As instructed, I opened no PDF and no abstract page for this paper. The title comes from the text header. Figure details come from captions only, so I could not see axis ranges, stripe slopes or line shapes.
- Page numbers follow the printed page markers in the text: main text pp. 1 to 10, supplement pp. 13 to 31.
- Data repository: none linked ("available from the corresponding author upon reasonable request", p. 10). No ancillary files, so read_mtx.py was not used.
- Recognition: I did not recognize the paper. It is dated 27 Aug 2026, after my knowledge cutoff.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| e/4 addition at ν = −5/2, −1/2, 3/2 (∆V/∆V1 = 0.27, 0.24, 0.25 ± 0.03) | Fig. 2a, b, d, e, f, h; Fig. S8, S9, S11; Fig. 4 | one gate-defined BLG antidot with air-bridge ADG (lithographic diameter about 210 nm; fitted 361 ± 30 nm) | Devices fabricated: "the devices" (plural, p. 9), number missing. Devices measured: one described. Cooldowns: missing. Datasets: one map per filling per regime, plus a temperature series at 13.95 T (Fig. S16). B = 14 T; window about 100 mT (dB = 1 mT, NB ≈ 101). ADG window not stated. Excitation 0.2 to 1 nA at 17.777 Hz. Base about 10 mK; electron temperature 30 to 50 mK. |
| e/3 at ν = 2/3 | Fig. 2c, g; Fig. S10, S13, S14 | same | 20 repeated sweeps at fixed B; histogram at several B values. Gate hysteresis noted. |
| Calibration: e and p = 1 at ν = −1 (10 T and 14 T), e and p = 2 at ν = −2 (10 T), e/3 and p = 4 at ν = −4/3 (14 T), e/3 at −1/3 | Fig. 1e to h; Fig. S3 to S7, S12 | same | ∆V1 = 233 ± 14.3 mV, ∆B1 = 40.3 ± 6.7 mT, both at 10 T |
| Side-gate crossover to doubled period at −5/2, −1/2, 2/3, 3/2; absent at −4/3, −1/3 | Fig. 3; Fig. 4; Fig. S6, S7 | same | Vsg 0.2, 2, 5 V at −4/3; −2, 0 V at −1/3; safe limit about 5 to 6 V |
| Temperature dependence | Fig. S16, S17 | same | T = 12.7 to 70 mK or 16 to 120 mK |

Numerical consistency checks:
- 0.24 to 0.27 × 233 mV = 56 to 63 mV. The text gives "112 mV to 126 mV" (p. 4), which matches ∆V/∆V1 ≈ 0.48 to 0.54, the doubled regime.
- The Fig. S8 uncertainty of 5.6 mV, propagated with ∆V1 ± 14.3 mV, gives ±0.03 only for a period near 60 mV. That supports 56 to 63 mV as the values used.
- ∆B1/∆B from the stated ∆B values: 6.8 (−5/2, text says p ≈ 10), 3.1 (−1/2, text says p ≈ 2, about 1.8σ away using the stated errors), 7.6 (3/2, text says p ≈ 6).
- Antidot diameter from ∆B1 = 40.3 mT is 361 nm. That matches the text.
- lB at 14 T is 6.9 nm. That matches.
- The capacitance ratio of about 1/10 matches.
- Other inconsistencies, all raised in question 5: "ν = −2/3" on p. 7; Fig. 3 panel letters on p. 6 swapped relative to the caption; suppression temperatures of 60 mK (p. 8), 50 to 70 mK (p. 28) and 30 to 50 mK (p. 30).

## Entries matched, adapted, skipped

- Matched: fine-tuning-and-selection (always).
- Adapted:
  - coulomb-dominated-interferometer. Written for FP interferometers read as AB. Here the paper claims Coulomb-dominated, so the lookalike is an AB or mixed regime setting the period. Same tests.
  - charge-trap-fractional-shift. Written for fractional shifts. Here the signal is a fractional period, so a trap or side dot could add resonances. Same tests.
- Checks walked: charge family (charge-regime-map, charge-control-regime, charge-repeat-sweeps) and practice (report-counts, report-ranges, report-processing).
- Skipped:
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: no superconductor, no Majorana or Josephson claim.
  - series-resistance-subtraction: the claim rests on period ratios, not conductance values.
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol.
  - local-probe-loophole: Majorana-specific.

## Status reasoning

- AB/mixed regime: the gate-period ratio of 0.25 is far from the AB-limit expectations the paper lists (ν, or νLL = 1/2). I still did not mark it ruled out. Field periods carry 20 to 45 percent errors, the paper says its temperature fits "cannot therefore identify the transport regime" (p. 30), and it says its DC-bias data "does not provide conclusive information" (p. 8). No charging energy or lever arm is reported, so the second test is part.
- Charge trap: gate isolation was monitored during fabrication ("the two-probe resistance between each gate and contact was monitored", p. 9). That is not a leakage check at measurement, so I marked that test no.
- Multiple rings (outside row): the integer ν = −2 control at 10 T shows that two edges halve the field period and leave the gate period at e. That supports the gate-period charge reading. It was not repeated at 14 T or at the integer filling under each fractional state, so the test is part.

## Hold-out

No library source cites this paper; all sources predate it. No sources skipped.

## Related work and outside-row sources (how checked)

All were confirmed with the arXiv API abstract (title, authors, summary) and the arXiv abstract page (citation_title and first author meta tags). Abstract only for each; no full texts read.
- 1201.1600, Kou et al.: abstract.
- 2010.11394, Mills et al.: abstract.
- 2509.04209, Di Luca et al.: abstract. Same group's earlier work, listed for its own results.
- 2603.11182, Henzinger et al.: abstract.
- 2603.11162, Kim et al.: abstract.
- cond-mat/0007383, Kataoka, Ford, Faini et al.: abstract. Source for the outside row: "the resonance through the outer spin states should occur twice per h/e period".
- 1010.4598, Halperin et al. (library source): abstract page confirmed.

## Library gaps

- No entry for multiple charged rings or edges around an antidot halving a period (Kataoka et al. 2000; Kou et al. 2012).
- No antidot-specific charge entry. The charge family assumes interferometers or dots.
- No entry for a reference calibration taken at a different field or filling (lever arm or area change between the reference and the state of interest).

## Skill issues

- Charge-family entries are framed as AB read as fractional. When a paper claims the Coulomb-dominated regime, the lookalike runs in reverse, and the skill gives no guidance for an inverted entry.
- The skill says to read the abstract page and PDF. This test forbade both, and the skill does not say how to report a text-only run (figure ranges unavailable).
- Step 6 allows one question no entry raises. My numerical-consistency question (question 5) is of that kind, and I folded the other small number slips into it to stay within eight questions. The skill does not say where internal inconsistencies belong.
- "Ruled out for the claim" through a single sufficient test needs a judgment on whether a test separates a pure limit or also a mixed regime. The skill does not say which.
- report-counts: it is unclear whether "one device described, devices plural in contributions" counts as partly or not done. I marked not done.
