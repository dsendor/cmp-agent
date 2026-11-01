# Lookalike check: Josephson diode effect in FeTe0.55Se0.45 van der Waals junctions (arXiv 2610.29124v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

Paper: "Magnetization and Josephson current coupling drives the Josephson diode effect in FeTe0.55Se0.45 van der Waals junctions", https://arxiv.org/abs/2610.29124v1

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a Josephson diode and Shapiro-step study, so the library's diode entry
and practice checks apply directly; I adapted its Shapiro checks, written for missing odd
steps, to your half-integer steps, and added three explanations from outside the library.

**The claim, as I read it.** One FTS van der Waals junction shows a diode at zero applied
field (|Ic+| = 35.2 μA, |Ic−| = 28.9 μA, η = 9.8 %, Fig. 2a-b, p. 7), a Fraunhofer pattern
that depends on sweep direction and a field-independent feature near 170 μV (Fig. 3, Supp.
Fig. 4), and asymmetric ±1/2 Shapiro steps at Bx = 75 G (Fig. 4, Supp. Figs. 6-7). You read
these together as interfacial magnetization coupled to the Josephson current through
spin-orbit coupling, which phase-shifts the first harmonic and enhances the second.

## Checks a careful reader will look for

The library has no ordered checks for diode signals, so these are its practice checks plus
its Shapiro checks adapted to half-integer steps.

