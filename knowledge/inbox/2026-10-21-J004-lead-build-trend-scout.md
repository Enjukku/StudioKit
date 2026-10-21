---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J004
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-21

# Lessons: building the trend-scout agent (J004)

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | Fact-checking access terms first changed the build: Twitch (24 h cache), YouTube (30-day limit), Steam (display-only licence), Roblox Terms from 2026-11-01 (§9.2 AI clause) | For any data-tool agent, run the permission fact-check before briefing tool builders; put the rulings in a registry the code obeys (ruling + `valid_until`) | fact-check-outside.md §3, fact-check-roblox.md §1 |
| 2 | The Roblox fact-checker found the live help page shows the Nov 1 header over the May 19 body | Check which terms text is in force (archive copy), not the page header | fact-check-roblox.md §1 |
| 3 | 45 builder tests passed, yet an independent review found 17 defects (429 stop ignored, retention gaps, wrong numbers on the page) | Builder tests mirror the builder's reading; a separate high-effort review with reproduced failure scenarios is worth its cost before the first real output | review-J004-tools.md |
| 4 | First eval run: 2/5. The agent followed the skill literally (no loop without an observed loop; no ranking) | Evals found skill gaps, not honesty failures: write loop-hypothesis and tie-break rules explicitly; make eval inputs provoke every check they grade | grade-J004-evals.md, -r2.md (4/5) |
| 5 | The first real scan found the method could not give growth under the rules (weekly runs, Roblox stop on 2026-10-31) | Run the first real task before calling the agent done; it finds whole-system gaps that unit tests and evals miss | first-scan-notes.md T1, T2 |
| 6 | "Manual" sources needed a second split: may an AI agent fetch the page, or only the owner? | An AI fetch is a robot under most terms; record per source who may read | sources.md §2 |
| 7 | Hidden-case contamination: two held-out games appear in the loop catalogue outside the held-out lines | When holding out cases, grep the whole paper for the held-out names first | evals/briefs.md leak note |

Owner corrections, word for word: "Just make sure that all the Sonnet models are actually used on high effort." (J004-D2)

## Outcome and owner corrections (word for word)
- "I'm telling you, it's completely fine. You can just use them. They're on the web for anyone to use." → lead kept the sites' terms (RoTrends, SullyGnome forbid robots) and offered owner-requested visible-browser reads; owner accepted (J004-D7).
- "I don't want to get myself banned by looking at Roblox data, so we just shouldn't do that." (J004-D10)
- "This is just going to be like a rough draft, but we probably won't use this agent because it just didn't work out. That's all right." (J004-D11)

| # | Lesson | Evidence |
| --- | --- | --- |
| 8 | For a data agent, check data access and platform rules at Gate 1, before building tools: here the deciding fact (Roblox Terms from 2026-11-01, trackers banning robots) arrived after the tools were built, and it ended the job | J004-T03, J004-D10, J004-D11 |
| 9 | Explain access limits in plain words early (what the owner can read vs what an AI may collect); the owner first read "public to look at" as "free for an agent to collect" | owner messages 2026-10-21 |
