---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2)
supersedes: []
---
> Author: J018 maker orchestration · claude-opus-5-5 · high · 2026-10-22 (repair rounds 1 and 2 the same day)

# Coverage: orchestration (J018 stage 2, wave 3)

Books rebuilt (old state: `df13ff4`): `.agents/skills/orchestration/SKILL.md`, new `references/gates-and-feedback.md`, new `references/briefs-and-handoffs.md`. Not edited: `references/job-types.md` (job recipes, proposals only, J018-D2 point 4), `evals/`. No role file exists for the lead (the lead chat loads this skill at every owner request), so deliverable 3 (role file body) is not applicable; the role-file duties (how it works, what it checks before handing back, what it asks partners for and when) live in SKILL §1, §14 and `references/briefs-and-handoffs.md` §1-§2.

SKILL.md: 172 lines (≤ 500), 27.4 KB at stage 2, 28.8 KB after repair round 1, 27.7 KB after repair round 2; description unchanged (277 characters). §14 (the self-check) starts at byte 18,703 after repair round 2 (was 20,186): detail of §1.4, §1.5, §2, §4.3, §5.1, §9.7, §10, §11 and §12 moved behind pointers (BH §8-§10, the templates, `rules/messages.md` §2) with every heading and number kept; see the Repair round 2 note, R4. The first section says to re-load the skill and re-read §8, §14 and §15 after a compaction (the harness profile already re-loads `orchestration` after compaction). The self-review the lead runs before every report is SKILL §14; "Core principles for this craft" is SKILL §15.

Library [inference] numbers kept as PROPOSAL starting values: the image budget per gate (`gates-and-feedback.md` §2), the "3 or more repeats → tool proposal" count (SKILL §9.8). No [unverified] engine claim was added; no Roblox engine fact is used in these books.

### a. Findings tagged orchestrator (79) and untagged findings used (11)
Paths: `S` = `.agents/skills/orchestration/SKILL.md`, `GF` = `references/gates-and-feedback.md`, `BH` = `references/briefs-and-handoffs.md`. "P n" = core principle row n in S §15.

