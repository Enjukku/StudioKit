---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2 (brief v2)
supersedes: []
---
> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22

# J018 coverage: sound-designer

Books rebuilt (old state: `df13ff4`): `.agents/roles/sound-designer.md` (body; frontmatter byte-identical), `.agents/skills/sound-design/` (SKILL.md and references; `evals/` and `evidence/` untouched). New references: `craft-process.md`, `review.md`, `worked-examples.md`. Tagged findings: 96 (91 landed, 2 of them partly: RI-27, SI-05; 5 rejected for the books with a reason: CR-16 as an evals proposal, EX-04, EX-07, WT-17, WT-19). Untagged findings used: 22. SKILL.md: 205 lines after repair round 2, description 328 characters (unchanged); steps, rules and self-check end at 19.2 KB (19,157 bytes) (the rule index moved to §6, S-75 and S-78 to `craft-satisfying.md`); §1 says to re-read §1-§5 and §7 after a compaction.

Legend for "landed in": `SKILL` = `sound-design/SKILL.md`; `cp` = `references/craft-process.md`; `rv` = `references/review.md`; `we` = `references/worked-examples.md`; `cc` = `references/cue-card.md`; `ai` = `references/ai-generation-prompts.md`; `mix` = `references/mix-and-loudness.md`; `rep` = `references/repetition.md`; `rw` = `references/reward-and-juice.md`; `ht` = `references/horror-and-tension.md`; `ra` = `references/roblox-audio.md`; `cs` = `references/craft-satisfying.md`; `role` = `.agents/roles/sound-designer.md`. Self-review lines are `rv` §3 R-xx; file measures `rv` §4 F-xx.

## a. Findings

