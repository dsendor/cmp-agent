# Lookalike check: Multiple nodal superconducting phases in pressurized UTe2 (arXiv 2601.01843v1)

*AI only. Written by the lookalike assistant on 2026-10-25 from arXiv version v1, with lookalike library version 0.5. A person hasn't checked it.*

**What this is.** I read your paper against a library of 28 known lookalikes in topological transport. These are ordinary effects that can produce the same signal you report. For each one that could apply, I note what the paper already shows, quote it, and suggest a check where one could help. This doesn't judge whether your result is right. It lists the simple explanations a careful reader will ask about, so you can answer them first. The library is written for hybrid nanowire and junction devices, and yours is point-contact spectroscopy on a bulk crystal. So I adapted its zero-bias-peak entries to a soft point contact and added two lookalikes from the point-contact literature.

**The claim, as I read it.** You see a zero-bias conductance peak (ZBCP) on the (0 0 1) surface of UTe2 at ambient pressure in samples S1 to S3 (Fig. 2). In S1 under pressure, side dips appear above 0.3 GPa and double dips at 1.0 to 1.2 GPa (Figs. 3, S3). An extended BTK model reads these as zero-energy Andreev bound states from a pz component. Its weight ⟨∆z⟩/⟨∆x(y)⟩ grows from SC1 to SC3 and has a temperature minimum at the SC2 to SC3 boundary (Fig. 5).

## Checks a careful reader will look for

1. Look for ordinary zero-bias anomalies near the contact (adapted from the dot search to magnetic or Kondo scattering) : Partly. The field series covers S1 at ambient pressure only, 0 to 8 T at 0.5 K (Fig. S2a). The paper says: "However, this is not relevant here because UTe2 does not exhibit magnetic ordering at ambient pressure [12]." (p. 5)
2. Show the peak over wide ranges, including where it is absent (adapted to pressure, temperature and field) : Partly. S1 is shown from 0 to 1.4 GPa and 0.3 to 3.6 K (Figs. 3, S3). There is no field data under pressure, and no PCS above 1.4 GPa, although the cell reaches "∼ 1.8 GPa" (p. 11).
3. Show the peak stays as the junction transparency changes (adapted to contacts with different Z) : Partly. "ZBCP are also observed in different samples (S2 and S3) with various contact sizes and resistances, seeing Fig. 2(e,f)." (p. 5). Z runs from 0.76 to 1.67 (Table S1), with a single contact under pressure.
4. State the series resistance subtracted and how it was calibrated, and show the raw data : Not done. GNS is shown in "(arb. unit)", and no contact resistance or normalization step is given.
5. Report devices and datasets measured, how many showed the effect, and why others were set aside : Partly. "To check the reproducibility of the results, two additional samples (S2 and S3) were measured at ambient pressure." (p. 11)
6. Disclose the full parameter ranges measured and why each shown range was chosen : Partly. Pressures, temperatures, the ±4 mV bias and the 8 T field are given in the figures. The reasons for the ranges are not given.
7. Give the processing steps from raw data to figures, with data and code : Partly. The BTK model and fit parameters are in SI IV to VI. The paper says "all source data supporting the findings of this study are available within the paper." (p. 12). Normalization, raw data and code are not given.

## Lookalikes

| Lookalike | Status | Tests shown | What the paper shows (quote, page or figure) | Suggested check |
|---|---|---|---|---|
| Fine-tuning and selection of the shown contact | Tested in part | Counts and how many showed it: part; how shown data were chosen: no; second device or dataset: part | "two additional samples (S2 and S3) were measured at ambient pressure" (p. 11); all pressure data come from S1 | Say how many contacts you made in the cell and at ambient pressure, and show a second pressurized contact or a repeat on release |
| Magnetic or Kondo zero-bias anomaly (adapted from kondo-resonance) | Tested in part | Even-odd occupancy: no (no dot here); temperature dependence: part; Zeeman splitting: part | "magnetic scattering may also induce conductance peaks at zero bias [45, 46]" (p. 5); no splitting up to 8 T at ambient pressure (Fig. S2a) | Take field sweeps at 0.6 to 1.4 GPa, closest to MO1 and MO2, and check whether the ZBCP splits |
| Normalization and series resistance set the peak height (adapted from series-resistance-subtraction) | Not tested (not mentioned) | Series resistance with value: no; raw data: no | Not discussed. The peak heights of 1.70 and 2.08 (p. 8) carry the pz argument | Report R_N and G0 for each contact and pressure, and show the raw dI/dV |
| Non-ballistic contact: critical-current dips and zero-bias enhancement (not in library) | Tested in part | Regime from R_N and mean free path: no; dips versus contact resistance: no; dip voltage versus critical current: no; peak amplitude and width in T and field: part | "we rule out this possibility because the shape of the peak degrades gradually with increasing T, and an application of a small field (< 2 T) only weakly affects its width, as shown in Fig. S2(a)" (p. 5) | Integrate dI/dV to I(V) and test whether the side dips sit at fixed current in T. The 1.4 GPa dips move inward on warming (Fig. 3d) |
| Parallel contacts over regions with different gaps (not in library) | Left open by the authors | Contact size from R_N: no; gap components to their own closing temperature: no; second contact at the same pressure: no | "An alternative possibility is due to pressure inhomogeneity, in the regard that the NM-SC junction may cover several SC domains with different gap parameters." (p. 9) | Follow each two-channel component in Fig. S9c to its own closing temperature, and refit Fig. 5f with two channels to see whether the minimum stays |

