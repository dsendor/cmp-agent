# Run notes: arXiv 2512.07017v1

**Library version:** 0.5 (meta.updated 2026-10-24), 28 lookalike entries.

## What I read
- The skill (SKILL.md), report-template.md, library/lookalikes.yaml including `tests` and `checks`. I did not need scripts/read_mtx.py (no .mtx data).
- The paper: the extracted text and the v1 PDF (38 pages). I rendered every figure page (pp. 20 to 23 and 29 to 38) and read figure details from the images. The PDF has the main text, Methods, 4 figures and 10 Extended Data figures. It does not include the Supplementary Information, so Figs. S1 to S11 (including S3 and S4 for Samples S3 and S4) were not available.
- The text extraction drops the "μ" in the μV values on p. 7 (for example "-101.1 V"). The figures show μV.
- Title: taken from the PDF. I did not open the arXiv abstract page because the run instructions forbid fetching the paper in any form.

## What I could not open or did not use
- Data repository (Zenodo, doi 10.5281/zenodo.17050703): not accessed. Zenodo is outside the fetch list in the run instructions, and the record page may carry the paper's abstract or links to later versions. So I did not use the data to count devices or ranges.
- OpenAlex: rate-limited ("Insufficient budget" without an API key). I did not request a key, since that needs an email address.
- Yasuda et al. 2020 (Nat. Nanotechnol. 15, 831, ref. 33, QAH edge-state nonreciprocal transport): not found through arXiv title or author search. I dropped it from related work.

## Claims table (step 1)

| # | Claimed signal | Figures | Device | Counts and ranges |
|---|---|---|---|---|
| 1 | V2ω_xx,L and V2ω_xx,R have opposite signs (electrode dependence), read as boundary-mode dominance | Fig. 1e, 1f; Fig. 2; ED Figs. 2, 7, 9, 10 | S1 (main); S2 (ED 9, 10) | S1 at 25 mK, 2 μA, (Vg-Vg0) = -5 and 10 V in Fig. 1; field ±1.5 T at 25 mK, ±1 T at 1.7 K |
| 2 | V2ω_xx,A dominates V2ω_xx,S | Fig. 2a to 2e; ED Fig. 7b, 7d | S1 | Five gate voltages in Fig. 2 (-15, -5, 0, 10, 100 V); gate sweeps -200 to 200 V in Fig. 3 and ED Fig. 7 at 0 T (QAH) and 0.25 T (Axion-II) |
| 3 | Sign set by magnetic order (Axion-I vs Axion-II) and carrier type | Fig. 1e vs 1f; Fig. 3 | S1 | As above |
| 4 | Near-zero plateau inside the QAH exchange gap; signals vanish at Vg0 and are largest slightly away from the quantized states | Fig. 2c, 2h; Fig. 3a, 3b | S1 | -5 V ≤ (Vg-Vg0) ≤ 10 V gap window |
| 5 | V2ω_yx ≈ V2ω_xx,R, matching the C2z relation V2ω_xx,L = -V2ω_xx,R = -V2ω_yx | Fig. 2f to 2j; Fig. 4 (simulation) | S1 | Only one Hall pair (2 and 6) measured |
| 6 | Frequency independence, quadratic current scaling, vanishing near Tc ~20 K, ground swap shows no gate-oscillation artifact | ED Figs. 3 to 6 | S1 | All at 1.7 K, (Vg-Vg0) = -5 V; frequencies 6.477 to 107.477 Hz (5 values); currents 2 to 5 μA (about 13 values); temperatures 1.7 to 40 K; ground swap at 5 μA |
| 7 | γ ~1.22 × 10^-9 m^2 A^-1, an order of magnitude above MnBi2Te4 and WTe2 | p. 7 | S1 | (Vg-Vg0) = -5 V |
| 8 | V2ω_xx,S reverses between the two axion states, consistent with quantum-metric bulk transport | Fig. 2b, 2d | S1 | |

Counts: 4 samples (S1 to S4), all grown as the same sandwich. S1 and S2 measured in the dilution refrigerator, all four in the PPMS. The paper doesn't give the number of devices fabricated, the number that showed the effect, the cooldowns, or the number of datasets. The field is perpendicular only. Hall bar about 1 mm × 0.5 mm, scratched, with pressed indium contacts and a SrTiO3(111) back gate. S2 is shown at 25 mK, 1 μA, (Vg-Vg0) = -15 and 20 V (ED Fig. 9), and at 1.7 K, 5 μA, -15 and 5 V (ED Fig. 10). No figure data files came with the paper.

