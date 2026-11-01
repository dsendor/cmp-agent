# Run notes: arXiv 2607.00683v1

- Library version: 0.5 (meta.version), 28 lookalike entries.
- Date: 2026-10-24.

## What I read
- The extracted text of the paper only (main text, Methods and references, 12 pages). The run instructions said not to fetch the abstract page, PDF or HTML. The title comes from the paper text.
- The extracted text has no Supplementary Information. I couldn't open Supplementary Notes 2 to 7, Figs. S1 and S7, or Table S1 (device dimensions). No data repository or ancillary files, so read_mtx.py wasn't used.
- Figure details come from the captions only.
- Page numbers follow the page markers in the extracted text (p. 1 to p. 8 for the main text).
- Quote normalization: the extraction renders "Js(x)" as "Js (x)". The quotes used in the report don't include it.

## Claims table (step 1)

| Claim | Figures | Devices | Counts and ranges given | Missing |
|---|---|---|---|---|
| ZrTe5 is in the WTI phase | Fig. 2a-g, Supp. Fig. S1, Supp. Notes 3-4 | One Hall bar device; STM on UHV-cleaved crystals | SdH at 2 K; STM at 5.1 K; gap ≈70 meV; step-edge states ≈6 nm wide; Tp ≈139 K | Number of crystals and STM sites; context only, outside library scope |
| Proximity supercurrent | Fig. 3a-c | Dev 1, Dev 2 (Pd/Al, current along a); Dev 3 (Pd/NbN, current along c) | Base temperature 15 mK; temperature series shown | Devices fabricated or measured; RN; Ic criterion; cooldowns |
| Ballistic transport from exponential Ic(T) | Fig. 3d, Supp. Note 2 | All three | Fits "in the high-temperature regime" | Fit range, δE values, L, mean free path (supplement) |
| SQUID-like, flux-quantum-periodic Ic(B), edge-peaked Js(x) | Fig. 4a,b,d,e; Fig. 5b; Supp. Notes 5-6, Fig. S7 | Dev 1, Dev 2 (Bz along b); Dev 3 (Bz) | 20 mK; Gaussian half-widths 0.7-1.5 µm | Field ranges in numbers; other temperatures; junction widths (Table S1) |
| Field-orientation contrast | Fig. 5c | Dev 3 only (By along a) | 20 mK | By on Dev 1 and Dev 2; field ranges |
| Sharp lobes read as a sawtooth current-phase relation | Fig. 5b,c; Fig. 5d-f simulations; Supp. Note 7 | Dev 3 | 20 mK | Lobe shape against temperature; Al devices' lobe shape |

## Entries skipped or adapted
- Applied as written: fine-tuning-and-selection, plus the practice checks report-counts, report-ranges and report-processing.
- Not adapted: none. Scope note in "What this is": the paper is Josephson interferometry on a 3D topological insulator, which no library family covers.
- Skipped, with reasons:
  - zbp, quantization, nonlocal and island entries (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode, island-states-coulomb-spacing): no zero-bias peak, quantized conductance, nonlocal gap or island signal is claimed.
  - local-probe-loophole: no Majorana claim. The STM step-edge data are supporting context, not read as separated Majorana modes.
  - protocol-parameter-sensitivity: no automated pass/fail protocol.
  - Shapiro entries (shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, transparent-junction-pi-crossing): no microwave or 4pi claim.
  - field-enhanced-supercurrent-resonances: the supercurrent decays with field. No growth with field is claimed.
  - charge, chiral, kitaev and diode entries (charge-trap-fractional-shift, coulomb-dominated-interferometer, chiral-plateau-superconductor-short, false-poor-mans-majorana, diode-vortex-screening): the signals don't match.
- Checks: only the practice family applies. The zbp, shapiro, kitaev and charge checks don't match the paper's signals.

## Sources held out
- None. No library source cites 2607.00683; the library sources predate July 2026.
- An arXiv API search (abs: triangular AND "interference pattern" AND Josephson) returned 2607.00683v1 in its listing. I did not open it.

## Related work and outside rows: how each was checked
- de Vries et al., 1709.03727: abstract page (ID, title, first author) and full-text PDF. The control (gate-tuned transition from bulk to edge transport in a non-topological junction) and the band-bending mechanism come from p. 1 and Fig. 3.
- Allen et al., 1504.07630: abstract page. Used in related work only.
- Dubos et al., cond-mat/0008146: abstract page and full text. The quote "numerically very close to a simple exponential dependence" is on p. 3.
- Chiodi et al., 1201.3509: abstract page.
- Friedrich et al., 1908.11067: abstract page and full text. Triangular modulation and the screening factor βL appear around Eq. for ΔIc.
- Also opened, not listed: Ke et al. 1906.07935 (abstract), Wang et al. 2012.05898 (abstract), Babich et al. 2302.02705 (abstract).
- OpenAlex: Golubov et al. RMP 76, 411 has no arXiv version, so it is not used.

## Library gaps
- There is no family for Josephson interferometry or edge supercurrent read as topological boundary states. Candidate entries:
  - trivial edge channels from band bending (de Vries 2018; Allen 2016; Aharon-Steinberg 2021, 2012.02842);
  - diffusive Ic(T) that mimics the ballistic exponential (Dubos 2001);
  - triangular or skewed lobes from loop or kinetic inductance (Friedrich 2019);
  - aspect-ratio dependent patterns in uniform junctions (Chiodi 2012);
  - possibly anomalous non-Fraunhofer patterns in ballistic junctions with no edge (Ke 2019).
- There is no check family for interferometry.

## Unsure
- Report-ranges was set to "not done". The figures display the ranges they show, but the text gives no measured ranges and no reason for the shown ones.
- Trivial edge row: the note is "argued, not tested". Fig. 5c also bears on it, since the paper calls the edge channels in the By geometry "puzzling" (p. 7). I picked "argued" because the paper argues against it explicitly.
- Aspect-ratio row: the first test is marked "part". The paper compares Fig. 5c with a uniform profile in its own model, but I can't tell from the main text whether that model includes the Dev 3 aspect ratio.
- Whether the Si substrate is gateable is not stated. Question 5 asks.
- I didn't recognize the paper (posted after my training data).

## Skill issues
- The scope rule says to "adapt the matching entries", but here none match except practice. The skill doesn't say whether outside rows should then carry the report, or how many are reasonable.
- Step 7 says to use the title on the arXiv abstract page and to write reports/<id>.md. This run forbade both, so I took the title from the text and put the outputs in the reply.
- "Take its tests from the control that paper describes": de Vries et al. describe a study, not a crisp control. I turned it into two tests (gate tuning, a trivial reference junction).
- When a paper both argues against a lookalike and has figures that bear on it, the skill doesn't say which "Not tested" note takes priority.
- "One quote per cell" conflicts with wanting both a paper quote and an outside source's quote in the same cell. I kept the outside source as a clause.
- The checks section has no family for this kind of signal, and the skill doesn't say whether to adapt the zbp checks in that case. I used practice only.
