> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Revised by J020 step 8 sound-designer · claude-opus-5-5 · high · 2026-10-23: the approved sound workflow (J020-D1 to D14): soundbench, takes per round, regenerate rounds, the play-test instead of check-ins. Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021-D4, on 982592c): target-experience sentence sets the emotion. Revised by J020 step 8 follow-up sound-designer · claude-opus-5-5 · high · 2026-10-24: generate, rank, layers, loops and variants from the soundbench README at 5a1b5bb.

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
- **Takes per round, by the card's tier (J020-D9):** minor 3, frequent 4 (kept together as the variant set), important 6. An important sound's layers (tick, body, tail; the five jobs of §3) are generated separately, one prompt per layer, so each layer can be ranked and placed alone. `soundbench generate <cue-folder>` asks ElevenLabs for the round from `prompts.json`, refuses round 4, stops before the credit budget, and decodes each take once to its master; the original take is never changed (G-1). How to run it: the last bullets of this section.
- One of the round's takes is an odd variant: reversed, an extreme pitch, an unrelated texture.
- For a new setting, material or natural effect, write what the real thing sounds like (its attack, its tail, how it changes with distance) before prompting, and use at least one observed property.
- **Rank against the card, never against a reference sound (CD-2).** `soundbench rank <cue-folder>` measures every take and scores each target as inside, near or missed: (1) rejected outright: clipped at the source, near-silent, no sound in the band the card needs; (2) each target scored with its distance; (3) a miss a recipe step can fix counts less than one it cannot (a late start → `trim`; too long → `cut`; too quiet only when the gain fits inside the true-peak headroom; all energy below 120 Hz on a phone cue, or the wrong sound, cannot be fixed); (4) the order, the reasons and the fixing steps for the top take. How to read its report: the last bullets of this section. Takes `rank` does not read (layer takes, below) are ranked by hand the same way from `soundbench measure --json` on every master, and the table is written.
- **Regenerate, do not pile on edits.** When no take passes after its fixable steps, change the prompt (write which misses the change must fix) and generate a new round. At most 3 rounds per cue (J020-D7); after round 3 the cue goes to the owner with its rank and render numbers.
- Bracket a key number (pitch, tail length, gap, level) with a too-low and a too-high value in the recipe, render both and pick by the targets.
- A tone shift (an event, a darker skin): one version pushed to the extreme and one pulled back to the identity sheet's tone words, both rendered; the targets and the tone words pick, the other is kept in the library; the owner's play-test may swap them.
- Good unpicked takes go to the game library with their tags (J020-D9).
- Budget: numbers for every take; a picture (`--picture`) only when a number fails or is near its limit, and for important cues (light checks).
- **Order of work for one cue** (commands from the repo root; `python -m tools.audio.soundbench` written `sb`; the full flags: `tools/audio/soundbench/README.md`, "Commands"). Every command reads and checks `card.json` first: an unknown field or a typo is exit 2, never a dropped target.

| # | Do | Command | Exit codes |
| --- | --- | --- | --- |
| 1 | Write `card.json` (`cue-card.md` §D); for a paid-reveal family, every member's card, in sibling folders, before any render (§6) | — | — |
| 2 | Write `prompts.json` for this round (below) | — | — |
| 3 | Plan and price the round, no call, no key | `sb generate content/audio/<cue> --dry-run [--json]` | 0 plan written (its `predicted_credits`; the budget is not checked in a dry run: compare it yourself); 2 refused (bad card or prompts, round 4) |
| 4 | Generate the round | `python tools/keys.py run --only ELEVENLABS_API_KEY -- python -m tools.audio.soundbench generate content/audio/<cue> --budget <credits> [--json]` | 0 every planned take made and decoded; 1 stopped by the budget, or a take rejected (moved to `takes/rejected/`; its credits stay counted); 2 refused before any call (also round 4, J020-D7, and a round predicted over the budget), or a call failed (auth, validation, every format refused, retries used up) |
| 5 | Rank the round | `sb rank content/audio/<cue> [--round K] [--picture] [--json]` | 0 verdict `use`; 1 `regenerate` (rounds 1-2) or `owner` (round 3); 2 refused (bad input, a changed take, an inconsistent family, rank and its proof render disagree) |
| 6 | Write `recipe.json` from rank's fix steps: one source (`take`, `layers` or `takes`), the `design` and `edit` lists, and `loop` or `variants` when the card's form asks (§6) | — | — |
| 7 | Render and judge the delivered files | `sb render content/audio/<cue> [--picture] [--json]` | 0 every must row passed; 1 a must row, the level or the family check failed (files still written); 2 refused; 3 paid-reveal family incomplete: re-render after the siblings |
| 8 | Wire, play-test, prove on the event | debug cue log (R-50, R-41); feel is the owner's play-test | — |

