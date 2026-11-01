# Run notes: arXiv 2608.12897v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes and the checks section. I read it once at the start, together with SKILL.md and report-template.md.
- Date of run: 2026-10-23. Version: v1 (the only version; submitted 13 Aug 2026, per the abstract page).
- Recognition: I did not recognize this paper. It is dated after my training data, and I used no outside knowledge of what happened to it later.

## What I read
- The local abstract page (abs.html): title, 10 authors, abstract, "15 pages, 3 figures", v1 only. It lists no ancillary files.
- The full text of the local paper.txt (40 PDF pages): main text pp. 1-12, references pp. 13-15, and the supplement pp. 16-40 (Note 1 on datasets, Note 2 on the theory of the Fano factors, Note 3 on the incoherent heating model). I checked page numbers against the PDF with pdftotext page by page. All page numbers are PDF pages. The supplement's printed page numbers sit at the top of each page and match the PDF pages.
- I rendered PDF pages 3, 4, 6 and 18 as images to read Figs. 1b, 2b, 3b and S1. They show no error bars, bias up to about ±5 (main text) or ±6 (supplement) in e*V_S/2k_BT, and QPC reflections of about 0.1 to 0.2.
- Data repository: the paper says "Source data are provided with this paper. All other data related to this paper are available from the corresponding author upon reasonable request." (p. 13). There are no arXiv ancillary files and no repository link, so I used no figure data and did not run read_mtx.py.
- I did not fetch the paper under review, as instructed.

## Claims table (step 1)

| Claimed signal | Figures | Devices / datasets | Counts and ranges |
|---|---|---|---|
| QP charge e* = e/4 from partition noise at the injection QPC | Fig. 1b (p. 3), Figs. S1-S4 panels b, f | Fig. 1b is data set 4 (Device C, second cooldown) | Fit to Eq. (1) at T = 10 mK; bias about ±5 in e*V_S/2k_BT |
| Charge Fano factor about 1.5, above the trivial value of 1, read as Abelian time-domain braiding of e/4 anyons; favors PH-Pf over A-Pf | Fig. 2b (p. 4), Figs. S1-S4 c, d | Fig. 2b is data set 4 | F_charge = 1.54 at e*V_S/2k_BT = 4.6, against 1.49 for PH-Pf and 0.94 for A-Pf (p. 12); no fitting parameters |
| Neutral Fano factor about 2.4, read as non-Abelian braiding (M_n = 0) | Fig. 3b (p. 6), Figs. S1-S4 g, h | Fig. 3b is data set 3 (Device C, first cooldown) | F_neutral = 2.37 at e*V_S/2k_BT = 5.0, against 2.33 for PH-Pf and 2.0 for A-Pf (p. 12); for data set 1 "the A-Pf prediction lies closer" (p. 17) |
| Incoherent heating ruled out | Fig. S9 (p. 39), Supp. Note 3 | Data set 4 only in Fig. S9 | Model falls short by "roughly a factor of two" |

Counts: "Three devices were measured" (p. 8): Devices A and B and Device C (QPC gaps 1.2 µm for two devices, 1.3 µm for one). There are four datasets; Device C was thermally cycled and cooled again with +0.3 V on a gate (p. 16). The paper implies all three showed the effect ("Measurements on the other devices show the same behavior", p. 7).
Missing counts: devices fabricated, cooldowns besides those listed, QPC settings or datasets set aside, magnetic field and plateau characterization (no R_xx or R_xy shown), temperatures other than 10 mK (no temperature dependence), and QPC separations other than L = 1.4 µm (the same in every device). Noise was measured at 720 and 690 kHz. The gain was calibrated by Johnson-Nyquist noise and checked at ν = 3 on a separate device (p. 8). The theory uses a reduction factor C_rd ≃ 0.47 taken from comparing numerical integrals (p. 28).

## Matching (step 2), skipped and adapted entries
- Scope: this is a shot-noise and Fano-factor experiment on fractional quantum Hall edges, outside the library's superconductor-semiconductor core. I said so in one sentence under "What this is".
- Matched directly: fine-tuning-and-selection (always included).
- Adapted: charge-trap-fractional-shift. Its signature is fractional shifts in Coulomb blockade or interference patterns. I adapted it to charge switching near the QPCs that modulates transmission and adds current-dependent excess noise. The paper raises QPC instability itself (p. 8).
- Adapted checks: charge-control-regime (a trivial-regime run of the same two-QPC sequence, plus gate leakage) and charge-repeat-sweeps (repeated datasets and cooldowns). The practice checks report-counts, report-ranges and report-processing apply as written.
- Skipped check: charge-regime-map. It needs a Fabry-Perot interferometer (Aharonov-Bohm versus Coulomb-dominated regimes); there is no interferometer here. I left it out of flags.json.
- Skipped lookalikes:
  - coulomb-dominated-interferometer: no interferometer and no enclosed bulk area.
  - All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: no superconductor, Josephson junction or tunneling-spectroscopy signal.
  - local-probe-loophole: about the separation of Majorana components; no local Majorana probe here.
  - protocol-parameter-sensitivity: there is no automated pass/fail protocol. The no-fit comparison to theory is a related issue, which I covered through the questions on data choices and temperature.

