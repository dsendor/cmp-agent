# Run notes: arXiv 2609.38003v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalike entries, checks for families zbp, shapiro, kitaev, charge, practice.
- Date of run: 2026-10-23. Output label: AI only.

## What I read
- Skill: skill/SKILL.md; template: skill/report-template.md; library in full, including `checks`.
- Paper: the extracted text supplied for the test (paper.txt, 14 pages incl. Methods and Extended Data Figs. 1 to 5) and the supplied abstract page (abs.html): title "Reversible field-free superconducting diode effect controlled by an antiferromagnet", v1, submitted 29 Sep 2026, "14 pages, 4+5 figures". No PDF; figure details taken from captions and text. Page numbers come from the page markers in the extracted text.
- I did not fetch the paper itself (per the test instructions). No supplementary material beyond Extended Data in the text. No data repository or ancillary files are linked, so no counts from data, and read_mtx.py was not used.
- Did not read any other file in cmp-assistant/.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Field-free SDE after zero-field cooling, η about 7% | Fig. 3a (I-V, switching distributions) | 5 µm x 180 µm CuMnAs(12.4 nm)/AlAs(2.0 nm)/Al(9.2 nm) bar along [010], four-terminal, 20 mK | 50 sweeps per polarity for the distribution; number of cooldowns not stated; ZFC sign reproducibility not stated |
| Preparation field reverses diode polarity along [100] | Fig. 3b,c,d | same [010] bar | prep along [100] to ±1 T; η up to about ±20%; 8 sweeps averaged per point |
| Weak, non-reversing response along [010] | Fig. 3e | same bar | prep along [010] to ±4 T |
| Same axis dependence in orthogonal bar | Extended Data Fig. 4 | bar along [100] (size not stated; same chip and cooldown not stated) | prep [100] to ±1 T, [010] to ±4 T |
| Néel-state anisotropy and remanence in CuMnAs | Fig. 4a,b,c | separate reference bar, 20 µm x 10 µm, from a CuMnAs wafer with 3 nm oxidized Al cap (no AlAs/Al superconductor), 5 K, ±4 mA, vector-magnet cryostat | sweeps along [100] about ±4 T (axis), [010] narrower axis; remanent prep −5 to 5 T |
| Uniaxial easy axis along [100] | Extended Data Fig. 5 | 10 µm x 10 µm region of the CuMnAs epilayer, about 100 K | one region shown |
| Vanishing net moment | Fig. 2b | 3 mm x 5 mm piece; series of samples across the 2" wafer | bound 3e-3 µB/Mn; temperature of the SQUID measurement not stated |
| Proximity tuning via AlAs thickness | Fig. 2c, Extended Data Fig. 3 | 2.0 nm (Tc about 350 mK) and 1.5 nm (no transition to 20 mK) samples | one sample each |

Missing counts: devices fabricated, devices measured, devices showing the effect, cooldowns, how many field-preparation runs, temperature dependence of η, any applied-field (non-remanent) η data near zero.

## Matching (step 2)
- Family: diode. Matched `diode-vortex-screening` (adapted: library signature reads the diode as exotic pairing; this paper reads it as antiferromagnetic control of a conventional superconductor). Always included `fine-tuning-and-selection` (adapted to bars and cooldowns).
- Skipped, cannot apply to a superconducting film bar with no tunneling probe or junction: all zbp entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode), quantization (fine-tuned-plateau, series-resistance-subtraction), nonlocal (one-end-only, trivial-andreev-band-gap-reopening), island, shapiro (all four), supercurrent (field-enhanced-supercurrent-resonances: Josephson-junction finite-bias resonances, signature is supercurrent growing with field), charge (both), chiral, kitaev, local-probe-loophole (Majorana-specific).
- micromagnet-stray-field: stray-field physics is relevant but the entry's signature and mechanism are zero-bias peaks from Andreev states in dots, so I skipped it and used an outside stray-field row with a diode-specific source.
- protocol-parameter-sensitivity: skipped, no automated pass/fail protocol in the paper.
- Scope sentence added under "What this is" (adaptation of the diode entry).

## Checks (step 3)
- No `checks` exist for family `diode`, so only the three `practice` checks were walked: report-counts partly, report-ranges partly, report-processing partly.

## Hold-out
- No library source cites the paper under review (title, authors or arXiv ID); grep of the library for 2609.38003, Krizek and CuMnAs returned nothing, and all diode-relevant sources predate the paper. No sources skipped.
- I did not recognize the paper; no later history used.

## Related work, how each was checked
- 2205.09276 (Hou et al.): arXiv API abstract; ID, title, first author confirmed; also library source and the paper's ref. 28.
- 2512.05427 (Jiang et al.): arXiv API abstract and full text (PDF, pdftotext). Confirmed poling-field sign control, trapped-flux attribution, and the magnet stray-field calibration with graphene ("Such hysteresis can often arise from a stray magnetic field due to the superconducting magnet. To rule out this possibility, we measured the resistance of few-layer graphene simultaneously during all measurements."). The paper's ref. 29 is the published version.
- 2205.12196 (Golod and Krasnov): arXiv API abstract; PDF downloaded and grepped for trapping/removing.
- 2506.17651 (Li et al.): arXiv API abstract; the paper's ref. 30 is the published version.
- 2601.03366 (Sachin et al.): arXiv API abstract; the paper's ref. 10.
- All five predate the paper under review. I avoided 2610.* hits (NbN/FePt, Mo2N/FePt) since they postdate it and I did not check whether they discuss it.

## Library gaps
- No `checks` for the diode family. Candidate steps: thermal cycle above Tc at zero field after preparation (trapped flux); residual-field calibration of the magnet after excursions; η versus small out-of-plane field near zero; plain-superconductor control bar; rotation of the chip relative to magnet axes; temperature dependence of η.
- Missing diode lookalikes, each now cited from a paper I opened: trapped flux written by a poling field (2512.05427, also 2205.12196); superconducting-magnet remanent field (2512.05427); stray fields from magnetic layers driving vortex entry (2506.17651).
- The diode family signature "taken as exotic pairing" is narrower than current diode claims (magnetic-order control without exotic pairing).

## Unsure
- Whether the two bars were on the same chip and mount; the paper doesn't say. My question 7 depends on it.
- Fig. 4b field range read from garbled axis labels; I did not quote it.
- Whether the dilution-fridge magnet is a vector magnet or the sample was remounted for [100] versus [010]; Methods name a vector magnet only for the 5 K setup.
- Status choice: all five rows "partly addressed"; for the magnet remanent field I picked partly addressed because the Fig. 3e data bear on it without discussion.

## Skill issues
- Step 3 assumes a `checks` section for the paper's family; for diode there is none, and the skill doesn't say what to do (I used only practice checks and said so in the report).
- The "(not in library)" marker: the skill says to put it in the table; flags.json wants "outside: <name>". I used both.
- "Scope" covers different measurement types; it is unclear whether a family in the library whose signature wording differs from the paper's claim (exotic pairing versus magnetic control) counts as adaptation. I treated it as adaptation.
- Step 7 says write files under reports/; this run returned them inline per the test instructions.
- Hold-out check for library sources requires knowing whether each source cites the paper; the skill gives no method for sources I don't open. I relied on dates and a grep.
