> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Revised by J020 step 8 sound-designer · claude-opus-5-5 · high · 2026-10-23: the approved sound workflow (J020-D1 to D14): soundbench, takes per round, regenerate rounds, the play-test instead of check-ins. Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021-D4, on 982592c): target-experience sentence sets the emotion.

# Craft process: from event to finished cue

The how behind SKILL.md §2 steps 1-9 and the SC rules in §3. The tool for §5-§7 is the kit editor `soundbench` (`python -m tools.audio.soundbench <command>`; design: `knowledge/jobs/J020-sound-workbench/editor-design.md`; usage: `tools/audio/soundbench/README.md`). Numbers marked (P) are start values a check may
change. Self-review lines R-xx live in `review.md` §3; the measures F-xx in `review.md` §4.

## 1. Inputs to read before the first cue (and whom to ask when one is missing)

| Input | Owner | What I take from it | Ask when |
| --- | --- | --- | --- |
| Direction sheet: the target-experience line (kind of fun + the sentence of what the player must feel) | lead, direction leads | quoted on every card (field 43); the sentence sets the target emotion | before step 1 |
| Feature spec feedback stack (`preproduction/references/documents.md` §6) | game designer | named stages, attempt cue, outcome response and its confirmation source, outcome tiers, failure and refusal cues, celebration tier and length, frequency and merge window | before step 2 |
| Threat and hazard sheets (same file §7) | game designer | the reaction window, the tell channels, escalation | before step 2 for any enemy or hazard |
| Read rank and information list (same file §9) | game designer | loudness tiers and caps per scene; what the player must know per moment | before step 1 |
| Timing list (`templates/anim/timing-list.md`) and the clip card's verb | animator | event ids, seconds, source frame, consumers, end-of-state tells; the mechanic verb; beat-sheet sound words | draft (blocking) markers before the temp pass; the final revision before the edit pass |
| VFX frame script | VFX designer | the flash or peak frame, the shared envelope (wind-up, peak, tail) on the same event ids | co-design before either builds |
| Ambience map (`templates/environment/ambience-map.md`) | environment designer | zones, the emotion per zone (`feeling`), the stage's signature element, causes, point sources, checkpoints, the space type per zone (outside, small room, hall, cave: which zone reverb the script switches to, `roblox-audio.md` §H), shared state | before any ambience cue |
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

1. Search the game library first (§7) and existing assets of the game; reuse, retime, re-pitch (in the file, `varispeed`).
2. Give every stage on the sheet a temp source, marked `TEMP` on the card; a stage still without one is listed.
3. Hand the temp cue list with event ids to the integrator, so the first playable or the animatic has sound on the markers.
4. Proof (`review.md` R-50): the studio operator runs a play-test and returns the debug cue log; every temp cue fires on its event, in the stage order. No listening check-in (J020-LD3): if the owner plays the build and flags something, the owner's words go on the card and into a `lesson`.
5. Nothing gets final processing until the timing list revision is locked.

## 5. Sources, takes and ranking (step 6)

Generating is our recording session (prompt rules: `ai-generation-prompts.md`). The cue folder is
`content/audio/<cue-id>/` in the game (`card.json`, `takes/`, `recipe.json`, `out/`, `report/`; §7).
- Describe textures, not only the literal object: an ice slow can come from "dry palm leaves crunching", "foil crumpling slowly", "glass bottle tink". Write 2-3 texture descriptions per layer and spread the round's takes across them.
- **Takes per round, by the card's tier (J020-D9):** minor 3, frequent 4 (kept together as the variant set), important 6. An important sound's layers (tick, body, tail; the five jobs of §3) are generated separately, one prompt per layer, so each layer can be ranked and placed alone. `soundbench generate <cue>` (being built) asks ElevenLabs for the round, refuses round 4, stops before the credit budget, and decodes each take once to its master; the original take is never changed (G-1).
- One of the round's takes is an odd variant: reversed, an extreme pitch, an unrelated texture.
- For a new setting, material or natural effect, write what the real thing sounds like (its attack, its tail, how it changes with distance) before prompting, and use at least one observed property.
- **Rank against the card, never against a reference sound (CD-2).** `soundbench rank <cue>` (being built) measures every take and scores each target as inside, near or missed: (1) rejected outright: clipped at the source, near-silent, no sound in the band the card needs; (2) each target scored with its distance; (3) a miss a recipe step can fix counts less than one it cannot (a late start → `trim`; too long → `cut`; too quiet only when the gain fits inside the true-peak headroom; all energy below 120 Hz on a phone cue, or the wrong sound, cannot be fixed); (4) the order, the reasons and the fixing steps for the top take. Until `rank` is built, do the same by hand from `soundbench measure --json` on every master and write the table.
- **Regenerate, do not pile on edits.** When no take passes after its fixable steps, change the prompt (write which misses the change must fix) and generate a new round. At most 3 rounds per cue (J020-D7); after round 3 the cue goes to the owner with its rank and render numbers.
- Bracket a key number (pitch, tail length, gap, level) with a too-low and a too-high value in the recipe, render both and pick by the targets.
- A tone shift (an event, a darker skin): one version pushed to the extreme and one pulled back to the identity sheet's tone words, both rendered; the targets and the tone words pick, the other is kept in the library; the owner's play-test may swap them.
- Good unpicked takes go to the game library with their tags (J020-D9).
- Budget: numbers for every take; a picture (`--picture`) only when a number fails or is near its limit, and for important cues (light checks).

