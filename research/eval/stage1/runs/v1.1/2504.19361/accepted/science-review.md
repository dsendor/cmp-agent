A. Must address

1. The headline TRSB and zero-field-diode signal has not been separated from extrinsic sources: a current offset, trapped flux, and remanent-field or magnet history. The only extrinsic source the analysis removes is a uniform remanent field, a rigid shift H → H + H0 found by minimising the asymmetry integral (Supplementary S2, S7, Eqs. 9-10). H0 is not measured independently, and the paper does not report it per dataset.
   - **Current offset.** In Fig. 2c (Ring 2), ΔI_TRSB has a roughly field-independent negative background of about -5 µA at 1000, 800 and 400 mK. Combining Fig. S6 (η = -2.0, -3.0, -3.7 %) with the Ic values of Fig. 2c (about 130, 100 and 70 µA) gives a zero-field |Ic+ - |Ic-|| of about 5 µA at all three temperatures. The absolute asymmetry is therefore nearly temperature-independent while Ic changes by a factor of two. That is the signature of a DC offset in the bias current, or of an asymmetric threshold or thermoelectric effect. An intrinsic diode should scale with Ic and vanish at Tc. Supplementary S2 corrects voltage offsets only.
   - **Trapped flux.** An Abrikosov vortex or other flux pinned in the wide Sr2RuO4 banks, leads or arms near one junction imposes a fixed phase offset on that junction, which acts like a φ0 shift. This breaks Ic+(H) = |Ic-(-H)| and produces a zero-field diode in an ordinary asymmetric SQUID with finite βL. The c-axis Hc1 is only a few mT, and demagnetisation in thin flakes lowers it further. The resulting corrections are not uniform in H, and neither are flux focusing that changes with field or magnet-hysteresis offsets, so a single H0 cannot remove them.
   - **Apparatus drift.** The authors' own control SQUID drifts by a ΔI of about 1 µA at larger fields (Fig. S10), which they attribute to temperature drift. That is comparable to the 2-4 µA asymmetries in Ring 3 (Fig. S5b) and not far below the 2-8 µA effects in the rings generally.
   - **The decisive test is missing.** In the authors' own chiral-domain picture, the sign of η and ΔI_TRSB is set by the domain configuration chosen at Tc. It should therefore be random or pinned across zero-field thermal cycles, and trainable by field cooling in ±Hz, by analogy with the Kerr training cited in S3. Trapped flux in the magnet or the banks would instead give a sign tied to magnet history, with a size that scales with the cooling field.

   The authors should:
   - report η and ΔI_TRSB at H = 0 over several zero-field cooldowns through Tc in a compensated field (Hall-probe or SQUID-calibrated), after field cooling in +Hz and -Hz, and after degaussing or quenching the magnet;
   - repeat the measurement with the bias-current leads swapped, or show the current-source offset directly;
   - report H0 for each dataset with its uncertainty;
   - tabulate the sign and size of η across cooldowns and devices.

   If the sign is fixed by geometry across thermal cycles, the authors need to explain how that is compatible with spontaneous symmetry breaking. As it stands, the claim in the abstract and conclusion rests on a few-µA asymmetry whose temperature scaling points to an extrinsic origin.
Raised by: r1, r2, r3

2. The point-symmetry test is not shown to be protocol-symmetric, even though the authors themselves describe the system as history-dependent. Time reversal maps a field sweep from -H to +H onto a sweep from +H to -H. It also reverses the order in which the two current polarities are applied. The paper never states how Ic+(H) and Ic-(H) in Fig. 2b,c and Fig. S5 were acquired: the field-sweep direction, whether both polarities come from the same IV sweep, and the order within each IV.
   - **Why it matters.** The central claims are that domain walls move with field (Discussion; Supplementary S3) and that Ic is bistable and set by bias history (Fig. 3). Comparing Ic+ at +H with Ic- at -H from a single sweep direction therefore compares states with different histories. A fully time-reversal-symmetric but hysteretic system would violate Ic+(H) = |Ic-(-H)| under such a protocol.
   - **The jumps in Fig. 2c.** ΔI_TRSB for Ring 2 shows abrupt, step-like jumps of about 10 µA at specific fields (for example near ±2-3 mT at 1000 mK), followed by sawtooth-like recovery. This looks like discrete flux entry or exit or history-dependent switching, not a smooth intrinsic asymmetry.

   The authors should state the protocol explicitly and show up- and down-sweeps separately for each dataset. They should then make the time-reversal-correct comparison: Ic+(H) on the up-sweep against |Ic-(-H)| on the down-sweep, with the current-polarity order also reversed. Finally, they should show that ΔI_TRSB survives this comparison beyond the scatter of repeated identical sweeps.
