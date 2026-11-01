# Run notes: arXiv 2608.17404v1

- Library version: 0.5 (meta.updated 2026-10-24). 28 lookalikes; checks sections exist for zbp, shapiro, kitaev, charge and practice.
- Date of run: 2026-10-24.

## What I read
- The paper as extracted text only (paper.txt, given by the caller), including the Supplementary Information (S1.A to S1.G, Figs. S1 to S5, Table S1). There was no PDF and no abstract page; I did not fetch the paper in any form, as instructed. I took the title from the first line of the text, not from the arXiv abstract page. The two-column layout was interleaved in the extraction, so I reconstructed page numbers from the page markers in the text. Figure details come from captions and body text only, since I could not see the figure images or axis values. Two axis readings are uncertain: the Fig. S4 VG axis appears to run from about -75 V to 25 V, and the Fig. S2 flux ticks could not be read.
- Data repository: the paper cites Zenodo 10.5281/zenodo.21988906. I did not open it (the run used text only), so no counts come from it.
- The skill, the template and lookalikes.yaml, read once at the start. I did not use read_mtx.py because there were no ancillary data.
- I recognized the paper: no. It postdates my training data.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| Ic oscillates with period h/2e and almost fully revives at integer flux | Fig. 1e, 3a, S2a | A, B, C | Bx roughly 0 to 4 T (Fig. 3), up to ±6 T (Fig. S1); 30 mK only |
| Diode efficiency about 20%, sign reversal at half-integer flux | Fig. 1e, 3a, S2a, S4 | A, B, C (VG maps for B and C) | VG maps for B and C, apparently -75 to 25 V (Fig. S4) |
| Local spectral jumps aligned with Ic minima and diode reversal | Fig. 1f-g, 3b-c, S2b-c | A (one probe), B, C (two probes) | Fig. 1f at VG = 10 V; device A VG -10, 0, 20 V (Fig. S1) |
| ZBP appears at the half-flux jump in device A and persists, stable in VG | Fig. 1f-g, S1 | A | 4 gate values; gate range limited by a leaky dielectric |
| Nonlocal jumps at expected phase boundaries | Fig. 3d-e, S2d-e, S5 | B, C | Nonlocal VG maps over ±40 V (Fig. S5) |
| ZBPs in both regimes, including at zero field; end-to-end correlation similar | Fig. 4, S3 | B, C | Bx = 0, 1, 2 T (B); 0, 2.5, 4 T (C); VG ±30 V |

Missing counts: the number of devices fabricated and measured (only "all examined devices" and a tunnel-junction yield "below 50%"), cooldowns, the number of datasets, temperature series, field-angle series, ZBP peak heights, and the subtracted resistance values. Device dimensions are in Table S1 (A 21 x 70 nm, B 36 x 70 nm, C 16 x 80 nm; B is about 1.7 times A, which matches the stated "approximately 70% larger").

## Entries matched, skipped and adapted
- Matched (14): fine-tuning-and-selection, diode-vortex-screening, abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, one-end-only, local-probe-loophole, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, trivial-andreev-band-gap-reopening.
- Skipped:
  - full-shell-flux-andreev: the wire is not fully covered (Nb on two sides, tunnel probes at the ends), per the skill's example. The physics (flux-tunable Andreev levels giving ZBPs in odd flux windows) is close, so I list Valentini et al. under related work.
  - micromagnet-stray-field: there are no magnets, and the zero-field ZBPs are not read as topological.
  - fine-tuned-plateau and series-resistance-subtraction: no quantized conductance is claimed. The subtraction itself is covered by the zbp-raw-conductance and report-processing checks.
  - protocol-parameter-sensitivity: there is no pass/fail protocol. The correlation classifier's dependence on data choices goes into question 6.
  - field-enhanced-supercurrent-resonances: Ic revives at integer flux, and the paper does not report supercurrent growing above its zero-field value or read anything as triplet pairing.
  - The shapiro (other than transparent-junction-pi-crossing), island, charge, chiral and kitaev entries: there is no such measurement.
