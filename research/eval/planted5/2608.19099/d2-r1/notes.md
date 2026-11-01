# Run notes: arXiv 2608.19099v1

- Library: cmp-assistant/library/lookalikes.yaml, meta.version 0.5 (28 lookalike entries; checks for zbp, shapiro, kitaev, charge, practice).
- Date: 2026-10-24. AI only.

## What I read

- skill/SKILL.md, skill/report-template.md, library/lookalikes.yaml (all entries, tests, checks section), once at the start.
- The paper: extracted text only (scratchpad planted2/blind/f59/paper.txt), v1, 5 pages of main text plus references. Figure details taken from captions.
- Not read, per the run instructions: the arXiv abstract page, PDF or HTML of the paper. The report title is taken from the paper text and shortened.
- Not available: the Supplemental Material [40]. The main text says self-fields, Meissner screening and geometric asymmetry "are ruled out, as shown in SM [40]", and points to the SM for sign conventions, RMCD, micromagnetics and first-principles. None of that was in the text.
- No data repository or ancillary files are linked in the text; read_mtx.py not used.
- I did not recognize the paper.

## Page convention

Pages follow the page markers in the extracted text: p. 1 abstract and intro; p. 2 Fig. 1 caption, fabrication, field-free SDE, start of the field-history discussion; p. 3 Fig. 2 caption, Fig. 3(a) discussion, symmetry argument and the inverted sign-change fields; p. 4 Fig. 3 and Fig. 4 captions, the SM ruling-out sentence, RMCD and micromagnetics; p. 5 GL theory and summary.

## Claims table (step 1)

| Claimed signal | Figures | Device | Counts and ranges stated | Missing |
|---|---|---|---|---|
| Field-free SDE, η = −15.2% after zero-field cooling, −35.7% after field training | Fig. 1(c), 1(d), 2(c), 3(b) | #1 | Current sweeps 0 to ±300 µA (Fig. 1(c)); four-probe; Fig. 1(e) temperature series "throughout the whole superconducting regime" | Temperature of Fig. 1(c)-(d) not stated; number of sweeps; Ic extraction details |
| Polarity programmable by field history | Fig. 2(a)-(c); Fig. 3(a) | #1; #3 | Fig. 2 at 200 mK, field −50 to 50 mT, both sweep directions; Fig. 3(a) training at ±6 T, 705 µA excitation | Field step; remanent-field calibration; Fig. 2 sweep for #3 |
| Nonmonotonic hysteretic reversals, Bcf < 0 and Bcb > 0 (inverted relative to a simple FM proximity model) | Fig. 2(c), Fig. 4(b) | #1 shown; text says "our NbSe2/CrBr3 devices consistently exhibit" it | η peaks at 45.3% near −10 mT in the forward sweep | Number of devices; values of Bcf and Bcb |
| Layered ferrimagnetic CrBr3 sets the interfacial exchange field | Fig. 4(a)-(b), RMCD in SM | simulation (trilayer), RMCD in SM | | CrBr3 thickness; RMCD data not in main text |
| Cubic odd-in-q GL mechanism | Fig. 4(c)-(d), Eqs. 1-3 | theory | | Transport direction relative to crystal axis (θ) not stated |

Device counts: devices fabricated, measured, and showing the effect are not given. Devices #1 and #3 are shown; device #2 is never mentioned. Cooldowns not stated. Datasets: one field-sweep pair (device #1), one rectification pair (device #3), one temperature series (device #1).

## Entries matched, skipped, adapted

- Matched: diode-vortex-screening (diode family), fine-tuning-and-selection (always).
- Checks: the library has no checks for the diode family, so only the practice checks (report-counts, report-ranges, report-processing) were walked.
- Skipped: all zbp, quantization, nonlocal, island, shapiro, supercurrent, charge, chiral and kitaev entries (their signatures are zero-bias peaks, quantized conductance, Shapiro steps, field-enhanced supercurrent, fractional charge, chiral plateaus or Kitaev chains, none of which this paper reports). micromagnet-stray-field skipped: its signature is zero-bias peaks in quantum dots; the stray-field route to a diode (CrBr3 dipolar field plus Meissner screening) is judged under diode-vortex-screening, and its "stray field mapped or bounded" idea went into that row's suggested check and question 5. protocol-parameter-sensitivity skipped: no automated pass/fail protocol. local-probe-loophole skipped: no Majorana claim. field-enhanced-supercurrent-resonances skipped: the claim is not a supercurrent growing with field read as triplet pairing.
- Adapted: none. The paper is transport in a superconducting heterostructure, inside the library's diode family.

