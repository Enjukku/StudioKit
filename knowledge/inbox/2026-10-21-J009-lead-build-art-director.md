---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J009
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Lessons: building the art-director agent (J009)

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | The agent's blind grades were two steps kinder than the owner's (egg shop B- vs C-, anime B+ vs B-). Its diagnoses and measurements were right; it led with measured passes and called finish flaws "owner taste" | A reviewing agent needs a grade scale anchored on owner-graded examples, and "finish is a finding" stated as a rule; measured passes are a floor, never a reason to raise a grade | J009-D6 (owner: "the eggshop is more like a C minus while the anime one was like a B minus"); `knowledge/jobs/J009-art-director/grades-g2.md` |
| 2 | Owner-graded work used as a blind test becomes calibration afterwards and cannot test the fix | Keep a fresh, owner-graded screen or scene back for each re-test; record which examples are spent | lead-notes N12, N16 |
| 3 | Drafted skills cited the cases planned as the hidden test set | Write the hidden set first and grep the skills for its case names before any eval run | lead-notes N12 |
| 4 | The measuring tool failed silently on the kit's own grey-background references and then on flat UI screens | Run every new image tool on a real kit image (not only synthetic tests) before the agent uses it; "invalid" must be a verdict, never a quiet number | T06 pushes 1-2, T12 |
| 5 | Fact-checks changed several studio claims (Deadlock parry cooldown, "fade away" not "muffled", Teemo colors, a dropped Fortiche clause) and found SLIM still a Client Beta | Fact-check studio precedents and dated platform facts before skills cite them; label who said each thing | `fact-check-studios.md`, `fact-check-a11y-ai-roblox.md` |
| 6 | A new role file is not an agent type until a new session starts | In the same session, run the new role as a general agent told to read the role file and load its skills | lead-notes N14 |
| 7 | Two chats picked the same job number (J008) at the same time | Check `knowledge/jobs/` immediately before creating a job folder, and again before the first gate | J008 / J009 rename, 2026-10-21 |
| 8 | Both "different" directions were one family, and a long fixed layout made 8 styles look alike | Explore across style families; for look images keep the subject short and put effort into a rich style paragraph; exact counts and positions only for working references | J009-D13, D14; `art/style-probe/probe-results.md` |
| 9 | One shared colour line ("washes the scene in warm orange") overrode four styles' palettes; separate sessions still chose one default layout | In style sets keep colour and light out of the shared text; give each style its own framing line | J009-T14 `style-test-2/prompts.md` |
| 10 | The same scene through ChatGPT web (GPT-6 chat, newest image model) was clearly better than through Codex, in the owner's words | Default image route is ChatGPT in the built-in browser, owner signed in; one new normal chat per image (temporary chats cannot make images); one download approval per batch; archive chats and close tabs after every batch | J009-D16, D17, D18; `art/style-test-3/` |
