# Run notes: arXiv 2608.12897v1 (lookalike assistant, skill-r1)

*AI only.* Run date 2026-10-23. Library: `cmp-assistant/library/lookalikes.yaml`, meta.version **0.4** (updated 2026-10-23), 28 lookalike entries plus `checks`.

## What I read
- arXiv abstract page (local copy `abs.html`): title "Observation of Time-Domain Braiding of Non-Abelian Anyons at $ν= 5/2$ State", Alkalay et al., v1 submitted 13 Aug 2026, comments "15 pages, 3 figures". No ancillary files are listed.
- Full text (local `paper.txt`, 40 pages), including the main text (pp. 1-15) and the Supplementary Notes (pp. 16-40). Page numbers in the report are PDF pages.
- I viewed the PDF images for pp. 3-6 (Figs. 1-3) and pp. 18-21 (Figs. S1-S4), and p. 39 (Fig. S9), to read the plotted ranges.
- No data repository is linked. "Source data are provided with this paper" (p. 13), but nothing is attached to arXiv v1, so I used no figure data. There are no .mtx files, so I did not run `read_mtx.py`.
- I did not read the two prompt files in the paper folder (`prompt_openaireview.txt`, `prompt_plain.txt`), since they are evaluation material.

## What I couldn't open
- Nothing failed to open. The source data are not on arXiv.

## Claims table (step 1)

| Claim | Figures | Device(s) | Counts and ranges |
|---|---|---|---|
| e* = e/4 from single-QPC partition noise | Fig. 1b (data set 4); S1-S4 panels b, f | All 3 devices | Bias about ±5 to 6 in e*V_S/2k_BT; T = 10 mK only |
| Charge-configuration excess noise above F = 1, matching PH-Pf (F_charge = 1.54 at 4.6; theory 1.49 PH-Pf, 0.94 A-Pf) | Fig. 2b (data set 4); S1-S4 c, d | Devices A, B, C; C twice | R_QPC about 0.1 to 0.27, V-dependent; bias ≤ about 6 |
| Neutral-configuration excess noise matching M_n = 0 braiding (F_neutral = 2.37 at 5.0; theory 2.33 PH-Pf, 2.0 A-Pf) | Fig. 3b (data set 3); S1-S4 g, h | Same | Same |
| Incoherent heating cannot explain the neutral signal | Fig. S9 (data set 4 only) | Device C, 2nd cooldown | Model underestimates by about 2x |
| Absence of tunneling current at the detection QPC in the neutral configuration | Stated pp. 34-37, not plotted | Not stated | Not stated |

Counts: 3 devices measured (p. 8; QPC gaps 1.2 µm on two devices, 1.3 µm on one; separation 1.4 µm in all). 4 data sets: A, B, C, plus C recooled with a +0.3 V gate bias (p. 16). All shown, all said to show the same behavior.

Missing: devices fabricated; QPC gate voltages; magnetic field and position on the 5/2 plateau; any temperature series; repeats within a cooldown; error bars or uncertainty on the gain, T and F; how set points were chosen; why the main-text panels come from data sets 4 and 3.

## Entries matched, skipped, adapted
- Scope adaptation: this is a shot-noise / anyon-statistics experiment. I used the `charge` family checks and the `practice` checks.
- Matched: `fine-tuning-and-selection` (always applies).
- Adapted: `series-resistance-subtraction`, reread as noise-gain, electron-temperature and normalization calibration moving the extracted Fano factor (through the `report-processing` check).
- Checks walked: `charge-control-regime` (adapted: no-anyon control for the two-QPC signal), `charge-repeat-sweeps` (adapted: repeated cooldowns and sweeps), `report-counts`, `report-ranges`, `report-processing`.
- Check skipped: `charge-regime-map`, which is interferometer-specific (no oscillations here).
- Entries skipped as inapplicable: all `zbp`, `quantization`, `nonlocal`, `island`, `shapiro`, `supercurrent`, `chiral`, `kitaev` and `diode` entries (no superconductor, no zero-bias peak).
  - `charge-trap-fractional-shift`: no Coulomb-blockade shifts are measured.
  - `coulomb-dominated-interferometer`: no interferometer.
  - `local-probe-loophole`: Majorana specific.
  - `protocol-parameter-sensitivity`: no pass/fail protocol, though bias-window choice is raised through `report-ranges`.

