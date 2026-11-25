## A. Must address

1. **The dichroism could be an elastic-line energy-shift or normalisation artefact, and this has not been excluded.** The largest CD and field-switching features (Fig. 3b(i,ii), Fig. 4a, regions I–II) lie within 0–0.05 eV of the elastic line. The resolution there is about 30 meV FWHM (Methods), so region I (about 0–0.03 eV) sits essentially inside the elastic peak. The difference spectra have a derivative-like, bipolar shape: positive near 0.01–0.02 eV, negative near 0.04–0.05 eV, then positive again. A small relative energy shift, width change or intensity-normalisation mismatch of a strong elastic or quasi-elastic peak produces exactly this shape. The elastic peak (about 1.0–1.5 a.u. in Fig. 3a) is roughly 10 times stronger than the phonon features (about 0.1–0.4), so a shift of a few meV gives a difference of about 0.1 in the units of Fig. 3, which matches the reported contrast. Such shifts are plausible between helicities (different undulator settings, beam position on the sample) and between field states. Under the ±0.2 V hold, piezoelectric or electrostrictive height changes of the membrane could move the scattering point on the spectrometer, and field-induced changes in specular or diffuse elastic scattering are also possible. An intrinsic field-induced phonon energy shift is not expected: time reversal plus the C2 rotation of C4v map ω(q, −P) onto ω(q, +P). The normalisation between spectra (incident flux, acquisition time, total counts, XAS, or elastic or dd intensity) is not stated, and neither is whether the energy zero is set per scan or per summed spectrum. The authors should:
   - show the four raw spectra I(C±, ±E) overlaid, and tabulate the fitted elastic-line position, width and integrated intensity for every scan, by helicity and field state, through the 15 h sequence, with the residual shifts in meV;
   - show the difference spectrum that a shift of the observed size would produce (shift a C+ spectrum by the measured scatter and subtract it), and the CD and field-switching spectra after deliberate ±few-meV relative shifts, to quantify how much of regions I and II survives;
   - subtract the fitted elastic line before forming differences, and report the CD of the elastic (zero-loss) intensity itself and in a window with no phonon weight;
   - state the normalisation and the energy-zero procedure explicitly.

   Without this, the sign reversal under field could reflect a reproducible field-dependent shift rather than reversal of the phonon angular momentum.

   Raised by: r1, r2, r3

2. **The two "independent" observations are the same data, and the decisive decomposition and significance tests are missing.** With four spectra I(helicity, field), CD(+E) − CD(−E) is identically FS(C+) − FS(C−). Fig. 3b(i) and 3b(ii) are therefore one double difference displayed twice, not the two independent confirmations claimed at the top of p. 8. If the contrast is purely a PAM effect, reversing P must be equivalent to reversing helicity, I(C+, +E) = I(C−, −E), and the helicity-averaged spectrum must not depend on field. Fig. 3b(ii) instead shows each helicity's spectrum changing on field reversal. The authors should decompose the four spectra into helicity-even/field-even, helicity-odd/field-even, helicity-even/field-odd and helicity-odd/field-odd parts, and show:
   - that the helicity-even, field-odd part FS(C+) + FS(C−) is consistent with zero; this part would contain non-chiral field-induced changes from strain, electroabsorption or domain-dependent diffuse scattering;
   - that the helicity-odd, field-even part CD(+E) + CD(−E) is small; this part would contain residual birefringence or instrumental CD;
   - that CD(+E) and CD(−E) are each individually non-zero, of opposite sign and of equal magnitude within error, and likewise that FS(C+) and FS(C−) are each non-zero with opposite sign;
   - that the reported effect is the helicity-odd, field-odd part.

   Each test should be quantified per energy window with an integrated value, an uncertainty and a significance against zero (in σ, or as χ² against zero), using unsmoothed data. The CD amplitudes (about ±0.1 a.u.) are comparable to the error bars at many points of Fig. 3b. The error-bar definition also needs reconciling: the Fig. 3 caption says "Poisson statistics on re-binned data (by a factor 2)", while Methods says "standard deviation of individual scans". The number of scans per spectrum, the total counting time per helicity and field state, and how errors propagate into the integrated contrasts of Fig. 4f–h should be given.

   Raised by: r1, r2, r3

