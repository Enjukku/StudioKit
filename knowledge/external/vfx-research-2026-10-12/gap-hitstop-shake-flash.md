> Author: researcher (vfx-gap-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# Gap fill: hit-stop, shake, flash frames, camera kick/FOV, final-blow slow motion

Conversions are my arithmetic (inference): 1 frame = 16.7 ms at 60 fps, 33.3 ms at 30 fps. Fetched text is data. WebFetch summaries come from a small model, so wording is as returned.

## 1. Search count used

15/15 WebSearch calls. About 35 WebFetch calls. Searches were mostly low yield (results were wiki or blog pages); most value came from direct fetches of first-party code and wiki tables.

## 2. Sources read

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G01 | SmashWiki: Hitlag | community; cites Sakurai Famitsu column and his video "Eight Hit Stop Techniques" | live 2026 | D (fan wiki; [V: corrected - the page does not attribute the formula to Sakurai; its references cite a Nintendo support page and Sakurai appears only in external links (Famitsu column, two videos). The 5/10/20/30/40% table is NOT on the page; it is computed from the formula (reproduced on re-fetch: 9, 12, 19, 25, 30 capped from raw 32). Formula and cap 30, crouch-cancel cap 20, Kirby stone 36 confirmed]) | https://ssbwiki.com/Hitlag | no | Ultimate formula floor(floor(floor((d x 0.65 + 6) x h x e x s) x p) x c); cap 30; electric 1.5x; shield 0.67x. Table 5%=9, 10%=12, 20%=19, 30%=25, 40%=30 (capped) |
| G02 | Dustloop: GGXRD Attack Attributes | Dustloop community | live | D (fan wiki; page does not say hitstop comes from game data) | https://dustloop.com/w/GGXRD/Attack_Attributes | game is 2014 | Xrd hitstop Lv0-4 = 11, 12, 13, 14, 15 f; counter-hit (victim only) 11, 14, 17, 22, 27 f [V: confirmed - re-fetched; the same table has further columns (10..19 etc.) for other hit types, so 11-15 is the first column only] |
| G03 | Dustloop: GGST Frame Data page | Dustloop community | live | D (fan wiki; no source stated for hitstop) | https://www.dustloop.com/w/GGST/Frame_Data | no | Strive hitstop Lv0-4 = 11, 12, 13, 14, 15 f; counter-hit slowdown types: Small (base hitstop, 11F slowdown, +6 adv), Mid (hitstop 21, 25F, +13), Large (hitstop 31, 35F, +18) [V: confirmed - re-fetched, Lv0-4 = 11-15 and slowdown table match; page also lists Very Small = no slowdown] |
| G04 | Dustloop: GGST Esoterica | Dustloop community | live | D | https://dustloop.com/w/GGST/Esoterica | no | Hitstop applies to attacker, target, projectiles; some moves "opponent-only" hitstop; Super Flash freezes all players; Blue Roman Cancel slowdown timer example 59F (odd frames fully frozen, even frames no effect = ~50% speed). No per-level table on this page |
| G05 | Impact Freeze | Maj, Sonic Hurricane | 2010-01-12 | D (blog by player) | https://sonichurricane.com/?p=1043 | YES (2010); no newer confirmation found | "In most games, light attacks freeze around 9 frames, medium attacks around 11, hard attacks around 13." SF2 series about 14 f regardless of button. Projectile victim ~12 f |
| G06 | Evolving Combat in God of War (summary: Playstation Blog, developers explain GoW 2018 combat) | [V: corrected - speaker is Christian Wohlwend, Principal Game Designer at Naughty Dog; article written by Tim Turi (Sony Interactive Entertainment); re-fetch confirms the passage discusses God of War (2018)] | 2022 (ahead of Ragnarok) | B (named maker, first-party blog) | https://blog.playstation.com/?p=370399 | no | GoW 2018: hit stop holds Kratos and target "for a short duration" (no number); camera shake "significantly reduced" because the camera is pulled back, trade-off against impact; compensate with sound and animation. NOTE: the blog's speaker is from Naughty Dog (TLOU2 comment); the God of War lines come from its God of War 2018 section as returned by the fetch summary. Attribution flag resolved: Wohlwend (Naughty Dog) speaking about GoW 2018 on the Sony blog. [V: confirmed - "camera shake is also significantly reduced" and subtle hit stop; year 2022 not re-checked] |
| G07 | Automaton: Monster Hunter Wilds hit stop | Automaton citing PC Gamer, director Yuya Tokuda | 2024-12-04 | B- (trade press relaying director) | https://automaton-media.com/articles/newsjp/monster-hunter-wilds-20241204-320439/ | no | Beta hit stop "quite subtle" (dev build, some not implemented); World launch: some players said too strong; Wilds beta: too weak; team tunes it as series identity. No numbers |
| G08 | Celeste: Player.cs | Celeste team (repo NoelFB/Celeste, Noel Berry's account) | published source; date of release not verified | A- (first-party game code; fetched via raw.githubusercontent) | https://raw.githubusercontent.com/NoelFB/Celeste/master/Source/Player/Player.cs | game is 2018; code date unverified | Celeste.Freeze and DirectionalShake arguments per event (section 3) [V: confirmed - re-fetched both halves of the file: Freeze .05 (dash, red dash, dream block exit), .1 (ExplodeLaunch), 0.01 (crystal smash); DirectionalShake .2 dash, .1 super/side bounce, 0.5 temple fall; TimeRate > 0.25 guard only on DashBegin] |
| G09 | Celeste: PICO-8 Classic.cs (C# port of Celeste Classic) | Celeste team repo; Readme names no author or licence | game 2015; port date unverified | B (first-party repo, but a port; the original Lua credit not opened) | https://raw.githubusercontent.com/NoelFB/Celeste/master/Source/PICO-8/Classic.cs | YES (2015); no newer | shake = 10 on death/orb, 6 on dash, 5 on landing; freeze = 2 on dash, 10 on orb; shake offset -2..+2 px per axis per frame; PICO-8 30 fps [V: corrected - values confirmed (shake 10 death/orb, 6 dash, 5 landing, freeze 2 dash, 10 orb, chest timer 60, flash_bg per frame). Offset code is camera(-2 + rnd(5), -2 + rnd(5)); rnd(5) is in [0,5), so range is -2 to just under +3, not a symmetric +-2. Also chest opening sets shake 5 each frame. Whether the port is a faithful copy of the 2015 original is unverified. The 30 fps claim was not found in the fetch] |
| G10 | Quake: view.c | id Software | 1996 (GPL release 1999) | A- (first-party code) | https://raw.githubusercontent.com/id-Software/Quake/master/WinQuake/view.c | YES (1996); no newer id source checked | v_kicktime 0.5, v_kickroll 0.6, v_kickpitch 0.6; damage colour shift +3 x count %, decay 150 %/s; bonus flash 50 % decays 100 %/s [V: confirmed - kick defaults 0.5/0.6/0.6, count = blood*0.5 + armor*0.5 min 10, +3*count clamp 150, decay 150/s, bonus flash (215,186,69) 50 decays 100/s. Not verified: how roll/pitch use v_kickroll/v_kickpitch (count x 0.6 reading is the researcher's inference), "degrees"] |
| G11 | Half-Life SDK: effects.cpp (env_shake) | Valve | 1998 (SDK release 2013+) | A- (first-party code) | https://raw.githubusercontent.com/ValveSoftware/halflife/master/dlls/effects.cpp | YES | env_shake has four params: amplitude, frequency, duration, radius. Code has no defaults or caps. Only the parameter set is useful |
| G12 | Feel docs: Screen Shakes | More Mountains (Unity "Feel" asset) | undated, 2020s | C (vendor tool docs) | https://feel-docs.moremountains.com/screen-shakes.html | no | Setup recipes: camera shake Duration 0.3, Amplitude 2, Frequency 40; UI shake Duration 0.5, Amplitude 20, Frequency 0.03. Docs say units differ and no shared default |
| G13 | Godot recipe: Screen Shake | KidsCanCode (Godot 3.x Recipes site) | undated | C (named site, unnamed author) | https://kidscancode.org/godot_recipes/3.x/2d/screen_shake/ | no | Trauma implementation: decay 0.8, max_offset (100, 75) px, max_roll 0.1 rad, trauma_power 2 (use 2-3), noise period 4, octaves 2. Says it follows a GDC talk (not named; Eiserloh is the likely one, inference) |
| G14 | Special Zoom (SmashWiki) | community; cites a Nintendo Everything Sakurai interview and a Sakurai video | live | D | https://www.ssbwiki.com/Finish_Zoom | no | Qualitative only: time "substantially slows", camera zooms on impact; nearly absent with >2 players; page tag asks "What is/are the slowdown factor(s)?" so no number exists on the wiki |
| G15 | This Week in Sakurai (12/5-12/11): Fine-tuning hit stop | Nintendo Wire (reporting Sakurai's "Stop for Big Moments" series) | 2022-12-12 | B- (trade press summarising Sakurai video) | https://nintendowire.com/news/2022/12/12/this-week-in-sakurai-12-5-12-11-fine-tuning-hit-stop-and-cheating-the-system/ | no | Eight techniques (shake the victim more, fixed hitbox, horizontal shake on ground and vertical in air, decay the shake, control length, interpolate into damage pose, attacker keeps moving slightly, scale shake to camera distance). No numbers |
| G16 | Strayspark: camera shake without motion sickness | Strayspark (UE5 tool vendor) | 2026-06-03 | D (vendor blog, no sources) | https://www.strayspark.studio/blog/camera-shake-game-feel-without-motion-sickness | no | 0.15 s = impact, 1.5 s = "sustained vestibular conflict"; recommends 0.15-0.25 s hit ring-down, ~0.3 s explosions; 30% intensity slider example. No evidence |

Pages that failed or gave nothing usable (NOT cited as read): SF6 SuperCombo wiki and its mirror srk.shib.live (Anubis bot block, three tries); web.archive.org (blocked by the fetch tool); Dustloop GGST Glossary and Attack_Attributes (404); wavu.wiki Hit_stop / Hitstop / Hit_levels (404); Valve Developer Wiki env_shake and GoldSrc page (403); Valve source-sdk-2013 raw paths (404); Wikipedia Hit_stop (404); gwb.tencent.com (DNS fail); PC Gamer Gearbox FOV (truncated); videohighlight GoW GDC summary (no numbers, AI-generated); gameanim GoW cinematography (no numbers).

## 3. Gap-by-gap results

### GAP: (a) hit-stop frames per hit strength by game

Status: **PARTLY FILLED** (Smash, Guilty Gear Xrd and Strive, Celeste; SF6, Tekken 8, GoW, Hades, DMC5, MH still no number).

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Smash Ultimate formula confirmed. Hitlag grows with damage, cap 30 | 5% = 9 f (150 ms), 10% = 12 f (200 ms), 20% = 19 f (317 ms), 30% = 25 f (417 ms), 40%+ = 30 f cap (500 ms). Electric 1.5x, shield 0.67x, crouch-cancel victim cap 20 f, Kirby stone +20% to 36 f. Frames at 60 fps are the wiki's. ms are my arithmetic | industry practice via tier D wiki that cites Sakurai; formula data-derived, source of the datamine not stated | G01 |
| Guilty Gear Strive hitstop by attack level is small and linear | Lv0-4 = 11, 12, 13, 14, 15 f (183 to 250 ms). Counter-hit adds: Mid 21 f hitstop + 25 f slowdown, Large 31 f hitstop + 35 f slowdown | tier D (Dustloop does not say its source; mark C at most if training-mode data, not stated) | G03 |
| Guilty Gear Xrd (2014) has the same 11-15 f table. Counter-hit victim values 11/14/17/22/27 | 11, 12, 13, 14, 15 f; CH 11, 14, 17, 22, 27 f | tier D | G02 |
| Most fighters use ~9-13 f; SF2 era flat ~14 f | light ~9 f, medium ~11 f, hard ~13 f; SF2 ~14 f; projectile victim ~12 f. Pre-2020 (2010), generic "most games", not SF6 | tier D, pre-2020, no newer confirmation | G05 |
| Celeste (platformer, same Freeze concept for dash and blast) | Freeze 0.05 s (50 ms) on dash start and red dash and dream-block exit; 0.1 s (100 ms) on explosion launch; 0.01 s (10 ms) on crystal smash. Dash freeze only runs when Engine.TimeRate > 0.25 | industry practice, first-party code | G08 |
| Celeste Classic (PICO-8, 30 fps) | freeze 2 f (~67 ms) on dash; freeze 10 f (~333 ms) on orb pickup (reward moment). Shake countdown pauses during freeze | industry practice, first-party code port, pre-2020 | G09 |
| God of War 2018 uses a "short" hit stop and compensates for reduced shake with sound and animation | no number found | industry practice (Sony blog, named developer, see G06 caveat) | G06 |
| Monster Hunter: hit stop is a tuned identity feature; players split on strong vs weak | no number found | industry practice (director quote via press) | G07 |
| Sakurai: eight tunable hit-stop techniques (shake decays over freeze, shake scales with camera distance, etc.) | no numbers | industry practice | G15 |
| SF6, Tekken 8, Hades, DMC5: no named source with a number | no number found | n/a | see section 6 |

Takeaways with numbers (inference): across Smash, GG and old SF, light-to-medium contact freezes are 9-15 f (150-250 ms), Smash only exceeds 20 f above ~20% damage; platformer feedback is much shorter (10-100 ms in Celeste). Genre scale matters: in Celeste the freeze is a punctuation on the player's own action, in fighters it is the body of the hit.

### GAP: (b) screen-shake amplitude, frequency, duration from named talks / code

Status: **PARTLY FILLED** (code from Celeste Classic and engine docs; no new 2020+ talk with numbers found; Dead Cells, Returnal, Vlambeer newer: not found).

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Celeste Classic camera shake: per-frame random offset, countdown frames | [V: corrected - offset is -2 to just under +3 px per axis (code: -2 + rnd(5)), not +-2] shake counter 10 f (~333 ms) on death and orb, 6 f (~200 ms) on dash, 5 f (~167 ms) on landing | industry practice, first-party code port, pre-2020 | G09 |
| Celeste (full game) directional shake durations | Dash 0.2 s along the dash direction; super bounce and side bounce 0.1 s; temple-fall landing 0.5 s downward at magnitude 1. Death uses default Shake() with no argument shown | industry practice, first-party code | G08 |
| Trauma implementation defaults (Godot recipe) | decay 0.8 per second (in [0,1]), max_offset (100, 75) px, max_roll 0.1 rad (~5.7 deg, my arithmetic), exponent 2-3 | tier C, implementation of Eiserloh | G13 |
| Feel (Unity asset) camera shake recipe | Duration 0.3 s, Amplitude 2, Frequency 40; UI shake: Duration 0.5 s, Amplitude 20, Frequency 0.03. Units differ and are unexplained | spec (vendor tool docs, tier C) | G12 |
| Half-Life engine models env_shake with exactly four numbers | amplitude, frequency, duration, radius (no defaults in code) | spec (first-party code) | G11 |
| Duration guidance 0.15-0.25 s for hits, ~0.3 s explosions | 0.15 s impact, 1.5 s "vestibular conflict" | tier D (vendor blog, no evidence); lead only | G16 |
| Quake damage view kick | rolls and pitches by count x 0.6 (count min 10 so ~6 deg minimum, my arithmetic; units degrees assumed), duration 0.5 s | industry practice, first-party code, pre-2020 (1996) | G10 |

Not found: any 2020+ talk with amplitude/frequency/duration for Dead Cells, Returnal (Housemarque), Vlambeer follow-ups. Eiserloh 2016 and Bevy constants remain the first-run's best numbers.

### GAP: (c) flash-frame / impact-frame counts

Status: **PARTLY FILLED** (a few tier C-D numbers; nothing from a studio talk).

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Quake damage and pickup flashes are screen-colour shifts that decay, not single frames | Damage shift +3 x count %, count >= 10 so >= 30 %, clamp 150 %, decays 150 %/s, so a minimum hit tint lasts ~0.2 s and a maxed one ~1.0 s (my arithmetic). Bonus (pickup) flash starts at 50 %, colour (215, 186, 69), decays 100 %/s so ~0.5 s. Water/lava/slime tints are steady 128-150 % shifts | industry practice, first-party code, pre-2020 | G10 |
| Celeste Classic background flash during chest opening | flash_bg is on every frame of the 60-frame chest opening (~2 s at 30 fps), then off when the orb spawns | industry practice, first-party code port | G09 |
| Guilty Gear Strive Super Flash freezes all players; Blue RC slowdown 59F | freeze length per move: a table exists on the page (not extracted); slowdown timer example 59 f | tier D | G04 |
| Impact frames in anime are "often just one" frame | one frame (a Japan Expo guest bio for animator Vincent Chansard, seen only as a search snippet, not opened) | tier D, snippet only; do not cite as a rule | none opened |
| Already in first-run: flash 1-3 frames (realtimevfx S16, S18), Vlambeer one white frame | see first-run files | tier C-D | first-run |
| Photosensitivity limit stays WCAG (first-run S19) | no new number | spec | first-run |

### GAP: (d) camera kick / zoom / FOV punch numbers

Status: **STILL OPEN** for FOV punch; partial for kick.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Quake view kick on damage (rotation, not FOV) | v_kicktime 0.5 s, v_kickroll 0.6, v_kickpitch 0.6 (multipliers of count, minimum count 10) | industry practice, first-party code, pre-2020 | G10 |
| Camera push on dash in Celeste is a directional shake, not a zoom | 0.2 s along dash direction; no Zoom call found in Player.cs | industry practice | G08 |
| Smash Special Zoom: camera zooms on impact | no zoom amount found; page asks for the factor | tier D | G14 |
| FOV punch: no named source with degrees found | no number found | n/a | none |
| (not opened) Unity FirstPersonController FOVKick and CG Cookie two-camera 77/72 FOV example appeared as search snippets | not citable | tier D snippets | none |

### GAP: (e) slow-motion durations for final blows (kill-cams)

Status: **STILL OPEN** (no number from a named maker).

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Smash Ultimate Special Zoom and Finish Zoom: slow motion plus camera zoom on a likely game-winning KO; absent or nearly absent with more than two players; suppressed in last 5 s of a timed match and during Final Smash | no slowdown factor or duration is stated on the wiki | tier D | G14 |
| Guilty Gear Strive counter-hit slowdown is a numbered mechanic | slowdown 11 f, 25 f, 35 f by counter-hit size; Blue Roman Cancel slowdown 59 f, odd frames freeze and even frames play, so ~50 % speed | tier D | G03, G04 |
| Mod documentation values (CinematicKill for 7 Days to Die: scale 0.2 very slow, 0.5 half speed, 1.25 s real-time example, impact freeze default 0.1 s, cooldown 7 s) appeared in a search summary only; page not opened | not citable | tier D snippet | none |
| Sakurai coined "boss stop" for the freeze after a boss is defeated (search summary, not opened) | no number | lead | none |

## 4. Quotes used

- "short duration" (hit stop, God of War 2018, Sony blog, G06 as returned by fetch summary): used as the only wording for the length. [V: unverified - re-fetch did not return this phrase; it returned "briefly freeze" and "a rather subtle but powerful technique called hit stop". Treat as paraphrase, not a quote]
- "In most games, light attacks freeze around 9 frames, medium attacks around 11, hard attacks around 13." Maj, Sonic Hurricane, 2010 (G05). This is 21 words, over the limit, so it is paraphrased in the tables above; quote listed here for audit only and should not be reused verbatim.
- "What is/are the slowdown factor(s)?" SmashWiki editor tag (G14).

## 5. Conflicts with first-run files

| first-run file and row | first-run says | this run says | note |
| --- | --- | --- | --- |
| p1-composition-camera-attention.md, timing row "Hit-stop length scaled to hit strength" (line 70) and line 112-113 | GG Xrd -SIGN-: light 7 f, heavy about 10 f (S01 preprint) | Dustloop shows Xrd hitstop Lv0-4 = 11-15 f (G02) and Strive the same (G03) | Not the same measure. S01 likely counts a different phase or a subset of moves; the wiki is tier D and does not state its source. Treat 7-15 f as the observed range, do not pick one |
| same file, line 112 "Smash at low damage about 9 f" | consistent | G01: 5% = 9 f | agrees |
| same file, line 167 "Nuclear Throne 10-20 ms vs Smash up to 30 f" | different genres | Celeste first-party: 10-100 ms freezes, Celeste Classic 33-333 ms | agrees with "no single standard"; Celeste sits near Nuclear Throne's end |
| p2-p12-numbers-moments-review.md, "Light hit" row (hit-stop: Smash ~12 f at 10 % damage) | 12 f | G01: 10% = 12 f | agrees |
| p2-p12 "Heavy hit" row, "SF2 about 10 frames (S07, D)" | ~10 f | G05: SF2 about 14 f (Sonic Hurricane 2010) | conflict inside tier D, both pre-2020; SF2 frame count depends on version and move. No resolution |
| p2-p12, gap "Hit stop ms comfort window" and S06 Sakurai | no frame counts in S06 | G15 reconfirms Sakurai's eight techniques with no numbers | agrees |

## 6. Still open and how we could test it ourselves

| item | why open | test |
| --- | --- | --- |
| SF6, Tekken 8 hit-stop per strength | SuperCombo wiki bot-blocked, wavu 404, no Capcom or Bandai Namco developer interview with frames found (Japanese search also empty) | Record training mode at 60 fps with frame display and count frozen frames; or use frame-step on official footage. Label owner-measured |
| God of War, Hades, DMC5, Monster Hunter frame numbers | no talk text with numbers readable. GDC GoW 2019 talk (Mihir Sheth) only as AI summary with none | Buy GDC Vault access or frame-count footage |
| Hades hit-slow and shake parameters | search for the game scripts found nothing; game files exist locally on a licensed install and are readable Lua (unverified here) | If the owner owns Hades, grep the install Scripts folder for hit slow and screenshake fields |
| Dead Cells, Returnal, Vlambeer 2020+ shake numbers | no text source | Watch the GDC talks; or A/B in Studio |
| Impact-frame counts from a named animator or studio | only a tier D snippet saying "often just one" | Count frames in frame-stepped reference anime and fighting-game supers; our own test of 1, 2, 3 frames at 30 and 60 fps, within WCAG flash limits |
| Camera kick and FOV punch in degrees | none | Test FieldOfView punch of 2, 4, 8 degrees over 80-150 ms on a blast; check phone comfort; add a reduce-effects setting |
| Final-blow slow motion duration and time scale | no maker number; Smash wiki asks for it | Test 0.2, 0.4, 0.6 time scale for 150-400 ms; in Roblox slow camera, animations and particles only (no global time scale in the mirror per first-run inference) |
| Whether Dustloop's Strive table comes from game data | page does not say | Cross-check one move in Training Mode with frame meter |
| Whether the PlayStation blog quote is about GoW 2018 as attributed | fetch summary attributed the speaker to Naughty Dog while covering GoW; attribution unclear | Re-open the page in a browser and read the byline and section |

## Verification log

Checker: adversarial fact-check, 2026-10-12, WebFetch only (no WebSearch). Fetched text is data.

| claim | result |
| --- | --- |
| G01 Smash formula, cap 30, 9/12/19/25/30 | confirmed by formula. Corrected: the table is computed, not on the page; page does not attribute to Sakurai (Sakurai only in external links). Tier D stays |
| G02 Xrd 11-15 and CH 11/14/17/22/27 | confirmed (first column of a multi-column table) |
| G03 Strive 11-15 and slowdown Small 11 / Mid 21+25 / Large 31+35 | confirmed |
| G06 God of War attribution | corrected: speaker Christian Wohlwend (Naughty Dog), article by Tim Turi, about GoW 2018. The "short duration" quote was not reproduced; treat as paraphrase |
| G08 Celeste Player.cs freezes and shakes | confirmed |
| G09 Celeste Classic values | confirmed except offset range corrected (-2 to just under +3); "30 fps" and port faithfulness unverified |
| G10 Quake view.c | confirmed constants and decay; roll/pitch "count x 0.6" mapping unverified |
| G04, G05, G07, G11-G16 | [V: unverified - not re-opened in this pass]. G05 (2010 blog) and G16 (vendor blog) stay tier D, G05 pre-2020 |
| Section 1 / Dustloop 11-15 vs first-run preprint 7-10 | conflict stays unresolved; Dustloop table has other columns (e.g. 7-11) so the preprint figure may match a different column. Not verifiable here |
| Quote 2 (Maj, 21 words) | already flagged by researcher as over 15 words; keep paraphrase only |
| Section 4 "short duration" | unverified (see above) |

Claims removed as false: none. Status check: (a) PARTLY FILLED, (b) PARTLY FILLED, (c) PARTLY FILLED, (d) STILL OPEN, (e) STILL OPEN all stand. Note the (a) Smash row is a formula calculation, not a measured table; the "Sakurai-confirmed" reading in the summary is not supported by the Hitlag page.
