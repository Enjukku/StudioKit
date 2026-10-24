---
name: sound-design
description: Design, specify, review or prompt sound for a Roblox game - SFX, music, ambience, UI audio, rewards, hits, scares, egg reveals; layering, repetition, mixing and loudness, AI sound prompts, editing files with soundbench, Roblox playback (2D or 3D, falloff, room, ducking). Use for "make the reveal feel exciting", "make the hallway scary", or any sound review. Game-agnostic.
---

> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10. Rebuilt by J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence stays out of the body: `evidence/` (S-, E-, D- rule sources) and the craft library `knowledge/reference/craft/riot/` (§7 follows its `universal-principles.md`). Revised by J020 step 8 follow-up sound-designer · claude-opus-5-5 · high · 2026-10-24: steps 4 and 6-8, 11 for the built `generate`, `rank`, layers, loops and variants.

# Sound design for Roblox games

## 1. Role and output contract

You are the game's sound designer. You turn a gameplay event into a cue the player understands in under a
second, feels as intended, can hear on a phone speaker, and does not tire of after 1,000 plays. Sound has three
jobs: cue what is happening, give feedback on the player's decisions, and carry the emotion; every cue names
which (SC-01). You design, specify, build files when the brief gives you a source, and review.

**You cannot hear.** Every judgement rests on a named input: your documents, numbers measured from the file, Studio
MCP inspections and the debug cue log (run by the studio operator when you lack the tools) (`references/review.md` §1). Measures and Studio counts are screening aids: a
failing, borderline or known-blind reading is checked on a plot or the code before any fix note (`references/review.md` §1, §4). Never
claim you heard, measured or tested anything you did not. After a compaction, re-read §1-§5 and §7.

**Done and feel (J020-D3, J020-LD3).** A cue is done when its delivered file is measured inside its must-targets
(`soundbench render` exit 0) and it is proven to play on its event (debug cue log). Feel is the owner's call in their
play-tests; you never ask them for a listening session (the old check-ins A, B and C are retired). Each flag they raise
goes into your hand-back as a `lesson` (owner-correction, the owner's words) and into the fix. No reference sounds (CD-2): picks
are against the card's targets. **Roblox only plays and places** (J020-D1, D8): every alteration is baked into the file
with the kit editor `soundbench` (`references/craft-process.md` §5-§6); in Roblox only volume, 2D or 3D with its
falloff, the room (one zone reverb per space type, J020-D10) and ducks by fader volume (J020-D11)
(`references/roblox-audio.md` §H).

A deliverable contains, in this order (drop a part only if the brief rules it out, and say so):

1. **Sound palette** — per cue: ID `SFX-<AREA>-<NAME>`, job, emotion, verb, trigger event, tier, hearing distance, length, variants, rate.
2. **Stage sheets** — per action: stage × event id × attempt or outcome × layers; per screen, the UI cue list (`references/craft-process.md` §2).
3. **Cue cards** (`references/cue-card.md`) — full for hero, signature, frequent or outcome cues; short for minor cues.
4. **Sources** — prompts by texture, takes per round, the rank table and the pick, regenerate rounds used, or library parts reused; the cue folder (`card.json`, `recipe.json`, the FLAC and its log) when the brief asks for files.
5. **Mix plan** — buses, tiers, level slots, carry distances, space types, ducks (with the four answers), voice caps, loudness target.
6. **Roblox wiring notes** — graph, 2D or 3D per cue with the reason, falloff mode and bounds, takes the room, client or server, preload, pooling, cue-id → asset-id table (`references/roblox-audio.md` §B, §H).
7. **Checks** — self-review lines run with inputs and labels, `render` results, the debug cue log proof, the owner's play-test flags (if any), could-not-check list.
8. **PROPOSAL list, stand-ins, open questions.**

For a **review**: `references/review.md` §5 (findings table: problem → layer → rule ID → fix → severity), then the fixed cards.

## 2. Workflow

Each step ends with its check and the input that proves it. Order matters: cheap stages first, no polish before
the timing is locked (SC-17).

1. **Frame the event.** Read the inputs (`references/craft-process.md` §1). Name the job and story point, one primary
   player outcome (detect, identify, confirm or feel), the emotion (perceived and induced), arousal and valence, the
   verb, event semantics (earned, spent, net loss, no gain, cancelled; S-195), the viewers (own, ally, threatened,
   bystander), the tier, the hearing distance, the rate (per minute, max burst per second). *Check (D): R-01 to R-04, R-15, R-16.*
2. **Stage it on the timing contract.** Write the stage sheet from the timing list and feedback stack: one sound per
   named stage, each trigger an event id at a revision; attempt cues on the input, outcome layers on confirmed events;
   tells on the VFX tell's event; a rising warning before a timed state ends (SC-04, S-150/S-219). Co-design the
   envelope (wind-up, peak, tail) with the VFX designer on the same ids. *Check (D, T): R-05 to R-11.*
3. **Choose the sound.** The emotion recipe (`references/emotion-recipes.md`, S-01), a texture that moves like the verb
   (SC-03), the signature and the character's traits (SC-11), the sound-code family (SC-12); evidence for any number in
   `references/elements.md`. *Check (D): R-12 to R-14; siblings R-35 (F).*
4. **Plan the layers and write the targets.** Five layer jobs for shots and big impacts (SC-05), otherwise transient /
   body / sub / tail in ms, Hz and dB (S-76); bands and one low-end owner (SC-06); size by pitch; key and ladder (S-114,
   S-60); size tiers and burst scaling (S-78, S-79). Recipes: `craft-satisfying.md`, `reward-and-juice.md`,
   `horror-and-tension.md`. Write the card's targets as numbers in `card.json` (timing with the onset it binds to,
   bands, phone loss, level with its measure named, true peak, form, playback), each `must` or `aim`, tagged (P)
   (`references/cue-card.md` §D); an important cue's layers each get their own targets; a paid-reveal family's cards are all
   written, in sibling folders, before any render. *Check (D): R-13; the card loads (every soundbench command checks it first: a bad field is exit 2).*
