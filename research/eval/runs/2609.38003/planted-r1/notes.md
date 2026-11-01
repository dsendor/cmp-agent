# Run notes: arXiv 2609.38003v1

AI only. Lookalike library version 0.4 (meta.updated 2026-10-23, 28 entries). Run date 2026-10-23.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml in full, including `checks`. Nothing else in cmp-assistant/ (per the task).
- The paper: the local extracted text (paper.txt, 14 pages, v1 dated 29 Sep 2026) and the local abstract page (abs.html: title, authors, abstract, "14 pages, 4+5 figures", cond-mat.supr-con). I did not fetch the paper in any form.
- No PDF, so no figures. Figure details come from captions; I used axis labels in the extracted text only cautiously (for example Fig. 3d appearing to span ±1 T and Fig. 3e ±4 T), and the report avoids relying on them.
- Extended Data Figs. 1 to 5 are in the text as captions. No separate supplement, no ancillary files, no data repository or data/code availability statement found. read_mtx.py not used (no .mtx data).
- Page numbers follow the page markers in paper.txt (p. 3 holds Fig. 2 text and the start of Fig. 3 results, p. 4 Fig. 3, p. 5 Fig. 4, p. 8 Methods for diode and nonlinear transport, p. 11 Extended Data Figs. 3 and 4).
- All quotes in the report were checked by script against paper.txt (whitespace normalized): all present.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges | Missing |
|---|---|---|---|---|
| Field-free SDE after ZFC, η about 7%, switching distributions well separated | Fig. 3a and inset (p. 3 to 4) | One 5 µm by 180 µm CuMnAs(12.4 nm)/AlAs(2.0 nm)/Al(9.2 nm) bar along [010], four-terminal | 20 mK base; 50 sweeps per polarity for the ZFC distributions; 50 µV switching threshold; 0.2 s step delay; Isw around 27 to 31 µA (inset axis) | Bars fabricated or measured, cooldowns, temperature dependence, how offsets were zeroed |
| Remanent polarity reversal by [100] preparation, up to about ±20%; weak, non-reversing [010] response | Fig. 3b to e (p. 4) | Same [010] bar | Prep ±1 T for Fig. 3b; Fig. 3d and 3e preparation ranges apparently ±1 T and ±4 T; 8 sweeps averaged per point | Reason for ranges, magnet type and residual field, whether reset fields drive Al normal, η vs small applied field |
| Anisotropy tied to crystal axes | Extended Data Fig. 4 (p. 11) | Second bar along [100] | Same protocol | Count of further bars |
| Néel-state correspondence | Fig. 4 (p. 5), Extended Data Fig. 5 (p. 12) | Reference CuMnAs bar from a different wafer with 3 nm oxidized Al cap, 20 by 10 µm; XMLD-PEEM on a 10 by 10 µm region | 5 K; ±4 mA; field sweeps along [100] and [010]; remanent Reven for prep "−5 to 5 T"; PEEM at about 100 K | Reven or remanent moment on the SDE heterostructure itself |
| Proximity tuned by AlAs thickness | Fig. 2c (p. 3), Extended Data Fig. 3 | Two heterostructures (2.0 nm, 1.5 nm AlAs) | 2.0 nm: Tc about 350 mK; 1.5 nm: no transition to 20 mK | No diode data versus spacer (1.5 nm is not superconducting) |
| Vanishing net magnetization | Fig. 2b (p. 3) | SQUID samples across the 2" wafer (number not given) | Bound 3×10−3 µB/Mn on a 3 mm by 5 mm by 12 nm sample | Remanent moment after the diode preparation protocol |

## Entries matched, adapted, skipped
- Matched: `diode-vortex-screening` (diode family; matched on physics, since the paper reads the T breaking as coming from the antiferromagnet's electronic structure, the library wording says "exotic pairing"); `fine-tuning-and-selection` (always).
- Adapted (scope rule; one sentence in "What this is"): `micromagnet-stray-field` (written for zero-bias peaks; physics of local stray fields from a magnetic layer breaking T transfers to a zero-field diode); `protocol-parameter-sensitivity` (written for pass/fail protocols; adapted to the threshold and sweep choices that define Isw and η).
- Skipped as not applicable to a superconducting film diode with no tunneling spectroscopy, junction, island, interferometer or dot chain: all zbp entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode), quantization (fine-tuned-plateau, series-resistance-subtraction), nonlocal (one-end-only, trivial-andreev-band-gap-reopening), chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro family (shapiro-landau-zener, shapiro-nonlinear-resistance, transparent-junction-pi-crossing, switching-jump-blind-region), field-enhanced-supercurrent-resonances (signature is supercurrent growing with field; not this claim), charge family (charge-trap-fractional-shift, coulomb-dominated-interferometer), false-poor-mans-majorana, local-probe-loophole.
- Checks walked: only the `practice` checks (report-counts, report-ranges, report-processing). The library has no `checks` block for the diode family.

## Sources held out
- None. The library sources used here (Hou et al. arXiv 2205.09276; Jiang et al. arXiv 2305.19970 and Frolov et al. arXiv 2309.09368 for micromagnet-stray-field; Legg arXiv 2502.19560; Frolov et al. and Akrap et al. arXiv 2501.18631 for practice entries) were posted before 29 Sep 2026 and are on other topics. I reasoned from dates and topics and did not open each to confirm. Legg and Akrap have 2026 v2 versions, which in principle could post-date the paper; I judged citation of this paper there very unlikely and did not check.