3. **Switching of the X-ray-illuminated volume is not verified, and the write voltage appears marginal.** The PFM loop in Fig. 2b is strongly imprinted. The down-to-up branch switches only near +3.5 to +4.5 V, while the other branch switches near −1 to −2 V. The caption nevertheless quotes a coercivity of "approx 3 V". The write pulse used during RIXS was ±3.5 V (Fig. 2c, Methods), so the positive-state write may be incomplete. The PFM was measured with a tip on the film before the beamtime, probably on a different area or device, not through the 60 µm top electrode at the beamline. The Methods claim of "a single ferroelectric domain state" is not supported by any measurement. Further points:
   - the membrane thickness is never given ("various thicknesses", Methods), so the field in kV/cm and its ratio to the coercive field cannot be assessed;
   - the 50 µm beam footprint is barely smaller than the 60 µm electrode (Fig. 2a, Fig. 3 caption), so part of the probed volume may lie on unswitched or unelectroded membrane, especially with beam drift over 15 h;
   - 90° (a/c) domains, which are possible in a freestanding membrane, are not discussed; they would dilute the P-odd signal and introduce birefringence;
   - X-ray photocurrents or charging during hours-long acquisitions could depolarise or pin domains.

   The authors should give the membrane thickness and the corresponding fields, and show switching currents or P–E loops recorded in situ on the measured device at ID32 for each write pulse (before, during and after the RIXS sequence). They should explain why 3.5 V suffices given Fig. 2b, estimate the switched volume fraction and the fraction of the footprint inside the electrode, and give PFM or XRD evidence of the domain population after the beamtime. A field-state-sensitive X-ray observable recorded at the same time would strongly support switching, for example XAS linear dichroism, a polarisation-sensitive XAS signature, or the elastic intensity at a Bragg-sensitive condition. A sub-coercive control is also needed: apply ±1 V write pulses, where no reversal should occur, and show that the CD does not reverse. This would separate polarisation reversal from any direct effect of the applied voltage.

   Raised by: r1, r2, r3

4. **The link between the CD-RIXS signal and J·q is not derived, and the stated geometry appears self-contradictory.** The text says the field-switching measurements "were performed at normal incidence with beam parallel to the optical axis, c" (p. 5; Methods: "largest face perpendicular to c"). It also says the relevant PAM "is expected to be perpendicular to this axis" and is "projected in-plane" (p. 5), and that "the outgoing angle is chosen to minimise the component along c". With the incident beam along c, the incident helicity has no projection on an in-plane J. Yet p. 9 says the CD "will only follow" the in-plane component of q and is "sensitive only to out-of-plane ion displacements", which is a third, different statement and hard to reconcile with Eq. (2) and an in-plane J. Normal incidence is also hard to reconcile with q_z = 0.42 Å⁻¹, the stated in-plane components, and φ rotation. Eq. (1) gives A_m with phase factors e^{±2iφ} without saying which axis φ refers to, or how A_m depends on k_in, k_out, q and J. The text moves between "CD directly probes the rotation of the 2p orbitals", "measures the circular motion of the oxygen atoms" (pp. 5–6) and the projection J·q. J is estimated as "the maximal area of the ellipse the oxygen atom traverses" rather than from the standard expression l = ħ ε†Mε summed over sublattices. It is not stated which oxygen sublattice (apical O1 or equatorial O2) is used, although these differ in symmetry and in hybridisation with the Ti 3d states excited at 531.25 eV. Ti motion also modulates those hybridised states, so the CD may weight Ti and O displacements differently from the mass-weighted J of Eq. (2). Without a derivation, the paper does not establish that the measured sign tracks the PAM rather than another P-odd quantity. The authors should:
   - give the full scattering geometry: incident and outgoing k-vectors relative to the crystal axes, the scattering angle 2θ, the incidence and exit angles for each q, and any analysed outgoing polarisation;
   - derive, at least in a minimal model (for example Franck–Condon with circularly displaced O sites using the DFT eigenvectors and effective charges), how the E1–E1 O K-edge CD depends on J in this geometry, and why J·q rather than J·k_in or J·(k_in − k_out) is the relevant projection;
   - compute J with the standard expression, per sublattice (O-projected) and in total, and show that the J·q maps of Fig. 4c–e are robust to this choice;
   - qualify the abstract's claim that CD-RIXS "directly probe[s]" the PAM until this is done.

   Raised by: r1, r2, r3

5. **There is no null control where the effect should be absent.** Every measurement is on one device at q points where the PAM is predicted to be non-zero, so nothing shows that the analysis returns zero when it should. The paper's own symmetry argument provides natural nulls. q3 = (0, 0.24, 0.42) lies on a σ_v mirror plane of C4v, where J·q = 0 by symmetry (the white line in Fig. 4c–e). Yet its spectrum is omitted from, or only dotted in, Fig. 4a, and it appears only as a single integrated point in Fig. 4f–h. At minimum, the full q3 spectra and their CD and field switching should be shown with error bars alongside q1, q2 and q4, with a statement of whether they vanish as predicted. Further controls would separate the PAM interpretation from electrode-, charging-, birefringence- or other field-odd effects:
   - the same measurement above the Curie temperature (about 120 °C), where the C4v polarity and the switching should vanish;
   - an unpoled, depolarised or multidomain state, or a membrane region outside the electrode;
   - a non-polar reference membrane such as SrTiO3 in the same electrode stack;
   - a q along a high-symmetry direction at both field polarities.

   Raised by: r1, r2, r3

