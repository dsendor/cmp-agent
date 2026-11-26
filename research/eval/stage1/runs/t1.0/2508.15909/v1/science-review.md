# Merged review

## A. Must address

1. **The superconductivity claim, which appears in the title and abstract, is not established by the data shown.** In SC1 the resistance never approaches zero. In Fig. 1f (inset) R_xx falls from about 200 Ω to about 80–100 Ω below the ~170 mK onset. In SC2 (Fig. S12b) it falls from about 175 Ω to about 140 Ω, roughly 20%, with T_c ≈ 80 mK. The authors attribute the residual resistance to "insufficient filtering" (p. 6) but do not test this. The same set-up reaches a 9 mK base temperature and resolves fine quantum oscillations, and no electron-temperature calibration is given. A partial drop together with a nonlinear dV/dI peak that a few mT of B⊥ suppresses (Figs. 1f, 3e, 3f, S12c,d) is not specific to superconductivity. It can also come from:
   - a filamentary or percolating superconducting path through an inhomogeneous channel. The leaf region is very narrow in n–E, so density or displacement-field inhomogeneity across the Hall bar would sample adjacent phases or a first-order phase coexistence;
   - Joule or electron heating in any state whose resistance depends strongly on temperature, for example at an isospin or first-order transition;
   - a current-driven transition or crossover between competing correlated states.

   The authors should:
   - remeasure with improved filtering or lower excitation until the resistance saturates, and report the electron temperature (for example from Shubnikov–de Haas amplitude against mixing-chamber temperature), the filtering stages and the excitation current;
   - show R_xx(T) and dV/dI from several voltage-probe pairs (contacts 1–6 in Fig. S13f), and in at least one other device. They should give the residual resistance as a fraction of the normal-state value for each pair and estimate what fraction of the Hall bar is in the leaf phase at a given gate setting;
   - show how the residual resistance depends on n and E, for example whether the minimum resistance is lowest at the centre of the leaf and rises toward its edges;
   - show I–V curves with a well-defined critical current and its T and B⊥ dependence, rather than only dV/dI colour maps, and R_xx(T) at several B⊥ and B∥ showing a systematic suppression of T_c;
   - look for a phase-coherence signature, such as Fraunhofer-like or Josephson-like modulation of the critical current in small B⊥, or Little–Parks-type or flux-periodic magnetoresistance.

   Without these, the title, abstract and text should consistently say "superconducting-like resistance drop", as the main text already does in places.

   Raised by: r1, r2, r3

2. **The claimed Pauli-limit violation is not supported and appears inconsistent with the out-of-plane critical field.** The text says the low-resistance state "persists up to an in-plane magnetic field of approximately 6 T — more than an order of magnitude higher than the estimated Pauli limit of ~300 mT" (p. 6, Fig. 3g, Fig. S9). Yet the dV/dI features of SC1 are suppressed by a few mT of B⊥ (Fig. 3e, ±10 mT axis), and Fig. S12d gives B⊥,c ≈ 1 mT for SC2. At 6 T, a misalignment of only 0.05° gives about 5 mT out of plane. So either the sample was aligned to better than ~0.05°, which the paper does not report, or the state seen at several tesla is not the state that a few mT of B⊥ destroys. There are further problems:
   - Fig. 3g follows a resistance minimum (the "left blue strip") along a single n–E line cut, not a superconducting transition. The S9 maps in which SC1 "persists" at 2 and 5 T show only R_xx at an unspecified temperature. Fig. S9 also shows the in-plane field strongly reshaping the phase diagram, suppressing the triangle and moving boundaries, so it is not clear that the same phase is being tracked.
   - The numbers are internally inconsistent: the text quotes about 6 T, while Fig. S9 says SC1 "shrinks" at 5 T and closes only at 10 T.
   - The paper does not say which T_c criterion (onset or midpoint) gives the ~300 mT Pauli estimate.
   - In a ~2 nm thick hexalayer with layer-polarized carriers, an in-plane field also couples orbitally.
   - If the normal state is spin polarized, the Pauli limit does not apply. The fermiology finds two-fold degenerate pockets in this region, and a large B∥ tolerance would then be expected, as in spin-polarized rhombohedral trilayer superconductivity (ref. 11). A violation is expected for any spin- or valley-polarized pairing, so on its own it does not single out an unconventional state.

   The authors should:
   - describe the rotator or alignment procedure and give the residual misalignment, for example from the Hall voltage measured in "in-plane" field;
   - show R(T) and dV/dI against I at several fixed B∥ (for example 0, 2, 4, 6 T), including the B⊥ dependence at finite B∥, and extract T_c(B∥) with a stated criterion (for example 50% of the normal-state resistance);
   - map the SC1 boundary in n–E at each B∥, so that the same region is followed;
   - if a violation survives, discuss specific mechanisms, such as spin-polarized or spin-triplet pairing.

   Raised by: r1, r2, r3

