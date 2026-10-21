---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J005-T08
supersedes: []
---
> Author: fact-checker · claude-sonnet-5-5 · high · 2026-10-21

Scope: every Tripo claim and every other rig-tool claim in the rigger paper (RP, `Roblox_Character_Rigger_Research.txt`) that a rig skill could turn into a rule. These are the claims-table rows of kind `tripo` and `other-tool` in `01-rig-quality-runtime-tripo.md` (C31-C56) and `02-weights-controls-export-tests.md` (CL54-CL68), plus the questions X07, X08 and the limits LM04, LM05, X15, X17. Roblox facts are in `fact-check-roblox.md`; Blender API facts are J005-T07; AI motion tools are out of scope.

How I checked. Read date for every row is 2026-10-21 (today), from the live vendor page. Tripo docs: I fetched the raw HTML of each page and read the stripped text (no summary model in the path for the numbers and ids below). I also grepped every Tripo page I read for "roblox" and "R15": zero hits. Tripo pages carry no publication date; only the model ids carry dates, and the changelog headings give a month. Pages where I could not read the vendor page directly are marked in the row. I called no Tripo API and made no account.

Verdicts: confirmed (source matches the paper), corrected (source gives a different value or a different page), partly (matches with a limit, or only part could be checked), unverified (not found or not reachable; I say what I tried), contradicted (source says the opposite). A vendor page that says "better" or "recommended" proves only what the vendor states, never output quality.

Short names for pages (each row still prints the full URL):
- RIG = `https://developers.tripo3d.ai/en/docs/animations-rig` (Auto Rigging)
- CHK = `https://developers.tripo3d.ai/en/docs/animations-rig-check`
- SEG = `https://developers.tripo3d.ai/en/docs/mesh-segment`
- SS = `https://developers.tripo3d.ai/en/docs/mesh-smartsegment`
- DEC = `https://developers.tripo3d.ai/en/docs/mesh-decimate` (Retopology)
- UV = `https://developers.tripo3d.ai/en/docs/mesh-uv` (Smart UV)
- CL = `https://developers.tripo3d.ai/en/docs/changelog`
- MV = `https://developers.tripo3d.ai/en/docs/models-and-versions`
- RM = `https://developers.tripo3d.com/en/models/rig` (Tripo Rigging model page, `.com` host)

## Settled items (a)-(k) from the ticket

| item | answer | verdict | rows |
| --- | --- | --- | --- |
| (a) rig id behind "v3.0-20260909"; API default | The id `v3.0-20260909` is a value of the `model` field of `POST /v3/animations/rig`. It is stated on RIG, on CL (entry "Rigging v3.0 and retargeting upgrade (2026-10)") and on RM. The default is `v1.0-20240301`, stated on RIG and RM. | confirmed | RT01, RT03, RT04 |
| (b) rig default vs "default is still v2.0" | The rig default `v1.0-20240301` is printed on RIG (and RM). CL's rigging entry says only that the default model is unchanged. The sentence "The default is still v2.0, so existing requests behave the same" sits in CL's Retopology entry and refers to the `model` field of `POST /v3/mesh/decimate`. DEC shows `v2.0` as the retopology default. | confirmed | RT03, RT05 |
| (c) segmentation ids and options | Default `v1.0-20250506` (geometry-based). `v2.0-20260430` is Beta (semantic labels). Field names: `model`, `segmentation_granularity` (`simple`/`balanced`/`detailed`, default `balanced`), `split_by_connectivity` (default `true`), `ref_image`. All three of the last are v2 only. When `ref_image` is given, the granularity and connectivity fields are ignored. | confirmed | RT13-RT16 |
| (d) 150 MB ceiling | Printed on RIG, CHK, SEG and DEC. Not printed on SS or UV. The File Upload page (`https://developers.tripo3d.ai/en/docs/files`) caps model uploads at 150 MB too. So "150 MB per documented endpoint" is right and must not be read as "all endpoints". | confirmed | RT10, RT17, RT21 |
| (e) Smart Segmentation | `POST /v3/mesh/smartsegment`; "includes auto modeling". Fields: `seg_type` (`image` or `model`), `input`, `granularity` (`coarse`/`medium`/`fine`, default `medium`), `hint`, `transform`. `seg_type=model` needs a GLB and `transform`, a column-major 4x4 matrix of 16 floats. | confirmed | RT18-RT20 |
| (f) rig-check output | `POST /v3/animations/rig-check`. Output fields `riggable` (boolean) and `rig_type` (string). The listed `rig_type` values are the seven named topologies; `others` is not among them. Free (0 credits in the example). | confirmed | RT12 |
| (g) topology categories and formats | `rig_type`: biped (default), quadruped, hexapod, octopod, avian, serpentine, aquatic, others (`others` only with v3.0). `out_format`: `glb` (default) or `fbx`. Input: GLB, FBX, OBJ, STL. | confirmed | RT08, RT09 |
| (h) naming presets | `spec` takes `tripo` (default), `mixamo`, `actorcore`, `unity`, `unreal`, `vrm`. It works only with `rig_type=biped`. v3.0 adds `actorcore`, `unity`, `unreal`, `vrm`. There is no Roblox or R15 preset. | confirmed | RT11 |
| (i) retopology | `POST /v3/mesh/decimate`, `face_limit` 500-20,000 (triangles) and 500-10,000 (quads) on v3.0. v2.0 has the same ranges. v3.0 must be requested with `model=v3.0`; the default is `v2.0`. | confirmed | RT23, RT24 |
| (j) Smart UV 80,000 | The ceiling is on the Smart UV page (`POST /v3/mesh/uv`) and in CL. It is not on DEC, the Retopology page the paper names as T6. | confirmed (number); corrected (page) | RT25, RT26 |
| (k) input polygon cap | None is stated on RIG, CHK, SEG, SS, files, models pages. A third-party Tripo reseller help page reports "no hard cap" but a soft guide of under 300k polygons for rigging. Studio web UI limits: not found. | partly | RT28 |

