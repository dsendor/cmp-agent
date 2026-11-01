# Run notes: arXiv 2610.29446v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (updated 2026-10-24), 28 lookalike entries plus checks.
- Read once at start: skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (entries, tests, checks).
- Paper: extracted text only (scratchpad planted2/blind/j50/paper.txt), v1, main text pp. 1-4 and supplement pp. S1-S8. Per the run instructions I did not fetch the abstract page, PDF or HTML. The title is taken from the text header. Figure content taken from captions only; I could not look at any figure, so tests that depend on reading a figure (for example the end-state energies in Fig. S1(a)) are judged from captions and text.
- No ancillary data or code; read_mtx.py not used. No data repository linked; none consulted.
- Recognition: I did not recognize the paper (dated 21 Oct 2026, after my training data) and used no knowledge of its later history.
- Output: report and notes returned in the reply (the run forbids .md writes); flags.json written to cmp-assistant/eval/planted5/2610.29446/num-r1/flags.json. Working copy of the report at scratchpad/work-2610.29446-num-r1/report.txt.

## Claims table (step 1)

| Claim | Figures | Device | Counts and ranges |
|---|---|---|---|
| Chain-length-driven closing and reopening of in-gap spectrum | Fig. 2(a) (exp.), 2(b) (calc.) | Cr4, Cr5, Cr8, Cr12 on Bi-terminated β-Bi2Pd | One chain per length shown, called "representative" (p. 2). Built by adding atoms to one end; whether one chain or several is not stated. Chains built, measured, broken: not given. Lengths 6, 7, 9-11, >12: not shown. Cr4 mini-gap unresolved by experiment. |
| Zero-bias modes localized at both ends of Cr12 | Fig. 2(a), Fig. 4(b), Fig. S1(a,c) | One Cr12 chain | Number of Cr12 chains: not given. End amplitudes imbalanced (p. 3). |
| Reopened gap Δtopo = 204 ± 50 µeV | Fig. S3 | Cr12 chain center minus clean substrate dI/dV | One spectrum pair. Calculated gaps 84 µeV (αR 1.8) and 146 µeV (αR 2.5). |
| Electron-hole character exchange, spin texture | Fig. 3, Fig. S2 | Calculation only | No spin-polarized measurement. |
| ξM ≃ 10.5 Å, about three sites | Eq. (1), Sec. S5 | Calculation only (δε = 16.8 µeV at ΓD = 5 µeV) | L given as 114 Å (p. 3) and 57 Å (p. S3). Experimental splitting not resolved. |
| RF broadening of compact modes | Fig. S4, Fig. S5 | "Cr∗12" chain, atoms 3 and 6 | 44 GHz; VRF up to 0.22 mV. |
| Ranges | | | T = 30 mK; lock-in 30 µV at 330 Hz; image setpoint 3 mV, 50 pA; Tc 5.2 K; Δ = 0.76 meV; no magnetic field data; spectroscopy setpoint and bias windows not stated. |

## Numbers I checked

- 12 × 4.75 Å = 57 Å. The main text's "114 Å" is inconsistent with its own product and with Sec. S5.
- Eq. (1) with ħ²/m_e = 7.62 eV Å², kF = 0.18/a0 = 0.340 Å^-1, δε = 16.8 µeV, cos = 1: L = 57 Å gives ξM ≈ 11.1 Å (close to 10.5); L = 114 Å gives ξM ≈ 24 Å. cos(kF L) at 57 Å is about 0.86, so cos ≈ 1 is a modest approximation.
- 10.5 Å / 4.75 Å ≈ 2.2 sites, against "three lattice sites" (p. 3).
- J gradient: 2.5 eV to 2.35 eV is 6%, consistent between main text and Sec. S3.
- Δ/kTc = 0.76 meV / (k × 5.2 K) ≈ 1.70, plausible. 44 GHz photon energy ≈ 182 µeV.
- Rashba coupling: 1.8 eV·Å (Sec. S2, from DFT) and 3.6 eV·Å (Sec. S4, "In the present work") conflict; which one the main figures use is unclear.
- Cross-reference slips: Sec. S6 cites "Fig. 3" for the edge asymmetry (Fig. 4 shows it); Sec. S8 cites "the microwave study of Fig. 4" (the RF profiles are Fig. S5).

## Entries matched, adapted, skipped

