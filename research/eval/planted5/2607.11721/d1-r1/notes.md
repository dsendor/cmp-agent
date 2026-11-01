# Run notes: arXiv 2607.11721v1

Library version: 0.5 (meta.updated 2026-10-24). 28 lookalike entries; checks for zbp, shapiro, kitaev, charge, practice.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (every entry, its tests and the checks section). Read once at the start.
- The paper: the extracted text only (main text pp. 1-16, SI pp. 17-51), as the run prompt said. I did not fetch the abstract page or PDF, so I took the title from p. 1 of the text: "High-field Josephson effect enabled by a moiré Hofstadter spectrum". Version v1 is from the arXiv stamp on p. 1 ("arXiv:2607.11721v1 [cond-mat.mes-hall] 13 Jul 2026").
- I could not view the figures. Every figure detail comes from captions and text.
- No ancillary files and no linked data repository. Data are "available from the corresponding author upon reasonable request" (p. 16). I did not use read_mtx.py.
- I did not recognize the paper. It postdates my knowledge.

## Claims table (step 1)
| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| C1. Ballistic, phase-coherent Andreev transport in the Dirac band and the moiré minibands: Fabry-Pérot oscillations in Ic and RN, a Fraunhofer pattern, and the long-ballistic Ic(T) | Fig. 1c-g; S5-S10, S12 | GH1 (main), GH2 (S12, S9d-f), non-aligned graphene junction (S15) | FP at 2 K (Ic) and 10 K (RN, normal-state bias maps S7); Fraunhofer at n/ns ∼ 1.6 (GH1) and 1.5 (GH2) near zero field; Ic(T) in GH1-2, δE vs 1/L over GH1-4 at n/ns ∼ 1.3; IcRN at n/ns ∼ 1.2 |
| C2. Zero-resistance pockets with oscillating Ic up to ∼6 T in the electron minibands (n/ns > 1), beyond 2rc = L | Fig. 2a-c, e; S10, S11, S13 | GH1 to ∼6 T; GH2 to 5 T | Ic up to 48 ± 2 nA (2.5 T trace); irregular periods 2.3-3.4 mT; interference at n/ns ∼ 1.8 around 4.3 T (Fig. 2c) and at 2.5, 3.5, 4.5 T (S11, two consecutive sweeps each); gate cut at 4.1 T (Fig. 2e); GH2 at n/ns = 1.6, 3.5 T |
| C3. The supercurrent does not come from quantum Hall chiral edge states | Fig. S14; text p. 5, p. 7 | GH1, GH2 | Landau fans at a dc bias of 200 nA |
| C4. Superconducting regions coincide with dispersive Hofstadter bands of high ⟨v²⟩ | Fig. 3a-e; S17-S22 | GH1 (Fig. 3), GH2 (S18-S20) | 205 rational fluxes from p/q = 1/3 to 1/20 (8.54 T to 1.28 T for GH1); zero-bias 1/R used as the superconductivity proxy; 1/R cutoff 20 mS in S18 |

Counts: devices fabricated, not stated. Moiré devices measured: 4 (GH1-4, Table S1), plus 1 non-aligned junction (Sec. H). Devices showing high-field superconductivity: 2 of 4 (GH1, GH2); GH3 and GH4 were set aside "as their much longer lengths lead to very low critical currents" (SI p. 33). Cooldowns: not stated. Datasets: not stated. The main text says "reproduced across multiple additional devices" (p. 3), but the SI shows the high-field result only in GH2.
Ranges: gate up to ±80 V (n/ns ∼ ±2.7 for low twist), ±70 V in Fig. S2; GH2 is limited by gate leakage near 80 V. Field up to 8 T (the magnet limit); calculations are cut off at 8 T. Temperatures 100 mK, 2 K and 10 K, plus Ic(T) series. Excitation 1 nA ac at 17.777 Hz; dc current step 2 nA. Field sweep about 0.2 mT/s, with three back-and-forth cycles before each interference pattern. Missing: high-field data for the hole minibands (n/ns < -1); the reason for the Fig. 2c settings; the temperature dependence of the high-field pockets.

## Entries matched, adapted, skipped
- fine-tuning-and-selection: used as written (it applies to every paper).
- field-enhanced-supercurrent-resonances: adapted. The library signature is "supercurrent that grows with field, read as triplet pairing". Here it is a supercurrent that survives to unusually high field, read as Hofstadter-band transport. I kept the mechanism (finite-bias features moving the extracted switching current, made relevant by the 50%-of-RN Ic criterion) and the entry's two tests.
- series-resistance-subtraction: adapted. The library signature is conductance near 2e^2/h. Here the extracted quantities are vanishing R and the 1/R map after subtracting 3447 Ω.
- Skipped, because the signal type is absent: every zbp entry (no tunneling spectroscopy, no zero-bias peak); fine-tuned-plateau (no quantization claim); one-end-only, trivial-andreev-band-gap-reopening, local-probe-loophole (no Majorana or nonlocal claim); island-states-coulomb-spacing; all shapiro entries, transparent-junction-pi-crossing and switching-jump-blind-region (no microwave irradiation, no phase spectroscopy); charge-trap-fractional-shift and coulomb-dominated-interferometer (no fractional-charge claim); chiral-plateau-superconductor-short (no QAH film); false-poor-mans-majorana; diode-vortex-screening (no direction comparison); micromagnet-stray-field; full-shell-flux-andreev. protocol-parameter-sensitivity: skipped because there is no pass/fail protocol. Some thresholds (Ic at 50% of RN, the 20 mS cutoff, ⟨v²⟩/vF² > 0.1) are set by choice, and question 8 touches them.
- Checks: the library has no checks for the supercurrent family, so I walked only the practice checks (report-counts, report-ranges, report-processing). All three are partly done.

