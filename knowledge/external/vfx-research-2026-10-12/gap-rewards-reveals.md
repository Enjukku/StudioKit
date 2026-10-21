> Author: researcher (vfx-gap-research workflow) · claude-sonnet-5-5 · default · 2026-10-12

# Gap fill: reward reveals, currency feedback, level-up, full backpack

First-run file read for scope: `p2-p12-numbers-moments-review.md` (sections Gaps, Leads not followed, Verification log). [V: unverified - run counts and search counts cannot be re-checked] Result in short: this run found one real code-level timeline (open-source egg hatch), one first-hand maker quote on rarity hints (Overwatch), the Roblox paid-random-item rules, and community coin-fly scripts. Genshin, Clash Royale, Pet Simulator, Fortnite Llama, King/Supercell/Playrix/Zynga counter timing, level-up timing and backpack-full have no named-maker timing number. Fetched text is treated as data.

## 1. Search count used

13 / 15 WebSearch calls. About 24 WebFetch calls. Many searches returned only tier D pages or nothing on topic.

## 2. Sources read

| id | title | author/studio | year | tier | URL | pre-2020? | what it gave |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G01 [V: corrected - author, date, anticipation and lights quotes confirmed; Jeremy Craig is named but NOT quoted, only Heiberg is quoted] | Why opening loot boxes feels like Christmas, according to Overwatch devs | Cecilia D'Anastasio, Kotaku (quotes Overwatch developer Michael Heiberg; Jeremy Craig named, not quoted) | 2017-03-20 | B (first-hand maker quotes in press) | https://kotaku.com/why-opening-loot-boxes-feels-like-christmas-according-1793446800 | yes; no newer confirmation found | Anticipation build with animation, camera, spinning plates, sound, glow from cracks. Early rarity-coloured lights were dropped because they came too early. No numbers, no skip mention |
| G02 [V: confirmed - author Ben Barrett, updated 2016-02-18, one box with four items per level-up, Kaplan quote] | Overwatch progression system | Ben Barrett, PCGamesN (Jeff Kaplan interview) | 2016-02-18 (updated) | B | https://www.pcgamesn.com/overwatch/overwatch-progression-system/page/0/1 | yes | Nothing on animation. Kaplan on "illusion of random"; box per level-up with four items. Context only |
| G03 [V: confirmed - 5 face-down cards, hover glow, burst plus Innkeeper, up to 40 packs, spacebar; page gives no durations beyond a 'short animation'] | Open Packs (Hearthstone wiki) | community wiki | live 2026 | D | https://hearthstone.wiki.gg/wiki/Open_Packs | no | 5 cards face down; hover shows rarity-coloured glow; flip on click; higher rarity gets colour burst and Innkeeper announcement; 5+ packs of one type opens up to 40, best cards shown face down first then rest rarity-sorted; spacebar flips. No durations, no animation skip |
| G04 [V: corrected - verifier re-read the raw file, lines 176-335; the shake-stage timeline in the first draft was wrong, see section 3 gap (a); flash, sound, reveal-wait and fade values confirmed] | Pokerogue egg-hatch phase source (`egg-hatch-phase.ts`) | pagefaultgames/pokerogue contributors (open-source fan game) | main branch, read 2026-10-12 | D for design (fan project); exact for what that code does | https://raw.githubusercontent.com/pagefaultgames/pokerogue/main/src/phases/egg-hatch-phase.ts | no | Full beat timeline with ms (section 3, gap a). Now read line by line by the verifier |
| G05 [V: unverified - Wikipedia not re-opened (250k characters); dates not re-checked] | Loot box (Wikipedia) | Wikipedia editors | read 2026-10-12, first 100,000 of ~250,000 characters | D (encyclopedia, secondary) | https://en.wikipedia.org/wiki/Loot_box | no | Dated regulation list: China 2016 announcement (effective May 2017), Belgium 2018, Netherlands 2018, UK ASA 2021, Korea 2023/2024. Reveals "colour-coded by rarity", slot-like UIs. Near-miss not mentioned |
| G06 [V: confirmed - 3.1.1 text matches] | App Store Review Guidelines, 3.1.1 | Apple | live 2026, first 100,000 of ~112,000 characters | spec (store policy) | https://developer.apple.com/app-store/review/guidelines/ | no | Loot boxes must disclose odds of each item type before purchase |
| G07 [V: confirmed against local mirror - percentages sum to exactly 100, indirect purchases and luck boosts covered, ArePaidRandomItemsRestricted] | Paid random items policy guidelines (local mirror) | Roblox Creator Docs | mirror | spec | knowledge/external/roblox-creator-docs/production/monetization/paid-random-items.md | no | Eggs, chests, wheels count; odds as % summing to 100 before purchase; luck boosts and pity systems count; per-user restriction via PolicyService |
| G08 [V: corrected - 4 h free chest, 24 h crown chest, full slots as 'soft progression blocker', presentation and pacing called 'fantastic' confirmed; author is a blogger so tier is B-, not full B; free chests also store up to two] | Breaking down Supercell's next hit: Clash Royale | Sheldon Laframboise, Game Developer | 2016-02-22 | B- | https://gamedeveloper.com/design/breaking-down-supercell-s-next-hit-clash-royale | yes | Chest timers (free chest 4 h, crown chest 24 h), "waiting" as anticipation. Praises opening "presentation and pacing" but gives no reveal timing |
| G09 [V: corrected - numbers 0/80/140 ms, ~400 ms and 60-150 ms band confirmed; year not shown on the page (footer and profile suggest 2026, inferred); the page does NOT say its numbers are illustrative, it says 'those offsets are the design'; still unsourced] | The reward moment is the product | PatilRB, DEV Community | Aug 26, year not shown (likely 2026) | D (blog, unsourced) | https://dev.to/patilrb/the-reward-moment-is-the-product-43h6 | unknown | Spark t=0, coin fountain t=80 ms, count-up start t=140 ms, "about 400 milliseconds" reward moment. Unsourced |
| G10 [V: confirmed - both scripts posted 2025-05-13; see section 3 gap (b) for the arithmetic correction] | How to make this coin UI animation? (thread, answers by oohypr, Nika/Antiwall_Dev) | DevForum users | 2022 to 2025-05-13 | D to C (credited forum users; code answers, not studio) | https://devforum.roblox.com/t/how-to-make-this-coin-ui-animation/1812608 | no | Two community scripts with numbers (section 3, gap b) |
| G11 [V: corrected - tweens 0.05 s, 0.05 s and a final 0.1 s; two wait(0.05) per coin so about 0.1 s per coin, not one wait] | Help with making animated coins! (248tomek, Scottifly) | DevForum | 2023-06-28 | D | https://devforum.roblox.com/t/help-with-making-animated-coins/2443332 | no | Coin pop tweens 0.05 s and 0.1 s, two `wait(0.05)` per coin; the cause of delay was a per-player loop |
| G12 [V: confirmed - YawnMcie 2025-04-14 'the counter seems too slow'; Gbabyboyg 2025-04-15 'it feels kind of slow'; the third name (rickrolledlololXD2) is not tied to a quote] | Feedback for my coin counter | rickrolledlololXD2 (By_Chaddeo), YawnMcie, Gbabyboyg | 2025-04-14 | D | https://devforum.roblox.com/t/feedback-for-my-coin-counter/3605637 | no | Two replies say the counter animation "seems too slow" and "kind of slow". Duration not given |
| G13 [V: corrected - author and date confirmed; page does not state his role, so tier is B (studio blog), not A/B; 'power up', phoenix, shareable card confirmed; 'multiple passes of rough animation' not 'several'; no clear 'final flight animation', only an aside '(er, flight?)'] | Streak milestone design animation | Kurt Hartfelder, Duolingo blog | 2022-01-21 | B (studio blog, first-hand) | https://blog.duolingo.com/streak-milestone-design-animation | no | Milestone as a "power up": transformation, final flight animation, shareable card. Several rough animation passes. No durations |
| G14 [V: unverified - not opened; marked unused] | Squeezing more juice out of your game design | Nathan Lovato, Game Developer / GameAnalytics blog | 2015-04-01 | B | https://www.gamedeveloper.com/design/squeezing-more-juice-out-of-your-game-design- | yes | Nothing on reward counters or timings. Not used |
| G15 [V: unverified - first-run ids S01/S02/S03/S23 not opened in this check] | Other first-run sources reused without reopening | see first-run file | | | S01 Material m1 motion; S02 Material Android Motion.md; S03 NN/g animation duration; S23 Larche et al. | | Cited by first-run id only |

