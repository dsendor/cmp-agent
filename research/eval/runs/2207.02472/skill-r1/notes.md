# Run notes: arXiv 2207.02472v4, skill-r1

**Library:** lookalikes.yaml meta.version 0.4 (updated 2026-10-23); 28 lookalikes, 18 check steps. The skill, template and library were each read once at the start.

**What I read**
- abs.html: title "InAs-Al Hybrid Devices Passing the Topological Gap Protocol"; v4 dated 8 Mar 2024, "Final version"; PRB 107, 245423 (2023); no ancillary files.
- paper.txt: main text pp. 1 to 32 in full.
  - Appendices D, E, F, G and H read in full, since they define and apply the protocol.
  - Appendices A, B and C skimmed.
- I extracted per-page text from the supplied PDF with pdftotext and used it to confirm the page of every quote. PDF page numbers equal printed page numbers.
- I rendered p. 17 (Fig. 10) to check the Stage 1 ZBP maps.

**What I could not open or use**
- The data repository (Ref. 98, github.com/microsoft/azure-quantum-tgp) is outside this run's allowed fetch domains. No counts were taken from data.
- There are no ancillary .mtx files, so read_mtx.py was not used.

**Claims (step 1)**

| # | Claimed signal | Figures | Devices | Counts and ranges |
|---|---|---|---|---|
| 1 | Devices pass the TGP | Figs. 11, 13, 14, 16, 18, 19; Table III | A (A1, A2, A3), B, C, D | See note 1 below |
| 2 | Cutter-stable ZBPs at both ends | Figs. 10, 15, 21 | A to E pass Stage 1; F fails | See note 2 below |
| 3 | Bulk gap closing and reopening in A(GRL), A(GLR) | Figs. 11 to 14, 16 to 19; Fig. 20 (E fails) | A to D | Gapless boundary 78 to 100% (threshold 60%); Gth = 0.05 max{GNL}, the max taken over all B for each Vp (p. 39) |
| 4 | Topological gap 17 to 61 µeV | Table III | A to D | Δmax is the upper quintile within SOI2; median 20 µeV (A1), 47 µeV (B) |
| 5 | FDR below 8% | Tables II, IV, V | Simulations | 349 realizations for testing, 28 for calibration; restricting to B ≤ 2.5 T gives one false positive (p. 41) |
| 6 | Phase extent consistent with simulations | Table III vs IV | A to D | δB about 0.2 to 0.5 T; δVp about 1 to 2.5 mV |
| 7 | Localization length ≥ 1 µm under Al | Fig. 6, App. C | One multi-segment device | Segments L = 1 to 8 µm |
| 8 | Material specification met | Figs. 5, 25, 26; App. B | Hall bars on each chip | n2D,int 0.79 to 3.1 × 10^12 cm^-2 |

1. Six devices are reported and four pass (p. 3, p. 23). The total fabricated or measured is not given (pp. 22 to 23). Device A was measured in two cooldowns with three passing runs. Its failing runs are not counted (p. 22).
2. Stage 1 used 21 cutter pairs with GN from 0.01 to 0.85 e²/h for device A (p. 16), and "always at least 20" pairs in general (p. 39). Stage 2 used 3 to 5 pairs (A1: 3, A2: 4, A3: 4, B: 5). Thresholds: 70% (Stage 1), 60% (Stage 2), Ci% 50%.

**Ranges in the figures** (from axis ticks; the extracted text drops minus signs on Vp, so negative values are inferred from the text)

| Data | B | Vp | Bias |
|---|---|---|---|
| A1, Stage 1 (Fig. 10) | 0 to 2.5 T | −1.150 to −1.180 V | |
| A1, Stage 2 | 0.5 to 2.5 T | −1.168 to −1.175 V | ±50 µV |
| A2 | 0.4 to 2.0 T | −1.398 to −1.414 V | ±100 µV |
| A3 | 0.6 to 1.6 T | −1.405 to −1.411 V | ±100 µV |
| B | 1.4 to 2.8 T | −1.1550 to −1.1580 V | ±80 µV |
| C | 0.7 to 1.5 T | −2.360 to −2.366 V | ±60 µV |
| D | 0.8 to 2.0 T | −2.705 to −2.725 V | ±100 µV |
| E | 0.4 to 0.8 T | −1.3870 to −1.3900 V | ±50 µV |
| F, Stage 1 (Fig. 21) | 0 to 2 T | −0.830 to −0.860 V | |

- Stage 1 maps are shown only for A and F.
- Field is along the wire. Base temperature is about 20 mK and Te < 40 mK. There is no temperature series ("difficult to study this systematically due to voltage drifts", p. 22). No field-angle data are shown.
- Fig. 16 (device B) extends to 2.8 T, while p. 13 says the TGP focuses on B up to 2.5 T. This is folded into Q3.

**Missing counts:** devices fabricated, measured, and removed by the pinch-off check (p. 12); cooldowns for B to F; TGP runs and failures per device.

**Entries matched**
- abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states
- kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode
- one-end-only, trivial-andreev-band-gap-reopening, local-probe-loophole
- protocol-parameter-sensitivity, fine-tuning-and-selection

**Entries skipped, and why**
- fine-tuned-plateau: no quantized plateau is claimed, and the paper says peak height proves nothing (p. 17).
- series-resistance-subtraction: no value at 2e²/h is claimed. Its check (zbp-raw-conductance) was still walked.
- micromagnet-stray-field: there are no magnets.
- full-shell-flux-andreev: the Al strip only partly covers the 2DEG.
- island-states-coulomb-spacing: there is no island measurement.
- chiral, Shapiro (four entries), supercurrent, charge (two entries), Kitaev and diode entries: different signatures.

