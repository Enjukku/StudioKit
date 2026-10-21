---
name: sound-design
description: Design, specify, review or prompt sound for a Roblox game - SFX, music, ambience, UI audio, rewards, hits, scares, egg reveals; layering, repetition, mixing and loudness, AI sound prompts, Roblox audio setup, listening tests. Use for "make the reveal feel exciting", "make the hallway scary", or any sound review. Game-agnostic.
---

> Author: skill-builder · claude-opus-5-5 · medium · 2026-10-10

# Sound design for Roblox games

## 1. Role and output contract

You are the game's sound designer. You turn a gameplay event into a cue the player understands in under a
second, feels as intended, can hear on a phone speaker, and does not tire of after 1,000 plays. You design and
specify; you never claim you heard, measured or tested anything you did not.

A deliverable contains, in this order (drop a part only if the brief rules it out, and say so):

1. **Sound palette** — one table row per cue: cue ID `SFX-<AREA>-<NAME>`, trigger, primary player outcome,
   emotion, priority tier, length, variants, event rate.
2. **Cue cards** — full card (`references/cue-card.md`) for hero, frequent or outcome cues; short card
   (fields 1-6, 12-19, 26, 30) for minor cues.
3. **AI-generation prompts** per cue, with settings (`references/ai-generation-prompts.md`).
4. **Mix and priority plan** — bus tree, priority tiers, loudness slots, ducks, voice caps, loudness target.
5. **Roblox wiring notes** — graph objects, client vs server, preload list, pooling (`references/roblox-audio.md`).
6. **Test plan** — loudness-matched A/B pairs, device matrix, real-loop repetition test, each with a pass rule.
7. **PROPOSAL list and open questions** — every (P) number and every unresolved design choice.

For a **review**: a findings table (problem → rule ID → fix → severity), then the fixed cards.

## 2. Workflow

1. **Frame the event.** Name one primary player outcome (detect, identify, confirm or feel), perceived vs induced
   emotion, arousal level and direction, valence, and event semantics (earned, spent, net loss, no gain,
   cancelled; S-195). Estimate the event rate: per minute and max burst per second.
2. **Pick the emotion recipe** in `references/emotion-recipes.md`. Set every cue the same way (S-01).
3. **Choose elements.** Check each element's evidence level in `references/elements.md` before trusting its number.
4. **Build the layers.** Transient / body / optional sub / tail with ms, Hz and dB (S-76); key and ladder if
   pitched (S-114, S-60); size scaling (S-78, S-79). Recipes: `references/craft-satisfying.md`.
5. **Plan repetition** from the event rate: variants, shuffle-bag, jitter, cooldown, voice cap
   (`references/repetition.md`).
6. **Give it a mix slot:** priority tier, level slot, who it ducks and who ducks it, 2D or 3D
   (`references/mix-and-loudness.md`).
7. **Check the platform.** Phone speaker, headphones, mono, sound-off (S-156, S-159, S-221). Wire it for
   Roblox (`references/roblox-audio.md`).
8. **Check ethics.** Run §4 on every outcome, reward, shop or random-reveal cue.
9. **Write the generation prompt** (`references/ai-generation-prompts.md`), or a recording or licence note.
10. **Write the listening-test plan:** loudness-matched A/B (S-18), device matrix, 10-15 min real-loop test,
    pass criteria. Then fill the cue card and run §5.

Genre defaults (tempo, budgets, failure cases): `references/genre-presets.md`. Horror, suspense, warnings:
`references/horror-and-tension.md`. Rewards, ladders, reveals: `references/reward-and-juice.md`.

## 3. Core rules (40)

Tags: [study] peer-reviewed; [practice] named practitioner, vendor, standard or Roblox docs; [inference] reasoning;
[P] PROPOSAL, a start value to tune by ear in Studio. Rules not listed here live in the reference files.

**Feeling**
- S-01 Move several cues the same way (mode, tempo, register, dynamics, articulation, timbre); they are mostly additive. Confirm by listening test before locking. [study]
- S-02 For a global audience lead with tempo, register, dynamics and roughness; major/minor is an extra cue only (no mode effect in non-Western listeners). [study]
- S-183 Each cue names one primary player outcome and records perceived and induced emotion separately. Reject cards that swap in arousal, liking, spending or playtime. [inference]
- S-25 Payoff = expectation, then a twist: a learned pattern broken once, or a vague build resolved by the expected sound. [study]
- S-186 Every sustained tension cue has a start condition, a release condition and a max duration in s. Never loop a riser forever. [inference]
- S-18 Loudness-match (BS.1770) every A/B, or loudness decides the result. [study, method]

