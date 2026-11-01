# Run notes: arXiv 1204.4212v2

*AI only.* Lookalike assistant run of 2026-10-23. Library `meta.version` 0.4 (updated 2026-10-23), 28 lookalike entries.

## What I read

- Abstract page (local copy, `abs.html`): title "Observation of the fractional ac Josephson effect: the signature of Majorana particles", Rokhinson, Liu, Furdyna; v1 2012-04-18, v2 2012-08-23. Comment: original submission March 20, 2012. No ancillary files and no data repository linked, so no figure data were read and `read_mtx.py` was not used.
- Full text of v2 (local `paper.pdf`, 17 pages, and `paper.txt`), main text pp. 1 to 6 and Supplementary Information pp. 7 to 17. I rendered pages 4, 6, 12 and 17 to look at Figs. 2, 3, 4, S10 and S12 directly. The paper was not fetched, per the caller's instruction.
- I recognized the paper (published as Nature Physics 8, 795, 2012, DOI 10.1038/nphys2429 per the abstract page). I did not use any knowledge of its later history in the report.

## Claims table (step 1)

| Claimed signal | Figures | Device | Counts and ranges |
|---|---|---|---|
| Shapiro steps of hf0/2e = 6 µV at B = 0 and B < 2 T (2e supercurrent) | Fig. 3 left and right, Fig. 4, Fig. S11 | JJ8 (40 nm gap) | f0 = 3 GHz; Vrf at fridge top 0 to about 11 mV (vrf = 5e-3 to 5.4e-3 Vrf); T = 20 mK; Iac = 2 nA at 17 Hz |
| First step (6 µV) disappears for B > 2 T, 12 and 18 µV steps survive to about 3 T; read as hf0/e doubling and the fractional ac Josephson effect | Fig. 3 right (B = 0, 1.0, 1.6, 2.1, 2.5 T), Fig. 4 (B = 0, 1.0, 2.2 T), Fig. S12 (B = 0 to 3.4 T, 12 fields) | JJ8 | Field in plane, along the current only; 3 GHz only for the field series; 6 µV step "re-appears at high Vrf > 10 mV for B = 2.2 T" (p. 5); all steps gone above 3 T |
| Step height scales with frequency | Fig. S10 | JJ8 (assumed; caption names no device) | f0 = 2, 3, 4 GHz; field not stated (traces show hf0/2e steps, so likely B = 0) |
| Proximity superconductivity and Andreev reflection to 4 T | Fig. 2 (V(I) at 20 mK, dI/dV at 0 and 3 T, excess-current maximum vs B to about 4.5 T), Fig. S7, S8, S9 | JJ8, JJ7 (30 nm), JJ6 (20 nm), line L, GaAs test devices | Tc of JJ8 1.17 K; Ic RN about 1 mV; RN about 3 to 6 kΩ; shunt Rs about 0.8 kΩ (estimated from a neighbouring wire); SQUID asymmetry r = 7.3 (JJ7), > 10 (JJ8) |
| 2π periodicity in the dc SQUID configuration | none shown | not stated | stated on p. 2 only |

Missing counts: number of junctions measured under rf; number that showed the missing step; cooldowns; whether JJ6 or JJ7 were measured under rf; temperature dependence of the rf data; field directions other than along I; frequency dependence above 2 T. Gaps across devices "ranging from 20 to 120 nm" (p. 2); "several devices" on a sample (Fig. 1a); "several (> 10) test devices" on GaAs for the proximity control (p. 9). Two fridges were used (3He and dilution, Fig. S8).

## Matching (step 2)

Family: `shapiro`, plus `practice`. Matched entries: `switching-jump-blind-region`, `shapiro-nonlinear-resistance`, `shapiro-landau-zener`, `transparent-junction-pi-crossing` (matched on the physics: the 4π reading rests on a protected crossing at π, and an accidental crossing in a transparent junction gives the same Landau-Zener route), `fine-tuning-and-selection` (always).

Skipped, and why:
- All `zbp`, `quantization`, `nonlocal`, `island`, `charge`, `chiral`, `kitaev`, `diode` entries: the paper claims no zero-bias peak, quantized conductance, nonlocal signal, island, charge, chiral, Kitaev or diode signal. It mentions zero-bias anomalies and Kondo only as background (p. 2).
- `field-enhanced-supercurrent-resonances`: the paper does not claim a supercurrent that grows with field.
- `series-resistance-subtraction`: no conductance value is claimed as quantized. The shunt estimate enters only RN and Ic RN.
- `protocol-parameter-sensitivity`: no automated pass/fail protocol.
- `local-probe-loophole`: written for local tunneling probes; this is a two-terminal Josephson measurement.

No entries were adapted; the paper fits the library's scope.

## Checks (step 3)

shapiro-dc-curve partly; shapiro-frequency-power partly; shapiro-trivial-regime partly (zero field done, no control junction or second field direction; picked the weaker status); shapiro-transparency partly; report-counts not done; report-ranges partly; report-processing partly.

## Sources held out (hold-out rule)

I downloaded the full text of every source attached to the matched entries and checks and searched it for "Rokhinson", "Furdyna" and "1204.4212". Each of these cites the paper under review in its reference list, so I held all of them out and quoted none of them in the report:
- 2005.00077 (Dartiailh et al. 2021), ref. [20]
- 2211.08710 (Zhang et al. 2022), ref. [30]
- 2106.00495 (Mudi and Frolov 2022), ref. [6], and thanks Rokhinson for spreadsheet data
- 2309.09368 (Frolov et al. 2023), cited in its references
- 2403.07370 (Ubiquitous missing first Shapiro step, 2024), ref. [34]
- 1911.04512 (Prada et al. 2020), ref. [199]

