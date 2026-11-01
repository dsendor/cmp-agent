# Run notes: arXiv 2509.02552v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 entries. Skill and report template read once at the start.
- Paper read: the v1 PDF supplied (8 pages: main text, Methods, references; figures checked on the page images) and its extracted text. Title from the PDF: "Interaction-limited conductivity of twisted bilayer graphene revealed by giant terahertz photoresistance". I did not open the arXiv abstract page, per the task instructions, so the title comes from the PDF.
- Could not read: the Supplementary Information. It is cited for the 70% photoresistance, the Te up to 15 K estimate, the setup and the umklapp prefactor enhancement, and it is not in the v1 PDF. No data repository or code is linked. No ancillary figure data, so read_mtx.py was not used.
- Recognition: I recognized no later history of this paper.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| C1. Positive ΔρTHz at TL = 2 K in doped TBG, growing with power, so e-e interactions set ρ(T), including the linear-in-T regime | Fig. 1d, 2a, 2b, 2c, 2d, 2e | 2° TBG; MATBG1 (1.05°); MATBG2 (1.04°) | f = 0.14 THz only; P = 0.03 to 1 Pmax, Pmax not given in absolute units; n within about ±2×10^12 cm^-2 (2°) and ν from about -5 to 5 (MATBG1); TL = 2 K for Fig. 2a,b, up to 80 K in Fig. 2e (MATBG2); dρ/dT = 92 Ω/K at ν = 1.7, 0 to 50 K (Fig. 2c, MATBG1 only). "Up to 70%" is in the SI. |
| C2. e-ph contribution (hot-electron phonon emission) negligible | Fig. 2f | MLG, one device | B from -0.3 to 0.6 T; SdHO inset 0.8 to 0.95 T |
| C3. Te up to 15 K above the lattice | SI only | not stated | from ρ(T) comparison and SdHO damping |
| C4. T² resistivity at \|ν\| ≈ 0.1 and 3.8, below the umklapp thresholds | Fig. 3a to 3f | 1.58° device; "all our high-angle (θ = 1.6 − 3°) devices" claimed, no count, none other shown | Fig. 3a at 4.2, 10, 20, 50 K, ν from -6 to 6; Fig. 3b,c roughly 10 to 200 K on log axes, four fillings; ρ0 not given; densities "as low as 10^11 cm^-2" |
| C5. Interpocket e-e scattering from broken Galilean invariance gives a prefactor of about 0.1 Ω/K², inside 0.005 to 0.5 Ω/K² | Eq. 1 to 6 | theory | Λ from 0.01 to 1 depending on screening |

Missing counts: total devices fabricated and measured, devices showing each effect, cooldowns, datasets. The photoresistance of the 1.58° device (the device behind C4) is not shown in the main text.

## Entries matched, adapted, skipped

- Matched: fine-tuning-and-selection (always applies).
- Adapted: series-resistance-subtraction. Its signature (conductance near 2e²/h) does not apply, but its mechanism (an analyst-chosen subtracted quantity moves the extracted value toward the expected one) matches the ρ0 subtraction in Fig. 3b,c, where ρ0 sets the apparent exponent on a log-log plot. Library test texts kept verbatim in flags.json; the report explains the adaptation.
- Checks: no library family covers this paper (no zbp, shapiro, kitaev or charge signal), so only the three practice checks were walked.
- Skipped as not applicable to a hot-electron transport measurement in TBG (no zero-bias peak, quantized conductance, tunnel probe, Josephson junction, island, QAH film, Kitaev chain, interferometer or diode): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, field-enhanced-supercurrent-resonances, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, local-probe-loophole, coulomb-dominated-interferometer, diode-vortex-screening.
- Skipped: protocol-parameter-sensitivity (no automated pass/fail protocol).

## Outside rows (library gaps)

1. Lattice heating (bolometric photoresistance). Source opened in full text: Freitag et al., arXiv 1202.5342. Their control: compare the photoresponse with the measured bolometric coefficient across gate voltage, and extract electron and lattice temperatures separately ("Our analysis yields elevated electron and phonon temperatures", abstract). Tests taken from that control. Status tested in part: dρ/dT shown at one filling (Fig. 2c), comparison itself in the SI, no lattice temperature estimate. I judged the MLG control as not separating lattice heating, since doped MLG at 2 K has a small dρ/dTL; that is my reasoning, stated in the report as such.
2. Te-dependent screening of charged impurities (with energy averaging of the transport time). Source opened in full text: Hwang and Das Sarma, arXiv 0811.1212 (abstract: "temperature dependent screening of the Coulomb disorder without any phonons"; text: the leading low-T correction in graphene goes as ρ0[1 + O(T/TF)²]). The paper mentions distribution smearing only at the CNP, so the note is "data bear on it" (Fig. 3b,c).
- Library gap suggestion: a "hot-electron transport" family covering bolometric lattice heating, Te-dependent impurity scattering and subtracted-offset exponents, with checks for lattice thermometry and dρ/dT comparison.

## Sources held out

- None of the library sources used (Frolov et al. 2309.09368, Akrap et al. 2501.18631, Zhang et al. 2101.11456) were opened in this run; I relied on the library's quotes. I did not check whether Akrap et al. v2 (2026) cites this paper; its topic (reproducibility reports) makes that possible but unlikely. No source was skipped.

## Related work checks

All via the arXiv API abstract (id_list query), confirming ID, title and first author:
- 1202.5342 Freitag (abstract and full text).
- 0811.1212 Hwang (abstract and full text).
- 2207.14223 Hubmann (abstract).
- 2301.13742 Mehew (abstract).
- 2108.07753 Jaoui (abstract).
Also opened: 2112.07971 Hubmann (abstract), not listed. Searches for Kravtsov et al. (viscous THz photoconductivity, ref. 50) and Ishizuka and Levitov (ref. 26) returned no match on the queries tried; not listed. No result was this paper or a version of it.

## Unsure

- Whether Fig. 3a raw ρ(ν) at four temperatures counts as "raw data before subtraction" for the adapted entry; marked "part".
- Whether the paper's comparison of ΔρTHz with ρ(T) counts as the Freitag bolometric-coefficient test; marked "part" because it is described for all fillings but shown only through Fig. 2c, and its details sit in the SI.
- Whether Te-dependent impurity screening counts against "electron interactions" in the paper's sense: it is an electronic many-body effect, but it is not the current-relaxing e-e scattering of Eq. 1. The report frames it against Eq. 1 and the e-e reading of ΔρTHz.
- I read T/TF near 0.5 from the "TF/2" label at the top of Fig. 3b; the exact temperature of that marker is my reading of the figure.

## Skill issues

- Scope: the skill covers papers outside the library's scope with "adapt the matching entries", but here almost none match. It does not say whether a near-empty match (only the always-on entry) should still produce a full report, or whether outside rows may be added to fill the gap without a hint in the library.
- The skill says to read the arXiv abstract page for the title; this task forbids it. I took the title from the PDF.
- For an adapted entry, flags.json asks for "test text from the library"; it is unclear whether adapted tests should keep the library wording (I kept it) or be rewritten for the device.
- No check family fits the paper, so only the practice checks ran. The skill does not say whether to borrow checks from a near family.
- The template's "What this is" asks for the lookalike count; with an out-of-scope paper the count of 28 overstates what was applied.
