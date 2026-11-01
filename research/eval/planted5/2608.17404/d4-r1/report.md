# Lookalike check: Flux-tunable global and local superconductivity in a TI nano-SQUID (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper reports global supercurrent features alongside local and nonlocal spectroscopy. The library has no check list for the diode or supercurrent families, so I adapted two entries (flux-tunable Andreev levels, protocol sensitivity) and added one outside row.

**The claim, as I read it.** Your global measurements on devices A, B and C (h/2e Ic oscillations, a diode-effect sign reversal at half-integer flux; Figs. 1e, 3a, S2a, S4) fit "a flux-driven global phase transition consistent with entering the topological regime" (p. 1), and spectral jumps in local and nonlocal conductance line up with them (Figs. 1f-g, 3b-e, S2). The zero-bias peaks appear in both the expected topological and trivial windows, including at zero field (Figs. 3b-c, 4, S3), and you read "at least some of these ZBPs" as "driven by disorder effects" (p. 5).

## Checks a careful reader will look for

1. Look for unintended quantum dots near the barrier and in the junction : Not done.
2. Show the peak over wide gate, field and field-angle ranges, with peak heights everywhere : Partly. "Relative fraction of gate voltages exhibiting correlated zero-bias conductance peaks" versus Bx (Fig. 4l caption, p. 4); no field-angle series and no peak heights.
3. Measure tunneling at both ends at the same settings : Partly. "differential conductance simultaneously detected at both ends of the TINW as Bx is tuned" (p. 4), for B and C. Device A has one probe.
4. Show the peak stays as the junction transparency changes : Not done. The barrier is a fixed ALD oxide.
5. Nonlocal conductance for a bulk gap closing and reopening : Partly. "some features correspond to the boundaries of the expected topological regimes" (Fig. 3d-e caption, p. 3), in B and C.
6. State the series resistance and show raw data : Partly. "The line resistances required were determined from two-terminal resistance measurements of the cryostat lines" (Suppl. p. 2), for the nonlocal data; local conductance not covered.
7. Report devices measured, how many showed the effect, and why others were set aside : Partly. "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5); totals not given.
8. Disclose full parameter ranges and why each shown range was chosen : Partly. "in this device A, the gating range was limited due to a leaky gate dielectric" (Suppl. p. 3).
9. Give processing steps with data and code : Partly. Data are deposited on Zenodo (p. 7); code and the third-derivative procedure are not described.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Ordinary SQUID interferometer diode (not in library) | Tested in part | Asymmetry gated through its sign change: part; trivial interferometer model compared: no | "the reversal of the SDE exactly at half-integer flux quanta" (p. 2) | Fit a trivial asymmetric two-junction model with your Ic and transparencies to Figs. 1e and 3a; track η's sign pattern versus VG in Fig. S4 |
| Vortex and Meissner screening diode | Tested in part | Plain Nb film or junction: no; versus field, width or edges: all | "The SDE efficiency η (grey) shows sign reversals at half-integer flux quanta." (Fig. 1e) | Measure Ic± on a Nb reference junction with no TI, and compare up and down field sweeps of η near zero field |
| Peak at one end only | Tested in part | Both ends: part; nonlocal: part | "we observe a jump in the spectrum and the appearance of a zero-bias peak (ZBP) within the predicted topological window" (p. 3, single-probe device A) | Treat device A's peak as one-end data; show B and C end pairs over the same flux window |
| Local-probe loophole | Tested in part | Nonlocal: part; overlap via dot: no | "The coincidence of nonlocal conductance features and those from Ic is broadly found in all devices." (pp. 4-5) | Plot nonlocal and both local channels at the same VG and Bx for each peak counted in Fig. 4l |
| Andreev states in an unintended dot | Tested in part | Dot search: no; both ends: part | "We find that both regimes contain ZBPs on either end (see Fig. 4c,f,i,l) the majority of the time." (p. 5) | Look in the zero-field VG maps (Fig. 4a-b) for diamond-like resonances above the gap and peaks that split and recross |
| Flux-tunable Andreev levels in the junction region (adapted) | Not tested (data bear on it) | Short and long junction regions: no | "the abrupt appearance of the zero-bias conductance anomaly at half-flux quantum, is very stable over the examined gate-voltage range" (Suppl. p. 3) | Compare devices with different tunnel-region lengths; follow device A's peak in gate maps for dot levels |
| Quasi-Majorana from smooth confinement | Tested in part | Nonlocal gap: part; correlated ends: part | "showing that some features correspond to the boundaries of the expected topological regimes" (Fig. 3d-e) | Show where in flux the peak first appears relative to the nonlocal jump, for B and C |
| Disorder-induced peaks | Tested in part | End correlation: part; nonlocal gap: part; gate insensitivity: all | "suggests that at least some of these ZBPs are driven by disorder effects" (p. 5) | Report peak heights and widths across VG and Bx so readers can see the spread |
| Crowded trivial subgap states | Tested in part | Range versus predicted window: all; subband model: part | "there is no clear distinction between expected topological regions and trivial regions, with both showing a large number of ZBPs at both ends" (p. 5) | Add disorder or extra subbands to the Fig. 2 model and compare peak prevalence |
| Kondo resonance | Not tested (data bear on it) | Even-odd: no; temperature: no; Zeeman: no | "Although the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5) | Check zero-field peaks for alternating-valley patterns and a temperature series |
| Weak antilocalization | Not tested (not mentioned) | Pikulin test: no; channel or disorder dependence: no | Not discussed. | Compare peak height and width with VG near and away from the Dirac point (Fig. 4j-k) |
| Exceptional-point zero mode | Not tested (argued, not tested) | Overlap measured: no | "we estimate the experimental localisation length of the MBSs to be a few 100 nm, which is shorter than the 1.3 − 2.5µm length of our devices" (p. 5) | None beyond the nonlocal comparison above |
| Trivial Andreev band mimicking gap reopening | Tested in part | Trivial model or device: no; other parameters varied: part | "the low-bias nonlocal conductance exhibits frequent sign changes as the gate voltage is varied" (Suppl. p. 6) | Show the nonlocal jumps at several VG and field-sweep directions; run your model in a trivial regime |
| Classifier set by data choices (adapted) | Tested in part | Code and data: part; reasons for ranges: no; rerun varied: no | "The data that support the findings of this study are available at the online depository zenodo" (p. 7) | Rerun Fig. 4l with other smoothing, bias steps and a curvature threshold; release the code |
| Fine-tuning and selection | Tested in part | Counts: part; how chosen: part; second device: all | "All key features are reproduced in this device." (Suppl. p. 3) | State total devices measured and how many showed each feature |

