# Lookalike check: Orientation-tunable correlated Chern insulators in WSe2/cTDBG (arXiv 2606.31267v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper is a moiré graphene Chern insulator measurement, outside the library's
hybrid superconductor core, so I adapted the quantization and practice entries to a Hall
plateau and a Streda slope, and added three explanations from the moiré literature marked
"(not in library)". The supplementary material was not in the PDF I read, so anything that
lives only in Supplementary Table I or Supplementary Figs. 1 to 11 counts here as stated, not shown.

**The claim, as I read it.** At quarter filling (ν = −1), WSe2/cTDBG devices with Φ ≈ 0°
show a correlated insulator that turns into a C = +1 state in field: a Streda line from
ν = −1 and Rxy reaching 97.6% of −h/e2 at B ≈ 3.0 T (device D1, Fig. 4a to d). A Φ ≈ 15°
device (D3) shows a similar zero-field insulator with a field-independent feature, read as
C = 0 (Fig. 4e, f). You read the contrast as Φ setting the topology through Ising versus
Rashba SOC (Figs. 1, 2).

## Checks a careful reader will look for

The library has no check list for Chern insulators or Hall quantization, so these are the
practice checks that apply to every paper.

1. Report devices and datasets measured, how many showed the effect, and why others were set aside : Partly. "transport data from seven devices spanning three categories: three Φ ≈ 0° devices (D1, D2, D4) all exhibiting C = +1" (p. 12); how many were fabricated, and whether any were set aside, isn't stated.
2. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Your figures show D from −1 to 1 V/nm, B from 0 to 7 T and T from 20 mK to 10 K, and the fans are "at D = 0.6 V/nm and T = 25 mK" (p. 9); why that D was chosen, and whether fans were taken at other D or at negative B, isn't stated.
3. Give the processing steps from raw data to figures, with data and code : Partly. "All data generated in this study are provided in the Source Data file." (p. 17), and the band-structure code is provided; the steps for Rxy (field antisymmetrization, the masking in Fig. 4b) and the Arrhenius fit range aren't described in the main text.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection | Tested in part | Devices and how many showed it: part; how shown data were chosen: no; second device shown: part | "We focus on two representative devices with cTDBG twist angles of 0.93° and 0.80°" (p. 8); D2 appears only at zero field (Fig. 3c to f) | Show the D2 and D4 fans and Rxy beside Fig. 4a to d, and say what "representative" meant |
| Quantized value from a fine-tuned trivial state (adapted from fine-tuned-plateau) | Tested in part | How it was found: all; wider field and gate ranges: all; other regimes and devices: part | "Hall quantization reaches 97.6% of −h/e2 at B ≈ 3.0 T" (Fig. 4d); the cut follows the C = +1 line over 0 to 7 T and falls to 79.7% at 2 T and 87.5% near 5 T (Fig. 4d) | Show Rxy along the same line at other D and in D2 and D4, so readers see how the best value compares |
| Field-catalyzed Chern insulator from Hofstadter subbands (not in library) | Tested in part | Zero-field anomalous Hall with hysteresis: no; onset field against the B = 0 state: part | The fan "becomes well developed above approximately 0.3 T" (p. 9); "achieving quantum anomalous Hall quantization at zero magnetic field ... remains an open goal" (p. 12) | Sweep B both ways through zero at ν = −1 in D1 and D2 and look for an anomalous Hall signal or hysteresis, as Kuiri et al. and He et al. did in tDBG |
| Unintended hBN alignment breaking C2 (not in library) | Not tested (argued, not tested) | hBN angle reported per device: no; search for hBN-moiré peaks: no | "with sublattice symmetry breaking playing a subleading role (Supplementary Fig. 11; see Supplementary Section XI for details)" (p. 11) | Report the bottom and top hBN angles from optical edges, and scan density past ±2×10^12 cm^-2 for extra full-filling peaks |
| Twist-angle difference or inhomogeneity between compared devices (not in library) | Not tested (argued, not tested) | Same-θ devices compared across Φ: no (D2 and D5 stated, not shown); θ homogeneity within a device: no; Landau-level quality compared: no | "D2 and D5 share the same twist angle (θ = 0.80°) and differ only in Φ, providing a direct controlled comparison" (p. 12); D1 is 0.93° and D3 is 0.83° (Fig. 4) | Bring the D2 and D5 fans into the main text, give θ from several contact pairs, and compare CNP Landau levels of D1 (Fig. 4a) and D3 (Fig. 4f) |

