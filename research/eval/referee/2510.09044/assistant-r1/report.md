# Lookalike check: Imaging of gate-controlled suppression of superconductivity via the Meissner effect (arXiv 2510.09044v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with
lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in
topological transport: ordinary effects that can produce the same signal as the one you
report. For each one that could apply, I note what the paper already shows, quote it, and
suggest a check where one could help. This doesn't judge whether your result is right.
It lists the simple explanations a careful reader will ask about, so you can answer them
first. Your paper images the gate-controlled supercurrent (GCS) effect with scanning NV
magnetometry, outside the library's topological scope, so I used its general entry on
data selection and its practice checks, and added three competing GCS mechanisms from
papers I opened, marked "not in library".

**The claim, as I read it.** A gate power P = IL·VG suppresses Meissner screening in a
region of radius r0 around the gate apex of a Nb island (Fig. 2c, device D2b at 0.45 K;
Fig. 4, device D3), and r0 depends on P alone, independent of bath temperature (0.4 K and
5.6 K), gate polarity and gate voltage (Fig. 3a,b, device D3, gate G1). You read this as a
hot spot of non-equilibrium particles (Eq. 3, diffusion length about 0.6 µm) that excludes
Joule heating, electron injection through vacuum and a direct field effect.

## Checks a careful reader will look for

The library has no check sequence for this kind of signal, so these are its practice checks.

1. Devices and datasets measured, how many showed the effect, why others were set aside : Partly. "We fabricate three geometries in separate fabrication runs" (p. 1), and the suppression "is reproducible given the same applied power P for all our devices" (p. 2). Devices fabricated and imaged per run, and cooldowns ("several cool-downs", p. 3), are not counted.
2. Full parameter ranges measured, and why each shown range was chosen : Partly. "temperatures between 0.4 − 5.8 K" (p. 1) and "B0 ∼ 1 mT" (p. 2). One bias field; no reason given for the power and gate ranges shown.
3. Processing steps from raw data to figures, with data and code : Partly. The Methods give the vector reconstruction ("a Fourier transform-based algorithm [47]", p. 7) and SuperScreen simulations; the r0 extraction is in the Supplementary Materials [25], not in the v1 PDF; data are "available from the corresponding author upon reasonable request" (p. 6), and no code is linked.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Data selection (`fine-tuning-and-selection`) | Tested in part | Devices measured and how many showed it: part; how the shown data were chosen: no; second device or dataset: part (the D2a and D2b r0(P) data are in Figs. S3 and S4, not in the PDF) | "Datasets from devices D2a and D2b (Figs. S3 and S4), which include a broader range of experimental parameters and measurements from several cool-downs, confirm this observation." (p. 3) | Show one D2a or D2b r0(P) set beside Fig. 3a, and say how the Fig. 2c and Fig. 4 scans were picked. |
| Joule (thermal) heating by the leakage power (not in library; Golokolenov et al.) | Tested in part | Suppression compared across bath temperatures: all; local temperature rise estimated from P: no | "Joule heating caused by the leakage current can be excluded because the quenching does not depend on temperature." (p. 3) | Estimate the steady-state temperature rise for 1 to 4 µW at the gate apex in SiO2/Si at both bath temperatures and the r0 shift it predicts; a resistive heater at the same distance, as in Ritter et al. 2021, would compare the two directly. |
| Field-emitted electrons through vacuum (not in library; Alegria et al.) | Tested in part | Gate polarity compared: all; leakage compared with Fowler-Nordheim emission: no | "electron injection through vacuum is ruled out because the effect does not depend on gate polarity" (p. 3) | Fit the IL/VG curves of Fig. 1c to the Fowler-Nordheim form; with the island as cathode the electrons land on the gate apex 80 nm away, which polarity symmetry alone does not separate. |
| Direct electric-field effect (not in library; De Simoni et al.) | Tested in part | r0 against VG at fixed P: part (Fig. 3b mixes powers); leakage current with no field at the superconductor: part (Fig. 4e, one gate pair, field at the island not quantified) | "Data of a plotted against gate voltage \|VG\| showing only weak correlation thereby ruling out a direct field effect." (Fig. 3b caption, p. 4) | Plot r0 against VG at fixed P from the D3 constant-power runs, and give the simulated \|E\| at the island edge for Fig. 4e next to Fig. 4d. |

## Questions about devices and data

1. How many devices did you fabricate in each of the three runs, how many did you image with the NV magnetometer, and how many showed the suppression? Was the nanowire D1 imaged as well?
2. If any devices or cooldowns were set aside (for example for leakage breakdown, vortex pinning or probe problems), why?
3. Which ranges did you measure beyond the ones shown: bias fields other than B0 ~ 1 mT, r0(P) at bath temperatures other than 0.4 K and 5.6 K, gate powers above about 4.5 µW, and r0(P) for gates G2 to G5?
4. What does the second-best dataset look like? The r0(P) data for D2a and D2b sit in Figs. S3 and S4; could the main text show one of them next to Fig. 3a?
5. In Fig. 3b, r0 rises steeply with |VG| within each temperature set, and the two sets reach the same r0 at different |VG|. Could you plot r0 against VG at fixed P, for example from the constant-power runs on D3, where VG is logged while P is held fixed?
6. What local temperature rise would 1 to 4 µW dissipated at the gate apex produce in SiO2/Si at 0.4 K and at 5.6 K, what Tc does the film have (Table S1), and how large a shift in r0 between the two bath temperatures would a thermal model predict?
7. Do the IL/VG curves follow Fowler-Nordheim emission, and does r0 at fixed P change when the onset voltage drifts between curves (Fig. 1c)?
8. Did you measure the transport GCS on the nanowire D1, and at what gate power did its critical current vanish, so the µW powers here can be compared with transport on the same film?

## Related work

- Golokolenov et al. 2020, "On the origin of the controversial electrostatic field effect in superconductors", <https://arxiv.org/abs/2009.00683>. Ties gate suppression in Dayem bridges to overheating by a Fowler-Nordheim leakage current, with a gate response that shifts with bath temperature.
- Alegria et al. 2020, "High-Energy Quasiparticle Injection into Mesoscopic Superconductors", <https://arxiv.org/abs/2005.00584>. Tunnel spectroscopy shows quasiparticle injection by field-emitted electrons, which switch the superconductor normal below 0.1 nA.
- Ritter et al. 2020, "A superconducting switch actuated by injection of high energy electrons", <https://arxiv.org/abs/2005.00462>. Gate switching of TiN, Ti and Nb nanowires tracks the gate current onset, with a polarity asymmetry on SiO2 and a decay length of about 1.2 µm.
- Ritter et al. 2021, "On the Role of Out-of-Equilibrium Phonons in Gated Superconducting Switches", <https://arxiv.org/abs/2106.01816>. With remote gates, a trench and a resistive heater, finds substrate phonons from high-energy electrons suppress superconductivity far more efficiently than Joule heating.
- De Simoni et al. 2017, "Metallic supercurrent field-effect transistor", <https://arxiv.org/abs/1710.02400>. Reports bipolar gate suppression of the critical current in Ti and Al films, read as an electric-field effect.

Happy to rerun this with the Supplementary Materials and r0(P) data.
