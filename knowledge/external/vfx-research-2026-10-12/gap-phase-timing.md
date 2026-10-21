> Author: researcher (vfx-gap-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# Gap fill: VFX phase timing (windup, punch, crescendo, follow-through, dissipation)

Scope: first-run files p1-value-colour-timing.md, p1-gameplay-shape.md, p2-p12-numbers-moments-review.md. Framework words as in the brief. Conversions: 1 frame = 16.7 ms at 60 fps, 33.3 ms at 30 fps, 41.7 ms at 24 fps (arithmetic, inference). Fetched text came back through a small summariser, so wording is "as returned by the fetch tool".

Bottom line: **still no tier A number per phase.** The best tier B number is one Riot VFX artist's "hit frame 0.1 s" (G10). Tier C named artists give frame counts for the punch (1-2 frames flash, 4-5 frames full burst) and for a 1-2 frame pre-blast distortion (G01, G02). One peer-reviewed study gives a hit-stop comfort window in seconds (G05). Both single-source claims (25% of lifetime, heal under 60 BPM) have **no second source** after this run.

## 1. Search count used

**11 / 15 WebSearch calls.** Used: Lyndon talk (1), Insomniac Spider-Man (2), Trümpler (3), 2XKO Riot (4), Sirhaian/Keyser/Chamberlin frames (5), Hallzy 25% (6), heal BPM (7), Riot style guide text (8), hit-stop user studies (9), 80 Level/fxguide/Game Developer phase breakdowns (10), Thomas Iché (11). About 40 WebFetch calls, of which roughly 14 failed (403, 405, 429, redirect, blocked host; see section 6).

## 2. Sources read

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G01 | Stylized Cartoon Explosion - Overwatch Inspired (thread, post 6) | Sirhaian (Riot VFX artist), realtimevfx | 2017-02-24 | C (named Riot artist) [V: corrected - removed 'second source G10 for the flash size': G10 gives a 0.1 s hit frame, not a flash size; G01 itself is confirmed: author, 2017-02-24, burst max 2 frames, 4-5 frames, 1-2 frames super bright] | https://realtimevfx.com/t/stylized-cartoon-explosion-overwatch-inspired/1767 | yes; no newer found | Burst not longer than 1 frame (max 2); full-size explosion about 4-5 frames; flash "super bright for one or two frames". fps not stated. Resolves a run-1 snippet-only lead (p2-p12 section 7) |
| G02 | Simon Trümpler Sketch 22: Barrel Explosion (thread) | simonschreibt (Simon Trümpler handle), realtimevfx | 2019-05 to 2020-08 | C (named) [V: corrected - the 1-2 frame inward distortion/bulge statements are by simonschreibt on 2020-07-31 and 2020-08-07 (he says he used it in earlier GIFs); the 2019-05-15 post is DieByZer0 asking for outward expansion for a few frames AFTER the blast, not a pre-blast contraction] | https://realtimevfx.com/t/simon-trumpler-sketch-22-barrel-explosion/8799 | no | 1-2 frames of distortion/inward bulge before the outward blast; [V: corrected - the old '1 frame contraction (a question, 2019)' was wrongly attributed; removed.] Context (own plan vs reference) not clear in the summary. fps not stated |
| G03 | Stylized Frag Launcher explosion, Overwatch inspiration breakdown (page 1) | Atif, realtimevfx [V: confirmed - Atif's opening post is dated 2017-03-06; effect had '18 components', not 'layers'] (with Agilethief quoting an Overwatch FX team member) | 2017-03 | C | https://realtimevfx.com/t/stylized-frag-launcher-explosion-overwatch-inspiration-breakdown-posted/1894 | yes | "expected life is 0.5 second" for the effect [V: confirmed - Atif, 2017-03-17]; flipbook of the Pharah rocket played back at "like 30 or even 24fps" (relayed quote, Overwatch FX team member in an Agilethief post of 2017-03-07; [V: unverified - 'davidschoneveld' is guessed from an avatar filename and 'Blizzard' is not stated on the page]). No flash number on page 1 (run 1 found 2-3 frames on page 2, S18, not re-read) |
| G04 | The Soul of Effects: What is Timing in VFX? (re-read) | VFX Apprentice (no byline) | 2025-08-20 | C [V: confirmed - date, no byline, 'less than 60 BPM', 0-48 frame axis, 'a crescendo has the time to react'; V: unverified - the fetch found NO 'first quarter of lifetime' wording on this page, so the 25% rule's origin on this page is not confirmed] | https://www.vfxapprentice.com/blog/the-soul-of-effects-what-is-timing-in-vfx | no | Definitions of wind-up, climax, fall-off; crescendo = build with "time to react", instant skips it; timing chart axis 0-48 frames, 0-1; "less than 60 BPM" for heals. Cites no outside source for the BPM rule |
| G05 | An Evaluation Research on Dynamic Hit Stop Using Eye Gaze (full PDF, was abstract-only in run 1) | Tomizawa, Ishikawa (Toyo Univ.), GRAPP 2024 | 2024 | study (GRAPP 2024 conference paper; [V: confirmed by reading the full PDF: authors, venue, N=16/16/15, teens and twenties, 8 levels 0.0-0.7 s, s=0.01, VR headset, means 0.37/0.56 (Scene 1 sword) and 0.39/0.57 (Scene 3 sword+bow), boundaries 0.537/0.55; Scene 2 has no boundary (non-normal)]; the paper does not say it is peer reviewed, GRAPP is a conference proceeding) | https://www.scitepress.org/Papers/2024/124614/124614.pdf | no | Hit-stop durations 0.0-0.7 s, 8 levels, three scenes, N=16/16/15; pleasant mean 0.37-0.39 s; unpleasant 0.56-0.57 s; boundary 0.537 / 0.55 s |
| G06 | Audio-to-video synchronization (Wikipedia; quotes ITU-R BT.1359-1, EBU R37, ATSC IS-191) | Wikipedia (secondary) summarising standards | live 2026 | spec via secondary (not tier A first-hand) [V: confirmed - 45/125 ms and +40/-60 ms match the Wikipedia text; standards themselves not opened; Wikipedia also lists per-stage +5/-15 ms] | https://en.wikipedia.org/wiki/Audio-to-video_synchronization | n/a | Sync tolerances in ms (section 3, punch). Standards themselves not opened |
| G07 | Are there any experienced VFX artists here who excel at timing? (thread) | DanielB, MadVFX, bgolus, Augie, others; realtimevfx | 2025-02 to 2025-05 | C (named forum users) [V: confirmed - bgolus 2025-03-03 'a breath'; the momentum point is MadVFX only, 2025-03-01, not bgolus] | https://realtimevfx.com/t/are-there-any-experienced-vfx-artists-here-who-excel-at-timing/28575 | no | No numbers. "Give them 'a breath'" between explosion and embers (bgolus, 2025-03-03); extra sparks break momentum (MadVFX) |
| G08 | Stylized VFX sketchbook thread (Quackenbush) | Beardilocks (Riot), Travis, others; realtimevfx | 2021-01 | C | https://realtimevfx.com/t/stylized-vfx/15639 | no | "tighten up the timing of the explosion" (Beardilocks 2021-01-04); no numbers |
| G09 | VFX Staples: Shape, Color and Motion (re-read) | Stefan Jevremovic, interview by Kirill Tokarev, 80 Level | 2018-01-17 | B [V: confirmed - interviewee is Stefan Jevremovic of Nordeus; the 0.5s -> 2s is a 'spell setting' for the Meteor Strike animation timing, dissipation quote is exact] | https://80.lv/articles/vfx-staples-shape-color-and-motion/ | yes; no newer found | Anticipation time set by game design (example 0.5 s to 2 s); climax and dissipation animated together in one clip; dissipation "shouldn't stay visible for long"; no frame counts, no ratios |
| G10 | Constructing VFX Worthy of League of Legends | Kevin Leroy (Riot VFX artist), interview by Kirill Tokarev, 80 Level | 2017-09-27 | B [V: confirmed - 'my favorite time is 0.1s' and exit order glow, lens flare 'almost as fast', sparks 'a bit later', bokeh last] | https://80.lv/articles/constructing-vfx-worthy-of-league-of-legends | yes; no newer found | Hit frame "very fast", "my favorite time is 0.1s"; exit order: main glow, then lens flare, then sparks, then bokeh dots last. No other numbers |
| G11 | Trail & Impact VFX Production | Guillermo Rossell, interview by Kirill Tokarev, 80 Level | 2019-02-11 | B | https://80.lv/articles/trail-impact-vfx-production | yes | Buildup, climax, aftermath named; trail starts when the slash gathers momentum; no numbers |
| G12 | Creating Stylized Combat VFX in The Legend of Zelda Style | Soenke Seidel, interview by Arti Sergeev, 80 Level | 2021-01-21 | B [V: confirmed - 'over a couple of frames'; cloud lifetime 'halved'] | https://80.lv/articles/creating-stylized-combat-vfx-in-the-zelda-style | no | Muzzle texture deforms "over a couple of frames"; explosion cloud lifetime halved to de-emphasise it (no absolute value) |
| G13 | The Role of Animations in Hit Effects | Peyman Massoudi (Dead Mage), Game Developer | 2016-03-25 | B | https://www.gamedeveloper.com/programming/the-role-of-animations-in-hit-effects | yes | Nothing usable (no numbers) |
| G14 | Take a closer look at character VFX made for 2XKO | Gloria Levine (80 Level) on Sonia Firsova | 2026-08-31 | B | https://80.lv/articles/take-closer-look-at-character-vfx-made-for-2xko/ | no | Nothing usable; frame-by-frame images only, no numbers in text |
| G15 | Master Timing and Punch with Jason Keyser (re-read) | VFX Apprentice | 2025-10-27 | C | https://www.vfxapprentice.com/blog/learn-timing-for-vfx-with-jason-keyser | no | Confirms run 1: terms used, no definitions, no numbers, no GDC/YouTube links on the page |
| G16 | Roblox Creator Docs mirror, effects/particle-emitters.md lines 424-431 | Roblox | mirror | spec | knowledge/external/roblox-creator-docs/effects/particle-emitters.md | n/a | FlipbookFramerate max 30 fps; OneShot rate = Lifetime / frame count |
| G17 | realtimevfx search and topic indexes (search.json lists) | realtimevfx.com | 2016-2024 | index only | https://realtimevfx.com/search.json?q=... | n/a | Found threads (Shannon McSheehan, Mursi, Magno, Sorangon). Read: McSheehan (1133) and Mursi (11615): no numbers. Index entries not cited as evidence |

Failed or empty (not cited as read): Lyndon GDC 2018 (GDC Vault login, Vimeo SIGGRAPH 2018 bot check, SideFX forum post only lists talk title), Keyser GDC YouTube (no transcript), youtubetotranscript (403), Riot 2017 style guide PDF (301 to homepage; Wayback blocked by the tool; r.jina.ai 401), Scribd copy and polycount comments (403), Insomniac Miles Morales VFX GDC 2021 page (abstract only, no video link), IEICE hit-stop pages (405), Semantic Scholar API (429), 2XKO (no text numbers).

## 3. Gap-by-gap results

### GAP: Frame / ms numbers per VFX phase

**Status: PARTLY FILLED.** Tier B: one number (0.1 s hit frame). Tier C: frame counts for punch and a pre-blast micro-windup. Tier A: none (Lyndon, Riot guide, Keyser GDC bodies unreadable). No source gives crescendo or follow-through duration. All "frames" below are as the artist wrote them; **none of the artists states fps**, so the ms columns are my conversion.

**Phase timing table (one row per claim; ms are inference unless stated)**

| phase | finding | frames (fps stated or assumed) | ms | evidence level | source ids |
| --- | --- | --- | --- | --- | --- |
| windup (micro, in the object) | Object distorts or bulges inward 1-2 frames before the outward blast | 1-2 frames; 60 fps = 1-2 f, 30 fps = 1-2 f | 17-33 ms at 60 fps; 33-67 ms at 30 fps | industry practice (named artist, realtimevfx 2019-2020); context unclear | G02 |
| windup (telegraph, gameplay) | Length set by game design, adjustable in a spell setting | 30-120 frames at 60 fps | 500-2000 ms (stated by source) | industry practice (Jevremovic, 80 Level 2018) | G09 |
| windup (dark or pull frames) | A few dark frames or an inward pull before the hit add impact | "a few"; no number | no number found | industry practice, relayed (sifa, realtimevfx 2019; index blurb only) | G17 (blurb) |
| punch (brightest layer) | Initial burst not longer than 1 frame (max 2); "super bright for one or two frames" | 1-2 frames | 17-33 ms at 60; 33-67 ms at 30; 42-83 ms at 24 | industry practice (Riot artist, 2017) | G01 |
| punch (hit flash) | LoL hit frame is "very fast"; his preferred value is 0.1 s | 6 f at 60; 3 f at 30; 2.4 f at 24 | 100 ms (stated by source) | industry practice (Riot artist, 80 Level 2017) | G10 |
| punch (full-size burst) | Explosion reaches full size in about 4-5 frames | 4-5 frames | 67-83 ms at 60; 133-167 ms at 30; 167-208 ms at 24 | industry practice (Riot artist, 2017) | G01 |
| punch (sync with sound) | Audio ahead of video is noticed from 45 ms; audio behind from 125 ms (ITU-R BT.1359-1); EBU R37 allows +40 ms lead, -60 ms lag end to end | 2-3 frames at 60 fps for the 40-45 ms lead limit | +40 / -60 ms (EBU); 45 / 125 ms (ITU) | spec via secondary summary; use for flash vs sound is inference | G06 |
| punch (freeze after contact) | Pleasant hit stop averaged 0.37 s (sword scene) and 0.39 s (sword+bow); unpleasant 0.56-0.57 s; computed boundary 0.537 and 0.55 s; tested range 0.0-0.7 s; playback during stop set to 0.01x | 22-23 f at 60 fps (0.37-0.39 s); 9 f at 24 fps | 370-390 ms pleasant; 537-550 ms boundary | study (N=16, 16, 15; teens and twenties; VR headset; one custom action game) | G05 |
| crescendo | Crescendo "has the time to react", an instant effect does not; no duration | timing chart axis 0-48 frames (fps not stated; 48 f = 0.8 s at 60, 1.6 s at 30, 2 s at 24) | no number found | industry practice (VFX Apprentice 2025); axis range only | G04 |
| follow-through / dissipation (order) | Main glow ends first, lens flare "almost as fast", sparks later, bokeh dots last | no number found | no number found | industry practice (Riot artist 2017) | G10 |
| dissipation (length) | Dissipation "shouldn't stay visible for long"; climax and dissipation can share one clip | no number found | no number found | industry practice (80 Level 2018) | G09 |
| dissipation (breath) | Delay embers behind the explosion with a brief gap: "Give them 'a breath'" | no number found | no number found | industry practice (named forum user, 2025) | G07 |
| whole effect | A stylized explosion with 18 layers had an expected life of 0.5 s | 30 f at 60 fps; 15 f at 30 fps | 500 ms (stated by source) | industry practice (Atif, 2017) | G03 |
| flipbook playback | An Overwatch FX team member said the Pharah rocket flipbook is played back at "like 30 or even 24fps" (relayed in the thread) | 24-30 fps | 33-42 ms per flipbook frame | industry practice, relayed (2017, pre-2020) | G03 |
| flipbook playback (engine limit) | Roblox FlipbookFramerate max 30 fps; OneShot plays across Lifetime | fps = frames / Lifetime | n/a | spec | G16 |
| muzzle flash | Hand-painted muzzle texture deforms "over a couple of frames" | about 2 frames | no number found | industry practice (Seidel, 80 Level 2021) | G12 |

**Cross-check (inference only).** G03 says one stylized explosion lives 0.5 s. If a Sirhaian-style burst of 4-5 frames (G01) sat inside it, the full-size moment would fill 13-17% of the life at 60 fps, 27-33% at 30 fps, 33-42% at 24 fps. The two sources are different effects, so this is a plausibility check against the "first quarter of lifetime" rule (S14 in p1-value-colour-timing.md, see the 25% gap below), not a proof.

**Reading for our agent (inference, not source claims).**
1. Punch is 1-2 frames of the very brightest layer, with the full shape reaching size in about 4-5 frames and a 0.1 s hit flash (G01, G10). Treat 1-2 frames at the target fps as a floor to test, not a rule.
2. Windup comes in two scales: a 1-2 frame object-level tell (G02) and a gameplay telegraph of 0.5-2 s set by the designer (G09). Do not mix them.
3. Only the order of exit is evidenced (glow, flare, sparks, bokeh; G10). Stagger lifetimes in that order and test the durations.
4. Hit stop: [V: corrected - the 0.37-0.39 s values are the mean of the durations each player rated MOST enjoyable (one vote per player), not a proven comfort ceiling; 0.56-0.57 s is the mean of the most stressful votes] one study finds players' favourite near-freeze about 0.4 s in its game (G05). That is longer than the Capcom 8/12/16 frame example in run 1 (S13). Both are single-context. Test short values first.

### GAP: Second source for "main action finishes or begins to dissipate within the first quarter of lifetime" (Sparkadia / VFX Apprentice)

**Status: STILL OPEN.** [V: confirmed still open; additionally the G04 page fetch showed no 'first quarter' wording, so even the single source is unverified.] The search for the phrase (search 6) returned only the same VFX Apprentice article and Hallzy's instructor page. No second source found.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| No independent source states a lifetime fraction for the main action | no number found | n/a | searches 6, 10 |
| Related but not equivalent: dissipation "shouldn't stay visible for long" (Jevremovic); glow exits first and sparks later (Leroy); explosion life 0.5 s with 4-5 frame burst (Sirhaian, Atif) | the cross-check above: 13-42% depending on assumed fps | inference | G01, G03, G09, G10 |

Verdict: keep the 25% rule as a **tier C single-source starting value**, flagged for an A/B test (peak at 10, 25, 40% of lifetime).

### GAP: Second source for "heal effects under 60 BPM; faster than a heartbeat reads aggressive" (VFX Apprentice 2025)

**Status: STILL OPEN.** Re-read G04: wording confirmed exactly: "make sure the pace is less than 60 BPM, and vice-versa for attack VFX". The page cites no outside source and gives no definition of "pace" (loop rate, pulse, flicker, or spawn rhythm). Search 7 found no second source. It did find unsourced AI-written skill pages that propose 50-70 BPM; those are tier D and rejected.

| finding | numbers | evidence level | source ids |
| --- | --- | --- | --- |
| Rule exists on one page, no named maker, no study | less than 60 BPM = a cycle longer than 1.0 s (arithmetic, inference) | industry practice (VFX Apprentice 2025), single tier C | G04 |
| A burst heal may need to be fast and punchy, not slow (Ubisoft artist feedback seen only in a search summary, page not opened) | no number found | lead only, not cited as evidence | none |

Verdict: keep as a tier C starting value. Suggested test: pulse a heal glow at 40, 60, 80, 120 BPM and ask the owner to rate "calm / aggressive" on a phone.

## 4. Quotes used (<=15 words)

| quote | attribution | id |
| --- | --- | --- |
| "my favorite time is 0.1s" | Kevin Leroy (Riot), 80 Level 2017 [V: confirmed] | G10 |
| "not longer than 1 frame (max 2)" | Sirhaian (Riot), realtimevfx 2017 [V: confirmed as returned by the fetch tool; Riot affiliation unverified on the page] | G01 |
| "Give them 'a breath' as it were" | bgolus, realtimevfx 2025 | G07 |
| "make sure the pace is less than 60 BPM" | VFX Apprentice 2025 [V: confirmed] | G04 |
| "shouldn't stay visible for long" | Stefan Jevremovic, 80 Level 2018 [V: confirmed - exact article wording is 'This stage shouldn't stay visible for long because effect is over and you don't want to distract the player.'] | G09 |

## 5. Conflicts with first-run files

| first-run file and row | what it says | what this run found |
| --- | --- | --- |
| p1-value-colour-timing.md, section 5 gaps row 1 and the method note ("no named source read gives frame or ms numbers per VFX phase") | none exists | Partly wrong: Jevremovic (0.5-2 s anticipation) was already in p1-gameplay-shape.md S15. The two first-run files disagree with each other. This run adds Leroy 0.1 s (G10) and Sirhaian 1-2 / 4-5 frames (G01) |
| p2-p12-numbers-moments-review.md, section 7 lead ("initial burst not longer than 1 frame (max 2); full-size explosion 4-5 frames", snippet only) | unverified | Confirmed by opening the thread (G01, Sirhaian, 2017-02-24) |
| p2-p12 section 4 "Explosion flash length" (S18 2-3 frames vs S16 1-2 frames) | newer 1-2 frames for the brightest layer | Consistent with Sirhaian 1-2 frames (G01). Leroy's 0.1 s hit frame (G10) is longer than 2 frames at 30 fps or more; they are different layers (2D hit flash vs brightest sprite), so not a conflict, but note both |
| p2-p12 section 2a "Heavy hit" and section 4 "Hit freeze" (Capcom 8/12/16F example, SF2 about 10 f, Vlambeer 10-20 ms) | hit-stop 8-16 frames at 60 fps (133-267 ms) | Tomizawa 2024 finds 0.37-0.39 s pleasant in one game with 0.01x playback (G05). Higher than the Capcom example. Do not reconcile: different game, VR headset, near-freeze |
| p1-value-colour-timing.md S23 row ("abstract gives no ms") | no ms | Full text now read (G05): ms values exist |
| p2-p12 S18 date 2017-06-06 for the Atif breakdown | posted 2017-06-06 | G03 page 1 shows Atif posts dated March 2017 (for example 0.5 s life, 2017-03-17). Likely different posts in one thread; not re-checked |

## 6. Still open and how we could test it ourselves

| open question | why still open | how we could test it |
| --- | --- | --- |
| Tier A phase numbers (Lyndon GDC 2018, Keyser/Chamberlin GDC 2017, Riot 2017 style guide timing section) | GDC Vault login, no transcripts, Riot PDF redirects, Wayback blocked by the fetch tool | Owner watches the free GDC YouTube videos or opens the Wayback PDF in a browser and pastes the timing page. Or buy GDC Vault access |
| fps behind Sirhaian's and Atif's frame counts | not stated | Assume 30 fps for flipbooks (G03 relay) and 60 for the game. Test in Studio at 60 fps with FlipbookFramerate 12, 24, 30 |
| Crescendo duration | no source gives it | A/B: build 0, 150, 300, 500 ms before the punch on one charge-up. Owner ranks "tense" vs "slow" |
| Follow-through and dissipation duration | only order, no times | Keep the Leroy order (glow, flare, sparks, debris). Test dissipation at 30, 50, 70% of lifetime on the owner's phone |
| Windup micro-tell of 1-2 frames (G02) | context unclear | Add a 1-frame and 2-frame inward squash on a brick blast; check at 60 fps and on a 30 fps phone |
| Punch length: 1-2 frames vs 0.1 s | two named sources, different layers | A/B a 1-frame, 2-frame, 6-frame white flash on the same hit |
| Hit-stop at our scale | one study, one game | Prototype freezes of 50, 100, 150, 250, 400 ms on a Roblox hit; owner A/B (extends run 1 gap) |
| Flash and sound alignment | standards read through a secondary summary | Test sound offset -3, 0, +3 frames at 60 fps against the flash; confirm the ITU/EBU window with the standards text |
| 25% lifetime rule and 60 BPM heal rule | single tier C each, no second source | A/B tests above. Mark both PROPOSAL in the VFX rules until the owner confirms |
| Insomniac (Miles Morales VFX, Spider-Man 2 symbiotes), God of War VFX talks, Thomas Iché | talks not freely readable; no Iché page found | Watch recordings when they reach GDC YouTube; ask the owner for any links |
| SideFX/Houdini real-time VFX docs with timing | not fetched (fetch cap) | Next run: fetch Labs Flipbook docs and Lyndon's SIGGRAPH 2018 slides |

## Verification log

Checked 2026-10-12 by an adversarial pass (WebFetch re-opens; the G05 PDF was downloaded and read with pdftotext). 22 claims checked.

Corrected (not false in whole, but wrong in part):
- G01 row: "second source G10 for the flash size" removed. G10 is a 0.1 s hit frame, not a flash size.
- G02 row: the "1 frame contraction (a question, 2019)" claim was wrongly attributed. The pre-blast 1-2 frame inward bulge is simonschreibt 2020-07-31 and 2020-08-07. The 2019 post (DieByZer0) asks for outward expansion after the blast.
- G03: "18 layers" is "18 components" (Atif, 2017-03-06). The speaker name "davidschoneveld" and "Blizzard" are not on the page: marked unverified.
- G05: "comfortable up to about 0.4 s" over-reads the paper. The values are mean durations that players voted most enjoyable or most stressful. Scene 2 has no boundary. The paper is a conference paper; "peer-reviewed" is not stated in it.
- G07: the "extra sparks break momentum" point is MadVFX only.
- Quote table: the Jevremovic "fetch paraphrase" note removed; the wording is exact.

Unverified:
- The "first quarter of lifetime" wording could not be found on the VFX Apprentice page (G04). The 25% rule has no confirmed source at all; keep as an untested guess.
- G06 standards (ITU, EBU) read only via Wikipedia.
- Sirhaian's Riot affiliation and the fps behind all frame counts.

Removed as false: none entirely.

FILLED/PARTLY status: the "frame/ms per phase" gap stays PARTLY FILLED (correct; no tier A number). The two single-source gaps stay STILL OPEN (correct).