- **`prompts.json`** (schema: `tools/audio/soundbench/generate.py` docstring), written for each round: `cue`, `prompts` (2-3 texture descriptions; the round's takes are spread over them in turn), `duration_s` (0.5-30; **always set it**: without it the service picks the length and charges 55 credits flat; `ai-generation-prompts.md` vendor facts), `prompt_influence` (0-1; service default 0.3), `loop`, `model` (`eleven_text_to_sound_v2` default, or `eleven_text_to_sound_v3`), `takes` (another count than the tier's is a warning), `note` (what this round changed and which misses it must fix; copied into every sidecar). An important cue gives `layers` instead of `prompts`: `[{"name": "body", "prompts": [...], <any optional field>}, ...]`; each layer is generated separately as `takes/<cue>.<layer>.r<k>.t<n>` (J020-D9). The 3-round limit is per cue (J020-D7), layers included: read the round a run will use in `--dry-run`'s `sounds[].round` before you spend.
- **`generate` facts to plan by** (README "Generating takes"): the next round is the highest round present (kept or in `takes/rejected/`) + 1, and round 4 is refused before any call (the tool is being changed to count rounds over the cue and all its layers together, J020 review F5: trust the `--dry-run` plan over this line); a round whose calls all failed made no take and is not used up. Cost is predicted per call as ceil(11 × `duration_s`) credits; `--budget` (default 300 credits, PROPOSAL) refuses a round predicted over it and stops before any call or retry that could pass it. Format: WAV 44.1 kHz first, MP3 192 then 128 kbps only when a response refuses the format; the received bytes decide the file type. Every take gets a sidecar (`request`, `credits`, `credits_predicted`, `requested_ms`, `format_used`, `status: not auditioned`, then `intake`) and the run writes `report/<cue>.generate.<UTC time>.json`; copy the credits spent into the card's sources field. The key comes only from the environment through `tools/keys.py` (never open the key file); a key already set in the Windows environment wins over the file in `keys.json`, and an auth error says so.
- **Reading `rank`'s report** (`report/<cue>.r<k>.rank.md` and `.json`; rank writes nothing else and never touches `out/` or family state):

