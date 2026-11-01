# Run notes: arXiv 2610.29124v1

- Library: lookalikes.yaml meta.version 0.5 (updated 2026-10-24), 28 lookalikes. Skill: skill/SKILL.md, template skill/report-template.md. Run date 2026-10-24.
- Read: the supplied abstract page (abs.html: title, 8 authors, dated 2026/10/21, comments "39 pages ... 4 figures ... 8 figures") and the full extracted text (paper.txt, main text and SI, 39 pages). PDF pages were rendered to check figures: Fig. 2 (p. 6), Fig. 3 (p. 9), Fig. 4 (p. 11), Supplementary Figs. 1 (p. 26), 3 (p. 30), 6 (p. 35), 7 (p. 36). Page numbers are PDF pages (form-feed split of paper.txt, which matches the 39-page PDF). The paper itself was not fetched.
- Not available: the abstract page lists no ancillary files, and data are "available from the corresponding authors upon reasonable request" (p. 17), so there was no repository and read_mtx.py was not used. The theory reference "Ahn C-E, Shin S-H, Lee G-H, Cho GY. in preparation" (SI ref. 7) could not be read.
- Recognition: I did not recognize this paper and know nothing of its later history.

## Claims table (step 1)

| Claimed signal | Figures | Device | Counts and ranges |
|---|---|---|---|
| Zero-field JDE: Ic+ 35.2 μA, Ic− 28.9 μA, η 9.8% | Fig. 2a-b, SI Fig. 1a (5,000 square-wave cycles), SI Fig. 2 | one junction ("the same junction", p. 7) | 20 mK after zero-field cooling; 7.777 Hz bias; 100 sweeps per field point |
| Field-dependent η, antisymmetric about Bx = −8 G, about ±20% | Fig. 2c-d, SI Fig. 1b, SI Fig. 3a-b | same | Bx −100 to 100 G (Fig. 2c); B0-relative ±20 G at 0 to 5 K (SI Fig. 1b); By to ±400 G (SI Fig. 3b) |
| Hysteretic Fraunhofer (main lobe at −6 G and +22 G) | Fig. 3a | same | Bx ±200 G, both sweep directions; maximum sweep amplitude and number of sweeps not stated |
| Field-independent feature at ±170 μV, read as magnetic resonance (about 82 GHz); Fiske argued against | Fig. 3b,d; SI Fig. 4 (By) | same | Bx ±200 G; By sweep; 17 μm and 8 μm effective lengths |
| Half-integer Shapiro steps with ±1/2 asymmetry | Fig. 4, SI Figs. 6-7; Bx = 0 in SI Fig. 5 | same | Bx = 75 G at 4.348, 5.776, 7.580, 9.680 GHz; Bx = 0 at 9.960 GHz; power −60 to 10 dBm |
| Coupled RCSJ + LLG simulation reproduces these features | Fig. 3d, Fig. 4d-i, SI Figs. 3c-d, 8 | n/a | several parameters "adjusted" per figure (SI p. 23) |

Missing counts: devices fabricated or measured (the abstract says "Our devices"), cooldowns, number of field sweeps and their history, and ranges measured beyond those shown.

## Matching (step 2)

- Matched: diode-vortex-screening (diode family; adapted from thin films to a vertical junction, where the analogous ordinary mechanism is screening currents and self-fields in the FTS electrodes) and fine-tuning-and-selection (always).
- Checks: the library has no `checks` for the diode family, so only the practice checks (report-counts, report-ranges, report-processing) were walked.
- Skipped, shapiro family (shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, transparent-junction-pi-crossing) and its checks: these concern missing odd steps or a 4π effect, and the paper reports extra half-integer steps (a π-periodic second harmonic). The shapiro-dc-curve idea is partly relevant: the paper shows the absence of I-V hysteresis at 75 G (SI Fig. 6) but no dV/dI without irradiation marked at hf/4e.
- Skipped, field-enhanced-supercurrent-resonances: its signature is supercurrent growing with field, read as triplet pairing, which this paper does not report.
- Skipped, protocol-parameter-sensitivity: there is no pass/fail protocol.
- Skipped, local-probe-loophole: it concerns Majorana separation.
- Skipped, the zbp, quantization, nonlocal, island, charge, chiral and kitaev entries: they do not fit this device or signal.
- Adapted: diode-vortex-screening, as above.

