# Run notes: arXiv 2510.09044v1

*AI only.* Lookalike assistant run, 2026-10-25. Library `meta.version` 0.5 (updated 2026-10-24), 28 lookalike entries, checks for families zbp, shapiro, kitaev, charge, practice.

## What I read
- Skill: cmp-assistant/skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (whole file, including every entry's `tests` and the `checks` section).
- Paper: the supplied v1 PDF (9 pages, main text, Methods and references) and its extracted text. I rendered PDF pages 2 to 5 and read Figs. 1 to 4 from the images. Per the task, I did not open the arXiv abstract page or any other version of the paper; the title comes from the PDF.
- The Supplementary Materials (Tables S1, S2; Figs. S1 to S7; the r0 extraction methods, ref. [25]) are not in the v1 PDF. I could not read them.
- Data: "available from the corresponding author upon reasonable request" (p. 6). No repository and no ancillary figure data, so read_mtx.py was not used.
- By mistake I printed the first five lines of scripts/check.py (its docstring) while counting library entries. I used nothing from it.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| C1. Gate power suppresses Meissner screening near the gate apex | Fig. 2c (D2b, 0.45 K, P = 0.08 to 1.74 µW); Fig. 4b to e (D3, 2 to 5 µW); sims Fig. 2d | D2b, D3 | B0 ~ 1 mT out of plane only; scan height ~100 nm |
| C2. r0 depends on P only, independent of bath T, gate polarity and VG; excludes Joule heating, vacuum electron injection, direct field effect | Fig. 3a,b | D3 gate G1, one cooldown; D2a, D2b in Figs. S3, S4 (not in PDF) | T = 0.4 and 5.6 K; both polarities; P from 0 to about 4.5 µW; \|VG\| about 4 to 11 V in Fig. 3b |
| C3. Hot-spot diffusion model fits r0(P), rd ≈ 0.57 µm, Pd ≈ 0.95 µW (D3); rd ≈ 0.65 µm, Pd ≈ 0.36 µW (D2b) | Fig. 3a, Eq. 3; Fig. S4 | D3, D2b | two fit parameters |
| C4. Gate geometry dependence consistent with point-like injection; quench with island floating | Fig. 4b to e, Fig. S6 | D3, gates G1 to G5 | one power per panel (5 µW in b, 2 µW in c to e) |
| C5. Vortices leave the island at the GCS onset; escape power depends on T | Fig. 2c, Fig. S7 | D2b and others | 0.45 K, 3.5 K, 5.8 K |

Counts: three geometries in separate fabrication runs (D1 nanowire, D2a/D2b square islands, D3 large island); four named devices. Devices fabricated per run: not stated. Devices imaged: D2a, D2b, D3 shown; D1 imaging not stated (D1 gives Table S1 properties). "All our devices" reproduce the suppression at the same P (p. 2). Cooldowns: one for Fig. 3a; "several" for D2a/D2b. Temperatures 0.4 to 5.8 K. Leakage onset |VG| ~ 7 to 16 V, drifting over time (Fig. 1c, Fig. S2). Several NV probes. Missing: number fabricated, number imaged, number of cooldowns, field values other than ~1 mT, reason for shown ranges.

## Entries matched, adapted, skipped
- Scope: the paper is GCS imaging by NV magnetometry, not topological transport. No library `signature` describes the signal. Used `fine-tuning-and-selection` (applies to every signature) and the `practice` checks (report-counts, report-ranges, report-processing).
- Skipped all other 27 entries: their signatures (zero-bias peaks, quantized conductance, nonlocal gap, island Coulomb peaks, Shapiro steps, triplet supercurrent, fractional charge, chiral plateau, Kitaev chains, diode effect, TGP sensitivity, local-probe loophole) do not describe a gate-induced suppression of Meissner screening. `diode-vortex-screening` involves Meissner screening but its signature is a nonreciprocal critical current, absent here. Skipped the zbp, shapiro, kitaev and charge check sequences for the same reason.
- Adapted: none of the library entries; the competing mechanisms are outside rows.
- Outside rows (library gaps), each from a paper I opened:
  1. Joule (thermal) heating by leakage power. Source Golokolenov et al., arXiv 2009.00683 (full text read). Tests from its control: bath-temperature dependence of the gate response (its Fig. 4) and an estimate of the heating from the dissipated power (its p. 5, "sufficient to raise the effective temperature to 1 K and above"). Paper: bath temperature shown for D3 G1 (all); no heating estimate (no). The suggested heater control comes from Ritter et al. 2106.01816.
  2. Field-emitted electrons through vacuum. Source Alegria et al., arXiv 2005.00584 (full text read; Fowler-Nordheim analysis, Eq. 5). Polarity test from Fowler-Nordheim physics and Ritter et al. 2005.00462 (asymmetry on SiO2). Paper: polarity shown (all); leakage only described as "increased exponentially" (p. 6), no Fowler-Nordheim fit (no). Not marked ruled out because with the island as cathode the emitted electrons land on the gate apex 80 nm away, so polarity symmetry alone does not separate the mechanism.
  3. Direct electric-field effect. Source De Simoni et al., arXiv 1710.02400 (abstract read). Tests taken from the separating control in Ritter et al., arXiv 2106.01816 (full text read: remote gates where field and current are separated). Paper: Fig. 3b plots r0 against |VG| over all powers, and within each temperature set r0 rises with |VG| (part); Fig. 4e floating island, one gate pair, field at the island not quantified, and the paper uses it for the injection-distance argument (part).
- Status reasoning: each outside row has one test shown for all the D3 G1 evidence and one not shown, so "Tested in part". No row met the single-test bar for "Ruled out for the claim".

## Sources held out
- None of the library sources I relied on discuss this paper; all are about topological transport and most predate it. I did not open the library sources themselves (I used only their quotes in the yaml), so this is not verified against their full text. No library source was used in the report except via the `fine-tuning-and-selection` entry.

## Related work: how each link was checked
- 2009.00683 Golokolenov et al.: arXiv API abstract (ID, title, first author Ilia Golokolenov) and full text v1 (bath-temperature dependence, Fowler-Nordheim fit).
- 2005.00584 Alegria et al.: arXiv API abstract (first author Loren D. Alegria) and full text v1 (field emission, below 0.1 nA switching, Fowler-Nordheim model).
- 2005.00462 Ritter et al.: arXiv API abstract (first author M. F. Ritter) and full text v1 (TiN, Ti, Nb; polarity asymmetry on SiO2; decay length about 1.2 µm).
- 2106.01816 Ritter et al.: arXiv API abstract (first author M. F. Ritter) and full text v1 (remote gates, trench, resistive heater comparison).
- 1710.02400 De Simoni et al.: arXiv API abstract only (first author G. De Simoni; bipolar suppression in Ti and Al, field-effect interpretation).
- Also confirmed but not listed: 2302.13734 Ruf et al. review (abstract), which is ref. [6] of the paper.
- Years in the report are arXiv submission years.
- Calls to the arXiv API were spaced about 3 seconds apart; no email address was sent.

## Recognition
I did not recognize this paper or know any later history of it.

## Things I was unsure of
- Whether 0.4 K versus 5.6 K is a strong enough temperature test against heating: with a thermal conductance that rises steeply with temperature, a thermal model might predict only a modest r0 shift. The paper gives no Tc in the main text (Table S1 not available), so I could not estimate it. Hence the question.
- In Fig. 3a, at the highest powers, the 5.6 K points sit slightly below the 0.4 K points, within error bars. I did not raise it as a question.
- Fig. 3b "weak correlation": my reading that r0 rises steeply with |VG| within each temperature set is from the rendered figure.
- Report length is about 930 words outside the table, above the 600 to 900 aim, mostly because of the eight questions.

## Skill issues
- Scope: the scope rule says "adapt the matching entries", but for a paper outside topological transport no entry matches except `fine-tuning-and-selection`. The skill doesn't say whether outside rows should then carry the main analysis, or how many to add.
- Inverted framing: here the claimed mechanism (non-equilibrium particle hot spot) is itself the conventional reading, and one competing explanation (a direct field effect) is the exotic one. The "lookalike" frame, "ordinary effects that can produce the same signal", fits this case poorly. I treated the competing mechanisms the paper argues against as outside rows.
- Outside-row source and control: step 5 says to cite a paper that shows the explanation and take tests "from the control that paper describes". For the field-effect row, the paper that proposes the explanation (De Simoni) describes no separating control; the control comes from a different paper (Ritter 2106.01816). The skill doesn't cover this; I cited De Simoni as source and named Ritter in the notes.
- Supplementary material referenced but absent: "judge the evidence the paper presents" is unclear when the main text leans on SI figures (Figs. S3, S4) that are not in the PDF. I marked tests that rely on them "part".
- Title: step 7 says to use the arXiv abstract page title, but the task forbade opening it; I used the PDF title.
- Output location: step 7 says to write reports/<id>.md and .notes.md; this run returned them in the reply, as the task asked.
- The template's check line format "<check> : Done" uses a space before the colon; I kept it as written.
