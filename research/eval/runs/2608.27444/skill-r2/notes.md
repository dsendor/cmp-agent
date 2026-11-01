# Run notes: 2608.27444v1

**Library version:** 0.4 (meta.updated 2026-10-23), 28 lookalike entries plus the `checks` section. I read SKILL.md, report-template.md and lookalikes.yaml once, at the start.

## What I read
- The arXiv abstract page (local abs.html): title "Trapping $e/4$ quasiparticles in bilayer graphene", first author Di Luca, v1 dated 27 Aug 2026, only one version listed.
- The full text (local paper.txt), all 31 pages, main text plus Supplementary sections D to M. I checked every quote against a column-ordered `pdftotext` extraction of the local PDF.
- I rendered PDF pages 3 to 5 (Figs. 1 to 3) to read axis ranges. I did not inspect the Supplementary figure images (S1 to S18) visually; I used their captions and text only.
- I did not fetch the paper itself in any form.
- Ancillary files: none on the abstract page. Data repository: none ("available from the corresponding author upon reasonable request", p. 10). I counted nothing from data, and `read_mtx.py` was not needed.
- Recognition: I did not recognize the paper. It postdates my training data, so I used no knowledge of its later history.

## Could not open
Nothing that I tried.

## Claims table (step 1)

| Claim | Figures | Device | Values and ranges shown |
|---|---|---|---|
| e/4 at ν = −5/2, −1/2, 3/2 (weak coupling) | Fig. 2a,b,d,e,f,h (p. 4); S8, S9, S11 (pp. 20 to 23) | one device | ΔV/ΔV1 = 0.27 ± 0.03, 0.24 ± 0.03, 0.25 ± 0.03; ΔB = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT. Windows: −5/2 at B 13.930 to 13.965 T and Vadg −3.60 to −2.90 V; −1/2 at 13.90 to 14.00 T and −3.30 to −2.90 V; 3/2 at 13.93 to 14.00 T and 0.55 to 1.05 V. Iac 0.2 to 1 nA, chosen per filling (p. 9). |
| e/3 at ν = 2/3 | Fig. 2c,g; S10, S13 to S15 (pp. 22, 25 to 27) | same | 0.32 ± 0.03; ΔB1/ΔB = 2.32 ± 0.93; window 13.90 to 14.00 T, Vadg 2.74 to 3.44 V; 20 repeated sweeps at fixed B (S13); histogram ΔB 19.6 ± 4 mT |
| Calibration of the reference | Fig. 1e to h (p. 3); S3 to S5 (pp. 15 to 17) | same | ν = −1 at 10 T: B 9.95 to 10.06 T, Vadg 0 to 2.6 V, ΔV1 = 234 ± 14 mV (233 ± 14.3 in the Supp), ΔB1 = 40.3 ± 6.7 mT. ν = −4/3 at 14 T: Vadg 1.5 to 2.1 V, ratio 0.37 ± 0.04, ΔB1/ΔB = 3.47 ± 0.79. Also ν = −1 at 14 T and ν = −2 at 10 T; TG check 2.9 ± 0.6 |
| Doubled gate period at stronger coupling | Fig. 3 (p. 5); S6, S7 (pp. 18, 19) | same | Side-gate series at −1/2, 2/3, 3/2; doubled-regime map at −5/2; ratio about 2 for all four states. Field ratio mixed (p ≈ 1 at 3/2, p ≈ 1/3 at −1/2). No doubling at −4/3 (Vsg 0.2, 2, 5 V) or −1/3 (Vsg −2, 0 V). Vsg safe limit about 6 V (p. 13) or 5 V (S6). |
| Temperature dependence | S16, S17 (pp. 28 to 30) | same | Steps of 12.7 to 70 mK, or 16 to 120 mK. e/4 suppressed between 50 and 70 mK; doubled regime at −1/2 and 2/3 persists to 120 mK. The fits do not identify the regime. |
| Displacement field per state | Fig. 1d (p. 3) | same | Circles at D between about −0.08 and +0.17 V/nm, B = 14 T |

**Counts found and missing:**
- Devices fabricated: not stated. "devices" appears in the author contributions (p. 9), and Fig. 1b shows "a device".
- Devices measured: one, implied ("The device was measured", p. 9).
- Devices that showed the effect: not stated.
- Cooldowns: not stated.
- Datasets: one minimal-excitation map and one doubled map per state, plus side-gate series. How many maps or tunings were tried per state is not stated.
- Whether ν = +1/2 and +5/2 (called "developing", p. 2) were tried: not stated.

## Entries matched, adapted and skipped
- **Matched and adapted (scope):**
  - `coulomb-dominated-interferometer`: written for an AB reading with a CD lookalike in a Fabry-Perot device. Here the paper reads CD in an antidot, so I used the reverse: an AB or mixed regime, where the gate period gives ν or νLL in place of the charge. Control used: the stripe slopes from Halperin et al.
  - `charge-trap-fractional-shift`: written for fractional shifts. Applied here to period ratios and gate instability.