3. **The ΔP·M interpretation of the reversal of hysteresis polarity (Fig. 4e) is not established against simpler explanations.** The key observation is that the sign of the R_xy loop in B⊥ flips between E = −35.5 and −36.2 mV/nm at fixed n. The authors take this to mean that "M·B alone does not capture the system's energetics" (p. 7). The argument assumes that the sign of the Hall hysteresis tracks the sign of M. But the anomalous Hall signal is set by the Berry curvature of the occupied states, not by the orbital magnetization. Several alternatives give the same sign flip without an electric polarization:
   - **A change of Hall sign rather than of magnetization.** At fixed valley polarization, the sign of σ_xy, and even of the orbital magnetization, can change as the Fermi level or the band filling within a flavor moves through a Berry-curvature hot spot, or across a layer-polarization change or band inversion. This is well known from moiré orbital Chern magnets and underlies the electrically switchable magnetism of twisted mono-bilayer graphene. The comet region lies next to the band-inversion and Lifshitz features of Fig. 2, which is the very mechanism the paper describes. In that case the polarity of the R_xy loop reverses with no change in the sign of M and no ΔP·M coupling.
   - **Branch mixing.** The reversal occurs "when the magnetic hysteresis is the largest", inside the narrow E window where the E-hysteresis itself is open (Fig. 4a–d). A B-sweep there may switch the system between the two E-branches rather than reversing M within one state.

   The authors should:
   - measure B-loops at fixed E prepared from both E-branches (approached from above and from below);
   - track the sign of the anomalous Hall step continuously across E and n, to see whether it follows a Berry-curvature sign change;
   - compute the sign of σ_xy and of M for the candidate flavor configurations within their model, or give a theoretical argument that the Chern number or Berry-curvature sign is the same on both sides; a magnetization-sensitive probe (nanoSQUID or MOKE) would settle whether M itself reverses;
   - write down the Landau free energy containing ΔP·M and show that it reproduces the observed sign change and the linear-in-B⊥ shrinkage of the E-loop (Fig. 4c,d). The slope dE_c/dB⊥ ~ ΔM/ΔP gives a quantitative constraint to compare with estimates of ΔM and of ΔP from the band structure.

   Raised by: r1, r2, r3

4. **The "ferroelectric" character, a spontaneous and switchable electric polarization, is inferred only from the Hall signal; P is never measured.** The E-hysteresis in Fig. 1i and Fig. 4a,b is seen through R_xy under a stabilizing 50 mT field. No capacitance, layer-polarization or penetration-field measurement is presented, and the "3:1 polarized state" is speculative. The loop is "unipolar": both switching fields lie on the same side, near −34 and −37 mV/nm. Ferroelectric switching implies two states of opposite polarization at the same applied field, switchable in both directions, with remanence. A narrow window between two nearby negative fields is instead the generic signature of an ordinary first-order transition between two phases with different layer polarization and magnetization (for example a layer-polarized and a partially polarized metal) with metastability on both sides. It is equally consistent with magnetoelectric switching of M driven by E-tunable Berry curvature, without spontaneous P. The linear shrinkage of the loop with B⊥ (Fig. 4c,d) fits a Zeeman-type M·B term shifting a first-order boundary and does not show that a polarization is switched.

   The authors should:
   - provide an independent measure of layer polarization or electric dipole that is not tied to M: penetration-field or layer-resolved capacitance, hysteresis of R_xx at B = 0, or shifts of Landau-level and band-edge positions between forward and backward sweeps;
   - at least show a top-gate/bottom-gate asymmetric sweep demonstrating remanent P at the same E;
   - show whether a counterpart state exists at E ≈ +35 mV/nm. The ±E asymmetry itself indicates whether this is a polarization-switching phase.

   Without these, "ferroelectric" should be replaced by a description of what is observed, for example "an electrically switchable orbital magnet with E-reversible Hall hysteresis".

   Raised by: r1, r2, r3

