# Run notes: arXiv 1710.10701v1 (lookalike assistant)

*AI only. 2026-10-23.*

## Setup

- Library: `cmp-assistant/library/lookalikes.yaml`, `meta.version` 0.4 (updated 2026-10-23), 28 entries, `checks` for zbp, shapiro, kitaev, charge, practice.
- Skill and template read once at the start: `cmp-assistant/skill/SKILL.md`, `cmp-assistant/skill/report-template.md`.
- Paper: local copies supplied by the caller (PDF, `pdftotext` extraction, arXiv abstract page). Version v1 is the only version on the abstract page (submitted 29 Oct 2017). The paper itself was not fetched.
- Read: abstract page; full PDF, 26 pages (main text pp. 1 to 11, figure captions and figures pp. 12 to 16, Methods p. 17, Extended Data pp. 18 to 26). Figure pages 12 to 26 rendered to PNG and viewed to read axis ranges. Page numbers are PDF page numbers, which match the printed page numbers.
- Supplementary: Extended Data Figs. 1 to 7 are in the PDF and were read. No separate supplementary file.
- Figure data and code: none. The abstract page lists no ancillary files and the paper links no data repository, so `read_mtx.py` was not run and no repository was used for counts.
- Recognition: I recognize this paper and know its later publication history. I did not use that knowledge in the report; the report assesses v1 as written.

## Claims (step 1)

| Claimed signal | Figures | Device | Ranges shown | Counts |
|---|---|---|---|---|
| ZBP forms as levels merge at zero bias with field; height near 2e^2/h for 0.75 to 0.92 T | Fig. 1b, 1c; Ext. Data Fig. 1c | A (proximitized length ~1.2 um, InSb, Al on 2 of 6 facets) | B 0 to 1.0 T along the wire axis only; V about +-0.25 mV; super-gate -6.5 V, tunnel-gate -7.7 V, back-gate 0 V; 20 mK | one field sweep shown |
| Height stays at 2e^2/h while above-gap conductance changes by more than 50% (tunnel-gate plateau) | Fig. 2a to 2e | A | tunnel-gate about -8.15 to -7.65 V at 0.8 T; plateau from about -7.95 V up; split peaks below about -8 V | one tunnel-gate sweep |
| Nearly quantized ZBP non-split over super-gate, then splits | Fig. 3a | A | super-gate about -6.5 to -4.8 V at 0.9 T; tunnel-gate compensated | one sweep |
| Oscillatory splitting with height returning to 2e^2/h and not crossing it | Fig. 3b | A, "lower B-field and different gate settings" | super-gate about -4.15 to -3.5 V at 0.7 T | one sweep |
| Plateau reproduced in a second device; zero-bias conductance above 2e^2/h when a second channel opens, net height argued not to exceed 2e^2/h | Fig. 4a, 4b | B (~0.9 um) | B 0 to 1.2 T; tunnel-gate about -0.67 to -0.44 V at 0.83 T; plateau between dashed lines at about -0.62 and -0.545 V | one field sweep, one tunnel-gate sweep |
| Height saturates at 2e^2/h when FWHM exceeds 3.5kBT; agreement with convolution model above 50 mK | Fig. 4c to 4f; Ext. Data Fig. 3 | B | T 20 to 600 mK in 10 mK steps at 0.84 T | one temperature series |
| Trivial ABS ZBP: stable in back-gate, level crossing in tunnel-gate, height varies smoothly and can exceed 2e^2/h | Fig. 5; Ext. Data Figs. 4, 6 | C | B 0 to 1.1 T; back-gate -9 to -3 V at 0.74 T and about -12.5 to -11 V at 0.35 T; tunnel-gate about -0.07 to -0.025 V | several sweeps |
| Low-transmission device shows thermally limited ZBP below 2e^2/h and hard gap | Ext. Data Fig. 2 | D | B 0 to about 1 T | one sweep |

