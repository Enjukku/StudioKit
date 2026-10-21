---
type: index
scope: universal
status: active
updated: 2026-10-20
source: J002
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# UI reference: owner material for the UI/UX designer (J002)

Raw transcripts and the research paper stay outside git (owner's Downloads folder). These notes are paraphrased extractions; skills cite them by id.

| Id | Source (owner-supplied 2026-10-20) | Tool in video | Trust | Notes |
| --- | --- | --- | --- | --- |
| TC | "Cartoon Guide" (UI Genesis, Hamuri), pet inventory | Figma | practice, one tutor, values by eye; strong Figma teaching | [[reference/ui/01a-cartoon-recipes]], [[reference/ui/01b-cartoon-techniques]] |
| TS | "Stud Guide" (UI Genesis, Hamudi/Hamuri), shop + HUD | Figma | practice, one tutor; most exact values of the four | [[reference/ui/02a-stud-recipes]], [[reference/ui/02b-stud-techniques]] |
| TA | "Anime Guide" (UI Genesis, Kek), TD unit inventory | Photoshop | practice, experimental, few values, file lost mid-video | [[reference/ui/03-anime-photoshop]] |
| TP | "PixleArt Guide" (Kakuza), rogue-like HUD | Photoshop | practice, narrated to ~1:02:35 only | [[reference/ui/04-pixel-photoshop]] |
| RP | "Game UI and UX Research for an AI Designer" (ChatGPT, dated 2026-10-21) | n/a | AI-written synthesis; keeps VERIFIED / EXPERIENCE / OPINION / UNSPECIFIED tags and a dated source register | [[reference/ui/05a-research-rules]], [[reference/ui/05b-research-templates]], [[reference/ui/06a-research-motion-a11y]], [[reference/ui/06b-research-process-sources]] |

Contradictions found while building the skills:
| Topic | Conflict | Resolution in the skills |
| --- | --- | --- |
| Pixel UI in Figma | TP says pixel UI is not made in Figma (no pencil) | Owner chose Figma (J002-D5). `ui-style-pixel` builds on the pixel grid with 1 px rects and allows a PNG import for freehand ornaments |
| Blend modes | All four videos rely on overlay / soft light / dodge | Roblox UI composites Normal only (TP@16:28): bake or approximate (`ui-figma/references/roblox-handoff.md`) |
| UIStroke Inner/Outer | ui-basics facts: live; class page: some properties need the Improved UIStrokes beta | Confirm in Studio; fallback nested Frame |
| Stud header blend | TS sets Overlay (11:04) then says "normal for now" (12:15) | Stud book: Overlay in Figma, baked or low-opacity Normal tile in Roblox |
| Motion timings | RP: almost all UNSPECIFIED; ui-basics ui-effects has practice timings | `ui-design`: motion records keep UNSPECIFIED fields as PROPOSAL values to tune, with provenance |
