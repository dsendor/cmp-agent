# Run notes: 2503.17875v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries. Skill: cmp-assistant/skill/SKILL.md and report-template.md.
- Date: 2026-10-25. Version: v1 (given).

## What I read
- The v1 PDF (28 pages, main text, Methods, Extended Data Figs. 1 to 4) and its extracted text. Per the task, I opened no arXiv abstract page, HTML, journal version or other copy of this paper.
- I looked at every figure on the rendered PDF pages: Fig. 1 (p. 5), Fig. 2 (p. 9), Fig. 3 (p. 11), Fig. 4 (p. 15), Extended Fig. 1 (p. 26), Extended Figs. 2 and 3 (p. 27), Extended Figs. 3b and 4 (p. 28).
- Page numbers are physical PDF pages.
- The Supplementary Information (T(n) fit, quantum capacitance correction, AFM probe alignment, hole-side field data, Fig. S4, model details) is not in this PDF, so I could not read it.
- Data: "available from the corresponding author upon reasonable request" (p. 16). No ancillary files and no repository, so read_mtx.py was not used.
- I recognized the group's planar tunneling work in general terms. I know of no later history (comment, replication, journal version) and used none.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| dμ/dn extracted from dI/dVb and dI/dVg; correlated gap at ν = 2 (Δ = 1.3 ± 0.14 meV), g = 5.4 ± 0.2 | Fig. 2a, b, e; Ext. Fig. 1 | One junction. Twist angle quoted as 1.06° ± 0.02° (p. 3), 1.08° (Fig. 1b caption), 1.07° (Methods p. 22) | T = 0.3 K and 4 K; Vb = ±42 mV for the extraction; Vac 0.2 to 1 mV on bias, 5 to 10 mV on gate, 11.07 Hz |
| Landau levels and Chern insulators in dμ/dn | Fig. 2c, d, f, g; Ext. Fig. 2 | Same | B 0 to 6 T (Fig. 2c), 0 to 2 T (Ext. 2a, b), 1 to 3 T (Ext. 2c), 0 to 8 T (Ext. 2d); 0.3 K |
| m* swings heavy to light across ν = 1, 2, 3, consistent with topological heavy fermion model; LL masses 0.174 me (flat, near CNP) and 0.047 me (remote) | Fig. 3a, b, d; Ext. Fig. 2e | Same | 0.3 K, 4 K, 20 to 77 K (Fig. 3d); text says the effect persists "up to ~ 50K" (p. 12) and "until ~77 K" (Fig. 3 caption) |
| Entropy plateaus near 10 K and 20 K, read as 4-fold and 8-fold local moments | Fig. 4b, c; Ext. Fig. 4 | Same | dμ/dn map to about 90 K (Fig. 4a); entropy 4.2 to 36 K at about 16 temperatures, three-point fits; electron side only; model comparison 5 to 24 K |
| Pomeranchuk-like non-monotonic dμ/dn(T) near ν = 1 | Fig. 4e | Same | 4 to about 90 K |

- Devices fabricated: not given ("devices" plural, p. 16).
- Devices measured, devices showing the effect, cooldowns: not given.
- Hole-side temperature series: not shown.
- Gate range in Fig. 1b: about -12 to +12 V. Bias range: -70 to +70 mV (to 140 mV in Ext. Fig. 2d).

## Entries matched, adapted and skipped
- Scope: the paper is out of the library's families (no zbp, quantization, nonlocal, island, shapiro, supercurrent, charge, chiral, kitaev or diode signal). Only the practice checks apply: report-counts, report-ranges, report-processing.
- Matched: fine-tuning-and-selection, which is always included.
- Adapted: series-resistance-subtraction. Its mechanism is that a subtracted circuit quantity moves the extracted value, and the same holds here for dividing by T(n) ∝ exp(0.258 n/n0), the choice of Cb and Cg, and the dropped factor in Eq. 3. In flags.json I kept the library test text verbatim and put the adaptation in the table.
- Skipped, with the device or claim each needs:
  - Majorana-specific zbp entries need a superconducting hybrid nanowire: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode.
  - fine-tuned-plateau needs a quantized conductance claim.
  - one-end-only, trivial-andreev-band-gap-reopening and local-probe-loophole need a Majorana wire.
  - protocol-parameter-sensitivity needs a pass/fail protocol. The analysis-window sensitivity of the entropy fit goes into question 7 instead.
  - chiral-plateau-superconductor-short needs a QAH insulator with a superconductor.
  - island-states-coulomb-spacing needs a Coulomb blockade island claim.
  - All shapiro entries, field-enhanced-supercurrent-resonances and diode-vortex-screening need a Josephson junction or superconductor.
  - charge-trap-fractional-shift and coulomb-dominated-interferometer need a fractional charge claim.
  - false-poor-mans-majorana needs a quantum dot Kitaev chain.
