---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J014-D3 (owner: "Show it to me before setting anything up. No bot tokens or passwords in the repo or in chat."); fact sheet knowledge/reference/live-ops/feedback-routes-fact-sheet.md (Q/R ids, read 2026-10-21); DevForum 4665118 read by the lead 2026-10-21
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Feedback plan: one place for player feedback (approved J014-D5, 2026-10-21)

**Status: approved, both stages (J014-D5).** Nothing is set up yet: stage 1 starts when a game launches; stage 2 runs the build tickets in §8 in that game's first update. No key, bot, webhook, channel or code exists yet.

## 1. What the plan does
Player feedback from the game, Discord and Roblox's own rating page goes into **one folder on the owner's computer**. The live-ops agent reads only that folder. A script counts players per theme (`tools/liveops/feedback_count.py`, built and tested in J014-T06).

## 2. Rules the plan keeps (warnings first)
| # | Rule | Source |
| --- | --- | --- |
| W1 | The game never sends player names or user ids to Discord or any chat app. Roblox says creators "may not send individual user data to social platforms, chat applications" | DevForum 4665118, Roblox staff, 2026-06-02 (lead read the post) |
| W2 | No link, invite or handle to Discord inside the game. Discord links show only on the game page, only to age-checked players aged 16 or more | Q6-01..Q6-04 |
| W3 | Discord is for ages 13 and more. So Discord feedback never speaks for younger players. The in-game route is the route for everyone | Q5-27, Q5-28 |
| W4 | Player-typed text is filtered on the server before it is stored. Fixed choices come first | Q2-01..Q2-03; `platform-policy` P-06 |
| W5 | Keys and tokens live only in the owner's environment variables. They never go in the repo, notes or chat. The agent never sees them | Q3-12; AGENTS.md §3.4 |
| W6 | A player's deletion request (right to be forgotten) must delete their feedback everywhere: in Roblox and in the local folder | Q8-01..Q8-03 |
| W7 | Discord message content is never used to train an AI model | Q5-15 (third-party quote of Discord's policy; owner to confirm, §7) |

## 3. The routes, and the recommendation
| Route | What players do | What it gives the agent | Cost | Recommend |
| --- | --- | --- | --- | --- |
| A. Roblox built-in feedback prompt | The game opens Roblox's own "rate and comment" window at good moments (after a round, after an event). One per player per day | Rating, device, platform, filtered comment (comments 13+ only). The owner exports a `.csv` file from Creator Hub. No API exists | 1 small code change. No secret | **Yes, at launch** |
| B. Our own in-game form | A small "Tell us" prompt at set moments (one in the first session), plus an always-available "Report a problem" entry. Fixed choices first ("I could not find…", "Too hard", "Bug", "Idea"), then optional short text | Exact themes, the moment, build version, and who saw the prompt (needed for honest counts). Stored in a Roblox data store. A script on the owner's computer reads it with an Open Cloud key | Feature-builder work (UI + server + tests) and a read script. Secret: 1 Open Cloud key, read-only, one data store | **Yes, first update after launch** |
| C. Analytics events for the form | Nothing extra | "Prompt shown / sent" counts and the chosen category for all players, in Roblox analytics | Part of B | **Yes, with B** |
| D. Discord forum channel "feedback" | Players post in one forum channel, each post with a required tag (bug, idea, too hard, …) | Detailed posts from engaged players aged 13 or more | The owner makes the channel. No secret | **Yes, at launch** |
| E. Discord read script | Nothing extra | The script reads only the "feedback" channel, on demand, when the owner runs it. No bot runs all the time | A small Discord app. Secret: 1 bot token. Message Content switch (free under 10,000 users, Q5-11) | **Yes, with B** |
| F. Game sends feedback to Discord by webhook | — | — | Breaks W1 and Q3-19 risk | **No** |
| G. Discord export tools that use a personal account token | — | — | Forbidden by Discord (self-bots, Q5-04) | **No** |

**Recommendation: two stages.**
1. **At launch (no secrets, about 1 small code change):** route A in the game, and route D on Discord. Each week the owner exports Roblox's `.csv` file and drops it into the inbox folder. The agent reads it. For Discord the owner copies the week's forum posts into a text file, or the agent waits for stage 2.
2. **First update after launch:** routes B, C and E. The owner makes 2 secrets (§5). After that, one command fills the folder.

## 4. The one place
```
<FEEDBACK_DATA_DIR>          default <repo>/.tools/feedback-data/  (gitignored: never in git)
  inbox/   raw files by date: roblox-feedback-2026-11-03.csv, discord-2026-11-03.jsonl, ingame-2026-11-03.jsonl
  items/   one line per feedback item, in the count tool's format; ids replaced by pseudonyms
  sorts/   the agent's weekly feedback sorts (templates/live-ops/feedback-sort.md)
```
- **Pseudonyms.** Before anything reaches `items/`, the scripts replace each Roblox or Discord id with a one-way code made with a secret salt (environment variable). The agent can count distinct players, but it cannot see who they are.
- **Rebuild, not append.** In-game items are read fresh from the Roblox data store each time. A deleted player is deleted in Roblox (deletion template), so the next pull drops them from the folder (W6). Raw inbox files older than a set number of days (PROPOSAL: 90) are deleted by the script.
- **Counts per source only.** Roblox gives new players a different id in each game, and Discord ids are separate. So the same person in two sources cannot be matched. The count tool reports "overlap unknown" (Q8-09, X-01).

## 5. Secrets (owner only; never in the repo or chat)
| Environment variable | What it is | The owner makes it in | Limits |
| --- | --- | --- | --- |
| `ROBLOX_FEEDBACK_KEY` | Open Cloud API key | Creator Hub → API Keys | Read-only data-store scope, one data store, one game. Expires after 60 days unused (Q3-09..Q3-11) |
| `DISCORD_FEEDBACK_BOT_TOKEN` | Bot token of a small Discord app | Discord Developer Portal | Bot invited with "read messages" in the feedback channel only. No admin rights |
| `FEEDBACK_SALT` | Random text for the pseudonyms | The owner's computer | Never shared |

The scripts read these at run time and never print them (same pattern as `tools/trends/trend_keys.py`).

## 6. Honest counts: who could answer
Each sort records who could answer, per source (template §A):
- **In-game form:** players who saw the prompt (from route C events), players who answered. The prompt goes to documented groups, not only to winners or event finishers, and **one prompt reaches new players in their first session** (for example when they leave the tutorial area or after a few minutes): a prompt that waits for the 3rd round never reaches the players who quit early (J014 G2 test). A **"Report a problem"** entry (lost progress, missing purchase, bug) is always available in the menu, outside the timed prompt.
- **Roblox built-in:** players who rated; comments are 13+ only.
- **Discord:** members who posted; ages 13+; most engaged players.
- **Silent players:** the analyst's behaviour data, not feedback.

## 7. Owner actions (in order, only after "yes")
1. Approve or change this plan (G1b).
2. Launch stage: create the Discord forum channel "feedback" with required tags. Each week, export the Creator Hub Feedback `.csv`.
3. Stage 2: create the 3 secrets in §5. Switch on Message Content for the Discord app.
4. Read once and confirm (the helper could not open them, HTTP 403): the Discord Developer Terms and Developer Policy (deletion and AI clauses, W7), the Roblox Creator Third-Party App Policy.
5. Write a short feedback notice for players: what is collected and why (wording from marketing; PROPOSAL).

## 8. Build tickets after "yes" (not started)
| Ticket | Who | What |
| --- | --- | --- |
| route A call sites | quick-builder | Call the built-in prompt at agreed moments |
| route B + C | feature-builder (high: player data) + reviewer | Form UI, server filter, data store keyed by user id (deletion templates), analytics events, tests |
| importers | feature-builder (medium) | Roblox `.csv` → items; Open Cloud data store → items; Discord channel → items; pseudonyms; 90-day cleanup; offline tests |
| plan in live-ops-craft | lead | The weekly feedback steps point to these commands |

## 9. What is not known (not filled)
- Roblox does not say how long it keeps built-in feedback, or the age rule for the in-game prompt (Q1-04, Q1-11).
- No Roblox page says whether text that only the developer reads must be filtered. The plan filters it anyway (stricter reading).
- Discord's rules on consent and a privacy notice for apps were not readable (Q5-17).