Raised by: r1, r2, r3

3. The in-plane-field results, the bistable Ic states (Fig. 3; Figs. S14, S17) and the half-integer Shapiro steps (Fig. 4; Figs. S15, S16), have conventional explanations that the paper does not exclude. Yet the Discussion and Conclusion state that these features "cannot originate from an s-wave superconductor."
   - **Out-of-plane misalignment.** The in-plane fields are 10-20 mT, and up to 70 mT in Fig. S17, while the out-of-plane SQUID period is about 3-4.5 mT (Fig. 2a). A misalignment of 1° at 20 mT gives about 0.35 mT out of plane, a sizable fraction of a lobe. The paper states no alignment procedure and no estimate of the misalignment.
   - **Flux through the junction cross-section.** The arms are 0.25-0.7 µm thick (Table S1), so the in-plane field threads flux through each junction's cross-section. For example, 20 mT × 0.45 µm × (2λ + d) ≈ 0.4 µm gives about 1.7 Φ0. The authors' own Fig. S16 shows a Fraunhofer-like in-plane pattern with minima near 4.5 and 9.9 mT, and the text concedes that the fractional steps near those minima are trivial. Multivalued Ic states from trapped Josephson vortices in extended junctions are a standard conventional effect: the bias current switches them, and field reversal swaps their roles.
   - **In-plane Abrikosov vortices.** The in-plane Hc1 of Sr2RuO4 is small, so vortices can enter the banks and arms at these fields. Vortices pinned near a junction and pushed by the Lorentz force of the bias current naturally give two Ic states, switched by current polarity, with roles exchanged on field reversal, exactly as in Fig. 3 and Fig. S14. The argument on p. 11, that the Josephson penetration depth exceeds the arm width, addresses Josephson vortices along the width. It addresses neither Abrikosov vortices in the electrodes nor the flux set by the thickness.
   - **Fluxoid states.** In a SQUID with βL ≳ 1 (including kinetic inductance, with λ ≈ 190 nm in sub-µm arms), Ic(Φ) is multivalued. Each fluxoid state has its own Ic, and driving the bias past Ic in one polarity switches the fluxoid state, which gives polarity-alternating switching. Reversing the field exchanges the roles of the two current polarities (Fig. S14b), as time-reversal symmetry requires. This is not evidence against time-reversal symmetry.
   - **Half-integer steps.** An asymmetric dc SQUID with finite inductance at non-integer flux bias has an effective non-sinusoidal current-phase relation and shows half-integer steps. At 144-145 MHz, Ω = f/(2eIcRn/h) ≈ 0.2. In this low-frequency regime, subharmonic structure is sensitive to capacitance, noise and inductance. The steps also change after the field is merely reset (Fig. S15, which also has missing integer steps), which suggests an uncontrolled flux state.

   The authors should:
   - state and quantify the field alignment, for example by nulling the SQUID oscillation shift with a small Hz trim at each in-plane field, and repeat key bistability and half-integer-step measurements with the out-of-plane component compensated;
   - estimate, for each ring, the in-plane flux per junction, λJ and βL (geometric plus kinetic, from Ic and the dimensions or from the modulation depth);
   - show that the bistability (including the Fig. S17 map) and the fractional steps do not follow the in-plane Fraunhofer minima of Fig. S16;
   - show whether bistability and half-integer steps persist in a singly connected device, such as the cut Ring 2, where fluxoid states do not exist. The text says bistability appears "irrespective of device geometry," but no singly connected data are shown;
   - test the vortex scenario: the dependence of the switching threshold on in-plane field magnitude, and whether bistability survives warming to just below Tc and re-cooling at fixed Hx;
   - model the Shapiro response with RCSJ including βL and asymmetry, and give the dependence of the half-integer steps on power and frequency (a map like Fig. 1d for the low-Ic state);
   - show that the noisy Fig. S17b angle map, with features near φ ≈ 0°, 180° and 360°, is repeatable.

   Failing this, the claim should be restricted to "consistent with," and "cannot originate from s-wave superconductivity" should be removed for these features.
Raised by: r1, r2, r3

B. Should address

