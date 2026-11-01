# Lookalike check: TI nano-SQUID global and local superconductivity (arXiv 2608.17404v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your main evidence is global (critical current and diode effect), which the library
covers only through its diode entry, so I adapted four entries and added one from outside
it. Page numbers are PDF pages (Supplement: pp. 10 to 16).

**The claim, as I read it.** In nano-SQUIDs A, B and C, h/2e oscillations of Ic and a
diode effect whose sign reverses at half-integer flux (Fig. 1e, 3a, S2a, S4), together with
local and nonlocal spectral jumps at the same fields (Fig. 1f-g, 3b-e, S2b-e), are read as a
flux-driven transition into a topological phase. Zero-bias peaks appear at both ends in expected
topological and trivial regimes, including zero field (Fig. 4, S3), and you read some as
disorder states.

## Checks a careful reader will look for

1. Unintended dots near the barriers : Not done. The zero-field gate maps (Fig. 4a-b, S3a-b) could show dot resonances; the text doesn't look for them.
2. Wide gate, field and angle ranges, with peak heights : Partly. "even over a region of VG that includes the Dirac point (Fig. 4j-k)" (p. 5); peak heights are not reported and the angle is fixed.
3. Both ends at the same settings : Partly. "we analysed the correlation of local states at opposite ends of the nanowire" (p. 5); devices B and C only.
4. Peak stability against junction transparency : Not done. The barriers have no gate of their own.
5. Nonlocal gap closing and reopening : Partly. "the nonlocal conductance reveals features that align with the Ic oscillations" (p. 4); some jumps match no Ic feature (p. 5).
6. Series and line resistance, raw data : Partly. The method is given (p. 11, quoted below); values and uncorrected data are not shown.
7. Device and dataset counts : Partly. "the yield of functional tunnel junctions fabricated on top remains below 50%" (p. 5); totals fabricated and measured are missing.
8. Full parameter ranges and why each was shown : Partly. "in this device A, the gating range was limited due to a leaky gate dielectric" (p. 12); temperature stays at base, and the Fig. 4 and S3 field cuts are not explained.
9. Processing, data and code : Partly. "The data that support the findings of this study are available at the online depository zenodo" (p. 7); the Fig. 4l classification and code are not described.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Trivial interferometer diode: non-sinusoidal junctions in a SQUID (not in library; Greco et al., https://arxiv.org/abs/2306.12765) | Partly addressed | "This h/2e periodicity and the almost complete revival of Ic for an integer flux quantum demonstrate that the surface state is dominant such that there is a negligible bulk contribution to the supercurrent" (p. 2, Fig. 1e); this argues surface dominance and leaves open whether ordinary junctions give the same Ic(Φ) and η(Φ). | Fit Ic±(Φ) with a two-junction model using ordinary skewed current-phase relations; a device with the Fermi level in the bulk bands would test it directly. |
| Vortex and screening diode (diode-vortex-screening) | Partly addressed | "Their strong dependence on the magnetic-field sweep direction points to a vortex dynamics and flux trapping origin within the Nb electrodes." (p. 4); discussed for high-field conductance jumps, while the diode data near zero field bear on it without discussion. | Show Ic± for both sweep directions and both field signs, and a plain Nb junction from the same process. |
| Accidental zero crossing at phase pi (transparent-junction-pi-crossing, adapted) | Partly addressed | "the main feature of the spectra, namely the abrupt appearance of the zero-bias conductance anomaly at half-flux quantum, is very stable over the examined gate-voltage range" (p. 12, Fig. S1); density is varied; transparency is untested. | Track the device A anomaly against RN over the full gate range and look for an anticrossing opening. |
| Dot Andreev states (abs-quantum-dot) | Partly addressed | "Although the zero field ZBPs largely have a strong dependence on VG (Fig. 4a-b)" (p. 5); the data bear on it; the paper doesn't discuss dots. | Search Fig. 4a-b and S3a-b, at higher bias too, for diamonds and recrossing peaks. |
| Kondo resonance (kondo-resonance) | Not addressed | Not discussed. | Check whether zero-field peaks sit in alternating gate windows, and show temperature and field splitting. |
| Disorder states (disorder-induced-zbp) | Partly addressed | "The fact this occurs even in theoretically trivial regions suggests that at least some of these ZBPs are driven by disorder effects" (p. 5); raised for the ZBPs in general, untested for the device A peak. | Fine gate steps around the device A peak, and peak-height scatter at each end. |
| Crowded trivial states (crowded-trivial-subgap-states) | Partly addressed | "with both showing a large number of ZBPs at both ends" (p. 5); no subband model is given. | Give the fraction of gate settings with a ZBP at each end, per flux lobe, from existing data. |
| Quasi-Majorana states (quasi-majorana-smooth-confinement) | Partly addressed | "As Bx is further increased the ZBP persists for a large range of Bx." (p. 3, Fig. 1f); device A has one probe. | Show where the device A peak first appears relative to the half-flux jump at every gate voltage of Fig. S1. |
| Flux-tunable dot levels at the probe (full-shell-flux-andreev, adapted) | Partly addressed | "we observe these even in theoretically trivial windows and notably even at zero Bx." (p. 5); peaks outside odd lobes bear on it; the probe region is not varied. | Compare subgap states across tunnel-contact geometries in A, B and C. |
| One end only (one-end-only) | Partly addressed | "We find that both regimes contain ZBPs on either end (see Fig. 4c,f,i,l) the majority of the time" (p. 5); devices B and C only. | Say whether the first-window peak of device A has a partner at the other end in B and C at the same gate voltage. |
| Local probe loophole (local-probe-loophole) | Partly addressed | "This disparity highlights that an apparently clear bulk topological transition does not guarantee the isolation of topological boundary modes" (p. 5); the overlap is estimated from a localisation length only. | Use zero-bias nonlocal conductance per gate setting as an overlap check. |
| Trivial Andreev band (trivial-andreev-band-gap-reopening) | Partly addressed | "there are also nonlocal conductance jumps at Bx values that do not correspond to the Ic features, especially at large values of magnetic flux" (p. 5); the gate maps of Fig. S5 bear on it. | Nonlocal conductance versus flux at several gate voltages, counting jumps that match Ic minima. |
| Circuit correction of conductance (series-resistance-subtraction, adapted) | Partly addressed | "The line resistances required were determined from two-terminal resistance measurements of the cryostat lines" (p. 11); values not given. | Give the resistances and show GLR and GRL before correction. |
| Choices in the correlation count (protocol-parameter-sensitivity, adapted) | Partly addressed | "we evaluated the end-to-end correlation using the relative signs of the third derivative of the current at zero bias" (p. 5); smoothing and the "no correlation" threshold are not given. | Rerun Fig. 4l with smoothing and threshold varied, and with one end's gate trace shifted as a null. |
| Fine-tuning and selection (fine-tuning-and-selection) | Partly addressed | "are also observed in all examined devices and are largely robust against gate voltage" (p. 4); the number examined is not stated. | List every nano-SQUID measured, its working probes, and which showed the global signals. |

## Questions about devices and data

1. How many nano-SQUIDs did you fabricate and measure, and how many showed the Ic oscillations and the diode sign reversal? Your p. 4 says "all examined devices"; how many is that?
2. Why were devices other than A, B and C set aside, and what did their tunnel spectra look like?
3. Which ranges of field, field angle, gate voltage and temperature did you measure beyond the ones shown, and why were Bx = 0, 1 and 2 T chosen for Fig. 4 and 0, 2.5 and 4 T for Fig. S3?
4. What does the second-best device look like for the zero-bias peak that device A shows in the first expected topological window? In device C, "a zero-bias conductance peak was mostly absent in this device" (p. 13) in the field sweep, while its gate analysis shows "a strong increase of correlated zero-bias conductance peaks" (p. 14); could you show the two side by side?
5. Do your diode data satisfy Ic+(B) = |Ic-(-B)| over the full field range, and does η depend on the field sweep direction?
6. In Fig. 4l, how are settings with near-zero curvature at zero bias classified, and what fraction of "correlated peaks" would you expect by chance, given that one back gate tunes both ends at once?
7. What line resistances did you use to correct the nonlocal conductance, and could you show GLR and GRL before the correction?
8. Would a nano-SQUID with the same Nb leads and ordinary, non-sinusoidal junctions (or this device with the Fermi level in the bulk bands) show the same Ic(Φ) and η(Φ), including the sign reversal at half-integer flux?

## Related work

- Greco, Pichard and Giazotto 2023, "Josephson diode effect in monolithic dc-SQUIDs based on 3D Dayem nanobridges", <https://arxiv.org/abs/2306.12765>. An all-Al dc-SQUID gives a flux-tunable diode near 20% from current-phase harmonics alone.
- Fominov and Mikhailov 2022, "Asymmetric higher-harmonic SQUID as a Josephson diode", <https://arxiv.org/abs/2208.10856>. With a second harmonic in one junction, the diode depends on flux and vanishes at integer and half-integer flux.
- Dartiailh et al. 2019, "Phase signature of topological transition in Josephson Junctions", <https://arxiv.org/abs/1906.01179>. A pi jump in junction phase with an Ic minimum in an Al/InAs loop, read as a topological transition.
- Valentini et al. 2020, "Nontopological zero-bias peaks in full-shell nanowires induced by flux tunable Andreev states", <https://arxiv.org/abs/2008.02348>. Robust zero-bias peaks follow the tunnel junction region and come from flux-tunable dot Andreev levels.
- Hess, Legg, Loss and Klinovaja 2022, "Trivial Andreev band mimicking topological bulk gap reopening in the non-local conductance of long Rashba nanowires", <https://arxiv.org/abs/2210.03507>. A trivial Andreev band mimics gap reopening in nonlocal conductance, alongside trivial end peaks.

Happy to rerun this if you share the figure data or the code behind Fig. 4l.
