# Run notes: arXiv 2607.00683v1

- Library version: 0.5 (meta.updated 2026-10-24), 28 lookalike entries.
- Skill files read: skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (entries, tests, checks). read_mtx.py was not used because no figure data were provided.
- Paper read: the extracted text only (planted2/blind/r23/paper.txt), as instructed. I had no PDF, no abstract page and no supplement. The title comes from the text header. Figure details come from the captions, and page numbers come from the page markers in the text. I did not fetch the paper in any form. No data repository is linked in the text.
- Recognition: I did not recognize this paper, and I used no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| ZrTe5 is in the WTI phase | Fig. 2a-g | Hall bar (count not given); STM on cleaved crystals | Tp ≈ 139 K; SdH at 2 K, one frequency; STM gap ≈ 70 meV at 5.1 K; step 0.8 nm; edge LDOS width "≈ 6 µm" (p. 5) against a 5 nm scale bar (Fig. 2g), which is internally inconsistent |
| Proximity supercurrent | Fig. 3a-c | Dev 1, Dev 2 (Pd/Al, a-axis), Dev 3 (Pd/NbN, c-axis) | Temperature ranges in the figures (not in the text); dimensions in Supp. Table S1 (not available) |
| Ballistic transport from exponential Ic(T) | Fig. 3d | Dev 1-3 | Fits "in the high-temperature regime" only; mean free path in Supp. Note 2 (not available) |
| SQUID-like Ic(Bz), flux-quantum period, edge-peaked Js(x) | Fig. 4a,b,d,e; Fig. 5b | Dev 1, Dev 2, Dev 3 | 20 mK; field range not given; Gaussian half-widths 0.7-1.5 µm |
| Distinct pattern for By | Fig. 5c | Dev 3 only | Range not given |
| Sawtooth CPR from sharp lobes | Fig. 5b,c vs simulations 5d-f | Dev 3 | Qualitative comparison with W = 0.5-1.0 and 0.2-0.3 |
| Missing counts | | | Junctions fabricated and measured, cooldowns, datasets, field ranges, Hall bar count |

## Entries matched, skipped and adapted

- Matched: fine-tuning-and-selection (applies to every signature).
- Checks: the practice checks (report-counts, report-ranges, report-processing). The library has no `checks` block for the supercurrent family, so I walked no family-specific checks.
- Skipped: field-enhanced-supercurrent-resonances (supercurrent family). Its signature is supercurrent growing with field, and this paper claims spatial confinement from interference patterns. All zbp, quantization, nonlocal, island, shapiro, charge, chiral, kitaev and diode entries were skipped because the paper reports no such signal. protocol-parameter-sensitivity was skipped because no pass/fail protocol is used. local-probe-loophole was skipped because there is no local probe of zero modes.
- Adapted: none. Scope: this is a supercurrent-interferometry paper on a 3D WTI, at the edge of the library's scope, and I said so in "What this is".
- Outside rows (library gaps):
  1. Trivial edge accumulation channels giving SQUID-like interference. Source: de Vries et al., arXiv 1709.03727, full text, p. 5: "superconducting edge transport and an h/e SQUID pattern only, cannot distinguish between topological and trivial edge states, nor can it be considered a definite proof for a topological phase." The tests come from that paper's control (gate tuning from bulk to edge transport) and from Hart et al.'s topological and trivial well comparison. Suggested library entry: signature "SQUID-like Ic(B) or edge-peaked Js(x) read as topological edge or surface supercurrent".
  2. Diffusive long junction giving quasi-exponential Ic(T). Source: Dubos et al., arXiv cond-mat/0008146, full text, p. 3: "within a limited temperature interval this expression is numerically very close to a simple exponential dependence Ic ∝ exp(−L/LT) with LT ∝ 1/T, as one would expect in a ballistic limit." The tests come from that paper's quantitative fit with the Thouless energy.
  - Considered and dropped: triangular lobes produced by loop inductance, or a skewed CPR outside the long ballistic limit. I could not find and open a citable source (the Golubov CPR review is not on arXiv under the search I ran), so I left this out of the table.
- Status calls I was unsure of:
  - Trivial edges. The By/Bz contrast is data. I did not count it as a test, because the library-style tests for this lookalike are gate control and a trivial reference, and the contrast is neither. I marked the row "argued, not tested". A reader could argue for "data bear on it" or for "tested in part".
  - Diffusive Ic(T). I marked the second test "part" because Supp. Note 2 apparently gives a mean free path estimate, and I could not see it.
  - report-counts: I marked it "partly" because three devices are named but fabricated and measured totals are not given.
- Numerical inconsistency I noticed: the STM edge-state width "≈ 6 µm" (p. 5) cannot fit inside a Fig. 2g image with a 5 nm scale bar. It also contradicts "half-widths of 0.7-1.5 µm ... substantially larger than the conducting channel width observed by STM" (p. 7). This is raised as question 8, the one question not tied to an entry.

## Hold-out

- No library source used here cites 2607.00683. The only library entry used is fine-tuning-and-selection, whose sources are Frolov 2309.09368v1 (2023) and Akrap 2501.18631. I did not open those sources and quoted none of them in the report, so nothing was held out.

## Related work verification

- 1709.03727 (de Vries): abstract page opened (title and first author confirmed); full text read for the control and the conclusion quote.
- 1504.07630 (Allen): abstract page opened; description checked against the abstract.
- 2012.02842 (Aharon-Steinberg): abstract page opened; description checked against the abstract.
- 1312.2559 (Hart): abstract page opened; description checked against the abstract.
- cond-mat/0008146 (Dubos): abstract page opened; full text read for the quasi-exponential passage (p. 3).
- arXiv API calls were spaced by at least 3 s. Nothing was rate limited.

## Skill issues

- No `checks` block exists for the supercurrent family, and no entry covers interferometry-based localization claims (SQUID-like vs Fraunhofer). For papers like this one, most of the substance has to come from outside rows.
- The skill says to "Use the title on the arXiv abstract page", but this run had no abstract page. I used the title from the text header and shortened it in the report heading.
- Step 7 says to write reports/<id>.md and notes files. This run's instructions overrode that and asked for chat output. The skill could say what to do when file writes are not allowed.
- The "data bear on it" note and the "argued, not tested" note overlap when the authors argue using data that do not match a listed test (here, the By/Bz contrast). A tie-break rule would help.
- The status rules only work for outside rows if tests are taken from the cited paper's control. When a control is spread across two papers (de Vries and Hart), it is unclear whether one row may cite both. I listed one URL in `source`.
- The skill allows only one question not raised by an entry. An internal numerical inconsistency, like the 6 µm width, has no home in the library. A "practice" check for internal consistency of the numbers would cover it.
