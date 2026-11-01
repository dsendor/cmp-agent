# Run notes: arXiv 2609.38003v1

AI only. Run on 2026-10-23. Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.4 (updated 2026-10-23), 28 lookalikes, checks for families zbp, shapiro, kitaev, charge, practice.

## What I read
- Skill: skill/SKILL.md and skill/report-template.md, read once at the start, plus the whole library including `checks`.
- Paper: the pre-extracted text (paper.txt, 14 pages: main text, Methods, Extended Data Figs. 1 to 5 captions, references) and the saved abstract page (abs.html: title, 22 authors, submitted 29 Sep 2026, "14 pages, 4+5 figures"). I had no PDF, so figure details come from the captions and garbled axis labels. Page numbers come from the page markers in the extracted text (each marker sits at the top of its page). I did not fetch the paper itself.
- No ancillary figure data, and the text has no data repository link or availability statement, so read_mtx.py was not used and I did not open a repository.
- Following the instructions, I read no other file in cmp-assistant/ and did not look at git history.
- I don't recognize this paper and used no knowledge of its later history.

## Could not open
- OpenAlex: every request returned "Rate limit exceeded" (the free daily budget for this IP was used up, and it asked for an API key). I didn't request a key. Nothing depended on it.
- The arXiv website search returned few or no parsed results for most queries. The export.arxiv.org API worked, with a 3 s wait between calls.

## Claims table (step 1)
| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Field-free SDE after zero-field cooling, η ≈ 7%, switching distributions well separated | Fig. 3a and inset (p. 4), text p. 3 | 5 µm x 180 µm CuMnAs(12.4 nm)/AlAs(2.0 nm)/Al(9.2 nm) bar along [010], four-terminal, 20 mK | 50 sweeps per polarity for the distributions; one bar; cooldowns not stated |
| Remanent polarity set by a preparation field along [100], η up to about ±20%; preparation along [010] weaker with no systematic sign reversal | Fig. 3b to e (p. 4) | same [010] bar | preparation along [100] to ±1 T, along [010] to ±4 T (axes); 8-sweep averages; reset field size and temperature during preparation not stated; number of repeat loops not stated; measured only at H = 0 and 20 mK |
| Same axis dependence in an orthogonal bar | Extended Data Fig. 4 (p. 11) | second bar along [100] | ranges as Fig. 3d,e; raw switching currents not shown |
| Néel-state link: hysteretic, anisotropic even nonlinear resistance; remanent Reven reverses with preparation along [100] | Fig. 4 (p. 5), text pp. 5 to 6 | separate CuMnAs wafer with a 3 nm fully oxidized Al cap, 20 µm x 10 µm bar, 5 K, ±4 mA (p. 8) | preparation along [100] "from −5 to 5 T" (p. 5); not measured on the superconducting heterostructure |
| [100] easy axis | Extended Data Fig. 5 (p. 12) | CuMnAs epilayer, XMLD-PEEM at about 100 K, 10 µm x 10 µm field of view | one region shown |
| Proximity tuned by the AlAs thickness | Fig. 2c (p. 3), Extended Data Figs. 2 and 3 | 2.0 nm barrier (Tc ≈ 350 mK) vs 1.5 nm reference (no transition to 20 mK) | two samples |
| Negligible net magnetization | Fig. 2b (p. 3), Methods p. 8 | heterostructure pieces from edge to center of the 2" wafer, plus MnAs reference | upper bound 3×10^-3 µB/Mn; SQUID measurement temperature not stated |

Missing counts: bars fabricated and measured, chips, cooldowns, repeat loops, temperature dependence of η, η versus applied field, the magnet type and how its residual field was handled, and the temperature during preparation.

## Matching (step 2)
- Matched: diode-vortex-screening (family diode), fine-tuning-and-selection (always).
- Adapted: diode-vortex-screening, whose signature reads "exotic pairing", applied to the claim of antiferromagnetic control. micromagnet-stray-field (family zbp) adapted from "Andreev states in dots" to "stray field from the magnetic layer acting on the superconductor's critical current", keeping its control (magnet switching, field mapping, devices without the magnet).
- Skipped: all zbp, quantization, nonlocal, island, chiral and kitaev entries (no tunneling spectroscopy, zero-bias peaks or quantization). All shapiro entries (no microwave irradiation, no Josephson junction). field-enhanced-supercurrent-resonances (the claim is direction asymmetry at zero field, not a supercurrent growing with field, and there is no junction). charge entries (no fractional shifts). local-probe-loophole (Majorana-specific). protocol-parameter-sensitivity (no pass/fail protocol; the 50 µV threshold is a data choice, which I covered under report-processing).
- Checks walked: practice only (report-counts, report-ranges, report-processing), all "partly". The library has no `checks` block for family diode.

