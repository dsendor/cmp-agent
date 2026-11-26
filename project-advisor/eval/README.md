# Blind test: the advisor against a plain prompt

*AI-drafted plan, 2026-11-22. Not run yet.*

**Question.** Does `/project-advisor:choose` help a researcher choose between their own ideas
more than Claude does with a plain "help me choose between these" prompt, for the time it
costs?

**Why a plain prompt is the bar.** In this repository the lookalike library lost to a plain
"Review this paper." prompt, 15% of referee concerns against 46% (`../../research/README.md`).
A structured tool has to earn its structure.

## Design in one paragraph

Each participant, an early-career experimentalist with three or more real ideas, dictates
them once. The plain prompt and the advisor both get that same dictation. `packet.py` turns
both outputs into two pages that look alike, labeled A and B at random. Two people rate
them: the participant, and a **blind second reader** who knows the ideas (their PI or a
labmate, if the participant agrees) and is never told which page came from which tool.
Factual checks (are the cited papers real, are they new to the participant) and a follow-up
in 3 to 6 months don't depend on blinding.

## What is and isn't blind

- **The second reader is blind.** They see only `A.html` and `B.html`, in the same layout,
  with tool names, labels and the chart removed (`packet.py`).
- **The participant is only partly blind.** They ran the advisor session, so they will
  recognize its content. They still rate pages A and B in the same layout, a day later,
  without the key. Treat their preference as a weaker signal than the second reader's.
- **The facts aren't a matter of opinion.** Whether a cited arXiv paper exists and is about
  what the output says, and whether the participant already knew it, can be checked.

## Participants

Two or three early-career experimentalists in condensed matter (astronomy welcome), each
with at least three ideas they are really choosing between in the next six months. This is
a pilot: with n of 3 it can find a clear loss or a clear win, not a small difference.

## Privacy

Unpublished ideas never leave the participant's machine and never enter this repository.
Only the filled rating forms come back, with ideas referred to as "idea 1, idea 2". The
public record (`results.md`, once there is one) has participant codes (P1, P2, P3), scores
and quotes the participant approves, and no idea content. No names.

## Steps for each participant (about 90 minutes in all, over two days)

**Day 1**

1. **Dictate** (10 min). The participant records or types their ideas as they'd tell a
   labmate, plus their stage, months available and setup, into `dictation.md`. Nothing else
   goes into either condition.
2. **Plain prompt** (5 min). In a fresh Claude Code session with no plugins enabled and the
   same model the advisor will use, paste the prompt in `baseline-prompt.md` followed by
   `dictation.md`. Answer any questions it asks, as briefly as you would in practice. Save
   the final answer as `baseline.md`. Note the minutes spent.
3. **Advisor** (under 60 min). In a fresh session with the plugin, run
   `/project-advisor:choose` and paste `dictation.md` as the ideas. Do the session as
   designed. Note the minutes spent. The output is in `project-choice/<date>/`.
4. **Make the packet** (1 min):
   `python3 <plugin>/eval/packet.py baseline.md project-choice/<date> packet/`.
   It writes `packet/A.html`, `packet/B.html` and `packet/key.json`. Move `key.json`
   somewhere you won't open it (or send it to the test organizer).

**Day 2**

5. **Participant rates** A and B with `rating-form.md` (15 min).
6. **Second reader rates** A and B with the same form, without the key (15 min). They should
   know the ideas from conversation, not from either page.
7. **Check the papers** (10 min). For every arXiv paper either page cites, the participant
   marks: exists and is described correctly / exists but described wrongly / doesn't exist;
   and: already knew it / new and relevant / new but irrelevant. `packet.py` lists them in
   `packet/papers.md`.
8. **Return** the forms, the minutes from steps 2 and 3, and the paper checks. Then open
   the key.

**3 to 6 months later:** `follow-up.md`.

## Measures, decided before the first run

| Measure | Source | Why |
|---|---|---|
| Which page sharpened your thinking more (A, B, same) | both raters | the main question |
| Which would you rather have had | both raters | overall preference |
| Did either change your ranking of the ideas | participant | an advisor that changes nothing has little value, unless the first ranking was right |
| Prior-work hits: real, correctly described, new and relevant | paper check | the part a plain prompt is most likely to invent |
| Minutes of the researcher's time | steps 2 and 3 | cost |
| Did they run the cheapest test, and what did they pick | follow-up | the only outcome that isn't an opinion |

## What would count as a result

Decided now, so the outcome can't move the bar:

- **The advisor earns more work** if the blind second readers prefer it for at least two of
  three participants, it cites at least one real, new, relevant paper per participant, it
  cites no paper that doesn't exist, and the session takes under 60 minutes.
- **Stop and simplify** if second readers prefer the plain prompt for two of three, or the
  advisor cites a paper that doesn't exist. Then try the plain prompt plus only the arXiv
  search and the value-of-information step, and test again.
- **Anything in between** is a draw: look at the comments, change one thing, run one more
  participant.

## Files

| | |
|---|---|
| `baseline-prompt.md` | The plain prompt, exactly as pasted |
| `rating-form.md` | The form both raters fill |
| `follow-up.md` | The 3 to 6 month questions |
| `packet.py` | Makes the two look-alike pages, the key and the paper list |