## Claims table

| id | claim | paper and line | paper's source ID | checked against (read 2026-10-21) | what the source says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RT01 | Tripo rig model id `v3.0-20260909` exists and is selectable on the auto-rig call. | RP:26, 221, 258, 551 (C42, C43; N19) | T1, T5 | RIG; CL; RM | RIG lists `model` values `v1.0-20240301`, `v2.5-20260210`, `v3.0-20260909`. CL says `POST /v3/animations/rig` accepts `model=v3.0-20260909`. RM names the same three ids. | confirmed | The id carries 2026-09-09; the changelog heading gives only "2026-10". No page gives a release day. |
| RT02 | Tripo recommends v3.0 for humanoids; it is faster and higher quality for humanoids; other rig types keep v2.5 quality and speed. | RP:221, 551 (C42) | T1, T5 | RIG; CL; RM | RIG: v3.0 is recommended for humanoid characters, faster and higher quality; other types keep v2.5 quality and speed. CL and RM repeat it. | confirmed | Vendor claim only (rule X17). No page gives a benchmark, a metric or a sample. The paper already marks this as a vendor claim. |
| RT03 | The rig API default is `v1.0-20240301`. | RP:221, 258 (C43; N20) | T1 | RIG; RM | RIG: `model` optional, default `v1.0-20240301`, "biped (humanoid) only", 90+ animation presets. RM: "default", biped only. | confirmed | The paper does not say that the default is biped-only. It matters: a request with no `model` field goes to the oldest model. What the API does when you ask that default for a non-biped `rig_type` is not stated. |
| RT04 | v3.0 must be requested explicitly; it is not the API default. | RP:26, 221, 258, 568 (C43; rule 11; D09) | T1, T5 | RIG; CL; RM | RIG and CL both say the default model is unchanged and v3.0 must be requested explicitly. RM says it must be set explicitly. | confirmed | RIG, CL and RM carry it. The paper's T1 key line matches RIG word for word in meaning. |
| RT05 | The T5 quoted sentence "default is still v2.0" is about retopology, not rigging. The rig default comes from T1. | RP:801, 258 (X07, LM05, CL64) | T5, T1 | CL; DEC | CL, entry "Retopology v3.0 and Smart UV (2026-10)": the default is still `v2.0`, and the same entry names `POST /v3/mesh/decimate` and `model=v3.0`. DEC: `model` default `v2.0`. CL's rigging entry does not print the id `v1.0-20240301`. | confirmed | Answers X07. Cite RIG for the rig default id, CL for the upgrade notice, DEC for the retopology default. |
| RT06 | The changelog entries are headed 2026-10 and 2026-09 with no exact day. | RP:798 (CL64; N19) | T5 | CL | Headings are month only: "Rigging v3.0 and retargeting upgrade (2026-10)", "Retopology v3.0 and Smart UV (2026-10)", then 2026-09 entries (texture v3.5-20260815, chat_image 2.5), 2026-08, 2026-04. | confirmed | The v3.0 rig id carries 20260909 while its entry is headed 2026-10. Do not turn the id date into a release date. |
| RT07 | Rig model `v2.5-20260210` supports non-humanoid creatures. | RP:221 (C41; N18) | T1 | RIG; RM | RIG: for non-humanoid creatures (quadruped, hexapod, octopod, serpentine, aquatic, avian); bipeds also work but are not recommended, "use v3.0 for humanoids". | confirmed | `others` is not available on v2.5 (RT08). |
| RT08 | Auto Rigging categories: biped, quadruped, hexapod, octopod, avian, serpentine, aquatic, others. | RP:221 (C40) | T1 | RIG; RM | RIG `rig_type` values are exactly those eight; default `biped`; "Recommend calling `rig-check` first". Per RIG and RM, `others` needs v3.0. | confirmed | The paper does not say `others` is v3.0-only. Rig-check returns only the first seven (RT12). |
| RT09 | Auto Rigging outputs GLB or FBX. | RP:221 (C40) | T1 | RIG; RM | `out_format`: `glb` (default, binary glTF) or `fbx`. | confirmed | Input formats are GLB, FBX, OBJ, STL. GLTF is no longer listed for rig input (CL). The paper does not mention input formats. |
| RT10 | Auto-rig input file ceiling is 150 MB. | RP:221, 257 (C44; N14) | T1 | RIG | `input`: max file size 150 MB. | confirmed | A byte limit. It is not a polygon limit (RT28). |
| RT11 | The v3.0 rig naming presets include no Roblox/R15 preset; Mixamo, Unity and Unreal naming exist. | RP:223 (C47; T06; CL63) | T1 | RIG; CL; RM | `spec` values: `tripo` (default), `mixamo`, `actorcore`, `unity`, `unreal`, `vrm`. Only used when `rig_type` is `biped`. RM and CL: v3.0 adds `actorcore`, `unity`, `unreal`, `vrm`. No page I read mentions Roblox or R15 (grep, 14 pages). | confirmed | The paper tagged it OPINION; the facts under it hold. The paper's list is incomplete (also `actorcore`, `vrm`, `tripo`). The preset only renames bones for biped rigs; a non-biped rig gets no preset. Absence of a Roblox preset is "not on these pages as of 2026-10-21". |
| RT12 | Rig-check tells whether the model can be rigged and recommends a rig type; it is not a Studio quality check. | RP:221, 511, 553 (C39; T03; CL59) | T3 | CHK | `POST /v3/animations/rig-check`. Output `riggable` (boolean) and `rig_type` (string: biped, quadruped, hexapod, octopod, avian, serpentine, aquatic). Input GLB, FBX, OBJ, STL, 150 MB. Example cost 0 credits. | confirmed | The "not a quality validator" half is the paper's reading; the page gives only these two fields. No `rig_type` value is documented for `riggable: false`. Rig-check had accepted GLB only before 2026-10 (CL). |
| RT13 | Segmentation endpoint is `POST /v3/mesh/segment`. | RP:215 (C31) | T2 | SEG; CL | SEG: Base URL `https://openapi.tripo3d.ai/v3`, path `POST /mesh/segment`. CL maps v2 `mesh_segmentation` to it. | confirmed | |
| RT14 | Segmentation default model is `v1.0-20250506`; `v2.0-20260430` Beta adds semantic labeling. | RP:215, 255 (C32; CL60; N15, N16) | T2 | SEG | `model` default `v1.0-20250506` (geometry-based). `v2.0-20260430` marked Beta, "semantic segmentation with labeling". | confirmed | A Beta can change. Pin the id in every request. |
| RT15 | v2 supports granularity simple/balanced/detailed and connectivity splitting. | RP:215 (C33; T01) | T2 | SEG | `segmentation_granularity`: `simple`, `balanced` (default), `detailed`; v2 only. `split_by_connectivity`: boolean, default `true`, v2 only. | confirmed | Parameter names are exact as printed. |
| RT16 | Giving `ref_image` overrides the granularity and connectivity options. | RP:215 (C34) | T2 | SEG | `ref_image` (v2 only, `file_token` or public URL): when given, `segmentation_granularity` and `split_by_connectivity` are ignored. The page shows a colour-coded mask as the reference image. | confirmed | |
| RT17 | Segmentation input ceiling is 150 MB. | RP:215, 257 (C35; N13) | T2, T1 | SEG | `input`: GLB, GLTF, FBX, OBJ, STL; max 150 MB. No face or polygon limit printed. | confirmed | |
| RT18 | Smart Segmentation is `POST /v3/mesh/smartsegment`, a separate pipeline that includes modeling. | RP:25, 217 (C36; CL61) | T4 | SS | `POST /mesh/smartsegment`, "End-to-end smart segmentation pipeline". SmartSegment includes auto modeling; `/v3/mesh/segment` only segments an existing model. | confirmed | The only task result shown is the image pipeline (`seg_type=image`, outputs `mask_url`, `seg_model_url`, `model_task_id`). The page does not show what the modeling step changes when `seg_type=model`. So "it regenerates your geometry" is likely but not shown. |
| RT19 | SmartSegment model input must be GLB and include a column-major 4x4 transform of 16 floats. | RP:217, 256 (C37; N17) | T4 | SS | `seg_type=model`: "GLB only; `transform` required". `transform`: number array, column-major 4x4 matrix, 16 floats; identity example given. | confirmed | The page does not say what space the matrix is in or what it does. Do not describe its meaning in a skill. |
| RT20 | SmartSegment supports text hints and coarse/medium/fine granularity. | RP:217 (C38) | T4 | SS | `hint` (optional text); `granularity` `coarse`, `medium` (default), `fine`. | confirmed | `seg_type=image` also exists (PNG, JPEG, WebP); the paper omits it. |
| RT21 | "150 MB per documented endpoint": the ceiling is stated for rig and segment. | RP:257 (N13, N14; CL62) | T1, T2 | RIG; CHK; SEG; DEC; SS; UV; `https://developers.tripo3d.ai/en/docs/files` | 150 MB printed on RIG, CHK, SEG, DEC. SS prints no size limit. UV prints no size limit (it has the 80,000 triangle limit). The upload page: models max 150 MB multipart; for files over 60 MB the docs suggest the large-file upload. | confirmed | Read the paper's phrase literally. A skill must not say "150 MB for every Tripo call". |
| RT22 | Tripo segmentation and Tripo rigging are different operations. | RP:25 (C49; rule 10) | T1, T2, T4 | RIG; SEG; SS | Different endpoints (`/animations/rig`, `/mesh/segment`, `/mesh/smartsegment`) and different model ids. RIG's `input` `task_id` is described as coming from a `text_to_model`, `image_to_model` or `multiview_to_model` task. | confirmed | Not stated on the page, but follows from the task_id text: feed a segmented or hand-fixed model to rigging by URL or `file_token`, not by the segmentation task id. I did not test this. |
| RT23 | Retopology v3.0 `face_limit` is 500-20,000 for triangle output and 500-10,000 for quad output. | RP:225, 259 (C45; N21, N22) | T5, T6 | DEC; CL | DEC and CL print these ranges for v3.0 (optional; omit for adaptive). Endpoint `POST /v3/mesh/decimate`; `quad` boolean default `false`. | confirmed | v2.0 has the same ranges on DEC. v1.0 differs (required; up to 2,000,000 triangles, 150,000 quads). The range is the target polycount of the output; it is not a Roblox budget. |
| RT24 | Retopology v3.0 must be requested explicitly; the default stays v2.0. | RP:225 (C45; N23) | T5 | DEC; CL | `model` default `v2.0`; `v3.0` is an accepted value ("newest retopology", optional `smart_uv`). CL: default is still `v2.0`. | confirmed | |
| RT25 | Smart UV input ceiling is 80,000 equivalent triangles. | RP:225 (C46; N24) | T5, T6 | UV; CL | UV: input must not exceed 80,000 equivalent triangles (a quad counts as two). Larger models are accepted at creation, but the task fails and credits are refunded. CL says the same. | confirmed | Number is right. The real page is `POST /v3/mesh/uv`. |
| RT26 | The Smart UV ceiling is documented on T6 (the Retopology page). | RP:225, 803-806 (X08) | T6 | DEC; UV; CL | DEC does not state 80,000. The limit is on UV and in CL (T5). `smart_uv` on DEC is a different thing: UV unwrap inside v3.0 retopology, no stated limit. | corrected | Answers X08. Cite UV and CL, not DEC. |
| RT27 | Retopology face ranges, the Smart UV limit and byte limits belong to their own operations and are not rigging limits or Roblox budgets. | RP:225, 806 (CL65; 4d-e) | T5, T6 | DEC; UV; RIG | Each limit is printed under its own endpoint. Nothing links them to rigging. | confirmed | The "not Roblox budgets" half is the paper's rule; no Tripo page mentions Roblox. |
| RT28 | No general input-polygon cap is documented for Tripo rigging or plain segmentation; Studio web UI limits may differ from the API. | RP:227, 260 (C48; 4d-e; N25; X02) | T1-T3 | RIG; CHK; SEG; SS; `https://developers.tripo3d.ai/en/docs/files`; third party: `https://help.scenario.com/articles/4692888910-tripo-family-the-complete-guide` | The Tripo pages print only a 150 MB file limit; no face, triangle or vertex cap on rig, rig-check, segment or smart-segment. The Scenario help page (a Tripo reseller; no absolute date, "last updated 7 days ago") says Tripo engineering told them there is no hard cap, but that dense meshes take longer and often fail with a "model too complex" error, and advises under 300k polygons for rigging (v1 and v2.5). | partly | API half confirmed as an absence. Studio UI half: I found no Tripo page on UI limits (unverified). The 300k figure is a reseller's advice, not Tripo docs. Do not put it in a skill as a limit; "keep dense meshes low and run retopology first" is safe as advice. |
| RT29 | Tripo carries four unrelated version numbers: API v3, geometry model, segmentation model, rigging model. | RP:223 (4d-c) | none | MV; CL; DEC; UV | There are more: geometry model (default `v3.1-20260211`; also `P1-20260311`, `P2-20260801`), segmentation model, rigging model, retopology model (`v1.0`/`v2.0`/`v3.0`), texture model (`v3.5-20260815`, default `v3.0-20250812`), Smart UV `model` (`default` only), and the API version `/v3`. | partly | The paper's four are right and each must be written down; the list is not complete. Retopology and texture also have their own ids. |
| RT30 | Mixamo FAQ: auto rigging is for bipedal humanoids only. | RP:237, 262 (C50; CL66; 4e-a) | A1 | `https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html` (HTTP 403 to my fetches, also `/au/`, `/ca/`, `/en/`); search-tool extract of the same page, same day | I could not open the page. A search-engine extract of the page text says the auto-rigger and the animation libraries are for bipedal humanoids only. | partly | Read secondhand through the search tool. Treat as consistent with the paper, not as my own read of the Adobe page. Re-check by hand before a skill cites it as read. |
| RT31 | The Mixamo FAQ was last updated 2021-09-14. | RP:237, 810 (C50; A1) | A1 | same as RT30; `https://helpx.adobe.com/creative-cloud/help/mixamo-rigging-animation.html` (403) | The search extract shows no "last updated" date. The Adobe page itself was not reachable. | unverified | I tried WebFetch (403), curl with a browser agent (403 "Access Denied"), regional Adobe URLs (403), a text proxy (401), the Wayback Machine (blocked / 429). |
| RT32 | The FAQ warns about extreme proportions, extra appendages, posed or asymmetric models, disconnected parts and dirty meshes. | RP:237, 262 (C50) | A1 | same as RT30 | The extract lists: distinguishable head, body, arm and leg areas; large extra appendages, floating parts, extra scene objects and non-neutral poses can make rigging fail; a clean mesh rigs more reliably. | partly | Same cautions in substance; the extract adds "extra scene objects". "Asymmetric" and "extreme proportions" were not in what I could read. |
| RT33 | No newer 2026 official Mixamo auto-rigger release exists. | RP:813 (CL67) | A1 | web search 2026-10-21 (two queries) | No Adobe announcement of a new auto-rigger or quadruped support came up. Only third-party vendor guides turned up, some describing Mixamo as unmaintained. | unverified | An absence claim from a short search, with competing vendors as the only hits. Do not state it as fact; say "none found". |
| RT34 | Reallusion AccuRIG: guided body and hand setup; the published comparison separates free and advanced versions. | RP:241 (C51; 4e-c) | A2 | `https://magazine.reallusion.com/2025/06/30/free-accurig-versus-cc-advanced-accurig/` | Dated June 30, 2025. Free AccuRIG is a stand-alone download; Advanced is inside Character Creator. Both use a step-by-step process, both rig humanoid (bipedal) meshes, both allow marker correction. Free does not create facial bones; Advanced can. Advanced adds editing of skin weights, hard/soft mesh choice and post-skin proportion edits. | confirmed | Vendor-hosted. The article covers bipedal meshes only; it does not say how it handles quadrupeds. The paper's "do not merge free and paid feature sets" is right. |
| RT35 | The AccuRIG Blender tutorial supports hands with zero to five fingers. | RP:241 (C51; N28) | A3 | `https://magazine.reallusion.com/2022/11/11/accurig-to-blender-pipeline-an-easy-accurate-way-to-auto-rig-any-character/` | Dated November 11, 2022. The text says AccuRIG can handle hands with zero to five fingers. It also says AccuRIG does not rig eyes, and Rigify can add eye controls. | confirmed | Vendor-hosted, 2022; the free tool has changed since (AccuRig 2.0, July 2025). Not proof of quality on generated hands. |
| RT36 | UniRig (arXiv, 2025) proposes skeleton and skinning prediction across categories. | RP:245 (C52; 4e-e) | A4 | `https://arxiv.org/abs/2504.12451`; arXiv API record, read 2026-10-21 | v1 submitted 2025-04-16, no later version. Abstract: a unified autoregressive framework that predicts skeletons and skinning weights; new dataset Rig-XL (over 14,000 models); works across categories. Authors report 215% and 194% gains on challenging data. | confirmed | Author-reported research metrics. No Roblox statement. The official repo `https://github.com/VAST-AI-Research/UniRig` exists (GitHub API: MIT licence field, last push 2026-06-04); I did not run it. |
| RT37 | Puppeteer (arXiv, Aug 2025) describes skeleton prediction, weight inference and an animation pipeline. | RP:245 (C53; 4e-e) | A5 | `https://arxiv.org/abs/2508.10898`; arXiv API record | Submitted 2025-08-14. Abstract: autoregressive skeleton prediction, attention-based skinning weight inference, and a differentiable optimisation-based animation stage. | confirmed | Research result. Official repo `https://github.com/Seed3D/Puppeteer` (GitHub API: Apache-2.0 licence field, last push 2025-09-19). Not run. |
| RT38 | Skin Tokens (first submitted 2026-02-04, revised 2026-10-19) introduces compact learned skin weights and a unified TokenRig framework. | RP:247 (C54; 4e-f) | A6 | `https://arxiv.org/abs/2602.04805`; arXiv API record | v1 2026-02-04, v2 2026-10-19; journal reference ACM Transactions on Graphics 2026. Abstract: SkinTokens (discrete skin-weight representation) and TokenRig (one sequence for skeleton and skin), refined with reinforcement learning. Authors report 98%-133% better skinning accuracy and 17%-22% better bone prediction. | confirmed | Author-reported metrics, not Roblox acceptance. The paper is right to say so. |
| RT39 | Availability, licence, hardware, MCP and R15 export of TokenRig and other research riggers are unknown. | RP:249-251 (X15; 4e-g) | A6 | GitHub API `https://github.com/VAST-AI-Research/SkinTokens`; GitHub repository search | A public repo `VAST-AI-Research/SkinTokens` exists (MIT licence field, last push 2026-05-12). Third-party wrappers exist (a Modly extension, `tokenrig-retarget`). Nothing found on MCP or an R15 exporter. | partly | Code and licence field found. Weights, hardware needs and the repo's terms were not read. Keep the paper's rule: candidate only, local benchmark first. |
| RT40 | Auto-Rig Pro game export supports Humanoid and Universal skeletons and has custom-bone export rules; its settings are not Roblox settings. | RP:344, 572 (CL55; K02) | B4 | `https://www.lucky3d.fr/auto-rig-pro/doc/ge_export_doc.html` | Two skeleton types: Humanoid for human bipeds, Universal for any creature. Custom bones (clothes, hair, props) are not exported by default; tag them or start the name with `cc_`. Targets named are Unity, Unreal, Godot. | confirmed | The page names no Roblox export. Page has no date; footer reads 2016-2023. |
| RT41 | The Auto-Rig Pro doc notes a bind-pose issue fixed in 3.78.49. | RP:671 (CL56) | B4 | same as RT40 | A warning says it applies only to older versions and was fixed in 3.78.49. It concerns bind pose import in Unreal Engine (export mesh and animations separately). | confirmed | Engine-specific. It does not tell you the newest release or anything about Roblox. |
| RT42 | A volume-preserving Blender preview can differ from ordinary game-engine skinning. | RP:279 (CL54; W18) | B4 | same as RT40 | The page says game engines generally do not support dual quaternion skinning, which Blender's Preserve Volume uses; uncheck Preserve Volume in the armature modifier to see engine deformation. Its Fix Rig step turns Preserve Volume off. | confirmed | General engine statement by an add-on vendor. How Roblox skins is a separate question (see `fact-check-roblox.md`, RR29). |
| RT43 | Exporting only Deform bones can drop a required non-deforming root. | RP:342, 572 (CL57) | B4, R3 | same as RT40 | By default the add-on exports all deforming bones. It does not export the `c_pos` and `c_traj` master controllers by default, and custom bones only when tagged. It does not say whether a plain root bone is exported. | partly | Supports "non-deforming nodes are not exported unless you ask". The Blender exporter option "Only Deform Bones" is a J005-T07 item. |
| RT44 | Rigify builds a reusable control rig from a metarig, with IK/FK features; stays useful after an AI skeleton is repaired. | RP:243, 344 (C27 first half; CL48) | B3 | Blender manual source, `https://projects.blender.org/blender/blender-manual/raw/branch/blender-v5.2-release/manual/addons/rigify/introduction.rst` and `.../rig_features.rst` | Building-block rig generation from a metarig; FK/IK and snapping features; "IK and FK Switching" section; generated rig works without the add-on. Rigify automates controls and bones only; you skin the mesh yourself. | confirmed | `docs.blender.org` returned 403, so I read the manual repository's 5.2 release branch. "Stays useful after an AI skeleton is repaired" is the paper's OPINION. The rest of C27 and CL48 are J005-T07. |
| RT45 | StraySpark (published 2026-05-14): a Tripo workflow exported fine but showed shoulder/chest slumping and poor jaw weights; protocol Blender + Unreal retargeting + movement tests. | RP:229, 840-843 (C55; 4d-f; CL68) | E1 | `https://www.strayspark.studio/blog/ai-auto-rigging-showdown-2026-tripo-meshy-cascadeur-mixamo` (raw page text) | Dated May 14, 2026, byline "StraySpark". Tripo exports cleanly to FBX; shoulder and chest weights are over-smoothed (broad shoulder pads slump); jaw weights are noisy. Protocol: one mesh of about 30K triangles, Blender 5.1, then Unreal 5.7 Mannequin retarget, walk/run/wave, Mover 2.0. | confirmed | The article names the tool "Tripo P1.0" and no rig model id. P1 is a generation family in Tripo's list (MV), so what rig model ran is unknown. It attributes the weight faults to Tripo, not to "older auto-riggers" as CL68 words it. No Roblox mention. |
| RT46 | E1 calls Tripo biped-only; current Tripo docs list many rig categories. | RP:229, 843 (X03; LM04) | E1, T1 | same article; RIG | Article: "The rig is biped-only; no facial joints, no IK chain pre-setup." RIG lists eight `rig_type` values and a non-humanoid model `v2.5-20260210`. | confirmed | Both halves hold. The article also says Tripo handled a stylised non-humanoid robot "better than any other tool", which sits oddly with its own biped-only line. The id date 20260210 is before the article, but an id date is not a release date. |
| RT47 | E1 has no reproducible sample set and the site sells its own mesh tools. | RP:231 (C56; 4d-g; LM23) | E1 | same article | One humanoid mesh through all tools plus three poses and a 30-second run; no raw measurements; no repeat runs. The page promotes MeshPrep (from $39.99) and lists other StraySpark tools. The article also cites a Tripo vendor guide as a source. | confirmed | The article itself says it is opinionated. Keep it as a list of failure modes to test, as the paper says. |
| RT48 | No reliable independent evidence exists on failure rate, quality order or time saved for the v3.0 rig model, or for v2 segmentation quality. | RP:231, 587 (Q03; X14) | none | web search 2026-10-21 (queries on v3.0-20260909 reviews and benchmarks); RM; RIG | No review or benchmark of `v3.0-20260909` came up. Tripo's own pages give "faster/better" wording and a ~30 s speed on RM, with no data. | unverified | An absence claim from short searches. It stays OPINION-unresolved. Do not write a success rate. |

