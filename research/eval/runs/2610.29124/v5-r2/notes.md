# Run notes: arXiv 2610.29124v1

- Library: lookalikes.yaml meta.version 0.5 (updated 2026-10-24), 28 lookalike entries.
- Date of run: 2026-10-24. Paper version v1 (given). AI only.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all entries, tests and checks), read once at the start.
- Paper: the provided extracted text (paper.txt, main text and SI, 39 pages) and the provided abs.html (title, authors, abstract, comments: 20 pages main with 4 figures, 19 pages SI with 8 figures). No ancillary files listed on the abstract page. I did not fetch the paper.
- Page numbers come from pdftotext run page by page on the provided PDF. I rendered PDF pages 4, 6, 9, 11, 12, 26, 27, 30, 32, 34, 35, 36 and 38 to PNG and looked at Figs. 1-4 and Supp. Figs. 1, 3, 5 and 6.
- Data: "available from the corresponding authors upon reasonable request" (p. 17). No repository to reach, so counts come from the paper only. read_mtx.py not used (no .mtx files).
- I did not recognize the paper (posted 2026-10-21) and used no knowledge of its later history.

## Claims table (step 1)
| Claimed signal | Figures | Device | Counts and ranges |
|---|---|---|---|
| Zero-field JDE: abs(Ic+) = 35.2 μA, abs(Ic−) = 28.9 μA, η = 9.8% | Fig. 2a-b (p. 6-7), Supp. Fig. 1a (5,000 square-wave cycles), Supp. Fig. 2 (histograms) | one junction | 20 mK after zero-field cooling; 100 sweeps per field; square wave 32.5 μA at 7.777 Hz |
| Field-dependent diode, η from about −20% to +20%, antisymmetric about Bx = −8 G | Fig. 2c-d, Supp. Fig. 1b (0 to 5 K), Supp. Fig. 3a-b | same junction | Bx ±100 G, By ±400 G; sweep direction for Fig. 2c not stated |
| Hysteretic Fraunhofer (main lobe at −6 G and +22 G for opposite sweeps) read as interfacial magnetism | Fig. 3a | same junction | Bx ±200 G, two sweep directions |
| Voltage feature near ±170 μV (about 82 GHz) read as magnetic resonance; Fiske excluded via Bx and By | Fig. 3b, Supp. Fig. 4 | same junction | effective lengths 17 μm (Bx) and 8 μm (By) |
| Asymmetric ±1/2 Shapiro steps read as I2 plus magnetization phase shift | Fig. 4, Supp. Figs. 6-7; Bx = 0 G data in Supp. Fig. 5 | same junction | 75 G at 4.348, 5.776, 7.580, 9.680 GHz; 0 G at 9.960 GHz; power −60 to 10 dBm |
| Simulations (RCSJ, RCSJ + LLG) reproduce features | Figs. 3d, 4d-i; Supp. Figs. 3c-d, 8 | model | α differs across Eqs. S5, S7, S10 |

- Missing counts: devices fabricated, measured and showing each effect; cooldowns; datasets set aside. The abstract says "Our devices"; Supp. Fig. 4 is "the same FTS vdW Josephson junction shown in Fig. 4". No out-of-plane field data are mentioned.

## Entries matched, adapted, skipped
- Matched: diode-vortex-screening (diode family), fine-tuning-and-selection (always).
- Adapted: field-enhanced-supercurrent-resonances, from "supercurrent growing with field" to the fixed-voltage feature at 170 μV and its effect on switching (same physics: an ordinary finite-voltage resonance). shapiro-nonlinear-resistance, from missing odd steps to half-integer bin-count features; its third test ("even steps go missing in other regimes") was judged as "is the anomaly seen in other regimes", using the Bx = 0 G map. Shapiro checks (dc curve, frequency-power, trivial regime, transparency) adapted to half-integer steps; the trivial-regime check was read as "a regime or control junction with no interfacial magnetization".
- Skipped: all zbp, quantization, nonlocal, island, chiral, charge and kitaev entries (no zero-bias peaks, quantized conductance, islands, interferometers or dot chains). shapiro-landau-zener, switching-jump-blind-region and transparent-junction-pi-crossing (about missing odd or first steps and a zero crossing at π, no counterpart here). protocol-parameter-sensitivity (no pass/fail protocol). local-probe-loophole and micromagnet-stray-field (Majorana or zero-bias specific; the stray-field idea reappears in the outside row on trapped vortices).
- Simulations were not counted as a shown test (step 3 asks for a measurement or analysis of the data).

