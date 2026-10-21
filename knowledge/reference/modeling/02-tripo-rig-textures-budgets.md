---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J007-T02, Modeler_Research_Paper.txt lines 423-711"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Modeling paper part 2: Tripo generation and Blender finishing, building for rigger and animator, textures and materials, Roblox budgets (lines 423-711)

Paraphrased notes. The paper (MP) stays outside git. Every row cites `MP:<line>`. Nothing here is fact-checked yet: the paper's claims are listed in "Claims to fact-check" for the next pass. The paper's cutoff and access date is 2026-10-21. Paper headings 9 and later (from MP:712) are out of range.

## Headings covered (C1)

| MP lines | Paper heading | Section here |
| --- | --- | --- |
| 423 | 5 Tripo generation and Blender finishing | 1 to 8 |
| 425-431 | Choose a production route, not a marketing label | 1 |
| 433-444 | Route and operation matrix | 2 |
| 446-454 | Reference preparation and real multiview input | 3 |
| 456-462 | What the output proves, and what it does not | 4 |
| 464-474 | Current processing behavior | 5 |
| 476-504 | Numbered Tripo to Blender to Roblox finish workflow (13 steps) | 6 |
| 506-510 | Cost and licensing, attach them to the route | 7 |
| 512-522 | 2026 AI modeling research, useful mechanisms, bounded evidence | 8 |
| 524-534 | Closing evidence table (section 5) | 9 (crosswalk) |
| 536-544 | 6 Building for the rigger and animator | 10 |
| 546-560 | Parts for animation (table plus requirements sheet) | 10 |
| 562-566 | Rule table (section 6) | 9 (crosswalk) |
| 568-570 | 7 Textures and materials | 11 |
| 572-578 | Separate authoring representation, imported assets, and client residency | 11 |
| 580-590 | Choose the cheapest representation that preserves approved art | 11 |
| 592-594 | Vertex colors are not a universal no-texture shortcut | 11 |
| 596-598 | Optional current texture tool | 11 |
| 600-609 | Evidence summary (section 7) | 9 (crosswalk) |
| 611 | 8 Roblox optimization and measured budgets | 12 |
| 613-617 | Ceilings are not affordable scene budgets | 12 |
| 619-633 | A truthful budget table for the requested eight types | 12 |
| 635-657 | Turn unknown budgets into a measured allocation (plus allocation record fields) | 12 |
| 659-661 | Reuse and batching | 12 |
| 663-669 | Three different streaming systems and a real documentation conflict | 12 |
| 671-673 | Collision fidelity, five choices not four | 12 |
| 675-679 | Measure with named current tools | 12 |
| 681-701 | Numbered optimization checklist with real numbers | 13 |
| 703-710 | Evidence table (section 8) | 9 (crosswalk) |

## 0. How to read

