A. Must address

1. The curvature criterion has not been shown to be specific to flat bands, and the competing explanations are dismissed too quickly. The headline claim (abstract, Conclusion) is that sublinear or superlinear high-T ρ(T) is a "clear and universal fingerprint" of FB proximity that "directly reveals" it. The alternatives get one paragraph on p. 6 and no quantitative tests. (a) Resistivity saturation: the MIR/parallel-resistor exclusion rests on the assertion "good metals (well below the MIR limit)", with no numbers. Yet in Fig. 5a Ni3In (Gim et al. data) reaches ≈120–150 µΩ cm by 300 K, and Ca(Rh,Ru)2 and Ni3Ge reach ≈160 µΩ cm at 860 K. Fig. 4a shows ρ − ρ0 ≈ 75 µΩ cm for Ni3In with clear flattening. These values lie within a factor of ~1–2 of typical intermetallic saturation values (~100–200 µΩ cm). (b) Sublinearity is generic: the curvature responds to any steep D(E) near E_F, and an ordinary dispersive d-band edge gives the same sublinear ρ(T). This is Mott's classic s-d case for Pd, Pt and Ni alloys, which is essentially this model. (c) Superlinearity is generic: above ~400 K, thermal expansion at constant pressure, phonon softening and anharmonicity, and Debye-Waller effects commonly produce superlinear ρ(T) in metals with no nearby FB. These are not discussed, although CoSn (Fig. 5e), Pt3Sn and Pd3Pb are assigned to "E_F above the FB edge" on exactly this basis. The authors should: give a mean-free-path or k_F ℓ estimate (from DFT Fermi velocities and carrier density) and ρ_sat for each compound; fit the same high-T data with BG plus a parallel-resistor saturation term, and with BG using an energy-independent DOS plus thermal expansion, then compare goodness of fit with the same number of free parameters, at least for Ni3In and Ca(Rh,Ru)2; and estimate the thermal-expansion contribution for CoSn and Pd3Pb. Most importantly, they should show at least one null-control compound measured in the same high-T setup: an isostructural or chemically similar metal with a smooth DOS and no FB within ~0.3 eV of E_F (for example a Cu3Au-type compound alongside Pt3Sn and Pd3Pb), where the model predicts nearly linear ρ(T) up to 860 K. Ideally they should also show one case where the curvature sign is predicted before the data are examined. If the method is meant for screening, the false-positive rate matters as much as the true positives. Without these tests, "universal" should be dropped and the claim reworded as "fingerprint of a steep DOS edge near E_F", which may or may not be a FB.
Raised by: r1, r2, r3

2. The paper never demonstrates that ρ(T) can locate a flat band independently of DFT. The abstract and Conclusion say the method lets one "locate FBs via transport", that "the temperature evolution of dρ/dT encodes information about the energy offset", and that it "provides an efficient way to determine the position of FB states" without ARPES or doping studies. In practice, every fit in Fig. 5a holds the DFT DOS fixed, fixes Θ_D and n, and frees only the prefactor C. These fits test whether the DFT-placed FB is consistent with ρ(T); they do not extract E_F − E_edge from the data. DFT FB positions are often off by tens of meV, as the authors themselves note. Eq. 7 in Methods frees E_F − E_edge, m2^{3/2}/D1 and C for exactly this purpose but is never applied to any data set. In the Ni3In1−xSnx series, the conversion from composition to E_F − E_edge also comes from DFT (alloy-averaged DOS, ref. 39). The only quantitative "location" result is CoSn (Fig. 5e): a deviation from linearity at ≈400 K, read as Δ_DFT/3 ≈ 0.1 eV, judged against a linear reference over an arbitrary window and compared only with DFT. The authors should fit Eq. 7, or Eq. 1 with the DFT DOS rigidly shifted by a free offset δ, to the measured ρ(T) of Ni3In, CoSn, Pt3Sn, Pd3Pb and the Ni3In1−xSnx series. They should report the fitted E_F − E_edge with an uncertainty (χ² versus δ), its covariance with C, and its sensitivity to Θ_D and n, and show fits with the DOS shifted by ±25 and ±50 meV to show discriminating power. They should then compare with independent determinations: ARPES for CoSn (refs. 29, 30, FB ≈ 0.1–0.2 eV below E_F) and Ni3In (ref. 23), and the Sommerfeld coefficients in Fig. 5c. If ρ(T) only weakly constrains δ (for example, if C and the FB weight are correlated or ±50 meV fits equally well), the claim should be narrowed to a qualitative sign test: "the curvature sign is consistent with the DFT-predicted FB position".
Raised by: r1, r2, r3