## Sources held out
None. No library source cites this paper by title, authors or arXiv ID. I grepped the library for 2607.11721, Díez, Efetov and Hofstadter and found no match.

## Related work, how each was checked
- 1504.03286 Ben Shalom et al. I read the abstract page (ID, title, first author confirmed) and parts of the full text (PDF via pdftotext): main text p. 5 (near-edge Andreev states, "the edge superconductivity was not observed for hole doping") and SI Sec. 7-9.
- 1512.09083 Amet et al. Abstract page confirmed. I searched the full text: the plateaus are revealed with IDC = 3-6 nA, and the switching current is about 0.5 nA.
- 1805.10184 Indolese et al. Abstract page confirmed. I read the full-text passage on the SQUID-like interference pattern and the Dynes-Fulton current density (edge current at the vHS, MoRe contacts).
- 1705.11170 Krishna Kumar et al. Abstract page only.
- 2402.14451 Barrier et al. Abstract page only (v2).
I found the IDs through the export.arxiv.org API with about 3 s between calls. No paper was listed from memory, and none was dropped.

## Library gaps (outside rows)
1. Chiral Andreev edge-state supercurrent in the quantum Hall regime (Amet et al., 1512.09083). Tests come from that paper's control: a dc bias that reveals plateaus, the nA-scale Ic, and a regular period.
2. Edge-localized Andreev states or edge supercurrent in graphene and graphene/hBN junctions (Ben Shalom et al., 1504.03286; Indolese et al., 1805.10184). The test comes from Indolese's control: the current distribution from the interference pattern.
3. Brown-Zak normal-state conduction in Hofstadter systems, which could feed a 1/R map (Krishna Kumar et al., 1705.11170). The test comes from that paper's finding that the oscillations persist at high temperature.
4. I considered domain-wall 1D supercurrent (Barrier et al., 2402.14451) but did not give it a row. Its Ic is non-oscillatory, while this paper shows oscillating Ic, so the data already differ. It stays in related work.
5. The library has no checks for the supercurrent family (unusual supercurrent at high field).

## Unsure
- Ruling out the chiral edge-state row rests on Fig. S14, taken at 200 nA dc bias. That bias may also wash out small Hofstadter gaps, and I could not see the figure. I kept "Ruled out for the claim" with the one-clause reason. A stricter reader might call it "Tested in part".
- For the edge-state row, the only current-distribution analysis is at zero field. Whether that counts as "part" or "no" for the high-field claim is a judgment call. I chose "part" and said why in the cell.
- The adapted series-resistance row is a light concern, because Fig. 2b shows switching transitions. I kept it because zero R and the 1/R map both depend on the subtracted 3447 Ω.
- Quotes: I normalized PDF-extraction spacing ("dV /dI" written as "dV/dI"). The extracted text uses U+2126 OHM SIGN, and the report uses Greek capital omega. All quotes otherwise match the text, which I checked by script after stripping whitespace.
- Report length: about 930 words outside the table, a little over the 900 target.
- Related-work years are arXiv posting years (Ben Shalom and Amet 2015, published 2016).

## Skill issues
- The skill says to read the abstract page and the PDF. This run forbade both, so the title came from the text, and figures came only from captions.
- The `checks` section has no family for supercurrent signals, although `meta.families` lists `supercurrent`. The skill does not say what to do when a family has no checks. I used practice only.
- The scope rule says to "adapt the matching entries" for a different kind of measurement. It does not say how far a signature may be stretched (for example "grows with field" versus "survives at high field"), or whether outside rows are preferred to stretched entries.
- The "What this is" template text ("lookalikes in topological transport ... the same signal as the one you report") reads awkwardly for a paper with no topological claim.
- "Ruled out" needs the paper to conclude against the lookalike. For an adapted library entry the paper never discusses, a row can therefore never reach "Ruled out", even when the tests are strong. That may be intended, but it is not stated.
- The test rule does not say how to mark a test whose numeric value is stated but whose calibration is not shown (the series resistance). I marked it "no", following "a sentence alone doesn't count".
- The template asks for "<the effect>" in fixed questions, while the skill says to skip questions the paper already answers. Questions 1-2 are partly answered, so I folded the answer into the question. The skill could say whether that is the intended form.
- flags.json has no place for adapted entries to be marked as adapted.