5. **Extrinsic origins of the E-hysteresis and the Hall hysteresis are not excluded (Figs. 1h, 1i, 4a–d, S2, S10, S11).**
   - **Gate hysteresis.** Hysteresis in a dual-gate sweep can come from charge trapping or interfacial polarization in the hBN, at the SiO₂/Si interface or in the SiO₂. It can also come from slow relaxation of the global Si gate, which is held at −90 to −100 V for hole-side contact doping and at +95 V for the electron side (Methods). Such effects could easily offset E by the ~3 mV/nm separating the switching fields.
   - **Longitudinal admixture.** R_xx is itself strongly hysteretic and of kΩ scale in the same regions (Fig. S2a,c,e), while the Hall steps are only a few hundred Ω (about 300–400 Ω). R_xy appears to be raw, at a single B = 50 mT, so R_xx admixture could generate or distort the loops.

   The "unipolar" character, the sign reversal in Fig. 4e and the step amplitudes all depend on excluding these. The authors should:
   - show that sharp, independent features (Landau-level crossings, the CI boundary) do not shift between forward and backward E sweeps over the same range;
   - show that the switching fields do not depend on sweep rate, sweep range or the n–E path, and that n-sweeps at fixed E agree with the E-sweeps;
   - show that the same E-sweep in a nearby non-magnetic region (for example the right end of the "comet", Fig. S10) gives no hysteresis at the same sweep rate. Fig. 4a,b partly does this and should be extended explicitly;
   - show that the comet-region behaviour is unchanged when the Si gate voltage is varied within the range that keeps the contacts transparent;
   - antisymmetrize all loops, comparing R_xy(+B, sweep up) with R_xy(−B, sweep down) and the corresponding E-sweep pairs, show R_xx loops alongside R_xy at the same E, and show B = 0 or both-polarity Hall data for Fig. 4a–d.

   Raised by: r1, r2, r3

## B. Should address

6. **Reproducibility across devices is asserted, not shown.** The Methods say "three devices were fabricated and measured with similar results", but every figure appears to come from one device and one contact configuration (Fig. S13f). Both SC phases and the comet occupy tiny regions of n–E next to sharp phase boundaries. Features like these are the most sensitive to stacking domains, strain and disorder, so their presence in one device only would considerably weaken the claims. The authors should show, for at least a second device, the n–E map, SC1 (R(T), dV/dI and the in-plane-field dependence), the Fig. 4e polarity reversal and the leaf-shaped fermiology, or state clearly which features were reproduced. If the other devices do not show SC1, SC2 or the comet state, they should say so and discuss why. They should also report whether the E-hysteresis and the polarity reversal survive thermal cycling.

   Raised by: r1, r2, r3

7. **The "electric-field-driven band inversion" in the abstract rests on a qualitative picture that is not checked against a calculation (Figs. 1a–d, 2a, 2f, 2g–j).** The inference rests on the opposite tilts of the dotted and dashed lines in the n–E plane and on hand-drawn band diagrams (Fig. 2g–j) based on a hypothesized 2×2 emergent-gap flavor splitting (pp. 3–4). The tight-binding model in Fig. 1a–d is single-particle and contains no correlated gap; the gaps that define flavors A and B are put in by hand. The tight-binding parameters for hexalayer (γ0–γ4, δ, Δ) are not listed, and the band overlap at U = 0 is very sensitive to γ2 and γ3. The mapping between U (±2 meV/layer in Fig. 1a) and the experimental E (±100 mV/nm), including screening, is not given, so the inversion field (≈42 mV/nm at n = −1.26×10¹² cm⁻²) and the Lifshitz lines cannot be compared with any model. The paper itself lists observations that conflict with the picture: two-fold rather than four-fold annular surfaces at E = 0 (Fig. 2e), valley-polarized magnetism contradicting the assumed layer antiferromagnet (p. 5), and leaf Fermi surfaces in Fig. 3b "incompatible with an n-independent band structure". The authors should give the parameter set and the U–E conversion. They should then carry out at least a self-consistent Hartree or Hartree–Fock (or a phenomenological flavor-split) calculation with flavor-dependent layer polarization for the proposed 2×2 (and 3:1) orders, and overlay its Lifshitz lines on Fig. 2a. The predicted slopes, crossing point, f_v values and the ~100 mV/nm band-insulator threshold should be compared with Figs. 2a–f. They should also explain how layer polarization is assigned from line tilts and how robust the assignment is. Otherwise "reveal" should become "is consistent with", and "band inversion", which has topological connotations given refs. 25–27, should be described more cautiously, for example as a crossing of layer-polarized band edges within one flavor.

   Raised by: r1, r2, r3

