# Run notes: 2607.00683v1

- Library version: 0.5 (meta.version), 28 lookalike entries; checks section read.
- Skill files read: skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml. scripts/read_mtx.py not used (no figure data).
- Paper read: extracted main text only (paper.txt, 12 pages incl. references), per the run instructions. No PDF, abstract page or Supplementary Information. Title taken from the text: "Facet-selective ballistic supercurrent in a weak topological insulator". Figure details from captions only; I could not see axis ranges. No data repository linked in the text; none used.
- Recognition: I did not recognize the paper and have no knowledge of its later history.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges |
|---|---|---|---|
| SQUID-like Ic(B), flux-quantum period, supercurrent at two side facets | Fig. 4a,b (Dev 1, Dev 2, Al, I along a, B along b, 20 mK); Fig. 4d,e Js(x); Fig. 5b (Dev 3, NbN, I along c, Bz) | Dev 1, 2, 3 | 3 junctions shown, all show it. Fabricated or measured total: missing. Field range: not in text. Js(x) half-widths 0.7 to 1.5 um (p. 7). Period analysis in Supp. Note 5 (not available). |
| Field-orientation contrast (By vs Bz) | Fig. 5b,c | Dev 3 only | One device. Range not in text. |
| Exponential Ic(T), ballistic long junction | Fig. 3a-d | Dev 1, 2, 3 | T range not in text; fits "in the high-temperature regime" only. Mean free path in Supp. Note 2 (not available). |
| Sharp lobes, sawtooth CPR | Fig. 5b,c vs simulations Fig. 5d-f | Dev 3 | One device. |
| ZrTe5 in WTI phase | Fig. 2a-d (one Hall bar, SdH at 2 K), Fig. 2e-g (STM at 5.1 K, gap about 70 meV, step-edge LDOS) | Hall bar: 1; STM: crystals | Supp. Notes 3, 4 not available. |

Missing counts: devices fabricated, devices measured, cooldowns, number of datasets, field ranges, temperature ranges, device dimensions (Supp. Table S1).

## Matching (step 2)

- Matched: fine-tuning-and-selection (always).
- Family: closest is `supercurrent`, which has no checks; practice checks applied (report-counts, report-ranges, report-processing).
- Skipped: all zbp, quantization, nonlocal, island, shapiro, kitaev, charge, chiral, diode entries (no tunneling peaks, quantization, Shapiro, islands, interferometry of fractional charge, or diode effect in this paper). field-enhanced-supercurrent-resonances skipped: its signature is supercurrent growing with field, which this paper doesn't claim. protocol-parameter-sensitivity skipped: no automated pass/fail protocol, though the Js(x) reconstruction does depend on field range (raised in questions and under report-ranges).
- Adapted: none of the library entries; the scope sentence under "What this is" says the library lacks entries for this signal.

## Status reasoning

- fine-tuning-and-selection: three devices shown for the SQUID-like claim; By and lobe-shape claims from Dev 3 alone, so "second device" is part. No statement of how data were chosen.
- Trivial edge accumulation (outside): the paper argues against it with three observations (reproducibility, By vs Bz contrast, ballistic Ic(T)). None tunes the Fermi level or uses a trivial reference, which are the separating measurements implied by de Vries et al. (gate-tuned bulk-to-edge crossover in a non-topological junction). The By data bear on it, but I did not count them as an equivalent test because the paper itself calls the edge channels there "puzzling". The paper also says Js(x) broadening "may reflect ... trivial boundary contributions" (p. 7); I treated that as about peak width, so status is "argued, not tested", not "left open".
- Diffusive long junction Ic(T) (outside): only the ballistic form is fitted (Fig. 3d caption). The independent mean-free-path estimate is in Supp. Note 2, which I could not read, so that test is marked "part" under the "still unclear" rule, giving "Tested in part". If the supplement holds no quantitative estimate, this should drop to "Not tested (argued, not tested)".

## Sources held out

- None of the matched library sources (Frolov et al. 2023; Akrap, Frolov et al. 2026 v2) appeared to discuss this paper. Frolov 2023 predates it. I did not open Akrap v2 in full to confirm it does not cite 2607.00683; judged by topic only.

## Related work: how checked

- 1709.03727 (de Vries et al.): arXiv API abstract plus full text (PDF to text); confirmed ID, title, first author, SQUID pattern from trivial edges, gate-tuned bulk-to-edge transition, Dynes-Fulton assumptions (sinusoidal CPR, near-longitudinal trajectories).
- cond-mat/0008146 (Dubos et al.): abstract plus full text; confirmed the quote that the diffusive Ic(T) is "numerically very close to a simple exponential dependence Ic ∝ exp(−L/LT) with LT ∝ 1/T, as one would expect in a ballistic limit" and that "This coincidence is purely accidental".
- 1611.00190 (Suominen et al.): abstract only.
- 1504.07630 (Allen et al.): abstract only. Cited in the paper under review as ref. 40.
- 2309.09368 (Frolov et al.): abstract only (library source).
- Ghatak et al. 1803.09976 (anomalous Fraunhofer in BiSbTeSe2): abstract read, not listed.

## Library gaps

- No family or checks for interference-based claims of edge- or facet-localized supercurrent (SQUID-like Ic(B) in topological insulators, quantum spin Hall systems, higher-order hinge states). Candidate entries: trivial edge accumulation (de Vries et al. 2018, 1709.03727); quasi-exponential diffusive Ic(T) mimicking ballistic (Dubos et al. 2001, cond-mat/0008146); Dynes-Fulton reconstruction assumptions and flux focusing (Suominen et al. 2017, 1611.00190).

## Unsure

- Page numbers follow the printed page numbers in the extracted text; quotes are verbatim from that text (subscripts flattened, e.g. "Al/ZrTe5").
- Without the figures I could not judge the field ranges, lobe sharpness or the quality of the exponential fits directly.

## Skill issues

- The skill tells me to read the arXiv abstract page and PDF; this run gave text only and forbade fetching, so the title came from the text. The template's "Use the title on the arXiv abstract page" can't be followed in that case.
- No guidance for a paper whose signal has no family checks (here `supercurrent` has none): I used practice checks only. A line saying so would help.
- "Tests" for an outside row come "from the control that paper describes"; de Vries et al. state no explicit control, so I derived the tests from what they did. The skill could say what to do when the outside paper implies the control without stating it.
- "Every status except Not tested (not mentioned) needs a quote": unclear whether a quote that supports a "part" test from an unavailable supplement is enough.
- The 600 to 900 word target: unclear whether questions and related work count as "outside the table".
