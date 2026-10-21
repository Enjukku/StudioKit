---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J014 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J014 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | G1 for J014 (`job-card.md`, `brief.md`) | approve / change | approve | waits for your answer |
| 2 | Skill names | `live-ops-design` + `live-ops-craft` (kit pattern) | as stated | as stated |
| 3 | The analyst is planned, not built. Live-ops depends on it for every number | (a) live-ops uses the `analytics` skill; hand-off briefs to the analyst are written now; the lead holds analyst tickets until the role exists; (b) build the analyst first | (a). Build the analyst next, before the first game goes live | (a) |
| 4 | Feedback plan. The paper gives no setup, only the rules for sampling and counting | The plan compares routes and recommends one: in-game (Roblox's own in-experience surveys vs a small feedback button that saves to a data store the agent reads through Open Cloud), Discord (you export a channel by hand vs a read-only bot on your machine with the token in an environment variable), comments and reviews (you paste). One folder of dated files is the "one place". I show it to you as gate G1b. Nothing is set up before your yes | as stated | as stated |
| 5 | Feedback count tool. "Count distinct players per theme" must be exact, not a model guess | (a) a small Python tool: reads the tagged feedback file, counts distinct authors and messages per theme per source and week, flags possible double counts; offline tests; (b) no tool, the agent counts | (a) | (a) |
| 6 | Effort for the Sonnet helpers (extract, fact-check, research, test pack, grade) | high / medium | high, as in J012 | high |
| 7 | G2 test subject. No game is live yet | (a) a synthetic live game: one analyst weekly report, about 150 feedback items from 4 sources, a trend note and a builder capacity line, all labelled synthetic. The agent sorts the feedback, ranks a plan, designs one event, writes the update brief and patch notes; (b) wait for a live game | (a), then repeat on the first real game | (a) |
| 8 | Who writes patch notes | (a) live-ops writes the facts (what changed, known issues, from your feedback); marketing writes the announcement voice; you publish; (b) live-ops does both | (a): the marketing books already own announcements | (a) |

# Decision digest: 2026-10-21 (J014 G1b)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 9 | Feedback plan (`feedback-plan.md`) | approve / change / stage 1 only | approve: stage 1 at launch (Roblox built-in prompt + Discord forum channel, no secrets); stage 2 in the first update (own in-game form, analytics events, on-demand Discord read script, 3 secrets in your environment) | nothing is set up; the plan waits |
| 10 | Job numbers. J013 is used by 3 jobs (analyst, film director, this one). Their ticket and decision ids collide | this job renamed to J014 (done); the other two chats choose for themselves | tell the analyst or film-director chat to take a free number | only this job changes |
| 11 | "One loud author" warning in the count tool: one author wrote at least 5 of a theme's messages and at least half of them | keep / change the numbers | keep: it is a warning only and changes no count | keep (PROPOSAL) |
| 12 | Standing emergency authority per game. The G2 test found live harm (a crate without odds, missing purchases) with nobody allowed to act before the owner answers | (a) per game, you pre-approve one action: "hide or switch off anything that breaks a Roblox rule or loses players' purchases or progress, then tell me the same day"; (b) every case waits for you | (a); it goes into the game's decisions when the first game launches | (b) until you answer |

# Decision digest: 2026-10-21 (J014 G2)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 13 | G2: the first test (`g2/live-ops/plan-2026-10-21.md`, `grades-g2.md` 24.5 / 26) | approve / change | approve; the 18 skill fixes are in (`skill-gaps-T08.md`) | waits for your answer |
| 14 | Hidden cases H1-H4 and E2's crate and countdown checks were not exercised by this pack | (a) one short extra run (1 agent + 1 grader, Sonnet/Opus) before G3; (b) run them on the first real game | (a): cheap, and E2 covers paid random items and timers, the riskiest rules | (b) |
