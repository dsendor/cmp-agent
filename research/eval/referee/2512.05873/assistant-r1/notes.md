# Run notes: 2512.05873v1

**Library version:** 0.5 (meta.updated 2026-10-24), 28 lookalikes.

**What I read**
- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (entries, tests, checks). I did not use scripts/read_mtx.py: there are no ancillary .mtx files.
- Paper: the v1 PDF (8 pages, all read) and its extracted text. I rendered pages 2 to 5 at 220 to 400 dpi to read Figs. 1 to 4. There are no supplementary sections beyond Appendix A.
- Title: taken from the PDF metadata and first page. I did not open the arXiv abstract page because the task forbade it. An arXiv API listing (search au:Luschmann AND au:Huebl) returned this paper's own entry among the results. I did not open it further, and its title and abstract match the PDF.
- I did not fetch the data repository (Zenodo 10.5281/zenodo.17629487), because the task allows only arxiv.org, export.arxiv.org and api.openalex.org. The device and dataset counts come from the paper alone.

**Claims table (step 1)**

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Discrete upward steps in Ω0 from single-vortex entry, at fields that change between cooldowns | Fig. 3(a), 3(b), Fig. 4 (green) | One Al nanostring, (l, w, d) = (30, 0.2, 0.11) µm, in a dc SQUID ending a λ/4 CPW (Fig. 1) | Devices fabricated or measured: not stated (one implied). Runs: 2 in one cooldown (Dataset 2: 12 to 20 mT, 0.5 mT steps; Dataset 1: 20 to 30 mT, 0.25 mT steps from about 20 to 24 mT, then 0.5 mT), 1 after a thermal cycle (18 to 35 mT, 0.5 mT steps). Steps marked: 12.0, 15.5, 20.0, 22.5, 24.0 mT (a); 18.0, 20.5, 22.5, 27.0 mT (b). T = 85 mK only, ZFC only. Sweep direction not stated. Probe power below 2 fW. |
| Step sizes of 10 to 50 Hz, i.e. 3 to 17 aN force steps and 0.09 to 0.44 eV pinning energy per vortex | Fig. 3; Eq. (9); p. 5 | same | My reading of Fig. 3: 27.0 mT (b) is about 0.95e9 Hz², about 82 Hz; 22.5 mT (a) is about 0.85e9 Hz² in two points, about 73 Hz; the others are about 26 to 52 Hz. Assumes one vortex per step, while the text also allows "one or a few flux quanta". |
| Smooth background Ω0² = Ω0,bare² + ϑ Bip^k with k = 1.81 ± 0.05, read as Campbell-regime stiffening; αL from 0.1 to 2 × 10^14 N m^-4; empirical Bc1 of about 5 mT | Fig. 2(d), Fig. 4 and inset | same | Fig. 2(d) and the black squares in Fig. 4 appear to be the same six fields as Fig. 2(c) (6.20 to 35.00 mT) from Ref. 46, the earlier lower-resolution data. The onset "at Bip ≈ 5 mT" is quoted from Fig. 2(d), but its lowest point is 6.2 mT. Fits use α = 0 (symmetric junctions, footnote 55). |

Other observations:
- The Fig. 4 caption says "blue circles", but the markers are green and match Fig. 3(b). Fig. 4 appears to show only the post-thermal-cycle run.
- The arrows at 12.0 and 18.0 mT sit on the first point of their runs, where no step can be seen.
- The Fig. 3(a) runs are both referenced to Ω0(20 mT), so their relative offset may be fixed by construction.

**Entries matched, adapted, skipped**
- Scope: this is a cavity-optomechanics measurement of vortex physics with no topological claim. No library family matches directly.
- Included: fine-tuning-and-selection (always), with its tests as written.
- Adapted: charge-trap-fractional-shift. Its physics (discrete shifts of a measured quantity caused by integer events in a nearby, weakly coupled element) maps onto flux trapped in the SQUID arms, junction leads or CPW and reaching Ω0 through the Eq. (3) fit (ϕoff, Ic). I kept its test texts and read "gate leakage" as drift of the flux offset and "two-gate space" as the Boop and Bip plane. Adapted checks: charge-control-regime and charge-repeat-sweeps. I skipped charge-regime-map because it is specific to Fabry-Perot interferometers.
- Practice checks used: report-counts, report-ranges, report-processing.
- Skipped, because the device or signal cannot apply (no tunneling spectroscopy, no zero-bias peaks, no Josephson radiation, no quantized conductance, no dots, no Kitaev chain, no diode measurement): all zbp, quantization, nonlocal, island, shapiro, supercurrent, chiral, kitaev and diode entries; protocol-parameter-sensitivity (no pass/fail protocol); local-probe-loophole (no Majorana reading); coulomb-dominated-interferometer (no interferometer). diode-vortex-screening is about Meissner screening and vortex barriers in films, but there the vortices are the lookalike and here they are the claim, so I left it out. The paper's footnote 51 assumes screening-field enhancement is negligible.