Pages that failed or gave nothing: ToucArcade Hearthstone Ben Thompson interview (403 again; only a search snippet seen, not cited as read); web.archive.org (blocked by the fetcher); Genshin Fandom wiki (402); GDC Vault search (redirect, nothing listed); pikami pokerogue html mirror (404); design.duolingo.com/motion (redirects to blog hub, not read); Devforum threads G-other (OutlookG Bezier thread: no durations; "How is my counter animation": unrelated; "Coin moving to player effect": no numbers); Wikipedia page was cut at 100,000 characters.

## 3. Gap-by-gap results

### GAP: (a) Gacha / egg / chest / pack reveal timing and escalation by rarity
Status: PARTLY FILLED [V: confirmed as partly, but weak: the only timeline is one fan game's code, no named-maker number; treat as OPEN for studio practice]. One exact timeline (open-source egg hatch, not a named design talk), one maker quote on what to withhold (Overwatch). No named-maker timing for Hearthstone, Genshin, Clash Royale, Pet Simulator or Fortnite Llama.

| finding | numbers | evidence level | source |
| --- | --- | --- | --- |
| [V: corrected - first draft numbers were wrong. Code: stage 1 at 2000 ms, one 500 ms shake (125+250+125); 1000 ms gap; stage 2 at 3500 ms, one 500 ms shake; 1000 ms gap; stage 3 at 5000 ms with crack sound, two cycles, 875 ms; doHatch at 5875 ms. The figures 3875, 6500, 7375 and '4 cycles' do not exist: the 2, 4, 8 arguments are shake intensity] Open-source egg hatch (Pokerogue) has 3 shake stages then a flash then reveal | Beats: 3 shake stages (escalating crack frames 0, 1-2, 3-4; spray 1, 2, 4; shake intensity 2, 4, 8). About 5.9 s from asset load to the hatch flash; about 7.4 s to the reveal start (5.9 s + 1.5 s) | industry practice, weak (shipped fan game code, not a studio talk); exact for that game only | G04 |
| [V: confirmed in code, with one correction: the reveal fires 1500 ms after doHatch starts, about 1375 ms after the flash ends, not 1500 after the flash; fade 3000/500 ms and info panel delays confirmed; fixedInt scaling not checked] Hatch flash: white overlay alpha 0 to 1 in 125 ms; 5 hatch sounds at 0, 375, 750, 1125, 1500 ms with volumes 1.0, 0.8, 0.6, 0.4, 0.2; auto-reveal at 1500 ms after flash; reveal fades the white overlay over 3000 ms (500 ms if skipped); info panel and fanfare about 1500 ms after reveal start (2000 ms if shiny) | flash 125 ms; reveal wait 1500 ms; fade 3000 ms; skipped fade 500 ms; shiny adds 500 ms | industry practice, weak (same) | G04 |
| [V: confirmed - window about 1.375 s, 6x particle speed, flag reset quirk at lines 321-327] Skip in that code is allowed only from the end of the 125 ms flash until 1500 ms later; skip makes the reveal fade 500 ms instead of 3000 ms and speeds particles 6x. A code quirk resets the skip flag so skipping during the shake stages does not shorten the flash | skip window about 1.4 s; skipped total about 0.5 s after reveal | industry practice, weak (same); the quirk is a bug note, not a design rule | G04 |
| [V: confirmed - egg tier changes only the shard sprite (line 457); shiny adds delay] That same code has NO per-rarity timing, shake count, colour or sound. Rarity only changes shard visuals and the shiny delay (+500 ms) | no number found for rarity-scaled duration | industry practice, weak (same) | G04 |
| [V: confirmed - Heiberg: 'we want to build anticipation'; list: animations, camera work, spinning plates, sounds] Overwatch: opening is built to maximise anticipation using animation, camera work, spinning plates, sound and the glow from cracks | no number found | industry practice (Overwatch developers Heiberg and Craig, 2017) | G01 |
| [V: confirmed - Heiberg: this 'was too early, and it killed your anticipation'. One developer anecdote, pre-2020 (2017)] Overwatch tried rarity-coloured lights that hinted each item's rarity; the team dropped them because they came too early and undercut suspense | no number found | industry practice (same) | G01 |
| [V: confirmed against wiki, tier D] Hearthstone shows rarity at a different beat: the card is face down with a hover glow in the rarity colour, then the flip gives a colour burst and Innkeeper voice for higher rarity. Multi-pack opens put the best cards face down first | 5 cards per pack; up to 40 packs at once; no durations. Colour ladder not listed on the page | industry practice (wiki description, tier D, no durations) | G03 |
| [V: unverified - Wikipedia not re-opened] Rarity is "colour-coded" in loot-box reveals in general; the exact ladder per game was not read from any tier A/B page | no number found | inference | G05 |
| [V: confirmed - 4 h / 24 h; tier B-, 2016 pre-2020] Clash Royale: reveal timing not found. Design of anticipation is mostly the unlock timer (free chest 4 h, crown chest 24 h) and a gate of chests in the inventory | 4 h / 24 h | industry practice (Game Developer 2016, article not the maker) | G08 |
| [V: confirmed against mirror] Roblox constraints: any egg, chest or wheel paid with Robux or Robux-bought currency is a paid random item. Odds must show as percentages summing to 100 before purchase; luck boosts and pity systems must show true odds; users with `ArePaidRandomItemsRestricted` need a non-random path | "sum to exactly 100%"; odds shown before spending | spec | G07 |
| [V: confirmed] Apple store rule: loot boxes must show odds of each item type before purchase | n/a | spec | G06 |
| [V: unverified - source G05 not re-opened] Regulation map (dated): China (announced 2016, from May 2017), Belgium (April 2018, gambling classification), Netherlands (April 2018), UK ASA (Sept 2021, store/ad disclosure), Korea (law 2023, enforced March 2024). This is why the odds must be on screen; none of it sets animation durations | dates as listed | spec/news summary (tier D) | G05 |
| [V: unverified - S23 and the 2026 review not opened] Near-miss tricks (showing the rare item "almost" landing): no regulation or study text on reveal animation found; the Waterloo abstract (first-run S23) shows rarer rewards raise anticipatory arousal before the reveal. A search found a 2026 review (Rozprawy Spoleczne) listing near-miss among mechanisms, snippet only, not opened | no number found | study (S23 abstract); near-miss review = not read | G15 |

Design use (inference, labelled): keep the escalation in the build-up, not in the colour hint. Overwatch's finding says do not show the final tier colour before the payoff. Use the open-source timeline only as a starting scale [V: corrected - 2 s lead-in, then about 3.9 s of shakes, hatch at about 5.9 s]: about 2 to 3 stages of build-up, then a short white flash (125 ms), then a hold of about 1.5 s. Test against a skip rule that always cuts to about 0.5 s.

### GAP: (b) Coin / currency fly-to-counter and counting-up timing
Status: PARTLY FILLED [V: weak - tier D/C forum scripts and a tier D blog only, no studio number; treat as OPEN for design purposes]. Only community script values and one author's unsourced offsets. No King, Supercell, Playrix or Zynga number. Material tokens (first-run S01/S02) remain the only vendor duration scale.

| finding | numbers | evidence level | source |
| --- | --- | --- | --- |
| [V: corrected - values confirmed (2025-05-13, 20 coins, 0.5 s Quad Out, 0.25 s wait, 0.8 s Quad In, 50x50 to 100x100) but the arithmetic was wrong] Script by oohypr (DevForum, 2025): 20 coins; burst tween 0.5 s Quad Out to random offset within +-0.2 scale; wait 0.25 s; flight tween 0.8 s Quad In to the counter; coin sizes 50x50 to 100x100 | total 1.55 s per coin (0.5 + 0.25 + 0.8); 1.05 s is burst-end to arrival (0.25 + 0.8) | industry practice, weak (forum answer, credited user, not a studio) | G10 |
| [V: corrected - second tween IS specified: default TweenInfo, 1 s Quad Out, no wait; new batch every 2 s] Script by Nika/Antiwall_Dev (2025): 5 to 15 coins per burst, burst tween 0.7 s with random spread 0.3 to 0.7 scale, size 40 to 60 | burst 0.7 s + flight 1.0 s = 1.7 s per coin | industry practice, weak | G10 |
| [V: corrected - 0.05 s tweens, final 0.1 s tween, two wait(0.05) per coin so about 0.1 s per coin; the '5 shortcut coin pops' wording is not supported by the page] Older script: coin pops of 0.05 s and 0.1 s | 0.05 to 0.1 s per pop, about 0.1 s per coin | industry practice, weak | G11 |
| [V: confirmed, n=2, 2025] Player feedback: a coin counter shown for too long "seems too slow" and "kind of slow" (two replies). Duration unknown | no number found | industry practice, weak (n=2 replies) | G12 |
| [V: corrected - numbers confirmed; the author does not call them illustrative; the 400 ms is the whole reward moment] One author's layered offsets: spark at 0, coin fountain at 80 ms, count-up start at 140 ms; reward tap about 400 ms; band 60 to 150 ms between layers. Author says it is "iteration, not calculation" | 0 / 80 / 140 ms; 60-150 ms | tier D, unsourced; treat as a start point to test | G09 |
| [V: unverified - first-run sources not opened] Responsiveness thresholds from first run: 100 ms feels instant; Material short tier 50 to 200 ms; exits shorter than entrances (195 vs 225 ms) | see first run | spec | G15 (S01, S02, S03) |
| Count-up duration for a numeric counter: no number from any named source | no number found | n/a | none |

### GAP: (c) Level-up / unlock celebration timing
Status: STILL OPEN for numbers [V: confirmed]. Only a qualitative maker source.

| finding | numbers | evidence level | source |
| --- | --- | --- | --- |
| [V: corrected - 'power up', phoenix, multiple rough passes, shareable card confirmed; 'flies' and 'several' not supported] Duolingo treats a streak milestone like a "power up": the mascot changes form (phoenix); multiple rough animation passes; a shareable card is added at the end | no durations, no beat count | industry practice (Duolingo blog, 2022) | G13 |
| [V: confirmed; the 'delivered as the next reveal' reading is inference] Overwatch grants a box per level-up (the reward is delivered as the next reveal, not as a separate long screen) | one box per level; four items | industry practice (Kaplan, 2016) | G02 |
| Timing for level-up, unlock, stage-clear: no named talk found (a GDC-focused search returned only level-design talks) | no number found | n/a | none |

### GAP: (d) Full-backpack / sell moment
Status: STILL OPEN [V: confirmed]. No named source found (DevForum and Game Developer search returned nothing on topic). One hobby-project playtest comment (itch.io Fantasy Logistics) says the walk back to sell is "empty and boring"; it is an unopened search snippet, tier D, not cited as read.

| finding | numbers | evidence level | source |
| --- | --- | --- | --- |
| No source on timing, colour, or sound for "bag full" or for the sell cash-out | no number found | n/a | none |
| [V: confirmed] Clash Royale: when the chest inventory is full, no new chests are earned; the author calls this a soft progression blocker. This is the nearest "full container" design in a named article | n/a | industry practice (secondary article, 2016) | G08 |

## 4. Quotes used

- [V: confirmed, full line 'we want to build anticipation'] "build anticipation" (Michael Heiberg, Overwatch, in Kotaku 2017, via G01).
- [V: corrected - exact wording 'only an illusion of random'] "illusion of random" (Jeff Kaplan, in PCGamesN 2016, via G02).
- [V: confirmed] "seems too slow" (YawnMcie, DevForum 2025, G12).
- [V: confirmed, full line 'finding it is iteration, not calculation'] "iteration, not calculation" (PatilRB, DEV Community, G09).
- [V: confirmed against live page] "must disclose the odds of receiving each type of item" (Apple App Store Review Guidelines 3.1.1, G06, page text via small-model summary).

## 5. Conflicts with first-run files

| first-run file / row | first run said | this run | resolution |
| --- | --- | --- | --- |
| `p2-p12-numbers-moments-review.md` section 2a row "Egg / chest reveal": "rarity colour ladders: no tier A/B source read" | no tier A/B | Still true for the ladder. Overwatch (tier B) now gives the opposite warning: rarity colour shown early hurt suspense | Added in G01. Rarity colour has a timing rule, not only a palette |
| Same file, section 2a "Collect / coin / pickup": "no number found from a named source" | none | Only community scripts (tier D/C) and an unsourced blog now exist | Still no named-source number; keep "test 200/400/700 ms" plan and add 0.5/0.8 s scripts as candidates |
| Same file, "Leads not followed": dev.to reward moment page tier D with spark 80 ms, coin fountain 80 ms, number 140 ms | tier D, unverified | Read (G09): [V: corrected - author does NOT say the numbers are illustrative] | Confirmed D |
| Same file, Gaps: "Hearthstone/Genshin footage frame by frame" | to do | Not possible by text research | Needs owner or an agent to capture video (section 6) |

No number in the first-run file was contradicted.

## 6. Still open and how we could test it ourselves

| question | status | test |
| --- | --- | --- |
| Genshin Impact wish animation: beats, colour per tier, duration, skip | STILL OPEN (four searches and two fetches gave only fan simulators and a paywalled page; a simulator option "Skip Meteor Animation Only" suggests two skippable stages, tier D, not read) | Record the real game at 60 fps, count frames per beat for 3-star, 4-star, 5-star; or ask the owner for clips |
| Hearthstone pack-open durations | STILL OPEN (interview page blocked) | Record 5 pack opens, mark time to first flip and time of legendary burst |
| Clash Royale chest reveal beats and durations | STILL OPEN | Record opening of common and legendary chests |
| Pet Simulator / Adopt Me egg hatch beats | STILL OPEN (no Roblox game timing found; a search summary said no DevForum guidance with durations) | Record hatch of cheapest and rarest egg; count seconds; test the skip toggle |
| Fortnite Llama | STILL OPEN (never reached a source) | Record a Llama open |
| Whether early rarity tell hurts or helps | One maker anecdote (Overwatch) | A/B in our game: no tell vs tint on egg at build-up; measure hatch skip rate and playtest comment |
| Coin fly duration | candidate 0.5 to 0.8 s | Our own test: 3 flight durations (0.4, 0.6, 0.8 s) with one counter pulse per batch; phone at 30 fps |
| Count-up duration | no number | Test 0.4, 0.7, 1.0 s; watch for "too slow" comments (G12 shows slow reads as distracting) |
| Level-up / unlock length | no number | Test a 1.0 s and a 2.0 s version; add tap-to-skip |
| Full backpack / sell moment | no source | Test full-bag cue: icon pulse + colour change at 100%, one sound; test sell: count-up tied to coin burst |
| Ethics: near-miss trick legality | not found | Do not use near-miss presentation (design rule, inference). Show odds per Roblox rule G07 before spending |

## Verification log

Checker: adversarial fact-check, 2026-10-12, WebFetch plus a direct read of the raw Pokerogue file and the local Roblox mirror. No WebSearch used.

| claim | verdict | reason |
| --- | --- | --- |
| Pokerogue stage 2 at 3875 ms with 4 cycles, stage 3 at 6500 ms, hatch at 7375 ms, about 7.4 s to hatch | replaced | Code (lines 186-218, 246-285): stages at 2000, 3500, 5000 ms; shakes 500, 500, 875 ms; doHatch at 5875 ms. The 2/4/8 arguments are shake intensity. About 7.4 s is the reveal start, not the hatch |
| oohypr total 1.05 s per coin | corrected | 0.5 + 0.25 + 0.8 = 1.55 s; 1.05 s is the post-burst part |
| Nika script second tween not specified | corrected | Default TweenInfo: 1 s Quad Out |
| G11 one wait(0.05) per coin | corrected | Two waits per coin |
| G09 'author says numbers are illustrative / tuning not data' (two places) | removed | Page says 'those offsets are the design'. Year inferred as 2026 only |
| G13 Duo 'flies', 'several' passes, tier A/B | corrected | Page says 'multiple passes'; flight only as '(er, flight?)'; role not stated; tier B |
| G01 Jeremy Craig as a quoted developer | corrected | Named, not quoted |
| Reveal fires 1500 ms after the flash | corrected | 1500 ms after doHatch starts (about 1375 ms after the flash ends) |
| Kaplan 'illusion of random' | corrected | Exact: 'only an illusion of random' |
| G08 tier B | downgraded to B- | Author is a blogger |
| Wikipedia regulation dates (G05), near-miss review, first-run sources S01/S02/S03/S23, G14, search counts | unverified | Not re-opened or not checkable |
| Status (a) PARTLY FILLED | kept with caveat | Only one fan game's code; no studio number |
| Status (b) PARTLY FILLED | kept with caveat | Tier D/C forum scripts only |
| Status (c), (d) STILL OPEN | confirmed | Nothing found in the sources opened |
