> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `live-ops-design`. Evidence: notes `01` §6 (LP:161-210), `02` §2 and §5 (LP:287-336, 401-429), Roblox fact-check FR-05..FR-58 (read 2026-10-21), feedback-routes fact sheet Q6. Tags: V platform-documented · E someone's account · O proposal. Code patterns for policy: `platform-policy`. Revised by J018 maker live-ops-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§1 the promise and the start, §2 confirmed celebrations and honest reveals).

# Events, offers, communication and Roblox rules

## 1. What an event is (O)
A temporary player proposition with **an entrance, a repeatable activity, a progress or reward structure and a stated end** (LP:163). A themed lobby is a theme. A discount is an offer. Either can support an event; neither gives a reason to return by itself. Roblox itself separates temporary events from permanent updates and expects an event to move several measures at once (FR-05).

**The promise (O).** Every event has one sentence, in player words, that says what players do and get; its look, sound, UI and announcement promise exactly that (rule: SKILL §4 L-16; checked on captures: `live-ops-craft/references/event-review.md` E-01, E-02).

**The start (V, O).** Roblox's planning page asks for an impactful, memorable start and a decision whether the event is limited to one space or game-wide (`liveops-planning.md:53-55`, read 2026-10-22). The start is a designed moment, and the entrance is visible in the first view of a player arriving by spawn or teleport (E-03).

**Audience first.** Active players wanting variety, lapsed players needing a return reason, new players needing an easy introduction, friends coordinating play: do not use one completion curve for all four. A returner event must not require every system added while the player was away. A new-player event must not hide its activity behind veteran progression (LP:165).

**Length (O).** Set it from observed play opportunities, content exhaustion and the team's coverage. Estimate required effort from reward costs and **observed earning distributions** (not only the average). Model late joiners, low-frequency players, device limits, missed days and skill gaps. Completion must be reachable through healthy play; "mathematically possible with near-perfect attendance" fails. If the reward does not fit an ordinary routine: lower the requirement, extend the window or add catch-up (LP:167). Roblox's events page says "the best events run for 7-30 days" (FR-15): a Roblox opinion, not a measured optimum. No source gives an optimal length (OQ-03).