## Coverage map (check C2)

Every `tripo` and `other-tool` row of the two claims tables, with the RT row that answers it. Nothing is merged away without a row.

| notes-file row | RT row(s) |
| --- | --- |
| C31 | RT13 |
| C32 | RT14 |
| C33 | RT15 |
| C34 | RT16 |
| C35 | RT17, RT21 |
| C36 | RT18 |
| C37 | RT19 |
| C38 | RT20 |
| C39 | RT12 |
| C40 | RT08, RT09 |
| C41 | RT07 |
| C42 | RT01, RT02 |
| C43 | RT03, RT04 |
| C44 | RT10 |
| C45 | RT23, RT24 |
| C46 | RT25, RT26 |
| C47 | RT11 |
| C48 | RT28 |
| C49 | RT22 |
| C50 | RT30, RT31, RT32 |
| C51 | RT34, RT35 |
| C52 | RT36 |
| C53 | RT37 |
| C54 | RT38 |
| C55 | RT45 |
| C56 | RT47 |
| CL54 | RT42 |
| CL55 | RT40 |
| CL56 | RT41 |
| CL57 | RT43 |
| CL58 | RT01, RT03, RT04 |
| CL59 | RT12 |
| CL60 | RT14 |
| CL61 | RT18, RT19 |
| CL62 | RT10, RT17, RT21 |
| CL63 | RT08, RT11 |
| CL64 | RT05, RT06 |
| CL65 | RT27 |
| CL66 | RT30 |
| CL67 | RT33 |
| CL68 | RT45, RT46 |

