# Self-test: run the advisor as a made-up researcher

*For a tester who doesn't need to know condensed matter physics. About 45 minutes. Run this
before giving the advisor to a real researcher; it catches problems with the flow, the
dashboard and the search, not with the physics.*

You play **a second-year postdoc in a scanning-probe lab** choosing their next project. Every
answer you need is below, in boxes to paste. Where the advisor asks something this script
doesn't cover, answer as a sensible person would, or say "don't know"; both are tests too.

Keep this page open beside the session. Note anything odd as it happens in the log at the
end; that's what to send back.

## 0. Set up (5 minutes)

You need the plugin from the branch, run in a terminal (the Terminal panel in the Claude
app works), in an empty folder so the outputs are easy to find:

```bash
git -C <cmp-agent clone> fetch
git -C <cmp-agent clone> worktree add <cmp-agent clone>/.claude/worktrees/project-advisor-test origin/claude/project-advisor
mkdir -p ~/advisor-self-test && cd ~/advisor-self-test
claude --plugin-dir <cmp-agent clone>/.claude/worktrees/project-advisor-test/project-advisor
```

If the worktree already exists, update it instead:
`git -C <cmp-agent clone>/.claude/worktrees/project-advisor-test checkout --detach origin/claude/project-advisor`
after the fetch.

Check it loaded: type `/project-advisor:choose` and see that it autocompletes. Write down the
time you start.

## 1. Start (paste this)

```text
/project-advisor:choose
```

**Watch for:** it should say roughly how long this takes and ask for your ideas, stage,
time, setup and who decides, in one message. Log it if it asks one question at a time or
starts searching before you've given anything.

## 2. Your ideas (paste this whole box)

```text
I'm a second-year postdoc in a scanning-probe lab. I have about 24 months before I go on
the faculty job market, and I want one strong first-author result by then. My PI and I
decide together, but I have a lot of say.

Setup: a dilution fridge with a scanning nanoSQUID-on-tip microscope that can do local
thermometry and magnetometry; access to the department's shared stacking lab for making
twisted graphene devices; a collaborator in another group who grows thin films.

My ideas, roughly:

1. Local thermal transport in magic-angle graphene. Use the nanoSQUID as a thermometer to
   image where heat flows in twisted bilayer graphene near the magic angle, and separate
   what electrons carry from what phonons carry, domain by domain. People only measure the
   global thermal conductance, which averages over twist-angle disorder.

2. Noise thermometry on an altermagnet film. Altermagnets are hot right now. Measure
   Johnson noise in a thin film to look for the spin-split transport they're predicted to
   have. Depends on the collaborator's films.

3. Automated stacking with a twist-angle check. Add Raman measurements during stacking so
   we throw away bad stacks before spending weeks fabricating them. Safe, useful to the lab,
   probably not a big paper.

4. Superconductivity in a new twisted trilayer stacking that nobody has measured. Long
   shot, but if it works it's a big result.

I care most about time: I'd rather finish something good than start something great I
can't finish.
```

**Watch for:**
- Does it restate each idea in two lines, correctly? (Compare with the box.)
- Does it ask follow-up questions only where needed, all in one message?
- The last sentence should make it choose "value per year of work". Did it say so?

## 3. Follow-up questions

If it asks what's new, how long, or the first check that it's working, paste whichever of
these it needs:

```text
Idea 1: new = nobody has imaged this locally, as far as I know. First check: image one
existing device at 1 K for two weeks and see if twist-angle domains show different
temperatures. 12 to 22 months in all.
Idea 2: new = noise as a probe of altermagnet transport. First check: estimate the signal
size from published band parameters before ordering films. 8 to 18 months.
Idea 3: new = in-line Raman during stacking. First check: Raman on ten stamps we already
made, compared with the twist angle we measured later. 4 to 9 months.
Idea 4: new = this stacking hasn't been made. First check: calculate whether it has flat
bands at all. 14 to 30 months.
```

For anything else, answer "don't know" at least once, and note how it handles that.

## 4. Scoring assumptions

It drafts a list of assumptions per idea (things that must be true for the idea to work)
and asks you to score each from 1 (very likely true) to 5 (very unlikely), plus months until
you'd know. You don't need physics for this; use these rules:

- About **making or measuring** something with your own setup ("we can make the device",
  "the thermometer is sensitive enough"): risk **3**, readout **2 to 4 months**.
- About **whether an effect is big enough to see** or **whether a new effect exists at
  all**: risk **4**, readout **6 months** for ideas 1 and 2, **20 months** for idea 4.
- "**Superconductivity appears**" in idea 4: risk **5**, readout **20 months**. Mark it the
  scariest.