1. Report devices and datasets measured, and how many showed the effect : Not done. The abstract says "Our devices exhibit a robust zero-field diode response" (p. 2), and every figure comes from "the same junction" (p. 7); the number fabricated and measured isn't given.
2. Disclose the full parameter ranges and why each shown range was chosen : Partly. You explain the 75 G choice: "This choice minimizes the influence of MR related effects on the microwave response" (p. 12). Out-of-plane field, cooldowns, and Shapiro data at other in-plane fields aren't reported.
3. Give the processing from raw data to figures, with data and code : Partly. The switching criterion is stated, "the bias current at the first point where the absolute junction voltage crossed upward from below a threshold of 10 μV" (p. 16), and the FFT filter is in Supp. Note 3 (p. 28); the data are "available from the corresponding authors upon reasonable request" (p. 17), with no code.
4. Show the dc V(I) and dV/dI without irradiation at the Shapiro settings, with features marked against the step voltages (adapted) : Partly. "the difference between the n-p and p-n sweeps is negligible and the I − V hysteresis is essentially absent" (p. 35); a zero-power trace at 75 G with ±hf/4e marked isn't shown.
5. Show full frequency and power maps : Done at 75 G. The maps "measured at 4.348, 7.580, and 9.680 GHz consistently exhibit integer and asymmetric half-integer Shapiro step structures" (p. 35), over −60 to 10 dBm (p. 15).
6. Run the same measurement where the effect is not expected (adapted: a control junction, or the mirrored field) : Not done. The 0 G data are set aside as "undesirable for analyzing the effective current-phase relation" (p. 34), and no control junction is shown.
7. Measure the junction transparency : Not done. You compare I2/I1 = 0.7 with literature values for transparent junctions (p. 13), with no transparency measurement on this junction.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Meissner screening and asymmetric vortex barriers in the superconductor (`diode-vortex-screening`) | Partly addressed | "the observed zero-field diode response is unlikely to originate from the bulk crystal alone" (p. 7); a crystal-symmetry argument, which leaves geometric screening currents open. | Measure an FTS bridge from the same crystal with no junction, with the same leads and field protocol, and compare η near B0 for flakes of different width. |
| Self-field from nonuniform bias plus a trapped Abrikosov vortex (not in library; Golod and Krasnov 2022, https://arxiv.org/abs/2205.12196) | Partly addressed | "revealing a hysteretic response that is absent in conventional non-magnetic Josephson junctions" (pp. 9-10); the data bear on it (the −8 G centre, the memory), and the paper doesn't discuss vortices or self-field. | Swap the bias leads (Golod and Krasnov flip polarity this way), sweep Bz, warm above Tc,FTS and recool in a reset magnet, and put a non-magnetic reference junction through the same field history. |
| Interference between two parallel channels with unequal phase response (not in library; Li et al. 2023, https://arxiv.org/abs/2306.08478) | Partly addressed | "This feature may arise from an additional transport channel operating in parallel with the dominant Josephson current" (p. 8); the ~11 G component is set aside, and η in Supp. Fig. 1b changes sign on a similar field scale. | Compute η from the FFT-filtered curves of Supp. Fig. 3a and report the zero-field η that remains. |
| Spatial coexistence of 0 and π regions giving half-integer steps (not in library; Yao et al. 2021, https://arxiv.org/abs/2109.13181) | Partly addressed | "no signature of such a 0 − π transition is observed in the present junction" (p. 13); this covers a transition, and leaves 0 and π segments side by side open. | Fit the Bx and By patterns of Supp. Figs. 3-4 (node depths included) with a segmented 0/π model, and show the half-integer steps versus temperature up to Tc,JJ. |
| Bias-dependent resistance features shaping step weight (`shapiro-nonlinear-resistance`, adapted) | Partly addressed | "This choice minimizes the influence of MR related effects on the microwave response" (p. 12); shown at 75 G only. | Overlay the zero-power dV/dI(V) at 75 G on the bin-count voltage axis at each frequency and look for features near ±hf/4e. |
| Fine-tuning and selection (`fine-tuning-and-selection`) | Partly addressed | The maps "consistently exhibit integer and asymmetric half-integer Shapiro step structures" (p. 35); shown for one junction at one in-plane field. | State how many junctions and cooldowns you measured, and show the second-best junction's diode and Shapiro data. |

## Questions about devices and data

1. How many junctions did you fabricate and measure, and how many showed the zero-field diode, the hysteretic Fraunhofer pattern, the 170 μV feature and the asymmetric half-integer steps? The abstract says "Our devices" (p. 2), and the figures all come from one junction.
2. Why were the others set aside?
3. Which ranges did you measure beyond the ones shown: out-of-plane field Bz, other in-plane fields for the Shapiro data (the main lobe, other nodes), temperature for the Shapiro data, and repeat cooldowns?
4. What does the second-best junction or dataset look like?
5. What was the magnet history before Fig. 2a, what is the vector magnet's remanent field at nominal zero on all three axes, and does the −8 G centre move after a magnet reset or a field-cooled cooldown? Which sweep direction does Fig. 2c use, given the shift between the two panels of Fig. 3a (main-lobe maxima at −6 G and +22 G)?
6. Are η in Fig. 2d and Supp. Fig. 1b computed from the raw or the FFT-filtered switching currents, and how large is the zero-field η once the ~11 G component is removed?
7. Does the asymmetry between the +1/2 and −1/2 steps reverse at the mirrored field (about −91 G, the reflection of 75 G about −8 G) and between field-sweep directions, as a field-aligned m+ would predict?
8. What are the flake thicknesses and the d_eff used in Φx = Bx d_eff Ly (p. 24), and does the observed Fraunhofer period match the junction area for both field directions?

## Related work

- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", https://arxiv.org/abs/2205.12196. Zero-field diodes in conventional Nb planar junctions from the self-field of nonuniform bias plus stray fields of a trapped Abrikosov vortex, with polarity set by bias configuration and by trapping or removing the vortex.
- Qiu et al. 2023, "Concurrent Ferromagnetism and Superconductivity in Fe(Te,Se) van der Waals Josephson Junctions", https://arxiv.org/abs/2303.00966. The same material in a van der Waals junction: magnetic hysteresis only below the superconducting transition, 0-π phase mixing in the Fraunhofer patterns, and a stochastic field-free diode.
- Hou et al. 2023, "Ubiquitous Superconducting Diode Effect in Superconductor Thin Films", https://arxiv.org/abs/2205.09276. Strong diode effects in plain Nb and V films at fields as small as 1 Oe, from asymmetric vortex edge or surface barriers and Meissner screening currents.
- Li et al. 2023, "Interfering Josephson diode effect in Ta2Pd3Te5 asymmetric edge interferometer", https://arxiv.org/abs/2306.08478. A diode at tiny applied fields from interference between asymmetric edge channels, with half-integer Shapiro steps confirming the second harmonic that the interference produces.
- Yao et al. 2021, "Half-integer Shapiro Steps in Strong Ferromagnetic Josephson Junctions", https://arxiv.org/abs/2109.13181. Half-integer steps in Nb-NiFe-Nb junctions, attributed to coexisting 0 and π states from spatial variation of the barrier thickness.

Happy to rerun this if you share the switching-current data behind Fig. 2c and Supp. Fig. 1b, or the Shapiro maps at other fields.
