# Lookalike check: Topological insulator nano-SQUID, global and local superconductivity (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-24 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper, "Flux-tunable global and local superconductivity in a topological insulator nano-SQUID", against a library of 28 known lookalikes in topological transport: ordinary effects that can produce the same signal as the one you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library has ordered checks for zero-bias peaks but none for diode or nonlocal signals. So I walked the zero-bias checks for your tunnelling data, and judged the diode and nonlocal signals through the lookalike entries that match them.

**The claim, as I read it.** In three TI nano-SQUIDs (devices A, B, C), the critical current oscillates with h/2e period and the diode efficiency changes sign at half-integer flux (Fig. 1e, Fig. 3a, Fig. S2a, Fig. S4). Local and nonlocal tunnelling spectra jump at the same fluxes (Fig. 1f-g, Fig. 3b-e, Fig. S2b-e). You read these together as a flux-driven transition into a topological phase. Zero-bias peaks appear in device A inside the predicted topological window (Fig. 1f-g, Fig. S1). In device B they also appear in trivial windows and at zero field (Fig. 3b-c, Fig. 4), and you don't count them as Majorana evidence.

## Checks a careful reader will look for

1. Search for unintended quantum dots : Not done. Your zero-field gate maps in Fig. 4a-b and Fig. S3a-b are the natural place to look.
2. Wide gate, field and angle ranges, with peak heights : Partly. "we observe these even in theoretically trivial windows and notably even at zero Bx" (p. 5). The field angle is set by the alignment procedure, and peak heights aren't reported.
3. Both ends at the same settings : Partly. "In Fig. 3b and c we show the differential conductance simultaneously detected at both ends of the TINW as Bx is tuned" (p. 4). Device A has one probe.
4. Peak followed as junction transparency changes : Not done. Only the global back gate is tuned.
5. Nonlocal gap closing and reopening : Partly. "the nonlocal conductance reveals features that align with the Ic oscillations, such as jumps at the boundaries where the phase transition is supposed to occur (see Fig. 3d-e)" (p. 4). Devices B and C only.
6. Series resistance and raw data : Partly. "the known filter resistance was subtracted from the recorded data" (p. 6). The values and the raw traces aren't shown.
7. Device and dataset counts : Partly. "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5). The number of devices measured isn't given.
8. Full ranges, and why each shown range was chosen : Partly. "in this device A, the gating range was limited due to a leaky gate dielectric" (p. S3).
9. Processing from raw data to figures, with data and code : Partly. "A small DC offset introduced by the preamplifier was numerically corrected for during data analysis." (p. 6). The data are on Zenodo. No code is mentioned.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Trivial asymmetric higher-harmonic SQUID diode (not in library) | Not tested (data bear on it) | η and its zeros compared with a trivial higher-harmonic SQUID model: no; Shapiro response: no | "The SDE efficiency η (grey) shows sign reversals at half-integer flux quanta." (p. 2, Fig. 1e) | Fit η(Φ) in Fig. 1e, 3a and S2a with a two-junction model that has a second harmonic and some asymmetry. In such a model η also vanishes at integer and half-integer flux, so compare how sharp the sign change is. |
| Vortex barriers and Meissner screening (diode) | Tested in part | Plain film or parent-superconductor junction: no; field, width or edge dependence: all | "which has an approximately 70% larger cross-section than the device in Fig. 1, exhibits multiple Ic oscillations and corresponding changes in the SDE" (p. 4) | Measure Ic+ and Ic− on a plain Nb strip or a Nb reference junction on the same chip, at the same Bx and Bz compensation. |
| Trivial Andreev band mimicking gap reopening | Tested in part | Trivial model or device: no; other parameters varied: part (gate in Fig. S5, no field direction) | "there are also nonlocal conductance jumps at Bx values that do not correspond to the Ic features, especially at large values of magnetic flux" (p. 5) | Compute nonlocal conductance in your model with the phase jump held off, and compare with Fig. 3d-e. Follow the Fig. S5 jumps in VG at fixed flux on each side of Φ0/2. |
| Andreev states in an unintended quantum dot | Tested in part | Dot signatures: no; both ends: part (B and C only) | "Although the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5) | Look in Fig. 4a-b and S3a-b for resonances above the gap and for peaks that split and recross. |
| Quasi-Majorana from smooth confinement | Tested in part | Gap closing and reopening: part (jumps at the boundaries, B and C only); both ends: part | "we analysed the correlation of local states at opposite ends of the nanowire" (p. 5) | Report the Fig. 4l correlated-peak fraction separately for topological and trivial flux windows, along with its threshold. |
| Disorder-induced subgap states | Tested in part | End-to-end: part; gap reopening: part; gate insensitivity: all | "we do not see a significant difference between the VG dependence of ZBPs in the expected topological or trivial regimes" (p. 5) | Count peak occurrence and height across VG in Fig. 4 and S3 for each flux window. |
| Crowded trivial subgap states | Tested in part | Range compared with predicted topological range: all; subband model: part (model is 150 nm long) | "present both within the predicted topological range of magnetic fields and in theoretically trivial regimes, including at zero magnetic field" (p. 1) | Run the finite-length model at your device lengths (1.3 to 2.5 µm) with some disorder, to see how often trivial windows host peaks. |
| Kondo resonance | Tested in part | Even-odd: no; temperature: no; Zeeman: part (Fig. 3b-c show the zero-field peaks in field, no splitting analysis) | "notably even at zero Bx" (p. 5) | Take a temperature series of one zero-field peak in device B, and check whether peaks appear in alternating gate windows. |
| Weak antilocalization | Not tested (data bear on it) | Pikulin test: no; channel number or disorder: no | Not discussed. | Compare zero-field peak height and width across the Dirac point in Fig. 4j-k, where the number of surface channels changes. |
| Spin-orbit length pinning | Tested in part | Pinning against other parameters: all (VG in Fig. S1, Fig. 4) | "is very stable over the examined gate-voltage range" (p. S3) | Compare where the peak sits in devices of different length (Table S1). |
| Exceptional-point zero mode | Not tested (argued, not tested) | Overlap measured: no | "Hence, the boundary modes should be localised at the junctions without significant overlap in our devices." (p. 5) | Bound the overlap from the nonlocal amplitude in Fig. 3d-e or from the end-to-end analysis. |
| Flux-tunable Andreev levels in a junction dot | Not tested (not mentioned) | Short and long junction regions: no | Not discussed. | Compare tunnel junctions of different size, or check whether device A's peak follows dot-like levels in the Fig. S1 gate data. |
| State at one end only | Tested in part | Both ends: part (B and C); nonlocal: part | "a first-generation device (device A) featuring a single functional tunnel contact" (p. 2) | For B and C, state whether each peak at one end has a partner at the other end at the same VG and Bx. |
| Local-probe loophole | Tested in part | Nonlocal measurement: part; overlap through a dot: no | "boundary modes should be localised at the junctions without significant overlap" (p. 5) | Same as for the exceptional-point row. |
| Fine-tuning and selection | Tested in part | Counts: part; how data were chosen: no; second device: all | "are also observed in all examined devices and are largely robust against gate voltage" (p. 4) | State how many devices were measured, and how the cuts and windows in Fig. 1, 3 and 4 were chosen. |