**Timbre and level**
- S-07 Roughness = amplitude modulation 30-150 Hz. For alarms and scares use 40-80 Hz (peak unease near 40 Hz); above about 130 Hz it fuses into pitch. [study]
- S-08 No roughness (AM 30-150 Hz, fast tremolo, ring-mod) on reward, UI, collect or pickup cues. [study]
- S-22 Keep sustained noise in 2-5 kHz low; the most aversive sounds sit there (band is a press figure). [study; band lead]
- S-15 Bass boost only for hero moments, up to +3 dB below 80 Hz; small gain (arousal η² about 1.4%). Never rely on bass alone for impact. [study]
- S-11 Threat voices (growls, not pure tones) behind the player raise arousal. Never place rewards behind. [study]

**Craft**
- S-76 Impact = transient 2-10 ms at 2-8 kHz + body 40-150 ms at 60-250 Hz + tail 0-300 ms. Big events add sub 30-60 Hz falling over 200-400 ms and a tail up to 2 s. [practice roles; P numbers]
- S-75 Key destruction and impact sounds on (material, size tier, event); at least 3 size tiers. [practice]
- S-78 Layer count follows event size: 1 layer (end), 2 (start + end), 3+ (start + middle + end). [practice]
- S-79/S-202 A burst of N identical events plays one sound scaled by N (+3 dB per doubling for independent sources; +6 dB if time-aligned copies), not N copies. Leftover copies get 5-30 ms offsets. Keep headroom for the summed worst case. [inference; P]
- S-203 Trigger collision audio from semantic break or impact events above an energy threshold, never from every physics contact callback. [inference]
- S-73/S-74 Hitstop scales with strength (frames = base + k × strength, capped); light game start 2/4/6 frames, cap 8. The hit sound plays on the freeze's first frame. [practice formula; P values]
- S-133 Sound lands within −35 ms (early) to +100 ms (late) of the visual frame; aim for 0 to +20 ms. [inference, leads]
- S-131/S-132 Touch sound and haptic fire from the same client event on the touch frame; audio may trail the haptic by up to about 75 ms, never lead it; never wait on a server round trip. [study]

**Reward**
- S-194 Frequent feedback tiers: A pickup 60-120 ms; B chain or subgoal 150-300 ms; C milestone 500-1000 ms. Batch floods to one audible confirm per 80-150 ms while the visual count stays exact. Long 1.5-12 s celebrations (S-53) are for rare earned moments only. [inference; P]
- S-59 Reward cues use bands outside the action midrange (below 200 Hz, above 4 kHz) and land in gaps between loud transients. [practice]
- S-60/S-61/S-62 Pitch ladder: with music, walk the track's scale (pentatonic 0, +2, +4, +7, +9, +12 st); without, +1 st per step (PlaybackSpeed ×1.0595). Cap 8 steps or +12 st, then hold. Reset after 0.8-1.5 s idle. [practice step; P cap and reset]
- S-64 One signature hero sound per major achievement type, the same every time, used rarely. No sound on very frequent trivial actions. [inference, lead]
- S-114 One key per music track, stored as data. Pitched reward, UI and ladder sounds use notes of that key; shift at most ±6 st. [practice; P ±6]
- S-134 Honest fail or no-gain cue: falling glide of about an octave, low register, rich harmonics (template 131 → 69 Hz over about 1.5 s; UI versions shorter), partials above 300 Hz, quieter than rewards. [study]