## Questions about devices and data

1. How many WSe2/cTDBG devices did you fabricate and measure in all, and how many at each alignment angle showed the ν = −1 state and a C = +1 or C = 0 fan? Your p. 12 lists seven; were others measured?
2. Were any devices or cooldowns set aside (for example for contacts, gate leakage, or no ν = −1 state), and why?
3. Which displacement fields and field directions did you measure Landau fans at beyond D = 0.6 V/nm and B from 0 to 7 T, for D1 and D3, and does the C = +1 line from ν = −1 hold across the D range where the zero-field peak exists (Fig. 3e)?
4. What do the Landau fans and Rxy of D2 and D4, your second- and third-best Φ ≈ 0° devices, look like next to Fig. 4a–d, and how close to −h/e2 does Rxy get there?
5. Is Rxy in Fig. 4b,d antisymmetrized in field, and how does the "longitudinal admixture" that you mask near CNP in Fig. 4b enter along the ν = −1 trajectory where the 97.6% is read?
6. Could you show Rxy for D3 along the line where a C = +1 state from ν = −1 would run, and the CNP Landau levels of D3 next to those of D1, so the C = 0 assignment rests on Hall data from a device whose fans resolve? In Fig. 4f the CNP Landau levels are hard to make out.
7. Did you look for an anomalous Hall signal or field hysteresis at ν = −1 near B = 0 in the Φ ≈ 0° devices, and do you know the hBN-graphene alignment angles (or see hBN-moire peaks) in each device?
8. How was Φ checked independently of the Chern numbers, given that Methods (p. 13) use "the consistency of the measured Chern numbers across all aligned devices" as "a posteriori confirmation of the alignment assignment"?

## Related work

- He et al. 2021, "Symmetry-broken Chern insulators in twisted double bilayer graphene", <https://arxiv.org/abs/2109.08255>. Across more than a dozen tDBG devices in both stackings, Chern insulators appear only in a narrow twist-angle window, each with an anomalous Hall effect at zero field, so θ alone can switch the topological response.
- Kuiri et al. 2022, "Spontaneous time-reversal symmetry breaking in twisted double bilayer graphene", <https://arxiv.org/abs/2204.03442>. Anomalous Hall hysteresis spanning hundreds of mT in tDBG, the zero-field test for valley polarization.
- Saito et al. 2020, "Hofstadter subband ferromagnetism and symmetry broken Chern insulators in twisted bilayer graphene", <https://arxiv.org/abs/2007.06115>. Chern insulators with |C| = 1 to 3 appear from about 2 T, driven by Hofstadter subbands, and B can catalyze them out of an unpolarized B = 0 state.
- Serlin et al. 2019, "Intrinsic quantized anomalous Hall effect in a moiré heterostructure", <https://arxiv.org/abs/1907.00261>. Zero-field Hall quantization in twisted bilayer graphene; the text ties the ferromagnetism to hBN alignment breaking C2 and uses hBN-moiré resistive peaks to check that alignment.
- Uri et al. 2019, "Mapping the twist angle and unconventional Landau levels in magic angle graphene", <https://arxiv.org/abs/1908.04595>. Local twist-angle maps show variations of about 0.1° inside good transport devices, enough to reshape the quantum Hall state.

Happy to rerun this with the supplementary material and the Source Data file.