## Hold-out
- No library source discusses this paper. I judged this from dates and titles: every library source except the 2026 versions of Frolov, Legg and Akrap predates 29 Sep 2026, and those three are about other subjects. Of the library sources, I opened only Hou et al. 2205.09276. Nothing was skipped.
- The search results listed the paper under review, and I didn't open it.

## Related work: how each was checked
- 2205.09276 Hou et al.: abstract page opened; ID, title and first author confirmed; the description matches the abstract.
- 2512.05427 Jiang et al.: abstract page and full text (PDF) opened. Confirmed the sign is set by a poling field (abstract), and in Appendix D (p. 10) the magnet hysteresis correction: "Because a superconducting magnet was used in this study, hysteresis due to the magnet should be observed at low magnetic fields after applying a large magnetic field." and "the magnetic field values of ≈ ±15 mT were shifted". Their own controls: a few-layer graphene field reference, and no hysteresis for out-of-plane fields (Appendix E).
- 2205.12196 Golod and Krasnov: abstract page opened; ID, title and authors confirmed.
- 2506.17651 Li et al.: abstract page opened; confirmed.
- 2601.03366 Sachin et al.: abstract page opened; confirmed.
- Also opened and not listed: 2206.00483 Narita et al. (abstract).
- All of these predate the paper under review, and refs. 10 and 28 to 30 of the paper cite four of them. They are listed for their own results.

## Outside-library lookalikes (library gaps)
1. Residual field of the superconducting magnet at nominal zero after a preparation excursion. Source: Jiang et al. 2512.05427, Appendix D. Control: an in-situ field reference.
2. Flux trapped in the superconductor by a poling or preparation field, giving a sign-switchable zero-field diode. Sources: Jiang et al. 2512.05427 (abstract), Golod and Krasnov 2205.12196. Control I suggested: a thermal cycle above Tc and below the Néel temperature.
3. The library needs a `checks` block for family diode: field calibration at zero, η versus small field, a plain-film control, thermal cycling, and the stray field of the magnetic layer.
4. micromagnet-stray-field is written for zero-bias peaks; a diode-family version (stray fields from magnetic layers, as in Li et al. 2506.17651) would avoid the adaptation.

## Unsure
- Statuses: I set all five rows to "partly addressed". The [010] vs [100] contrast and the orthogonal bar bear on every field-history lookalike without discussing them. If the coils are fixed to the crystal axes, the contrast does not separate a coil artifact from a crystal-axis effect, so I didn't rule anything out.
- Stray-field estimate: 3e-3 µB/Mn x 2 Mn per 3.80 x 3.80 x 6.32 Å^3 cell gives M ≈ 600 A/m, so µ0M ≈ 0.76 mT. This is my arithmetic, labeled rough in the report. The stray field outside a thin in-plane film is much smaller than µ0M except near edges and domain walls.
- Refs. 28 to 30 (Hou, Jiang, Li) appear in the reference list but not in the extracted body text. A sentence may have been lost in extraction (there is a double space before "We therefore conclude", p. 6), so the report phrases this as "I couldn't find where the v1 text cites them".
- Fig. 4c: the text says preparation from −5 to 5 T, while the axis ticks show ±4. The garbled axis text may hide the endpoints, so I didn't raise it.
- Report length is about 910 words outside the table, slightly above the 600 to 900 target.

## Skill issues
- Step 3 assumes a `checks` block exists for the paper's family. Family diode has none, and the skill doesn't say what to do (I used practice only).
- Scope: the description says "claims a topological signature", but the library has a diode family whose entry reads "exotic pairing". A claim of magnetic control that isn't topological sits in a grey zone; the adaptation sentence covered it.
- Outside rows: the template doesn't say where the outside source's URL goes. I put it in the Lookalike cell, which strains "one quote and one clause".
- Hold-out rule: it doesn't say whether screening by title and date is enough, or whether every library source must be opened to check that it doesn't cite the paper.
- The skill says OpenAlex "needs no key". In practice the shared free budget ran out and it asked for a key, and the skill gives no fallback for DOI checks.
- Step 7 tells the skill to write reports/<id>.md and .notes.md; this run's instructions overrode that (inline output).
- Page numbering from extracted text with no PDF is not covered; I used the page markers.
- Quotes that span a page break with figure text in between can't be quoted verbatim from the extracted text. I swapped in a caption quote.