6. **The assignment of the switching CD to specific chiral modes is not supported at the stated resolution.** At 30 meV FWHM resolution, CD features at about 20, 40 and 100 meV are attributed to calculated modes at 11, 38 and 100 meV (p. 7). An 11 meV mode cannot be separated from the elastic line at that resolution, and the 20 versus 11 meV mismatch is not explained. Several modes contribute to each region, as the paper itself invokes for the q1 "outlier". The 100 meV feature lies at the top of the BTO one-phonon spectrum, where p. 5 says features are presumed to be multi-phonon. A clear feature near 0.2 eV is not discussed. The high-resolution (15 meV) scan is described as confirmation (p. 6) but is not shown, although it is the best way to separate phonon contrast from the elastic tail. The integration windows (regions I–III in Fig. 4a) appear to have been chosen after the fact. The authors should:
   - show the high-resolution spectra at the same q, with CD and field switching;
   - show the computed dispersion and the effective-charge intensity estimate (Fig. S.11) in the main text;
   - fit all spectra (both helicities, both field states, all four q, plus the high-resolution data) with resolution-convolved, effective-charge-weighted DFT mode intensities, with energies fixed and amplitudes free, and compare a predicted CD spectrum per q with the full measured spectrum rather than three windows;
   - show which modes contribute to each window and state how the windows were chosen.

   Raised by: r1, r2, r3

## B. Should address

7. **The q-dependence comparison with DFT (Fig. 4f–h) rests on free scale factors, possibly including a sign, applied to four points per mode.** The measured contrasts are compared with J·q "when scaled accordingly" (p. 9) at four φ values over about 1.2 rad. With one free amplitude and a predicted curve that changes sign once, agreement in sign at three or four points is a modest test, and the q1 point in region I (Fig. 4f) is an acknowledged outlier. From the colour coding, the scale factor appears positive in panel f (red, negative-J·q points have negative contrast) but negative in panel g (red points near φ ≈ 1.1 rad have contrast of about +1). The sign of the contrast relative to P is the key physical prediction, so a free per-mode sign reduces the test to the shape of a sinusoid-like curve. In panel h the computed J·q (±0.002) is about 50 times smaller than for the 11 and 38 meV modes (±0.1, ±0.06), yet the measured contrast is of comparable magnitude (about 0.75 against about 2 a.u.). This is unexplained if contrast is proportional to J·q. Fig. 4a shows only q1, q2 and q4 in C− light. The authors should:
   - state which parameters are fitted (scale, sign, offset), give the fitted values with uncertainties, and justify any sign difference between modes from the scattering matrix element;
   - give a goodness of fit and compare it with null models such as a φ-independent or zero contrast, a random sign, or sin/cos forms not tied to DFT;
   - say whether field-switching data were taken in both field states and with both helicities at all four q;
   - temper "excellent agreement" accordingly.

   Raised by: r1, r2, r3

8. **Fitting the elastic line from the energy-gain side is biased at room temperature.** The text (p. 6) says the energy-gain side contains only thermally excited states and fits the elastic line to it with a half-Lorentzian. At room temperature kT ≈ 25 meV, so the 11 and 38 meV modes have substantial anti-Stokes weight on that side, with Bose factors of roughly 0.6 and 0.2 relative to Stokes. This biases both the energy zero and the elastic subtraction. The bias would differ between helicities if the anti-Stokes phonons themselves carry CD. The authors should fit Stokes and anti-Stokes phonons together with the elastic line under detailed balance, or calibrate the zero independently (for example with a carbon-tape reference before and after each block), and show that the CD conclusions do not depend on the choice.

   Raised by: r1

