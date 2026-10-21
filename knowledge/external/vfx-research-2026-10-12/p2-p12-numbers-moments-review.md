> Author: researcher (vfx-deep-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# VFX research: Part 2 (moment numbers) and Part 12 (review method)

Scope note: WebSearch budget ran out mid-task (shared 200/turn cap), so several planned lookups were NOT done (Dustloop/SF6/Tekken hitstop tables, Celeste freeze frames, Material 3 site, Apple HIG body text, Hearthstone/Clash Royale/Genshin/Pet Simulator reveal timing, FFXIV/Destiny/WoW telegraph data). They are listed in Gaps. Conversions: 1 frame = 16.7 ms at 60 fps, 33.3 ms at 30 fps (arithmetic, inference). Roblox runs at up to 60 fps (spec-adjacent, not re-checked here).

## 1. Sources read (pages actually opened; fetched text treated as data)

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave us |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Motion: Duration & easing (Material m1) | Google Material | undated (~2018) | A (vendor design system) | https://m1.material.io/motion/duration-easing.html | yes (m1 site). Newer: S02 | Mobile ~300 ms; enter 225; leave 195; full-screen 375; >400 slow; tablet +30%; wearable -30%; desktop 150-200 [V: confirmed, all values re-read] |
| S02 | Material Components Android: Motion.md | Google Material | undated (M3 era) | A/spec (vendor docs) | https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md | no | Duration tokens 50-1000 ms: 50 ms steps up to 600, then 100 ms steps (700-1000, no 650); easing curves; doc inconsistency noted (Long1 450 vs 300) [V: corrected - steps are 50 ms only from 50 to 600, then 100 ms; Long1 450 vs 300 inconsistency not re-checked; page also lists a second default standard easing 0.4,0,0.2,1] |
| S03 | Executing UX Animations: Duration and Motion Characteristics | Page Laubheimer, Nielsen Norman Group | 2020-02-09 | C (practice; source list cites one 2010 attention study, not discussed) [V: corrected - author and date added; 2020 so not pre-2020] | https://www.nngroup.com/articles/animation-duration/ | unknown | 100 ms feedback; 200-300 ms big change; general guidance 100-400 ms, 500 ms is where it drags; exit shorter than enter; frequency shortens [V: corrected - 100-400 ms range, 500 ms is the ceiling] |
| S04 | Response Times: The 3 Important Limits | Jakob Nielsen | 1993 (2014 note) | A (first-hand, book excerpt) | https://www.nngroup.com/articles/response-times-3-important-limits/ | yes; no newer replacement found | 0.1 s instant; 1 s flow; 10 s attention [V: confirmed; excerpt of Usability Engineering ch.5, 1993] |
| S05 | Hitlag (SmashWiki) | community, datamined | live 2026 | D (fan wiki) | https://ssbwiki.com/Hitlag | no | Hitlag formulas per Smash game, caps (30 frames Brawl onward). Use only as lead, cross-read with S06 [V: confirmed; Brawl, Smash 4, Ultimate cap 30; Melee 20; Ultimate formula, shield 0.67x match live page] |
| S06 | Thoughts on Hitstop (Sakurai Famitsu col. 490, fan translation) | Masahiro Sakurai (Nintendo/Sora), tr. Source Gaming | 2015 | A via fan translation (translation fidelity unchecked) | https://sourcegaming.info/2015/11/11/thoughts-on-hitstop-sakurais-famitsu-column-vol-490-1/ | yes; no newer maker source found | Stronger attack = longer hitstop; cap; attacker also shakes; amplitude decays; hurtbox fixed; camera-distance scaling; 4-frame hurt transition [V: confirmed, article gives no total hitstop frame counts; credited to Source Gaming Team, no named translator; Weekly Famitsu vol. 490-491] |
| S07 | Hitstop/hitfreeze/hitlag/hitpause | Celia Wagar (CritPoints) | 2017 | D (blog) | https://critpoints.net/2017/05/17/hitstophitfreezehitlaghitpausehitshit/ | yes | Perceptual rationale; SF2 about 10 frames |
| S08 | Making Game "Feel" (summary of Vlambeer pistol breakdown) | infovore.org summarising Vlambeer/J.W. Nijman | undated (~2013) | D (secondary blog of tier A source) | https://infovore.org/?p=5275 | yes | Nuclear Throne shot sequence with numbers (camera kick 6 px, shake +4, weapon kick 2, freeze 10-20 ms). Needs primary confirm [V: confirmed as quoted by the secondary page (page says milliseconds); primary not checked] |
| S09 | Keys to Combat Design: Anatomy of an Attack | Nicolas Kraj, GDKeys | 2020-04-25 | C | https://gdkeys.com/keys-to-combat-design-1-anatomy-of-an-attack/ | no | Anticipation formula, 0.25 s reaction rule of thumb, Hollow Knight Hornet frame table, input lag target [V: confirmed (2020-04-25, Nicolas Kraj); Hornet table assumes 30 fps; lasso recovery about 1 s, no frame count] |
| S10 | Enemy Attacks and Telegraphing | Mike Stout, Game Developer | 2015-09-02 | B | https://www.gamedeveloper.com/design/enemy-attacks-and-telegraphing | yes | Telegraph channel mix (animation, sound, VFX, VO, force feedback); no numbers |
| S11 | How does enemy attack timing work | Isaiah Everin Cooper (Signals and Light) | 2024 | D | https://signalsandlight.substack.com/p/how-does-enemy-attack-timing-work | no | Nothing usable (no numbers). Read, not cited as proof |
| S12 | 10 Design Tips from the League of Legends VFX Style Guide | VFX Apprentice (summarising Riot 2017 guide) | undated | C | https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips | derived from 2017 guide, so yes | Scale of importance, value/saturation limits, short duration, anticipation quote [V: corrected - blog dated 2022-08-29; the 2017 style guide is by Riot art director Jin Ho Yang; quote attributed to Jason Keyser from a video, text matches] |
| S13 | Feedback: How to Get (and Give) What You Need | VFX Apprentice | undated | C | https://www.vfxapprentice.com/blog/how-to-work-with-feedback | n/a | Feedback etiquette steps |
| S14 | Jason Keyser on in-game VFX | 80 Level (interview with Jason Keyser, ex-Riot) | 2022-11-25 [V: corrected - date added] | B | https://80.lv/articles/jason-keyser-on-in-game-vfx-and-the-demand-for-fx-artists/ | unknown | Define purpose, judge by player experience, PvP restraint, junior mistakes |
| S15 | Video: Applying artistic principles to VFX design for games (GDC 2017 listing) | Game Developer (Chamberlin/Blizzard, Keyser/Riot) | 2017/2019 | B (listing only) | https://gamedeveloper.com/art/video-applying-artistic-principles-to-vfx-design-for-games | yes | Existence of the talk only; no content read |
| S16 | Looking for feedback on Explosion VFX | cEssex (critic) / nadalsm, realtimevfx.com | 2025-08/10 | C (named credited users, long thread) | https://realtimevfx.com/t/looking-for-feedback-on-explosion-vfx/29528 | no | Model critique thread: ordered notes, flash/light/muzzle 1-2 frames, flipbook 64 frames 4K, blur test [V: confirmed 1-2 frames, light radius 2-3x fireball, 64 frames 4K called standard (cEssex, Aug-Sep 2025); one critic's opinion, not a measured standard] |
| S17 | Explosion effect help needed (reply by aarku) | aarku ("Jon"), realtimevfx.com | 2021-02-14 | C | https://realtimevfx.com/t/explosion-effect-help-needed/16021/2 | no | Reference frame-stepping; smoke >= 5 s; mesh swap at flash peak; delayed shake; bloom spike; light [V: confirmed; wording is 'at minimum like 5 seconds', one forum reply, 2021-02-14; bloom spike and light not re-checked] |
| S18 | Stylized Frag Launcher explosion breakdown | Atif, realtimevfx.com | 2017-06-06 | C | https://realtimevfx.com/t/stylized-frag-launcher-explosion-overwatch-inspiration-breakdown-posted/1894?page=2 | yes; S16 is newer | 18 layers; flash 2-3 frames; emitter starts offset 2-3 frames [V: confirmed, posted 2017-06-06 by Atif] |
| S19 | Feedback on my VFX | Travis (reply), realtimevfx.com | 2021-01 | C | https://realtimevfx.com/t/feedback-on-my-vfx/15736 | no | Forum scope (real-time only); shape and origin questions; no numbers |
| S20 | Unite 2017 Realtime VFX of Spellsouls | forum replies (Niels, Bruno, others) | 2017 | C | https://realtimevfx.com/t/unite-2017-realtime-vfx-of-spellsouls-i-would-really-appreciate-your-input/2494 | yes | Slow motion plus element separation as inspection; "reads well"; phone-performance worry |
| S21 | Spider-Man: Into the Spider-Verse tech article | Mike Seymour, fxguide (Danny Dimian quoted) | 2018 | B | https://www.fxguide.com/?p=244678 | yes; no newer found | Mostly on twos (12 img/s); threes "snappy"; no motion blur; hand-drawn smoke/sparks/explosions; on-screen BOOM/POW [V: confirmed except BOOM/POW, not seen; article 2018-12-17] |
| S22 | Riot Games and Fortiche get revolutionary with Arcane S2 | VFX Voice | 2024 | B | https://vfxvoice.com/riot-games-and-fortiche-get-revolutionary-with-arcane-season-2/ | no | Smoke and fire as 2D FX; steam on gauntlets to sell power. No timing |
| S23 | Rare Loot Box Rewards Trigger Larger Arousal and Reward Responses (abstract page) | Larche, Chini, Lee, Dixon, Fernandes (Univ. of Waterloo repository copy) | repository 2019-11-23; cited J Gambling Studies 37(1), 2021 | peer-reviewed journal article, accepted version (abstract only read) [V: corrected - not an undated study; lab experiments with skin conductance and pause measures; abstract supports the summary] | https://uwspace.uwaterloo.ca/items/f3df3e42-ecb1-4cf9-89cf-87626dbfbaf1/full | no | Rarer reward: larger skin conductance and force response, longer post-reinforcement pause, anticipatory arousal before reveal, higher urge |
| S24 | Visual Effects Summit: World of Warcraft VFX Pillars (listing) | Sarah Carmody, Blizzard, GDC 2023 | 2023 | A (listing only) | https://gdcvault.com/play/1029418/Visual-Effects-Summit-World-of | no | Existence only; mentions style guides and VFX hubs |
| S25 | Use particles for explosions (local mirror) | Roblox Creator Docs | mirror | spec | knowledge/external/roblox-creator-docs/tutorials/use-case-tutorials/vfx/use-particles-for-explosions.md | n/a | Spark burst: Lifetime 0.2-0.6 s, Speed 20-40, Drag 10, SpreadAngle 180,180, Emit(100). Engine capability only |

Tier count read [V: unverified - tier A is generous: S01/S02 are vendor design docs, S24 a listing only, S06 a fan translation; only S04 is a clean first-hand source]: A = 4 (S01, S04, S06, S24; S02 spec-like), B = 5 (S10, S14, S15, S21, S22), C = 9 (S03, S09, S12, S13, S16-S20), D = 4 (S05, S07, S08, S11), study = 1 (S23, abstract), spec = 1 (S25). Total 25 opened; roughly 14 yielded usable content, the rest are thin (S11, S15, S19, S20, S24).

Pages that failed or were unusable (NOT cited as read): ToucArcade Hearthstone interview (403), Destructoid Genshin wish piece (403), Motomura Xrd PDF (compressed, unreadable), 3dreference Notion GDC 2017 notes (empty), Riot Nexus style guide post (redirect to homepage), Apple HIG motion (title only), Material 3 site (title only), Springer 2025 loot-box paper (auth redirect), Kao 2019 ToG PDF (over 10 MB), Dustloop GGST (404), Game Developer Art of Screenshake (listing page).

## 2. Findings

### 2a. Moment recipe table
Rule applied: cells hold only what a source gave; "no number found" otherwise; "(inf)" = my reasoning. Evidence key: IP = industry practice, spec, inf.

| moment | feeling | importance rating | communication job | layers | timing per phase (ms or frames) | value and colour | shape and motion | camera and screen effect | sound sync point | what to leave out | examples from film, anime and games | evidence level |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Light hit | snappy contact | low; size/intensity must match attack significance (S12) | "it connected" (inf) | hit spark, victim flinch, tiny freeze | hit-stop: no number found for light moves from a tier A/B source. Smash Ultimate formula gives about 12 frames at 10% damage with all multipliers 1 (S05, tier D, my arithmetic) [V: confirmed, floor(12.5)=12]. Vlambeer pistol: one white frame, two big-eye frames, freeze 10-20 ms (S08, tier D, check unit) | no number found | S08: enemy pushed 3 px/frame; S06: victim vibrates | Vlambeer pistol: camera kick 6 px, shake +4 (S08) | impact sound same instant as freeze start (inf) | repeated freezes in multi-hit crowds (S06: Dynasty Warriors avoids hitstop) | Smash, Nuclear Throne | S06 industry practice (A); S08 D; S05 D |
| Heavy hit | weight, resistance | high | "this was strong" | freeze, bigger flinch, spark, camera | S06: stronger/higher damage = longer hitstop, capped; S05 cap 30 frames Brawl onward, about 25 frames at 30% and capped at 30 at 50% (formula, D) [V: confirmed; d=30 gives 25, d=50 gives 38 so capped; cap reached from about d=37]. SF2 about 10 frames (S07, D). No number found from a tier A maker for exact heavy frames | no number found | S06: attacker vibrates too, amplitude starts large and shrinks over the freeze; vibrate sideways on ground, up/down in air; hurtbox stays fixed | S06: vibration intensity raised when camera is far | no number found | long freezes in crowds slow the game (S06) | Smash Ultimate, Street Fighter II | S06 industry practice (A, 2015, pre-2020); S05, S07 D |
| Critical / final blow | climax | highest in the fight (inf from S12 scale-of-importance) | "fight over" | longer freeze, bigger flash | S06: Final Smash and hammer are why a cap exists (cap applies even then). No other number found | no number found | no number found | no number found | no number found | do not exceed cap; a third party could act in a long freeze (S06 on free-for-alls) | Smash | S06 IP; rest inf |
| Blocked hit | resisted | lower than a clean hit (inf) | "hit was stopped" | no number found | S05: shielded multiplier 0.67x on hitlag (D) [V: confirmed] | no number found | no number found | no number found | no number found | no number found | Smash | S05 D only |
| Small explosion | punchy pop | low-medium | area and moment | instant flash, burst ring/core, sparks, smoke | S18: flash 2-3 frames [V: confirmed], emitter starts offset 2-3 frames, sparks die just after ring. S16: muzzle-flash-style spiky sprite 1-2 frames; real light 1-2 frames [V: confirmed]. S25 spec spark: lifetime 0.2-0.6 s, speed 20-40, drag 10, Emit(100) | S16: HDR-bright start for bloom; light radius 2-3x fireball; desaturated light (not orange-saturated); blackbody 0-3500 K for fire emissive; brown sinking dirt vs grey rising smoke | S16: ground blast pushes debris in about 45 degree cone; spawn clumped cones, not a sphere; fireball stretches when fast; sparks small with leader sparks | S17: small shake delayed by distance to match shockwave speed; bloom strength spike by script | no number found | spherical spawn, huge blobby sparks, high-saturation light (S16); too much scale for grenade-sized blast (S16) | Overwatch-style frag launcher (S18) | S16, S17, S18 IP (tier C, three independent artists, consistent); S25 spec |
| Large / huge explosion | awe, destruction | highest | area of damage, scale | flash, shockwave, fireball, debris, dust, smoke, scorch decal | S17: smoke at least 5 s (longer if not mobile); swap to destroyed mesh at flash peak, not at t=0 [V: confirmed]. S16: lifetime randomisation on fireball sprites; flipbook 64 frames at 4K called industry standard (2K/16 frames acceptable) | S17: flash bright enough to cover the object; S16: top brighter, bottom darker smoke, direction lighting | S17: shockwave must expand much more over same time; smoke must not outpace shockwave; S16: low-frequency shapes first, then high-frequency detail (80/20) | S17: shake + bloom + point light fading with flash | no number found | big noise frequency, too many overlapping sprites (S16) | same | S16, S17 IP (tier C) |
| Chain explosion | cascade | rises per link (inf) | no number found | no number found | no number found | no number found | no number found | no number found | no number found | no number found | no number found | none; gap |
| Delayed charge (C4-style) | tension | medium | "about to blow" | warning light/glow | S16 author replaced a glow "anticipation" sprite with flashes; no timing. No number found | no number found | no number found | no number found | no number found | no number found | no number found | inf |
| Collect / coin / pickup | small reward | low, frequent | "got it" | flash, fly, counter tick | no number found from a named source. Frequency rule: more frequent = shorter, subtler (S03). Feedback up to 100 ms feels immediate (S03, S04 0.1 s). Material short tier 50-200 ms (S02) | no number found | motion toward target; exits shorter than entrances: leave 195 vs enter 225 ms (S01) | none | no number found | long sequences for frequent pickups (S03) | no | S01 spec/IP; S03 C; S04 A |
| Egg / chest reveal | anticipation then payoff | scales with rarity | which tier it is | build-up, flash, reveal | no named-source timing found. Study: rarer rewards produce larger arousal and longer pauses; anticipatory arousal rises before the reveal (S23, abstract, study) | rarity colour ladders: no tier A/B source read (Genshin/Wuthering colours came only from search snippets, not opened) | no number found | no number found | audio raised loot-box opening in Kao 2019 abstract, not read (lead) | no number found | Hearthstone, Genshin, Pet Simulator (all unread) | S23 peer-reviewed journal article, abstract only [V: confirmed, see S23 row]; rest gap |
| Ability: windup / charge | threat build | by power | readable start | glow, anticipation | S12: "lead the brain with anticipation" (Keyser quote) [V: confirmed, 2022 blog]; S09 anticipation = reaction time + trigger time + buffer | S12: higher saturation draws focus, avoid 0% and 100% | S12: blur on moving shapes to show direction and end point | no number found | no number found | contradictory shapes (S12) | LoL | S12 C; S09 C |
| Ability: projectile / muzzle flash | launch | by power | direction | muzzle flash, projectile, trail | S16: muzzle flash 1-2 frames; S08: bullet is a circle on frame 1 (fake muzzle flash) | no number found | S08: shell eject 2-4 px/frame, bullet 16 px/frame (30 fps, 320x240) | S08 camera kick 6 px, shake +4 | S08: sound plays first in the sequence | no number found | Nuclear Throne | S16 C; S08 D |
| Ability: impact / area | landing | by power | area and damage | shockwave | S16: shockwave ring from short spawn window with drag, little velocity | no number found | S16 | S17 | no number found | no number found | no number found | S16 C |
| Warning / telegraph | threat | by lethality | "act now" | anim, sound, VFX, VO | S09: anticipation min = reaction (0.25 s = 8 frames at 30 fps, 15 at 60) + ability trigger + buffer; example 10-frame block gives 18 frames at 30 fps. Hornet at 30 fps: dash 15 f, throw 20 f, lasso 20 f, dive "very long" (S09) [V: confirmed; the 18-frame example has no difficulty buffer, so it is a minimum] | no number found | S10: use several channels (animation, sound, VFX, voice, force feedback), not only cartoon cues | no number found | S10: sound is a primary channel | telegraph that is too fast for the reaction rule (S09) | Hollow Knight | S09 C; S10 B (no numbers) |
| Movement: dash / jump / landing / teleport | agility | low-medium | state change | trail, dust | no number found | no number found | S12: motion blur shows direction | no number found | no number found | no number found | no number found | gap |
| Ambient mood | atmosphere | lowest | tone | low smoke, dust | S17: low lying wispy dust sticks around as a secondary element; no timing | no number found | no number found | none | no number found | competing with gameplay (S12) | no number found | S16/S17 C |
| UI: button press | immediate | low | acknowledge | scale/colour | S03: about 100 ms; S04: 0.1 s feels like direct cause; S02: Short1 50 ms, Short2 100 ms | no number found | S03: ease-out entering, ease-in leaving, not linear | none | no number found | long animation for frequent actions (S03) | no | S03 C; S04 A; S02 spec |
| UI: panel / purchase success | confirmation | medium | "done" | panel, flash | S01 mobile ~300 ms, enter 225, leave 195, full-screen 375, >400 feels slow; S03 200-300 ms, ceiling 500 ms; S02 Medium 250-400 [V: confirmed] | no number found | S02: decelerate when entering, accelerate when exiting | none | no number found | >500 ms (S03) | no | S01, S02, S03 |
| UI: error / notification | alert | by severity (inf) | no number found | no number found | S04: waits over 1 s lose direct feel, over 10 s need progress (applies to waits, not animations) | no number found | no number found | no number found | no number found | no number found | no | gap |

### 2b. Anime and film pacing (supports "timing" choices; hit-stop analogue)
| finding | number | source | evidence |
| --- | --- | --- | --- |
| Spider-Verse animated mostly on twos (12 images/s) with variable holds, threes called "snappy" | 12 img/s; holds of 2 or 3 | S21 | industry practice (2018, tier B); no newer found [V: confirmed; 'snappy' is Danny Dimian's word] |
| No motion blur; stepped repetition ("shifting") suggests motion; frames stay sharp when paused | none | S21 | IP |
| Smoke, sparks, explosions drawn by hand in both Spider-Verse and Arcane | none | S21, S22 | IP |
| Arcane steam added to gauntlets to emphasise power | none | S22 | IP |
| Impact-frame timing for hits in either production | no number found | S21, S22 (checked, not covered) | gap |

### 2c. Timing and interaction constants (UI/feedback)
| constant | value | source | evidence |
| --- | --- | --- | --- |
| Instantaneous feel | 0.1 s | S04 | A, 1993, pre-2020, no newer found [V: confirmed] |
| Flow of thought limit | 1 s | S04 | same |
| Mobile transition | about 300 ms; enter 225; leave 195; full-screen 375; avoid >400 | S01 | spec/IP, pre-2020 |
| Tablet / wearable / desktop | +30% / -30% / 150-200 ms | S01 | same |
| Material token scale | 50-1000 ms; 50 ms steps to 600, then 100 ms steps (Short 50-200, Medium 250-400, Long 450-600, Extra Long 700-1000) | S02 | spec (newer than S01) [V: corrected - step size not uniform; values otherwise confirmed] |
| Easing | standard (0.2,0,0,1); decelerate for entering (0,0,0,1); accelerate for exiting (0.3,0,1,1); emphasized decelerate (0.05,0.7,0.1,1) | S02 | spec |
| UI feedback guideline | 100 ms feedback; 200-300 ms major; <=500 ms ceiling | S03 | tier C practice, 2020 [V: confirmed] |
| Reaction rule | 0.25 s = 8 f at 30 fps, 15 f at 60 fps | S09 | tier C practice (2020) [V: confirmed; rule of thumb, no study cited] |
| Input lag target | under 100 ms for critical actions | S09 | tier C [V: confirmed] |
| Hit freeze, Smash Ultimate | floor((d x 0.65 + 6) x h x e x s), cap 30 f; d=15 gives 15 f | S05 | tier D, datamined; needs maker confirm [V: corrected - full formula also has player-count p and crouch-cancel c terms; simplified form holds for 2 players, no crouch-cancel; d=15 gives 15 confirmed] |

Newer-first note: S01 (older) vs S02 (newer): S02 keeps the 300 ms medium centre but widens range to 50-1000 ms and ties duration to area travelled.

## 3. Quotes used (<=15 words)
| quote | attribution | source |
| --- | --- | --- |
| "Lead the brain with anticipation and then overload the brain in that moment." [V: confirmed, 14 words, source has no final period] | Jason Keyser (via VFX Apprentice) | S12 |
| "pick one that you feel like you can work on and start there" | VFX Apprentice | S13 |
| "the artist has final say" | VFX Apprentice | S13 |
| "what is this effect for?" [V: confirmed, 2022] | Jason Keyser interview (80 Level) | S14 |
| "Timing is critical for each component because most layers are short lived." [V: confirmed] | Atif, realtimevfx | S18 |

## 4. Conflicts between sources (newer first)
| topic | claim A | claim B | resolution |
| --- | --- | --- | --- |
| Mobile UI duration | S01 (older): ~300 ms medium, 150-200 desktop | S02 (newer): 50-1000 ms tokens; doc itself inconsistent (Long1 300 vs 450) | Use S02 token scale as menu; treat 100 ms feedback and 200-300 ms panels as consistent across S01, S02, S03 |
| Reaction time | S09: 0.25 s rule of thumb | search snippet (not opened): averages over 0.3 s; up to 3 s for novices | Not resolved. Playtest on phone; use 0.25 s as floor, not target |
| Hit freeze for Vlambeer | S08: 10-20 ms (under 1 frame at 30 fps) | S05/S07: ~10-25 frames for fighters | Different genres and likely a unit error in S08 (tier D). Do not use S08's ms as a rule |
| Smash hitlag formula | S05 live page | search snippet of older revision with different structure | Use live page only; still tier D |
| Explosion flash length | S18 (2017): 2-3 frames | S16 (2025): 1-2 frames for muzzle flash and light [V: both confirmed] | Newer first: 1-2 frames for the brightest layer, 2-3 frames for the whole flash sprite stack. Both short |

## 5. Gaps and how to test
| question | status | test we can run |
| --- | --- | --- |
| Exact hit-stop frames for light/medium/heavy/final blow in SF6, Tekken, GG, DMC, God of War, Hades | no tier A/B number read (search budget ended) | Capture a few reference clips at 60 fps and count frames; then A/B 2-3 values in Studio at 60 fps with owner on phone |
| Final blow / critical numbers | none | Use S06 cap logic: define the ceiling first, then scale |
| Collect/coin fly-to-counter timing | none from a named source | Test 3 durations (200, 400, 700 ms) with the counter ticking on arrival; check on a 30 fps phone |
| Egg/chest reveal timing and rarity colour ladder | only S23 abstract | Read full S23, Kao 2019 ToG paper (PDF too big for the fetcher), Hearthstone/Genshin footage frame by frame |
| Telegraph lead times from named talks (Destiny, WoW, FFXIV, Elden Ring) | none | Frame-count videos; use S09 formula as start; test with the weakest phone |
| Movement (dash, jump, landing, speed lines, teleport) | none | Same A/B method |
| Ambient mood timing | none | n/a |
| Black-and-white value check as a documented studio step | not found | We define it ourselves (greyscale screenshot, Section 6) |
| Phone small-screen check as a documented step | not found (S20 only mentions phone performance) | Scale test: render at 375x812 emulation or a real phone |
| Sound on/off test | not found in sources | Mute and unmute during review, compare the "feel" note |
| Feedback format on realtimevfx beyond S16 | only S16 is rich | Read more threads (Sketch/WIP) with credited artists next round |

## 6. Review method

### 6a. Steps with sources
| # | step | what to do | source / evidence |
| --- | --- | --- | --- |
| 1 | State purpose | Write what the effect is for, how often it occurs, what it sits next to, and whether it is a climax | S14 (Keyser): IP; S12 scale-of-importance |
| 2 | Block-in first | Review the primary shape and timing before detail; do not polish a wrong read | inf (from S12 tip 1: primary shape reads at a glance); no source names "block-in" directly |
| 3 | Reference | Collect reference and step through it frame by frame, noting timings per element at the right frame rate | S16, S17: IP |
| 4 | Frame-by-frame own effect | Step through the effect; look for sparks not inheriting velocity, texel-density mismatches, spawn offsets | S16 (post 12): IP |
| 5 | Slow playback | Use slow motion and separate elements to see layers | S20 (Niels), S16 (author built a frame-step tool): IP |
| 6 | Scale check | Compare real-world size to effect size (grenade vs massive) | S16: IP |
| 7 | Blur test (squint equivalent) | Blur the effect; defined shapes must still read | S16 (post 14, cEssex): IP |
| 8 | Value check | Check range, avoid extremes; keep mid values as base. Greyscale screenshot check: our own step | S12: IP for value limits; greyscale check is inf |
| 9 | Importance check | Does size/intensity match attack significance and not outshine the ultimate? | S12: IP |
| 10 | In-gameplay read | Judge in real play; competitive/dense scenes need restraint | S12, S14: IP |
| 11 | Many-at-once | Spawn many effects together; short durations to avoid blocking later spells | S12 tip 10: IP; stress test is inf |
| 12 | Bright and dark stages, phone, sound on/off | Repeat on both lighting extremes, phone, with and without sound | not found in sources; inf, listed as our own checks. S14 notes timing is tied to audio and post-processing |
| 13 | Give notes | Prioritised, specific, solution direction not a finished fix; avoid "should"; ask consent | S13 |

### 6b. Ranked fix order (inference, built from S12, S14, S16)
1. Truth of area and timing (does it show where and when the hit/AOE is; reaction rule S09).
2. Communication at the right importance (S12 scale of importance).
3. Visibility, clutter, brightness, value contrast (S12 value; S16 flash/light brightness).
4. Theme, polish, secondary detail (S16 debris, dust, decals come after the core punch).
Evidence level: inference; the ordering itself is not stated by one source.

### 6c. Feedback format seen on realtimevfx.com (S16)
Each critic reply = numbered list, ordered by implied priority; mixes reference request, principle ("12 principles of animation"), scale/size, texture/flipbook specs, per-layer notes, then a closing request for the next progress video. Author replies list what they changed. Forum asks for one continuing thread per person and real-time engine scope (S19). Evidence: industry practice, tier C.

### 6d. Mistakes table
| mistake | why it looks bad | how to spot it | fix |
| --- | --- | --- | --- |
| Effect size/intensity does not match attack importance | weak attack looks like an ultimate (S12) | Compare light and heavy side by side | Rescale per S12 importance ladder |
| Primary shape unclear | player cannot tell the idea of the effect (S12) | Blur test (S16) | Make one dominant shape; secondary elements support by value/saturation |
| Value or saturation at 0% / 100% | blends into environment or UI (S12) | Greyscale and bright/dark stage test | Keep mid values; widen range only for the focus |
| Competing complementary colours | noise (S12) | Squint/blur | One dominant colour, one secondary, desaturate rest |
| Spherical particle spawn with point force | uniform, fake look (S16) | Frame step | Clumped cones, several bursts in different directions |
| Sparks too big/blobby | read as flames, not sparks (S16) | Zoom a still frame | A few pixels, leader sparks with secondary sparks |
| Flash and light too dim or too long | no punch at start (S16, S17) | Frame step first 5 frames | Flash/light 1-2 frames, very bright, bloom spike |
| Smoke outpaces shockwave or ends too early | physically wrong (S17) | Frame step | Smoke behind shockwave; lifetime at least 5 s on non-mobile |
| Mesh swaps at t=0 | object vanishes before the flash (S17) | Frame step | Swap at flash peak |
| Over-complicated flipbook | muddy; hard to layer (S14) | Blur test | Simple flipbook plus supporting GPU particles / shaders |
| Too many overlapping sprites, high noise frequency | muddy read (S16) | Blur test | Low-frequency shapes first, then detail (80/20) |
| Scorch/decal too burn-like, light too orange and saturated | cheap look (S16) | Review in lit scene | Spikier dark mark, desaturated light colour |
| No clear purpose or style target | team members drift (S14) | Ask "what is this effect for?" | Write purpose and style descriptors first |
| Telegraph shorter than reaction rule | unfair hit (S09) | Count frames: anticipation < reaction + trigger + buffer | Lengthen anticipation, add sound/VFX channel (S10) |
| Hit freeze too long in crowds | game feels slow (S06) | Many-at-once test | Shorter freeze, cap, or none for projectiles/crowds |
| Animation too long for frequent action | feels like a drag (S03) | Time it; repeat 20 times | Cut to 100-300 ms; frequency shortens duration |
| Notes too vague or "should" statements | not actionable, defensive (S13) | Re-read note | Specific, prioritised, solution direction |

## 7. Leads not followed (tier D / unread)
- Search snippets claiming hit-pause ranges 2-3 / 4-6 / 8-10 frames (mocaponline "Animation Polish & Game Feel Guide"), tier D, not opened.
- Search snippet: "initial burst not longer than 1 frame (max 2); full-size explosion 4-5 frames" from realtimevfx Overwatch-inspired explosion thread 1767/6, not opened (tier C candidate, worth reading next).
- Kao 2019 "Infinite Loot Box" IEEE ToG: abstract says high audio effects raised boxes opened; visual effects not significant; PDF too large for fetcher.
- bugnet.io pages on hit pause and telegraphs: tier D.
- dev.to "The reward moment is the product": tier D (spark 80 ms, coin fountain +80 ms, number +140 ms, unverified).
- Uhiyama-lab, wayline.io, gamineai.com game-feel primers: tier D.
- Hearthstone pack opening via ToucArcade (Ben Thompson, 2017): page blocked (403).
- Destructoid Genshin wish animation article: page blocked (403).
- Motomura GDC 2015 Xrd talk (Arc System Works): PDF unreadable by fetcher; GDC Vault 1022031 not opened.
- Sakurai YouTube eight hit-stop tips: video, not read.
- GDC 2017 Chamberlin/Keyser talk and Notion notes: video/notes unreadable; Riot LoL VFX Style Guide original post redirected.
- Dustloop, Frame data sites for SF6/Tekken/GGST hitstop tables: Dustloop URL 404; others not opened.

## Verification log
> Verifier: adversarial fact-check · claude-sonnet-5-5 · default · 2026-10-12. Cited URLs re-opened with WebFetch (a small model summarises each page, so wording is as returned by it).

Checked (15 sources, about 30 claims): S01, S02, S03, S04, S05, S06, S08, S09, S12, S14, S16, S17, S18, S21, S23. Not re-opened (unverified): S07, S10, S11, S13, S15, S19, S20, S22, S24, S25 and the blocked leads in sections 1 and 7.

Claims proved false and removed: none. Every headline number matched its source; the faults were in metadata and wording.

| item | was | now |
| --- | --- | --- |
| S23 | "undated, recent", plain "study" | Larche et al., J Gambling Studies 37(1), 2021; peer-reviewed accepted version; abstract only read |
| S03 | undated; "100-500 range" | Laubheimer, 2020-02-09 (not pre-2020); guidance 100-400 ms, 500 ms is the drag ceiling |
| S02 | "50 ms steps" across 50-1000 | 50 ms steps to 600, then 100 ms steps (no 650) |
| S12 | undated | blog 2022-08-29, derived from Riot's Oct 2017 style guide by Jin Ho Yang |
| S14 | undated | 2022-11-25 |
| S05 formula row | simplified formula | full formula adds player-count and crouch-cancel terms |
| S06 | "fan translation" | credited to Source Gaming Team, no named translator |

Weak but kept, with tags:
- Tier A is generous. S01 and S02 are vendor design docs, S24 is a listing only, S06 is a fan translation. Only S04 (Nielsen 1993) is clean first-hand.
- S08 freeze of 10-20 ms comes from a secondary blog, primary not read. Do not use as a rule.
- Explosion frame counts (S16, S17, S18) are tier C forum posts by individuals. They agree with each other but none is a studio source. "64 frames at 4K is standard" is one critic's claim.
- S09 0.25 s reaction time is a rule of thumb; use it as a floor.
- S23 is a lab loot-box task read from its abstract. It cannot set reveal durations.

Gaps and missing tier A sources:
- No hitstop frame data by move class from fighting-game primaries (Dustloop, SF6 and Tekken frame data, Motomura GDC 2015 on Guilty Gear Xrd). These would replace the tier D Smash wiki numbers.
- Jan Willem Nijman's "Art of Screenshake" talk (primary for S08) not read.
- Riot's original LoL VFX style guide and the GDC 2017 Chamberlin/Keyser talk not read.
- No source for Roblox mobile particle budgets or 30 fps device behaviour.
- Reveal timing (Hearthstone, Genshin, Pet Simulator): no named-source number exists in this file; the summary's statement is accurate.
