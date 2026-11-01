# Run notes: arXiv 2608.12897v1

- Skill: lookalike-assistant (SKILL.md, report-template.md), run 2026-10-23.
- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes plus the checks section.

## What I read

- The arXiv abstract page (local abs.html): title, ten authors, v1 submitted 13 Aug 2026, "15 pages, 3 figures", cond-mat.mes-hall. It lists no ancillary files.
- The full text (local paper.txt, 40 PDF pages): main text pp. 1 to 7, Methods pp. 8 to 12, data availability p. 13, references pp. 13 to 15, Supplementary Notes pp. 16 to 40. I read all of Supplementary Notes 1 and 3. I read Note 2 in part: notation, edge models, the reduction factor on p. 28, and the structure of the correlators. I did not check the long Keldysh derivations line by line.
- PDF pages 3 to 6 and 18 to 21 (Figs. 1 to 3 and S1 to S4), rendered as images to read the axis ranges and QPC reflection values.
- Page numbers are PDF page numbers. In the main text they match the printed footers; in the supplement they match the printed headers.
- Per the run instructions, I did not fetch the paper from arXiv in any form.

## What I couldn't open

- "Source data are provided with this paper" (p. 13) points to journal source data, which aren't on arXiv. There are no ancillary files. So I couldn't count devices or ranges beyond what the figures show. I did not use any data repository.

## Claims table (step 1)

| Claim | Figures | Data | Counts and ranges |
|---|---|---|---|
| QP charge e* = e/4 from shot noise at the injection QPC | Fig. 1b (data set 4); Figs. S1 to S4, panels b and f | all 4 datasets | bias up to about \|e*VS/2kBT\| = 5 to 6 (roughly 34 to 41 μV); T = 10 mK only |
| Charge Fano factor above 1, matching PH-Pf (Abelian braiding, Mc = e^{-iπ/4}) | Fig. 2b (data set 4, Device C second cooldown); Figs. S1 to S4, panels c and d | measured 1.54 at e*VS/2kBT = 4.6, against 1.49 (PH-Pf) and 0.94 (A-Pf), p. 12 | one QPC setting per dataset; R about 0.1 to 0.25, nearly flat in bias |
| Neutral Fano factor matching Mn = 0 (non-Abelian Ising) | Fig. 3b (data set 3, Device C first cooldown); Figs. S1 to S4, panels g and h | measured 2.37 at 5.0, against 2.33 (PH-Pf) and 2.0 (A-Pf), p. 12; A-Pf "less clearly distinguishable" (p. 17) | same ranges as above |
| Incoherent heating cannot explain the neutral noise | Supp. Note 3, Fig. S9 | data set 4 only, neutral configuration only | heating model about a factor of two below the data (p. 39); main text says "far smaller" (p. 7) |
| Combined conclusion: PH-Pf order, evidence for non-Abelian anyons | p. 7 | | |

Counts:

- Devices fabricated: not stated.
- Devices measured: 3. QPC gaps 1.2 μm (two devices) and 1.3 μm (one), QPC separation 1.4 μm in all (p. 8).
- Devices that showed the effect: 3, all of them (p. 7, p. 17).
- Cooldowns and datasets: 4 datasets. All three devices were first cooled without gate voltage; Device C was then cooled again with 0.3 V on a gate (p. 16). S1 is Device A, S2 Device B, S3 and S4 Device C.
- Magnetic field: not stated.
- Temperature: 10 mK only, and how it was determined isn't stated.
- Noise detection: 720 and 690 kHz.
- Density: 3.16e11 cm^-2.
- Not shown: no error bars, no temperature dependence, no field dependence, no plateau data.

## Matching, skipped and adapted entries

Scope note: this is a quantum Hall shot-noise experiment. The closest library family is `charge`, whose signature is fractional charge or anyons.

Adapted:

- Check `charge-regime-map` is written for Fabry-Perot interferometers. I used it as "map the signal across the field and gate plane and state the regime".
- Check `charge-control-regime`: "where the exotic state is not expected" became "integer filling, or a trivial channel, in the same two-QPC configuration".
- Lookalike `protocol-parameter-sensitivity`: I used it for the PH-Pf versus A-Pf discrimination. That is a parameter-free model comparison whose outcome depends on fixed inputs: T, the reduction factor Crd ≈ 0.47, the bias window, and binomial versus Poisson statistics. There is no automated protocol.

