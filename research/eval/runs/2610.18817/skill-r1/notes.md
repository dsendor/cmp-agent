# Run notes: arXiv 2610.18817v1

AI only. Lookalike assistant run on 2026-10-23. Library `meta.version` 0.4.

## What I read
- arXiv abstract page (local abs.html): title "Single anyons and anyon binding in a quantum Hall dot", Valentini et al. (13 authors, last Young), v1 dated 2026-10-13. There are no ancillary files.
- Full text (local paper.txt), all 24 PDF pages: main text, Methods, Tables I-III and Extended Data Figs. 1-11. I used pdftotext per page on paper.pdf to confirm the page number of each quote. PDF page numbers match the printed ones.
- The paper links no data repository and has no data or code statement, so I counted no devices from external data. There are no .mtx files, so I did not run read_mtx.py.
- Everything I tried to open, I could open.
- I did not read the other files in the paper folder (prompt_*.txt).
- I did not recognize the paper. It postdates what I know, and I used no knowledge of its later history.

## Claims (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Integer dot benchmark: Coulomb diamonds, EC ≈ 2 meV, dot in the hole | Figs. 1f-g, ED Fig. 2 | single device, 90 nm hole | B = 5 T; gate maps in ED Fig. 2 |
| Spin blockade, emptied to the last quasihole at ν = 1 | Figs. 2a-i | same | Vdot −3 to 4 V at 5 T; excited states 0.3-0.8 meV |
| e/3 resonances, period about 1/3 of ν = 1 | Figs. 1h-j, ED Fig. 3 | same | δ 80-100 mV versus 250-300 mV; 1j at 5, 8.97, 13.4, 13.5 T; Te saturates near 110 mK |
| Single-anyon dot, Nqp = 0 to 5, irregular addition energies matched by DMRG | Figs. 3a-g, ED Figs. 6-8 | same | Nqp = 0 calibrated at ν = 1, 4.5 T; the few-quasihole regime was not reached (p. 5) |
| Regular versus irregular spectra at abs(Nqp) ≈ 10-20 | Figs. 4a-d, ED Figs. 9-11 | same | gate sweeps of VT, Vedge, Vqpc and D |
| Missing sector and 2e/3 steps, EB ≥ EC | Figs. 4e-g | same | VT 0.040-0.050 V, Vdot 3.785-4.5 V, VDC = 55 µV, 13.5 T |

- Missing: devices fabricated, devices measured and devices that showed the effect (the Author Contributions say "devices" in the plural); datasets per regime; the full ranges explored.
- Cooldowns: two. Cooldown 1 used lock-in and cooldown 2 used DC. Table I suggests Fig. 1j mixes both (the 13.77 and 17.77 Hz rows), while Figs. 3-4 are DC, from cooldown 2.

## Entries matched, adapted, skipped
- Matched and adapted: charge-trap-fractional-shift, from fractional shifts to period tripling and the hidden-charging route to missing sectors. Frolov Example 4 says the side dot carries little current.
- Matched and adapted: island-states-coulomb-spacing, from Majorana hybrid islands to orbital even-odd structure in an FQH dot.
- Always included: fine-tuning-and-selection.
- Skipped coulomb-dominated-interferometer. The paper reads the oscillations as Coulomb blockade of a dot, not Aharonov-Bohm interference, so this lookalike cannot stand in for the claim. I still walked its check, charge-regime-map.
- Skipped protocol-parameter-sensitivity. There is no pass/fail protocol; the dip-finding algorithm is covered under report-processing and the resolution question.
- Skipped every zbp, quantization, nonlocal, shapiro, supercurrent, chiral, kitaev and diode entry. There is no superconductor, Josephson junction, chiral Majorana or Kitaev chain. That includes series-resistance-subtraction: no quantized-value claim, and a four-terminal QPC measurement.
- Skipped local-probe-loophole. It is Majorana-specific.

## Sources held out
- None. All library sources predate 2026-10-13. I checked the submission histories of 2309.09368 (v1, 2023), 2501.18631 (v2, 2026-03-25), 2101.11456 (2021) and 2203.07829 (v3, 2022). The rest are 2011-2025.
- Note: Marco Valentini is first author of both this paper and library source 2203.07829. That source does not discuss this paper, so it is not held out.

## Related work checks
- 2005.12723: abstract page. Confirmed the ID, the title and Röösli as first author, plus e*/e = 0.32 ± 0.03 and the two-compressible-region model.
- 2502.00124: abstract page. Confirmed Liang as first author, plus the Φ0/2 from capacitive coupling and e* = 1 in operando.
- 2312.03150: abstract page. Confirmed Werkmeister as first author, plus apparent pairing from repulsive coupling and charge quantization.
- 2309.09368: abstract page and full text of v1 (Example 4, p. 9). Confirmed Frolov as first author, plus the 1/3-period jumps and the side dot.
- 2603.11182: abstract page. Confirmed Henzinger as first author, plus the gate-controlled dot and the controlled phase slips.
- Also opened but not listed: 1409.4427 (Choi et al., pairing) and 2312.14767 (Yang et al., pairs and triplets).

## Library gaps
1. Apparent pairing, or a doubled charge step, from capacitive coupling between a probed compressible region and a hidden one (Liang 2025; Werkmeister 2023). I added it as "not in library".
2. Inferring e* from the ratio of gate periods assumes a fixed Cd and lever arm across fillings and gate settings. I found no source to cite, so it appears as question 8 and is not in the table.
3. "Missing charge sector" claims need a resolution bound (temperature, bias, gate step). No entry covers this.
4. There are no `checks` for the island family, and the charge-family checks are written for interferometers and side-dot jumps.

## Unsure
- The cooldown assignment of Fig. 1j is inferred from Table I's frequencies.
- The Fig. 1i caption gives EC = 3e ΔVDC. The conversion looks unusual next to EC = e* ΔVDC; I left it out of the questions to stay within eight.
- Methods give lock-in frequencies of 13.333 or 17.777 Hz, while Table I lists 13.77 and 17.77 Hz.
- The abstract page says the binding energy is "as large as" the charging energy; the PDF says "at least as large as".
- For the adapted rows, I chose "partly addressed" because the paper discusses each alternative and does not test it directly.

## Skill issues
- Step 7 names reports/<id>.md and reports/<id>.notes.md; this run used the caller's paths and names instead.
- The harness Write tool refused the two .md files. Only flags.json was written; the report and notes were returned as text.
- The template says "<short title>", while step 7 says to use the arXiv abstract page title. I used the full title.
- The Scope rule does not say which `checks` to walk for adapted families, or whether to walk a check whose lookalikes were all skipped (charge-regime-map).
- For a paper with two claims, it is unclear whether a status is set per claim or overall. I judged the adapted rows against the binding claim.
- The 600-900 word target sits close to the minimum content the steps require (six checks, eight questions, five related papers).
- Status rules say a quote is required, but not how to handle data that bear on a lookalike only at a different filling (the lever-arm test at ν = 1). I chose "partly".
