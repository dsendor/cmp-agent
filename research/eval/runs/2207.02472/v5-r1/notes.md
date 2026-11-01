# Run notes: arXiv 2207.02472v4 (lookalike assistant, run v5-r1)

AI only. 2026-10-24.

## Library and inputs
- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries, checks for families zbp, shapiro, kitaev, charge, practice.
- Read: the skill, report-template.md, the full library (entries, tests, checks).
- Paper: the local copies only (no fetch of the paper). abs.html confirms title "InAs-Al Hybrid Devices Passing the Topological Gap Protocol", Microsoft Quantum (Aghaee et al.), v4 of 8 Mar 2024, Phys. Rev. B 107, 245423. The PDF header reads "arXiv:2207.02472v4", so the version given (v4) is the one read.
- I extracted text per page with pdftotext (56 pages; printed page numbers equal PDF page numbers) and read the main text (Secs. 1 to 6, pp. 1 to 32) and the appendices (A to H, pp. 32 to 51) in full. I rendered pp. 24, 26, 27 as images to read the field, Vp and bias ranges of Figs. 16, 18, 19.
- Every quote in the report was checked against the per-page text with a whitespace and punctuation normalized match. Two quotes cross figure pages (pp. 19 and 22; pp. 22 and 23) and are cited with both pages; the p. 22-23 one is only used in the questions as a page pointer.
- No ancillary figure data on arXiv; read_mtx.py not used.
- Data repository: the paper links github.com/microsoft/azure-quantum-tgp (Ref. 98). I could not reach it: the GitHub API answered that access to this repository is not enabled for this session. I did not request access (out of scope for a test run). So no counts or ranges come from the repository.

## Claims table (step 1)
| Claimed signal | Figures | Device | Counts and ranges |
|---|---|---|---|
| Stage 1: clusters of (B, Vp) with ZBPs at both ends for > 70% of 21 cutter pairs (ROI1) | Fig. 10 (A1); Fig. 21 (F fails) | A (SLG-β); F | 21 cutter pairs, GN 0.01 to 0.85 e2/h; B 0 to 2.5 T; Vp window 30 mV above depletion (−1.18 V). Stage 1 maps for B, C, D, E not shown (text says "very similar ROI1s" in B, C, D, E, p. 16). |
| Stage 2: SOI2 with stable ZBPs, gapped interior, gapless boundary (78 to 100%) | Figs. 11, 33, 34 (A1); 13 (A2); 14, 15 (A3); 16, 17 (B); 18 (C); 19 (D); 20 (E fails) | A, B, C, D pass; E fails Stage 2 | A1: 3 cutter pairs (GN 0.3, 0.5, 0.7), B about 0.5 to 2.5 T, Vp about −1.168 to −1.175 V, bias about ±50 µV. A2: 4 pairs (0.3 to 0.9), B about 0.5 to 2.0 T, Vp −1.398 to −1.414 V, bias ±100 µV. A3: 4 pairs (0.3 to 0.8), B 0.75 to 1.6 T, Vp −1.405 to −1.411 V. B: 5 pairs (0.15 to 0.5), B 1.4 to 2.8 T, Vp −1.1550 to −1.1580 V (SOI2 at the lower edge, p. 25), bias ±80 µV. C: GN 0.6 to 1.0 left, 0.2 to 0.4 right (number of pairs not stated), B 0.7 to 1.5 T, Vp −2.360 to −2.366 V. D: GN about 0.8, B 0.7 to 2.0 T, Vp −2.705 to −2.725 V, bias ±100 µV. Ranges for B, C, D read from figure axes. |
| Maximum topological gap 17 to 61 µeV; SOI2 extent | Table III (p. 30) | A to D | 7 SOI2s (A1, A2, A3, B, C, D twice). Gaps on applied-bias axes; average bias correction 16% not applied (p. 50). |
| Gap closing depends on Vp (argues against orbital closing) | Fig. 13 (A2), Fig. 18 (C); B by a "large scale Stage 1 scan" not shown | A, B, C | Text only for B. |
| Simulated false discovery rate < 8% at 95% confidence | Table II | 349 simulated devices | 0 false positives at full field range; 1 false positive when B restricted to ≤ 2.5 T (p. 41). |
| Supporting: zero-field gaps, localization length > 1 µm, Hall-bar disorder | Figs. 6, 9, 25, 26, 36 | A; separate multi-segment device; Hall bars | One localization device. |