**Sources held out:** none. I did not open any library source, since the matched entries' sources (Frolov et al. 2309.09368, Zhang et al. 2101.11456, Akrap et al. 2501.18631) were not needed for related work. None of them predates-cites this paper as far as the library entries show.

**Related work: how each was checked**
- 2104.10577 (Luschmann et al.): abstract via the arXiv API. The ID, title and first author are confirmed, and the abstract states the residual field-dependent shift attributed to vortex flux pinning.
- 2501.08289 (Maksymowych et al.): full text (PDF). It confirms random telegraph signals attributed to single TLS, with temperature and power series: "The spectral diffusion in our devices is dominated by a random telegraph signal (RTS), likely arising from state changes of a single TLS."
- 1611.03842 (Shevchuk, Steele, Blanter): full text (PDF): "in the presence of the asymmetry the current never reaches zero value. Even at half flux quantum when the critical current for the symmetric case is zero, the critical current of the asymmetric SQUID is at minimum".
- 0812.3645 (Song et al.): full text (PDF): "The addition of vortices through field-cooling results in a downward shift in the resonance frequency and a reduction in the quality factor."
- 1006.2402 (Dykman et al.): abstract via the arXiv API. It confirms the theory of an oscillator spectrum with shot-noise frequency jumps.
- Found but not listed: cond-mat/0703735 (Sanchez-Lotero and Palacios, critical fields for vortex expulsion from narrow strips; abstract read). I could not find Bolle et al. 1999 (Ref. 56) or Stan, Field and Martinis 2004 on arXiv, and the OpenAlex search returned an error, so I did not list either.

**Library gaps (outside rows)**
- Two-level-system telegraph frequency jumps in nanomechanical resonators (source 2501.08289). This applies to any claim that rests on discrete jumps in a mechanical or resonator frequency.
- Residual flux-mediated spring from junction asymmetry in SQUID-embedded mechanics (source 1611.03842, plus the paper's own Eq. (A1), whose T(φb, α) does not vanish at half flux when α ≠ 0). This is my inference from the source: Shevchuk et al. show the nonzero critical current at half flux, and I connected it to a B²-like residual term through Eq. (3) and (A1). A reader should check that step.
- The library has no family for vortex physics or optomechanical sensing.

**Unsure**
- I read step sizes off the plotted points by eye. The 80 Hz figure for the 27.0 mT step could be off by about 10%.
- Whether Fig. 2(d) is the Ref. 46 data: I inferred this from matching field values and markers.
- The status for the TLS row: Fig. 3 shows shifted levels persisting over consecutive field points, which bears on telegraph switching without settling it (slow switches would look the same). I marked it "Not tested (data bear on it)", not "Tested in part", because no measurement aimed at it is shown.
- Mapping the adapted charge-trap entry onto this device is a judgment call.
- I don't recognize this paper and know nothing of its later history.

**Skill issues**
- Step "Input" says to read the arXiv abstract page and take the title from it. In this harness that is forbidden, and the skill has no fallback for a PDF-only run (I used the PDF title).
- Scope rule: when no family matches, the skill doesn't say which checks to walk beyond practice. I used the checks of the family whose entry I adapted. The rule could say this.
- For adapted entries, it's unclear whether the test text should be kept verbatim (flags.json wants library text) or rewritten for the device. I kept the text and put my reading in parentheses in the report.
- Outside lookalikes need "a paper ... that shows it". It's unclear whether a source showing a key ingredient (here, a nonzero Ic at half flux) plus the paper's own equations is enough.
- The line between "data bear on it" and "tested in part" is unclear when a figure partly discriminates without being a test aimed at the lookalike.
- Step 7 says to write reports/<id>.md and .notes.md. The harness overrides this; no conflict, but worth noting.
- The arXiv API search can return the paper under review in a results list. The skill could say to drop it from listings without opening it.
