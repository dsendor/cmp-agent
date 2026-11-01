# Lookalike check: Flux-tunable superconductivity in a TI nano-SQUID (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 27 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. I worked from the extracted text, so figure details come from the captions. Your main claim rests on supercurrent and diode signatures, and the library has few entries for these. So I adapted the diode entry and added one lookalike from outside the library, an ordinary SQUID diode, with a source.

**The claim, as I read it.** In BiSbTeSe2 nano-SQUIDs (devices A, B and C), the paper reads three global features as a flux-driven transition into a topological phase near odd flux quanta: h/2e critical-current oscillations, a diode-efficiency sign reversal at half-integer flux (Fig. 1e, 3a, S2a, S4), and spectral jumps in local and nonlocal conductance (Fig. 1f-g, 3b-e, S2). Zero-bias peaks appear in both the expected topological and the trivial windows, including at zero field, and their end-to-end correlation shows no clear relation to the bulk phase (Fig. 4, S3).

## Checks a careful reader will look for

1. Search for unintended quantum dots near the barrier : Not done. The paper shows rich Andreev spectra, and it doesn't search for Coulomb resonances or even-odd patterns.
2. Peak over wide gate, field and angle ranges, with heights everywhere : Partly. "even over a region of VG that includes the Dirac point (Fig. 4j-k)" (p. 5). It shows no field-angle series, and it gives no peak heights across the maps.
3. Tunnelling at both ends at the same settings : Partly. Done for B and C ("Simultaneous global and dual-local spectroscopy", Fig. 3 caption, p. 3). Device A has "a single functioning tunnel probe" (p. 3).
4. Peak stable as the junction transparency changes : Not done. The ALD tunnel barriers are fixed, and the back gate tunes the chemical potential.
5. Nonlocal gap closing and reopening where end peaks appear : Partly. For B and C, "some features correspond to the boundaries of the expected topological regimes" (Fig. 3 caption, p. 3). This shows jumps. It doesn't resolve a closing and reopening.
6. Series resistance stated and calibrated, raw data shown : Not done. "the known filter resistance was subtracted from the recorded data" (p. 6). The value isn't given, and Supplement Section C, "Effects of measurement circuit", has no text.
7. Device and dataset counts : Partly. "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5). The paper names three devices, and "all examined devices" (p. 4) is not counted.
8. Full ranges and why each shown range was chosen : Partly. For device A, "the gating range was limited due to a leaky gate dielectric" (Supp. p. 3). The other choices aren't explained.
9. Processing from raw data to figures, with data and code : Partly. Data are "available at the online depository zenodo with the identifier 10.5281/zenodo.21988906" (p. 7). There is no analysis code, and the correlation classifier's settings aren't given.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Ordinary SQUID diode from junction asymmetry and non-sinusoidal current-phase relations (not in library) | Tested in part | trivial SQUID model compared: no; diode followed as asymmetry is gated: part; trivial control SQUID: no | "In device B, the sign reversals of the diode effect exhibit a largely regular periodicity as a function of Bx" (Supp. p. 6, Fig. S4) | Fit Ic±(Φ) and η(Φ) with a two-junction model using your asymmetry and loop inductance, then show which feature it misses |
| Diode from vortex barriers and Meissner screening | Tested in part | plain Nb control: no; field and width: all | "Their strong dependence on the magnetic-field sweep direction points to a vortex dynamics and flux trapping origin within the Nb electrodes" (p. 4) | Ic± versus field on a Nb-only bridge of the same thickness, plus diode traces for both sweep directions at low field |
| Trivial Andreev band mimicking gap reopening | Tested in part | trivial model or device: no; other parameters varied: part | "there are also nonlocal conductance jumps at Bx values that do not correspond to the Ic features" (p. 5) | Follow the boundary jumps in GLR and GRL across back gate (Fig. S5 at several fields), and compute nonlocal G for a trivial SQUID with a phase jump |
| Andreev states in an unintended dot | Tested in part | dot search: no; both ends: part | "Although the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5) | Look in your gate maps for Coulomb-like resonances above the gap and peaks that split and recross |
| Disorder-induced zero-bias peaks | Tested in part | end-to-end correlation: part; gap closing and reopening: part; gate insensitivity: all | "suggests that at least some of these ZBPs are driven by disorder effects" (p. 5) | Your data already lean this way. Report peak-height distributions per regime |
| Crowded trivial subgap states | Tested in part | range compared with prediction: all; subband model: part (clean model only) | "both showing a large number of ZBPs at both ends" (p. 5) | Add disorder to the Fig. 2c model and compare how common zero modes are |
| Quasi-Majorana states from smooth confinement | Tested in part | nonlocal gap: part; correlated ends: part | "we estimate the experimental localisation length of the MBSs to be a few 100 nm, which is shorter than the 1.3 − 2.5µm length of our devices" (p. 5) | Show where peaks first appear relative to the nonlocal jumps, field point by field point |
| Peak at one end only | Tested in part | both ends: part; nonlocal: part | "first generation device with a single functioning tunnel probe" (p. 3) | Treat the device A peak as one-ended. Compare with the B and C right ends at matching flux |
| Local-probe loophole | Tested in part | nonlocal: part; overlap through a dot: no | "which in principle adds another global probe of the superconductivity" (p. 4) | Report the nonlocal signal at zero bias when both ends show peaks |
| Kondo resonance | Tested in part | even-odd: no; temperature: no; Zeeman splitting: part (field maps start at zero field, splitting not analyzed) | "notably even at zero Bx" (p. 5) | A temperature series of the zero-field peaks, and their low-field splitting |
| Weak antilocalization | Not tested (data bear on it) | Pikulin test: no; channel number or disorder: no | "which has an approximately 70% larger cross-section than the device in Fig. 1" (p. 4) | Compare zero-field peak statistics across devices of different cross-section |
| Fine-tuning and selection | Tested in part | counts: part; how chosen: no; second device: all | "making devices with two decent tunnel probes to be comparatively rare" (p. 5) | State devices fabricated, measured and kept, and how the Fig. 3 gate voltage was chosen |