**Shapes.** A multi-week progress window and a single synchronized spectacle are different shapes (Adopt Me 4-week festival vs Fortnite's live finale, `cases.md`). A small studio usually runs repeatable activities and scheduled reward beats more reliably than a one-shot, high-concurrency show. If a moment must be synchronized: plan an encore or another route for players who miss it, and rehearse the failure (LP:169).

**Calendar (O).** For each event: game beat, theme, target cohort, content lock, test window, policy and approval dependencies, communication dates, staff coverage, gameplay end, reward-claim end, measurement dates. Write time zones; show local times to players. Start from the audience's countries and routines; never assume a holiday is global; never infer a child's personal schedule (LP:171).

**Trends (O).** A trend qualifies only if its appeal fits the game, its useful life is longer than build-and-review time, the audiences overlap and the rights exist. Ask the trend scout for first-seen date, growth or fade, audience, source reliability, saturation and rights. A broad seasonal idea on reusable mechanics beats a rushed copy of a protected character (LP:173).

## 2. Honest urgency (O, with Roblox rules in §4)
Urgency = **a true end, clear consequences, a fair way to take part.** Tell players which rewards expire, whether currency converts, whether a cosmetic may return, whether purchases speed progress (LP:175).
Never: fake stock counters, timers that reset, hidden requirements, streak loss that punishes absence, late purchase prompts for rewards the player can no longer earn in time, permanent competitive power that depends on being present in a narrow window.
A returning player gets a clear next action and a route back; absence never grows into a penalty (paper rule 13).
Celebrations and paid random reveals: SKILL §4 L-19.

## 3. Communication (V limits, O practice)
| Channel | Limit (read 2026-10-21) | Use it for | FR |
| --- | --- | --- | --- |
| Experience events | at most 10 ongoing or upcoming ("currently"); "Notify Me" reminders; joins through an event carry its id in `player:GetJoinData()` | a real event with a time | FR-11, FR-12 |
| Trending Events, off-platform featuring | Trending: active public event started within 7 days, at least 1,000 RSVPs. Featuring: submitting creator 13+, at least 7 days before start | | FR-15 |
| Update announcements | 60 characters; once every 3 days. Roblox's tips: say what is new and reachable; avoid vague "bug fixes"; avoid too many updates in a short time | broad news | FR-13, FR-14 |
| Personalized experience notifications | recipient 13+ and opted in; under-13 get update announcements only; one per user per day per experience; game needs 100 visits and no moderation hold; delivery not guaranteed | a true, player-specific event ("your build finished") | FR-16 |

These are ceilings, not a sending plan. Send a message only when the receiver has a real reason to return (LP:291).

**Sequence (O):** announce the benefit and timing when the work is credible → explain entry and eligibility at release → publish exact changes and known issues (`templates/live-ops/patch-notes.md`) → remind near real deadlines → report the result or the next correction. The game's own UI orients returning players; Discord is never the only explanation (LP:295; W2 in the feedback plan).

**Promise ledger (O).** Live-ops and marketing share one: for every claim, the approved feature, audience, real start and end, reward conditions, exclusions, build readiness and fallback wording. A teaser never outruns the build. If a feature slips, every surface changes together; no expired event label stays in the title, icon or description (LP:289). Marketing owns the voice (`marketing-design`); live-ops owns the facts (J014-D4).

**Roadmap labels (O, not a Roblox standard):** "now" = approved and being delivered; "next" = prioritized, subject to readiness; "exploring" = no promise. Dates only on work with credible dependencies and approved capacity (LP:297).

**Update tags (V absence).** No Roblox page says an "[UPDATE]" title tag boosts recommendations; Roblox says description hashtags are unused in ranking and suggests an optional short "Recent updates" blurb (FR-48). Recommendations reflect what players do after they find the game; updates are one of four named drivers of change, with seasonality, competition and Roblox's own changes (FR-47). Never change title, icon, ad spend and onboarding together and credit the patch.

## 4. Roblox rules for events and offers (read 2026-10-21; re-read at design time)
**Policy is a release gate with a named owner and current links** (LP:403 O). Past compliance is not enough when the audience, reward, channel or content changes.

| # | Rule | Strength | Source |
| --- | --- | --- | --- |
| R1 | Present products "transparent, honest, and user-friendly"; users "must never be misled, confused, or pressured" | must | Monetization page `:142, :147` (FR-54) |
| R2 | Discounts "must be genuine and fair": not genuine if the item is always "on sale"; not fair if offered "only ... for a very short time, pressuring users" | must; no number for "very short" | `:142-145` (FR-54) |
| R3 | Never claim "almost out of stock" or "only available for a short time" when untrue. "Don't use a countdown timer that isn't accurate or automatically restarts for the same item" | practices "to avoid at all times" | `:149-152` (FR-54) |
| R4 | Avoid pushy or urgent messages with minors ("GET IT NOW" → "View Item") | recommendation; no age defined | `:167-190`; Help article 2026-10-08 (FR-57) |
| R5 | Promotions should suit all audiences by default | should | `:156` |
| R6 | Notifications: "not permitted to incorporate dark patterns"; false time pressure is one of four named examples ("Make a purchase ... in the next 10 minutes") | not permitted; notifications only | FR-19 |
| R7 | "Games should not require users to turn on notifications" to play or advance | should | FR-18 |
| R8 | Paid random items: direct or indirect (Robux-bought currency, keys, spin tickets, bundles containing a random item); all final outcomes and numeric odds before purchase, summing to exactly 100 % (rounding allowed with a disclaimer); boosts, pity and rate-up change shown odds live; every outcome gives some benefit; `ArePaidRandomItemsRestricted` and `IsPaidItemTradingAllowed` gates | must | FR-35..FR-41; `platform-policy` §A |
| R9 | Maturity questionnaire: an update that changes any answer must be resubmitted (owner action). No playable or simulated gambling | must | FR-42, FR-43 |
| R10 | Brand events are ad integrations: eligibility check, labels and disclosures; rewarded video 13+ only; labels "frequent and sufficiently large" if players 12 or under are in the audience | must | FR-44 |
| R11 | No content that recreates or capitalizes commercially on real-world sensitive events | prohibited | FR-45 |
| R12 | Creators cannot give Robux or money refunds; players go to Roblox Customer Support | platform fact | FR-46 |
| R13 | Social links: added and seen only by age-checked 16+; up to 3; never shared inside the game. (One Roblox page says 13+ "upcoming": unresolved, keep 16+, re-read) | must | FR-21..FR-24 |
| R14 | Player data: no user ids, usernames or display names sent to social platforms or chat apps | must not | DevForum 4665118, 2026-06-02 (fact sheet Q8-07) |

**What Roblox allows.** Roblox's own design pages recommend truthful limited-time content and visible timers ("temporary availability incentivizes players"; "Making the timer ... highly visible") (FR-55, FR-09). There is **no blanket ban on truthful limited-time offers**. What is forbidden or flagged is untruthful urgency. The studio's own bar is higher (§2): it rejects fake scarcity, hidden costs and pressure, especially for younger players (O).

**Age bands (do not carry one to another feature).** Kids 5-8 and Select 9-15 reach only games whose label allows them; Roblox 16+ (age-checked) reaches all but Restricted; Restricted 18+. Notifications 13+, featuring submitter 13+, rewarded video 13+, social links 16+. PolicyService flags vary by age range, location and platform (FR-58). "Younger players" has no single Roblox age: **design every offer to pass the strictest reading** whenever the label lets Kids or Select accounts in (FR inference, adopted O).

**Launch checklist.** `templates/live-ops/event-design.md` §E. A failed must row blocks release.

**Owner vs platform (O, 02 X-37).** The owner decides every studio choice. Nobody in the studio can waive a Roblox rule. When the owner's choice and a rule conflict, build the version that keeps the rule, name the rule, and return `needs-decision` (AGENTS.md §4).
