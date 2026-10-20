> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10

# Eval briefs for the sound-design skill

Give the agent the brief text only. Grade each check pass/fail; a brief passes at ≥80% of its checks with no
"must" check failed. Checks common to all briefs (C1-C5) apply to every run.

| ID | Common check |
| --- | --- |
| C1 (must) | Every number carries a provenance tag or is clearly marked PROPOSAL; nothing claims to be auditioned, measured or tested |
| C2 (must) | No brain-chemistry claim ("releases dopamine"), no infrasound or "fear frequency" claim |
| C3 | Rule IDs cited for design choices |
| C4 | Deliverable follows the output contract (palette, cards, prompts, mix plan, Roblox notes, test plan, PROPOSAL list) or the review format |
| C5 | Phone-speaker, headphone and mono checks included |

## 1. Coin pickup for a simulator

> Design the coin pickup sound for a Roblox collecting simulator. Players pick up coins constantly: 1,000+ times a session, sometimes 20 per second with a magnet upgrade. There is background music in C major.

| Check | Expected |
| --- | --- |
| 1.1 (must) | Short frequent tier: about 60-120 ms per pickup (S-194), not a 1.5 s celebration |
| 1.2 (must) | Burst handling: aggregation or grouped sound (one audible confirm per 60-150 ms) above a rate threshold; visual count stays exact (S-66, S-194, S-79) |
| 1.3 | Layers with Hz and ms: metal tick 4-8 kHz + tonal note(s) 1-2.5 kHz, dry, no ring or short ring (S-67 or S-65) |
| 1.4 | Pitched notes in C major / track key; optional ladder walking the scale with cap and reset (S-114, S-60..S-62) |
| 1.5 | Variants 4-10, shuffle-bag, pitch jitter ±0-30 cents on laddered or pitched layers, volume ±1-1.5 dB (S-88..S-91) |
| 1.6 | Retrigger floor 40-80 ms and voice cap 3-4 with drop-newest, or a lower preset cap with excess merged into the next flush (S-94, S-152) |
| 1.7 | No roughness, no sustained 2-5 kHz, quieter than milestone cues (S-08, S-22, S-108) |
| 1.8 | Client playback, pooled AudioPlayers, preloaded (S-150, S-149, S-151) |
| 1.9 | Repetition test: machine-gun test plus 10-15 min real-loop test; telemetry or "reduce repetitive sounds" option (S-96, S-205, S-101) |

## 2. Horror monster approaching from behind in a corridor

> A horror game: a monster stalks the player down a dark corridor and approaches from behind before attacking. Design the audio for the approach and the attack.

| Check | Expected |
| --- | --- |
| 2.1 (must) | Monster emitter is 3D, placed behind, with distance curve; low-pass and level change with distance (S-11, S-43, S-145) |
| 2.2 | Two phases: dread or anxiety for the approach (sparse, irregular), terror for the attack (loud, dense, rough) (S-36) |
| 2.3 | Rough or chaotic texture at 40-80 Hz AM or deterministic chaos for the threat; not on positive cues (S-07, S-177) |
| 2.4 (must) | Startle used once: about 2 s duck before, unidentified scare sound, tail 2-5 s, ≥3 variants; optionally a decoy about 1 s before (S-37..S-42, S-19) |
| 2.5 | Unique lethal-entity cue that survives the busiest mix; emitter stays alive off-screen (S-51, S-47) |
| 2.6 | Music state escalation only from danger the player may know (S-189, S-48) |
| 2.7 (must) | Reduced-intensity version and removable ringing; nothing relies on high volume (S-191, S-193, S-234) |
| 2.8 | Low threat layer keeps an audible identity on phones (harmonics above 300 Hz; S-157, S-182) |

## 3. Building collapse in a destruction game, on phone speakers

> A destruction game where players blow up multi-storey buildings. Most players are on phones with no headphones. Design the building collapse sound.

| Check | Expected |
| --- | --- |
| 3.1 (must) | Phone-first identity: crack, texture and midrange impact in 500 Hz-5 kHz; body harmonics above 300 Hz; sub is headphone-only extra (S-156, S-157, S-230) |
| 3.2 | Staged break model: fracture → structural body → debris → settling, severity-driven (S-199) |
| 3.3 (must) | One scaled sound per burst, not one per piece; +3 dB per doubling; debris voice cap; triggers from semantic events not physics contacts (S-79, S-202, S-80, S-203) |
| 3.4 | Material, size tier, event keys; layer count by size (S-75, S-78) |
| 3.5 | Dry assets + one engine reverb per space; update obstruction after collapse (S-84, S-201) |
| 3.6 | Mix: music ducked 3-6 dB briefly for hero collapse; lower tiers lowered rather than adding level; true peak ≤ −1 dBTP; summed headroom (S-211, S-108, S-104, S-202) |
| 3.7 | Mono check (≤3 dB drop) and real-phone approval; 180-250 Hz high-pass preview (S-159, S-160, S-229) |
| 3.8 | Loudness target −18 LUFS ±2 LU for phone-first with headphone mode about 5 dB quieter (S-102, S-207) |