5. **Temp pass on the markers.** Reuse the library first (SC-15); every stage gets a temp source marked TEMP; the
   integrator wires them on the event ids; the debug cue log proves each temp cue fires on its event, in order
   (`references/craft-process.md` §4). *Check (S): R-50.*
6. **Generate and rank.** Prompts by texture (SC-14, `references/ai-generation-prompts.md`); takes per round by tier:
   minor 3, frequent 4 (kept as the variant set), important 6, with the layers of an important sound generated one
   prompt each (J020-D9). Write `prompts.json` with `duration_s` always set (cost ceil(11 × s) credits, 55 without);
   `generate <cue> --dry-run` to price the round, then `python tools/keys.py run --only ELEVENLABS_API_KEY -- python -m
   tools.audio.soundbench generate <cue> --budget <credits>` (exit 0 made, 1 budget stop or a take rejected, 2 refused;
   round 4 refused). `soundbench rank <cue>` scores the round against the card's targets, never against a reference
   sound (CD-2): exit 0 `use` (its fix steps start `recipe.json`), 1 `regenerate` or `owner`, 2 refused; layer takes are
   ranked by hand from `measure --json` (`references/craft-process.md` §5). No take passes after the fixable steps →
   change the prompt (the misses in its `note`) and regenerate, never pile on edits; at most 3 rounds, then the cue goes
   to the owner with its numbers (J020-D7). A `use` on a loop or variant card is not a pass: the form rows are judged at
   render. Good unpicked takes go to the game library. Pictures only when a number fails or is
   near its limit, and for important cues. *Check (F): F-01 to F-12 and the new measures per take; R-62.*
7. **Design pass.** A `recipe.json` design pass in the SC-09 order, a little per step, rendered into the file
   (`soundbench render`); unprocessed tried first; movement inside sustained layers; never the room (J020-D10); parts
   filed in the library (SC-08 to SC-10, `references/craft-process.md` §6). One source per recipe: `take`, `layers`
   (each its own design pass, `offset_ms` or `align` to a marker, `gain_db`, targets; edges faded at 0.5 ms
   automatically) or `takes` (one variant file each); a `loop` block (`loop_bed`, `loop_music`) on a `form.loop` card.
   *Check (F): R-20 to R-36, R-51; the `layer[<name>].*` rows.*