## Related work: how each link was checked
- 2205.09276 (Hou et al.): abstract page opened; ID, title, first author (Hou, Yasen) confirmed; description matches the abstract ("external magnetic fields as small as 1 Oe", "asymmetrical vortex edge/surface barriers and the universal Meissner screening current").
- 2512.05427 (Jiang et al.): abstract page opened and full text read in parts (PDF via arxiv.org/pdf, pdftotext). Confirmed: sign of zero-field SDE set by ±1 T in-plane poling field above the in-plane critical field; attributed to trapped flux; "Such hysteresis can often arise from a stray magnetic field due to the superconducting magnet. To rule out this possibility, we measured the resistance of few-layer graphene simultaneously during all measurements." Also seen in both I perpendicular and I parallel to H. This paper is ref. [29] of the paper under review.
- 2205.12196 (Golod and Krasnov): abstract page opened; ID, title, authors confirmed; description matches abstract (trapped Abrikosov vortex plus self-field; polarity switched by trapping or removing a vortex).
- 2601.03366 (Sachin et al.): abstract page opened; confirmed title, first author, up to 50%, compensated (T2) and nearly compensated (T1) order, "rich interplay of multiple contributing mechanisms". This is ref. [10] of the paper under review.
- 2610.30556 (Zapata et al., 22 Oct 2026, later than the paper): abstract page opened; confirmed the AlN spacer statement ("reduces electronic proximity effects while preserving magnetic coupling through stray fields"). Described only for its own results.
- Also opened but not listed (limit of five): 2206.00483 (Narita et al., field-free SDE in Nb/V/Co/V/Ta multilayers, polarity set by magnetization).

## Outside lookalike
- "Trapped flux or magnet remanence set by the preparation field", cited to Jiang et al. arXiv 2512.05427 (opened). Judged against that paper's controls (field calibration with a hysteresis-free sensor; dependence on field geometry). Status partly addressed: the orthogonal-bar result (Extended Data Fig. 4) bears on a field-versus-current geometry dependence, but a coil-specific residual field along [100] would also follow the crystal axis for both bars on one chip, so it does not settle it; the weaker response after the larger [010] excursion also bears on it if the same kind of coil is used.

## Library gaps
1. No zero-field diode lookalike for trapped flux or magnet remanence after a poling or preparation field (sources: arXiv 2512.05427, arXiv 2205.12196).
2. No `checks` block for the diode family. Candidate steps: control film without the magnetic layer; η versus small perpendicular field around zero after each preparation; thermal cycle of the superconductor above Tc at compensated zero field; magnet residual-field calibration; threshold and sweep-rate sensitivity of η; spacer series to separate proximity from stray fields (arXiv 2610.30556).
3. `micromagnet-stray-field` is written only for zero-bias peaks; a diode version (stray fields from magnetic layers or domain walls) would avoid adaptation.
4. Possible lookalike without a source I could cite: instrument current or voltage offsets in separately measured positive and negative sweeps biasing η. Not put in the table (no opened paper shows it); folded into the extraction-choices row as a processing check.

## Things I was unsure of
- Whether the extraction is missing a passage: refs. [28] to [30] (Hou et al., Jiang et al., Li et al.) appear in the reference list with no in-text citation, and there is a double space after "field-free diode response." on p. 6. I assessed the text as given and only noted in the report that I couldn't find where they are cited.
- The 4πM estimate: 3×10−3 µB/Mn times 2 Mn per cell (a = b = 3.80 Å, c = 6.32 Å from Methods) gives about 0.6 emu/cm3, 4πM about 7.7 G. This is a sample-averaged upper bound; local stray fields at bar edges or domain walls depend on geometry. Labeled "by my estimate".
- Status choices: every row is "partly addressed". For diode-vortex-screening and the outside row the paper shows data that bear on the mechanism without discussing it; I picked the weaker of "ruled out"/"partly" where the data cut only one way.
- Whether Al is superconducting at 1 T in-plane (9.2 nm film, Tc 350 mK) is not stated; it matters for flux trapping on the way back to zero.
- Recognition: I did not recognize the paper (dated after my training data); no knowledge of its later history was used.
- Shared scratch folder: a working folder I used for downloads and drafts (scratchpad/rw) is shared with other concurrent runs; another process overwrote my draft report there. I rewrote it in a private folder and verified every report question appears verbatim in flags.json. I did not read the other runs' files.

## Skill issues
- The library has no `checks` for the diode family, and the skill does not say what to do when a family has none. I walked only the practice checks and said so in the report.
- The template's "What this is" fixes the phrase "lookalikes in topological transport", which sits oddly for a non-topological diode claim; kept it per template and added the scope sentence.
- Scope rule: unclear whether a paper inside a library family (`diode`) whose reading is not "exotic pairing" counts as a "different kind of measurement". I treated it as in scope and adapted two entries from other families.
- Step 3 tension: "shows data that bear on it without discussing it" is "partly addressed", but every partly needs a quote; when the bearing data are described in a caption that does not mention the lookalike, it is unclear whether that quote qualifies. I used such caption quotes.
- Hold-out rule: does not say whether to open each library source to check it doesn't cite the paper; I reasoned from dates.
- Step 7 asks for files under reports/; this run returned them in the reply per the caller.
- Word target (600 to 900 outside the table) conflicts a little with eight questions plus five related-work lines; the report is about 910 words outside the table.
