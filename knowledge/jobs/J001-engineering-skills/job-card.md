---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J001 — Rebuild the engineering skills for the kit

| Field | Value |
| --- | --- |
| Size | L (many skills; research; owner reviews each) |
| Job owner | lead (orchestrator) |
| Status | G1 approved 2026-10-20. Step 0 done 2026-10-20 (mirror `7400643` in the kit; `knowledge/reference/roblox/whats-new.md`). Step 1 done 2026-10-20 (skill `studio-mcp`, owner approved). Step 2 done 2026-10-20 (skill `platform-policy`, owner approved). Step 3 done 2026-10-20 (skill `data-saving`, owner approved). Step 4 done 2026-10-20 (skill `performance`, owner approved). Step 5 done 2026-10-20 (skill `networking-security`, owner approved). Order change: steps 6-7 wait for the owner's ChatGPT research papers (architecture, testing, updates, performance targets, exploits); step 8 next |
| Kit | `C:\Users\Firew\Downloads\uterd\StudioKit` (0.3.0) · audit source: DestructionSimulator skills/rules (read-only) |

## Owner's words (2026-10-20, verbatim excerpts)
- "using both the Roblox docs as well as maybe web research ... Roblox documentation as the main thing ... modern web research as well, specifically for the Roblox platform ... information needs to be recent, like within 2026."
- "I don't want us to utilize information that might misguide us ... if they are from the actual Roblox team, then their information might be valuable, or if they're like a lead dev ... The Roblox documentation is definitely reliable."
- "before we do this, we should update the Roblox studio information ... upgrading UI shadow capabilities ... in studio beta ... I would just have us update the Roblox documentation before we begin."
- Architecture / code review / Luau: "research what strong game architecture looks like, how to build a strong foundational system so that when you are building games, it's easy to add new content and everything is like properly modular."
- UI: "add the new Roblox UI features ... I'm going to feed strong information to the UI agent ... for now, we can just do the basics."
- Anti-over-engineering: "a big problem with AI in the modern day ... use mostly things from the Claude team ... look at popular GitHubs ... one called like Ponytail or something ... for Luau, specifically for the Roblox platform ... stronger code bases that are more future-proof while not being over-engineered."
- Also improve: analytics, security, package list (kit gets a short "choosing packages" rule; game pins stay in games).

## Source rules (binding for this job)
| Rank | Source | Use |
| --- | --- | --- |
| 1 | Roblox Creator Docs (local mirror, refreshed first) | engine truth |
| 2 | Official Roblox posts (DevForum announcements / release notes by Roblox staff), 2026 only | new features, policy |
| 3 | Claude / Anthropic team (engineering posts, docs) | anti-over-engineering, agent coding practice |
| 4 | Recognised lead developers and widely used open-source Luau projects (GitHub), 2026 activity | architecture patterns, with stated reasons |
| ✗ | Unattributed forum opinions, SEO blogs, anything before 2026 | not used as evidence |
Every fact in a skill cites its source and date.

## Steps and order
0. **Refresh the local Roblox docs mirror** (and its "what's new" note: include Studio beta items such as new UI shadow features, marked beta).
1. Studio MCP workflow + rule (current tool inventory; "files are the source, MCP verifies" as an option, not a universal ban).
2. Platform policy (paid random items, all categories, odds updates; ads; age checks; regions) — re-verify on create.roblox.com.
3. Data saving: generic persistence (schema, migration, session lock, failure handling, request budgets, batching); any wrapper is one adapter.
4. Performance: MicroProfiler, scene analysis, device/network simulators, streaming features; game-specific physics stays in games.
5. Networking and security (remotes-security is the best base).
6. Architecture + code review + Luau: research strong modular game foundations (easy to add content); modern Luau (task, strict types, new solver, Parallel/Actors, buffer, native).
7. Anti-over-engineering (Claude team first; popular GitHub projects are input only. Owner 2026-10-20: the "Ponytail" repo is not important; "we could just design the stuff ourselves").
8. UI basics + new Roblox UI features (deep UI agent later from owner material); keep the UI effects page.
9. Analytics, security rule cleanup, "choosing packages" rule.
Each skill: design via `/build-agent` steps 2-5 where it applies (notes → skill → evals); owner sees each before it lands (G3 per skill).

## Budget and models
Research and extraction: Sonnet medium (cheap, parallel by source). Skill writing and architecture judgment: Opus medium. Scripts/tools: Opus medium minimum. Lead: no mechanical work.

## Decision log
| Date | Gate | Owner's words |
| --- | --- | --- |
| 2026-10-20 | G1 | (approved scope and source rules in chat; see "Owner's words") |
| 2026-10-20 | G3 step 5 | "And yes, I approve of it for now. You can begin working on the next section" |
| 2026-10-20 | G3 step 4 | "Approved. Commit the performance skill and start J001 step 5: networking and security." |
| 2026-10-20 | G3 step 3 | "Approved. Commit the data saving skill and start J001 step 4: performance." |
| 2026-10-20 | G3 step 2 | "Approved. Commit the platform policy skill and start J001 step 3: data saving." |
| 2026-10-20 | G3 step 1 | "Approved. Commit the Studio MCP skill and start J001 step 2: platform policy." |