Scope adaptation: STM spectroscopy of atomic chains is outside the nanowire transport the library is written for. I used the zbp checks and entries with chain length as the tuning knob, the chain center as the bulk probe, and tip height as transparency.

Matched (adapted where noted): abs-quantum-dot (adapted to trivial Andreev or YSR end states; test 1 read as end peaks that split and recross with length), quasi-majorana-smooth-confinement (gap test read as chain center versus length), disorder-induced-zbp (gate test read as local perturbations), trivial-andreev-band-gap-reopening (the "protocol" read as the paper's combined criteria), one-end-only, local-probe-loophole, kondo-resonance (adapted to magnetic adatoms; even-odd occupancy has no direct analogue), fine-tuning-and-selection.

Skipped: crowded-trivial-subgap-states (signature is ubiquitous peaks across many multiband nanowire devices; borderline, since β-Bi2Pd is multiband and the model is single-gap); weak-antilocalization (needs a disordered multichannel wire); fine-tuned-plateau and series-resistance-subtraction (no quantized conductance claim); micromagnet-stray-field (no magnets); full-shell-flux-andreev (no full shell); spin-orbit-length-pinning (no normal segment, no field sweep); exceptional-point-zero-mode (chain coupled to a superconductor, weak tunnelling to the tip; borderline); false-poor-mans-majorana (quantum dot Kitaev chains, though its "extend the chain" test overlaps the length series); protocol-parameter-sensitivity (no pass/fail protocol); all shapiro, supercurrent, charge, chiral, island, diode entries (wrong signal).

Checks walked: zbp-dot-search, zbp-wide-ranges, zbp-both-ends, zbp-transparency, zbp-nonlocal-gap, zbp-raw-conductance (all adapted), report-counts, report-ranges, report-processing.

## Sources held out

None. No library source could plausibly discuss a paper posted 21 Oct 2026; I checked dates of the two latest-revised sources: 2502.19560 v2 posted 21 Oct 2026 (a comment on the Microsoft TGP paper, source only for protocol-parameter-sensitivity, which I did not match) and 2501.18631 v2 posted 25 Mar 2026. I did not fetch every source to confirm.

## Related work, how checked

All five opened on their arXiv abstract page (title and first author confirmed from page metadata) and abstract read via the arXiv API:
- 2104.11503 Schneider et al., abstract.
- 2211.00561 Schneider et al., abstract (also the source and control for the outside row).
- 2112.05708 Küster et al., abstract.
- 2204.02324 Hess et al., abstract.
- 1412.0151 Peng et al., abstract.
No full texts read.

## Library gaps

- Trivial end states identified by a local perturbation at one end (Schneider et al. 2022, arXiv 2211.00561): a Majorana pair should respond together. Added as an outside row; worth a library entry for spin-chain papers.
- No family or checks for STM spin chains on superconductors (Shiba chains): trivial YSR end states (Küster et al. 2112.05708), length-dependent splitting at both ends (Schneider et al. 2104.11503), and spin-polarized STM tests are all missing.
- Kondo entry's tests assume a quantum dot (even-odd occupancy); an adatom version would help.

## Unsure

- Whether a length-driven gap closing counts as equivalent to bulk gap closing in nonlocal conductance. I counted it as an equivalent test shown "part", since chain length changes finite-size level structure along with any bulk gap.
- fine-tuning-and-selection note: "representative" hints at more chains, which I left as "not mentioned" with the quote in the table. "data bear on it" was the alternative.
- Outside row note: "data bear on it" since Fig. S1(a) holds energy-resolved data at both ends; "argued, not tested" was possible given the paper's theory argument about the asymmetry.
- Kondo inclusion is a stretch at T ≪ Δ; kept as not mentioned.
- Report runs about 1,000 words outside the table, over the 600-900 aim, mainly from the nine checks and the eight questions.

## Skill issues

- Step "Input" says to read the abstract page and PDF; this run allowed text only, so the title came from the text and figures from captions. The skill has no instruction for text-only input.
- The skill doesn't say whether to check internal arithmetic. I used the one free question for the L = 114 Å versus 57 Å discrepancy.
- Hold-out rule gives no method for checking whether sources discuss the paper short of fetching every source.
- Scope adaptation: the skill says to adapt entries but not which checks family to use when none fits; I used zbp.
- "Every status except Not tested (not mentioned) needs a quote" leaves open whether a quote may be shown for a not-mentioned row; I showed one for fine-tuning-and-selection.
- Step 7 says write reports/<id>.md; the run instruction overrides this.