## Sources held out
- None. Every library source I used (Frolov et al. 2309.09368, Akrap et al. 2501.18631 v2 of 25 Mar 2026) predates this paper (13 Aug 2026), so none can discuss it. I checked the Akrap v2 date on its abstract page. I checked the other library sources by date only, not by reading them.

## Related work: how each was checked
I opened every abstract page on arxiv.org, waiting about 3 s between calls, after export.arxiv.org title searches. I confirmed the ID, title and first author from the page metadata, and each one-line description against the abstract.
- 2209.15461, Lee et al.: abstract only. Overlapping authors with the paper under review; it predates it.
- 2202.03649, Lee and Sim: abstract only.
- 1005.5724, Bid et al.: abstract only (noise from injected neutral modes at 2/3, 3/5 and 5/2).
- 2401.06069, Glidic et al.: abstract only.
- 2606.17753, Ratnakar et al. (June 2026, before this paper): abstract only.
- I also opened, and did not list, 2110.13925 (Morel et al., integer QH collider theory), 2006.13157 (Bartolomei et al.) and 2311.15094 (Iyer et al., finite anyon width).
- None of these discusses the paper under review.

## Library gaps
- The library has no family for shot noise or Fano factors (anyon colliders, time-domain braiding, fractional charge from noise). Candidate entries:
  - incoherent heating of upstream neutral modes producing noise at a downstream QPC (Bid et al., 1005.5724; theory in Park et al. 2019 and Spånslätt et al. 2019, cited by the paper as S8 and S9);
  - interaction-induced fractionalization between co-propagating channels mimicking time-domain braiding (Glidic et al., 2401.06069; Ratnakar et al., 2606.17753; Morel et al., 2110.13925);
  - finite anyon width or nonuniversal scaling dimensions shifting the predicted Fano factor (Iyer et al., 2311.15094);
  - transmission switching (telegraph or 1/f noise) in QPCs adding noise that grows as the current squared. I found no source for this one in this run, so it entered only as the adapted charge-trap row.
- The charge family's checks assume interferometers and dots. A noise-family check list (trivial-regime control in the same device, temperature calibration, QPC separation dependence, comparison with an Abelian alternative order) would fit papers like this one.

## Unsure
- Heating row: I chose "partly addressed" over "ruled out". The paper gives a direct argument, but it rests on one assumed length hierarchy (Eq. S56) and one heat split (Eq. S61), and Fig. S9 shows one dataset. When unsure, the skill says to pick the weaker status.
- Coulomb-coupling row: "not addressed". The paper discusses inter-mode equilibration lengths (p. 7), which is a different, incoherent process. I judged that the discussion does not bear on coherent fractionalization. Ratnakar et al. is theory; I counted it as a paper that "shows" the lookalike.
- report-ranges: "not done" over "partly". The bias windows are shown for every dataset, but nothing else is disclosed.
- Charge-trap row: the "partly addressed" rests on the stability sentence (p. 8) and on the injection-QPC noise following Eq. (1) (Fig. 1b). It is a judgment call, since the entry is adapted.
- Small inconsistency I noticed and did not raise in the report: the Fig. S9 caption uses data set 4, while the main-text Fig. 3b is data set 3. Question 8 covers it indirectly.
- Report length: about 950 words outside the table, above the 600 to 900 target, mostly because of the eight questions.

## Skill issues
- Scope adaptation is underspecified for a paper whose signal type (a Fano factor) has no library family. It is unclear whether adapting an entry with a different signature (charge-trap-fractional-shift) counts as a match or an adaptation. It is also unclear whether non-applicable checks in the matched family (charge-regime-map) should appear in the report and flags as "not done" or be omitted. I omitted them.
- Step 6 says to always ask the four standard questions "unless the paper already answers them (then say where)", but gives no format for a partial answer. I quoted the partial answer inside the question.
- Step 5 says to include an outside explanation only when a paper you opened "shows it". It does not say whether a theory paper counts.
- The hold-out rule asks you to skip library sources that discuss the paper, but checking that requires reading every source. I checked by publication date only.
- Step 7 says to write files under reports/. For this run the caller asked for chat output; no conflict, only noted.
- Page numbering: the skill doesn't say whether to use printed or PDF page numbers when they differ. I used PDF pages; here they agree.
- The 600 to 900 word target is hard to meet with eight questions that each carry a quote.
