# Run notes: 2608.17404v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalikes.
- Skill read: skill/SKILL.md and skill/report-template.md. scripts/read_mtx.py was not used because there are no ancillary .mtx files.
- Paper read: the local PDF (re-extracted with pdftotext in reading order, all 16 pages including the SM) and the local abs.html. The paper was not fetched. I rendered PDF pages 2 to 4 and 11 to 14 as images to read Figs. 1, 3 and 4.
- Page convention: main-text pages use the printed numbers 1 to 9. "SM p. N" uses the printed SM numbers 1 to 7 (PDF pages 10 to 16).
- Could not open: the Zenodo record 10.5281/zenodo.21988906. The proxy refused it (CONNECT 403), so the data repository was not used to count devices or ranges.
- Recognition: I did not recognize this paper and know nothing of its later history.

## Claims table (step 1)

| Claimed signal | Figures | Devices | Counts and ranges |
|---|---|---|---|
| h/2e Ic oscillations with near-full revival, read as surface-dominated transport | Fig. 1e (A), 3a (B), S2a (C) | A, B, C | A: about ±2.5 Φ0. B: about ±4 T. C: about -2 to 4 T (read from axes). Base about 30 mK, no temperature series. |
| Diode sign reversal at half-integer flux, read as a ground-state π phase jump, which theory ties to the topological transition | Figs. 1e, 3a, S2a; VG maps in S4 (B, C) | A, B, C | S4: VG about -75 to 25 V, Bx 0 to 4 T. η up to about 20%. |
| Spectral jumps in local conductance at the Ic minima | Figs. 1f-g, 3b-c, S2b-c | A (one probe), B, C | A: Bx ±6 T, Vb ±1 mV, VG = 10 V, plus S1 at VG = -10, 0, 20 V. B: ±4 T. |
| Nonlocal conductance jumps at phase boundaries | Figs. 3d-e, S2d-e, S5 | B, C | Field for S5 not stated. Some jumps are unmatched at high flux (p. 5). |
| Device A ZBP appears in the predicted window, persists, and splits at 2 Φ0; stable over VG | Figs. 1f-g, S1 | A | Three extra VG values. Gate range limited by a leaky dielectric. |
| ZBPs in both topological and trivial windows, including zero field; end-to-end correlation similar in both | Figs. 3b-c, 4, S3 | B, C (C: ZBP "mostly absent" in field sweeps, SM p. 4) | VG ±30 V at Bx = 0, 1, 2 T (B) and 0, 2.5, 4 T (C). Vb ±500 µV. Fig. 4l: Bx 0 to 4 T. |

Missing counts: total devices fabricated or measured ("a series of devices", "all examined devices"), cooldowns, number of datasets, temperature dependence, field-angle ranges. Known: tunnel junction yield below 50% (p. 5). Dimensions are in Table S1 (L = 1.9, 1.3, 2.5 µm).

## Entries matched, skipped, adapted

- Matched (zbp): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization.
- Matched (nonlocal): one-end-only, trivial-andreev-band-gap-reopening.
- Matched (diode): diode-vortex-screening.
- Matched (practice): local-probe-loophole, fine-tuning-and-selection.
- Adapted: full-shell-flux-andreev. The device is a columnar sandwich with axial flux, not a full shell. The mechanism (flux-tunable Andreev levels in the junction region under the probe) still applies.
- Adapted: transparent-junction-pi-crossing (shapiro family). The topological claim rests on the φ = π crossing of the TI line junction (Fig. 1c), so the entry applies to the zero-energy states at odd flux.
- Skipped: fine-tuned-plateau and series-resistance-subtraction, because there is no quantized-conductance claim. The zbp-raw-conductance check was still walked.
- Skipped: micromagnet-stray-field (no magnets), protocol-parameter-sensitivity (no pass/fail protocol), and field-enhanced-supercurrent-resonances (Ic is not claimed to grow with field).
- Skipped: spin-orbit-length-pinning. The mechanism needs a Rashba normal segment with a spin-orbit length, which the Dirac surface states lack. This was a judgment call.
- Skipped: exceptional-point-zero-mode. Tunnel contacts are above 100 kΩ (p. 5), so lead coupling is weak. This was a judgment call.
- Skipped as not applicable: chiral, island, the shapiro entries apart from the one adapted above, the charge entries, and false-poor-mans-majorana.
- Checks walked: zbp and practice. There is no checks section for the diode or nonlocal families.

## Sources held out

None. The library sources dated after August 2026 could have cited this paper. I checked Legg's comment arXiv 2502.19560v2 (updated 2026-10-21; Legg is an author here) by searching its full text for "Nikodem", "nano-SQUID", "2608" and "17404": no hits. Akrap et al. v2 is dated 2026-03 and Frolov et al. v1 is from 2023, both before this paper.

## Related work, how checked

- 2008.02348 (Valentini), 2210.03507 (Hess), 2205.09276 (Hou), 2205.09419 (Banerjee): abstract checked through the arXiv API and the arXiv abs page (title, first author, date).
- 2304.00484 (Ciaccia): abstract checked, plus full text. The quote "Note, that for Φext/Φ0 = 0.5, which equals φext = π, η = 0 independent on any other parameters." is in the Fig. 3 caption, PDF p. 6.
- 2205.04469 (Souto, Leijnse, Schrade): abstract and full text read as theory background for the outside row. It states that the diode vanishes at Φ = nΦ0/2 (p. 2). It is not listed in the report.

## Library gaps

- Trivial SQUID interference diode. In any two-junction interferometer with asymmetric arms and a non-sinusoidal CPR, η is zero and changes sign at half-integer flux (Ciaccia 2304.00484; Souto 2205.04469). A diode reversal at half flux therefore shows the phase jump. It does not separately show topology. This needs an entry and a diode-family checks section.
- Possible, not in the report because it is uncited: a reflectionless-tunneling or proximity zero-bias anomaly at zero field in disordered N-I-proximitized junctions.
- Possible, not in the report because it is uncited: spectral jumps from vortex entry or flux trapping in the Nb leads. The paper raises this itself (p. 4).
- No checks section for the nonlocal or diode families.

## Unsure

- Treating nonlocal "jumps at the boundaries" as the equivalent of "gap closing and reopening". In this phase-driven platform the theory predicts jumps (Fig. 2c). I marked the test "part" because it covers B and C only.
- diode-vortex-screening: the flux periodicity across three cross-sections likely separates it on its own. The paper does not conclude against it explicitly, so it stays "Tested in part".
- Field and gate ranges were read from low-resolution renders of the figure axes. They are approximate.
- Fig. S5: the field at which the nonlocal VG maps were taken is not stated.

## Skill issues

- The paper is partly self-critical: it reads its own ZBPs as likely trivial. The status scale has no slot for "the authors favour the lookalike". "Left open by the authors" needs no test shown, and "Ruled out" needs the paper to conclude against. Disorder therefore lands in "Tested in part", which reads oddly.
- The claim is mixed: global signals read as topological, local ZBPs read cautiously. The skill assumes a single claimed signal, so I wrote both into "The claim, as I read it".
- There are no checks for the diode and nonlocal families. I said so in "What this is".
- The template's "<n> known lookalikes" does not say whether that is the library total or the matched count. I used the total (28).
- The skill does not say how to cite pages for SM printed with its own numbering. I used "SM p. N".
- Step 7 says to write reports/<id>.md. The run prompt said to return the report inline, and I followed the prompt.
- The quote rule for "Not tested (data bear on it)" asks for a verbatim quote even when the paper does not discuss the lookalike. I quoted the sentence that points to the relevant figure.
