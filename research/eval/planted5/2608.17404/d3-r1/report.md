# Lookalike check: TI nano-SQUID global and local superconductivity (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper pairs supercurrent interferometry with tunnel spectroscopy, so I applied the zero-bias entries to the tunnel spectra, adapted the diode and full-shell entries to the flux-driven phase winding, and added one interferometer lookalike from the literature that the library doesn't hold.

**The claim, as I read it.** In topological insulator nano-SQUIDs, h/2e oscillations of Ic and a diode efficiency that reverses sign at half-integer flux (Fig. 1e, device A; Fig. 3a, device B; Fig. S2a, device C) mark a flux-driven π phase jump that your theory ties to a topological transition, with jumps in local and nonlocal spectra at the same fields (Figs. 1f,g and 3b-e) and a zero-bias peak in device A inside the predicted window. You also report that end-to-end zero-bias correlations don't separate topological from trivial flux regimes (Fig. 4, Fig. S3).

## Checks a careful reader will look for

1. Look for unintended quantum dots near the tunnel barriers : Not done. The Bx = 0 gate maps (Fig. 4a,b; Fig. S3a,b) could be read for Coulomb resonances.
2. Show the peak over wide gate, field and angle ranges, with heights : Partly. "the abrupt appearance of the zero-bias conductance anomaly at half-flux quantum, is very stable over the examined gate-voltage range" (Supp. p. 3, Fig. S1); field angle is fixed and peak heights aren't reported.
3. Measure both ends at the same settings : Partly. "we evaluated the end-to-end correlation using the relative signs of the third derivative of the current at zero bias" (p. 5, Fig. 4); devices B and C only, since device A has one probe.
4. Show the peak stays as junction transparency changes : Not done. The ALD tunnel barriers have no barrier gate.
5. Nonlocal gap closing and reopening : Partly. "the nonlocal conductance reveals features that align with the Ic oscillations, such as jumps at the boundaries where the phase transition is supposed to occur (see Fig. 3d-e)" (p. 4); devices B and C, and the figures show jumps with no gap closing and reopening identified.
6. Series resistance and raw data : Partly. "The line resistances required were determined from two-terminal resistance measurements of the cryostat lines." (Supp. p. 2); the values, the filter resistance subtracted (p. 6) and uncorrected data aren't shown.
7. Report devices measured and kept : Partly. "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5); three devices are shown and the total measured isn't given.
8. Disclose full ranges and why each was chosen : Partly. "in this device A, the gating range was limited due to a leaky gate dielectric" (Supp. p. 3); other range choices aren't explained.
9. Give processing steps with data and code : Partly. Data "are available at the online depository zenodo" (p. 7) and the circuit correction is described (Supp. S1.C); the derivative step behind Fig. 4l and any code aren't described.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Andreev states in an unintended quantum dot | Tested in part | Dot signatures searched: no; both ends compared: part | "We find that both regimes contain ZBPs on either end (see Fig. 4c,f,i,l) the majority of the time." (p. 5); device A's peak comes from one probe. | Read the Bx = 0 maps in Fig. 4a,b and Fig. S3a,b for resonances above the gap, and run a gate scan for device A's probe. |
| Quasi-Majorana states from smooth confinement | Tested in part | Nonlocal gap closing and reopening: part; correlated zero modes at both ends: part | "jumps at the boundaries where the phase transition is supposed to occur (see Fig. 3d-e)" (p. 4); jumps are shown, a closing and reopening gap isn't identified. | Show GLR and GRL against bias at the fluxes where end peaks appear and say whether a gap closes and reopens there. |
| Disorder-induced zero-bias peaks | Tested in part | End-to-end correlation: part; bulk gap closing and reopening: part; gate insensitivity: all | "suggests that at least some of these ZBPs are driven by disorder effects, rather than a potential topological superconducting phase" (p. 5) | Plot peak height and position against VG per flux lobe from the Fig. 4 and Fig. S3 data. |
| Crowded trivial subgap states | Tested in part | Peak range against predicted range: all; subband model of the device: part | "there is no clear distinction between expected topological regions and trivial regions, with both showing a large number of ZBPs at both ends" (p. 5); the model is clean, 18 nm wide and 150 nm long (p. 7). | Run the Fig. 2 model at the measured cross-sections (Table S1) with disorder and compare where zero-energy states sit. |
| Kondo resonance | Not tested (data bear on it) | Even-odd occupancy: no; temperature: no; Zeeman splitting: no | Not discussed; Fig. 4a,b show gate maps at Bx = 0. | Check the Bx = 0 maps for peaks in alternating gate valleys, and add a temperature series for one peak. |
| Weak antilocalization | Not tested (not mentioned) | Pikulin et al. test: no; channel number or disorder dependence: no | Not discussed. | Compare peak shape and height across probes with different tunnel conductance. |
| State at one end only | Tested in part | Both ends at same settings: part; nonlocal conductance: part | "we observe a jump in the spectrum and the appearance of a zero-bias peak (ZBP) within the predicted topological window" (p. 3), from device A's single probe. | Show both ends' traces at each Fig. 4 setting, and say whether device A's second probe ever worked. |
| Trivial Andreev band mimicking gap reopening | Tested in part | Tested on trivial models or devices: no; unused parameters varied: part | "there are also nonlocal conductance jumps at Bx values that do not correspond to the Ic features" (p. 5); Fig. S5 varies gate. | Run the nonlocal calculation in a trivial setting of your model and vary field direction to see whether the jumps track flux. |
| Flux-tunable Andreev levels in a junction dot (adapted from full-shell entry) | Not tested (data bear on it) | Short and long junction regions compared: no | Not discussed; the gate maps of each probe (Fig. 4, Fig. S3) could show dot levels. | Compare peak occurrence with probe geometry across devices A to C. |
| Local-probe loophole | Tested in part | Nonlocal measurement: part; overlap through a dot in series: no | "Interestingly, the nonlocal conductance reveals features that align with the Ic oscillations" (p. 4), devices B and C. | Use the nonlocal data at the zero-bias fluxes in B and C to bound end-state overlap. |
| Exceptional-point zero mode | Not tested (not mentioned) | Overlap of Majorana components: no | Not discussed. | Report tunnel coupling per probe; if strong, test overlap with the nonlocal data. |
| Diode from vortex barriers and Meissner screening in Nb | Tested in part | Plain Nb control: no; effect against field or width: all | "Their strong dependence on the magnetic-field sweep direction points to a vortex dynamics and flux trapping origin within the Nb electrodes." (p. 4); the reversal period scales with wire cross-section across devices (Figs. 1e, 3a, S2a). | Measure Ic+ and Ic− on a plain Nb junction or strip from the same run, in both sweep directions. |
| Analysis outcome set by data choices (adapted to the Fig. 4l correlation count) | Tested in part | Code and data published: part; reasons for ranges and resolution: no; rerun with choices varied: no | "Relative fraction of gate voltages exhibiting correlated zero-bias conductance peaks" (Fig. 4l caption); data on Zenodo, code not mentioned. | Release the analysis code and rerun Fig. 4l with different smoothing, bias windows and resolution. |
| Fine-tuning and data selection | Tested in part | Counts: part; how data were chosen: no; second device shown: all | "We were able to fabricate an additional device C with two functional tunnel probes" (Supp. p. 3) | State devices measured and kept, and how the gate voltages in Figs. 1f and 3 were picked. |
| Trivial two-junction interferometer diode (not in library) | Not tested (data bear on it) | Trivial interferometer model compared with Ic(Φ) and η(Φ): no; feature at half flux a trivial interferometer lacks: no | "all fit the expected theoretical global signatures of a ground-state phase experiencing a phase jump across the junction" (p. 2); Seoane Souto et al. find the interferometer diode vanishes at integer multiples of Φ0/2. | Fit Figs. 1e and 3a with a two-junction model with unequal, skewed current-phase relations and compare the shape near half flux with Fig. 2b. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the global signatures and the zero-bias peaks? Page 4 says the global features appear "in all examined devices" and p. 5 gives a tunnel junction yield below 50%, but the number of devices examined isn't stated.
2. Why were the other devices set aside, for example devices with a single working tunnel probe other than device A?
3. Which ranges did you measure beyond the ones shown: field angle, negative Bx for the correlation analysis, temperature, both field sweep directions for the half-flux jumps (p. 4 says the high-field jumps depend on sweep direction), and device A gate voltages (the Fig. S1 caption lists VG = −10, 0, 20 V while the panels read 0, 10 and 20 V)?
4. What does the second-best device or dataset look like? Device C appears in Figs. S2 and S3; were there cooldowns or gate settings of device A where the zero-bias peak did not appear at half flux?
5. For the end-to-end analysis in Fig. 4l and Fig. S3l, how did you compute the third derivative (smoothing, bias window, resolution), what fraction of correlated peaks would uncorrelated signs give, and how does the fraction move when those choices change?
6. In device C, Supp. p. 4 says a zero-bias peak "was mostly absent in this device", while Supp. p. 5 reports "a strong increase of correlated zero-bias conductance peaks" in the first expected topological regime. Which gate voltages does each statement cover?
7. What are the tunnel resistances of TJ1 and TJ2 in each device? Methods give "resistances exceeding 100 kΩ" (p. 5), while Fig. S1a shows G of about 0.6 to 1.4 e²/h at 2 mV, roughly 18 to 43 kΩ.
8. Would a two-junction interferometer with unequal arms and skewed current-phase relations, and no topological surface states, give the same Ic(Φ) and the same η sign reversal at half-integer flux as Figs. 1e and 3a? Which feature of your data would differ?