4. The error bars cover only voltage noise, and the Ic criterion is not fixed per dataset. The bootstrap uncertainty on Ic "only accounts for the uncertainty in measured voltage" (Supplementary S2). The error bars leave out the uncertainty in the fitted H0, thermal drift (about 1 µA in Fig. S10), sweep-to-sweep reproducibility and the choice of voltage criterion. Ic is defined with a 0.1 or 0.2 I0RN threshold "depending on the degree of rounding," but the paper does not say which threshold applies to which figure. The IVs in Figs. 3, S7 and S14 are strongly rounded and differ in shape between polarities and states. A fixed voltage threshold can therefore produce an apparent polarity asymmetry by itself. The authors should:
   - state the criterion used for each dataset, including in the Fig. 2 caption;
   - show that ΔI_TRSB and η are robust to the criterion, for example at 0.05, 0.1 and 0.2 I0RN;
   - include the H0 uncertainty and the sweep-to-sweep scatter in the error bars of Fig. 2;
   - quote η and ΔI_TRSB with their significance relative to the total statistical plus systematic uncertainty.
Raised by: r1, r2, r3

5. There is no null device matched in geometry and measurement conditions. The only no-TRSB control (Figs. S8-S10, S12b) is a MoGe/Ag SNS SQUID. It differs from the rings in material, Hc1, pinning, junction type, resistance and geometry. Its TRSB comparison window covers only about ±2 mT, against ±10 mT in Fig. 2a. The control shows that the analysis pipeline returns ΔI_TRSB = 0 for a conventional device. It does not test whether FIB-made constriction rings with wide banks generate extrinsic asymmetries. 3K-phase Sr2RuO4 rings show no SQUID oscillations (Refs. 23, 47), so they cannot serve as the null either. The better reference is a ring of the same geometry and lead and bank layout, milled from a conventional superconductor (for example a Nb or MoGe film) or made as a Dayem-bridge SQUID of matching dimensions. It should be measured in the same cryostat and wiring over the same field range, and run through the same ΔI_TRSB and η analysis, including the current-offset check of item 1.
Raised by: r1, r2

6. The narrow central lobe (about 0.73 Φ0, Fig. 2a) is called irreconcilable with established mechanisms (p. 8), but several non-domain explanations are not discussed.
   - **Field-dependent effective area.** Meissner screening and flux focusing by the large banks at low field, vortex entry into the banks or leads above a threshold of a few mT, and field-dependent kinetic inductance could each make the first lobe differ from the rest. Vortex entry is especially relevant given the discrete jumps in ΔI_TRSB in Fig. 2b,c.
   - **Junction effects.** The narrow lobe could also come from the field-dependent Gaussian envelope of the individual junctions combined with junction asymmetry and inductance.
   - **The area convention.** The lobe widths depend on the normalisation π r_in r_out. That choice should be justified, since the ring width is comparable to λ and the banks are large. As it stands, the comparison is really with the outer lobes.
   - **A narrow lobe without TRSB.** In Fig. S5a, Ring 3 at 1200 mK is called "normal SQUID behavior," yet its central lobe is already 0.82 Φ0, against 0.92-0.93 Φ0 for its neighbours. A narrowed central lobe therefore does not by itself indicate TRSB.

   The authors should model these alternatives and compare devices with different bank sizes, using Ring 4's straight-arm geometry to check whether the anomaly scales with the banks or the ring. They should also show the field-sweep-direction data that the text says were checked, give the temperature dependence of the lobe width, and test whether it changes after field excursions large enough to trap vortices in the banks.
Raised by: r1, r2, r3

7. The domain-wall toy model (Supplementary S3) is under-constrained, unchecked against existing limits, and does not produce the TRSB it is meant to explain.
   - **Free parameters.** φm, a and Φint^max are fitted separately for each dataset (Fig. S11). The RCSJ asymmetry, screening and envelope parameters add to these, the sigmoid of Eq. 4 is ad hoc, and the fits visibly miss the peak heights.
   - **Scanning-SQUID limits.** The fitted Φint^max = 0.24 Φ0 (Ring 1) and 0.16 Φ0 (Ring 2) imply a spontaneous flux from a single chiral domain far larger than the edge-current magnetisation bounded by scanning SQUID (Refs. 28-30).
   - **No zero-field diode.** In the model the domain fluxes cancel at zero field ("At zero external field, where the domain wall is centered, the contributions of the domains cancel out," p. 13). The model therefore does not produce the zero-field diode or ΔI_TRSB. The Discussion instead attributes these to the Sigrist-Agterberg φ0-like energy (S5).
   - **Coupling term.** Eq. 3 couples Ψ± linearly to B without specifying the gauge-invariant form or the physical quantity, such as angular momentum or magnetisation, that carries the coupling.

   The authors should list which parameters are free and which fixed, and report how many free parameters there are relative to independent data features. They should fit Ic+ and Ic- jointly, so that the model must reproduce ΔI_TRSB(H) and η. They should compare with a minimal non-domain alternative: an RCSJ fit with a φ0 shift (or trapped flux) in one junction plus a uniform H0. Finally, they should estimate the flux expected from chiral edge currents in a ring of these dimensions and confront the fitted Φint^max with the scanning-SQUID bounds, stating any contradiction. Without this, "consistent with domain walls" rests on qualitative agreement.
