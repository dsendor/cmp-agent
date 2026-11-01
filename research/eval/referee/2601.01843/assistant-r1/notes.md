# Run notes: 2601.01843v1

**Library version:** 0.5 (updated 2026-10-24), 28 lookalike entries.

**What I read**
- skill/SKILL.md, skill/report-template.md and library/lookalikes.yaml, read in full once at the start.
- The paper's extracted text, all 35 pages (main text, Methods, SI I to VI).
- The PDF, with pages 17 to 21 and 23 to 25 rendered to PNG to read Figs. 2, 3, 5 and S2. I also checked the page numbers of every quote with per-page pdftotext.
- I did not open the paper's arXiv abstract page because the task forbids it. The report title comes from the PDF title. The short title in the header drops "and order-parameter evolution".
- No ancillary data, and no data repository is linked ("all source data ... available within the paper", p. 12). read_mtx.py is not used.

**Could not open**
- OpenAlex answered "Rate limit exceeded" (shared daily budget), so I did no DOI checks.
- The arXiv website search returned empty result pages for several queries, so I used the arXiv API.
- The API gave thin results for some queries; I found Yoon et al. with ti:"point-contact" AND ti:UTe.

**I did not recognize the paper.** I have no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| ZBCP on (0 0 1) at ambient pressure, read as zero-energy ABS from a nodal gap with a pz component | Fig. 2c-f, S2, S7, Table S1 | S1, S2, S3 (one contact each, implied) | 3 samples. Temperature series for S1 only (0.3 to 3.0 K). S2 and S3 at 0.3 K only. Field 0 to 8 T along a, S1 only, 0.5 K (Fig. S2a). Bias ±4 mV. Contact resistances not given |
| Side dips above about 0.3 GPa, read as growing pz weight (∆z/∆x(y) from 0.57(5) to about 1.03 at 0.6 GPa) | Figs. 3b, 5c-d, S3b, S8 | S1 only | Pressures with PCS: 0, 0.2, 0.3, 0.6, 0.8, 1.0, 1.2, 1.4 GPa. T 0.3 to 3.6 K. No field under pressure |
| Double side dips at 1.0 to 1.2 GPa, fitted by a two-channel superposition (Eq. 2) | Figs. 3c, 5e, S3c, S9c | S1 | Origin "remains elusive" (p. 8). Multiple gaps or pressure inhomogeneity proposed |
| Nonmonotonic T dependence of ⟨∆z⟩/⟨∆x(y)⟩, minima near 1.6, 1.5 and 0.7 K at 0.6, 0.8 and 1.2 GPa, matching the SC2-SC3 line, read as a phase transition | Figs. 5a, 5f, S9 | S1 | Flat at p = 0 (Fig. S9d) |
| B2u or B3u favored from qualitative comparison with simulations; Au "cannot entirely exclude" (p. 9) | Figs. 4, S5, S6 | Model | Not a lookalike claim |

Resistivity phase diagram from S1 up to 1.8 GPa (Fig. 2b). The cell reaches "∼ 1.8 GPa", but PCS is shown only to 1.4 GPa.

**Missing counts:**
- contacts fabricated or attempted;
- cooldowns and pressure cycles;
- whether pressure was released and remeasured;
- contact resistances R_N;
- normalization procedure;
- fit uncertainty on ⟨∆z⟩/⟨∆x(y)⟩ beyond the error bars in Fig. 5.

**Noticed:**
- Table S1 lists S1 as ∆z = 1.18(7), ∆x(y) = 0.72(4). Fig. S7a and Fig. S2c give ∆x(y) = 1.18, ∆z = 0.72. The text ratio 0.57(5) matches the figure labels, so the Table S1 columns look swapped. I put this in question 8.
- At ambient pressure the ZBCP is visible at 2.3 and 2.5 K, above Tc0 = 2.1 K (Fig. 2c). The fitted gaps go to about zero near 2 K (Fig. S2c). I did not raise this.

## Entries adapted, skipped, added

**Adapted** (scope rule: bulk point-contact spectroscopy, not a hybrid device):
- **kondo-resonance**, adapted to a magnetic-impurity or Kondo zero-bias anomaly at the contact, as the paper itself raises with its refs. 45 and 46. The test "Even-odd occupancy of the dot" has no analogue here. I kept it in the test list as "no" and marked it n/a in the table cell.
- **series-resistance-subtraction**, adapted to normalization and series resistance setting the normalized peak height. The paper uses peak heights below 1.2, then 1.70 and 2.08, as evidence about the pz weight.
- **fine-tuning-and-selection**, applied to contacts and pressure runs.

