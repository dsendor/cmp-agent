# Run notes: 2603.02450v1

- Library: lookalikes.yaml meta.version 0.5 (updated 2026-10-24), 28 entries. Skill and template read once at the start.
- Read: the v1 PDF (36 pages: main text, Methods, Extended Data Figs. 1 to 10) and its extracted text. I took figure details from page renders of Figs. 1, 3 and 4, with a zoom on Fig. 4e and 4f. Per the task, I did not open the arXiv abstract page, so the title comes from the PDF and the report heading is a shortened form of it. The Supplementary Information (Figs. S2 and S7, and the temperature-during-pulse plot) is cited but isn't in the PDF, and I could not see it. No data repository was reachable: the paper says data "will be uploaded ... prior to publication". No ancillary figure data, so I did not run read_mtx.py.
- Recognition: I don't recognize this paper and know nothing of its later history.

## Claims table (step 1)

| Claim | Figures | Device | Ranges and counts |
|---|---|---|---|
| A pump (abrupt drop of J to zero) raises Jc, and an erase (slow ramp-down) resets it | Fig. 1b; Ext. Fig. 3, 4 | S1 at 20 T, 50 mK (Fig. 1b); S1 at 20 T, 170 mK (Ext. 3); S2 at 7 T (Ext. 4) | J about ±8 A cm^-2; both polarities (Ext. 4) |
| Memory state lasts at least several hours | Text p. 7; Fig. 1c | S2 at 7 T | No retention trace shown; Fig. 1d spans 400 s |
| Pump/probe switching between 0 and nonzero V | Fig. 1d, e | S2 (field not stated) | About 6 cycles shown |
| Three tuning axes with saturation | Fig. 2; Ext. Fig. 1 | S2 at 9 T and 14 T, 50 mK | Jex 0 to 20 A cm^-2; Δt 0.01 to 20 ms; α 2 to 500 A cm^-2 ms^-1 |
| Effect fades with T, gone by about 0.6 to 0.65 K | Fig. 3a, b; Ext. Fig. 5, 6 | S1 at 20 T (50 mK to 1.0 K); S2 at 14 T (50 to 600 mK) | 4 to 5 temperatures |
| Memory only in a B-θ window below SC2 | Fig. 4c to g; Ext. Fig. 7, 8, 10 | S2 | B 0 to 30 T at 0°; 0 to 22 T at 15°; θ -1° to 31° (b toward c) at 15 T and 29 T |
| Equilibrium V(B) and ∂V/∂J anomalies at the region's edge | Fig. 4b; Ext. Fig. 9 | S2 (0 to 22 T); S1 (9 to 30 T) | Equilibrium only |
| Flux-flow ρ(B) | Fig. 4h | S3 at 400 mK, ac, NHMFL | 0 to 33 T, J 0.5 to 15 A cm^-2 |
| RSJ two-minimum model reproduces it qualitatively | Fig. 3c; Ext. Fig. 2 | Simulation | N = 60 noise realisations |

Counts: 3 samples named (RRR 105, 44, 395). Memory shown in 2 of them; S3 not reported under pulses. Devices fabricated, cooldowns and set-aside samples: not stated. Two facilities (SECUF dc, NHMFL ac). Cross-sections, contact resistances and voltage-lead spacing: not stated. Field history (swept or field cooled): not stated.

## Matching (step 2)