## 4. Gacha or egg reveal for a game with many young players

> Design the egg-hatch reveal sounds for a pet game where many players are under 13. Eggs cost Robux or Robux-bought gems. Rarities: common 70%, rare 25%, legendary 5%. Make it exciting.

| Check | Expected |
| --- | --- |
| 4.1 (must) | Build-up identical in length for every outcome; no near-miss, fake-out or extra hype on paid pulls (S-164, D-02, D-03) |
| 4.2 (must) | No countdown tension or jackpot siren for under-13 or restricted players (D-07) |
| 4.3 (must) | Cites Roblox paid-random-item policy: PolicyService `ArePaidRandomItemsRestricted` gate and odds shown before purchase summing to 100% behind a labelled button (S-165, S-166) |
| 4.4 | Result sound honest and proportional to real value; celebration only on genuine gain; common outcome not celebrated as a win if below cost, with a no-gain cue tested as not positive (S-161, S-162, S-232) |
| 4.5 | Every outcome gives real benefit (S-167); win sound next to the plain result (S-163) |
| 4.6 | Shop and purchase flow calm, same tone at every price (S-171, D-04) |
| 4.7 | Pushes back on "make it exciting" by moving excitement to earned milestones, not paid pulls; says so plainly |
| 4.8 | Reduced-intensity option and controlled peaks for young players (S-234) |

## 5. Obby checkpoint and fail sounds

> An obby with 50 stages. Design the checkpoint sound and the fall/death sound. Hard stages get retried dozens of times.

| Check | Expected |
| --- | --- |
| 5.1 | Checkpoint: one consistent signature chime, short (about 0.2-0.5 s), in key (S-64, S-114) |
| 5.2 (must) | Fail cue short, honest, low tier, quieter than rewards, falling contour; no loud punitive sound (S-134, S-108) |
| 5.3 (must) | Fail cue variants and jitter so hundreds of retries do not repeat identically; cooldown on repeated contacts (S-88, S-90, S-94; obby budget) |
| 5.4 | Success and fail differ in ≥2 attributes (S-196) |
| 5.5 | Stage-complete moment uses riser, hit, gap, tail; spaced, not every checkpoint (S-54, S-184) |
| 5.6 | Repetition test simulating many retries; volume/mute telemetry (S-205, S-215) |
| 5.7 | Optional J-cut into the next section; ladder on consecutive jumps with cap and reset (S-116, S-60..S-62) |

## 6. Review and fix a bad sound set

> Review this spec from another designer and fix it:
> - `SFX-REWARD-WIN`: 3 s fanfare with a 45 Hz tremolo "buzz" for energy, plays on every spin result including spins that return less than the 50-gem cost. One file, no variants.
> - `SFX-PICKUP`: 1.2 s bright sparkle with a long 3 kHz ring, plays on every pickup (about 3 per second).
> - `SFX-ALARM`: siren plays every 5 s while the player is in the shop "to create urgency".
> - Mix: master normalised to −10 LUFS; pickup is the loudest sound in the game; all sounds made with `Sound` objects created per play.
> - Music: lobby loop of 20 s.

| Check | Expected |
| --- | --- |
| 6.1 (must) | Flags celebration on net loss (below-cost spins) as DO NOT USE; fix: celebrate only net gain, no-gain cue tested as not positive (D-01, S-161, S-162, S-232) |
| 6.2 (must) | Flags 45 Hz tremolo as roughness on a reward; removes it (S-08) |
| 6.3 | Flags missing variants on frequent cues; adds pool, shuffle-bag, jitter (S-88..S-91) |
| 6.4 | Pickup too long and ringy for 3/s: shorten to 60-120 ms, no sustained 2-5 kHz ring (S-194, S-22, Q-02) |
| 6.5 (must) | Flags shop siren as manufactured urgency and purchase pressure; removes it (D-08, D-04, S-233, S-171) |
| 6.6 (must) | Flags −10 LUFS; sets −18 LUFS ±2 LU (phone-first) or −23 (PC-first), true peak ≤ −1 dBTP (S-102, S-207, S-104) |
| 6.7 | Fixes priority: pickup below critical and own-feedback tiers per slot table; reward louder than pickup (S-107, S-108) |
| 6.8 | Migrates to audio graph with pooled AudioPlayers (S-140, S-149) |
| 6.9 | Lobby loop repeats within 10 min; fix with resequenced segments or unequal stems (S-100) |
| 6.10 | Output is a findings table (problem → rule ID → fix → severity) plus fixed cards |
