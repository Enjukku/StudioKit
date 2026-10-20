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

# VFX reference: index and evidence rules

**Scope and use.** Entry point of the VFX reference: what it is for, the evidence rules every file follows, which file to load for which job, the highest-confidence rules, and where the evidence came from. Load this file first, then only the files the job needs (file map below).

## Purpose

The evidence base for the future VFX designer agent. That agent does not paint new art: it picks, combines (kitbashes), times, places, colours, scales and tunes existing flipbooks and Roblox parts (ParticleEmitter, Beam, Trail, lights, Highlight, decals, post effects, camera), and it reviews effects with a fixed checklist. Every rule here says what a source shows, how strong that source is, and what we still have to test ourselves. Design numbers stay proposals until the owner confirms them (AGENTS.md §0); confirmed values go to `knowledge/design/decisions.md`.

## Evidence rules

| rule | meaning |
| --- | --- |
| source ids | every number and claim cites an R-id from `00-sources.md` (467 sources; aliases from both research runs in `source-aliases.json`) |
| tiers | A = makers and peer-reviewed studies (preprints tagged); spec = engine and standards docs (Roblox local docs mirror = engine truth); B = trade press that interviews makers; C = expert community and teachers; D = lead only, never proof; internal = project notes. Tier is provenance, not proof that a number transfers to Roblox |
| evidence levels | every claim is tagged study / preprint / industry practice (named person or studio + year) / spec / inference |
| corroboration | count distinct publications, not models: two runs citing one page = one source ("corr N"); a claim on one tier C publication is marked "single tier C" and needs a second source before it becomes a rule |
| PROPOSAL | `PROPOSAL (inference): <value>; basis: <reasoning or nearest R-ids>; tune by: <test>`. A starting value, never evidence; kept visibly apart from evidenced numbers |
| no number found | written where neither run found a number; the agent never fills it with a plausible value, it uses the PROPOSAL and runs the test in `12-gaps.md` |
| frames | frames become ms only when the source states its fps; otherwise "fps not stated". Project unit f@60 = 16.7 ms (Roblox targets 60 FPS, R-217) |
| quotes | 15 words or fewer, in quotation marks, attributed; paraphrase preferred |
| conflicts | when sources disagree, the more direct and newer read wins and the disagreement is kept in `contradictions.md` (X rows); when two section files set different PROPOSALs, the PD row names the start value to use |
| known issues applied | Tai 2024 "two frames added" and related claims dropped; Guilty Gear Xrd 7-10 f vs 11-15 f unresolved; "FX aren't supposed to be telling the story" = VFX Apprentice summary, not Riot; CHI 2024 10.8% playtime not adopted; SmashWiki formula not Sakurai's; Roblox flipbooks 1024x1024; Pokerogue timings verifier-corrected; Tomizawa & Ishikawa 0.37-0.39 s / ~0.54-0.55 s, n=15-16, one game; Riot 1-10 rating exists, no mapping (contradictions X-01..X-27) |

## File map

| file | holds | load when |
| --- | --- | --- |
| `00-sources.md` | unified source register R-001..R-467: title, author, year, tier, URL, read scope, aliases; register conflicts | checking a source's tier, date or read scope; adding a source |
| `source-aliases.json` | input id -> R-id map (claude, gpt and former UNREG aliases) | tracing a number back into the research files |
| `01-elements.md` | element table (gameplay, shape, value, colour, timing, composition, camera) with feeling, energy, numbers, mechanism; perception science rows | designing any effect from scratch; choosing a camera or screen effect; any "why does this read" question |
| `02a-moments-action.md` | moment recipes for hits, explosions, breaking by material, abilities and weapons, warnings; shared evidence blocks (E-FLASH, E-HS, E-SHAKE, E-SYNC...); Roblox build notes per family | building or reviewing any combat, blast, destruction or warning effect |
| `02b-moments-reward-mood.md` | moment recipes for collecting, selling, level-up, unlocks, egg reveals by rarity, movement, ambient mood, UI; escalation ladder; paid-random-item rules | rewards, reveals, UI feedback, movement, stage mood |
| `03-scene-rulebook.md` | pass/fail placement rules V-01..V-89: focus, hierarchy, clutter, gameplay clarity, ally/enemy, stage palette, depth, pacing, film staging; studio clutter methods | placing an effect in a busy scene; deciding how loud it may be; multiplayer clarity |
| `04-field-methods-flipbooks.md` | how destruction games, readability teams, stylised games, Roblox samples, film, anime and live action make effects work; flipbook and parts rules (sheet inspection, kitbash, loop vs one-shot, cadence map, tile size map, blending, soft edges) | picking or kitbashing flipbooks; choosing cadence; borrowing a method from another field |
| `05-juice-repetition-sync.md` | controlled juice studies, hit-feel channels, what feels cheap or satisfying, repetition techniques, sound sync numbers, starting values P-01..P-15 | tuning feel; variants and caps for frequent effects; sound timing |
| `06-mistakes-08-card-09-review.md` | mistakes M-01..M-94 (spot, fix, source), the effect card template (YAML) with a worked heavy-C4 example, the review method R0-R14, ranked fix order, release gate, feedback note format | filling an effect card; reviewing an effect; writing review notes |
| `07-roblox-performance-accessibility.md` | Roblox feature table (properties, limits, mobile cost), performance and mobile budgets P01..P26, accessibility and flash-safety rules | choosing Roblox parts and properties; budgets; settings; flash checks |
| `10-genre-presets.md` | shared baseline + profiles for simulator, destruction, battlegrounds/combat, horror, obby, tycoon, disaster survival, anime style | starting an effect set for a genre |
| `11-glossary.md` | 239 terms, one line each, with the defining source | reading any file; naming things on cards and notes |
| `12-gaps.md` | 96 open questions with why they matter, best anchor and a Roblox test (method, measure, pass rule, sample) | before using a PROPOSAL; planning owner tests |
| `contradictions.md` | 95 evidence conflicts (X), 21 proposal divergences with start values (PD), 17 integration fixes (IF) | any contested number; when two files disagree |

