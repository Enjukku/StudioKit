---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2
supersedes: []
---
> Author: J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22

# Coverage: game-designer (J018 stage 2, wave 1)

Books rebuilt (old state: `df13ff4`): `.agents/roles/game-designer.md` (body), `.agents/skills/game-design/` (SKILL.md, `references/loops.md`, `principles.md`, `systems-economy.md`, `playtest-live.md`, `review.md`, new `spaces.md`; `social.md` unchanged), `.agents/skills/preproduction/` (SKILL.md, `references/documents.md`, `growth-order.md`, `handoffs.md`), `.agents/skills/game-concept/` (SKILL.md, `references/idea-method.md`, `pitch-template.md`, `hook-promise.md`, `rubric-taste-evidence.md`; `case-library.md` unchanged; `evals/` untouched).
SKILL.md lines: game-design 115, preproduction 79, game-concept 82 (all ≤ 500); descriptions unchanged (377, 368, 373 characters).
Where the self-review lives (the sections the agent runs before hand-back): `game-concept` §6 (pitches), `preproduction` §6 (specs, documents, briefs), `game-design` §6 (reviews and verdicts) and `game-design/references/review.md` §7 (one check list per job-recipe review slot); the role file's "Before you hand back" points to all of them. The "Core principles for this craft" section is `game-design` SKILL §7 (the skill every task loads; `game-concept` §1 and `preproduction` §1 point to it).

Library numbers marked [inference] are written as PROPOSAL starting values with the test that may change them (reaction windows, celebration length, merge window, pending-state delay, hit-stop lengths, walk limit, footprint band, read speed). No [unverified] engine claim was added; the engine facts used (walk speed 16, the jump defaults (JumpPower 50 governs by default; JumpHeight 7.2 only when UseJumpPower is false, so each game measures its own: repair round 1), PolicyService paid-random checks, ReducedMotionEnabled) were checked in the local docs mirror.

### a. Findings tagged game-designer (145) and untagged findings used (21)

Paths are under `.agents/skills/` unless they start with `role file` (`.agents/roles/game-designer.md`). "core principle N" = `game-design` SKILL §7 row N.

