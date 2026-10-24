---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J027
supersedes: []
---
> Author: orchestrator (side session) · claude-opus-5-5 · default · 2026-10-24

# Job card: J027 the lead routes work to the right specialist

Owner words (verbatim): "sometimes the orchestrator is not deploying the agents when it should. Given a task, working on UI, it won't call upon the UI agent unless I tell it to do so." Then: "The lead needs to be able to recognize when it makes sense to call upon an agent for a given task. And to automatically do so." Then: "I feel like you didn't fully try to grasp how our workflow works before you suggested a plan of improvement."

| Key | Value |
| --- | --- |
| Problem | In real game builds, craft work (UI, VFX, sound, lighting, review) starts only when the owner complains. A routed UI agent also cannot reach Figma |
| Constraints | Keep the J024 run cut; add a run only where the lead did craft work itself. Owner sets role tool lists and settings: propose, never edit them. Other chats' uncommitted files (J025, J026) stay untouched. Session < 500k context |
| Target experience | Trust: the owner names a goal and the right specialists start on their own, at the right time |
| Type, size | Kit change (no game recipe), M by effort; the owner picked fixes from the proposal, so no G1. G3 = the owner reads the result |
| Success test | Gate PASS (or only other chats' failures); a ui-ux-designer started after a sync lists Figma tools; on the next game build the game has a roadmap with every needed craft area as a row under a milestone before the first build session, and every job card names its milestone, and UI, VFX and sound rows start without an owner prompt |
| Evidence | Side-session notes `routing-proposal-v2.md` and `routing-study-A-kit.md`, `-B-owner.md`, `-C-practice.md` (folder `C:\Users\Firew\AppData\Roaming\Claude\side-session-notes\local_1595ace9-36b0-452c-a928-f5fa79a86f0a\`) |
| Linked | J026-context-structure: its F5 (role sessions with their books) is built here as J027 F4 |