**Entries adapted:** none.

**Sources held out**
- 2207.02472 itself:
  - quasi-majorana and fine-tuned-plateau sources;
  - the zbp checks' note_source;
  - the zbp-transparency and zbp-nonlocal-gap step sources.
- 2309.09368 (Frolov et al.): cites the paper as its ref. 40 (found by grep of the full text). Every instance was held out:
  - entries: abs-quantum-dot, fine-tuned-plateau, series-resistance-subtraction, trivial-andreev-band-gap-reopening, micromagnet, full-shell, island, shapiro-nonlinear, field-enhanced-supercurrent, charge-trap, fine-tuning-and-selection (×2);
  - check steps: zbp-dot-search, zbp-wide-ranges, zbp-raw-conductance, shapiro-frequency-power, charge-control-regime.
- 2210.03507 (Hess et al.): cites it as ref. 65 (trivial-andreev-band-gap-reopening).
- 2502.19560 (Legg): a Comment on this paper, by title (protocol-parameter-sensitivity, ×2).

**Sources checked and kept**
- 2501.18631 (Akrap et al.): no mention found in the full text.
- 2101.11456 (v1 2021), 2004.08583 (v1 2020), 1911.04512 (v3 2020), 1806.02801 (v3 2019) and 1711.06256 (v2 2018): every version predates the paper (from their abstract pages).
- Other matched sources predate 2022 by arXiv ID.
- Not checked, because their entries were skipped: 2305.19970, 2408.10030, 2504.06732, 2403.07370, 2211.08710, 2205.09276.

**Related work:** each was checked on its arXiv abstract page for ID, title, first author and abstract content.
- 2103.12217 (Pikulin), 2009.11809 (Pan), 2006.01275 (Puglia), 2204.02430 (Pöschl), 2104.02671 (Martinez). The last also supports the outside row.
- One arXiv API search was used. Calls were spaced about 3 seconds apart.
- Opened but not used: 1509.02675 (Nijholt and Akhmerov; orbital effects) and 2206.08045 (a Kitaev chain paper, opened by mistake).

**Library gaps**
- Voltage-divider mixing of local into non-local conductance in three-terminal circuits. Added as an outside row from 2104.02671.
- No checks family for `nonlocal`. I used the zbp checks.
- Gap closing from the orbital effect (half flux quantum). The paper argues it away on p. 31. No opened source shows this exact mimic, so I did not add a row.
- Correlated trivial peaks at both ends from a state that spans a low-gap or long-coherence wire (the paper raises this for device E, p. 28). It is only partly covered by local-probe-loophole.

**Where I was unsure**
- spin-orbit-length-pinning: ruled out on Vp and cutter stability over small windows (δVp 1.5 to 2.5 mV).
- quasi-majorana: ruled out because the SOI2 definition requires a gapped interior. Quasi-MZMs before reopening are seen (p. 19), but outside the SOI2.
- local-probe-loophole: ruled out by the non-local measurement, although the overlap of the two end states is not quantified.
- weak-antilocalization: a stretch for a single-subband wire. Kept because App. H reports multichannel junctions.
- kondo-resonance: "partly" rests on a single B = 0 setting.
- zbp-raw-conductance: rated partly, not done, because the values sit only in the repository.
- Circuit row: rated ruled out although the DC bias axis is left uncorrected (1 to 6%).
- The report runs to about 950 words outside the table, a little over the 600 to 900 target.
- Quotes with subscripts follow the pdftotext rendering, for example "A(GRL )" and "SOI2 ".

**Recognition:** I recognize this paper (the Microsoft Quantum TGP paper) and know of later commentary on it. I did not use that knowledge. The statuses rest on the paper's text and the library entries.

**Skill issues**
1. Hold-out can empty an entry. All sources for trivial-andreev-band-gap-reopening and protocol-parameter-sensitivity were held out, and the skill does not say whether to still use such an entry. I used both on their control text.
2. Hold-out covers sources only. For this paper the library's own text comes from the paper and its critique:
   - the checks header says the checks are modeled on this paper's TGP stages;
   - protocol-parameter-sensitivity paraphrases the held-out Comment.
   The skill has no rule for entry text that comes from a held-out source, so this run is not blind.
3. Some check steps cite the paper itself as their source. I held out the source and kept the check; the skill does not say whether that is right.
4. The paper is both zbp and nonlocal, and only zbp has checks. "The checks for the paper's family" is unclear for papers that span families.
5. There is no tie-breaker for check statuses. I applied "pick the weaker one" by analogy with the lookalike statuses.
6. Nine checks with quotes, seven questions and five related-work lines make the 600 to 900 word target hard to meet.
7. The skill says to use a linked data repository. This run's allowed fetch domains excluded GitHub, and the skill does not say what to do when it is out of reach.
8. The skill writes to reports/<id>.md. This run redirected output to eval/, and the harness blocked .md writes by subagents.
9. Library page label: the quote "By design, Stage 2 of the TGP weeds out..." is labelled "Section 6, p. 31". In v4 it is in Section 5, p. 31. I did not edit the library.
10. "Verbatim quote" is unclear for math. Text extraction loses subscripts and the minus signs on gate voltages.
