# Run notes: arXiv 2508.07351v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries, checks for zbp, shapiro, kitaev, charge and practice.
- Date: 2026-10-25.

## What I read
- The v1 PDF (6 pages, rendered at 150 and 400 dpi for Figs. 3 to 5) and its extracted text, both supplied by the task. No supplementary material is in the PDF: Ref. 35 points to "http://link.aps.org/supplemental/XXX". Figs. S1 to S11 were not available.
- I did not open the arXiv abstract page or any other version, as the task instructed. The title comes from the PDF metadata and first page.
- No data repository or ancillary files are linked, so read_mtx.py was not used.
- I did not recognize this paper and used no knowledge of its later history.

## Claims table (step 1)
| Claim | Figure | Sample | Counts and ranges |
|---|---|---|---|
| Strain-free (1x1) ML-Si2Te2 on HfTe2, lattice 390 pm, step 7.1 Å | Fig. 3 | Islands of about 5 to 10 nm in Fig. 3(a), (b) | "Systematic measurements across multiple samples" (p. 3), number not given |
| Bulk gap about 300 meV (VBM about -10 meV, CBM about 290 meV) | Fig. 4(a) and inset | One spectrum shown | "20 ML-Si2Te2 islands (See Ref. 35)" (p. 4); bias -1.0 to +1.0 V (main), about -0.6 to +0.6 V (inset) |
| In-gap edge state, a dI/dV peak near EF, about 2 to 3 nm wide | Fig. 5(a) to (c) | Island A, about 10 nm across; one point pair and one line cut, 0.36 nm spacing | Bias -0.1 to +0.1 V, Vstab -0.1 V, Vmod 2 mV; "multiple ML-Si2Te2 islands" (p. 4), number not given; Fig. S11 not available |
| Continuous edge ring in a dI/dV map | Fig. 5(d), (e) | Island B, about 9 nm across, a different shape from island A | One energy (+7 mV), Vstab 0.2 V, a grid of about 25 x 25 pixels |
| QSH phase in DFT (Z2 = 1, edge Dirac dispersion, nanoribbon edge width 1.35 nm) | Figs. 1, 2, S3 | Theory | n/a |

- Temperature: 5.8 K only. No magnetic field. W tips.
- Missing counts: islands with edge spectra, islands showing the peak, tips and cooldowns, number of samples.

## Entries matched, adapted and skipped
- Matched: fine-tuning-and-selection (always applies).
- Adapted: local-probe-loophole. Its signature is about Majorana overlap; I read it as "a local DOS probe can't establish that an edge mode is topological". Its tests are Majorana-specific. I read "nonlocal measurement" as an edge-conduction measurement and marked the quantum-dot test as not applicable ("no"). The test text in flags.json is kept verbatim from the library.
- Skipped (they need a superconducting hybrid device, Josephson junction, Kitaev chain, quantum Hall interferometer, QAH-superconductor or diode geometry): abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, field-enhanced-supercurrent-resonances, charge-trap-fractional-shift, spin-orbit-length-pinning, exceptional-point-zero-mode, transparent-junction-pi-crossing, switching-jump-blind-region, false-poor-mans-majorana, coulomb-dominated-interferometer, diode-vortex-screening.
- Skipped, with some doubt: kondo-resonance. The edge peak sits near EF, but the entry's signature is a hybrid device with a superconducting contact, and the feature runs along the whole edge with no isolated spin site. A Kondo-type zero-bias feature from edge moments is not impossible.
- Skipped: protocol-parameter-sensitivity. There is no pass/fail protocol here.
- Checks: no family check list fits STM edge states. Only the practice checks (report-counts, report-ranges, report-processing) were walked.

## Outside lookalikes (library gaps)
- Trivial edge states from band bending or in-gap states. Source: Shi et al. 2018, arXiv 1807.09342 (abstract): "The edge conductivity shows no gap as a function of gate voltage, ruling out trivial conduction due to band bending or in-gap states, and is suppressed by magnetic field as expected." The tests are taken from that control and adapted to STS as edge LDOS across the whole gap.
- Set-point (feedback) contrast in constant-current STS. Source: Scarfato et al. 2024, arXiv 2406.03294 (abstract): "the tip-sample distance variations imposed by the feedback loop result in set-point-dependent STS images". The check comparing tip paths that climb and descend the step comes from Leis et al. 2022 (full text, p. 5).
- Supporting the adapted local-probe row: Leis et al. 2022, arXiv 2204.03753 (abstract): "This demonstrates that the detection of edge states in spectroscopy can be misleading with regard to the identification of a QSH phase."
- Suggested library additions: a family for STM/STS edge states of 2D topological insulator candidates, with checks for gap-spanning edge LDOS, set-point and topographic crosstalk at steps, a trivial reference edge, edge conduction or spin-resolved probes, and island-size dependence.

## Sources held out
- None. A text search of lookalikes.yaml for "Si2Te2", "HfTe2" and "2508.07351" found nothing. The library sources are Majorana, Josephson and anyon papers. I did not fetch every library source to confirm none cites this paper.

## Related-work verification
- 2204.03753 (Leis): arXiv API abstract plus full text (PDF downloaded to the work folder); abs page HTTP 200; ID, title and first author confirmed.
- 1807.09342 (Shi): arXiv API abstract; ID, title and first author confirmed.
- 2011.10096 (Maximenko): arXiv API abstract; abs page HTTP 200; confirmed.
- 2406.03294 (Scarfato): arXiv API abstract; abs page HTTP 200; confirmed.
- 2206.00919 (Huang, the authors' earlier paper): arXiv API abstract; abs page HTTP 200; confirmed. It is the paper under review's group, but a separate earlier paper, so it is not held out.
- Opened and not listed: 2206.04858 (theory, not relevant), 2301.00402 (bismuthene edge states, no clear lookalike), 1606.07402 (FT-STS set-point artifacts, superseded by Scarfato for this use).
- I could not find the authors' Ref. 30 (lateral heterojunction band bending) on arXiv. OpenAlex answered "Rate limit exceeded" with no key, so I did not use it.

## Things I was unsure of
- Whether Fig. 5(a) and 5(d) are different islands. I judged them different by shape and scale bar. If they are the same island, "A second device or dataset shown" drops to "no".
- The peak position in Fig. 5(b) (about -5 mV) and the crossover where the edge curve falls below the center curve (about +15 to +20 mV) are read from the rendered figure.
- Whether the Fig. 5(e) map is a grid of point spectra with feedback at each pixel. The caption gives Vstab = 0.2 V, which suggests so.
- The Ref. 35 description ("three stripe orientations") looks like leftover text, but I can't confirm that without the supplementary material.

## Skill issues
- No check family covers STM/STS edge states, so the checks section here is only the practice checks.
- Adapting an entry leaves the library's test text Majorana-specific. The skill doesn't say whether to reword the tests or keep them verbatim. I kept them verbatim in flags.json and explained the adaptation in the table.
- Step 7 says to write reports/<id>.md and use the title from the abstract page. This task forbade both (no .md writes, no abstract page), so I used the PDF title and put the report here.
- The template's "library of <n> known lookalikes in topological transport" reads oddly for an STM paper. I added a sentence to explain.
- The hold-out rule needs each library source checked for citations of the paper, which in principle means fetching all of them. The skill doesn't say whether a text search of the library is enough.
- The status rules don't say whether an outside lookalike the paper never mentions can be "Tested in part" when a figure happens to carry a test. I applied the rule as written (at least one test shown).