## Hold-out

No library source discusses 2608.19099. Hou et al. 2205.09276 (the diode-vortex-screening source) is cited by the paper as [19] but predates it; kept. No sources held out.

## Status decisions

- diode-vortex-screening: plain-film control marked "no" because the main text only points to the SM; field-following marked "part" (device #1 in Fig. 2; device #3 shown only after ±6 T training at zero field). The paper concludes against it ("cannot be explained by Meissner screening", abstract; "ruled out, as shown in SM", p. 4), but the field sweep alone does not separate it, because a hysteretic stray field from CrBr3 or a remanent magnet field can also give a history-dependent screening diode. Tested in part.
- outside, trapped vortex plus self-field: tests taken from the control in Golod and Krasnov's abstract (trapping and removing a vortex; changing bias configuration). Zero-field cooling shown for device #1 only (Fig. 1(d), p. 2), and a residual field during cooling could still trap flux. Paper does not name trapped vortices; Tested in part.
- outside, strain-induced diode: tests from Li et al. (B-odd versus B-even behavior of ΔIc) and Zhu et al. (even-in-B SDE without TRS breaking). Polarity reversal with magnetization shown for both devices presented (Fig. 2(c), Fig. 3(a)); field-even part never separated. The paper does not mention strain, so it cannot be "ruled out for the claim" under the skill's rule even though one test is shown for all evidence. Tested in part.
- fine-tuning-and-selection: count test "part" from the qualitative "devices consistently exhibit"; second device "part" (device #3 shown for rectification only). Tested in part.
- Checks: report-ranges marked "not done" because only the shown ranges appear; report-counts "partly" because of the qualitative consistency statement.

## Related work, how checked

All five: found with the arXiv API (export.arxiv.org, about 3 s between calls), abstract read from the API response, then the arxiv.org/abs page opened to confirm ID, title and first author. Abstract only for each; none of the pages mention 2608.19099.
- 2205.09276 Hou et al.: abstract.
- 2205.12196 Golod and Krasnov: abstract.
- 2509.23707 Li et al.: abstract.
- 2608.03072 Zhu et al. (posted 2026-08-04, before the paper under review): abstract.
- 2406.14417 Xiong et al. (the paper's ref. [26], matched by title): abstract.
Also seen in search, not listed: 2402.16264 (NbSe2 nanobridge SDE), 2609.09097 (Fe3GeTe2/NbSe2 junction-free SDE, later than this paper).

## Library gaps

- No checks for the diode family. Candidates: plain-film or bare-region control; calibrated zero of field after excursions; even/odd decomposition of ΔIc; contact swap; zero-field cooling.
- Trapped-vortex diode with memory (Golod and Krasnov, arXiv 2205.12196): field-free, history-programmable polarity in a conventional superconductor.
- Strain or pressure-induced field-free diode in NbSe2 (arXiv 2509.23707, 2608.03072).
- Remanent field of the superconducting magnet after high-field excursions, as a source of an apparent "field-free" effect: no source opened, so not added as a row; raised as question 5.

## Unsure

- Whether "as shown in SM [40]" should count as a shown test: I marked the plain-film control "no" since the SM was not available and the main text shows no such measurement; if the SM shows it, that row could move toward ruled out.
- Page numbers come from text page markers; quotes rejoin hyphenated line breaks and drop extraction spacing in "NbSe2 /CrBr3".
- The temperature for Fig. 1(c)-(d) is not stated in the text.
- Whether a second device shown for a different sub-claim (device #3, rectification only) counts as "part" for "a second device or dataset shown"; I chose part.

## Skill issues

- Step 7 and the template ask for the title from the arXiv abstract page; this run forbade opening it, so I used the paper text's title. The skill could allow the paper's own title page.
- The skill says to walk "the checks for the paper's family"; the diode family has none. It does not say whether to improvise family checks; I used the practice checks only and said so in "What this is".
- No rule for evidence the paper points to in an unavailable SM. The "can't tell, mark part" rule seems written for unclear figures; a pointer looks like "a sentence or citation alone", so I used "no". Clarify which applies.
- "Ruled out for the claim" requires the paper to conclude against the lookalike, which an outside lookalike the paper never mentions can never meet, even with a separating test shown for all evidence (the strain row). Worth stating explicitly.
- For checks, "partly" is defined by part of the evidence (one of three devices); it is unclear how to mark a check done qualitatively for all evidence (counts given as "consistently", shown ranges stated without full ranges). I used partly for the first and not done for the second.
- Step 7 says to write report files; this run's prompt overrides that and the report and notes are returned in the reply.