Also answered, outside the claims tables: numbers N13-N24 (RT10, RT14, RT17, RT19, RT01, RT03, RT23-RT25, RT07), T01-T06 (RT14-RT20, RT12, RT07-RT11, RT23-RT25), 4d-c (RT29), 4d-e (RT27, RT28), 4e-a to 4e-g (RT30-RT39), questions X03 (RT46), X07 (RT05), X08 (RT26), X15 (RT39), X17 (RT02), Q03 (RT48), C27 first half (RT44). C27 second half and CL48 are Blender items for J005-T07.

## Facts the skills may state

Each line is safe to put in a skill, with the page and read date 2026-10-21. "Vendor" means Tripo's own words, not measured quality.

1. Tripo auto-rig is `POST /v3/animations/rig`. The model field is `model`. Ask for `v3.0-20260909` by name; it is not the default. (RT01, RT04; RIG, CL)
2. The default rig model is `v1.0-20240301`, which is biped (humanoid) only. For non-humanoids use `v2.5-20260210` or `v3.0-20260909`. (RT03, RT07; RIG)
3. Tripo recommends `v3.0-20260909` for humanoids and says other rig types keep v2.5 quality and speed. Label it a vendor claim; no benchmark is published. (RT02; RIG, CL)
4. `rig_type` values: biped (default), quadruped, hexapod, octopod, avian, serpentine, aquatic, others. `others` needs v3.0. (RT08; RIG)
5. `spec` (bone naming) only applies to biped: `tripo` (default), `mixamo`, plus on v3.0 `actorcore`, `unity`, `unreal`, `vrm`. There is no Roblox or R15 preset on the pages as of 2026-10-21. (RT11; RIG, RM)
6. Output is GLB (default) or FBX. Input is GLB, FBX, OBJ or STL, up to 150 MB. (RT09, RT10; RIG)
7. Run rig-check first: `POST /v3/animations/rig-check` returns `riggable` and a recommended `rig_type`. It is a riggability screen, not a deformation check. (RT12; CHK)
8. Segmentation is `POST /v3/mesh/segment`, default `v1.0-20250506`; `v2.0-20260430` is Beta and adds semantic labels. For v2: `segmentation_granularity` simple/balanced/detailed, `split_by_connectivity`, and `ref_image`, which makes the other two fields ignored. Input up to 150 MB. (RT13-RT17; SEG)
9. Smart Segmentation is `POST /v3/mesh/smartsegment`. It includes modeling. A model input must be GLB and needs a `transform` of 16 floats, column-major 4x4. Optional `hint`; `granularity` coarse/medium/fine. (RT18-RT20; SS)
10. Retopology is `POST /v3/mesh/decimate`. `model=v3.0` must be requested; the default is `v2.0`. `face_limit` is 500-20,000 for triangles and 500-10,000 for quads. (RT23, RT24; DEC, CL)
11. Smart UV is `POST /v3/mesh/uv`. Input may not exceed 80,000 equivalent triangles (a quad counts as two); larger tasks fail and credits are refunded. It remaps existing textures, rigging and animation onto the new layout. (RT25; UV, CL)
12. The Tripo pages state no triangle or face cap for rigging, rig-check, segmentation or smart segmentation. Write "none documented as of 2026-10-21", and keep dense meshes low as advice, not as a limit. (RT28)
13. Tripo has several independent version ids: geometry model, segmentation model, rigging model, retopology model, texture model. Record each. (RT29; MV, CL)
14. Adobe says Mixamo's auto-rigger is for bipedal humanoids only. Cite it as read secondhand until someone opens the Adobe page. (RT30)
15. AccuRIG (free) rigs bipedal humanoid meshes, can set up hands with zero to five fingers, and creates no facial bones; CC Advanced AccuRIG can. (RT34, RT35)
16. UniRig, Puppeteer and Skin Tokens/TokenRig are research papers with author-reported metrics. Public repos exist for each (GitHub licence fields: MIT, Apache-2.0, MIT). Nothing documents a Roblox exporter. (RT36-RT39)
17. Auto-Rig Pro exports Humanoid and Universal skeletons; custom bones are exported only when tagged (`cc_` prefix or custom-bone property); game engines generally lack dual quaternion skinning, so turn Preserve Volume off to preview engine deformation. (RT40, RT42)
18. Rigify generates a control rig from a metarig with FK/IK features and does not bind it to the mesh. (RT44)

