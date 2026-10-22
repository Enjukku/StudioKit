> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018).

# Craft process: from event to finished cue

The how behind SKILL.md §2 steps 1-9 and the SC rules in §3. Numbers marked (P) are start values a check may
change. Self-review lines R-xx live in `review.md` §3; the measures F-xx in `review.md` §4.

## 1. Inputs to read before the first cue (and whom to ask when one is missing)

| Input | Owner | What I take from it | Ask when |
| --- | --- | --- | --- |
| Direction sheet: the target-experience line | lead, direction leads | quoted on every card (field 43) | before step 1 |
| Feature spec feedback stack (`preproduction/references/documents.md` §6) | game designer | named stages, attempt cue, outcome response and its confirmation source, outcome tiers, failure and refusal cues, celebration tier and length, frequency and merge window | before step 2 |
| Threat and hazard sheets (same file §7) | game designer | the reaction window, the tell channels, escalation | before step 2 for any enemy or hazard |
| Read rank and information list (same file §9) | game designer | loudness tiers and caps per scene; what the player must know per moment | before step 1 |
| Timing list (`templates/anim/timing-list.md`) and the clip card's verb | animator | event ids, seconds, source frame, consumers, end-of-state tells; the mechanic verb; beat-sheet sound words | draft (blocking) markers before the temp pass; the final revision before the edit pass |
| VFX frame script | VFX designer | the flash or peak frame, the shared envelope (wind-up, peak, tail) on the same event ids | co-design before either builds |
| Ambience map (`templates/environment/ambience-map.md`) | environment designer | zones, the emotion per zone (`feeling`), the stage's signature element, causes, point sources, checkpoints, reverb approach per space, shared state | before any ambience cue |
| Floor-material list | environment designer, modeler | every walkable material; new ones | before materials are built; I may refuse one I cannot cover in time, naming the existing material to use instead |
| Reward and celebration tier table | progression designer | tier T1-T4 per reward event (first and repeat), its confirmed trigger, its measured rate | before any reward cue; the cue's tier and rate come from it (`reward-and-juice.md` S-194) |
| Character card | art director | feel words, size, age, material, the nearest similar character | before any character or creature cue |
| UI event list with static states and the motion table | UI designer | every UI event, its static state, its tween timing | before UI cues |
| Game sound identity sheet (§8) | me | signatures, forbidden directions, tone words, sound-code table | first cue of a game: write it |

Missing and design-changing: state an assumption in the hand-back and continue, or ask (`rules/messages.md` §2).

## 2. The stage sheet (step 2)

One table per action, written before any source is chosen. Stage names are the timing list's names, never mine.

| Stage | Event id @ timing rev | Time (s) | Attempt / outcome | Layer(s) and job | Sync | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| charge | `charge_start` @ r2 | 0.133 | attempt | tonal signature rising, mech click | onset on the event | pitch and level rise to the release |
| release | `release` @ r2 | 0.433 | attempt | shot: tick + crunch + body | S-133 window | loudest point of the action |
| travel | projectile spawn | code | attempt | loop on the projectile's emitter | moves with it | no baked pass-by in the loop |
| impact | `contact_confirmed` | server | outcome | impact layers, tier by strength | same trigger as the flash | never on a miss |
| tail | after impact | +0.1 | outcome | ice crumble, slows like the verb | after its cause | longer than a normal hit |

- A visible stage with no sound needs a reason in Notes ("covered by the music hit").
- The tell of an enemy attack starts on the same event as the VFX tell, is identical every time, lasts the whole reaction window and stops on the damage event.
- A state with a timer or a breaking point gets a warning cue that rises in intensity before the end, keyed to its end-of-state event (for example `shield_break_warn`).
- Combos and multi-hit sequences keep the animator's unequal gaps; my cues follow the events, never an even grid.
- Each designed moving part (a sliding barrel, an opening blade, a retracting stock) gets its own mechanical cue on its event.

**UI cue list (per screen).** Keyed to the UI designer's event names; each cue id goes into the Sound column of the game's motion table.

| UI event | Cue | Keyed to | Rate rule |
| --- | --- | --- | --- |
| press | soft tick (S-129) | the input event, first changed frame (attempt) | none; release is its own quieter cue |
| confirm | short rise (S-130, S-220) | the confirmed outcome | — |
| refusal | soft "no" (S-220 invalid family) | the refusal event (client check or server rejection) | at most about one per 0.5 s (P) when spammed |
| reward | per tier of the reward tier table | the confirmed grant | one per merge window (S-194) |
| count | none per digit; a tick on the first coin arrivals, one closing sound on the last | the flight's arrival events | one per merge window |

