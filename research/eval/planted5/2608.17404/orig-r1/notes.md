# Run notes: 2608.17404v1

- Library version: 0.5 (meta.updated 2026-10-24). 28 lookalikes, 18 check steps.
- What I read: the skill, report-template.md and lookalikes.yaml, all in full. Paper: the extracted text at the given scratchpad path only, main text plus Supplementary Information (Notes S1.A to S1.G, Figs. S1 to S5, Table S1). Per instructions I did not open the abstract page, PDF or HTML, so the title comes from the paper text. The text is a two-column extraction; I split the columns with a small script. Figure axis labels are garbled and minus signs are lost, so I took figure details from captions and text. Ranges read off axes are approximate.
- Page mapping: main-text pages follow the printed page numbers (pp. 1 to 7). SI pages are cited as "SI p. N" from the SI page numbers: S1.A-B p.1; S1.C-D and Fig. S1 p.2; Fig. S1 text, S1.E and Fig. S2 p.3; Fig. S2 text and Fig. S3 p.4; Fig. S3 text, S1.F and Fig. S4 p.5; Fig. S4 text and S1.G p.6.
- Could not open: the Zenodo data (10.5281/zenodo.21988906). Zenodo is outside the hosts this run allowed, so I did not try it and no device counts came from it. No ancillary .mtx files were provided, so read_mtx.py was not run.
- Verification: every paper quote in the report was checked by script against the normalized paper text and all matched. The only difference is the Ohm sign, which the extraction stores as U+2126.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Ic oscillates with period h/2e through the nanowire cross-section, with near-full revival, read as surface-dominated transport | Fig. 1e (A), 3a (B), S2a (C) | A, B, C | Bx about ±4 T for B and C; A's range is unclear from the caption. Ic ramped from zero. 30 mK base only. |
| Diode effect, η ≈ 20%, polarity reverses at half-integer flux, read as a ground-state phase jump (the trivial-to-topological transition) | Fig. 1e, 3a, S2a, S4 | A, B, C | S4: VG from about -75 to 25 V, Bx 0 to 4 T, for B and C. |
| Local spectral jumps at Ic minima and diode reversals | Fig. 1f-g, 3b-c, S2b-c | A (one probe), B, C (two probes) | Vb about ±1 mV. A at VG = 10 V, plus -10, 0, 20 V (Fig. S1). |
| Nonlocal conductance jumps at boundaries, plus extra jumps at high field | Fig. 3d-e, S2d-e, S5 | B, C | Corrected for circuit effects (Martinez formalism); line resistances measured; values not given. |
| ZBP appears in the first topological window and splits at 2Φ0, robust in VG | Fig. 1f-g, S1 | A | Four gate voltages; gate range limited by leaky dielectric. |
| ZBPs in trivial windows and at zero field; end-to-end correlation shows no clear regime difference | Fig. 3b-c, 4, S3 | B, C | VG -30 to 30 V at Bx = 0, 1, 2 T (B) and 0, 2.5, 4 T (C). Vb ±500 µV. Fig. 4l covers 0 to 4 T. |

Counts: three devices presented. Devices fabricated, devices measured, cooldowns and dataset totals: not given. The paper gives "a series of devices with two functioning tunnel contacts" (count missing), "all examined devices" (count missing), and a tunnel-junction yield "below 50%". Temperature: base temperature only. Field direction: axial, with Bz compensation from Fraunhofer scans; no angle dependence shown. Device geometry is in Table S1 (A 21 nm × 70 nm × 1.9 µm; B 36 × 70 × 1.3; C 16 × 80 × 2.5).

## Entries matched, adapted, skipped

- Matched directly: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, spin-orbit-length-pinning, exceptional-point-zero-mode, one-end-only, trivial-andreev-band-gap-reopening, local-probe-loophole, diode-vortex-screening, fine-tuning-and-selection.
- Adapted:
  - full-shell-flux-andreev: the device is a sandwich, not a full shell. The physics carries over: ZBPs in odd flux lobes, read through flux-driven topology. Its test was read as the length of the uncovered TI segment under the tunnel probe.
  - transparent-junction-pi-crossing (shapiro family): the topological reading rests on the protected crossing at phase pi in the TI line junction. Gate-tuned density was taken as the tuning knob.
  - protocol-parameter-sensitivity: applied to the automated peak/dip/none classification behind Fig. 4l. That classification is not a pass/fail protocol, but its outcome depends on the same kinds of data choices.