- **Matched as is:** `fine-tuning-and-selection` (always included).
- **Checks walked:** charge family (`charge-regime-map`, `charge-control-regime`, `charge-repeat-sweeps`) and practice (`report-counts`, `report-ranges`, `report-processing`).
- **Skipped, because the device has no superconductor and makes no Majorana or Josephson claim:**
  - zbp, quantization and nonlocal families: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, micromagnet-stray-field, full-shell-flux-andreev, spin-orbit-length-pinning, exceptional-point-zero-mode.
  - local-probe-loophole (Majorana-specific).
  - island-states-coulomb-spacing (superconducting hybrid island).
  - Shapiro entries: shapiro-landau-zener, shapiro-nonlinear-resistance, transparent-junction-pi-crossing, switching-jump-blind-region.
  - field-enhanced-supercurrent-resonances, chiral-plateau-superconductor-short, false-poor-mans-majorana, diode-vortex-screening.
- **Also skipped:** `protocol-parameter-sensitivity`, because the paper has no automated pass/fail protocol. Its concerns about data windows and processing are covered by the `report-ranges` and `report-processing` checks.

## Sources held out
None. The library sources for the matched entries all predate this paper (27 Aug 2026), so none can cite it. I confirmed dates on their abstract pages:
- 2309.09368 v1: Sep 2023
- 2101.11456: Jan 2021
- 1010.4598: Oct 2010
- 2501.18631: latest version 25 Mar 2026

I did not grep their full texts.

## Related work: how each link was checked
I opened each arXiv abstract page and confirmed the ID, title and first author, and that the abstract supports my one-line description. All five were checked from the abstract only.
- 1010.4598: Halperin. Abstract states the stripe spacings and opposite slopes.
- 1201.1600: Kou. Abstract states field and gate periods, the number of charged edges, and 2e/3 with a single charged edge at 2/3.
- cond-mat/0007383: Kataoka. Abstract states that resonance through the outer spin states should occur twice per h/e period.
- 2412.11401: Hata. Abstract states that the area at 2/3 is significantly smaller than at 2 and 1, and assumes a constant gate capacitance.
- 2412.19886: Kim. Abstract states the 2Φ0 period at two even-denominator states and bulk quasiparticles of e/4.

Also opened but not listed:
- 0711.4746 (Sim, Kataoka and Ford review): abstract mentions h/2e oscillations and a capacitive-interaction model.
- 2509.04209 (same group's earlier coulombmeter paper).
- 2403.18983 (Werkmeister, telegraph noise).
- 1111.6475 (Rosenow and Simon).

## Library gaps
1. **Lever arm and reference calibration in period-ratio charge measurements.** A filling- or gate-dependent area or lever arm shifts ΔV/ΔV1. Source: Hata et al. 2412.11401, abstract. The library has no entry, and no check for using the reference at the same gate window, field and gate settings.
2. **Several charged edges bound to an antidot.** Interleaved resonances give an h/2e-type shortened period. Sources: Kataoka et al. cond-mat/0007383 and Kou et al. 1201.1600.
3. **The charge-family checks are written for shifts and interferometers.** A check for antidot charge spectroscopy would help, for example "measure the integer reference at the same field and gate windows" and "count the bound edges".
4. **`coulomb-dominated-interferometer` works in one direction only.** It is written for an AB reading; papers that read CD need the reverse.

## Unsure
- **The p values.** From the quoted numbers, ΔB1/ΔB comes out near 6.8, 3.1 and 7.6 for −5/2, −1/2 and 3/2, while the paper states p ≈ 10, 2 and 6. There may be an area correction or a definition I did not follow. I kept this out of the report beyond question 8.
- **The bound-edges row.** I chose "partly addressed (data bear on it)" over "not addressed" because the p values bear on the edge count. The paper does not discuss bound edges.
- **The regime row.** I chose "partly" over "ruled out". The minimal-regime ratios of about 0.25 do not match the AB expectations of 1/2 or ν that the paper lists. Even so, the paper itself says the temperature and DC-bias data are inconclusive about the regime.

## Skill issues
- Step 7 asks for reports/ files. This runner refused .md writes, so the report and notes went in the reply.
- The skill doesn't say how to handle a lookalike whose direction is reversed for a given paper (an AB reading versus a CD reading).
- The template's "What this is" says lookalikes "in topological transport". For a fractional quantum Hall charge paper that reads oddly, but I kept the template wording.
- flags.json has no "not applicable" status for checks, so I listed only the families I walked.
- "Ruled out and partly addressed need a verbatim quote" sits awkwardly with "the data bear on it; the paper doesn't discuss it". The quote then describes data and not a discussion. I used a data quote.
- The hold-out rule doesn't say whether checking dates is enough or a full-text grep is required.
- The word target (600 to 900) is tight once the template's fixed text, eight questions and five related-work lines are in. I ended near 910 words outside the table.
