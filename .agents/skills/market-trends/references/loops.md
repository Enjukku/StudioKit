> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-21. Kit reference: universal (J004). Evidence: owner research paper, notes `knowledge/reference/trends/01-roblox-data-loops.md` (**N1**) §11-§13; tracker numbers re-read 2026-10-20 (`fact-check-roblox.md` **FR** §3). All player numbers here are **3P-S** (highest recorded tracker sample, not the true peak) unless marked OFF. They are history for scale, not current data: pull current numbers from the store.

# Loops: track the behaviour, not the game

## 1. The loop line (always this shape)
"Player **[repeated action]** to gain **[reward]**, spends it on **[persistent change]**, then repeats against **[harder goal / rarity / social contest]**; returns because **[trigger]**." (N1 §11 O)
- Theme and monetisation stay out of the action slot. "Anime simulator" is packaging, not a loop.
- Note also: what the player controls, what can be lost, who creates opposition, how the next goal becomes visible.

**8 fields per loop:** action · reward · reinvestment · escalation · session ending · return trigger · social relationship · where monetisation enters. Keep the core loop apart from metagame and live events (a weekly admin event brings players back; it is not an ordinary Tuesday).

**Evidence order:** store page and trailer = the promise → recent unedited gameplay = the real first session → permitted direct play = friction and return triggers. Keep a two-column **promise vs observed** log. Never claim a playtest when only a video was watched; write the confidence.

## 2. Classify on separate axes
Theme · input complexity · progression model · social relationship. Brainrot is a theme and collection universe that sits on stealing, hazard runs, RNG or tower defense. Use multi-label tags for design questions, one primary loop label for share maths, and an "unclassified" bucket. Never count one game's players twice in a family total (N1 §12 O).

## 3. Families with dated evidence (2024-2026)
| Family: loop | Reference game(s) | IDs (U universe / P root place) | Highest recorded sample (3P-S) | What the dates show |
| --- | --- | --- | --- | --- |
| Offline growth tycoon: buy inputs → grow while away → harvest/sell → rarer production | Grow a Garden | U 7436755782 / P 126884695634066 | 22,375,597 on 2025-08-23 | launched 2025-03-25, top by spend within a month (OFF); far lower peaks by Oct 2026 |
| PvP ownership economy: buy/steal collectors → income → defend/rebirth → contest rarer ones | Steal a Brainrot | U 7709344486 / P 109983668079237 | 25,836,222 on 2025-10-11 | over 25 M concurrent in Sep 2025 (OFF); still large in Oct 2026 |
| Risky retrieval + idle base: cross hazards → bring collectible home → earn → better movement/storage | Escape Tsunami For Brainrots | U ? / P 131623223084840 | 4,996,032 on 2026-01-24 | much smaller peaks by Oct 2026 |
| Fishing collection: catch → sell/catalogue → better gear → rarer pools | Fisch; Fish It! | Fisch U 5750914919 / P 16732694052; Fish It U 6701277882 / P 121864768012064 | 1,273,618 (2025-10-18); 2,716,766 (2025-12-07) | Fish It credits Fisch and Fishing Simulator; both keep large 2026 audiences |
| Excavation reskin: dig → sell finds → better shovels → new rarity pools | Dig it! (one universe) | U ? / P 76455837887178 | 28,135 on 2025-02-01 | credits Fisch; near zero now; cause of decline UNKNOWN |
| Co-op expedition survival: scavenge → maintain transport → survive route → unlock runs | Dead Rails; a dusty trip | Dead Rails U 7018190066 / P 116495829188952 | (not re-checkable) | Dead Rails in June 2025 top 10 by spend (OFF) |
| Night survival crafting: gather → build/refuel camp → survive harder nights → better next run | 99 Nights in the Forest | U 7326934954 / P 79546208627805 | 14,153,173 on 2025-10-04 | launched June 2025 after a 3-month build (DEV); 7-day peak 2,141,327 in Oct 2026 |
| Fashion social judging: read prompt → build outfit → present/vote → status → next prompt | Dress To Impress | U 5203828273 / P 15101393044 | 1,743,147 on 2024-12-14 | durable through 2025-2026 |
| Short competitive mastery: duel → win keys → unlock options/cosmetics → rematch | RIVALS | U 6035872082 / P 17625359962 | 967,342 on 2026-02-14 | established; rise/fade dates UNKNOWN |
| Combat RPG grind: beat enemies/quests → power → new zones/bosses → better build | Blox Fruits | U 994732206 / P 2753915549 | 2,781,531 on 2024-12-31 | long-lived predecessor |
| Social roleplay and pet collection: inhabit a place → personalise/collect → trade/perform → return for friends | Brookhaven; Adopt Me | Brookhaven U 1686885941 / P 4924922222; Adopt Me U 383310974 / P 920587237 | — | Brookhaven top search of 2025 (OFF): durable, not early |
IDs: universe IDs read from the public game pages and the Games API on 2026-10-21 (J004-T08); root place IDs from the tracker page URLs read on 2026-10-20 (`fact-check-roblox.md` §3; Dead Rails from the paper, S23). "U ?" = universe not yet resolved: resolve by hand (§ universe IDs in `trend-scan/references/sources.md`). Recorded samples are from Rolimon's pages read once for the fact-check (history only; Rolimon's is not used for studio decisions without consent).

A family table is not a market-share claim. New families come from the store and the weekly scan, never from memory.

## 4. Proven loop + new theme + twist
- **A twist changes a decision, a stake, cooperation or expression.** A new noun on the same assets and onboarding gives players little reason to switch (N1 §13 O). Examples of decision changes: risky retrieval turns "wait for income" into "how far is it safe to go?"; co-op survival turns solo accumulation into division of labour and shared failure.
- **Same family, different outcomes:** Fish It (2.7 M recorded) and this Dig it universe (28 K) share a structure; public counts cannot separate theme, quality, promotion, timing or live operations as the cause. Not a matched experiment; a low current count is not proof of commercial failure.
- **A twist does not guarantee staying power:** Grow a Garden 2 (guilds, night-time stealing) reached a recorded 929,371 on 2026-06-19 (3P-S) and was named a fast riser by Roblox (OFF); its 7-day peak was 2,984 by Oct 2026.
- **Growth stories are outliers:** Grow a Garden's "500 to 100,000 in two weeks" is a developer recollection about a selected success (DEV), never a target.
- **Launch-lag record:** keep `launch_date`, `predecessor_breakout_date`, `public_evidence_date`, `development_start` separate. Missing → a range or UNKNOWN, never "built in a week".

## 5. What the scout hands on about a loop
The loop line, the 8 fields (with confidence per field), the reference games by universe ID, the family's trend from the store (rising / steady / fading with dates), the gap the twist would fill, and the rights gate (`copying-and-rights.md`). The fantasy, title and design belong to the game-designer.
