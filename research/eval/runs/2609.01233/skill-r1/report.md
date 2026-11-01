# Lookalike check: Interferometry reveals spin-singlet fractional quantum Hall edges in graphene (arXiv 2609.01233v1)

*AI only. Written by the lookalike assistant on 2026-10-23 from arXiv version v1, with
lookalike library version 0.4. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your experiment is a quantum Hall Mach-Zehnder measurement, at the edge of the
library's scope, so I adapted its interferometer and charge-trap entries (written for
Fabry-Perot devices and fractional shifts) to your p-n junction interferometer.

**The claim, as I read it.** In one graphene p-n junction device, the presence, absence and
FFT frequencies of Aharonov-Bohm oscillations along the interface identify a spin-polarized
ν = 2/3 edge near 11 T (Fig. 2d, Extended Data Fig. ED3) and a spin-unpolarized edge near
8 T (Fig. 3a to 3c), with a sharp change near 9.5 T (Fig. 2b). At low field, components at
f_nm = n f10 + m f01, f11 in particular, are read as two-electron interference through
spin-charge separation with a spin swap (Figs. 3c, 4d), and their temperature dependence
as decoherence from that separation (Fig. 3e).

## Checks a careful reader will look for

1. Map field and gate, and name the regime (Aharonov-Bohm or Coulomb-dominated) : Partly.
   You tie the field frequency to the geometry: "we extract a separation of approximately 170 nm between the
   two arms" (p. 3, Fig. 1e). The regime of the fractional-filling maps isn't discussed.
2. Show the effect is absent where it isn't expected, and rule out charge traps and gate
   leakage : Partly. "only a single winding is allowed in the noninteracting MZI of the
   integer QH regime in Fig. 1" (p. 4), and near 11 T "the AB oscillations exhibit a
   regular pattern with a single frequency (Fig. 2d)" (p. 3). Traps and leakage aren't
   discussed.
3. Repeat sweeps to separate reproducible features from charge jumps : Not done.
4. Report devices and datasets measured, and why others were set aside : Not done. Supplementary Note 1 says "The devices were fabricated from
   high-quality hBN/graphene/hBN/graphite van der Waals heterostructures" (p. 13), with no
   count; the figures show one device.
5. Disclose the full parameter ranges : Partly. "The
   junction transmission exhibits AB oscillations throughout the νN = 2/3 plateau (Fig.
   2b)." (p. 3). The gate and field ranges beyond each map aren't listed.
6. Give the processing from raw data to figures : Partly. You state the fit choice, "after excluding the three lowest-temperature data points" (p. 18, Fig. S3),
   and the data are "available from the corresponding author upon reasonable request"
   (p. 8). The step from raw T to δT and the FFT windows aren't given.

## Lookalikes

| Lookalike | Status | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|
| Coulomb-dominated oscillations: bulk-edge charging adds or sets the periodicity (adapted from Fabry-Perot to your MZI) | Partly addressed | "we extract a separation of approximately 170 nm between the two arms" (p. 3, Fig. 1e); the data bear on it, the paper doesn't discuss it. | For each f_nm in Figs. 2c, 2d and 3b, give the area from the field frequency next to the expected arm separation, and the sign of the constant-phase slope in the B and Vleft plane. |
| Charge trap near the interferometer: a switching trap shifts the AB phase by part of a period (adapted) | Not addressed | Not discussed. The regular pattern near 11 T (Fig. 2d) is a different regime, so I kept the weaker status. | Repeat the Fig. 3b map, look for phase slips at the same (B, Vleft) points, and FFT sub-windows separately to see whether the f_nm set holds in each. |
| Fine-tuning and selection of the shown example | Partly addressed | "The junction transmission exhibits AB oscillations throughout the νN = 2/3 plateau (Fig. 2b)." (p. 3); counts and the choice of the Fig. 3b window aren't given. | State the device and cooldown counts, and show f_nm spectra from other low-field gate settings or cooldowns. |
| Nested multi-path loops in a noninteracting graphene MZI, where a loop enclosing the summed area gives a sum-frequency peak (not in library) | Partly addressed | "The AB oscillations now exhibit two distinct frequencies in the FFT (Fig. 1f), demonstrating the coexistence of two MZIs" (p. 3); the size of any sum peak there isn't reported. | Give the f11 and f02 amplitudes next to f10 and f01, and the FFT level at the sum and doubled frequencies in the (−2, 2) data of Fig. 1f, following the amplitude comparison in Song and Myoung. |

## Questions about devices and data

1. How many devices did you measure, over how many cooldowns, and how many showed the multi-frequency f_nm pattern at low field? Supplementary Note 1 refers to "devices" (p. 13).
2. Why were the others set aside?
3. Which ranges of B, Vleft, Vright and VSi did you measure beyond those in Figs. 2c, 2d and 3b, and at which fields were the integer checks of Fig. 1 and Extended Data Fig. ED2 taken?
4. What does the second-best low-field dataset look like, for example the f_nm spectrum at another gate setting or cooldown?
5. How do you get δT from the raw transmission (background subtraction, derivative, filtering), and which B and gate windows, at what resolution, went into each FFT?
6. Did you repeat the Fig. 3b map, and do phase slips or switching events recur at the same points?
7. What are the f11 and f02 amplitudes relative to f10 and f01, and what is the FFT level at the sum frequency in the (−2, 2) integer data?
8. From your Fig. 3c values, f10 + f01 sits near (0.169 µm², 94.0 V⁻¹), close to the single spin-polarized frequency (0.148 µm², 91.8 V⁻¹) of Fig. 2d. How do you tell an f11 component from a spin-polarized-type interferometer contributing at low field?

## Related work

- Wei et al. 2017, "Mach-Zehnder interferometry using spin- and valley-polarized quantum
  Hall edge states in graphene", <https://arxiv.org/abs/1703.00110>. Graphene p-n junction
  MZIs where same-spin scattering at the physical edge forms the beam splitters.
- Jo et al. 2020, "Quantum Hall valley splitters and tunable Mach-Zehnder interferometer in
  graphene", <https://arxiv.org/abs/2011.04958>. Beam splitters tuned from zero to near
  unity, used to identify the MZ interference and study its bias dependence.
- Song and Myoung 2025, "Asymmetric-gate Mach--Zehnder interferometry in graphene:
  Multi-path conductance oscillations and visibility characteristics",
  <https://arxiv.org/abs/2508.07380>. In modeled graphene p-n MZIs, extra interface
  channels form nested loops, and a loop enclosing the summed area gives a small
  secondary harmonic.
- Goldstein and Gefen 2016, "Suppression of interference in quantum Hall Mach-Zehnder
  geometry by upstream neutral modes", <https://arxiv.org/abs/1605.06060>. Theory for
  ν = 2/3 MZIs in which downstream-upstream mode entanglement suppresses visibility.
- Lafont et al. 2018, "Counter-propagating charge transport in the quantum Hall effect
  regime", <https://arxiv.org/abs/1808.05898>. GaAs devices showing a significant upstream
  charge current at short distances in the spin-unpolarized ν = 2/3 state.

Happy to rerun this if you share the figure data and the FFT windows.