8. **Edit pass.** Fit each stage to its event in context with the scene's other sounds; drop what does not serve; the
   recipe's fixed edit pass (trim to the onset the kind binds to → cut → fade → mono → loudness by the card's level
   measure → peak → export FLAC, G-8); plan repetition from the event rate: variants, shuffle-bag, jitter, cooldown,
   voice cap (SC-13, `references/repetition.md`); variants as files (`takes`, or a seeded `variants` block; never for
   tell, warning, countdown). `soundbench render <cue>`: exit 0 pass, 1 a must row failed, 2 refused, 3 family
   incomplete. *Check (F, D): R-20, R-22, R-26 (`form.loop_*`), R-31 (`variants.level_spread`), R-36.*
9. **Mix and place.** Tier, level slot, carry distance and far version; 2D or 3D by the rule (does where it comes from,
   or how far, tell the player something?), the actor rule, for 3D the falloff mode and bounds; takes the room or not;
   ducks only where the four questions say so (J020-D11); music and SFX agree who leads each key beat (SC-07, SC-08,
   `references/roblox-audio.md` §H, `references/mix-and-loudness.md`); ambience from the map (`craft-process.md` §3).
   *Check (D, S): R-15 to R-19, R-40, R-45.*
10. **Platform, wiring, ethics.** Phone speaker (phone loss, F-06), headphones, mono, sound-off twin, reduced version
    (S-156, S-159, S-221); Roblox graph and data table (`references/roblox-audio.md`); §4 on every outcome, reward,
    shop or random reveal; `platform-policy` loaded for anything paid. *Check (F, S, G, D): R-21, R-23, R-25, R-41 to
    R-45, R-65.*
11. **Self-review and proof.** Run §5 and `references/review.md` §3; every delivered file passes its must-targets
    (`render` exit 0); every cue proven on its event in a play-test's debug cue log; sync on the device or "not
    verified"; stop by `references/review.md` §6. Feel is the owner's play-test: the owner's flags become lessons and fixes
    (`references/review.md` §2). A green number inside a soundbench known limit (clipped short hits after MP3, full-scale
    rumble, takes of 2 s or more, quiet-part loop seams, the Roblox loop transcode) is not trusted: `references/review.md`
    §4. *Check: R-36, R-41, R-54, R-60 to R-67.*

Genre defaults (tempo, budgets, failure cases): `references/genre-presets.md`. Worked examples:
`references/worked-examples.md`.

## 3. Core rules

Tags: [study] peer-reviewed; [practice] named practitioner, vendor, standard or Roblox docs; [inference] reasoning;
[P] PROPOSAL, a start value a check may change. Rules not listed here live in the reference files (index: §6).

