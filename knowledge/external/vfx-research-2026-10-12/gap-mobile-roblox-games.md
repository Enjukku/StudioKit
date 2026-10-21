> Author: researcher (vfx-gap-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# Gap fill: mobile VFX readability, Supercell, Wild Rift, Fortnite, Roblox games

Result in one line: the four gaps are mostly STILL OPEN at tier A/B. Searches returned job postings, not talks. What was found is listed below with honest tiers.

## 1. Search count used

15/15 WebSearch calls. About 27 WebFetch calls. DevForum and realtimevfx run on Discourse, so their `search.json` and `t/<id>.json` endpoints worked through WebFetch and cost no search budget (realtimevfx returned 429 once).

## 2. Sources read

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave |
|---|---|---|---|---|---|---|---|
| G1 | /Dev: Behind the Scenes of VFX Updates | Riot Sirhaian, Riot Riru (Riot) | 2022-04-25 | A (maker blog) | https://leagueoflegends.com/en-au/news/dev/dev-behind-the-scenes-of-vfx-updates | no | Readability outranks theme. No mobile or budget text. Same page as first-run S2 [V: confirmed - authors, date, both quotes, equal indicator sizes, no mobile mention] |
| G2 | What Riot Games Head of Creative Looks For in VFX Artists | Magnus Lehmann (Riot), interviewed by Jason Keyser (VFX Apprentice) | 2023-01-26 | C (named maker, interview) | https://www.vfxapprentice.com/blog/riot-games-head-creative-vfx-artist-needs | no | Timing structure and shape language. Nothing on mobile or Wild Rift in the text [V: confirmed - Lehmann/Keyser/2023-01-26 match; Wild Rift appears only in image filenames] |
| G3 | Technical Artist Summit: The Art of Not Reinventing the Wheel in Wild Rift Asset Pipeline | Sean Low (Riot), GDC | 2021 | A (abstract only) | https://www.gdcvault.com/play/1027061/ | no | Abstract is about an asset analysis tool. No VFX. Members-only [V: confirmed - Sean Low, GDC 2021, asset analysis tool, no VFX] |
| G4 | Art Directing VFX for Stylized Games | Kladis (Epic), Lindsey (Volition), Mitchell (Double Fine), Spurgeon (Motiga), GDC | 2017 | A (abstract only) | https://gdcvault.com/play/1023999/contactUs | yes | Abstract only. No numbers. Talk not opened (video not located) [V: confirmed - four speakers and affiliations match, GDC 2017, abstract has no numbers] |
| G5 | 5 creative pillars for designing brawlers (PocketGamer.biz) | Fernanda Oliveira (Supercell), Games First Helsinki | 2024-10-30 | B | https://www.pocketgamer.biz/5-creative-pillars-for-designing-brawlers-in-supercells-brawl-stars/ | no | Character design only. Nothing on VFX or readability [V: confirmed - Oliveira, Games First Helsinki, 2024-10-30] |
| G6 | Mobile games vfx (thread) | bgolus, Torbach, yunus, Unique and others (realtimevfx) | 2017-06 to 07 | C (named, several posters) | https://realtimevfx.com/t/mobile-games-vfx/2567 | yes | Mobile particle counts, overdraw, texture caps. Old engines [V: corrected - posts are dated 2017-06-21 to 2017-06-28; single posters per figure: bgolus (10 particles, few hundred, 1-2 frames), Torbach (40-50 embers), yunus (512x512)] |
| G7 | Genshin Impact console rendering (Unity Dojo slides) | Zhenzhong Yi (miHoYo) | 2021-06 | A (maker slides) | https://docswell.com/s/UnityJapan/KWRPQ5-210617-unity-dojo20211mihoyozhenzhongyi | no | Console renderer costs only. Nothing on VFX [V: corrected - talk first given at Unite Seoul 2020, slides posted 2021-06; 0.05 ms is a shadow-texture decompression and 2.6 ms is an original soft-shadow pass cost, so not a range of passes; 'mobile is the primary development platform' is confirmed] |
| G8 | Particles' Flipbook Release | DevForum user LightBeamRays (not flagged as staff, writes as "we") | 2022-10-21 | C | https://devforum.roblox.com/t/2029388 | no | Flipbook texture sizes 8x8 to 1024x1024 square power of two. Memory framing [V: confirmed - 8x8 to 1024x1024 square power of two, 2022-10-21; post not labelled staff] |
| G9 | Egg accessories from "The Hatch" Event have no VFX | DevForum users (idelww, others) | 2025-07-06 | D | https://devforum.roblox.com/t/3801221 | no | Players guess mobile performance is the reason. No staff reply. Lead only [V: corrected - thread started by AleksDema3; the mobile-performance guess is by idelww; the 'no staff reply' claim holds only as 'no visible staff label'] |
| G10 | Roblox Creator Docs, particle emitters (local mirror) | Roblox | current | spec | knowledge/external/roblox-creator-docs/effects/particle-emitters.md | no | Rate cap 400/s (100/s mobile), flipbook auto-deactivation on low memory [V: confirmed - docs line 212 and 410 of the local mirror] |
| G11 | Visual effects for mobile games: creating a clean visual effect for small screens (Nordberg, Flatfish Games Oy, 2020) | Jaani Nordberg, thesis | 2020 | thesis (title seen in search only) | https://www.theseus.fi/handle/10024/355124 | no | Fetch returned 403. Not read. Listed as a lead only |

Failed or empty: gamedev.net/news/4113 (403), Epic "Optimizing Fortnite Battle Royale for mobile" URL guess (403), Epic UEFN effects doc (no budget text), YouTube search page (no results in fetch), Theseus PDF (403), DevForum searches for named game VFX artists (zero results), realtimevfx "Wild Rift" (429).

## 3. Gap-by-gap results

### GAP: (a) Supercell VFX readability, effect size, budgets
Status: STILL OPEN.

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| No Supercell VFX talk, interview or blog on readability was found in 5 searches and the fetches | no number found | inference (absence) | search log |
| Supercell VFX art for Brawl Stars is partly outsourced; the in-house role gives direction and feedback (job text, so hiring text, not practice) | no number found | tier D lead | search result (hitmarker, supercell.com careers; not opened) |
| Supercell artist talk found (Oliveira, 2024) covers character pillars, "iconic simplicity", not effects | no number found | industry practice (Supercell artist, 2024), off-topic for VFX | G5 |
| GDC "Making of a Brawler" exists on GDC Vault; only teaser summaries seen | no number found | not read | search result only |

### GAP: (b) Other top mobile VFX readability sources (Genshin, Wild Rift)
Status: STILL OPEN for mobile (no Wild Rift or Genshin VFX number or mobile text at all). [V: corrected - was PARTLY FILLED. Riot G1 and G2 never mention mobile and G6 is tier C and from 2017, so only a general PC readability rule exists.]

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| No Riot source about porting League VFX to Wild Rift was found. Riot's only VFX-for-mobile text found is job postings (balance authenticity vs. reimagining; low-end performance budgets), not read in full | no number found | tier D lead | search results |
| Riot's PC VFX update policy: readability beats theme; spells "not too bright or too hard to see"; indicator sizes kept equal across skins | no size or opacity value | industry practice (Riot 2022) | G1 |
| Riot Head of Creative on timing: structure of anticipation, build-up, payoff, settle; best effects sometimes break the pattern | no number found | industry practice (Lehmann, Riot, 2023; tier C) | G2 |
| miHoYo's published rendering talk is console-only; it states mobile is the lead platform and the engine is customised for it | console passes 0.05 to 2.6 ms; not VFX | industry practice (miHoYo 2021), off-topic | G7 |
| Old but named mobile VFX advice: reduce desktop effects to roughly "10 particles"; high-end mobile "a few hundred" particles maybe low thousands; 40 to 50 ember billboards plus 2 to 3 boards plus a few trails for one effect; mobile textures often capped near 512x512; a flipbook explosion can read with 1 or 2 key frames (bright fireball then smoke) | 10; few hundred; 40-50; 512x512; 1-2 frames | industry practice (named artists bgolus, Torbach, yunus, 2017), pre-2020, Unity/UE4 era | G6 |

[V: confirmed] Second source for the G6 numbers: none found. They are tier C only, so treat as hypotheses.

### GAP: (c) Fortnite VFX first-hand
Status: STILL OPEN.

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| No Epic or Fortnite VFX readability or mobile-scaling talk found. Only GDC 2017 "Art Directing VFX for Stylized Games" (Epic speaker Bill Kladis) as an abstract | no number found | industry practice (abstract only), pre-2020 | G4 |
| Search results say Epic's Fortnite mobile work fed 100+ optimisations into Unreal Engine 4.20 (not opened, not VFX-specific) | 100+ (unverified) | tier D lead | search result |
| Epic UEFN effects doc has no budget or mobile text | no number found | spec | fetch |

### GAP: (d) Roblox games with strong VFX, official VFX material, what works on phones
Status: PARTLY FILLED (spec and one announcement only; no named game artist breakdown).

| finding | numbers | evidence level | source ids |
|---|---|---|---|
| No tier A to C breakdown by a credited VFX artist of The Strongest Battlegrounds, Blox Fruits, Doors, Pet Simulator 99, Jujutsu Shenanigans or Grow a Garden found. Search returned job posts and freelance gigs | no number found | absence | search log |
| No Roblox RDC 2023 to 2025 session on VFX found; RDC 2025 playlist exists on YouTube but was not opened | no number found | absence | search result (create.roblox.com RDC page) |
| Per-emitter rate cap 400/s, 100/s on mobile; flipbooks auto-deactivate on low memory (likely old phones); reusing textures costs less than unique ones | 400/s, 100/s | spec | G10 |
| Flipbook textures may be any square power of two, 8x8 to 1024x1024, added for memory control (announced 2022-10-21) | 8 to 1024 px | industry practice (Roblox announcement, tier C author flag) | G8 |
| Players speculate the Hatch event eggs lack particles for mobile performance; no staff answer | no number found | tier D | G9 |
| Common mobile levers named in many sources: particle count, light count, overdraw layers, texture size | no number found | inference | G6, G10 |

## 4. Quotes used

- "gameplay readability will always prevail over thematic resonance." (Riot Sirhaian and Riru, 2022, G1; page paraphrase as extracted)
- "spells should not be too bright or too hard to see." (Riot, 2022, G1)
- "Great VFX ooze amazing texture in timing." (Magnus Lehmann, Riot, 2023, G2)
- "try to think of how to reproduce that with, say 10 particles." (bgolus, realtimevfx, 2017, G6)
- "less is more." (Fernanda Oliveira, Supercell, 2024, G5)

## 5. Conflicts with first-run files

| file + row | conflict |
|---|---|
| p4-games-readable-stylised.md section 6, "Brawl Stars GDC summaries (gamedev.net)" | Still 403. Searches show the Brawl Stars GDC material is about character design, not VFX, so it is not a VFX source |
| p4-games-readable-stylised.md section 5, "Splatoon 3 / TotK / Balatro / Vampire Survivors / Supercell / named Roblox games" | Confirmed: no usable tier A to C source for Supercell or named Roblox games after 15 more searches |
| p9-p10-p11-access-perf-roblox.md section 6, robloxapi ParticleFlipbookTextureCompatible "1024 required" | G8 (2022 announcement) says any square power of two from 8x8 to 1024x1024 is allowed. This supports the first-run reading that the "1024 required" claim is outdated |
| p9-p10-p11 section 5, "mobile 100/s cap" | G10 confirms the 100/s mobile figure in the docs. Whether `Emit()` bypasses it is still unanswered |

## 6. Still open and how we could test it ourselves

| open question | test |
|---|---|
| Supercell effect size and readability on small screens | Not findable from public text so far. Own test: one blast at 3 sizes (radius as % of screen height: small, medium, large) on a 5-inch phone, 20 testers, record "where did it hit" accuracy and time |
| Wild Rift/Genshin effect budgets | Own test: spawn N simultaneous blasts on a low-end phone, find N where marked danger ring is missed or FPS under 30; also count live particles at Editor Quality Level 1 vs 10 |
| Fortnite mobile scaling | Own test: build quality-tiered variants (full, half emitters, no flipbook) and switch by `UserGameSettings.SavedQualityLevel`; compare readability and FPS |
| Roblox game artist breakdowns | Leads not opened: RDC 2025 YouTube playlist; YouTube behind-the-scenes from game studios; ArtStation by hand. Needs a human or a browser session; WebSearch did not index them |
| Nordberg 2020 thesis on small-screen VFX (G11) | Open the PDF manually from Theseus (403 to WebFetch); likely the best peer-style source for the (b) gap |
| GDC 2017 "Art Directing VFX for Stylized Games" and Riot 2017 style guide | Free on GDC YouTube channel; need a transcript fetch with the exact watch URL |
| Does Emit() obey the 100/s mobile cap | Emit 200 in one call on a phone and count particles on screen |

## Verification log

Checked 2026-10-12 by re-fetching G1 to G10 (G11 not re-opened, still unverified: Theseus returned 403 for the researcher; unverified). Search-result leads (hitmarker/Supercell careers, Epic 100+ UE4.20 optimisations, RDC 2025 playlist, GDC "Making of a Brawler") were not opened and stay unverified.

| claim | result |
|---|---|
| 5 quoted strings (section 4) | All present at or under 15 words. G1 "gameplay readability will always prevail over thematic resonance", "spells should not be too bright or too hard to see" confirmed as page text (fetch summarised the second; exact punctuation not seen). G2, G6 (bgolus, 2017-06-21), G5 "less is more" confirmed. [V: confirmed] |
| G6 figures | Confirmed but each rests on one poster in 2017; they are tier C, pre-2020. [V: confirmed] |
| G7 "console passes 0.05 to 2.6 ms" | [V: corrected] Mixed items, not a range of passes (see G7 row). |
| G9 poster | [V: corrected] Poster names fixed in the G9 row. |
| Gap (b) status | [V: corrected] PARTLY FILLED changed to STILL OPEN for mobile. |
| Gap (a), (c) STILL OPEN | Holds; the Oliveira talk, G3 and G4 contain no VFX numbers. [V: confirmed] |
| Gap (d) PARTLY FILLED | Holds: 400/s and 100/s mobile is in the docs mirror (spec, not tier A talk), flipbook 8 to 1024 from a non-staff-labelled announcement (tier C). [V: confirmed] |
| "About 27 WebFetch calls" | Not checkable. [V: unverified - no log] |

Claims removed as false: none.
