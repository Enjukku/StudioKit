---
title: Makeup specifications
description: Makeup is a cosmetic look made up of multiple facial textures and optional eyebrow and eyelashes.
tags: [roblox, documentation, external-reference, priority-reference, avatar]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [avatar/makeup/specifications.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/avatar/makeup/specifications.md). Published page: [https://create.roblox.com/docs/avatar/makeup/specifications](https://create.roblox.com/docs/avatar/makeup/specifications).

Makeup requires a specific set of components and configuration standards to ensure it displays properly on avatar faces of all shapes and sizes. Before you start the export process, verify that your makeup meets the following specifications and guidelines for proper Studio compatibility.

When you're ready to export your makeup, reference all [[external/roblox-creator-docs/avatar/makeup/reassign-textures|export setting requirements]] for Blender and Maya.

<Alert severity = 'info'>
<AlertTitle>For other types of 3D models:</AlertTitle>
<ul>
<li>[[external/roblox-creator-docs/art/modeling/specifications|General mesh]] specifications.</li>
<li>[[external/roblox-creator-docs/avatar/rigid-accessories/specifications|Rigid accessory]] specifications.</li>
<li>[[external/roblox-creator-docs/avatar/layered-accessories/specifications|Layered accessory]] specifications.</li>
</ul>
</Alert>

## General

If you are following the best practice [[external/roblox-creator-docs/avatar/makeup/index#creation-process|creation process]], ensure that your template file submission includes the following objects that are correctly configured and named in their respective third-party modeling software:

<img src="../../assets/makeup/Makeup-Blender-Datamodel.png" width="55%" />

- A **head mesh object** and associated **cage mesh object**.
  - These two objects must include the prefix "TransferTarget_" in their name.
- **TransferTexture mesh objects** for each region: `Eyes`, `Face`, `Lips`.
  - These three objects must follow the following naming conventions.
    - `TransferTexture_Eyes_01`
    - `TransferTexture_Lips_01`
    - `TransferTexture_Face_01`
    - Any for multiple regions, increment the affix number: `TransferTexture_Face_02`
- Optional [eyebrows and eyelashes](#eyebrows-and-eyelashes).

<Alert severity = 'warning'>
The [provided Roblox makeup template head](https://github.com/Roblox/avatar/tree/main/Makeup) should already be properly configured with the correct objects and naming conventions. To prevent issues with import, avoid renaming or deleting the data model of the template head when creating your own makeup.
</Alert>

## Decals and textures

All accessory textures must meet Roblox's [[external/roblox-creator-docs/art/modeling/texture-specifications|texture specifications]], but makeup textures include two additional considerations:

- There is a 4K texture limit for [[external/roblox-creator-docs/avatar/in-experience-creation|in-game]] makeup creation.
- There is a 1K texture limit for makeup that you upload to the [Marketplace](https://www.roblox.com/catalog).

For additional information on PBR textures, see [[external/roblox-creator-docs/art/modeling/surface-appearance|PBR textures]].

## Eyebrows and eyelashes

Eyebrows and eyelashes are optional layered accessories for makeup looks. If you choose to include them in your creations, they must meet all [[external/roblox-creator-docs/avatar/layered-accessories/specifications|layered accessory requirements]], notably:

- **Cage data** - Eyebrows and eyelashes each require their own inner and outer cage.

  <img src="../../assets/makeup/Makeup-Eye-Accessory-Datamodel.png" width="55%" />

  - Eyebrows and eyelashes can also take advantage of automatic skinning, specifically with [[external/roblox-creator-docs/avatar/automatic-skinning-transfer#special-skinning-transfer-joints|special skinning joints]].

- **Geometry size** - Eye accessories can't exceed the [[external/roblox-creator-docs/avatar/layered-accessories/specifications|maximum dimensions]] for their asset type.
- **Budgets** - Eye accessories can't exceed 4k triangles each.


## Related Files

- [[external/roblox-creator-docs/avatar/makeup/import]] - Import into Studio.
- [[external/roblox-creator-docs/avatar/makeup/index]] - Makeup.
- [[external/roblox-creator-docs/avatar/makeup/reassign-textures]] - Reassign textures.