| Key | Meaning |
| --- | --- |
| MP:n | line n of `Modeler_Research_Paper.txt`. One paragraph or table row = one line. Source register = MP:976-1974. |
| Tag | VERIFIED (a primary source states it; for vendors, only what the vendor documents, not output quality), EXPERIENCE (a named report), OPINION (the paper's own proposal), UNKNOWN (stays unknown, never turn into a fact). Tags are the paper's. |
| OPINION* | The paper put an advice or inference sentence inside a paragraph tagged VERIFIED, or left a table column untagged. I tag that sentence OPINION* (a downgrade, never an upgrade). The fact part of the same paragraph keeps VERIFIED in its own row. |
| Src | paper source ID (resolved in section 16). P00 = the paper's own proposed method (OPINION). |
| Surface | API = Tripo developer API (developers.tripo3d.ai). Studio = Tripo Studio web app and its product docs. The owner runs Studio (J007-D4). A row marked API does not prove the same control exists in Studio. |
| Stage | rig-pipeline stage the row serves: S0 intake, S1 motion needs, S2 rig plan, S3 geometry (modeler), S4 geometry acceptance, S5 rig + tests, S6 rig acceptance, S7 animate, S8 owner final. `pre-S0` = making the model source. `-` = not tied to a stage. |
| Who | [for-rigger] [for-animator] [for-art-director] [for-ui] [for-vfx] [for-environment] [for-owner-tripo] = the role that also needs or must act on the row. [for-owner-tripo] = what the owner must do or decide in Tripo. |
| Row IDs | TR route, input, output checks, processing; FW finishing step; CL cost and licence; RS research; RG rig building; TX textures; BG budgets; CK checklist item; CW crosswalk. |
| Ceiling rule | Every limit from the paper is a ceiling, generator maximum, other-game number or category limit unless the row says "project". None is a phone budget. The owner budget (J007-D5): 20,000 triangles per mesh is the Roblox upload ceiling only; creatures and characters stay under about 7,000 triangles. |

## 1. Choose a production route (MP:425-431)

| ID | MP | Lesson | Tag | Src | Surface | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-01 | 427 | Tripo Studio labels: "Best Quality" = HD Model = H Series. "Clean Topology" = Smart Mesh = P Series. Source undated, accessed 2026-10-21. | VERIFIED | T27 | Studio | pre-S0 | [for-owner-tripo] |
| TR-02 | 427 | The labels name routes. They do not prove H is best for every Roblox hero character. | OPINION* | T27, P00 | Studio | pre-S0 | [for-owner-tripo] |
| TR-03 | 427 | Keep the fixed image-first workflow and the mainly hand-built Blender route. Use Tripo for a candidate hero asset only when reference fidelity and cleanup burden look promising. A preference for quality is not a guarantee a generator delivers it. | OPINION | P00 | - | pre-S0 | [for-art-director] |
| TR-04 | 427 | A character that bends cleanly and keeps identity at gameplay distance can be better than a denser static surface. | OPINION | P00 | - | S2, S3 | [for-rigger] |
| TR-05 | 428 | H3.1 snapshot is v3.1-20260211 (live card, accessed 2026-10-21). Documented triangle ceiling: 1,500,000 at standard geometry, 2,000,000 at detailed geometry. The quad option forces FBX output. If a quad face limit is omitted the card gives 10,000 faces. These are generator capabilities, not runtime asset counts. | VERIFIED | T01 | API | pre-S0 | [for-owner-tripo] |
| TR-06 | 428 | Treat a high-detail H result as a source for a controlled low-poly asset or bake unless it meets the approved in-game budget on its own. Never import the maximum resolution only because it generated. | OPINION | P00 | - | S3 | [for-owner-tripo] |
| TR-07 | 431 | API model card: P2-20260801 is still marked Preview; P1-20260311 is the previous stable release. Studio's September update says P2 officially launched (blog index date 2026-10-10). | VERIFIED | T02, T06, T07 | API + Studio | pre-S0 | [for-owner-tripo] |
| TR-08 | 431 | Studio announcement advertises 500-50,000 triangle faces or 500-25,000 quad faces. The API accepts 48-50,000 triangles or 48-25,000 quads. P2 adds quad output; P1 does not support quad. | VERIFIED | T02, T06, T07 | API + Studio | pre-S0 | [for-owner-tripo] |
| TR-09 | 431 | A date inside a model ID, or an updated blog title, does not prove an API preview became stable. Save the exact surface, snapshot, request and returned result metadata. | OPINION* | T02, T06, T07, P00 | API + Studio | pre-S0 | [for-owner-tripo] |

## 2. Route and operation matrix (MP:433-444)

Paper columns: "Verified scope" (tag VERIFIED, sources in the cell) and "What the modeler must not infer" (untagged, so OPINION*).

| ID | MP | Route or operation | Verified scope | Tag | Src | Do not infer (OPINION*, P00) | Who |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-10 | 436 | H3.1 v3.1-20260211 | VERIFIED: high-detail geometry; text, image and multiview input; independently controlled texture options. Accessed 2026-10-21. | VERIFIED; OPINION* | T01 | More triangles do not mean better silhouette, rigging, hidden geometry or phone performance. | [for-owner-tripo] |
| TR-11 | 437 | P2-20260801 API | VERIFIED: Preview; triangles or quads; text, image, multiview; no smart_low_poly, generate_parts or geometry_quality parameters. Accessed 2026-10-21. | VERIFIED; OPINION* | T02 | Do not assume Studio Mesh Edit, variants or automatic part-generation controls exist in this API. | [for-owner-tripo] |
| TR-12 | 438 | P2 Studio official | VERIFIED: native-quad claim; independent parts; regional Mesh Edit; up to four different-polycount variants on eligible plans. Accessed 2026-10-21, update 2026-10-10. | VERIFIED; OPINION* | T06, T07 | Four variants are not a temporally stable, validated LOD chain. Topology changes do not necessarily keep rig or UV indices. | [for-owner-tripo] [for-rigger] |
| TR-13 | 439 | Segmentation v2.0-20260430 | VERIFIED: Beta; semantic plus geometry. Default is v1.0-20250506, geometry only. | VERIFIED; OPINION* | T11 | Semantic names do not prove correct articulation boundaries or completed hidden surfaces. | [for-rigger] |
| TR-14 | 440 | Retopology v3.0 | VERIFIED: introduced October 2026; must be selected explicitly because the default is v2.0. | VERIFIED; OPINION* | T03, T12 | The endpoint name /mesh/decimate does not mean every algorithm is simple decimation. | [for-owner-tripo] |
| TR-15 | 441 | Texture v3.5-20260815 | VERIFIED: added September 2026; pin it independently with texture_version in generation. | VERIFIED; OPINION* | T03, T14 | Geometry model v3.1 does not select the newest texture model automatically. | [for-owner-tripo] |
| TR-16 | 442 | Smart UV /mesh/uv | VERIFIED: re-unwraps and remaps; returns a UV atlas preview. Accessed 2026-10-21. | VERIFIED; OPINION* | T13 | A clean atlas preview does not prove correct texel density, seam hiding or runtime material setup. | [for-owner-tripo] |
| TR-17 | 444 | Route choice at blockout | OPINION: route can be revised at blockout. Prefer hand authoring for exact grid-fitting modular kits, authored mechanical pivots, hard dimensional constraints, or a few intentionally simple shapes. Trial Tripo when organic massing or an intricate reference is expensive to rebuild by hand. Drop or rebuild a candidate when keeping identity or deformation needs more correction than hand work. These are planning judgments, not a measured speed ranking. | OPINION | P00 | - | [for-environment] [for-rigger] |

## 3. Reference preparation and real multiview input (MP:446-454)

| ID | MP | Lesson | Tag | Src | Surface | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR-18 | 448 | Tripo recommends: centered, complete subject filling 70-85% of the image; even background; diffuse lighting; at least 1024x1024 for quality. Warns against low resolution, occlusion, reflectivity, transparency, multiple subjects. Vendor help, undated, accessed 2026-10-21. These are recommendations, not upload minima or measured optima. | VERIFIED | T08 | Studio help | pre-S0 | [for-owner-tripo] [for-art-director] |
| TR-19 | 448 | Multiview help asks for matching pose, scale, lighting, background and design across views. | VERIFIED | T09 | Studio help | pre-S0 | [for-owner-tripo] |
| TR-20 | 448 | Conflicting views do not become consistent because they share a character name. | OPINION* | T09, P00 | - | pre-S0 | [for-art-director] |
| TR-21 | 450 | v3 API takes either named view-key inputs (each key is one of front, left, back, right) or legacy positional inputs of exactly four slots ordered front, left, back, right. A front view is required and at least two real images must be given. Missing optional positional views are empty slots; named views can omit absent directions. Do not mix the two schemas. | VERIFIED | T04, T05, T29 | API | pre-S0 | [for-owner-tripo] |
| TR-22 | 450 | v3 documents PNG, JPEG and WebP input and recommends at least 256x256. Older v2 docs use files and model_version (not inputs and model) and describe JPEG/PNG URL input up to 20 MB. These are versioned endpoint differences, not permission to mix request bodies. | VERIFIED | T04, T05 | API | pre-S0 | [for-owner-tripo] |
| TR-23 | 450 | The four-slot legacy order is easy to corrupt, because Studio tutorials sometimes discuss front/side/back loosely. (Paper gives no source for the tutorial remark.) | OPINION* | T04, T05, T29 | API + Studio | pre-S0 | [for-owner-tripo] |
| TR-24 | 452 | A ChatGPT turnaround collage is an approval artifact, not automatically a valid multiview input. Crop approved views into independent images; remove labels, callouts and background clutter; keep matching scale and neutral pose; check which side each view shows. | OPINION | P00 (based on T04, T08, T09) | - | pre-S0 | [for-art-director] [for-owner-tripo] |
| TR-25 | 452 | Single-image mode: give one coherent subject, not a sheet of four people. Do not relabel a three-quarter image as a strict left elevation without testing the selected interface's convention. | OPINION | P00 (based on T04, T08, T09) | - | pre-S0 | [for-owner-tripo] |
| TR-26 | 452 | If views disagree (tail count, handle location, shoulder width, roof depth), repair the design before generation. Use the approved front and the intentional backside design as the source of truth, not the view a generator emphasized. | OPINION | P00 (based on T04, T08, T09) | - | pre-S0 | [for-art-director] |
| TR-27 | 454 | Studio offers multiview image generation from one image, and image Cutout into 1-10 transparent PNGs. Cutout is image extraction, not 3D segmentation. Tripo itself says unseen surfaces in generated multiview images are inferred. Product doc October 2026, help page accessed 2026-10-21. | VERIFIED | T10, T28 | Studio | pre-S0 | [for-owner-tripo] |
| TR-28 | 454 | Generated views can make an approved design explicit. They are not independent evidence that the original image held a correct rear surface. The workflow starts with the ChatGPT reference, not with Tripo replacing the art director's approved design. | OPINION | P00 | - | pre-S0 | [for-art-director] [for-owner-tripo] |

## 4. What the output proves and what it does not (MP:456-462)

| ID | MP | Lesson | Tag | Src | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- |
| TR-29 | 458 | Tripo's published P2 workflow (2026-10-14) follows one semi-anime fantasy girl through regional repair, UVs, textures, rigging and an Unreal preview. It shows a possible workflow, not a Roblox-mobile performance test or a studio-wide success rate. Tripo's own blog. | EXPERIENCE | T20 | - | - |
| TR-30 | 458 | Generation and finishing are separate stages. Inspect the exported mesh and textures, not a textured browser beauty render. | OPINION | P00 | S3 | [for-art-director] |
| TR-31 | 460 | Nexus (research, 2026-07-15) reports geometry/texture ambiguity, missing faces, resolution/grid artifacts and normal-orientation inconsistencies. Do not claim commercial P2 equals Nexus because some authors are tied to VAST. | VERIFIED | T21 | - | - |
| TR-32 | 460 | Turn those failure types into inspections on every generated candidate: clay view (texture-only fake detail); wireframe (density, connectivity); face-orientation display (inverted surfaces); underside and rear views (invented or missing structure); check disconnected components (floaters); deformation trial (joints). | OPINION | P00 | S3, S4 | [for-rigger] |
| TR-33 | 462 | Digital Production's independent trade review (2026-09-29) separates quad count from useful pole placement, loops and deformation. Its title invites a production test, but it publishes no reproducible exported-asset set or measured success rate. | EXPERIENCE | T25 | - | [for-rigger] |
| TR-34 | 462 | GLBGPT review by a named author (2026-09-10; lower confidence, optional): three H3.1 inputs, Standard vs Detailed; both modes missed held-out rear/underside structure. A small, commercially interested third-party report, not proof that one mode is better. | EXPERIENCE | T26 | - | - |
| TR-35 | 462 | No robust independent 2026 benchmark of Tripo cleanup hours, hero acceptance rate or Roblox-ready yield was verified by the paper. | UNKNOWN | P00 | - | - |
| TR-36 | 462 | Do not fill that gap with vendor claims such as "production-ready", unscoped percentage time savings or competitor comparison scores. | OPINION | P00 | - | [for-owner-tripo] |

## 5. Current processing behavior (MP:464-474)

All rows in this section describe API docs (accessed 2026-10-21 unless noted). The paper does not show that Studio exposes each control.

| ID | MP | Lesson | Tag | Src | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- |
| TR-37 | 466 | Semantic segmentation v2 takes granularity simple, balanced or detailed, plus split_by_connectivity. Giving ref_image makes both controls ignored. Inputs: task IDs, uploaded tokens or URLs. Listed formats GLB, GLTF, FBX, OBJ, STL, maximum 150 MB. | VERIFIED | T11 | S3 | [for-owner-tripo] |
| TR-38 | 466 | Check segmentation labels against the rig requirements sheet. A shoulder clothing boundary and a shoulder articulation boundary are not necessarily the same cut. Keep the source mesh; inspect caps and overlap before accepting a split. | OPINION | P00 | S3, S4 | [for-rigger] |
| TR-39 | 466 | Cut by hand in Blender when the modeler needs exact hinge lines, retained edge loops or deliberate seam covers. | OPINION | P00 | S3 | [for-rigger] |
| TR-40 | 468 | Retopology v3 takes 500-20,000 triangles or 500-10,000 quads. smart_uv works only with v3.0; with v1 or v2 it returns 400 / error 1004. It adds UV unwrapping at no extra charge but does not return the UV-atlas preview. Texture baking and per-part targeting are documented, with v1 exclusions. October 2026 changes. | VERIFIED | T12, T03 | S3 | [for-owner-tripo] |
| TR-41 | 468 | Do not turn an approved 20,000-triangle budget into 10,000 quads by assumption. Triangulate and count the output, check for non-quad faces, measure the imported result. Count triangles after required modifiers and export, not Blender's displayed polygon number. | OPINION | P00 | S3, S4 | [for-rigger] |
| TR-42 | 470 | Standalone Smart UV accepts at most 80,000 equivalent triangles (a quad counts as two). A larger input can be accepted at task creation, then fail and refund credits; reduce first. bake=true is the default; a UV preview is returned. | VERIFIED | T13 | S3 | [for-owner-tripo] |
| TR-43 | 470 | Review distortion, island boundaries, padding for the chosen mip chain and surface importance. A service remapping rig or animation does not remove the need to recheck vertex-dependent downstream data. | OPINION | P00 | S3, S4, S5 | [for-rigger] [for-animator] |
| TR-44 | 472 | Texture requests take text, image or images guidance, mutually exclusive; style_image can accompany text. v3.5 adds delight (remove baked reference lighting) and a fast quality option. The default texture stays v3.0. The geometry snapshot does not imply v3.5 textures. | VERIFIED | T14 | S3 | [for-owner-tripo] |
| TR-45 | 472 | Use neutral-basecolor and lit renders separately. Keep authored stylized value gradients when wanted; do not erase all shading from an intentionally hand-painted look. Do not accept baked cast shadows posing as albedo on a moving PBR object. Keep palette and broad material separation, not only texture sharpness. | OPINION | P00 | S3 | [for-art-director] |
| TR-46 | 474 | Convert takes format, face_limit, quad, texture_size, bake, pack_uv, pivot_to_center_bottom and scale_factor. quad forces FBX. Vertex-color export is documented only for OBJ and GLTF. Default diffuse texture size 4096 is a conversion default, not a Roblox phone recommendation. | VERIFIED | T15 | S3 | [for-owner-tripo] |
| TR-47 | 474 | Do not blindly accept a bottom-center pivot for a wheel, door or shoulder. Keep intentional pivot, scale and orientation through the Blender intermediate; check in the Roblox importer. A file format being available does not prove every material channel or rig convention survives. | OPINION | P00 | S3, S5 | [for-rigger] |

## 6. Numbered Tripo to Blender to Roblox finish workflow (MP:476-504)

Paper rule (MP:478): all 13 steps are OPINION, a proposed studio procedure dated 2026-10-21, informed by T01-T15 and the Blender/Roblox evidence. They are not executed measurements. Tag and Src of every row: OPINION, P00.

| ID | MP | Step (paraphrase) | Stage | Who | Tag | Src |
| --- | --- | --- | --- | --- | --- | --- |
| FW-00 | 478 | All 13 steps below are proposed procedure, not measured results. | - | - | OPINION | P00 |
| FW-01 | 480 | Approve the reference and rig requirements first. Record owner/art-director approval, style block, dimensions, camera distance, articulation plan, attached props, allowed asymmetries, runtime budget. Reject mutually impossible image views. | S0, S1 | [for-art-director] [for-rigger] [for-animator] | OPINION | P00 |
| FW-02 | 482 | Prepare single-subject input or independently checked directional views. Record image hashes and direction labels. Do not treat generated hidden sides as recovered truth. | pre-S0 | [for-owner-tripo] | OPINION | P00 |
| FW-03 | 484 | Choose surface and exact geometry/texture snapshots. H for source-detail experiments, P for topology-oriented experiments; "hero" does not mean maximum polygons. Save requested face limit, seeds, geometry setting, texture model, task ID, costs and output files. | pre-S0 | [for-owner-tripo] | OPINION | P00 |
| FW-04 | 486 | Inspect the raw candidate before spending more work. Match camera projection and framing to the approved reference; compare silhouette, landmark proportions and negative spaces in clay and textured renders. Reject wrong anatomy, wrong part count, fused grips, missing openings, false backs, weak identity before retopology. | pre-S0, S3 | [for-art-director] | OPINION | P00 |
| FW-05 | 488 | Save raw output as immutable source; work in a separate Blender asset. Measure dimensions; list mesh objects, materials, textures, UVs; compute evaluated and triangulated totals; record normals, disconnected pieces, duplicates, non-manifold boundaries, interior geometry. Do not delete an intentional open surface just to make everything watertight. | S0, S3 | [for-rigger] | OPINION | P00 |
| FW-06 | 490 | Settle moving-part construction with rigger and animator. Use semantic segmentation as a proposal, then correct it. Cut rigid moving assemblies at intended joints; keep continuous deforming skin where skinning is the design. Rebuild hidden surfaces or seam covers; test the motion range, not only the rest pose. | S2, S3, S4 | [for-rigger] [for-animator] | OPINION | P00 |
| FW-07 | 492 | Simplify by error, not by face count alone. Decimation can serve static candidates; rebuild or retopologize joints, silhouette turns and mechanical interfaces when simplification destroys their function. Compare silhouettes before and after at game distance and a closer diagnostic distance. | S3 | [for-rigger] | OPINION | P00 |
| FW-08 | 494 | Repair orientation and surface integrity. Test faces, hard/soft shading, narrow details, contact surfaces, seams, intersections. Separate textured look from geometric shape; repair a missing handle as geometry, do not paint one on. | S3 | - | OPINION | P00 |
| FW-09 | 496 | Finalize UVs only after structural edits stabilize. Keep intended density hierarchy, seam placement, packing. Bake approved source detail to the runtime mesh; check cage/projection artifacts, overlaps, colour bleeding. Use the high-poly source only as reference or bake input when fitting. | S3 | [for-rigger] | OPINION | P00 |
| FW-10 | 498 | Finish stylized materials in Blender. Confirm palette, material groups, baked-shading policy, texture-channel meaning. Reduce to approved texture and material use, not service defaults. Re-render approved angles with neutral and representative lighting. | S3 | [for-art-director] | OPINION | P00 |
| FW-11 | 500 | Prepare an export copy. Apply the agreed scale/axis strategy, names, part origins, required modifier results. Recount triangles after triangulation; keep the editable authoring source. Export by the chosen Roblox-supported path and inspect the imported result, not the export log. | S3, S4 | [for-rigger] | OPINION | P00 |
| FW-12 | 502 | Validate in Roblox: scale against the player, attachments, normals, UVs, texture look, collision, deformation, distance behaviour. Profile in a representative population and device scene, not alone in an empty scene. If the budget is missed, return a failure report with the specific regression. | S4, S5, S8 | [for-rigger] [for-animator] | OPINION | P00 |
| FW-13 | 504 | Deliver: source .blend, raw Tripo outputs, reference IDs, generation manifest, textures, export, importer settings, part/rig sheet, preview angles, measured in-game result. The creative director decides artistic approval; platform validity and a render match do not replace it. | S3, S4 | [for-rigger] [for-art-director] | OPINION | P00 |

## 7. Cost and licensing (MP:506-510)

| ID | MP | Lesson | Tag | Src | Surface | Who |
| --- | --- | --- | --- | --- | --- | --- |
| CL-01 | 508 | API price list (accessed 2026-10-21): 1 credit = $0.01 USD. Standard-textured H image or multiview generation 30 credits. Separate processing: segmentation 40; retopology v3 triangle 35, quad 40; Smart UV 20; conversion 5 basic, 10 advanced. | VERIFIED | T16 | API | - |
| CL-02 | 508 | These are request prices, not end-to-end cost per accepted asset. Failed or rejected candidates, optional processing and human or agent cleanup change the total. | OPINION* | T16, P00 | API | - |
| CL-03 | 508 | P2 API card: 100 credits untextured; 110, 120 and 130 for standard, detailed and 8K texture. | VERIFIED | T02 | API | - |
| CL-04 | 508 | Studio prices differ (October 2026): HD generation 15 credits, P2 generation 100, segmentation 30. | VERIFIED | T17 | Studio | [for-owner-tripo] |
| CL-05 | 508 | Do not compare credit counts across Studio and API as identical work or identical dollar value. | OPINION* | T16, T17, P00 | both | [for-owner-tripo] |
| CL-06 | 508 | No account's checkout, tax or discount was inspected. | UNKNOWN | P00 | Studio | [for-owner-tripo] |
| CL-07 | 510 | Studio current table (October 2026): free output allows commercial use with attribution and Tripo owns the IP; paid private models get full commercial rights and user ownership. | VERIFIED | T17 | Studio | [for-owner-tripo] |
| CL-08 | 510 | Terms (last updated 2025-07-11): broad retained rights for free users, general rights for paid users, a licence to provide the service; paid inputs and outputs are not AI training data. | VERIFIED | T18 | both | [for-owner-tripo] |
| CL-09 | 510 | An older Tripo marketing page (2026-04-02) says free outputs are strictly noncommercial. (Vendor page, tagged EXPERIENCE by the paper.) | EXPERIENCE | T19 | - | [for-owner-tripo] |
| CL-10 | 510 | Do not resolve the contradiction by promising free-tier clearance. Record account plan, generation date, privacy setting and governing terms; get clarification of conflicting rights before shipping. Output rights are not a warranty that a reference or generated asset avoids another party's IP. Source reporting, not legal advice. | OPINION | P00 | both | [for-owner-tripo] |

## 8. 2026 AI modeling research (MP:512-522)

Table columns: "Verified setup/result" is tagged VERIFIED with the T id; "Transferable idea and limit" is OPINION, P00.

| ID | MP | Research | Verified setup and result | Tag | Src | Transferable idea and limit (OPINION, P00) |
| --- | --- | --- | --- | --- | --- | --- |
| RS-01 | 515 | UltraTex, 2026-09-19 | 2048-resolution multiview texturing; foreground/background token redundancy reduction; dataset over 268,000 assets. Reported end-to-end speedup 22.3x-74.6x against its baseline on common dataset samples. | VERIFIED (setup); OPINION (idea) | T24 | Judge coherent texture coverage, not output image size. A research baseline comparison, not a service latency promise or a Roblox 8K budget. Commercial Tripo identity not established. |
| RS-02 | 516 | ViSculpt, 2026-08-25 | Visual GUI geometry edits in Blender 4.5 LTS; Gemini 3 Flash main agents, 3 Pro grounding; 20 tasks, 40 edited meshes, 48 participants (39 nonexperts, 9 experts). Average rating 7.53 agent vs 7.20 human-created edits. | VERIFIED (setup); OPINION (idea) | T22 | Keep the observe, local-edit, render loop. Not proof of beating professional game artists or the current Python/MCP agent. It edits existing geometry; it does not author rig-ready assets from scratch. |
| RS-03 | 517 | Nexus, 2026-07-15 | Vertex/topology diffusion; tested on Objaverse/Toys4K and images; 1,221 pairwise practitioner comparisons; 93.0% preference in the reported baseline set; up to 20,000 faces. | VERIFIED (setup); OPINION (idea) | T21 | Judge geometry and connectivity separately. Missing faces and normals problems are acknowledged. Not proof P2 shares its architecture or results. |
| RS-04 | 518 | EZBlender, 2026-01-12 | Older backend GPT-4o; 245 preset BlenderGym scenes; 512x512 Cycles two-view renders; RTX 3090 24 GB, 96 GB RAM, Intel Core i9-13900K. Single-edit latency 37.35 s EZBlender, 286.08 s BlenderAlchemy, 23.85 s BlenderGPT. | VERIFIED (setup); OPINION (idea) | T23 | Planning plus bounded domain edits is useful. A 2026 paper on older models is not a current model ranking. Preset shape-key/material/light/camera edits and CLIP closed-set checks cannot certify arbitrary mesh topology. |

| ID | MP | Lesson | Tag | Src |
| --- | --- | --- | --- | --- |
| RS-05 | 520 | Treat screenshot similarity as one observation channel. Mesh inspection supplies dimensions, connectivity, material and UV evidence that a beauty image lacks. Viewpoint agreement, untextured renders and real deformation expose failures a global CLIP-like score misses. Do not invent an acceptance threshold such as 90% visual similarity without a project-specific definition and a measured link to approval. | OPINION | P00 |
| RS-06 | 522 | EZBlender Table 3 labels its latencies in seconds; Table 4 repeats the numbers under a millisecond header. The paper follows the explicit seconds of Table 3. | VERIFIED | T23 |

## 9. Crosswalk: the paper's summary tables

Each summary line is already covered by the row named. The paper's own tag and source are kept.

| ID | MP | Summary line (paraphrase) | Tag | Src | Covered by |
| --- | --- | --- | --- | --- | --- |
| CW-01 | 527 | Pin the P2 surface and snapshot: P2-20260801; API Preview vs Studio Official. Accessed 2026-10-21, update 2026-10-10. | VERIFIED | T02, T07 | TR-07, TR-09 |
| CW-02 | 528 | Keep the API multiview contract: front required; 2-4 actual views; legacy 4 slots. | VERIFIED | T04, T29 | TR-21 |
| CW-03 | 529 | Do not use generator maxima as phone budgets: H standard 1,500,000, H detailed 2,000,000 are ceilings only. | VERIFIED/OPINION | T01 | TR-05, TR-06 |
| CW-04 | 530 | Select latest processing explicitly if wanted: retopology v3.0 (default v2.0); texture v3.5 (default v3.0). 2026-09/10. | VERIFIED | T03, T12, T14 | TR-14, TR-15, TR-44 |
| CW-05 | 531 | Reduce before standalone Smart UV: 80,000 equivalent triangles maximum. | VERIFIED | T13 | TR-42 |
| CW-06 | 532 | Keep API and Studio credits apart: API 1 credit = $0.01; Studio conversion not assumed. | VERIFIED/OPINION | T16, T17 | CL-01, CL-05 |
| CW-07 | 533 | Do not infer deformation from quad count; no universal pass rate verified. 2026-10-14, 2026-09-29. | OPINION/EXPERIENCE | T20, T25 | TR-29, TR-33 |
| CW-08 | 534 | No fabricated hero-quality or cleanup ranking; unknown across the user's assets. | OPINION | P00 | TR-35, TR-36 |
| CW-09 | 563 | Separate rigid articulation from skin deformation: no compulsory universal object count. | VERIFIED/OPINION | B28, B29 | RG-01, RG-02 |
| CW-10 | 564 | Loose parts is not semantic segmentation: it only separates disconnected components. | VERIFIED | B13 | RG-04 |
| CW-11 | 565 | General skin weights obey the platform limit: at most 4 influences per vertex. | VERIFIED | B31 | RG-07 |
| CW-12 | 566 | Do not apply armature transforms late as an automatic fix: scale 1, 1, 1 is not zero. | VERIFIED | B18, B31 | RG-07 |
| CW-13 | 603 | General rendering ceiling, not a phone target: 4096x4096; 8K stored sources may be transcoded. 2026-01-30. | VERIFIED | R03 | TX-04 |
| CW-14 | 604 | Size-based starting guidance: 5x5 -> 256x256; 10x10 -> 512x512; 20x20 -> 1024x1024. | VERIFIED | R02 | TX-08 |
| CW-15 | 605 | General mesh: 1 material, 1 UV set, 0-1 UV space. | VERIFIED | R02 | TX-08 |
| CW-16 | 606 | Low-end Android texture-streaming matrix: below 3.5 GB, 4K disabled. 2026-03-23 update. | VERIFIED | R04 | TX-06 |
| CW-17 | 607 | Example maps need not match resolution: normal 1024; color 512; roughness 256; no metalness. | EXPERIENCE | R12 | TX-12 |
| CW-18 | 608 | Emissive input: 1 channel; an RGB input uses red. 2026-02-12. | VERIFIED | R09 | TX-16 |
| CW-19 | 609 | Marketplace emissive strength constraint: 0-40. 2026-09-02. | VERIFIED | R34 | TX-16 |
| CW-20 | 704 | Generic individual mesh ceiling: 20,000 triangles. | VERIFIED | R01 | BG-01 |
| CW-21 | 705 | Marketplace character body ceiling: 10,742 across specified groups. | VERIFIED | R05 | BG-03 |
| CW-22 | 706 | Layered clothing ceiling: 4,000 triangles per accessory. | VERIFIED | R06 | BG-03 |
| CW-23 | 707 | Collision choices include Tunable: five choices; cost is measured in context. 2026-09-17. | VERIFIED | R07, R08 | BG-40 |
| CW-24 | 708 | New mesh streaming overrides per-mesh fidelity; legacy 250/500 stud thresholds are conditional. 2026-04-27. | VERIFIED | R14, R07 | BG-31, BG-32 |
| CW-25 | 709 | Triangle and draw-call analysis: Sizes.Triangles and Sizes.Drawcalls by pass. | VERIFIED | R27 | BG-43 |
| CW-26 | 710 | Per-type phone budgets: UNKNOWN until project-set and measured. 2026-10-21. | OPINION | P00 | BG-04 to BG-12 |

## 10. Section 6: building for the rigger and animator (MP:536-560)

Link to the fixed rig split: animator says what moves; rigger says which parts are separate and where cuts go; modeler makes the cuts, seam clean-up and re-modelling (J005-D1). Rig method is chosen per joint (J005-D9). The paper agrees that the representation is a per-joint choice.

| ID | MP | Lesson | Tag | Src | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- |
| RG-01 | 538 | Roblox supports rigged meshes and workflows with multiple meshes. | VERIFIED | B28, B29 | S2 | [for-rigger] |
| RG-02 | 538 | "Every moving part is a separate object" is false as a universal rule. A skinned continuous body can bend under bones; a rigid hinged door needs motion independent of its frame. Choose the representation with the rigger before topology and UV work. The question is where relative motion or deformation happens, not how many object names exist. | OPINION | P00 | S2, S3 | [for-rigger] [for-animator] |
| RG-03 | 540 | Organic skin: put useful edge flow around shoulder/hip transitions, elbow/knee bends, neck, and mouth/eyelids when needed. Test the real intended extremes. No fixed count of joint loops is a universal quality rule. Concentrate topology where bending and silhouette change need it; thin out flat low-importance regions; keep poles and long thin triangles away from sensitive bends when possible. Quads help editable flow, but exported triangles still need evaluation. A static hero pose is not evidence of deformation quality. | OPINION | P00 | S3, S4 | [for-rigger] [for-animator] |
| RG-04 | 542 | Separate by Loose Parts only splits disconnected geometry; it cannot anatomically segment a truly fused generated mesh. Separate by Selection moves selected geometry to another object. | VERIFIED | B13 | S3 | [for-rigger] |
| RG-05 | 542 | Bisect cuts with a defined plane. Fill can cap cleared cuts and takes material, UV and colour from the surroundings. | VERIFIED | B14 | S3 | [for-rigger] |
| RG-06 | 542 | For a merged Tripo mesh, first map the intended moving parts and class each boundary: skin-continuous, rigid overlap, hinge, detachable, or replaceable. Cut only the rigid separation regions. Rebuild missing hidden geometry and repair UVs after cutting. A flat cap is a construction result, not a convincing shoulder socket. For continuous skin, retopologize and skin; do not cut every limb off. If a hand is fused to a weapon, rebuild hand and grip and remove the bridge so the tool can detach or switch. | OPINION | P00 | S2, S3 | [for-rigger] |
| RG-07 | 544 | Object origins govern object transforms; "center of mass" assumes uniform density (B17). Apply transforms before rigging and animation when possible; applying armature transforms does not rewrite pose locations, animation curves or constraints (B18). General Roblox skinning: at most 4 bone influences per vertex; root at 0, 0, 0; no root influences; frozen transforms with scale 1, 1, 1 and rotation 0, 0, 0 (B31). | VERIFIED | B17, B18, B31 | S3, S5 | [for-rigger] |
| RG-08 | 544 | The skeleton rules are not an instruction to move every rigid object's hinge origin to world origin. Document root, object pivots, bone rest space and attachment frames separately. | OPINION | P00 | S2, S3, S5 | [for-rigger] [for-animator] |

Parts-for-animation table (MP:546-558). Paper rule (MP:548): the table lists independent control needs, not compulsory mesh-object separation. Tag and Src of every row: OPINION, P00 (tool evidence B13-B14, B17-B18, B28-B31).

| ID | MP | Model type | Independently controllable parts (not always separate meshes) | Where to cut if using rigid parts | How to hide the seam, or the alternative | Who | Tag | Src |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RG-09 | 551 | Organic humanoid | Jaw, eyes, tools when their motion needs it; body can be one continuous skinned mesh | Only designed clothing/armor or rigid joint boundaries | Collar/sleeve overlap, or skin-continuous deforming topology; test full neck and shoulder range | [for-rigger] [for-animator] | OPINION | P00 |
| RG-10 | 552 | Toy/block humanoid | Head, torso, limb segments under the chosen rigid articulation | At designed toy joints | Ball/socket, collar/cuff, or an approved stylized gap; overlap through the full range | [for-rigger] [for-animator] | OPINION | P00 |
| RG-11 | 553 | Quadruped pet | Jaw, ears, tail, legs need motion controls; skin may stay continuous | Only a rigid/fur-layer transition if the representation calls for it | Overlapping fur clumps, or continuous skinned shoulder, hip and tail base | [for-rigger] [for-animator] | OPINION | P00 |
| RG-12 | 554 | Winged creature | Wing membrane/feathers and tail, per the fold plan | Rigid feathers may separate; avoid arbitrary membrane cuts | Continuous membrane topology, or overlapping feather layers; check fold extremes | [for-rigger] [for-animator] | OPINION | P00 |
| RG-13 | 555 | Weapon/tool | Detachable tool plus trigger, bolt, magazine, hinge parts when animated | Along real assembly seams | Mechanical housings, rails, sleeves; keep the grip/socket constant | [for-rigger] [for-animator] | OPINION | P00 |
| RG-14 | 556 | Vehicle | Wheels, steering, doors, suspension, turret as the motion needs | At axles, hinges, panel joints | Fenders, bearings, panel gaps; keep collision surfaces from blocking travel | [for-rigger] [for-environment] | OPINION | P00 |
| RG-15 | 557 | Building/prop | Doors, shutters, drawers, levers or destruction chunks only as needed | At meaningful hinges, slides, material construction joints | Frames, reveals, trim; collision must leave the intended opening | [for-environment] [for-rigger] | OPINION | P00 |
| RG-16 | 558 | Soft cape/tail/tentacle | Continuous deformation controls, not compulsory rigid cuts | No cut if the surface should flex continuously | Skinning and topology at the attachment; keep enough cross-sections for bends | [for-rigger] [for-animator] | OPINION | P00 |

| ID | MP | Lesson | Tag | Src | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- |
| RG-17 | 560 | The shared rig requirements sheet should state: semantic parts, local axes, rest pose, required motion range, attachment frames, contact surfaces, silhouette priority, rigid or skinned choice, topology ownership, collision needs, export category. | OPINION | P00 | S0, S1, S2 | [for-rigger] [for-animator] |
| RG-18 | 560 | Paper role split: animator proposes poses and ranges; rigger defines controls and deformation needs; modeler proposes economical construction and flags impossible intersections; art director checks style; owner decides trade-offs. (See gap X-04 for the owner's rig split.) | OPINION | P00 | S1, S2, S3 | [for-rigger] [for-animator] [for-art-director] |
| RG-19 | 560 | Joint limits and seam overlap distances left unspecified are project decisions. The paper gives no constants and warns against inventing them. | OPINION | P00 | S1, S2 | [for-rigger] [for-animator] |

## 11. Section 7: textures and materials (MP:568-598)

| ID | MP | Lesson | Tag | Src | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- |
| TX-01 | 570 | UV packing can keep pinned island transforms and reserve a custom region for atlas or trim layouts. | VERIFIED | B16 | S3 | - |
| TX-02 | 570 | Keep intentional texel-density differences for focal areas; equal density is not always the art goal. Set target density only after camera distance, resolution and texture budget are known. Report no single pixels-per-stud or pixels-per-meter rule. Shared atlas: reserve named regions and coordinate revisions so one asset's repack does not corrupt others. UV seams are not physical cuts; the mesh can stay connected while UVs split. | OPINION | P00 | S3 | [for-art-director] [for-rigger] |
| TX-03 | 570 | UV data is stored per loop (corner), which supports the seam-versus-cut point. | VERIFIED | B09 | S3 | - |
| TX-04 | 574 | General experience texture rendering supports up to 4096x4096 (R02, accessed 2026-10-21). January 2026 release (R03, 2026-01-30): image assets up to 8K can be imported and kept at original quality; runtime transcodes down to 4K. The R02 page contradicts itself: its UV section still gives a 1024x1024 maximum. Marketplace assets have separate limits. | VERIFIED | R02, R03 | S3 | [for-art-director] |
| TX-05 | 574 | Not permission to promise an 8K runtime texture, nor that every device shows 4K. Prefer the specific dated runtime release over the contradictory general page. | OPINION* | R02, R03, P00 | S3 | [for-art-director] |
| TX-06 | 576 | Texture streaming (R04, 2025-12-12, status 2026-03-23) picks mip detail by scene importance and available device memory. Support matrix: 4K disabled for low-end Android below 3.5 GB. Labels are > 3.5 GB and < 3.5 GB; exactly 3.5 GB is not specified. Matrix lists UI, SurfaceGUI, Terrain, TerrainDetail and Sky among not-yet-supported categories. | VERIFIED | R04 | S3 | [for-ui] [for-environment] [for-art-director] |
| TX-07 | 576 | Do not generalize the unsupported classes to future releases. Texture streaming is not Workspace instance streaming. Check the current feature status when UI, Terrain or Sky assets enter the project. | OPINION* | R04, P00 | - | [for-ui] [for-environment] |
| TX-08 | 578 | General texture-size guidance (R02): 256x256 for a 5x5 stud object, 512x512 for 10x10, 1024x1024 for 20x20. A mesh has one assigned material; PBR maps are channels of that material, not separate material slots. The general UV spec needs one UV set, coordinates in 0-1, and allows overlap. | VERIFIED | R02 | S3 | [for-art-director] |
| TX-09 | 578 | These sizes are starting guidelines, not per-character budgets. Record per asset in the manifest: authored resolution, expected visible size, reuse count, measured residency, not one "texture cost" number. | OPINION* | R02, P00 | S3 | - |
| TX-10 | 582 | A MeshPart can use TextureID or a SurfaceAppearance. With both SurfaceAppearance and MaterialVariant, SurfaceAppearance gives the texture maps and non-texture MaterialVariant settings (incl. physical properties) still apply. The older "up to four PBR textures" line on the meshes page is incomplete after the emissive-mask release (R07). MaterialVariant sits under MaterialService, can override a base material or be chosen per BasePart; StudsPerTile sets tile scale; it can change density, friction, elasticity via CustomPhysicalProperties (R11). | VERIFIED | R07, R11 | S3 | [for-environment] |
| TX-11 | 582 | Modelers may propose reusable tile materials. Physics-affecting material changes need gameplay/physics review; painted wood must not silently change vehicle friction. | OPINION | P00 | S3 | [for-environment] |
| TX-12 | 584 | Duvall Drive leather-trim example (Roblox production case, undated): normal map 1024, base color 512, roughness 256, no metalness map. A concrete channel-specific allocation, not a mobile universal; maps need not share one resolution. | EXPERIENCE | R12 | S3 | [for-art-director] |
| TX-13 | 584 | Use unique painted maps for identity-critical forms, tiled variants for repeatable surfaces, trim/atlas sheets for reusable families. Judge the final in-game image, not whether every asset uses PBR. Baking broad gradients or highlights can support a style and can also bake an unwanted light direction; that trade-off is the art director's. | OPINION | P00 | S3 | [for-art-director] [for-environment] |
| TX-14 | 586 | SurfaceAppearance.Color multiplies ColorMap, not MeshPart.Color; near-white grayscale gives a stronger tint range. Overlay alpha shows MeshPart.Color beneath; TintMask alpha controls how much SurfaceAppearance tint applies. Docs say tinting adds no performance cost and lets one color map be reused (an engine documentation statement, not a benchmark). | VERIFIED | R10 | S3 | [for-vfx] [for-art-director] |
| TX-15 | 586 | Reuse tintable maps for palette variation instead of a unique texture per colour. Keep RGB in transparent regions when using a tint mask. Check rendered results; do not assume Blender shader nodes transfer intact. | OPINION | P00 | S3 | [for-art-director] |
| TX-16 | 588 | Emissive masks (R09, 2026-02-12) are live in published clients. They are intensity masks, not independent RGB maps; with an RGB(A) mask only red is used. Emissive hue comes from existing colour data and EmissiveTint. Marketplace emissive items (R34, 2026-09-02): strength 0-40, MeshPart-based accessories; a generated legacy accessory has no emissive support. | VERIFIED | R09, R34 | S3 | [for-vfx] [for-art-director] |
| TX-17 | 588 | Store emission as a deliberate glow hierarchy, not as a stand-in for readable base values. An emissive surface does not imply emitted scene light. | OPINION | P00 | S3 | [for-vfx] [for-environment] |
| TX-18 | 590 | Normal maps use OpenGL tangent space; object-space and world-space normals are unsupported. Tangents must be exported. A reversed green channel can invert the bumps (R11). | VERIFIED | R11 | S3 | [for-art-director] |
| TX-19 | 590 | Recent report (R36, 2026-10-19): SurfaceAppearance ColorMap looks darker than TextureID, and an unset roughness map looks glossy. No resolution or reproduced root cause was verified. | EXPERIENCE | R36 | S3 | - |
| TX-20 | 590 | Treat that report as an import-review test case, not a proven universal colour transform and not a reason to auto-brighten every texture. | OPINION | P00 | S3 | [for-art-director] |
| TX-21 | 594 | The FBX/glTF importer supports vertex colours (R20). | VERIFIED | R20 | S3 | - |
| TX-22 | 594 | Forum replies on Marketplace colour inconsistencies: R31 (reply 2026-06-23) and R32 (reply 2026-05-26) say renderers handled vertex colours differently and new UGC validation prevents them; one reply says old affected items would not be fixed. Marketplace-specific, not proof that experience MeshParts cannot use vertex colours. Tagged EXPERIENCE because staff-badge verification was not captured. | EXPERIENCE | R31, R32 | S3 | [for-art-director] |
| TX-23 | 594 | For authored experience vertex-colour art: import only the intended colour layer and check in published gameplay. For Marketplace: do not ship hidden authoring masks. Per-vertex mesh colour is not the same as the SpecialMesh.VertexColor global multiplier. | OPINION | P00 | S3 | [for-art-director] |
| TX-24 | 598 | Roblox Quality Texture Generation beta (R35, 2026-10-16) advertises 4K PBR colour/roughness/metalness in about 2 minutes, versus Fast: 1K colour-only in about 30 seconds. Vendor estimates, not measured throughput. No alpha support. It does not know Assistant chat history or surrounding game context. | VERIFIED | R35 | S3 | [for-art-director] |
| TX-25 | 598 | Supplemental finishing option only; not a replacement for the ChatGPT-reference-first workflow. Texture generation cannot fix a missing silhouette or fused articulation. | OPINION | P00 | S3 | [for-art-director] |

## 12. Section 8: Roblox optimization and measured budgets (MP:611-679)

### 12.1 Ceilings (MP:613-617)

| ID | MP | Lesson | Tag | Src | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- |
| BG-01 | 615 | Generic individual mesh: at most 20,000 triangles. General guidelines also need volume/watertight geometry, no exposed holes or backfaces, quads where possible rather than n-gons, at most 4 bone influences per vertex. These are compatibility guidelines. Accessed 2026-10-21. Owner budget: this 20,000 is only the upload ceiling; creatures and characters stay under about 7,000 triangles (J007-D5). | VERIFIED | R01 | S2, S3 | [for-rigger] |
| BG-02 | 615 | A 20,000-triangle pet is not proven affordable when 100 are visible. Count the triangulated, evaluated mesh after modifiers and export, not source quads. Do not split a heavy model into many 20,000-triangle pieces just to pass upload. | OPINION* | R01, P00 | S3, S4 | [for-rigger] |
| BG-03 | 617 | Marketplace character bodies: 15 mesh objects in 6 assets: DynamicHead 4,000; Torso 1,750; each arm 1,248; each leg 1,248; total 10,742 triangles. Body textures capped at 2048x2048 (R05). Layered clothing: 4,000 triangles per accessory, a single mesh, plus its own cage and size rules (R06). Accessed 2026-10-21. Avatar body requirements, not custom NPC budgets. | VERIFIED | R05, R06 | S2 | [for-rigger] |
| BG-03a | 617 | Pick the asset category first; "the Roblox model limit" is not one number. | OPINION | P00 | S2 | [for-rigger] |

### 12.2 Budget table for the eight types (MP:619-633)

MP:621: no reviewed source gives a universal low-end-phone triangle budget, a universal unique-material count per model type, or a scene-wide maximum of unique meshes or textures. UNKNOWN means a project measurement must supply it, not that no limit exists. Ceilings must not be copied into content targets. Collision choices are OPINION built on R07/R08/R13.

| ID | MP | Type | Triangle budget | Texture size | Unique materials | Collision (OPINION) | Source | Tag | Who |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BG-04 | 624 | Player character | Mobile target UNKNOWN. Ceilings (VERIFIED): Marketplace body 10,742 across the specified parts; generic experience mesh 20,000 each | Mobile target UNKNOWN. Marketplace body max 2048x2048; general size guidance is separate | UNKNOWN per character; 1 per mesh assignment | Approved movement/hit proxies; do not collide all visual detail | R01, R05 (VERIFIED); collision OPINION | UNKNOWN (budgets); VERIFIED (20,000 ceiling); OPINION (collision) | [for-rigger] |
| BG-05 | 625 | NPC | UNKNOWN mobile target; 20,000 per generic mesh ceiling | UNKNOWN; choose from footprint and visible importance | UNKNOWN per NPC; 1 per mesh | Movement/hit proxies or simple hull/boxes if required | R01, R02; OPINION | UNKNOWN (budgets); VERIFIED (20,000 ceiling); OPINION (collision) | [for-rigger] |
| BG-06 | 626 | Pet | UNKNOWN; 20,000 per generic mesh ceiling | UNKNOWN; do not promote all pets to 4K | UNKNOWN; reuse a material family where fitting | No physical collision if decorative; otherwise an approved simple proxy | R01, R02, R13; OPINION | UNKNOWN (budgets); VERIFIED (20,000 ceiling); OPINION (collision) | [for-rigger] |
| BG-07 | 627 | Weapon/tool | UNKNOWN; 20,000 per generic mesh ceiling | UNKNOWN; first-person screen size may differ from world version | UNKNOWN; 1 per mesh | Gameplay hit query/proxy separate from the decorative mesh | R01, R02; OPINION | UNKNOWN (budgets); VERIFIED (20,000 ceiling); OPINION (collision) | [for-rigger] [for-animator] |
| BG-08 | 628 | Small prop | UNKNOWN; 20,000 per generic mesh ceiling | 256x256 only if comparable to the official 5x5 stud guideline; not a category rule | UNKNOWN; prefer reuse when art permits | Box for small anchored objects where bounds suffice | R01, R02, R13 | UNKNOWN (budgets); VERIFIED (20,000 ceiling); OPINION (collision) | [for-environment] |
| BG-09 | 629 | Large prop | UNKNOWN; 20,000 per generic mesh ceiling | 512x512 at 10x10 or 1024x1024 at 20x20 are guidance, not guarantees | UNKNOWN | Hull/boxes or Tunable only as precision requires | R01, R02, R08; OPINION | UNKNOWN (budgets); VERIFIED (20,000 ceiling); OPINION (collision) | [for-environment] |
| BG-10 | 630 | Building | UNKNOWN total; 20,000 per generic mesh ceiling | UNKNOWN; tile/trim/reuse by view | UNKNOWN; share a kit palette | Simple separate floor/wall proxies that keep doors and windows | R01, R11, R13; OPINION | UNKNOWN (budgets); VERIFIED (20,000 ceiling); OPINION (collision) | [for-environment] |
| BG-11 | 631 | Environment piece | UNKNOWN; 20,000 per generic mesh ceiling | UNKNOWN; size guidance, visible detail and reuse decide the trial | UNKNOWN | None for purely decorative; simple interaction proxy otherwise | R01, R02, R13; OPINION | UNKNOWN (budgets); VERIFIED (20,000 ceiling); OPINION (collision) | [for-environment] |
| BG-12 | 621 | All eight types | No universal low-end-phone triangle budget, unique-material count per type, or scene-wide unique mesh/texture maximum is established by the sources reviewed. | | | | P00 | UNKNOWN | |

BG-12 tag: UNKNOWN. Budget cells marked UNKNOWN in BG-04 to BG-11 stay UNKNOWN. The "20,000 per mesh" cells carry VERIFIED R01 (ceiling only). Collision cells carry OPINION.

### 12.3 Turning unknown budgets into a measured allocation (MP:633-657)

| ID | MP | Lesson | Tag | Src | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- |
| BG-13 | 633 | Turn UNKNOWN into an approved project budget by recording: target handset, graphics level, game camera, concurrency, populated map, streaming state, memory and frame-time capture, acceptance threshold. Owner or art director can approve trial targets; they stay project choices until measured. A model's isolated cost does not predict its crowded-scene cost. Disk cost of a texture is not decoded resident memory. | OPINION | P00 | S2, S8 | [for-art-director] |
| BG-14 | 637 | Keep three records apart: (1) compatibility record: sourced hard limits for the real asset category; (2) comparison record: scoped examples from other productions (Duvall Drive map allocation, Dota item-slot specs); (3) project allocation record: numbers the studio chooses and measures for its own camera, devices and scene. Do not promote a ceiling or comparison into a budget. | OPINION | P00 | S2 | [for-rigger] |
| BG-15 | 639 | Method: start from a representative playable scene with approved cheap placeholders; take the maximum visible population per role from game design; record a baseline with lighting, effects and gameplay on; swap one asset family cohort for the candidate, other variables fixed; capture render passes, memory and frame work; then test the full mixed scene (isolated deltas do not necessarily add up, because batching, streaming, shadows and visibility change with composition). | OPINION | P00 | S5, S8 | [for-environment] |
| BG-16 | 641 | An allocation is a tested content envelope, not only a triangle maximum: evaluated triangles, unique mesh resources, repeated instances, texture maps and sizes, material identities, transparency, shadows, collision representation, animation when present, typical on-screen size. Equal triangle counts do not equal equal frame work. Test both a camera's visible subset and the full imported asset. | OPINION | P00 | S2, S5 | [for-rigger] |
| BG-17 | 643 | When a candidate fails, find the measured bottleneck first. Options: material/texture reuse, remove invisible interior geometry, simplify distant silhouettes, reduce shadow participation where design permits, cheaper collision proxies, narrower visibility populations. Keep approved visual identity and interaction. Fewer triangles only help if they improve the relevant outcome without breaking those. | OPINION | P00 | S3, S5 | [for-rigger] [for-environment] |
| BG-18 | 645 | Approve a trial allocation with the performance owner and art director and record its measured status. A new device tier, graphics setting, camera or crowd size can void the envelope; rerun representative scenes when the family changes. Do not ask the owner to approve every topology edit inside an accepted budget; escalate changes to style, function, visibility assumptions or the budget itself. | OPINION | P00 | S2, S8 | [for-art-director] |

Allocation record fields (table MP:647-657, header at 647). Every field row: tag OPINION (the paper's proposed record), Src P00. The last column is the paper's own status label.

| ID | MP | Field | Required value | Tag | Src | Paper status label |
| --- | --- | --- | --- | --- | --- | --- |
| BG-AR1 | 648 | Asset family and revision | Player, NPC, pet, tool, prop, building or environment family plus version | OPINION | P00 | Project data |
| BG-AR2 | 649 | Scene and camera | Place revision, visible population, camera distance, screen coverage | OPINION | P00 | Project data |
| BG-AR3 | 650 | Device and runtime | Named handset, OS/client build, graphics level, thermal conditions | OPINION | P00 | Measured context |
| BG-AR4 | 651 | Compatibility ceiling | Exact category rule and source date | OPINION | P00 | VERIFIED source |
| BG-AR5 | 652 | Proposed content limits | Triangles, instances, unique resources, maps, collisions | OPINION | P00 | OPINION until tested |
| BG-AR6 | 653 | Baseline and candidate captures | Same scene before and after cohort replacement | OPINION | P00 | Measurement artifact |
| BG-AR7 | 654 | Frame and memory result | Recorded distributions/spikes and relevant memory categories | OPINION | P00 | Measured result |
| BG-AR8 | 655 | Visual and interaction pass | Matched renders, motion and collision checks | OPINION | P00 | Approved project evidence |
| BG-AR9 | 656 | Accepted envelope | Limits plus the conditions under which they passed | OPINION | P00 | Scoped project result |
| BG-AR10 | 657 | Owner and exceptions | Responsible approver, rationale, next recheck trigger | OPINION | P00 | Project decision |

### 12.4 Reuse, batching, streaming, collision, tools (MP:659-679)

| ID | MP | Lesson | Tag | Src | Stage | Who |
| --- | --- | --- | --- | --- | --- | --- |
| BG-29 | 661 | The engine batches meshes with the same MeshContent when SurfaceAppearances match; without SurfaceAppearances when TextureContents match; if neither exists, materials must match. Reimporting identical geometry under different IDs defeats this identity test. Upload reusable assets once, duplicate in Studio, use packages for reuse. Render Stats shows draw calls; client shortcut Shift + F2. | VERIFIED | R13 | S3 | [for-environment] |
| BG-30 | 661 | An atlas can cut unique texture assets without collapsing different geometry into one draw call. Keep a manifest of canonical mesh and material IDs. Do not merge a whole city; visual grouping, independent movement, collision, culling and streaming granularity must survive. Measure the repeated scene, not one prop. | OPINION | P00 | S3, S5 | [for-environment] |
| BG-31 | 665 | MeshStreamingAndImprovedLoDs (R14, 2026-04-27) enables cloud-generated mesh LoDs, importance-based selection and a mesh memory budget, independent of Workspace.StreamingEnabled. When on, it ignores every MeshPart.RenderFidelity setting. The announcement planned phased rollout with default behaviour around July 2026; a forecast does not prove phase 3 shipped. | VERIFIED | R14 | S5 | [for-environment] |
| BG-32 | 665 | General mesh page (R07, accessed 2026-10-21) still describes Automatic: below 250 studs highest, 250-500 studs medium, 500 studs and above lowest. That is legacy behaviour, not a guarantee under the new streaming system. | VERIFIED | R07 | S5 | [for-environment] |
| BG-33 | 665 | Record the actual workspace flag and screenshots in every profiling result. Do not prescribe Precise as a universal fix when the active system ignores it. | OPINION | P00 | S5 | [for-environment] |
| BG-34 | 667 | The mesh-streaming rollout (R15, 2026-03-16, update 2026-06-17) excludes skinned meshes and does not change collision geometry (a separate blob). Do not infer animated custom character support from static mesh LoD support. | VERIFIED | R15 | S2, S5 | [for-rigger] [for-animator] |
| BG-35 | 667 | SLIM (R17, 2025-10-30, updates through 2026-02-25) composites model representations with instance streaming; the platform-avatar extension (R18, 2026-05-12) supports R15 avatars. Not the same as per-asset mesh streaming. | VERIFIED | R17, R18 | - | [for-environment] |
| BG-36 | 667 | New debug tints (R19, 2026-10-09) show streaming state, LoD and transcoder state: Studio visualization modes (Studio beta) and F9 developer-console visualizations in Player. | VERIFIED | R19 | S5 | [for-environment] |
| BG-37 | 667 | Confirm a model really receives its lightweight representation before claiming an optimization. | OPINION | P00 | S5 | [for-environment] |
| BG-38 | 669 | Production report (R16, response 2026-09-04): meshes stuck at lowest LoD; a responding account said an interfering feature was rolled back. One reported incident and fix, not evidence all mesh streaming is broken or cured. | EXPERIENCE | R16 | - | - |
| BG-39 | 669 | Take close-up and moving-camera screenshots on the weakest supported device. Inspect silhouette-critical weapons, holes and thin pieces after cloud simplification. A passing source mesh is not a passing streamed image. | OPINION | P00 | S5 | [for-environment] |
| BG-40 | 673 | Collision choices: Box, Hull, Default, PreciseConvexDecomposition and now Tunable (R07 accessed 2026-10-21; R08 2026-09-17). Box = bounding box; Hull = convex; Default approximates concavity; Precise costs more and is still not an exact visual match; Tunable exposes CollisionPrecision to trade accuracy for cost, with default precision chosen by mesh size, not one constant. | VERIFIED | R07, R08 | S5 | [for-environment] [for-rigger] |
| BG-41 | 673 | Review collision visualization with character traversal and projectile cases. A detailed hollow visual should not get expensive decomposed collision by default. Prefer a small explicit proxy assembly when it makes interaction predictable, and measure proxy count too. Keep visual/physical mismatch intentional: no invisible blocked doorways; decorative bevels need not collide. | OPINION | P00 | S5 | [for-environment] |
| BG-42 | 677 | Scene Analysis: Window > Performance Summary > Scene Analysis, for play/test sessions (R25 accessed 2026-10-21; full release R26 2026-07-10). Triangle composition separates render passes (opaque, transparent, shadows). Studio counts can differ greatly from a phone because scaling differs. | VERIFIED | R25, R26 | S5 | [for-environment] |
| BG-43 | 677 | SceneAnalysisService:GetTriangleCompositionAsync returns a tree with Sizes.Triangles and Sizes.Drawcalls by pass, not one Size field; exposed through the Studio MCP per the guide (R27). Its memory methods cover script, audio and animation, not per-model GPU textures; do not invent texture-memory methods. | VERIFIED | R27 | S5 | [for-environment] |
| BG-44 | 679 | MicroProfiler (R28/R29, accessed 2026-10-21) splits frame work into timings and supports captures in Studio and live client. Client and server profiles answer different questions because rendering is client-side. Frame time to FPS: 1000 / FPS milliseconds; this does not pick a required framerate. | VERIFIED | R28, R29 | S5 | [for-environment] |
| BG-45 | 679 | For each model revision archive: dimensions, triangulated mesh count, texture-map sizes and IDs, material count, render-pass deltas with/without the asset cohort, client memory categories, frame-time captures, collision visualization. Compare warm loading and first appearance separately. A phone-shaped Studio viewport is not a measured phone GPU. | OPINION | P00 | S5 | [for-environment] |

## 13. Numbered optimization checklist (MP:681-701)

| ID | MP | Item (paraphrase) | Tag | Src |
| --- | --- | --- | --- | --- |
| CK-01 | 683 | Each generic imported mesh is at most 20,000 triangles. | VERIFIED | R01 |
| CK-01a | 683 | Also meet the independently approved scene/asset target; that threshold stays UNKNOWN until set. | OPINION | P00 |
| CK-02 | 685 | Use category-specific limits only where they apply: body 10,742 total with per-part groups; layered accessory 4,000. | VERIFIED | R05, R06 |
| CK-03 | 687 | One UV set and one material assignment per mesh; UVs in 0-1. | VERIFIED | R02 |
| CK-04 | 689 | Skinned vertices have at most 4 influences; this is not an optimal bone count. | VERIFIED | R01 |
| CK-05 | 691 | Record authored sizes; official examples 256x256, 512x512, 1024x1024 match 5x5, 10x10, 20x20 stud sizes. | VERIFIED | R02 |
| CK-06 | 693 | 4K is a supported top mip, not guaranteed residency; the low-end Android matrix disables 4K below 3.5 GB. | VERIFIED | R03, R04 |
| CK-07 | 695 | Identical mesh and texture characteristics can batch into 1 draw call; no guarantee for different meshes. | VERIFIED | R13 |
| CK-08 | 697 | Inspect the chosen option among 5 collision fidelities; no published fixed milliseconds-per-hull budget was found. | VERIFIED | R08 |
| CK-09 | 699 | New mesh streaming ignores per-mesh RenderFidelity; legacy 250/500 stud thresholds are conditional. | VERIFIED | R14 |
| CK-10 | 701 | Capture triangles and draw calls by pass. | VERIFIED | R25, R27 |
| CK-10a | 701 | Pass only on the project's measured target devices; scene and unique-asset maxima UNKNOWN. | OPINION | P00 |

## 14. Claims to fact-check

Numbered list. Domain: Roblox, Blender, Tripo, other. Every claim is the paper's, unverified here. Tripo, Blender and Roblox items are the likeliest to be wrong or stale (paper cutoff 2026-10-21).

| No | MP | Domain | Exact claim (paraphrase, numbers kept) | Paper src |
| --- | --- | --- | --- | --- |
| 1 | 427 | Tripo | Tripo Studio "Best Quality" = HD Model = H Series; "Clean Topology" = Smart Mesh = P Series | T27 |
| 2 | 428 | Tripo | H3.1 snapshot is v3.1-20260211 (shown as Default) | T01 |
| 3 | 428 | Tripo | H3.1 documented triangle ceiling 1,500,000 (standard) and 2,000,000 (detailed) | T01 |
| 4 | 428 | Tripo | H3.1 quad option forces FBX; omitted quad face limit gives 10,000 faces | T01 |
| 5 | 431 | Tripo | API card marks P2-20260801 as Preview and P1-20260311 as previous stable | T02 |
| 6 | 431 | Tripo | Studio's September update says P2 officially launched; blog index date 2026-10-10 | T07 |
| 7 | 431 | Tripo | Studio announcement: 500-50,000 triangle faces or 500-25,000 quad faces | T06 |
| 8 | 431 | Tripo | API accepts 48-50,000 triangles or 48-25,000 quads | T02 |
| 9 | 431 | Tripo | P2 supports quad output; P1 does not | T02, T06 |
| 10 | 436 | Tripo | H3.1 supports text/image/multiview and independent texture options | T01 |
| 11 | 437 | Tripo | P2 API: triangles or quads; text/image/multiview; no smart_low_poly, generate_parts, geometry_quality parameters | T02 |
| 12 | 438 | Tripo | P2 Studio: native quad, independent parts, regional Mesh Edit, up to four different-polycount variants on eligible plans | T06, T07 |
| 13 | 439 | Tripo | Segmentation v2.0-20260430 is Beta (semantic + geometry); default v1.0-20250506 is geometry only | T11 |
| 14 | 440 | Tripo | Retopology v3.0 introduced October 2026; default stays v2.0; endpoint /mesh/decimate | T03, T12 |
| 15 | 441 | Tripo | Texture v3.5-20260815 added September 2026; selected by texture_version; default v3.0 (see 472) | T03, T14 |
| 16 | 442 | Tripo | Smart UV /mesh/uv re-unwraps and remaps and returns a UV atlas preview | T13 |
| 17 | 448 | Tripo | Tripo help: subject 70-85% of image, at least 1024x1024 for quality, even background, diffuse light | T08 |
| 18 | 448 | Tripo | Tripo multiview help: views must match in pose, scale, lighting, background, design | T09 |
| 19 | 450 | Tripo | v3 API: named view keys (front/left/back/right) or exactly four legacy positional slots in order front, left, back, right | T04, T05, T29 |
| 20 | 450 | Tripo | v3 multiview: front required, at least two real images; empty slots allowed for missing positional views | T04, T05, T29 |
| 21 | 450 | Tripo | v3 accepts PNG/JPEG/WebP and recommends at least 256x256 | T04 |
| 22 | 450 | Tripo | v2 docs use files/model_version; JPEG/PNG URL input up to 20 MB | T05 |
| 23 | 450 | Tripo | Studio tutorials discuss front/side/back view order loosely (no source given) | none cited (T04, T05, T29 in paragraph) |
| 24 | 454 | Tripo | Studio generates multiview images from one image and cuts images into 1-10 transparent PNGs (Cutout) | T10 |
| 25 | 454 | Tripo | Tripo states unseen surfaces in generated multiview images are inferred | T28 |
| 26 | 458 | Tripo | Tripo's P2 workflow post (2026-10-14) covers regional repair, UVs, textures, rigging, Unreal preview of one semi-anime fantasy girl | T20 |
| 27 | 460 | other | Nexus (2026-07-15) reports geometry/texture ambiguity, missing faces, resolution/grid artifacts, normal-orientation inconsistencies; some authors tied to VAST | T21 |
| 28 | 462 | other | Digital Production review (2026-09-29) separates quad count from pole placement, loops and deformation; no reproducible asset set published | T25 |
| 29 | 462 | other | GLBGPT review (2026-09-10): three H3.1 inputs; Standard and Detailed both missed held-out rear/underside | T26 |
| 30 | 466 | Tripo | Segmentation v2: granularity simple/balanced/detailed and split_by_connectivity; both ignored when ref_image is given | T11 |
| 31 | 466 | Tripo | Segmentation inputs: task IDs, uploaded tokens, URLs; GLB/GLTF/FBX/OBJ/STL; max 150 MB | T11 |
| 32 | 468 | Tripo | Retopology v3 accepts 500-20,000 triangles or 500-10,000 quads | T12 |
| 33 | 468 | Tripo | smart_uv valid only with retopology v3.0; v1/v2 returns 400 / error 1004 | T12, T03 |
| 34 | 468 | Tripo | Retopology v3 smart_uv adds UVs at no extra charge and returns no UV-atlas preview | T12 |
| 35 | 468 | Tripo | Retopology: texture baking and per-part targeting documented, v1 excluded | T12 |
| 36 | 470 | Tripo | Standalone Smart UV max 80,000 equivalent triangles (quad = 2); larger input accepted at creation can fail and refund credits | T13 |
| 37 | 470 | Tripo | Smart UV bake=true by default; UV preview returned | T13 |
| 38 | 472 | Tripo | Texture API: text, image, images guidance mutually exclusive; style_image can accompany text | T14 |
| 39 | 472 | Tripo | Texture v3.5 supports delight and fast quality; default texture v3.0; geometry snapshot does not pick v3.5 | T14 |
| 40 | 474 | Tripo | Convert parameters: format, face_limit, quad, texture_size, bake, pack_uv, pivot_to_center_bottom, scale_factor | T15 |
| 41 | 474 | Tripo | Convert: quad forces FBX; vertex-color export only OBJ/GLTF; default diffuse texture size 4096 | T15 |
| 42 | 508 | Tripo | API credits: 1 credit = $0.01 USD; H standard-textured image/multiview generation 30 | T16 |
| 43 | 508 | Tripo | API processing prices: segmentation 40; retopology v3 triangle 35, quad 40; Smart UV 20; conversion 5 basic, 10 advanced | T16 |
| 44 | 508 | Tripo | P2 API card prices: 100 untextured; 110 standard, 120 detailed, 130 8K texture | T02 |
| 45 | 508 | Tripo | Studio prices: HD generation 15 credits, P2 generation 100, segmentation 30 (October 2026) | T17 |
| 46 | 510 | Tripo | Studio table: free output commercial with attribution, Tripo owns IP; paid private models get full commercial rights and ownership | T17 |
| 47 | 510 | Tripo | Terms last updated 2025-07-11: broad retained rights for free users, general paid-user rights, service licence; paid inputs/outputs not AI training data | T18 |
| 48 | 510 | Tripo | Marketing page (2026-04-02) says free outputs are strictly noncommercial | T19 |
| 49 | 515 | other | UltraTex (2026-09-19): 2048 multiview texturing, over 268,000 assets, 22.3x-74.6x end-to-end speedup | T24 |
| 50 | 516 | other | ViSculpt (2026-08-25): Blender 4.5 LTS, Gemini 3 Flash/3 Pro, 20 tasks, 40 meshes, 48 participants (39 non-experts, 9 experts), ratings 7.53 vs 7.20 | T22 |
| 51 | 517 | other | Nexus: 1,221 pairwise comparisons, 93.0% preference, up to 20,000 faces, Objaverse/Toys4K | T21 |
| 52 | 518 | other | EZBlender (2026-01-12): GPT-4o, 245 BlenderGym scenes, 512x512, RTX 3090 24 GB, 96 GB RAM, i9-13900K; latency 37.35 s / 286.08 s / 23.85 s | T23 |
| 53 | 522 | other | EZBlender Table 3 gives seconds; Table 4 repeats values under a millisecond header | T23 |
| 54 | 538 | Roblox | Roblox supports rigged meshes and multi-mesh rigging workflows | B28, B29 |
| 55 | 542 | Blender | Separate by Loose Parts splits disconnected geometry only; Separate by Selection moves selected geometry to a new object | B13 |
| 56 | 542 | Blender | Bisect cuts with a plane; Fill can cap cuts and derives material/UV/colour from surroundings | B14 |
| 57 | 544 | Blender | Origin governs object transforms; "center of mass" origin assumes uniform density | B17 |
| 58 | 544 | Blender | Apply transforms before rigging when possible; applying armature transforms does not rewrite pose locations, animation curves or constraints | B18 |
| 59 | 544 | Roblox | General skinning: at most 4 bone influences per vertex; root at 0, 0, 0; no root influences; scale 1, 1, 1; rotation 0, 0, 0 | B31 |
| 60 | 570 | Blender | UV packing can preserve pinned island transforms and reserve a custom region | B16 |
| 61 | 570 | Blender | UV data is stored per loop/corner | B09 |
| 62 | 574 | Roblox | General texture rendering up to 4096x4096; January 2026 release: 8K import, kept at original quality, transcoded down to 4K at runtime | R02, R03 |
| 63 | 574 | Roblox | The texture spec page also states a 1024x1024 maximum in its UV section (self-contradiction) | R02 |
| 64 | 576 | Roblox | Texture streaming: low-end Android below 3.5 GB has 4K disabled; matrix lists UI, SurfaceGUI, Terrain, TerrainDetail, Sky as not yet supported | R04 |
| 65 | 578 | Roblox | Texture size guidance: 5x5 studs 256x256; 10x10 512x512; 20x20 1024x1024 | R02 |
| 66 | 578 | Roblox | One material per mesh; PBR maps are channels; one UV set; UV 0-1; overlap allowed | R02 |
| 67 | 582 | Roblox | MeshPart: TextureID or SurfaceAppearance; with MaterialVariant, SurfaceAppearance supplies maps, non-texture MaterialVariant settings still apply; "up to four PBR textures" line is outdated | R07 |
| 68 | 582 | Roblox | MaterialVariant sits under MaterialService; StudsPerTile sets tiling; can change density/friction/elasticity via CustomPhysicalProperties | R11 |
| 69 | 584 | Roblox | Duvall Drive leather trim: normal 1024, base color 512, roughness 256, no metalness | R12 |
| 70 | 586 | Roblox | SurfaceAppearance.Color multiplies ColorMap (not MeshPart.Color); overlay alpha shows MeshPart.Color; TintMask alpha controls tint; tinting has no performance cost | R10 |
| 71 | 588 | Roblox | Emissive masks live since 2026-02-12; red channel only; hue from existing colour and EmissiveTint | R09 |
| 72 | 588 | Roblox | Marketplace emissive items: strength 0-40, MeshPart accessories only (2026-09-02) | R34 |
| 73 | 590 | Roblox | Normal maps OpenGL tangent space only; tangents must be exported; reversed green inverts bumps | R11 |
| 74 | 590 | Roblox | Report (2026-10-19): ColorMap darker than TextureID; unset roughness looks glossy | R36 |
| 75 | 594 | Roblox | FBX/glTF importer supports vertex colours | R20 |
| 76 | 594 | Roblox | Marketplace: renderers handled vertex colours differently; new UGC validation prevents them; old items not fixed (replies 2026-06-23, 2026-05-26) | R31, R32 |
| 77 | 598 | Roblox | Quality Texture Generation beta (2026-10-16): 4K PBR in about 2 min vs Fast 1K colour-only about 30 s; no alpha; no chat or game context | R35 |
| 78 | 615 | Roblox | Generic mesh limit 20,000 triangles; guidelines: watertight, no exposed holes/backfaces, quads where possible, at most 4 bone influences | R01 |
| 79 | 617 | Roblox | Marketplace body: 15 mesh objects in 6 assets; DynamicHead 4,000, Torso 1,750, each arm 1,248, each leg 1,248, total 10,742; textures at most 2048x2048 | R05 |
| 80 | 617 | Roblox | Layered clothing: 4,000 triangles per accessory, single mesh | R06 |
| 81 | 661 | Roblox | Batching rules by MeshContent, SurfaceAppearance/TextureContent or material; Render Stats draw calls; Shift + F2 | R13 |
| 82 | 665 | Roblox | MeshStreamingAndImprovedLoDs: cloud LoDs, mesh memory budget, independent of StreamingEnabled, ignores RenderFidelity; default planned around July 2026 | R14 |
| 83 | 665 | Roblox | Legacy Automatic RenderFidelity: below 250 studs highest, 250-500 medium, 500 and above lowest | R07 |
| 84 | 667 | Roblox | Mesh streaming and next-gen cloud LoDs support only un-skinned meshes and do not change collision | R15 |
| 85 | 667 | Roblox | SLIM composites models with instance streaming; supports R15 platform avatars | R17, R18 |
| 86 | 667 | Roblox | Debug tints for streaming state, LoD, transcoder state: Studio visualization modes (beta) and F9 console in Player (2026-10-09) | R19 |
| 87 | 669 | Roblox | Incident report (2026-09-04): meshes stuck at lowest LoD; an interfering feature rolled back | R16 |
| 88 | 673 | Roblox | Collision choices Box, Hull, Default, PreciseConvexDecomposition, Tunable; Tunable has CollisionPrecision, default chosen by mesh size | R07, R08 |
| 89 | 677 | Roblox | Scene Analysis at Window > Performance Summary > Scene Analysis; triangle composition by opaque/transparent/shadow pass; full release 2026-07-10 | R25, R26 |
| 90 | 677 | Roblox | SceneAnalysisService:GetTriangleCompositionAsync returns tree with Sizes.Triangles and Sizes.Drawcalls by pass; memory methods cover script, audio, animation only | R27 |
| 91 | 679 | Roblox | MicroProfiler: timing breakdown; Studio/live client captures; frame rate = 1000 ms / frame time | R28, R29 |
| 92 | 683-701 | Roblox | Checklist items 1-10 restate claims 78, 79, 80, 66, 59, 65, 62-64, 81, 88, 82-83, 89-90 | R01-R14, R25, R27 |

## 15. Contradictions and gaps (inside MP:423-711)

Compared with the owner budget (J007-D5: 20,000 triangles per mesh is the upload ceiling only; creatures and characters under about 7,000) and the rig split (animator says what moves; rigger says which parts are separate and where cuts go; modeler cuts, cleans seams, re-models; rig method per joint, J005-D1, J005-D9).

| ID | MP | Type | Finding | Effect for the modeler |
| --- | --- | --- | --- | --- |
| X-01 | 428, 431, 468, 615, 617 | Owner budget | Every number in range is a ceiling: H3.1 1,500,000 and 2,000,000; P2 Studio 50,000 triangles or 25,000 quads; P2 API 48-50,000 or 48-25,000; retopology v3 500-20,000 triangles or 500-10,000 quads; generic mesh 20,000; Marketplace body 10,742; layered clothing 4,000. None is a phone budget. The paper's own phone budget for player, NPC, pet and others is UNKNOWN (BG-04 to BG-12). | The 7,000 owner budget is a project decision (J007-D5), not a paper number. In the paper's allocation record it belongs in "proposed content limits" until measured. Request a Tripo face limit near the owner budget, not a tool maximum. |
| X-02 | 615 | Owner budget scope | The owner brief does not say if "under about 7,000" is per mesh or per whole creature or character. The paper's ceilings are per mesh (R01) and it warns against splitting a heavy model to pass upload (BG-02). A rigid-piece rig makes several meshes. | Lead should state which scope applies, especially for rigid-piece rigs. |
| X-03 | 468 | Owner budget arithmetic (extractor note, not in paper) | Retopology v3 takes 500-20,000 triangles, so a 7,000 target fits. In quads it is about 3,500 (7,000 triangles / 2) if all faces are quads. The paper says to count after triangulation, not assume. | Count triangles after export. |
| X-04 | 490, 560, 466, 431 | Rig split | Paper lets the modeler "propose economical construction" and says "resolve moving-part construction with rigger/animator". The owner split gives the rigger the decision on which parts are separate and where cuts go; the modeler makes the cuts (J005-D1), with one counter-proposal round at S3. Tripo auto-separation (P2 Studio: body, clothing, accessories; segmentation v2) cuts by meaning, not by the rigger's joint list. | Treat any Tripo cut or segmentation as a proposal. The rigger's cut list wins. The paper's wording gives the modeler more say than the owner split. |
| X-05 | 538, 551-558 | Rig method | The paper's "rigid part vs skinned continuous, chosen per region" matches J005-D9. No conflict. | Use the per-joint choice. |
| X-06 | 667 | Rig vs streaming (extractor inference) | Mesh streaming and next-gen cloud LoDs support only un-skinned meshes (R15). A skinned creature at about 7,000 triangles gets no cloud LoD and must meet its budget as authored. The paper does not state this consequence. Rigid un-skinned pieces may be eligible; the paper does not say so. | Flag to rigger and performance engineer; fact-check claim 84 first. |
| X-07 | 431, 438 | Date | MP:438 gives "update 2026-10-10" beside T06 and T07. The register dates T07 at 2026-10-10 but T06 as "undated updated announcement". | Do not cite 2026-10-10 for T06. |
| X-08 | 508 | Surface | Studio "P2 generation 100 credits" (T17) and API P2 "100 untextured" (T02) share a number. The paper says do not compare, and does not say if the Studio price includes a texture. | The owner reads the Studio price list live. |
| X-09 | 450-474 | Surface | Almost all processing detail (view slots, parameters, 80,000 limit, retopology v3, texture_version, convert options, credit prices) is API documentation. The owner runs Studio (J007-D4). The paper does not verify that Studio shows the same controls, view order, model versions or limits. | Treat API rows as intent. The skill must tell the owner to check the Studio UI. No Studio control names are verified. |
| X-10 | 428 | Ambiguity | "10,000 faces if a quad face limit is omitted" does not say whether faces means triangles or quads. | Do not use as a count. |
| X-11 | 450 | Source gap | The remark that Studio tutorials describe front/side/back loosely has no source id. | Claim 23. |
| X-12 | 574 | Source conflict | R02 states 4096x4096 and 1024x1024 maximums on the same page. Paper prefers the dated R03 release and keeps the conflict. | No single texture maximum for the skill; use "4K top mip, not a target". |
| X-13 | 510 | Source conflict | Studio table (T17) says free output commercial with attribution; Terms (T18) say broad retained rights for free users; marketing page (T19, 2026-04-02) says free is noncommercial. Paper does not resolve it. | [for-owner-tripo]: owner records plan and date; no free-tier clearance. |
| X-14 | 427, 458, 510 | Tag oddity | T19 and T20 are Tripo's own pages but tagged EXPERIENCE, while other Tripo vendor pages are VERIFIED. Kept as given. | Fact-checkers should treat T19 and T20 as vendor statements. |
| X-15 | 462, 534 | Evidence gap | No verified independent benchmark of Tripo cleanup hours, hero acceptance rate or Roblox-ready yield. | Do not quote time savings. |
| X-16 | 560, 570, 633 | Gap | No numbers for joint limits, seam overlap distance, joint-loop count, texel density, texture sizes per type, unique materials per type, or phone triangle budget except the owner's. | Project decisions; keep as open fields. |
| X-17 | 683 vs 617 | Minor | Checklist item 2 says per-part groups for the 10,742 body total, but the paper lists the groups only in MP:617. Arithmetic check (extractor): 4,000 + 1,750 + 4 x 1,248 = 10,742, which matches. | Claim 79 is internally consistent. |
| X-18 | 544, 689 | Duplicate source | B31 and R01 are the same URL (create.roblox.com/docs/art/modeling/specifications); R01's register quote points to B31. The 4-influence limit is cited as B31 in section 6 and as R01 in section 8. | Count once when fact-checking. |

## 16. Sources used (resolved from MP:976-1974)

Dates and evidence tags are the paper's. "Accessed" = undated live page read on 2026-10-21. Quotes are short locator fragments only.

| Id | Title | Date | Evidence | URL | Locator |
| --- | --- | --- | --- | --- | --- |
| P00 | Proposed studio method | 2026-10-21 | OPINION | none (paper's own synthesis) | not an external measurement |
| B09 | Mesh Python API | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/api/5.2/bpy.types.Mesh.html | "Validate geometry" |
| B13 | Separate mesh | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/sr/5.2/modeling/meshes/editing/mesh/separate.html | "independent (disconnected) piece" |
| B14 | Bisect mesh | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/id/5.2/modeling/meshes/editing/mesh/bisect.html | "infinitely large plane" |
| B16 | UV editing and packing | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/uk/5.2/modeling/meshes/uv/editing.html | "specified margin" |
| B17 | Object origin | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/en/latest/scene_layout/object/origin.html | "uniform density" |
| B18 | Apply transforms | undated, accessed 2026-10-21 | VERIFIED | https://docs.blender.org/manual/ja/5.2/scene_layout/object/editing/apply.html | "apply transforms before rigging" |
| B28 | Roblox rigging simple mesh | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/rig-a-simple-mesh | "rigged mesh" |
| B29 | Roblox humanoid mesh rigging | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/rig-a-humanoid-model | "multiple meshes require additional steps" |
| B31 | Roblox general model specifications | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/specifications | "more than 4 bones or joints" |
| R01 | General specifications | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/specifications | same page as B31 |
| R02 | Texture specifications | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/texture-specifications | "up to 4096x4096" |
| R03 | 4k Texture Rendering | 2026-01-30 | VERIFIED | https://devforum.roblox.com/t/4k-texture-rendering/4316229 | "4k Textures are now available" |
| R04 | Introducing Texture Streaming | 2025-12-12, status 2026-03-23 | VERIFIED | https://devforum.roblox.com/t/introducing-texture-streaming/4144855 | "4k textures disabled" |
| R05 | Character body specifications | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/avatar/character-bodies/specifications | "can't exceed 2048x2048" |
| R06 | Clothing specifications | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/accessories/clothing-specifications | "can't exceed 4k triangles" |
| R07 | Meshes | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/parts/meshes | "still not a 1:1 representation" |
| R08 | Collision Geometry Workflow Improvements: Tunable Precision | 2026-09-17 | VERIFIED | https://devforum.roblox.com/t/collision-geometry-workflow-improvements-tunable-precision-and-better-visualizations/4878198 | "CollisionPrecision slider" |
| R09 | Emissive Masks are Now Live | 2026-02-12 | VERIFIED | https://devforum.roblox.com/t/emissive-masks-are-now-live-for-published-experiences/4357705 | "only the Red channel" |
| R10 | PBR textures | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/art/modeling/surface-appearance | "Tinting does not affect performance" |
| R11 | MaterialVariant API | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/reference/engine/classes/MaterialVariant | "descendants of MaterialService" |
| R12 | Materialize the world: Duvall Drive | undated, accessed 2026-10-21 | EXPERIENCE | https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/materialize-the-world | "a normal map at 1024" |
| R13 | Improve performance | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/performance-optimization/improve | "single draw call" |
| R14 | Mesh Streaming and Improved Cloud LoDs (opt-in phase) | 2026-04-27 | VERIFIED | https://devforum.roblox.com/t/introducing-mesh-streaming-and-improved-cloud-lods-in-published-experiences-opt-in-phase/4601232 | "RenderFidelity ... will be ignored" |
| R15 | Early Access: Mesh Streaming and Next-gen Cloud LoDs | 2026-03-16, update 2026-06-17 | VERIFIED | https://devforum.roblox.com/t/early-access-introducing-mesh-streaming-and-next-gen-cloud-lods/4525340 | "only support un-skinned meshes" |
| R16 | Mesh streaming low LoD production incident | 2026-09, fix report 2026-09-04 | EXPERIENCE | https://devforum.roblox.com/t/meshstreamingandimprovedlods-persistently-stuck-at-lowest-lod-level-for-all-meshes/4835534 | "The feature rolled back today" |
| R17 | SLIM client beta | 2025-10-30, updates 2025-12-09 and 2026-02-25 | VERIFIED | https://devforum.roblox.com/t/client-beta-introducing-scalable-lightweight-interactive-models-slim/4034709 | "supported on all platforms" |
| R18 | Platform Avatars in SLIM | 2026-05-12 | VERIFIED | https://devforum.roblox.com/t/introducing-support-for-platform-avatars-in-slim/4632702 | "supports R15 platform avatars" |
| R19 | SLIM debug tints | 2026-10-09 | VERIFIED | https://devforum.roblox.com/t/slim-debug-tints-in-studio-and-roblox-player/4924019 | "SLIM now has debug tints" |
| R20 | Importer | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/studio/importer | "Scale Unit" |
| R25 | Scene Analysis | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/performance-optimization/scene-analysis | "don't necessarily match what players see" |
| R26 | Scene Analysis Tool full release | beta 2026-05-05, full 2026-07-10 | VERIFIED | https://devforum.roblox.com/t/full-release-scene-analysis-tool/4620678 | "out of beta and fully released" |
| R27 | SceneAnalysisService API | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/reference/engine/classes/SceneAnalysisService | "by render pass" |
| R28 | Identify performance issues | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/performance-optimization/identify | "computational time ... each frame" |
| R29 | MicroProfiler | undated, accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/performance-optimization/microprofiler | "Divide 1,000 milliseconds" |
| R31 | Marketplace vertex colors renderer inconsistency | report 2024-09-24, response 2026-06-23 | EXPERIENCE | https://devforum.roblox.com/t/marketplace-assets-with-mesh-vertex-colors-displaying-vertex-colors-instead-of-texture/3171022 | "won't be fixing this" |
| R32 | UGC vertex color validation | report 2025-06-13, response 2026-05-26 | EXPERIENCE | https://devforum.roblox.com/t/ugc-accessory-color-changes-under-certain-circumstances/3730515 | "validation now prevents vertex colors" |
| R34 | Create and Sell Emissive Items on Marketplace | 2026-09-02 | VERIFIED | https://devforum.roblox.com/t/full-release-create-and-sell-emissive-items-on-marketplace/4846756 | "A value from 0 to 40" |
| R35 | Quality Mode for Texture Generation Beta | 2026-10-16 | VERIFIED | https://devforum.roblox.com/t/beta-introducing-quality-mode-for-texture-generation/4938282 | "doesn't currently support alpha" |
| R36 | SurfaceAppearance rendering differences report | 2026-10-19 | EXPERIENCE | https://devforum.roblox.com/t/appearance-issues-with-surfaceappearance/4944376 | "slightly darker than MeshPart.TextureID" |
| T01 | Tripo H3.1 model card | undated live, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/models/v3-1 | "v3.1-20260211 Default" |
| T02 | Tripo P2 model card | undated live, snapshot P2-20260801, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/models/p2 | "P2-20260801 Preview" |
| T03 | Tripo Developers changelog | entries 2026-04 to 2026-10 | VERIFIED | https://developers.tripo3d.ai/en/docs/changelog | "default is still v2.0" |
| T04 | Multiview to 3D Model, H series v3 | undated live, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/generation-multiview-to-model/standard | "at least 2 images" |
| T05 | Legacy multiview to model H3 | undated legacy v2 docs, accessed 2026-10-21 | VERIFIED | https://docs.tripo3d.ai/model-generation/multiview-to-model-v3-0-v3-1.html | "exactly 4 items" |
| T06 | Tripo P2 official announcement | undated updated page, accessed 2026-10-21 | VERIFIED | https://www.tripo3d.ai/blog/tripo-p2-0-preview | "automatically separates body, clothing" |
| T07 | Tripo September update | 2026-10-10 per blog index; covers September 2026 | VERIFIED | https://www.tripo3d.ai/blog/tripo-september-update | "officially launched P2.0" |
| T08 | Getting better image to 3D results | undated live help, accessed 2026-10-21 | VERIFIED | https://www.tripo3d.ai/help/features/how-to-get-better-image-to-3d-results | "70-85% of the image" |
| T09 | Using multiview input effectively | undated live help, accessed 2026-10-21 | VERIFIED | https://www.tripo3d.ai/help/features/how-to-use-multi-view-input-effectively | "match in pose, lighting" |
| T10 | Tripo image preparation | 2026-10 (month supplied) | VERIFIED | https://www.tripo3d.ai/product-doc/model-generation/image-preparation | "1-10 transparent PNGs" |
| T11 | Mesh segmentation API | undated live, v2.0-20260430, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/mesh-segment | "v2.0-20260430 Beta" |
| T12 | Retopology API | undated live, v3.0 introduced 2026-10, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/mesh-decimate | "three algorithm tiers" |
| T13 | Smart UV API | undated live, introduced 2026-10 per changelog, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/mesh-uv | "80,000 equivalent triangles" |
| T14 | Texture API | undated live, texture v3.5-20260815 added 2026-09, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/models-texture | "Regenerate texture maps" |
| T15 | Model format conversion API | undated live, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/models-convert | "force the output format to FBX" |
| T16 | Tripo API pricing | undated live price list, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/pricing | "1 credit = $0.01 USD" |
| T17 | Tripo Studio pricing and credits | 2026-10 (month supplied) | VERIFIED | https://www.tripo3d.ai/product-doc/getting-started/pricing-credits | "Full commercial ... set to private" |
| T18 | Tripo Terms of User Agreement | last updated 2025-07-11 | VERIFIED | https://www.tripo3d.ai/terms | "Paid Users generally have all rights" |
| T19 | Game development retopology marketing page | 2026-04-02 | EXPERIENCE | https://www.tripo3d.ai/game-development/game-development-retopology | "Free tier ... NOT for commercial use" |
| T20 | Game character workflow using Tripo P2.0 | 2026-10-14 per blog index | EXPERIENCE | https://www.tripo3d.ai/blog/mesh-game-character-p-2 | "removes the character artist" |
| T21 | Nexus: Native Mesh Generation with Diffusion | 2026-07-15 v1 | VERIFIED | https://arxiv.org/html/2607.13563v1 | "ignores the face normals" |
| T22 | ViSculpt: Visual-Centric Agentic Geometry Editing | 2026-08-25 v1 | VERIFIED | https://arxiv.org/html/2608.24169v1 | "20 geometry-editing tasks" |
| T23 | EZBlender: Efficient 3D Editing with Plan and ReAct Agent | 2026-01-12 v1 | VERIFIED | https://arxiv.org/html/2601.07143v1 | "GPT-4o as the LLM backend" |
| T24 | UltraTex: 2K Multi-View Diffusion for 3D Texturing | 2026-09-19 v1 | VERIFIED | https://arxiv.org/html/2609.23169v1 | "Background Token Dropping" |
| T25 | Tripo P2.0 quad mesh review (Digital Production) | 2026-09-29 | EXPERIENCE | https://digitalproduction.com/2026/09/29/tripo-p2-0-put-quad-mesh-generation-to-the-test/ | "says nothing about pole placement" |
| T26 | Tripo H3.1 Standard vs Detailed three-input review (GLBGPT) | 2026-09-10 | EXPERIENCE | https://www.glbgpt.com/hub/nl/tripo-h3-1-review-2/ | "missed ... underside and rear structure" |
| T27 | Tripo image to 3D feature instructions | undated live help, accessed 2026-10-21 | VERIFIED | https://www.tripo3d.ai/help/features/how-to-use-the-image-to-3d-feature | "Best Quality = HD Model = H Series" |
| T28 | Preparing models for 3D printing | undated live help, accessed 2026-10-21 | VERIFIED | https://www.tripo3d.ai/help/features/how-to-prepare-models-for-3d-printing | "unseen surfaces are inferred" |
| T29 | P series multiview API | undated live, accessed 2026-10-21 | VERIFIED | https://developers.tripo3d.ai/en/docs/generation-multiview-to-model/p | "P2-20260801" |