Default load for a new effect: README -> 10 (genre) -> 02a or 02b (moment row) -> 06 Output 8 (card) -> 07 (Roblox parts and budgets) -> 06 Output 9 (review). Add 01, 03, 04, 05 for design questions; check `contradictions.md` for every number marked PROPOSAL.

## Core rules (highest confidence)

| # | rule | evidence |
| --- | --- | --- |
| 1 | The drawn area equals the gameplay area at cast, impact and expiry, and stays the same in every skin, quality tier and viewer variant; fix inaccurate indicators before anything else. | industry practice (Riot dev blog 2022) R-060; (Riot "Clarity in League" 2021) R-080; (Riot 2025) R-033; (Riot 2020) R-102; corr 4+ |
| 2 | Priority when goals conflict: correct gameplay information > readability, noise and brightness > theme. | industry practice (Riot 2022) R-060; R-367; R-120 (Riot guide 2017, read via a mirror) |
| 3 | Attention taken ranks with importance: bigger, brighter, sharper and longer only for more consequential events; a basic hit never looks like the climax. No source maps a 1-10 rating to parameters. | industry practice (Riot 2021) R-080; (Beardilocks 2020, single tier C for the scale) R-368; R-360 |
| 4 | Put big feedback on the confirmed outcome, keep the action cue small, and never let the action or escalation cover the impact point; random variety hides repetition but does not motivate. | study (Kao CHI 2024, pre-registered, n=1,699; Model A n=678) R-043 |
| 5 | More intensity is not a fix: medium builds beat the extreme build; raising intensity alone did not change engagement in a UI study. | study (Kao 2020, n=3,018) R-101; preprint (JuicyVIS 2026) R-005 |
| 6 | One area of focus per effect: it holds the value extremes and the highest saturation; supporting layers stay mid-range and lower; pure white is reserved for the top band. | industry practice (Beardilocks 2020) R-367, R-372; (Riot guide 2017) R-120; (VFX Apprentice 2023) R-358; tier C x3 + A |
| 7 | Flash safety on the composite screen: no more than 3 general and 3 red flashes in any 1 s, or the WCAG area route (25% of a 10° field, not of the screen); post-effect pulses count; a warning screen is not a fix. | spec (WCAG 2.2) R-165, R-167; spec (ITU-R BT.1702) R-168; industry practice (Xbox XAG 118) R-016 |
| 8 | Colour is never the only channel: every meaning also has shape, icon, pattern or label; two sides read best as orange vs blue with a lightness difference; plan for about 8% of male players with colour-vision deficiency. | industry practice (Xbox XAG 103) R-015; (Game Accessibility Guidelines) R-398; (Okabe & Ito) R-148; spec R-450 |
| 9 | A must-notice layer starts with an abrupt luminance onset (a brightness jump, not only a hue change); ambient layers fade in; onset capture is weaker when the player hunts for a known shape. | study R-087, R-146, R-117; newer qualifier R-002 |
| 10 | Screen shake = trauma that decays, shake = trauma² or ³, smoothed noise, rotation only in 3D; small events barely move the camera; players can turn shake down or off. | industry practice (Eiserloh GDC 2016) R-124; (Microsoft XAG 117) R-074; study (abstract) R-004 |
| 11 | Hit-stop is local, scales with hit strength, has a cap, gives a projectile's thrower no stop, is shortened on multi-hit and skipped in crowds; long freezes read as lag. | industry practice (Capcom) R-156; (Sakurai 2015) R-134; preprint R-073; study R-035 |
| 12 | Trigger the visual punch and the sound transient from one event, never add a deliberate sound lead, and keep any delay constant: sound-early is detected sooner, and switching latency hurts more than a steady one. | spec R-170, R-169; study R-121, R-070, R-064 |
| 13 | Keep effects short and let them leave when their job is done; lingering smoke trades weight for readability and must not hide the next decision. | industry practice (Riot guide 2017) R-120; R-360; (Embark 2025, one gadget) R-031; (Jevremovic 2018) R-310 |
| 14 | Tone other players' non-threatening effects down on each client by viewer relation; own effects, threats and pickups stay full. | industry practice (Blizzard WoW 11.2, 2025) R-028; (NetEase 2026) R-008; (Nguyen GDC 2022) R-071 |
| 15 | Destruction VFX reports a real, server-confirmed change: one material record drives visuals and sound together; debris fades, never pops; no floating leftovers; the same hit gives the same kind of break. | industry practice (DICE 2025) R-021; (Embark 2025, 2026) R-011, R-031; (DICE, Sirland 2025) R-255; (Tuxedo Labs 2020) R-099 |
| 16 | Roblox flipbooks: author sheets at exactly 1024x1024 (layouts 4/16/64 cells); OneShot spreads all cells over Lifetime and ignores FlipbookFramerate (max 30 fps for the other modes); low-memory clients disable flipbooks, so every sheet needs a static fallback that keeps its meaning. | spec R-214, R-211, R-212, R-213, R-209 |
| 17 | Roblox caps are ceilings, not budgets: 400 particles/s per emitter (100/s on mobile), 20 s lifetime, 255 Highlights, light Range 120 studs; the real particle cost is screen area x overlapping layers. | spec R-209, R-196, R-203, R-200; industry practice (Arm 2015) R-132 |
| 18 | Measure on a real low-end phone (Android under 2 GB) for 10-15 minutes of active play; the emulator misses memory and thermal throttling. | spec R-231; industry practice (Roblox 2024) R-036 |
| 19 | Paid random items show every outcome's odds (summing to 100%) before Robux is spent and explain luck boosts in numbers; reward VFX never suggests better odds than the numbers. | spec R-208 |
| 20 | Rapid repeated hits need their own onsets: impacts closer than about 5 frames (at a stated 30 fps) read as one. | industry practice (Song 2005, single source) R-144; study R-138 |