| ID | Title | Landed in (file § section) | As | Rejected: reason |
| --- | --- | --- | --- | --- |
| SD-01 | Sound has three jobs and tells the story with every layer | SKILL §1 (three jobs), §3 SC-01, §2 step 1; cc field 43; rv R-01, R-02, R-52 (screen covered), R-65; SKILL §7 #1 | standard / step / self-review check / core principle | |
| SD-02 | Every cue names its emotion, not only its object | SKILL §3 SC-02, §2 step 1; rv R-03, R-52 ("which emotion?") | standard / self-review check | |
| SD-03 | Ambience, foley and one signature element put the player in the world | cp §1 (ambience map: emotion per zone, the stage's signature element), §3 "Ambience (from the ambience map)"; rv R-17 (map emotion, signature); role job flow (stages) | step / self-review check | |
| SD-04 | The sound theme comes from what the thing does in play | SKILL §3 SC-03, §2 step 3; cc field 44; rv R-04 (verb; F-05 longest tail for a slow), R-51 (O-B question); we §1; SKILL §7 #10 | standard / self-review check / example | |
| SD-05 | Stage the action: one sound per named stage | SKILL §3 SC-04, §2 step 2; cp §2 stage sheet; cc field 45; rv R-05, R-06, R-50; we §1 | standard / step / self-review check / example | |
| SD-06 | Attach sounds to game events, listed and tested | cp §2 (event ids), §9 (debug cue log asked of the integrator); rv R-41 (S: one cue per event); ra §G | step / self-review check | |
| SD-07 | Shape the envelope: the attack and transient make the hit land | SKILL §3 S-76 (sharpened), S-133 (file starts on its transient); cp §3, §6 step 7; rv R-20 (F-01, F-02) | standard / self-review check | |
| SD-08 | Think in frequency bands; pitch sets size | SKILL §3 SC-06; cp §3 bands, size and weight; rv R-23 (F-06), R-27 | standard / self-review check | |
| SD-09 | Set how far each sound carries by its importance | SKILL §3 SC-07; cc field 47; mix §B far version; rv R-16 (D + S: real roll-off, mode read first); ra §G distance row | standard / self-review check | |
| SD-10 | Far sounds lose their highs first | SKILL §3 SC-07; mix §B far-version row; rv R-16 (high layer on the shorter curve) | standard / self-review check | |
| SD-11 | EQ: cut what is not wanted before boosting | SKILL §3 SC-06 (cut before boost, low cut start value); cp §6 steps 1, 3; mix S-113; rv R-24 (F-06 share below the cut) | standard / step / self-review check | |
| SD-12 | Compression lifts the tail; compress again after layering | SKILL §3 SC-09; cp §6 steps 4, 6 | step | check left to check-in B (O-B: raw vs processed); a tail-lift number (F-05 level at +100 ms) is reported, no pass value: the right amount is taste |
| SD-13 | Reverb and delay place the sound and glue its layers | SKILL §3 SC-08; cp §6 step 5; ra §B baked vs live; rv R-40 (one AudioReverb per space type), R-52 ("does the space sound like the place?"); we §3 | standard / self-review check / example | |
| SD-14 | Process in a fixed order, a little at each step | SKILL §3 SC-09; cp §6 table; cc field 49 (purpose per step); rv R-51 (raw vs processed) | standard / step / self-review check | |
| SD-15 | Tonal layers: stacked sources, kept clean and separate | SKILL §3 SC-06 (tonal stems separate, in key); cp §3 bands; rv R-27 (F-10) | standard / self-review check | |
| SD-16 | A shot is built from five layer jobs | SKILL §3 SC-05; cp §3 table; ai §B layers line; we §1; glossary | standard / step / example | |
| SD-17 | Put movement inside the sound | SKILL §3 SC-10; cp §6 movement bullet; ai S-124, examples; rv R-29 (F-11) | standard / self-review check | |
| SD-18 | Pass-bys make travel; let the engine move real projectiles | SKILL §3 SC-10 (no engine Doppler on graph emitters: scripted PlaybackSpeed or one-shot whoosh); ra §B Doppler row (docs); rv R-30 (F-05); we §1 | standard / self-review check | |
| SD-19 | Process for variety, but keep a natural sound when it works | cp §6 (unprocessed first; family variants by processing); cc field 49; rv R-62 | step / self-review check | |
| SD-20 | Build long, varied beds from spliced takes | cp §6 beds bullet; rep §A step 8; rv R-26 (F-08, F-12) | step / self-review check | |
| SD-21 | Every weapon and the whole game get a signature sound | SKILL §3 SC-11; cp §8 identity sheet; cc field 46; rv R-13, R-35 (siblings: F-10 3 st or F-06 band), R-53 (sequence listen), R-52 (signature through the mix), §2 check-in C question; SKILL §7 #5, #11; we §1 | standard / stage (identity sheet) / self-review check / example | |
| SD-22 | Characters sound like who they are, and sound telegraphs their state | SKILL §3 SC-11; cp §2 (end-of-state warning); ht §B tells; rv R-09, R-12, R-53 | standard / self-review check | |
| SD-23 | Every floor material is a footstep callout | SKILL §3 SC-12; cp §8 footstep table, §9 partners; ra §B footsteps row, §G; rv R-14; role job flow; we §3 | standard / self-review check / example | |
| SD-24 | Design and editing are two separate passes | SKILL §3 SC-13, §2 steps 7-8; cp §6; rv R-52 (the edit is judged in the full mix) | standard / stage / self-review check | |
| SD-25 | Mix as you go; music and effects are designed together | SKILL §3 SC-13; mix §C music-and-SFX row; rv R-52 (masking by music) | standard / self-review check | |
| SD-26 | Review the key event solo, then in the full mix | rv §2 check-in C (two listens), §5 step 3, R-52; SKILL §2 step 11 | stage / self-review check | |
| SD-27 | Give sound notes in technical terms with a direction | rv R-60, §5 step 4; SKILL §7 #16 | self-review check / core principle | |
| SD-28 | Judge against real reference and name every stand-in | cp §5 (pick against the category reference), §8 References row; rv R-62 (F-01..F-10 of the pick beside the reference's), §2 check-in B (reference after the options), R-61; SKILL §3 SC-14; role "Before you hand back" | standard / self-review check | |
| SD-29 | Sources by texture, not by name: many takes, some odd ones | SKILL §3 SC-14; cp §5; ai S-123, S-124, template; rv R-62; we §1 | standard / step / self-review check / example | |
| SD-30 | Keep a library of building blocks; cues are data | SKILL §3 SC-15; cp §7; ra §B cue-id row; rv R-44 (G), R-61 | standard / self-review check | |
| SD-31 | A fixed cue template and categories | cc (template, fields 43-50); cp §7 (categories = buses); rv R-40 | standard / self-review check | |
| SD-32 | Bake per-sound processing into the file | SKILL §3 SC-08; cp §6 bake bullet; ra §B; cs S-84 | standard | file check: a raw play is an owner listen (check-in B/C); no number proves "finished" |
| SD-33 | Rules are guides; the listening test decides | SKILL §3 SC-16; rv §2 (a rule break needs a passing check-in answer), R-63 | standard / self-review check | |
| CC-01 | One target experience, signed by every craft | cp §1 (target-experience line); cc field 43; rv R-01 | step / self-review check | |
| CC-02 | One marker list is the timing contract for animation, VFX and sound | SKILL §3 S-133 (new sync rule), SC-04, §2 step 2; cp §2; rv R-06 (T), R-20, R-43 (L), R-54 (V); role job flow | standard / step / self-review check | |
| CC-06 | Split a big craft job by category, with one integrator and a shared library | cp §7 last bullet (the lead's call) | standard | |
| CD-01 | Know the character, then decide on their behalf | SKILL §2 step 3, §3 SC-11; cp §1 character-card row, §9; rv R-12; role partner table | step / self-review check | |
| CD-09 | Every action shows who this character is | SKILL §3 SC-11 (feel words); rv R-12 | standard / self-review check | |
| CD-13 | Twist the tone within bounds; darker still keeps the appeal | cp §5 (tone shift: extreme and pulled-back options), §6 (mood variants by processing the base); rv R-12 | step / self-review check | |
| CD-15 | Re-theme the abilities, not only the costume | rv R-12 (a variant re-themes every ability's sound, keeps the signature); SKILL §3 SC-11; SKILL §7 #11 | self-review check / core principle | |
| CR-03 | Solve the problem behind the note; separate goals from tactics | rv §5 step 5, R-60 | self-review check | |
| CR-16 | Calibrate on simple basics in many moods | — | — | rejected for the books: calibration belongs in `evals/` (not editable this job); proposal row (evals) |
| CR-17 | Say what each input can prove; end with a could-not-check list | SKILL §1 ("You cannot hear"); rv §1 input table and labels, R-54, R-64; role "Before you hand back" | standard / self-review check | |
| EX-01 | Larger than life: extend and sharpen what must read | SKILL §7 #9; rv R-51 (raw vs processed, core still there) | core principle / self-review check | |
| EX-04 | Emotes and reactions: maximum expression for a two-second read | — | — | rejected: a visual read-time rule; the sound side is covered by the UI length rules (`cs` S-130) and principle #9 |
| EX-07 | Cartoony hang time: hold near the apex, then fall fast | — | — | rejected: animation timing; sound keys to the launch and landing events of the timing list (SC-04), no sound-specific rule |
| GD-01 | Every asset has jobs: clarity first, then feel, then style | SKILL §3 SC-01 (clarity, satisfaction, style); rv R-01 | standard / self-review check | |
| GD-02 | Every action gets immediate feedback; reached goals get a short celebration | rv R-02, R-22 (in-play celebration ends within about 2 s, F-04); rw §B S-194 (in-play celebration under about 2 s; tiers from the reward tier table), S-53; we §2 (T2 bag-full confirm 150-300 ms, repair 2) | standard / self-review check | |
| GD-05 | Behaviour sets the tone before art does | SKILL §3 SC-03; cp §1 (feature spec first); rv R-04 | standard / self-review check | |
| GD-11 | Build a climactic arc toward the resolution | mix §C climax row; rv R-18 | standard / self-review check | |
| GD-13 | Fairness comes from clear expectations and consistency | SKILL §3 SC-12 (same tell every time); ht §B tells; rv R-08 | standard / self-review check | |
| GD-34 | Feedback follows the real outcome | SKILL §3 S-150/S-219 (sharpened), §2 step 2; rv R-07, R-41; SKILL §7 #19; we §1-2 | standard / self-review check / example | |
| GD-35 | Paid random reveals are honest | SKILL §4 D-03 (one windup asset, rarity after the result, skip, batch; momentary maximum within 1 LU by F-13 b (repair 2), peaks within 1 dB by F-03), D-07, platform-policy line; rw §D S-164 (points to D-03, D-07), D-03 alternative; rv R-31 (F-13 b momentary maximum + F-03), R-32; we §4 | standard / self-review check / example | V4 diff: platform-policy wins on odds wording (fixed `ra` S-166, S-172); GD-35's "crescendo" maps to added notes and tail in sound, never level (D-03, stricter, ours); library proposal row |
| LC-02 | Keep a colour-role table: one hue never means both help and harm | SKILL §3 SC-12 (sound family); cp §8 sound-code table; rv R-14 | standard / self-review check | |
| PP-14 | Design moving parts with room to move | cp §2 (a mechanical cue per designed moving part); rv R-05 (every stage, incl. mechanical moves, has a cue) | step / self-review check | |
| PP-25 | Reuse first: search the zoo and existing effects before making new | SKILL §3 SC-15; cp §4 step 1, §7; rv R-61 | standard / step / self-review check | |
| PI-01 | The cheapest stage goes first | SKILL §3 SC-17, §2 step 5; cp §4; rv R-50; SKILL §7 #4, #15 | standard / stage / self-review check | |
| PI-08 | Find the right number by bracketing | cp §5 bracket bullet; SKILL §2 step 6; rv R-62 (tested values and why the pick won) | step / self-review check | |
| PI-09 | Not precious: most attempts fail | cp §5 (3-5 options for hero cues, first take a warm-up); rv R-62; SKILL §7 #15 | step / self-review check | |
| PI-10 | Park a stuck part and come back | rv §6 (stuck part logged, parked, revisited), R-66 | step / self-review check | |
| RI-05 | Research first; one narrow moodboard with pillars and key features | cp §5 (write what the real thing sounds like before prompting), §8 tone words and references | step | |
| RI-10 | Study the real thing closely for the details invention misses | cp §5; rv R-62 (references and one observed property named) | step / self-review check | |
| RI-23 | Bring in one unexpected element from outside the genre | cp §5 (one odd variant per layer; one named unexpected element per signature cue); rv R-62 | step / self-review check | |
| RI-24 | Act it out: agents write the performance beat by beat | cp §1 (timing list row: the beat sheet's sound words) | step (input) | |
| RI-27 | Design a variant through a narrative lens | rv R-12 (variant re-theme); cp §5 tone-shift options | self-review check | partial: the variant's story is the art director's brief; I read it |
| RH-01 | Vary the cadence: fast and slow beats, never metronomic | cp §2 combos bullet; rv R-10 | step / self-review check | |
| RH-03 | Every effect tells a beginning, a middle and an end | SKILL §3 SC-04; rv R-11 | standard / self-review check | |
| SS-05 | Shape language carries meaning: sharp is danger, round is friendly | SKILL §3 SC-11 (sharp transients for threat hits, soft attacks for friendly one-shots; tells and warnings rise by design); rv R-34 (onset-to-peak F-02 − F-01, threat hits and attacks < friendly one-shots; tells, warnings, charges excluded, repair 2); SKILL §7 #5 (check R-34) | standard / self-review check / core principle | |
| SI-03 | Theme fit can rule out an otherwise cool idea | cp §8 tone words; rv R-13 | standard / self-review check | |
| SI-05 | Make it for a specific audience, and give fans what they want | role work method 1 (audience age) | step (input) | partial: the audience and "fans want" line come in the brief; options are judged by the goal questions (rv §2), no separate sound rule |
| SI-13 | Refresh a tone by pushing to the extreme, then pulling back | cp §5 tone-shift bullet; rv R-51 (the owner's pick at check-in B) | step / self-review check | |
| UI-01 | Flow first, then style, then motion | cp §1 (UI event list with static states before UI cues) | step (input) | |
| UI-11 | The static state explains; motion and sound make it felt | rv R-65; cp §1 UI row | self-review check | |
| UI-12 | Motion goal: responsiveness | SKILL §3 S-150/S-219 (attempt cue at once), S-131; rv R-20 (onset) | standard / self-review check | |
| UI-17 | Seed the motion table with tested durations | cp §1 (motion table from the UI designer) | step (input) | |
| UI-18 | Errors and denials say what is wrong and how to fix it | rv R-02 (refusal sounds soft, rate-limited about 0.5 s) | self-review check | |
| UI-19 | Counters tell the truth; their animation is decoration | rw §B counters row; rv R-19 | standard / self-review check | |
| VC-01 | Fix a weak read with contrast, not detail | SKILL §7 #3 (unique timbre, space before it, top tier); rv R-52 | core principle / self-review check | |
| VR-01 | Specify the read, then pick the cheapest technique | SKILL §2 steps 1-2 (job, verb, stage times before sources); rv R-65 (reads with sound off) | step / self-review check | |
| VR-09 | The hit is one peak frame between cause and result | SKILL §3 S-133; rv R-06, R-20 | standard / self-review check | |
| VR-22 | Hit-stop is local, short and scaled by hit strength | SKILL §3 S-73/S-74 (hit sound on the first freeze frame; lengths owned by game design); rv R-06 (the hit cue keys to the contact event) | standard / self-review check | |
| VR-24 | Frequent effects are shorter, quieter, merged and capped | rw §B S-194 (merge window from the feature spec; rate from the reward tier table); rv R-15 (tier and rate from T1-T4), R-22, R-41 | standard / self-review check | |
| VR-25 | Randomise decoration only; lock what carries meaning | SKILL §3 SC-12; rep §B S-90/S-91, §A step 3; rv R-08 (tells: one asset, no jitter) | standard / self-review check | |
| VR-26 | Pulse and blink rates carry meaning | SKILL §3 SC-12; rv R-42 | standard / self-review check | |
| VH-02 | Rank loudness across a set | mix §B S-107/S-108 (read rank wins); rv R-15, R-52 (top tier dominates); SKILL §7 #3 | standard / self-review check | |
| WT-01 | Anticipation must read | cp §2 tells; ht §B tells; rv R-08 | step / self-review check | |
| WT-02 | One consistent physics lets players predict | cs §B S-75 (size tiers, moved from SKILL in repair 1), cp §3 (S-82 pitch per size class, same step in every family); rv R-33 (F-10 step per tier, F-05 decay); SKILL §7 #7 | standard / self-review check / core principle | |
| WT-03 | Motion sets the emotional tone; giants move slowly | cp §3 size and weight (giants low, slow, long settles); rv R-53 (heaviness ranked at check-in C) | standard / self-review check | |
| WT-11 | Bursts reach size fast and ease out slowly | SKILL §3 S-76 (fast attack, decaying body and tail); rv R-20 | standard / self-review check | |
| WT-12 | Build-ups rise: smaller to bigger, dim to bright, low to high | SKILL §3 SC-04; cp §3 build-ups; rv R-28 (F-05, F-10) | standard / self-review check | |
| WT-13 | Cause first, then effect | SKILL §3 SC-04; rv R-11 | standard / self-review check | |
| WT-17 | Hold the first pose before moving | — | — | rejected: animation start hold; sound keys to the first motion event, nothing to add |
| WT-19 | Push off with force | — | — | rejected: foot timing in animation; a push-off sound keys to its event (SC-04) |
| WT-21 | Fast contact; delete frames until the hit lands | rv R-06 (impact event = contact marker, offset 0 frames) | self-review check | |
| WT-23 | Small changes in attack and release change the felt weight | SKILL §3 S-76 (heavier = longer release); cp §3; rv R-22 (F-05), R-53 | standard / self-review check | |
| WL-18 | Materials follow gameplay rules | cp §8 footstep table (impact sets follow the material-to-rule table); rv R-14 | standard / self-review check | |
| CR-01 | Judge in the game (untagged, used) | SKILL §2 step 11; rv §2 check-in C on the playable at the game camera | stage | |
| CR-02 | Ask a goal question, never "do you like it?" (untagged, used) | rv §2 goal questions | stage | |
| CR-07 | No grand reveals: show early, partner crafts first (untagged, used) | SKILL §2 step 5; cp §4 (check-in A) | stage | |
| CR-08 | Diagnose by layer (untagged, used) | rv §5 step 4 (layer column) | step | |
| CR-13 | Close with an honest recap (untagged, used) | rv R-61 (stand-ins named), role "Before you hand back" | self-review check | |
| GD-04 | Name the target experience, not "fun" (untagged, used) | cp §1; rv R-01 | step / self-review check | |
| GD-15 | Prove the fun with the crudest prototype (untagged, used) | cp §4 temp pass | stage | |
| PI-02 | Gates freeze decisions (untagged, used) | SKILL §3 SC-17 (final processing after the timing lock); rv §2 check-ins | stage | |
| PI-06 | Work in passes over the whole (untagged, used) | cp §4 (every stage gets a temp source before any is polished) | step | |
| PI-07 | One named problem per pass; fix the worst first (untagged, used) | rv §5 step 5 | step | |
| PI-11 | A time box forces the readable choice (untagged, used) | rv §6 stop criteria | step | |
| PI-12 | Know when it is done (untagged, used) | rv §6; R-66 | self-review check | |
| PI-14 | "It would be cooler" is new scope (untagged, used) | rv §6 (follow-up list) | step | |
| RI-02 | Options at equal, low finish (untagged, used) | cp §5 (same finish, loudness-matched); rv §2 check-in B | step | |
| RI-18 | Each option gets its own hook from a different source (untagged, used) | cp §5 | step | |
| RI-19 | Present options with your pick and the reasons (untagged, used) | cp §5; rv R-62 | step / self-review check | |
| RI-21 | The first output is a warm-up (untagged, used) | cp §5 | step | |
| UI-15 | One motion table (untagged, used) | cp §1 UI row (motion table timing) | step (input) | |
| VR-06 | Budget each effect's footprint for the worst-case crowd (untagged, used) | rv §2 check-in C budget (busiest expected moment, 10 s burst) | stage | |
| VR-19 | Rate each effect per viewer (untagged, used) | SKILL §3 SC-07 (threatened player full, bystanders lower); mix §B per-viewer row; cc field 47 | standard | |
| VR-23 | Every intense channel has an off path (untagged, used) | rv R-65 (reduced version keeps the information) | self-review check | |
| WL-01 | Gameplay readability beats beauty; test in the busiest moment (untagged, used) | rv §2 check-in C (busiest expected moment); SKILL §7 #1 | stage / core principle | |

## b. Universal principles

| UP-ID | Applies (yes/no + reason) | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: every state change needs an identifiable cue; sound must not mask the read | SKILL §7 #1 |
| UP-02 | yes: judged in the full mix, at distance, on phone speaker and headphones | SKILL §7 #2 |
| UP-03 | yes: unique timbre, space before, top tier for the important cue | SKILL §7 #3 |
| UP-04 | yes: gesture, stages and envelope before layers and processing | SKILL §7 #4 |
| UP-05 | yes (by analogy): signature element; transient shape follows shape language | SKILL §7 #5 |
| UP-06 | yes: cut frequencies and layers; one low-end owner | SKILL §7 #6 |
| UP-07 | yes: one sound family per meaning, one footstep set per floor, one tell per attack | SKILL §7 #7 |
| UP-08 | yes: stages, rising charge, transient on contact, one marker list | SKILL §7 #8 |
| UP-09 | yes: boosted transients, pitch for size, on a natural core | SKILL §7 #9 |
| UP-10 | yes: verb picks the texture; characters sound like who they are | SKILL §7 #10 |
| UP-11 | yes: identity sheet, signatures survive variants | SKILL §7 #11 |
| UP-12 | yes: takes, jitter, spliced beds; meaning never varies | SKILL §7 #12 |
| UP-13 | yes: card fields before any prompt | SKILL §7 #13 |
| UP-14 | yes: texture prompts, odd variant, reasoned pick | SKILL §7 #14 |
| UP-15 | yes: temp pass, timing lock, not precious | SKILL §7 #15 |
| UP-16 | yes: solo then mix; technical notes | SKILL §7 #16 |
| UP-17 | yes: event ids, transient-start files, library, data table | SKILL §7 #17 |
| UP-18 | yes: stop criteria, stand-ins named | SKILL §7 #18 |
| UP-19 | yes: tick on input, outcome on confirmation, honest reveals | SKILL §7 #19 |
| UP-20 | yes: no sound-only fact; reduced versions; pulse rates | SKILL §7 #20 |

## c. Old book changes (old = git revision df13ff4)

| Old text (file:line at df13ff4) | Kept / sharpened / replaced / moved / removed | Why |
| --- | --- | --- |
| SKILL.md:6 author line | sharpened: J018 rebuild line with "built also from the owner's Riot transcripts (J018)" | brief rule |
| SKILL.md:10-28 §1 role and output contract | sharpened: three jobs (SC-01), "you cannot hear" with named inputs, deliverable list adds stage sheets, sources, checks, stand-ins; review format points to `review.md` §5 | SD-01, CR-17; agent senses (V1) |
| SKILL.md:30-48 §2 workflow (10 steps) | replaced by 11 steps: frame, stage, choose, layers, temp pass, sources and options, design pass, edit pass, mix, platform and ethics, self-review; every old step kept inside a new one (recipe → 3, elements → 3, layers → 4, repetition → 8, mix → 9, platform and ethics → 10, prompt → 6, listening-test plan → 11 as check-ins) | SD-05, SD-24, PI-01, CR-07 |
| SKILL.md:53 "Core rules (40)" | sharpened: retitled "Core rules"; SC-01 to SC-17 added | new craft standards |
| SKILL.md:58-64 Feeling rules (S-01, S-02, S-183, S-25, S-186, S-18) | moved to `emotion-recipes.md` §C; S-01 "confirm by listening test" → "confirm at a check-in"; S-18 measured with F-09 | V7 size; V6 one home; agent cannot listen |
| SKILL.md:66-71 Timbre and level rules (S-07, S-08, S-22, S-15, S-11) | moved to `elements.md` §B (unchanged text) | V7 size; V6 |
| SKILL.md:74 S-76 | sharpened: heavier = longer release; telegraphed = longer attack or pre-sound; light vs heavy differ in envelope | WT-23, SD-07 |
| SKILL.md:79 S-73/S-74 hitstop numbers (base + k × strength, 2/4/6 frames, cap 8) | replaced: the sound book keeps only "hit sound on the first freeze frame"; lengths point to `game-design/references/principles.md` §7 | V6 one rule one place; game design owns hit-stop length (VR-22) |
| SKILL.md:80 S-133 window −35 ms to +100 ms, aim 0 to +20 | replaced: one trigger; onset 0 to about +40 ms after the first lit contact frame, never more than one frame early; steady delay beats jitter | animator proposal row (V11), CC-02 DS line, V10 |
| SKILL.md:84 S-194 (batch 80-150 ms; long 1.5-12 s celebrations rare) | sharpened and moved to `reward-and-juice.md` §B: merge window from the feature spec (about 100 ms); in play under about 2 s; long ones only on non-play screens | GD-02, game-design §7 consistency |
| SKILL.md:85-89 Reward rules (S-59, S-60/61/62, S-64, S-114, S-134) | moved to `reward-and-juice.md` §B | V7, V6 |
| SKILL.md:92-96 Repetition rules | moved to `repetition.md` §B; S-90/S-91 sharpened (no jitter on tells, warnings, countdowns; vary samples, never the timing of a meaningful cue) | VR-25, GD-13 |
| SKILL.md:99-100 Warning rules (S-136/S-99, S-137) | moved to `horror-and-tension.md` §B | V7, V6 |
| SKILL.md:103-105 Mix rules | moved to `mix-and-loudness.md` §A-B; S-107/S-108 sharpened ("or the scene's read rank" wins) | VH-02, game-designer read rank sheet |
| SKILL.md:109 S-150/S-219 | sharpened: attempt cue at once, outcome layer on the server's confirmation, pending past about 100 ms, never an early success | GD-34, UP-19 |
| SKILL.md:112 S-159/S-160 "approve nothing before hearing it on a real phone speaker" | sharpened: "before check-in C on a real phone speaker and headphones" | the agent cannot hear (V1) |
| SKILL.md:119 D-03 | sharpened: one shared windup asset, rarity layers only after the result, tap to skip, batch opens | GD-35 |
| SKILL.md:125 "Paid random items must pass Roblox's odds and PolicyService rules (S-165, S-166)" | replaced: load `platform-policy`; its rules win | V4 |
| SKILL.md:131 four verification statuses | sharpened: "auditioned" means an owner check-in answer | V1 |
| SKILL.md:136-149 §5 self-check | replaced: input-labelled list that runs `review.md` §3; every old line kept (job, provenance, layers, frequent cues, no roughness, tiers and ducks, D-01 to D-08, wiring, claims, genre preset); "test plan has A/B pairs, device matrix, pass criteria" replaced by check-ins A/B/C | V1, CR-17 |
| SKILL.md:151-169 §6 routing | sharpened: rows for `craft-process.md`, `review.md`, `worked-examples.md` | new references |
| roles/sound-designer.md:12 build comment | sharpened: J018 line added | brief rule |
| roles/sound-designer.md:14 intro | sharpened: three jobs, signature, event sync; "you cannot hear" | SD-01, CR-17 |
| roles/sound-designer.md:16-20 read first | sharpened: new references; `platform-policy` read for anything paid; Studio checks run by the studio operator (no Studio MCP in the tools line) | V4; tools line unchanged (owner) |
| roles/sound-designer.md:24 job flow | sharpened: temp sound on the animatic or first playable, finish on the locked timing list, `log-diff`, footstep table | CC-02, SD-23, PI-01 |
| roles/sound-designer.md:28 "Craft practice from Riot's artists ... J016 riot-extracts.md §4" | removed | job card: role files point to their own books, not to J016 extracts; the material now lives in the books |
| roles/sound-designer.md:30-36 work method | replaced: restate adds job, verb, viewers, target line; follow the eleven steps; stage sheets; measure every file | SD-01 to SD-05 |
| roles/sound-designer.md:38-40 working with other agents | replaced by "What you ask your partners for, and when" (table); the ticket rule kept | CC-01, CC-02, V8 |
| roles/sound-designer.md:46 hand-back list ("Listening-test plan") | sharpened: stage sheets, sources, checks with inputs, check-in answers, could-not-check list, stand-ins | CR-17, SD-28 |
| references/cue-card.md:5-6 short card fields | sharpened: adds 22, 43, 45, 47 | SD-01, SD-05, SD-09 |
| references/cue-card.md:33 field 22 Sync | replaced: trigger event id, file onset, the new sync window | CC-02 |
| references/cue-card.md:40 field 29 Test plan | replaced: Check plan (self-review lines, check-ins, A/B) | V1 |
| references/cue-card.md:51 field 40 | sharpened: "auditioned" = an owner check-in answer | V1 |
| references/cue-card.md:80 example field 22 "0 to +20 ms after the break frame" | replaced: trigger, onset ≤ 5 ms, 0 to +40 ms window | CC-02 |
| references/cue-card.md:87 example field 29 "blind listeners" | sharpened: R-lines plus the owner at check-in C | V1 |
| references/cue-card.md:117 JSON `test_plan` | replaced: `check_plan`; new keys for fields 43-50 | template matches fields |
| references/craft-satisfying.md:5-7 header | sharpened: SC-05, SC-06, SC-08 pointers | V6 |
| references/craft-satisfying.md:60 S-84 "Dry assets: short dry tails; space from one engine reverb" | replaced: the designed tail and glue baked; the room live per space (SC-08) | SD-13, SD-32 (the old rule read as "never bake space") |
| references/ai-generation-prompts.md:13 S-123 | sharpened: texture descriptions, takes, odd variant | SD-29 |
| references/ai-generation-prompts.md:14 S-124 | sharpened: texture not object; motion words | SD-17, SD-29 |
| references/ai-generation-prompts.md:15 S-125 "add space with the engine reverb" | replaced: designed tail baked in the design pass; room live | SD-32 |
| references/ai-generation-prompts.md:16 S-126 | sharpened: first step of the design-pass order; measured with `review.md` §4 | SD-11, SD-14 |
| references/ai-generation-prompts.md:30 layers line | sharpened: one prompt per layer job | SD-16 |
| references/ai-generation-prompts.md:45-46 "until a human or agent has listened" | replaced: until the owner has heard it at a check-in | V1 |
| references/mix-and-loudness.md:5-7 header | replaced: rules moved here; pointers | V6 |
| references/mix-and-loudness.md:32 S-113 "high-pass every non-sub layer near 100 Hz" | sharpened: points to SC-06; bright layers cut higher (200-300 Hz (P)) | SD-11 |
| references/repetition.md:5-6 header | replaced: rules moved here; meaning never varies | V6, VR-25 |
| references/repetition.md:12 step 3 | sharpened: no jitter on tells, warnings, countdowns | VR-25, GD-13 |
| references/repetition.md:16 step 6 | sharpened: listening tests are check-in C; the fixture and cue log are the agent's | V1 |
| references/roblox-audio.md:66 S-166 "odds ... behind a labelled Odds or Details button" | replaced: points to `platform-policy` `references/rules.md` §A (odds as numbers before purchase; only long lists behind a worded label) | V4: the old wording contradicted the binding skill |
| references/roblox-audio.md:69 S-172 "Brazil: under-18 players are ineligible" | replaced: never hard-code regions or ages; `ArePaidRandomItemsRestricted` (platform-policy) | V4: platform-policy says regions change centrally |
| references/reward-and-juice.md:5-6 header | replaced: rules moved here | V6 |
| references/reward-and-juice.md:29 S-53 | sharpened: in play under about 2 s; 4-12 s only on non-play screens | GD-02, game-design §7 |
| references/reward-and-juice.md:69 D-03 fair alternative | sharpened: one windup asset, skip, batch | GD-35 |
| references/horror-and-tension.md:5-7 header | replaced: pointers to the rules' homes | V6 |
| references/emotion-recipes.md:5-7 "(S-01, core)", "(S-02, core)" | sharpened: point to §C | rules moved |
| references/genre-presets.md:19 destruction row "hitstop 2-6 frames (S-73)" | replaced: hit sound on the first hit-stop frame, lengths from the game designer | S-73/S-74 change (V6) |
| references/glossary.md term table | sharpened: 15 terms added (attempt cue, outcome layer, check-in A/B/C, five layer jobs, stage sheet, stand-in, temp pass, ...) | new vocabulary of the books |
| references/elements.md, horror-and-tension.md, emotion-recipes.md, reward-and-juice.md, repetition.md, mix-and-loudness.md §B tables | sharpened: rules moved in from SKILL.md §3 as rows, same IDs and tags | V7 size, V6 one home |

## d. Command runs (V3) and proposal rows from other roles (V11)

Synthetic samples: `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-v3/` (48 kHz WAV unless named), built by `sound-designer-make-samples.py`; measures by `sound-designer-measure.py` (the computations `rv` §4 describes: soundfile 0.14.0 / libsndfile 1.2.2, numpy, scipy, pyloudnorm).

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| R-20 (F-01, F-02) | onset at peak −30 dB; peak position | impact with 20 ms leading silence | onset 20.0 ms, peak 20.1 ms: flags the leading silence (right) |
| R-20 (F-01) | same | 100 ms noise head 26 dB below peak, then hit | onset 0 ms but peak 100.2 ms: the wrong number with no error; the onset-to-peak gap catches it (rule written into R-20) |
| R-20 (F-01) | same, MP3 delivery | the impact encoded as MP3 | onset 19.8 ms vs 20.0 WAV: no decoder delay added by this reader; peak +5.1 dBFS on a clipped source (decoder overshoot: measure the delivered format, F-03 note) |
| R-21 (F-03) | sample and true peak (resample ×4) | clipped impact | 0.0 dBFS sample, +3.0 dBTP true: fails both, as it should |
| R-22 (F-04, F-05) | −40 dB tail, `ends_above_-40`, decay to −20 dB, level at +100 ms | light vs heavy impact cut at 420 ms | both report 420 ms to −40 (file length) with the flag true: the cut tail is caught only by the flag (written into F-04); heavy −4.0 dB vs light −7.4 dB at +100 ms: heavy decays slower (right) |
| R-23, R-24 (F-06) | band shares, share below the cut (300 Hz) | 3 kHz tone with and without a 40 Hz rumble 20 dB down | 0.99 % vs 0.00 % below 300 Hz: the 0.5 % start value separates them; a 100 Hz-body impact has 0.7 % in 500 Hz-5 kHz: flagged by R-23 (right for a body with no crunch layer) |
| R-25 (F-07) | mono drop | stereo in phase vs anti-phase | 0.0 dB vs −25.7 dB (right) |
| R-26 (F-08) | seam ratio | 220 Hz loop with whole cycles vs 2.013 s cut mid-cycle | 1.0 vs 27.5 (right); first version (last-minus-first sample in dB) read −31 dB on the clean loop and was replaced by the ratio |
| R-27 (F-10) | strongest peak 60 Hz-4 kHz → note, cents | C5 tone; C5 with a 3rd harmonic 14 dB louder than the fundamental | C5 −1 cent (right); G6 (wrong with no error: the harmonic trap, written into F-10) |
| R-28 (F-05, F-10) | envelope peak position; first and last frame pitch | rising charge 1.5 s | peak at 1,490 ms of 1,500; pitch 440 → 600 Hz (right) |
| R-29 (F-11) | centroid variation, Hann frames within 10 dB | moving tone vs static tone vs decaying C5 vs impact | 0.393 vs 0.0 vs 0.0 (right); impacts 1.3-2.0 (attack frame inflates it: "sustained layers only", written into R-29 and F-11); the first version without a window read 0.42 on the static decaying tone and was replaced |
| R-30 (F-05) | envelope peak position | 1.2 s noise pass-by | peak at 590 ms (middle third, right); F-10 on noise gave a meaningless note (noted in F-10) |
| R-31 (F-09) | loudest 400 ms window RMS; LUFS | 80 ms tick; 1 s files | RMS works on the tick; pyloudnorm raises "Audio must have length greater than the block size" under 0.4 s (an error, not a wrong number) |
| R-32 | sha256 of the windup files | two copies of one file, one other file | identical hashes for the copies, different for the other; a re-export with new metadata would fail a true match (safe direction); the asset id is the first test |
| R-06 (T) | `python tools/anim/clip_check.py sound-designer-samples.json --timing sound-designer-timing.json --out ...` | sampled clip JSON with markers charge, release, impact; timing JSON with one marker the clip lacks | exit 1; `shield_break_warn` FAIL (missing), `contact_candidate` MEASURED 1.0 frame offset; a 1-frame offset reads MEASURED, not FAIL, without `event_offset_frames` in a tolerance file (so R-06 asks for offset 0 on my events) |
| R-43 (L) | `python tools/film/shotlist.py cues templates/film/shotlist.example.json` | paper example shot list | Markdown cue sheet, all times UNKNOWN on the paper example (right: lengths not set) |
| R-43 (L) | `python tools/film/shotlist.py log-diff tools/tests/fixtures/film/drill.shots.json tools/tests/fixtures/film/drill.log.json` | fixture log with a cue 12 ms late | exit 0, verdict measured, signed diff +12 ms; planned-not-logged and extra cues listed |
| R-43 (L) | same with `--tol-ms 40 --tol-source ...` and the cue moved to −30 ms | edited log | the −30 ms (early) cue PASSES: the tolerance is symmetric (`abs`): the wrong answer with no error; R-43 now forbids `--tol-ms` for sync and reads the signed column; proposal row for an asymmetric tolerance |
| R-44 (G) | Grep `rbxassetid://\d+`, then `\.Asset\s*=` | synthetic `src/` with a data table and a client script setting `.Asset` | both patterns find the hard-coded client line; the data table hit is excluded by path; a bare number later joined into an id is only found through the `.Asset =` line (written into R-44) |
| R-14, R-16, R-40, R-41, R-42 (S) | Studio MCP read-only `execute_luau`, `get_console_output` | in-place graph and play-test log | not run: `list_roblox_studios` returned no connected Studio; `ra` §G marks the first use in a game job as a probe |
| R-54 (V) | device capture with sound | — | not run (needs the owner or studio operator on a device); stays "not verified" by design |

| Proposal row (from) | Adopted / declined | Where / why |
| --- | --- | --- |
| `proposals/animator.md` row "`.agents/skills/sound-design/SKILL.md` S-133": align the sync window to 0 to +40 ms, never more than 1 frame early | adopted | SKILL §3 S-133; cc field 22 and example; rv R-43, R-54; old −35/+100 window removed |
| `proposals/game-designer.md` row "`vfx-design`, `sound-design`, ... read the feature-spec sheets" | adopted | cp §1 inputs (feedback stack, threat and hazard sheets, read rank) and §2 stage sheet keyed to the stage names; SKILL §2 steps 1-2; role partner table |
| `proposals/animator.md` row `templates/anim/timing-list.md` (sync target, verb, end-of-state tells) | not against my books; supported | my stage sheet reads exactly those fields (cp §1, §2) |
| `proposals/animator.md` G3 row effect recipe (blocking markers to VFX and sound first) | not against my books; supported | matches my temp pass (cp §4) and my recipe proposal |

## Pass over this table (V5)

Scripted after the last edit: every R-, M- and SC- id named in table a exists in its file; every landed-in file exists; every tagged ID in `matrix.md` (96) has a row. Worked examples re-read after the S-133, SC-08 and S-194 changes: `we` §1 (sync and tails), §2 (merge window), §3 (baked vs room reverb) and §4 (windup) use the new rules.

## Repair round 1 (review `reviews/sound-designer-rev1-reviewer.md`, verdict fix-first)

> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22 (repair round 1)

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (blocking) R-31 measured RMS, not loudness or peak | New measure `rv` §4 F-13 (pad every compared file to one common length, the longest plus 0.4 s; integrated LUFS with pyloudnorm); R-31 rewritten (variants of one sound: F-09 ±1 dB; different spectra always F-13; paid reveal results F-13 within 1 LU and F-03 sample peaks within 1 dB); F-09 wrong-number cell names the K-weighting trap; SKILL §4 D-03 points to F-13 and F-03; `we` §4 stage and checks lines; `cp` §5 and `rv` §2 check-in B options loudness-matched by F-13; `emotion-recipes.md` S-18 now F-13. The V3 run below found a second silent trap (unequal padding) and wrote it into F-13 |
| F2a (blocking) Doppler misread | `ra` §B Doppler row: DopplerScale is legacy-only, the docs say it does not affect AudioPlayer or AudioEmitter (`SoundService.yaml:178-195`), the graph classes have no Doppler property; SC-10 rewritten (no baked pass-by in a loop because it repeats every cycle; a pitch pass-by is a scripted PlaybackSpeed change or a one-shot whoosh, or none); `we` §1 edit line re-read and rewritten; proposals library row (c) corrected |
| F2b (blocking) distance-curve inspection read the wrong value | `ra` §G distance row: read `DistanceAttenuationMode` first; Custom → `GetDistanceAttenuation()` keys (empty = the default curve); preset → `DistanceAttenuationBounds` + mode (the custom curve is ignored though still returned, `AudioEmitter.yaml:135-185, 349-365`); the listener's own curve multiplies with it (`AudioListener.yaml:287`, `:450`); `rv` R-16 says so. Not run in Studio: `list_roblox_studios` returned no instance (2026-10-22) |
| F3 (blocking) 5 findings with rules but no checks | SD-28: `rv` R-62 (the pick's F-01..F-10 beside the category reference's), `rv` §2 check-in B (reference heard after the options), `cp` §5 dead pointer replaced (§8 References row), `cp` §8 References row. SD-21: new `rv` R-35 (F-10 at least 3 st (P) apart or a different F-06 main band), R-53 and a check-in C question (sequence listen), R-13 points to R-35, `we` §1 R-35 line. SS-05: new `rv` R-34 (onset-to-peak, threat shorter than friendly), F-02 cell (measure the attack layer's part). WT-02: new `rv` R-33 (F-10 step per tier equals the declared S-82 step in every family, F-05 decay grows; harmonic-trap note), `cp` §3 points to it. GD-02: `rv` R-22 (an in-play celebration ends within about 2 s by F-04). New lines are rows appended to `rv` §3b (no renumbering); SKILL §2 steps 3 and 7 and §5 name them |
| R1 D-07 wording | SKILL §4 D-07: no countdown tension or siren on any paid roll; restricted players never reach one (`ArePaidRandomItemsRestricted`); never sort players by age or region for sound. `rw` S-164 now points to D-03 and D-07 instead of restating them (V4 diff against `platform-policy/references/rules.md` §A, §D: ours is stricter, never looser) |
| R2 DC offset and F-10 band | `rv` §4 preamble: subtract each channel's mean first (with its three effects named); F-10: band to 12 kHz for chimes, sparkles and ticks, the peak's height above the band median reported, a note trusted only at 20 dB or more |
| R3 sync and attempt/outcome copies | Sync numbers now live only in SKILL S-133; `cc` field 22 and its example say "inside the S-133 window"; `cp` §2 stage-sheet Sync cell "S-133 window"; `rv` R-43 and R-54 name S-133 and keep only the signed bounds they compare. Attempt/outcome: R-07 is the check, the `cp` §2 rows are a worked sheet, SKILL §7 #19 the principle, the role's "Before you hand back" a one-line reminder: each is a different use and none restates numbers (kept) |
| R4 wiring self-check lost | `rv` R-40 (S, G): cosmetic SFX on the client from replicated events; pooled AudioPlayers (Client data model AudioPlayer count flat across a 10 s burst) that set `Asset` from the cue table; `ra` §G graph row adds the count; SKILL §5 graph line names client playback and pooling |
| R5 same-wave proposal rows | adopted: see the V11 table below |
| R6 animator books still say the sound window is wider | not my files: proposals row added for the lead |
| R7 SKILL.md size | done: S-75 and S-78 moved to `cs` §B as rows (header updated); the "Rules by topic" index moved from §3 to the top of §6 (routing) and §3 points to it. §1-§5 now end at 19,088 bytes (19,541 before the repair) |
| R8 evals check 3.5 | proposals evals row extended with (d) |
| keep list | all ten kept in substance; the F table gained F-13 and two traps, the check-ins gained the reference listen and the sequence question |

Other changes found on re-read (same rules): `genre-presets.md` destruction row and `emotion-recipes.md` power row said "dry assets + engine reverb", which contradicts SC-08; now "designed tail baked, room from the zone reverb". `we` §2 names the coin's tier (T1) and the milestone (T2) from the reward tier table; `we` §3 names the substitute material for a refused glass floor.

### d2. V3 runs, repair round 1

Script `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r1/sound-designer-r1-v3.py` (soundfile 0.14.0, numpy 2.4.6, scipy 1.17.1, pyloudnorm), output `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r1/sound-designer-r1-v3-out.json`, WAVs beside it (48 kHz float). Measures computed as `rv` §4 now describes (mean removed first).

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| R-31 (F-09 vs F-13) | loudest-400 ms RMS; F-13 padded LUFS | two 1.2 s results, same envelope, 220 Hz vs 3,520 Hz | F-09 −13.56 vs −13.56 dBFS (would pass); F-13 −19.81 vs −15.69 LUFS (4.1 LU apart, fails D-03): right |
| R-31 (F-03) | sample peak | the 220 Hz result with a 3 ms click added | F-13 within 0.2 LU of the plain one (passes); sample peak −5.03 vs −6.04 dBFS (1.0 dB louder, at the limit). Loudness parity alone misses a click: R-31 pairs F-13 with F-03 (right) |
| F-13 padding | the set padded to the longest, longest + 0.4 s, + 1 s, + 5 s; and each file to its own length | 4 results incl. a 250 ms one | longest + 0.4 s and more: stable (−19.81, −15.69, −19.68, −17.44); padded to the longest only: 0.6 LU drift; each to its own length (0.4 s minimum): the 250 ms result reads −14.45 instead of −17.44, 3 LU off with no error. Written into F-13 (one common length, the longest + 0.4 s) |
| F-13 short file | pyloudnorm on a 250 ms result padded to the common length | 250 ms tone | measured without error (the old "under 0.4 s errors out" no longer applies once padded) |
| §4 preamble (DC) | F-01, F-06 share below 300 Hz, F-04 with and without mean removal | 4 kHz tick, 20 ms leading silence, +0.02 DC | raw: below-300 Hz share 28.7 %, F-04 300 ms with `ends_above` true (both wrong, no error); mean removed: 0.0 %, 30 ms, flag false (right). F-01 read 20.3 ms both ways because this offset sat below peak −30 dB; a larger offset reads 0 ms (reviewer's run) |
| F-10 band and height | strongest peak 60 Hz-4 kHz vs 60 Hz-12 kHz; height above the band median | 5,274 Hz chime with −48 dB noise; 523 Hz chime | 4 kHz band: 606 Hz "D#5 −45 c", height 11 dB (wrong note, caught by the 20 dB rule); 12 kHz band: E8 +0 c, 72 dB (right); 523 Hz: C5 in both bands, 72 dB (right) |
| R-34 | F-02 minus F-01 | threat (2 ms attack + noise burst), friendly (40 ms attack), friendly with a small pre-click | rise 4.2 ms vs 39.2 ms (right); the pre-click moves F-01 only (40.2 ms, still right). Wrong with no error: a threat whose later body is louder than its tick reads slow, so the F-02 cell says measure the attack layer's part |
| R-33 | F-10 per tier, steps in st | 4 body tiers (110 Hz base, weak fundamental, 2nd harmonic strongest), −4 st per tier | steps 4.00, 4.03, 4.00 st (right). The harmonic trap cancels while the same partial is strongest in every tier; R-33 names the 7 / 12 st symptom when it does not |
| R-35 | F-10 notes | signatures E5, G5, F5 | E5 vs G5 3 st apart (pass); E5 vs F5 1 st (flagged): right |
| R-22 (celebration) | F-04 end point and flag | 3 s file, 250 ms decay; a 600 ms-decay celebration cut at 1.5 s | 1,170 ms, flag false (pass under 2 s); 1,500 ms with the flag true (cut tail caught by the flag, as F-04 says) |
| R-16, R-40 (S) | Studio MCP `list_roblox_studios` | — | no Studio instance connected: not run; `ra` §G keeps "first use in a game job is a probe" |

### V11 rows from same-wave roles (repair round 1)

| Proposal row (from) | Adopted / declined | Where / why |
| --- | --- | --- |
| `proposals/progression-designer.md` row "`.agents/skills/sound-design` (wave 2 maker)": map reward tiers to T1-T4, rates from the table | adopted | `rw` §B S-194 (T1 → A, T2 → B, T3 → C, T4 → the rare tier of S-53; measured rate); `cp` §1 input row, §9 partner row; `rv` R-15; role partner table; `we` §2 |
| `proposals/ui-ux-designer.md` row "`sound-design/SKILL.md` (sound-designer maker, wave 2)": UI cue list keyed to the UI event names | adopted | `cp` §2 "UI cue list (per screen)" (press, confirm, refusal at most about one per 0.5 s (P), reward per tier, count tick and closing sound), cue ids into the motion table's Sound column; SKILL §1 deliverable 2; `cp` §9 and role partner rows |
| `proposals/environment-designer.md` row "`sound-design/SKILL.md` (sound-designer, wave 2)": own the footstep table; a refusal names the material to use; read the emotion per zone and the signature element | adopted | `cp` §1 ambience and floor rows, §8 footstep table, §9 env row; `rv` R-17; role job-flow line and partner table; `we` §3 |
| `proposals/film-director.md` and `proposals/vfx-designer.md` S-133 rows | already met in the rebuild (SKILL S-133) | — |
| `proposals/film-director.md` row `tools/film/shotlist.py` (`log-diff --pair ... --window`) | supported (not against my books) | the same need as my `shotlist.py` row; when it lands, R-43 should name the mode |

### V5 pass, repair round 1

Scripted after the last edit: every R-, F- and SC- id named in the role file, SKILL.md and every reference resolves to a defined row (R: 52 rows incl. R-33 to R-35; F-01 to F-13; SC-01 to SC-17); S-75, S-78, S-82, S-133, S-150, S-164, S-194 still defined; role frontmatter identical to `HEAD`; skill description 328 characters; LF endings in every book file; the J018 phrase in every book file header. Worked examples re-read after the R-31, SC-10, S-194 and footstep changes: `we` §1 (Doppler, R-35), §2 (tiers), §3 (the refusal names Slate), §4 (F-13 + F-03) use the new rules.

## Repair round 2 (review `reviews/sound-designer-rev2-reviewer.md`, verdict fix-first)

> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22 (repair round 2)

| Review finding id | Fixed where / declined: why |
| --- | --- |
| B1 (blocking) F-13 integrated loudness lets a louder rare result hide behind a longer tail | `rv` §4 F-13 split: (a) integrated, padded to one length, for options and siblings; (b) momentary maximum, for paid results: window 400 ms or the shortest compared file's length if shorter, 10 ms steps, `pyloudnorm.Meter(rate, block_size=window)`. The wrong-number cell names the tail hole (a), the fixed-window hole for results under 400 ms (b) and the residual short-burst hole (under about 50 ms at equal peak: asked at check-in B "does any result hit harder?"). The fixed-window hole was found by my V3 run: an honest 300 ms result read 3.0 LU louder than a 150 ms one on a padded 400 ms window, so the fix as first proposed would have failed a correct design and pushed the agent to shorten or quieten the rarer result. `rv` R-31 (paid results by F-13 b, never a); SKILL §4 D-03 "momentary maximum within 1 LU, F-13 b"; `we` §4 stage and checks lines re-read and rewritten; options and A/B references now say F-13 a (`rv` §2 check-in B, `cp` §5, `emotion-recipes.md` S-18); proposals `cue_check.py` row names both measures |
| B2 (blocking) the pooling check passes create-per-hit code | `ra` §G: new row "Pooling (creation counter)": a `game.DescendantAdded` counter for AudioPlayer and Sound on the Client data model, warm-up, reset, 10 s burst, pooled = 0; it says why a before/after count is never used; first use is a probe (does the connection outlive the `execute_luau` call); the counter misses an unparented player and the grep misses a template `:Clone()`, so both run. The graph row lost its count. `rv` R-40: (S) no AudioPlayer or Sound created during the burst after warm-up; (G) no `Instance.new("AudioPlayer")` outside the pool module. Proposals: the `engineering-craft` debug row now also asks for a burst test hook. Docs: `Instance.yaml:2329-2341` (DescendantAdded fires for every descendant); studio-mcp C-03 (Client data model `execute_luau`); the AudioPlayer page does not say whether an unparented player plays (hence the probe) |
| B3 (blocking) R-34 fails correct tells and warnings | `rv` R-34 scoped to threat hits and attacks (impact and contact one-shots) against friendly one-shots; tells, warnings, charges and build-ups excluded (S-76, R-09, R-28). SKILL SC-11 and §7 #5 now say "threat hits" (SC-11 adds that tells and warnings rise by design); the §7 #5 check column names R-34 (F) |
| R1 bag-full example sized like a milestone | `we` §2: "the bag-full event at T2 (small goal)"; "Bag full (T2) gets its own short confirm, 150-300 ms (S-194 tier B), not a milestone flourish"; its R-15 check compares with the bag-full confirm. Matches `progression-design/references/reward-tiers.md` §2 (T2 small goal) |
| R2 evals 4.2, 4.3 grade the old wording | proposals evals row: (e) added (4.2 → D-07 on any paid roll; 4.3 → odds as numbers before purchase per `platform-policy` rules §A, S-166) |
| R3 coverage cites `AudioListener.yaml:398` | fixed to `:450` (repair round 1 row F2b) |
| keep list | all seven kept; the only keep-list line edited is R-34's scope (B3) |
| weak spot (not a finding): 38 KB always loaded, eleven steps for every job | declined this round: a minor cue already runs on the short card, is picked by numbers and is heard only at check-in C (`cp` §5 listening budget); cutting steps would change the step order the keep list names. Left as a note for the owner, not a change |

### d3. V3 runs, repair round 2

Script `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r2/sound-designer-r2-v3.py` (soundfile 0.14.0, numpy 2.4.6, pyloudnorm), output `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r2/sound-designer-r2-v3-out.json`, WAVs beside it (48 kHz float, mean removed before measuring, as `rv` §4 says). Grep sample: `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r2/sound-designer-src/`. Studio: `list_roblox_studios` returned `{"studios":[]}` (2026-10-22).

| Check id | Command or tool mode | Sample input type | Result |
| --- | --- | --- | --- |
| R-31 (F-13 a vs b) | integrated (padded) vs momentary maximum (400 ms, 10 ms steps) | common result: click + 300 ms body; rare result: same peak, body made 3 dB denser by soft clipping, + 600 ms tail 7 dB down | integrated 0.33 LU apart (would pass: the hole); momentary maximum 2.88 LU louder (fails D-03: right); sample peaks equal (F-03 alone passes it) |
| R-31 (F-13 b) | same | honest rare result: same body level, 2 extra notes, 2× tail | 0.22 LU (passes: right) |
| F-13 b window | 400 ms padded vs window = shortest file (150 ms) | common 150 ms; rare 300 ms honest; rare 300 ms with the louder body | 400 ms window: honest reads +3.02 LU (wrong, no error: a correct design fails); shortest-file window: honest +0.07 (right), louder +2.62 (fails: right). Written into F-13 b |
| F-13 b short file | momentary maximum on a 150 ms file padded to the window | 150 ms result | runs without error (−14.94 LUFS) |
| F-13 b residual | momentary maximum | 30 ms square burst at equal peak inside the body (3.2 dB louder on a 30 ms window) | 0.81 LU: passes with no error; written into F-13's wrong-number cell (under about 50 ms; the check-in B question "does any result hit harder?") |
| R-34 (scoped) | F-02 minus F-01 | threat hit (2 ms attack noise), friendly pickup (40 ms attack), rising 1 s warning | threat 4.1 ms < friendly 38.7 ms: PASS (right); warning 999.5 ms: the old R-34 failed it, the scoped line excludes it (right) |
| R-40 (G) | Grep `Instance\.new\(\s*["']AudioPlayer["']` outside the pool module | synthetic `src/`: a pool module, a per-hit `Instance.new( 'AudioPlayer' )`, a per-hit `template:Clone()` | finds the per-hit creation with spaces and single quotes and excludes the pool module; misses the `:Clone()` (wrong with no error: written into `ra` §G, where the counter catches it) |
| R-40 (S) creation counter | Studio MCP `execute_luau` (Client data model) | — | not run: no Studio connected; `ra` §G marks the first use as a probe |

### V11, repair round 2

| Proposal row (from) | Adopted / declined | Where / why |
| --- | --- | --- |
| `proposals/ui-ux-designer.md` row at line 18 (G3 UI-screen recipe: the sound designer joins the motion storyboard with the UI cue list) | supported (a recipe, not my books) | my UI cue list (`cp` §2) is the input it names |
| `proposals/art-director.md` row at line 17 (the art bible gains a "Sound pointer" section) | supported (not my books) | meets my art-bible row (identity sheet linked from the art bible) |
| all rows listed in the round 1 tables | unchanged | — |

### V5 pass, repair round 2

Scripted after the last edit (`C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r2/sound-designer-r2-v5.py`): every R-, F- and SC- id named in the role file, SKILL.md and every reference resolves (R: 52 rows, F-01 to F-13, SC-01 to SC-17); "F-13 a" and "F-13 b" are the only F-13 sub-labels used; every R id in table a exists; LF endings and the J018 phrase in every book file; no "Riot" or library id in any body; SKILL.md 205 lines, description 328 characters, §1-§5 19,157 bytes; role frontmatter identical to `HEAD`. Worked examples re-read after the F-13, R-34 and S-194 changes: `we` §2 (T2 confirm 150-300 ms, R-15 against it) and §4 (F-13 b and F-03) use the new rules; §1 and §3 use none of the changed lines.

## Repair round 3 (review `reviews/sound-designer-rev3-reviewer.md`, verdict fix-first)

Scripts and files: `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r3/` (`sound-designer-r3-v3.py` runs the recipe exactly as `rv` §4 now writes it, output `sound-designer-r3-v3-out.json`; `sound-designer-r3-diag2.py` compares the two end-point rules). Values are F-13 b rare minus common, in LU; the D-03 limit is 1 LU.

| Finding | Fixed where | Test input and result |
| --- | --- | --- |
| B1 (blocking) F-13 b window follows the file length, so trailing silence fails honest results | `rv` §4 F-13 b Compute: "trim each result to its F-12 sound before measuring; window = 400 ms, or the shortest trimmed result's length if shorter". Wrong-number cell (b): "trailing silence in a delivered file makes the window longer and fails an honest longer result by up to about 3.6 LU: trim first". The sound is defined once in F-12 (F-01 onset to the last sample at or above the peak minus 40 dB). I used sample resolution, not F-04's 10 ms window end: the grid end added up to 10 ms to a short result (next row). R-31, D-03 and `we` §4 name F-13 b and need no change | Reviewer's short pair (common 120 ms 880 Hz; rare 240 ms 880 + 1,320 Hz, same sample level), trailing silence 0 / 100 / 300 ms: untrimmed 1.09 / 3.26 / 3.59 (window 0.12 / 0.22 / 0.40 s); trimmed 1.09 / 1.09 / 1.09 (window 0.12 s). The verdict no longer depends on padding. The 1.09 is K-weighting (the 1,320 Hz note reads about 1 LU louder at the same sample level): a true difference, now named in the cell. Reviewer's egg pair (click + 300 ms body; honest: + extra note + tail): unpadded 0.38; both with 250 ms silence: untrimmed 1.47 (false FAIL), trimmed 0.38 (PASS); only the common result padded: 1.47 untrimmed, 0.38 trimmed. Reviewer's egg trap (near-square body + tail): 2.92 unpadded, 2.92 trimmed and padded (FAIL: right). Round-2 files: trap (`r2-common` vs `r2-rare-loud-body-long-tail`) 2.64 unpadded, 2.64 with 300 ms silence (FAIL: right); honest 2× tail −0.04 / −0.04 (PASS); short honest (150 vs 300 ms) 0.07 / 0.07, untrimmed padded 3.02; short loud 2.62 / 2.62 (FAIL: right) |
| B1, real input types | the recipe reads every format through `soundfile` (`always_2d`, DC removed) | Short honest pair delivered as stereo, 44.1 kHz, DC offset 0.01, a −70 dBFS noise floor under 300 ms of trailing silence. Untrimmed: 3.59 (WAV 16-bit), 3.61 (OGG Vorbis), 3.60 (MP3), 3.59 (FLAC): all false FAILs. Trimmed: 1.09, 1.16, 1.10, 1.09. The noise floor does not move the end point; the OGG codec smear adds 3 ms (0.07 LU). Egg trap as OGG and MP3, padded: 2.90 and 2.91 (FAIL: right). No errors |
| B1, end-point rule (found in this round) | F-12 sound: last sample at peak −40 dB, not F-04's 10 ms window end | `diag2`: F-04 window end vs sample end. OGG short pair 1.41 vs 1.16 (the grid adds 10 ms to the 123 ms common result); common result started 5 ms off the grid: 1.19 vs 1.09. WAV and MP3 equal under both rules. The 10 ms grid is wrong with no error by up to 0.3 LU on results near 120 ms |
| R1 `pyloudnorm` raises when the block equals the result's length | F-13 b Compute: `Meter(rate, block_size=(window samples − 1) / rate)` with the reason | 492 noise lengths, 1,000 to 19,200 samples: block = n / rate, 33 errors; block = (n − 1) / rate, 0 errors. Every B1 run above uses the new block size: no errors on any length or format |
| Same kind (my search): F-09 "or the whole file if shorter" reads trailing silence as quieter | `rv` §4 F-09: RMS of the loudest 400 ms window of the F-12 sound; wrong-number cell names the trap. R-31 uses F-09 for variants of one sound | Variant pair, 200 ms 440 Hz, one with 300 ms of trailing silence: untrimmed −13.47 vs −16.48 dBFS (3 dB: a false FAIL of R-31's ±1 dB); trimmed −13.47 vs −13.47 |
| Same kind: length checks read the file length | `rv` §4 F-12 Compute (file and sound length) and wrong-number cell; `rv` R-08 "(F-12 sound length)"; SKILL §4 D-03 tail "up to 2× the shortest result's F-12 sound length" | Tell of 600 ms with 400 ms of trailing silence: file 1,000 ms, sound 600 ms. A tell checked by file length would pass a reaction window it does not fill |
| Same kind, checked, no change: F-13 a | none: (a) pads the set to one common length, and silence blocks fall under the gate | Options 440 vs 660 Hz, 600 ms; B with 500 ms of trailing silence: −15.44 / −15.29 LUFS both ways. F-05, F-06, F-10 and F-11 read the loudest part or power shares: silence does not move them. R-26 bed length keeps the file length on purpose (a loop plays its silence) |
| R2 pooling counter counts re-parents and character Sounds | `ra` §G pooling row: before the warm-up, a weak-keyed set of every AudioPlayer and Sound (existing ones and every one `DescendantAdded` brings); during the burst count only those not in the set and not under a model that holds a Humanoid; the reason (the event fires on every re-parent; S-224 resets `parent`) | Docs: `Instance.yaml:2335-2337` ("parenting an object ... will fire the event for this object and all of its descendants"). Not run: no Studio connected in this round; the row's first use stays a probe. R-40 unchanged |
| R3 animator lines (lead) | not my files | proposals row for the lead is present (last row) |
| Proposals | `proposals/sound-designer.md` `cue_check.py` row: the sound length, F-09 on the sound, F-13 b trim and block size; the round-3 holes; offline tests on the round-1 to round-3 pairs (honest and trap, with and without trailing silence, WAV, OGG, MP3, FLAC) so a later change cannot reopen a hole | — |

### V5 pass, repair round 3

`sound-designer-r2-v5.py` re-run after the last edit: every R-, F- and SC- id resolves (R: 52 rows, F-01 to F-13, SC-01 to SC-17), no problems; "F-13 a" and "F-13 b" are the only F-13 sub-labels; SKILL.md 205 lines, description 328 characters, §1-§5 19,177 bytes; role frontmatter identical to `HEAD`; LF endings in every changed file; no Riot name or library id in the changed lines. `we` §4 re-read: it names F-13 b and F-03 and inherits the trim from F-13 b.

## Repair round 4 (final) (review `reviews/sound-designer-rev4-reviewer.md`, verdict fix-first)

> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22 (repair round 4, final by the lead's decision)

Scope set by the lead: apply the reviewer's tested smallest fix, make every measuring recipe a labelled screening aid with its known false readings, no new measuring code; the measures move to a tested kit tool only with the owner's yes (proposals row, G3).

| Finding | Fixed where | Note |
| --- | --- | --- |
| B1 (blocking) F-13 b window grows with a noise floor or a reverb tail | `rv` §4 F-13 b Compute: "measure all channels; window = 100 ms, or the shortest trimmed result's length if shorter". Wrong-number cell (b) rewritten: the growing window (3.59 LU at a −50 dBFS floor, 2.80 LU with −20 dB wet reverb), all channels, K-weighting, the 100 ms window sees the loudest 100 ms only (bells), the short-pluck case, the dense-burst clause updated (20 ms passes at 0.26 LU, 30 ms square reads 1.22 LU), the trim inherits F-12's floor limit | the reviewer's fix as written |
| B1 F-12 and F-09 end point | `rv` §4 F-12 Compute: end of the last 10 ms window within 40 dB of the loudest (as F-04), then the last sample at or above peak −40 dB inside it; the cell names the floor limit (a floor within about 40 dB of the loudest window still reaches the file end) and that a reverb tail above the limit is part of the sound. The F-09 and F-04 cells name the noise-floor reading | F-09 uses the F-12 sound, so it inherits the new end; R-08 and D-03 use the F-12 sound length and need no change |
| R1 pooling counter | `ra` §G pooling row: warm-up = one 10 s burst at the real top rate, count during a second burst; the Humanoid clause dropped for "no character spawns or respawns during the counted burst, else run it again"; each counted instance's full name printed. `rv` R-40 (G): grep `Instance.new("AudioPlayer")` and `Instance.new("Sound")` | not run: no Studio in this job (rounds 2-4) |
| Screening aids (lead's scope) | `rv` §1: every T, F, S, L and G reading is a screening aid; a failing or borderline reading is checked by eye (plot, instances, log lines) and by the owner's ear for level, feel or timing before any fix note; a pass on a known false-reading case is checked the same way. `rv` §4 intro: the rule, borderline = within about 20 % of the limit or 0.5 dB / LU (P), result written "MEASURED, screened: ..."; the last column renamed "Known false readings". `rv` R-40, R-43, R-44: a screening sentence beside each command. `ra` §G: a "Known false readings" column on every check. SKILL.md §1 "You cannot hear" paragraph: one sentence pointing to the rule | role file not edited (it has no recipe; SKILL.md carries the rule into every task) |
| Proposals | `proposals/sound-designer.md` `cue_check.py` row rewritten as **G3**: a tested kit tool with these cases as fixtures, each reading carrying the false readings its case matches | — |

### d5. V3 runs, repair round 4 (final)

Script `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r4/sound-designer-r4-v3.py` runs F-12, F-09 and F-13 b exactly as `rv` §4 now writes them, beside the round-3 rule (per-sample end, window up to 400 ms) on the same files; output `C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/sound-designer-r4/sound-designer-r4-v3-out.json`, WAVs beside it (written and read back; 16-bit unless stated). Round-2 and round-3 files are read from `sound-designer-r2/` and `sound-designer-r3/` in the same scratchpad. pyloudnorm, numpy 2.4.6, scipy 1.17.1, soundfile 0.14.0. Values: F-13 b rare minus common, in LU; the D-03 limit is 1 LU. "K" = the honest short pair's true K-weighting difference (1,320 Hz vs 880 Hz note, about 1.09 LU), which the cell names; right = within 0.15 LU of it.

| Case | New window | New F-13 b | Round-3 rule (window, value) | Right? |
| --- | --- | --- | --- | --- |
| short honest pair, digital silence 0 / 100 / 300 ms | 100 ms | 1.08 / 1.08 / 1.08 | 120 ms, 1.09 each | yes (K) |
| short honest, peak −1 dBFS, noise floor −70 / −60 / −55 dBFS | 100 ms | 1.08 / 1.08 / 1.08 | 120 ms, 1.09 | yes (K) |
| short honest, peak −1 dBFS, noise floor −50 / −45 dBFS | 100 ms | 1.08 / 1.09 | 400 ms, 3.59 / 3.59 (false FAIL) | yes (K); fixed |
| short honest, peak −12 dBFS, floor −70 / −60 dBFS | 100 ms | 1.08 / 1.09 | 120 ms 1.09 / 400 ms 3.59 (false FAIL) | yes (K); fixed |
| one pluck vs three, dry; reverb −30 / −25 dB wet on both | 100 ms | 0.00 / 0.00 / 0.00 | 150 ms, 0.00 | yes |
| one pluck vs three, reverb −20 dB wet on both | 100 ms | 0.00 | 244 ms, 2.80 (false FAIL) | yes; fixed |
| egg honest, silence 0 / 250 ms | 100 ms | 0.51 / 0.51 | 303 ms, 0.50 | yes (pass) |
| egg trap, silence 0 / 250 ms | 100 ms | 3.00 / 3.00 | 303 ms, 2.99 | yes (FAIL) |
| round-2 trap, unpadded / 300 ms silence | 100 ms | 2.19 / 2.19 | 303 ms, 2.64 | yes (FAIL) |
| round-2 honest 2× tail, unpadded / padded | 100 ms | −0.10 / −0.10 | −0.04 | yes (pass) |
| round-2 short honest (150 vs 300 ms), unpadded / padded | 100 ms | −0.04 / 0.10 | 150 ms, −0.03 / 0.07 | yes (pass) |
| round-2 short loud, unpadded / padded | 100 ms | 2.37 / 2.51 | 150 ms, 2.52 / 2.62 | yes (FAIL) |
| round-2 30 ms square burst (3.2 dB louder on its own 30 ms) | 100 ms | 1.22 (FAIL) | 303 ms, 0.81 (missed) | yes, just over the limit: borderline, screened by the rule |
| round-2 20 ms dense burst (soft-clipped, same peak) | 100 ms | 0.26 (pass) | 303 ms, 0.47 | known false pass: named in the cell, asked at check-in B |
| short honest as WAV 16 / OGG / MP3 / FLAC (stereo, 44.1 kHz, DC 0.01, −70 dBFS floor, 300 ms trailing part) | 100 ms | 1.08 / 1.12 / 1.09 / 1.08 | 120-123 ms, 1.09 / 1.16 / 1.10 / 1.09 | yes (K) |
| egg trap as OGG / MP3 | 100 ms | 2.73 / 2.75 | 303 ms, 2.90 / 2.91 | yes (FAIL) |
| common 44.1 kHz, rare 48 kHz | 100 ms | 1.08 | 1.09 | yes (K) |
| stereo, rare second note 0.5 ms Haas, all channels | 100 ms | 1.08 | 1.08 | yes (K) |
| rare with a −35 dB swell before the hit | 100 ms | 1.08 | 1.09 | yes (K; F-01 cuts the swell) |
| pluck vs the same pluck + a 1,320 Hz second note | 100 ms | 1.08 | 279 ms, 1.08 | K-weighting (register), named in the cell |
| 1 bell vs 5 overlapping bells, same peak | 100 ms | 0.18 (pass) | 400 ms, 2.71 | intended: more notes at the same level (D-03); named in the cell |
| 40 ms decaying pluck vs 600 ms sustained note, same peak | 40 ms | 8.45 (FAIL) | 40 ms, 8.45 | a true difference in the window, but a case to look at before a fix note; named in the cell |

F-12 and F-09 (200 ms 440 Hz variant, peak −1 dBFS, 300 ms trailing part):

| Trailing part | New F-09 / sound length | Round-3 rule F-09 / sound length |
| --- | --- | --- |
| digital silence; −70 / −60 / −55 dBFS floor | −4.05 dBFS / 200 ms each | −4.05 / 200 ms each |
| −50 / −45 dBFS floor | −4.05 / 200 ms each | −7.06 / 497 and 500 ms (false 3 dB drop) |
| −42 / −40 dBFS floor | −7.06 / 500 ms each | −7.06 / 500 ms |

The −42 and −40 dBFS floors sit within 40 dB of the loudest 10 ms window (about −4 dBFS RMS), so the window step keeps them as sound: the floor limit the F-12 cell now names (look at the waveform when the sound length is near the file length). Other F-12 runs: 600 ms tell with 400 ms of silence: file 1,000 ms, sound 600 ms; 150 ms pluck with −30 dB wet reverb: sound 150 ms; with −20 dB wet: 245 ms (the tail is above the limit and part of the sound, named in the cell). Block size (window samples − 1) / rate on every length from 300 samples to 100 ms in steps of 7 at 22.05, 44.1 and 48 kHz: 0 errors.

Not run: the pooling counter and every §G check (no Studio connected in this job; the rows stay probes). No new measuring code beyond the tested fix: the recipe script above is the book text, run once.

### V5 pass, repair round 4

`sound-designer-r2-v5.py` re-run after the last edit: every R-, F- and SC- id resolves (R: 52 rows, F-01 to F-13, SC-01 to SC-17), no problems; "F-13 a" and "F-13 b" are the only F-13 sub-labels; SKILL.md 206 lines, description 328 characters; role file not edited (frontmatter identical to `HEAD`); LF endings in every changed file; no Riot name or library id in the changed lines; headings unchanged except the §4 table's last column header; nothing renumbered.