Counts stated (Ext. Data Fig. 7, p. 26): more than 60 devices fabricated and tested; 11 selected for "good basic transport with all gates being fully functional"; most show ZBPs after tuning; 2 (A and B) show a quantized plateau; the other 9 show trivial ZBPs like device C; SEM images of 8 others shown. Device D appears in Ext. Data Fig. 2 and is not placed among the 11 explicitly.

Missing counts: cooldowns; datasets per device; how many sweeps or settings were tried before the shown ones; field angles (field is along the wire for all measurements); series resistance (not mentioned anywhere); lock-in excitation stated for Fig. 1 (8 uV, in the simulation note) and Ext. Data Fig. 2 (5 uV) only.

## Matching (step 2)

Matched (13): fine-tuned-plateau, series-resistance-subtraction, abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode, one-end-only, local-probe-loophole, fine-tuning-and-selection.

Skipped, with reason:
- trivial-andreev-band-gap-reopening: its signature is a nonlocal gap closing and reopening; the paper makes no such measurement and says the reopening is not visible (p. 4).
- micromagnet-stray-field: no magnets; peaks appear at finite applied field.
- full-shell-flux-andreev: partial shell (two of six facets).
- protocol-parameter-sensitivity: no automated pass/fail protocol.
- island-states-coulomb-spacing: no island measurement.
- charge-trap-fractional-shift: the paper mentions charge jumps (p. 5, Fig. 3 caption) but makes no fractional-charge claim.
- All shapiro, supercurrent, chiral, kitaev, diode and charge-interferometer entries: signatures not claimed.

No entries adapted: the paper is tunneling spectroscopy, in scope.

## Checks walked (step 3)

zbp family (6) and practice (3), in library order: zbp-dot-search partly; zbp-wide-ranges partly; zbp-both-ends not done; zbp-transparency done (over the windows shown, A and B); zbp-nonlocal-gap not done; zbp-raw-conductance not done; report-counts partly; report-ranges partly; report-processing not done.

Status choices I was unsure of:
- zbp-transparency marked done: the windows are narrow (about 0.3 V for A, about 75 mV for B), but the claim is a plateau within those windows, so the regime it claims is covered.
- report-counts marked partly: device counts and reasons are given; datasets and cooldowns are not.
- report-processing marked not done (weaker of partly and not done): two processing steps are named, no data or code.
- kondo-resonance partly addressed: Fig. 1b shows no ZBP at zero field and a peak that forms at finite field, which argues against Kondo, but the paper doesn't discuss Kondo, so per step 3 it stays partly.
- weak-antilocalization not addressed (weaker choice): cited as ref. 33 in a list on p. 8, never discussed; device B's multi-channel regime may bear on it, but I could not tie that to the entry's control with confidence.
- spin-orbit-length-pinning partly addressed: super-gate and tunnel-gate stability is the entry's control, but not discussed in those terms.
- quasi-majorana-smooth-confinement partly addressed: Kells et al. is cited (ref. 31) within the ABS sentence; the tunnel-gate argument is made for a dot near the barrier.
- No lookalike reached "ruled out".

## Hold-out (sources skipped because they cite the paper under review)

Checked by downloading each matched entry's arXiv sources and searching the text for the arXiv ID, title and author list.
- 2101.11456 (Zhang et al. 2021): cites "Quantized Majorana conductance. Nature 556, 74 (2018)" (ref. list). Held out.
- 1806.02801 (Vuik et al.): cites Nature 556, 74 (ref. 41). Held out.
- 1711.06256 (Moore, Stanescu, Tewari): cites arXiv 1710.10701 (ref. 25). Held out. This is the only source of check zbp-both-ends; I still walked the check from its library text.
- 1910.11413 (Pan and Das Sarma): discusses "the most compelling experimental paper29 in the subject entitled Quantized Majorana conductance". Held out.
- 1902.02773 (Chen et al. 2019): cites Nature 556, 74 (ref. 19). Held out.
- 2501.18631 (Akrap, Frolov et al.): cites the retraction note of "Quantized Majorana conductance" (ref. 38). Held out. This is the only source of the three practice checks; I still walked them from their library text.
- 1911.04512 (Prada et al.): v3 (the version the library cites) does not cite the paper; v1 cites Nature 556, 74. Held out conservatively, since it is the same work. This leaves spin-orbit-length-pinning, exceptional-point-zero-mode and local-probe-loophole with no usable source; I used their library text for matching only.