Counts: devices fabricated, not given. Devices measured: not given; six shown (A to F), "we have measured devices in which we were not able to find a topological phase" (pp. 22-23). Devices passing: four (A to D). Discard rule: junction pinch-off > −3 V (p. 12). Cooldowns: A has two (A1 in one fridge; A2 and A3 one week apart in another); B, C, D not stated. A "regularly passed the TGP, but also failed sometimes" (p. 22); number of runs not given. Temperature: one setting (base 20 mK, Te < 40 mK); no temperature series ("difficult to study this systematically due to voltage drifts", p. 22). Field direction: along the wire; rotation described in one sentence, no data. Lock-in frequency: several hundred Hz.

## Entries matched, skipped, adapted
- Matched (13): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, one-end-only, trivial-andreev-band-gap-reopening, protocol-parameter-sensitivity, local-probe-loophole, spin-orbit-length-pinning, exceptional-point-zero-mode, fine-tuning-and-selection.
- Checks walked: zbp family (6) and practice (3).
- Skipped: fine-tuned-plateau and series-resistance-subtraction (no quantized conductance is claimed; the paper says ZBPs "are not expected to have quantized values", p. 17; the zbp-raw-conductance check was still marked). micromagnet-stray-field (no magnets; finite applied field). full-shell-flux-andreev (partial Al strip on a 2DEG, no full shell). island-states-coulomb-spacing (no island measurement). chiral, shapiro (4 entries), supercurrent, charge (2), kitaev, diode families (signal types absent).
- Adapted: none; the paper is in scope (three-terminal transport).

## Hold-out (sources skipped)
- arXiv 2207.02472 itself: sources in quasi-majorana-smooth-confinement and fine-tuned-plateau; the zbp checks note_source; the zbp-transparency and zbp-nonlocal-gap check sources.
- Frolov et al. 2309.09368: its reference list cites "Microsoft Quantum, M. Aghaee ... devices passing the topological gap protocol. Phys. Rev. B. 107, 245423 (2023)". Held out wherever it appears (abs-quantum-dot, trivial-andreev-band-gap-reopening, fine-tuning-and-selection, zbp-dot-search, zbp-wide-ranges, zbp-raw-conductance).
- Hess, Legg, Loss and Klinovaja 2210.03507: ref. [65] is arXiv:2207.02472. Held out.
- Legg 2502.19560: a Comment on this paper. Held out.
- Checked and kept: Akrap, Frolov et al. 2501.18631v2 (no match for 2207.02472, Aghaee, Microsoft, 245423, "topological gap"); Prada et al. 1911.04512v3 (no match). Other kept sources predate July 2022 (v1 of this paper); I checked the latest arXiv versions of 2101.11456 (v1, Jan 2021), 2004.08583 (v1, Apr 2020) and 1206.6687 (v4, 2014) through the arXiv API.
- Effect: trivial-andreev-band-gap-reopening and protocol-parameter-sensitivity have no usable source left. I judged them from the entries' own mechanism, tests and control, and cite no source for them in the report.