| ID | Title | Landed in (file § section) | As | Or rejected: reason |
| --- | --- | --- | --- | --- |
| CC-01 | One target experience, signed by every craft | preproduction SKILL §4 P-13, §3 step 5; preproduction/references/handoffs.md §1 shared header; game-design §4 G-01 | standard; step | |
| CC-02 | One marker list is the timing contract for animation, VFX and sound | preproduction/references/documents.md §6 (named stages); growth-order.md §3 (animator joins at design time); handoffs.md §2 animator row; game-design/references/review.md §7 effect (peak on contact marker) | standard; self-review check | |
| CC-05 | Share strong motifs across crafts; seek input from several roles | preproduction/references/growth-order.md §3 (a motif found by any craft is recorded in the contract); review.md §8 (best solution from any craft) | standard | |
| CD-01 | Know the character, then decide on their behalf | preproduction/references/documents.md §8 (role card: character core); handoffs.md §1 sell list | standard; self-review check (fresh reader names role) | |
| CD-02 | Write the sell list before drawing | preproduction SKILL §4 P-16, §6; preproduction/references/handoffs.md §1 (sell list in every brief); documents.md §8 (sell list) | standard; step | |
| CD-03 | Understand the archetype before evolving it | preproduction/references/documents.md §8 (character core: archetype traits kept in every option) | standard | |
| CD-04 | Variants hold the identity anchors and change the rest | game-design/references/systems-economy.md §8 (identity anchors, check); preproduction/references/handoffs.md §3.7; game-design/references/review.md §7 character | standard; self-review check; example | |
| CD-14 | Keep the cool core, swap one iconic item, justify it by lore | game-design/references/systems-economy.md §8 (a variant is a story: keep/swap line); handoffs.md §3.7 swap_line | standard; example | |
| CD-15 | Re-theme the abilities, not only the costume | game-design/references/systems-economy.md §8 (re-theme each ability's effect and sound); handoffs.md §3.7 ability_retheme | standard; example | |
| CD-17 | A complex signature item signals a skilled owner | preproduction/references/documents.md §8 (shape and build intent: hero signature item more intricate; role-card check: parts and moving pieces counted against common items) | standard; self-review check | |
| CD-26 | Design a prop or a place as a character | game-design/references/spaces.md §2 (place personality in 3-5 words) | step | |
| CD-27 | Hard cases: scary creature-humanoids and multi-form characters | preproduction/references/documents.md §8 (cost flags: extra forms, "keep it scary") | standard | |
| CD-29 | Move a sensitive theme onto a prop motif | game-design/references/systems-economy.md §8 (sensitive themes onto a prop motif); game-concept SKILL §5 rule | standard; rule | |
| CF-13 | A bright focal light can hide a surprise | game-design/references/spaces.md §7 (surprise outside the focal light; check: grayscale capture, surprise outside the top focus, testers do not spot it early) | standard; self-review check | |
| CR-02 | Ask a goal question, never "do you like it?" | game-concept SKILL §3 step 7, §4 C-20, §6; preproduction SKILL §3 step 2; game-design/references/review.md §8; playtest-live.md §1 step 5; rubric-taste-evidence.md §2; core principle 16 | step; self-review check; core principle | |
| CR-03 | Solve the problem behind the note; separate goals from tactics | game-design SKILL §3 step 8, §4 G-02, §6; game-design/references/review.md §8; playtest-live.md §1 step 5; role file (Working with other agents) | step; standard; self-review check | |
| CR-06 | Notes are direct and visual; the maker drives; conflicts go up | game-design/references/review.md §8 (direct notes, visual targets, conflicts go up) | standard | |
| CR-11 | The project's needs come first; the lead curates the best solution | game-design/references/review.md §8 (curate the best solution from any craft, record sources) | standard | |
| CR-13 | Close with an honest recap of your own result | game-design SKILL §3 step 9, §6; review.md §1 step 12, §8; spaces.md §9; role file Hand-back and "Before you hand back" | step; self-review check | |
| CR-14 | Pitch the experience the player will have, with conviction | game-concept SKILL §3 step 7, §4 C-19, §6; pitch-template.md §4 item 2 | standard; step; self-review check | |
| CR-15 | Start from the player's pain points | game-design/references/playtest-live.md §1 (pain points before a live change) | step | |
| EX-05 | A believable base earns the extremes; break only the joints that can take it | - | - | rejected: Animation craft (where the extremes sit on a believable base, which joints can stretch). My side, choosing which moments are signature moments, is already in the key-moments step (growth-order.md §1 step 4); universal principle 9 is not a design principle for this role. |
| EX-07 | Cartoony hang time: hold near the apex, then fall fast | preproduction/references/documents.md §1 vision record (one physics and motion language: jump arc and hang time, agreed with the animator) | standard | |
| GD-01 | Every asset has jobs: clarity first, then feel, then style | game-design/references/review.md §7 intro (clarity, then feel, then style); core principle 1 | quality bar; core principle | |
| GD-02 | Every action gets immediate feedback; reached goals get a short celebration | game-design SKILL §4 G-19, §6; principles.md §7 (celebrations short, every action answers); preproduction/references/documents.md §6 | standard; quality bar; self-review check | |
| GD-03 | A game needs a goal, opposition, decisions and rules | game-design/references/loops.md §1; game-design SKILL §3 step 2, §6; game-concept §4 C-15, §6; documents.md §3 field 2 | standard; step; self-review check | |
| GD-04 | Name the target experience, not "fun" | game-design SKILL §4 G-01, §3 step 1; loops.md §2; game-concept §4 C-15; preproduction P-13; role file intro | standard; step | |
| GD-05 | Behaviour sets the tone before art does | game-design SKILL §4 G-17; loops.md §5b (plain-block test); principles.md §3 | standard; stage (plain-block test); self-review check | |
| GD-06 | Movement patterns give enemies character | game-design SKILL §4 G-17; loops.md §5b; review.md §7 character; documents.md §8 (movement pattern) | standard; self-review check | |
| GD-07 | Art and mechanics must promise the same thing | game-design SKILL §4 G-18, §3 step 4; principles.md §3 (mismatch list); loops.md §6 item 9; hook-promise.md HC12 | standard; self-review check | |
| GD-08 | Art turns rules and numbers into a fantasy players build around | game-design/references/principles.md §3 (theme families; check: every item in a set names its family) | standard; self-review check | |
| GD-09 | Mechanics and numbers are design constraints for art | game-design SKILL §4 G-18; principles.md §3; preproduction/references/handoffs.md §1 (pass mechanics and numbers as tuning keys); documents.md §8 | standard; step | |
| GD-10 | Make progress toward the goal visible | game-design/references/principles.md §4 (progress visible, midpoint as event, check) | standard; self-review check | |
| GD-11 | Build a climactic arc toward the resolution | game-design/references/principles.md §4 (climactic arc, intensity plot); core principle 8 | standard; self-review check | |
| GD-12 | Give opposition and the tools to beat it; the right frustration | game-design SKILL §4 G-08; principles.md §5; loops.md §1 (each obstacle names its counter) | standard; self-review check | |
| GD-13 | Fairness comes from clear expectations and consistency | game-design SKILL §4 G-08, G-20; principles.md §5, §8; documents.md §7 | standard; self-review check | |
| GD-14 | Place luck and skill on purpose | game-design/references/principles.md §5 (where randomness sits; sim check) | standard; self-review check | |
| GD-15 | Prove the fun with the crudest prototype before art | game-design SKILL §4 G-05; loops.md §5 (crudest form, verdict before art); preproduction §4 P-15, §3 step 5; role file Work method 5 | standard; stage (grey-box verdict gate); self-review check | |
| GD-16 | Cosmetics never change the gameplay read or cost gameplay | game-design SKILL §4 G-22; systems-economy.md §8; review.md §7 character | standard; quality bar; self-review check | |
| GD-17 | Cosmetics refresh repeated play without changing balance | game-design/references/systems-economy.md §8 intro; playtest-live.md §4 | standard | |
| GD-18 | A new character starts from the roster gap | preproduction §4 P-19; documents.md §8 role card; playtest-live.md §4 | standard; step | |
| GD-19 | A mode change re-checks the whole roster | game-design/references/playtest-live.md §4 (mode change re-checks every unit; check: a balance-pass list covering every unit ships with the change) | standard; self-review check | |
| GD-20 | Choose themes from data; combine proven themes and tune the maturity | game-concept §4 C-18; game-design/references/systems-economy.md §8 (themes from data, maturity); pitch-template.md field 9 | standard | |
| GD-21 | Low mental load on the player's own character | game-design/references/review.md §7 character (own moves identifiable from behind); handoffs.md §2 animator row (key pose that must show each move) | self-review check | |
| GD-22 | Find the genre's demands first | preproduction §4 P-14, §3 step 1; game-design SKILL §3 step 1; review.md §1 step 1; role file Work method 1 | standard; step | |
| GD-23 | The map is the board: map mechanics stay in the background | game-design/references/spaces.md §1; SKILL §4 G-23 | standard; self-review check | |
| GD-24 | A level is a puzzle with ability-shaped holes | game-design/references/spaces.md §2 (puzzle with tool-shaped holes) | standard; self-review check | |
| GD-25 | Build conflict into the objective; tie it to the world's story | game-design/references/spaces.md §2 (conflict sentence and story reason) | standard; self-review check | |
| GD-26 | Plan the first seconds from the round-start positions | game-design/references/spaces.md §3 (spawn-to-contact times) | step; self-review check | |
| GD-27 | Neither side takes neutral space too easily | game-design/references/spaces.md §3 (neutral space parity) | self-review check | |
| GD-28 | Cover gives both sides options and a counter | game-design/references/spaces.md §4 (cover with counters) | standard; self-review check | |
| GD-29 | Turn a dead boundary into a risk and reward | game-design/references/spaces.md §5 (dead boundary as risk and reward) | standard | |
| GD-30 | Every hazard has written rules | game-design/references/spaces.md §5; preproduction/references/documents.md §7 hazard sheet; principles.md §10 | standard; template; self-review check | |
| GD-31 | Art stays inside the blockout's gameplay | game-design/references/spaces.md §6; review.md §7 stage (collision diff) | standard; self-review check | |
| GD-32 | Hide small secrets that reward discovery | game-design/references/spaces.md §8 | standard; self-review check | |
| GD-33 | A map is never done; new worlds are an escape | game-design/references/spaces.md §8; playtest-live.md §4 | standard | |
| GD-34 | Feedback follows the real outcome: a small cue on input, the big layer on confirmed success | game-design SKILL §4 G-19, §5, §6; principles.md §7; preproduction/references/documents.md §6; review.md §7 feature; core principle 19 | standard; quality bar; self-review check; core principle | |
| GD-35 | Paid random reveals are honest | game-design SKILL §4 G-22, §5; systems-economy.md §9; review.md §7 UI (odds before buy) | standard; rule; self-review check | |
| LC-01 | Reserve the gameplay colours; keep them, and fast motion, out of decoration | game-design/references/principles.md §10; preproduction/references/growth-order.md §1 step 3 inputs; spaces.md §7; review.md §7 stage | standard; self-review check | |
| LC-02 | Keep a colour-role table: one hue never means both help and harm | game-design/references/principles.md §10 (one hue never two meanings); growth-order.md step 3; review.md §7 effect | standard; self-review check | |
| PI-03 | Closing doors: from broad to narrow, never reopen | preproduction §3 step 2, §4 P-21, §5; documents.md §1 closed doors; game-concept §3 step 8, §4 C-20, §5; rubric-taste-evidence.md §2; core principle 15 | step; rule; core principle | |
| PI-04 | Block out first, in the engine, and play it before detail | game-design SKILL §4 G-05; loops.md §5; role file Work method 5 | stage | |
| PI-14 | "It would be cooler" is new scope: log it | preproduction §3 step 7, §4 P-21; role file (Working with other agents); core principle 6 | rule; core principle | |
| PP-15 | Spend expensive features only where they earn it | preproduction §4 P-21; documents.md §8 cost flags | standard | |
| PP-26 | Environment order: blockout, composition, kit, dressing, mechanics, then light and polish | game-design/references/spaces.md §6 (order: grey box ... lighting last) | step order | |
| RH-03 | Every effect tells a beginning, a middle and an end | game-design/references/review.md §7 effect; preproduction/references/documents.md §6 named stages; core principle 8 example | self-review check | |
| RI-01 | Concept work solves a problem; it is a functional vehicle, not a nice picture | preproduction/references/growth-order.md §1 "How every step runs" (each option states problem, clarity effect, build cost); P-16 | step | |
| RI-02 | Show options at equal, low finish on a clean, labelled sheet | game-concept §3 step 6, §4 C-20, §6; pitch-template.md §4 item 2; growth-order.md §1 (equal low finish) | step; self-review check | |
| RI-03 | Know the problem, the constraints and the end before making anything | preproduction §4 P-16, §3 step 5; handoffs.md §1; core principle 13 | standard; core principle | |
| RI-17 | Take the big swings at concept stage | game-concept §3 step 3, §4 C-16, §6; growth-order.md §1 (one big swing per step) | step; self-review check | |
| RI-18 | Each option gets its own hook from a different source | game-concept §3 step 3-4, §4 C-17, §6; idea-method.md §3 hook sources, §4 diagnosis | step; self-review check | |
| RI-19 | Present options with your pick and the reasons; then iterate | preproduction/references/growth-order.md §1 "How every step runs" (3); pitch-template.md §4; core principle 14 | step | |
| RI-21 | The first output is a warm-up; reject the typical idea | game-concept §3 step 3, §4 C-16, §6; idea-method.md §1 step 3 | step; self-review check | |
| RI-23 | Bring in one unexpected element from outside the genre | game-concept §3 step 3, §4 C-17; idea-method.md §3 (one unexpected element, outside-games source, why it repels) | step; self-review check | |
| RI-24 | Act it out: agents write the performance beat by beat | preproduction/references/growth-order.md §1 step 4 (key moments as timed stages); documents.md §1 key moments row | step | |
| RI-27 | Design a variant through a narrative lens | game-design/references/systems-economy.md §8 (a variant is a story); handoffs.md §3.7 story | standard; example | |
| RI-29 | Find the hook that makes the subject compelling | game-concept/references/idea-method.md §3 (one-line hook per candidate); pitch-template.md field 4 | step | |
| SD-01 | Sound has three jobs and tells the story with every layer | game-design/references/principles.md §7 (every state change has a two-channel cue); review.md §7 effect (screen covered) | standard; self-review check | |
| SD-02 | Every cue names its emotion, not only its object | preproduction/references/handoffs.md §2 sound row (intended emotion) | brief requirement | |
| SD-04 | The sound theme comes from what the thing does in play | preproduction/references/handoffs.md §2 sound row (mechanic verb); review.md §7 effect | brief requirement; self-review check | |
| SD-05 | Stage the action: one sound per named stage | preproduction/references/documents.md §6 (named stages shared by all crafts); handoffs.md §2 sound row | template; brief requirement | |
| SD-06 | Attach sounds to game events, listed and tested | game-design/references/principles.md §7 (every state change has a cue); handoffs.md §2 sound row (state changes that need a cue) | standard; brief requirement | |
| SD-09 | Set how far each sound carries by its importance | preproduction/references/handoffs.md §2 sound row (how far it must carry); review.md §7 effect | brief requirement; self-review check | |
| SD-16 | A shot is built from five layer jobs | - | - | rejected: Building a shot from five layer jobs is sound-design craft; my brief states the job, priority and verb (handoffs.md §2 sound row) and the sound designer decides the layers. |
| SD-21 | Every weapon and the whole game get a signature sound | preproduction/references/handoffs.md §2 sound row (signature identity); review.md §7 effect | brief requirement; self-review check | |
| SD-22 | Characters sound like who they are, and sound telegraphs their state | game-design/references/principles.md §8 (rising cue before a break); review.md §7 effect | standard; self-review check | |
| SD-23 | Every floor material is a footstep callout | game-design/references/spaces.md §6 (material table drives footsteps); review.md §7 stage (walk capture with audio); handoffs.md §2 sound row | standard; self-review check | |
| SI-03 | Theme fit can rule out an otherwise cool idea | game-concept §3 step 5, §4 C-18, §6; core principle 11 | standard; self-review check | |
| SI-05 | Make it for a specific audience, and give fans what they want | game-concept §3 step 1, §4 C-18, §6; pitch-template.md field 4 | step; self-review check | |
| SI-10 | Proportions are read against the cast | preproduction/references/documents.md §8 (build against the cast); review.md §7 character (lineup) | standard; self-review check | |
| SI-11 | An update keeps the kernel and trims what is dated | game-design/references/systems-economy.md §8 (loved traits kept, dated traits trimmed) | standard | |
| SI-12 | Each theme needs its own niche | game-design/references/systems-economy.md §8 (niche); game-concept §3 step 5, §4 C-18; playtest-live.md §4 | standard; self-review check | |
| SI-13 | Refresh a tone by pushing to the extreme, then pulling back to the brand | game-design/references/systems-economy.md §8 (extreme pass, pulled-back pass) | step | |
| SI-19 | A cohesive set, with a documented break for the top tier | game-design/references/systems-economy.md §8 (tiers: documented top-tier break); core principle 11 | standard | |
| SS-05 | Shape language carries meaning: sharp is danger, round is friendly | preproduction/references/documents.md §8 shape intent; growth-order.md step 3; review.md §7 character; core principle 5 | standard; self-review check | |
| SS-19 | Design the group silhouette | - | - | rejected: Group silhouette staging is composition craft for marketing art, cutscenes and lobby poses (art director, marketing, film director). My part, what must read first in a scene, is the read rank (documents.md §9). |
| UI-01 | Flow first, then style, then motion; polish cannot save a bad flow | game-design/references/review.md §7 UI (taps per task vs flow sheet) | self-review check | |
| UI-02 | Each element: one thing to understand, one action it leads to | game-design/references/review.md §7 UI (one thing, one action) | self-review check | |
| UI-03 | Design for the audience and the device: phone first | preproduction §3 step 1 (phone-first parameters); review.md §7 UI (phone-size prototype); core principle 2 | step; self-review check | |
| UI-04 | The genre sets how much UI the game needs | preproduction/references/documents.md §9 information per moment; P-20; review.md §7 UI | template; standard; self-review check | |
| UI-05 | UI is every screen and state, not only the HUD | preproduction/references/documents.md §9 screens and states; review.md §7 UI | template; self-review check | |
| UI-09 | Proximity creates meaning | game-design/references/review.md §7 UI (value next to the thing it describes) | self-review check | |
| UI-10 | Layout sets reading speed: critical information in fixed, prominent places | preproduction/references/documents.md §9 (read speed, critical about 1 s PROPOSAL); review.md §7 UI | template; self-review check | |
| UI-13 | Motion goal: intention, one attention motion at a time | game-design/references/review.md §7 UI (only the next action moves) | self-review check | |
| UI-18 | Errors and denials say what is wrong and how to fix it, at the control | game-design/references/principles.md §7 (refusals at the control); documents.md §6; review.md §7 UI and feature | standard; self-review check | |
| VC-05 | Give each screen layer its own value and saturation band | game-design/references/principles.md §9 (environment is the backdrop; UI and effects own the extremes); spaces.md §7; review.md §7 stage (grayscale, look_check value) | standard; self-review check | |
| VH-01 | Rank what must be seen; UI and VFX first, characters second, environment last | game-design SKILL §4 G-21; principles.md §9; documents.md §9 read rank; core principle 3 | standard; template; self-review check | |
| VH-02 | Rank loudness across a set: if everything is loud, nothing is | game-design SKILL §4 G-21; principles.md §9 (loudness tiers); documents.md §9 | standard; template | |
| VH-06 | The source of power is the primary read | preproduction/references/documents.md §8 (source of power reads first); review.md §7 character | standard; self-review check | |
| VH-07 | Recognisable in under a second beats unique | preproduction/references/documents.md §8 nearest look-alike; review.md §7 character (thumb_check icon at 150x150) | standard; self-review check | |
| VH-10 | Size signals importance | preproduction/references/documents.md §8 (size follows rank); review.md §7 character (lineup); hook-promise.md §3 item 7; core principle 5 | standard; self-review check | |
| VR-05 | Effects follow a game-wide shape code | game-design/references/principles.md §10 (one shape code); review.md §7 effect (type reads in grayscale) | standard; self-review check | |
| VR-06 | Budget each effect's footprint for the worst-case crowd | game-design/references/principles.md §9 (worst-case crowd); review.md §7 effect | standard; self-review check | |
| VR-07 | Never cover what the player needs to see; stay low | game-design/references/principles.md §9; review.md §7 effect (never covers players, HUD, shop) | standard; self-review check | |
| VR-19 | Rate each effect per viewer and build it for the viewer's relation | game-design/references/principles.md §9 (per viewer); handoffs.md §2 vfx row, §3.6; review.md §7 effect (two-client capture) | standard; example; self-review check | |
| VR-20 | The drawn danger area is the real hit area, from warning to last tick | game-design SKILL §4 G-20, §6; principles.md §8; documents.md §7; handoffs.md §3.6; review.md §7 feature and effect | standard; template; example; self-review check | |
| VR-21 | Camera and screen punches are rare, local, rotation-only and gated by importance | game-design/references/principles.md §9 (camera punches rare, top tier, local); documents.md §6 channels | standard; self-review check | |
| VR-22 | Hit-stop is local, short and scaled by hit strength | game-design/references/principles.md §7 (hit-stop local and scaled, PROPOSAL values); review.md §7 effect | standard; self-review check | |
| VR-23 | Every intense channel has an off path that keeps the information | game-design SKILL §5 rule (safety faults block release); principles.md §9 comfort; documents.md §6; review.md §7; core principle 20 | rule; standard; self-review check; core principle | |
| VR-24 | Frequent effects are shorter, quieter, merged and capped | game-design/references/principles.md §7 (frequent events quiet, merged); documents.md §6 frequency; review.md §7 effect | standard; self-review check | |
| VR-26 | Pulse and blink rates carry meaning: slow is safe, fast is urgent, never above 3 Hz | game-design/references/principles.md §9 (pulse rates, 3 per second cap); review.md §7 effect | standard; self-review check | |
| WL-01 | Gameplay readability beats beauty; test it in the busiest moment | game-design/references/spaces.md §7; review.md §7 stage; core principle 1 | standard; self-review check; core principle | |
| WL-02 | Items must be identifiable on the ground, even partly hidden | game-design/references/spaces.md §7 (items 30-50 % hidden still named) | standard; self-review check | |
| WL-03 | Every piece says "what I am" and "what you can do here" | game-design/references/spaces.md §7 (what I am, what you can do here) | standard; self-review check | |
| WL-04 | One gameplay constraint, many fictional answers | game-design/references/spaces.md §5 (boundary from 2-3 fictional answers) | standard; self-review check | |
| WL-06 | Rank the environment work: it is 90 % of the screen | game-design/references/spaces.md §6 (rank environment work with the environment designer); role file partners table | step | |
| WL-07 | The first view tells where you are and what to do | game-design/references/spaces.md §7 (first view); review.md §7 stage | standard; self-review check | |
| WL-08 | Spawns first, then the route to the objective | game-design/references/spaces.md §3 (spawns first) | step order | |
| WL-09 | Paths face forward; no doubling back in multiplayer maps | game-design/references/spaces.md §3 (paths face forward; check: walk capture from spawn to each objective never turns the camera back) | standard; self-review check | |
| WL-10 | Keep the layout simple: two ways in per side | game-design/references/spaces.md §3 (two ways in per side, default; check: ways in counted per side per objective) | standard; self-review check | |
| WL-11 | One orientation convention across all maps | game-design/references/spaces.md §3; documents.md §1 vision record (orientation conventions) | standard; self-review check | |
| WL-14 | Flat play spaces; every height change is intentional | game-design/references/spaces.md §4 (flat play, intentional height list) | standard; self-review check | |
| WL-15 | Predictable geometry: players lose to opponents, not to the map | game-design/references/spaces.md §4 (predictable collision) | standard; self-review check | |
| WL-16 | Name dead space and oversized areas in self-review | game-design/references/spaces.md §9 (dead space in self-review) | self-review check | |
| WL-18 | Materials follow gameplay rules | game-design/references/spaces.md §6 (materials follow gameplay rules); review.md §7 stage | standard; self-review check | |
| WL-22 | Environmental storytelling: someone lives here, time has passed | game-design/references/spaces.md §7 (2-3 story facts at backdrop contrast; check: a fresh reader states one story fact per main area) | standard; self-review check | |
| WL-23 | Give each zone or team an identity symbol | game-design/references/spaces.md §7 (identity symbol per zone; check: visible from its entry at the game camera on a phone) | standard; self-review check | |
| WL-29 | Plan routes in player metrics: seconds at walk speed, ledges against jump height | game-design/references/spaces.md §3 (route table in seconds, ledges vs jump height); review.md §7 stage | standard; self-review check | |
| WL-30 | Score a level review on ten fixed checks | game-design/references/spaces.md §9 (fixed list every time; a re-review re-rates every check) | self-review check (the 0-2 score and total out of 20 rejected: the kit rates Pass / Fail / Unproven with no totals, game-design §5 and level-design §6; proposal to level-design) | |
| WT-01 | Anticipation must read: long enough to react to, tight enough to feel strong | game-design SKILL §4 G-20; principles.md §8 (reaction window, PROPOSAL values); documents.md §7; handoffs.md §2 animator row, §3.6 | standard; template; example; self-review check | |
| WT-02 | One consistent physics lets players predict | game-design/references/principles.md §10 (one physics); documents.md §1 vision record; growth-order.md step 3 | standard; self-review check | |
| WT-03 | Motion sets the emotional tone; giants move slowly | game-design/references/principles.md §3 (giants slow); review.md §7 character; core principle 10 example | standard; self-review check | |
| WT-21 | Fast contact; delete frames until the hit lands | preproduction/references/handoffs.md §2 animator row (player-action response budget); principles.md §8 (own actions tight) | brief requirement (frame-deleting technique rejected as animation craft) | |
| WT-22 | Land low and strong, with tension; elbows sink | - | - | rejected: Landing poses (low, strong, elbows sink) are animation craft with no design decision in them; the animator's books carry them. |
| WT-24 | Secondary motion adds perceived value | game-design/references/systems-economy.md §8 tiers (premium keeps secondary motion) | standard | |

Untagged findings used (not tagged game-designer in the matrix; added because they change how this role works):

| ID | Title | Landed in (file § section) | As | Or rejected: reason |
| --- | --- | --- | --- | --- |
| CC-03 | Build for the next craft: ask what they need first | preproduction SKILL §3 step 3; handoffs.md §1 (ask each craft what it needs first); role file partners table | step | |
| CC-04 | The concept leaves room for the next crafts' decisions | preproduction SKILL §4 P-05 (motion and effect ideas are intent, not timing) | standard | |
| CD-07 | The fantasy must survive every real view | game-concept §4 C-08 (first image from the game camera); preproduction §4 P-03; growth-order.md step 1 | standard | |
| CD-28 | Represent ethnicity and culture accurately | game-design/references/systems-economy.md §8 (culture and ethnicity represented accurately) | standard | |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | game-design/references/playtest-live.md §1b (judge in the real build at the game camera, moving, with effects on); core principle 2 | standard | |
| CR-07 | No grand reveals: show early and often, partner crafts first | preproduction SKILL §3 step 3 (rough states to partner crafts, no grand reveals) | step | |
| CR-08 | Diagnose by layer; "not happy" may mean "not done" | game-design/references/review.md §8 (diagnose by layer, re-check other layers) | step | |
| CR-10 | Keep the right mistakes: follow a happy misread | game-design/references/playtest-live.md §1 (a fun misread may become the design) | standard | |
| CR-12 | When every option meets the brief, choose and commit | game-design/references/review.md §8 (when every option meets the brief, choose and commit) | standard | |
| CR-17 | Say what each input can prove; end with a could-not-check list | game-design SKILL §3 step 3, §6; playtest-live.md §1b (what each input can prove, could-not-check list); review.md §5 finding template | standard; self-review check | |
| PI-02 | Gates freeze decisions: rough, approved direction, materials, polish | preproduction SKILL §3 step 2 (the decision freezes the step); growth-order.md §1 | step | |
| PI-07 | One named problem per pass; fix the worst first | game-design SKILL §3 step 8; review.md §8 (one named problem per pass, worst first) | step | |
| PI-09 | Not precious: most attempts fail, so delete, redo and let go | game-concept §4 C-16 (most candidates are meant to die); core principle 15 | standard | |
| PI-12 | Know when it is done: written stop criteria, repeating notes | preproduction SKILL §6 (stop criteria); core principle 18 | self-review check | |
| PI-13 | Finish a concept only as far as the next maker needs | preproduction/references/growth-order.md §1 (finish only as far as the next step needs); preproduction SKILL §6 | step; self-review check | |
| RI-22 | Vary one element per option, label them, merge the best two | game-concept/references/idea-method.md §3 (expand one named element per variant); game-concept SKILL §3 step 4 | step | |
| RI-28 | One message, one symbol, before drawing | game-concept §4 C-08 (one message, one symbol); hook-promise.md §3 item 7 | standard | |
| UI-19 | Counters tell the truth; their animation is decoration | game-design/references/principles.md §7 (counters tell the truth); documents.md §6; review.md §7 UI | standard; self-review check | |
| VR-16 | Ambient environment effects: tiny, slow, partly hidden | game-design/references/review.md §7 stage (ambient effects off sight lines) | self-review check | |
| WL-05 | Hazards explain themselves | game-design/references/spaces.md §5 (a hazard shows its source and containment); documents.md §7 | standard | |
| WL-20 | It must read at the lowest graphics setting | game-design/references/spaces.md §7 check (lowest graphics setting); role file partners table (studio-operator) | self-review check | |

### b. Universal principles

Rows in `game-design` SKILL §7 use the master's numbers (1-20) without the "UP-" prefix, because book bodies carry no library IDs.

| UP-ID | Applies (yes/no + reason) | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: every rule I write must read in play; art and mechanics promise the same thing; threats telegraph | `game-design` §7 row 1 (example: lava moat edge; check: busiest capture on a phone viewport) |
| UP-02 | yes: design is proven in the real build, camera, phone size, full server | §7 row 2 (example: sell pad under the thumbstick; check: every verdict names its capture, paper-only = Unproven) |
| UP-03 | yes: I rank what must be noticed per scene and tier rewards and celebrations | §7 row 3 (example: boss arena read rank; check: blurred view, first-noticed = rank 1) |
| UP-04 | yes: core loop in grey box before features, systems and production art | §7 row 4 (example: "Fly or Die" launch test with a plain Part; check: dated loop verdict before feature specs and before the first production art brief) |
| UP-05 | yes: roles and threats read from shape and size; I set the intent in the role card | §7 row 5 (example: tiny boss vs huge harmless slime; check: lineup size rank = threat rank) |
| UP-06 | yes: a feature earns its place; HUD sized by need; "cooler" is scope | §7 row 6 (example: story cutscene filed in a tycoon; check: traces to target experience, tickets after the gate) |
| UP-07 | yes: rules, tells, physics, colour and shape roles, hazards behave the same everywhere | §7 row 7 (example: poison not green; check: hazard sheet, same tell in two captures) |
| UP-08 | yes: I set the windows and stage names others key to; tension rises to the climax | §7 row 8 (example: rebirth stages; check: named stages, intensity plot, celebration length measured) |
| UP-09 | no: pushing forms, poses, effects and sounds past real is craft execution; the master does not list game-designer. My side (what must read and how strongly) is rows 1 and 3 | listed as not applying in the §7 intro |
| UP-10 | yes: behaviour, verb and movement pattern say what a thing is before art; tuning sets tone | §7 row 10 (example: heavy golem timing; check: plain-block test) |
| UP-11 | yes: themes fit the tone; variants keep gameplay anchors; top tier breaks only by decision | §7 row 11 (example: sci-fi skin rejected in a whimsical farm game; check: tone words and anchors in each brief) |
| UP-12 | no: controlled variation of surfaces, motion and sound is craft execution; the master does not list game-designer. The design cousin (variety must change decisions) is `loops.md` §6 item 8 | listed as not applying in the §7 intro |
| UP-13 | yes: every spec and brief opens with problem, target experience, parameters, success test | §7 row 13 (example: shop brief rewritten from "make it fun"; check: brief has the four items first) |
| UP-14 | yes: warm-up, distinct options, an atypical one, equal finish, one reasoned pick | §7 row 14 (example: three flood mechanics for a dam game; check: count, families, reasons per rejection) |
| UP-15 | yes: paper and grey box first; steps freeze; closed doors logged; let go of own ideas | §7 row 15 (example: closed PvP theft not re-proposed; check: closed-doors list) |
| UP-16 | yes: goal questions, problem-behind-the-note, one named problem at a time, honest recap | §7 row 16 (example: "make the boss easier" → a read problem; check: goal word in every question, one weakness named) |
| UP-17 | yes: specs give each craft what it needs as tuning keys and leave the how open; costs written | §7 row 17 (example: slam radius as a tuning key the effect reads; check: receivers restate with no questions) |
| UP-18 | yes: stop criteria; documents go only as far as the next craft needs | §7 row 18 (example: spec stops at its 15 fields; check: stop criteria in the brief, round with no new notes ends) |
| UP-19 | yes: attempt cue at once, outcome layer on confirmation, tiers by learnable causes, honest paid reveals | §7 row 19 (example: sell flow; check: rejected-request capture, five outcomes distinct with sound off, identical paid windups) |
| UP-20 | yes: no meaning on one channel; comfort settings with off paths are part of the spec | §7 row 20 (example: low-health warning in three channels; check: grayscale + sound off + reduced motion capture) |

### c. Old book changes (old text at `df13ff4`)

New text added without replacing anything (new craft-core rows G-17..G-23, P-13..P-21, C-15..C-20, §7 core principles, `principles.md` §7-§10, `systems-economy.md` §8-§9, `review.md` §7-§8, `documents.md` §6-§9, `playtest-live.md` §1b, `spaces.md`, the role file's two new sections, handoffs §3.6-§3.7) is not listed. Every author line of a changed file got the J018 phrase (not listed per file).

| Old text (file:line at df13ff4) | Kept / sharpened / replaced by (new location) / moved / removed | Why |
| --- | --- | --- |
| `.agents/roles/game-designer.md:14` intro ("Your bar: concepts players want…") | sharpened (same place) | adds the bar for specs (every action answers, threats read, look matches behaviour) and the three working habits (name the experience, crudest prototype first, judge at the game camera) |
| `game-designer.md:18` skills by task | sharpened | `game-design` §7 for every task; `review.md` §7 for review slots |
| `game-designer.md:19` game facts | sharpened | adds the job's closed-doors list |
| `game-designer.md:25-27` direction lead, check-ins, reviews | sharpened | names the role card, hazard sheets, information list, importance; points each review slot to its check list (`review.md` §7) |
| `game-designer.md:32` "Craft practice from Riot's artists and designers: `knowledge/jobs/J016-orchestration/riot-extracts.md` §4" | replaced by "Craft standards: your own books; `game-design` §7" (same section) | owner spec: role files point to their own books, not to the J016 card; the material now lives in the books |
| `game-designer.md:35-41` work method steps 1-7 | replaced by steps 1-9 (same section); all old content kept | step 1 adds target experience and parameters; step 2 warm-up, hook sources, tile-size check; step 3 options, goal question, freeze; step 4 the new sheets; new step 5 "prove before art"; new step 7 craft-output review; old 6-7 become 8-9 |
| `game-designer.md:44-47` working with others | sharpened | digest items as goal questions; "cooler" is new scope; a note with a solution is a pointer to a problem |
| `game-designer.md:53` hand-back | sharpened | every hand-back ends with an honest recap |
| `game-concept/SKILL.md:11` §1 | sharpened | points to the core principles |
| `game-concept/SKILL.md:16, 18` §2 rows | sharpened | names the warm-up and hook sources; hook check grew to 12 items |
| `game-concept/SKILL.md:26` step 1 intake | sharpened | adds closed directions and the audience's "want" line |
| `game-concept/SKILL.md:28` step 3 "Diverge" | replaced by step 3 "Warm up, then diverge" | the first ideas are the expected ones; each candidate needs its own hook source, one from outside games, one big swing |
| `game-concept/SKILL.md:29-33` steps 4-8 | sharpened | one named element per variant; critic flags (no decision, tone, niche); equal finish and tile check; goal question and conviction; closed-doors record |
| `game-concept/SKILL.md:45` C-08 first image | sharpened | from the game camera, scale (outsized object vs player), one message and one symbol, tile-size check |
| `game-concept/SKILL.md:58` young-audience rule | sharpened | adds: a theme that could read badly moves onto a motif or is dropped |
| `game-concept/SKILL.md:62, 64` self-check lines | sharpened | target experience in every pitch; hooks from different sources, outside source, big swing |
| `game-concept/SKILL.md:65, 67-69` self-check lines | sharpened | goal question; closed directions; sensitivity; conviction |
| `game-concept/references/idea-method.md:12, 14, 15, 44` funnel steps 3, 5, 6 and batch diagnosis | sharpened | warm-up round, hook-source column, critic flags |
| `game-concept/references/pitch-template.md:8` "8 lines" | sharpened to 9 lines | the card gains an "Experience:" line |
| `pitch-template.md:28-30, 34` record fields 3, 4, 5, 9 | sharpened | target experience; hook source and audience; game-camera first image with tile check; themes combined, maturity, niche, sensitivity |
| `pitch-template.md:44, 47` presenting items 2, 5 | sharpened | equal finish, the moment told with conviction; goal question instead of an open "decide" |
| `game-concept/references/hook-promise.md:28` test item 6 | kept as item 6 (repair round 1 restored the order); new item 7 (tile-size first-image check) appended | the first image is checked at the size players meet it before it reaches the owner |
| `game-concept/references/rubric-taste-evidence.md:17, 20` RB1, RB4 | sharpened | RB1 needs a named target experience; RB4 fails a loop with no opposition or real decision |
| `rubric-taste-evidence.md:37` taste-log rule | sharpened | goal questions; closed directions |
| `game-design/SKILL.md:11` §1 | sharpened | adds craft-output reviews and the core principles |
| `game-design/SKILL.md:16-18, 20-22, 24` §2 rows | sharpened | new content in each reference; `spaces.md` row added |
| `game-design/SKILL.md:29-37` steps 1-9 | sharpened (same numbers) | parameters and target experience first; four parts; input labels; look vs behaviour; game camera and behaviour read; rejected request and worst-case crowd; one problem at a time; honest recap |
| `game-design/SKILL.md:42-43` G-01, G-02 | sharpened | never "fun", file what serves another kind; tag notes goal or tactic |
| `game-design/SKILL.md:46` G-05 | sharpened | crudest form, stand-in colours, no production art brief before the verdict |
| `game-design/SKILL.md:49` G-08 | sharpened | every obstacle names its counter; same tell every time |
| `game-design/SKILL.md:56` G-15 | sharpened | a flat effect: outcome link and timing before size |
| `game-design/SKILL.md:60, 63, 65` rules | sharpened | PROPOSAL starting values; near-miss and early celebration as dark patterns; closed directions |
| `game-design/SKILL.md:67-73` §6 self-check | sharpened and extended | input status labels, game-camera judging, threats, feedback, read order, notes as problems, honest recap |
| `game-design/references/loops.md:50, 55` check items 4, 9 | sharpened | feedback: attempt vs confirmed outcome; promise: look matches behaviour |
| `game-design/references/principles.md:27-28, 31-32` §3, §4 | sharpened with checks | tuning as tone, theme families, numbers passed to art, mismatch list; progress midpoint, arc in space, intensity plot |
| `game-design/references/playtest-live.md:10` protocol step 5 | sharpened | failure-attribution question; goal questions; requested fix → underlying problem |
| `game-design/references/review.md:6-7, 11, 17, 44` steps 1, 2, 6, 12 and the finding template | sharpened | parameters; four parts; input labels; honest recap; template gains "goal or tactic" and input status |
| `preproduction/SKILL.md:11` §1 | sharpened | points to the core principles |
| `preproduction/SKILL.md:17-21` §2 rows | sharpened | names the new sheets, the progression lead and `spaces.md` |
| `preproduction/SKILL.md:24-30` steps 1-7 | sharpened (same numbers) | parameters first; options, goal question, freeze, closed doors; ask crafts' needs, no grand reveals; the four sheets, behaviour before looks; shared header and the grey-box gate; cooler is scope |
| `preproduction/SKILL.md:37` P-03 | sharpened | the fantasy must survive the real views (tiny, from behind, in motion) |
| `preproduction/SKILL.md:39` P-05 | sharpened | motion and effect ideas are intent, never timing curves |
| `preproduction/SKILL.md:53` invented-numbers rule | sharpened | starting values written as PROPOSAL with their test; new rule: no production art brief without the grey-box verdict |
| `preproduction/SKILL.md:57-62` §6 self-check | sharpened and extended | options and closed doors; parameters; feedback stack; threat and hazard sheets; role cards; read rank; grey-box citation; stop criteria |
| `preproduction/references/documents.md:12, 16` vision record and key-moment rows | sharpened | target experience, parameters, physics and motion language, orientation conventions; timed stages; role-card and closed-doors rows added |
| `documents.md:47, 51, 54, 62` feature-spec fields 2, 6, 9 and the experience test | sharpened | four parts; named timing stages and sheets; feedback stack and read rank; plain-block test |
| `preproduction/references/growth-order.md:36, 39` what each lead needs; trace-back | sharpened | role cards, mechanics and numbers, motif sharing; animator at design time; grey-box verdicts and feedback stacks in readiness |
| `preproduction/references/handoffs.md:6` shared header (five items) | sharpened to the full shared header | target experience, parameters, timing stages, read rank, problem, constraints, success test, sell list; ask crafts' needs first |
| `handoffs.md:13, 15, 16` trend-scout "(building, J004)", art-director "(planned)", architect "(planned)" | sharpened (status words removed; art-director skills now `art-direction, art-review, reference-images`) | the roles are built; the old skills column named a placeholder |
| `handoffs.md:14, 17-22` marketing, UI, VFX, sound, animator, environment, progression rows | sharpened | what each craft needs from me (lists in the rows) |
| `handoffs.md:26, 64, 103, 141` example headings "(planned role)" | sharpened (status words removed) | the roles are built |
| `handoffs.md:76` marketing example skills `[game-concept, reference-images]` | replaced by `[marketing-design, marketing-craft, reference-images]` | marketing now has its own skills |
| `handoffs.md:115` art-director example skills with "until an art skill exists" | replaced by `[art-direction, art-review, reference-images]` | the art skills exist |
| `handoffs.md:178` §3.5 pattern | sharpened | points to the new worked examples §3.6, §3.7 |

Removed: nothing. No old rule was shown wrong by the library; the closest tension (a scored 0-2 level review with a total) was not adopted because the kit's no-totals rule stands (table a, WL-30).

## Repair round 1 (stage 3 review `reviews/game-designer-rev1-reviewer.md`, 2026-10-22)

The keep list is kept whole: G-17..G-23 and the §7 rows were tightened, and each keeps its example and check.

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (blocking) | `game-design/references/systems-economy.md` §9 first bullet rewritten to the Roblox MUST rules (visible before the buy button, sum 100 %, never covered or animated, updated while a boost is active or after a once-only win, pop-up only for a long list from a worded "Info" or "Details" label, never a bare icon); §9 check adds "odds changed in a capture with a boost active"; `review.md` §7 UI line the same. Proposals: library GD-35 wording (lead), and the `platform-policy` row reworded so it no longer says "static" |
| F2 (blocking) | Checks added: `spaces.md` §3 check (walk capture never turns back: WL-09; ways in counted per side per objective: WL-10); `spaces.md` §7 check (surprise outside the top focus in grayscale and not spotted early: CF-13; a fresh reader states one story fact per main area: WL-22; identity symbol visible from its entry on a phone: WL-23); `principles.md` §3 check (theme family per item: GD-08); `playtest-live.md` §4 (balance-pass list for every unit: GD-19); `preproduction/references/documents.md` §8 role-card check (hero signature item parts and moving pieces counted: CD-17). Table a rows now say "self-review check" |
| R1 | Role file Read first item 2: "after a compaction, re-read `game-design` §7". `game-design` SKILL §7 rewritten shorter (one phrase per cell, depth pointed to the references; rows 1, 3, 7, 8, 19, 20 no longer restate `principles.md`) and G-17..G-21 tightened: SKILL.md 24,987 to 22,263 characters, §7 now starts at character 15,715 (was 16,060). Steps, rules and §6 stay inside the first 5 k tokens; §7 ends about 5.5 k tokens in, so the re-read line in the role file covers the rest |
| R2 | One source per number: `documents.md` §6 (pending state, celebration length, merge window) and §7 (reaction windows) point to `game-design/references/principles.md` §7 and §8; SKILL §7 row 8 no longer says "before 2 s"; `review.md` §7 UI read time points to `documents.md` §9 (its one source). Kept on purpose: the example briefs in `handoffs.md` §3.6-§3.7 write the value out with its source comment, because a brief's `fixed` values are written out with a source (`rules/messages.md` §2); the footprint comment now names `systems-economy.md` §8 as the one source |
| R3 | `preproduction/references/handoffs.md` §1: a header item a later growth step settles is written `TBD (step N)` (read rank step 3, timing stages steps 4 and 7), never invented |
| R4 | `game-design` SKILL §3 step 1: "no review starts without them, or without assumed values written down as assumptions" |
| R5 | `preproduction/references/growth-order.md` §1: step 6 "Settles" adds the loop's dated grey-box verdict before step 7 specs features (a FAIL sends the loop back); the step 6 design-input row says the same; SKILL §7 row 4 check names growth step 7 |
| R6 | Tools named: `look_check.py silhouette` (area and bbox per capture, `--compare` aligned IoU, `--component N` per unit) in `systems-economy.md` §8 check, `review.md` §7 character (black-fill image, lineup areas, nearest-neighbour IoU as a flag), `documents.md` §8 check, `handoffs.md` §3.7 C2, SKILL §7 row 5; `clip_metrics.py` (`onset_ms`, `visible_ms`, `peak_ms`; fixed-camera frame folder `f###_<ms>ms.jpg` from the press) in `principles.md` §7 checks, `documents.md` §6 checks, `review.md` §7 feature and effect lines; the role file's studio-operator row asks for frames named for it. Found while checking: the tool's regex needs `ms` before `.jpg` (its docstring omits it) and onset counts from a tenth of the clip's peak, so the attempt cue is timed on a clip without a big outcome; tool proposal row added. No IoU threshold invented (look_check needs `--tolerance-source` for one) |
| R7 | `spaces.md` header and §3: CharacterUseJumpPower defaults to true, so JumpPower 50 governs; 7.2 studs applies only with JumpHeight; ledges are checked against the jump height measured in the place and written in the game profile (probe in Studio before relying on a number). Checked in the mirror: StarterPlayer.yaml:243-249, 272-278, 329-339; Humanoid.yaml:608-660 |
| R8 | Two-client captures only for effects and threats with per-viewer variants, batched in one request; the owner starts the local two-client server; without it the per-viewer check is Unproven: role file studio-operator row, `principles.md` §9 check, `review.md` §7 intro and effect line, `handoffs.md` §3.6 C2 |
| R9 | Proposal row added (**recipe**, character recipe, direction stage): a plain-block behaviour capture judged by the game-designer before the modeler starts, for a new enemy or creature with gameplay behaviour |
| R10 | `game-concept/references/hook-promise.md` §3: old item 6 restored to 6, the tile-size test appended as item 7; §4 header "(12 items, O)". Table a and c references updated to item 7 |
| Note: lowest graphics setting (could not check) | `spaces.md` §7 check: the studio-operator sets the Studio quality level, otherwise the check is Unproven. The docs show `RenderSettings.QualityLevel` is plugin-writable (RenderSettings.yaml:256-268); not probed: proposal row to `studio-mcp` |
| Note: J003 citations that name Riot | Left for the lead, as the review asks: they cite the owner's J003 research paper, not the J018 transcripts |

## Repair round 2 (stage 3 review `reviews/game-designer-rev2-reviewer.md`, 2026-10-22)

The rev2 keep list is kept whole; every change below is a clause on an existing line, no new section, no renumbering. SKILL.md lines unchanged (115 / 79 / 82); descriptions unchanged; role frontmatter unchanged.

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (blocking) | One definition of the **flat-key capture** in `game-design/references/review.md` §7 intro (same game-camera angle and distance as play; one flat colour filling the frame border, a plain magenta #FF00FF backdrop Part by default, under the subject for a top-down camera; one subject per capture or units spaced apart for `--component`; on `invalid-mask` ask for a recapture or a `--mask`, never judge by eye and call it measured). Used at each black-fill measure: `review.md` §7 character lines 1, 2, 4, 7 (role from black-fill, lineup size rank, look-alike IoU, variant footprint); `systems-economy.md` §8 check (flat-key captures, `--mask` fallback); `preproduction/references/documents.md` §8 role-card check; `handoffs.md` §3.7 example brief C2; `game-design` SKILL §7 row 5 check ("Flat-key lineup capture"). Role file studio-operator row now asks for flat-key captures for lineups, variants and look-alikes and says why. Same gap found in `review.md` §7 stage line (`look_check.py value` on an in-scene capture): now `--box` around the focal subject. Not probed: that a plain backdrop Part keys flat under the place's lighting; the check itself reports `invalid-mask` when it does not, and a proposal row asks `studio-mcp` for the recipe |
| R1 | `game-design/references/principles.md` §7 checks: `visible_ms` = first to last changed frame; the clip has still frames before and after the event for more than half its length and nothing else moves (idle off, HUD counters outside the frame), because the background is the median frame and every other change counts (clip_metrics.py:51-57, 78-93). `documents.md` §6 Checks field points to it; the role file's studio-operator row asks for frame sequences with still frames before and after and nothing else moving |
| R2 | `game-concept/references/hook-promise.md` §3 item 7: `--size` and `--bottom-band <percent>` from the phone capture in `knowledge/design/marketing/surfaces.md` (marketing measures it; the file does not exist yet, so the tile check is reported `not measured` and marketing is asked, never an invented size); `--box <hero and its action>`, since without it the subject fields say "not measured". `game-concept` SKILL §6 first-image line says the same in short |
| Note: library GD-35 "static" | Unchanged: proposal row already filed for the lead |
| Note: J003 citations that name Riot | Left for the lead, as both reviews ask (they cite the owner's J003 research paper) |
| Note: `ReducedMotionEnabled` in this file's header | No book change: the books say "reduced motion"; the property exists (GuiService.yaml:262) |
