---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: vfx-synthesis (vfx-reference-synthesis workflow) · claude-opus-5-5 · default · 2026-10-12

# VFX reference: Output 6 mistakes table, Output 8 effect card template, Output 9 review checklist

## Scope and use

Merged from the Claude research files (`knowledge/external/vfx-research-2026-10-12/`, verifier corrections applied, gap files over first-run files) and the ChatGPT package (06, 08, `effect_card_template`, 09, claim ledger, supporting reference). Claims were reconciled per publication: two models citing one page count as one source.
The VFX designer agent fills the Output 8 card before it picks assets. It runs the Output 9 review on every effect and diagnoses with the Output 6 ids (M-xx). Sources are R-ids in `00-sources.md`. PROPOSAL values are starting points to test. They are never evidence, and they stay proposals until the owner confirms them.

## Keys

| key | meaning |
| --- | --- |
| evidence level | study, preprint, industry practice (who, year), spec, inference. "single tier C" = the only source is tier C (rule: needs a second source). Tier D = lead only, never proof |
| PROPOSAL | `PROPOSAL (inference): <value>; basis: <reason / nearest R-ids>; tune by: <test T-xx>`. In YAML: `{value, ev: "PROPOSAL (inference)", basis, tune_by}` |
| frames | Frame counts stay in frames unless the source states its fps ("fps not stated"). Our own conversions use the 60 FPS default client cap (spec, R-198) and are labelled |
| M-xx / T-xx / C-xx | mistake id (Output 6) / test in "Open / test ourselves" / conflict in "Conflicts" |
| Roblox checks | Studio greyscale = `ColorCorrectionEffect.Saturation = -1` on Camera (spec, R-184). Blur = `BlurEffect.Size` px (spec, R-181). Slow playback = `ParticleEmitter.TimeScale` 0..1 (spec, R-211). Quality = Studio "Editor Quality Level" lowest and highest (spec, R-209). Perf = Debug Stats, Performance Stats, MicroProfiler (spec, R-198), `Stats.RenderGPUFrameTime` (R-461) |

## Output 6. Mistakes table

Sub-tables use the same columns. A fix is a hypothesis to retest, not a guarantee (ChatGPT 06 intro; inference).

