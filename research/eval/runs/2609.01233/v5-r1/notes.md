# Run notes: arXiv 2609.01233v1

- Library: lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries. Skill and template read once at the start.
- Date of run: 2026-10-24. Paper version: v1 (given).

## What I read
- abs.html (local copy): title, authors, date 2026-09-01, abstract.
- paper.txt (full extracted text, main text, Methods, Extended Data captions, Supplementary Notes 1 to 9). 21 PDF pages.
- paper.pdf: rendered pages 2, 4, 5, 10, 11 and high-resolution crops of Fig. 2, Fig. 3b and Fig. 3c to read axes, FFT labels and Extended Data panels. Pages are cited by PDF page number (supplement pages 1 to 10 are PDF pp. 12 to 21).
- No ancillary files or figure data with the paper. Data "available from the corresponding author upon reasonable request" (p. 8); no repository to reach. read_mtx.py not used.
- Did not fetch the paper itself. Did not recognize the paper (dated after my knowledge of the field); no later history used.

## Claims table (step 1)
| Claim | Figures | Device | Ranges shown | Counts |
|---|---|---|---|---|
| p-n interface MZIs are spin selective in the integer regime: one frequency at (−2,1), two at (−2,2), none at (−1,1) | Fig. 1e,f; ED1; ED2 | one device (700 nm constriction, 70 nm gate slit) | (−2,1): B 8.00 to 8.20 T, Vright 1.09 to 1.14 V; (−2,2): B 8.05 to 8.25 T, Vright 1.66 to 1.75 V; (−1,1): B 10.4 to 10.6 T, Vleft −1.3 to −1.0 V | devices fabricated: "The devices" (plural, p. 13), number missing; devices measured: missing; cooldowns: missing |
| Spin transition of the 2/3 interface channel near 9.5 T | Fig. 2a,b | same | Fig. 2a fan B 6 to about 13 T; Fig. 2b B 8 to 11 T, Vright − αB 0.20 to 0.32 V | one dataset |
| Spin-polarized (spin-down) 2/3 channel near 11 T | Fig. 2d; ED3 | same | Fig. 2d B 11.00 to 11.10 T, Vleft −2.27 to −2.23 V; ED3 B 11.00 to 11.10 T, Vleft −1.3 to −1.1 V | one dataset each |
| Spin-unpolarized 2/3 channel below 9.5 T: spin-up probe couples, and both spins couple | Fig. 3a; Fig. 2c; Fig. 3b | same | Fig. 3a B 8.35 to 8.45 T, VSi 31.0 to 32.0 V; Fig. 2c B 7.70 to 8.80 T, Vleft −2.37 to −2.18 V; Fig. 3b B 8.35 to 8.60 T, Vleft about −2.118 to −2.064 V | one dataset each |
| Combination frequencies fnm = n f10 + m f01, f11 read as two-electron spin-swap interference | Fig. 3c; Fig. 4; Supp. Notes 5, 6 | same | FFT of Fig. 3b only; labelled (1,0), (0,1), (1,1), (0,2), (1,2), (0,3) | one dataset |
| Faster thermal and bias decay of f10, f01 vs spin-polarized regime; time delays 7.31, 1.67, 2.18 ps | Fig. 3d,e; ED4; Fig. S3; Supp. Note 7 | same | T 0.1 to 1.0 K (10 maps); bias about ±1.3 mV; base 10 mK; ac excitation 1 to 5 nA at about 7 Hz | fits exclude three lowest-T points |

Missing counts: devices fabricated, measured, showing the effect; cooldowns; datasets taken. My reading of the FFT resolution in question 5 comes from the axis ranges of the rendered Fig. 3b (approximate).