| Part | What it says | How to use it |
| --- | --- | --- |
| Rejected | clipped at the source (10 ms or more at or above -1 dBFS inside any 300 ms window), near-silent (sample peak under -60 dBFS), no sound in a `must` band (share under a tenth of its minimum) | no fix is claimed for these; they rank last. A clean result is not proof of no clipping (`review.md` §4, soundbench limits) |
| Each target | `inside`, `near` (inside, within the `tables.json` margin of a limit: still a pass) or `miss`, with `margin` or `miss_by` | a `near` reading gets a picture before any note (`review.md` §4) |
| Three plans | the edit-pass fix for every miss, for the must misses only, and no step; the kept plan has the fewest must misses after it, then the fewest aim misses, then all > must > none | an aim fix that would break a must (the level reset after a trim) is left out and listed; a plan an operation refused is recorded with its reason |
| Fixed, introduced | a miss counts as fixed only when its re-measured row passes; `introduced` = a row the fix itself broke | anything no edit step moves (bands, phone loss, flatness, attack, key, too short or early) is a **prompt miss**: rank computes no design steps, so an `eq` or `limit` you could try reads as a prompt miss (`render` measures your try) |
| Level and peak ceiling | `gain_needed`, `peak_limit` = min(-1.0, card true-peak max, card sample-peak max) - 0.5, `headroom`, `peak_cut`, `predicted`; fits when within the level's tolerance | `peak` is gain only: a quiet take fits only when its gain fits under the ceiling; a take too loud always fits. Derived and simulated level agree within 0.1 dB, or rank refuses |
| Order key (`rank_key`) | rejected last; passes after its fix first; then fewest must misses after the fix, fewest aim misses, fewest misses that needed a fix, fewest near readings, take number | a must miss never ranks above a pass; recompute it from the table when two takes look close |
| Proof | the top take's fix recipe rendered for real on a temp copy; every row must match the simulation | a mismatch is exit 2: report it to the lead as a tool fault, never pick by hand around it |
| Verdict | `use` (top take and its edit steps: the start of `recipe.json`), `regenerate` (rounds 1-2: the targets still missed, how many takes miss each, the closest value and its direction: write them into the next round's `note` and prompt), `owner` (round 3: the cue goes to the owner with the rank and render tables, J020-D7) | takes per round off the tier's count are a warning. On a loop or variant card, `use` adds "form rows (loop, variants) are judged at render": rank judges such takes as one-shots; only `render` reads the seam and the set spread |

- **Layer takes are not ranked by `rank`**: it reads only `takes/<cue>.r<k>.t<n>`, and a layer's takes are named `<cue>.<layer>.r<k>.t<n>`. Rank each layer's round by hand from `sb measure <master> --json` against that layer's own targets (the same inside / near / miss table), then let `render` judge the mix and the `layer[<name>].*` rows. (Open: a layer-aware `rank` is a tool follow-up for the lead.)

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
- **Layers** (recipe source `layers`, at most 8, PROPOSAL): an important sound's separately generated layers. Each layer entry: `name`, `take`, its own `design` list (its own design pass, in the SC-09 order), `offset_ms` (0 or more; negative refused) **or** `align` (`{"to_ms": <marker>, "on": "main_transient" | "F-01"}`), `gain_db` (-48 to +12), `fade_in_ms` / `fade_out_ms` for splices, and `targets`. The recipe's top-level `design` then runs on the mix, then the edit pass. Rules the render keeps (README "Layers, loops and variants"):
  - `align` puts the layer's main transient (or F-01 for a rising layer) on the marker sample: one reading on the layer alone, one correction on the layer as placed (`align_correction_samples`); more than one sample off after it is flagged `align_unstable`. DC is removed **for the reading only** (`reading_dc` in the log), never from the delivered audio; add a `dc` design step to a layer only when its own numbers ask for it.
  - Each layer's two ends get trim's hot-edge fade automatically: 0.5 ms when the edge sample is over peak - 60 dB, logged per layer as `edge_fade` with the attack share before and after and `edge_fade_attack_loss`. The fade can move the align reading up to 1.6 ms (the delivered audio is what is aligned); a big `edge_fade_attack_loss` on a hit layer is a reason to regenerate that layer, not to lengthen the fade.
  - A layer at another sample rate is resampled to the first layer's rate (a `resample` step in the log). The log gives per layer the offset, F-01, main transient and F-09 as placed, `share_energy`, `share_of_mix` and the mix's `interference_db` (negative = the layers cancel: try another offset; still negative, regenerate the layer), and the mix `headroom`: a mix past full scale with no `loudness` or `peak` after it is refused before the edit pass.
  - **Per-layer targets:** an important cue's every layer needs its own `targets` (render refuses otherwise); they are judged on the layer as placed, alone, as rows `layer[<name>].<target>`. The row `layer[<name>].edge_clicks` (clicks within 1 ms of the layer's edges, max 0) is a **must for important cues and an aim for the others**.
