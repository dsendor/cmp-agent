# Run notes: arXiv 2610.29124v1 (lookalike assistant, skill-r1)

*AI only.* Run date 2026-10-23. Library `meta.version` 0.4 (updated 2026-10-23), 28 lookalikes, checks for families zbp, shapiro, kitaev, charge, practice.

## What I read
- SKILL.md and report-template.md, read once at the start; lookalikes.yaml read in full, including `checks`.
- The arXiv abstract page (local copy abs.html): title, 8 authors, submitted 2026-10-21, v1. The comments field says "39 pages, including 20 pages of main text with 4 figures and 19 pages of Supplementary Information with 8 figures". No ancillary files are listed.
- The full text (paper.txt) and the PDF. I mapped page numbers with pdftotext per page (PDF page numbers; the main text starts p. 2, the SI p. 21). I rendered pp. 4, 6, 9, 12, 26, 30, 32, 35, 36 to read the figure axes.
- Data repository: none linked ("available from the corresponding authors upon reasonable request", p. 17), so there was nothing to count. No figure data, so read_mtx.py wasn't used.
- I did not fetch the paper itself. I did not open the two prompt_*.txt files in the paper folder.
- I didn't recognize the paper. It postdates my training data, so no later history was used.

## Claims table (step 1)
| Claimed signal | Figures | Device | Ranges and counts |
|---|---|---|---|
| Zero-applied-field diode, \|Ic+\| = 35.2 μA, \|Ic−\| = 28.9 μA, η = 9.8 % | Fig. 2a (p. 6-7), Fig. 2b half-wave rectification at 32.5 μA, 7.777 Hz; Supp. Fig. 1a, 5,000 cycles | one junction ("the same junction", p. 7) | 20 mK after zero-field cooling; one I-V shown |
| Field-dependent η, antisymmetric about Bx = −8 G, about −20 % to +20 % | Fig. 2c-d; Supp. Fig. 1b (η vs Bx − B0, ±20 G, 0 to 5 K); Supp. Fig. 2 histograms | same | Bx −100 to +100 G; 100 sweeps per field value; By −400 to +400 G (Supp. Fig. 3b); sweep direction for Fig. 2c not stated |
| Hysteretic Fraunhofer (main-lobe maxima at −6 G and +22 G) as interfacial magnetism | Fig. 3a | same | Bx −200 to +200 G, both sweep directions; one loop shown; no Bz data |
| Field-independent feature at V_MR ≈ 170 μV (about 82 GHz) as magnetic resonance; Fiske argued out via Bx vs By (17 μm vs 8 μm effective lengths) | Fig. 3b, 3d (simulation); Supp. Fig. 4 (By −800 to +800 G) | same (Supp. Fig. 4 says "same FTS vdW Josephson junction shown in Fig. 4", p. 32) | two in-plane field directions |
| Asymmetric ±1/2 Shapiro steps as second harmonic (I2/I1 = 0.7 effective) plus phase shift | Fig. 4 (5.776 GHz, Bx = 75 G); Supp. Fig. 6 (4.348, 7.580, 9.680 GHz at 75 G, n-p and p-n); Supp. Fig. 7; Supp. Fig. 5 (9.960 GHz, 0 G, set aside) | same | power −60 to 10 dBm (p. 15); Shapiro at only two field values (0 G, 75 G); Shapiro temperature dependence not shown |
| Junction formation | Fig. 1c STEM, Fig. 1d R(T): Tc,FTS ≈ 13.5 K, Tc,JJ ≈ 6 K | STEM specimen; R(T) device presumably the same | one specimen |

Missing counts: devices fabricated, devices measured, devices showing each effect (the abstract says "Our devices", p. 2), cooldowns, flake thicknesses, and the d_eff used in the flux formula (p. 24).

## Entries matched, skipped and adapted
- Matched directly: `diode-vortex-screening` (diode family), `fine-tuning-and-selection` (always included).
- Adapted: `shapiro-nonlinear-resistance`. Its signature is missing odd steps; I adapted it to a bias-dependent resistance feature (here the MR feature) shaping half-integer step weight in the bin-count maps. The Shapiro checks `shapiro-dc-curve`, `shapiro-frequency-power`, `shapiro-trivial-regime` and `shapiro-transparency` were adapted from missing-odd-step logic to half-integer-step and phase-shift logic. For `shapiro-trivial-regime`, the "regime where the effect is not expected" became a control junction or the mirrored field.
- Skipped:
  - `shapiro-landau-zener`, `switching-jump-blind-region` and `transparent-junction-pi-crossing`: they explain missing odd or first steps, or a 4π crossing, none of which this paper claims. At 75 G the paper reports no hysteresis or switching jump.
  - `field-enhanced-supercurrent-resonances`: the paper does not read field-enhanced supercurrent as exotic pairing.
  - `protocol-parameter-sensitivity`: there is no pass/fail protocol.
  - `local-probe-loophole`: not a local-probe Majorana claim.
  - All zbp, quantization, nonlocal, island, charge, chiral and kitaev entries: no such signals.