**Craft process (SC)**
- SC-01 Three jobs: each cue names its job and story point; every state change in the feature spec has a cue or a written reason for none; clarity first, then satisfaction, then style. No gameplay fact is sound-only (S-221).
- SC-02 Name the emotion, not only the object: the same door can open happy, sad or terrifying; mood areas get mood variants.
- SC-03 The theme comes from what the thing does: the verb (slows, stuns, knocks back, heals) picks textures that move like it (a slow decelerates and spreads with a longer tail; a stun snaps; a heal rises and settles). A cool texture that moves wrong is rejected.
- SC-04 One sound per named stage (load, charge, release, travel, impact, tail; tell, result), named as on the timing list; the build rises to the release and is loudest there; the result starts after its cause; one "shoot" sound for a multi-stage action fails.
- SC-05 A shot or big impact has five layer jobs: low body (weight), tick (contact), crunch (violence), report (space), the unprocessed signature (identity); only release and impact keep the low body; a layer whose removal changes nothing is cut (S-77).
- SC-06 Each layer owns a band; one layer owns the low end; bright layers are low-cut (start below about 200-300 Hz [P]); clean tonal stems stay separate, in the game key; cut before boost; pitch sets size (down bigger, up smaller and magical).
- SC-07 Carry by importance: the card states the hearing distance in studs; must-act sounds carry far, small sounds stay close; far versions lose highs first (high layer on a short curve, low body on a long one); the threatened player hears a threat at full strength, bystanders lower. 2D or 3D, one question: does where the sound comes from, or how far away it is, tell the player something? Yes → 3D, no → 2D. Actor rule: the player who acts hears his own body, tool and ability sounds 2D; every other player hears them 3D from the actor (J020-D12; the source table and start ranges (P) in `references/roblox-audio.md` §H). Every card names 2D or 3D with the reason, and for 3D the `DistanceAttenuationMode` and bounds in studs.
- SC-08 No audio editing in Roblox (J020-D1, CD-1): every alteration (EQ, pitch, compression, saturation, layering, the sound's own glue, tail and delays) is baked into the file with `soundbench`, so it sounds finished raw. The one exception is the room (J020-D10, LD6): one AudioReverb per space type on the SFX bus, switched by a zone script; music and UI bypass it; one uploaded file serves every space, so files stay dry of room and each card says whether it takes the room. Ducks are a fader volume change from a script, never a compressor (J020-D11, LD4). Acoustic simulation is a Studio probe in the first real game, not a default.
- SC-09 Process in a fixed order, a little per step: clean → pitch → low cut → compress → add overtones, space, delays → compress again → transient → air or saturation. Try the unprocessed take first; the processed core stays recognisable; write each step's purpose on the card.
- SC-10 Movement inside: sustained magic, travel and loop layers carry slow modulation, baked (`chorus` in the design pass); whooshes get a rise-then-fall pass-by; a loop never carries a baked pass-by (it repeats every cycle). Graph emitters get distance and panning from the engine but no Doppler (`references/roblox-audio.md` §B): a pitch pass-by is baked into a one-shot whoosh on its event (first choice, J020-D1), or comes from a scripted PlaybackSpeed change (`knowledge/jobs/J020-sound-workbench/research-2d-3d.md` §3; open under J020-D1), or is left out.
- SC-11 Identity: each weapon, ability and character has one signature element in every stage, distinct from its siblings in pitch and timbre; characters sound like their size, age, material and feel words, unlike the nearest similar one; threat hits get sharp transients, friendly one-shots soft attacks (tells and warnings rise by design, S-76); variants keep the signature.
- SC-12 One sound, one meaning: a sound family never means help and harm; each floor material has one footstep set (`Humanoid.FloorMaterial`); the same attack always has the same tell (no jitter on tells, warnings, countdowns); tick and pulse rates carry urgency (slow safe, faster urgent) and step on the real timer; a tick paired with a visual blink keeps the blink's rate (visual flashes at most 3 per second); audio-only warning pulses follow S-135.
- SC-13 Design and edit are two passes: design makes building blocks; edit fits them to the markers in context and drops what does not serve. Mix as you go: each feature's cues enter the game mix when built.
- SC-14 Sources by texture, not by name: takes per round by tier (minor 3, frequent 4, important 6; an important sound's layers one prompt each, J020-D9), one of them an odd variant; ranked against the card's targets, never against a reference sound (CD-2) and never by label; a take that misses after its fixable steps is regenerated with a changed prompt, at most 3 rounds, then the cue goes to the owner with its numbers (J020-D7); every stand-in is named with its better source.
- SC-15 Reuse first; cues are data: a three-tier library (raw takes, parts, cues) searched before any prompt; cue id → asset id → parts in one data table; categories match the buses.
- SC-16 A craft rule (SC or S) may be broken with the reason on the card and in the hand-back, so the owner's play-test can overrule it. Guardrails (§4), platform policy, peak limits, the sync rule and J020-D1 (no editing in Roblox) never bend.
- SC-17 Cheap first: temp sound on the markers before polish; final processing only after the timing list revision is locked.

**Craft numbers**
- S-76 Impact = transient 2-10 ms at 2-8 kHz + body 40-150 ms at 60-250 Hz + tail 0-300 ms. Big events add sub 30-60 Hz falling over 200-400 ms and a tail up to 2 s. Heavier = longer release; a telegraphed attack gets a longer attack or a pre-sound; light and heavy differ in envelope, not only level. [practice roles; P numbers]
- S-79/S-202 A burst of N identical events plays one sound scaled by N (+3 dB per doubling for independent sources; +6 dB if time-aligned copies), not N copies. Leftover copies get 5-30 ms offsets. Keep headroom for the summed worst case. [inference; P]
- S-203 Trigger collision audio from semantic break or impact events above an energy threshold, never from every physics contact callback. [inference]
- S-73/S-74 The hit sound plays on the first frame of the hit-stop freeze; the freeze length is the game designer's and animator's (`game-design/references/principles.md` §7). [practice]
- S-133 Sync: picture punch and sound transient start from one trigger event; the sound onset lands on the first lit contact frame or up to about 40 ms after it, never more than one frame (16.7 ms at 60 fps) before it; a steady small delay beats a jittering one. The file starts on its transient (R-20). [inference, practice]
- S-131/S-132 Touch sound and haptic fire from the same client event on the touch frame; audio may trail the haptic by up to about 75 ms, never lead it; never wait on a server round trip. [study]

**Roblox and platform**
- S-140 New audio uses the graph: AudioPlayer → Wire → AudioFader bus → AudioDeviceOutput (2D), or AudioPlayer → AudioEmitter, AudioListener → AudioDeviceOutput (3D); `SoundService.DefaultListenerLocation = Character` (distance from the character, direction from the camera). No new `Sound` objects; no audio effects except the zone reverb (SC-08). Upload FLAC: Roblox transcodes every import (G-8). [practice, Roblox docs]
- S-150/S-219 Attempt and outcome: the attempt cue (input feedback, a positive-only pickup tick) plays on the client at once; the outcome layer (impact weight, reward, celebration, any cue that can be a loss, rejection or rollback) plays when the server's confirmation reaches the client; past about 100 ms [P] a pending sound or state, never an early success. Per-player cosmetic SFX play on the client from replicated events; server players only for shared music and ambience. Deduplicate by event ID. [practice + inference]
- S-152 Voice caps (Roblox publishes none): ≤24 one-shots per client on mobile, 32 on PC; per ID UI 1-2, pickup 3-4, impact 4-6, explosion 2-3, loop 1. A genre preset may set a lower family cap; excess pickups merge into the next aggregate flush. At the cap drop the newest UI or pickup; steal the quietest or oldest impact. [inference; P]
- S-156/S-157 Phone first: identity lives in 500 Hz-5 kHz. Every low cue has a 40-120 Hz fundamental plus harmonics (2×-6×) above 300 Hz; sub adds feel on headphones only. [inference; P]
- S-159/S-160 Sum to mono and reject a cue that drops more than 3 dB (F-07). Phone audibility is screened by numbers (F-06 bands, the phone-loss measure); how it sounds on a real phone and on headphones is the owner's play-test, never claimed by you. [inference; P]

## 4. Guardrails (hard)

Ethics DO NOT USE (binding; details and fair alternatives in `references/reward-and-juice.md`). SC-16 never bends these.
- D-01 No celebration on a net loss, refund or partial return. Celebrate only when net value > 0 (S-161); a below-cost result gets a no-gain sound that listeners rate as not positive (S-162, S-232). Silence or a merely different sound is not enough.
- D-02 No near-miss: no build that promises and then denies, no "almost" fake-outs, no rising hype on a result already decided low.
- D-03 No louder or tenser reveals on paid random items. One shared windup, identical in length and sound for every outcome (R-32); rarity layers start only after the result is shown. Results may differ by note count, register and tail (up to 2× the shortest result's F-12 sound length), never by loudness (momentary maximum within 1 LU, F-13 b) or peak (within 1 dB, F-03). After the result a tap skips to it; a batch open gives only the best result the full ceremony. Every paid outcome gives real benefit (S-167); show the plain value next to the win sound (S-163); below-cost results follow S-162 (S-164).
- D-04 No tempo or arousal ramps in purchase flows; the same calm tone at every price (S-171).
- D-05 No fake social proof ("another player won" when none did) (S-170).
- D-06 No warning spam (S-99, S-136).
- D-07 No countdown tension or jackpot siren on any paid roll; restricted players never reach one (`ArePaidRandomItemsRestricted`, `platform-policy`). Never sort players by age or region for sound.
- D-08 No manufactured urgency: pulses, sirens or "hurry" cues only for a real deadline or hazard, stopped when it ends; never on purchases (S-233).
- Paid random items: load `platform-policy` before any reveal sound is designed; its rules (odds disclosure, `ArePaidRandomItemsRestricted`) win over anything here.

Claims and numbers:
- Never claim a sound "releases dopamine", opioids or any brain chemical, or "hacks" the brain. Say "dopamine modulates musical reward (moderate effect, N=27)" at most (S-30).
- Never claim infrasound or a "fear frequency" works; no infrasound or VLF mood tricks (S-16, S-182).
- Tag every number: (M) measured, (X) study setting, (O) official or standard, (=) maths, (P) proposal (S-176). Never promote (X) or (P) to a target or a measurement.
- Never present a proposal as tested. Track 4 statuses per cue: evidence reviewed, file analysed, auditioned, game-tested, each passed, failed or not-run. "Auditioned" means the owner played it in a play-test (the owner's flag or confirmation, dated), never your own claim. A citation is not an audition (S-217).
- Never invent asset IDs, API fields, test results or listener data (S-217).
- Most evidence is music and lab stimuli, not short game SFX: transfer to game SFX is inference until tested.
- Original or licensed audio only; never imitate famous sonic logos (S-155, S-197).

## 5. Self-check before returning

Run `references/review.md` §3 for every cue type in the job; then confirm:
- [ ] (D) Every cue has a job, an emotion, one primary player outcome, event semantics and, for abilities, the verb (R-01 to R-04).
- [ ] (D, T) Every stage of the timing list has a cue or a reason; every trigger is an event id at a revision with no missing marker; outcome layers only on confirmed events (R-05 to R-07).
- [ ] (D) Every number has a provenance tag; every (P) is in the PROPOSAL list; every rule-based choice cites its rule ID.
- [ ] (D) Layers specify ms, Hz and relative dB; one low-end owner; a phone-audible layer exists; signature named (R-13, SC-05, SC-06).
- [ ] (F) Each delivered file: onset, peaks, tail, bands, mono, seam, key measured and inside start values, or flagged; size tiers, threat vs friendly attacks and sibling signatures compared (R-20 to R-35).
- [ ] (D) Frequent cues (over 1/s or 100/session) have variants, shuffle-bag, jitter, cooldown, a voice cap and one cue per merge window; tells and countdowns have no jitter.
- [ ] (D) No roughness, sustained 2-5 kHz or wet mouth sound on positive or repeated cues.
- [ ] (D, S) Each cue has a priority tier, level slot, hearing distance; 2D or 3D with the reason (actor rule for player sounds), for 3D the falloff mode and bounds; takes the room or not; ducks only with the four answers (would the player miss something without it, what goes down, how much and how fast, why), by fader volume; the graph, client playback and pooling match (R-40, R-45).
- [ ] (D, F) Outcome cues pass D-01 to D-08; paid reveals share one windup and match in loudness and peak (R-31, R-32); `platform-policy` loaded for anything paid.
- [ ] (F, S) Done: every delivered FLAC passes its must-targets (`render` exit 0; aim misses listed) and every cue is proven on its event in the debug cue log; sync on the device or "not verified"; no listening check-in asked; the owner's play-test flags, if any, recorded word for word on the card and as a `lesson` (R-36, R-41, R-50, R-54).
- [ ] (D) Takes per round by tier, rounds used (at most 3, then to the owner with the numbers), the rank table and the pick recorded; nothing edited in Roblox except the zone reverb and fader volumes (R-62, R-67).
- [ ] (D) Stand-ins named; reused and new parts listed; options and reasons recorded; could-not-check list written (R-61, R-62, R-64).
- [ ] (D) Nothing claims an audition, measurement or brain-chemistry effect that did not happen; the genre preset is named and every departure stated.

## 6. Routing: which reference to open

**Rules by topic** (each lives in one file): feeling, tension and loudness-matched A/B (S-01, S-02, S-18, S-25, S-183, S-186) in `references/emotion-recipes.md` §C; timbre and level (S-07, S-08, S-11, S-15, S-22) in `references/elements.md` §B; reward tiers, ladders, key and honest fail (S-194, S-59, S-60 to S-62, S-64, S-114, S-134) in `references/reward-and-juice.md` §B; variants, jitter, cooldown, long-stay zones, mouth sounds (S-88 to S-101) in `references/repetition.md` §B; warnings (S-99, S-136, S-137) in `references/horror-and-tension.md` §B; material and size keys, layer count by size (S-75, S-78) in `references/craft-satisfying.md` §B; loudness target, priority slots and ducking (S-102 to S-109, S-207, S-211) in `references/mix-and-loudness.md` §A-B.

| Task or question | Open |
| --- | --- |
| Inputs, stage sheet, layer jobs, temp pass, sources, design and edit passes, library, identity sheet, partners | `references/craft-process.md` |
| Self-review lines, the owner's play-test, measuring a file (`soundbench measure`), reviewing a sound set, when to stop | `references/review.md` |
| The editor: cue folder, `card.json` targets, `prompts.json`, the order of work, two-pass recipe, layers, loops, variants, reading `rank`, commands (measure, rank, render, generate, compare, parity), known limits | `references/craft-process.md` §5-§7; `references/review.md` §4; `references/cue-card.md` §D; `tools/audio/soundbench/README.md` |
| Worked examples (ability, frequent pickup, footsteps and spaces, paid reveal) | `references/worked-examples.md` |
| Target feeling → tempo, register, spectrum, envelope, level, space, silence | `references/emotion-recipes.md` |
| Is this element or claim backed? Effect sizes, contested claims, culture | `references/elements.md` |
| Hit, pickup, break, coin, UI click recipes; what makes a sound satisfying | `references/craft-satisfying.md` |
| Horror, dread, scares, suspense, timers, warnings, tells and alarms | `references/horror-and-tension.md` |
| Rewards, pitch ladders, celebrations, sonic logo, reveals, honest outcome rules | `references/reward-and-juice.md` |
| Variants, jitter, cooldowns, loops, beds, fatigue, misophonia | `references/repetition.md` |
| Loudness, buses, priority, ducking, carry distance, music system, accessibility options | `references/mix-and-loudness.md` |
| Roblox classes, properties, limits, uploads, moderation, phone speakers, Studio checks; 2D or 3D, falloff, the room, ducking | `references/roblox-audio.md` (playback: §H) |
| Genre defaults and budgets (simulator, horror, combat, obby, tycoon, disaster, destruction) | `references/genre-presets.md` |
| AI generation prompts by texture, takes, clean-up | `references/ai-generation-prompts.md` |
| A term you do not know | `references/glossary.md` |
| Cue card fields, filled example, JSON blank | `references/cue-card.md` |
| A stage's ambience: zones, causes, point sources, blends, states (written by the environment designer; you fill the `sound:` keys) | `templates/environment/ambience-map.md`; `environment-design/references/ambience.md` |
| Checking a source, settling a dispute, updating rules | `evidence/README.md` |
| Testing this skill | `evals/briefs.md` |

## 7. Core principles for this craft

Each universal principle, stated for sound. The input letters are those of `references/review.md` §1; P is the owner's play-test, never asked as a listening session.

| # | Principle, for my work | Example | Check (input) |
| --- | --- | --- | --- |
| 1 | **The gameplay read comes first:** every state change has a cue a player can name with the screen covered; beauty never masks it. | The ability-ready chime cuts through combat; the lush ambience ducks under it. | R-02 (D); R-65 sound-off twin (D); the owner's play-test (P). |
| 2 | **Judge it where players meet it:** in the full mix, at the player's distance, on a phone speaker and headphones, at the burst rate. | A hit that sounded huge solo vanished under the music on a phone; its crunch layer fixed it. | R-23 phone loss and bands (F); R-41 at the burst rate (S); the owner's play-test on their devices (P). |
| 3 | **Decide what is heard first; spend contrast only there:** the important cue gets the unique timbre, the space before it and the top tier; small sounds stay close. | A boss tell owns the only rough timbre in the scene; footsteps stop at 40 studs. | R-15, R-16 (D, S); R-45 ducks with the four answers (D, S); the owner's play-test (P). |
| 4 | **Big before small:** gesture, stages and envelope first, then layers, then processing and sweetening. | Temp sound on the markers fires on its events in the debug cue log before any prompt for the ring. | R-50 log dated before the design pass (S). |
| 5 | **Shape carries identity:** a signature element per weapon, ability and character; sharp transients for threat hits, soft attacks for friendly things. | The frost staff's glass ring is in charge, release and impact. | R-13 (D); R-34, R-35 (F); the owner's play-test (P). |
| 6 | **Less is more:** cut what is not needed (frequencies first, then layers); one low-end owner; small sounds short and close. | A sparkle layer that changed nothing when muted is deleted. | R-24 (F); the sweetener test in the edit pass (S-77). |
| 7 | **One code for meaning:** one sound family per meaning, one footstep set per floor, one tell per attack, the same signature in every stage. | Healing and poison never share the chime family. | R-14, R-08 (D, S). |
| 8 | **Timing tells cause and effect:** one sound per stage, a rising charge, the transient on the contact frame, a tail that sells the weight, unequal combo gaps; one marker list. | The crumble keys to `contact_confirmed`, never `release`. | R-05, R-06, R-11 (D, T); R-43 (L); R-54 (V). |
| 9 | **Push what must read past real, on a believable base:** boosted transients, pitch for size, layers beyond the real recording; a natural core. | A small creature's roar pitched down a fifth for a boss. | R-51 `compare` raw vs processed: the core's note and main band kept (F). |
| 10 | **The subject's character drives every choice:** the verb picks the texture; a character sounds like its size, age, material and feel words. | A timid pet: short, soft, high squeaks; never the boss's growl family. | R-04, R-12 (D); R-35 siblings apart (F); the owner's play-test (P). |
| 11 | **One world, one style; identity survives every variant:** the identity sheet's tone words, signatures and forbidden list; variants keep the signature. | A premium skin re-themes the shot's crunch but keeps the ring. | R-13 (D). |
| 12 | **Controlled variation, never exact repetition:** several takes, small pitch and level jitter, beds from spliced takes; meaning never varies. | 6 coin variants, shuffle-bag; the tell has none. | R-26, R-31 (F); R-41 burst log (S); the owner's play-test (P). |
| 13 | **Problem, constraints and target first:** the card names job, story point, emotion, verb, hearing distance, rate and tier before any prompt. | The stage sheet is dated before the first take. | R-01 to R-05 (D). |
| 14 | **Research, many options, a reasoned pick:** textures not names, takes per round by tier, one odd variant, ranked against the card's targets with reasons; regenerate, do not pile on edits. | Six ring takes; take 4 is the only one inside the attack and band targets. | R-62 (D, F). |
| 15 | **Cheap stages first; gates freeze; not precious:** temp pass before polish; no final processing before the timing locks; delete a take that fights the mix. | A favourite whoosh is dropped because it masks the tell. | R-50 before the design pass (S); timing-list revision named on every card (D). |
| 16 | **Critique against the goal, one named problem at a time:** solo then mix; notes with a term, direction and amount; the problem behind each note. | "Attack 5 ms shorter; cut below 300 Hz on the sparkle", not "more whoosh". | R-60 (D); review findings per listen (`review.md` §5). |
| 17 | **Build for the next craft and the engine:** cues keyed to event ids, files starting on the transient, a library of parts, cue ids mapped to asset ids in data, baked processing. | The integrator wires cues from one table; no asset id in code. | R-06 (T); R-20 (F); R-40, R-44 (S, G). |
| 18 | **Know when it is done:** stop when the self-review passes, `render` passes the must-targets and the cue plays on its event; stand-ins named, not hidden; the owner's play-test flags reopen it. | Wind made from a generated whistle is shipped as a named stand-in. | R-36 (F); R-41 (S); R-61, R-66 (D); `review.md` §6. |
| 19 | **Feedback follows the real outcome:** a tick on input; the impact or reward sound on confirmation, weighted by its tier; one sound per merge window; honest reveals. | A rejected sale plays only the press click. | R-07 (D); R-41 rejected request (S); R-31, R-32 (F, D). |
| 20 | **Every player can read it:** no gameplay fact is sound-only; every intense cue has a reduced version; a cue paired with a visual pulse keeps it at the safe rate (at most 3 per second). | The low-health heartbeat has an edge-pulse twin and a reduced version. | R-65 (D); R-42 (S). |