## 6. Design pass and edit pass (steps 7-8)

**Design pass: make the building blocks.** Written as the `design` list of `recipe.json`, rendered by
`soundbench render <cue-folder>` from the untouched take. Order (SC-09); a step out of this order needs a `why` or
`render` refuses it:

| # | Step | soundbench operations | Purpose (write it on the card) and rules |
| --- | --- | --- | --- |
| 1 | Clean | `dc`, `highpass`, `lowpass`; `denoise` (hiss; `nr_db`, and `nf_db`, which defaults to the take's measured tail floor); `declick` (sustained sounds and loops only: on a clean hit it cuts the attack); `dehum`; `gate` (tail floor; `threshold_db` below the take's own peak) | remove hiss, hum and rumble; fades and trimming come in the edit pass. `denoise` is refused when it would change the level, the length or the attack (attack share, rise, main transient) |
| 2 | Pitch | `varispeed` (`semitones`; pitch and length together: the default for percussive takes and layers); `pitch` (`semitones`, length kept, at most ±3 st), `stretch` (pitch kept, ratio 0.8-1.25): sustained layers only; `to_key` (nearest note of the game key, ±50 cents, S-127; refused on an untrusted F-10) | set size and register |
| 3 | EQ | `eq` (bell, low shelf, high shelf, notch); the low cut is a `highpass` | keep only the band this layer owns; cut before boost (SC-06): a boost over 6 dB needs a `why` |
| 4 | Compress | `compress` (`threshold_db` in dB below the take's own peak, `ratio`, `knee_db`, attack, release, make-up); `limit` (true-peak ceiling) | control peaks; hard compression lifts a shimmering tail when the tail is the point. On sfx and ui, limiting a transient needs a `why` |
| 5 | Add | `space` (the sound's own designed tail and glue, never a room: J020-D10), `echo`, `chorus` (movement, SC-10) | overtones, delays, the tail that glues the layers into one event |
| 6 | Compress again | `compress` | the added material changed the dynamics |
| 7 | Transient | `transient` (attack and sustain up or down) | boost or add the first ms of every hit |
| 8 | Air, saturation | `saturate` | a little brightness or harmonics for phone speakers (S-156); the log shows the phone loss before and after |

- Design-pass dynamics (`compress`, `saturate`, `gate`) are relative to the take's own peak, so a quiet take and a loud one are shaped the same; the edit pass sets the absolute level (`loudness`, `peak`). The limiter's ceiling stays absolute (a delivery limit).
- A little at each step; `soundbench compare` raw vs processed: the core's note and main band must still be there (R-51).
- Try the unprocessed take first (an empty design list); keep it when it meets the targets and write "unprocessed tried" on the card.
- Everything is baked into the file (J020-D1, CD-1): nothing is left for a Roblox effect. The only part fitted in Roblox is the room: files stay dry of room sound (their designed tail stays) and the card says whether the cue takes the zone reverb (SC-08, `roblox-audio.md` §H).
- **Layers** (`layers`, being built): an important sound's separately generated layers, each with its own design pass, mixed at offsets in ms with gains; `align` puts each layer's transient on its marker; per-layer targets.
- **Variants** (`variants`, being built): a frequent cue's variant set, one file per take of its round, or n files with small seeded pitch (`varispeed`) and level changes from one take. Refused for cards of kind tell, warning or countdown (SC-12: the same attack always has the same tell). Variants of one family (an upgrade tier, a mood variant) come from processing the base, so the family stays recognisable.
- Movement: magic, travel and loop layers carry slow modulation (prompt words "spinning", "swirling", "passing", or `chorus`); a one-shot whoosh gets a rise-then-fall pass-by envelope; a pitch bend only where the material suits it.
- **Loops** (`loop_bed`, `loop_music`, being built): beds and long loops spliced from several takes with crossfades, a short fade on every splice, no repeat inside the first loop (S-100); music loops bar-aligned from the BPM; the seam measured (F-08).
- A take that still misses after its recipe: change the prompt and regenerate (§5), never stack more steps on it.
- File the results as parts in the library (§7).

**Edit pass: make them work in the scene.** A separate pass with its own judgement, written as the `edit` list of
`recipe.json`. `render` runs it in this fixed order whatever the recipe lists: `trim` → `cut` → `fade` → `mono` →
`loudness` → `peak` → `export`.
- Cut each stage to its event in the capture or animatic, with the other sounds of the scene present.
- Drop any layer the moment does not need (the sweetener test, S-77).
- `trim` to the onset the card's kind binds to: hits, impacts, clicks and pickups to the main transient; rising sounds (tells, warnings, whooshes, risers, voices, sustained sounds) to F-01, never to the main transient. The log writes `lead_in_ms` (onset to main transient) so the integrator can start a rising sound early. A take that starts mid-waveform (most real takes do) gets a short fade from its first sample, so the file starts without an edge click (card target `edge_clicks`).
- `cut` through sound needs a fade-out; a `fade` that softens the attack needs a `why`.
- `loudness` uses the same function as the card's level measure (F-09 for one-shots, F-13 a for a family of siblings, integrated LUFS only for 0.4 s or more); `peak` sets the true-peak ceiling by gain only, with a margin for Roblox's transcode (P until the first upload is measured).
- `export` writes FLAC at the take's sample rate (G-8: Roblox transcodes every import; FLAC adds no third lossy codec and keeps loops sample-exact; Ogg only for a file over 20 MB), with a log of every step and its numbers before and after, so any output can be rebuilt from the original take.
- `render` exit codes: 0 pass (every must-target and the level); 1 a target failed (the file is still written; the report says why); 2 refused or bad input (a malformed card or recipe, a changed take, a step out of order without its `why`, a one-sided paid-reveal family); 3 family incomplete: "re-render after the siblings".
- **Paid-reveal families** (D-03): write every member's `card.json` (same family id, `paid_reveal: true`, the same member set) before the first render. A missing or one-sided card is refused (exit 2); a member not rendered yet gives exit 3, never a pass. Each render re-checks the whole family on the current delivered files (F-13 b within 1 LU, F-03 sample peaks within 1 dB) and writes `<family-id>.family.json` beside the cue folders.
- Set variants, jitter and cooldowns from the event rate (`repetition.md`).
- Place the cue in the mix (step 9, `mix-and-loudness.md`) and in Roblox (2D or 3D, falloff, room, ducks: `roblox-audio.md` §H).

## 7. The game's sound library and data

| Tier | Holds | Tags |
| --- | --- | --- |
| Raw | generated or recorded takes, untouched, with their sidecar (prompt, settings, model, date, credits, sha256); good unpicked takes are kept here (J020-D9) | texture, source prompt, date, rights |
| Parts | processed building blocks: tonal, mechanical, crunch, low body, tail, tick | job, band, pitch or key, length |
| Cues | finished cue files per stage and variant | cue id, stage, category, tier |

- Search the library before writing a prompt; the hand-back lists reused and new parts.
- One folder per cue, `content/audio/<cue-id>/`: `card.json` (the card's machine part, `cue-card.md` §D), `takes/<cue-id>.r<round>.t<n>.mp3` + `.json` + `.master.wav`, `recipe.json` (the take or takes and the two passes), `out/<cue-id>[-v<k>].flac` + `.log.json`, `report/` (numbers, a table, pictures).
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
| References | none: reference sounds are not used as targets (J020-D3, CD-2); picks are against each card's targets |
| Space types | each space type of the game (outside, small room, hall, cave, ...) with its zone `AudioReverb` settings (PROPOSAL until the owner's play-test), and which cue categories take the room (`roblox-audio.md` §H) |

## 9. Partners: what I ask for, and when

| When | Partner | I ask for | I give back |
| --- | --- | --- | --- |
| Step 1 | game designer | the feedback stack, threat sheet, read rank and tiers for this feature | the cue list per state change; a missing cue or reason |
| Step 1, gameplay features | architect | the presentation contract rows at their revision (event id, layer, source, viewers, cap owner) | before the contract freezes: my needs in the exchange note (the list is in the role file's partner table) |
| Step 2 | animator | the draft timing list (event ids, verb, sound words, end-of-state tells) | the stage sheet keyed to its ids; a missing event as a request |
| Step 2 | VFX designer | the frame script on the same ids | the shared envelope (wind-up, peak, tail) as an exchange note |
| Step 1, stages | environment designer | the ambience map (emotion per zone, signature element) and floor-material list | the `sound:` keys; footstep sets; refusal of a material I cannot cover in time, with the material to use instead |
| Step 1, rewards | progression designer | the reward tier table (tier, trigger, measured rate) | reward cues sized per tier; a tier whose rate is too high for its cue length, as a finding |
| Step 2, screens | UI designer | the screen's event names and the motion table | the UI cue list (cue id per motion-table row) |
| Step 3 | art director | the character card and tone words | the signature plan per character |
| Step 5 | integrator (feature-builder) | the temp cues wired on the event ids; a debug log `cue` line per play (`engineering-craft/references/presentation.md` §9) | the temp cue list and wiring notes |
| Step 9 | integrator (feature-builder) | 2D or 3D per cue as the cards say (the actor version and the others version), the emitters' falloff, the zone-reverb switch, the duck calls by fader volume | the cue-id table with the playback columns, the space-type table, the duck table (`roblox-audio.md` §H) |
| Step 9-11 | studio operator | the debug cue log from a play-test (each cue on its event); the read-only graph inspections (`roblox-audio.md` §G); a device capture with sound for sync | the cue list to check and what each line must show |
| Any time | owner | the owner's play-test flags, when given (never a listening session) | the fix, and a `lesson` with the owner's words |
| Any timing change | animator | the new revision in the same hand-back | re-keyed stage sheet, acknowledged |
