---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J009 step 2 hand-backs (T01-T03)
supersedes: []
held_out: true   # repeats held-out cases, keys, rubrics or answers (rules/knowledge.md §3)
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J009 lead notes: issues found in step 2 (for the skills and the G2 digest)

| # | From | Issue | Checked by the lead | Goes to |
| --- | --- | --- | --- | --- |
| N1 | T03 | Anchors work only for shape: `art_refs.py` tells the model to take silhouettes, proportions and details from anchors and not their shading, lighting or rendering. The paper wants anchors by purpose (shape, palette, light, material) | yes: `tools/art/art_refs.py:159-161` | G2 digest: optional `purpose` per anchor in the tool (out of J009 scope; owner decides). Skill: say that today look comes from the lock text, shape from anchors |
| N2 | T03 | Without a manifest `anchors` value, owner anchors are picked by a hash of the row id, not by relevance | yes: `tools/art/art_refs.py:124` | `art-review` skill: the art director always names anchors in the manifest |
| N3 | T03 | The newest approved generated anchor takes the last slot with no recorded reason | yes: `tools/art/art_refs.py:115,126` | `art-review`: name anchors explicitly; note in the review which anchors steered a batch |
| N4 | T03 | Image model name: kit says `gpt-image-2` via Codex; the paper names ChatGPT Images 2.5 (A01) | no | T08 fact-check |
| N5 | T01 | Paper rule 8 cites A06 (luminance definition) for "complementary diagnostics"; A06 does not back that advice | no (T01 report) | skill: keep rule 8 as OPINION, cite A06 only for the formula |
| N6 | T01 | Invented examples in the paper ("seaside repair town", "EXAMPLE-CAPTURE-17", "Lantern Workshop") | marked FICTIONAL by T01/T02 | skills: never cite as precedent |
| N7 | T02 | Art-bible template lacks slots for most of the paper's 12 fields (purpose, scope, approved example, failure example, test per lock) | to check against `templates/skill/art-bible.md` | template change (in scope), keep `art_refs.py` machine-read format |
| N8 | T04 | The paper's checklist routes failures straight to a role; the kit needs a ticket inside an approved brief (`rules/company.md` §3) | rule known | `art-review`: a failure becomes a ranked finding + a ticket in the job ledger, never a direct order |
| N9 | T04 | `reference-images` I-06 (an image is never the final asset) vs marketing key art, which may ship as an image | to decide | G2 digest: key art / thumbnails may be final images (marketing route); I-06 stays for game assets |
| N10 | T04 | No lock or family for the experience icon and thumbnails (ICON LOCK is for 48 px in-game icons) | `templates/skill/art-bible.md` families table | template: propose `key-art` / `store-icon` family rows for marketing (owner approves) |
| N11 | T04 | New art-bible fields (permitted variation, exceptions, revision id, transition packet) must stay outside the machine-read lock blocks | format: `art_refs.py` docstring | template change + run `tools/tests/test_art_refs.py` |
| N12 | lead | Hidden eval cases must stay out of the skills: Resistance Illaoi (R08/R19, notes 02:RD5-RD6), Hearthstone effects (C08/C09, notes 01:SC-HS), first-game collectibles read as rubble (05:OR24; D-053/D-054/D-056/F-015). Drafts cited all three; removed 2026-10-21 | grep of `.agents/skills/art-*` = 0 hits after the edit | `precedents.md` must exclude them too; the grader gets them in `evals-hidden.md` |
| N13 | lead | `preproduction/references/handoffs.md` brief to the art director names `skills: [reference-images, vfx-design, ui-design]` "until an art skill exists" | yes: handoffs.md (J003 file) | follow-up for J003 owner: point it at `art-direction`, `art-review` (not edited here; J003 is in its own G2) |
| N14 | lead | New role files are not registered as agent types until a new session starts; T09/T10 ran as general-purpose + the role file + the same skills | Agent tool error 2026-10-21 | note in G2; next session uses `subagent_type: art-director` |
| N15 | T08 | The tool record (`art_refs.py` .json) has no model/surface field; the image model version is not exposed by Codex | FI06 | follow-up: add `model: not exposed` to the record (tool change, owner digest) |
| N16 | T10 | Skill gaps from the hidden-eval run: (1) briefs table named modeler/animator as if they exist → marked planned, lead routes; (2) clarity parity was one-sided → two-sided in art-direction C-06; (3) no "choosing" task row (emphasis read as advice) → added to clarity-cohesion §1; (6) no screen-share measure → silhouette area_frac on an effect mask, look-check §3; (7) role hand-back vs brief write scope → brief wins, lesson in hand-back | fixed 2026-10-21 | H2 is now partly taught (row added after the run): the hidden set is spent; a new hidden set is needed for later regrades |
| N17 | T10 | vfx-design gaps (not this job's files): no context for a persistent state effect (onset then quiet); no recipe for an uncollected pickup lying among debris | not fixed | follow-up for the vfx-designer skill owner |
| N18 | T09 | 12 skill gaps from the blind UI review: grades vs "no score" (1), no-bible standard order (2, 10), what counts as an acceptance condition (3), UI capture fields (4), UI masks and sampled contrast (5, tool), ring neighbors and "brightest control" (6), UI checklist rows K16-K18 + split with ui-design review (7), UI layers (8), fit factor (9), role vs brief write scope (11, fixed in N16), naming and cross-job ticket ids (12) | fixed 2026-10-21 in art-review SKILL.md, feedback-briefs.md, look-check.md; tool part → T12 | — |
| N19 | owner | J009-D9 makes N15 (model field in the image record) unnecessary; skill text now says "newest model" | 2026-10-21 | closed |
| N20 | owner | N1 resolved by J009-D11: anchors now guide the whole look; tool note and skills changed | 2026-10-21 | closed |