- Checks walked: practice (`report-counts`, `report-ranges`, `report-processing`) and the 4 adapted Shapiro checks. The library has no `diode` checks.

## Sources held out
None. Every library source predates this paper (v1 submitted 2026-10-21). The ones cited for the matched entries (Hou 2023, Zhang 2022, Mudi and Frolov 2022, Frolov 2023, Akrap 2026, Legg 2025) are about other systems. I did not open the library sources to search them for a citation of this paper; the hold-out rests on dates.

## Related-work and outside-lookalike verification
I opened each arXiv abstract page (arxiv.org/abs/<id>) and confirmed the ID, title and first author, and that the abstract supports the one-line description. All five were checked from the abstract only; none from full text.
- 2205.12196: Golod and Krasnov, abstract. It names "self-field effect from nonuniform bias and stray fields from a trapped Abrikosov vortex" and polarity switching "by changing bias configuration and by trapping/removing a vortex".
- 2303.00966: Qiu et al., abstract. Hysteresis only below Tc, "0-π phase mixing in the Fraunhofer patterns", "stochastic field-free superconducting diode effect".
- 2205.09276: Hou et al., abstract. Also a library source.
- 2306.08478: Li et al., abstract. "interfering Josephson diode effect", "second-order harmonic ... confirmed by half-integer Shapiro steps".
- 2109.13181: Yao et al., abstract. "co-existence of 0- and pi-states ... with the spatial variation of the NiFe thickness".
- Found by search but not listed: 2303.05951 (Iorio et al., half-integer steps of possible non-equilibrium origin, abstract opened) and 2108.13455 (Zhao et al., fractional Shapiro steps in twisted BSCCO, abstract opened). arXiv API searches were spaced about 3 s apart, with no rate-limit errors.

## Library gaps
1. No `checks` section for the diode family, and none for supercurrent, quantization, nonlocal, island or chiral either.
2. Missing diode lookalikes:
   - Self-field from nonuniform bias plus trapped Abrikosov vortices and magnet remanence, giving a "zero-field" diode and memory (Golod and Krasnov 2022).
   - Two-channel or edge interference giving a diode plus a second harmonic (Li et al. 2023).
3. No half-integer (fractional) Shapiro step entries. Candidates:
   - spatial 0/π mixing (Yao 2021);
   - inertial or underdamped dynamics (the paper itself cites Kautz 1996 for this; I did not open it);
   - non-equilibrium origin (Iorio 2023).
4. No entry for hysteretic Fraunhofer patterns read as magnetism (flux trapping in the electrodes, magnet remanence).
5. No entry for fixed-voltage resonances read as magnetic resonance: Fiske modes (the paper addresses them), and electromagnetic-environment or self-induced resonances. I found no source to open for the second, so it is not in the report.

## Unsure
- Quotes with math: pdftotext garbles math glyphs (for example "𝐵𝐵x", "𝐼𝐼 − 𝑉𝑉"). I wrote those symbols plainly (Bx, I − V) and kept the words verbatim. Superscript reference numbers were dropped from quotes.
- Page numbers are PDF page numbers. The quote "revealing a hysteretic response that is absent in conventional non-magnetic Josephson junctions" spans pp. 9-10.
- The three outside rows are rated "partly addressed" because the paper shows data or arguments that bear on them, without discussing the mechanism. "Not addressed" is a defensible weaker reading for the self-field and vortex row.
- I read the η period in Supp. Fig. 1b (sign changes roughly 10 to 13 G apart) and the By node near ±250 to 300 G from rendered figures; both are approximate.
- The "−91 G mirrored field" in question 7 is my arithmetic (−8 G − 83 G), not a number from the paper.

## Skill issues
1. Step 3 says to walk "the checks for the paper's family", but the diode family has no checks, and the skill doesn't say what to do then. I used practice checks plus adapted Shapiro checks.
2. The Scope rule covers adapting entries for "a different kind of measurement" (for example qubit data). It is unclear whether it also covers a different signal within transport (half-integer steps against the library's missing odd steps).
3. Step 7 says to write `reports/<id>.md` and `reports/<id>.notes.md`, while this eval asked for `eval/runs/.../report.md` and `notes.md`. I followed the caller. In this environment the Write tool refused .md report files from a subagent, so the contents went back as text.
4. The statuses "data bear on it; the paper doesn't discuss it" still need "a short verbatim quote from the paper". When the bearing data are a figure with no matching sentence, it is unclear what to quote; I quoted the nearest sentence.
5. The skill is silent on quoting text whose math is garbled by PDF extraction.
6. It is unclear whether outside-library sources also count toward the "up to five" related-work papers. I listed them in both places.
7. The template's "What this is" says "lookalikes in topological transport", which reads oddly for a non-topological diode paper. The template's status words are capitalized ("Done / Partly / Not done"), while flags.json uses lower case.
8. "Keep each table cell to one quote and one clause" is tight for outside rows, which also need the source URL in the Lookalike cell.