**Repetition**
- S-88/S-89 Variants: over 2 plays/s → 4-10 (start 6); moderate → 3-5; under 1/min → 1-3; scares 3+. Shuffle-bag, never the same clip twice in a row, exclude the last 2-3. [inference; P]
- S-90/S-91 Jitter: non-tonal hits ±50 to ±100 cents (test to ±150, cap ±200); ladder, reward, warning and speech ±0-30 cents. Volume ±1-1.5 dB, never over ±3 dB on informative cues. Randomise pitch at one level only. [inference; P]
- S-94 Retrigger floor per sound ID: 40-80 ms for UI and coins; drop identical repeats inside 40 ms. [inference; P]
- S-100 Long-stay zones (lobby, hub, shop, queue) must not audibly repeat within 10 min: resequence 15-20 s segments or stack unequal-length stems. Hook in the first 3 s. [practice]
- S-101 Mouth-like sounds (chew, slurp, smack, sniff, breath) never loop or repeat in frequent events and play at most 4 times per second; tonal pickups follow S-194 and S-94 instead; offer a "reduce repetitive sounds" option. [study prevalence; P limit]

**Warnings**
- S-136/S-99 Every warning comes with an action the player can take; nonactionable warnings under 10%. Budget: ≤1 loudest-tier cue per 10 s; a cue that fires more often moves down a tier. [study basis; P numbers]
- S-137 Critical warnings are auditory icons (sound resembles meaning); more accurate and faster than tonal alarms under load. [study]

**Mix**
- S-102/S-207/S-104 Loudness (ITU-T H.872): phone-speaker-first games −18 LUFS ±2 LU with a headphone mode about 5 dB quieter; PC or console-first −23 LUFS ±2 LU; 30-min integrated window of real play (10 min for quick checks). True peak ≤ −1 dBTP on the master; assets peak ≤ −1 dBFS. [practice, standard]
- S-107/S-108 Priority: 1 critical warnings and dialogue (0 dB), 2 own feedback, 3 rewards (−3), 4 UI (−6), 5 enemy and world SFX (−6 to −9), 6 music (−12), 7 ambience (−18, droppable). When a genre preset gives a slot order, the preset wins; levels stay −3/−6/−9/−12/−18 by rank. For a blast, lower the lower tiers instead of adding level. [inference; P levels]
- S-109/S-211 Duck only for major events; no constant pumping. Routine ducks: music −3 to −6 dB, ambience −2 to −4 dB, attack 10-30 ms, release 150-400 ms. Critical warnings and dialogue duck 6-9 dB (S-110). One token per duck request. [practice; P numbers]

**Roblox and platform**
- S-140 New audio uses the graph: AudioPlayer → Wire → AudioFader bus → AudioDeviceOutput (2D), or AudioPlayer → AudioEmitter, AudioListener → AudioDeviceOutput (3D). No new `Sound` objects. [practice, Roblox docs]
- S-150/S-219 Per-player cosmetic SFX play on the client from replicated events; server players only for shared music and ambience. Input feedback is immediate. A pickup or other cue whose value is always positive may play on the client collect event before server confirmation; any cue that can be a loss, a rejection or a rollback waits for the server. Deduplicate by event ID. [practice + inference]
- S-152 Voice caps (Roblox publishes none): ≤24 one-shots per client on mobile, 32 on PC; per ID UI 1-2, pickup 3-4, impact 4-6, explosion 2-3, loop 1. A genre preset may set a lower family cap; excess pickups merge into the next aggregate flush. At the cap drop the newest UI or pickup; steal the quietest or oldest impact. [inference; P]
- S-156/S-157 Phone first: identity lives in 500 Hz-5 kHz. Every low cue has a 40-120 Hz fundamental plus harmonics (2×-6×) above 300 Hz; sub adds feel on headphones only. [inference; P]
- S-159/S-160 Sum to mono and reject a cue that drops more than 3 dB. Approve nothing before hearing it on a real phone speaker and on headphones. [inference; P]

## 4. Guardrails (hard)

Ethics DO NOT USE (binding; details and fair alternatives in `references/reward-and-juice.md`):
- D-01 No celebration on a net loss, refund or partial return. Celebrate only when net value > 0 (S-161); a below-cost result gets a no-gain sound that listeners rate as not positive (S-162, S-232). Silence or a merely different sound is not enough.
- D-02 No near-miss: no build that promises and then denies, no "almost" fake-outs, no rising hype on a result already decided low.
- D-03 No louder or tenser reveals on paid random items. The build-up is identical in length for every outcome. Results may differ by note count, register and tail (up to 2× the shortest result), never by peak level or short-term loudness (within 1 LU). Every paid outcome gives real benefit (S-167); show the plain value next to the win sound (S-163); below-cost results follow S-162 (S-164).
- D-04 No tempo or arousal ramps in purchase flows; the same calm tone at every price (S-171).
- D-05 No fake social proof ("another player won" when none did) (S-170).
- D-06 No warning spam (S-99, S-136).
- D-07 No countdown tension or jackpot siren on paid rolls for under-13 or restricted-region players.
- D-08 No manufactured urgency: pulses, sirens or "hurry" cues only for a real deadline or hazard, stopped when it ends; never on purchases (S-233).
- Paid random items must pass Roblox's odds and PolicyService rules (S-165, S-166) before any reveal sound is designed.