## Hold-out
- No library source skipped. All library sources are dated before 2026-10-21 by their arXiv versions, so none can cite this paper. I did not text-search them.

## Related work: how each was checked
- 2205.09276 Hou et al.: abstract page opened; ID, title, first author (Hou, Yasen) and description confirmed from the abstract.
- 2205.12196 Golod and Krasnov: abstract page opened; confirmed from the abstract.
- 2303.00966 Qiu et al.: abstract page opened; confirmed from the abstract. Probably the arXiv version of the paper's ref. 19 (Nat. Commun. 2023); the arXiv title differs from the journal title.
- 2004.14039 Ueda et al.: abstract page opened; confirmed from the abstract.
- 2512.01586 Zhu et al.: abstract page opened; confirmed from the abstract.
- Also opened, not listed: 2207.03633 (Sundaresh et al., diamagnetic diode in multilayers), 2303.05951 (Iorio et al.). arXiv API searches spaced about 3 s apart; no rate limits hit.

## Library gaps
- No checks section for the diode family.
- No entry for a zero-field diode from self-field of nonuniform bias, trapped vortices, or a magnet's residual field (outside row from 2205.12196).
- No entries for half-integer Shapiro step lookalikes: skewed CPR in transparent junctions (2004.14039), trapped vortices (2512.01586), inertial or underdamped dynamics (the paper raises this itself, Supp. p. 34, citing Kautz 1996, which I did not open), and nonuniform phase near a Fraunhofer node (no source found).
- No entry for fixed-voltage features from Fiske modes or circuit resonances. The paper tests Fiske itself (Supp. Note 4). I found no Fiske source on arXiv to open, so no outside row.
- No entry for hysteretic Fraunhofer patterns from flux trapping in the electrodes.

## Unsure
- Whether "effect followed against field" alone should count as "all" for diode-vortex-screening. I counted it because the test text allows field, width or edge quality.
- The outside self-field and vortex row is marked "data bear on it". Zero-field cooling (p. 7) resets vortices only if the residual field is zero, so I did not count it as a test.
- Small inconsistencies in the paper that I left out of the report: Supp. Fig. 7 refers to "Fig. 3c" and "Fig. 3d" for Shapiro data shown in Fig. 4; the Fig. 3 caption says "Differential conductance (dV/dI)"; the Fig. 3d caption cites Supp. Note 3 where the text cites Note 4; the Methods and Supp. Note 2 name the switching branches n-p and p-n, the main text 0-p and 0-n.

## Skill issues
- The template asks for a "<short title>", while step 7 says to use the title on the arXiv abstract page. I used the full arXiv title.
- The scope rule covers a different kind of measurement, but not a known family (Shapiro) with a different anomaly (half-integer steps where the library has missing odd steps). Whether to adapt or skip those entries is unclear. I adapted them and said so.
- Step 3 says to walk "the checks for the paper's family", but the diode family has no checks. I walked the Shapiro checks (adapted) and the practice checks.
- When a library test text does not fit an adapted entry, the skill does not say whether to keep it verbatim or reword it. I kept it verbatim and explained my reading here.
- The skill does not say whether simulations count as "shown" for a test.
- Step 7 says to write the files to reports/; this run asked for chat output, which I followed.
