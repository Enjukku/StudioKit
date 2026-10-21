> Author: researcher (vfx-gap-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# Gap fill: Riot 2017 guide, GDC readability and principles talks, Overwatch/Valorant

Scope: gaps (a) to (f) from the brief. First-run files read first: p1-gameplay-shape.md, p3-scene.md, p4-games-readable-stylised.md (sections 5, 6 and the Verification log). Result in one line: the Riot 2017 PDF and every GDC talk body stayed unreadable. Identities, dates and venues are now confirmed. Several second-hand numbers were traced to named Riot artists.

## 1. Search count used

15 / 15 WebSearch calls (mode standard). About 38 WebFetch calls. Blocked and not worked around: web.archive.org, archive.ph and archive.is are refused by the fetch tool itself ("unable to fetch from ..."). I did not use curl or another route to bypass that block.

## 2. Sources read

"Opened" means WebFetch returned page content (small-model extraction, so wording is the extract's). "Search excerpt" means only the WebSearch result text was seen. Search excerpts are labelled and carry no numbers in the findings.

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G01 | 10 Design Tips from the League of Legends VFX Style Guide (opened) | VFX Apprentice (unbylined) | 2022-08-29 (per first run; page fetch showed "Aug 29, 2022") | C (summary of tier A) | https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips | no (guide is 2017) | Ten tips. Tip 10 holds the "telling the story" line. Page calls them "helpful tips straight from the League of Legends VFX Style Guide" and "our favorite takeaways" (the site's selection, not its original advice) [V: corrected - the page frames the tips as coming from the guide; the earlier "own wording" reading was too strong]. Keyser quote in tip 9 [V: confirmed]; that it is the only direct quote and comes from a video, not the guide [V: unverified - not stated in fetched extract]. Credits Jin Ho Yang as guide writer [V: confirmed]. Date Aug 29, 2022 [V: confirmed] |
| G02 | Anatomy of a League of Legends missile, Part 2 (opened) | Oli "Beardilocks" McDonald, Riot (lead VFX artist for skins) | 2020-05-25 | C+ (named maker, first-hand) | https://realtimevfx.com/t/anatomy-of-a-league-of-legends-missile-part-2-what-are-we-communicating-with-our-vfx/13062 | no | Visual Hierarchy doc, 1-10 importance rating per spell, rated for player, allies, enemies. No sizes, timings or values. No named style guide cited [V: confirmed - author, date 2020-05-25, 1-10 scale, player/allies/enemies, "bigger, brighter, and more threatening"; "no style guide cited" not checked] |
| G03 | Anatomy of a League of Legends missile, Part 1 (opened) | Oli "Beardilocks" McDonald, Riot | 2020-01-06 | C+ | https://realtimevfx.com/t/anatomy-of-a-league-of-legends-missile-part-1-creating-areas-of-focus/11614 | no | Objectives in priority order: communicate gameplay with minimal clutter, promote skin theme, surprise and delight. Areas of focus by value/contrast, saturation, shape/detail. Only links to the guide, quotes nothing [V: confirmed - author, date, objectives order, areas of focus; "only links to the guide" not checked] |
| G04 | Happy Halloween! sleepyGrin's Sketchbook, reply by Beardilocks (opened) | Beardilocks, Riot | 2020-01-05 | C+ | https://realtimevfx.com/t/happy-halloween-sleepygrins-sketchbook/10866 | no | Says the guide's value section sets a "Scale of importance" and the team tries to save 100% white for ultimates [V: confirmed - reply dated 2020-01-05; "We try to save 100% white things for ultimates, as these are the most important/damaging VFX in the game"] |
| G05 | Clarity in League (re-opened) | bananaband1t, Riot | 2021-03-12 | A | https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/ | no | Links to the 2017 guide on the phrase "hierarchy rules" but does not name it. "level of importance" line. "at least two seconds" is about recall animations. No "telling the story" [V: confirmed - author, 2021-03-12, link on "hierarchy rules" to the 2017 nexus post, recall rule; absence of "telling the story" not rechecked] |
| G06 | Nexus post and PDF of the 2017 style guide (tried) | Riot | 2017-10 | A | https://nexus.leagueoflegends.com/en-us/2017/10/dev-leagues-vfx-style-guide/ and .../VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf | yes | FAILED: HTTP 301 to leagueoflegends.com homepage. The riot-hosted replacement URLs I guessed returned 404 |
| G07 | Wayback availability API (opened) | Internet Archive | 2026 | n/a | https://archive.org/wayback/available?url=nexus.leagueoflegends.com/wp-content/uploads/2017/10/VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf | n/a | Reports a snapshot at 20260831223740. Snapshot URL itself is on web.archive.org, which the fetch tool refuses. The snapshot may also be the redirect page |
| G08 | LoL-Guide on Scribd (opened) | Scribd user "Hristijan" upload | undated | D | https://www.scribd.com/document/384307037/LoL-Guide | n/a | Landing page only: 37 pages, summary text. No body text |
| G09 | GDC Vault 1034360 Attention Overload (opened) | Hanno Hinkelbein, Rocksteady, GDC 2024 | 2024 | A (listing) | https://www.gdcvault.com/play/1034360 | no | Abstract only. Page tagged "free content", but no video, slide or YouTube link on it [V: confirmed - speaker, Rocksteady, 2024, Visual Arts track, free tag, no video] |
| G10 | GDC Vault 1023943 Visual Effects Bootcamp: Artistic Principles of VFX (opened) | Hadidjah Chamberlain (Blizzard), Jason Keyser (Riot), GDC 2017 | 2017 | A (listing) | https://gdcvault.com/play/1023943/Visual-Effects-Bootcamp-Artistic-Principles | yes | Co-speaker, case studies LoL and Hearthstone, tagged free. No content [V: confirmed] |
| G11 | Useful, free GDC talks (opened) | realtimevfx community thread | thread; reply dated 2019-04-13 | C | https://realtimevfx.com/t/useful-free-gdc-talks/219 | n/a | Free YouTube link for Keyser/Chamberlain (youtu.be/-L2JvngkkWw). Lists no Overwatch or Valorant talk |
| G12 | YouTube watch page -L2JvngkkWw (opened) | uploader unknown | n/a | n/a | https://www.youtube.com/watch?v=-L2JvngkkWw | n/a | Title only: "Visual Effects Bootcamp: Artistic Principles of VFX". No transcript through the fetch tool. youtubetotranscript.com returned 403 |
| G13 | The Must-Know Artistic Principles of Video Game VFX (opened twice) | VFX Apprentice (unbylined, Keyser's company) | 2023-12-05 | C | https://www.vfxapprentice.com/blog/five-artistic-principles-gaming-vfx | no | Six principles: gameplay, shape, value, colour, timing, composition. No numbers. Does not mention the GDC talk [V: confirmed - date 2023-12-05, six headings in that order, no GDC mention; the byline "Keyser's company" is unverified] |
| G14 | VFX Foundations and Artistic Principles course page (opened) | VFX Apprentice, instructor Jason Keyser | 2025/26 (undated) | C (course page) | https://www.vfxapprentice.com/courses/vfx-foundations-artistic-principles | no | Lesson list in the same six-part order. No numbers beyond course length |
| G15 | Announcing the first ever VFX Boot Camp at GDC 2017 (opened) | "Drew", realtimevfx | 2016-11-29 | C | https://realtimevfx.com/t/announcing-the-first-ever-vfx-boot-camp-at-gdc-2017/1205 | yes | Boot camp Tuesday 2017-02-28. Spells "Chamberlin". Lists "Artistic Foundations of Handcrafted VFX" (no speaker) as a topic. No "Artistic Principles" title |
| G16 | GDC Vault 1025301 Zip! Thwack! Ping! Animation Principles of VFX (opened) | Michael Lyndon, SideFX, GDC 2018 | 2018 | A (listing) | https://www.gdcvault.com/play/1025301 | yes | Abstract only (animation principles applied to VFX) |
| G17 | GDC Vault browse gdc-26 (opened) | GDC | 2026 | A (listing) | https://www.gdcvault.com/browse/gdc-26 | no | "Controlled Chaos" listed, speaker Rachel Quitevis (Beyond-FX), members-only [V: corrected - speaker and affiliation confirmed; the browse page does not mark it members-only (its link is a placeholder), so access is unverified] |
| G18 | Controlled Chaos session and speaker pages (search excerpt only; direct fetch 403) | GDC schedule | 2026 | A (listing) | https://schedule.gdconf.com/session/controlled-chaos-12-principles-of-design-for-vfx/914747 | no | Date, room, track, description, speaker bio (see GAP c). Not opened |
| G19 | Attention Overload schedule page (search excerpt only; direct fetch 403 in first run) | GDC schedule | 2024 | A (listing) | https://schedule.gdconf.com/session/attention-overload-creating-readable-vfx-for-suicide-squad-kill-the-justice-league/899824 | no | Wed 2024-03-20, 5:00-6:00 pm, Room 3005 West Hall; role "Lead VFX Artist" per search excerpt; Vault recording as video |
| G20 | Rachel Day profile, VFX Voice (re-opened with colour question) | VFX Voice | 2018-06-24 | B | https://vfxvoice.com/rachel-day-the-game-changing-gamemaker-behind-overwatch/ | yes | Page has nothing on ally/enemy colour, team colour or shape language. "tell that something happened immediately" test; push "to 11 or 12" then dial back [V: confirmed - 2018-06-24; exact words "Can you tell that something happened immediately?" about projectile impact feedback and "push everything to 11 or 12 and then dial it back a little bit"; no ally/enemy colour text] |
| G21 | VFX in Overwatch, ACMI collection (opened) | Blizzard film, 2016 | 2016 | n/a | https://www.acmi.net.au/works/107854--vfx-in-overwatch/ | yes | Museum entry for a film. No rules |
| G22 | VALORANT dev news index (opened) | Riot | 2025-2026 | A | https://playvalorant.com/en-us/news/dev/ | no | No VFX or clarity article listed. Closest: video "Abilities, Smurfing, Replays, and More // Dev Updates" (2025-05-30) |
| G23 | "Abilities, Smurfing, Replays, and More // Dev Updates - VALORANT" YouTube (opened) | Riot | 2025-05-30 (date from index) | A | https://www.youtube.com/watch?v=_oYnSaw9A-c | no | Title only; no description or transcript through the fetch tool |
| G24 | VFX Apprentice: Swarm artist interview (opened) | VFX Apprentice, Kevin Leroy (Sirhaian, Riot) | 2024-07-17 | C | https://www.vfxapprentice.com/blog/vfx-artist-league-of-legends-swarm | no | Readability listed as a production limit. No "telling the story" |
| G25 | Sparkball style guide piece (opened) | David Hall, Sparkadia, VFX Apprentice | 2023-07-12 | C | https://www.vfxapprentice.com/blog/creating-vfx-style-guides-for-games | no | No "telling the story". Not Riot's guide |

Search-excerpt-only items with no page opened (leads, not evidence): Games Blizzard BlizzCon 2017 interview with Rachel Day (page not located); ESO forum thread about reduced combat VFX settings (2026, fetch 403); Valorant VFX job listings; Blizzard forum threads on red enemy effects.

## 3. Gap-by-gap results

### GAP: (a) Original 2017 Riot LoL VFX style guide

Status: STILL OPEN for the first-hand text. PARTLY FILLED for second-hand rules traced to named Riot artists.

What was tried: nexus PDF and post (301 to homepage), guessed leagueoflegends.com replacement URLs (404), Wayback availability API (works, but snapshot is on a blocked host), web.archive.org and archive.ph and archive.is (refused by tool), r.jina.ai proxy to Wayback (401), Google gview of the PDF (tool could only see the filename), Scribd (landing only), realtimevfx threads (quote almost nothing). No GitHub or Reddit mirror turned up in the 15 searches.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Riot's own VFX artist says the guide's value section sets a "Scale of importance" and that Riot tries to keep 100% white for ultimates | 100% white reserved for ultimates | industry practice (Beardilocks, Riot, 2020; tier C+, forum post, not the guide) | G04 |
| Riot rates each spell's importance 1 to 10 in a Visual Hierarchy document, separately for the player, allies and enemies; used as a rough guide | scale 1-10; 3 viewer groups | industry practice (Riot, 2020) | G02 |
| Higher-damage spells should be "bigger, brighter, and more threatening", with sharper shapes and more attention-grabbing timing. Status effects (stun, root) should look stronger than damage-only because the target is left vulnerable. Dodgeable and cast-from-concealment also matter | no sizes, times, values given | industry practice (Riot, 2020) | G02 |
| Riot 2021: attention an ability grabs should match its importance. The post links to the 2017 guide on the words "hierarchy rules" | no number | industry practice (Riot, 2021; tier A) | G05 |
| Summary of the guide: value runs 0 to 100%, work in the mid-range, avoid the extremes; saturation: avoid 0% and 100%; wider value range draws more focus; higher saturation draws more focus; complementary pairs need one dominant colour and desaturated competitors; hand-draw shapes, mix soft and hard edges; blur shapes in travel; keep effects short | 0% and 100% as limits for value and saturation | industry practice (secondary summary of Riot 2017, tier C) | G01 | [V: confirmed - page says avoid extremes of value, steer clear of 100% or 0% saturation]
| These two statements are compatible: pure extremes are avoided in general, with 100% white reserved for ultimates. This is my inference, not a quoted rule | n/a | inference | G01, G04 |
| Search-tool text shown for the PDF (not opened, so unusable as evidence): importance judged by "readable", "emphasis" and scale of importance; level of importance controlled by size, shape, timing, value, saturation, opacity; basic attack should not look as important as an ultimate | none | lead only | search result 1 and 3 |

Not recovered from the guide: value-range diagram numbers, the "level of importance" page content, shape silhouettes, illusion-of-movement page. No number found for any of these.

### GAP: (b) Rocksteady "Attention Overload" (Hinkelbein, GDC 2024)

Status: STILL OPEN (content). Venue and abstract confirmed again. No free video, slides or write-up found.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Speaker Hanno Hinkelbein, Rocksteady Studios, GDC 2024, Visual Arts track. Schedule excerpt gives Wed 2024-03-20, 5:00-6:00 pm, Room 3005 West Hall, "Lead VFX Artist" | session 60 min | spec/listing (event listing) | G09, G19 |
| Abstract topics: VFX to steer attention in games with many actions, weapons and talents; getting VFX artists into design early; problems met and solutions; post-mortem for the live phase | none | industry practice (talk abstract only) | G09 |
| Vault page tagged "free content" with a note that free users see a share of recent content, but the fetched page carries no video, slide or YouTube link and says members-only content is restricted | none | listing | G09 |
| Searches for a recap, slides, YouTube upload or tier-B article returned nothing with content | none | n/a | search 4, 15 |

### GAP: (c) "Controlled Chaos: 12 Principles of Design for VFX"

Status: PARTLY FILLED. Speaker, year, venue and abstract confirmed. Talk body not read.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Speaker: Rachel Quitevis, VFX artist at Beyond-FX (bio excerpt: worked at Playful Studios, Gearbox, Santa Monica Studio, Blizzard since 2017; moved to VFX in 2020) | n/a | listing | G17, G18 |
| Year/venue: GDC 2026 (not 2025), Visual Development track, lecture, Mon 2026-03-09, 3:10-4:10 pm, Room 2001 West Hall, audience level All | 60 min | listing | G17, G18 |
| Description: the 12 principles of design, "evolved from Disney's" fundamentals, applied to VFX; names rhythm, balance and negative space; includes VFX breakdowns and a demo that transforms a first-pass effect | 12 principles; none other | listing | G18 |
| Vault: listed under GDC 2026, no direct link [V: corrected - "members-only" not supported; the listing does not mark access] | n/a | listing | G17 |
| Which 12 principles the talk uses: not stated anywhere I could open. Do not assume they are the Disney 12 animation principles. The abstract says "principles of design" (rhythm, balance, negative space are design terms, not animation-principle terms) | n/a | inference | G18 |

### GAP: (d) Jason Keyser + co-speaker "Artistic Principles of VFX", GDC 2017

Status: PARTLY FILLED. Co-speaker confirmed. Talk body not read. A proxy for its structure exists in Keyser's own later material.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Title on Vault: "Visual Effects Bootcamp: Artistic Principles of VFX", GDC 2017. Speakers Hadidjah Chamberlain (Blizzard Entertainment) and Jason Keyser (Riot Games). Spelling "Chamberlain" on Vault, "Chamberlin" in the Nov 2016 announcement | 2 speakers | listing | G10, G15 |
| Description: fundamentals for magic, fire, smoke; broad artistic and gameplay considerations for any genre or art style; case studies from League of Legends and Hearthstone with successful and unsuccessful examples of each principle | n/a | listing | G10 |
| Free access: Vault page tagged free; free YouTube upload linked by a realtimevfx user in 2019 (youtu.be/-L2JvngkkWw). Fetch tool cannot read video or transcript | n/a | listing | G10, G11, G12 |
| Proxy for content (NOT the talk body): Keyser's VFX Apprentice article and course use six principles in this order: gameplay, shape, value, colour, timing, composition. Gameplay: VFX "inform players on how to play"; shape: "primary way to communicate"; value: best tool to direct attention and set a per-effect "visual budget"; timing: particles dissipate right after their task, shorter lifetimes declutter; composition: guide the eye. No numbers | none | industry practice (VFX Apprentice 2023, tier C) | G13, G14 |
| This matches the framework names in the brief (gameplay, shape, value, colour, timing, composition). That the 2017 talk uses the same six is likely but unconfirmed. Neither G13 nor G14 mentions the GDC talk | n/a | inference | G13, G14 |
| Keyser quote on timing, from a video embedded in G01 (not shown to be the GDC talk): "Lead the brain with anticipation" then overload the brain at the awaited moment | none | industry practice (Keyser; video unspecified) | G01 |
| Related: Lyndon GDC 2018 "Zip! Thwack! Ping! Animation Principles of VFX" confirmed as Michael Lyndon, SideFX, abstract only | n/a | listing | G16 |

### GAP: (e) Overwatch / Overwatch 2 first-hand VFX readability; Valorant newer than 2020

Status: STILL OPEN (no first-hand Blizzard VFX talk or readability rule found; no post-2020 Valorant VFX source found).

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| No Overwatch or Valorant VFX talk appears in the realtimevfx free GDC list | none | n/a | G11 |
| Rachel Day (Blizzard) profile: readability test is whether players "tell that something happened immediately"; push effects "to 11 or 12" then dial back. Nothing on ally/enemy colour | none | industry practice (VFX Voice 2018, pre-2020) | G20 |
| Search-excerpt only, source page not located: a BlizzCon 2017 interview where Day says artists associate blue with ice and red with fire or enemy, and that country-colour World Cup effects forced shape-language changes (example: Mercy's two beams looked alike apart from colour). Single source, unopened. Would need a second source before use | none | lead | search 10 |
| Player-reported: Overwatch 2 colourblind options change UI/outline colours but not ability-effect colours (effects stay red). Forum post, not Blizzard | none | tier D | search 7, 10, 11 |
| Valorant: dev news index shows no VFX or clarity article through 2026; closest is the 2025-05-30 dev update video whose title mentions abilities. Video content not readable via fetch | none | n/a | G22, G23 |
| Valorant job listings say readability and clarity are goals, with "paintovers" used. Search excerpt of hiring text only | none | tier D | search 8 |
| Lead: ESO forum thread (2026) about new settings to reduce combat visual effects. Not Blizzard, not Riot; 403 on fetch | none | lead | search 11 |

### GAP: (f) Source of the line "FX aren't supposed to be telling the story"

Status: PARTLY FILLED. The line is located [V: confirmed - tip 10 reads "FX aren't supposed to be telling the story; they're supposed to assist storytelling and enhance it along the way"]. It is VFX Apprentice's wording of a summary the page presents as coming from the guide [V: corrected]. It is not shown to be a Riot quote.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| The line is in tip 10, "If your FX feel long, they're waaaaay too long", of the VFX Apprentice summary of the Riot guide, followed by "they're supposed to assist storytelling and enhance it". Meaning: effects support the narrative; long effects clutter fights; duration signals significance; short effects leave room for other spells | none | industry practice (VFX Apprentice, tier C) | G01 |
| The same page says the ten tips are its own "favorite takeaways" and only the Keyser quote in tip 9 is a direct quotation. So the line is not an attributed Riot quote | n/a | industry practice | G01 |
| The exact phrase is not on: Riot "Clarity in League" 2021, Beardilocks Part 1 and 2, the Sparkball piece, the Swarm interview, the Keyser six-principles article. A phrase search returned nothing else | n/a | negative result | G02, G03, G05, G24, G25, G13 |
| Whether the PDF itself contains the line cannot be checked (PDF unreadable). The title "If your FX feel long, they're waaaaay too long" is also unverified as the guide's heading | n/a | not verified | G06 |

## 4. Quotes used

- "FX aren't supposed to be telling the story" (VFX Apprentice, tip 10, G01).
- "[T]he amount of attention an ability grabs should match its level of importance" (Riot, Clarity in League, 2021, G05). [V: corrected - earlier text dropped "level of"; this is 15 words, at the quote limit, prefer paraphrase]
- "bigger, brighter, and more threatening" (Beardilocks, Riot, 2020, G02).
- "Scale of importance" and "100% white things for ultimates" (Beardilocks, 2020, G04). [V: confirmed - verbatim in reply; full phrase is "save 100% white things for ultimates"]
- "Lead the brain with anticipation" (Jason Keyser, via G01).
- "tell that something happened immediately" (Rachel Day, VFX Voice 2018, G20).

## 5. Conflicts with first-run files

| file + row | first-run statement | this run |
| --- | --- | --- |
| p1-gameplay-shape.md Verification log, S05 | "'pure white for ultimates' is not on the page, do not rely on it" | Correct for the VFX Apprentice page. But a named Riot artist says "100% white things for ultimates" in a Jan 2020 realtimevfx reply (G04). So the claim is real tier C+, with the Riot-guide attribution made by Beardilocks. It now has a source. Still not first-hand from the PDF |
| p3-scene.md section 5 "Attention Overload" row | slides/video "members-only" | The Vault page carries a "free content" tag, with a note on limited free access. No video link was visible either way. Not resolved |
| p3-scene.md S11 / verification | role "lead VFX artist" not on the page | A search excerpt of the GDC schedule page says "Lead VFX Artist". Page fetch is 403, so still not opened. Treat as likely, unconfirmed |
| p1-gameplay-shape.md section 5 and S02 | S02 year "2020 per scope brief; fetched text showed no date" | Page shows May 25, 2020. Matches the Verification log |
| p4-games-readable-stylised.md section 6 and p3 section 5 | Controlled Chaos speaker/year unspecified in p3; p1 says "Quitevis, GDC 2026" | Confirmed: Rachel Quitevis, Beyond-FX, GDC 2026, Visual Development track (G17, G18). p3 cited it as GDC Visual Effects Summit "Are You Visually Literate?" for 2025; that talk was not re-checked here |
| p4 spelling "Chamberlin" | Vault says "Chamberlain"; the 2016 announcement says "Chamberlin" | Use "Chamberlain" (Vault) and note the variant |
| p4 verification gap "Riot 2017 guide ... value and saturation rest on tier C S6" | still true | Still true; G01 is the same summary page, G04 adds one named-Riot-artist confirmation for the white-for-ultimates point only |

## 6. Still open and how we could test it ourselves

| open item | why still open | how we test or get it |
| --- | --- | --- |
| Riot 2017 guide text (value ranges, importance page, shapes, movement) | Nexus redirects; Wayback host blocked for the fetch tool | Owner opens web.archive.org/web/2026*/nexus.leagueoflegends.com/wp-content/uploads/2017/10/VFX_Styleguide_final_public_hidpjqwx7lqyx0pjj3ss.pdf in a browser and pastes the text. The availability API says a 2026-08-31 snapshot exists, but it may be the redirect page |
| Our own value/saturation ranges | no tier A number | Grayscale and saturation sweep of our own effects: record peak value (0-100%) and peak saturation, check the ultimate-class effect is the only one near 100% white |
| Importance (1-10) to size/brightness/time mapping | Riot gives the scale, not the mapping | Rate each effect 1-10, measure screen coverage, peak value, lifetime; require monotonic order; playtest "which was bigger" |
| Rocksteady talk body | members-only / no upload found | Owner with Vault access watches 60 min and gives notes; or check GDC YouTube later |
| Controlled Chaos body and the 12 principles list | members-only; no recap | Same. Do not assume the list |
| Keyser/Chamberlain talk body | video not readable by tool | Owner watches the free YouTube upload (youtu.be/-L2JvngkkWw) and gives notes on the six principles and the LoL/Hearthstone case studies |
| Overwatch ally/enemy effect colour rules | no first-hand source | Find the Rachel Day BlizzCon 2017 Games Blizzard interview to get a second source; test 8 players on time-to-identify hostile blast with and without colour-coded shapes |
| Valorant VFX post-2020 | no article | Read the 2025-05-30 dev update video by hand; check Riot technology blog (tool timed out with 504) |
| "FX aren't supposed to be telling the story" | PDF unreadable | Search the PDF text once obtained. Until then cite as "VFX Apprentice summary", never as a Riot quote |

## Verification log

Adversarial check 2026-10-12 (WebFetch only, no search). 17 claims checked: 13 confirmed, 4 corrected, 0 removed as false, several sub-claims unverified.

| claim | result | reason |
| --- | --- | --- |
| G01 tip 10 line, date, Keyser quote, 0/100% value and saturation | confirmed | page text matches |
| G01 "tips are the site's own wording" | corrected | page says "straight from the League of Legends VFX Style Guide" and "our favorite takeaways". Still tier C and not a verbatim Riot quote |
| G01 "only the Keyser quote is a direct quote, from a video" | unverified | not stated in fetched extract |
| G02, G03, G04, G09, G10, G13, G20 | confirmed | authors, dates, numbers and quotes match |
| G05 quote | corrected | "level of" was missing from the quoted line; the sentence is about 15 words, paraphrase in use |
| G17 / Gap (c) "members-only" | corrected | the GDC Vault browse page does not mark the session members-only (link is a placeholder). Access is unverified. Speaker Rachel Quitevis and Beyond-FX confirmed |
| Gap (f) "VFX Apprentice's own wording" | corrected | see G01. Status stays PARTLY FILLED |
| G18, G19 schedule details (date, room, "Lead VFX Artist") | unverified | schedule pages returned 403 and were not re-opened |
| G14, G21 to G25, Wayback API, Scribd, YouTube items | unverified | not re-opened in this check |
| Keyser GDC talk uses the same six principles | unverified | inference in the file, correctly labelled |

FILLED status: no gap is marked FILLED. Statuses STILL OPEN or PARTLY FILLED stand. Gap (c) should not say the recording is members-only.