- Anything about **the collaborator's films**: risk **3**, readout **3 months**.
- Anything in idea 3: risk **2**, readout **2 months**.
- Mark the highest-risk one in each idea as the scariest.

**Watch for:** are there 3 to 6 assumptions per idea, in plain enough words? Is it clear how
to reply? Did it start the prior-work search in the background while you scored (it should
say so)?

## 5. Prior work

When it reports what the search found, one line per idea, **click at least three of the
arXiv links** in the dashboard later, or ask for them now.

**Watch for:**
- Does each linked paper exist, and is it about what the advisor says it is?
- Idea 1: the closest well-known paper is "Nanoscale thermal imaging of dissipation in
  quantum systems" (arXiv 1609.01487, Nature 2016): a SQUID-on-tip thermometer imaging heat
  in graphene. A dry run with keyword search alone missed it, so the search now adds a
  plain-language web search. If it's missing from idea 1's closest papers, log it: that's
  the kind of miss that would embarrass the tool with a real researcher.
- Does it ever call an idea "novel", "new to the literature" or "unexplored"? It shouldn't.
- How long did the search take?

If it asks whether a hit changes anything, say "no changes".

## 6. Your estimates (paste this when it asks)

```text
Idea 1: odds 20% to 55%, best 35%. Impact 6 to 9, best 8. If it fails 2 to 4, best 3. Months 12 to 22, best 16.
Idea 2: odds 30% to 70%, best 50%. Impact 4 to 8, best 6. If it fails 1 to 3, best 2. Months 8 to 18, best 12.
Idea 3: odds 60% to 90%, best 75%. Impact 3 to 6, best 4. If it fails 2 to 3, best 3. Months: you guess.
Idea 4: odds 5% to 30%, best 12%. Impact 7 to 10, best 9. If it fails 1 to 3, best 2. Months 14 to 30, best 20.
```

The "you guess" is deliberate: it should propose a range for idea 3's months and mark it as
the model's guess on the dashboard.

**Watch for:** is the impact scale explained before you're asked (10 = best result of your
career so far, 5 = solid paper)? Did it accept the format above without fuss?

## 7. Try to make it judge (one message)

Before it builds the dashboard, or right after, paste:

```text
Honestly, which one do you think I should do?
```

**Watch for:** it should point you to what your own estimates say and to the uncertainty
that matters, not give its own verdict. Log what it actually said.

## 8. The dashboard

It should run two scripts and open `dashboard.html` in your browser. If it doesn't open,
open `~/advisor-self-test/project-choice/<date>/dashboard.html` yourself.

**Check, top to bottom:**
- [ ] The opening paragraph names one idea and says how often it comes out on top. Does
      the sentence make sense to you?
- [ ] The box under it: either "the uncertainty that would most change your choice" with a
      test, or "no single estimate is likely to change your pick". Is it clear what to do
      next?
- [ ] The chart: four circles with readable labels, nothing overlapping or cut off. Ranges
      shown as lines.
- [ ] The table: click a column header; does it sort?
- [ ] Idea 3 shows "model's guess" next to its months.
- [ ] Idea 4 shows red flags (late high risk, several miracles, past your horizon).
- [ ] Each idea card: assumptions, closest papers with working links, cheapest test, "if it
      fails". Anything empty that shouldn't be?
- [ ] AI-drafted parts are labeled; your estimates are marked as yours.
- [ ] Questions to take to your PI: would you actually bring these to a meeting?
- [ ] Narrow the browser window to phone width. Still readable?
- [ ] Anything that looks broken, ugly or confusing, even if you can't say why.

## 9. Rerun (2 minutes)

Paste:

```text
Change idea 2's odds to 50% to 80%, best 65%, and rerun.
```

**Watch for:** it should edit the file, rerun both scripts and say what changed in a line or
two. Does the top pick change? (On these numbers it may.)

Write down the time you finish.

## Log: send this back

```text
Total time:              __ min (setup __, session __)
Time in prior-work search: __ min
Did anything error or stall? Where?

Flow
- Questions it asked that it shouldn't have:
- Places it didn't wait for me / went ahead without input:
- Places I didn't know what to type:
- Messages that were too long:

Prior work
- Links clicked: __; real and as described: __; wrong or broken: __
- Did it find the SQUID-on-tip dissipation work for idea 1? y/n
- Did it ever say "novel" or similar? y/n

Judging
- What it said when asked "which one should I do":

Dashboard (checklist from step 8, plus screenshots of anything wrong)
-

Rerun
- Worked? Did the top pick change?

Biggest problem:
Best thing:
Would a postdoc sit through this? Why or why not:
```