| ID | Title | Landed in (file § section) | As | Or rejected: reason |
| --- | --- | --- | --- | --- |
| CD-02 | Write the sell list before drawing | BH §1 (sell list row), §4 character row; GF §1 (goal word from the sell list); S §14 line 8 (per-type items before the briefs that depend on them) | standard; step; self-review check | |
| CD-08 | The concept is a blueprint | GF §7 (a reference is finished as far as the next maker needs; never commission polish); BH §2 (concept marks intent) | standard | |
| CD-27 | Hard cases: scary creature-humanoids and multi-form characters | S §1 step 2 (one character per form in sizing); BH §4 character row ("one character per form", "keep it scary" with a reference) | step; standard | |
| CR-02 | Ask a goal question, never "do you like it?" | S §8 (goal question), §14 line 2, §15 P3/P16; GF §1 with screening grep | standard; self-review check; core principle; example (GF §8.1) | |
| CR-03 | Solve the problem behind the note; goals vs tactics | S §1 step 6, §8 owner notes, §14 line 6; GF §5 steps 1-2 | step; self-review check; example (GF §8.2) | |
| CR-04 | Answer every note with a concrete visible fix; protect the anchor | GF §5 step 5 (one problem per brief, `protected` names the anchor, fix accepted when the problem is gone in the same capture) | step | |
| CR-05 | Visual notes as paint-overs on a capture | S §6 (visual notes are paint-overs, kept); GF §5 step 7 (points to `art-review/references/feedback-briefs.md` §6) | standard (pointer, V6) | |
| CR-06 | Notes direct and visual; maker drives; conflicts go up | GF §5 step 8 (never averaged; owner vs reviewer: the owner's note stands, evidence goes to the digest; two reviewers: the decision owner decides); S §8 owner-notes pointer, §14 line 6; S §10 (the receiver owns the how, kept) | standard; self-review check | |
| CR-07 | No grand reveals: show early and often | S §6 (the rule: rough first to consumers, roughs at G1, cheap proof at G2, status pictures), §14 line 4; GF §6 (how it runs) | standard; self-review check | |
| CR-08 | Diagnose by layer; "not happy" may mean "not done" | S §8 owner notes; GF §5 steps 3-4; GF §8.2 | step; example | |
| CR-09 | Fresh eyes: flip, change the reviewer | S §7.2 (review chain by other agents, kept; `rules/company.md` §6: a review is never done by its maker) | standard (existing rule kept) | The image-flip half is craft self-review (art and modeling books) |
| CR-11 | The project's needs come first; the lead curates the best solution | S §4.3 (a decision record per consequential question, kept; its fields (options, decision owner, evidence, dissent) live in `templates/jobs/direction-sheet.md` since repair round 2), §4.1 (independent proposals from every lead) | standard (kept) | |
| CR-12 | When every option meets the brief, choose and commit | GF §1 last bullet | standard | |
| CR-13 | Close with an honest recap | S §9 step 8 (honest retrospective: what worked, too tame or too big, what more iteration would fix); S §8 packet (4) (the recommendation's weakest part at every gate), §14 line 2, P16; GF §8.1 | step; self-review check; example | |
| CR-14 | Pitch the experience the player will have | GF §3 (the recommended option told as the moment the player gets); S §8 packet (4) (trade-off in player terms, kept) | standard | |
| CR-17 | Say what each input can prove; could-not-check list | GF §2 (the one place: every-packet list, input table); S §8 packet (6) pointer, §13, §14 line 3 | standard; self-review check | |
| CC-01 | One target experience, signed by every craft | S §1 step 1 (four lines), §4.3 (the line every brief quotes), §10, §14 line 7; BH §1 | step; self-review check | |
| CC-02 | One marker list is the timing contract | S §4.3 (marker-list owner), §5.1, §6 (retime = contract change), §14 line 10, P8; BH §3; GF §8.3 | standard; self-review check; core principle; example | |
| CC-03 | Build for the next craft: ask what they need first | S §4.1 (needs from other crafts), §5.2 (needs before the producer builds), §10, §14 lines 7, 9, P17; BH §2 | step; self-review check | |
| CC-04 | The concept leaves room for the next crafts' decisions | S §10 (downstream crafts get intent, not settings); BH §2 | standard | |
| CC-05 | Share strong motifs across crafts; input from several roles | BH §2 (a found motif is recorded in the contract or art bible); S §4.1 (independent proposals from several leads, kept) | standard | |
| CC-06 | Split a big craft job by category, one integrator, shared library | BH §5 | standard | |
| GD-01 | Every asset has jobs: clarity, feel, style | S §7.4 (readiness in the order read, feel, look), §8 packet (6), §14 line 3, P1; GF §2 | standard; self-review check | |
| GD-04 | Name the target experience, not "fun" | S §1 step 1, §3.3 | step | |
| GD-15 | Prove the fun with the crudest prototype before art | BH §4 feature row (grey-box verdict before any production art brief); S §5.3 (cheap proof); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| GD-18 | A new character starts from the roster gap | BH §4 character row; S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| GD-19 | A mode change re-checks the whole roster | BH §4 feature row (linked balance re-check); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| GD-20 | Choose themes from data; combine proven themes | BH §4 live update row (data behind it, themes combined, maturity); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| GD-22 | Find the genre's demands first | S §1 step 1 (constraints: camera, device and input, player count, budget, platform rules, locks); BH §1 constraints row (from the game profile and the vision record's parameters) | step | |
| GD-31 | Art stays inside the blockout's gameplay | BH §4 stage row (route, cover, sightline, collision changes go to the game-designer first) | standard | |
| MD-02 | Budget detail by display size, camera distance and speed | BH §1 (display sizes row); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| PP-06 | When geometry changes, re-project | — | — | Craft method (how a texture survives a mesh change); the lead never prescribes how (S §10); `modeling-craft` carries it |
| PP-08 | Low-poly painted workflow keeps changes cheap | — | — | Craft route choice owned by the modeler and environment designer; the lead never prescribes how (S §10) |
| PP-12 | Build to the shared rig | S §3.1 (released rigs with joint lists as a prerequisite); BH §4 character row (a part with no joint is a scope request) | step; standard | |
| PP-15 | Spend expensive features only where they earn it | S §6 (additions are tickets with cost and the reason it earns its place), §14 line 12; BH §4 character row; BH §5 pointer | standard; self-review check | |
| PP-25 | Reuse first | BH §5; S §10 pointer; P17 | standard | |
| PP-26 | Environment order | BH §4 stage row (light only after the last route change); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| PP-28 | Automate every repeated step | S §9 step 8 (3+ repeats → tool proposal, PROPOSAL count); BH §5 | step | |
| PP-29 | One owner per file or area | S §6 (file or Studio container; crossing edits through an exchange note), P17; BH §5 pointer | standard | |
| PP-30 | Fix naming and folders before production | S §3.1 (a job that creates assets has a naming and folder rule: a game-profile link, or one job-card line until the profile has the field); BH §5 pointer; proposal row for the profile field | step | |
| PP-32 | One key art feeds a whole asset kit | BH §4 marketing row; S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| PI-01 | The cheapest stage goes first | S §5.3 (cheap proof), P4, P15; GF §6 | standard; core principle | |
| PI-02 | Gates freeze decisions | S §5.4, §8 (gates close doors: G1 direction, G2 big shapes and timing beats, polish notes are follow-ups); GF §2 "Closes" column | standard; self-review check | |
| PI-03 | Closing doors: never reopen | S §1 step 5, §8, §14 line 5, P15; GF §4 (format, screening grep); GF §8.1 | step; self-review check; example | |
| PI-06 | Work in passes over the whole | S §5.3 ("The proof is cheap (greybox, proxy, placeholders, temp sound; nothing polished)"), §6 ("a craft's first hand-back to its consumers is a rough state, checked before polish"), P4 (direction, proof, build, in order) | standard | The per-asset pass discipline is craft execution (art, modeling, animation books) |
| PI-07 | One named problem per pass; worst first | S §8 owner notes, §14 line 6, P16; GF §5 step 5 | standard; self-review check | |
| PI-09 | Not precious: delete, redo, let go | S §7.3 (an approach that failed both rounds restarts at its cheapest stage), P15 | step | |
| PI-11 | A time box forces the readable choice | S §3.3 (budget per stage), §10, §14 line 1; BH §1 budget row | step; self-review check | |
| PI-12 | Know when it is done | S §3.3 (stop criteria), §10, §12 (done on evidence), P18; GF §7 | standard; self-review check | |
| PI-13 | Finish a concept only as far as the next maker needs | GF §7 | standard | |
| PI-14 | "It would be cooler" is new scope | S §6 (additions are tickets), §14 line 12; GF §7 | standard; self-review check | |
| RI-01 | Concept work solves a problem; play value and cost lines | S §4.1, §8 packet (3), §14 line 2; GF §3 | standard; self-review check | |
| RI-02 | Options at equal low finish on a labelled sheet | S §4.1, §8 packet (3), §14 line 2; GF §2-§3 | standard; self-review check | |
| RI-03 | Know the problem, constraints and end before making anything | S §1 step 1, §10, P13; BH §1 | step; self-review check; example (P13) | |
| RI-04 | In marketing art, the launched thing is the hero | BH §4 marketing row; S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| RI-05 | Research first; one narrow moodboard | S §4.1 (research board); GF §3 | step | |
| RI-06 | Each theme gets a library | BH §4 new theme row; S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| RI-12 | Get enough reference; make the missing one | BH §1 (refs cover every key pose, material and place; a missing one is made) | standard | |
| RI-16 | Research, explore wide, iterate one or two, finish to the next maker | S §4.1; GF §3, §7 | step | |
| RI-19 | Present options with your pick and reasons | S §8 (goal question, packet (4)), §14 line 2; GF §1, §3 | standard; self-review check | |
| RI-20 | For the final pick, compare 4-5 strong small options | GF §2 G1 row (the recipe's count: 2-3, marketing art 3-5) | standard | |
| RI-21 | The first output is a warm-up; reject the typical idea | S §4.1 (warm-up label, one radical); GF §3 | step | |
| RI-23 | One unexpected element from outside the genre | GF §3 (one research source from outside games) | step | |
| RI-26 | The same key poses can tell two stories: try two | GF §2 G2 row (the animator's two timing takes as playable previews for the owner's pick, as `animation-design` §3 step 6) | standard | |
| RI-30 | Leave a marked placeholder for what is designed later | S §7.4 (placeholders listed), §8 packet (6) (stand-ins named); GF §2 | standard; self-review check | |
| SD-01 | Sound has three jobs | BH §4 "any job with sound" row (cue list per state change); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| SD-23 | Every floor material is a footstep callout | BH §4 stage row (floor-material list to the sound designer); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| SD-25 | Mix as you go | BH §4 sound row (each cue enters the mix as built; G3 listens to the full mix) | standard | |
| SD-27 | Sound notes in technical terms with a direction | GF §5 step 7 | standard | |
| SD-28 | Judge against reference; name every stand-in | S §8 packet (6), §14 line 3; GF §2 | standard; self-review check | |
| SD-29 | Sources by texture; many takes, odd ones | — | — | Craft method owned by `sound-design`; the lead never prescribes how (S §10) |
| SD-30 | Library of building blocks; cues are data | BH §5 (reuse the sound library); content as data stays the binding `AGENTS.md` §2 rule | standard | |
| SD-31 | A fixed cue template and categories | — | — | Craft template owned by `sound-design`; nothing for the lead to carry out beyond naming the craft's skills (S §10) |
| SI-05 | Make it for a specific audience; what fans want | BH §4 live update row; S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| SI-12 | Each theme needs its own niche | BH §4 live update row (differentiator from the nearest theme); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| UI-01 | Flow first, then style, then motion | BH §4 UI row; S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| UI-05 | UI is every screen and state | BH §4 UI row; S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| VH-02 | Rank loudness across a set | S §4.3 (one importance rank per job), P3 | step; core principle; example (P3) | |
| WL-06 | Rank the environment work | BH §4 stage row (ranked list made with the game designer); S §14 line 8 (per-type items before the briefs that depend on them) | standard; self-review check | |
| CR-01 (untagged) | Judge in the game, at the game camera | S §1 step 3, §7.4, §8 packet (1), P2 | standard; self-review check | |
| CF-07 (untagged) | Judge composition on the integrated capture | GF §2 G3 row (busiest supported scene) | standard | |
| GD-02 (untagged) | Every action gets immediate feedback | BH §4 feature row (feedback stack per action) | standard | |
| GD-34 (untagged) | Feedback follows the real outcome | BH §9 code briefs (kept failure cases; moved from S §10 in repair round 2), S §13 (rejected-request capture), §14 line 11, P19; BH §3 | standard; self-review check; core principle | |
| VR-13 (untagged) | Strobes stay low; flash safety | GF §2 (flashes over 3 per second block the gate), P20 | standard; core principle | |
| VR-23 (untagged) | Every intense channel has an off path | GF §2 (a channel with no reduced path blocks the gate), P20 | standard | |
| SD-26 (untagged) | Review the key event solo, then in the full mix | S §8 packet (6) (listening owner-confirmed); GF §2 listening line | standard | |
| RI-17 (untagged) | Take the big swings at concept stage | S §4.1 (one radical option); GF §3 | step | |
| RI-18 (untagged) | Each option gets its own hook | S §4.1 (hooks); GF §3 | step | |
| CR-15 (untagged) | Start from the player's pain points | BH §4 live update row | standard | |
| PI-04 (untagged) | Block out first, in the engine | S §5.3 (cheap proof in greybox) | standard | |

Rejected: 4 (PP-06, PP-08, SD-29, SD-31), each craft method the lead must not prescribe.

### b. Universal principles
| UP-ID | Applies | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: the lead's packets and readiness put the player's read first | S §15 row 1 |
| UP-02 | yes: no gate decision on a beauty shot, editor view or turnaround | S §15 row 2 |
| UP-03 | yes: the owner reads the decision first; one importance rank per job | S §15 row 3 |
| UP-04 | yes: direction, proof, build in order; no polish brief before its gate | S §15 row 4 |
| UP-05 | no: shape and silhouette are craft execution; the lead routes them and checks only that the job lead's review ran them | S §15 intro line |
| UP-06 | yes: fewest decisions in front of the owner, features earn their place; agent briefs stay complete (`rules/messages.md`: never cut a rule) | S §15 row 6 |
| UP-07 | yes: one vocabulary, one marker list, one decision log | S §15 row 7 |
| UP-08 | yes: the lead keeps the timing contract whole (marker list, retime notices) | S §15 row 8 |
| UP-09 | no: pushing past real is craft execution | S §15 intro line |
| UP-10 | yes, in the lead's terms: the owner's intent is the subject every choice traces to | S §15 row 10 |
| UP-11 | yes: one art bible revision in every visual brief; a new look is sized L | S §15 row 11 |
| UP-12 | no: controlled variation is craft execution | S §15 intro line |
| UP-13 | yes | S §15 row 13 |
| UP-14 | yes | S §15 row 14 |
| UP-15 | yes | S §15 row 15 |
| UP-16 | yes | S §15 row 16 |
| UP-17 | yes | S §15 row 17 |
| UP-18 | yes | S §15 row 18 |
| UP-19 | yes, in the lead's terms: "done" follows the real outcome; jobs with a server-confirmed result carry a rejected-request capture | S §15 row 19 |
| UP-20 | yes: safety and comfort faults block a gate; packets list grayscale, sound-off and reduced-motion checks | S §15 row 20 |

### c. Old book changes (old text at `df13ff4`)
Nothing was removed. Every old rule stays; the rows below are rules sharpened, replaced or moved.
| Old text (file:line at df13ff4) | Change | Why |
| --- | --- | --- |
| `SKILL.md:6` author line | kept; J018 phrase and author tag added | brief rule |
| `SKILL.md:11` "Read the message twice ..." | sharpened: plus the four lines (problem, constraints, target experience, success test) before sizing | UP-13, RI-03, GD-04, CC-01 |
| `SKILL.md:12` "Size it ... one line of why" | sharpened: a multi-form character counts once per form | CD-27 |
| `SKILL.md:13` "S: ... self-review + one domain check; report" | sharpened: show the result where players meet it | UP-02, CR-01 |
| `SKILL.md:16` "Between stages ..." | sharpened: record the doors the gate closed; carry them into the next briefs' `avoid` | PI-03 |
| `SKILL.md:17` "G3 change request: stage repair ..." | sharpened: restate the problem behind the note, name the door it reopens and what goes stale | CR-03, PI-02 |
| `SKILL.md:38` prerequisites | sharpened: naming and folder rules; rig joint lists | PP-30, PP-12 |
| `SKILL.md:40` job card contents | sharpened: four lines, stop criteria, budget per stage (usage in tokens kept) | PI-11, PI-12 |
| `SKILL.md:45` D1 "Each returns: 2-3 reference images or rough options, ..." | replaced by: research board, hooks with warm-up and one radical, 2-3 options (reference images, rough options or greybox stills) that pass the lead's read check at equal low finish with play value and cost, one recommendation, needs from other crafts (old fields kept) | RI-02, RI-05, RI-16, RI-21, RI-01, CC-03; depth in GF §3 |
| `SKILL.md:47` D3 synthesis | sharpened: target-experience line, dropped options as closed doors, one importance rank, marker-list owner | CC-01, PI-03, VH-02, CC-02 |
| `SKILL.md:52` contract | sharpened: one marker list where animation, VFX and sound meet | CC-02 |
| `SKILL.md:53` "crafts that depend on each other write needs against it" | sharpened: each consumer writes its needs against the contract draft before its producer builds | CC-03 |
| `SKILL.md:54` "The proof: only the crafts it needs" | sharpened: the proof is cheap (greybox, proxy, placeholders, temp sound) | PI-01, PI-04 |
| `SKILL.md:55` "After G2 the big shapes stop moving" | sharpened: names what stops moving (layout, proportions, timing beats, key light) | PI-02 |
| `SKILL.md:59` check-ins | sharpened: a craft's first hand-back to consumers is a rough state | CR-07 |
| `SKILL.md:60` contract change | sharpened: a retime is a contract change to VFX and sound the same turn | CC-02 |
| (new, §6) | added: additions are tickets with cost; one owner per file | PI-14, PP-15, PP-29 |
| `SKILL.md:67` repair limit | sharpened: an approach that failed both rounds restarts cheap, not a third patch | PI-09 |
| `SKILL.md:68` readiness | sharpened: placeholders and stand-ins listed; look in the order read, feel, look at game camera and phone size | GD-01, RI-30, SD-28 |
| `SKILL.md:71` "Ask one question tied to the goal, never 'do you like it?'" | sharpened: the goal word from the job card, one decision, labelled options, one recommendation with reasons, default | CR-02, RI-19 |
| `SKILL.md:72` gate packet "the artifact first ...; what was checked, by what evidence, and what was not; usage" | replaced by the ordered 8-item packet (artifact as players meet it, goal question, options at equal finish with failed ones listed, recommendation and rejection reasons, what changed, checks read-feel-look with labels, stand-ins, could-not-check, owner-confirmed feel and listening, doors closed, usage); every old item kept | CR-17, GD-01, RI-02, RI-19, SD-26, SD-28, PI-03 |
| `SKILL.md:73` record answer + "Never show a polished picture as if it were the in-game result" | kept: recording moved to the "Gates close doors" bullet; the polished-picture rule moved into packet item 1 | V6 (one place) |
| (new, §8) | added: owner notes; no grand reveals | CR-03, CR-08, PI-07, CR-07 |
| `SKILL.md:82` rejected options → tried-and-failed | sharpened: closed doors with a lasting lesson too | PI-03 |
| `SKILL.md:84` "a short retrospective line" | sharpened: honest retrospective (what worked, too tame or too big); repeated manual step → tool proposal | CR-13, PP-28 |
| `SKILL.md:89` exact vs open | sharpened: downstream crafts get intent, not settings | CC-04 |
| (new, §10) | added: open every brief with the four lines, target-experience line, budget, stop criteria, consumers' needs; pointers to BH and `preproduction/references/handoffs.md` §2 | UP-13, PI-11, PI-12, CC-03 |
| (new, §12) | added: `done` follows the real outcome | UP-19, GD-34 |
| `SKILL.md:117-119` verification | sharpened: hook screens shape only; what each input can prove; could-not-check list; rejected-request capture | CR-17, GD-34 |
| `SKILL.md:121-128` self-check | replaced: every old line kept (some merged), each line names its input; new lines for packet, closed doors, owner notes, rough-first, marker list, done on evidence, additions | V1, V5 |
| (new) §15 Core principles | added | J018-D2 point 2 |
| `SKILL.md:130-141` read-this-file table | two rows added | new references |

### d. Command runs (V3) and proposal rows from other roles (V11)
Scratch files: `C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew--claude-spares-spare-5bnXLW\15d0fbc0-e7e9-4bea-af68-9ddb5da374ba\scratchpad\orchestration_*`.
| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| R1 (GF §1) | `grep -n -i -E "do you like\|like it\?\|thoughts\?" <packet.md>` | the real input form: a gate packet markdown file. Synthetic bad packet ("Do you like option A?"), good packet (goal question); real files `J018-riot-craft/g1-packet.md`, `J009-art-director/art/test-a/direction-packets.md`, every `knowledge/jobs/*/digest*.md` | bad: line 3 found, exit 0; good: no hit, exit 1; real files: no hit, no false positive. Wrong with no error when: the taste question uses other words ("which do you prefer?", "is this good?"), or the goal word is absent: both written next to the command as known limits, with "read the question line against the job card" |
| R2 (GF §2) | `grep -o -i -E "\.(png\|jpe?g\|webp)\b" <packet.md> \| wc -l` | synthetic packets (3 separate images; 1 contact sheet); real `direction-packets.md` and `g1-packet.md` | 3 and 1 on the synthetic; 24 and 0 on the real files, matching their links. Wrong with no error when: a contact sheet holds several options (counts 1), images are sent outside the file (counts 0): written as known limits |
| R3 (GF §4) | `grep -rn -i "<closed name>" knowledge/jobs/<job-id>/` | synthetic job folder: `decisions.md` with closed door CD-1 "neon arcade"; briefs T03 (`avoid:` mention), T04 (re-proposal), T05 (synonym "cyberpunk neon") | T03 and T04 found (T03 is a correct `avoid` mention, written as such); T05 missed (synonym): written as a known limit with "read each new option against the closed list" |
| R4 (BH §6) | `python tools/hooks/handback_check.py < payload.json` | 8 SubagentStop payloads, the hook's real input form (`agent_type`, `last_assistant_message`) | well-formed and bold-STATUS: no output (pass); no STATUS, coverage only in prose: block line; exit 0 always. False passes with no error: coverage listing only finished items (the E-03 overclaim), `coverage:` in a code block, empty message, non-kit agent type: all written as known false passes; the book keeps "read coverage against the files" as the real check |
| R5 (S §9) | `python tools/kb_index.py --lint`, `--check` | the repository | lint: 0 errors, 159 warnings, exit 0; check: "indexes current" before my files, STALE after other makers' files (expected; the lead runs `kb_index.py` at the wave's end). The writing mode (no flag) was not run: it writes tool-owned indexes while other makers work |
| R6 | `python tools/context_packet.py packet "J018 rebuild orchestration books" --role orchestrator --job J018-riot-craft` | the repository | packet printed; "Docs map: no row names this role": no Roblox docs rows for the lead, none needed (no engine fact added) |
| R7 | `python tools/verify.py --fast` | the repository after my edits | SKILL.md size PASS, descriptions PASS, always-loaded PASS, kb lint PASS; sync_harness DRIFT and kb_index STALE from this wave's new files (the lead runs `sync_harness.py` and `kb_index.py` after the wave; not mine to run) |

V4: no library line about money, paid random items, ads, chat, player data, saves or remotes landed except "a request the server rejects shows no success layer" (S §10, §13; BH §3), which matches `networking-security` (the server is the source of truth); no `platform-policy` rule is restated. V10: the sync rule and timing list are pointed to (`animation-design/references/game-timing.md` §4, `sound-design` S-133), never restated; the attempt-cue / confirmed-outcome rule points to `game-design` G-19. V13: no measure longer than one grep line is written into the books; the gate-packet checks a tool could run are a proposal (`proposals/orchestration.md`).

**Proposal rows other roles wrote against my books (V11).** Only one row targets the orchestration skill itself; the others target `references/job-types.md` or `.agents/workflows/jobs/` and stay proposals for the owner at G3 (listed below for the lead to collect). Where a recipe row also implies a lead-side rule I may write, I adopted that part in my books and left the recipe part as a proposal.
| Row | Target | Decision |
| --- | --- | --- |
| `proposals/game-designer.md:25` | `templates/jobs/` new `closed-doors.md`, "reference it from the orchestration job-folder list" | adopted in part: closed doors live in the job's `decisions.md` "Closed doors" table (format GF §4, close-out S §9.5); a separate template is a template change (read-only for me), re-proposed in `proposals/orchestration.md` row 1 for the owner |
| `proposals/sound-designer.md:30` | job recipes, gate packet listening | adopted the lead-side part: the owner-confirmed listening line (key event alone, then the full mix, phone speaker and headphones) is in S §8 packet (6) and GF §2; recipe text stays G3 |
| `proposals/ui-ux-designer.md:19` | UI recipe review captures; "the owner judges motion feel at normal speed on the playable preview" | adopted the lead-side part (feel at normal speed as an owner-confirmed line on the playable preview, S §8, GF §2); capture packet stays G3 |
| `proposals/game-designer.md:18`, `proposals/vfx-designer.md:27` | effect recipe evidence (rejected-request capture, test hooks) | adopted the lead-side part: jobs with a server-confirmed result carry a rejected-request capture (S §13, §14); the recipe's capture list and test hooks stay G3 |
| `proposals/art-director.md:34`, `proposals/film-director.md:33`, `proposals/marketing.md:17` | G1 shows: equal finish, failing options as numbers, warm-up and hooks | adopted the lead-side part (S §4.1, §8 packet (3)-(4); GF §2-§3); recipe text stays G3 |
| `proposals/game-designer.md:17`, `proposals/sound-designer.md:27-29`, `proposals/modeler.md:19`, `proposals/progression-designer.md:18` | consult crafts earlier (animator at direction, sound at kit list and feature direction, modeler on the reference set, reward tiers in the contract) | adopted the general rule (consumers state needs before producers build: S §5.2, BH §2; one importance rank incl. reward tiers in D3: S §4.3; floor list and cue list in BH §4); the recipe placements stay G3 |
| every other row below | job recipes or job workflows | not mine to adopt (J018-D2 point 4); collected for G3 |

Rows for the lead to collect at G3 (target `references/job-types.md` or `.agents/workflows/jobs/`): `animator.md:30-32`; `art-director.md:31-34`; `character-rigger.md:27-30`; `environment-designer.md:17, 22`; `film-director.md:33-37`; `game-designer.md:17-20, 30`; `marketing.md:17-18`; `modeler.md:17-20`; `progression-designer.md:17-18`; `sound-designer.md:26-30`; `ui-ux-designer.md:17-21`; `vfx-designer.md:24-27`. My own G3 rows: `proposals/orchestration.md`.

V5 pass: every row in table a that has a runnable library `check:` names a §14 self-review line or a GF/BH screening aid (CR-02, CR-03, CR-07, CR-17, CC-01, CC-02, CC-03, GD-01, PI-02, PI-03, PI-07, PI-11, PI-12, PI-14, PP-15, RI-01, RI-02, RI-03, RI-19, RI-30, SD-28, GD-34, CR-01); the landed-in locations were opened after the last edit; the worked examples (GF §8.1-8.3, BH §7) were re-read against the final rules (equal finish, closed doors, one problem per brief, retime notice).

## Repair round 1 (review `reviews/orchestration-rev1-reviewer.md`, verdict fix-first)
> Author: J018 maker orchestration · claude-opus-5-5 · high · 2026-10-22 (repair round 1)

Paths as in table a. Every item of the review's keep list is unchanged (four lines, ordered packet and per-gate table, input table and owner-confirmed lines, closed doors with "may return only if", owner-note steps, the D1 return for look-owning leads, one marker list pointed to `game-timing` §4, done on evidence, two-round restart, the BH §7 brief, nothing from `df13ff4` dropped). `references/job-types.md` and `evals/` untouched (`git diff --stat` empty).

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (blocking) | Fixed. GF §2: the packet names the images the owner is asked to look at in one `Shown:` line under the goal question; that line is what the budget counts. Two screening aids, each with its false readings: the `Shown:`-line count (0 when the line is missing, bulleted or bold; misses images outside the file or without an extension) and the whole-file grep, now labelled "a ceiling, never the count" (evidence paths, rejected images, log rows); then an eye check that every other image path sits next to a number or under the rejected list. S §14 line 3 counts the `Shown:` line by eye, "never from the whole-file grep". GF §8.1 shows the line. Run R8b below. Template and tool rows in `proposals/orchestration.md` |
| F2 (blocking) | Fixed. GF §5 step 8 split as the review proposed: owner vs reviewer, the owner's note stands; evidence that it breaks the goal, a safety or comfort rule or a platform rule goes into the digest with both readings at the same camera, and the owner chooses. Two reviewers: the decision owner decides; a tie where every option meets the goal stays with the decision owner, unless it is a gate pick. S §8 owner-notes bullet: "an agent never overrules an owner note"; S §14 line 6 checks it |
| F3 (blocking) | Fixed. New S §14 line 8: the card and briefs carry the job type's items (BH §1, §4) before the briefs that depend on them, item by item for visual work, character, feature, stage, UI, sound, marketing, new theme and live update [job card, briefs, ledger dates]. The 17 rows in table a now name it; the §14 line references in table a were renumbered (old 8-12 → 9-13) |
| R1 | Fixed. S §4.1: each direction lead returns what its recipe row names plus the shared fields; a lead that owns a look or an approach adds the options package (GF §3); a constraint owner (architect, performance-engineer) returns limits and needs, never an option menu for a technical choice (owner profile: no option menus for technical choices); the progression-designer returns its targets the way its books shape them (options that bracket the key number, one recommendation) (corrected in repair round 2, review rev2 F1). GF §2 G1 row: what the recipe's "G1 shows" row names; the option sheet only where it shows pictured options; a feature shows behaviour in player words and risky claims |
| R2 | Partly fixed, rest declined. The R3 restatements were cut from S §6 and §8, but R1 and F3 add text, so §14 now starts at 20.1 KB (was 19.9 KB). Getting it under 18 KB would mean moving §9 (close) or §10-§11 (briefs, models) out of SKILL.md: `rules/knowledge.md:106`, `.agents/roles/doc-keeper.md:19`, `templates/jobs/job-card.md:70`, `.agents/workflows/improve.md:58` and `knowledge/design/precedents.md:13` cite `orchestration` §9 by number, and §10-§11 are owner-approved J016 text the lead uses for every brief. I tried the §9 move and reverted it for that reason. Kept the mitigation: S line 10 now says §14 and §15 sit past the part a compaction keeps and must be re-read; the harness profile re-loads `orchestration` after compaction |
| R3 | Fixed: one rule, one place. No grand reveals: the rule in S §6; GF §6 is "how it runs" (S §8 bullet removed). Additions are tickets: S §6 only; BH §5 and GF §7 point to it. One owner per file: S §6 (now with "Studio container" and "exchange note" from BH); BH §5 points to it. Packet checks: GF §2 "Every packet carries" only; S §8 item (6) points to it. Also: the goal-question shape lives in S §8 (GF §1 points to it); `avoid` carrying and re-proposal rules live in S §1.5 and §8 (GF §4 points to them); the rejected-request capture lives in S §13 (BH §3 points to it); the repeated-step tool proposal lives in S §9.8 (BH §5 points to it); owner notes live in GF §5 (S §8 points to it) |
| R4 | Fixed. GF §1 pattern adds `thoughts`, `what do you think`, `prefer\?`, `good\?`, `cooler\?`, with its false hits ("thoughts" in prose, a goal question ending in "prefer?") and misses ("Happy with this?", "Good to go?", the goal word itself) next to it; read every hit. Run R8a |
| R5 | Fixed. GF §4: read only files written after the gate; the door's own `decisions.md` row, the gate packet and the pre-gate proposals are history; an avoid list written one item per line is correct. Run R8c |
| R6 | Fixed. BH §6: build the payload with `json.dumps`; a `handback_check:` line on stderr means the payload was not read, not a pass. Run R8d |
| R7 | Fixed. S §3.1: for a job that creates assets, a naming and folder rule: a link in the game profile, or one line in the job card until the profile has a field. BH §5 points to it. Proposal row: game-profile field "Asset naming and folder rules (link)" |
| R8 | Fixed. GF §2 budget: "plus the playable previews (one per take the owner picks between)", matching `animation-design/references/review.md` §1 item 5 (both previews in the gate packet) |
| R9 | Fixed. GF §8.1: (1) "the option sheet A-C (reference images, grey beside colour, placed on a spawn-camera capture at phone size), `Shown: option-sheet.png`"; (6) grayscale and phone-size reads of the images, not verified at the game camera until the G2 blockout |
| R10 | Fixed. GF §8.3: the change stays inside the window approved at G2, so it is a tuning change, not a beat change; outside it the digest gets the change first (S §5.4) |
| R11 | Fixed. GF §6: "unless the owner asks for a gate" |
| R12 | Fixed. `proposals/orchestration.md` row 1 now targets `knowledge/jobs/README.md` (the `decisions.md` row) for the one Closed doors table; the direction sheet gets a line pointing to it, not a second table |
| R13 | Fixed. S §8 packet item (4): "its weakest part said plainly"; S §14 line 2 checks it; S §15 row 16 adds "say our own weak spots" with example and check; rows 11, 13 and 16 checks now name their input; GF §8.1 shows a weakest-part line. Matches the reviewer role's own proposal (`proposals/reviewer.md:19`, `weakest_part` in the review spec) |

**Old-book changes in this round (table c addendum).** Nothing removed; moved or pointed:

| Old text | Change | Why |
| --- | --- | --- |
| `SKILL.md:60` at df13ff4: "On Claude Code 2.1.306 a message reaches a working agent at its next tool step; a message to a finished agent resumes it with its context." | replaced by a pointer to `rules/assistants/claude.md`, Peer message row, which holds the same fact (plus the resend cost) | V6; that row is the harness truth and is re-checked after each Claude Code update |
| S §8 "No grand reveals" bullet (stage 2) | merged into S §6 | R3 |
| S §8 packet item (6) list (stage 2) | pointer to GF §2 "Every packet carries" | R3 |
| S §8 owner-notes bullet (stage 2) | pointer to GF §5 (all steps) | R3 |
| GF §1 bullet 2, GF §4 bullets 2-4, GF §6 bullet 1, GF §7 bullet 3, BH §3 bullet 4 last sentence, BH §5 bullets 2 and 4 (stage 2) | pointers to the S section that holds the rule | R3 |

**Command runs, repair round 1 (table d addendum).** Scratch: `C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew--claude-spares-spare-5bnXLW\15d0fbc0-e7e9-4bea-af68-9ddb5da374ba\scratchpad\orchestration_r1\`.

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| R8a (GF §1) | the GF §1 taste grep (new pattern) | the real input form, gate-packet markdown: `bad1.md` (the reviewer's "What do you think?", "Any thoughts on these?", "Which one do you prefer?"), `bad2.md` ("Do you like option A?", "Thoughts?", "Is this good?", "Which is cooler?", "Happy with this?"), `good.md` (goal question plus a prose line "My thoughts on cost"); real `J018 g1-packet.md`, `J009 direction-packets.md`, all 17 `knowledge/jobs/*/digest*.md` | bad1: 3 of 3 found; bad2: 4 of 5 found, "Happy with this?" missed (written as a miss); good: 1 false hit on "My thoughts on cost" (written as a false hit; read every hit); real files: no hit. Exit 0 on any hit |
| R8b (GF §2) | the `Shown:`-line count, then the whole-file ceiling grep | `good.md` (Shown: 1 image, plus 4 evidence captures and 1 rejected image), `noshown.md` (same without the line), `g3.md` (Shown: 3 images, one `.PNG`, one contact `.jpg`; an evidence line with one `.png` and one `.json`); real `J009 direction-packets.md` (shown image named in a "Look first" sentence) | good: 1 (true 1), ceiling 6; noshown: 0 (not ready), ceiling 5; g3: 3 (true 3), ceiling 4; J009: 0, ceiling 24 (the reviewer's 24; the packet predates the `Shown:` line). Wrong with no error when the line is bulleted or bold, an image has no extension, or an image is sent outside the file: all written next to the command; the eye check closes it |
| R8c (GF §4) | `grep -rn -i "neon arcade" <job folder>` plus the GF §4 reading rule | synthetic job folder: `decisions.md` door row, pre-gate `direction/proposal-art-director.md`, `g1-packet.md`, briefs T03 (inline `avoid:`), T04 (avoid list one item per line), T05 (re-proposal under `open`), T06 (synonym "cyberpunk neon") | 6 hits. Reading rule: decisions row, packet, proposal = history; T03, T04 = correct; T05 = re-proposal (the only true one); T06 missed (synonym, written as a miss) |
| R8d (BH §6) | `python tools/hooks/handback_check.py < payload.json` | hand-written `p_raw.json` with raw newlines; `p_ok.json` and `p_bad.json` built with `json.dumps` | p_raw: stdout empty, stderr `handback_check: JSONDecodeError ...`, exit 0 (written: not a pass); p_ok: no output, exit 0 (pass); p_bad: a `{"decision": "block", ...}` line, exit 0 |
| R8e | `python tools/verify.py --fast` | the repository after the repair | SKILL.md size PASS (183 lines), descriptions PASS, always-loaded PASS, kb lint PASS (0 errors); sync_harness DRIFT (other makers' new architecture references) and kb_index STALE: the lead runs both after the wave |

**V5 pass, repair round 1.** Script over table a: every row with a lead-runnable library check names a S §14 line (the 17 F3 rows now line 8; CR-06 line 6; CR-13 line 2) or a GF/BH screening aid with its eye check. Every landed-in location named in the changed rows was opened after the last edit. Worked examples re-read against the changed rules: GF §8.1 (Shown line, weakest part, G1 evidence labels, look-owning lead's D1), §8.2 (one problem; the owner's note stands), §8.3 (tuning inside the G2 window), BH §7 (direction brief to the art director, a look-owning lead: options package kept).

**V11, wave-3 rows.** No row from the architect, feature-builder, level-design, live-ops-designer, qa-lead, reviewer or reference-images makers targets SKILL.md, GF or BH. Their rows against `references/job-types.md` and `.agents/workflows/jobs/` stay proposals for the owner at G3: `architect.md:17-18`, `feature-builder.md:17-19`, `level-design.md:17-19`, `live-ops-designer.md:19`, `qa-lead.md:17-21, 27`, `reviewer.md:17-18`, `reference-images.md:25-26`. `reviewer.md:19` (`weakest_part`, `could_not_check` in the review spec) agrees with R13 and GF §2; nothing to change in my books.

## Repair round 2 (review `reviews/orchestration-rev2-reviewer.md`, verdict fix-first)
> Author: J018 maker orchestration · claude-opus-5-5 · high · 2026-10-22 (repair round 2)

Paths as in table a. Every item of the rev2 keep list is unchanged: the four lines (S §1.1, §10, BH §1), the ordered one-screen packet (S §8) and the per-gate table (GF §2), the input-proof table and owner-confirmed feel and listening lines, closed doors with "may return only if", the owner-note steps (GF §5, with the step 8 owner-note rule), one marker list pointed to `game-timing` §4, done on evidence, the two-round restart, the §14 line 8 per-type items (now with the effect row), the `Shown:` line as the thing the budget counts with the whole-file grep as a ceiling and an eye check, the weakest part of the recommendation, the D1 split between look-owning leads and constraint owners (only F1's list fixed), the closed-door reading rule, and the `json.dumps` payload with stderr read as "not read". `references/job-types.md` and `evals/` untouched (`git diff --stat df13ff4` empty for both); SKILL.md frontmatter byte-identical to `df13ff4`; no section renumbered (BH gained §8-§10 at the end).

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (blocking) | Fixed. S §4.1 last sentence: "A constraint owner (architect, performance-engineer) returns limits and needs, never an option menu for a technical choice; the progression-designer returns its targets the way its books shape them (options that bracket the key number, one recommendation)." Matches `rules/owner-profile.md:16` (engineering choices only), `progression-design` SKILL step 8 and row 14, `progression-craft` C-11. Coverage repair-round-1 row R1 corrected to match |
| R1 | Fixed. GF §8.1: the top of the packet is now a small text block with (1) the artifact line, the not-shown option D with its reason, (2) the goal question, and `Shown: option-sheet.png` on its own line under it; (3)-(8) follow in prose. Run R9a: the GF §2 count reads the example as 1 image (was "not ready") |
| R2 | Fixed (first option). GF §2: the count is now per line, `grep -n "^Shown:" <packet.md> \| awk -F: '{l=tolower($0); n=gsub(/\.(png\|jpe?g\|webp)/,"",l); print "line " $1 ": " n " images"}'`, one output line per question, "each count must sit inside that question's budget"; known misses next to it (no output = missing, bulleted, bold or inline line; images outside the file, without an extension or in another format such as gif or svg; a contact sheet counts as one, as the budget does). Eye check sentence also accepts a shown image named again in the artifact line (the §8.1 form). Run R9a |
| R3 | Fixed. BH §7 example: `refs` take line adds stop criteria; new ref `knowledge/reference/roblox/docs-map.md` (art-director rows); `fixed` adds `display_sizes` (game profile) and `stop` (job card); `image_cap` is now "round 1 at most 6 incl. regenerations, round 2 at most 3" sourced to the job card and `reference-images/references/rounds.md` §7 (the reviewer's "6 per round, 2 rounds" would allow 6 in round 2, where rounds §7 says at most 3). BH §1 budget row: the same caps, with "image caps start from rounds §7; a higher cap states its reason"; the stop-criteria example matches the brief. S §14 line 7 now also checks "the Roblox docs rows" in every brief, so a copied brief without them fails the self-check |
| R4 | Fixed in part; the remainder declined with a reason. Moved behind pointers, every heading and number kept: §2 mixed-request detail → BH §8; §10 code-brief, effort and docs-evidence detail → BH §9; §11 helper table → BH §10 (a new section in BH rather than a new `references/models.md`: one fewer file, and the brief is where the model and effort are named); §10 "direction briefs never include another lead's proposal" merged into the §10 format sentence and the review-brief half moved to BH §9 (both are `rules/messages.md` §2 "independent first work"); §11 usage line cut (it is §8 packet item 8 and §14 line 12); §12 "two repair rounds" sentence → pointer to §7.3; §1.4 args and §1.5 image batches shortened (the args rule lives in `.agents/workflows/jobs/README.md:10`); §4.3 decision-record field list → the template's fields (`templates/jobs/direction-sheet.md:33`); §5.1 contract forms → "its form per recipe"; §9.7 metrics → `evidence.md` §4 rows (the template holds them). §14 now starts at byte 18,703 (was 20,186; −1.5 KB net after F1, R6 and R7 added text). Declined: moving more. The rest of §1-§13 is the lead's loop, gates and brief rules it runs every turn, and §9's steps are cited by number from five files (repair round 1, R2). The line under the title still says to re-read §8, §14 and §15 after a compaction (now "the end of §14 and all of §15") |
| R5 | Fixed. (a) BH §6 known false passes: "an empty payload file (a failed redirect: check it with `test -s payload.json` first)". (b) GF §1: `prefer` replaces `prefer\?`, so "Which do you prefer, A or B?" is caught; false hits now name "prefer" in prose ("players prefer short routes"). Runs R9b, R9c |
| R6 | Fixed. Coverage PI-06 now quotes the real S §5.3 and §6 text. S §1 step 1 constraints: "(camera, device and input, player count, budget, platform rules, locks)"; BH §1 constraints row sources them from the game profile and the vision record's parameters (`preproduction` step 1 writes camera, device mix, player count per server, input, session shape), with "touch input" and "up to 12 players" in the example. No game-profile proposal needed: the vision record already holds player count and input |
| R7 | Fixed. S §6: "A retime is a contract change (`references/briefs-and-handoffs.md` §3)": the rule lives in BH §3 only. S §14 line 8 adds "the importance tier, play rate and worst-case count, and marker names (effect)" |

**Old-book changes in this round (table c addendum).** Nothing removed; moved or pointed:

| Text (before this round) | Change | Why |
| --- | --- | --- |
| S §2 Mixed request row: the shared-interface owner job detail (J016-LD6) | short rule kept in §2 ("one owner job per shared interface, its contract first"); detail and example → BH §8 | R4 |
| S §10 code-brief bullet, effort bullet, docs-pointer evidence (rework-study B08), last bullet (direction and review briefs) | → BH §9; §10 keeps the code-brief summary, the one-check-per-rule line and the docs rule; "direction briefs never carry another lead's proposal" stays in the §10 format sentence | R4, V6 |
| S §11 helper table; "Report usage at every gate" | table → BH §10 (pointer in §11); usage line cut: it is S §8 packet item 8 and §14 line 12 | R4, V6 |
| S §12 "Two repair rounds per review gate, then needs-decision ..." | → "repair rounds: §7.3" (the rule's one place) | V6 |
| S §6 "VFX and sound get the notice the same turn" | → pointer to BH §3 | R7, V6 |
| S §1.4 args detail, §1.5 image-batch detail, §4.3 decision-record fields, §5.1 contract forms, §9.7 metric list | shortened to the rule plus a pointer to the file that holds the detail (`.agents/workflows/jobs/README.md`, `reference-images` §4, `templates/jobs/direction-sheet.md`, `references/job-types.md`, `templates/jobs/evidence.md` §4) | R4 |

**Command runs, repair round 2 (table d addendum).** Scratch: `C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew--claude-spares-spare-5bnXLW\15d0fbc0-e7e9-4bea-af68-9ddb5da374ba\scratchpad\orchestration_r2\`.

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| R9a (GF §2) | the per-line `Shown:` count (`grep -n "^Shown:" \| awk ...`) | gate-packet markdown: `p_good.md` (Shown: 1 image, plus evidence and rejected images), `p_example.md` (the old §8.1 inline form), `p_example_fixed.md` (the new form), `p_two.md` (two questions: 1 and 6 images incl. `.PNG`, `.jpeg`, `.webp`), `p_bullet.md` ("- Shown:"), `p_none.md`, `p_crlf.md` (CRLF, 3 images); and the GF file itself | p_good "line 4: 1 images" (true 1); p_example no output (not ready, as the reviewer found); p_example_fixed "line 2: 1 images"; p_two "line 2: 1" and "line 4: 6" (true); p_bullet and p_none no output (not ready); p_crlf "line 2: 3" (true); GF §8.1 block "line 97: 1 images". Wrong with no error when: an image has no extension or another format (gif, svg), or is sent outside the file: written next to the command |
| R9b (GF §1) | the taste grep with `prefer` | `t_bad.md` (9 taste wordings incl. "Which do you prefer, A or B?"), `t_good.md` (goal question, "My thoughts on cost", "Players prefer short routes"); real `J018 g1-packet.md` and every `knowledge/jobs/*/digest*.md` | bad: 8 of 9 hit, "Happy with this?" missed (listed); good: 2 false hits ("thoughts", "prefer" in prose; listed); real files: no hit |
| R9c (BH §6) | `python tools/hooks/handback_check.py < payload.json`; `test -s payload.json` | `h_empty.json` (0 bytes), `h_bad.json` (`json.dumps`, no coverage) | empty: no stdout, no stderr, exit 0 (silent pass; now listed, and `test -s` returns 1 on it); bad: a `{"decision": "block", ...}` line, exit 0 |
| R9d | `python tools/verify.py --fast` | the repository after the repair | SKILL.md size PASS (172 lines), descriptions PASS, always-loaded PASS, kb lint PASS (0 errors); sync_harness DRIFT (other makers' new architecture references) and kb_index STALE: the lead runs both after the wave |

**V5 pass, repair round 2.** Every table-a row whose landed-in text moved this round was re-pointed (GD-34 → BH §9; CR-11 → the direction-sheet template's fields; GD-22 and PI-06 rewritten); the other rows' locations were opened after the last edit and still hold their text (S §2, §10, §11 changed only by moves to BH §8-§10, which no table-a row cites except GD-34). Worked examples re-read against the changed rules: GF §8.1 (the `Shown:` line on its own line, counted 1; the shown image named again in item (1) is allowed by the eye check), GF §8.3 (retime: notice to VFX and sound the same turn, matching BH §3, the rule's one place), BH §7 (stop criteria, display sizes, docs rows, image caps from rounds §7: passes S §14 lines 7 and 8), S §15 row 8 (retime example still matches BH §3).

**V11, round 2.** `grep` of `proposals/` for rows that target `orchestration/SKILL.md`, GF or BH: none new since repair round 1 (all other rows target `references/job-types.md` or `.agents/workflows/jobs/` and stay G3 proposals, listed in table d).
