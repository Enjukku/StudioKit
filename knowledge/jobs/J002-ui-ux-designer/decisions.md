---
type: decision
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J002 decisions

| ID | date | decision | owner's words |
| --- | --- | --- | --- |
| J002-D1 | 2026-10-20 | G1 approved: six skill books (ui-design, ui-figma, ui-style-cartoon, ui-style-stud, ui-style-anime, ui-style-pixel), role, evals, first test | "Okay, yeah, you can plan the 6 skill books." |
| J002-D2 | 2026-10-20 | Extraction agents run Sonnet at high effort (brief raised from medium) | "have these Sonnet models be on high?" |
| J002-D3 | 2026-10-20 | The agent may build directly in the owner's Figma account through the Figma MCP | "the Figma can access use my Figma" |
| J002-D4 | 2026-10-20 | Add generating reference images and icons with ChatGPT to the agent's workflow | "something to also iterate into the workflow is generating reference images and icons with ChatGPT." |
| J002-D5 | 2026-10-20 | Defaults accepted (no objection): pixel style in Figma with pixel grid; first test = cartoon shop screen | (defaults from G1 digest; owner did not change them) |
| J002-D6 | 2026-10-20 | Load the Figma server skills (figma-use and its companions) and fold their rules into the ui-figma skill | "I also want you to run this command. So you properly understand all the Figma skills. So we have a stronger fundamentals of how to utilize the tool. figma-use" |
| J002-D7 | 2026-10-20 | The UI agent uses the shared VFX texture library (content/vfx/library/catalog.json) for glows, sunbursts, sparkles and other effects instead of drawing them | "If you look at the VFX agent, the agent has access to this large pool of assets that we have of various like elements. And it would be incredibly useful for your workflow." |
| J002-D8 | 2026-10-20 | Lead (engineering recommendation, owner may override): fit each screen's outer UIScale to the CoreUISafeInsets area, f = min(safe w / 1920, safe h / 1080); phone fit ≈ 0.294 | lead recommendation after G2 gap G-06; not an owner decision |
| J002-D9 | 2026-10-20 | Face gradients need a clearly visible step; shine bars cross the whole face (owner review of the G2 egg shop) | "How come we're not really doing gradients and then something else I'm noticing is sometimes you'll do these streaks of shine or whatever, but they don't fully go all the way down." |
| J002-D10 | 2026-10-20 | Second test: a different style (anime or pixel) using the VFX texture library | "I want to try again with a but this time pick a different style, like the anime or pixel art. And then I want you to also use the texture library to help you as well." |
| J002-D11 | 2026-10-21 | ChatGPT (owner's subscription through the Codex app) is the default image route for UI; Figma generate_image is the fallback; agents must know they can create images with ChatGPT | "why are we using Figma to generate images rather than ChatGPT? It's ChatGPT has a better image gen model." / "we should make sure that they know that they have access to creating images with ChatGPT." |
| J002-D12 | 2026-10-21 | Owner review of both tests: quality "B minus", some buttons "A"; a ChatGPT target reference image is required before styling; every UI/UX agent must know it has ChatGPT image generation and the VFX texture library | "the quality is just like alright ... it's usable, but it's not it's like a B. It's like a B minus. With some buttons being pretty good, like an A." / "I think with the reference photos, this can be improved." / "make sure that when ... new UI or UX models are opened or started, that they understand that they have access to ChatGPT for image generation as well as the flipbook or the texture book." |
| J002-D13 | 2026-10-21 | Keep the Codex route (`art_refs.py`) for ChatGPT images; no browser route and no API route. Codex does not name its image model (probably GPT Image 2.5; not verified) | "Okay, we'll keep using, doing it the way we're doing it then. It's probably GPT 2.5 image generate." |
