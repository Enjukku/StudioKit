> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `live-ops-design`. Evidence: notes `01` §4-5 (LP:98-159), Roblox fact-check FR-01..FR-10 (read 2026-10-21), cases fact-check FG (`fact-check-cases.md`). Tags: V platform-documented · E someone's account · O the paper's or the kit's proposal. Revised by J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§4 items row, variants and colourways, worlds revisited).

# Update rhythm and content types

## 1. What Roblox's own pages say about rhythm (V, read 2026-10-21)
Roblox gives **several rhythms on different pages, for different things**. Never average them into one "Roblox cadence" (01 X-45).

| Page | Says | Scope | FR |
| --- | --- | --- | --- |
| Monetization overview | "A weekly cadence for updates is ideal"; monthly "at the bare minimum" | general guidance; the page says the techniques guarantee nothing | FR-01 |
| Content updates | many games ship content-cadence updates "every two weeks to one month"; "fewer than three weeks' effort" per content-cadence release is recommended | the three weeks is **effort per release**, not the gap between releases | FR-02 |
| LiveOps essentials | content cadence builds "exclusively" on existing systems; it ranges "from weekly to monthly" with the developer's capability; a release that adds a system is an **expansion** and may take many months | | FR-03, FR-04 |
| LiveOps planning | events are temporary activities; "content updates" are large permanent releases (this page's word, opposite to the content-updates page: keep the terms apart) | | FR-05 |
| Season pass design | one month "is a good starting point"; at least one week of rest between seasons; ten tiers "a good place to start"; season length "is based on your team's bandwidth" | starting points, not targets | FR-07 |

All of these are **recommendations**. None is a platform rule, a measured comparison or a promised discovery boost (FR-01..04; LP:100 O).

## 2. Choosing a rhythm (O)
Pick the rhythm from four constraints, read separately (01 RH):
1. How fast the target players use up meaningful content.
2. How often their normal routine gives them a reason to come back.
3. How much change the game can take without confusing players.
4. How reliably the team can build, test and support that change.

More builder time does not prove players want more tasks. Bored veterans do not prove new players need another system.

| Candidate rhythm | Fits | Benefit to test | Cost to include |
| --- | --- | --- | --- |
| Weekly | variants of existing systems, rotating challenges, small reward drops, targeted fixes | predictable return appointment, fast correction | repeated QA, communication, support, context switching |
| Every two weeks | a bounded content package or several related improvements | a more complete, readable change | still easy to over-commit if every release adds a system |
| Monthly | a real area, a feature package, a prepared event | more meaningful novelty, clearer marketing | a struggling cohort waits longer for help |
| Seasonal | a theme over several releases | coherent goals, a clear return moment | expiry pressure, catch-up work, large integration risk |
| As needed | security, data loss, exploits, severe stability | stops harm fast | never an excuse for poorly tested routine releases |

This table is a menu, not a benchmark. Starting shape for a small studio (O): **one content lane on existing systems, one separately scoped improvement lane, and emergency capacity.** Choose the rhythm only after builder estimates and consumption evidence exist. Do not draw parallel lanes when the same builder would do everything in sequence.

**Public cadence.** Keep a public promise ("new content every Friday") only when a credible minimum meaningful release stands behind it every time (LP:120 O). A fixed release-day appointment has costs for the team and the players: Adopt Me moved from fixed Fridays to announced times after 56 weekly updates (`cases.md`, FG-01).

## 3. Capacity rule (O)
- Committed work must fit the capacity left **after** maintenance and release support already committed (LP:116).
- Ask builders for **active effort and elapsed lead time separately**: concept approval, design, art, code, integration, device tests, progression simulation, localization, policy checks, announcement, rollout, support (LP:114).
- Use measured past throughput when it exists; otherwise an estimate range with a confidence label. No universal buffer percentage. Never "AI can build this in a day". Adding unmeasured parallel agents is not a capacity estimate.
- If estimates exceed the window: cut scope, reuse a validated pattern, move the date, or cancel.
- Small vs large: small updates shrink each failure and teach faster, but release overhead can eat the saving. Large updates give an easier return reason and fix structural problems, but stack risks and blur attribution. Compare a bundle against its smallest useful alternative. An empty weekly reskin can be worse than a useful monthly change. A large expansion never replaces a broken purchase fix (LP:118).

## 4. Content types: name the player problem first (O)
"Add a season" is packaging, not a hypothesis. Revenue can rise because more players arrive, more players pay, payers spend more, or purchases move forward from later; these mean different things for durability and trust (LP:131). **No source gives a portable lift for any content type** (01 N-45; OQ-01).

| Type | Player job it may do | Measure | How it fails |
| --- | --- | --- | --- |
| Areas, quests, story | a next destination for progressed players; a return reason for lapsed ones | eligibility, reach, completion, return after completion, cost | most players cannot reach it |
| Items, pets, characters, gear | expression, collection, strategic choice | adoption and continued use, collection goals, spending displacement, balance | inventory bloat, strictly better purchases, old rewards made worthless; a variant that loses the original's anchors; a premium item that reads like the standard one |
| Limited-time modes | temporary novelty and social play | participation among eligible players, repeat sessions, core-mode displacement, queue health | split matchmaking; a mode unrelated to the game's appeal |
| Seasonal goals and passes | readable progress across visits | start / finish / drop-off by cohort, payer and non-payer health | homework, missed-day penalties, rewards that need unhealthy play |
| Collaborations, holiday themes | recognition, a shared moment | qualified arrivals, reactivation, later core play, margin | spectacle swamps the game; expires before costs return |
| Balance changes | fair competition, strategic variety | outcome spread by skill and context, pick rates, counterplay | reactive nerfs destroy learning |
| Quality-of-life, accessibility | remove repeated friction | task success, abandonment, device performance, support load | dismissed as "no content" because it is not visible |
| Bug, exploit, stability fixes | restore the intended game and economy | error and crash rate, failed rewards and purchases, affected cohorts | new monetization ships while known damage continues |

**Season pass (V starting points, O sizing).** Roblox's season-pass page also recommends automatic enrolment, daily missions that never need hard currency, double XP in the final week as catch-up, full premium rewards for tiers already passed, and a visible countdown (FR-10, FR-09). Size the real pass from observed session opportunities and earning rates, and model late starters and low-frequency players. A large tier count can add admin work without adding meaningful play (LP:144).

**Add, improve, remove (O).** Add when the need requires a new capability and the game can absorb it. Improve when an existing system serves the need badly (access, usability, balance, depth). Remove or merge when systems duplicate each other, split play, cost too much to maintain or undermine the intended experience. "More rewards" may really mean unclear progress, irrelevant rewards or a missing social goal (LP:224).

**Variants and colourways (V, O).** Roblox's content-updates page names simple variants of existing assets, such as slight colour changes, as ideal recurring content because few people can make them quickly (`content-updates.md:34`, read 2026-10-22). Each variant keeps the original's identity anchors and changes no stat (`game-design/references/systems-economy.md` §8); a colourway can change the value balance, so the art director re-checks it before it ships.

**Worlds are revisited (O).** A map or system is never done forever: keep revisit rows with their evidence in the backlog. A new world or zone states its escape in one line and differs clearly from the last one (palette, shapes, theme).

**Retirement (O).** Before removing content, check active use, paid entitlements, dependencies and an alternative path for affected players. Retirement is a design and communication project; an announcement is not a safe migration (LP:152). When progression changes, explain the migration before asking players to invest more in the old system (Clash Royale, `cases.md`).