### 6.1 Truth: area and timing

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-01 Visible area does not match the gameplay area (ring, flash or dust edge bigger or smaller than the server blast) | Teaches a false safe/unsafe edge. Riot ranks fixing inaccurate hitbox indicators above every other VFX goal | Overlay the server shape (debug sphere of the blast radius) on frozen frames at contact and at active end; check every variant (quality tier, viewer, skin) | Fix the primary edge first. Keep the footprint identical in all variants. Decoration never extends past it | industry practice (Riot dev blog 2022) R-060; (Riot "Clarity in League" 2021) R-080; (Riot PBE notes 2020, single tier C) R-374 |
| M-02 Indicator drawn "slightly larger or smaller" than the hitbox on purpose | A big circle implies more dodge room than the real threat (Riot's Arcane Comet example) | Compare indicator radius with the config radius as numbers, not by eye | Match exactly. A deliberate offset is an owner decision, never a default (C-03) | industry practice (Riot 2021) R-080 vs descriptive "some games do this" (VFX Apprentice 2026, single tier C) R-336 |
| M-03 Visual peak not on the gameplay contact frame | Hit reads late, soft or unfair. The effect must appear when damage lands | Capture at 60 fps; log frames of server contact, first bright frame, sound transient. They must coincide | Retime the art (start on an energetic cell or pick another asset). Never move the gameplay hit to fit the art | industry practice (VFX Apprentice 2025) R-346; (Beardilocks/Riot 2020) R-368; both tier C; inference |
| M-04 Windup or crescendo added to an instant event | An instant effect skips anticipation and starts at high intensity; a swell before it reads as lag | Compare contact time with the frame where the visual peaks | Remove the build; start at peak. Keep crescendo only where gameplay gives warning time | industry practice (VFX Apprentice 2025, single tier C) R-346; inference (ChatGPT 06) |
| M-05 Danger look stays after the hazard ends | Player keeps avoiding a harmless area | Step to the last active server tick; anything still in hazard colour or shape after it fails | End the hazard cue on the active-end tick. Residue changes look (lower value, no hazard colour). Hall's expiring stun trap blinks out | industry practice (Hall/Sparkadia 2023, single tier C) R-355; inference |
| M-06 Fuse or charge visual does not match the real countdown | Teaches a false escape window | Log visual stages against the server detonation time over 20 runs | Drive every fuse stage from the server timer. Anticipation length is a game-design setting, not art | industry practice (Jevremovic/Nordeus via 80 Level 2018: anticipation 0.5 s to 2 s set in a spell setting) R-310; inference |
| M-07 Telegraph shorter than human reaction | Unavoidable hit = unfair. Lab visual simple reaction time: mean 230.8 ms (n=1469; hardware-corrected 213 ms) for a known stimulus and one response. A game dodge adds choice, motor and render time | Count frames at the capture fps from first visual change to the damage frame; compare with reaction + trigger + buffer | Lengthen the windup; add sound and animation channels. Floor 0.25 s is a minimum, not a target (T-01) | study (Woods et al. 2015) R-130; industry practice (Kraj/GDKeys 2020, single tier C) R-373; industry practice (Stout 2015: use several channels) R-320 |
| M-08 Hit effect in the wrong place under latency | Correct simulation looks wrong (body hit shown at the head; client and server disagree) | Frame-step a moving target with Studio Network Simulation latency | Spawn locally on the hit event, attach to the struck part, reconcile when the server disagrees | industry practice (Riot "State of Hit Registration" 2020) R-102; spec R-198 |
| M-09 Destruction VFX hides or fakes the structural change | Players cannot read the new hole, remaining cover or loose bricks. Destruction must be readable and deterministic | Pause at dissipation start and 1 s later: can a viewer point at the hole and the loose bricks? | Depict only server-confirmed breaks. Dust clears the hole first. Keep debris traversable and calm | industry practice (DICE/Sirland 2025) R-255; (Embark Season 8 2025) R-030; (Embark Season 9 2025) R-031; inference (ChatGPT destruction contract) |
| M-10 Break visual fires without its sound, or the reverse | Mismatch reads as a bug; Embark shipped a fix for missing paired destruction visuals and audio | Data gate: every break type has {visual id, sound id}; fail if one is empty | One data record per break type | industry practice (Embark update 10.0, 2026) R-011 |

### 6.2 Communication and importance (readability)

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-11 Every effect looks top-tier | Prominence stops predicting consequence; a basic hit as big as the climax devalues the climax | Show tiny, normal, big and rare events side by side. Rank by importance and by measured peak value x screen area; the two orders must match (T-02) | Trim ordinary peaks; keep the top of size, brightness and noise for rare events | industry practice (Riot 2021) R-080; (Beardilocks/Riot 2020) R-368; (Riot guide via VFX Apprentice 2022) R-360. No source maps a rating to size, brightness or duration (C-11) |
| M-12 No single area of focus | Viewer cannot say what the effect is ("if everything is important, nothing is", Beardilocks 2020) | Freeze at punch: can one element be pointed at within 1 s? Blur test: does one shape survive? | One dominant primary shape; secondary elements lower in value and saturation; plan areas of rest | industry practice (Beardilocks/Riot 2020) R-367; (VFX Apprentice 2023) R-358; (cEssex realtimevfx 2025, blur test) R-344; all tier C, 3 publications |
| M-13 Decoration brighter than the gameplay part (bright trail on a weak projectile head; embers hold the brightest pixel) | The eye follows decoration, not the collision | Pause; find the max-luminance and max-saturation pixels; they must sit on the damaging or rewarding part | Lower trail value, opacity and detail; give the head the extremes. Direction must read without motion | industry practice (Beardilocks 2020) R-367; (Riot 2021) R-080; inference |
| M-14 Own-weapon feedback outshines threat cues | Launch and muzzle effects compete with incoming danger | After play, ask what the muzzle flash looked like. Correct answer: "did not notice" | Keep own launch cues below threat and hazard cues | industry practice (Nguyen/Counterplay GDC 2022) R-071 |
| M-15 Big feedback on the action (swing, throw, charge) instead of the result | Pre-registered study (n=1,699 in all). Model A (n=678): amplification lowered competence (-.43) and effectance (-.19). Model B (n=1,699): success-dependent feedback raised competence (+.45). Amplified swings covered the hit | Compare miss, hit and big hit: is the big cue only on success? Does the action cue cover the impact point? | Small cue on the action; big cue only on the confirmed outcome; never cover the impact point | study (Kao et al. CHI 2024; both inputs read the same paper = 1 publication) R-043; study poster, abstract only (Juul & Begy 2016: juicy rated higher, played worse) R-123 |
| M-16 Judged in the preview, invisible in play | Faint, desaturated, wispy first passes vanished in busy play | Review only in a real stage, real camera distance, with other players, debris and UI | Bolder, crisper shapes and value separation; retest in context | industry practice (Hall/Sparkadia 2023, single tier C; ChatGPT rates it first-hand) R-355 |
| M-17 Strong for the caster, blinding for others | Target and bystanders lose the scene | Review from the target's and a bystander's camera, not only the caster's | Smaller, dimmer or more transparent for others; per-viewer variant | industry practice (Nguyen GDC 2022) R-071 |
| M-18 Miss, blocked and success look the same | Player cannot learn cause and effect | Play the 3 outcomes muted; observers name each | Distinct shape and value per outcome; outcome cue after the action cue | study (Kao 2024) R-043; inference (ChatGPT 09 V25) |

### 6.3 Value

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-19 Whole effect at 0% or 100% value or saturation | Pure grey sinks into the world; pure white or full saturation fights UI and kills hierarchy | Greyscale capture and saturation check at punch | Mid-value base; extremes (100% white) only on the focus of top-tier events (C-04) | industry practice (Riot VFX style guide 2017, read by ChatGPT from an unofficial mirror) R-120; summary (VFX Apprentice 2022) R-360; (Beardilocks 2020: save 100% white for ultimates, tier C+) R-372 |
| M-20 Effect and stage behind it have the same value | Effect vanishes on some stages | Greyscale capture on each stage; focus must stay the highest-contrast patch | Separate by value first, colour second, shape third | industry practice (Beardilocks 2020) R-367; (VFX Apprentice 2023) R-358; both tier C, 2 publications |
| M-21 Bloom wash or uniform bright blob | Low bloom threshold makes everything glow; internal structure and nearby targets vanish | Capture normal and greyscale with Bloom on and off | Raise `BloomEffect.Threshold` so only focus pixels bloom; never pulse Bloom (M-84) | spec (BloomEffect Threshold 1 = only pure white blooms) R-180; inference |
| M-22 Additive blend on smoke or dust; stacked additive layers | Additive smoke disappears on bright stages; overlaps blow out to white | Bright stage plus greyscale; zoom where layers overlap | `LightEmission` 0 (normal) for mass that hides things; 1 (additive) only for luminous core and sparks | spec (LightEmission 0 normal, 1 additive) R-211; industry practice (Seavert/JangaFX, single tier C) R-399; (two-tone film smoke, VFX Voice 2022) R-286 |
| M-23 Effect value band above UI or below characters | UI gets covered, or the effect reads weaker than characters | Sample luminance: UI > effect focus > characters > world | Effects higher than characters and slightly lower than UI | industry practice (Hall/Sparkadia 2023, single tier C) R-355 |
| M-24 `LightInfluence` left at default | Self-lit flash goes black on dark stages, or lit smoke glows flat. Studio-inserted emitters default to 1, `Instance.new` to 0 | Test on the darkest and the brightest stage | Set it in data: 0 self-lit, 1 lit smoke and dust | spec R-211, R-209 |

### 6.4 Colour

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-25 Two strong complementary hues, none dominant | Hues compete; reads as noise | Blur; count hues at full saturation | One dominant colour plus one secondary; desaturate the rest (Riot cut Nocturne to two colours) | industry practice (Riot guide via VFX Apprentice 2022) R-360; (Riot PBE 2020) R-374; (Hall 2023) R-355; all tier C |
| M-26 One colour means different things | Vocabulary breaks (danger hue used on a reward or decoration) | Colour-to-meaning table: duplicates fail; new players classify unknown effects | One colour per category everywhere (VALORANT unified placed utility to one teal) | industry practice (Riot VALORANT 11.07, 2025) R-033; inference |
| M-27 Colour is the only signal (danger, team, rarity) | 1 in 12 men and 1 in 200 women have colour vision deficiency (UK charity); one study sample: 4.2% boys | Simulator plus greyscale, then real colour-blind testers | Add shape, pattern, motion or icon; two teams = orange vs blue plus a lightness difference; offer presets | industry practice (Xbox XAG 103) R-015; (Game Accessibility Guidelines, tier C) R-398; (Colour Blind Awareness) R-328; study (Mashige & van Staden 2019, one sample) R-107; industry practice (Okabe & Ito 2002) R-148 |
| M-28 Effect hue equals the stage hue at the same value | An all-orange projectile does not read in a fire-heavy scene | Place the effect over the most saturated area of each stage | Add a complementary secondary (Avalanche added blue to orange) | industry practice (Bernelind/Avalanche 2019) R-300 |
| M-29 Colour-blind filter treated as proof | Simulators are blunt; people differ | Only a simulator was recorded | Redundant signals, configurable colours, real player tests | industry practice (XAG 103) R-015; (GAG, tier C) R-398 |
| M-30 Light and scorch too orange and saturated | Reads cheap | Review in the lit scene | Desaturated light colour; darker, spiky scorch | industry practice (cEssex 2025, single tier C) R-344 |

### 6.5 Timing

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-31 Linear curves everywhere | Equal rates hide acceleration and release; `NumberSequence` interpolates linearly between keypoints | Plot size, transparency and speed over life | Ease with extra keypoints (2 to 20 per sequence); keep deliberately constant motion constant | industry practice (Hall 2023, single tier C) R-355; study (Hicks et al. DiGRA 2018: developers name smooth curves) R-110; spec R-206 |
| M-32 Punch flash too dim or too long | No punch at onset | Frame-step the first 5 frames | Brightest layer 1-2 frames; full-size burst about 4-5 frames; whole flash stack 2-3 frames (all: fps not stated). LoL hit frame 0.1 s (stated in seconds) | industry practice (Sirhaian/Riot realtimevfx 2017) R-387; (cEssex 2025) R-344; (Atif 2017) R-388; tier C, 3 publications; (Leroy/Riot via 80 Level 2017) R-312 (C-08) |
| M-33 Effect lingers (main action late; long tail) | Clutters, signals the wrong importance, blocks the next effect | Timeline: when does the main action end or start to dissipate? Count live particles 1 s after the beat | Main action done or dissipating within the first quarter of lifetime (single tier C, C-05, T-19); dissipation "shouldn't stay visible for long" (Jevremovic 2018); cut lingering smoke | industry practice (Hall 2023, single tier C) R-355; (Jevremovic 2018) R-310; (Embark Season 9 2025) R-031; (Riot guide via VFX Apprentice) R-360 |
| M-34 All layers start and end together | Complexity collapses into one mass; no follow-through | Solo each layer; compare onsets and exits | Offset secondary starts (about 2-3 frames, fps not stated); exit order glow, lens flare, sparks, small bits; keep the contact aligned. Lab: crowding drops with about 150 ms separation | industry practice (Atif 2017, tier C) R-388; (Leroy/Riot 2017) R-312; study (Whitney & Levi 2011) R-138 |
| M-35 Smoke outruns the shockwave; smoke too short on big blasts | Physically wrong; no scale | Frame-step big blasts | Shockwave expands far faster than smoke; smoke stays behind it. One reply asks for smoke of at least 5 s, longer off mobile; this conflicts with readability (C-09, T-12) | industry practice (aarku realtimevfx 2021, single tier C) R-363 |
| M-36 Destroyed state shown before the flash | Object vanishes before the blast reads | Frame-step: frame where bricks detach vs flash peak | Detach (server) and flash in the same frame window; swap at flash peak | industry practice (aarku 2021, single tier C) R-363; inference |
| M-37 Hit-stop too long, or on every hit in a crowd | Feels like lag; third parties act during long freezes. One study (n=15-16, one VR sword/bow game): pleasant votes 0.37-0.39 s; pleasant/unpleasant boundary about 0.54-0.55 s | Many-at-once test; compare freeze lengths with that boundary as an outer limit | Cap it; shorten on multi-hit; no freeze for the thrower of a projectile; none in crowds | industry practice (Sakurai, Famitsu col. 490, 2015, fan translation) R-134; study (Tomizawa & Ishikawa GRAPP 2024) R-035; industry practice (Capcom hit-stop column) R-156 |
| M-38 Same hit-stop and shake for every strength | Flattens weight | Light vs heavy side by side | Scale with strength. Guilty Gear Xrd: light 7 f, heavy about 10 f (preprint) vs 11-15 f by attack level (Dustloop, tier D); unresolved, fps not stated (C-02) | preprint (Lin et al. 2022) R-073; tier D (Dustloop) R-431; industry practice (Capcom 8/12/16 F hypothetical example, fps not stated) R-156 |
| M-39 Rapid hits merge into one | In a 30 fps clip, impacts under about 5 frames apart (167 ms) looked like one long impact; under about 8 frames (267 ms) were hard to tell apart | Measure the gap between impact onsets | Give each impact its own flash or particle so each onset stays distinct | industry practice (Song, Game Developer 2005, 30 fps stated) R-144 |
| M-40 Scale-wrong speed (building-size dust at chip speed, or toy chips slowed) | Speed carries scale: fast reads small, slowed reads big. Default Roblox gravity 196.2 studs/s2 vs "realistic" 35 studs/s2, so fall times are 2.37x shorter than at real scale (sqrt of 196.2/35 = 5.6; arithmetic) | Show one break at two dust speeds; ask "toy or building?" (T-13) | Decide scale first: toy chips fast, building dust slower (emitter `TimeScale`) | spec (Roblox units) R-222; industry practice (Animal Logic Ninjago, Cartoon Brew 2017) R-313; tier D, lead only (miniature over-crank rule) R-436; inference |

### 6.6 Composition and camera

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-41 Layers without distinct jobs | Muddy silhouette, more overdraw; redundant feedback can overwhelm. Layer count alone is not the fault: an 18-component explosion read well | Mute each layer; name what information is lost; if nothing, delete it | One primary read; every extra layer gets a named job and a quality tier | study (Hicks et al. 2018) R-110; industry practice (Atif 2017) R-388; inference (ChatGPT 06) |
| M-42 Uniform spherical spawn with a point force | Fake, even look | Frame-step the burst | Clumped cones and several bursts in different directions; a ground blast throws debris in about a 45 degree cone | industry practice (cEssex 2025, single tier C) R-344 |
| M-43 Big, blobby sparks | Read as flames | Zoom a still frame | Few-pixel sparks, leader sparks with secondaries; streaks with `Orientation = VelocityParallel` | industry practice (cEssex 2025, single tier C) R-344; spec R-211 |
| M-44 Windup cue away from the payoff spot | The eye is in the wrong place at the punch | Mark windup and punch positions on one frame | Put the anticipation cue on the payoff location | industry practice (Nguyen GDC 2022: Titanfall titan drop, Destiny super) R-071 |
| M-45 Plain opacity fade on shapes that should break up | Looks like a card being switched off | Watch the tail on light and dark ground | Break the shape up (subdivide, carve, smaller-blob cells); a hard blink-out is the exception when clarity needs it | industry practice (Pixar Turning Red via VFX Voice 2022) R-286; (DreamWorks Bad Guys 2 via befores & afters 2025) R-251; (Hall 2023) R-355 |
| M-46 Camera shake from random offsets per frame | Jitter; breaks under pause and slow motion | Watch the shake at 0.25x | Smoothed noise, one seed per axis; trauma model | industry practice (Eiserloh GDC 2016) R-124 |
| M-47 Translation shake in 3D; shake on everything | Translation moves the view through walls (Eiserloh: "VERY BAD" in 3D); constant shake removes contrast ("Camera shake is like salt") | Third-person test near walls; count shakes per minute | Rotation only in 3D; shake only big events; trauma +0.2 or +0.5 per event, shake = trauma squared or cubed | industry practice (Eiserloh 2016) R-124 |
| M-48 Camera or screen effect hides the next action | Feedback steals control or sight | Aim and move during the effect, do not just watch | Reduce or remove the layer; per-effect off switch (M-88) | industry practice (Xbox XAG 117) R-074; inference |

### 6.7 Clutter

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-49 Too many simultaneous effects | Cluttered backgrounds raised find-the-target time by 28% to 130% (static images, 20 observers per experiment). Attention holds about 3 to 5 items. "There IS such a thing as too many particle effects" (Nguyen 2022) | Spawn 2, 4, 8, 16 effects with one pickup; time the find; score screenshots with a Feature Congestion clutter metric (T-05) | Rank by importance; trim low-rank, ambient and residue first; stagger onsets. PROPOSAL (inference): at most 4 simultaneously relevant effects per player (own action, nearest threat, pickup, one ambient); basis: capacity limits R-139, R-145 (not effect studies); tune by: T-05 | study (Semizer & Rosenholtz 2025) R-029; (Rosenholtz et al. 2007) R-142; (Cowan 2010) R-139; (Cavanagh & Alvarez 2005) R-145; industry practice (Nguyen 2022) R-071 |
| M-50 Other players' effects at full strength | Ally and bystander effects hide the local threat | 8 players act at once: is the local threat still the clearest element? | Tone down others' non-threatening effects on the client, by viewer relation; own effects and threats stay full. WoW 11.2: Everything / Reduced / Essential, only party and raid members' visuals reduced. Marvel Rivals: local Team-Up VFX toggle. Opacity %: no number found (T-06) | industry practice (Blizzard WoW 11.2, 2025) R-028; (Blizzard Watch 2025) R-250; (NetEase Marvel Rivals 2026) R-007, R-008 |
| M-51 Lingering dust or smoke hides pickups, targets and routes | Readability lost | Put a target brick behind the cloud; time until readable (T-12) | Shorter dust; dissipate on a set curve | industry practice (Embark Season 9 2025: lingering smoke cut, Thermal Bore gadget only) R-031; (Embark Season 8 2025) R-030 |
| M-52 Fine texture detail the effect does not need | Busy small detail is noise at gameplay distance | Remove the detail layer at gameplay distance; if the read does not change, delete it | Cut it | industry practice (Riot 2022) R-060 |
| M-53 Ambient effects as saturated as combat effects | Combat colours lose meaning | Saturation histogram: ambient vs combat | Keep strong colour for weapons and abilities | industry practice (Avalanche 2019) R-300 |
| M-54 Pickups lost under debris and effects | The collect loop fails | Stand in a blast cloud: can the tester point at the nearest pickup? | Pickups above effects in value; `Highlight` (AlwaysOnTop) within the 255 cap; create once, change properties | industry practice (Nguyen 2022: Destiny motes) R-071; spec (255 Highlights; first up to 1 ms GPU on mobile) R-196 |

### 6.8 Repetition

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-55 Identical playback every trigger | Repeats are noticed. Neural response fell from 3.4 to 2.5 on the second showing of a face image (plateau modelled near the 4th repeat; transfer to VFX is inference) | Fire the effect 100 times at 1 per second; note when it reads as a repeat (T-17) | Vary decorative axes: Rotation [0, 360], size, lifetime range, per-particle framerate range, random start for loops, asset variants per layer. Sound practice: about 10 variants for the most frequent sounds; 5 per layer gives 125 combinations. VFX variant count: no number found | study (Rangarajan et al. 2020) R-094; industry practice (Keith/Partikel realtimevfx 2017) R-386; (Jacobsen 2018, sound, single tier C) R-383; spec R-211 |
| M-56 Randomisation changes the message | Variants imply other reach, power, direction or team. Random variety gave enjoyment +.11 only and no curiosity gain | Compare the extremes of each random range | Randomise ornament only. Lock footprint, contact time, team colour, power rank. Variety is against repetition, not a reward | study (Kao 2024) R-043; inference |
| M-57 No cap or cooldown on frequent effects; budget set per single copy | Many copies at once overload the frame | Count worst-case concurrent copies per effect | Budget from the maximum concurrent copies; priority tiers (essential, supporting, environment) dropped bottom-up under load. Halo 3 had a 256-effect engine limit | industry practice (Stabrov/Azur Games 2026) R-248; (Stavrides/Bungie 2019) R-299; (Bungie GameFest 2008) R-326 |
| M-58 Escalation covers the impact point or is not tied to success | Amplified feedback hid the hit in the study | Highest-tier screenshot: is the impact point visible? | Higher tiers add at the edges, never over the contact; escalate only on real success | study (Kao 2024) R-043 |
| M-59 Full flourish on every-second events (coins, chips) | Long animation on a frequent action drags | Time it; repeat 20 times | Frequent = shorter and subtler: 100 ms feedback, 200-300 ms for a major change, 500 ms is where it drags (UI guidance); reserve standout moments | industry practice (Laubheimer/NN/g 2020, single tier C) R-370; study (Hicks et al. Juicy Audio 2024, 12 interviews) R-044 |

### 6.9 Sound sync

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-60 Sound before picture | Sound-early is detected sooner and annoys more. Broadcast detectability: +45 ms sound early, -125 ms sound late | Record screen and audio on the target phone; measure the offset at the punch frame (T-07) | Schedule on the same frame. PROPOSAL (inference): measured sound 0 to 40 ms after the first visible punch frame, never more than 1 frame (16.7 ms at 60 fps) early (same as 05 P-13); basis: 40 ms game audio delay had no effect (R-070), EBU end-to-end limit 60 ms sound late (R-169), sound-early is detected sooner (R-170: +45 ms is the sound-EARLY detection threshold, -125 ms the sound-late one; R-121, R-061); tune by: T-07 | spec (ITU-R BT.1359, 1998) R-170; spec (EBU R37, 2007) R-169; preprint (Ebenezer 2022) R-061; study (Cecere et al. 2016: d' 1.58 sound-lead vs 0.98) R-121 |
| M-61 Hit sound and hit visual not coherent | Sound coherence is one of 3 strongest impact-feel features (correlational, 16 games). Audio delay 40 ms: no effect; 270 ms: higher tension only (n=24; first-run verifier read the PDF and corrected the 270 ms reading; the gap run only did not re-open it) | Mute and unmute; frame-step transient vs flash | One named sound event per visual landmark; pair sound per material | preprint (Lin et al. 2022) R-073; study (Halbhuber et al. 2022) R-070 |
| M-62 Authored timestamps trusted as output sync | Display and audio paths add different delays per device. Varying delay is worse than a constant one (flow drop with 12 switches, eta2 = .28, n=264) | Code says "same frame" but a capture shows a gap; compare devices | Measure emitted audio and displayed frame on target hardware; keep the delay constant | study (Halbhuber et al. 2022) R-064; inference |
| M-63 Picture needs sound to be understood | Muted and deaf players miss the event | Review muted | The picture alone carries the meaning; sound adds weight | industry practice (XAG 103) R-015; inference |

### 6.10 Flipbook

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-64 Blurry sprite: cell pixels below on-screen pixels | Detail smears at close camera | Phone-resolution capture at the closest typical camera; compare cell px with on-screen px. 1024 sheet: 2x2 = 512 px cells, 4x4 = 256, 8x8 = 128 (arithmetic) | Fewer cells per sheet (4x4 = 16 frames is the common in-game ceiling), or a smaller on-screen size. PROPOSAL (inference): cell px >= on-screen px at the closest typical camera; basis: arithmetic on R-209 layouts, R-338; tune by: T-20 | spec R-209, R-212; industry practice (VinceWee realtimevfx 2016: max 16 frames per sub-UV in game, single tier C) R-394; (VFX Apprentice 2026, tier C-) R-338 |
| M-65 Pixelated or shimmering small sprites | Primary shape turns to shimmer in motion | View at real projected size while moving | Match texture to on-screen size (avoid 512 px or more on tiny particles; use 256 or 128). Roblox flipbooks need 1024 (M-69), so tiny bits use plain textures; coarser silhouettes; drop tertiary detail | industry practice (Snap Lens Studio docs) R-332; spec R-214; inference (ChatGPT 06) |
| M-66 Visible loop seam or pop at wrap | The loop jumps from last cell to first | Watch 3 loops; step around the wrap | `OneShot` for one-shot events; `Loop` only when end matches start; `PingPong` only for reversible motion (an explosion run backward looks wrong); a loop needs a longer source than its target length | spec (ParticleFlipbookMode) R-213; spec (Unity Flipbook Player) R-193; tier D, lead only R-433; inference |
| M-67 Particles pop in or out | Reads as a glitch; Embark fixed debris "pop in and out" to fade | Step the first and last frames of each particle | Fade Transparency at start and end of life; fade debris at despawn | spec R-209; industry practice (Embark update 10.0, 2026) R-011 |
| M-68 Hard line where a sprite cuts into ground or a wall | A straight edge where the card meets geometry | Low camera angle at the contact point | No soft-particle or depth-fade property in the Roblox mirror; use `ZOffset` toward the camera, keep cards off surfaces, fade near contact, ground-aligned cards for ground dust. PROPOSAL (inference): test `ZOffset` -0.5 vs 0 and a 0.1 s fade-in; basis: Unity soft-particle concept R-227, absence in R-211/R-214; tune by: T-11 | spec (Unity soft particles) R-227; spec (Roblox ZOffset) R-211 |
| M-69 Sheet the engine rejects (2048 or 4K sheet from Unreal practice; size not a multiple of the grid) | Flipbook playback is disabled (`NotCompatible`); the effect shows a static texture | After load, read the emitter's flipbook compatibility (`Enum.ParticleFlipbookTextureCompatible`) | Author 1024x1024, an exact multiple of the layout. 2048 is not supported per the docs mirror (C-01, T-18) | spec (playback requires 1024x1024) R-214; spec (exact multiple of layout) R-211; spec (1024 8x8 example) R-209; tier C (2022: square power-of-two 8 to 1024) R-361; tier A, read second-hand (2025 custom layouts) R-025; Unreal context R-344, R-350 |
| M-70 No spacing between cells | Neighbour cells bleed in; mips make it worse | Zoom the edges of a held cell | Transparent spacing around each cell; more for mip filtering | spec R-209; tier C R-361 |
| M-71 `OneShot` with more cells than the lifetime can show | Rate = cells / lifetime: 64 cells over 1.0 s = 64 cells/s against a 60 FPS display, so cells are skipped (arithmetic) | Compute cells / lifetime; compare with display fps (default cap 60) | Fewer cells (4x4) or a longer lifetime | spec R-209, R-213, R-198; inference (arithmetic) |
| M-72 Wrong frame blending | `FlipbookBlendFrames` on held, stepped drawings ghosts the silhouette; off on slow smoke it stutters | Step frames; look for double images | Blend off for stepped or hand-drawn sheets; on for slow organic loops | spec (linear crossfade vs instant swap) R-211; industry practice (R0i3in realtimevfx 2024: sub-UV blend is a crossfade, single tier C) R-347; inference |
| M-73 Random start skips the meaningful onset (empty first cells; contact cell not at contact) | The event starts on random states: skips the windup or jumps to dissipation | Log first meaningful cell and peak cell per asset; compare with the timeline | `FlipbookStartRandom = false` for semantic one-shots; trim empty cells; vary secondary layers instead | spec R-211; inference (ChatGPT 06, 09) |
| M-74 Many unique sheets | Clients disable flipbooks when low on memory (likely older phones): the effect disappears | Count unique sheet ids per scene; test on a low-memory phone | Reuse sheets; fewer unique animated effects; a static fallback that keeps the meaning. 1024x1024 RGBA8 = 4 MiB before mips (arithmetic, not measured Roblox memory) | spec R-209; inference (ChatGPT arithmetic) |
| M-75 Colour baked into a sheet that is tinted | Tint cannot rebuild missing detail | Tint to 3 colours; check detail | Author neutral grey sheets for tinting; grey sheets need `LightEmission` 1 to read as glow | industry practice (Orlowski realtimevfx 2024, single tier C) R-350; spec R-209 |

### 6.11 Performance

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-76 Emission cap used as a budget | 400 particles/s per emitter (100/s on mobile) is a hard cap, not a safe budget; big overlapping sprites spike the GPU | On-device GPU frame time at worst concurrency | Budget by measured visible area, overlap and concurrency; keep `Rate` low; use size, lifetime and flipbook instead | spec R-209; inference (ChatGPT 06) |
| M-77 Large overlapping transparent sprites (overdraw) | GPU cost follows covered pixels x layers; doubling width and height = 4x area. Arm called about 2.5x average overdraw "quite high" for one scene and 10x "definitely too much" | Debug Stats; `Stats.RenderGPUFrameTime` on a low-end phone; sweep emitter count | Fewer, smaller, less overlapping sprites. Epic halved 3 overdraw-heavy emitters and removed most 7+-layer overdraw | spec R-209, R-200, R-207; spec (Epic Niagara docs) R-204; industry practice (Dal Col/Arm 2015, one scene) R-132 |
| M-78 Many emitters and beams; property changes every frame | Emitters batch poorly; community: one draw call each; docs: emitter property changes can hurt a lot | Debug Stats draw-call count with and without the effect | Fewer emitters; bake stable properties into templates. Draw-call budget: docs example 1,000 calls / 1M triangles (illustrative) vs community 500 / 500k (opinion) | spec R-200, R-191; industry practice (MrChickenRocket 2024, single tier C) R-351 |
| M-79 `Emit()` bursts assumed to scale with graphics quality | One community post says `Emit()` ignores the automatic quality reduction; whether the mobile 100/s cap applies: unknown | Emit 200 at Editor Quality Level 1 and 10; count (T-21) | Scale `Emit` counts in code by `SavedQualityLevel` | industry practice (Mystifine 2020, single tier C) R-375; spec R-224 |
| M-80 Pooled effect reused without a full reset | Teleport streaks, stale particles, leftover light | Interrupt and reacquire quickly; inspect the first frame | `Clear()` emitters and trails, reset properties, lights and connections. `Highlight`: create once and change properties (add/remove causes spikes; a disabled one still holds a slot) | spec (Trail, ParticleEmitter Clear) R-237, R-211; spec (Highlight) R-196, R-195; inference (ChatGPT) |
| M-81 Shadow-casting lights on effects | Extra draw calls and triangles | Count shadow-casting lights | `Shadows = false` on effect lights; short `Range` | spec R-200; industry practice (MrChickenRocket 2024, single tier C) R-351 |
| M-82 Physical debris uncapped; effects run where nobody sees them | Frame drops. Control kept active rigid bodies at or under 200 on screen; Embark fixed VFX and sound firing with no player near | Count live bodies and off-screen emitters | Cap bodies; per client, cull or stagger far and off-screen cosmetic spawns | industry practice (Remedy Control via CGWorld 2020) R-295; (Embark Season 8 2025) R-030; (DICE Battlefield 6, 2025) R-021 |
| M-83 Performance judged in the Studio emulator or in short runs | Emulation misses memory, thermal throttling and real frame rates | Check the test log: device, session length | Real low-end phone (low-end = Android under 2 GB); 10-15 min of active play for thermal throttling (T-10) | spec (Test on hardware) R-231; industry practice (Roblox analytics announcement 2024) R-036 |

### 6.12 Accessibility and safety

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-84 More than 3 flashes per second over a large area (chained blasts, auto-fire, pulses, pulsed Bloom or ColorCorrection) | Seizure risk: about 3% of people with epilepsy are photosensitive; 16-25 Hz is the most likely range | Record worst-case footage; count opposing luminance pairs of 10% or more (darker state below 0.80) per second, and their area | 3 flashes/s or fewer, or combined flash area at most 0.006 sr in any 10 degree field. Leading edges 334 ms or more apart at 60 Hz always pass (ITU). Count post-effect pulses as flashes | spec (WCAG 2.2 Understanding SC 2.3.1) R-165; spec (ITU-R BT.1702-3) R-168; industry practice (Epilepsy Society) R-330; inference (post effects) |
| M-85 "25%" read as a whole-screen allowance | WCAG's 25% is of a 10 degree visual field (341x256 px at 1024x768 = 11.1% of that screen, arithmetic); ITU's 25% of screen is a different rule | Check the denominator | Design to the stricter WCAG area; use standards-aware tools | spec R-165, R-168; inference (arithmetic) |
| M-86 Saturated red flash or pulse (low-health vignette) | Red is a separate trigger: WCAG R/(R+G+B) >= 0.8; ITU: any change to or from saturated red | Check colour ratio and pulse rate | No saturated-red full-screen pulse; pair with shape or direction. PROPOSAL (inference): red pulse 1 Hz (tests up to 2 Hz; never above 3 Hz at full contrast; start value: PD-12); basis: margin under the 3/s cap R-165; tune by: T-22 | spec R-165, R-168 |
| M-87 Warning screen or "epilepsy safe" label instead of a fix | Exposure can happen before players change settings | Known failures ship behind a splash screen | Redesign the failing effect; name settings by what they control ("screen flash effects") | industry practice (Game Accessibility Guidelines, tier C, summariser read) R-396; (Xbox XAG 118) R-016 |
| M-88 Shake, blur or flash cannot be turned off | Motion discomfort; Xbox guidance: avoid or allow off; Halo Infinite has per-effect sliders 0-100% | Settings list | Separate controls: shake, flashes, full-screen effects, decoration density | industry practice (Xbox XAG 117) R-074 |
| M-89 Reduced-effects mode deletes warnings | Less decoration also removed essential information | Play reduced mode, muted | Keep footprint, outcome confirmation and pickups; replace flashes with steady shapes | inference (ChatGPT 06); industry practice (WoW keeps own and enemy visuals full) R-028 |
| M-90 One analyser pass, or one isolated effect, treated as proof | Combined output and devices differ; an analyser pass is not a medical guarantee | Only isolated-effect footage tested | Test the composite worst case; record tool, standard and version | industry practice (Harding FPA G2) R-155; (XAG 118) R-016; inference |

### 6.13 Review process

| mistake | why it looks bad | how to spot it | fix | source / evidence |
| --- | --- | --- | --- | --- |
| M-91 Polish before block-in | Expensive shaders hide weak timing and composition | Swap the look for plain grey parts: does it still read? | Block in shapes and timing first; detail after (C-07) | industry practice (Lyndon/SideFX GDC 2018) R-115; (Keyser realtimevfx 2025, tier C) R-340; 2 publications |
| M-92 Raising intensity to fix a flat hit | In one RPG (n=3,018) medium and high juice beat both the lowest and the extreme build; a 2026 preprint found no engagement change from none to high intensity; amplification without success lowered competence | Check readability and success-linking first | Fix truth, readability and timing; then intensity | study (Kao 2020, read in full by ChatGPT) R-101; study (Kao 2024) R-043; preprint (Liang et al. 2026, exploratory n=26) R-005 |
| M-93 A lab or standard number used as a design default | Task, display and population change (0.37 s hit-stop from one VR sword game; ITU speech sync windows). Significance is not size (Kao 2020 partial eta2 .003 to .006 per measure, ChatGPT read) | Each number field shows its source and scope | Keep evidence in evidence fields; project values as PROPOSAL with a test | inference (ChatGPT 06); study R-101 |
| M-94 Vague notes ("make it pop", "it should...") | Not actionable; defensive | Re-read the note: does it name the moment, the symptom and a change? | Use the Output 9.4 format | industry practice (VFX Apprentice 2024, tier C) R-348; (Riot 2022: notes name a specific actionable issue) R-060 |

## Output 8. Effect card template

### 8.1 Rules

| rule | detail |
| --- | --- |
| order | Fields run in the order below: communication job and importance first, review results last, card metadata at the end |
| null | `null` = not chosen yet. Never a production zero |
| numbers | Each number is `{value, ev, basis, tune_by}`. `ev` = study / preprint / industry practice (who, year) R-xxx / spec R-xxx / inference / PROPOSAL (inference) |
| gameplay-owned | `gameplay_truth` values come from the gameplay config and the server. The VFX agent reads them and never invents them |
| design numbers | Every design number is PROPOSAL until the owner confirms (AGENTS.md section 0); list it in `evidence.proposals` |
| links | `reads_wrong_if` uses Output 6 ids; `review_results.notes` uses the Output 9.4 format |

### 8.2 Template

```yaml
# EFFECT CARD v1 (template). null = not chosen. Number = {value, ev, basis, tune_by}.
communication_job:
  what_it_is: null              # the event in plain words: what the player sees happen
  what_it_does: null            # gameplay consequence the viewer must understand (state change, damage, reward)
  how_big: null                 # tier: tiny | normal | big | rare_climax; must match the consequence (M-11)
  must_be_read_in_ms: null      # window the viewer has to understand it; from gameplay, else "no number found"
importance_rating:              # 1-10 per viewer; Riot practice (R-368, single tier C); no mapping to size/brightness/duration exists (C-11)
  player: null                  # local player who caused it
  ally: null                    # other player who is not threatened by it
  enemy_or_threatened: null     # player inside the area or affected by it
  outranks: []                  # effect ids this one must stay above when both are on screen
  yields_to: []                 # effect ids that must stay readable over this one
  rationale: null               # one line: why these ranks
trigger:
  event: null                   # network event / server message that starts it
  authority: null               # server | client_predicted_server_confirms | client_cosmetic
  success_dependent: null       # true = big feedback only on a confirmed outcome (R-043)
  cancel_or_interrupt: null     # what stops it early and which cleanup runs
  max_rate_per_s: null          # how often one player can fire it (gameplay config)
gameplay_truth:
  area_shape: null              # sphere | box | cone | line, exactly as the server query
  area_size_studs: null         # from gameplay config; VFX never sets it
  origin: null                  # world anchor: attachment, contact point, surface normal
  telegraph_start_ms: null      # t = 0 is the trigger; first warning frame
  contact_ms: null              # frame the gameplay result happens (damage, break)
  active_end_ms: null           # last moment the area is active or dangerous (M-05)
  hitbox_match_check: null      # how the overlay test is done and its result (Output 9 step R2)
  footprint_locked_across_variants: true   # same area in every quality and viewer variant (R-060)
feeling_target:
  words: []                     # 2-3 feeling words
  style_reference: null         # reference clip or still, with date
  reads_wrong_if: []            # Output 6 ids that describe failure for this effect
layers:                         # one entry per part; every layer has a distinct job (M-41)
  - name: null                  # L1, L2 ... referenced by review notes
    role: null                  # primary | secondary | tertiary
    job: null                   # information this layer carries; delete the layer if none
    phase: null                 # windup | crescendo | punch | follow_through | dissipation
    roblox_part: null           # ParticleEmitter | Beam | Trail | PointLight | SpotLight | Highlight | Decal | MeshPart | camera
    asset_id: null              # rbxassetid of texture or sheet
    flipbook:                   # null when not a flipbook
      sheet_px: null            # 1024 (R-214: playback requires 1024x1024; C-01)
      layout: null              # Grid2x2 | Grid4x4 | Grid8x8 | Custom (FlipbookSizeX/Y)
      mode: null                # OneShot | Loop | PingPong | Random (R-213)
      framerate_fps: null       # NumberRange, max 30; ignored by OneShot, which uses Lifetime / cells (R-209)
      start_random: null        # false for semantic one-shots (M-73)
      blend_frames: null        # false = stepped drawings, true = crossfade (M-72)
      first_meaningful_cell: null   # index of first visible cell
      peak_cell: null           # index of the contact or peak cell
    blend_mode: null            # LightEmission 0 = normal, 1 = additive (R-211; M-22)
    light_influence: null       # 0 self-lit, 1 lit by the scene; always set explicitly (M-24)
    colour: null                # ColorSequence keypoints (time 0..1 -> RGB)
    transparency: null          # NumberSequence; fade in and out (M-67)
    size_studs: null            # NumberSequence or NumberRange
    lifetime_s: null            # NumberRange; capped at 20 s (R-209)
    count: null                 # Emit(n) for bursts, or Rate per s (cap 400, 100 on mobile; R-209)
    speed_studs_s: null         # NumberRange
    emission_shape: null        # Shape, ShapeStyle, cone/spread, orientation of the emitter
    start_offset_ms: null       # delay after contact_ms (negative = before)
    z_offset_studs: null        # render order: flash over fireball over dust (R-211)
    orientation: null           # FacingCamera | FacingCameraWorldUp | VelocityParallel | VelocityPerpendicular
    randomise: null             # decorative axes and ranges only; never footprint, contact, team, power (M-56)
    min_quality_tier: null      # lowest quality tier that keeps this layer
phase_timing:                   # ms from trigger; each value is a number object
  windup_ms: null               # warning or anticipation before the build
  crescendo_ms: null            # build right before the punch; 0 for instant events (M-04)
  punch_ms: null                # brightest moment, on contact_ms
  follow_through_ms: null       # mass and secondary motion after the punch
  dissipation_ms: null          # breakup and fade until clean (M-33)
  fps_note: null                # frames from a source + its stated fps, else "fps not stated"; our timebase
camera_screen:
  shake: null                   # trauma model {add, exponent, decay_per_s, max_rotation_deg, falloff}; rotation only in 3D (R-124)
  hit_stop_ms: null             # freeze length and what freezes (emitter TimeScale, animation); no global time scale
  screen_flash: null            # full-screen flash: frames, area, WCAG rate check (R-165)
  fov_kick_deg: null            # Camera.FieldOfView change; clamped 1-120, default 70 (R-182)
  post_effects: null            # Bloom / ColorCorrection on Camera (local) or Lighting (all); never pulsed (M-84)
  applies_to: null              # self | players_in_falloff | all
sound_sync:
  sound_events: []              # sound ids, one per visual landmark
  visual_landmark: null         # frame the main sound locks to (usually punch)
  offset_ms: null               # planned offset; sound never more than 1 frame before picture (M-60)
  measured_offset_ms: null      # from a phone capture (T-07)
repetition_plan:
  expected_rate: null           # triggers per minute in normal play
  variants: null                # asset variants per layer
  random_ranges: null           # decorative ranges (rotation, size, lifetime, loop start)
  semantic_invariants: []       # what never varies
  concurrency_cap: null         # max live copies and what happens to extras (merge, drop layers, cull)
  escalation: null              # growth with combo or tier; tied to success, never over the contact (M-58)
viewer_variants:
  self: null                    # full version
  others_not_threatened: null   # reduced (WoW model, R-028)
  threatened_or_inside_area: null   # full threat information
  offscreen_or_far: null        # cull or simplify; distance threshold measured, not guessed
reduced_effects_variant:
  keeps: []                     # essential information kept (footprint, contact, outcome, pickups)
  drops: []                     # optional layers removed
  replaces: []                  # e.g. flash -> steady shape, shake -> none (M-89)
performance_budget:
  target_device: null           # low-end phone model, OS, quality level
  max_live_particles: null      # peak alive across all layers
  emitters: null                # emitter + beam count (about 1 draw call each; R-351 single tier C)
  unique_textures: null         # count and sizes
  lights: null                  # count; shadows off
  concurrency_tested: null      # copies at once in the test
  measured_gpu_ms_delta: null   # RenderGPUFrameTime with vs without, worst case
  pool_reset: []                # fields reset on reuse (M-80)
review_results:                 # filled by Output 9; null = not run
  truth: null                   # pass | fail + note id
  communication_importance: null
  visibility_clutter: null
  theme_polish: null
  safety: null
  performance: null
  notes: []                     # Output 9.4 notes
evidence:
  source_ids: []                # R-xxx used on this card
  proposals: []                 # field paths still PROPOSAL (owner has not confirmed)
card_meta:
  id: null                      # stable id, e.g. vfx.c4.heavy.brick_wall
  version: null                 # bump on every change
  status: null                  # draft | in_review | owner_confirmed
```

### 8.3 Worked example: heavy C4 breaking a brick wall

Timed-fuse variant; t = 0 is "charge armed". A remote-trigger variant drops L2 and the fuse windup. Gameplay owns radius and fuse; the card reads them.

```yaml
communication_job:
  what_it_is: "Heavy C4 the player stuck on a brick wall detonates."
  what_it_does: "Server breaks every connected brick inside the blast sphere; the wall gets a hole; loose bricks fall and become collectable."
  how_big: big                  # rare, player-caused, below the stage-climax tier
  must_be_read_in_ms: {value: null, ev: "no number found", note: "hole and loose bricks must be readable when L8 clears (T-12)"}
importance_rating:
  player: {value: 8, ev: "PROPOSAL (inference)", basis: "own rare heavy tool; 9-10 kept for stage-climax events (hierarchy R-080; top tier reserved R-372)", tune_by: "T-02"}
  ally: {value: 4, ev: "PROPOSAL (inference)", basis: "others' non-threatening effects are toned down (R-028)", tune_by: "T-06"}
  enemy_or_threatened: {value: 8, ev: "PROPOSAL (inference)", basis: "anyone inside the area needs full threat information (R-028, R-071)", tune_by: "T-06"}
  outranks: [ambient_dust, brick_chip_small, pickup_sparkle]
  yields_to: [stage_climax_event, low_health_warning]
  rationale: "Strongest player tool on a stage; the hole and the reward bricks are the outcome."
trigger:
  event: "C4Detonated {charge_id, position, normal, radius, broken_brick_ids}"   # name illustrative; gameplay owns the schema
  authority: server             # server decides the break; clients draw (AGENTS.md server authority)
  success_dependent: true       # punch layers only when broken_brick_ids is not empty (R-043)
  cancel_or_interrupt: "charge removed before detonation: stop L1-L3, play no punch, Clear() emitters"
  max_rate_per_s: {value: null, ev: "gameplay config (gear table)"}
gameplay_truth:
  area_shape: sphere
  area_size_studs: {value: null, ev: "gameplay config", note: "read from the C4 gear table"}
  origin: "charge attachment on the wall face; normal = wall normal"
  telegraph_start_ms: 0
  contact_ms: {value: 1500, ev: "PROPOSAL (inference)", basis: "fuse is a game-design setting; anticipation 0.5-2 s set by design (industry practice, Jevremovic/Nordeus 2018, R-310); above lab visual reaction 213-231 ms (study, R-130)", tune_by: "T-01"}
  active_end_ms: {value: 1500, ev: "inference", note: "instant blast; no lingering hazard (M-05)"}
  hitbox_match_check: "debug sphere of area_size_studs at contact; L1 edge, L4 edge and L6 stop line sit on it"
  footprint_locked_across_variants: true
feeling_target:
  words: [sudden, heavy, satisfying]
  style_reference: "toy-brick world: chunky brick-coloured debris, little gritty smoke (industry practice, Animal Logic LEGO Movie 2014 R-135, LEGO Movie 2 2019 R-303)"
  reads_wrong_if: [M-01, M-03, M-09, M-32, M-36, M-51, M-54]
layers:
  - name: L1_area_ring
    role: primary
    job: "shows exactly which bricks will break, from arming to contact"
    phase: windup
    roblox_part: "flat ring MeshPart on the wall face (or Decal), radius = area_size_studs"
    colour: {value: "project 'danger' category colour", ev: "inference (one colour per category, R-033)"}
    transparency: {value: "fill 0.8, outline 0.2", ev: "PROPOSAL (inference)", basis: "outline carries the edge, light fill keeps bricks visible; clear outline matters more as targets grow (R-336, single tier C)", tune_by: "T-03"}
    size_studs: {value: "= area_size_studs", ev: "industry practice (Riot 2022, R-060): indicator equals hitbox"}
    lifetime_s: {value: "0 to contact_ms", ev: "inference"}
    pattern: "dashed outline so colour is not the only signal (R-015, R-398)"
    min_quality_tier: lowest
  - name: L2_fuse_blink
    role: secondary
    job: "armed state and time left"
    phase: windup -> crescendo
    roblox_part: "Neon light strip on the charge + PointLight (Shadows false)"
    blink_rate: {value: "1 Hz armed, 2 Hz in the last 2 s, 3 Hz in the last 1 s (02a schedule; with the card's 1500 ms fuse the 1 Hz step is skipped)", ev: "PROPOSAL (inference)", basis: "start value PD-13 (02a schedule, longer warning); at most 3 flashes/s (spec, WCAG R-165); faster pulse reads more urgent (industry practice, VFX Apprentice 2025, single tier C, R-346; Nguyen 2022 citing Love, R-071)", tune_by: "T-04"}
    light_shadows: {value: false, ev: "spec R-200; industry practice R-351"}
    min_quality_tier: lowest
  - name: L3_inward_squash
    role: tertiary
    job: "pre-punch tell: the charge pulls inward just before the blast"
    phase: crescendo
    roblox_part: "charge mesh scale tween (client)"
    start_offset_ms: {value: -33, ev: "PROPOSAL (inference)", basis: "1-2 frame inward bulge before the blast (industry practice, Trumpler realtimevfx 2020, single tier C, R-380; fps not stated); 2 frames at our 60 FPS cap (R-198)", tune_by: "T-08"}
    scale: {value: 0.85, ev: "PROPOSAL (inference)", basis: "no number found", tune_by: "T-08"}
    min_quality_tier: lowest
  - name: L4_flash_core
    role: primary
    job: "the punch: brightest pixel on screen at contact"
    phase: punch
    roblox_part: "ParticleEmitter (Enabled false; Emit on event)"
    flipbook: null
    blend_mode: {value: "LightEmission 1", ev: "spec R-211"}
    light_influence: {value: 0, ev: "spec R-211"}
    colour: {value: "near-white warm (1.00, 0.96, 0.86)", ev: "PROPOSAL (inference)", basis: "100% white kept for top-tier events (industry practice, Beardilocks/Riot 2020, R-372)", tune_by: "T-02"}
    size_studs: {value: "diameter 0.8 x blast diameter", ev: "PROPOSAL (inference)", basis: "flash covers the object (aarku 2021, single tier C, R-363) but never overstates the area (R-060, R-080)", tune_by: "Output 9 step R2"}
    lifetime_s: {value: 0.05, ev: "PROPOSAL (inference)", basis: "brightest layer 1-2 frames (Sirhaian 2017 R-387; cEssex 2025 R-344; fps not stated); LoL hit frame 0.1 s (Leroy 2017, R-312); start value PD-01: flash sprite Lifetime 0.05-0.1 s including its fade, brightest peak 2 f@60 = 33 ms; this card builds the low end, 0.05 s", tune_by: "T-09"}
    count: {value: "Emit(1)", ev: "inference"}
    start_offset_ms: 0
    z_offset_studs: {value: 1.0, ev: "PROPOSAL (inference)", basis: "flash renders over L5 and L8 (ZOffset order, spec R-211)", tune_by: "visual check"}
    min_quality_tier: lowest
  - name: L5a_fireball
    role: primary
    job: "hot mass leaving the wall along its normal"
    phase: punch -> follow_through
    roblox_part: "ParticleEmitter (Enabled false; Emit on event)"
    flipbook: {sheet_px: {value: 1024, ev: "spec R-214"}, layout: Grid4x4, mode: OneShot, framerate_fps: "ignored by OneShot (spec R-209)", start_random: false, blend_frames: false, first_meaningful_cell: 0, peak_cell: {value: 3, ev: "PROPOSAL (inference)", basis: "full size in about 4-5 frames (R-387, fps not stated)", tune_by: "asset inspection"}}
    blend_mode: {value: "LightEmission 1", ev: "spec R-211; additive only for luminous mass (R-399, single tier C)"}
    light_influence: 0
    colour: {value: "white-hot 0.0 -> orange 0.3 -> dark grey-brown 1.0", ev: "PROPOSAL (inference)", basis: "common ramp; no named source gives values (research gap)", tune_by: "T-02 greyscale rank"}
    transparency: {value: "0 at 0.0, 0 at 0.6, 1 at 1.0", ev: "PROPOSAL (inference)", basis: "fade at end of life (spec R-209)", tune_by: "visual"}
    size_studs: {value: "0.4 -> 0.7 x blast radius over life", ev: "PROPOSAL (inference)", basis: "mass stays inside the area (R-060)", tune_by: "Output 9 step R2"}
    lifetime_s: {value: "0.45-0.55", ev: "PROPOSAL (inference)", basis: "stylised explosion expected life 0.5 s (Atif 2017, single tier C, R-388); randomise fireball lifetime (R-344)", tune_by: "T-09"}
    count: {value: "Emit(1)", ev: "inference"}
    emission_shape: "cone along the wall normal, not a sphere (cEssex 2025, single tier C, R-344)"
    start_offset_ms: 0
    z_offset_studs: {value: 0.5, ev: "PROPOSAL (inference)", basis: "below L4, above L8 (spec R-211)", tune_by: "visual check"}
    min_quality_tier: lowest
  - name: L5b_outward_puffs
    role: secondary
    job: "2-3 smaller sprites that carry the burst outward after the first sprite"
    phase: follow_through
    roblox_part: "ParticleEmitter, same sheet as L5a"
    count: {value: "Emit(3)", ev: "industry practice (Lyndon GDC 2018, R-115: 2-3 smaller outward sprites after the first)"}
    start_offset_ms: {value: 33, ev: "PROPOSAL (inference)", basis: "emitter starts offset about 2-3 frames (Atif 2017, R-388, fps not stated); 2 frames at 60 FPS", tune_by: "T-09"}
    speed_studs_s: {value: "8-14", ev: "PROPOSAL (inference)", basis: "no number found; puffs must stop inside the area (R-060)", tune_by: "Output 9 step R2"}
    size_studs: {value: "0.5 x L5a size", ev: "PROPOSAL (inference)", basis: "smaller than the first sprite (R-115)", tune_by: "visual"}
    lifetime_s: {value: "0.4-0.6", ev: "PROPOSAL (inference)", basis: "close to L5a (R-388)", tune_by: "T-09"}
    min_quality_tier: medium
  - name: L6_dust_ring
    role: secondary
    job: "shows radius and weight; its stop line is the area edge"
    phase: follow_through
    roblox_part: "ParticleEmitter, Shape Disc, ShapeStyle Surface, facing the wall normal"
    flipbook: {sheet_px: 1024, layout: Grid4x4, mode: OneShot, start_random: false, blend_frames: true}   # shares the dust sheet with L8 (reuse, spec R-209)
    blend_mode: {value: "LightEmission 0", ev: "spec R-211"}
    light_influence: 1
    colour: {value: "struck brick colour mixed toward neutral grey", ev: "PROPOSAL (inference)", basis: "effects stay in the brick palette (industry practice, Animal Logic, R-303); tint rule is inference", tune_by: "visual on 3 stages"}
    lifetime_s: {value: "0.6-0.9", ev: "PROPOSAL (inference)", basis: "shockwave expands far faster than smoke (aarku 2021, single tier C, R-363)", tune_by: "T-09"}
    speed_and_drag: "tuned so the ring stops at area_size_studs (truth, R-060); record the values"
    count: {value: "Emit(24)", ev: "PROPOSAL (inference)", basis: "no number found", tune_by: "T-10"}
    min_quality_tier: lowest
  - name: L7_brick_chips
    role: secondary
    job: "small brick-coloured bits: material and direction; NOT the collectable bricks (those are server physics)"
    phase: follow_through
    roblox_part: ParticleEmitter
    flipbook: {sheet_px: 1024, layout: Grid4x4, mode: Loop, framerate_fps: 0, start_random: true}   # random static silhouette per particle (spec R-211); silhouettes instead of polygon debris (PlatinumGames 2023, R-056)
    blend_mode: "LightEmission 0"
    light_influence: 1
    colour: {value: "struck brick colour", ev: "inference (data from the break event)"}
    size_studs: {value: "0.3-0.6", ev: "PROPOSAL (inference)", basis: "chips smaller than one brick", tune_by: "visual"}
    lifetime_s: {value: "0.6-1.0", ev: "PROPOSAL (inference)", basis: "fade before landing piles form (M-67)", tune_by: "T-10"}
    speed_studs_s: {value: "20-40", ev: "spec tutorial example (Roblox spark burst, R-189), not design evidence"}
    drag: {value: 10, ev: "spec tutorial example (R-189), not design evidence"}
    acceleration: {value: "workspace gravity, 196.2 studs/s2 downward", ev: "spec R-222"}
    emission_shape: "cone of about 45 degrees around the wall normal (cEssex 2025, single tier C, R-344)"
    count: {value: "Emit(16)", ev: "PROPOSAL (inference)", basis: "mobile studios cut burst counts hard (Azur Games 2026, R-248: smoke + sparks 200 -> 50)", tune_by: "T-10"}
    min_quality_tier: lowest   # half count at lowest
  - name: L8_dust_cloud
    role: tertiary
    job: "weight and aftermath; clears the hole first"
    phase: dissipation
    roblox_part: ParticleEmitter
    flipbook: {sheet_px: 1024, layout: Grid4x4, mode: OneShot, start_random: false, blend_frames: true}
    blend_mode: "LightEmission 0"
    light_influence: 1
    colour: {value: "brick colour toward grey; lighter top, darker base", ev: "PROPOSAL (inference)", basis: "smoke brighter on top, darker below (cEssex 2025, single tier C, R-344)", tune_by: "visual on 3 stages"}
    size_studs: {value: "0.5 -> 1.0 x blast radius over life", ev: "PROPOSAL (inference)", basis: "no number found", tune_by: "T-12"}
    lifetime_s: {value: "2.0-3.0", ev: "PROPOSAL (inference)", basis: "start value PD-16 (impact dust 1.5-3 s, see-through by 2 s); C-09: at least 5 s asked for big blasts (R-363, single tier C) vs cut lingering smoke for readability (R-031) on mobile", tune_by: "T-12"}
    time_scale: {value: 0.6, ev: "PROPOSAL (inference)", basis: "start value PD-17 (owner decides toy vs big, X-55); speed carries scale (R-313; R-436 tier D, lead only; gravity arithmetic R-222)", tune_by: "T-13"}
    count: {value: "Emit(6)", ev: "PROPOSAL (inference)", basis: "few large puffs beat many small ones on mobile (R-248)", tune_by: "T-10"}
    start_offset_ms: {value: 50, ev: "PROPOSAL (inference)", basis: "secondary starts offset 2-3 frames (R-388, fps not stated); 'a breath' before embers (bgolus 2025, single tier C, R-339)", tune_by: "T-09"}
    emission_shape: "spawned behind the L6 ring front, never ahead of it (R-363)"
    transparency: {value: "fade in over 0.1 of life, fade out from 0.5", ev: "PROPOSAL (inference)", basis: "no pop in or out (M-67, R-209)", tune_by: "visual"}
    min_quality_tier: medium   # 3 puffs at lowest
  - name: L9_blast_light
    role: secondary
    job: "lights nearby bricks briefly so the blast sits in the world"
    phase: punch
    roblox_part: "PointLight on the charge attachment"
    colour: {value: "desaturated warm white", ev: "industry practice (cEssex 2025, single tier C, R-344): light not orange-saturated"}
    range_studs: {value: "2.5 x L5a radius", ev: "PROPOSAL (inference)", basis: "light radius 2-3x the fireball (cEssex 2025, single tier C, R-344); start value PD-21: Range 2-3x the fireball radius inside the 120-stud clamp, this card picks 2.5x", tune_by: "visual"}
    brightness: {value: "8 -> 0", ev: "PROPOSAL (inference)", basis: "no number found", tune_by: "visual on dark stage"}
    timing: {value: "hold 2 frames, fade to 0 by 150 ms", ev: "PROPOSAL (inference)", basis: "light 1-2 frames (R-344, fps not stated); hit frame 0.1 s (R-312); start value PD-21: hold 2 frames, fade at most 0.3 s, this card picks 150 ms", tune_by: "T-09"}
    shadows: {value: false, ev: "spec R-200; industry practice R-351"}
    min_quality_tier: medium
  - name: L10_scorch
    role: tertiary
    job: "history: marks the bricks around the hole"
    phase: dissipation
    roblox_part: "Decal on surviving bricks at the hole rim (client)"
    persistence_s: {value: "until the structure regenerates, then fade 0.5 s; at most 30 live scorch decals per client, oldest fades first", ev: "PROPOSAL (inference)", basis: "start value PD-18; persistent surface damage (industry practice, Battlefield Labs 2025, R-019); no duration found", tune_by: "T-12"}
    min_quality_tier: high
phase_timing:                   # ms from arming
  windup_ms: {value: "0-1100", ev: "PROPOSAL (inference)", basis: "contact_ms minus crescendo", tune_by: "T-01"}
  crescendo_ms: {value: "1100-1500 (400 ms)", ev: "PROPOSAL (inference)", basis: "a crescendo gives time to react (VFX Apprentice 2025, single tier C, R-346); no duration found", tune_by: "T-08"}
  punch_ms: {value: "1500-1550 (L4); L5a full size by about 1550-1580", ev: "PROPOSAL (inference)", basis: "see L4, L5a", tune_by: "T-09"}
  follow_through_ms: {value: "1550-2050", ev: "PROPOSAL (inference)", basis: "stylised explosion life 0.5 s (R-388, single tier C)", tune_by: "T-09"}
  dissipation_ms: {value: "2050-4550", ev: "PROPOSAL (inference)", basis: "L8 starts 1550 ms (1500 + 50) and lives 2.0-3.0 s, ends by 4550; C-09", tune_by: "T-12"}
  fps_note: "Frame counts from R-380, R-387, R-344, R-388 have no stated fps. Conversions use the 60 FPS default client cap (spec R-198): 1 frame = 16.7 ms. A 30 fps phone shows half the frames."
camera_screen:
  shake:
    model: "trauma (industry practice, Eiserloh GDC 2016, R-124)"
    add: {value: 0.5, ev: "industry practice R-124 (+0.2 or +0.5 per event)"}
    exponent: {value: 3, ev: "industry practice R-124 (0.30/0.60/0.90 -> 3/22/73% matches a cube)"}
    decay_per_s: {value: 1.0, ev: "PROPOSAL (inference)", basis: "start value PD-03 (same as 07 P15); the Bevy 2D example 0.5/s (R-397, single tier C) gives a 1 s tail and is a test level, not the default", tune_by: "T-14"}
    signal: "smoothed noise, one seed per axis (R-124)"
    axes: "rotation only (3D, R-124)"
    max_rotation_deg: {value: 3, ev: "PROPOSAL (inference)", basis: "Bevy 2D example 10 degrees max roll (R-397, single tier C), reduced for third-person phone comfort (XAG 117, R-074)", tune_by: "T-14"}
    falloff: {value: "linear to 0 at 3 x area_size_studs from the camera", ev: "PROPOSAL (inference)", basis: "shake scales with camera distance (Sakurai 2015, R-134)", tune_by: "T-14"}
    delay_far: {value: "distance / shock-front speed for far viewers", ev: "industry practice (aarku 2021, single tier C, R-363)"}
  hit_stop_ms: {value: 0, ev: "PROPOSAL (inference)", basis: "start value PD-02: 0 ms for explosions and charges; no explosion hit-stop evidence; nearest: Celeste explosion-launch freeze 0.1 s (first-party code, platformer, R-154); long freezes feel like lag (R-134); Roblox has only per-emitter TimeScale, no global time scale (spec R-211; inference)", tune_by: "T-15"}
  screen_flash: {value: none, ev: "inference: local L4 + L9 instead of a full-screen flash; nothing to count against WCAG (R-165)"}
  fov_kick_deg: {value: "up to -4 in at most 0.15 s; off under reduced motion", ev: "PROPOSAL (inference)", basis: "start value PD-04: FOV kick only for rating >=8 (this card is 8), at most 4 degrees in at most 0.15 s; no named source gives FOV-kick degrees", tune_by: "T-16"}
  post_effects: {value: none, ev: "inference: never pulse Bloom or ColorCorrection (R-165, R-219)"}
  applies_to: players_in_falloff
sound_sync:
  sound_events: ["c4_fuse_beep: one per L2 blink", "c4_detonate: sharp transient + low end", "brick_clack: per landing, from physics"]
  visual_landmark: "first frame of L4 = contact_ms"
  offset_ms: {value: 0, ev: "inference from R-170, R-061, R-121: same frame, sound never more than 1 frame early (start value: PD-14)"}
  allowed_drift_ms: {value: "sound 0 to 40 ms late, at most 1 frame early (same as 05 P-13)", ev: "PROPOSAL (inference)", basis: "40 ms game audio delay no effect (R-070); EBU end-to-end 60 ms sound late (R-169); R-170 +45 ms is the sound-early detection threshold", tune_by: "T-07"}
  low_end: "heavy bass on c4_detonate (industry practice, Godzilla Minus One via nippon.com 2024, tier B-, R-264)"
  measured_offset_ms: null
repetition_plan:
  expected_rate: {value: null, ev: "gameplay config (C4 per stage)"}
  variants: {value: "1 fireball sheet, 1 dust sheet (L6 + L8), 1 chip sheet; variety from rotation, size, lifetime", ev: "inference: reuse sheets to save memory (spec R-209)"}
  random_ranges:
    rotation_deg: {value: "[0, 360]", ev: "spec R-211 (engine range)"}
    size_spread: {value: "+-15%", ev: "PROPOSAL (inference)", basis: "no sourced range exists (research gap)", tune_by: "T-17"}
  semantic_invariants: [area_size_studs, contact_ms, L4 colour, L1 colour and pattern, layer onset order]
  concurrency_cap: {value: "4 full-detail C4 blasts per client; more play the primary layers only (L1, L4, L5a) (start value: PD-10)", ev: "PROPOSAL (inference)", basis: "priority tiers dropped bottom-up under load (Bungie 2019, R-299); budget from max concurrent copies (Azur Games 2026, R-248)", tune_by: "T-10"}
  escalation: {value: "chained blasts keep their own centre and onset; if onsets are under about 167 ms apart, drop secondary layers instead of delaying a punch", ev: "PROPOSAL (inference)", basis: "hits under 5 frames apart at 30 fps merge (Song 2005, R-144); crowding drops with about 150 ms separation (R-138); truth wins over spacing (R-060)", tune_by: "T-05"}
viewer_variants:
  self: full
  others_not_threatened: {value: "L7 and L8 at LocalTransparencyModifier 0.5; no shake, flash or post effect from others; a count cut (x0.7) is optional (start value: PD-08)", ev: "PROPOSAL (inference)", basis: "WoW 11.2 reduces only others' visuals (R-028); no % found", tune_by: "T-06"}
  threatened_or_inside_area: full
  offscreen_or_far: {value: "skip L5b-L10 when off-screen; distance threshold null", ev: "inference (R-030); threshold measured in T-10"}
reduced_effects_variant:
  keeps: [L1, L4 without L9, L5a, L6, "L7 at half count"]
  drops: [L3, L5b, L9, L10, shake]
  replaces: ["L2 blink -> steady glow + ring fill countdown (XAG 117/118, R-074, R-016)", "L8 lifetime x0.5"]
performance_budget:
  target_device: {value: "low-end Android (< 2 GB class) at Editor Quality Level 1 and Automatic", ev: "industry practice (Roblox 2024, R-036); spec R-209"}
  max_live_particles: {value: 51, ev: "arithmetic of the PROPOSAL counts (1 + 1 + 3 + 24 + 16 + 6)"}
  emitters: {value: "start value PD-10: at most 5 at High, at most 3 at Low (drop chips, puffs, lingering tails); the layers above list 6 (L4, L5a, L5b, L6, L7, L8), so one layer must be merged or dropped before build (open: which one)", ev: "count of L4, L5a, L5b, L6, L7, L8 = 6; about 1 draw call each (R-351, single tier C)"}
  unique_textures: {value: "3 sheets at 1024x1024 + 1 core texture + ring texture", ev: "spec R-214; 1024x1024 RGBA8 = 4 MiB before mips (arithmetic, not measured)"}
  lights: {value: "1 during the blast (L9; start value PD-10); L2 is the armed glow before the blast; Shadows false", ev: "spec R-200"}
  concurrency_tested: null
  measured_gpu_ms_delta: null
  pool_reset: ["ParticleEmitter:Clear()", "Enabled = false", "TimeScale = 1", "PointLight Brightness = 0, Enabled = false", "ring Transparency = 1", "disconnect event connections"]
review_results:                 # not run yet
  truth: null
  communication_importance: null
  visibility_clutter: null
  theme_polish: null
  safety: null
  performance: null
  notes: []
evidence:
  source_ids: [R-015, R-016, R-019, R-028, R-030, R-031, R-033, R-036, R-043, R-056, R-060, R-061, R-071, R-074, R-080, R-115, R-121, R-124, R-130, R-134, R-135, R-138, R-144, R-154, R-165, R-169, R-170, R-189, R-198, R-200, R-209, R-211, R-214, R-219, R-222, R-248, R-264, R-299, R-303, R-310, R-312, R-313, R-336, R-339, R-344, R-346, R-351, R-363, R-372, R-380, R-387, R-388, R-397, R-398, R-399, R-436]
  proposals: [importance_rating.*, gameplay_truth.contact_ms, layers.*.PROPOSAL fields, phase_timing.*, camera_screen.shake.max_rotation_deg, camera_screen.shake.falloff, camera_screen.hit_stop_ms, camera_screen.fov_kick_deg, sound_sync.allowed_drift_ms, repetition_plan.size_spread, repetition_plan.concurrency_cap, repetition_plan.escalation, viewer_variants.others_not_threatened]
card_meta:
  id: vfx.c4.heavy.brick_wall
  version: 1
  status: draft                 # all PROPOSAL values wait for tests and owner confirmation
```

## Output 9. Review checklist (Part 12)

### 9.1 Review method (run in this order; pass and fail per step)

| step | what to do (Roblox) | pass | fail -> fix | source / evidence |
| --- | --- | --- | --- | --- |
| R0 Card | Fill communication job, importance per viewer, gameplay truth; ask "what is this effect for?" | No null in those blocks | Get gameplay facts before any art work | industry practice (Keyser via 80 Level 2022) R-283; (Beardilocks 2020) R-368; inference |
| R1 Block-in first | Build with plain grey shapes, no glow, no detail textures, real timing; record at 60 fps | Primary silhouette and phase order read without polish; retiming changes the read as expected | Retime the core or swap to a coarser asset (M-91) | industry practice (Lyndon/SideFX GDC 2018) R-115; (Keyser 2025, tier C) R-340; (VFX Apprentice timing workshop 2025) R-345 |
| R2 Truth overlay | Debug shape of the server area at contact and active end; check self, ally, threatened and every quality tier | Edges coincide; visual contact = server contact; nothing hazard-coloured after active end | M-01 to M-10 (rank 1) | industry practice (Riot 2022) R-060; (Riot 2021) R-080 |
| R3 Frame by frame | Step the capture frame by frame; step a reference clip the same way and log per-element timing | No pop, no reversal, contact cell on the contact frame, punch present in the first 5 frames | Change one responsible parameter, then replay at 1x (M-03, M-32, M-36, M-67, M-73) | industry practice (cEssex 2025) R-344; (aarku 2021) R-363; tier C; inference |
| R4 Slow playback | Set `TimeScale` 0.25 on all emitters (spec 0..1) or play the capture at 0.25x; solo each layer | Windup, crescendo, punch, follow-through, dissipation each deliberate and in order; layer onsets staggered | Retime the core phase; re-check at 1x (slow playback does not prove feel) | spec R-211; industry practice (Spellsouls thread replies 2017, tier C) R-390; inference (ChatGPT 09) |
| R5 Black-and-white value check | `ColorCorrectionEffect.Saturation = -1` on Camera; capture at punch and mid-dissipation on each stage | Focus is the highest-contrast patch; effect separates from the stage; footprint edge readable | Value fix (M-13, M-19, M-20) | spec R-184; industry practice (Beardilocks 2020) R-367; (Keyser 2025: grey block-ins expose timing and composition) R-340; no studio names this exact step (inference) |
| R6 Squint test | `BlurEffect.Size` on Camera, raised until fine detail is gone (record the value) | One defined shape still reads | One dominant shape; cut detail (M-12, M-41, M-52) | spec R-181; industry practice (cEssex 2025 blur test, single tier C) R-344 |
| R7 Phone small-screen check | Real phone at the intended camera distance; Editor Quality Level lowest and highest; emulator only for layout | Identity and footprint read at real size and at lowest quality | Coarser variant; cell size check (M-16, M-64, M-65, M-74) | spec R-209; spec (Test on hardware) R-231 |
| R8 Many at once | Worst plausible concurrency with pickups, other players and UI (T-05, T-10) | Local threat and nearest pickup still found; frame time inside the project budget | Trim low-rank layers, residue, simultaneous onsets (M-49 to M-54, M-57) | industry practice (Riot guide via VFX Apprentice: short effects leave room) R-360; (Nguyen 2022) R-071; inference |
| R9 Bright and dark stages | Brightest, most saturated and darkest stage; also inside dust | No background erases the primary; `LightInfluence` correct | M-21 to M-24, M-28 | industry practice (Avalanche 2019) R-300; (Hall 2023, single tier C) R-355 |
| R10 Sound off, then on | Muted: picture alone carries the meaning. Unmuted: measure transient vs punch on a phone capture | Muted read passes; sound not before picture | Split readability fault from sync fault (M-60 to M-63) | industry practice (XAG 103) R-015; preprint R-073; spec R-170 |
| R11 Repetition run | 100 triggers at 1 per second with a saved seed (T-17) | Meaning never changes; repeat not obvious to the owner | Vary decorative axes only (M-55, M-56) | industry practice (realtimevfx 2017, tier C) R-386; inference |
| R12 Comfort and safety | Reduced-effects mode on; count flashes and area on worst-case composite footage; shake off | Essential information kept; 3 flashes/s or fewer, or WCAG area pass | Block release until fixed (M-84 to M-90) | spec R-165, R-168; industry practice (XAG 117) R-074 |
| R13 Performance | Low-end phone, worst concurrency, 10-15 min active play; set the budget before the test | Project budget met through the whole session | Optimisation order: keep footprint and onset; cut overlap and tails first (M-76 to M-83) | spec R-231, R-200, R-198 |
| R14 Record | Before/after with the same seed, camera, competing effects; log capture fps and display fps | Comparable evidence on the card | Re-capture | inference (ChatGPT 09 step 14); industry practice (VFX Apprentice 2024) R-348 |

### 9.2 Ranked fix order

| rank | fix area | gate before moving on | Output 6 ids | source / evidence |
| --- | --- | --- | --- | --- |
| 1 | Truth of area and timing | R2 and R3 pass: edges match, visual contact = server contact, no lingering hazard, telegraph above the reaction floor | M-01 to M-10 | industry practice (Riot 2022: hitbox indicator correction first) R-060 |
| 2 | Communicates the right thing at the right importance | Viewers name event and consequence; importance rank = prominence rank; miss, hit and big hit distinct | M-11 to M-18 | industry practice R-080, R-368; study R-043 |
| 3 | Visibility, clutter, brightness | R5 to R9 pass | M-19 to M-30, M-49 to M-54 | industry practice (Riot 2022: readability, noise, brightness second) R-060 |
| 4 | Theme and polish | Theme does not break ranks 1-3 (re-run R2, R5, R8) | rest | industry practice (Riot 2022: theme third) R-060 |
| gate | Safety and performance | Block release at any rank | M-76 to M-90 | inference (ChatGPT 09 intro) |

Riot's published order has 3 tiers (gameplay accuracy; readability, noise, brightness; theme). Splitting rank 2 from rank 3 follows the brief. Both inputs say this split is not Riot's wording (inference).

### 9.3 Release gate (all must pass)

| check | pass condition | step |
| --- | --- | --- |
| truth | footprint and contact match in every variant | R2 |
| importance | prominence order = importance order on the card | R0, R8 |
| readability | greyscale, squint, phone, bright/dark all pass | R5-R7, R9 |
| sound | muted read passes; measured offset inside the card value | R10 |
| safety | flash count and area pass on the composite; reduced mode keeps essentials | R12 |
| performance | project budget met on the low-end phone for 10-15 min | R13 |
| owner | PROPOSAL values listed in `evidence.proposals`; owner confirmation recorded in `decisions.md` before they lose the label | AGENTS.md section 0 |

### 9.4 Practitioner feedback format

One note = one moment, one symptom, one concrete change. Fields, in order:

| field | content |
| --- | --- |
| rank | 1 truth, 2 communication, 3 visibility, 4 theme (9.2) |
| moment | phase + time or frame + viewer (self, ally, threatened) |
| symptom | what is seen, with the Output 6 id |
| probable cause | layer and property believed responsible |
| change | `layer.property: from -> to`, or "raise/lower until <test> passes (record value)" |
| protects | what must not change (footprint, contact, colour meaning) |
| retest | Output 9 step id |

Rules:
- Numbered list, highest rank first; the builder replies with what changed and a new capture (industry practice, cEssex realtimevfx 2025, R-344, tier C).
- Name a solution direction, not "should"; the builder chooses the final fix (industry practice, VFX Apprentice 2024, R-348, tier C).
- Polish one phase at a time: change one phase, replay at 1x, then move on (inference; R-348: start with one item you can act on).
- Feedback names a specific, actionable issue (industry practice, Riot 2022, R-060).

Example, on the 8.3 card:

| # | rank | moment | symptom | probable cause | change | protects | retest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | punch, t = 1500 ms, frames 0-12, self view | M-01: L6 dust ring stops past the debug sphere; bricks outside the ring stay intact | L6 speed too high for its drag | Raise L6 drag until the stop line sits on `area_size_studs` (record the value) | L4 timing, L1 size | R2 |
| 2 | 1 | punch, frames 0-3, self view | M-03: L4 peaks some frames after the detonate transient (count them in the capture) | built L4 start offset differs from the card | L4 `start_offset_ms`: built value -> 0 (card value); re-measure | sound event, L5a timing | R3, R10 |
| 3 | 3 | dissipation, t = 2050-4550 ms, ally view | M-51 / M-09: L8 hides the hole and the loose bricks for the whole tail | L8 lifetime too long for this stage | L8 `lifetime_s`: 2.0-3.0 -> 1.0-1.5 (halve), then run T-12 | L6 and L7 unchanged | R8, R9 |

Work order: note 1, re-shoot; note 2, re-shoot; then note 3.

## Conflicts

| id | topic | value A (source) | value B (source) | preferred and why |
| --- | --- | --- | --- | --- |
| C-01 | Roblox flipbook sheet size (issue f) | a 64-frame 4K sheet called standard (cEssex 2025, R-344, one critic's opinion); 9x9 at 2048 (realtimevfx 2024, R-350); Unreal context | Docs mirror (read 2026-10-12): "Flipbook playback requires a 1024x1024 texture", else `NotCompatible` (R-214); texture "exact multiple of the flipbook layout size" (R-211); guide example 1024 8x8 (R-209); no 2048 anywhere in the mirror | SETTLED: author 1024x1024; 2048 not supported. UNRESOLVED: whether smaller or non-square sheets play. R-361 (tier C, 2022) allows square power-of-two 8 to 1024; R-025 (tier A, 2025 beta, read second-hand by ChatGPT only) allows custom 1-64 per axis without square/power-of-two. R-214 says 1024 only. Test T-18 |
| C-02 | Guilty Gear Xrd hit-stop (issue b) | light 7 f, heavy about 10 f (Lin et al. 2022 preprint, R-073; fps not stated) | 11-15 f by attack level Lv0-4; counter-hit victim 11/14/17/22/27 f (Dustloop, tier D, R-431; data source not stated; first column of a wider table) | UNRESOLVED. Shown both with tiers; may measure different things. No ms conversion. Related: Capcom 8/12/16 F hypothetical (R-156); Tomizawa & Ishikawa 2024 (R-035) pleasant 0.37-0.39 s, boundary about 0.54-0.55 s, n=15-16, one game (issue h). SmashWiki formula (R-442, tier D) not used; not confirmed as Sakurai's (issue e) |
| C-03 | Indicator size vs hitbox | match (Riot 2022 R-060, 2021 R-080, PBE 2020 R-374; both models) | some games draw enemy indicators larger, player indicators smaller (VFX Apprentice 2026, R-336, single tier C, descriptive) | Match: tier A, first-hand. Offset only by owner decision |
| C-04 | Value extremes | avoid 0% and 100% value and saturation (Riot guide 2017, R-120, read by ChatGPT from an unofficial mirror; Claude via summary R-360) | focus takes highest and lowest value and highest saturation (Beardilocks 2020, R-367); 100% white for ultimates (R-372); faint desaturated effects failed in Sparkball (Hall 2023, R-355; ChatGPT AUD-07) | Reconciled (inference, both models): mid-value base, extremes only for the focus of top-tier events; context decides |
| C-05 | "Main action within the first quarter of lifetime" | Hall 2023 (R-355): both models read the same page = 1 publication; wording allows dissipation to begin by then | Claude gap run found no such wording on R-346 (a different page); ChatGPT excludes it from defaults | Single tier C. Used only as a review heuristic (M-33); test T-19 |
| C-06 | "FX aren't supposed to be telling the story" (issue c) | VFX Apprentice tip 10 (R-360, 2022, tier C), framed as from the 2017 guide | Not found in Riot text read: Claude could not open R-120; ChatGPT read R-120 and reported no such line | VFX Apprentice summary, single tier C; not a Riot quote; not used as a rule here |
| C-07 | Block-in as a named step | Claude first run: no source names block-in (p2-p12 6a) | Lyndon GDC 2018 slides (R-115, tier A, full read by ChatGPT); Keyser 2025 block-ins post (R-340, tier C) | ChatGPT: direct full reads. Block-in first = industry practice, 2 publications |
| C-08 | Punch flash length | brightest layer 1-2 frames (Sirhaian 2017, R-387; cEssex 2025, R-344) | flash stack 2-3 frames (Atif 2017, R-388); LoL hit frame 0.1 s (Leroy 2017, R-312) | Not a contradiction: different layers. Frames have no stated fps. Test T-09 |
| C-09 | Smoke and dust duration | at least 5 s for big blasts, longer off mobile (aarku 2021, R-363, single tier C) | keep effects short; lingering smoke cut for visibility (Embark 2025, R-031, tier A, one gadget only; Jevremovic 2018, R-310; Riot guide via R-360) | Short, for gameplay readability (tier A + B + C, newer). Long smoke only where nothing must be read through it. Example uses PROPOSAL 2-3 s; test T-12 |
| C-10 | Audio-visual sync tolerance | broadcast speech: detect +45 / -125 ms (ITU 1998, R-170); EBU end-to-end +40 / -60 ms (R-169) | non-speech sports tolerate far more (Ebenezer 2022 preprint, R-061); game: 40 ms no effect, 270 ms tension (R-070); action JND 143 ms high-causality (Li et al. 2021, R-078) | Not a plug-in budget (both models). Rule: same frame, sound 0 to 40 ms late and never more than 1 frame early (start value: PD-14), measure on device (T-07) |
| C-11 | 1-10 importance rating (issue i) | exact scale from one source (Beardilocks 2020, R-368, tier C, first-hand Riot artist) | hierarchy corroborated (Riot 2021 R-080, 2022 R-060); ChatGPT AUD-10 agrees | No source maps rating to size, brightness or duration. The card stores ranks; mapping is a project test (T-02) |
| C-12 | Kao 2020 lowest condition | "low" (CHI 2024 text, R-043) | "None" build (ChatGPT full read of R-101: None and Extreme both lost on playtime; enjoyment: Extreme below Medium/High) | ChatGPT full read preferred. Safe wording: medium and high beat the lowest and the extreme build |
| C-13 | Draw-call budget | docs example 1,000 calls / 1M triangles (R-191; illustrative per ChatGPT RBC27) | community 500 / 500k (MrChickenRocket 2024, R-351, single tier C) | Neither is a budget; measure on the target phone (T-10) |
| C-14 | Ally effect toning | shipped settings give structure only (WoW 11.2 R-028; Marvel Rivals R-007, R-008); no opacity % | Claude inference grid 100/70/40/0% | No number found; start value LocalTransparencyModifier 0.5 (PD-08), optional count cut x0.7 is PROPOSAL; test T-06 |
| C-15 | Known issues not used here | Tai 2024 frame claims and quote (issue a): dropped; CHI 2024 10.8% playtime (issue d, ChatGPT AUD-01): not adopted; Pokerogue timings (issue g): out of scope | n/a | Applied |

## Open / test ourselves

Test grids come from the research test plans (inference). Results become card values only after owner review.

| id | question | test | metric |
| --- | --- | --- | --- |
| T-01 | Fuse / telegraph length | Dodge-or-step-away harness, telegraph 400, 600, 800, 1200 ms; 30 fps phone and PC | hit or escape rate; owner "fair" rating |
| T-02 | Importance to prominence | Rate every effect 1-10; measure screen coverage %, peak value, lifetime; check monotonic order | order match; "which was bigger" playtest |
| T-03 | Danger ring style | Fill + outline vs outline only; red vs orange; 3 stage palettes; dashed pattern on | time to spot, misreads |
| T-04 | Fuse blink urgency | Blink 1, 2, 3 Hz final rate; owner rates urgency; flash count check | urgency rating; WCAG pass |
| T-05 | Clutter set size | 2, 4, 8, 16 concurrent effects with one pickup; Feature Congestion score on screenshots | find time, misses, metric vs human |
| T-06 | Others' effect toning | Ally effects at 100, 70, 40, 0% alpha (and saturation); threats pinned at 100% | time to spot own threat and pickup; comfort |
| T-07 | Sound offset | Sound at -3, 0, +3 frames at 60 fps vs the flash; phone speaker and headphones; screen + audio capture | "snappy" vs "off"; measured offset |
| T-08 | Crescendo and micro-tell | Crescendo 0, 150, 300, 500 ms; inward squash 0, 1, 2 frames at 60 and 30 fps | "tense" vs "slow"; "heavy" rating |
| T-09 | Punch length | White core 1, 2, 6 frames; fireball life 0.3, 0.5, 0.8 s | "punch" rating; flash count |
| T-10 | Concurrency cost | 1, 5, 20 simultaneous C4 blasts on a low-end phone; Editor Quality Level 1 vs 10; 10-15 min session | RenderGPUFrameTime, live particles, flipbook drop-out |
| T-11 | Soft edges at contact | ZOffset -0.5 vs 0; 0.1 s transparency fade-in; ground-aligned card | visible line in low-angle screenshots |
| T-12 | Dust lifetime vs readability | Dust life 4 steps up to the 20 s cap; target brick behind the cloud | time until readable; "heavy" rating |
| T-13 | Scale by speed | Dust TimeScale 1.0, 0.6, 0.4 (bodies at real speed) | "toy" vs "building" answers |
| T-14 | Shake strength | Max rotation 1, 3, 6 degrees; trauma +0.5, cube; phone; 10 blasts | impact rating; comfort; aim error |
| T-15 | Hit-stop on blasts | Freeze L4/L5a TimeScale 0, 50, 100, 150 ms | weight rating; "lag" reports |
| T-16 | FOV kick | 2, 4, 8 degrees over 80-150 ms | impact vs comfort |
| T-17 | Repetition | 100 triggers at 1/s; 1, 3, 6 variants; size and tint spread 0, 10, 25% | trigger where owner sees a repeat; legibility |
| T-18 | Flipbook sheet compatibility (C-01) | Upload 512x512, 1024x1024, 2048x2048 and a non-square Custom sheet; read `ParticleFlipbookTextureCompatible` | Compatible / NotCompatible per size |
| T-19 | Lifetime fraction of the main action (C-05) | Peak at 10, 25, 40% of lifetime on one blast | "punch" and clutter rating |
| T-20 | Cell size vs on-screen size | 1024 sheet at 8x8 (128 px), 4x4 (256), 2x2 (512); effect 2, 6, 12 studs at 10, 30, 60 studs; phone screenshots | cell px / screen px where blur appears |
| T-21 | Emit vs quality | Emit(200) at quality 1 and 10; phone | live particle count |
| T-22 | Red pulse rate | Low-health pulse 0.5, 1, 1.5, 2 Hz with opacity under 40% | comfort; WCAG flash and red checks |

No number found (do not fill without a test): impact-frame length in frames from a maker; FOV-kick degrees; ally opacity %; VFX variant counts and random ranges; effect screen-coverage budget; effect-to-scene brightness ratio in stops; collapse phase timings; Roblox audio-visual output latency.

## Unregistered sources (resolved 2026-10-13)

Integration: every alias below now resolves to a register row (`00-sources.md`, R-450..R-467) and to a key in `source-aliases.json`; the text above cites the R-ids.

| alias | resolved to | what | where |
| --- | --- | --- | --- |
| UNREG:roblox-docs-Stats | R-461 | Roblox Creator Docs, `Stats` class (`Stats.RenderGPUFrameTime`), spec | `knowledge/external/roblox-creator-docs/_api-reference/classes/Stats.yaml` (local mirror) |

## Check log

Trace check, 2026-10-12, local files only (Claude research files, ChatGPT package, docs mirror, `00-sources.md`). All 137 R-ids resolve in `00-sources.md`; tiers and years in the text match the register.

Fixed in place (9):

| # | where | was | now | evidence |
| --- | --- | --- | --- | --- |
| 1 | M-15 | n=1,699 attached to -.43 and -.19 | Model A n=678 for -.43 / -.19; Model B n=1,699 for +.45 | p5-p6-p7 S1 `[V: confirmed - Model A n=678]`; Model B n=1,699 |
| 2 | M-20 | two tier C sources, no marking | "both tier C, 2 publications" added | register R-367, R-358 |
| 3 | M-40 | "falls are 2.37x faster" | "fall times are 2.37x shorter" (sqrt of 196.2/35); R-436 marked "tier D, lead only" (also in C4 L8 basis) | gap-destruction-feel G17 arithmetic |
| 4 | M-51, C-09 | Embark Season 9 "lingering smoke cut" read as general | scope added: Thermal Bore gadget only | p4-destruction S03 `[V: confirmed ... gadget only]` |
| 5 | M-61 | "n=24" stated as settled | marked "first-run figure, abstract not re-opened, unverified" | gap-juice-studies G13 `[V: unverified]` |
| 6 | M-66 | tier D R-433 listed without limit | "tier D, lead only" | register R-433 |
| 7 | M-92 | Kao 2020 partial eta2 "about .005" | ".003 to .006 per measure" | ChatGPT JS02 (.005, .004, .003, .006, .006, .006) |
| 8 | C-01 | "2048 / 4K sheets standard (cEssex)" | "a 64-frame 4K sheet called standard ... one critic's opinion" | p2-p12 S16 `[V: confirmed ... 64 frames 4K called standard]` |
| 9 | C4 card `phase_timing.dissipation_ms`, note 3 in 9.4 | 2050-4500 ms | 2050-4550 ms (L8 starts 1550 ms and lives up to 3.0 s) | arithmetic of the card's own PROPOSAL values |

Flagged, left as written (3):

| # | where | issue |
| --- | --- | --- |
| F1 | M-61 | Halbhuber 2022 audio-latency figures (40 ms no effect, 270 ms tension, n=24) come from the first run only. The gap run did not open the abstract. Treat as unverified until R-070 is re-read. Integration 2026-10-13: resolved; p5-p6-p7 S9 carries `[V: corrected]` from a PDF read (270 ms raised tension only; positive affect fell only at 500 ms), so the figures are verified; M-61 reworded. |
| F2 | M-87 | R-396 is described as "summariser read". The register says "full". Wording not changed because no input file states how it was read; re-check before relying on it. |
| F3 | Card, PROPOSAL count | The card holds 53 `ev: "PROPOSAL (inference)"` values, not 54. With the 5 in the mistakes table (M-49, M-60, M-64, M-68, M-86) the file has 58, not 59. No content is missing. The writer's count was off by one. |

Checked and confirmed (no change): reaction time 230.8 ms, n=1469, 213 ms; Tomizawa 0.37-0.39 s, 0.537 / 0.55 s, n=16/16/15; Lin and Dustloop GG Xrd values in C-02 (7 f, about 10 f, 11-15 f, counter-hit 11/14/17/22/27 f); Song 5 and 8 frames at 30 fps (167, 267 ms); Whitney and Levi about 150 ms; Cecere d' 1.58 vs 0.98; Halbhuber flow n=264, eta2 .28, 12 switches; ITU +45 / -125 ms, EBU +40 / -60 ms; Li et al. JND 143 ms; WCAG 3 flashes/s, 0.006 sr, 341x256 px (11.1%), 334 ms at 60 Hz, red 0.8; Epilepsy Society 3%, 16-25 Hz; Semizer and Rosenholtz 28% to 130%, 20 observers per experiment; Cowan 3 to 5; Rangarajan 3.4 to 2.5; Kao +.11 enjoyment; Eiserloh +0.2/+0.5, 3/22/73%, "VERY BAD", "salt"; Roblox docs (400/s, 100/s mobile, 20 s lifetime, 30 fps cap, 1024x1024 flipbook rule, exact-multiple rule, LightInfluence defaults, ZOffset, TimeScale 0..1, FOV 1-120 default 70, Bloom Threshold, 255 Highlights, 1 ms mobile, 1,000 calls / 1M triangles, 20 keypoints, spark tutorial speed 20-40, drag 10); Stats.RenderGPUFrameTime exists in the mirror; Arm 2.5x / 10x and Epic three halved emitters; Control 200 bodies; Halo 3 256; Azur Games 200 to 50; Celeste 0.1 s; Leroy 0.1 s; Sirhaian and Atif frame counts and 0.5 s life; NN/g 100 / 200-300 / 500 ms; 12 interviews in Hicks 2024; arithmetic (64 cells/s, 4 MiB, 51 particles, 6 emitters, frame-to-ms conversions at 60 FPS).

Rules checked: quotes are 15 words or fewer and found in the inputs; table headers keep `| mistake | why it looks bad | how to spot it | fix |` in order, with the added trailing column; Tai 2024 and CHI 2024 10.8% appear only as "dropped" in C-15; the "FX aren't supposed to be telling the story" line is attributed to the VFX Apprentice summary, tier C (C-06); the SmashWiki formula (R-442, tier D) is not used and not credited to Sakurai; tier D appears only as labelled lead (Dustloop, R-433, R-436); every PROPOSAL carries basis and test.
