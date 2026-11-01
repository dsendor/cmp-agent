# Run notes: arXiv 2609.38003v1

AI only. Lookalike assistant run on 2026-10-24.

## Library
- lookalikes.yaml meta.version 0.5 (updated 2026-10-24), 28 lookalike entries. Read once at the start, together with SKILL.md and report-template.md.

## What I read
- The arXiv abstract page (local copy abs.html): title, 22 authors, first author Filip Krizek, dated 2026-09-29, "14 pages, 4+5 figures". No ancillary files and no data or code link.
- The full text (local paper.txt), read in full: main text, Methods, Extended Data Figs. 1 to 5, references. Page numbers come from the page markers in the extracted text, checked against the PDF (14 pages).
- I rendered PDF pages 4, 5 and 11 and looked at Fig. 3, Fig. 4 and Extended Data Figs. 3 and 4 to judge the tests and read the field scales in question 5.
- I didn't fetch the paper itself. There was no data repository to open, so I counted devices from the text only. I didn't open the other files in the paper folder.
- I don't recognize this paper. It postdates my training data, so no later history was used.

## Claims table (step 1)

| Claimed signal | Figures | Device | Counts and ranges |
|---|---|---|---|
| Zero-field diode after zero-field cooling, η about 7% | Fig. 3a (with 50-sweep switching histograms) | 5 µm by 180 µm CuMnAs(12.4 nm)/AlAs(2.0 nm)/Al(9.2 nm) bar along [010], four-terminal, 20 mK | One bar shown. Cooldowns not stated. Switching threshold 50 µV, 0.2 s step delay |
| Polarity reversal after ±1 T [100] preparation | Fig. 3b | same bar | Preparation ±1 T; 8-sweep averages |
| η against preparation field: reversal for [100], weak and mostly one sign for [010] | Fig. 3d,e | same bar | [100] from -1 to 1 T; [010] from -4 to 4 T; reset field value not stated |
| Same axis dependence on an orthogonal bar | Extended Data Fig. 4 | bar along [100], same wafer as stated | [100] ±1 T, [010] about ±5 T. No ZFC or histogram data shown for this bar |
| Hysteretic and remanent even-in-current nonlinear resistance, matching the axis anisotropy | Fig. 4a to c | reference CuMnAs bar with 3 nm oxidized Al cap, from a different wafer, 20 µm by 10 µm, 5 K, ±4 mA | In-field [100] ±5 T, [010] ±2 T; remanent [100] ±5 T. Remanent Reven crosses zero near ±1.5 T (read from Fig. 4c), while η in Fig. 3d reverses near ±0.1 T (read from Fig. 3d) |
| Net moment bound of 3e-3 µB/Mn | Fig. 2b, Methods p. 7 | wafer pieces 3 mm by 5 mm, several positions across the 2-inch wafer | Number of pieces not given |
| Proximity tuning through AlAs thickness | Fig. 2c, Extended Data Fig. 3 | 2.0 nm wafer (Tc about 350 mK) and 1.5 nm wafer (no transition to 20 mK) | Two wafers |

Missing counts: bars fabricated and measured on the 2.0 nm wafer, cooldowns, how many bars showed the effect, the reset-field magnitude in the Fig. 3c protocol, whether the two diode bars shared a chip, the magnet type and its remanence.

