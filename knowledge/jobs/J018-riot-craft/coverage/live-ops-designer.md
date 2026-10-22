---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2); repair round 1 (stage 3 review rev1)
supersedes: []
---
> Author: J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22

# Coverage: live-ops-designer (J018 stage 2, wave 3)

Books rebuilt (old state: `df13ff4`): `.agents/roles/live-ops-designer.md` (body only; frontmatter byte-identical to df13ff4, checked by script), `.agents/skills/live-ops-design/` (SKILL.md; references `cadence-content.md`, `events-offers-rules.md`, `evidence-feedback.md`, `measurement-health.md`; `cases.md` unchanged), `.agents/skills/live-ops-craft/` (SKILL.md; references `process.md`, `handoffs.md`, `feedback-ops.md`; new `event-review.md`; `evals/` untouched).
SKILL.md lines: live-ops-design 120, live-ops-craft 77 (both ≤ 500). Descriptions: live-ops-design unchanged (351 characters), live-ops-craft 390. All book files written LF (5 reference files were CRLF in the working tree before; normalized).
Where the self-review lives: `live-ops-design` SKILL §6 (decision-level lines, each with its input) and §7 (core principles, each with its check and input); `live-ops-craft` SKILL §6 (document and process lines, each with its input); the event review checklist `live-ops-craft/references/event-review.md` §3 E-01..E-18 (each line names its input, pass condition and fix owner), run on the capture set of §2. The role file's "Before you hand back" runs all of them. Compaction: `live-ops-design` §1-§6 end at 17.4 KB, §7 follows; §1 of both skills and the role file say to re-read §4 and §7 after a compaction. `live-ops-craft` SKILL is 11.6 KB in total.

What the agent now owns that it did not (V8): the event concept round (2-3 premise one-pagers at equal finish, pick with reasons, owner gate that freezes theme and scope); the brief lines every event, theme or variant brief carries (target experience, promise, what fans want with its count file, niche, story and twist lines, tone shift, reward family, anchors-kept list, tier rows); the craft-ask table (what each craft is asked for, when, judged on which capture); the named capture set C-01..C-12 with an image budget; the event review E-01..E-18; promise, tier, identity and keep / change rows in the post-update review; the count tool's known false readings. No art, VFX, sound, UI or animation craft advice was added: the books say what each craft is asked for and how the result is checked, and point to the partner books for the rules (game-design §8-§9, reward-tiers, marketing M-15..M-23, platform-policy).

Docs read for the new steps (all in the local mirror): `production/game-design/liveops-planning.md` (lines 13-75; the start of an event, local or game-wide, internal communication, hourly same-day data), `liveops-essentials.md` (lines 20-79), `content-updates.md` (lines 34, 51-60, 96-109; simple colour variants as recurring content). No [unverified] engine claim was added.

Legend for "landed in": `design` = `.agents/skills/live-ops-design/`, `craft` = `.agents/skills/live-ops-craft/`, `role` = `.agents/roles/live-ops-designer.md`, `ER` = `craft/references/event-review.md`. "principle N" = design SKILL §7 row N. "self-check D" = design SKILL §6; "self-check C" = craft SKILL §6.

### a. Findings tagged live-ops-designer (36) and untagged findings used (25)