## Drop or keep as OPINION

| item | paper and line | decision | reason |
| --- | --- | --- | --- |
| "The Mixamo FAQ is dated 2021-09-14" | RP:237, 810 | Drop the date until re-read | I could not read the Adobe page (RT31). Say "Adobe FAQ, date not re-verified". |
| "No newer 2026 official Mixamo auto-rigger release" | RP:813 | Keep as OPINION, worded "none found" | Short search only (RT33). |
| "Mixamo is a weak default for toy parts, birds, quadrupeds, mechanisms" (D11, 4e-b) | RP:239, 570 | Keep as OPINION | Follows from "bipedal humanoids only" plus the FAQ cautions; the paper's own tag is OPINION. |
| "Tripo rig-check is not a Studio quality validator" | RP:221, 553 | Keep as OPINION | The page documents only `riggable` and `rig_type` (RT12). |
| "Tripo has four version numbers" | RP:223 | Reword | There are more (RT29): list them all or say "several". |
| Any 300k-polygon rigging limit | not in RP; found at a reseller | Drop as a limit; keep as advice at most | Reseller guidance, undated, not Tripo docs (RT28). |
| Tripo Studio UI limits | RP:227 | Keep as OPINION-unresolved | I found no page (RT28). |
| Success rate, repair time, quality order for v3.0 rig or v2 segmentation | RP:231, 587 | Keep as OPINION-unresolved | No independent evidence found (RT48). Do not invent numbers. |
| StraySpark results as a feature matrix or as the current Tripo state | RP:229-231 | Keep as EXPERIENCE; failure-mode list only | One mesh, unknown rig model, commercial interest (RT45, RT47). |
| "Tripo is biped-only" (from E1) | RP:229 | Drop | Contradicted by RIG (RT46). |
| `smart_uv` flag on retopology as the "Smart UV" feature | not in RP | Do not conflate | Different endpoints and limits (RT26). |
| Auto-Rig Pro Unreal bind-pose warning as a rule | RP:671 | Drop as a rule | Fixed in 3.78.49 and engine-specific (RT41). |
| Research riggers as production tools | RP:245-251 | Keep as OPINION | Papers and repos only; no Roblox path (RT36-RT39). |

