# Run notes: arXiv 2608.27444v1

AI only. Lookalike library version 0.5 (meta.updated 2026-10-24). Run date 2026-10-24.

## What I read
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all 28 entries and the full checks section). No other file in cmp-assistant/ was opened. scripts/read_mtx.py not used (no figure data).
- The paper from local copies, per the caller: abs.html (title "Trapping $e/4$ quasiparticles in bilayer graphene", 7 authors, first author Mario Di Luca, v1 submitted 2026-08-27, cond-mat.mes-hall), paper.txt (main text, Methods, Supplementary sections D to M), and paper.pdf pages 3 to 7 rendered as images to read the axes of Fig. 2, Fig. 3 and the values in Fig. 4a. I also ran pdftotext on the PDF to check quotes that the two-column paper.txt split. The paper itself was not fetched.
- Supplementary material is in the PDF and was read (text and captions; figures S4 to S17 not viewed as images).
- Data repository: none linked. Data availability says "available from the corresponding author upon reasonable request" (p. 10). No arXiv ancillary files referenced.
- I did not recognize the paper (it postdates my training data); no later history used.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| e/4 localized charge at ν = −5/2 | Fig. 2a,e; Fig. 3l (doubled); Fig. S8; Fig. S16a,b | one device ("the device") | B 13.930 to 13.965 T (about 35 mT), Vadg −3.60 to −2.90 V; ∆V = 62.8 ± 5.6 mV, ∆B = 5.9 ± 2.6 mT; ∆V/∆V1 = 0.27 ± 0.03; one map shown per regime; weakest oscillations (Fig. S8) |
| e/4 at ν = −1/2 | Fig. 2b,f; Fig. 3 side-gate series (caption d to f; panels labeled g to i in the figure) and 3m; Fig. S9; Fig. S16c,d | same | B 13.90 to 14.00 T, Vadg −3.30 to −2.90 V (Fig. 2b) and 0.98 to 1.60 V (Fig. 3 series); ∆V = 55.8 ± 5.1 mV, ∆B = 13 ± 1.4 mT; ratio 0.24 ± 0.03 |
| e/4 at ν = 3/2 | Fig. 2d,h; Fig. 3j,k,o; Fig. S11; Fig. S16g,h | same | B 13.93 to 14.00 T, Vadg 0.55 to 1.05 V; ∆V = 57.5 ± 4.7 mV, ∆B = 5.3 ± 1.4 mT; ratio 0.25 ± 0.03 |
| e/3 at ν = 2/3 | Fig. 2c,g; Fig. 3 (2/3 series), 3n; Figs. S10, S13 to S15 | same | B 13.90 to 14.00 T, Vadg 2.74 to 3.44 V; ratio 0.32 ± 0.03; ∆B1/∆B = 2.32 ± 0.93; 20 repeated sweeps at fixed B with gate hysteresis in the first 6 |
| Calibration: ν = −1 (10 T and 14 T), ν = −2 (10 T), ν = −4/3 and −1/3 (14 T) | Fig. 1e to h; Figs. S3 to S7 | same | ∆V1 = 233 ± 14.3 mV, ∆B1 = 40.3 ± 6.7 mT at 10 T; −4/3 ratio 0.37 ± 0.04 and ∆B1/∆B = 3.47 ± 0.79; ADG versus TG comparison 2.9 ± 0.6 |
| Crossover to doubled gate period (two explanations left open) | Fig. 3, Fig. 4; Figs. S6, S7, S16, S17 | same | side gates up to about 6 V (5 V used at −4/3: 0.2, 2, 5 V; −1/3: −2, 0 V); temperatures 16, 30, 50, 70, 95, 120 mK (one panel 12.7 to 70 mK) at 13.95 T |

Other numbers: AC current 0.2 to 1 nA at 17.777 Hz, chosen per filling; base temperature about 10 mK, electron temperature 30 to 50 mK quoted; field step 1 mT, about 101 points per scan; third-order polynomial background and two-point moving average along B.

Missing counts: devices fabricated and measured (only "the device" and "a device with the air-bridge"), cooldowns, datasets per filling, full gate, field and displacement ranges explored, how the shown tunings were selected, whether the developing states at ν = +1/2 and +5/2 were tried.