Skipped:

- `charge-trap-fractional-shift`: the signal is not a fractional shift of a Coulomb or interference pattern.
- `coulomb-dominated-interferometer`: there is no interferometer.
- All zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries: no superconductor, no tunneling spectroscopy, no Josephson junction.
- `local-probe-loophole`: written for Majorana local probes.

Included as required: `fine-tuning-and-selection`.

## Sources held out

None.

- Matched-entry sources were Frolov et al. 2309.09368 (2023), Akrap et al. 2501.18631 (v2, 25 Mar 2026) and Legg 2502.19560. The first two predate the paper.
- Legg's v2 is dated 21 Oct 2026, after the paper. I downloaded its v2 PDF and searched it for "2608.12897", "Alkalay", "Heiblum", "non-abelian anyon", "time-domain braiding" and "5/2". There were 0 hits, so I kept it.

## Related-work checks

For each paper I opened the arXiv abstract page and confirmed the title and first author, and read the abstract through the arXiv API. I checked abstracts only, not full texts.

- 2209.15461 (Lee, June-Young M.): abstract confirms ν = 1/3, a braiding phase of 2π/3, and no fitting parameters.
- 2401.06069 (Glidic, P.): abstract confirms interaction-induced fractional charges in the integer regime and a time-domain braiding origin of the signal.
- 2606.17753 (Ratnakar, Amulya; v1 16 Jun 2026, before the paper): abstract confirms inter-edge interactions, beam decomposition and the negative Fano factor at 2/5.
- 2403.17097 (Schiller, Noam): abstract confirms a heavily renormalized scaling dimension at ν = 1/3.
- 1906.05623 (Spånslätt, Christian): abstract confirms shot noise as an edge probe in the incoherent regime, in three universality classes.

All five predate the paper, so none discusses it. Search queries used: abs:"time-domain braiding", abs:"anyon collider", plus title searches.

## Library gaps

The library has no noise or time-domain braiding family. These lookalikes came from outside it:

1. Incoherent heating of upstream neutral modes, which produces excess noise at a downstream QPC (Spånslätt et al. 2019, 1906.05623).
2. Renormalized or nonuniversal scaling dimensions at QPCs, which shift the predicted Fano factors and the discrimination between topological orders (Schiller et al. 2024, 2403.17097).
3. Interaction-induced fractionalization between co-propagating channels, which gives braiding-like noise without the bulk topological order (Glidic et al. 2024, 2401.06069; theory in Ratnakar et al. 2026, 2606.17753).
4. Other candidates for a new family: a control check "same geometry at integer filling", and the electron-temperature calibration as an input to parameter-free fits.

## Unsure

- Calling `report-ranges` "not done" versus "partly": the bias range is shown, but field, temperature and QPC settings aren't. I picked the weaker status.
- The scaling-dimension row: I marked it "partly addressed" on the grounds that the paper discusses nonuniversal effects canceling and the RQPC(VS) data bear on it. A stricter reading would make it "not addressed", since the scaling dimension itself is never tested.
- The interaction lookalike: at ν = 5/2 the active ν = 1/2 channel runs alongside the outer integer channels. I judged this plausible from the abstracts of Glidic and Ratnakar, but did not work out its size.
- Recognition: I did not recognize the paper (it postdates my knowledge) and used no knowledge of its later history.

## Skill issues

- No family fits noise-based braiding experiments. The `charge` checks are written for interferometers and Coulomb dots, so step 3 forces done, partly or not done statuses onto adapted checks. flags.json has no "not applicable" status either.
- The skill doesn't say whether the papers cited for "not in library" lookalikes count toward the five related-work papers. I counted them.
- The "every quote verbatim" rule clashes with math-heavy PDF text extraction (doubled glyphs such as 𝑒𝑒). Only prose sentences can be quoted reliably, which biases which evidence gets cited.
- "The regime it claims" is unclear for model-comparison claims, where the result is a choice between two theories.
- Step 7 says to write files under reports/. This run's instructions overrode that, and the skill says nothing about this case.
- Step 6 says to ask the standard questions "unless the paper already answers them (then say where)". When the paper answers only part of a question, it isn't clear whether to keep the question. I kept it and added a pointer.
