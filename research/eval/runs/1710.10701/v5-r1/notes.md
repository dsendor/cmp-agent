# Run notes: 1710.10701v1 (lookalike assistant, v5-r1)

## Setup
- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 entries; checks for zbp, shapiro, kitaev, charge, practice).
- Skill and template read once at the start: cmp-assistant/skill/SKILL.md, skill/report-template.md. scripts/read_mtx.py not used (no ancillary figure data).
- Paper: local files only, as instructed (paper.pdf, paper.txt, abs.html). Did not fetch the paper. Version v1 (only version on the abstract page, 29 Oct 2017). Title from abs.html: "Quantized Majorana conductance".
- Read: full extracted text (main text, Methods, Extended Data captions); rendered PDF pages 12 to 16 (Figs. 1 to 5) and 19, 20, 22, 25, 26 (Ext. Data Figs. 1, 2, 4, 6, 7) to read axis ranges. Pages 21, 23, 24 (Ext. Data Figs. 3 and 5, simulations) read from captions only.
- No data repository is linked; none used.
- Page numbers are the PDF page numbers printed at the foot of each page (p. 1 title, p. 2 abstract, pp. 12 to 16 figure captions, pp. 18 to 26 Extended Data).
- I recognized this paper (published in Nature 2018 and later retracted, with a reanalysis on arXiv). That knowledge was not used in the report; the paper was assessed as written.
- Process slip: while counting library entries I ran an `ls` that printed the folder names under cmp-assistant/eval/runs (three arXiv IDs). I opened no files there and nothing from it was used.

## Claims table (step 1)
| Claim | Figures | Device | Ranges shown |
|---|---|---|---|
| ZBP height reaches 2e²/h and stays near it in field | Fig. 1b, 1c; Ext. Data Fig. 1c | A (proximitized ~1.2 µm) | B 0 to 1 T along wire axis, plateau 0.75 to 0.92 T; SG -6.5 V, TG -7.7 V, BG 0 V; 20 mK |
| Plateau against tunnel gate (transmission) | Fig. 2a to 2e | A | B = 0.8 T; TG about -8.15 to -7.65 V; GN about 0.35 to 0.55 × 2e²/h; splitting below about -8 V |
| Stability and splitting against super-gate | Fig. 3a, 3b | A | 0.9 T, SG about -6.5 to -4.7 V (tunnel gate compensated); 0.7 T, SG about -4.1 to -3.5 V, "different gate settings" |
| Reproduction in a second device | Fig. 4a, 4b | B (~0.9 µm) | B 0 to 1.2 T; TG about -0.67 to -0.44 V at 0.83 T, plateau about -0.61 to -0.55 V; zero-bias G above 2e²/h when GN > e²/h, attributed to background |
| Temperature dependence | Fig. 4c to 4f; Ext. Data Fig. 3 | B | 20 to 600 mK in 10 mK steps at 0.84 T |
| Trivial ABS comparison | Fig. 5; Ext. Data Figs. 4, 6 | C | B 0 to 1 T; BG -9 to -3 V (0.74 T), about -12.5 to -11 V (0.35 T); TG about -0.07 to -0.02 V; Ext. Data Fig. 6 BG -5.6, -7.5, -11.1 V |
| Thermally limited ZBP at low transmission | Ext. Data Fig. 2 | D | B 0 to 1.5 T |
| Counts | Ext. Data Fig. 7 (p. 26) | all | >60 fabricated and tested; 11 "selected" with working gates and measured extensively; most show ZBPs after tuning; 2 (A, B) show a plateau; 8 others shown as SEM only |
Missing counts: cooldowns, datasets per device, number of gate settings explored, how the plateau settings were found, back-gate and field-angle ranges for A and B, any series resistance or line resistance. Lock-in excitation 8 µV (Fig. 1 caption).

## Entries matched and skipped (step 2)
Matched (13): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, spin-orbit-length-pinning, exceptional-point-zero-mode, local-probe-loophole, fine-tuning-and-selection.
Skipped:
- trivial-andreev-band-gap-reopening: the paper claims no gap closing and reopening (it says reopening is not visible) and has no nonlocal data.
- micromagnet-stray-field: no magnets; peaks at finite applied field.
- full-shell-flux-andreev: partial shell (two of six facets).
- protocol-parameter-sensitivity: no automated pass/fail protocol.
- island-states-coulomb-spacing: no island or Coulomb blockade spectroscopy.
- chiral-plateau-superconductor-short, coulomb-dominated-interferometer, charge-trap-fractional-shift: different systems or signals (the trapped-charge switches in Figs. 2 and 3 are not offered as a signal).
- shapiro-landau-zener, shapiro-nonlinear-resistance, transparent-junction-pi-crossing, switching-jump-blind-region, field-enhanced-supercurrent-resonances, diode-vortex-screening: no Josephson junction measurements.
- false-poor-mans-majorana: no Kitaev chain.
No entries adapted. Checks walked: zbp (6) and practice (3).

