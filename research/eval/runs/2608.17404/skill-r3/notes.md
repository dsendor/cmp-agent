# Run notes: arXiv 2608.17404v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes, checks for the zbp, shapiro, kitaev, charge and practice families.
- Skill and template: cmp-assistant/skill/SKILL.md and skill/report-template.md, read once at the start.
- Date of run: 2026-10-23.

## What I read
- The abstract page from the local copy (abs.html). Title: "Flux-tunable global and local superconductivity in a topological insulator nano-SQUID". First author: Nikodem. Dated 2026-08-18, v1.
- The full text: the local paper.txt, plus a per-page pdftotext of paper.pdf (16 pages) to fix page numbers. The supplement is in the PDF on pages 10 to 16, and I cite those pages by PDF page number (the supplement numbers its own pages 1 to 7).
- PDF pages 2 and 3 rendered as images, to read field and bias ranges.
- I did not fetch the paper itself, per the run instructions.
- Data repository: Zenodo 10.5281/zenodo.21988906 (p. 7). I did not open it, because the run instructions allowed only arxiv.org, export.arxiv.org and api.openalex.org. Counts below come from the paper alone.
- No ancillary figure data, so read_mtx.py was not used.
- I didn't recognize the paper (it postdates my training data). I noticed author overlap: H. F. Legg wrote the library's protocol-sensitivity source (2502.19560) and co-wrote Hess et al. (2210.03507). This doesn't trigger the hold-out rule, which is about sources that discuss this paper.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Ic oscillates with h/2e period, near-full revival at integer flux, surface-state dominated | Fig. 1e (A), 3a (B), S2a (C) | A, B, C | A: Bx about -6 to 6 T (Φ about -2 to 2 Φ0). B: Bx -4 to 4 T (Φ -4 to 4). C: Bx about 0 to 4 T. |
| Diode efficiency about 20% with sign reversal at half-integer flux, read as the 0-π ground-state jump that marks the topological transition | Fig. 1e, 3a, S2a, S4 | A, B, C | S4: VG about -75 to 25 V and Bx 0 to 4 T for B and C. "largely robust against gate voltage" (p. 4). |
| Spectral jumps in local conductance at the predicted transitions. Device A: a ZBP appears in the predicted window and persists over a wide Bx range, then splits at 2 flux quanta | Fig. 1f-g, S1 (A); 3b-c (B); S2b-c (C) | A (one TJ), B, C (two TJs) | Vb ±1 mV. Device A at VG = -10 (or 0), 10, 20 V; gate limited by a leaky dielectric (p. 12). Device C: ZBP "mostly absent" (p. 13). |
| Nonlocal conductance jumps that align with Ic features, plus extra jumps at high field | Fig. 3d-e, S2d-e, S5 | B, C | S5: VG -40 to 40 V. Circuit correction from line resistances (p. 11). |
| ZBPs appear in both predicted regimes and at zero field. End-to-end correlation shows no clear topological/trivial distinction. Attributed partly to disorder | Fig. 4, S3 | B, C | B: Bx = 0, 1, 2 T; VG -30 to 30 V; Vb ±500 µV. C: Bx = 0, 2.5, 4 T. Fraction plots against Bx from 0 to 4 T. |
| Overall reading: a bulk topological state "is successfully realised" (p. 5) | All | | |

**Counts.**
- Named devices: 3 (A with one functional tunnel junction; B and C with two).
- Number of devices fabricated or examined: not stated ("all examined devices", p. 4; "a series of devices", p. 4).
- Tunnel-junction yield "below 50%" (p. 5).
- Cooldowns: not stated.
- Temperature: base, about 30 mK, only.
- Field direction: axial Bx, with Bz compensation (pp. 6, 10).
- Device lengths 1.3 to 2.5 µm (Table S1, p. 10).

## Matching (step 2)
- Families matched: zbp (local peaks), nonlocal (nonlocal jumps), diode (sign reversal of the diode effect), and practice.
- Included (15 library entries plus 1 outside): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, exceptional-point-zero-mode, one-end-only, local-probe-loophole, full-shell-flux-andreev, trivial-andreev-band-gap-reopening, transparent-junction-pi-crossing, diode-vortex-screening, protocol-parameter-sensitivity, fine-tuning-and-selection, and the outside entry "trivial supercurrent-interferometer diode".
- Adapted entries:
  - diode-vortex-screening: its signature reads the diode effect as exotic pairing; here the diode is read as a topological transition.
  - full-shell-flux-andreev: the device is a Nb sandwich with flux through the TI core, close to the full-shell flux physics but not a full shell.
  - transparent-junction-pi-crossing: a shapiro-family entry applied to a phase-biased junction whose spectrum and peaks are read at phase π.
  - protocol-parameter-sensitivity: applied to the third-derivative end-to-end correlation classifier in Fig. 4l, which is not a pass/fail protocol.
