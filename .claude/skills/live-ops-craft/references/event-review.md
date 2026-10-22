> Author: J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22. Part of `live-ops-craft`; built also from the owner's Riot transcripts (J018). The why: `live-ops-design` §4 L-16..L-23 and §7. Rules I point to and never copy: variants, cosmetics, theme niches and paid reveals `game-design/references/systems-economy.md` §8-§9; reward tiers `progression-design/references/reward-tiers.md`; event art `marketing-design` §4 M-15..M-23; paid random items and younger players `platform-policy` (it wins).

# Event briefs and the event review on named captures

Use this file for **event-scope work**: an event, a season beat, a theme, a variant line, a limited item, or a new world or zone. A plain fix or balance update uses only `process.md`. The brief lines for event-scope work are listed once, in `process.md` §3.

## 1. The craft-ask table (what each craft is asked for, and when)
Every row goes into the update brief (`process.md` §3) and reaches its craft through the lead's job recipe or a ticket inside the approved plan. I state what and why; the craft owns how. Every row carries the same three lines from the brief: the target experience, the promise sentence, the cohort. Columns: who · what I ask for · when (the stage where a change is cheapest) · the capture or file it is judged on.

| Craft | What I ask for | When | Judged on |
| --- | --- | --- | --- |
| game-designer | the play spec; the activity proven in the crudest playable form (plain Parts or a config build); the feedback stack (attempt cue on input, the big layer on the confirmed result); for a limited mode, where luck sits and a balance-pass list over every unit; hazard rules; any hunt or secret placed off the routes | right after the owner's pick, before any art brief | the grey-box verdict from the studio-operator's play captures; the spec |
| progression-designer | amounts, issuance, catch-up trace for the median late joiner; every event reward placed in the game's tier table; a new top-tier reward with the same rarity proof (re-simulated rate) | before ranking (feasibility), then before any reward moment is briefed | the tier table checks (`reward-tiers.md` §8); the late-join trace |
| art-director | the theme's niche against the nearest existing theme; the style levers kept; event rewards as one named theme family with a shared motif; the anchors-kept list per variant, and whether each is a new version (new palette) or the same subject in a new scene (base palette); reserved gameplay colours kept out of event decor; colourways re-checked for value; a top-tier style break proposed for the owner if wanted | concept round (before any production art) | the theme rough; variant vs base flat-key captures with the anchors listed; their palette and silhouette measures |
| environment-designer, level-design | event space or lobby dressing; the entrance visible in the first view after spawn or teleport; decor above the player band and off routes; for a new world or zone, the escape line and a first view that differs clearly from the last world (palette, shapes, theme) | after the grey-box verdict | first-view and busiest-moment captures at phone size; C-13 for a new world |
| vfx-designer, sound-designer | what players do re-themed (the action, the collect, the reward moments), sized by the tier rows; the game's signature sounds kept and event cues added to the shared library as data; routine pickups short and merged; every flash, shake or tint with its off path | after the tier rows, before build | their own review captures; the rejected-request capture |
| ui-ux-designer | the entrance pointer; the event HUD: a true timer in words, progress toward the event goal, exact counters; odds placement for any paid random item; the event frame's motif taken from the game's own icons or story | after the flow is agreed | HUD and shop captures at phone size |
| animator, modeler | variants and limited cosmetics that keep the anchors, proportions and contact points; premium items with at least the base's secondary motion and separable finishes | after the art director's anchors list | the art director's variant review |
| marketing | first, calendar rows and the fact sheet (`handoffs.md` §6); then the launched thing as the hero; one crop-safe, layered master that feeds the event kit (icon, thumbnails, listing, in-game banner); one brand property changed; every claim from the fact sheet | calendar and fact sheet after the pick; the event kit when the build is credible; again when live; teasers only for built scope | their image review lines (`marketing-craft/references/image-review.md`); the promise ledger |
| analyst | the measurement plan; an hourly read on the first day (rewards granted vs planned, completion of what the event asks) | before release | the plan file (`handoffs.md` §2) |
| builders (via the lead) | estimates; event timing and rewards as config and data (dormant until start); a tested disable path | before ranking, then after the pick | the estimate file; QA evidence |

A craft that is not built yet in the kit: write the row anyway and give it to the lead.

## 2. The capture set (asked for through the lead; the studio-operator takes it)
Name each capture in the brief so every craft knows what it will be judged on. Conditions for all: the game camera, the phone viewport the game profile names, the real build and config version, lighting and effects on.

