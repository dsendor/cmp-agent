# Run notes: 2509.04209v1

**Library version:** 0.5 (meta.updated 2026-10-24), 28 lookalike entries plus the checks section.

## What I read
- The v1 PDF (all 28 pages rendered at 110 dpi; looked closely at pp. 2, 3, 5, 6, 7, 11, 18, 20, 21, 25, 26, 27, 28) and the extracted text in full, supplementary sections C to I included.
- I did not open the arXiv abstract page or any other version of the paper, as the task required. The title comes from the PDF. An arXiv API search result listed 2509.04209v2. I did not open it.
- Data repository: none linked ("available from the corresponding author upon reasonable request", p. 10), so I counted devices and datasets from the figures only.
- No ancillary figure data, so I did not run read_mtx.py.
- I did not recognize the paper and know nothing of its later history.

## Claims table (step 1)

| Claim | Figures | Device(s) | Counts and ranges |
|---|---|---|---|
| Coulomb-dominated oscillations at integer ν with q close to e | Fig. 2a-h; Figs. S6, S7, S8, S12 | AD #1 (5 T); AD #2 (13.5 T, 8 T, 5 T) | AD #1: ν = 1-4 at 5 T, B windows of about 0.25-0.3 T, Vtg windows of about 30-40 mV, bias ±0.8 mV. AD #2: ν = 1, 2, 4 at 13.5 T; ν = -2, 1 at 8 T; ν = 2, 4 at 5 T (ν = 4 at 300 mK). q is about 5% high, which they attribute to the TG changing the AD potential (Sec. G). |
| Fractional oscillations at 3/5, 2/3, 4/3, 5/3, 7/3, 8/3 | Fig. 3b-g; Figs. S13-S18 | AD #2 only | Maps per fraction: 3/5 two, 2/3 three, 4/3 four (two at 13.5 T, two at 8 T), 5/3 five (four at 13.5 T, one at 8 T), 7/3 one (8 T), 8/3 two (small period seen in S18a). D from -0.46 to -0.03 V/nm. Windows of about 0.1-0.2 T and 8-25 mV, bias ±0.2 mV. Charging energy about 50 µeV. |
| e/3 tunneling charge at 4/3, 5/3, 7/3 and small 8/3 (headline) | Fig. 4d-e; Eq. 1 | AD #2 | N from 2ΔB2/ΔB (Fig. 4b) assuming constant area. Diameters in Fig. 4c come from the same N. 7/3 has "a larger uncertainty". |
| 2e/3 at 2/3 and large 8/3; 3/5 at q close to 3/5 | Fig. 4 | AD #2 | 3/5 departs from the expected 1/5, and they say they "cannot directly test this hypothesis" (p. 6). |
| Slope ΔV/ΔB follows ν | Fig. 5; Fig. S10c-d | both | Within ±10% for most points; ν = 4 deviates. |
| Bottom-gate repeat of the charge | Figs. S9-S10 | AD #1 (ν = 1-3); fractional data labeled AD #2 in the caption and AD #1 in the text | ν = 2/3, 4/3, 5/3, 8/3. |
| Area oscillations | Fig. S11 | AD #1 ν = 2; AD #2 ν = 5/3 | ΔV of about 39 mV vs. density period. |

Missing counts: devices fabricated, cooldowns, how many fractions were tried, how many windows were taken per fraction, and any temperature dependence (only one 300 mK dataset). Base temperature is about 10 mK. Vac is 10 µV (IQHE) and 3 µV (FQHE). Steps are dB = 1 mT and dV = 0.1 mV, with about 101 points per axis.

## Entries matched, adapted, skipped
- Matched in the charge family: coulomb-dominated-interferometer and charge-trap-fractional-shift. The practice entry fine-tuning-and-selection always applies. Checks walked: charge-regime-map, charge-control-regime, charge-repeat-sweeps, report-counts, report-ranges, report-processing.
- Adapted, with the one-sentence scope note under "What this is":
  - coulomb-dominated-interferometer. The library frames Coulomb-dominated oscillations as the lookalike for Aharonov-Bohm anyon interference. This paper adopts the Coulomb-dominated regime as its mechanism, so I flipped the entry to ask whether some oscillations (4/3 in particular) are Aharonov-Bohm or mixed, which would break Eq. 1.
  - charge-trap-fractional-shift. Adapted from "fractional shifts" to "extra periods or jumps" from a side dot or trap. It targets the small 8/3 period and the visible discontinuities in Figs. S11c and S17a, plus the paper's note on impurities that "can locally trap electrons" (p. 13).