Raised by: r1, r2, r3

8. The temperature and device dependence of the TRSB signal is sparse, partly counterintuitive and not discussed.
   - **Ring 2.** η is given at only three temperatures, and its magnitude grows toward Tc, from about 2 % at 400 mK to 3.7 % at 1000 mK (Fig. S6). An order-parameter-driven φ0 junction would be expected to vanish at Tc.
   - **Ring 3.** It shows significant TRSB at 1100 mK but none at 1200 mK (Fig. S5), about 0.3 K below its Tc of 1.5 K (Table S1), and no lower-temperature data are given. Zero-field µSR and Kerr data place the TRSB onset at Tc in unstrained material.
   - **Ring 1.** It is analysed only at 50 mK.

   The authors should show η(T) and ΔI_TRSB(T) in finer steps from base temperature up to Tc for at least two devices, ideally all rings. They should discuss whether the onset below Tc and the growth of η with T fit the domain-wall picture, or point instead to a thermally activated or extrinsic origin. The answer bears on the pairing discussion on pp. 14-15.
Raised by: r1, r2, r3

9. The sample statistics and the "universal" claims are not quantified. The text says the features are "universally observed in a large selection of samples" (p. 5), and S6 says bistability appears "in all samples, irrespective of device geometry" and is "a universal property." Yet the main text shows three rings, bistability mainly for Rings 1 and 3, and the Supplement refers to four devices. The authors should add a table of all devices measured, giving for each one: Shapiro steps, ΔI_TRSB above error, the narrow central lobe, the sign and magnitude of η (per cooldown), bistability and half-integer steps. The table should say whether any device with Tc ≈ 1.5 K lacked these features, and how the properties changed after FIB re-milling (Ring 2 was re-milled four times, Fig. S1) and after thermal cycling. This distinguishes an intrinsic property from a device-specific one, provides a natural null population, and bears on the claim that the junctions are deterministic domain walls fixed by confinement (Fig. 1a).
Raised by: r1, r2, r3

10. The case that the junctions are domain walls, and not constriction weak links or phase-slip centres, needs tightening. Page 7 says Shapiro steps "can only originate from the Josephson effect," which rules out kinematic vortices and phase-slip centres. But phase-slip lines and kinematic vortex flow in narrow bridges also phase-lock to RF and produce steps at Φ0 f. Shapiro steps prove Josephson-like coupling, but they do not establish where it comes from. The arms are 250-380 nm wide (Table S1), only a few ξ0 = 66 nm, and the necks are narrower still. Together with FIB-damaged edges (about 10 nm), they are natural weak links that are themselves time-reversal symmetric. The argument rests mainly on Ref. 23 and on the absence of the effect in 3K-phase rings. The Gaussian Ic(H) of the singly connected device (Fig. S3) is acknowledged to be characteristic of long diffusive junctions, which the authors do not expect. The authors should moderate the wording or compare the step-power dependence with RCSJ Bessel-function behaviour (the Fig. 1d histogram is otherwise strong). They should also give a brief quantitative comparison of the expected Dayem-bridge or phase-slip response with the observed Rn, step widths against power, Ic(T) (Fig. S1) and IcRN (for example 80 µA × 19 mΩ ≈ 1.5 µV for Ring 1).
Raised by: r1, r2, r3