## Outside rows (library gaps)

- Self-field diode shifted to zero field by trapped flux. Source: Golod and Krasnov 2022, arXiv 2205.12196, full text read. Their controls are changing the bias configuration (flips polarity) and trapping or removing an Abrikosov vortex. They also show that self-field nonreciprocity is centrosymmetric, Ic+(H) = −Ic−(−H). The −8 G centre of η(Bx) in this paper has the same symmetry about an offset field, which made this row relevant. "Part" on the trapped-flux test: one zero-field-cooled state is shown, with no reset or deliberate-trapping comparison.
- Trapped vortices from remanent field or field history. Source: Zhu et al. 2025, arXiv 2512.01586, full text read. Half-integer steps are unstable under thermal cycling, return after small-field training with sweep-direction hysteresis, and the remanent field was measured with a fluxgate. This bears on both the half-integer steps and the hysteretic Fraunhofer. Status "argued, not tested": the paper argues that hysteresis is "absent in conventional non-magnetic Josephson junctions" (pp. 9-10) but shows none of the three tests.
- Interference with a second current path. Source: Kalashnikov et al. 2025, arXiv 2510.15526, abstract and parts of the full text read. Shapiro asymmetry from two parallel paths oscillates with the SQUID period. The paper itself suggests a parallel channel for the 11 G fast component (p. 8). Status "data bear on it" because Fig. 2c-d and SI Fig. 3a show that component.
- Not added for lack of an opened source: inertial or underdamped dynamics as a source of half-integer steps (the authors raise it themselves, SI p. 34, and address it with the overdamped 75 G data); environmental or circuit resonances for the 170 μV feature; a current-source offset as a cause of Ic+ ≠ |Ic−| (it could be checked against the retrapping currents).

## Hold-out

No library source discusses this paper: all sources predate 2026-10-21 or concern other topics (the Legg comment concerns the TGP). The arXiv search listing for "Shapiro diode asymmetric" returned 2610.29124 itself as a hit. I did not open it.

## Related-work checks

Each paper below was confirmed by opening its arXiv abstract page (ID, title, first author), plus the arXiv API abstract.

- 2205.12196: Golod; full text read (Figs. 1-4 text).
- 2512.01586: Zhu; full text read (thermal cycling, field training, Methods remanent field).
- 2510.15526: Kalashnikov; abstract plus a grep of the full text for the periodicity and asymmetry passages.
- 2205.09276: Hou; abstract.
- 2303.00966: Qiu; abstract. The arXiv title differs from the Nat Commun title cited in the paper (ref. 19); the arXiv title is used.

## Unsure

- Whether field following (Fig. 2c-d) should count as "all" for the diode-vortex-screening test "Effect followed against field, sample width or edge quality". It is shown for the one junction, but it does not separate the lookalike.
- Whether zero-field cooling counts as "part" of the trapped-flux test. I chose part.
- SI Fig. 7 caption says "replotted from the same dataset as Fig. 3c" and refers to "Fig. 3d", while the text says the data are Fig. 4. This looks like a figure-number slip; it is not in the report.

## Skill issues

- The diode family has library entries but no `checks` section, and nothing covers extra (half-integer or fractional) Shapiro steps read as a second harmonic. The step 3 instruction "go through the checks for the paper's family" has nothing to walk for such papers.
- The flags.json `note` field takes "argued, not tested" or similar only for "Not tested". It is unclear whether a "Tested in part" row may carry a note; I used null.
- Outside rows need a "short name"; the report and flags use slightly different wording (the report adds the source). It is unclear whether they must match exactly.
- The "Hold-out rule" says to skip library sources that discuss the paper, but it does not say what to do when an arXiv search lists the paper under review. I ignored it without opening it.
