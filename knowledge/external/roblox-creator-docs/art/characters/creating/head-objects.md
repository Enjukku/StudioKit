---
title: Template head structure
description: Each Roblox avatar template contains modular separate pieces that must later be combined or removed.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
next: /art/characters/creating/blender-configurations
prev: /art/characters/creating/template-files
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/creating/head-objects.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/creating/head-objects.md). Published page: [https://create.roblox.com/docs/art/characters/creating/head-objects](https://create.roblox.com/docs/art/characters/creating/head-objects).

Each avatar character body template includes extra head mesh objects and face armature bones. Separating these objects within the templates allows you to make easier changes to each of these separate objects, as demonstrated during the texturing section of this tutorial.

To avoid validation errors, you must [[external/roblox-creator-docs/art/characters/creating/combine-head-geometry|join]] and [[external/roblox-creator-docs/art/characters/creating/remove-extra-bones|remove]] these extra objects during the cleanup process prior to exporting.

The extra head mesh objects are the following:
<GridContainer numColumns="2">

  <figure>
   - Head_Geo
   - UpperTeeth_Geo
   - LowerTeeth_Geo
   - Tongue_Geo
   - RightLash_Geo
   - RightEye_Geo
   - LeftLash_Geo
   - LeftEye_Geo
</figure>

  <figure><img
  alt="Head-Related Meshes"
  src="../../../assets/art/blender-ui/Face-Objects.png"
  width="800" /><figcaption>Extra head-related meshes in Blender's Outliner</figcaption></figure>
</GridContainer>

<p />

The extra head bone children are the following and may differ between templates:

<GridContainer numColumns="2">

  <figure>
   - Tongue
   - LowerTeeth
   - UpperTeeth
   - LeftEye
   - RightEye
</figure>

  <figure><img
  alt="Head-Related Meshes"
  src="../../../assets/art/blender-ui/Face-Bones.png"
  width="800" /><figcaption>Extra head-related bones in Blender's Outliner</figcaption></figure>
</GridContainer>

While these extra objects exist to aid the creation and modification process, leaving them in your project on final export will cause validation issues when uploading these assets to the Marketplace.


## Related Files

- [[external/roblox-creator-docs/art/characters/creating/blender-configurations]] - Blender configuration.
- [[external/roblox-creator-docs/art/characters/creating/caging]] - Caging character head.
- [[external/roblox-creator-docs/art/characters/creating/combine-head-geometry]] - Combine head geometry.
- [[external/roblox-creator-docs/art/characters/creating/index]] - Create with templates.
- [[external/roblox-creator-docs/art/characters/creating/export-character]] - Export character model.
- [[external/roblox-creator-docs/art/characters/creating/export-textures]] - Export textures.
- [[external/roblox-creator-docs/art/characters/creating/final-checks]] - Final checks.
- [[external/roblox-creator-docs/art/characters/creating/modeling-best-practices]] - Modeling best practices.
- [[external/roblox-creator-docs/art/characters/creating/modeling-tips]] - Modeling tips.
- [[external/roblox-creator-docs/art/characters/creating/texturing-pbr]] - PBR textures (optional).
- [[external/roblox-creator-docs/art/characters/creating/remove-extra-bones]] - Remove extra bones.
- [[external/roblox-creator-docs/art/characters/creating/sculpting]] - Sculpt the head.
- [[external/roblox-creator-docs/art/characters/creating/template-files]] - Template files.
- [[external/roblox-creator-docs/art/characters/creating/texturing-eyes]] - Texturing eyes.
- [[external/roblox-creator-docs/art/characters/creating/texturing-face]] - Texturing face.
- [[external/roblox-creator-docs/art/characters/creating/texturing-setup]] - Texturing setup.
- ...and 1 more local docs.