8. **The low-frequency "emergent Fermi surfaces" FS1 and FS2, which carry the leaf-region argument, may be analysis artefacts.** FS1 and FS2 in Fig. 3b,c are said to emerge and vanish at zero frequency, and the "half-dome" manifolds in Fig. 3d sit at f_v < 0.1. At n ≈ 2×10¹² cm⁻², f_v = 0.05 corresponds to about 4 T, which completes only a few periods over the 0.4–1.6 T (or 0.5–2 T) window. This is the part of an FFT most prone to artefacts from background subtraction and windowing. The analysis details are missing: field window, background subtraction, windowing or apodization function, whether the data were interpolated onto a uniform 1/B grid, and the resulting f_v resolution. Low-frequency branches can also arise as combination frequencies (f_i − f_j) from magnetic breakdown or chemical-potential oscillations. The authors should state the procedure and resolution, show that the low-f_v peaks are stable under changes of window and background, and check whether FS1 and FS2 coincide with differences of the major branches.

   Raised by: r1, r2, r3

9. **The carrier type and degeneracy of the pockets are assigned through the f_v sum rule, and violations are explained after the fact, so the logic is partly circular (Fig. S5).** The sign s_i and degeneracy k_i of each pocket are chosen so that Σ s_i k_i f_i = 1, but the rule is violated over wide ranges (Fig. S5f,i), and different choices can satisfy it equally well. The claim that FS1 and FS2 are two-fold degenerate ("the higher f_v peak exceeds the sum of FS1 and FS2 by 0.5") depends on the sum rule holding inside the leaf. Elsewhere violations are attributed to unresolved heavy pockets. The same pockets could be present in the leaf, which would change the degeneracy assignment and with it the "dual-carrier" link to SC1. The electron-like character of the pockets that underpins the "band overlap" and "band inversion" claims (for example "a new electron pocket emerges in Fig. 2c") also needs independent support. The authors should plot the sum (grey points, as in Fig. S5i) explicitly across the leaf, state the uncertainty on each f_v, and discuss which alternative assignments remain allowed. They should check carrier sign and total count independently, from the sign of the Landau-level slope dn/dB in fan diagrams, the Hall sign of minority carriers, the Hall density, or a comparison of electron-like and hole-like branch masses.

   Raised by: r1, r2, r3

10. **The "emergent nature" of FS1 and FS2 is inferred from their fading with temperature, without a Lifshitz–Kosevich analysis (Fig. S6 and the text after Fig. 3b).** Oscillation amplitudes fall with temperature for all pockets, fastest for heavy ones, so disappearance between 150 mK and 1 K may simply reflect a large cyclotron mass. The authors should extract effective masses from LK fits for FS1, FS2 and the main branches. They should show whether the suppression of FS1/FS2 is anomalous, for example because the frequency itself shifts or vanishes rather than the amplitude merely decreasing.

   Raised by: r1, r2, r3

11. **The link between SC1 and the two emergent Fermi surfaces (the "dual carrier origin") rests on visual coincidence of regions (Figs. 3a, 3d).** The authors should overlay the zero-field SC region, defined by a criterion such as R_xx below 50% of the normal-state value at base temperature, directly on the FS1/FS2 manifolds of Fig. 3d. They should also state whether SC appears anywhere outside the overlap region, for example SC2 in Fig. S12a.

    Raised by: r2

12. **The magnetic field used for fermiology may itself alter the phases being mapped.** The fermiology uses B⊥ up to 1.6–2 T, but the phases it explains are defined at B = 0 (Fig. 1e). Several of them (the ferrovalley triangle, SC1, the comet) respond strongly to tens of mT. In rhombohedral graphene, isospin phase boundaries shift appreciably with B⊥, and orbital magnetic states are favoured by B⊥. Fig. 2a at 1.5 T differs visibly from Fig. 1e at 0 T. Identifying zero-field resistive boundaries with Lifshitz transitions seen at 0.4–1.6 T assumes that the band structure does not change in this range, which is questionable for flavor-polarized states with large orbital moments. The authors should show how the boundaries move with B⊥ (for example n–E maps at 0, 0.5 and 1.5 T), show that the Lifshitz lines extrapolate to the zero-field boundaries used to place SC1 and the magnets, and restrict the claimed correspondence to boundaries that do not move.

    Raised by: r1, r2, r3