## Entries matched, adapted and skipped
- Matched: coulomb-dominated-interferometer (adapted), charge-trap-fractional-shift (adapted), fine-tuning-and-selection (always).
- Adapted: coulomb-dominated-interferometer is written for a Fabry-Perot interferometer read as AB; here the antidot claim is CD and the lookalike is an AB or mixed regime where the gate period does not give the charge. Its slope test is replaced by the field-period comparison the paper uses (AB limit gives ∆B1/∆B = 1), since the paper says the slope method is not applicable with the ADG (p. 3). charge-trap-fractional-shift is written for fractional shifts; here the signal is a fractional period, so I read it as a coupled charging region adding features at a fraction of the period. Its two-gate-map test I counted as part from the side-gate series in Fig. 3.
- Status for coulomb-dominated-interferometer: one test shown for all, but the field period alone excludes only the pure AB limit and leaves a mixed regime open, so not ruled out.
- Skipped: all zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev, diode entries (no superconductor, no Majorana or Josephson signal). local-probe-loophole (Majorana-specific). protocol-parameter-sensitivity (no automated pass/fail protocol in the paper).
- Checks walked: charge family (charge-regime-map, charge-control-regime, charge-repeat-sweeps) and practice (report-counts, report-ranges, report-processing).

## Sources held out
None. The matched entries' sources (1010.4598, 2309.09368, 2101.11456, 2501.18631) all predate the paper or are revisions whose quoted passages do not discuss it. I did not open their full texts to confirm, so this rests on dates and quotes.

## Related work: how each link was checked
All five: ID, title and first author confirmed on the arXiv abstract page (arxiv.org/abs/<id>, citation meta tags), and the one-line description checked against the abstract text from the export.arxiv.org API. Full texts not read.
- 2509.04209 (Di Luca, Fractional Coulombmeter): abstract.
- 2504.16750 (Di Luca, Tunable inter-edge interactions): abstract.
- 1201.1600 (Kou, Coulomb Oscillations in Antidots): abstract.
- 2412.19886 (Kim, AB Interference in Even-Denominator FQH States): abstract.
- 1010.4598 (Halperin, Theory of the Fabry-Perot QH Interferometer): abstract (also a library source).
Also opened but not listed: 2010.11394 (Mills, graphene antidots, e/3), 2606.24831 (Thamm, antidot interferometry theory).

## Library gaps
- No entry for antidot charge measurements specifically (CD versus AB or mixed regime in an antidot, and "gate period gives the change in localized charge, not the tunneling charge", which the paper itself stresses on p. 3).
- No entry for gate hysteresis or history dependence corrupting period extraction (Fig. S13 shows it at ν = 2/3).
- Considered and not added as an outside row: a filling- or field-dependent gate lever arm between the 10 T reference and the 14 T data. I found no paper I opened that shows it, so it went in as question 5.

## Unsure or worth a second look
- Text p values ("p = 10, 2, and 6", p. 4) differ from Fig. 4a (about 6.8, 3.1, 7.6, which also match 40.3 mT divided by the quoted ∆B values). Raised as question 6.
- Fig. 3 caption says d to f are ν = −1/2 and g to i are ν = 2/3, while the panels are labeled the other way; the text on p. 6 follows the panels. P. 7 writes "ν = −2/3" where 2/3 seems meant. Not put in the report.
- "Field and gate map with stripe slope and spacing" marked all with an equivalent named; a stricter reading (slope not done) would make it part. Status is Tested in part either way.
- Report is about 1000 words outside the table, above the 600 to 900 target, mostly from the six quoted checks and eight questions.

## Skill issues
- Done/partly and all/part are defined by coverage of the evidence presented. For multi-part checks and tests (counts, processing with data and code, slope and spacing) where one part is done for all evidence and another is not, the skill doesn't say which mark to use. I used partly or part, or all with a named equivalent.
- Library entries are written for one reading direction (coulomb-dominated-interferometer assumes an AB claim). The skill says match on the physics, and it doesn't say how to handle a paper that claims the opposite regime.
- "Scope" asks for one sentence under "What this is" only for a different kind of measurement. This paper is in the charge family and still needed adapted entries, so I added the sentence anyway.
- Step 7 says to write reports/<id>.md and notes files; this run's caller asked for them in the reply. I followed the caller.
- The four standard questions plus paper-specific ones share the cap of eight, so the paper-specific room is four. That could be stated outright.