- **Variants** (`card.form.variants` = n; files `out/<cue>-v<k>.flac`): a frequent cue's variant set, from one of two sources, and judged file by file against every card row (named `<cue>-v<k>:<target>`):
  - `takes`: one file per take of the round (the frequent round of 4, J020-D9) through the same recipe; the count must equal the card's.
  - `variants` block (`seed`, `count`, `max_cents`, `max_db`): n files from one sound, each `varispeed` by a seeded stratified draw in ±`max_cents` (at most the kind's `variant_max_cents`: hits, whooshes, beds 100; pickups, chimes, stingers, voice, music loops 30; 30 when the card has a key) and a level offset in ±`max_db` (at most 1 dB). The same seed gives the same files (G-1); write the seed on the card.
  - Set rows: `form.variants` (file count equals the card's) and `variants.level_spread` (each file's F-09 within ±1 dB of the set's mean: R-31). The pitch is varied in the files, so no runtime `PlaybackSpeed` jitter on top (S-92).
  - Refused (exit 2) for kinds tell, warning and countdown (SC-12: the same attack always has the same tell), on a loop, and when the count differs from the card's. Every variant file of a paid-reveal member is in its D-03 family check (a member with a variant missing is incomplete, exit 3).
  - Variants of one family (an upgrade tier, a mood variant) come from processing the base, so the family stays recognisable.
- Movement: magic, travel and loop layers carry slow modulation (prompt words "spinning", "swirling", "passing", or `chorus`); a one-shot whoosh gets a rise-then-fall pass-by envelope; a pitch bend only where the material suits it.
- **Loops** (recipe `loop` block; the card needs `form.loop: true`): beds and long loops spliced from several takes with crossfades (as `layers` with `fade_in_ms` / `fade_out_ms`), a short fade on every splice, no repeat inside the first loop (S-100); music loops bar-aligned from the BPM; the seam measured (F-08).
  - `loop_bed`: `crossfade_ms`, `start_ms` (default: the crossfade), `end_ms` (default: the end), `search_ms` (moves the end to the best-matching point), `curve` (auto: equal power, or equal gain when the two parts correlate at 0.414 or more). `loop_music`: the downbeat `start_ms`, `bpm`, `bars`, `beats_per_bar` (4), `crossfade_ms` (20), `curve`; the length is the bar length rounded to a whole sample, the drift logged per loop and per 10 minutes.
  - The file's last sample and first sample are neighbours in the source, kept within one 24-bit step in the FLAC. The edit pass after a loop is gain only: `trim`, `cut` and `fade` are refused; also refused: a crossfade over half the loop, a start under the crossfade, an end past the sound, variants of a loop.
  - **Must rows on every `form.loop` card** (with or without a loop step, so a pre-looped take is judged too): `form.loop_f08` (F-08 at most R-26's 2), `form.loop_wrap_clicks` (no click within 1 ms of the wrap), `form.loop_wrap_hf` (the wrap's 2 ms high-frequency energy at most 3 dB over the loop's own 99th percentile), `form.loop_seam_gap` (the seam's quietest 50 ms at most 6 dB under the loop's own 5th percentile); with a loop step also `form.loop_crossfade_level` (within 2 dB of the band between its two parts' levels), and for `loop_music` `form.loop_length_samples`.
  - A card's `loop_seam` max **only tightens** R-26's limit of 2. Loosening it needs `"must": true` and a non-empty `why` on the target (logged in `limit_from`); an aim `loop_seam` never lifts it. A looser limit is a choice to name in the hand-back.
  - Known limits (a green loop is not proof): a seam jump in the quiet part of a bed with a loud section is not caught (F-08 and `wrap_hf` read the seam against the whole loop; only the click floor at 1 % of peak remains); a spike inside low-passed noise, a gap in a bed that already has near-silent lulls and a slope break with no jump are not read; how Roblox's transcode treats the loop point is not measured yet. For a bed with loud and quiet parts, look at the wrap on a picture (`render --picture`) and list the cue for the owner's play-test.
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
- `render` runs in this order: source(s) → each layer's own design pass → mix → the recipe's `design` → loop → each variant → the edit pass → export. Its report (`report/<cue>.render.md` and `.json`) holds the card's rows in `targets` and the layer, loop and variant rows in `form_checks`; every must row of either goes into `must_failed` and the exit code.
- `render` exit codes: 0 pass (every must-target and the level); 1 a target failed (the file is still written; the report says why); 2 refused or bad input (a malformed card or recipe, a changed take, a step out of order without its `why`, a one-sided paid-reveal family); 3 family incomplete: "re-render after the siblings".
- **Paid-reveal families** (D-03): every member's cue folder sits **side by side** in one parent folder (`content/audio/<cue-a>/`, `content/audio/<cue-b>/`, ...): the family check finds members by scanning the sibling folders of the cue being rendered, so a member elsewhere is "no card.json" (exit 2). Write every member's `card.json` (same family id, `paid_reveal: true`, the same member set) before the first render of any member. A missing or one-sided card is refused (exit 2); a member not rendered yet gives exit 3, never a pass. Each render re-checks the whole family on the current delivered files (F-13 b within 1 LU, F-03 sample peaks within 1 dB) and writes `<family-id>.family.json` beside the cue folders.
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