B. Should address

3. The experimental σ(E) reconstruction from Ni3In1−xSnx (Fig. 4c), σ(E) ∝ (ρ − ρ0)⁻¹ at 100 K, rests on unstated assumptions and unquantified errors, and it is the main direct experimental test of the σ(E) step. (a) Θ_D, the phonon spectrum and the conduction-band velocities are taken to be the same across the In/Sn series, but Sn substitution changes band structure and phonons, not just E_F. Also, 100 K is not the high-T BG regime, so the prefactor there depends on Θ_D(x). (b) Matthiessen's rule is assumed in a concentrated substitutional alloy, where it is known to fail substantially; ρ0 is large, disorder-dominated and composition-dependent, and the disorder also broadens the FB. (c) Absolute ρ of anisotropic polycrystalline bars carries geometric-factor, porosity and grain-boundary errors of 10–30% between samples. The step spans a factor of ~5, but no error bars are shown. (d) The σ axis is in arbitrary units, and the paper does not say how the experimental points were normalised onto the model curves; if they were scaled to match, the agreement is partly by construction. (e) The x → E_F − E_edge mapping rests on alloy-averaged DFT, which is the quantity the method claims to determine, so the agreement is partly circular. The authors should give ρ0, RRR and the estimated geometry uncertainty for each x; add error bars on both axes; state the normalisation and the x → E mapping with its uncertainty; give Θ_D(x) (for example from specific heat) or argue it is nearly constant, and show the step survives its variation; and repeat the reconstruction at other temperatures (e.g. 50, 200 and 300 K) to test the temperature independence the model requires. The x = 0.4 and 0.6 samples were measured by a different person (author contributions); please confirm that the setup and contact geometry were the same.
Raised by: r1, r2, r3

4. The "single free parameter" fits in Fig. 5a hide fixed inputs, and the fit results are not reported. For each compound the paper does not state which exponent n (3 or 5) was used (the text says "either 5 or 3", while CoSn shows n = 4.99 at low T), the Θ_D and its source, the fitted C and its uncertainty, the fit range, whether ρ0 was subtracted, how the DFT DOS was broadened and aligned, or residuals and a goodness-of-fit measure. The main text says the fit has a single free parameter, while Methods say Eq. 7 has "three independent fit parameters" once Θ_D is known; n is also a choice and should be listed. Please add a table with these quantities for every compound, show how fit quality changes if the DFT DOS is replaced by a constant, and compare the fitted C with an independent estimate from λ_ep and v_F as a stronger test of the single-parameter claim.
Raised by: r1, r2, r3

5. The T ≈ Δ/3 onset criterion (Fig. 3e) is derived for one sharp parabolic model (m_FB = 10 m0) and then used to infer Δ_DFT ≈ 0.1 eV for CoSn (Fig. 5e). It is not shown to hold for other m_FB, for a finite bandwidth W or a smeared edge (box-car model, Fig. S1), for other n, or for a non-parabolic DOS such as the real DFT DOS in Fig. 5b. The inferred Δ also depends on the window used for the dashed linear reference in Fig. 5e. Please show how the onset ratio T*/Δ depends on m_FB, W and n, and show that the CoSn result is robust to the choice of linear-fit window. Ideally this would become a practical recipe, with uncertainties, that others can apply.
Raised by: r1, r2, r3