| ID | Title | Landed in (file § section) | As | Or rejected: reason |
| --- | --- | --- | --- | --- |
| CD-04 | Variants hold the identity anchors and change the rest | design SKILL §4 L-17; craft/references/process.md §3 (anchors-kept list); ER §1 art-director and animator/modeler rows; ER §3 E-09; handoffs.md §9; principle 11 | standard; step (brief line); self-review check (E-09 on C-07 + the art director's anchor list; self-check C brief line) | |
| CD-13 | Twist the tone within bounds; darker still keeps the appeal | process.md §3 (tone shift and its limit; a darker tone re-checks the maturity answers); design L-17; ER §5 example (Mild answers kept) | step; self-review check (self-check C brief line: tone shift against the last run) | |
| CD-14 | Keep the cool core, swap one iconic item, justify it by lore | process.md §3 ("keep core X, swap Y for Z because of W"); handoffs.md §9 refs (twist line) | step (brief line); self-review check (self-check C: twist line when an iconic item changes) | |
| CR-03 | Solve the problem behind the note; separate goals from tactics | design SKILL §3 step 2 (request → problem); craft/references/feedback-ops.md §3 step 4 (requests tagged with their problem); ER §4 (notes say what and why, never how); role Work method 5; principle 16 | step; standard; self-review check (self-check D plan line: each request restated as its problem) | |
| CR-15 | Start from the player's pain points | design SKILL §3 step 2; design/references/evidence-feedback.md §5 (pain points from the current build); craft SKILL §3 step 4 (capture walk through the lead) | step; self-review check (self-check D plan line: each pain point names where it was observed) | |
| GD-04 | Name the target experience, not "fun" | design SKILL §1 q3, §3 step 3, §4 L-03; process.md §3 field; ER §1 (every row carries it); handoffs.md §4 fixed; role intro, Work method 1 and 5; principle 13 | standard; step; self-review check (self-check D plan line; self-check C brief line) | |
| GD-08 | Art turns rules and numbers into a fantasy players build around | process.md §3 (reward family, in the one list of brief lines); ER §1 art-director row (event rewards as one named theme family with a shared motif) | step (brief line); hand-off ask; self-review check (self-check C: every `process.md` §3 brief line filled or n/a, the reward family included; repair round 1) | partial: the family's look is the art director's; my check is the brief line |
| GD-14 | Place luck and skill on purpose | design L-23; ER §1 game-designer row; ER §3 E-16; handoffs.md §4 deliver | standard; hand-off ask; self-review check (E-16 on the game designer's file) | |
| GD-16 | Cosmetics never change the gameplay read or cost gameplay | ER §3 E-15; design L-22 (without touching balance); cadence-content.md §4 variants paragraph (changes no stat; pointer to game-design §8) | self-review check (E-15 on the builders' data diff and the art director's footprint numbers) | the footprint and silhouette measures belong to the art director and game designer (`game-design/references/systems-economy.md` §8); I read their numbers |
| GD-17 | Cosmetics refresh repeated play without changing balance | design L-22; cadence-content.md §4 "Variants and colourways"; E-15 | standard; self-review check (E-15) | |
| GD-19 | A mode change re-checks the whole roster | design L-23; ER §1 game-designer row; handoffs.md §4 deliver (balance-pass list); E-16 | standard; hand-off ask; self-review check (E-16) | |
| GD-20 | Choose themes from data; combine proven themes and tune the maturity | design L-20; process.md §2 item 10; evidence-feedback.md §4 item 7 | standard; step; self-review check (self-check C brief line: what fans want with its count file) | |
| GD-27 | Neither side takes neutral space too easily | design L-23 (side or team win rates measured after); E-16 (in the measurement plan) | standard; self-review check (E-16) | partial: spawn-to-neutral timing is level design's; my side is the live measure with the analyst |
| GD-32 | Hide small secrets that reward discovery | ER §1 game-designer row (hunts and secrets off the routes); ER §2 C-12; ER §3 E-17 | hand-off ask; self-review check (E-17 on C-12) | the "tie a secret to a release as a teaser" part is not written as a rule: a teaser is marketing's channel decision |
| GD-33 | A map is never done; new worlds are an escape | design L-22; cadence-content.md §4 "Worlds are revisited"; process.md §3 (new world or zone: escape line and how it differs from the last world); ER top (event-scope work includes a new world or zone), ER §1 environment row, ER §2 C-13, ER §3 E-19; process.md §6 keep / change row (revisit rows with evidence); principle 18 | standard; step (brief line); self-review check (E-19 on C-13; self-check C brief line; self-check C post-update line for the revisit rows) | |
| GD-35 | Paid random reveals are honest | design L-19 (pointer to game-design §9 and platform-policy); ER §2 C-06; ER §3 E-08 | standard (pointer); self-review check (E-08 on the partner's frame compare and C-08) | the frame compare itself is the game designer's / UI designer's measure; V4 diff in table d |
| LC-23 | Iterate colour globally; colourways are the same object | cadence-content.md §4 "Variants and colourways" (art director re-checks value); ER §1 art-director row; design L-22 | standard; hand-off ask | the colourway value check is the art director's (`art-review`); I check that it was run (E-09 input) |
| PP-32 | One key art feeds a whole asset kit; deliver switchable layers | handoffs.md §6 rules and deliver (event kit from one master); ER §1 marketing row | hand-off ask | the crop checks are marketing's (`marketing-craft/references/image-review.md`); pointed to, not copied |
| PP-33 | The icon and thumbnail are the box art: highest effort, tested at grid size | ER §1 marketing row (judged on their image review lines); ER §3 E-10 input C-11 (their sheet) | hand-off ask | the tile-size test (`thumb_check.py`) is marketing's measure (V13: point, never copy) |
| PI-02 | Gates freeze decisions: rough, approved direction, materials, polish | design SKILL §3 step 6, §4 L-21; craft SKILL §3 steps 7 and 8a; process.md §1 row 9; principle 15 | step; standard; self-review check (self-check C concept-round line) | |
| PI-14 | "It would be cooler" is new scope: log it | design SKILL §3 step 6, L-21; role Work method 6; process.md §7 pointer row; principle 6 | standard; step; self-review check (principle 6 check: additions after the pick are tickets with a cost) | |
| RI-04 | In marketing art, the launched thing is the hero | handoffs.md §6 rules; ER §1 marketing row | hand-off ask | the image check is marketing's (M-15) |
| RI-23 | Bring in one unexpected element from outside the genre | design SKILL §3 step 3; process.md §2 item 9; principle 14; ER §5 example (option C) | step; self-review check (self-check D plan line: one atypical option) | |
| RI-27 | Design a variant through a narrative lens | process.md §3 (story line); handoffs.md §9 refs | step (brief line); self-review check (self-check C: story line) | |
| SD-21 | Every weapon and the whole game get a signature sound | ER §1 vfx/sound row (the game's signature sounds kept) | hand-off ask | the listening check is the sound designer's |
| SD-30 | Keep a library of building blocks; cues are data | ER §1 vfx/sound row (event cues added to the shared library as data); design principle 17 (rewards and timing as data) | hand-off ask | |
| SI-05 | Make it for a specific audience, and give fans what they want | design L-20; evidence-feedback.md §4 item 7 (what fans want, at its strongest, with counts) | standard; step; self-review check (self-check C brief line) | |
| SI-11 | An update keeps the kernel and trims what is dated | process.md §6 keep / change row (what the next run keeps); principle 12 | standard; self-review check (self-check C post-update line) | the remake rule for a character lives in `game-design/references/systems-economy.md` §8 (pointed to by L-17) |
| SI-12 | Each theme needs its own niche | design L-17, §3 step 3; process.md §2 item 10 and §3; ER §1 art-director row; handoffs.md §9 | standard; step; self-review check (self-check C brief line: niche against the nearest existing theme) | |
| SI-13 | Refresh a tone by pushing to the extreme, then pulling back to the brand | craft SKILL §3 step 8a (extreme option and brand option for a recurring line); process.md §3 (tone shift against the last run); principle 12 | step; self-review check (self-check C brief line: tone shift) | its roblox_fit text-filter line not landed (V4: proposal row 6) |
| SI-14 | Names and logos: keep the brand pattern, change one thing | design L-17; handoffs.md §6 rules; ER §3 E-10; principle 7 | standard; self-review check (E-10 on C-11) | |
| SI-15 | Draw graphic motifs from the game's own UI and story | ER §1 ui-ux row; ER §3 E-11 | hand-off ask; self-review check (E-11 on C-08, C-11) | |
| SI-18 | A variant changes the palette; the same character in a new scene keeps it | process.md §3 (new version or same subject in a new scene); ER §1 art-director row | step (brief line); hand-off ask; self-review check (self-check C: every `process.md` §3 brief line; repair round 1) | the palette measure is the art director's |
| SI-19 | A cohesive set, with a documented break for the top tier | design L-18; ER §1 art-director row; handoffs.md §9 rules | standard; hand-off ask | |
| SI-20 | Premium tiers get separable finishes | design L-18; ER §1 animator/modeler row; ER §3 E-18 | standard; self-review check (E-18 on the art director's review) | |
| WT-24 | Secondary motion adds perceived value | design L-18; ER §1 animator/modeler row; ER §3 E-18 | standard; self-review check (E-18) | |
| GD-02 (untagged) | Every action gets immediate feedback; reached goals get a short celebration | principle 8 (celebration lengths from the game designer's feedback stack); ER §3 E-06 | core principle; self-review check (E-06) | |
| GD-07 (untagged) | Art and mechanics must promise the same thing | design L-16; events-offers-rules.md §1 "The promise"; ER §3 E-01, E-02 | standard; self-review check (E-01 cold read; E-02 mismatch list) | |
| GD-10 (untagged) | Make progress toward the goal visible | ER §1 ui-ux row; ER §3 E-12 | hand-off ask; self-review check (E-12 on C-08) | |
| GD-11 (untagged) | Build a climactic arc toward the resolution | principle 8 (rising beats and a finale in the calendar) | core principle | |
| GD-15 (untagged) | Prove the fun with the crudest prototype before art | design L-21; craft SKILL §3 step 8c; ER §1 game-designer row; handoffs.md §4 rules; principle 4 | standard; step; self-review check (self-check C: dated grey-box verdict before the first production art brief) | |
| GD-34 (untagged) | Feedback follows the real outcome | design L-19; handoffs.md §4 rules and C2; ER §2 C-05; ER §3 E-07; principle 19 | standard; self-review check (E-07 on C-05 key frames) | |
| CD-15 (untagged) | Re-theme the abilities, not only the costume | design L-16; ER §1 vfx/sound row | standard; hand-off ask | |
| CC-01 (untagged) | One target experience, signed by every craft | design L-16; ER §1 (every row carries the target experience and the promise) | standard; step | |
| CC-05 (untagged) | Share strong motifs across crafts | ER §1 ui-ux row and E-11 (the event motif from the game's own UI or story, reused by UI and marketing) | hand-off ask; self-review check (E-11) | |
| VH-02 (untagged) | Rank loudness across a set: if everything is loud, nothing is | design L-18; ER §3 E-06; principle 3 | standard; self-review check (E-06 on C-04 key frames and the tier table) | |
| VR-24 (untagged) | Frequent effects are shorter, quieter, merged and capped | ER §1 vfx/sound row (routine pickups short and merged); E-06 | hand-off ask; self-review check (E-06) | the caps and merge windows are the VFX and sound designers' numbers |
| WL-07 (untagged) | The first view tells where you are and what to do | design L-08; events-offers-rules.md §1 "The start"; ER §2 C-01; ER §3 E-03 | standard; self-review check (E-03 on C-01) | |
| LC-01 (untagged) | Reserve the gameplay colours | ER §1 art-director row; ER §3 E-05; principle 1 example | hand-off ask; self-review check (E-05 by eye; the art director's palette measure when run) | the palette measure is the art director's |
| UI-19 (untagged) | Counters tell the truth | ER §3 E-12 | self-review check (E-12) | |
| VR-23 (untagged) | Every intense channel has an off path | ER §1 vfx/sound row; ER §3 E-13; principle 20 | hand-off ask; self-review check (E-13 on C-09 and each craft's off-path list) | |
| CR-17 (untagged) | Say what each input can prove; end with a could-not-check list | craft SKILL §4 K-10, §3 step 9 check; ER §3 (status per line, could-not-check list) | standard; self-review check (self-check C event review line) | |
| CR-07 (untagged) | No grand reveals: show early and often | craft SKILL §3 step 8c (check-ins at the stages the table names) | step | |
| CR-06 (untagged) | Notes are direct; conflicts go up | ER §4; role "Working with other agents" | step | |
| CR-13 (untagged) | Close with an honest recap | ER §3 close (one honest weakness); role Hand-back | step; self-review check (role "Before you hand back") | |
| RI-02 (untagged) | Show options at equal, low finish | craft SKILL §3 step 8a | step; self-review check (self-check C concept-round line) | |
| RI-19 (untagged) | Present options with your pick and the reasons | craft SKILL §3 step 8a; principle 14 | step; self-review check (self-check C: pick recorded with a reason per rejected option) | |
| RI-21 (untagged) | The first output is a warm-up; reject the typical idea | process.md §2 item 9 | step | |
| PI-01 (untagged) | The cheapest stage goes first | design L-21 | standard | |
| PI-03 (untagged) | Closing doors: never reopen | principle 15; process.md §6 closed-directions row | core principle; step | |
| PI-12 (untagged) | Know when it is done: written stop criteria | process.md §3 field (stop criteria and revisit trigger); principle 18 | step; core principle | |

Untagged findings read and not used, for the groups closest to my work: GD-13 (consistent tells: game designer), GD-23 to GD-31 (maps as gameplay: level design and game designer; my side is the revisit row of GD-33), VR-19 to VR-22 and VR-26 (per-viewer effects, danger areas, camera punches, hit-stop, pulse rates: VFX craft; my side is asking for the off paths, E-13), UI-17 and UI-18 (motion durations, error messages: UI craft), WL-29 and WL-30 (route metrics, level review: level design), SD-01 to SD-29 except SD-21 (sound craft), CF and VC topics (image craft: marketing and the art director own them; I read their measures), SS and EX topics (shape and exaggeration: art crafts; my side is the anchors list).

### b. Universal principles

| UP-ID | Applies (yes/no + reason) | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: event decoration, effects and banners must not hide the play read | design §7 row 1 (check E-04) |
| UP-02 | yes (not in the master's list for this role, but every event is judged in the real build at phone size): the event review runs on named captures | design §7 row 2 (check: ER §2 capture set; "not verified" without one) |
| UP-03 | yes (master's "design: celebrations, rewards and threats are tiered so the rare and important feel bigger"): event rewards in the tier table | design §7 row 3 (L-18, E-06) |
| UP-04 | yes: premise, activity and calendar proven before reward lists, art and announcements | design §7 row 4 (grey-box verdict before the first production art brief) |
| UP-05 | no: shape and silhouette are art-craft execution; my side is the anchors-kept list (row 11) and the craft asks | named in the §7 lead-in |
| UP-06 | yes: one event, one promise, the fewest new systems | design §7 row 6 |
| UP-07 | yes: reserved colours, sounds, brand pattern kept; one brand property changes | design §7 row 7 (E-05, E-10) |
| UP-08 | yes (design line: "tension rises toward the climax; celebrations are short"): the event calendar as a story with rising beats and an honest end | design §7 row 8 |
| UP-09 | no: pushing forms, poses and sound past real is craft execution; nothing in a live-ops plan or brief is "pushed" | named in the §7 lead-in |
| UP-10 | yes: the event premise drives every craft choice | design §7 row 10 (E-01 cold read) |
| UP-11 | yes: variants and limited items keep identity and one style | design §7 row 11 (E-09) |
| UP-12 | yes: a recurring event keeps its anchors and changes one named thing per run | design §7 row 12 |
| UP-13 | yes: hypothesis, target experience, promise and constraints before any option | design §7 row 13 |
| UP-14 | yes: evidence first, options differ in mechanism, one atypical, a reasoned pick | design §7 row 14 |
| UP-15 | yes: owner gates freeze theme and scope; closed directions stay closed | design §7 row 15 |
| UP-16 | yes: review notes name the promise or problem, evidence and fix owner | design §7 row 16 (ER §4) |
| UP-17 | yes: briefs give each craft what it needs, at its stage; timing and rewards as data | design §7 row 17 |
| UP-18 | yes: each update closes with stop criteria and a revisit trigger | design §7 row 18 |
| UP-19 | yes: no celebration before the server confirms; paid reveals honest; announcements claim only what is live | design §7 row 19 (E-07, E-08) |
| UP-20 | yes (not in the master's list for this role, but event state, timer and end must read without colour or sound, and never only on Discord) | design §7 row 20 (E-13) |

No row contradicts the master: every check is the master's general check restated for an event (captures at the game camera on a phone viewport; rare bigger; rejected request shows no success layer; grayscale, sound off, reduced motion).

### c. Old book changes (old text at `df13ff4`)

| Old text (file:line at df13ff4) | Kept / sharpened / replaced by / moved / removed | Why |
| --- | --- | --- |
| design SKILL.md:16 "What is the smallest change that could remove it, and what does it cost..." | sharpened (design §1 q3): adds the target experience | an update without a named experience lets each craft push a different kind of fun |
| design SKILL.md:20 "How to run the cycle..." | kept, plus the compaction line | V7 |
| design SKILL.md:27, :33 (Read-this-file rows) | sharpened (what fans want; event art standards) and 3 rows added (event-review, game-design §8-§9, reward-tiers) | pointers to the partner rules instead of copies (V6) |
| design SKILL.md:39 step 2 Diagnose | sharpened: pain points with their observation; requests restated as problems | a change with no observed pain point is a restyle |
| design SKILL.md:40 step 3 Generate options | sharpened: target experience, options differ in mechanism, cheapest and atypical, promise / fans / niche for events | options that differ only in packaging give the owner no real choice |
| design SKILL.md:41 step 4 Estimate | sharpened: the progression designer also gives the tier each reward would hold | rarer must feel bigger from the first plan |
| design SKILL.md:43 step 6 Owner decides | sharpened: the decision freezes cohort, experience and scope; the concept round freezes premise, promise and theme; "cooler" is new scope | gates freeze decisions |
| design SKILL.md:44 step 7 "After release, decide again" | moved to step 8 and sharpened (did the look, sound and wording keep the promise); new step 7 "Brief, then review the build against the promise" | the brief and the event review were missing as decision steps |
| design SKILL.md:47 table header "Evidence" | sharpened to "Evidence or why" | new rows carry a reason, not a citation |
| design SKILL.md:51 L-03 | sharpened: names the target experience too | as above |
| design SKILL.md:56 L-08 | sharpened: a designed start and an entrance visible where players arrive (Roblox planning page, V) | the start is the first thing players meet |
| design SKILL.md:63 L-15 | sharpened: also whether players got what the look, sound and announcement promised | the post-release decision missed the promise |
| design SKILL.md:71 rules line "Rewards and amounts come from..." | sharpened: the look, sound and UI come from their crafts; one new rule line (named captures decide) | what and why, never how |
| design SKILL.md:73-79 §6 | kept; two lines added (plan file; pointer to craft §6) | each line names its input (V1) |
| craft SKILL.md:3 description | sharpened (event briefs, event review); 390 characters | the new work must trigger the skill |
| craft SKILL.md:11, :13 §1 | sharpened (what experience; compaction line) | V7 |
| craft SKILL.md:19-20 Read-this-file rows | sharpened; event-review row added | |
| craft SKILL.md:28 log line | sharpened (gates, captures) | the log must show the gates and the captures |
| craft SKILL.md:30 step 2 | sharpened: the known false readings checked by eye before a count drives a decision | V14 |
| craft SKILL.md:32 step 4 | sharpened: pain points from a capture walk or funnel; target experience; cheapest and atypical | |
| craft SKILL.md:35 step 7 | sharpened: the pick freezes cohort, experience and scope | |
| craft SKILL.md:36 step 8 "Brief" | replaced by step 8 (a) concept round, (b) brief + craft-ask table, (c) check-ins; image budget stated | cheap stages first; each craft asked at the stage where change is cheapest |
| craft SKILL.md:37 step 9 Readiness | sharpened: the event review E-01..E-18 on named captures | events were released without a capture review of the whole |
| craft SKILL.md:38 step 10 | sharpened: the analyst's hourly first-day read (Roblox planning page) | catch over-granting early |
| craft SKILL.md:39 step 11 | sharpened: the promise held? keep / change line | |
| craft SKILL.md:42 table header "Evidence" | sharpened to "Evidence or why"; K-09, K-10 added | |
| craft SKILL.md:62-63 §6 first two lines | sharpened (gates and captures in the log; false readings read by eye); four lines added | V1, V5 |
| craft process.md:18-19 §1 rows 9-10 | sharpened: concept round and craft-ask table; event review on captures | |
| craft process.md:46 §3 "Fields (LP:454-460)" | sharpened: target experience, stop criteria and revisit trigger; event, theme and variant brief lines added after it | |
| craft process.md §7 (109 rows end) | kept; one pointer row added (no copied rules) | V6 |
| craft handoffs.md:15 engineering row | sharpened: event timing and rewards as config and data | |
| craft handoffs.md:76, :107, :170 deliver lines | sharpened (tier rows; grey-box verdict and feedback stack; the event kit list) | |
| craft feedback-ops.md:33 step 4 Codebook | sharpened: the promise themes and request tagging | the post-update review needs these themes counted |
| design cadence-content.md:52 Items row "How it fails" | sharpened: a variant that loses its anchors; a premium item that reads like the standard one | |
| role body (lines 12-57 at df13ff4) | rebuilt: intro (bar), Read first (compaction re-read, partner rules on demand), Work method (steps 5-7 new; old 5-6 kept as 8-9), new "What you ask partners for, and when", new "Before you hand back"; the old first bullet of "Working with other agents" (role:40) moved into the partner table with its content kept (marketing writes the voice, the owner publishes; architect, feature-builder, quick-builder routing); role:42 sharpened (name the capture: camera, viewport) | the role file now says how the agent works, what it checks and what it asks partners for and when |

Nothing was removed as wrong: no old rule contradicted the material.

### d. Command runs (V3), the V4 diff, proposals from other roles (V11) and the V5 pass

Sample: a synthetic event feedback file in the real input form (`items/*.jsonl` lines as `feedback-ops.md` §2 defines, written by script, LF): 19 items over 4 sources (in-game, Discord with one loud author, Roblox reviews rows with `anon-` keys, one urgent support item), an event start at 2026-10-24T16:00Z inside the window, one item exactly at the window end and one exactly at the start. Scratch folder: the session scratchpad `live-ops-designer/`.

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| R1 | `python tools/liveops/feedback_count.py validate <items.jsonl>` | 19 good lines | exit 0, "19 good item(s), 0 rejected line(s)" |
| R2 | `validate` on the good file plus a bad file (local time without `Z`, `themes` as a string, a duplicate `item_id`) | bad line | exit 1; "REJECTED <file>:1: occurred_at_utc must be an ISO 8601 time ending in Z"; one reason per rejected line (fix and re-run until clean) |
| R3 | `count <items> --start 2026-10-21 --end 2026-10-28 --out <counts.md>` | full window | wrote the file; hand-checked every row: in-game 7 items / 6 authors (the item at the end excluded, the item at the start included); `event.entrance-hard-to-find` 3/6; `event.promise-mismatch` 2/6 with 3 messages (one author twice) and 2/2 in reviews (anon rows: each counted as one author); Discord `event.final-reward-too-long` 2/3, 7 messages, flag "one loud author: 6 of 7"; urgent `sp-01` listed; overlap "unknown". All correct |
| R4 | two `count` runs split at the event start (`--end 2026-10-24T16:00:00Z`, then `--start 2026-10-24T16:00:00Z`) | split window | before: entrance 2/2; after: entrance 1/4, promise 2/4 (3 messages). Hand-checked: correct |
| R5 | `count` on an edge file: one author with 4 of 4 messages on a theme; the same theme spelled `event.pvp-wanted` and `event.pvp_wanted` | edge cases | no loud flag (threshold needs at least 5 messages); two rows with split counts and no warning. Wrong numbers with no error, now in `feedback-ops.md` §4 known false readings, plus a tool proposal (proposals row 5) |
| R6 (repair 1) | `validate` then `count dateonly.jsonl --start 2026-10-21 --end 2026-10-27`, then `--end 2026-10-28`, then `--end 2026-11-04` | items on Oct 21, 25, 27 15:00Z, 27 18:00Z, 28 09:00Z (a week written "Oct 21-27"; the file also holds the next week) | validate exit 0. `--end 2026-10-27`: entrance 1/2, promise 1/2: the whole of Oct 27 dropped, no error. `--end 2026-10-28`: entrance 2/4, promise 2/4 (correct). `--end 2026-11-04` (the old book's "one window past"): entrance 3/5: the next week's item counted, no error. Both now in `feedback-ops.md` §4 (end kept at the boundary; date-only end is 00:00Z) and next to the command in §3 step 7 |
| R7 (repair 1) | `count e3.jsonl --start 2026-10-21 --end 2026-10-28` | the eval E3 shape: 60 Discord messages on `veterans.no-goals`, 52 from 4 authors (13 each), 8 from 8 others | the theme row read 12 / 12 authors, 100.0 %, 60 messages, with an empty flag cell (no author has half). Wrong reading with no error: now a §4 row (messages per author above about 3, a starting value, then the per-author spread read by eye on the raw items) and proposals row 5 (e) |
| R8 (repair 1) | `validate` then `count dup.jsonl ...` | 3 real Discord messages exported twice in overlapping exports; the 2 repeats hand-turned into items with new ids (`y1`, `y2`) | validate exit 0 (no duplicate id); theme row 2 / 2 with 5 messages (real 3); top author 4 of 5 (real 2 of 3). Now a §4 row and the §1 rule (take `item_id` from the export's own message or row id) |
| R9 (repair 1) | the scripted V5 pass below | coverage table a after the repair | every E, C, L and principle id named in table a exists in the books; rows without a self-review line are the partner-measure rows (reason in their last column) and the untagged step or standard rows |

What makes it give a wrong number with no error (asked per V3, written next to the command in `feedback-ops.md` §4 with the eye check): a local time written with `Z`; an item exactly at `--end`; split theme spellings; `anon-` rows (one author each); renamed Discord users without ids; one author below the flag threshold; untagged items in the denominator. The tool's silent thresholds (loud flag at ≥ 5 messages and ≥ half; end exclusive) are written next to the command (V12). The count is labelled a screening aid there (V14). No other command or tool mode is named by a check in the books: the event review reads partner measures from their hand-backs and points to them (V13); the role's `context_packet.py` call is unchanged.

**V4 diff** (`platform-policy/references/rules.md`, read 2026-10-22): design L-19 and ER E-08 (odds before the buy button, a boost's numeric effect shown before purchase and the shown odds changed while it is active (added in repair round 1; before that only launch checklist L3 carried it), the restricted-player path, one windup) match §A rows 2, 5, 7 and the game designer's §9; the worked example's egg is opened with earned-only pumpkins, which §A row 1 does not count as paid random; the Mild-rated Halloween tone keeps the questionnaire answers (§D maturity row, launch checklist L9); E-13 (explained in the game, not only on Discord) matches §D social links. The library's SI-13 text-filter remark differs from §D: not landed; proposals row 6. No line about ads, chat, saves, remotes or player data was added.

**V10 partner consistency:** tier names T1-T4 and the "attempt cue on input, big layer on the confirmed result" wording follow `progression-design/references/reward-tiers.md` and `game-design` G-19; flat-key captures for variants follow the game designer's role file; marketing standards are pointed to by their ids (M-15, M-22). No conflict found.

**Proposals from other roles against my books (V11):**
| Row | From | Decision | Where |
| --- | --- | --- | --- |
| `.agents/skills/live-ops-design`: "Event rewards are placed in the same tiers; a new top-tier event reward needs the same rarity proof (re-simulated rate)" | progression-designer (`proposals/progression-designer.md:27`) | adopted | design L-18; handoffs.md §3 rule and check C2; ER §1 progression row; principle 3 |
No other proposal row targets `live-ops-design` or `live-ops-craft` (grep of `proposals/`, 2026-10-22). The game-designer's GD-35 row targets the library, not my books.

**V5 pass:** a script read table a, opened each landed-in file and confirmed the cited section or line id exists (results in the hand-back); every row whose finding has a runnable check names its self-review line (E-line, self-check D or C line, or principle check); the one worked example that uses changed rules (ER §5) was re-read after the edits (tier names, the paid-random status of the egg, the fix notes saying what and why, not how).

### Repair round 1 (stage 3 review `reviews/live-ops-designer-rev1-reviewer.md`, 2026-10-22)

Scratch for runs R6-R8: the session scratchpad `live-ops-designer-rep1/` (files carry the role name). Every keep-list item is kept: event-review.md as a whole (one capture row C-13 and one line E-19 added, E-08 widened), the worked example (re-read; scope fit, story, reward family, variant type and n/a lines added), L-16, the concept round and freeze, the false-readings table (rows corrected and added), the role's partner table (shortened to one line per partner with the pointer) and "Before you hand back", every old rule, §7, V11.

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 | fixed: `process.md` §3 brief lines gain "for a new world or zone: its escape in one line and how it differs from the last world (palette, shapes, theme)"; "event-scope work" (an event, season beat, theme, variant line, limited item, or new world or zone) defined at the top of `event-review.md` and used in `process.md` §1 row 9, §3, §4, craft SKILL step 8 and self-check C, design SKILL step 6, §5, §6, role Work method 6 and "Before you hand back"; `event-review.md` §1 environment row asks for the escape and a first view unlike the last world, §2 C-13 (the two first views, same camera, two stills), §3 E-19 (cold read by eye; the art director's palette measure if run; fix owners environment-designer, art-director); design L-22 points to E-19; coverage GD-33 row corrected |
| F2 | fixed: `process.md` §3 is the one list of event brief lines ("each line filled or marked n/a: <reason>"); craft self-check C now reads "every event brief line of `process.md` §3" (input: the brief, the count file, the tier table); role Work method 6 and design SKILL step 3 point to it; coverage GD-08 and SI-18 rows name self-check C |
| R1 | fixed: `feedback-ops.md` §4 "item at exactly --end" row corrected (keep the end at the boundary; a later end counts the next window); rows added for a date-only end, several loud authors none with half (messages per author above about 3, a starting value, then the spread read by eye), and duplicate overlapping exports; §1 hand-made items take `item_id` from the export's own id; §3 step 7 lists the silent rules next to the command (V12). Runs R6-R8 confirm each; proposals row 5 gains (e) |
| R2 | fixed: every kept line in design SKILL §6 and craft SKILL §6 now names its input in parentheses |
| R3 | fixed: craft step 8a one-pager fields gain "fit to the approved scope and capacity (a builder rough or "reuses X")"; a premise the owner already fixed means the round covers only what is open, or is skipped with that decision id; self-check C accepts that decision id; role Work method 6 matches; the worked example shows the fit field (B did not fit the approved scope) |
| R4 | fixed: §7 row 13 check names the plan header and option fields (problem, target experience, constraints, success test) on the plan file, written in the header until the template has them (proposals row 2 extended); row 18 adds the capacity and effort budget and actual effort recorded in the review |
| R5 | fixed: role partner table is one line per partner pointing to `handoffs.md` §1 (planning partners) and `event-review.md` §1 (crafts), with one "when" each; marketing has one timing everywhere (calendar and fact sheet after the pick; event kit when the build is credible; again when live) in `handoffs.md` §1 and `event-review.md` §1; `process.md` §3 craft row now points to `event-review.md` §1; design §7 rows 3, 11, 15, 19 point to L-18, L-17, L-21, L-19 for the rule and keep their example and check; design step 3 points to the brief lines instead of restating them. Design SKILL §1-§6 now 17.8 KB (inside the 18 KB first-read budget) |
| R6 | fixed: E-08 input adds the odds screen with the event boost active; pass adds the boost's numeric effect before purchase and the shown odds changed while it is active (`platform-policy` rules §A); coverage V4 line corrected |
| R7 | fixed: craft step 8 check `rules/messages.md` §6 → §2; craft step 11 and `process.md` §6 lesson row now say the hand-back's `lesson` field (the lead writes the inbox draft) |

