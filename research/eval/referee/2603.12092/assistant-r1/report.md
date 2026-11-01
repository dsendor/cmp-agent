# Lookalike check: Twisted high-Tc SQUID senses emergent interfacial order (arXiv 2603.12092v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is phase-sensitive SQUID interferometry on a twisted cuprate, a
different measurement from the library's tunneling and Shapiro entries, so I adapted the
diode and practice entries and added three lookalikes from outside the library, each
with a paper I opened. The SI (SI 1 to SI 14) is cited throughout but is not in the v1
PDF, so I judged only the main text, Figs. 1 to 5 and Extended Data Figs. 1 and 2.

**The claim, as I read it.** In a 45° twisted Bi-2212 SQUID at 20 K, the extrapolated
I = 0 intercept of the dV/dI minima moves from an integer flux period (Fig. 3a, 10 µT
in-plane) to a half-integer one (Fig. 3b, 0 µT in-plane; Extended Data Fig. 2), which
you read as ϕ12 ≈ π from d ± id order of opposite chirality in the two arms. Supporting
claims: a finite η′ at B = 0 in a 45° and a 40° device (Fig. 4a, b) read as broken
time-reversal symmetry, and a second harmonic in Is(B) (Fig. 4c, d) read as Cooper pair
co-tunneling.

## Checks a careful reader will look for

The library has no ordered checks for SQUID phase or diode signals, so only the practice
checks apply.

1. Report devices and datasets, how many showed the effect, and why others were set aside : Partly. You list "(0°, 40°, 42°, 44°, 45° devices, details of the devices are provided in supplementary information SI 3)" (p. 4); how many showed the half-period intercept is not given.
2. Disclose full parameter ranges and why each shown range was chosen : Partly. "We sweep the in-plane magnetic field from −20 µT to 20 µT and sweep it back, both sweeps in steps of 10 µT." (p. 9); the reasons for this range and for the bias ranges in Fig. 3 are not given.
3. Give the processing steps from raw data to figures, with data and code : Partly. "We track the relative phase of the minima of these dV/dI oscillations" (p. 9); the background subtraction in Fig. 4d is not described, and the PDF has no data or code statement.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Counts: part; how data were chosen: no; second device or dataset: part | "Data from another device is shown in SI 14." (p. 9); in the PDF the phase result comes from one 45° device | State how many devices show each signal and show the second-best phase dataset |
| Vortex barriers and Meissner screening giving a diode (adapted to the zero-field η′) | Tested in part | Same measurement on a plain junction: part (0° SQUID data sit in SI 9, absent from the v1 PDF); followed against field: all | "The nominally 0° twisted SQUID does not show a diode effect at zero magnetic field and serves as a crucial control." (p. 7) | Plot the 0° device's η′(B) beside Fig. 4a and 4b at matched temperature and bias |
| Vortex-induced Josephson phase shift (not in library) | Not tested (data bear on it) | Flux trapped vs removed: no; phase values checked for shifts between 0 and π: no | "the in-plane field [12, 49] can result in flux focusing due to the coupling of Josephson and Abrikosov vortices" (p. 10); Extended Data Fig. 2 shows half-integer values near 0.75π to 0.95π that depend on sweep direction | Warm above Tc, cool in zero field, and repeat the Fig. 3 intercept at each in-plane value; give intercept error bars |
| Vortex stray field with nonuniform bias, zero-field diode (not in library) | Not tested (data bear on it) | Vortex trapped vs removed: no; bias contacts changed: no; Is(B) pattern offset measured: no | "there is time reversal symmetry breaking at B = 0 as the switching currents are not the same at the zero magnetic field." (p. 11); in Fig. 4a the two traces look like copies shifted along B | Fit the shift between Is+(+B) and \|Is−(−B)\|, measure the residual field, and repeat after zero-field cooling and with swapped current contacts |
| Asymmetric-SQUID readout distortion of the CPR (not in library) | Not tested (data bear on it) | Derivative asymmetry shown: no; angle-shaped extremes checked: no | "However, in our devices, the geometric inductance and the Josephson inductance are comparable." (p. 8); Fig. 4c shows cusp-like maxima | Simulate Is(Φ) for a first-harmonic CPR with 3:1 asymmetry and β ∼ 1, and compare its FFT with Fig. 4d |