## Entries matched, adapted, skipped
- Matched: diode-vortex-screening (diode family) and fine-tuning-and-selection (always).
- Adapted: micromagnet-stray-field. Its signature is zero-bias peaks, but the physics (a magnet's stray field breaking time-reversal symmetry locally in a trivial superconductor) maps onto a stray-field diode from uncompensated moments, which the paper itself raises (p. 6, ref. 30). I kept its three tests, with "magnet" read as the CuMnAs layer.
- Skipped, because they need tunneling spectroscopy, nanowires, islands, Shapiro steps, Kitaev chains, interferometers or charge sensing, none of which the paper has: abs-quantum-dot, quasi-majorana-smooth-confinement, disorder-induced-zbp, crowded-trivial-subgap-states, kondo-resonance, weak-antilocalization, fine-tuned-plateau, series-resistance-subtraction, one-end-only, trivial-andreev-band-gap-reopening, full-shell-flux-andreev, chiral-plateau-superconductor-short, island-states-coulomb-spacing, shapiro-landau-zener, shapiro-nonlinear-resistance, switching-jump-blind-region, transparent-junction-pi-crossing, charge-trap-fractional-shift, coulomb-dominated-interferometer, false-poor-mans-majorana, spin-orbit-length-pinning, exceptional-point-zero-mode, local-probe-loophole.
- Skipped field-enhanced-supercurrent-resonances: its signature is a supercurrent that grows with field, which is not claimed here.
- Skipped protocol-parameter-sensitivity: the paper uses no automated pass/fail protocol.
- Checks: the library has no `checks` block for the diode family, so I walked only the three practice checks.

## Judgment calls
- diode-vortex-screening, "Effect followed against field, sample width or edge quality": marked part. The paper follows η against the preparation field and crystal axis on two bars, but shows no η against the applied field at measurement and no width or edge series.
- micromagnet-stray-field, "Magnet switching": marked part, because the switching is shown on a reference bar from another wafer at 5 K, and not on the superconducting device. "Stray field bounded": marked part, because SQUID bounds the net moment of a 3 mm by 5 mm piece, which doesn't bound local fields at edges or domain walls of a 5 µm bar.
- I didn't count the two-bar comparison (Extended Data Fig. 4) as enough on its own to rule out field artifacts. A sample tilt in a fixed mount would give an out-of-plane field component for one in-plane magnet axis and not the other, which would follow the chip axes for both bars if they share a chip. That is unknown, so it became question 6.
- Outside rows take their tests from the controls Jiang et al. describe: field dependence after each poling sign (their Fig. 3), in-plane versus out-of-plane poling (their Appendix E), and a field sensor measured alongside the sample (their Appendix D).
- I marked magnet remanence "not mentioned": the paper mentions "spurious flux trapping" in the sample but never the magnet's own remanent field.
- Question 5 rests on values read from the figures (η sign change near ±0.1 T in Fig. 3d, Reven zero crossing near ±1.5 T in Fig. 4c). Worth a human look.

## Sources held out
- None. No library source I relied on cites this paper. The library sources dated 2026 (Legg 2502.19560v2, Akrap et al. 2501.18631v2) were not opened in this run, so I couldn't confirm by opening them that they don't cite it. Their quoted passages don't mention it.

## Related work, how each was checked
- 2205.09276 (Hou et al.): abstract page opened, ID, title and first author confirmed; abstract read via the arXiv API.
- 2512.05427 (Jiang et al.): abstract page opened and confirmed; full text read (PDF, results section, Appendices D and E). This is the source for both outside rows.
- 2601.03366 (Sachin et al.): abstract page opened and confirmed; abstract read.
- 2608.19099 (Sun et al.): abstract page opened and confirmed; abstract read.
- 2610.16972 (Cruz et al., later than the paper under review): abstract page opened and confirmed; abstract read. Described for its own results only.
- Also read but not listed: 2502.08928 (Terashima et al., abstract), on apparent nonreciprocity from contact heating and thermoelectric voltages. I left it out of the table because a contact artifact isn't expected to reverse with the preparation field. It could add a fixed offset to η, like the 7% ZFC value or the one-sign [010] response.

## Library gaps
- No `checks` block for the diode family (suggested steps: plain-superconductor control, η(H) near zero, magnet remanence calibration, out-of-plane versus in-plane preparation, two bar orientations).
- No entry for trapped flux set by a poling or preparation field (source: 2512.05427).
- No entry for superconducting magnet remanence at nominal zero field (source: 2512.05427, Appendix D).
- No diode-specific stray-field entry. Domain stray fields giving field-free diodes appear in 2610.16972.
- Possible entry: contact heating and thermoelectric artifacts in nonreciprocal transport (2502.08928).

## Skill issues
- Step 3 says to walk "the checks for the paper's family", but the diode family has none. It's unclear whether to borrow checks from another family or walk practice checks only. I did the latter.
- It's unclear how to mark a test shown on a reference sample from another wafer and temperature (Fig. 4). I marked it part.
- Step 5 says to take an outside row's tests "from the control that paper describes". When that paper describes several controls for different artifacts, it's unclear whether one paper may seed two rows. I made two rows from Jiang et al.
- Scope rule: adapting an entry from another family (zbp) for a paper in the library's diode family isn't covered explicitly. I treated it as matching on physics under step 2.
- The 600 to 900 word target is hard to reach with the template's sections alone once the table is excluded. I kept to the template and didn't add sections.