## Entries matched, skipped, adapted
- Matched as written: fine-tuning-and-selection (always applies).
- Checks: no family check list fits (zbp, shapiro, kitaev and charge don't apply), so I walked only the three `practice` checks.
- Skipped: every zbp, quantization, nonlocal, island, shapiro, supercurrent, kitaev entry (they need a superconductor, a nanowire, a Josephson junction or a dot chain). Also skipped:
  - chiral-plateau-superconductor-short: no superconductor; the QAH film is the same material class, but the mechanism needs an Al strip.
  - diode-vortex-screening: nonreciprocity, but the mechanism is superconducting vortex screening.
  - protocol-parameter-sensitivity: no automated pass/fail protocol.
  - local-probe-loophole: Majorana-specific.
  - charge-trap-fractional-shift and coulomb-dominated-interferometer: no fractional-charge claim.
- Adapted: none. Scope noted in one sentence under "What this is".
- Outside rows (not in library), each from a paper I opened:
  - Gate-voltage oscillation (Xu et al. 2401.00679, full text). Tests taken from that paper's grounding method and its intentional gate-oscillation experiment.
  - Back-gate self-gating (Iwakiri et al. 2306.09907, full text). Tests taken from its no-back-gate control and its model built from linear coefficients and capacitance.
  - Joule-heating thermoelectric 2ω (Avci et al. 1412.0865, abstract and text). Tests taken from its symmetry and field separation and its light-metal control.

## Sources held out
None found. The library sources used (2309.09368 and 2501.18631 for fine-tuning-and-selection and the practice checks) were used only through the library's own quotes. I did not open them, so I could not fully confirm that 2501.18631v2 (2026) does not cite this paper.

## Related work: how each link was checked
- 2401.00679 Xu et al.: arXiv API (ID, title, first author Liangcai Xu, abstract) plus full-text PDF read for the grounding test (source vs drain sign reversal, averaging over Hall-electrode grounding).
- 2306.09907 Iwakiri et al.: arXiv API plus full text (no-back-gate control, contact-configuration dependence, capacitive model).
- 1412.0865 Avci et al.: arXiv API (first author Can Onur Avci) plus a full-text grep. Its geometry is in-plane magnetization with a vertical thermal gradient. For perpendicular magnetization, as here, the relevant contribution would come from in-plane gradients; that link is my inference.
- 2307.08917 Li et al.: arXiv API, abstract only (first author Chunfeng Li).
- 2306.09285 Wang et al.: arXiv API, abstract only (first author Naizhou Wang).
All five are earlier than the paper under review; none of them discusses it.

## Library gaps
- No family for nonlinear or second-harmonic transport (nonlinear Hall, nonreciprocal resistance) in magnetic topological insulators and 2D magnets. Candidate entries: gate-voltage oscillation (Xu 2024), back-gate self-gating in the quantum Hall regime (Iwakiri 2023), Joule-heating thermoelectric 2ω (Avci 2014), and magnon-scattering unidirectional magnetoresistance (Yasuda 2016, 1609.05906, abstract seen; not used, because it needs in-plane magnetization).
- No `checks` list for the chiral or diode families.

## Unsure
- Status of the Iwakiri row. The paper's exclusion sentence cites this work (ref. 46) with Extended Data Fig. 3, but a ground swap does not test position-dependent self-gating, so I set "argued, not tested". A stricter reader could call the ground swap a partial test.
- The remark that the C2z relation holds for any response even in current is my own reasoning from the paper's Methods. I phrased it as a question a reader may ask.
- Avci's relevance to perpendicular magnetization (see above).
- The heating row's note: I chose "argued, not tested" because the paper argues that 2 μA minimizes heating. "Data bear on it" also fits, since ED Figs. 5 and 6 could test it.
- I don't recognize this paper or its later history.

## Skill issues
1. Step 0 asks for the title from the arXiv abstract page; the test harness forbids opening it. I used the PDF title.
2. Step 7 says to write reports/<id>.md and notes files; the harness asks for them in the reply. I followed the harness.
3. Scope: the skill says to adapt matching entries for out-of-scope papers, but here no entry's mechanism carries over. The skill doesn't say whether outside rows should then carry the load, or how many to add.
4. The hold-out rule asks me to skip library sources that discuss the paper, but checking that means opening every source. The skill doesn't say whether I should open them.
5. It is unclear which status to use when the paper's exclusion sentence cites the source of a lookalike but uses a test that doesn't separate it ("argued, not tested" vs "tested in part").
6. The `checks` section has no fallback for families without a check list. Only `practice` applied here.
7. The fetch rules (OpenAlex with no key) hit a shared daily budget, and the skill gives no fallback for DOI lookups.
