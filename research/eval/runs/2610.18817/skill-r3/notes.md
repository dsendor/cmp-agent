# Run notes: arXiv 2610.18817v1

AI only. Lookalike library version 0.4 (meta.updated 2026-10-23), 28 lookalike entries, 18 checks.

## What I read
- Skill: SKILL.md, report-template.md, library lookalikes.yaml (all entries and the `checks` section), each read once at the start.
- Paper: the local copies the caller supplied. These were abs.html (title, authors, date 2026-10-13, v1, abstract), paper.pdf (24 pages, re-extracted with pdftotext; main text pp. 1-8, Methods pp. 8-12, references p. 13, Extended Data Figs. 1-11 and Tables I-III pp. 14-24) and paper.txt (the layout extraction, used to read Table I). Per the caller's instructions I did not fetch the paper from arXiv. Supplementary material is the Extended Data in the PDF, and I read all captions.
- Figure data and code: none. The abstract page lists no ancillary files, and the paper has no data or code availability statement. I did not run read_mtx.py. No data repository was reached or used.
- Every quote in the report was checked by string match against the extracted PDF text (whitespace-normalized). Page numbers are PDF pages.
- Small mismatch: the arXiv abstract page ends "an anyon binding energy as large as the charging energy", while the PDF abstract says "at least as large". I quoted only the PDF.
- I did not recognize the paper. It is dated after my knowledge cutoff, and I used no outside knowledge of its later history.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Whole-electron Coulomb blockade backscattering at ν = 1, EC ≈ 2 meV | Fig. 1e-g, Ext. Data Fig. 2 | the one device | B = 5 T; Vdot [-2.5, -0.5] V; VDC to about ±2 mV |
| Spin blockade and full depletion at ν = 1; quasielectrons seen via magnon-assisted tunneling at abs(VDC) ≳ 1 mV | Fig. 2 | same | B = 5 T; DMRG comparison Fig. 2g-h |
| e/3 tunneling charge from a gate period about 1/3 of that at ν = 1 (δ 80-100 mV versus 250-300 mV) | Fig. 1h-j, Ext. Data Figs. 3, 7 | same | B = 5, 8.97, 13.4, 13.5 T; the 8.97 and 13.4 T rows are lock-in (first cooldown), with other VT, Vqpc, Vedge; Table I lists Fig. 1h as νbulk = 2/5, νdot = 1/3, while the text says 1/3 |
| Nqp = 0 at ν = 1/3 fixed by an electrostatic calibration (ν = 1 at 4.5 T, then the field tripled; quantum capacitance shift under one quasiparticle) | Fig. 3b, Ext. Data Fig. 6 | same | 4.5 and 13.5 T; ν = 1/3 at VT = 49 ± 1 mV, ν = 1 at VT = 50 ± 2.5 mV |
| Single anyon dot; irregular addition energies for Nqp = 1-5 matched to DMRG; few-quasihole regime not reached in weak backscattering | Fig. 3 | same | Vdot [-1.03, 3.97] V, 13.5 T |
| Regular spectra (1/3 quasiholes, 2/3 quasiparticles) versus irregular ones (1/3 quasiparticles, 2/3 quasiholes) at abs(Nqp) about 10-20 | Fig. 4a-d, Ext. Data Figs. 9-11 | same | gate sweeps of VT, Vedge, Vqpc, D; Ext. Data Fig. 10 says the even-odd locations "depend strongly on the gate voltages" |
| Anyon binding: a missing charge sector as VT is lowered, 2e/3 periodicity, EB > EC | Fig. 4e-g | same | VT from 0.050 to 0.040 V; Vdot [3.785, 4.5] V; one window, chosen as "particularly pronounced" |
| Charge noise Sq ≈ 1e-3 e/√Hz at 10 mHz | Ext. Data Fig. 5, Table III | same | ν = 1, 5 T; 15.5 h trace; three transitions |

Counts:
- Devices fabricated: not stated ("M.V. fabricated the devices", plural).
- Devices measured: one ("The device").
- Devices showing the effect: one.
- Cooldowns: two (the first with lock-in, the second DC).
- Datasets: each main panel's settings are in Table I. How many VT windows showed a missing sector is not stated.
- Temperature: base about 20 mK; electron temperature saturates near 110 mK (Ext. Data Fig. 3k); Ext. Data Fig. 3 runs from 25 to 500 mK.
- Field: out-of-plane only.
- Missing counts: devices fabricated, full ranges explored, number of repeated sweeps, number of windows searched for Fig. 4e.

Minor inconsistency: Methods gives lock-in frequencies of 13.333 or 17.777 Hz, while Table I lists 13.77 and 17.77 Hz.

