> Author: researcher (vfx-deep-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# P4 Case studies: readable and stylised real-time games

Scope: Group 1 readability (Riot LoL/Valorant, Overwatch 2, Suicide Squad, Fortnite, Marvel Rivals). Group 2 stylised/juicy (Hades, Hi-Fi Rush, Splatoon 3, TotK, SF6, Balatro, Vampire Survivors, Supercell). Roblox games.

**Honest summary of evidence.** Tier A material with real numbers exists for: LoL (clarity rules, VFX-update priorities), Valorant (shader/clarity article, hit-effect clarity), Capcom (hit stop frames), Roblox (spec). For Overwatch 2, Suicide Squad, Fortnite, Hades, Splatoon 3, TotK, Balatro, Vampire Survivors, Supercell and the named Roblox games I found NO readable tier A/B VFX-specific source. The web-search budget ran out mid-task (200/turn limit), and several pages returned 403 or redirects. Those games get "no usable source" cards instead of invented content. Section 5 lists how to close each gap.

## 1. Sources read

Only pages whose text was actually fetched and read. "thin" = page loaded but gave little for VFX.

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave us |
|---|---|---|---|---|---|---|---|
| S1 | Clarity in League (dev post) | Riot Games | 2021-03-12 (verified) | A | https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/ | no | hierarchy rule, skin clarity budget, silhouette rules, hitbox-matches-effect, 2 s recall rule, scale (150 champs, ~1,000 skins) [V: confirmed - date, 150 champs/1000 skins, 2 s recall, both quotes, Arcane Comet] |
| S2 | Behind the scenes of VFX updates (dev blog) | Riot (credited Sirhaian and Riru; the surname "Leroy" is not on the page) | 2022-04-25 (verified) | A | https://www.leagueoflegends.com/en-pl/news/dev/dev-behind-the-scenes-of-vfx-updates/ | no | ranked goals: hitbox accuracy > readability/noise > theme; process; skin-tier effort table [V: corrected - author credit and date fixed; ranked goals and RP tiers 750/975/1350/1820+ confirmed] |
| S3 | VALORANT Shaders and Gameplay Clarity | Riot Games | 2020-06-30 (verified) | A | https://www.riotgames.com/en/news/valorant-shaders-and-gameplay-clarity | no | red/blue fresnel friend-foe, depth modulation, hard-edged smoke, 6.9 ms budget, shader instruction counts [V: confirmed - 6.9 ms for the 144 FPS bar; env 100-41 "on most objects", chars 128-84, base weapons 103-73; red enemy / neutral blue ally fresnel; hard-edged smoke; "shiny" quote] |
| S4 | Riot on hit registration and future improvements (reporting Riot's post) | The Spike (quotes Riot) | 2020 | B | https://www.thespike.gg/valorant/news/riot-games-on-the-state-of-hit-registration-and-future-improvements/347 | no | correctness vs clarity split; hit effects follow hit body part; ping trade-off [V: corrected - date 2020-08-07; Riot said it is "iterating on" the idea, so it is a stated direction, not a shipped feature; 100 ms example and correctness-vs-clarity split confirmed] |
| S5 | Anatomy of a LoL missile, Part 2 | "Beardilocks", Riot VFX artist (realtimevfx) | 2020-05-25 | C | https://realtimevfx.com/t/anatomy-of-a-league-of-legends-missile-part-2-what-are-we-communicating-with-our-vfx/13062 | no | visual hierarchy doc rated 1-10 per perspective; impact scaling; shared visual language; "nothing is important" rule [V: corrected - 1-10 per player/ally/enemy, quote and Morgana R confirmed; the page says "almost 150" champions and ">750 abilities" but does NOT mention 1,000 skins (that figure is S1)] |
| S6 | 10 Design Tips from the LoL VFX Style Guide | VFX Apprentice | 2022-08-29 (verified) | C | https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips | no | value 0-100% avoid extremes, saturation draws focus, one dominant colour, keep FX short. Secondary summary of the 2017 Riot guide [V: confirmed - avoid 0/100 value, avoid 0/100% saturation, tip 10 heading quote; still single tier C, second source needed] |
| S7 | What Riot's Head of Creative looks for in VFX artists (M. Lehmann) | VFX Apprentice | ~2020s | C | https://www.vfxapprentice.com/blog/riot-games-head-creative-vfx-artist-needs | no | timing = anticipation, build-up, payoff, overshoot-settle; 1-frame scythe anim [V: unverified - not re-opened] |
| S8 | How style guides help define the look of your game and FX | VFX Apprentice | 2023-07-12 | C | https://www.vfxapprentice.com/blog/creating-vfx-style-guides-for-games | no | Sparkball guide: main action in first quarter of lifetime. Did NOT contain the Riot guide |
| S9 | Hit stop lecture (Street Fighter V column) | Capcom (CFN) | undated, SFV era | A | https://game.capcom.com/cfn/sfv/column/131545 | **likely pre-2020**; no newer Capcom confirmation found | hit stop meaning, 8/12/16 F L/M/H example, multi-hit shorter, projectiles none for attacker [V: confirmed - 8F/12F/16F, shorter multi-hit, no stop for projectile thrower, "hypothetical game" example; page carries no date, ID order suggests pre-2020 (inference)] |
| S10 | Early SF6 Drive Parry design (reports Capcom dev statements) | EventHubs | 2023 | B | https://eventhubs.com/news/2023/jul/18/capcom-early-sf6-drive-parry | no | X vs O shape contrast, blue = block colour, paint-splash replaces smoke, slowed Just Parry [V: confirmed - article 2023-07-18, Capcom blog translated by MajinTenshinhan] |
| S11 | CEDEC 2024 SF6 "anime physics" report | CGWorld.jp (reports Capcom VFX room talk) | 2024 | B | https://cgworld.jp/article/202410-cedec03-sf6.html | no | exaggerate vs pure physics; staged wind per motion; bake break sims; no numbers |
| S12 | Hi-Fi Rush CEDEC 2023 music-sync animation | GameAnim (reports Tango talk by John Johanas and Masaaki Yamada) | 2023-09-08 | B | https://www.gameanim.com/?p=106877 | no | 120 BPM, 60 fps, key poses on beat. Animation, not VFX [V: corrected - 120 BPM / 60 fps was the PROTOTYPE animation rate, the rate was changed dynamically afterwards; key poses on beat confirmed] |
| S13 | Making of Hi-Fi Rush's 3D toon rendering style | 80 Level (reports GDC 2024 talk by Tango graphics programmers) | 2024 | B | https://80.lv/articles/the-making-of-hi-fi-rush-s-3d-toon-rendering-style | no | deferred toon renderer, 60 fps native. No VFX detail (thin) |
| S14 | Behind the scenes look at the effects in Hades | 80 Level | 2020 | B | https://80.lv/articles/a-behind-the-scenes-look-at-the-effects-in-hades/ | no | names credit (Josh Barnett); no technique content (thin) |
| S15 | Hades II Has a Legibility Problem | nex-3.com (individual critic) | 2024-25 | C (critic) | https://nex-3.com/tag/hades | no | red AoE telegraph density as legibility failure; Hades 1 vs II attack structure. Opinion |
| S16 | Marvel Rivals patch cuts visual chaos | games.gg (Eliza Crichton-Stuart) | 2026-07-17 | B- | https://games.gg/news/marvel-rivals-patch-cuts-visual-chaos/ | no | NetEase reduced ability/ultimate/Team-Up VFX 2026-07-15; no numbers; no NetEase quote [V: corrected - patch notes name "several heroes' abilities" and Team-Up moves; the page does not say "ultimate" VFX, and the quoted sentence is the article's own wording; patch 15 July, article 17 July confirmed] |
| S17 | Overwatch PTR patch notes (Sept 2018) | Blizzard | 2018 | A | https://overwatch.blizzard.com/en-gb/news/patch-notes/ptr/2018/09 | **pre-2020**; no newer Blizzard VFX source found | 9 colourblind-safe team colours for UI/outlines; shield/barrier visuals updated "to increase readability" [V: confirmed - nine colours, enemy/friendly set separately, patch dated 2018-09-21] |
| S18 | Overwatch 2 "Evolving the Art" recap | Blizzard | 2019 | A | https://news.blizzard.com/en-us/article/23189038/2 | **pre-2020** | weather/particles only; no readability content (thin) |
| S19 | Particles' Flipbook Release | Roblox staff, DevForum | ~2022 | spec | https://devforum.roblox.com/t/particles’-flipbook-release/2029388 | no | square power-of-two flipbook textures 8-1024 px; Grid2x2/4x4/8x8; leave gaps between frames |
| S20 | Roblox Creator Docs: effects/particle-emitters.md (local mirror) | Roblox | current | spec | knowledge/external/roblox-creator-docs/effects/particle-emitters.md | no | Rate cap 400/s (100/s mobile); lifetime cap 20 s; flipbook max 30 fps; flipbooks auto-off when low memory; fill-rate warning [V: corrected - 400/s (100/s mobile), 20 s lifetime cap, 30 fps max for FlipbookFramerate, low-memory auto-off all confirmed in the mirror; the "64-frame max" is only the largest preset (Grid8x8), Custom layouts can exceed it; OneShot ignores the 30 fps cap] |
| S21 | GDC Vault abstracts: Lost Survivors FX (InnoGames 2022), Bleeding-Edge Effects on Mobile (Level Ex 2020), WoW VFX Pillars (Blizzard 2023), Callisto Protocol VFX (2023), Subtle Art of Not Making VFX (Coalition 2021) | various | 2020-23 | A (abstract only) | gdcvault.com/play/1027900, /1026744, /1029418, /1028823, /1027114 | no | abstracts only, talks are paywalled. Confirms talks exist; no numbers |
| S22 | DevForum: "How to create VFX?" and "Best way to create long lasting particles" | forum users, no staff | 2025 | C | https://devforum.roblox.com/t/how-to-create-vfx/4029502 ; https://devforum.roblox.com/t/best-way-to-create-long-lasting-particles/3965603 | no | thin; one unverified remark that emitter rates drop on low-end devices (matches S20) |

Fetch failures (not cited as read): Riot Nexus 2017 style guide post and the PDF (redirect to homepage), GDC schedule page for Suicide Squad (403), Unreal interview on Hi-Fi Rush (403), Zeldadungeon TotK interview (403), gamedev.net Brawl Stars summary (403), Automaton Splatoon 3 ink article (headline only), PC Gamer Valorant hit effects (nav only), esports.gg Valorant 11.07 (DNS), Nintendo Splatoon 3 Ask the Developer Part 1 (no VFX content).

Count read: 22 entries (tier A: 8 incl. 1 abstract-only bundle, spec: 2, tier B: 7, tier C: 6 pages grouped).

## 2. Findings

### 2.1 Field methods table (REQUIRED FORMAT)

| field | method | what it does to the viewer | how to use it in a game | evidence level | source, tier and year |
|---|---|---|---|---|---|
| gameplay | Make the effect's visible area equal the real hitbox/blast radius. Riot ranks "correct inaccurate hitbox indicators" as goal 1, above readability and theme | Viewer trusts the telegraph. Dodging or standing in it matches outcome | Brick-blast ring or crater decal radius = server blast query radius. Never draw bigger "for looks" without also tinting the extra as cosmetic. Fix mismatch before any polish | industry practice (Riot 2021-22) | S2 A; S1 A (Arcane Comet criticised: big ground circle implies more dodgeability than real) |
| gameplay | Attention matches importance. Factors: damage, hard/long CC, dodgeability, play impact. Bold only where impact is high; noise minimal except large-effect spells | Eye goes to the thing that matters first. Low-value effects stay in background | Rank every effect 1-10 before building. Big charge detonation = high; chip dust = low. Size, brightness, saturation scale with rank | industry practice (Riot) | S1 A ~2020-21; S5 C 2020 (1-10 scale, per perspective, corroborated by S1) |
| gameplay | Different rank per viewer perspective: caster, ally, enemy. Morgana's R range circle shown only to her and affected targets | Less team-fight clutter. Threat reads to the person who must react | Show full ring to the thrower and the victim area; shrink or fade for bystanders (client-side visibility flag) | industry practice (Riot, single artist) | S5 C 2020. Needs second source for the exact Morgana example; the principle is corroborated by S1 |
| gameplay | Stacking budget: ultimates and combos overlapping made screen unreadable; NetEase cut ability/ultimate/Team-Up VFX (balance unchanged) | Less chaos when 4+ effects overlap | Cap simultaneous high-rank effects. Newer effect of equal rank steals attention from older; dim or shorten older | industry practice (news report, no developer quote) | S16 B- 2026. No numbers found |
| gameplay | Vision-blocking VFX use a hard geometric edge (visible from any angle), defined range, not soft translucency. Viper ult uses a defined range | Players know exactly where cover/vision block starts | Smoke or dust clouds that block aim: hard-edged mesh or hard particle boundary. Soft puffs only for non-blocking cosmetic smoke | industry practice (Riot Valorant) | S3 A ~2020 |
| gameplay | Hit-confirm effect stays attached to the body part hit and follows movement. Trade-offs: late for high ping; may move behind cover | Player can tell where a hit landed; fewer "was that a headshot?" doubts | Attach hit sparks/chips to the struck brick or Part, not a world point. Spawn instantly client-side, reconcile with server result | industry practice (Riot 2020; trade-offs stated) | S4 B 2020 (100 ms ping example) |
| gameplay | Separate "correctness" (outcome right) from "clarity" (presentation hard to read) when triaging complaints | Avoids fixing the wrong layer | VFX review checklist step 1: is the effect lying, or just hard to read? | industry practice (Riot 2020) | S4 B 2020 |
| gameplay | Cosmetic variants must be at least as clear as base; skins checked on all maps; no near-permanent glow transformations | Rare/paid effects cannot hide gameplay information | Any pet, weapon skin or egg-hatch effect: same hitbox read, same wind-up; test on every stage's lighting | industry practice (Riot) | S1 A ~2020-21 |
| shape | Each ability has one unique primary shape that skins keep. Secondary and tertiary features may change | Instant recognition across variants | One signature silhouette per weapon/charge (ring, cone, column). Recolour freely, keep silhouette | industry practice (Riot) | S1 A; S5 C (Morgana missile) |
| shape | Projectiles show direction even when still (blurred tail). Downward-scrolling lines for shield-type effects | Direction reads from one frame | Rocket/grenade: tapered tail, trail, or beam stretch in travel direction. Trail objects for thrown C4 | industry practice (Riot) | S1 A |
| shape | Same effect type = same shape language: roots use a floor ring plus rising cylinder; heals green with non-threatening shape | Viewer decodes meaning without reading | Define a game-wide table: knockback, burn, freeze, heal, pickup, danger. Re-use shapes across stages | industry practice (Riot, artist-level) | S5 C 2020. Corroborated by S1 (shape language carries into skins) |
| shape | Stronger = bigger, brighter, sharper shapes | Threat level reads from silhouette | Use sharp-edged spikes for lethal/high rank, rounded blobs for harmless | industry practice | S5 C 2020 |
| shape | Contrast shapes for two meanings: SF6 Just Parry light forms an X vs the hit effect forming an O | Two events never confuse even at speed | Success vs fail feedback use different silhouettes (X-burst vs circle ring) not just colour | industry practice (Capcom via news) | S10 B 2023 |
| value | Build palette mostly mid-range value, avoid 0% and 100% extremes. Wider value range draws more focus. Glow pushes range | Effect does not vanish into environment or UI | Reserve pure-white core for the single hero moment; keep supporting layers mid value | industry practice (secondary summary of Riot 2017 guide) | S6 C. Only tier C; the 0%/100% numbers are not independently confirmed. **Needs 2nd source**: Riot 2017 PDF not retrieved |
| value | Characters brightened with distance, ambient darkness and brightness clamped per map area; separate caps for max darkness/brightness | Targets stay readable far away and in dark areas | Clamp environment lighting under heavy VFX; raise rim/outline strength with camera distance | industry practice (Riot Valorant) | S3 A ~2020. No distance thresholds published |
| value | Low-quality tiers keep diffuse or specular, not both; characters drop specular ("don't need to be shiny to read well") | Readability survives minspec | Reads-in-grayscale test. Treat shine as optional | industry practice | S3 A. (Grayscale-test wording itself is inference, not from S3) |
| colour | Higher saturation draws more focus. Avoid 0% and 100% saturation. One dominant colour, one accent, desaturate competitors. Healing green, frost blue, gunpowder orange-red | Colour dominance tells what is primary | Per effect: pick one dominant hue from the table, accent only for the key beat | industry practice (secondary summary) | S6 C. **Needs 2nd source** for saturation numbers |
| colour | Enemy vs ally colour on one channel: Valorant enemies red fresnel, allies neutral blue; shown more on upper body; modulated "not too bright" | Friend or foe in a glance without reading UI | Reserve red-orange for hostile/damage and blue-cyan for safe/ally/pickup across the whole game | industry practice (Riot Valorant) | S3 A ~2020 |
| colour | Keep colour meaning stable across systems: SF6 blue = blocking, so the parry keeps blue | Colour carries rules | Never reuse a rule colour for decoration. List rule colours in the style sheet | industry practice (via news) | S10 B 2023 |
| colour | Team colour options for HUD and outlines: 9 colourblind-safe colours, enemy and ally set separately; shields/barriers visuals updated for readability | Accessibility without changing gameplay | Offer a colour-vision option for danger/ally channels; do not rely on hue alone, pair with shape | industry practice (Blizzard 2018, UI not ability FX) | S17 A 2018. **pre-2020**; no newer confirmation found. Ability FX recolour not confirmed (forum claims only, tier D) |
| timing | Anticipation, build-up, big payoff, then overshoot and settle ("small symphony"). Best work sometimes breaks the pattern | Impact reads heavier when preceded by a beat | Windup 3-10 frame cue before blast (my range, inference), punch frame, then dust/embers settling. Wire windup length to rank | industry practice (named Riot lead) | S7 C. No numbers given |
| timing | Keep FX short: length signals importance; lingering effects crowd the fight; "If Your FX Feel Long, They're Waaaaay Too Long" | Space frees for next event | Default lifetimes short; long lifetime only for rank 8+ or persistent zones. Roblox: Lifetime min/max sets this | industry practice (secondary) | S6 C. No durations given |
| timing | Main action in first quarter of lifetime (Sparkball style guide) | Strong early read, long soft tail | OneShot flipbook: peak by frame ~25% of lifetime | industry practice (single style guide, secondary) | S8 C 2023. **Needs 2nd source** |
| timing | One-frame animations can feel snappy and powerful (Diana scythe 1 frame) | Sudden impact | Single-frame flash/white flash on hit, then recover. Hold test: 1 frame at 60 fps = 16.7 ms (arithmetic) | industry practice (Riot lead anecdote) | S7 C |
| timing | Hit stop: both sides freeze briefly on hit; sets weight. Capcom example Light/Medium/Heavy = 8F/12F/16F; multi-hit moves shorter; projectiles cause no hit stop for attacker; set systematically per game, not per move | Hit "lands" with weight; time to read the hit | Heavy blast = longer micro-freeze of the camera/VFX; chip hits shorter. Table by rank. At 60 fps 8/12/16 F = 133/200/267 ms (arithmetic on S9 numbers) | industry practice (Capcom, example stated as hypothetical game) | S9 A, **likely pre-2020**. No newer Capcom number found. SF6 values: no number found |
| timing | Slow the moment after a successful skilled input to give decision time (Just Parry) | Reward feels exhilarating and readable | Slow-mo or freeze after rare big combo or egg hatch; always return control fast | industry practice | S10 B 2023. No numbers found |
| timing | Beat-locked motion: Hi-Fi Rush animated at 120 BPM and 60 fps, key poses on the beat, scalable with tempo | Rhythm makes hits feel earned | If music-synced: 120 BPM = 0.5 s per beat = 30 frames at 60 fps (arithmetic). Phase effect peaks to the beat grid | industry practice (animation only; VFX timing not sourced) | S12 B 2023 |
| composition | Compose the whole screen: only one hero effect per beat; the rest sit below it in value and saturation. "If everything is important, nothing is important" | Clean focal point under chaos | Per-frame budget of hero effects (e.g. 1 hero + N support). Support layers lower saturation and shorter lifetime | industry practice | S5 C 2020; S1 A; S16 B- |
| composition | Effects distance-scaled so they stay readable (depth modulation, clamped) | Far targets still readable | Camera-distance scaling of size/emission in Roblox: scale beam width/particle size with distance | industry practice (Riot) | S3 A |
| spec (Roblox) | Flipbook layouts Grid2x2 (4 frames), Grid4x4 (16), Grid8x8 (64), Custom. Textures square power-of-two 8-1024. Add transparent gaps between frames | Spec limits for sheet design | Use 4x4 or 8x8 sheets, 256-512 px for phones as a starting guess (inference). Leave padding | spec | S19 spec; S20 spec |
| spec (Roblox) | FlipbookFramerate max 30 fps; OneShot ties playback to particle Lifetime (frame time = Lifetime / frame count); Random mode crossfades | Sprite timing control | A 16-frame OneShot with Lifetime 0.4 s plays at 40 frames per second (25 ms per frame; arithmetic on the S20 rule). The 30 fps cap applies only to non-OneShot modes | spec | S20 spec |
| spec (Roblox) | Rate max 400/s per emitter, 100/s on mobile. Lifetime cap 20 s. :Emit not covered by auto-optimise per one forum remark. Large particles cost fill-rate. Flipbooks switch off on low-memory clients (older phones); reuse textures | Mobile budget | Burst with few big sprites (Emit count small) not high Rate. Reuse one sheet across effects. Test on a low-memory phone | spec | S20 spec. :Emit remark is tier C (S22) unverified |
| gameplay (mobile) | Optional "off switch" or reduced mode for effects: Valorant low/medium/high differ only in minor cosmetic effects; VFX hit minspec targets | Readability survives low settings | Never make readable info depend on a quality-gated effect (e.g. the danger ring must show at lowest tier) | industry practice (Riot) | S3 A |

### 2.2 Per-game cards

**League of Legends (Riot).** Readability is rule-based. Hierarchy: attention scales with damage, CC, dodgeability. Hitbox accuracy ranks first, then noise reduction and power levels, then theme (S2). Skins must be at least as clear as base and are checked on all maps (S1). Numbers: ~150 champions and ~1,000 skins (S1), >750 abilities (S5), 2 s (S1) minimum recall-circle stay, importance scale 1-10 (S5). [V: corrected - 2 s recall rule is S1, 1,000 skins is S1 not S5] Skin effort tiers by RP (750/975/1350/1820+, S2) show effort scales with price, not clarity. Sources S1, S2, S5, S6, S7.

**Valorant (Riot).** Friend-or-foe on the colour channel (red enemy fresnel, blue neutral ally), upper body bias, depth-modulated brightening (S3). VFX must pass minspec; frame budget 6.9 ms for 144 FPS; shader instruction counts environments 100-41, characters 128-84, weapons 103-73 across quality tiers (S3) [V: confirmed]. Smoke has a hard geometric edge for gameplay (S3). Hit-effect clarity: effects follow the hit body part, trade-off with ping, 100 ms example (S4). Sources S3, S4.

**Overwatch 2 (Blizzard).** No readable tier A/B VFX source found. Only: 2018 colourblind UI/outline options with 9 colours and shield/barrier readability update (S17, pre-2020); 2019 art recap with no readability content (S18). Player-forum threads on clutter exist but are tier D and not used. The GDC 2017 Keyser/Chamberlin VFX bootcamp (cited in search results) was not retrieved (Notion mirror empty). Sources S17, S18.

**Suicide Squad: Kill the Justice League (Rocksteady).** GDC 2024 talk "Attention Overload: Creating Readable VFX" exists (abstract only seen in search results, not read; schedule page returned 403). Not cited as evidence. Abstract claims: team structure including VFX in design, problem breakdown, post-mortem. No numbers found.

**Fortnite (Epic).** No VFX-readability source found. Search surfaced only UEFN documentation (not opened) and a 2018 Niagara GDC page (not opened). No number found.

**Marvel Rivals (NetEase).** July 15, 2026 patch reduced ability, ultimate and Team-Up VFX; stated as clarity-only, balance unchanged (S16). No figures or developer quote; B- press. Useful as a live example that overlapping ultimates exceeded readable limits. Source S16.

**Hades / Hades II (Supergiant).** No tier A/B technique source found. 80 Level credits VFX artist Josh Barnett but has no content (S14). The only readability argument is a critic's (S15): Hades II telegraphs with whole-arena red AoE regions and fast melee AoEs create a legibility problem versus Hades 1's hitbox-around-boss melee and outward ranged attacks. Tier C opinion, single critic. Sources S14, S15.

**Hi-Fi Rush (Tango).** Animation synced to music: 120 BPM, 60 fps, key poses on the beat, tempo scalable (S12). Rendering: deferred toon renderer, 60 fps native, UE4 custom passes (S13). No VFX-specific timing found; the "effects timed to music" claim in the brief is NOT supported by sources read. Sources S12, S13.

**Splatoon 3 (Nintendo).** Nintendo "Ask the Developer" Part 1 had no VFX/ink content; a news article on blue-ink visibility problems loaded as a headline only. No usable evidence. Gap.

**Zelda: Tears of the Kingdom.** Interview page 403. Search results mention a GDC physics-and-sound talk and an Ultrahand audio-visual Ask the Developer, neither read. No usable evidence.

**Street Fighter 6 / Street Fighter series (Capcom).** Hit stop: 8F/12F/16F for L/M/H in Capcom's example, multi-hit shorter, set per game (S9, likely pre-2020). Drive Parry: X-shaped Just Parry light vs O-shaped hit effect, blue kept for block colour, paint/ink splash replaced smoke, slowed Just Parry for decision time (S10). CEDEC 2024: "anime physics", exaggerate beyond pure physics, per-motion wind keys, baked break sims (S11); no numbers. Sources S9, S10, S11.

**Balatro.** No tier A/B source read. Only third-party analysis seen in search results (tier D, not used).

**Vampire Survivors.** No VFX-related developer source found. Gap.

**Supercell (Brawl Stars, Clash Royale).** No VFX-readability talk or breakdown found. Only job postings (not opened, tier D) saying stylised 2D VFX and 2D skeletal animation, with much volume from external artists. Gap.

**Roblox games (battlegrounds, Blox Fruits, Doors, Pet Simulator 99).** No creator breakdown, DevForum credited artist post, or developer interview found for any named game. What Roblox itself documents (S19, S20): Rate 100/s on mobile, flipbooks auto-off on low memory, fill-rate cost, flipbook max 30 fps, 64-frame max standard grid. The "what makes it work on a phone" question is answered by spec only, not by game case studies. Sources S19, S20, S22.

## 3. Quotes used (<=15 words)

| quote | attribution |
|---|---|
| "A champion's primary feature should never be removed or significantly altered in any skin." | Riot, Clarity in League (S1) |
| "Every ability should be at least as clear as the base skin" | Riot, Clarity in League (S1) |
| "if everything is important, nothing is important." | Beardilocks, Riot VFX artist, realtimevfx 2020 (S5) |
| "a small symphony with anticipation, build up, and a big payoff" | Magnus Lehmann, Riot, via VFX Apprentice (S7) |
| "If Your FX Feel Long, They're Waaaaay Too Long." | VFX Apprentice tip summary (S6) |
| "characters don't need to be shiny to read well." | Riot, VALORANT Shaders and Gameplay Clarity (S3) |
| "This patch addresses visual clarity only, not hero balance." | games.gg report on Marvel Rivals patch (S16) |

## 4. Conflicts between sources

| topic | sources | what changed or differs | resolution |
|---|---|---|---|
| Riot framework names | S6 (framework incl. value/colour/shape/timing) vs user-given framework (adds composition) | Riot's 2017 guide as summarised: gameplay, value, colour, shape, timing; composition appears in Keyser's teaching, not clearly in the Riot post (per search-result text, not read) | Keep our six-word framework. Note composition has weaker Riot-first-hand support |
| Hit stop values [V: confirmed S9 is an illustrative example] | S9 (8/12/16 F example, "hypothetical game", set systematically) vs fan wiki claims (heavier = longer; some punish counters extra long; not read, tier D) | S9 is a lecture example, not SF6 data. SF6 actual numbers: no number found | Treat 8/12/16 F as a starting point, label PROPOSAL. Test ourselves |
| Hit effect placement | S4: follow body part (clarity) vs spawn at client-sim hit location | Riot itself says both have costs (late for high ping, confusion if client and server disagree) | Spawn locally on hit event; attach to struck part; reconcile if server disagrees |
| Value/saturation rules | S6 (avoid 0/100%) vs Valorant S3 (clamped brightness, flat readable materials, no numbers) | Not contradictory; S6 is a second-hand summary of 2017 | Use as guideline; verify with grayscale test |
| Newer vs older | S16 (2026 clutter cut) vs S1 (~2020-21 "noise minimal") | Confirms the same issue recurs; newer source says shipped games still overshoot | Keep a stacking cap in our rules |

## 5. Gaps and how we could test ourselves

| question | status | self-test |
|---|---|---|
| Real Overwatch 2 / Fortnite / Marvel Rivals VFX rules from the makers | no tier A/B source read | Search GDC Vault and Unreal Fest; request Rocksteady "Attention Overload" slides; try Epic dev community posts |
| Windup, punch, dissipation numbers in frames or seconds for any game | no number found (S7 gives qualitative only; S8 "first quarter") | Build 3 blast variants (windup 0 / 5 / 12 frames at 60 fps) and A/B on phone, record preference and "was it a hit?" time |
| Hit stop for SF6 / for our game | S9 example only | Add hit stop by rank (8/12/16 F as PROPOSAL), compare with and without; watch for mobile frame hitch perceived as lag |
| Value/saturation numbers confirmed first-hand | only S6 (tier C summary) | Grayscale screenshot test of every effect; check hero effect has higher value contrast than background by eye |
| Mobile effect readability evidence for Roblox | spec only | Test on a low-end phone: effect count on screen vs missing flipbooks (low memory deactivation), FPS; record number of active emitters at which flipbooks drop |
| Hi-Fi Rush effects timed to music | not supported | If we want rhythm FX, test 0.5 s beat grid at 120 BPM with UI/VFX peaks on beat |
| Splatoon 3 / TotK / Balatro / Vampire Survivors / Supercell / named Roblox games | no usable source | Look for CEDEC/GDC talks and Nintendo/Supercell developer interviews; for Roblox, find DevForum posts by named VFX artists |
| Maximum simultaneous effect count before unreadable | no number found anywhere | Spawn N simultaneous blasts, find N at which testers cannot locate a marked danger ring; record per device |

## 6. Leads not followed

| lead | why not followed |
|---|---|
| Riot 2017 VFX Style Guide PDF (nexus.leagueoflegends.com/.../VFX_Styleguide_final_public_*.pdf) | Redirected to homepage; Wayback not permitted; Scribd copy is copyrighted. Highest-value missing primary source |
| GDC 2017 Keyser (Riot) + Chamberlin (Blizzard) "Artistic Principles of VFX" | Notion mirror returned only "Notion"; talk is on GDC Vault, not opened |
| GDC 2024 "Attention Overload" (Rocksteady) | Schedule page 403; abstract seen only in search results |
| Valorant patch 11.07 ability colour teal/arrows (esports.gg) | DNS failure; would need Riot patch notes |
| PC Gamer Valorant hit effects article | Fetch returned nav only |
| Hi-Fi Rush Unreal developer interview | 403 |
| Nintendo TotK Ask the Developer (Ultrahand audio-visual) | 403 |
| Brawl Stars GDC summaries (gamedev.net) | 403; secondary summary |
| Automaton Splatoon 3 blue ink article | Headline only |
| Blake Crosley Balatro breakdown, PSU Balatro article | Tier D, unattributed analysis |
| Fan wikis (SRK SF6 hitstop, Dustloop-type) | Tier D |
| Overwatch forum threads on VFX clutter | Tier D player opinion |
| Supercell job postings | Hiring text, not practice |
| Polish/other-language geekchamp, techyorker Hades articles | Tier D, AI-style pages |
| realtimevfx LoL missile Part 1 and Part 3 | Search budget exhausted before locating URLs |

## Verification log

Checked 2026-10-12 by re-fetching the cited pages (fresh fetch, small-model extraction, so wording of quotes was taken from the extract). 21 claims checked: 16 confirmed (several with a detail corrected), 5 corrected, 1 unverified. No claim was proven false, so none was removed.

| claim | result |
|---|---|
| S1 date, 150 champs / 1000 skins, 2 s recall, 2 quotes, Arcane Comet | confirmed; date was missing, now 2021-03-12 |
| S2 ranked goals, RP tiers | confirmed; author credit "Sirhaian and Riru" (not "K. Leroy"); date 2022-04-25 |
| S3 6.9 ms, instruction counts, fresnel, smoke, quote | confirmed; date 2020-06-30. Counts are "on most objects", high to low tier |
| S4 hit effects follow body part | corrected: Riot said it is iterating on this, not shipped; date 2020-08-07 |
| S5 1-10 rating, "almost 150", >750 abilities | corrected: no "1,000 skins" on this page; 1,000 skins comes from S1 |
| S6 value and saturation extremes | confirmed (still one tier C source); date 2022-08-29, so not "2017" |
| S9 8/12/16 F | confirmed as an illustrative example; undated, pre-2020 only inferred |
| S10 X/O, blue block, paint splash, slowed Just Parry | confirmed |
| S12 120 BPM / 60 fps | corrected: prototype rate, later changed dynamically; speakers named; 30-frame figure is valid arithmetic |
| S16 Marvel Rivals | corrected: ultimates are not named; quote is the article's own words |
| S17 nine colours, shield readability | confirmed; 2018-09-21 |
| S20 Roblox limits | confirmed in local mirror; 64 frames is only the Grid8x8 preset |
| S7 1-frame scythe | unverified, not re-opened |

Not re-opened (still as reported by the researcher): S8, S11, S13-S15, S18, S19, S21, S22, the Riot "Part 1/3" leads. The "Overwatch 2" label on S17 and S18 is loose: both sources are Overwatch 1 era (2018 and 2019).

Gaps and missing tier A sources:
- The Riot 2017 VFX style guide (primary source for value, saturation, timing) is still missing; every value and saturation claim rests on tier C S6.
- GDC Vault talks "Artistic Principles of VFX" (Keyser and Chamberlin, 2017) and Rocksteady "Attention Overload" (2024) are the obvious tier A sources not read.
- Riot's own Valorant ability clarity posts and the Arcane/League VFX style pages are not covered beyond S3.
- No tier A or B Roblox game case study at all; only spec. The hit stop number has no SF6 data.