- Adapted: transparent-junction-pi-crossing (family shapiro) applied to the claimed protected π crossing behind the device A ZBP (Fig. 1c). Checks: the diode and nonlocal families have no checks section, so I walked the zbp and practice checks.

## Status judgments I was unsure of
- disorder-induced-zbp: the paper's own conclusion leans toward this lookalike, and the status scale has no slot for "authors favour it". I used Tested in part.
- weak-antilocalization channel-number test marked part: the VG sweep through the Dirac point changes the channel count, but the paper does not analyse it that way.
- transparent-junction-pi-crossing and spin-orbit-length-pinning: one test is shown for all of the device A evidence, but the paper does not argue against either lookalike, so neither can be Ruled out.
- diode-vortex-screening: field sweeps across three cross-sections are an equivalent of the "width" test, so I marked it all. The paper does not discuss screening as an origin of the diode effect.
- Kondo Zeeman test marked no: field maps exist (Fig. 3b-c), but the text gives no splitting analysis and I could not see the figures.
- The device C flux question (question 5) uses the geometric cross-section. The effective area of the surface state may be smaller, which would lengthen the period, so I phrased it as a question.

## Sources held out
None. All library sources predate 18 Aug 2026 (the latest are Frolov et al., Science, January 2026, Akrap et al., PRB 113, 2026, and Legg's comment, v2 2026), so none can discuss this paper. I did not fetch them to confirm.

## Related work: how each was checked
- 1906.01179 (Dartiailh): arXiv API abstract; ID, title, first author and claim confirmed.
- 2205.04469 (Seoane Souto): API abstract and full text (PDF). Quote used for the outside row: "The external flux should not be an integer multiple of the half flux quantum, Φ ≠ nΦ0/2. If this condition is not satisfied, then I(ϕ) = −I(−ϕ) and Ic+ = Ic−, implying that the JD effect vanishes".
- 2304.00484 (Ciaccia): API abstract and full text (PDF). Appendix: "The sign of the diode efficiency is mirrored with respect the magnetic field value corresponding to half flux quantum when the critical current asymmetry α between the two junctions changes sign."
- 2004.08583 (Yu) and 2008.02348 (Valentini): API abstracts; confirmed.
- I opened the abstract pages through the export API, not the HTML abstract page, and waited 3 s between calls.

## Library gaps
- Diode: the library's only diode entry is vortex and Meissner screening. A trivial two-junction interferometer diode (skewed current-phase relations plus junction asymmetry) reproduces both the Φ0-periodic Ic and a diode sign change at half-integer flux, which are the core global signatures here. I suggest a new entry sourced from Seoane Souto et al. 2022 and Ciaccia et al. 2023, with tests: junction asymmetry tuned with η tracked; CPR harmonics characterized; loop inductance estimated.
- There is no checks section for the diode or nonlocal families.
- There is no entry for flux trapping or vortex entry in the superconducting leads producing spectral jumps (the paper raises it itself, p. 4).

## Skill issues
- Step 3's status rules leave no clean status for a lookalike the authors themselves favour (disorder here); Tested in part reads oddly.
- "Ruled out" needs the paper to conclude against the lookalike. When a single shown test separates it but the paper is silent, the row drops to Tested in part, which may understate what the data show.
- The template asks for the title from the arXiv abstract page. With text-only input this is not possible, and the skill does not say what to do.
- The skill does not say whether a paper whose headline is partly a negative finding (ZBPs uncorrelated with global signals) should treat the ZBP family as a claimed signal. I treated the device A ZBP as claimed and the B and C ZBPs as data bearing on the lookalikes.
- Matching full-shell-flux-andreev is ambiguous for partly covered wires that are flux tuned through phase. The skill's skip example decided it.
- Hold-out checks need the library sources' contents; the skill does not say whether to fetch them all.