- The zero-bias gap in Fig. 1b is an ordinary phonon gap, and the authors explain it as one. It is not part of the claim, so I did not treat it.

## Sources held out
- None. I did not open any matched library source. The two used entries cite Frolov et al. 2023, Zhang et al. 2021 and Akrap/Frolov et al. 2026, which are about Majorana and reproducibility work and do not concern this paper.
- In the arXiv search for "planar tunneling" and "twisted bilayer", one result was this paper (2503.17875v1). I skipped it and did not open it.

## Related work and outside-row sources, how checked
For each paper I confirmed the ID, title and first author from the arXiv API and from the arxiv.org/abs page meta tags, and checked the description against the abstract.
- 1912.06150 Zondiner et al.: abstract.
- 2009.01836 Rozen et al.: abstract. Supports "about 1kB per unit cell" and "quenched by an in-plane magnetic field".
- 2008.10830 Saito et al.: abstract. Supports "of order unity per unit cell area, with a measurable fraction that is suppressed by an in-plane magnetic field".
- 2106.11333 Tilak et al.: full text (v1 PDF). Section on the planar device, p. 6 to 7: "This work difference results in the TBG becoming electron doped and creates a potential-well, approximately the size of the tunneling electrode, where charge carriers can be confined." Fig. 4e shows Coulomb diamonds at 0.3 K. The authors include S. Wu, Z. Zhang and E. Y. Andrei, which is why question 8 says "your group".
- 1908.04595 Uri et al.: abstract. Supports "display significant variations in the local θ with a span close to 0.1°".
- 1402.1981 Larentis et al.: abstract. Source for the exchange-correlation outside row: negative compressibility interpreted "using the random phase approximation (RPA) for the exchange and correlation energies". It is in the table, and I left it off the related-work list to keep that list at five.
- 1903.10492 (Tomarken et al., compressibility in MATBG) and 1109.5701 (Li, Hwang and Das Sarma): abstracts read, not used.
- One wrong ID guess (1904.07887) returned an unrelated cosmology paper. Not used.

## Library gaps
- No entries for thermodynamic signals: compressibility, chemical potential, or entropy from the Maxwell relation.
- Missing lookalikes:
  - carrier confinement or quantum dots under a planar tunneling probe (Tilak et al. 2021);
  - twist-angle inhomogeneity in moiré devices (Uri et al. 2020);
  - the exchange-correlation contribution to compressibility read as effective mass (Larentis et al. 2014, or Eisenstein's classic work, which is not on arXiv);
  - reference-choice systematics in the Maxwell-relation entropy (μ at the CNP fixed at every T, S = 0 at ν = 4). I found no opened paper that shows this as a lookalike, so it went into question 7 only.
- No checks family for spectroscopy or thermodynamics in moiré systems.

## Unsure
- The Eq. 3 derivation: from Methods Eqs. 1, 5 and 7, Eq. 3 drops a factor 1/(1 - ρ(EF)/ρ(EF + eVb)). At Vb = -42 mV the probe sits on the valence flat-band peak (Fig. 1b, Ext. Fig. 1a), so the ratio may not be small. I raised this as a question, not as a finding.
- Whether test 1 of the confinement row counts as "part": Landau fans and Chern insulators follow the Streda lines at 0.3 K, which argues against a dot dominating, but no offset under the probe is quantified.
- Whether "Left open by the authors" fits the exchange row: the quoted sentence limits the formula to weakly correlated excitations without naming exchange.
- Fig. 4c shows CNP entropy near 6.5 kB per moiré at 36 K, above ln 70 ≈ 4.25, the maximum for 8 flavors. The paper links the rise to phonons or charge excitations (p. 15). Not raised.
- The text says Fig. 3b shows persistence "up to ~ 50K", but Fig. 3b covers only 0.3 K and 4 K. Not raised.
- Math in the quotes is normalized from PDF glyphs (for example "exp(0.258 ∙ n/n0)").

## Skill issues
- Step 7 says to take the title from the arXiv abstract page, and the Input section says to read the abstract page and PDF. This test forbids both, so I took the title from the PDF and shortened it for the header.
- The skill says to write reports/<id>.md and .notes.md. The test overrides this and the output goes in the reply.
- The template's "library of <n> known lookalikes in topological transport" reads oddly for an out-of-scope paper. The scope rule allows only one sentence to explain the adaptation.
- It is unclear whether flags or tables should keep the library's test text verbatim or adapted text for an adapted entry. I did both: verbatim in flags.json, with a bracketed adaptation in the table.
- The step-5 cap of five related papers does not say whether outside-row sources count toward it. I counted them separately.
- There is no guidance on how many outside rows are appropriate when most of the library does not apply.
- The writing rules ban contrast phrasing, while the template's "Raw data before subtraction" wording needed adapting here. That is minor.
- The report runs about 930 words outside the table, counting the header and the eight questions, a little above the 900 aim. The questions are long because flags.json must carry them verbatim.