6. Sample reproducibility and high-temperature artifacts are not documented, although the high-T curvature is the main observable. The 2–300 K (helium bath cryostat) and 300–860 K (ZEM3) data come from different setups, and the paper does not say how they were joined (scaling, offset, overlap region). Heating to 860 K can anneal, oxidise or change the stoichiometry of samples (Sn or Pb loss). Flux-grown CoSn commonly contains Sn inclusions, which melt at 505 K, inside the measured range and close to the ≈400 K onset of the claimed CoSn anomaly; melting or redistribution of inclusions, or surface reaction above ~500 K, could alter the slope Fig. 5e interprets. Only one sample per compound appears to have been measured. The authors should show the overlap region and state whether any scaling was applied, show heating and cooling curves, repeat a low-T measurement after the high-T run, show that CoSn is free of flux inclusions (e.g. no Sn superconducting transition at 3.7 K), and confirm reproducibility on at least one repeat sample of the new compounds, including a second CoSn crystal after high-T cycling.
Raised by: r1, r2, r3

7. The evidence that the effect is "independent of microscopic details" rests on a single compound. Only Ni3In has a full BTE-RTA calculation (Fig. 4c, Fig. S2); Ni3Ge is from earlier work (ref. 36). It is also unclear how the BTE-RTA σ(E) was computed as a function of E: whether the chemical potential was shifted rigidly in a fixed band structure with fixed phonons, and whether the smooth line is a transport function at fixed T. PBE is known to misplace flat bands in kagome compounds, and the Hubbard U and spin-orbit settings are not discussed. The authors should add a BTE-RTA calculation for CoSn, where ARPES gives an independent FB position, or soften the generality claim. They should also specify the rigid-band procedure, the spin-orbit treatment and the sensitivity of E_edge to the functional.
Raised by: r2, r3

8. Anisotropy and sample form differ across the comparison set, and their effect on the curvature is not discussed. CoSn was measured only along c, while its kagome FB states are largely in-plane with small v_z. Ni3In ab-plane single crystals show strange-metal behaviour at low T (ref. 23), and the text notes that the Ni3In/Ni3Sn contrast is "even stronger in single crystals". The Ni3In1−xSnx samples, Pt3Sn, Pd3Pb and Ni3Ge are polycrystals, averaging over strongly anisotropic transport. The model's interband phase-space argument is isotropic, but real velocity anisotropy can change the curvature. Please discuss whether the curvature sign is expected to depend on current direction and how polycrystalline averaging affects it, and show in-plane ρ(T) for CoSn if possible.
Raised by: r1, r2, r3

9. The model leaves out temperature-dependent shifts of the chemical potential and of the bands. With a large, asymmetric FB DOS near E_F, μ(T) shifts appreciably at fixed carrier number at k_B T ~ 50–75 meV (300–900 K), comparable to the Δ ≈ 20–100 meV offsets considered. Thermal expansion also moves the FB edge. Either effect changes E_F − E_edge in exactly the regime used for the diagnosis, altering both the onset temperature and the curvature. The paper does not state whether the 2PB calculations (Fig. 3) and Eq. 1 keep μ fixed or conserve particle number. Please state the choice and compute μ(T) self-consistently from the DFT DOS, at minimum for Ni3In and CoSn.
Raised by: r1, r3

10. The Sommerfeld coefficient γ ≈ 0.03 mJ mol⁻¹ K⁻² quoted for Pd3Pb (p. 6, Fig. 5c) is implausibly small for a metal with 3 Pd per formula unit, about 20 times smaller than for Cu, and the Pd3Pb bar in Fig. 5c appears visibly larger than that value. It may be a units, per-atom/per-f.u. or fitting error. Because γ is used as the independent confirmation of the FB positions, an error here weakens the consistency argument. Please check the value and its normalisation, and show the C/T vs T² data and fit range clearly in Fig. S4.
Raised by: r1, r2, r3

11. Quasiparticle broadening and electron-electron scattering are acknowledged but not quantified. Ni3In is a strongly correlated, non-Fermi-liquid metal at low T, and the text itself notes that strong electron-phonon scattering smears the conductivity edge. Please estimate ħ/τ at 300–800 K and compare it with the edge sharpness and with Δ, to show whether the semiclassical picture holds where it is applied.
Raised by: r1

C. Minor