## Extra findings

- Default trap. A request with no `model` field goes to `v1.0-20240301`, which is biped only (RT03). A rigger skill that sends a non-humanoid rig request must name `v2.5-20260210` or `v3.0-20260909` and set `rig_type`.
- Input formats changed in 2026-10 (CL): rig-check now accepts GLB, FBX, OBJ, STL (was GLB only), and auto-rig inputs use the same four and no longer list GLTF. SEG and DEC still list GLTF. The paper does not mention input formats.
- Rig `input` accepts a `task_id` only from a text/image/multiview generation task (RIG). A model that went through segmentation or Blender must be passed as a public URL or a `file_token`.
- Upload route: models up to 150 MB by multipart upload; above 60 MB Tripo suggests the large-file upload (files and files-presign pages). Smart Segmentation takes a `file_token` or public URL only.
- Smart UV remaps "rigging and animation" onto the new layout (UV). So a re-unwrap after rigging should keep the rig. Not tested by me; the page states it.
- Tripo's game-asset generators: `P1-20260311` (50-20,000 faces) and `P2-20260801` (Preview; native quads; 48-50,000 triangles or 48-25,000 quads). Default geometry model is `v3.1-20260211` (MV). These are vendor descriptions of generation output, not rig-ready proof.
- Smart Segmentation, image pipeline: the example task result lists a mask, a segmented model and a separate `model_task_id` (SS), so the model is generated from an image. The page shows no equivalent result for `seg_type=model`.
- AccuRig 2.0 (July 2025, CG Channel article dated 2025-07-17, updated 2025-07-21): free download, FBX/USD export presets for Blender, Unity, Unreal; a free ActorCore account is required to export; OBJ and FBX import. Press report, not Reallusion's own page; I could not reach a Reallusion product page.
- Competing vendors describe Mixamo as in maintenance mode. These are marketing pages from tools that compete with it; I give them no weight.
- Rate limits: the Animation category (auto-rig, rig-check, retarget) and the Mesh Operations category each list 10 as a concurrency figure on the rate-limits page. The RM page says 10 parallel tasks for Animation. Not needed by the skills.