- Skipped:
  - fine-tuned-plateau and series-resistance-subtraction: no quantized peak height is claimed. The zbp-raw-conductance check was still walked.
  - micromagnet-stray-field: there are no magnets, and the zero-field ZBPs are not read as topological.
  - field-enhanced-supercurrent-resonances: the Ic revival is periodic interference read as surface transport. It is not supercurrent growing above the zero-field value read as exotic pairing. I considered it because switching-current phase dynamics could affect diode values.
  - chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, charge-trap-fractional-shift, coulomb-dominated-interferometer, false-poor-mans-majorana: no matching signal in the paper.
- Checks walked: the zbp family (6) and practice (3). No library checks exist for the nonlocal or diode families.

## Sources held out

None of the library sources cite this paper. Legg 2502.19560 has a v2 dated 2026-10-21, after this paper (2026-08-18), and Legg is a co-author here. I downloaded the v2 PDF and searched it for "nano-SQUID", "2608.17404" and "Nikodem": no hits, so I did not hold it out. Akrap et al. 2501.18631v2 (2026-03-25) predates the paper; a grep found no hits either. Hess et al. 2210.03507 is the paper's ref. [12]: it is cited by the paper and does not discuss it, so I kept it.

## Related work checks

All five abstract pages were opened on arxiv.org, and ID, title and first author confirmed from the citation meta tags. Abstracts were also read through export.arxiv.org.
- 2412.07993 (Nikodem): abstract.
- 2406.08265 (Schluck): abstract. The abstract-page title says "Robust"; the paper's reference list says "Protected". I used the abstract-page title.
- 2008.02348 (Valentini): abstract.
- 2210.03507 (Hess): abstract.
- 2205.04469 (Souto): abstract and full text. I confirmed the requirement "The external flux should not be an integer multiple of the half flux quantum, Φ ≠ nΦ0/2", the requirement of unequal transmissions, and efficiencies of about 40%.

## Library gaps

- No entry covers the global signatures this paper rests on: an h/2e-periodic Ic and a diode effect that reverses at half-integer flux, read as a phase jump that equals a topological transition. Trivial two-junction interferometers with skewed current-phase relations give flux-tunable diode effects that vanish at nΦ0/2 (Souto et al. 2205.04469). I added this as the outside row. Suggested library entry: diode family, "interferometer diode from trivial non-sinusoidal CPRs".
- No check family exists for nonlocal or diode signals.
- No entry covers end-to-end correlation metrics that lack a random-pairing baseline.

## Unsure

- Kondo: field maps from zero field exist (Figs. 3b-c, S2b-c), but Zeeman splitting is not analyzed. I marked that test "no" and the row "data bear on it". A "part" mark would also be defensible.
- Outside row: I marked the gate-asymmetry test "part". The Methods say gating breaks inversion symmetry, and Fig. S4 shows |η| versus VG, but the paper does not show whether η vanishes at any gate voltage.
- spin-orbit-length-pinning and transparent-junction-pi-crossing: every listed test is shown, but the paper does not conclude against these lookalikes, so both stay "Tested in part".
- The axis ranges come from garbled extracted labels.
- I did not recognize this paper or know any later history. I know the group's earlier nano-SQUID and diode papers only as cited.

## Skill issues

- The status set has no value for a lookalike the authors themselves conclude is present (the disorder ZBPs here). "Tested in part" fits by the rules but undersells it.
- Papers whose claim is partly negative (global signatures positive, ZBPs not diagnostic) don't fit the single "claim" in the template well.
- "Effect followed against field, sample width or edge quality": the "or" lets field alone satisfy the test.
- It is unclear whether an existing measurement with no analysis counts as a test "shown" (for example field maps versus Zeeman splitting).
- protocol-parameter-sensitivity is written for pass/fail protocols. Whether it should cover automated classifications like the one behind Fig. 4l is not stated.
- The skill says to read the abstract page for the title. This run forbade that, so the title came from the text. The skill has no fallback for this case.
- The skill doesn't say how to cite supplementary page numbers when the SI restarts its numbering.
- The prompt allowed no fetching from data repositories, which the skill otherwise permits for counting.