## Questions about devices and data

1. How many SQUIDs did you fabricate and measure, and in how many did you see a half-period intercept, a finite η′ at B = 0, and the second harmonic? Your p. 4 lists 0°, 40°, 42°, 44° and 45° devices, but the counts behind each claim are not in the v1 PDF.
2. Why were the other devices set aside for the phase measurement, and does any device show only integer intercepts at every in-plane field?
3. Which in-plane fields, perpendicular field ranges, bias currents and temperatures did you measure beyond those shown, and were the in-plane sweeps of Extended Data Fig. 2 repeated in another cooldown?
4. What does the second-best phase dataset look like? SI 14 is cited for another device but is not part of the v1 PDF.
5. What is the uncertainty on each intercept in Fig. 3 and Extended Data Fig. 2? The fit in Fig. 3a spans 41 to 59 µA and extrapolates to I = 0 over more than twice that span, and the slopes in Fig. 3a and 3b read about 0.05 and 0.07 period per µA to me; why would A Lgeo change between 0 and 10 µT in-plane field, and how did you make sure each star tracks the same minimum?
6. Did you warm above Tc and cool in zero field between in-plane settings, and does the intercept repeat after that? The half-integer values spread from about 0.75π to 0.95π and differ between sweep directions at 0 µT (Extended Data Fig. 2), and the period is about seven times smaller than Φ0/Ageo (p. 6), which suggests flux in the surrounding flakes couples to the loop.
7. Where is the true zero of flux in Fig. 4? Is+(+B) and |Is−(−B)| in Fig. 4a look like copies shifted along B; what residual field do you measure inside the cryoperm shield, what offset would bring η′(0) to zero, and how does the 0° control's η′(B) compare?
8. Did you simulate Is(Φ) for a purely first-harmonic CPR with your 3:1 arm asymmetry and β ∼ 1, and compare its FFT with Fig. 4d? How was the background in Fig. 4d chosen and subtracted?

## Related work

- Zhao et al. 2021, "Emergent Interfacial Superconductivity between Twisted Cuprate Superconductors", <https://arxiv.org/abs/2108.13455>. Twisted Bi-2212 junctions whose critical current density falls by almost two orders of magnitude near 45° yet stays finite, with fractional Shapiro steps and Fraunhofer analysis read as Cooper pair co-tunneling.
- Zhu et al. 2019, "Presence of s-wave pairing in Josephson junctions made of twisted ultrathin Bi2Sr2CaCu2O8+x flakes", <https://arxiv.org/abs/1903.07965>. Over 90 twisted Bi-2212 junctions with Josephson tunneling seen repeatedly at a nominal 45°, read as a persistent s-wave component; a useful benchmark for device counts.
- Golod, Rydh and Krasnov 2010, "Detection of the phase shift from a single quantized superconducting vortex", <https://arxiv.org/abs/1003.1033>. A single trapped Abrikosov vortex near a junction gives a π-step or an arbitrary phase shift between 0 and π, switched by trapping and removing the vortex.
- Golod and Krasnov 2022, "Demonstration of a superconducting diode-with-memory, operational at zero magnetic field with switchable nonreciprocity", <https://arxiv.org/abs/2205.12196>. Conventional Nb junctions show large zero-field nonreciprocity from nonuniform bias plus stray fields of a trapped vortex, switched on and off by trapping and removing it.
- Babich et al. 2023, "Limitations of the current-phase relation measurements by an asymmetric dc-SQUID", <https://arxiv.org/abs/2302.02705>. The same device shows both skewed and sinusoidal SQUID oscillations; the measured shape follows the CPR only when the arms differ strongly in the derivatives of their supercurrents.

Happy to rerun this with the SI and the figure data if you share them.