9. **The DFT structure departs substantially from experiment in the quantity that controls the effect.** The relaxed lattice (Methods, p. 13) has c/a = 4.11/3.99 ≈ 1.030, against the experimental 4.03/4.00 ≈ 1.0075. PBE overestimates tetragonality in BaTiO3, which inflates the polar distortion and so, by the paper's own argument, the PAM. It particularly affects the low-energy, soft-mode-derived 11 and 38 meV modes on which the assignment rests. At 0 K, tetragonal BTO in DFT is not the ground state and typically has imaginary modes. The relaxation "to an internal pressure of 70 kPa" with a D3 dispersion correction is not explained. It is not stated whether the non-analytic (LO–TO, Born effective charge) correction was included at |q| ≈ 0.48 Å⁻¹ (in-plane components about 0.23 Å⁻¹). Bulk calculations are compared with a freestanding membrane of unspecified thickness and possibly different strain. The authors should show the full dispersion with any imaginary modes and say how they were treated. They should recompute the key mode energies, eigenvectors and J·q (sign pattern and magnitude) at the experimental lattice parameters and displacement, or with PBEsol, and state the non-analytic treatment. They should also compare with the membrane's actual lattice parameters from the XRD in Figs. S.1–2, and confirm that the membrane is tetragonal at the measurement temperature.

   Raised by: r1, r2, r3

10. **The "non-volatile" and 15-hour stability claims are not demonstrated.** The abstract and p. 3 claim non-volatile control. However, every RIXS spectrum was taken under a ±0.2 V hold bias (Fig. 2c, p. 6), applied explicitly "to ensure the ferroelectric domains remain stable". The data therefore show reproducible switching under bias, not retention at zero field. "Stable for at least 15 hours" (abstract, Fig. 3 caption, p. 10) is inferred from data summed over a sequence of roughly five to eight state changes (Fig. 2c), so it is not shown that the sign follows the field in every cycle or that the CD is stable within each state. The authors should show the CD or field-switching contrast for each cycle and block against time across the 16 h sequence, and measure at least one state at zero bias after writing. Otherwise they should remove or rephrase these claims.

    Raised by: r1, r2, r3

11. **The exclusion of birefringence and domain effects is qualitative and rests on unstated assumptions.** Birefringent CD is said to be removed by normal incidence along c (p. 5, Methods Eq. 5), although Fig. S.4 shows it can be "strong". This assumes a pure c-domain membrane with no a/c domains, no in-plane anisotropy from transfer, clamping or wrinkling, and exact alignment. The outgoing beam is far from c in any case. Birefringent CD should be P-even, since the optic axis is unchanged under P → −P, so CD(+E) + CD(−E) directly measures this background (see concern 2). However, 180° switching may change the domain-wall configuration, so a residual birefringent CD could also change under field. A linear electro-optic contribution under the hold bias would be P-odd. The authors should give the incidence and exit angles for each q and the misalignment tolerance, and estimate the residual birefringent CD at those angles from the Fig. S.4 model. They should also characterise the domain state of the measured membrane (PFM on the device, or XRD for a-domain fractions), estimate the electro-optic term, and explain why the residual cannot be field-odd.

    Raised by: r1, r2, r3

12. **The device stack could contribute to the O K-edge signal and its dichroism.** The top electrode is 4 nm Cr / 8 nm Au, and Cr adhesion layers readily oxidise. Any Cr oxide, interfacial or adsorbed oxygen contributes at 531.25 eV, on the leading edge, where such contributions are strongest. The electrode layers are also in the beam path and are not addressed in the birefringence discussion. The authors should quantify the O K-edge XAS from a bare-electrode region, estimate the electrode contribution to the signal and its polarisation dependence, and explain why the electrode cannot produce field-odd dichroism.

    Raised by: r1, r3

13. **Conditions that could produce slowly evolving or field-correlated changes are not reported.** The sample temperature during RIXS is not stated; room temperature is only implied. It should be shown to stay within the tetragonal phase under beam and Joule heating. Prolonged soft X-ray exposure at the O K edge under bias can create or migrate oxygen vacancies and alter leakage or imprint. The leakage current under the hold bias and the X-ray photocurrent under the electrode are not given. The authors should state the temperature, show XAS before and after the sequence (Methods mentions XAS "before/during"), and show leakage current against time, so that an electrostatic or defect contribution to the field-switching signal can be excluded.

    Raised by: r1, r2, r3

14. **Only one device is shown.** All results come from one membrane and electrode. The effect is a small difference signal that is vulnerable to device-specific artefacts: electrode edges, leakage under bias, charging. The authors should report whether other devices, electrode pads or membrane thicknesses were measured, and whether the sign and magnitude of the switching reproduce, ideally including a repeat after a thermal cycle. If only one device was measured, this should be stated clearly.

    Raised by: r1, r2, r3