## Related work

- Seoane Souto, Leijnse and Schrade 2022, "The Josephson diode effect in supercurrent interferometers", <https://arxiv.org/abs/2205.04469>. Theory: two junctions with skewed current-phase relations in a loop give a diode effect up to about 40% with only flux breaking time reversal, and it vanishes at integer multiples of half a flux quantum.
- Ciaccia et al. 2023, "Gate Tunable Josephson Diode in Proximitized InAs Supercurrent Interferometers", <https://arxiv.org/abs/2304.00484>. An InAs SQUID with gate-tuned diode efficiency up to about 30%, whose sign is mirrored about half a flux quantum when the junction asymmetry changes sign.
- Valentini et al. 2021, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", <https://arxiv.org/abs/2008.02348>. Dots in the tunneling region host flux-tunable Andreev levels that give robust zero-bias peaks; short tunnel regions show no subgap states.
- Pan and Das Sarma 2020, "Physical mechanisms for zero-bias conductance peaks in Majorana nanowires", <https://arxiv.org/abs/1910.11413>. Strong disorder generically gives trivial zero-bias peaks, and end-to-end correlation has limits in short wires.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a diode effect from asymmetric vortex barriers and Meissner screening at fields as small as 1 Oe.

Happy to rerun this if you share the figure data or the analysis code behind Fig. 4l.