## Reading notes

- Tripo page text came from raw HTML I stripped myself; ids, parameter names and ranges in the rows are from that text. I also ran a summary-model fetch on the same pages first. Its extract of RIG wrongly said the VRM example used `spec: mixamo`; the raw page shows `vrm`. I used only the raw text. This is why I checked every number against raw text where I could.
- Adobe (Mixamo), `docs.blender.org` and `reallusion.com` product pages blocked my fetches. For Rigify I read the Blender manual repository (5.2 release branch). For Mixamo I have only a search-tool extract (RT30-RT33 reflect that). The Reallusion Magazine pages were readable and their dates match the paper.
- arXiv dates and abstracts came from the arXiv API record; GitHub licence and push dates from the GitHub API on the read date. I did not download weights or run any code.
- I edited no file other than this one.

## Lead re-check (2026-10-21)
| id | claim | checked against | what the source says | verdict |
| --- | --- | --- | --- | --- |
| RT31-L | Mixamo FAQ date 2021-09-14; auto-rigger bipedal humanoids only | https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html, opened in the built-in browser 2026-10-21 by the lead (orchestrator · claude-opus-5-5) | Page shows "Last updated on Sep 14, 2021"; FAQ answer: the auto-rigger and animation libraries are for bipedal humanoids only | confirmed (supersedes RT30-RT31 "secondhand" status) |
