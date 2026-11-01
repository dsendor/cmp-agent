# Run notes: 2608.17404v1

- Library version: 0.5 (meta.updated 2026-10-24).
- Skill read: cmp-assistant/skill/SKILL.md and report-template.md; library cmp-assistant/library/lookalikes.yaml, including each entry's tests and the checks section. read_mtx.py not used, since no .mtx files were provided.

## What I read
- The paper's extracted text only (main text, Methods, Supplementary Information S1.A to S1.G, Figs. S1 to S5), as the run instructions specified. I had no PDF and no abstract page. The title comes from the paper text. Page numbers are main-text pages 1 to 7 and supplement pages 1 to 6, inferred from page markers in the text. Figure details come from the captions. I glanced at tick and colour-bar labels only for the tunnel-resistance remark, and labelled that remark as approximate.
- I did not open the Zenodo data repository (10.5281/zenodo.21988906), because the run instructions allowed fetches only from arxiv.org, export.arxiv.org and api.openalex.org. So I counted no devices or datasets from it.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| h/2e-periodic Ic oscillations, near full revival at integer flux | Fig. 1e, 3a, S2a | A, B, C | Bx about -4 to 4 T (B, C); device A spectra -6 to 6 T (Fig. S1). Periods not stated numerically |
| Diode effect, eta up to about 20%, sign reversal at half-integer flux, robust in VG | Fig. 1e, 3a, S2a, S4 | A, B, C (S4 maps for B, C) | VG about -75 to 25 V in S4; field 0 to 4 T |
| Local spectral jumps aligned with Ic features; device A ZBP appears in the predicted window | Fig. 1f-g, S1, 3b-c, S2b-c | A (one probe), B, C (two probes) | Device A VG = -10, 0, 10, 20 V (gate limited by leaky dielectric) |
| Nonlocal jumps at expected boundaries, plus extra jumps at high field | Fig. 3d-e, S2d-e, S5 | B, C | Nonlocal corrected with the Martinez et al. formalism |
| ZBPs at both ends in topological and trivial windows and at zero field; correlation via sign of d3I/dV3 | Fig. 4, S3 | B, C | B: Bx = 0, 1, 2 T cuts, VG -30 to 30 V, bias +-500 uV; C: Bx = 0, 2.5, 4 T |
- Counts: three devices presented (A, B, C). "a series of devices" with two probes; tunnel-junction yield "below 50%"; global signatures "in all examined devices". Missing: devices fabricated, measured, cooldowns, number of gate points in Fig. 4l, temperature series.
- Geometry (Table S1): A 21 nm x 70 nm x 1.9 um; B 36 x 70 x 1.3; C 16 x 80 x 2.5.

## Internal consistency points noticed
- Cross-section: text says B is "approximately 35% larger" than A. Table S1 gives 36 x 70 vs 21 x 70 nm^2, a ratio of 1.71. Methods give d ~ 20 nm, which device B (36 nm) does not match. Raised as question 5.
- Device C: "All key features are reproduced" vs "a zero-bias conductance peak was mostly absent in this device" vs the strong increase of correlated ZBPs in Fig. S3. Raised as question 6.
- Tunnel resistance: Methods say contacts "typically exhibit resistances exceeding 100 kΩ". The colour scales of Fig. S1 (device A) and S2 (device C) read about 0.8 to 2 e^2/h, roughly 13 to 30 kOhm. This rests on garbled tick labels, so I put it in the report body under check 6 and not in the questions.
- Not in the report (too uncertain from extracted ticks): Fig. S3j for device C seems to show Ic about 3 to 4.5 uA with RN about 4.8 to 4.9 kOhm. That gives IcRN of about 15 to 20 mV, far above what a Nb gap allows (about 1 meV, IcRN of a few mV at most). Device B (Fig. 4j: Ic hundreds of nA, RN hundreds of Ohm) gives about 0.1 to 0.5 mV. If the units read right, one axis in Fig. S3j is off by orders of magnitude. Worth checking against the figure.