## Questions about devices and data

1. How many point contacts did you make on (0 0 1) surfaces, at ambient pressure and in the pressure cell, and how many showed a ZBCP? Your Methods give three samples at ambient pressure and one contact, on S1, under pressure; were there others?
2. Why were any other contacts or pressure runs set aside?
3. Which ranges did you measure beyond the ones shown: point-contact spectra above 1.4 GPa (the cell reaches about 1.8 GPa and Fig. 2b goes to 1.8 GPa), bias beyond ±4 mV, and magnetic field under pressure?
4. What does the second-best contact look like under pressure, and did the 0.6 to 1.2 GPa spectra repeat on a second contact or on releasing pressure?
5. What were the normal-state resistances of the S1, S2 and S3 contacts at each pressure, how did you choose the normalization G0, and could you show the raw dI/dV before normalization?
6. From those resistances and the mean free path implied by RRR ≈ 410, is each contact in the ballistic regime? If you integrate dI/dV to I(V), do the side dips at 0.6 to 1.4 GPa sit at a fixed current as temperature changes?
7. Did you take field sweeps under pressure, especially between 0.6 and 1.4 GPa near MO1 and MO2? Does the ZBCP split, and do the side dips move with field?
8. Table S1 lists ∆z = 1.18(7) meV and ∆x(y) = 0.72(4) meV for S1, while Fig. S7a gives ∆x(y) = 1.18(7) meV and ∆z = 0.72(4) meV for the same 0.3 K fit; which labels are right, and how much does ⟨∆z⟩/⟨∆x(y)⟩ move when you refit the 0.6 and 0.8 GPa data with two channels or with the other representations?

## Related work

- Yoon et al. 2024, "Probing p-wave superconductivity in UTe2 via point-contact junctions", <https://arxiv.org/abs/2403.00933>. Point contacts on several UTe2 facets at ambient pressure, down to 250 mK and up to 18 T. A p-wave BTK fit gives a py gap of 0.26 ± 0.06 meV, a useful comparison for your fitted gap amplitudes.
- Gu et al. 2025, "Pair Wavefunction Symmetry in UTe2 from Zero-Energy Surface State Visualization", <https://arxiv.org/abs/2501.16636>. Zero-energy Andreev conductance at the (0-11) surface with s-wave tips. The peak splits with enhanced proximity, pointing to a non-chiral B1u, B2u or B3u state.
- Sheet, Mukhopadhyay and Raychaudhuri 2004, "The role of critical current on point contact Andreev Reflection spectrum between a normal metal and a superconductor", <https://arxiv.org/abs/cond-mat/0311648>. Conductance dips above the gap track contact area and come from contacts outside the ballistic limit. Thermal-regime contacts can raise the zero-bias conductance above twice its high-bias value.
- Daghero and Gonnelli 2010, "Probing multiband superconductivity by point-contact spectroscopy", <https://arxiv.org/abs/0912.4858>. A review. Soft contacts conduct through parallel nanometric channels, and dips shift to lower energy on warming and "can make a broad maximum centered at zero bias look as a sharp zero-bias conductance peak" (p. 13).
- Kirzhner et al. 2012, "Unconventional superconductivity in CuxBi2Se3", <https://arxiv.org/abs/1111.5805>. Point contacts on the same crystals of a candidate odd-parity superconductor give three kinds of spectra, one of them with zero-bias conductance peaks.

Happy to rerun this if you share the raw dI/dV curves and the contact resistances.