11. The materials-quality and strain statements go beyond the evidence. The Methods conclude from Tc ≤ 1.5 K that there are no edge dislocations or strain (p. 16), and state that "neither the exfoliation nor the focused ion beam structuring reduces the quality of the crystal." Tc ≤ 1.5 K shows only the absence of the 3K-phase. Tc itself ranges from 1.3 to 1.5 K across devices (Table S1), and the cited TEM damage depth of about 10 nm comes from a different study (Ref. 48). Tc does not exclude differential thermal-contraction strain from the SrTiO3 substrate, inhomogeneous strain near the FIB-cut edges, or strain at the constrictions. These are exactly what the accidental-degeneracy scenarios (Refs. 64-65) require, and the "strain-free" argument is used against them. The authors should either support the point directly, for example with TEM or strain characterisation of these devices, or soften it. Given that the chiral d_xz + id_yz state conflicts with heat-capacity data (Refs. 59-60), the conclusion should be phrased as "consistent with a multi-component order parameter" rather than as discriminating between candidate states.
Raised by: r1, r3

C. Minor

12. Supplementary Eq. 10 minimises [Ic+(H+H0) - Ic-(H+H0)]², a same-field, diode-type comparison without the sign flip or absolute value. Eq. 9 and the stated test use |Ic-(-H)|. Please state which expression was actually used, since Eq. 10 as written would partly remove genuine TRSB, and state the integration window of the minimisation. Eqs. 9-10 also have unbalanced bars and brackets and omit dH.
Raised by: r1, r2, r3

13. The Fig. 2 caption defines the area as π r_in r_out but calls r_in and r_out "diameters." They should be radii. The main text gives a typical outer diameter of 1.2 µm, while Table S1 lists 1.01 µm for Ring 1. Please state the dimensions and area used to normalise the Φ0 lobe widths for each ring.
Raised by: r1, r2, r3

14. Several cross-references are wrong or inconsistent.
   - The main text (p. 13) cites "Supporting Figure S5" for a doubly connected structure without constricting necks, whose pattern "becomes noticeably more irregular and noisy." Fig. S5 shows Ring 3 TRSB data. If the device is Ring 4 (Fig. S4), the Supplement says it shows "similar SQUID-like oscillations ... as on the other ring samples." The reference and the two descriptions need to be reconciled.
   - Page 7 cites "Supplementary Figure S3" for the singly connected Shapiro steps, which are in Fig. S2.
   - The Methods cite "Supporting Figure S2" for the re-milled Tc values, which are in Fig. S1.
Raised by: r1, r3

15. The Fig. S14 caption writes "I+ and I+" for "I+ and I-," refers to "Figure 4 of the main text" where Figure 3 is meant, and gives the field as "-20 mT" while panel (a) is at +20 mT.
Raised by: r1, r2, r3

16. The Fig. S10 caption reads "showing the absence of no TRSB," a double negative. It also says "first three peaks" where the text says "central four periods."
Raised by: r1, r2, r3

17. The Fig. S11 caption describes a panel (d) (Ring 2 at 400 mK) that is not shown.
Raised by: r1, r2, r3

18. The main text says the data come from three rings, while Supplementary S1 says four devices. The asterisks in Table S1 ("80**", "0.475*", "1.38*") are undefined.
Raised by: r1

19. In Supplementary S4 the Gaussian envelope is written exp(-H²/2²); presumably 2σ² is meant.
Raised by: r1

20. The figures do not consistently give the measurement conditions. The Fig. 1c,d captions give the source power (0-20 dBm) but not the power at the sample, or at least the attenuation, for each frequency. The Fig. 1d axis label (V/fΦ0) should match the Fig. 1c inset. Other examples: the temperature of Fig. 2b, the frequency for Fig. 4 (S15 says 145 MHz, Fig. 1 uses 144 MHz) and the ring used for Fig. S5. Every caption should give the ring, temperature, frequency and RF power.
Raised by: r1, r2, r3

21. The angle conventions are inconsistent. In Fig. S16, φ is measured from the y-axis (30°). In Fig. S17, φ = 0 lies along x, "the direction along the ring." The S17 caption says no hysteresis occurs below 10 mT, but the map starts at 10 mT. Please unify the conventions and extend or annotate the map.
Raised by: r2

22. The claim of a "complete breakdown of the RCSJ model" (p. 5) is too broad. What is shown is that a two-junction sinusoidal-CPR RCSJ model with a uniform field cannot reproduce the data. Please phrase it accordingly.
Raised by: r2

23. Currents of about 100 µA flow through Ti/Au contacts at 50 mK base temperature. Please give the contact resistances, confirm the four-probe geometry, and state whether the effective temperature at the 50 mK points is known, since Ic still varies strongly between 400 mK and 50 mK in some panels.
Raised by: r3

24. Reference 62 contains the LaTeX artifact "textitSuperconducting."
Raised by: r1, r2

Verdict: major revision