## Entries matched, skipped, adapted
- Matched (13 rows including one outside): fine-tuning-and-selection, abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, one-end-only, local-probe-loophole, trivial-andreev-band-gap-reopening, diode-vortex-screening, kondo-resonance, weak-antilocalization, full-shell-flux-andreev, plus the outside asymmetric higher-harmonic SQUID diode.
- Adapted: full-shell-flux-andreev. The device is a columnar TI nanowire with Nb on two sides, not a full shell. The physics carries over: flux-tunable Andreev levels in a junction dot giving ZBPs in odd flux lobes. diode-vortex-screening: here the signature is read as a topological transition signal, and the library reads it as finite-momentum pairing. I matched on the physics.
- Skipped: fine-tuned-plateau and series-resistance-subtraction (no quantization claim; the subtraction is covered by the zbp-raw-conductance check). micromagnet-stray-field (no magnets; trapped flux in Nb is mentioned by the authors for high-field jumps). spin-orbit-length-pinning (TI Dirac surface states, no Rashba normal segment with an SO length). exceptional-point-zero-mode (strong tunnel barriers, weak lead coupling). protocol-parameter-sensitivity (no pass/fail protocol; the correlation metric's thresholds are raised as question 7). field-enhanced-supercurrent-resonances (Ic revival at integer flux does not exceed the zero-field value). The chiral, island, shapiro, charge, kitaev, interferometer and transparent-junction entries don't apply to this device.
- Check families walked: zbp and practice. The library has no checks for the diode, supercurrent or nonlocal families.

## Sources held out
- None. Every library source predates the paper (18 Aug 2026) except Legg 2502.19560 v2 (21 Oct 2026). I downloaded that version's PDF and searched it for "2608", "nano-SQUID", "Nikodem" and "topological insulator", with no hits, so I kept it. The report uses no quote from it. Akrap et al. 2501.18631 v2 is dated 25 Mar 2026.

## Related work, how checked
- 2208.10856 (Fominov, Mikhailov): abstract page opened; title and first author confirmed; abstract read via the arXiv API.
- 2205.04469 (Souto, Leijnse, Schrade): abstract page opened; title and first author confirmed; abstract read.
- 2008.02348 (Valentini): abstract page opened; abstract read.
- 2210.03507 (Hess): abstract page opened; abstract read.
- 1902.02773 (Chen): abstract page opened; abstract read.
- None checked in full text.

## Library gaps
- Asymmetric two-junction SQUID diode (trivial): flux-tunable diode with polarity tied to integer and half-integer flux, from non-sinusoidal current-phase relations plus junction asymmetry (2208.10856, 2205.04469). It bears on any claim that reads diode sign reversal in an interferometer as a topological transition. Suggested family: diode.
- More generally, a ground-state phase jump of pi at half flux is ordinary SQUID physics. Spectral jumps in local and nonlocal conductance follow any such jump, whether the phase is topological or not. The library has no entry for "global phase-jump signatures read as a topological gap". The outside row covers part of this.
- No library checks exist for the diode, supercurrent or nonlocal families.

## Unsure
- Status semantics when the authors themselves favour the lookalike (disorder, crowded states). I used "Tested in part", since tests are shown and the paper doesn't conclude against them.
- Kondo Zeeman test: field sweeps exist but also tune the phase, so I marked them "no", with a clause in the table.
- I did not recognize this paper (it postdates my training). I know the authors' earlier nano-SQUID papers (2412.07993, Sci. Adv. diode paper) and did not use them.

## Skill issues
- The skill assumes the abstract page and PDF; this run had extracted text only. The title then comes from the paper text, and figure details from captions are thin for colour-scale checks.
- No guidance for papers whose main claim is global (critical current, diode) with local ZBPs reported as inconclusive by the authors. The status ladder is built around authors arguing against a lookalike, and doesn't cover authors endorsing one.
- The "Left open by the authors" status requires that no test is shown. A paper that shows a test and then concludes for the lookalike has no fitting status other than "Tested in part".
- The data repository rule ("if you can reach it") conflicts with run-level fetch restrictions. I skipped Zenodo.
- The template has no slot for internal numeric inconsistencies (for example the 35% vs Table S1 mismatch). I put them in the questions.