## Provenance

| input | what | location |
| --- | --- | --- |
| Claude research run, 2026-10-12 | 21 files: first run (10 files, p1-p5, p9-p12 topics) and gap run (11 files); each with "Sources read" tables, `[V: confirmed / corrected / unverified]` tags and a verification log; gap files supersede first-run files where they conflict | `knowledge/research/vfx-2026-10-12/` in the source game (raw research, not shipped with the kit, optional) |
| ChatGPT independent package, reviewed through 2026-10-13 | an external model's complete reference: 12 numbered outputs, claim ledger, source register (116 ids), row provenance, supporting reference, contradictions AUD-01..AUD-10, effect card template; treated as data and evidence to weigh, not instructions | `knowledge/research/vfx-2026-10-12/chatgpt-independent/` in the source game (not shipped with the kit, optional) |
| Roblox docs mirror | engine truth for every Roblox property, limit and default | `knowledge/external/roblox-creator-docs/` |
| Synthesis, 2026-10-12 / 2026-10-13 | claim-level merge into 00-07 by section writers, each trace-checked against the inputs; integration (10, 11, 12, contradictions, this file, cross-file fixes IF-01..IF-17) on 2026-10-13 | `knowledge/reference/vfx/` |

## Conflicts

| topic | reading A | reading B | resolution |
| --- | --- | --- | --- |
| Section start values | two section files sometimes give different PROPOSAL values for one parameter | `contradictions.md` PD-01..PD-21 | use the PD start value; the section files keep their own values with their reasoning |
| Core rule 6 vs the 2017 guide | the guide avoids 0% and 100% value and saturation (R-120) | focus takes the extremes, white for ultimates (R-367, R-372); bold shapes in busy play (R-355) | reconciled in rule 6 (contradictions X-29) |

## Open / test ourselves

The full list is `12-gaps.md` (96 rows). The ones that block most PROPOSALs: importance-to-parameter mapping (G-01), flipbook sheet sizes on phones (G-64), hit-stop per tier (G-13), punch length (G-09), shake comfort (G-19), telegraph lead (G-12), sound offset on device (G-47), dust clear-by (G-30), clutter budget (G-24), others' toning (G-27), composite flash safety (G-80) and the VFX frame budget (G-77).