12. The statement (p. 4) that the experimental σ(E) "depends inversely on the DOS and does not follow a D⁻²(E) dependence", which distinguishes electron-phonon from electron-electron scattering (τ_ee⁻¹ ∝ D², p. 2), is asserted but not shown. Please overlay a D_DFT⁻² curve in Fig. 4c so readers can judge whether the data discriminate between the two.
Raised by: r1, r2

13. Fig. 3c shows model resistivities of hundreds of µΩ cm (up to ~500 µΩ cm) with dρ/dT < 0, far above the MIR scale, where Boltzmann theory is not valid. The text and caption should state that the "semiconductor-like" m_FB = 100 m0 regime is illustrative and lies outside the model's range of validity.
Raised by: r1, r2

14. Ni3In data provenance in Fig. 5a. Fig. 5a mixes literature data (Ni3In, Ca(Rh,Ru)2, Ni3Ge) with new data, and Ni3In appears in Fig. 4a and Fig. 5a with different magnitudes. Please state which Ni3In data set was used (polycrystal or single crystal, and the current direction). Also explain why Fig. 5a uses the Gim et al. data (to ~300 K) rather than the authors' own Ni3In data measured to 860 K (Fig. 4a), which would be the stronger test of the high-T regime.
Raised by: r1, r3

15. Material label. The compound appears as "Ca(Rh,Ru)2" in the Fig. 5a legend but as "CaRh2" in the text, the caption and Fig. 5c. Please state the actual composition of the ref. 35 sample and make the material and γ value consistent.
Raised by: r1, r3

16. Pt3Sn and Ni3Ge appear in Fig. 5a, but their FB positions, γ values and agreement with the curvature-sign rule are not discussed. Either add them to Fig. 5c and the discussion or explain why they are omitted.
Raised by: r2

17. Fig. 4a and its text. The text says the Ni3In and Ni3Sn slopes "converge" at high temperatures, but in Fig. 4a Ni3In flattens to a slope that appears smaller than that of Ni3Sn. Please quantify both slopes, for example dρ/dT at 700–860 K.
Raised by: r1

18. Sample characterisation in Methods. Report residual resistivities, RRR values and phase-purity checks (XRD, EDX) for Pt3Sn, Pd3Pb and CoSn. Some Cu3Au-type phases have order-disorder transitions, so please state whether L12 order is retained after the 1173 K anneal and during the 860 K measurements.
Raised by: r1

19. Wording of the sign rule (pp. 2–3). The text says the rule reverses for an electron-like FB. Please restate the criterion in one unambiguous sentence (E_F inside vs. outside the high-DOS region), so that "above/below the edge" does not confuse readers.
Raised by: r1

20. Pd3Pb wording. On p. 6, Pd3Pb is described as having its FB "not placed right at but above E_F", which reads as the opposite of the conclusion drawn (E_F > E_edge gives superlinear ρ(T)). Please clarify.
Raised by: r3

21. DOS form in Eqs. 2, 6 and 7. These use (E − E_edge)^{1/2}, which describes an electron-like band above E_edge, whereas the FB is described as hole-like, occupying E < E_edge (Fig. 2). Use (E_edge − E)^{1/2}Θ(E_edge − E) or equivalent, and state the convention.
Raised by: r3

22. Fig. 5e does not state the Δ_DFT value used; it can only be read off Fig. 5b as roughly 0.1 eV. Please state it in the caption or text.
Raised by: r3

23. The Methods statement that σ_FB is "10 and 100 times weaker … from the higher effective mass alone" ignores the different carrier densities of the two bands. Please give the carrier density assumed for the FB.
Raised by: r3

24. The ab initio "Fermi window width of ∂f/∂T = 1×10⁻¹⁰" needs units and an energy-window equivalent.
Raised by: r3

25. Fig. 3c rendering. The BG and m_FB = 100 m0 curves are hard to tell apart near the peak, and the "activation of conductivity edge" annotation should point to the specific E_F − E_edge curve.
Raised by: r3

26. Code availability. The code is available only on request. Given the proposed use as a screening tool, consider releasing a short script implementing Eq. 1 and Eq. 7.
Raised by: r3

27. Typos: "temprature" (p. 5), "intial" (Methods), and the opening quotation mark in "burns" (Methods).
Raised by: r2

Verdict: major revision