**Checks:**
- zbp-dot-search adapted to magnetic or Kondo scattering.
- zbp-wide-ranges adapted to pressure, temperature and field.
- zbp-transparency adapted to contacts with different Z.
- zbp-both-ends and zbp-nonlocal-gap skipped: a single contact on a bulk crystal has no second end or nonlocal channel.
- Practice checks applied as written.

**Skipped entries:**
- abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, spin-orbit-length-pinning, exceptional-point-zero-mode, one-end-only and local-probe-loophole: they need a nanowire geometry, and the paper makes no Majorana claim.
- weak-antilocalization: I considered it as an analogue for disorder interference (reflectionless tunneling) in a diffusive contact. I skipped it because Pikulin et al. treat a class D nanowire and I had no opened source for the point-contact version.
- fine-tuned-plateau (no plateau claim), micromagnet-stray-field, full-shell-flux-andreev, trivial-andreev-band-gap-reopening, protocol-parameter-sensitivity, chiral, island, shapiro, supercurrent, charge, kitaev and diode entries: their signatures do not match.

**Added (not in library):**
- **Non-ballistic contact.** Source: Sheet et al., cond-mat/0311648, full text read. Tests come from its control: the Sharvin versus Maxwell regime from R_N, dips versus contact area, and dip voltage versus critical current. I counted the paper's own T and field heating check (p. 5, Fig. S2a) as a fourth, partial test. That is my judgment: it addresses heating of the ZBCP, and the side dips are not discussed under that heading.
- **Parallel contacts over regions with different gaps.** Source: Daghero and Gonnelli, 0912.4858, full text read. Quotes used:
  - p. 1: "parallel contacts are very likely to form between sample and tip ... unless the sample is highly inhomogeneous on a length scale comparable with the tip end";
  - p. 17: "A discontinuity in the temperature evolution of the gap suggested the existence of parallel contacts in clean and dirty regions of the sample".
  Status "Left open by the authors" rests on the p. 9 sentence on pressure inhomogeneity. Fig. S9c shows two-channel components versus T at 1.2 GPa, but the paper does not read them as an inhomogeneity test, so I marked that test "no" and named it in the suggested check.

## Sources held out

None. The library sources are about nanowires, junctions, interferometers and reproducibility practice, and none concerns UTe2 point contacts by title. I did not open library sources in this run.

## Related-work checks

All five abstract pages were opened at arxiv.org/abs, with ID, title and first author confirmed from citation meta tags.

| Paper | Checked against |
|---|---|
| 2403.00933 Yoon, Hyeok | abstract (API and abs page) |
| 2501.16636 Gu, Qiangqiang | abstract |
| cond-mat/0311648 Sheet, G. | full text (PDF) |
| 0912.4858 Daghero, D. | full text (PDF, Secs. I, III, VI, VII) |
| 1111.5805 Kirzhner, T. | abstract |

All five predate the paper under review. I avoided 2604.04883 (Zhu et al. 2026), which is later and could discuss this paper.

## Library gaps

The library has no point-contact spectroscopy family. Candidates:
- non-ballistic (thermal or diffusive) contacts producing dips and zero-bias enhancement (Sheet 2004);
- parallel contacts and inhomogeneity (Daghero 2010);
- a proximity or degraded surface layer producing dips between ∆prox and ∆bulk (Daghero Sec. VI A, citing Strijkers et al., not opened);
- spreading resistance (Daghero Sec. VI D);
- magnetic-impurity zero-bias anomalies in metallic contacts;
- BTK fit degeneracy among Z, Γ and the gap components.

## Unsure

- Whether the T and field data (Fig. S2a) count as an equivalent test for the non-ballistic row. I marked it part.
- Whether "Left open" is right for the parallel-contacts row, since the authors fold inhomogeneity into their Eq. 2 model.
- Fig. S2a shows no visible splitting up to 8 T at 0.5 K. I read that from the rendered figure, without data.

## Skill issues

- Checks have no "not applicable" status. I left out zbp-both-ends and zbp-nonlocal-gap from flags.json and the report, and said so here.
- When adapting an entry, the skill does not say how to record a test with no analogue (the dot occupancy test). I kept it as "no" and flagged n/a.
- For rows not in the library, the skill says to take tests from the cited paper's control. It does not say whether the paper's own different check can count as an equivalent test.
- Step 7 says to use the title on the arXiv abstract page. This task forbade opening it, so I used the PDF title.
- Step 7 says to write reports/<id>.md. This environment refuses .md writes, so the report is returned inline per the task.
- "Left open by the authors" needs a sentence saying the explanation is possible. It is unclear when the authors adopt that explanation into their own model.
- The scope rule covers adapting entries, but not adding a whole missing family (point contacts). I added two rows marked "not in library".
