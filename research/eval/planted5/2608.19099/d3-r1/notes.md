# Run notes: arXiv 2608.19099v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries. Skill: cmp-assistant/skill/SKILL.md and report-template.md.
- Date: 2026-10-24. Label: AI only.

## What I read
- Only the extracted text of v1, as instructed: paper.txt in the scratchpad blind folder. I had no PDF, no abstract page and no Supplementary Material. The SM (ref. [40]) is not in the text. It holds device #2, the RMCD data, the micromagnetic details and the stated controls for self-fields, Meissner screening and geometric asymmetry. None of those could be judged.
- I took the title from the first page of the text, since the abstract page was off limits.
- Page numbers come from the page markers in the extracted text: p. 1 abstract and intro; p. 2 Fig. 1 and the Fig. 1-2 discussion; p. 3 Fig. 2 caption, Fig. 3 discussion and symmetry argument; p. 4 Figs. 3-4 captions, "trivial mechanisms" sentence, RMCD and micromagnetics; p. 5 GL theory and summary.
- No ancillary figure data, so read_mtx.py was not used. No data repository is linked in the text.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Zero-field SDE, η = −15.2% after ZFC and −35.7% after field training | Fig. 1(c)-(e), 2(c) | #1 | Current 0 to ±300 µA; Fig. 2 at 200 mK; Fig. 1(e) temperature range not stated; training field before Fig. 2 not stated |
| Polarity set by field history; nonmonotonic hysteretic reversals, max +45.3% at about −10 mT, Bcf < 0, Bcb > 0 | Fig. 2(a)-(c) | #1; "similar" in #2 (SM only) | Field ±50 mT, perpendicular, 200 mK; number of sweeps per Ic not stated |
| Zero-field rectification switched by ±6 T training | Fig. 3(a) | #3 | 705 µA excitation; Ic of device #3 not stated |
| Efficiency among highest reported | Fig. 3(b) | #1 | Literature comparison |
| Mechanism: layered FIM CrBr3 proximity plus cubic q term | Fig. 4 | Simulation (trilayer), RMCD (SM) | CrBr3 and NbSe2 thicknesses not stated in the main text |
| "our NbSe2/CrBr3 devices consistently exhibit" Bcf < 0, Bcb > 0 (p. 3) | Fig. 2 | Implied several | No count |

Missing counts: devices fabricated, devices measured, devices showing the effect, cooldowns, sweeps per Ic value, flake thicknesses, Tc of each device, and whether RMCD was taken on the transport flakes.

## Entries matched, adapted, skipped
- Matched: diode-vortex-screening (family diode); fine-tuning-and-selection (always).
- Adapted: micromagnet-stray-field. Its signature is zero-bias peaks from dot Andreev states. I matched it on its physics: a stray dipolar field from a nearby magnetic layer breaks time reversal at zero applied field and is read as an exotic mechanism. Its tests (magnet switching, stray field bounded, devices without magnets) carry over directly.
- Skipped, wrong signature or device: all zbp entries except micromagnet-stray-field (abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode), because there is no tunneling spectroscopy. Also skipped:
  - quantization (fine-tuned-plateau, series-resistance-subtraction): no conductance quantization.
  - nonlocal and island entries: not relevant to this device.
  - shapiro entries: no microwave steps.
  - field-enhanced-supercurrent-resonances: no claim of Ic growing with field read as triplet pairing.
  - charge and chiral entries: not relevant.
  - kitaev: not relevant.
  - protocol-parameter-sensitivity: no pass/fail protocol.
  - local-probe-loophole: no Majorana claim.
  - coulomb-dominated-interferometer: not relevant.
- Checks: the library has no `checks` block for the diode family. Only the three practice checks were walked.

## Sources held out
- None. No matched-entry source (Hou 2205.09276; Frolov 2309.09368; Akrap 2501.18631; Jiang 2305.19970) discusses this paper. All predate it, and none of the abstracts I opened mention it. I did not open the full texts of Frolov, Akrap or Jiang 2305.19970 to check for a citation, since all predate August 2026 except possibly Akrap v2.
- A grep for "2608.19099" over every page I fetched returned nothing.

## Related work, how checked
- 2205.09276 Hou et al.: abstract page opened (title, first author, date confirmed); abstract read via arXiv API.
- 2512.05427 Jiang et al.: abstract page opened; full text read (PDF), including Sec. on hysteresis, Appendix D (magnet correction about ±15 mT with a graphene reference) and Appendix E (orientation).
- 2205.12196 Golod and Krasnov: abstract page opened; abstract read.
- 2206.00483 Narita et al.: abstract page opened; abstract read.
- 2406.14417 Xiong et al.: abstract page opened; abstract read.

## Outside rows (library gaps)
- Trapped magnetic flux in the superconductor after a poling field. Source: Jiang et al. 2025, https://arxiv.org/abs/2512.05427, "These results confirm that the zero-field superconducting diode effect originates from trapped magnetic flux, whose sign is determined by the sign of Hp." Tests are taken from its controls: poling sign, poling magnitude (1 T versus 2 T), and field orientation. The only test the paper shows (opposite poling fields) does not separate this lookalike from the CrBr3 reading. Golod and Krasnov 2205.12196 (trapped Abrikosov vortex plus self-field) is a second source for the same gap.
- Remanent field of the superconducting magnet. Source: Jiang et al. 2025, Appendix D, "Because a superconducting magnet was used in this study, hysteresis due to the magnet should be observed at low magnetic fields after applying a large magnetic field." Tests are taken from its graphene-reference correction. I consider this a strong gap for any hysteretic, field-history diode claim. The ±10 mT sign-change fields here are comparable to the 15 mT offset Jiang et al. corrected.
- Self-field from nonuniform bias (Golod and Krasnov) is also a gap. The paper says it is ruled out in the SM, so I did not add a separate row.

## Unsure
- diode-vortex-screening "effect followed against field" marked part: field sweeps are shown for device #1. Device #3 has only zero-field data, and device #2 is in the SM.
- micromagnet-stray-field "magnet switching" marked part: the transport hysteresis in Fig. 2 tracks switching, but the RMCD loops are in the SM. Fig. 4(b) is a simulation.
- Trapped-flux "opposite poling fields" marked all: it is shown for #1 (sweep history) and #3 (±6 T). It does not discriminate, which is why the status stays at tested in part.
- I may have read the text's page markers correctly but cannot verify against the PDF.
- Possible text oddities, not used in the report: the text says "Figures 1(a) and 1(b) illustrate the schematic and optical image", while the caption puts the optical image in the inset of 1(b). Also, device #3 uses a 705 µA excitation while device #1 sweeps only to ±300 µA; this is plausible if Ic differs, but Ic of #3 is not given.
- I did not recognize this paper or know any later history of it.

## Skill issues
- The library has a diode family and a diode lookalike, but no diode `checks` block. Step 3 says to walk "the checks for the paper's family", and here that set is empty. The skill doesn't say whether to adapt checks from other families.
- How to treat controls stated as "shown in SM" when the SM is not available is unclear. I marked them not shown and said so in "What this is".
- The `note` field in flags.json is defined only for "Not tested". I set it to null for the other statuses.
- Outside-row tests: the skill says to take them from the cited paper's control. When that control does not discriminate the lookalike from the paper's own reading (poling-sign reversal), the status rules still give "tested in part", which may overstate it.
- The template's "Tests shown" column and the one-quote-per-cell limit made it hard to fit the device-level qualifiers (#1 versus #3 versus #2 in the SM). I put them in parentheses.
- The skill asks for 600 to 900 words outside the table, but doesn't say whether the questions and related-work list count toward that.