## Judgement calls
- Weak antilocalization set to "Ruled out for the claim": Pikulin et al. (full text, Discussion) list raising the tunnel barrier as a test that suppresses the antilocalization peak but not the Majorana resonance; the paper shows the height constant while GN changes >50% in A and over the plateau in B, and cites Pikulin (ref. 33) among non-topological origins it argues against. Pikulin caveat (thermal narrowing) does not apply since the height stays at 2e²/h.
- Spin-orbit-length pinning set to "Ruled out for the claim": its one test (pinning against parameters other than field) is shown for A and B; the paper concludes against local ABS origins via the tunnel-gate argument. The tunnel gate tunes the normal segment, which is the parameter the length condition depends on.
- Kondo kept at "Tested in part" even though the zero-field test (no peak at 0 T, peak forms at finite field) is shown for A and B: the paper never names Kondo or concludes against it specifically (Lee et al. 2012 is cited only within the ABS list). Unsure; it could be argued as ruled out.
- abs-quantum-dot dot-search test marked "part": tunnel-gate maps of A and B near zero bias count in part; no zero-field or above-gap dot search for A or B (only for C, Ext. Data Fig. 4b). Fig. 3b shows split-and-rejoin behaviour the authors read as Majorana overlap.
- zbp-dot-search check marked "Partly" for the same reason, though the "partly" definition is about evidence subsets (see skill issues).
- disorder-induced-zbp gate test "part": tunnel gate shown for A and B; back gate held at 0 V in A and not stated for B.
- fine-tuned-plateau "peak heights from other regimes and devices" marked "all" (Fig. 3b, Fig. 4b open regime, devices C and D, Ext. Data Fig. 6 heights above 2e²/h in C).
- Series resistance: "not mentioned" chosen over "data bear on it"; Ext. Data Fig. 4e (GS versus GN fit) could constrain it, but only for device C.
- Report-counts "Partly": devices counted with reasons; datasets and cooldowns not.
- Report runs to about 920 words outside the table (target 600 to 900), mostly from nine checks and eight questions.

## Sources held out (hold-out rule)
Checked by downloading each source's current arXiv PDF and searching for the title, arXiv ID 1710.10701 and "Nature 556, 74":
- Held out (cite or discuss the paper): 2101.11456 (Zhang et al. 2021, replaces the paper), 1711.06256 (Moore et al.; cites arXiv 1710.10701), 1806.02801 (Vuik et al.; cites Nature 556, 74), 1910.11413 (Pan and Das Sarma; discusses it at length), 1902.02773 (Chen et al.; cites it), 2501.18631 (Akrap, Frolov et al.; cites the retraction note).
- Kept (no citation found): 2309.09368 (Frolov et al.; Example 2 is their own InAs-Al device), 1911.04512 v3 (Prada et al.; earlier versions not checked), 2207.02472 (Microsoft; cites the replacement 2101.11456 only), 2004.08583 (Yu et al.).
- Predate the paper, so cannot cite it: 1705.02035, 1207.3067, 1207.1259, 1206.6687.
- Not checked (sources of skipped entries only): 2210.03507, 2502.19560, 2008.02348, and the rest.
Effect: the library entries still apply; held-out sources were not quoted and not used as related work. The zbp-both-ends check's only source (Moore) is held out; the check was still used.

## Related work checks
- 2004.08583 Yu et al.: abstract page opened (ID, title, first author P. Yu confirmed); abstract and full text read (PDF downloaded for the hold-out check).
- 1705.02035 Liu et al.: abstract page opened and confirmed; abstract read.
- 1207.3067 Kells et al.: abstract page opened and confirmed; abstract read.
- 1206.6687 Pikulin et al.: abstract page opened and confirmed; full text read (Discussion, barrier test).
- 2205.06736 Wang et al.: found through the arXiv API title search; abstract page opened and confirmed (first author Zhaoyu Wang); abstract read. It's not a library source, so the hold-out rule does not apply; listed for its own results only.
- 2207.02472 abstract opened but not listed.

## Library gaps
- No entry or check covers subtracting an assumed second-channel background from the zero-bias conductance (Fig. 4b). The series-resistance entry does not cover it. No outside row added since I did not open a paper showing it as a lookalike.
- The quantization family has no `checks` section; the zbp checks were used (their signal text includes peaks near 2e²/h).
- Field-angle dependence is not a listed test in any zbp entry, though Pikulin et al. and Yu et al. use it.
- Field-induced (singlet-triplet) Kondo at finite field is not in the kondo-resonance entry; it would change how the zero-field test is read.

## Skill issues
- "Partly" for checks is defined by evidence subsets ("one of the three devices"); there is no rule for a check done incompletely on all the evidence (zbp-dot-search, zbp-wide-ranges here).
- "The paper concludes against the lookalike" is unclear when the paper cites the lookalike's source in a generic list and argues against "non-Majorana origins" as a group (Kondo vs weak antilocalization here).
- The hold-out rule says "cites it by title, authors or arXiv ID"; unclear whether a source citing a later reanalysis of the same data (2207.02472 citing 2101.11456) counts. I kept it.
- The hold-out rule covers library sources only; it is unclear whether related work found by search that cites the paper (Wang et al. 2022 likely does) should also be avoided.
- The step 3 rule that selection gaps count only under fine-tuning-and-selection overlaps with fine-tuned-plateau, whose own tests are selection tests ("How the plateau was found").
- Step 7 says to write reports/<id>.md and notes; this run delivered them inline per the run prompt.
- The 600 to 900 word target is tight with nine checks and eight questions.
