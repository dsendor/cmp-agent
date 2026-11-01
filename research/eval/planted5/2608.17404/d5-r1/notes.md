# Run notes: arXiv 2608.17404v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (27 lookalike entries). Skill and template read once at start.
- Input: extracted text only (paper.txt, main text pp. 1-9 and Supplement pp. 1-7). No PDF, no abstract page; per the task I did not fetch the paper. Title taken from the text header ("Flux-tunable global and local superconductivity in a topological insulator nano-SQUID"), shortened in the report heading. Figure details from captions only; axis labels in the extraction lose minus signs.
- Data repository (Zenodo 10.5281/zenodo.21988906): not opened. The task limited fetches to arxiv.org, export.arxiv.org and api.openalex.org, so device counts come from the text only.
- Recognition: I did not recognize this paper or know any later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| h/2e Ic oscillations with near-full revival, read as surface-dominated transport and a ground-state phase jump | Fig. 1e (A), 3a (B), S2a (C) | A, B, C | Bx about -4 to 4 T for B, C (axis labels); A range not readable; T base about 30 mK, no temperature series |
| Diode efficiency (about 20% in A) reversing sign at half-integer flux, read as the trivial-to-topological transition | Fig. 1e, 3a, S2a, S4 | A, B, C; gate maps for B, C only | S4: VG about -75 to 25 V, Bx 0 to 4 T; current "always ramped up from zero" |
| Local spectral jumps and a ZBP in A appearing in the predicted topological window, persisting over a large Bx range | Fig. 1f-g; S1 | A (single probe) | VG = 10 V main; S1 at VG = -10, 0, 20 V, Bx about -6 to 6 T; A gate range limited by leaky dielectric |
| Local and nonlocal spectral jumps aligned with Ic anomalies | Fig. 3b-e, S2b-e, S5 | B, C | Nonlocal Bx 0 to 4 T; S5 VG -40 to 40 V, field not stated |
| ZBPs in both topological and trivial windows, including Bx = 0; end-to-end correlation shows no clear relation to the bulk phase; some ZBPs attributed to disorder | Fig. 4, S3 | B (Bx = 0, 1, 2 T), C (0, 2.5, 4 T) | VG -30 to 30 V; correlation fractions vs Bx 0 to 4 T |
| Device counts | Methods, S1.E | 3 shown (A, B, C) | Devices fabricated: missing. Devices examined: missing ("all examined devices"). TJ yield "below 50%". Cooldowns: missing. Dimensions in Table S1 (L = 1.3 to 2.5 um, W = 70 to 80 nm, d = 16 to 36 nm) |

Possible internal inconsistencies noted: (a) Supplement Section C "Effects of measurement circuit" is a heading with no text, though the main text and Supp. Ref. [2] (Martinez et al.) point to circuit effects; (b) tunnel resistances "typically exceeding 100 kΩ" versus G of order 1 e^2/h in A and C; (c) device C "zero-bias conductance peak was mostly absent" versus "strong increase of correlated zero-bias conductance peaks" in Fig. S3l. All three raised as questions.

## Entries matched, skipped, adapted

- Matched: abs-quantum-dot, disorder-induced-zbp, crowded-trivial-subgap-states, quasi-majorana-smooth-confinement, one-end-only, local-probe-loophole, kondo-resonance, weak-antilocalization, trivial-andreev-band-gap-reopening, diode-vortex-screening, fine-tuning-and-selection.
- Adapted: diode-vortex-screening (its signature reads the diode as finite-momentum pairing; here the diode's sign reversal is read as a topological phase jump). trivial-andreev-band-gap-reopening (no protocol here; applied to the nonlocal jumps offered as "another global probe").
- Skipped: full-shell-flux-andreev (columnar sandwich, not a full shell, no uncovered junction segment; the skill's own example says to skip it for partial coverage, though the flux-lobe physics is close, so Valentini et al. appears in related work); spin-orbit-length-pinning (needs a semiconductor normal segment with an SO length); exceptional-point-zero-mode (needs strong lead coupling; probes are tunnel junctions); fine-tuned-plateau and series-resistance-subtraction (no quantized height is claimed; the series resistance issue is kept in check 6 and question 5); field-enhanced-supercurrent-resonances (the Ic revival is periodic interference, not monotonic growth read as triplet pairing; the outside SQUID-diode row covers the relevant ordinary mechanism); protocol-parameter-sensitivity (no pass/fail protocol; the correlation classifier's settings are raised as question 7); micromagnet-stray-field, island, shapiro, charge, chiral, kitaev, transparent-junction-pi-crossing, switching-jump-blind-region, coulomb-dominated-interferometer (do not apply).
- Checks walked: zbp family (6) and practice (3). No checks exist for the diode or supercurrent families, which carry the main claim.

## Sources held out

- None. Every library source predates the paper (Aug 2026) except Legg 2502.19560 (v2, updated 2026-10-21; I grepped its full text for "2608", "nano-SQUID", "Nikodem", "topological insulator": no hits) and Akrap et al. 2501.18631 v2 (March 2026, before the paper).

## Related work verification

- 2304.00484 Ciaccia et al.: abstract via the arXiv API (ID, title, first author confirmed) plus full text (pdftotext): Fig. 3 caption "for Φext/Φ0 = 0.5 ... η = 0 independent on any other parameters"; sign lobes and gate-tuned asymmetry in App. C. Used as the source for the outside row.
- 2205.04469 Souto et al.: abstract plus full text: requirement (1) "The external flux should not be an integer multiple of the half flux quantum".
- 2205.09276 Hou et al.: abstract (also a library source).
- 2210.03507 Hess et al.: abstract (also a library source; your Ref. [12]).
- 2008.02348 Valentini et al.: abstract (also a library source; your Ref. [11]).

## Library gaps

- No entry for an ordinary SQUID diode and phase jump: in any flux-periodic two-junction SQUID with unequal junctions and non-sinusoidal current-phase relations, Ic minima, a diode-efficiency sign change at half a flux quantum and phase-driven Andreev spectral jumps arise without topology (Ciaccia et al. 2023, Souto et al. 2022). Suggested tests: a non-topological SQUID model fitted to Ic±(Φ) and η(Φ); the diode sign pattern followed as asymmetry is gated; a trivial control SQUID.
- No checks for the diode and supercurrent families.
- No entry for the reliability of automated end-to-end correlation classifiers (sign of a derivative without a threshold).

## Uncertainties

- Several "part" marks rest on captions only (Kondo Zeeman splitting, nonlocal gap closing and reopening, gate tuning of the nonlocal boundary jumps).
- Whether the high tunnel conductance in A and C reflects the series circuit or the barrier is unclear from the text.
- The page numbers follow the page markers in the extracted text.

## Skill issues

- The status ladder has no value for the case where the paper itself concludes in favor of the lookalike (disorder-induced ZBPs here). I used "Tested in part" and said so in the cell.
- Library families center on ZBPs and Shapiro steps. A paper whose main claim is a global supercurrent and diode signature leaves most of the checks off target; the zbp-transparency check (cutter gates) has no analog for fixed ALD barriers.
- The rule that "a test counts as shown only when the paper shows the measurement" is unclear when the measurement exists but the specific analysis (for example peak splitting in field) is not done. I marked such tests "part".
- "Look at the figure again" can't be followed with text-only input.
- The skill says to use a linked data repository if reachable; the task's fetch limits ruled out Zenodo. The skill could say what to do when that conflicts with the run's limits.
- Step 7 says to write reports/<id>.md; this run returned the report in the reply as instructed.