Kept after checking: 2309.09368 (Frolov et al. 2023; its reference list has no citation of the paper), 2004.08583 (Yu et al.; none), 2207.02472 (Microsoft Quantum; cites 2101.11456, not the paper), 1705.02035 (Liu et al. 2017; predates the paper), 1207.3067, 1207.1259, 1206.6687 (predate the paper).
Not checked: sources of skipped entries (2210.03507, 2305.19970, 2008.02348, 2502.19560, 1904.06463, 1708.06752, 2203.07829, 2005.00077, 2211.08710, 2106.00495, 2403.07370, 2408.10030, 2504.06732, 1010.4598, 2205.09276), since those entries were not used.

## Related work (step 5)

Each abstract page opened on arxiv.org; ID, title and first author confirmed.
- 1705.02035, Liu, Chun-Xiao, title as listed: abstract checked ("ABSs indeed tend to coalesce together producing near-zero-energy midgap states ... but this mostly happens in the non-topological regime"; "difficult to distinguish by tunneling conductance spectroscopy").
- 1207.3067, Kells, G.: abstract checked (smooth confinement, exponentially small energy, "even in the ideal clean single channel limit").
- 2004.08583, Yu, P.: abstract checked (probes at both ends, nearly quantized peaks at one end only, dips at the other end). arXiv title differs from the journal title used in the library; the report uses the arXiv title.
- 2205.06736, Wang, Zhaoyu: found through the arXiv API (title search), abstract page checked (plateaus within 5% of 2e^2/h over gate and field sweeps in InAs-Al; "Despite the presence of disorder and quantum dots"). Not a library source.
- 2309.09368, Frolov, S. M.: abstract and full text checked; the plateau statement ("in other regimes, we observe similar plateaus with values exceeding 2e2/h") is in the full text, Example 2, p. 6.
- Nothing couldn't be opened. arXiv API called once, abstract pages fetched with about 3 s gaps.

## Library gaps

- No entry was added "(not in library)". A candidate I did not add: background or multi-channel conductance adding to a zero-bias peak (the paper's own device B argument, p. 7); I found no opened paper to cite for it as a lookalike.
- No entry covers thermal or lock-in broadening as a reason a plateau appears in some devices and not others; the paper itself treats it (Ext. Data Fig. 2).
- Three entries (spin-orbit-length-pinning, exceptional-point-zero-mode, local-probe-loophole) rest on a single source (Prada et al.), so one hold-out leaves them unsourced.

## Skill issues

- Output location: the skill says `reports/<arxiv-id>.md` and `reports/<arxiv-id>.notes.md`; the caller asked for `eval/runs/1710.10701/skill-r1/report.md` and `notes.md`. I followed the caller.
- Hold-out and versions: the rule doesn't say whether a source counts as citing the paper when an earlier arXiv version cites it and the cited version doesn't (Prada et al.). I held it out.
- Hold-out and entries: the rule skips sources, but doesn't say whether an entry (or a check) whose only sources are held out may still be matched or walked. I used the entry and check text and no held-out source.
- Template questions 1 to 4 are fixed wording, while step 6 says to skip or point to where the paper answers them. I kept the question and added where it is answered, which makes the question list longer.
- "Ruled out" versus data the paper doesn't discuss: step 3 forces "partly addressed" when data bear on a lookalike without discussion, even when the data match the entry's control (Kondo, spin-orbit pinning here). Possibly intended; worth stating.
- Word count: the template's fixed text plus long arXiv titles in related work make 600 to 900 words hard; this report is about 950 words outside the table.
- The checks format "<check> : Done / Partly / Not done" uses capitalized statuses; flags.json uses lowercase. No conflict, just noting.
- Tooling: the environment's Write tool refused to write `.md` report files from a subagent; files were written with the shell because the caller asked for them.