15. **The gyroelectric analogy is not justified for C4v.** Eqs. 3–4 are drawn from the electrogyration of gyrotropic ferroelectrics such as Pb5Ge3O11 (point group 3), which are optically active at q ≈ 0. Tetragonal BTO (4mm) is not an optically active class, so the q → 0 gyration tensor g_ij of Eq. (4) vanishes by symmetry for a uniform polar state. The effect here relies on finite-q (spatially dispersive) response, which is a different thing. The notation λ_klj in Eq. (3) is not defined. Eq. (4) posits g ∝ P_s, but with only two states (±P), linearity in P is not tested. The authors should derive the symmetry-allowed tensor component for 4mm at finite q that maps onto the CD-RIXS observable, and test intermediate (partially switched) states if they want to claim linearity. Otherwise they should rephrase the result as a sign reversal consistent with a P-odd response and drop the "gyroelectric effect" label from the abstract and p. 8.

    Raised by: r1, r2, r3

## C. Minor

16. The momentum units are inconsistent. The main text (p. 5) gives q = (−0.12, 0.20, 0.42) "r.l.u.", while Table 1 gives the same numbers in Å⁻¹. At 531 eV the maximum momentum transfer is about 0.54 Å⁻¹, so q_z = 0.42 r.l.u. (about 0.65 Å⁻¹) would be kinematically inaccessible. Please correct the units, give q also in r.l.u. of the measured lattice, and give the scattering and incidence angles used.

    Raised by: r1, r2, r3

17. The Fig. 3 caption says Savitzky–Golay smoothing is applied "to guide the eye", but Fig. 4f–h integrate "SG smoothed" contrast (Fig. 4a caption). Please state whether the integrated values use raw or smoothed data, give the SG window relative to the 30 meV resolution, and show unsmoothed data in the main figures.

    Raised by: r1, r2, r3

18. The Fig. 3a axis is labelled "FY (a.u.)" for RIXS spectra, and the vertical offset between spectra is not stated. Please correct the label and state the offset and the normalisation used before forming the CD.

    Raised by: r1

19. The Fig. 2b caption says the loop "yields a measure of coercivity of approx 3 V", but the loop is markedly asymmetric (about −1 V and +4 V). Please give both coercive voltages and the imprint.

    Raised by: r1

20. In Fig. 2c, make the colour legend and the '+ − − +' sequence consistent with the text. The time-axis break near 4 h hides part of the protocol; please show the full sequence.

    Raised by: r1

21. Eq. 1 uses φ without defining it. The transfer matrix "Eq. 5 in Methods" is the Stokes polarisation matrix, not the RIXS scattering tensor. Please define all symbols and give the full scattering amplitude used.

    Raised by: r1, r2

22. Fig. 4 labelling: Fig. 4b labels the angular momentum as ω, which conflicts with ω for frequency in Eq. (3), and the units of "Δ_AM" should be defined. "Maximal area of the ellipse" should be defined quantitatively. The colour bar of Fig. 4h spans ±0.002 while Fig. 4e spans ±0.05 for the same 100 meV mode; please explain or make them consistent. The Fig. 4a legend (q4, q1, q2 with overbars?) should be clarified.

    Raised by: r2, r3

23. Fig. 1b is labelled "Energy (meV)" with ±10 meV wells for Ti displacements of ±0.05 Å, "taken from Cohen". Please state the original units and parameters.

    Raised by: r2

24. The Fig. 3 caption mentions "positive electric field (0.2 V)". A voltage is not a field; please give the field, which requires the thickness (concern 3).

    Raised by: r2

25. Wording overstates the agreement: "perfect qualitative agreement" (p. 6), "excellent agreement" (abstract), "within experimental error" (p. 9), and the Fig. 4 caption's contrast "matches the calculated values well for the 3 phonon modes". These should be replaced by quantitative statements and qualified in light of the q1 outlier and the free scaling (concern 7).

    Raised by: r1, r2, r3

26. Typos and reference errors:
    - "hexagonal lattice constants" (Methods, p. 13) should be tetragonal;
    - "an orbital magnetic moments" (p. 2);
    - "temporally applied" should be "temporarily applied" (p. 6);
    - "As an aide" should be "As an aside" (p. 8);
    - "Phonons modes" (p. 6);
    - p. 3: "applied across the plane of the sample" conflicts with the out-of-plane field geometry;
    - Ref. [52] is dated 2028;
    - Ref. [42] has garbled formatting.

    Raised by: r1, r2, r3

27. The supplementary material was not available, so statements relying on Figs. S.3–S.11 could not be checked. Key elements are cited only there: the XAS, the energy optimisation that fixed the 531.25 eV operating point, the birefringence data, and the dispersion and effective charges (Fig. S.11). The main text should carry enough of them to support the central claims, particularly the birefringence check and the energy optimisation.

    Raised by: r1, r3