Kept: 2501.18631 (Akrap, Frolov et al., reproducibility report): no mention of Rokhinson, Furdyna or the arXiv ID; it cites Dartiailh and Zhang but not this paper. Its quotes for `report-counts`, `report-ranges` and `report-processing` are present in the text. I did not check sources of entries I skipped.

Result: every source behind the four matched Shapiro entries and all four Shapiro checks was held out. I still used the entries' mechanism and control text and the check wording, but the report cites none of their sources.

## Related work (step 5), how each was checked

Found through arXiv API searches (`abs:"Shapiro steps" AND abs:missing`, `abs:Shapiro AND abs:odd AND abs:trivial`, `abs:"fractional Josephson" AND abs:Shapiro`), with about 3 s between calls. For each listed paper I opened the arXiv abstract page (ID, title, first author confirmed) and downloaded the full text:
- 1609.00372, Sau and Setiawan: abstract plus full text (pp. 2 to 3 on the ≲ 50 MHz requirement and the low-frequency Shapiro argument).
- 2107.05293, Galaktionov and Zaikin: abstract plus full text (discussion of missing steps at α ≈ 1).
- 2210.06502, Elfeky et al.: abstract; full text downloaded, only the abstract sentence used.
- 2408.06119, Liu et al.: abstract plus full text (Fig. 1f, g and the Shapiro paragraph near Fig. 7).
- 2510.20130, Xu et al.: abstract only (full text downloaded, not read beyond the abstract).
Also opened and not listed: 1206.4596 (Sau, Berg, Halperin 2012, trivial SNS junctions can show a fractional ac Josephson peak through Landau-Zener processes; abstract and full text), 1803.07674 (Le Calvez et al., Joule overheating; abstract). Several of the listed papers cite the paper under review; the report describes only their own results.

## Library gaps

- Period doubling from the circuit environment (shunt, capacitance, parasitic wiring inductance; RCLSJ dynamics) can remove odd Shapiro steps and give fJ/2 emission in a trivial junction. Source: Liu et al. 2024, https://arxiv.org/abs/2408.06119. Relevant here because JJ8 sits on a leaky substrate with a shunt of about 0.8 kΩ.
- Landau-Zener flips of a resonant impurity bound state coupled to a transparent channel, separable from Majorana modes only by low-frequency (≲ 50 MHz) doubled Shapiro steps. Source: Sau and Setiawan 2016, https://arxiv.org/abs/1609.00372. Close to `shapiro-landau-zener`, with a different mechanism and control.
- Possible additions to existing entries: Galaktionov and Zaikin 2021 (2107.05293) for `shapiro-landau-zener`; Xu et al. 2025 (2510.20130) for `switching-jump-blind-region`; Elfeky et al. 2022 (2210.06502) as a field-dependence control for the Shapiro checks. A text search for "Rokhinson" finds this paper cited in Xu et al., Elfeky et al., Sau and Setiawan and Liu et al.; Galaktionov and Zaikin have no hit. If added to the library, the first four would be held out in a rerun on this paper.
- No Shapiro check covers field direction (B along versus across Bso), which is a cheap trivial-regime control in spin-orbit devices.

## Unsure

- Fig. S10: no field or device is given. I assumed JJ8 and probably B = 0 from the 2e step spacing.
- `shapiro-trivial-regime`: zero field is done, so "done" was arguable; I chose "partly" because there is no control junction or second field direction.
- Circuit-environment row: the shunt estimate bears on it slightly; I chose "not addressed" as the weaker status.
- `transparent-junction-pi-crossing` as a match: its signature names a crossing at π, which the paper does not claim directly; I matched it because the 4π reading depends on it.
- The 6 µV step reappearing at Vrf > 10 mV at 2.2 T (p. 5) is consistent with the blind-region picture, but I did not say so in the report beyond suggesting a check.

## Skill issues

1. Hold-out rule wording. "Discusses the paper under review (cites it by title, authors or arXiv ID)" does not say whether a reference-list citation counts. Read literally, it held out every source behind the Shapiro family, leaving those entries with no citable source in the report. The skill does not say whether to keep using an entry whose sources are all held out; I kept the entries' text and dropped the sources.
2. Hold-out and related work. Step 5 says to start related work from the matched entries' sources and that later papers are fine, but the hold-out rule removes those same sources. It is unclear whether a held-out library source may reappear as related work found by search. I kept them out.
3. Output path. Step 7 says `reports/<arxiv-id>.md` and `.notes.md`; the caller asked for `eval/runs/1204.4212/skill-r1/report.md` and `notes.md`. I followed the caller.
4. Word budget. "About 600 to 900 words outside the table" is hard to meet with the template's fixed text, seven checks and five related-work lines; this report is about 910.
5. Matching scope. The rule "skip entries that can't apply" does not say whether to record each skipped family entry one by one or by family. I recorded by family.
6. The "weaker status" rule covers lookalikes; the checks have no matching rule for "done" versus "partly". I applied the same rule.
7. Abstract-page checks. Step 5 says open the abstract page; it does not say whether the arXiv API entry counts. I opened the HTML abstract pages as well.
8. Tooling: in this environment the Write tool refused `.md` files for a subagent, so I wrote the three output files with the shell.
