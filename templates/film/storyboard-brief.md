<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J015). Kit template: one brief per storyboard panel. Fields from the owner's research paper (N3 SB-01..15, OPINION, 2026-10-21). The `identity` line goes into the reference-images manifest (family `storyboard`); everything else stays in this file, next to the image, as the authority where the image is ambiguous. Copy to `content/film/<sequence>/boards/<shot-id>.brief.md`. -->
# Storyboard brief: <sequence> shot <id> rev <n>

| Field | Fill in |
| --- | --- |
| Project and revision | <game>, <sequence>, shot <id>, shot-list revision <n>, panel revision <n> |
| Approved visual references | <`inputs`: approved character / environment / prop images (attach them; name each by order: "image 1 is ..."), the previous approved panel>. Reference ≠ exact geometry |
| Story purpose | <the new information this panel must communicate> |
| Character intention | <what the character wants and what visibly changes> |
| Composition | <subject, foreground / background relationship, silhouette, negative space; who is left / middle / right> |
| Shot size and angle | <qualitative framing only (wide, close, low, eye level); no invented lens> |
| Continuity constraints | <screen direction, eyeline target, prop hand, costume state, landmark sides, light direction: copied from the continuity ledger> |
| Action moment | <the exact instant shown; key pose, not the motion path> |
| Camera change | <the planned move in words; a separate start and end panel if the move matters> |
| Lighting and colour | <the sequence's colour relationship and the brightest area; no universal mood labels> |
| UI and crop | <16:9 crop, protected areas (subtitles, skip), checked again in runtime> |
| Exclusions | <what would contradict geography, timing or the approved style> |
| Acceptance test | <what must be identifiable for the panel to pass, e.g. "the exit arch is on the right and readable at thumbnail size"> |
| Unresolved | <lens, distance, timing and anything Blender or runtime must measure> |

## Manifest row (`reference-images`, family `storyboard`)
`<sequence>-<shot-id lowercase>-r<n>,storyboard,"<identity: Storyboard panel, shot <id> of <N>: size, angle; image 1 is ...; positions; action moment; landmarks; light side; no ...>",<inputs>,<anchors>`

## Review (fill after generation; `film-craft` §3 step 3)
| Check | Pass / fail and note |
| --- | --- |
| Story purpose readable | |
| Identity matches the approved references | |
| Screen direction and eyeline match the ledger | |
| Prop hand, costume, landmarks, light direction match | |
| Prop state (lit / dark, open / shut) and contact (touching / not) match the moment | |
| Subject and acceptance test readable at small size | |
| Continuity with the previous and next panels | |
| Decision | accept / regenerate (max 2) / revise the plan openly |
