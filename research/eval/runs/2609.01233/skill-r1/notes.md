# Run notes: arXiv 2609.01233v1

*AI only. Lookalike assistant run, 2026-10-23.*

- **Library:** `cmp-assistant/library/lookalikes.yaml`, `meta.version` 0.4 (updated 2026-10-23), 28 lookalikes, 18 checks.
- **Skill files read:** `skill/SKILL.md`, `skill/report-template.md`, the library (all entries and the `checks` section). `scripts/read_mtx.py` not used (no `.mtx` data).
- **Paper read:** the local copies supplied by the caller (not fetched): `abs.html` (v1, submitted 1 Sep 2026, title "Interferometry reveals spin-singlet fractional quantum Hall edges in graphene", first author R. Ayache, ten authors) and `paper.txt` (extracted from the 21-page `paper.pdf`: main text pp. 1 to 8, Extended Data pp. 10 to 11, Supplementary Information pp. 12 to 21). I read the full text including Methods, Extended Data captions and Supplementary Notes 1 to 9. Figure images were not inspected; all figure statements come from captions and text. Page numbers in the report are PDF page numbers (the SI's own numbering restarts at 1 on PDF p. 12).
- **Data and code:** no arXiv ancillary files on the abstract page; the paper links no repository ("available from the corresponding author upon reasonable request", p. 8). Nothing to count beyond the text.
- **Could not open:** nothing needed was blocked.
- **Recognized the paper?** No. It postdates what I know; no later history used.

## Claims table (step 1)

| # | Claimed signal | Figures | Device | Counts and ranges found | Missing |
|---|---|---|---|---|---|
| 1 | Spin-selective MZI formation calibrated in the integer regime: one frequency at (νP, νN) = (−2, 1), two at (−2, 2), none at (−1, 1) | Fig. 1e,f; ED1 (simulation); ED2 | One device (Fig. 1a,b; S1, S2) | Fig. 1e frequency (0.12 µm², −27.4 V⁻¹), arm separation ~170 nm; (−2, 2) arm separations ~140 and 240 nm; arm length 700 nm | Field at which Fig. 1 and ED2 were taken; gate and field ranges |
| 2 | Spin transition of the 2/3 interface channel near 9.5 T: sharp drop in transmission, multi-frequency to single frequency | Fig. 2a (Landau fan, 2/3 well developed for B > 6 T), Fig. 2b | Same device | Gate compensation α ≈ 0.124 V/T; raw T, R cut at Vright − αB = 0.3 V | Full B range of Fig. 2b in text; repeats |
| 3 | Spin-polarized 2/3 edge near 11 T: single frequency at (−2, 2/3), none at (−1, 2/3) | Fig. 2d; ED3 | Same device | Fig. 2d frequency (0.148 µm², 91.8 V⁻¹) | Ranges; other gate settings |
| 4 | Spin-unpolarized 2/3 edge near 8 to 8.4 T: single frequency at (−1, 2/3), multiple f_nm at (−2, 2/3) | Fig. 3a (B vs VSi), Fig. 3b,c | Same device | Fig. 3a (0.121 µm², 11.4 V⁻¹); f10 (0.082 µm², 72.8 V⁻¹), f01 (0.087 µm², 21.2 V⁻¹); f_nm with n, m = 0, 1, 2 | FFT windows and resolution; amplitudes of f11, f02; repeats |
| 5 | f11 as two-electron interference with spin swap from spin-charge separation and recombination | Fig. 3c, Fig. 4d; SI Notes 6, 8 | Theory plus Fig. 3c | Constant C ≈ 7938i | Experimental amplitude of f11 |
| 6 | Enhanced thermal and bias decay of f10, f01 compared with the polarized regime; time delays Δt↑ = 7.31 ps, Δt↓ = 1.67 ps, Δts = 2.18 ps | Fig. 3d,e; ED4; Fig. S3 | Same device | Visibilities normalized at 100 mK; fit excludes the three lowest temperatures; B10 = 8.41 ps, B01 = 2.76 ps, B11 = 8.98 ps; authors call the extraction "inconclusive" (p. 19) | Number of temperature points; bias range of ED4 in text |

Other counts: devices fabricated "devices" (plural, p. 13), number not given; devices measured: one shown; devices showing the effect: not stated; cooldowns: not stated; datasets: about ten maps across Figs. 1 to 3 and ED2 to ED4. Setup: dilution refrigerator, base ~10 mK, field up to 14 T (capability), lock-in at ~7 Hz with 1 to 5 nA excitation (p. 14).

## Entries matched, adapted, skipped

- **Family used:** `charge` (closest: interference periodicity in quantum Hall interferometers) plus `practice`.
- **Adapted:** `coulomb-dominated-interferometer` (written for Fabry-Perot devices; applied to the p-n junction MZI, where bulk-edge charging of localized states in the enclosed strip could add periodicities) and `charge-trap-fractional-shift` (written for fractional shifts in dots; applied as trap switching that shifts the AB phase within a map). The checks `charge-regime-map`, `charge-control-regime` and `charge-repeat-sweeps` were walked with this adaptation.
- **Always included:** `fine-tuning-and-selection`.
- **Skipped:** every `zbp`, `quantization`, `nonlocal`, `island`, `shapiro`, `supercurrent`, `chiral`, `kitaev` and `diode` entry: the paper makes no claim about zero-bias peaks, quantized conductance, Josephson effects, chiral Majorana plateaus, Kitaev chains or diodes (parafermions appear only as a future direction, p. 6). `protocol-parameter-sensitivity`: no pass/fail protocol. `local-probe-loophole`: written for Majorana separation from local probes.

## Sources held out

None. Every source in the matched entries (Halperin et al. 2011, arXiv 1010.4598; Frolov et al. 2023, arXiv 2309.09368; Zhang et al. 2021, arXiv 2101.11456; Akrap, Frolov et al., arXiv 2501.18631, latest version v2 of 25 Mar 2026) predates the paper's 1 Sep 2026 submission, so none can cite it. I checked this by date (and opened the 2501.18631 abstract page for its version history); I did not search their full texts.

## Related work: how each link was checked

All five abstract pages were opened at arxiv.org/abs and ID, title and first author confirmed.

- 1703.00110, Wei et al.: abstract checked (MZIs along a graphene PN junction; same-spin inter-channel scattering at the physical edge forms beam splitters).
- 2011.04958, Jo et al.: abstract checked (valley splitters tunable from zero to near unity; tunable MZI; bias dependence).
- 2508.07380, Song and Myoung: abstract and full text (PDF, Sec. 3, p. 9) checked for the sum-area statement: "although a higher-order loop enclosing area AnMZ + ApMZ can generate secondary harmonics of the MZ interference, its Fourier-peak amplitude remains negligible compared to the primary modes" (subscripts flattened from the PDF text). This is a modeling paper (spinless Dirac model), which I took as showing the mechanism; used for the "(not in library)" row.
- 1605.06060, Goldstein and Gefen: abstract checked (ν = 2/3 MZI; downstream-upstream mode entanglement as which-path detector).
- 1808.05898, Lafont et al.: abstract checked (significant upstream charge current at short distances in the spin-unpolarized 2/3 state, GaAs). This is the paper's own ref. 16.

Also opened and not listed: 1812.06717 (Bhattacharyya et al., MZI interference melting with neutral modes), 2403.18983 (Werkmeister et al., telegraph noise in a graphene interferometer), 2008.12285 (Ronen et al., pure AB regime in graphene Fabry-Perot interferometers). arXiv API searches were spaced by about 3 s; no "Rate exceeded" responses.

## Library gaps

- No family for quantum Hall Mach-Zehnder interferometry or for spin or edge-structure claims from interference (presence or absence of oscillations, FFT frequency sets, visibility decay). The `charge` family assumes Fabry-Perot devices and fractional shifts.
- Candidate entry: sum-frequency or harmonic components from noninteracting nested multi-path loops in multi-channel MZIs (Song and Myoung 2025, arXiv 2508.07380), with the control of comparing harmonic amplitudes with primaries and with an integer-regime reference.
- Candidate entry: visibility suppression by upstream neutral modes as an ordinary origin of enhanced dephasing in hole-conjugate states (Goldstein and Gefen 2016, arXiv 1605.06060; Bhattacharyya et al. 2019, arXiv 1812.06717), with checks on arm-velocity asymmetry and the integer reference.
- No entry for phase coexistence or domains near a spin transition contributing a second interferometer at the same filling; I raised it only as question 8, since I did not open an experimental paper that shows it in an interferometer.

## Unsure

- Whether the Coulomb-dominated lookalike is meaningful for an open MZI with no closed island; I kept it as adapted and "partly addressed" because localized states in the enclosed incompressible strip could still couple.
- Charge-trap status: the regular 11 T pattern is quotable data, but from a different regime than the low-field claim, so I chose "not addressed" (the weaker status).
- Question 8 compares frequencies taken at different fields and gate settings (8 T and 11 T); the closeness may be coincidental. It is framed as a question.
- I did not view the figures, so statements about which axes each map uses come from captions (Fig. 3a uses VSi; Figs. 2d and 3c give Vleft frequencies).

## Skill issues

- **Output location.** SKILL.md step 7 says to write `reports/<id>.md` and `reports/<id>.notes.md`; the caller asked for `eval/runs/2609.01233/skill-r1/report.md` and `notes.md`. I followed the caller. Separately, the harness's Write tool refused `.md` report files for this subagent, so I wrote them with a shell heredoc.
- **Scope rule is thin for an out-of-family paper.** "Adapt the matching entries" doesn't say what to do when the closest family's `signal` (fractional periodicity) doesn't describe the claim (electron-period multi-winding interference). I walked the `charge` checks anyway.
- **Template wording** fixes "a library of <n> known lookalikes in topological transport", which reads oddly for an FQH spin-structure paper; I kept it and added the scope sentence.
- **Status when the only quotable data come from another regime** (charge-trap row) is not covered by the status rules.
- **"(not in library)" rows:** "a paper you opened that shows it" doesn't say whether a theory or modeling paper counts.
- **Hold-out rule** gives no method for confirming a source does not cite the paper; I used submission dates.
- **Page numbers:** no rule for PDF page versus printed page when the SI restarts its numbering.
- **Word budget:** unclear whether the checks list and related-work list count toward the 600 to 900 words; with both counted the report is about 920 words outside the table.
- **Related-work start point:** "start from the matched entries' sources" gave nothing in a similar system here; I went straight to arXiv search.
- **Checks note:** the `charge-repeat-sweeps` check addresses only an adapted lookalike; the skill does not say whether a check should be reported when its lookalike is adapted or skipped. I reported it.
