---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent trend-scout)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · medium · 2026-10-20

# J004 — Build the trend-scout agent

| Field | Value |
| --- | --- |
| Job id | J004-trend-scout |
| Size | L (new role, 2 skill books, one research paper to extract and fact-check, data tools with tests, report template, schedule plan, first real scan) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | Closed 2026-10-21: in use in legal-only mode (decisions.md J004-D12, supersedes D11). Built: 2 skills, role, tools (69 tests), evals 4/5, first scan |

## Owner's words (2026-10-20, excerpts)
- "an agent who can accurately look at the market and depict upcoming trends by looking at real-world market data ... some sort of visual for me to look at, or some sort of paper"
- "Use it as strong evidence, but not as gospel. Check claims that matter, especially numbers, data sources and Roblox facts, and drop what you cannot back up. Be strict about which numbers are official and which are third-party estimates."
- "It tracks core loops, not only games ... the 'proven loop, new theme, plus a twist' opportunities ... It flags where copying a loop crosses Roblox rules or copyright."
- "It sends a weekly report to me and the game designer ... It does not design the games; the game designer does that."
- "Data tools: scripts in tools/ that pull the public Roblox data (and other free, legal sources) and save the history ... Tests for each script. Only legal, allowed access: no scraping that breaks a site's terms. Never put keys or passwords in the repo."
- "A plan for running the scan every week automatically. Show it to me before setting anything up."
- "Keep the analyst role (our own game's player data) separate from this one."
- "Model: Sonnet, medium effort for the agent. Scripts and tools are built on Opus at medium effort or higher."

## Goal
One `trend-scout` agent that finds what is rising early, with dated data, and says how sure it is. Each week it gives the owner and the game-designer: rising Roblox games with their numbers, rising core loops, outside trends that may move into Roblox, and the top 3 research opportunities ("proven loop + new theme + twist") with evidence, rights and policy flags. Every number is marked official, third-party sampled, third-party estimate or derived. It never designs the game.

## Material received (outside git)
| File | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\uterd\NewGame\Roblox_Trend_Scout_Research_2026.txt` | Evidence contract; Roblox public endpoints and their limits; trackers and their models; growth, breakout and fade formulas; 13 loop families with sampled numbers; proven loop + twist cases; copyright vs mechanics; outside-trend chains (Squid Game, brainrot, Verity, Bruno Mars); Steam, mobile, social and Google Trends access; legal access registry; timing; opportunity scoring sheet; weekly report template; source register S01-S62 | 649 lines, 102 KB | high: every block tagged VERIFIED / EXPERIENCE / OPINION with provenance and a dated source; most sources are dated after the model cutoff, so numbers and access terms need a live check |

## Scope
| In | Out |
| --- | --- |
| Reference notes in `knowledge/reference/trends/` + 2 fact-check tables (Roblox; outside platforms and access terms) | Designing games (game-designer) |
| 2 skill books: `market-trends` (design) and `trend-scan` (craft) | Our own game's player data (analyst, planned) |
| Role file `trend-scout`, eval briefs, hidden test set | Building the marketing agent (roster row only; it is already "planned", J003-D4) |
| Data tools in `tools/trends/` with tests in `tools/tests/`: history store, Roblox public counters, growth/breakout/fade metrics, free official outside sources, manual-entry import, weekly report renderer (Markdown + HTML charts) | Scrapers for sites whose terms forbid it (SteamDB, Rolimon's, RoVitals, RoTrends, TikTok, Instagram, Reddit, Discord) |
| Weekly report template | Paid data services (Sensor Tower and others) |
| Schedule plan (shown to the owner, not set up) | Setting up any schedule before the owner says yes |
| Hand-off briefs to game-designer and marketing (`rules/messages.md`) | Changing other skills (only pointers to them) |
| First real scan (G2) | |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×2 (paper §0-2; paper §3-10 + register) | Sonnet | high (J004-D2) | dense notes per part |
| fact-checkers ×2 (Roblox facts, endpoints, numbers, terms; outside platforms, APIs, quotas, access terms) | Sonnet | high (J004-D2) | fact-check tables: claim, source, checked against, verdict |
| tool builder A (store, Roblox collector, metrics, report renderer) | Opus | medium (owner: "Opus at medium effort or higher") | `tools/trends/` core + tests |
| tool builder B (Steam, Apple, YouTube, Twitch, manual import) | Opus | medium | `tools/trends/` sources + tests |
| lead (merge, skills, role, evals, code review, schedule plan, hand-offs) | Opus | medium; high for code review and the access-terms ruling | skills, role, evals, review notes |
| trend-scout (new, first scan) | Sonnet | high for this job (J004-D2); role default medium | G2 weekly report |
| grader (evals, separate context) | Sonnet | high | rubric scores on the hidden set |

## Mechanism
Subagents, max 3 at a time. Wave 1: 2 extractors + Roblox fact-checker. Wave 2: outside-platform fact-checker + tool builder A. Wave 3: tool builder B (after the store interface exists). The lead writes the skills (needs the whole picture) and reviews the code with `code-review`. The new agent runs the first scan as a subagent; a separate grader scores the hidden set.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | 1 |
| Agents | 2 extract + 2 fact-check + 2 build + 1 scan + 1 grader = 8 | 13: 2 extract, 2 fact-check, 2 build, 1 review, 1 fix, 1 scan, 2 eval runs, 2 graders (extra: review + fix after 17 findings; second eval round after 2/5) |
| Models / effort | Sonnet high ×6 incl. scan (J004-D2), Opus medium ×2 (tools); lead Opus | |

## Acceptance checks
- [ ] Every number, endpoint, quota and access term used in a skill or tool has a source and a fact-check verdict (confirmed / corrected / unverified-kept-as-OPINION / dropped). Dropped claims are listed with the reason.
- [ ] Every number in the skills, template and first report carries one provenance label: official, third-party sampled, third-party estimate, owner/developer statement, or derived (formula shown).
- [ ] No tool calls a source whose terms forbid automated access; each source in the tools has a row in a permission registry (route, purpose, auth, quota, storage limit, terms URL, date checked).
- [ ] No key, token or password in the repo: keys come from environment variables only; `git grep` for key patterns = 0 hits.
- [ ] Each script has offline tests (recorded responses, no network); `python tools/verify.py` → PASS.
- [ ] Growth math matches the paper's definitions: g7 on non-overlapping complete weeks, time-weighted means, coverage shown, gaps stay gaps; tests cover zero baseline, gaps, and overlap-vs-WoW.
- [ ] Report template has every section the owner asked for (rising games with numbers, rising loops, outside trends, top 3 opportunities with evidence) plus rights/policy flags and "what was wrong last week".
- [ ] Hand-off briefs to game-designer and marketing follow `rules/messages.md` §2 and match the game-designer's intake fields (`knowledge/reference/game-design/02-preproduction-docs.md` N0 intake).
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` PASS.
- [ ] Hidden test: the agent passes ≥ 4 of 5 rubric items on held-out cases (separate grader).
- [ ] Schedule plan written and shown to the owner; nothing scheduled without the owner's yes.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-20 | "All right, seems good. Just make sure that all the Sonnet models are actually used on high effort." |
| G2 first samples (L): first real scan + tool demo | 2026-10-21 | answered with decisions J004-D4..D10 (RoTrends, SullyGnome, on-demand only, no Roblox data) |
| G3 final look | 2026-10-21 | "Okay, actually, maybe we will use this, but like, legally, without getting me banned on any platforms or anything." (after first: "This is just going to be like a rough draft, but we probably won't use this agent because it just didn't work out. That's all right." |
