# Run notes: arXiv 2610.17701v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries).
- Skill: cmp-assistant/skill/SKILL.md and report-template.md, read once at the start. scripts/read_mtx.py not used (no figure data).
- Date: 2026-10-24.

## What I read
- The paper is extracted text only (provided paper.txt): title, authors, abstract, main text, references, figure captions for Figs. 1 to 4, acknowledgements, data and code availability. The test instructions forbid fetching the abstract page, the PDF or the HTML.
- Not available: Methods ("see details in Methods" is referenced but not in the text), Supplementary figures S2 to S11, and page numbers. Quotes are cited by section heading, caption or figure.
- Title taken from the text header, since the abstract page wasn't opened.
- No data repository: "Source data will be provided with this paper"; more data and code on request. No ancillary files, so no device or range counts beyond the text.
- I don't recognize this paper and know nothing of its later history.

## Claims table (step 1)

| Claim | Figures | Device / settings | Counts |
|---|---|---|---|
| Interfacial superconductivity confined to Bi2Te3-covered regions, with coherence peaks at ±1.85 and ±2.92 meV and moiré-modulated gap (2.9 nm period) | Fig. 1D-I, S3, S4 | 1QL Bi2Te3 on 20 UC FeTe, MBE; Fig. 1 at 1.6 K, 10 mV / 200 pA | Samples and islands not given |
| Star-shaped vortex with QPI-like modulation matching Bi2Te3 QPI | Fig. 2A-G, S8 | 0.4 K, 1.0 T perpendicular, "defect-free region", 50 nm maps, 10 mV / 500 pA | One vortex shown |
| ZBCP at the vortex core, FWHM about 0.5 meV, about twice the out-of-gap conductance | Fig. 2I | 1.0 T core versus 0 T "clean surface" | Same-site status of the 0 T spectrum unclear |
| ZBCP stays unsplit along two directions; X-shaped dispersive branch 10 to 20 nm out | Fig. 3B-F | Single vortex in island, 100 nm map, 10 mV / 1 nA | Two linecuts (white and orange arrows) |
| Five discrete levels L-2..L2 at -2.1, -0.93, 0.003, 0.79, 1.96 meV, read as integer CdGM sequence | Fig. 3G | Core region of Fig. 3B | One vortex; resolution about 0.37 meV at 0.4 K. My computed ratios: L2/L1 = 2.48, L-2/L-1 = 2.26 (integer predicts 2; half-integer 1/2, 3/2 predicts 3) |
| ZBCP decay isotropic, fitted with MZM spatial profile | Fig. 3H-I | Same linecuts | Two directions |
| FeTe origin: Dirac-like dispersion in Te-annealed FeTe, absent in as-grown | Fig. S6, S7 (ARPES) | Bare FeTe films | Not on the heterostructure |
| Number control: 1, 2, 3 vortices by field and island size; "MZMs are observed in all measured vortices" | Fig. 4B-E | 68 nm zero-energy maps, 10 mV / 1 nA, fields not given | Number of vortices, islands, samples, cooldowns not given; no spectra shown for multi-vortex configurations |

Missing counts: samples, islands, vortices measured, cooldowns, field values for Fig. 4, temperature range (only 0.4 K and 1.6 K), setpoint series.