## Questions about devices and data

1. How many devices did you measure, and how many showed the global signatures, the spectral jumps and the zero-bias peaks? You write that the global signatures appear "in all examined devices" (p. 4) and that you "were able to produce a series of devices with two functioning tunnel contacts" (p. 4), but the size of that series isn't given.
2. Why were the other devices set aside, and was the tunnel-junction yield ("below 50%", p. 5) the only reason?
3. Which ranges of Bx, VG and field angle did you measure beyond the ones shown, for example Bx above 4 T in devices B and C, or VG outside the window of Fig. 4?
4. What does the second-best device or dataset look like, beyond A, B and C, for example a two-probe device that was set aside or another cooldown of device B?
5. What were the tunnel-contact resistances of devices A, B and C, and what filter resistance did you subtract in the two-terminal measurements? Your Methods say the contacts "typically exhibit resistances exceeding 100 kΩ" (p. 5), while Fig. S1a shows about 0.6 to 1.4 e^2/h at 2 mV, roughly 18 to 43 kΩ. Raw traces before subtraction would help.
6. In Fig. S1, panels b to d are labelled VG = 0, 10 and 20 V, while the caption and text give "VG = −10, 0, and 20 V" (p. S3). Which gate voltages were measured, and how were they chosen?
7. For the diode effect, does η change sign as an abrupt jump at half-integer flux or as a smooth zero crossing, and how does η(Φ) in Fig. 1e, Fig. 3a and Fig. S2a compare with a trivial two-junction SQUID with a second harmonic, which also has zeros at integer and half-integer flux?
8. In Fig. 4l and Fig. S3l, how did you set the threshold on the third-derivative product that counts a gate voltage as a correlated peak, a correlated dip or no correlation, and how do the fractions change if you vary it?

## Related work

- Fominov and Mikhailov 2022, "Asymmetric higher-harmonic SQUID as a Josephson diode", <https://arxiv.org/abs/2208.10856>. A trivial two-junction SQUID with a second harmonic in one junction is a flux-tunable diode, and its asymmetry vanishes at integer and half-integer flux.
- Greco, Pichard and Giazotto 2023, "Josephson diode effect in monolithic dc-SQUIDs based on 3D Dayem nanobridges", <https://arxiv.org/abs/2306.12765>. An all-Al dc-SQUID reaches about 20% flux-tunable rectification from higher harmonics in its current-phase relation.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", <https://arxiv.org/abs/2205.09276>. Plain Nb and V films show a strong diode effect at fields of about 1 Oe from vortex barriers and Meissner screening.
- Hess et al. 2023, "Trivial Andreev band mimicking topological bulk gap reopening in the non-local conductance of long Rashba nanowires", <https://arxiv.org/abs/2210.03507>. A trivial Andreev band can produce an apparent gap closing and reopening in nonlocal conductance, alongside trivial end peaks.
- Valentini et al. 2021, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", <https://arxiv.org/abs/2008.02348>. Dots in the tunnel junction host flux-tunable Andreev levels whose Zeeman and Little-Parks dependence gives robust trivial zero-bias peaks.

Happy to rerun this if you share the figure data or the Zenodo files.