- Scope: the paper is bulk dc transport on a multiphase superconductor, a history-dependent Jc read as intrinsic vortex physics. No library signature matches directly. I adapted `diode-vortex-screening`: its ordinary mechanism (asymmetric vortex edge barriers and Meissner screening) is a known extrinsic source of direction- and history-dependent Jc in ordinary superconductors. I recast its "plain film of the parent superconductor" test as the in-sample SC1-only and SC2-only regimes.
- Always included: `fine-tuning-and-selection`.
- Skipped: every zbp, quantization, nonlocal, island, shapiro, kitaev, chiral and charge entry (no tunneling spectroscopy, junction, island, microwave drive or fractional shift). `field-enhanced-supercurrent-resonances` was skipped because its mechanism needs finite-bias mesoscopic resonances in a junction, and this is a mm-sized bulk crystal with no junction. `protocol-parameter-sensitivity` was skipped because there is no pass/fail protocol. Its concern (a region defined by a threshold) went into question 7 and the report-processing check. `local-probe-loophole` was skipped as irrelevant here.
- Checks: the library has no `checks` family for this signal, so only the three practice checks were applied.

## Outside rows (library gaps)

1. Supercooled disordered vortex phase near a peak effect. Source Henderson et al., cond-mat/9606074 (full text read). Tests come from its control (field-cooled vs zero-field-cooled preparation, and location relative to the peak effect), supported by Xiao et al. and Ravikumar et al.
2. Edge contamination through surface barriers. Source Paltiel et al., cond-mat/9912157 (full text read). Tests come from its control (Hall sensor arrays across the width; ac vs dc Ic and its frequency dependence).
3. Joule heating during pulses. Source Courtois et al., 0805.4524 (abstract only). Test: a direct measurement of the sample or electron temperature.

The library has no entries for bulk vortex-matter metastability, for edge contamination, or for heating artifacts in pulsed transport. Those are worth adding if the library grows past topological transport.

## Hold-out

Library sources I quoted or relied on: 2205.09276 (Hou et al.) and 2501.18631 (Akrap et al. v2, 2026). I fetched both full texts and searched them for "UTe2", "2603.02450" and "memory effect": no hits. 2309.09368v1 (2023) predates the paper. No source was held out.

## Related-work verification

- cond-mat/9606074 Henderson: ID, title and first author confirmed from the arXiv API; abstract and full text read.
- cond-mat/9904141 Xiao: confirmed; abstract and full text read (the ramp-speed dependence is in the text).
- cond-mat/9912157 Paltiel: confirmed; abstract and full text read.
- cond-mat/0007436 Ravikumar: confirmed; abstract only.
- 0805.4524 Courtois: confirmed; abstract only.
- I searched for the UTe2 paper by Tokiwa et al. (ref. 46 of the paper) on arXiv and OpenAlex but could not find or open it, so it is not listed. I made no OpenAlex calls with an email address.

## Judgment calls

- The Joule-heating test is marked "part" under the skill's "can't tell" rule: the text says the SI shows temperature traces, but the SI isn't in the PDF. A stricter reading would mark it "no", which would make the row "Not tested (argued, not tested)".
- For the adapted diode entry, I counted the in-sample regimes (3 T, 30 T, 27°, 29 T at all angles) as a "part" equivalent of the parent-superconductor control. They are S2 only, and ordinary vortex metastability is itself field-dependent.
- For the peak-effect row, I marked "memory region placed against Jc(B)" as "part" because Fig. 4b and Ext. Fig. 9 show the data and mark the memory region on them, but the paper doesn't analyse a peak effect. The comment on Xiao et al. and the relaxation-rate argument is my own reading.
- I couldn't fit everything into eight questions, so the retention question was folded into question 3.

## Skill issues

- The scope rule says "adapt the matching entries", but when no entry matches the signature it doesn't say whether to adapt the nearest one or rely on outside rows. I did both.
- With no `checks` family for the signal, it is unclear whether to say so or to adapt checks from another family. I applied only the practice checks and said so.
- The task forbade opening the arXiv abstract page, while the skill says to use the title from it. I used the PDF title.
- Supplementary material that a PDF cites but doesn't contain isn't covered. I used the "can't tell, mark part" rule.
- The template's "What this is" sentence names "topological transport" even when the paper is outside it. I kept the template and added one scope sentence.
- The 600 to 900 word target leaves little room once five rows and eight questions are needed. The report runs near the upper end.