13. **The calibration of n and E is not described.** The Methods give no hBN thicknesses, gate capacitances, formulas for n and E, definition of E (D/ε₀ or otherwise), zero offsets or uncertainty in n. Because f_v = f_FFT·e/(nh) is normalized by n, a few-percent capacitance error shifts every f_v value, the sum-rule tests and every degeneracy assignment (peaks at 1/2 or 1/4). The locations of features such as "E ≈ −35 mV/nm" also depend on the calibration. The authors should report the calibration and how n was cross-checked (Hall density, Landau-fan slopes from the full-metal regions, the E-symmetry of the band-insulator gap), state the resulting uncertainty in f_v, and give any offsets.

    Raised by: r1, r2, r3

14. **The stacking of the measured channel after fabrication is not verified.** Raman mapping (Fig. S13c) was done on the bare flake before transfer, stacking and etching, and rhombohedral domains are known to relax toward Bernal stacking during these steps. Bernal or mixed-stacking inclusions, or a domain wall crossing the Hall bar, would produce exactly the inhomogeneity that gives partial resistance drops and phase coexistence (concern 1). The authors should show post-fabrication Raman of the encapsulated channel, or argue from transport that the whole channel is rhombohedral (for example from the CI gap at E = 0, the band-insulator threshold, or the absence of Bernal-specific Landau-level sequences).

    Raised by: r1, r2, r3

15. **The alignment of the graphene to the top and bottom hBN is not reported.** Near-alignment with hBN produces a moiré potential that strongly changes rhombohedral multilayers. In graphene/hBN heterostructures it has also been tied to unconventional "ferroelectric" hysteresis in gate and displacement-field sweeps. It could also explain the ±E asymmetry between SC1 (positive E) and the finite-E magnet (negative E). The authors should report the twist angles (for example from straight edges or SHG) and show the absence of moiré features (satellite resistance peaks, Brown–Zak oscillations) over the full density range.

    Raised by: r1, r2

16. **Electron temperature, excitation and self-heating in the R(T) and dV/dI data are not given (Figs. 1f, 3e,f, S12b–d).** Base temperature is quoted as 9 mK, but the electron temperature is not calibrated. The SC2 onset (about 80 mK) and the critical currents are small: the dV/dI features occur at tens of nA (about 50 nA) through a 4.7 MΩ bias resistor. The AC excitation for the R_xx maps and for R(T) is not stated, and the "sharp drop" T_c comes from a single R(T) trace. In Fig. S12b the SC2 step is about 30 Ω on a 175 Ω background, about the size of the scatter well below T_c. The authors should state the excitation and electron temperature, show that the R(T) transitions do not depend on excitation, and give the T_c criterion.

    Raised by: r1, r2, r3

17. **The ferrovalley assignment of the zero-field triangle is weakly supported, and part of its reasoning is internally inconsistent (Figs. 1h, S2, S9).**
    - The main text says the butterfly hysteresis is called ferrovalley "due to the absence of electric dipole and Berry curvature at E = 0". Orbital magnetism requires Berry curvature, so the intended argument should be stated precisely.
    - The state is said to be "incompatible with the widely assumed layer antiferromagnet", but the triangle is at n ≈ −0.68×10¹² cm⁻², not at charge neutrality, so the comparison with the CI ground state needs justification.
    - Fig. S9 argues that suppression by in-plane field "is consistent with their valley-polarized nature" because Zeeman energy favours competing states. This is equally consistent with a competing spin-polarized phase becoming favoured, and a valley-polarized state can itself be spin-polarized, so the argument does not discriminate between flavor orders.
    - The transition temperature is given only as "> 3.6 K" (Fig. S2h), and all S2 data are at 1 K rather than base temperature.

    The authors should state which flavor structure they propose. They should give the critical in-plane field as a function of n and compare its slope with the expected Zeeman energy difference between candidate states, or compare the size of ΔR_xy with the expected Chern number. Otherwise they should present the assignment as tentative.

    Raised by: r1, r2, r3

18. **The transition temperatures of the finite-field multiferroic are inconsistently stated.** The main text gives "T_c = 1.5 K (Fig. S11)". Fig. S11 says the coercive field vanishes at about 1.3 K, the switch becomes soft at 2 K, the Hall signal vanishes at 3 K, and calls it a "two-step transition". The statement that the loop "shrinks linearly" with B⊥ (Fig. 4c,d) is also not quantified. The authors should define the criterion behind each temperature, plot the coercive E-width and ΔR_xy against T and B⊥, and use one consistent value in the main text.

    Raised by: r1, r2, r3

