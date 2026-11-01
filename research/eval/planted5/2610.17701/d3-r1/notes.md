# Run notes: arXiv 2610.17701v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries).
- Read: the skill, report-template.md, the library (entries, tests and checks) and the extracted paper text (paper.txt). I did not run read_mtx.py because there was no figure data.
- Not opened, by instruction: the arXiv abstract page, the PDF and any version of the paper. The title comes from the text's first lines. The extracted text has no page numbers, so quotes are located by section and figure. Figure details come from the captions only. The supplementary figures (S1 to S11) are referenced but not in the text, so I could not check claims that rest on them (ARPES in Figs. S6-S7, island growth in Fig. S3, QPI in Figs. S8 and S10, the four-terminal concept in Fig. S11). No data repository is linked ("Source data will be provided with this paper"), so I counted no devices from data.
- Recognized the paper: no.

## Claims table (step 1)

| Claim | Figures | Device / data | Counts and ranges |
|---|---|---|---|
| Interfacial superconductivity confined to the 1QL Bi2Te3 islands on 20 UC FeTe; moiré-modulated gap | Fig. 1D-I, S3, S4 | One heterostructure (number of samples not stated) | Gap peaks at ±1.85 and ±2.92 meV; moiré period 2.9 nm; Fig. 1D at T = 1.6 K |
| Star-shaped vortex with QPI-like modulations from the Bi2Te3 layer | Fig. 2A-G | One vortex, 50 nm map, 1.0 T, 0.4 K | Maps at 0 and ±3 meV |
| Zero-bias peak at the core: FWHM about 0.5 meV, height about twice the above-gap conductance, plus levels spaced about 0.7 meV read as integer CdGM | Fig. 2I, 3B-E, 3G | One vortex in an island (Figs. 2 and 3 may be the same vortex) | 1.0 T and 0 T only; 0.4 K only; setpoints 500 pA (Fig. 2I) and 1 nA (Fig. 3); resolution about 0.37 meV; Vmod 0.1 mV |
| Isotropic decay of the zero-bias peak, shorter than the Bi2Te3 branch, read as FeTe origin (stacked core) | Fig. 3H-I, 4A | Same vortex, two directions | Decay length value not given in the text |
| Dispersive X-shaped Bi2Te3-derived branch | Fig. 3F, S8A | Same vortex, 10 to 20 nm from the center | k_F about 0.3 nm^-1, E_F about 300 meV, spacing about 0.03 meV |
| Majorana zero modes in all measured vortices; number tuned by field and island size (1, 2, 3 vortices) | Abstract, Fig. 4B-D | Zero-energy maps, 68 nm, without spectra | Fields not stated; island sizes not stated; number of vortices, islands and samples measured: missing |
| Dirac-like band in Te-annealed FeTe, absent in as-grown FeTe | Figs. S6-S7 (not available) | Separate ARPES samples | Not in the heterostructure |

## Entries matched, adapted, skipped

- Scope: this is STM vortex spectroscopy. I adapted the zbp checks to vortex spectra: dot search became trivial bound states at the core; both ends became the partner at the far end of the vortex line; transparency became tip-sample coupling; the nonlocal gap became the bulk topology of the host layer; raw conductance became normalization.
- Adapted entries: fine-tuning-and-selection (applies as written), local-probe-loophole (STM is a local probe), and disorder-induced-zbp. I adapted the last one to zero-energy states from disorder, here interstitial excess Fe, which the paper itself discusses. For the test "Bulk gap closing and reopening" I marked "no": the ARPES Dirac-like band is on Te-annealed FeTe, a separate sample, and the paper argues that the heterostructure resembles it.
- Skipped, because they need a wire, junction or transport device:
  - abs-quantum-dot: there is no tunnel-barrier dot in STM through vacuum.
  - quasi-majorana-smooth-confinement: wire-end potential.
  - crowded-trivial-subgap-states: multiband wire. Its STM analog is covered by the outside row on merged CdGM states.
  - kondo-resonance: no quantum dot. The 0 T spectrum shows a gap.
  - weak-antilocalization: disordered wire transport.
  - fine-tuned-plateau and series-resistance-subtraction: no quantized conductance claim.
  - one-end-only: no wire ends. The partner question is covered by local-probe-loophole.
  - trivial-andreev-band-gap-reopening: no nonlocal conductance.
  - micromagnet-stray-field: applied field, no magnets.
  - full-shell-flux-andreev: no full-shell wire.
  - spin-orbit-length-pinning: no normal segment.
  - exceptional-point-zero-mode: weakly coupled STM tip.
  - protocol-parameter-sensitivity: no automated protocol.
  - All shapiro, supercurrent, charge, chiral, island, kitaev and diode entries: different signatures.
- Outside rows, with tests taken from each source's described control:
  - Half-odd-integer CdGM levels in a trivial vortex (Kong et al., 1901.02293).
  - Merged CdGM states giving a zero-bias peak at the center (Xu et al., 1312.7110; supported by Chen et al., 1709.09401).

## Hold-out

- I searched the library for the arXiv ID, title words and system (2610.17701, "Han", "Bi2Te3/FeTe"). Nothing matched, so I held out no source. I did not open the library's source URLs.

## Related work checks

All five were confirmed by opening the arXiv abstract page (ID, title, first author and abstract content):
- 1901.02293 Kong
- 1709.09401 Chen
- 1312.7110 Xu
- 1403.1027 Yin
- 1904.06124 Zhu

None was checked in full text. The arXiv API search for Machida et al. (Nat. Mater. 2019) returned nothing, so I left it out.

## Library gaps

- The library has no family for STM vortex spectroscopy. Candidate entries:
  - Half-odd-integer CdGM levels in a trivial vortex (Kong 2019).
  - CdGM states merging into a zero-bias peak when Δ²/E_F is below resolution (Chen 2017, Xu 2013).
  - The zero-energy bound state at interstitial Fe (Yin 2014).
- A vortex check list would help: level-sequence fit at the stated resolution; spatial splitting profile; spectra at the same spot at zero field; tunnel-coupling plateau (Zhu 2019); temperature series; spectra for every vortex in a multi-vortex map.

## Unsure

- Figs. 2 and 3 may show the same vortex. I treated the spectra as one vortex.
- I counted the Figs. 4B-D zero-energy maps as evidence offered for "number controllable" Majorana modes. So the spectral tests are "part", with spectra shown for one vortex.
- The paper's wording moves between "consistent with Majorana zero modes" (introduction, near Fig. 3 text) and "These observations provide compelling spectroscopic evidence for the presence of Majorana zero modes" (Fig. 3 section).
- "A trivial scenario is that this MZM is generated from superconducting FeTe" probably means "a simple scenario". I didn't raise it.
- The decay length value is not in the text, so I phrased the overlap suggestion qualitatively.
- I counted "all measured vortices" as a stated fraction without a number, so I marked it "part".

## Skill issues

- The skill asks for page numbers, but for text-only input there are none. It doesn't say what to cite instead.
- The skill doesn't say how to fill flags "test" text for an adapted entry. I kept the library wording and judged by the adapted meaning.
- When an STM instance of a library mechanism exists (interstitial-Fe zero modes as disorder-induced zero-energy states), it is unclear whether it should be an adapted library row or an outside row. I chose the adapted row and put the specific control in the suggested check.
- The zbp check "both ends" has no STM analog. "Not done" is a little harsh when the measurement is out of reach, and the skill doesn't cover that case.
- The template's Related work line shape doesn't say how to treat LaTeX in titles. I wrote plain text.