| ID | Capture | Notes |
| --- | --- | --- |
| C-01 | first frame after spawn, and after any teleport into the event | as a new player and as a returning player |
| C-02 | the lobby or hub at the busiest expected moment (event start, the server's player cap) | one still |
| C-03 | the activity loop at its busiest moment | one still |
| C-04 | each reward moment: the most frequent event reward and the top tier | frame sequence at 30 fps; key frames only |
| C-05 | a request the server rejects (a purchase declined, a claim refused) | frame sequence; key frames only |
| C-06 | paid random reveal, lowest and highest tier (only if the event sells one) | the game designer's or UI designer's frame compare; I read their result |
| C-07 | each variant next to its base, flat key, same distance | the art director's capture; I read their anchor list |
| C-08 | the event HUD and shop | one still each |
| C-09 | C-03 in grayscale, with sound off and reduced motion on | one still |
| C-10 | after gameplay end, before claim end, as a returning player | one still |
| C-11 | the event logo and tile next to the last two events' | marketing's sheet |
| C-12 | a route walk past every hidden item | key frames at each item |
| C-13 | a new world or zone: its first view after spawn next to the last world's first view, same camera and viewport | two stills |

**Image budget.** Numbers first: the partners' measures in their hand-backs (tier checks, palette and silhouette measures, thumb checks, frame compares). I look at stills only for the key cases above: one still per still-capture; at most 4 key frames per sequence (the input frame, the first response, the result frame, the end of the celebration); more stills only for a line that fails. Feel at normal speed is not mine to judge from stills: the owner judges it on a playable preview at the gate.

## 3. The event review checklist (run before release; each line names its input and status)
Status per line: gate-verified, MCP-verified, owner-confirmed, not verified, or n/a with the reason (no paid reveal, no variant, no new world). A missing capture is asked for; until it arrives, the line is "not verified" and goes on the could-not-check list. A cold read means: I write what the stills show before I re-open the brief; when I can spawn a subagent, a fresh one gets only the stills.

| ID | What I look for | Input | Pass when | Fix owner |
| --- | --- | --- | --- | --- |
| E-01 | The promise reads | cold read of C-03 and C-04 | what players do and get matches the promise sentence | game-designer, art-director |
| E-02 | No look, sound or word promises what the activity does not do | C-02..C-04, C-08, the announcement draft | the mismatch list is empty, or each item is justified in the brief (a "rare" glow on a common drop, a scary theme on a calm loop) | the craft that made it |
| E-03 | The entrance is found | C-01 | the entrance or its pointer is in the first frame and is the frame's strongest focal point | environment-designer, ui-ux-designer |
| E-04 | The gameplay read comes first | C-02, C-03 | route, threats, own state and objective are named at a glance; no event decor or effect covers them | environment-designer, vfx-designer |
| E-05 | Reserved colours stay reserved | C-02, C-03; the art director's palette measure if they ran it | no enemy, danger or rarity hue on decoration | art-director |
| E-06 | Rarer looks bigger | C-04 key frames; the tier table | the top tier is clearly the biggest moment; the frequent reward is small and merged; no event celebration out-shouts the core track's top tier; the tier is named in words | vfx-designer, sound-designer, ui-ux-designer |
| E-07 | Only the confirmed outcome celebrates | C-05 key frames | no success layer, "+N", sound or celebration after a rejected request | game-designer, feature-builder |
| E-08 | Paid reveals are honest | C-06 result; the odds screen in C-08; the odds screen with the event boost active (if the event has one) | the partner's frame compare passed (one windup for every tier); odds visible before the buy button; a boost's numeric effect shown before purchase and the shown odds changed while it is active; the restricted-player path exists (`platform-policy` §A) | game-designer, ui-ux-designer |
| E-09 | Identity survives the variant | C-07; the art director's anchor list | every listed anchor present (at most one hidden by a pose); the new theme obvious; it reads as the same game | art-director |
| E-10 | One brand property changed | C-11 | same name pattern, font and lock-up; exactly one property differs | marketing |
| E-11 | The motif comes from the game | C-08, C-11 | the event frame or banner motif traces to an in-game icon or story element | ui-ux-designer, marketing |
| E-12 | Timer and progress tell the truth | C-08; the event config | the timer counts to the true end and the end is written in words in the player's local time; progress toward the goal is visible; counters match the server value | ui-ux-designer, feature-builder |
| E-13 | Every player can read it | C-09; each craft's off-path list | the event, its state and its end are still identified; every flash, shake or tint has an off path; the event is explained in the game, not only on Discord | ui-ux-designer, vfx-designer |
| E-14 | Returners get a way back | C-10, C-01 as a returning player | a clear next action; what happened to rewards and currency is shown | game-designer, ui-ux-designer |
| E-15 | Cosmetics cost no gameplay | the builders' data diff; the art director's footprint numbers | cosmetic rows change no stat; footprint inside its limit (`systems-economy.md` §8) | art-director, game-designer |
| E-16 | A limited mode is balanced on purpose | the game designer's balance-pass list; the analyst's plan | every unit covered; luck placement written; side or team win rates in the measurement plan | game-designer |
| E-17 | Secrets reward, never block | C-12 | no hidden item on a route or in the player band; none hurts a read | level-design, environment-designer |
| E-18 | Premium reads as premium | the art director's variant review | premium items keep at least the base's secondary motion, have separable finishes and read apart from standard at thumbnail size | art-director, animator |
| E-19 | The new world is an escape (new world or zone only) | C-13, by eye; the escape line in the brief; the art director's palette measure if they ran it | a cold read of the new still names a place clearly unlike the last world (palette, shapes and theme differ) and matches the escape line | environment-designer, art-director |

Close the review with the could-not-check list (line, missing input, the capture that would close it) and one honest weakness of the event.

## 4. Writing a review note
One problem per note: the line id, what the capture shows, the promise or rule it breaks, the evidence (capture id, frame), why it matters to the player, and the fix owner. The note says what is wrong and why, never how to build the fix. A conflict between two crafts' notes goes to the lead with the conflict stated; I never average two notes.

## 5. Worked example (illustrative; every value EXAMPLE ASSUMPTION)
A pet simulator rated Mild (Kids and Select can play). The owner picked "a Halloween event for lapsed players".
- **Concept round:** three one-pagers at equal finish, each with its scope fit: (A) a pumpkin hunt across the existing zones (fit: reuses the zones and the collect system), (B) a haunted mine built as a new zone (fit: builder rough 3 weeks against an approved 2), (C) atypical: a "ghost pet" parade where players' own pets glow for one night (fit: config and one effect). My pick: A, because returners need no new system, with C's glow kept as the top-tier reward. B did not fit the approved scope; C alone gave lapsed players nothing to do.
- **Brief lines:** target experience: discovery with friends. Promise: "Find the lost pumpkins in every zone with your friends; the rarest hatch ghost pets." Fans want: 14 of 52 sampled in-game authors (one window, one source) asked for "something to do with friends" (count file `sorts/counts-2026-10-20.md`). Niche: last year's Winter event was a solo collection; this one is a co-op hunt. Story: a friendly ghost scattered the pumpkins and the pets sniff them out (no iconic item changes, so no twist line). Tone shift: cute last run, spooky-but-friendly now. Reward family: ghost pets with one lantern motif. Anchors: each ghost pet keeps its base pet's ears, tail shape and size; only material and colour turn ghostly (a new version, new palette). New world or zone: n/a, no new zone (so E-19 is n/a). Policy: spooky-but-friendly keeps the game's Mild questionnaire answers (launch checklist L9); the ghost-pet egg is opened with pumpkins, which are earned only and never sold for Robux in any bundle, so it is not a paid random item (`platform-policy` rules §A).
- **Craft asks:** as in §1; the progression designer places "pumpkin found" at T1, "zone set complete" at T3, "ghost pet hatched" at T4 with a re-simulated rate.
- **Review findings:** E-03 failed: C-01 showed the event board behind the shop, so the first frame's strongest focal point was the shop sign (fix owner: environment-designer; the note says what is wrong: the entrance must be the strongest focal point of the first frame; where it goes is their call). E-06 failed: the C-04 key frames showed every pumpkin pickup playing the zone-complete fanfare (fix owner: sound-designer and vfx-designer; the note: pickups are T1 in the tier table and must stay below the T3 moment). E-09 not verified: the art director's flat-key capture of the ghost cat next to the base cat was missing; asked through the lead and listed on the could-not-check list until it arrives. E-08 and E-19 n/a, with the reasons above.