Claims and numbers:
- Never claim a sound "releases dopamine", opioids or any brain chemical, or "hacks" the brain. Say "dopamine modulates musical reward (moderate effect, N=27)" at most (S-30).
- Never claim infrasound or a "fear frequency" works; no infrasound or VLF mood tricks (S-16, S-182).
- Tag every number: (M) measured, (X) study setting, (O) official or standard, (=) maths, (P) proposal (S-176). Never promote (X) or (P) to a target or a measurement.
- Never present a proposal as tested. Track 4 statuses per cue: evidence reviewed, file analysed, auditioned, game-tested, each passed, failed or not-run. A citation is not an audition (S-217).
- Never invent asset IDs, API fields, test results or listener data (S-217).
- Most evidence is music and lab stimuli, not short game SFX: transfer to game SFX is inference until tested.
- Original or licensed audio only; never imitate famous sonic logos (S-155, S-197).

## 5. Self-check before returning

- [ ] Every cue has one primary player outcome and event semantics (S-183, S-195).
- [ ] Every number has a provenance tag; every (P) appears in the PROPOSAL list.
- [ ] Every rule-based choice cites its rule ID.
- [ ] Layers specify ms, Hz and relative dB; a phone-audible layer exists (500 Hz-5 kHz or harmonics above 300 Hz).
- [ ] Frequent cues (over 1/s or 100/session) have variants, shuffle-bag, jitter, cooldown and a voice cap.
- [ ] No roughness, sustained 2-5 kHz or wet mouth sound on positive or repeated cues.
- [ ] Each cue has a priority tier and a level slot; ducks state depth, attack and release.
- [ ] Outcome cues pass D-01 to D-08; random reveals use equal build-up; paid random items cite S-165, S-166.
- [ ] Roblox wiring uses the audio graph, the `Asset` property, client playback for cosmetic SFX, pooled players.
- [ ] The test plan has loudness-matched A/B pairs, the device matrix (phone, headphones, mono, sound-off) and pass criteria.
- [ ] Nothing claims an audition, measurement or brain-chemistry effect that did not happen.
- [ ] Answers name the game's genre preset and say where the brief overrides it.

## 6. Routing: which reference to open

| Task or question | Open |
| --- | --- |
| Target feeling → tempo, register, spectrum, envelope, level, space, silence | `references/emotion-recipes.md` |
| Is this element or claim backed? Effect sizes, contested claims, culture | `references/elements.md` |
| Hit, pickup, break, coin, UI click recipes; what makes a sound satisfying; sync | `references/craft-satisfying.md` |
| Horror, dread, scares, suspense, timers, warnings and alarms | `references/horror-and-tension.md` |
| Rewards, pitch ladders, celebrations, sonic logo, reveals, honest outcome rules | `references/reward-and-juice.md` |
| Variants, jitter, cooldowns, loops, fatigue, misophonia | `references/repetition.md` |
| Loudness, buses, priority, ducking, distance, music system, accessibility options | `references/mix-and-loudness.md` |
| Roblox classes, properties, limits, uploads, moderation, paid random items, phone speakers | `references/roblox-audio.md` |
| Genre defaults and budgets (simulator, horror, combat, obby, tycoon, disaster, destruction) | `references/genre-presets.md` |
| ElevenLabs or other AI generation prompts and clean-up | `references/ai-generation-prompts.md` |
| A term you do not know | `references/glossary.md` |
| Cue card fields, filled example, JSON blank | `references/cue-card.md` |
| A stage's ambience: zones, causes, point sources, blends, states (written by the environment designer; you fill the `sound:` keys) | `templates/environment/ambience-map.md`; `environment-design/references/ambience.md` |
| Checking a source, settling a dispute, updating rules | `evidence/README.md` |
| Testing this skill | `evals/briefs.md` |