## 3. Layers (step 4)

**Five layer jobs for a shot or a big impact.** Each layer has one job; remove it and that job is missed.

| Job | Layer | Band (P) | Notes |
| --- | --- | --- | --- |
| Weight | low body | 40-250 Hz, with harmonics above 300 Hz for phones | only the release and impact stages keep it |
| Contact | high tick or transient | 2-8 kHz, 2-10 ms | on the first ms of the file |
| Violence | concussive crunch | 500 Hz-4 kHz | carries the hit on phone speakers |
| Space | report or echo tail | 200 Hz-3 kHz | lower and further back for distant shooters |
| Identity | the signature element, unprocessed | its own register | the same element in every stage |

Smaller events use fewer layers (S-78); UI and pickups use their recipes in `craft-satisfying.md` §B.

**Bands (SC-06).** Write each layer's main band, the low-end owner and each bright layer's low cut on the card, so layers do not mask each other; tonal stems stay separate from mechanical and noise parts.

**Size and weight.** Pitch sets size: down is bigger and heavier, up is smaller, lighter, magical (S-82: about 3-5 st per size class, the same step in every family; checked by R-33). Giants and bosses: low, slow, long settles, the ground they touch (S-45). Light vs heavy and telegraphed envelopes: S-76.

**Ambience (from the ambience map).** Per zone: a base bed only where the place needs one, intermittent detail one-shots,
point sources each with a visible cause (the map's anchors), one signature element that puts the player in this place,
footsteps per floor material and character foley (clothing, gear). Natural phenomena (wind, rain, water) come from
natural-sounding sources; a stand-in (wind from whistles) is named. Near and far versions for every important far source
(SC-07). Fill only the map's `sound:` keys.

**Build-ups.** A charge rises in pitch, level or density and is loudest at the release; a second charge sits higher than the first; a reversed copy of the impact or tonal layer swells into the release. For a variable-length charge, tween the playback speed up instead of stretching a file (S-144: speed changes length).

## 4. Temp pass (step 5): sound on the markers before polish

1. Search the game library first (§7) and existing assets of the game; reuse, retime, re-pitch.
2. Give every stage on the sheet a temp source, marked `TEMP` on the card; a stage still without one is listed.
3. Hand the temp cue list with event ids to the integrator, so the first playable or the animatic has sound on the markers.
4. Check-in A (`review.md` §2): the owner hears order, timing and the job of each stage, not polish.
5. Nothing gets final processing until the timing list revision is locked after check-in A.

## 5. Sources and options (step 6)

Generating is our recording session (prompt rules and template: `ai-generation-prompts.md`).
- Describe textures, not only the literal object: an ice slow can come from "dry palm leaves crunching", "foil crumpling slowly", "glass bottle tink". Write 2-3 texture descriptions per layer.
- Takes: 4 per texture description (P); at least 3 candidates per layer before a pick.
- One odd variant per layer: reversed, an extreme pitch, an unrelated texture. Keep good leftovers for the library.
- For a new setting, material or natural effect, write what the real thing sounds like (its attack, its tail, how it changes with distance) before prompting, and use at least one observed property.
- Each option takes its idea from a different source; one named unexpected element per signature cue.
- Hero and signature cues: 3-5 options built to the same finish and loudness-matched (F-13 a) before anyone listens; the first take is a warm-up, not a pick.
- Bracket a key number (pitch, tail length, gap, level) with a too-low and a too-high value, then pick between them.
- A tone shift (an event, a darker skin): one option pushed to the extreme and one pulled back to the identity sheet's tone words; the owner picks.
- Pick against the card and the category reference (§8 References; measured beside the pick by R-62, heard after the options at check-in B) with a stated reason; record why each rejected option lost.
- Listening budget: numbers (F-01..F-12) for every take; the owner hears at most 3 options per hero cue at check-in B; minor cues are picked by numbers and heard only in the mix at check-in C. Images: none (a plot only when a number fails and its cause is unclear).

## 6. Design pass and edit pass (steps 7-8)

**Design pass: make the building blocks.** Order (SC-09):

| # | Step | Purpose (write it on the card) |
| --- | --- | --- |
| 1 | Clean | trim silence to the transient, fade every cut and the last 10-30 ms, remove hiss, hum and rumble |
| 2 | Pitch | set size and register; shift pitched parts to the game key |
| 3 | Low cut | keep only the band this layer owns |
| 4 | Compress | control peaks; hard compression lifts a shimmering tail when the tail is the point |
| 5 | Add | overtones, delays, the designed space that glues the layers into one event |
| 6 | Compress again | the added material changed the dynamics |
| 7 | Transient | boost or add the first ms of every hit |
| 8 | Air, saturation | a little brightness or harmonics for phone speakers |

- A little at each step; compare raw and processed: the core must still be recognisable.
- Try the unprocessed take first; keep it when it works and write "unprocessed tried" on the card.
- Variants of one family (an upgrade tier, a mood variant) come from processing the base (pitch, phase, chorus) so the family stays recognisable.
- Movement: magic, travel and loop layers carry slow modulation (prompt words "spinning", "swirling", "passing", or chorus and flanger here); a one-shot whoosh gets a rise-then-fall pass-by envelope; a pitch bend only where the material suits it.
- Bake: every per-sound step above is rendered into the file. Live effects stay for context only: the zone's reverb, an underwater filter, ducks (SC-08).
- Beds and long loops: splice several takes with crossfades, a short fade on every splice, no repeat inside the first loop (S-100).
- File the results as parts in the library (§7).

**Edit pass: make them work in the scene.** A separate pass with its own judgement:
- Cut each stage to its event in the capture or animatic, with the other sounds of the scene present.
- Drop any layer the moment does not need (the sweetener test, S-77); trim every file to start on its transient.
- Set variants, jitter and cooldowns from the event rate (`repetition.md`).
- Place the cue in the mix (step 9, `mix-and-loudness.md`).

## 7. The game's sound library and data

| Tier | Holds | Tags |
| --- | --- | --- |
| Raw | generated or recorded takes, trimmed | texture, source prompt, date, rights |
| Parts | processed building blocks: tonal, mechanical, crunch, low body, tail, tick | job, band, pitch or key, length |
| Cues | finished cue files per stage and variant | cue id, stage, category, tier |

- Search the library before writing a prompt; the hand-back lists reused and new parts.
- Category folders and names follow the buses: `ui`, `sfx`, `foley`, `ambience`, `music` (S-141).
- Cue id → asset id → parts lives in one data table the integrator reads; no asset id is hard-coded in logic.
- Large jobs split by category (tonal and magic, impacts, mechanisms, environment) with one owner each, one integrator, and hand-over through library parts; the split is the lead's call.

## 8. The game's sound identity sheet

Written once per game (default path `output/sound/identity/sound-identity.md` unless the brief names one) and read before every cue.

| Section | Holds |
| --- | --- |
| Tone words | 3-5 words from the game profile and art bible; options outside them are rejected at brief stage |
| Signatures | per weapon, ability, character and the game itself: the signature element, its register and timbre, where it appears |
| Forbidden directions | sounds and styles this game never uses (and why) |
| Sound-code table | meaning → sound family (heal, damage, warning, reward, refusal, spotted, ready); one family never means help and harm |
| Footstep table | floor material (`Enum.Material`) → footstep set; a refused new material names the existing material to use instead; decorative material too small to read as a floor uses its neighbour's set; impact sets per material follow the same table and the level designer's material-to-rule table |
| Key and tempo | the music key and tempo per state (S-114) |
| References | per category, the reference sound file I compare against (its F-01 to F-10 sit beside each pick, R-62), and what it shows |

## 9. Partners: what I ask for, and when

| When | Partner | I ask for | I give back |
| --- | --- | --- | --- |
| Step 1 | game designer | the feedback stack, threat sheet, read rank and tiers for this feature | the cue list per state change; a missing cue or reason |
| Step 2 | animator | the draft timing list (event ids, verb, sound words, end-of-state tells) | the stage sheet keyed to its ids; a missing event as a request |
| Step 2 | VFX designer | the frame script on the same ids | the shared envelope (wind-up, peak, tail) as an exchange note |
| Step 1, stages | environment designer | the ambience map (emotion per zone, signature element) and floor-material list | the `sound:` keys; footstep sets; refusal of a material I cannot cover in time, with the material to use instead |
| Step 1, rewards | progression designer | the reward tier table (tier, trigger, measured rate) | reward cues sized per tier; a tier whose rate is too high for its cue length, as a finding |
| Step 2, screens | UI designer | the screen's event names and the motion table | the UI cue list (cue id per motion-table row) |
| Step 3 | art director | the character card and tone words | the signature plan per character |
| Step 5 | integrator (feature-builder) | the temp cues wired on the event ids; a debug cue log line per play (`cue <id> <event> <time>`) | the temp cue list and wiring notes |
| Step 9-10 | studio operator, owner | a playable preview for check-ins A and C; a device capture with sound for sync | the questions and pass rules for each check-in |
| Any timing change | animator | the new revision in the same hand-back | re-keyed stage sheet, acknowledged |
