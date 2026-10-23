> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Revised by J020 step 8 sound-designer · claude-opus-5-5 · high · 2026-10-23 (soundbench, takes per round, playback, the play-test).

# Worked examples (Roblox, our pipeline)

Numbers are illustrative: settings are (P) start values, results are what the checks would report. They show the order of SKILL.md §2 and which checks prove each step.

## 1. Frost bolt staff (battlegrounds): an ability that slows

**Frame (step 1).** Job: feedback on the player's shot plus a cue for the target ("the bolt freezes the target"). Emotion: power for the caster, alarm for the target. Verb: *slows* (same word on the animator's clip card and the VFX frame script). Viewers: the caster hears the full set; the target hears the travel and impact at full strength from 60 studs; bystanders hear it lower and shorter (SC-07). Rate: one cast per 4 s cooldown.

**Stage (step 2).** From timing list r2 (30 fps): `charge_start` 0.133 s, `release` 0.433 s, projectile spawn (code), `contact_confirmed` (server), `slow_end_warn` 0.5 s before the slow ends. Stage sheet: charge (attempt), release (attempt), travel loop on the projectile's emitter, impact and ice crumble (outcome, only on a confirmed hit), slow-end warning (rising). A miss gets a dry ice puff where the bolt lands, not the freeze.

**Choose (step 3).** Texture that moves like *slows*: decelerating, spreading crackle with a long tail. Signature: a bright glassy ring on one note of the game key, in the charge, the release and the impact (SC-11). It must differ from the fire staff's signature (low roar): different register and timbre.

**Layers (step 4).** Release = five jobs (`craft-process.md` §3): low body 60-150 Hz (release and impact only), tick 3-6 kHz in the first 5 ms, crunch 1-3 kHz (carries it on phones), short icy report, the signature ring unprocessed. Impact adds the crumble tail, 600 ms vs 250 ms for a normal hit, so the slow is heard as slow.

**Temp pass (step 5).** Library parts: an old glass tick, a generic whoosh loop, a crunch from the crate break. Wired on the event ids by the integrator. The debug cue log from the studio operator's play-test shows the crumble firing on `release`, 0.3 s before `contact_confirmed` (R-50). Fix: the crumble keys to `contact_confirmed`, not `release`.

**Sources and design (steps 6-7).** Important cue: its layers generated separately, 6 takes per round each (J020-D9). Prompts by texture: "dry palm leaves crunching slowly", "foil crumpling, slow" (crumble layer), "glass bottle tink, single" (ring layer); odd variant: a reversed tink for the charge. Rank against the card: ring takes 1-3 miss the attack target (rise 9-14 ms vs ≤ 4 ms must), take 4 passes all musts, take 6 passes but its F-10 is untrusted (noise), so take 4 wins; the others go to the library. Recipe on the ring: `varispeed` +12 st, `highpass` 300 Hz, `compress` hard to lift the shimmer, `echo` short, `compress` again, `transient` attack up; edit pass trim → fade → loudness F-09 → peak → FLAC. `compare` raw vs processed: the note moved by the intended octave, the main band kept (R-51). A crumble round that missed the length target in all 6 takes was regenerated with "settling slowly, long tail" added (round 2 of 3).

**Edit and mix (steps 8-9).** Release trimmed to start on its tick (F-01 = 1.2 ms); the travel loop has no baked pass-by (a loop would repeat it); the moving emitter gives distance and panning, and graph emitters get no Doppler, so the pass-by is left out (SC-10). Tier 2 own feedback; the target's impact tier 1 for the threatened player.