## Entries matched, adapted, skipped
- Matched and adapted: coulomb-dominated-interferometer (library entry is for Fabry-Perot interferometers read as fractional quasiparticles; adapted to an open Mach-Zehnder geometry where the claim is spin structure and combination frequencies). Charge-family checks (charge-regime-map, charge-control-regime, charge-repeat-sweeps) adapted the same way: "exotic state not expected" read as the spin-polarized and integer configurations.
- Always included: fine-tuning-and-selection. Practice checks report-counts, report-ranges, report-processing applied.
- Skipped: charge-trap-fractional-shift (no fractional shifts or phase jumps are claimed); protocol-parameter-sensitivity (no pass/fail protocol); local-probe-loophole (about Majorana separation); all zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries (no superconductor in the device; the parafermion outlook is not a claimed signal).

## Sources held out
- None. No library source cites this paper (all library sources predate or concern unrelated systems; the 2026 items are Frolov et al. Science, Akrap et al. PRB and Legg's TGP comment). I did not refetch them to confirm.

## Related work, how checked
- 1703.00110 Wei et al.: abstract page opened; ID, title, first author and the beam-splitter statement confirmed in the abstract.
- 2407.11490 Shimizu et al.: abstract page opened; confirmed in the abstract. Also the source of the outside row.
- 0801.2338 Levkivskyi and Sukhorukov: abstract page opened; confirmed in the abstract.
- 2312.03150 Werkmeister et al.: abstract page opened; confirmed in the abstract.
- 2508.07380 Song and Myoung: abstract page opened and full text read (PDF); the summed-area peak statement is on p. 9 of their text.
- Searched also and opened, not listed: 1812.06717 (Bhattacharyya et al., neutral modes quench MZI interference), 1602.06944 (Sivan et al., area breathing in Coulomb-dominated FPI), 1303.4339 (Chirolli et al.), 2011.04958 (Jo et al., cited by the paper as ref. 19).
- arXiv API calls spaced by 3 s; no rate limit hit.

## Library gaps
- No entry for interaction effects of copropagating integer channels in Mach-Zehnder interferometers (Levkivskyi and Sukhorukov 2008; Shimizu et al. 2024). Added as an outside row with source 2407.11490.
- No entry or check for FFT window resolution against the frequency spacing used to assign combination peaks, and for sum versus difference frequencies as a test of coupled loops.
- No family for spin or edge-structure interferometry in the quantum Hall regime; the charge family is written for fractional charge and statistics.
- coulomb-dominated-interferometer has only a Fabry-Perot source; a Mach-Zehnder or graphene source (for example Werkmeister et al. 2023) would help.

## Unsure
- Whether the 0.1 K panel of Fig. 3d is the same sweep as Fig. 3b or a repeat; I counted Fig. 3d as repeated sweeps (charge-repeat-sweeps: partly).
- charge-regime-map marked partly: the regime is named AB and the maps exist, but the area check uses a separation inferred from the same period.
- Main text says VSi "further fine-tunes the separation between the interfering edge channels" (p. 2), while Supplementary Note 2 says VSi "is used on the right side to tune contact resistance" (p. 13). Not raised in the report.
- Faint weight near the origin of the Fig. 3c spectrum may or may not be a difference frequency; asked as a question without asserting.
- Fig. 1f inset labels (0.2, 2.7) and (0.1, 39.2) are rounded against ED1's 0.095 and 0.167 µm²; not raised.

## Skill issues
- Scope rule says to "adapt the matching entries", but here no entry's signature matches the claim exactly (spin structure, not fractional charge); unclear whether a loose physics match should count as a match or a skip.
- "Ruled out for the claim" needs the paper to "conclude against the lookalike"; for outside rows the paper never names the lookalike, so the bar is unclear (I used tested in part).
- charge-control-regime bundles two parts (absent in control regime; charge traps and gate leakage); with one part done the mark is necessarily "partly", which hides that the main part was done.
- Page numbering when the supplement restarts its own numbering is not specified; I used PDF page numbers.
- The template's "library of <n> known lookalikes in topological transport" reads oddly for an out-of-scope paper.
- Step 7 says to write reports/<id>.md files; this run's prompt overrides that (report given inline only).
- Step 5 says to start from matched entries' sources, but those sources (Halperin et al. 2011) were already in the library and not about this geometry; unclear whether to list library sources as related work.
