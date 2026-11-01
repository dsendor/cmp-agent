# Run notes: arXiv 1809.05513v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalikes, checks for zbp, shapiro, kitaev, charge, practice).
- Skill and template: cmp-assistant/skill/SKILL.md, report-template.md. read_mtx.py not used (no figure data).

## What I read
- Local abs.html (title, authors, abstract; only v1 listed) and paper.txt, all 12 pages: main text pp. 1 to 6, supplement pp. 7 to 12. I confirmed page numbers with pdftotext -layout on paper.pdf and rendered pp. 2, 3, 4 and 8 to look at Fig. 2, Fig. 3, Fig. 4, Fig. S2 and Fig. S3.
- No data repository is linked and there are no ancillary files, so no counting from data.
- I did not fetch the paper itself.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Destructive Little-Parks lobes in the shell (context) | Fig. 1C, 1D, S1 | device 1 (4-probe) | B -0.3 to 0.3 T axial; T 20 mK to about 1.3 K; Is ±80 µA |
| Hard gap in zeroth lobe, discrete ZBP throughout first lobe, no ZBP in second lobe | Fig. 2B to 2F, S2, S3, S9A to C | device 1, one end (Al removed at end, back-gate barrier) | B -0.3 to 0.3 T axial only; VBG -1.2 to -0.8 V; V ±0.3 mV; 20 mK only; ZBP height about 0.15 e^2/h (Fig. 2F) |
| ZBP splits into a dip as the barrier opens | Fig. S3B | device 1 | VBG -1.10 to -0.80 V, six traces |
| 2e CB peaks in zeroth lobe, even-odd near-1e in first lobe | Fig. 3, S4 to S8 | device 2, six islands 210, 300, 420, 620, 810, 970 nm on one wire | B ±0.4 T (210, 300 nm), ±0.3 T (others); VG ranges per island; diamonds at 0 and 110 mT |
| Exponential length dependence of even-odd energy, ξ = 180 nm at 110 mT and 230 nm at 140 mT | Fig. 4F, S9D, Table S1 | device 2 | six lengths; "several different gate configurations for each island" (p. 9), count not given |
| Counts | p. 2 | | "Two device geometries, measured in three devices each, showed similar results. Data from two devices are presented"; cooldowns not stated; how many showed each effect not stated; field angle not varied |

## Entries matched, skipped, adapted
- Matched: full-shell-flux-andreev, abs-quantum-dot, spin-orbit-length-pinning, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, one-end-only, local-probe-loophole, kondo-resonance, exceptional-point-zero-mode, weak-antilocalization, island-states-coulomb-spacing, fine-tuning-and-selection.
- Skipped: fine-tuned-plateau and series-resistance-subtraction (no quantization claim; peak about 0.15 e^2/h; the series-resistance check was still walked as zbp-raw-conductance); trivial-andreev-band-gap-reopening (no nonlocal data or protocol; the gap closing shown is the Little-Parks destructive regime); protocol-parameter-sensitivity (no pass/fail protocol); micromagnet-stray-field (no magnets, ZBP at finite field); all shapiro, supercurrent, charge, chiral, kitaev and diode entries (signals not claimed; the shell switching current is used only for Little-Parks characterization).
- Adapted: none. The paper is within scope.
- Checks walked: the zbp family (it includes hybrid islands) and practice. The island family has no checks in the library.

## Sources held out (they cite the paper under review, as its Science 367, eaav3392 (2020) version)
I grepped the full text of each source for "Vaitiek", "1809.05513", "Flux-induced" and "aav3392":
- 2309.09368 (Frolov et al.): cites "Flux-induced topological superconductivity in full-shell nanowires. Science. 367, eaav3392 (2020)". Held out.
- 1911.04512 (Prada et al.): cites Science 367 (2020). Held out.
- 2207.02472 (Microsoft TGP): cites "Flux-induced topological superconductivity in full-shell". Held out.
- 2008.02348 (Valentini et al. 2021): cites ref. 40, Science 367, eaav3392. Held out.
- 2203.07829 (Valentini et al. 2022): cites ref. 12, Flux-induced topological superconductivity. Held out.
- Kept, since they cite other Vaitiekėnas or Deng papers only or none: 1705.02035, 1207.3067, 1806.02801 (v3), 1711.06256, 1910.11413, 2101.11456, 1902.02773, 1207.1259, 1206.6687, 2004.08583, 2501.18631.
- As a result, every source of full-shell-flux-andreev, island-states-coulomb-spacing, spin-orbit-length-pinning, exceptional-point-zero-mode and local-probe-loophole is held out. I kept those entries (the rule names sources, not entries) and cited none of their sources.

## Related work checks
- I read the abstracts of 1603.03217, 1702.04357, 1705.02035, 1806.02801 and 1902.02773 through the arXiv API (export.arxiv.org) and confirmed the ID, title and first author. For 1705.02035, 1806.02801, 1902.02773 and 1702.04357 I also downloaded the full PDFs to check that none cites the paper under review. 1603.03217 predates it and is the paper's own ref. [8].
- 1811.06136 (Cao et al.) came up in a search and was not used.
- I left Valentini et al. 2021 (2008.02348) out of related work because it is a held-out source that addresses this paper.

## Judgment calls
- I counted the island length dependence (device 2) as "part" for the end-to-end correlation and overlap tests (quasi-majorana, disorder, local-probe-loophole). It bears on end-to-end hybridization in this wire type but does not measure the two ends of device 1. For the literal tests ("both ends compared", "nonlocal conductance") I marked "no", which is why one-end-only is "argued, not tested".
- I marked zbp-transparency done on Fig. 2E and S3B, even though the global back gate tunes both the barrier and the wire.
- I marked zbp-raw-conductance partly: the line resistance value is given, but neither the subtraction nor the raw data are.
- For Kondo, I counted the field series in Fig. 2B as "part" for Zeeman splitting. The paper does not discuss Kondo.

## Recognition
- I recognize this paper (published as Science 367, eaav3392, 2020) and know of later work on full-shell zero-bias peaks (Valentini et al. 2021). I did not use that history in the report. The full-shell-flux-andreev entry itself was written from that later work.

## Library gaps
- No entry covers trivial even-odd spacing that falls exponentially with island length. The only island test is open-regime tunneling on the same island. Chiu et al. 1702.04357 suggests Andreev bound states and multiband effects as a second test.

## Skill issues
- The hold-out rule skips sources but says nothing about entries whose every source is held out. Here five entries were left with no citable source, and one (full-shell-flux-andreev) was written from a paper that addresses this one. So the hold-out does not keep the run blind for that entry. The skill should say whether to keep or drop such entries.
- The rule on "equivalent tests" does not say whether evidence from a different device in the same paper (islands vs the tunneling wire) counts as "part" for a test on the other claim. I chose "part" for correlation and overlap tests and "no" for literal both-end tests.
- The island family has no `checks`, while the zbp checks say they include hybrid islands. It is unclear whether island-only papers should walk the zbp checks.
- The skill's step 7 names reports/<id>.md and reports/<id>.notes.md. This run overrides that by putting both in the reply.