- Skipped entries, with reasons:
  - fine-tuned-plateau and series-resistance-subtraction: no claim of quantized conductance.
  - micromagnet-stray-field: no magnets in the device.
  - chiral-plateau-superconductor-short: not a quantum anomalous Hall device.
  - island-states-coulomb-spacing: not a Coulomb island.
  - shapiro-landau-zener, shapiro-nonlinear-resistance and switching-jump-blind-region: no microwave data.
  - field-enhanced-supercurrent-resonances: Ic revives at integer flux and is read as interference, not as triplet pairing.
  - charge-trap-fractional-shift and coulomb-dominated-interferometer: no fractional-charge claim.
  - false-poor-mans-majorana: not a dot chain.
  - spin-orbit-length-pinning: the mechanism is derived for a Rashba normal section, and the TI surface spectrum differs.

## Checks walked (step 3)
- zbp family, 6 checks: zbp-dot-search not done; zbp-wide-ranges partly; zbp-both-ends partly; zbp-transparency not done; zbp-nonlocal-gap partly; zbp-raw-conductance partly.
- practice family, 3 checks: report-counts, report-ranges and report-processing, all partly.
- zbp-both-ends: I marked it partly because device A has a single probe, although B and C are fully done.
- The diode and nonlocal signals have no check list in the library.

## Sources held out
- None. I checked the two library sources revised in 2026:
  - Legg 2502.19560v2 (updated 2026-10-21, after this paper): I downloaded the PDF and grepped it for "2608", "Nikodem", "nano-SQUID", "SQUID" and "topological insulator". No hits.
  - Akrap et al. 2501.18631v2 (updated 2026-03-25): this predates the paper, so it can't cite it.
- Frolov et al. is quoted from the 2023 preprint.

## Related work: how each link was checked
- 2205.04469 (Souto, Leijnse, Schrade): API abstract, plus the full text v1, where I confirmed the efficiency of about 40%, the condition Φ ≠ nΦ0/2 and the need for unequal transmissions (p. 2).
- 1906.01179 (Dartiailh et al.): API abstract (title, first author, π jump with Ic minimum).
- 2008.02348 (Valentini et al.): API abstract.
- 2210.03507 (Hess et al.): API abstract.
- 1902.02773 (Chen et al.): API abstract.
- API calls were spaced about 3 seconds apart or more. Nothing was rate-limited.

## Library gaps
- Trivial supercurrent-interferometer diode effect (source: 2205.04469). Flux-threaded two-junction loops with skewed current-phase relations give a diode whose sign changes at multiples of Φ0/2 without topology. The library has no entry for SQUID-type global signatures read as a topological transition.
- No check list for the diode, nonlocal or supercurrent families, and none for phase-driven (flux or phase-bias) transitions.
- No entry for a 0-π ground-state phase jump in an interferometer read as a topological transition. Dartiailh et al. (1906.01179) is a positive example of that signature; the library has no trivial counterpart beyond the diode gap above.
- No entry on vortex entry and flux trapping in the leads producing spectral jumps at high field. The paper raises this itself (p. 4); I didn't find a source in this run.

## Unsure
- How to grade lookalikes when the paper itself argues the ZBPs are not Majorana evidence. I graded what the paper shows about each one; several become "partly addressed" because the paper names disorder as the likely origin.
- Whether to grade the outside diode entry as not addressed or partly addressed. Fig. S4 shows the diode against gate voltage, but nothing that separates a trivial interferometer from the topological model, so I picked the weaker status.
- Kondo and abs-quantum-dot share one quote (Fig. 4a-b), which is the only data that bear on both.
- The Fig. S1 caption lists VG = -10, 0, 20 V while the panel labels read 0, 10, 20 V. I used the caption range.

## Skill issues
- Step 3 says to walk "the checks for the paper's family", but a paper can span several families (here zbp, nonlocal and diode), and some families have no checks. The skill doesn't say what to do then. I walked zbp and practice only.
- Step 2 and the status rules don't say how to treat a paper that reports a signature and then argues against reading it as topological. The status definitions assume the paper wants the lookalike excluded.
- "Skip entries that can't apply" leaves a judgment call for entries that could apply only weakly (exceptional point, weak antilocalization). I included them, which makes the table long.
- Step 7 says to write reports/<id>.md. This run's instructions overrode that, so the report goes in the final reply.
- The data-repository rule ("if you can reach it") conflicts with run-level domain limits. The skill could say to note the conflict and skip.
- The template's 600 to 900 word target is hard to meet with 16 table rows plus 9 checks. The checks section is outside the table and adds about 250 words.