**Checks.** R-04 (crumble F-05 decay to −20 dB: 410 ms vs 160 ms for a normal hit), R-06 (no missing marker), R-07 (impact on the confirmed event), R-20, R-23 (crunch keeps 31 % in 500 Hz-5 kHz), R-24, R-27 (ring within 12 cents of E5), R-28 (charge rises, peak in the last 6 %), R-35 (the ring's E5 sits in 500 Hz-5 kHz, the fire staff's roar in 120-500 Hz: different main bands, F-06), R-36 (`render` exit 0 on every stage file), R-45 (the caster hears charge and release 2D; others hear the bolt 3D on the projectile, `Linear` 4-60 studs (P), the target's impact at full tier), R-54 not verified until a device capture. Feel: the owner's play-test.

## 2. Coin pickup with a magnet (simulator)

**Frame.** Job: feedback ("you got it"). Emotion: satisfaction, small. Rate: up to 20 per second with the magnet; 1,000+ per session. The feedback stack (game designer) gives a 100 ms merge window: one sound and one label per window; the counter shows the true value at once. The reward tier table (progression designer) puts the coin at T1 and the bag-full event at T2 (small goal).

**Stage.** Attempt: the touch on the client plays the small tick at once (positive-only pickup, S-219). Outcome: the counter bump and, every 10th coin in a chain, one ladder step. Bag full (T2) gets its own short confirm, 150-300 ms (S-194 tier B), not a milestone flourish.

**Layers.** Tick 4-8 kHz, 3 ms + one note 1-2.5 kHz in the music key, 80 ms, dry (S-65, S-67). No body below 200 Hz: a bright layer gets a low cut (R-24). Ladder: pentatonic steps of the track key, cap +12 st, reset after 1 s idle (S-60 to S-62).

**Repetition.** 6 variants, shuffle-bag excluding the last 2, ±15 cents on the pitched note, ±1 dB (S-88 to S-91); retrigger floor 60 ms; voice cap 3, drop newest.

**Checks.** R-15 (shorter and quieter than the bag-full confirm), R-22 (to −40 dB in 140 ms), R-31 (variants within ±1 dB), R-41 (debug cue log at 20 per second: one cue per 100 ms window), R-36 (each of the 4 variant files of its round passes `render`), R-45 (2D for the collector, no 3D version for others: a crowd's pickups would spam them). Repeats by ear: the owner's play-test.

## 3. Hub footsteps and a reverb per space

**Inputs.** Ambience map rev 3: zones Z-PLAZA (open stone), Z-HALL (wooden interior), Z-CAVE (rock, wet). Floor-material list from the environment designer: Slate, WoodPlanks, Grass (decorative tufts only), Rock, Sand.

**Footstep table (identity sheet).** Slate → stone set, WoodPlanks → wood set, Rock → rock set, Sand → sand set; Grass tufts are non-collidable decoration on Slate, too small to read as a floor: players stand on Slate and hear stone, so the tufts stay small (SC-12). Each set: 6 variants, ±50 cents, played from `Humanoid.FloorMaterial` on the footfall events of the walk and run clips. Carry (actor rule, `roblox-audio.md` §H1): own steps 2D, quiet; other players' steps 3D, `InverseTapered`, bounds 8 to 40 studs (P) (SC-07).

**Space.** One AudioReverb per space type on the SFX bus, its settings switched by a zone script as the player walks in: plaza short and open, hall wooden medium, cave long and dark (settings PROPOSAL). The footstep files stay dry, one file per step for every space, and take the room (field 53), so the own 2D steps sound like the cave too (SC-08, J020-D10).

**Checks.** R-14 (read-only listing of the place's walkable materials: all five in the table; a new "Glass" floor added later is flagged to the environment designer before it is built, with Slate named as the set to use if glass steps cannot be made in time), R-16, R-40 (three AudioReverbs, one per type, and no other audio effect), R-45 (the zone script switches the reverb; music and UI bypass it). Whether each space sounds like the place: the owner's play-test.

## 4. Paid egg reveal (honest)

**Frame.** Job: feedback on a purchase result; emotion: anticipation, then joy scaled to the real value. Load `platform-policy` first: odds shown before purchase, the restricted-player path exists (S-165, S-166).

**Stage.** One shared windup (same asset, same 1.2 s for every tier), the result frame, then the tier ladder. Tiers differ by note count, register and tail (Common 1 note, Legendary 5 notes and a 2× tail), never by loudness or peak: the results' momentary maxima within 1 LU (F-13 b; the 2× tail does not hide a louder body there) and their peaks within 1 dB (F-03) (D-03). A result below the egg's cost plays the neutral no-gain sound (D-01). A tap skips to the result; a batch open gives the full ceremony only to the best result.

**Checks.** R-32 (one windup asset id for all tiers), R-31 (results' momentary maxima within 1 LU, F-13 b; peaks within 1 dB, F-03: every result's `card.json` names the paid-reveal family, so each `render` runs the family check and exits 1 on a miss, 3 while a sibling is missing), R-07 (result sound on the server-confirmed roll), §4 guardrails D-01 to D-08 on the card. All 2D (about me; no 3D version for others).