## Questions about devices and data

1. How many nano-SQUIDs did you fabricate and measure, and in how many did you see the global signatures (h/2e oscillations, diode reversal) and the spectral jumps? The text says "all examined devices" without a number.
2. Why were the others set aside? For example, were there improved-series devices with one working tunnel probe, or with two, beyond B and C?
3. Which ranges of field, field angle, back-gate voltage and temperature did you measure beyond the ones shown? A temperature series of the zero-field zero-bias peaks would be especially useful.
4. What does the second-best dual-probe dataset look like, for instance device B at another back-gate voltage in Fig. 3, or a fourth device if one exists?
5. Section C of the supplement, "Effects of measurement circuit", has a heading and no text in the version I read. What series and filter resistances sit in the two-terminal tunnel spectroscopy and nonlocal circuits, how were they calibrated, and did you correct for the circuit effects described by Martinez et al. (your supplementary Ref. [2])?
6. The Methods give tunnel resistances "typically exceeding 100 kΩ" (about 0.26 e^2/h), while the conductance in device A (Fig. S1) and device C (Fig. S2b) is of order 1 e^2/h. What were the TJ1 and TJ2 resistances in each device, and are A and C in the tunnelling regime?
7. For the end-to-end correlation in Fig. 4l and Fig. S3l: the sign of the third derivative at zero bias takes a value even where there is no peak. What smoothing, bias step and threshold separate a peak or dip from no feature, and how do the fractions change with them? This also bears on device C, where a zero-bias peak "was mostly absent" (Supp. p. 4) while Fig. S3l shows a strong increase of correlated peaks.
8. The diode efficiency of any flux-periodic SQUID vanishes at half a flux quantum (Ciaccia et al. show this in a trivial InAs SQUID). Have you compared Ic+(flux), Ic-(flux) and the diode efficiency with a non-topological SQUID model using your junction asymmetry, and which feature of the reversal (its abruptness, the Ic recovery) carries the topological reading?

## Related work

- Ciaccia et al. 2023, "Gate Tunable Josephson Diode in Proximitized InAs Supercurrent Interferometers", https://arxiv.org/abs/2304.00484. In a trivial two-junction InAs SQUID, the diode efficiency reaches about 30%, changes sign across flux lobes and vanishes at half a flux quantum. A model with junction asymmetry and loop inductance reproduces this.
- Souto, Leijnse and Schrade 2022, "The Josephson diode effect in supercurrent interferometers", https://arxiv.org/abs/2205.04469. Theory: a SQUID of non-diode junctions with non-sinusoidal current-phase relations is a diode needing only flux, with efficiency up to about 40% and none at multiples of half a flux quantum.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", https://arxiv.org/abs/2205.09276. Plain Nb and V films show a strong diode effect from asymmetric vortex barriers and Meissner screening at fields as small as 1 Oe.
- Hess, Legg, Loss and Klinovaja 2023, "Trivial Andreev band mimicking topological bulk gap reopening in the non-local conductance of long Rashba nanowires", https://arxiv.org/abs/2210.03507. A trivial bulk Andreev band gives an apparent gap closing and reopening in nonlocal conductance, alongside trivial end peaks.
- Valentini et al. 2021, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", https://arxiv.org/abs/2008.02348. Flux-tunable Andreev levels in dots at the tunnel junction give robust zero-bias peaks in flux lobes, and these are unrelated to topology.

Happy to rerun this if you share the figure data or the Supplement Section C text.
