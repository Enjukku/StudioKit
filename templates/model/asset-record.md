<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit template (J007): copy to content/models/<asset-id>/asset-record.md. Owner of the file: the modeler. How to fill it: `modeling-design` skill. Write UNKNOWN for a missing fact, never a guess. revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6): read plan, iconic qualities, self-review results. -->
# Asset record: <asset-id>

| Field | Value | Source |
| --- | --- | --- |
| Revision | rev 1, <date> | |
| Kind | character / NPC / creature / pet / weapon / tool / prop / vehicle / building / kit piece / environment piece | brief |
| Role in the game | <what the player does with it> | brief |
| Used how | <grip, seat, walk-through, pick-up, decoration> | brief |
| Game camera and distance | <third person ~N studs / first person / icon only> | game profile |
| Visible sides | <all / front only / top only> | brief |
| Size against the player | <studs, or UNRESOLVED> | owner / art director |
| Moves? | static / rig sheet: content/rigs/<asset-id>/rig-sheet.md | animator, rigger |
| Attach points | <name: position, orientation, parent, purpose> | brief, VFX, animator |
| Collision | none / Box / Hull / proxies / Tunable; openings that must stay open | brief |
| Material families and palette roles | <from the art bible> | art bible rev <n> |
| Triangle budget (whole model) | <number> | owner J007-D5 / game profile / PROPOSAL |
| Texture plan | <maps and sizes, shared atlas or tint> | PROPOSAL / game profile |
| Approved reference | <image path, id, revision> | decision line |
| Build views | <paths> | |
| Route | hand / Tripo + finish, because <reason> | modeler |
| Tripo record (if Tripo) | surface, model and version, settings used, task id, output files, date, account plan | owner run |
| Invariants (must match the image) | <list> | |
| Shown / inferred / left out / awaiting decision | <per feature> | |
| Deviations from the image | <what, why, who approved> | |
| Open questions | <list> | |

## Read plan (before the reference check and the blockout)
What each row holds, and which rows a simple model fills: `modeling-design/references/read-and-form.md` §1. One line per row; UNKNOWN when a fact is missing.

| Row | Value | Source |
| --- | --- | --- |
| Job in play | | |
| Sell list | | |
| Character (tension words) or personality words | | |
| Identity anchors (ranked; the 1-2 that survive the icon crop) | | art director |
| Read order | | |
| Viewing conditions (game camera; on-screen height in px on the smallest phone; sides; other sizes) | | game profile |
| Detail spots | | |
| Shape language | | art bible rev <n> |
| Value plan | | |
| Palette roles (and reserved colours it must not use) | | art bible rev <n> |
| Motion facts | | animator, rigger |
| Neighbours | | |
| Stop criteria and pass budget | | |

## Iconic qualities, gaps, material intent
From the reference check (`modeling-design/references/reference-check.md` §7).

| Item | Value |
| --- | --- |
| Iconic qualities to keep | <list> |
| Gaps and the choice made (inside the art bible, or asked) | <gap: choice, who decided> |
| Material intent per region (unlit local colour) | <region: material, colour> |

## Self-review results (each hand-off)
Lines and pass values: `modeling-design/references/review.md` §5. Result: pass, fail, MEASURED (no tolerance) or not verified.

| Group | Lines run | Result | Evidence | Label |
| --- | --- | --- | --- | --- |
| RP read plan | | | | |
| SL silhouette | | | | |
| VL value | | | | |
| CL colour and light | | | | |
| DT detail and surface | | | | |
| MO motion | | | | |
| VA variants, tiers, families | | | | |
| GR grounding and place | | | | |
| IM in game and honest close | | | | |

## Results (filled at each hand-off)
| Check | Value | Evidence | Label |
| --- | --- | --- | --- |
| Triangles (evaluated) | | audit json | gate-verified / MCP-verified / not verified |
| Size in studs | | audit json | |
| Loose parts / flipped faces / open edges | | audit json | |
| Materials / UV sets per mesh | | audit json | |
| Texture sizes | | audit json | |
| Review render set | <paths, count made, count looked at> | | |
| Roblox import | <asset ids, importer settings, warnings> | | |

## Lineage
| Item | Path or id |
| --- | --- |
| Source .blend (never edited after release) | |
| Raw Tripo output (never edited) | |
| Export files + export settings | |
| Roblox asset ids | |
