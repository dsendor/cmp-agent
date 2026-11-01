# Run notes: arXiv 2608.27444v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries).
- Skill and template read once at the start: cmp-assistant/skill/SKILL.md and report-template.md.
- Paper read: the extracted text only (main text, Methods, Supplementary Sections D to M, figure captions), as the task instructed. I did not fetch the abstract page or PDF. The title comes from the text header. I could not view the figures, so all figure details come from captions and text. Page numbers follow the page breaks in the extracted text.
- Data repository: none linked ("available from the corresponding author upon reasonable request", p. 10). There were no ancillary files, so read_mtx.py was not used.
- I did not recognize this paper. I know no later history for it.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| e/4 localized charge at ν = −5/2, −1/2, 3/2 (∆V/∆V1 = 0.27, 0.24, 0.25 ± 0.03; ∆B = 5.9 ± 2.6, 13 ± 1.4, 5.3 ± 1.4 mT; p ≈ 10, 2, 6) | Fig. 2a,b,d,e,f,h; Figs. S8, S9, S11 | One device ("The device was measured", p. 9) | B = 14 T; ADG periods 56 to 63 mV; dB = 1 mT with NB ≈ 101 points per scan; Iac 0.2 to 1 nA; T base about 10 mK, electron T 30 to 50 mK claimed. Devices fabricated: missing ("fabricated the devices"). Cooldowns: missing. ADG windows: not given numerically. |
| e/3 at ν = 2/3 (∆V/∆V1 = 0.32 ± 0.03; ∆B1/∆B = 2.32 ± 0.93) | Fig. 2c,g; Figs. S10, S13 to S15 | Same | 20 repeated sweeps at 14 T (Fig. S13); histogram ∆B = 19.6 ± 4 mT; several fields, count not given |
| Reference ∆V1 = 233 ± 14.3 mV, ∆B1 = 40.3 ± 6.7 mT at ν = −1, 10 T; checks with ν = −1 at 14 T, ν = −2, ν = −4/3 | Figs. S3, S4, S5 | Same | 10 T and 14 T |
| Doubled gate period at stronger side-gate coupling for ν = −5/2, −1/2, 2/3, 3/2; absent at −4/3 and −1/3 | Fig. 3, Fig. 4, Figs. S6, S7 | Same | Side gates up to 5 V ("approximately 6 V" limit); −4/3 at 0.2, 2, 5 V; −1/3 at −2, 0 V |
| Temperature dependence | Figs. S16, S17 | Same | T = 16 to 120 mK (12.7 to 70 mK for panel a), B = 13.95 T |
| States characterized but not measured for oscillations | Fig. 1d | Same | Developing states at ν = +1/2 and +5/2 |

## Entries matched, adapted, skipped

- Family: charge (checks charge-regime-map, charge-control-regime, charge-repeat-sweeps), plus practice.
- Matched and adapted: coulomb-dominated-interferometer. The library entry is a Fabry-Perot interferometer read as AB. Here the device is an antidot read as CD, and an AB or mixed regime is the lookalike for the charge reading (the paper's own Fig. 4c and Ref. 48). I adapted the direction of the reading.
- Matched and adapted: charge-trap-fractional-shift. The claim here is a fractional period, not a fractional shift. The entry applies through the ν = 2/3 gate instability and to the period extraction.
- Matched: fine-tuning-and-selection (always).
- Skipped: protocol-parameter-sensitivity (there is no pass/fail protocol; range and processing questions are covered by the practice checks). I also skipped all zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries, and local-probe-loophole: they need superconducting hybrids, Majorana claims, Josephson junctions or diodes, none of which apply to a quantum Hall antidot.

## Sources held out

- None. No library source discusses this paper. All but two predate it. Akrap/Frolov 2026 (v2) and Legg 2026 (v2) treat unrelated subjects; I did not open them to confirm.

## Related work: how each was checked

All five were checked through the arXiv API abstract record (ID, title, first author, abstract). I read no full texts.
- 1010.4598 Halperin et al.: abstract, matches the stripe-slope description (also a library source).
- 1201.1600 Kou et al.: abstract, matches.
- 2509.04209 Di Luca et al. (v2): abstract, matches. This is the authors' own prior work (Ref. 30).
- 2412.19886 Kim et al.: abstract, matches. The published version is Ref. 22 (Nature 2026).
- 1010.4494 Hackens et al.: abstract, matches. This is Ref. 62 of the paper.
- Also opened but not listed: 2010.11394 (Mills, Averin, Du, graphene antidots, e/3 at ±1/3) and 2602.08468 (Alkalai et al., e/4 at ν = 1/2 in GaAs; I saw the title only, so it was not used).

## Library gaps

- Outside row "Coulomb island in a constriction", from Hackens et al. 2010 (https://arxiv.org/abs/1010.4494). A localized island in the constriction can produce Coulomb oscillations unrelated to the intended loop. The control Hackens describes is scanning gate imaging of the island location. I framed the tests as locating the oscillating state (imaging or lever arms) and comparing loop areas. A candidate new charge entry.
- The library has no antidot entry and no entry for gate-period ratio calibration: the choice of reference state and field, and a lever arm that differs between fillings. Question 7 covers this. A candidate check step for the charge family.
- The charge family has no entry for gate hysteresis or two competing configurations (the ν = 2/3 instability).

## Unsure

- Slope test: the captions give periods but not the stripe slope sign, so I marked the map test "part". The figures may answer it.
- charge-trap row: I marked the first test "all" from the integer and odd-denominator controls at the reference periods, though ν = −1 at 14 T "exhibit substantially stronger fluctuations".
- Gate leakage: the fabrication-time monitoring is a sentence with no data, so I marked it "no".
- I chose "partly" over "done" for charge-regime-map because of the slope sign and the ν = 2/3 FFT.

## Skill issues

- The skill assumes an arXiv fetch, but this run was text-only with no abstract page. The template asks for "the title on the arXiv abstract page", so I took it from the text header.
- "Signature" matching for charge-family entries is narrow ("shifted by a fraction of a period"), while the checks section covers "fractional periodicity". It was unclear whether charge-trap-fractional-shift should match a periodicity claim; I matched it.
- coulomb-dominated-interferometer reads only in one direction (AB claimed, CD lookalike). For a paper claiming CD, it has to be inverted, and the skill does not say whether that counts as adapting.
- The outside-row test wording is left to the runner ("take its tests from the control that paper describes"). When the cited paper's control is a technique such as scanning gate microscopy that the authors cannot easily run, it is unclear whether lever-arm or area analyses count as equivalent.
- The ruled-out rule ("one test ... that by itself separates") is hard to apply when a test separates the lookalike for some states but not others, as with the ν = 2/3 field ratio. I used "Tested in part".