## Judgment calls
- Kondo: the ZBP field dependence over 1 to 2.5 T is shown, so "Zeeman splitting in field" is marked all. The paper never mentions Kondo, so the status stays Tested in part.
- Crowded trivial subgap states: I counted the comparison of SOI2 extent, field and gap with the simulated distributions (Tables III and IV) as equivalent to "field and gate range compared with the predicted topological range". A stricter reading (all ZBPs, mapped for A1 only in Fig. 10) would give "part" and Tested in part.
- Spin-orbit length pinning: ruled out on the paper's general conclusion against trivial ABS (p. 13, p. 31). The paper doesn't name this mechanism.
- Local-probe loophole: ruled out by the one-test path; the entry's control says nonlocal measurement "or" a dot in series, so the nonlocal measurement is enough on its own.
- Trivial Andreev band: "protocol tested on trivial models" marked part because I can't tell whether any of the 349 disordered simulations forms a bulk Andreev band.
- Exceptional point: both-end correlation counted as an indirect overlap estimate, so part.
- Disorder-induced ZBP: cutter-gate stability counted as the "gates that should not matter" test.
- B, C, D: Stage 1 maps are not shown. I treated the Stage 2 figures as the evidence presented for those devices and put the missing Stage 1 maps under fine-tuning and questions only.
- Device B text places a trivial region at "Vp = −1.573 V" (p. 25), outside the plotted range of −1.155 to −1.158 V; probably a typo for −1.1573 V. Not used in the report.

## Related work: how each link was checked
All five: arXiv abstract page fetched (arxiv.org/abs/<id>) and checked for ID, title and first author; one-line descriptions checked against the abstract text (from the arXiv API record of the same ID). Full text not read for any.
- 2103.12217 Pikulin et al., v1 (2021). Abstract.
- 2006.01275 Puglia et al., v1 (2020). Abstract.
- 2201.03453 Banerjee et al., v1 (Jan 2022). Abstract.
- 2009.11809 Pan, Sau, Das Sarma, v3 (first posted 2020). Abstract.
- 1910.11413 Pan and Das Sarma, v2 (first posted 2019). Abstract. (It is also a library source of disorder-induced-zbp.)
- Left out on purpose: Hess et al. 2210.03507 and Legg 2502.19560 (held-out library sources that discuss this paper).

## Library gaps
- Orbital-effect gap closing in gate-defined wires: the paper raises it and argues against it from the Vp dependence of the closing (p. 31). No library entry. I ran an arXiv search (orbital, gap, nanowire, Majorana, trivial) and found no paper I could open that shows it as a lookalike, so no outside row.
- Sign changes in nonlocal conductance that inflate the extracted gap (paper, pp. 25 and 38). No entry for gap-extraction artifacts.
- Bias rescaling left unapplied (16%, p. 50): this affects extracted gap values (µeV). The series-resistance entry is written only for conductance quantization.
- Data-window-normalized thresholds (Gth = 0.05 × max GNL over the field range, p. 39): this is covered in spirit by protocol-parameter-sensitivity, whose only source is held out here. A non-held-out source would help.

## Skill issues
- Hold-out can remove every source of an entry (two entries here). The skill does not say whether to keep such an entry, drop it, or mark it. I kept it and cited no source.
- The library's checks section is built on this paper's own protocol (its comment says so, and three check sources are this paper). For this paper the checks partly restate the paper's design, so several "Done" marks are close to circular. The skill could say how to handle a paper that is itself a library source.
- "A test counts as shown only when the paper shows the measurement or analysis": unclear when the measurement is shown but never analyzed for that lookalike (Kondo, Zeeman splitting). I counted it as shown.
- "Ruled out" needs "the paper concludes against the lookalike". It is unclear whether a general conclusion (against trivial ABS) counts for a specific ABS mechanism the paper never names (spin-orbit length pinning).
- Step 7 says to write reports/<id>.md and .notes.md. The run prompt overrides this (no .md writes), so the report and notes go in the reply only.
- The word target (600 to 900 outside the table) is tight with nine checks and eight questions. I shortened the check names from the library wording to fit; the template does not say whether check names must be verbatim.
- Step 1 says to quote page numbers. For papers whose figure text interleaves with the body, a quote can cross figure pages. The skill could say how to cite that.

## Recognition
I recognized this paper (Microsoft Quantum's topological gap protocol paper) and know parts of its later history: the published comment, theory papers on trivial passes, and the public debate. I did not use that knowledge in the report. The rows on the trivial Andreev band and on protocol sensitivity come from library entries that already exist, judged against the paper's own text.

## Unsure
- Whether Stage 2 ZBP stability for device C uses the same number of cutter pairs as the others (the caption gives ranges only).
- Whether the deposited data include the runs where device A failed (repository not reached).