19. **The proposed connection between superconductivity and the multiferroic phases is not supported.** The text says "because both multiferroic order is accompanied by a superconducting state, we note a potential connection", and that SC2 "appears in the nearby region of the ferroelectric orbital magnetism (Fig. S12)". But Fig. S12a places the SC2 pockets at n ≈ −1 to −2×10¹² cm⁻² and E ≈ +35 to +55 mV/nm, whereas the finite-E magnet sits at n ≈ 0, E ≈ −35 mV/nm (Fig. 1e, green square). Likewise SC1 (n ≈ −1.7×10¹² cm⁻², E ≈ +35 mV/nm) is not clearly adjacent to the ferrovalley triangle. SC2 is also only a ~20% drop (concerns 1 and 16). The authors should show the relative positions on a common map and give a physical argument, or remove the statement.

    Raised by: r1, r2, r3

## C. Minor

20. The sign of the density is inconsistent: Fig. 4c,d use n = −0.46×10¹¹ cm⁻², while Fig. S10b,c use n = +0.46×10¹¹ cm⁻² for apparently the same maps. The Fig. S10 caption refers to "white arrows in e to f", which should be b and c.

    Raised by: r1, r2, r3

21. Some axis units appear wrong. Fig. S1a has R_xx in kΩ spanning 10² to 10⁶, and Fig. S11a has R_xy in kΩ up to 3000; both are presumably Ω.

    Raised by: r1, r2

22. The Fig. S6 caption gives "1.5 × 10¹² < |n| < 33 × 10¹²", presumably 3.3 × 10¹² cm⁻².

    Raised by: r1, r2, r3

23. The layer-polarization formula in the Methods needs parentheses: (|ψ_top|² − |ψ_bot|²)/(|ψ_top|² + |ψ_bot|²).

    Raised by: r1, r2, r3

24. Typographical issues: "~30 meV/nm" (p. 6, Fig. 3 discussion) should be mV/nm; "electron electron-doped" (Fig. S3 title); "hole hole-doped" (Fig. S5 text); "both multiferroic order is"; "situate the correlated insulator" (p. 3); the garbled Fig. 2 caption reference "f3 Fig. S5i"; and the placeholder "Additional information ... at XXX".

    Raised by: r1, r2, r3

25. The cross-references between Fig. 3g and Fig. S12a are circular: the Fig. 3 caption says the Fig. 3g cut passes through "two superconducting phases (see Fig. S12a)", while Fig. S12a says its dashed line marks the Fig. 3g cut. Make them consistent and mark the cut in the main figure.

    Raised by: r1, r3

26. The "BI" and "CI" labels mentioned for Fig. 1e are hard to find, and the symbols for SC1, the triangle and the comet are small. Labelling the phases directly on Fig. 1e would help readers.

    Raised by: r1

27. The text says the f_v sum rule is "violated" in partially flavor-polarized regimes and cites other rhombohedral systems. Please quote the size of the violations in this device.

    Raised by: r1

28. The Arrhenius gaps in Fig. S1b (29 meV for the CI, 23 meV for the band insulator) are fitted over a narrow high-temperature window (about 20–45 K), where the caption itself says the gap is temperature-dependent. State the fit range and uncertainty, or call these rough activation energies, and note that the 29 meV CI gap is far larger than the U scale of Fig. 1a.

    Raised by: r2, r3

29. The Methods should give the lock-in excitation currents (including for the zero-bias SC data), the Hall-bar dimensions, which contact pairs were used for R_xx and R_xy, the B⊥ range used for each FFT, the sweep rates for the hysteresis measurements, the hBN thicknesses, and whether the R_xy loops were antisymmetrized.

    Raised by: r1, r2, r3

30. Compare the phase diagram, superconductivity and anomalous Hall regions explicitly with the concurrent hexalayer studies (refs. 16 and 19), and state the specific novelty of this work (the semimetal fermiology and the finite-E magnet) against them.

    Raised by: r2

31. The abstract places the ferroelectric state "at large fields around charge neutrality", but it sits at E ≈ −35 mV/nm, well below the ~100 mV/nm band-insulator threshold. Please reword.

    Raised by: r3

32. The names of the orbital-magnet phases vary: the Fig. 1 legend has "Multiferroic orbital magnetism" and "Unipolar multiferroic orbital magnetism", the caption has "Ferrovalley" and "Ferroelectric", and the text has "ferrovalley" and "ferroelectric". Use one consistent nomenclature.

    Raised by: r3