## Entries matched, adapted and skipped
- Scope: STM vortex-core spectroscopy, outside the transport scope. Adapted: kondo-resonance (magnetic excess Fe in place of a dot; even-odd test marked "no" as inapplicable), local-probe-loophole (partner mode at the island edge or the vortex line's far end), and the zbp checks: dot search to a bound-state search near the core, transparency to tip height, nonlocal gap to independent topological band evidence (ARPES), raw conductance to raw spectra and fit processing.
- fine-tuning-and-selection: always included.
- Skipped: abs-quantum-dot (no tunnel barrier or wire; the vortex-core analogue, trivial CdGM states, is handled by outside rows with vortex-specific sources); quasi-majorana-smooth-confinement (wire end confinement); disorder-induced-zbp (wire tests: end-to-end correlation, gates; disorder at defects covered by the YSR outside row); crowded-trivial-subgap-states (multiband wire; unresolved CdGM crowding covered by outside rows); weak-antilocalization (transport through a disordered wire); fine-tuned-plateau and series-resistance-subtraction (no quantization claim, STM); one-end-only (no wire ends; covered by local-probe-loophole); trivial-andreev-band-gap-reopening and protocol-parameter-sensitivity (no nonlocal data or protocol); micromagnet-stray-field (applied field, no magnets); full-shell-flux-andreev (no full-shell wire); spin-orbit-length-pinning (no normal segment); exceptional-point-zero-mode (weakly coupled tip, no open lead); all chiral, island, shapiro, supercurrent, charge, kitaev and diode entries (signals not present).

## Sources held out
- None. I didn't open library sources (their quotes and titles were enough to match), and none of their titles or quotes refer to this paper. Kim et al. 2021 (related work) mentions earlier Bi2Te3/FeTe0.55Se0.45 work, a different system and paper; it doesn't discuss this one.

## Related work and outside rows: how checked
All IDs, titles and first authors confirmed on arxiv.org/abs pages; abstracts read through the export.arxiv.org API.
- 2105.01354 Kim et al.: abstract and full text (PDF, pdftotext). Basis for the outside row "anisotropic non-split zero-energy CdGM states"; tests from its text: angle-dependent radial cuts, quasi-classical calculation with the real Fermi contour, superconducting tip for resolution. It also states that a non-split zero-energy state "is not a characteristic signature of a MBS".
- 1709.09401 Chen et al.: abstract and full text (grep of key passages: levels at μ = 1/2, 3/2, 5/2, E1/2 about 0.45 meV, levels stable with tip position). Basis for the outside row "trivial quantum-limit CdGM levels".
- 1901.02293 Kong et al.: abstract (integer versus half-odd-integer level ratios tied to presence of ZBP). Used for the ratio test.
- 1812.08995 Machida et al.: abstract.
- 2603.27217 Li et al.: abstract. Basis for the outside row "impurity-induced near-degenerate YSR states"; tests from its abstract (superconducting tip, field, tunneling transmissivity).
- 1403.1027 Yin et al. (interstitial excess Fe zero-energy bound state in Fe(Te,Se), robust to 8 T): abstract opened; supports the impurity row's relevance to Fe1+yTe; not listed in related work to keep five.

## Library gaps
- No entries for STM vortex-core signatures: (1) trivial quantum-limit CdGM levels, half-integer series, lowest level below resolution (Chen 2017, Kong 2019); (2) anisotropic non-split zero-energy CdGM states (Kim 2021); (3) impurity-induced zero-energy states and near-degenerate YSR states (Yin 2014, Li 2026); (4) vortex-to-vortex variation of zero modes with field (Machida 2018). A "vortex" family with checks (level-ratio fit, angle-resolved splitting, resolution versus level spacing, tip-height series, same-site zero-field spectrum, per-vortex statistics) would cover this class.

## Unsure
- Whether Fig. 2 and Fig. 3 show the same vortex, and whether the Fig. 2I 0 T spectrum was taken at the later core site; marked the related tests "part".
- Adapting zbp-nonlocal-gap to ARPES evidence is a judgment call; it could also be marked not applicable.
- The level ratios (2.48, 2.26) are my arithmetic from the listed energies; they ignore the stated uncertainties (±0.11 to ±0.22 meV), which may allow either sequence.
- Status of "data bear on it" for local-probe-loophole rests on Fig. 4B-D zero-energy maps existing; spectra may exist in the Supplement I didn't have.

## Skill issues
- The skill requires page numbers for every quote; text-only input has none. I used section and caption locators.
- The skill says read the abstract page and use its title; the run instructions forbid it. I took the title from the text.
- The flags schema has no "not applicable" value for a test (Kondo even-odd test); I used "no" and said so.
- "A sentence alone doesn't count" conflicts with the fine-tuning test "Devices and datasets measured, and how many showed the effect", which is by nature a statement; I marked "part" for "all measured vortices" without a number.
- The rule that gaps about unshown data count once, under fine-tuning-and-selection, overlaps with the practice checks report-counts and report-ranges, which count the same gap again.
- Outside rows take one source URL in flags; the CdGM row draws on two papers (Chen for the lookalike, Kong for the ratio test). I listed Chen.
- For non-transport papers, the guidance is "adapt the matching entries" but there is no guidance on adapting checks whose physics has no analogue (both ends, series resistance).