- Skipped:
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries. They concern superconducting hybrids, Majorana or Josephson signatures, or chiral Majorana plateaus, none of which exist in this device.
  - series-resistance-subtraction. The 1.02 current factor affects conductance amplitude, not the periods that set the charge. I mention it under report-processing.
  - protocol-parameter-sensitivity. There is no pass/fail protocol. The data-choice sensitivity of the FFT period picking is covered under report-ranges and report-processing.
  - local-probe-loophole. It is specific to Majorana separation.
  - island-states-coulomb-spacing. Even-odd Coulomb patterns read as Majorana overlap. The paper's even-odd amplitude idea is about a different question.

## Status reasoning, briefly
- Coulomb-dominated regime (adapted): the slope test is shown for all fillings (Fig. 5). Regime and charging energies are reported, but the paper itself flags 4/3 as possibly AB-like and says ν = 1 and 4 at 13.5 T "may not be operating in the single-level hopping regime" (p. 17), so that test is part. Result: tested in part.
- Charge trap (adapted): the integer control gives q close to 1 in both devices (all). Leakage is not mentioned (no). Two-gate data: BG sweeps for 2/3, 4/3, 5/3, 8/3 and area sweeps for ν = 2 and 5/3, none for 7/3, and the small 8/3 period is not followed (part).
- Filling-dependent area (outside): Fig. 4c diameters use N, which was fixed assuming constant area, so the clustering near 300 nm is partly built in. The BG repeat (Fig. S10) partly covers the gate-coupling side. Part / no.
- Charged-edge counting (outside): argued explicitly only for 4/3 (part). Eq. 1 combines both periods for all fillings (all). The separation rests on the constant-area assumption, so it stays at tested in part and does not reach "ruled out".

## Sources held out
None skipped. All library sources I relied on (Halperin et al. 2011, Frolov et al. 2023, Zhang et al. 2021, Akrap et al. 2026) predate the paper or concern other work by title. I did not read the full texts of the 2026 versions (Akrap et al. v2, Legg v2), so I can't confirm they never cite this paper. Neither is quoted about it.

## Related work, how each was checked
All five were checked on their arXiv abstract pages (title, first author, abstract text), fetched with 3 s waits:
- 1201.1600 (Kou): abstract confirms e with two charged edges at ν = 2, and (2/3)e with a single edge at 2/3.
- 2412.11401 (Hata): abstract confirms the smaller area at 2/3 and the 2/3 effective charge under constant gate capacitance.
- 2010.11394 (Mills): abstract confirms charges of about ±e/3 at ν = ±1/3 in graphene antidots.
- cond-mat/0007383 (Kataoka): abstract confirms compressible rings and resonance twice per h/e.
- 1010.4598 (Halperin): abstract confirms the opposite stripe slopes and the superposition at intermediate coupling.

Not used: cond-mat/0010093 (Goldman, invariance of e/3; abstract read). I did not open 2608.27444 (a later paper by the same first author) because it might discuss this paper.

## Library gaps
- No entry for a filling-dependent antidot or interferometer area, or gate lever arm, biasing charge from period ratios (source: Hata et al. 2024, 2412.11401).
- No entry for the number of charged edges or compressible rings setting the field period, as an alternative reading of N (sources: Kou et al. 2012, 1201.1600; Kataoka et al. 2000, cond-mat/0007383).
- The charge-family checks lack a step for "calibrate area and gate coupling independently of the charge assignment" and for "temperature dependence of the oscillations".
- coulomb-dominated-interferometer is written for FPIs claiming AB. It has no variant for papers that adopt the CD regime and need to exclude AB or mixed contributions.

## Unsure
- Whether repeated maps at other D or B count as "repeat sweeps" (I marked partly).
- Whether to mark charge-regime-map "done" given the paper's own 4/3 caveat (I marked done, since maps and a regime statement exist for all fillings).
- Page numbers follow the PDF page counter. Quotes spanning columns were checked against the rendered pages.
- The device-label conflicts (Fig. S9 text vs. caption; p. 3 vs. p. 11 on FQH states at 8 T) may be typos. I asked and did not infer.

## Skill issues
- Step 7 and the Input section say to read the arXiv abstract page and use its title. This test forbids fetching the paper, so I used the PDF title. The skill could say what to do when the abstract page is unavailable.
- Step 7 says to write reports/<id>.md and .notes.md. This environment refuses .md writes from subagents, so I returned both in the reply.
- The status rules don't cover an adapted entry where the paper embraces the library's "lookalike" (here CD) as its own mechanism. I reframed it as regime misidentification. Guidance would help.
- The "ruled out" bar (one test that by itself separates) is unclear when that test depends on an assumption covered by another row (constant area). I kept it at tested in part.
- The hold-out rule needs each source's full text to apply strictly. The skill doesn't say whether checking titles and dates is enough.
- arXiv search listings can show the paper under review (here v2), which you see before you can skip it.
- The template's check line format "<check> : Done / Partly / Not done" leaves it unclear whether to quote the library's check text verbatim or paraphrase it. I shortened the wording.