## Sources held out
- None. No library source cites this paper by title, authors or ID. Every library source predates Aug 2026; I checked the library text for the ID, the authors and "time-domain braiding".

## Related work: how each was checked
- 1005.5724 (Bid et al. 2010, Nature 466, 585): abstract page and full-text PDF. The temperature and distance decay is in the text (2/3 data, Fig. 4); the 5/2 neutral-mode noise is in Fig. 7.
- 0911.3023 (Dolev et al. 2010, PRB 81, 161303): abstract page and full text. At 5/2 the charge is "substantially higher" than e/4 at t of about 0.9 at low excitation, approaching e/4 near 75 mK.
- 1611.07359 (Fu et al. 2016, PNAS): abstract page and full text. The g values shift with confinement (331-like at strong confinement).
- 2401.06069 (Glidic et al. 2024, Nat. Commun. 15, 6578): abstract page and full text (grep of the time-domain braiding and co-propagating-channel passages).
- 2111.05399 (Schiller, Oreg, Snizhko 2022, PRB 105, 165150): abstract page only.
- Also opened but not listed:
  - 2209.15461 (Lee et al. 2023, the ν = 1/3 predecessor): abstract.
  - 2312.04475 (Thamm and Rosenow 2024): abstract.
  - 2606.17753 (Ratnakar et al. 2026, inter-edge interactions change the collider Fano factor sign at 2/5): abstract. It supports the Edge2 coupling row.
  - 2510.10525 (Safi 2025): abstract.
  - 1104.2723 (Dolev et al. 2011, neutral modes in the second Landau level): abstract.
- The arXiv API returned the paper under review in one search; I excluded it. API calls were spaced about 3 s apart, with no rate limiting.

## Library gaps (outside lookalikes added)
1. A family for shot-noise / anyon-collider / time-domain braiding signals is missing entirely.
2. Neutral-mode or charge-mode heating noise at a downstream QPC (Bid 2010; also Park et al. 2019 and Spånslätt et al. 2019, cited by the paper and not opened).
3. Nonuniversal tunneling charge at a QPC (Dolev 2010).
4. A different (Abelian) state or exponent inside a QPC constriction (Fu 2016), plus scaling-dimension extraction as a control (Schiller 2022).
5. Interchannel Coulomb coupling producing braiding-like signals (Glidic 2024; Ratnakar 2026).

## Unsure
- Whether integer channels actually co-propagate with the 1/2 channel along Edge2 depends on the gate geometry; I phrased that row as a request to state it.
- I marked the Abelian-QPC row "not addressed", the weaker choice: the p. 12 saddle-point remark is adjacent, not on point.
- I marked the heating row "partly" even though the paper says "ruling out": it is one model with assumed length hierarchies, on one data set, with no experimental control.
- The reduction factor C_rd ≃ 0.47 (p. 28) is fixed by numerics while the paper says "without any fitting parameter". I did not raise it because of the eight-question limit.
- Recognition: I did not recognize this paper (it postdates my knowledge) and used no outside history.

## Skill issues
1. Output paths: the skill says `reports/<id>.md` and `reports/<id>.notes.md`; the caller asked for `eval/runs/.../report.md` and `notes.md`. I followed the caller.
2. Checks have no "not applicable" status (and flags.json has no slot for one), so for a paper outside the families I had to drop `charge-regime-map` silently from flags and explain it only here.
3. The `charge` family check signal covers "quantum dots or quantum Hall interferometers"; noise-based statistics measurements fit no family. The Scope rule allows adapting, but gives no guidance on which checks to walk when the family fits only loosely.
4. Adapted entries: it is unclear whether a reinterpreted library entry (`series-resistance-subtraction` as gain calibration) should keep its library ID in flags or become an "outside" row.
5. Step 6 asks for the four standard questions "unless the paper already answers them (then say where)", but the template numbers them as fixed questions. It is unclear whether an answered question stays in the list (I kept them, with the location stated).
6. The template header asks for a "<short title>" while step 7 says "Use the title on the arXiv abstract page". I used a shortened form of the arXiv title.
7. Status rules ("across the regime the paper claims") are written for lookalikes; it is unclear how strict "done" should be for practice checks such as `report-counts` when device counts are given but setting counts are not.
8. The subagent environment refused to write report.md and notes.md (report-file guardrail), so the caller has to save them.