## Matching, skipped and adapted entries
- Family: charge, plus practice.
- Matched:
  - charge-trap-fractional-shift.
  - fine-tuning-and-selection (always included).
  - island-states-coulomb-spacing, adapted. The signature (even-odd Coulomb spacing read as an exotic state) matches Fig. 4 on physics. I re-read the lookalike as ordinary orbital shell structure of the dot and the control as the missing-sector test plus resolution.
- Adapted checks: charge-regime-map is written for interferometers (Aharonov-Bohm versus Coulomb-dominated). For a Coulomb blockade dot I read it as "map field and gate, and use both periods to get the charge".
- Skipped:
  - coulomb-dominated-interferometer: the paper claims Coulomb blockade in a dot, so there is no Aharonov-Bohm claim to mimic. Its check was still walked.
  - protocol-parameter-sensitivity: no pass/fail protocol.
  - series-resistance-subtraction: the claims rest on gate periods, and V is measured directly across the device.
  - local-probe-loophole: Majorana-specific.
  - All zbp, quantization, nonlocal, shapiro, supercurrent, chiral, kitaev and diode entries: no superconductor and none of those signatures.
- Scope sentence added under "What this is", as the skill requires for adapted entries.

## Sources held out
None. The library sources I relied on (2309.09368 v1 2023; 2504.05221 is not a library source; 1010.4598; 2101.11456; 2501.18631 v2 25 Mar 2026; 1911.04512; 2203.07829) all predate the paper (13 Oct 2026), so none can discuss it. I confirmed the 2309.09368 and 2501.18631 dates on their abstract pages.

## Related work: how each was checked
All were opened on their arXiv abstract pages, where I confirmed the ID, title and first author and checked the one-line description against the abstract. I read no full texts.
- 2504.05221: Byard, Gomanko, ..., Frolov.
- 2502.00124: Liang, Nakamura, Gardner, ...
- 2005.12723: Röösli, Hug, Nicolí, ...
- 1201.1600: Kou, Marcus, Pfeiffer, ...
- 1608.05721: Hamo, Benyamini, Shapir, ...

I also opened 2309.09368 and 2501.18631 for hold-out dates. The arXiv API was used with 3 s waits and never returned "Rate exceeded"; OpenAlex was used once (the Martin et al. 2004 DOI, not listed).

## Outside lookalike
"Capacitive coupling between nested edge modes or compressible regions", sourced to Liang et al. 2502.00124: a halved period read as pairing comes from capacitive edge coupling. Röösli 2005.12723 supports the two-region dot picture. I marked it partly addressed because the paper discusses the nested 2/3-1/3 edge scenario but frames it as pairing. Judged against Liang's control: the charge determined in operando from field and gate periods.

## Library gaps
- No entry for period-based charge claims that assume a lever arm and capacitance independent of filling. The paper flags this itself (p. 3), and field-and-gate period methods (Kou 1201.1600, Röösli 2005.12723) address it. I found no source that shows the failure, so I added no row.
- No entry for capacitive edge-edge or bulk-edge coupling mimicking pairing (Liang 2502.00124).
- No entry for an unresolved or weakly coupled charge sector read as a missing sector.
- The charge-family checks are written for interferometers; a dot or Coulomb blockade version would help.
- Byard et al. 2504.05221 would be a direct source for charge-trap-fractional-shift in dots.

## Unsure
- Every check and lookalike landed on Partly. In each case the paper does part of the control (ν = 1 controls, gate maps, one VT window). Where unsure I chose the weaker status:
  - island adapted: the sector could be unresolved, which Ext. Data Fig. 10 notes for the dip finder.
  - charge trap: localization was done at ν = 1 only.
- Questions 7 and 8 rest on Table I and the Fig. 1i caption as extracted. The "3e" could be an extraction or typesetting issue.
- I inferred from Methods (first cooldown lock-in, second DC) that the lock-in rows of Table I are from the first cooldown.

## Skill issues
- Step 7 says to write reports/<id>.md and .notes.md; the caller overrode this.
- The Input section says to fetch the arXiv abs and pdf; the caller forbade it, and I used the local files.
- It is unclear whether to list a check that addresses only a skipped lookalike (charge-regime-map addresses only coulomb-dominated-interferometer). I listed it, adapted.
- It is unclear whether the 600-900 word target counts the checks list, questions and related work. Mine is about 925 words outside the table, headings included.
- The template's "<short title>" fits poorly when the arXiv title is already short; I used the full title.
- The Scope rule covers "a different kind of measurement" but gives no guidance when a family's checks are written for a different device type (interferometer versus dot).
