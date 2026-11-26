# Assumptions, risk and readout

Adapted from Anthropic's `scientific-problem-selection` skill, reference
`02-risk-assessment.md` and `07-problem-inversion.md`
(https://github.com/anthropics/knowledge-work-plugins/tree/main/bio-research/skills/scientific-problem-selection,
Apache-2.0), which follows Fischbach and Walsh, "Problem choice and decision trees in science
and engineering", Cell 2024. Changed for condensed matter and astronomy, shortened, and run
across several ideas at once.

## Two kinds of assumption

**About nature.** Facts that are or aren't true, and won't change while you work.
- The gap opens at a filling you can reach with your gate.
- The signal (thermal, magnetic, optical) is larger than your noise floor.
- The phase survives in a thin film, or at the twist-angle disorder you'll have.
- The source is bright enough at this wavelength to reach the signal-to-noise you need.

**About capability.** What you, your instruments and your collaborators can do. These can
change as methods improve.
- You can make the device (stack, twist angle, contacts) at a usable yield.
- The instrument keeps its sensitivity in the field, temperature or bandwidth needed.
- The material can be grown, or a collaborator will really send it.
- You'll get the telescope time, the beamtime, the fridge time.
- The analysis can separate the effect from the obvious artifact (contact resistance,
  heating, substrate, systematics in the calibration).

Questions that surface them: what must be true for this to work? What must the setup be able
to do? If it all works, how would a referee argue it's an artifact, and can you rule that
out? Will the result be interpretable?

## Scoring (the researcher does this)

- **Risk, 1 to 5.** 1 = very likely true (over 90%), 2 = likely, 3 = uncertain (40 to 70%),
  4 = unlikely, 5 = very unlikely (under 10%).
- **Readout, months.** How long until you'd know.
- Mark the scariest one.

## Red flags (decide.py checks these)

- **Late high risk.** Risk 4 or 5, reading out after more than 18 months. Fischbach and
  Walsh's rule of thumb: a risk-5 assumption three years out means pick another project.
- **Several miracles.** More than two assumptions at risk 4 or 5.
- **Past the horizon.** The high end of months exceeds the time the researcher has.

A good sign: the riskiest assumption reads out within six months. Then the project has an
early go or no-go.

## The cheapest test

For the scariest assumption, the quickest, crudest experiment or calculation that would
answer most of it. Examples: image one existing device before making new ones; estimate the
signal from published parameters before ordering samples; reanalyse archival data before
proposing for new time. Say which estimate it would change (usually odds of success) and
how many months it takes. Don't start with the easy, safe part; the risk doesn't go away.

## If it fails

What would the researcher still have? A method (a calibrated thermometer, a new fabrication
step), a dataset others would use, a smaller paper, a null result worth reporting. This is
"value if it fails" in the estimates. An idea with a good fallback can carry more risk.