## Questions about devices and data

1. How many nano-SQUIDs did you measure in total, including those with one or no working tunnel probe, and how many showed the Ic oscillations, the diode sign reversal, the spectral jumps and zero-bias peaks?
2. Why were the other devices set aside, beyond the tunnel-junction yield you mention ("below 50%", p. 5)?
3. Which ranges did you measure beyond the ones shown: Bx above 4 T for devices B and C, VG beyond ±30 V, field angle, and temperature?
4. What does the second-best device or dataset look like, in particular any other first-generation single-probe device, and the device A data where the zero-bias peak did not appear at the diode reversal?
5. What are the tunnel resistances of each junction in devices A, B and C? Figs. S1 and S2b show local conductance of about 1 e^2/h (about 26 kΩ) and above, while the Methods say the contacts "typically exhibit resistances exceeding 100 kΩ" (p. 5). Was any filter or line resistance subtracted from the local conductance, and how was the preamplifier offset that sets zero bias corrected (per trace or once per dataset)?
6. For the end-to-end correlation (Figs. 4c,f,i,l and S3), what smoothing and bias step did you use for the third derivative, was there a threshold below which a curvature counts as neither peak nor dip, and how does the "strong increase of correlated zero-bias conductance peaks" in device C (Suppl. p. 5) fit with "a zero-bias conductance peak was mostly absent in this device" (Suppl. p. 4)?
7. In the zero-field gate maps (Fig. 4a-b), do the zero-bias peaks follow Coulomb-diamond-like or even-odd patterns, and how do they change with temperature?
8. Does the sign pattern of η in Bx (Fig. S4) mirror when the back gate changes the top-bottom asymmetry, and how does a trivial asymmetric two-junction interferometer model with your measured parameters compare with Figs. 1e and 3a?

## Related work

- Ciaccia et al. 2023, "Gate Tunable Josephson Diode in Proximitized InAs Supercurrent Interferometers", <https://arxiv.org/abs/2304.00484>. In a trivial InAs two-junction SQUID the diode efficiency is gate tunable up to about 30%, and at half a flux quantum "η = 0 independent on any other parameters" (Fig. 3 caption).
- Souto, Leijnse and Schrade 2022, "The Josephson diode effect in supercurrent interferometers", <https://arxiv.org/abs/2205.04469>. Theory: two junctions with non-sinusoidal current-phase relations in a loop form a diode needing only flux, with the effect vanishing at multiples of half a flux quantum.
- Valentini et al. 2020, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", <https://arxiv.org/abs/2008.02348>. Flux-tunable Andreev levels in dots in the junction region give robust zero-bias peaks in odd flux lobes; short junctions show none.
- Hess, Legg, Loss and Klinovaja 2022, "Trivial Andreev band mimicking topological bulk gap reopening in the non-local conductance of long Rashba nanowires", <https://arxiv.org/abs/2210.03507>. A trivial Andreev band can mimic gap closing and reopening in nonlocal conductance, alongside trivial end peaks.
- Chen et al. 2019, "Ubiquitous non-Majorana Zero-Bias Conductance Peaks in Nanowire Devices", <https://arxiv.org/abs/1902.02773>. Zero-bias pinning becomes "common to the point of ubiquity" at finite field, traced to crowded trivial subgap states.

Happy to rerun this if you share the figure data and the correlation code.
