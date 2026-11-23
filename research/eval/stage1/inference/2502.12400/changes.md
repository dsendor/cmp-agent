# Changes from arXiv v1 to the accepted version (2502.12400)

AI-generated change log. Old = arXiv v1 (7 pages, PRB-style). New = the version the journal
accepted (Communications Physics, 8 pages). The supplement was not available for either
version. Page numbers refer to the `=== old|new PAGE n ===` markers.

## Title, abstract and framing

- c1 (editorial). The abstract is unchanged in substance. Only the wording changes: "transport
  current" becomes "transport supercurrent", and "mediate" becomes "conveying". The claims stay
  the same: contact width increases both I_c and η, B_η is linear in 1/W_sc and saturates, and
  B* is gate dependent. Old p1, new p1.
- c2 (added). The introduction adds that "few experimental works have systematically varied
  this geometric parameter", citing Haxell et al. (ref. 32). Old p1, new p1.

## Devices and geometry

- c3 (added). The W_sc → ∞ device is now defined: "we do not etch the superconducting leads".
  The nearest superconductor–insulator edge is tens of microns away, so the device is treated
  as the W_sc → ∞ limit. Old p2 (undefined), new p2.
- c15 (added). The geometry is clarified. The mesa etch goes "down to an insulating substrate".
  The Al etch defining W_sc goes "down to the underlying semiconductor", so the 2DEG continues
  behind each contact. A new Methods section on device nanofabrication gives the etchants and
  the 380 nm mesa etch depth. Old p2, new p2 and p6.
- c14 (added). A new Methods section on the material heterostructure gives the growth sequence,
  with the quantum-well layers listed bottom to top (4 nm InGaAs bottom barrier, 4 nm InAs,
  10 nm InGaAs top barrier). It also gives van der Pauw values: μ = 9.86 × 10³ cm²/Vs,
  n = 8.14 × 10¹¹ cm⁻² and ℓ_e = 147 nm. **New inconsistency:** the main text (new p2–3)
  still uses n = 6 × 10¹² cm⁻² and ℓ = 130 nm for the dirty-limit coherence length. New p6.

## Measurement method

- c4 (new_analysis). A new subsection, "Eliminating nonreciprocal effects of an out-of-plane
  magnetic field component", explains why B_⊥ drift and misalignment matter. It defines I_c±
  as extrema over a narrow B_⊥ sweep (new Eqs. 1a, 1b) and justifies extremizing over B_⊥ as
  equivalent to extremizing over phase without flux modulation (citing Dynes and Fulton). Fig. 1
  gains panels c–g: a full Fraunhofer map, zooms near the extrema at B_∥ = −125, 0 and +125 mT,
  and a gate map. Old p2 had a two-sentence description pointing to the supplement. New p2–3.
- c5 (added). The current is swept with increasing magnitude, so switching (not retrapping)
  currents are compared. Each branch is fitted locally about its own extremum. The text notes
  that B_⊥+ ≠ B_⊥− because of a slightly asymmetric J_c(x), and says that comparing each branch
  at its own extremum removes geometric nonreciprocity from fabrication imperfections. New p2.
- c7 (added). B_⊥ is kept within the central lobe throughout the B_∥ sweep "to avoid trapping
  vortices", with a new supplementary section on flux jumps. The W_sc → ∞ device is an
  exception: its data come from a separate smoothing procedure (new supplementary section).
  New p2.
- c13 (added). A new Methods section on measurement and analysis gives a base temperature of
  about 30 mK, the dc current-bias and voltage-readout chain, and the triple-axis vector magnet.
  The I_c uncertainty is the rms deviation of the data from the local Fraunhofer fit, and is
  propagated into η assuming zero covariance. The text says the chip was "cooled down multiple
  times". New p6.

## New data

- c6 (new_data). Fig. 1h shows η(B_∥) with the field parallel to the current (θ = 0) and
  perpendicular to it (θ = π/2), with one-standard-deviation bands. The θ = 0 band includes a
  possible 2° misalignment, and a new supplementary section covers the longitudinal diode
  effect. This is the null control with the field along the current. It is shown for one
  representative device. New p3, p6.
- c11 (added). The text now states that there is no measurable nonreciprocity at zero field,
  η(0) ≈ 0 within uncertainty, so the applied field is the only source of time-reversal
  breaking. New p4.
- c12 (new_analysis). Uncertainties are added. B* in Figs. 3c and 4 (old Figs. 2c and 3) now
  has error bars, "the standard errors obtained from a fit" to the model of ref. 8. Fig. 5a (old
  Fig. 4a) has shaded one-standard-deviation bands, explained in Methods. Figs. 3b, 5b and 5c
  get no stated error bars. Old p3–4, new p4–5.

## Coherence-length model (Eq. 1 old, Eq. 2 new)

- c8 (reframed). The mechanism behind Eq. 1 is reworded. The old version said a Cooper pair
  "may be reflected at the rear interface". The new version says it "may be Andreev-reflected at
  the distal interface", "converting supercurrent into normal current". This treats the rear
  edge as an S/N boundary. The sentence relating reflection probability to wavefunction
  amplitude is unchanged. Old p2, new p2.
- c9 (added). After the ξ = 586 nm fit, the text adds that the agreement with the dirty-limit
  length indicates that correlations "propagate diffusively in the superconducting contacts",
  which suppresses I_c for W_sc ≲ ξ. The fit itself, its value and the missing uncertainty are
  unchanged. Old p3, new p2.
- c10 (added). A new caveat says finite W_sc may also cause confinement effects that modify the
  Andreev spectrum beyond the exponential-decay picture. These are "not required" to explain
  the scaling but matter more as W_sc → 0. New p3.

## Diode-effect interpretation

- c16 (reframed). The footnote on Eq. 5 (now Eq. 6) moves into the text. A sentence notes that
  the second Rashba Fermi surface shifts oppositely and is neglected. The estimated extremal
  field B_∥^max is renamed B_η, which makes clear that it is compared with the measured B_η.
  The sentence "none of the above estimates ... are a particularly good match" is unchanged.
  It also says "none" in v1, where a footnote split the sentence across the page. Old p5,
  new p5.
- c17 (softened). The Conclusion adds that orbital and spin–orbit contributions coexist "with
  their relative contributions varying with gate voltage, magnetic field, and W_sc". Old p5,
  new p6.
- Unchanged: Eq. 3 (now Eq. 4), the Fig. 5c fit excluding W_sc → ∞, Φ/Φ0 ≈ 0.36–0.61, the
  saturation claim for W_sc ≳ 2ξ, the Josephson-vortex explanation for the excluded point, the
  resonance-condition sentence, and the whole B* gate-dependence argument (Eq. 2, now Eq. 3).

## Editorial

- c18 (editorial). Data and code availability statements (Zenodo) are added, along with author
  contributions and a note that a peer review file is available. New p6–7.
- c19 (editorial). Figures are reorganized: old Fig. 1b becomes its own Fig. 2 ("not to
  scale"), and old Figs. 2, 3 and 4 become Figs. 3, 4 and 5. Equations are renumbered. The text
  moves to journal format, with section numbers removed and reference titles added.
