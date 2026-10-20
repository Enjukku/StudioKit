---
title: Sculpt the head
description: Use Blender's sculpting tools to make unique changes to the shape of your character.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
next: /art/characters/creating/texturing-setup
prev: /art/characters/creating/modeling-tips
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/creating/sculpting.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/creating/sculpting.md). Published page: [https://create.roblox.com/docs/art/characters/creating/sculpting](https://create.roblox.com/docs/art/characters/creating/sculpting).

After reviewing the modeling best practices and sculpting tips, you can begin sculpting your avatar character body. This tutorial demonstrates sculpting changes to the [RoundMale template](../../../assets/art/reference-files/RoundMale.zip), creating a goblin-like character.

The sculpting instructions utilize the following Sculpting tools:

- **Grab** - Selects and pulls a group of vertices.
- **Smooth** - Eliminates irregularities in the area of the brush's influence.
- **Flatten** - Averages out the vertices within the brush's influence on a common plane.
- **Elastic Deform** - Similar to Grab, but adds an organic stretch and elasticity to the neighboring vertices.

<Alert severity='info'>
You can use Blender's other sculpting tools, though it's important to use a tool that aligns with the [[external/roblox-creator-docs/art/characters/creating/modeling-best-practices#non-destructive-modeling|Non-Destructive Modeling]] concepts to preserve the vertices of the model.
</Alert>

To begin sculpting the head:

1. With the template project opened, hide the other Geo objects to isolate the head mesh.
1. Select the `Head_Geo` mesh object and switch to **Sculpting** mode.
1. At the top right of the viewport:
   1. Enable **X-Axis symmetry**.
   1. Enable **Wireframe** mode.

   <video controls src="../../../assets/art/avatar/basic-creation/Sculpting_01.mp4" width="100%"></video>

1. Using the **Mask** tool, paint over the mouth and eyes where you do not want to sculpt unexpectedly.

   <video controls muted src="../../../assets/art/avatar/basic-creation/Sculpting_02.mp4" width="100%"></video>

1. With the **Grab** and **Smooth** tools, make the following edits to your template head:

   1. Reshape the head, flattening and enlarging the top.

   1. Elongate the ears.

      1. Expand the surface near the ear to broaden the base
      1. Grab and extend each ear, ensuring it connects smoothly to the base and vertices remain proportionally spaced when possible.
      1. Try the **Flatten** tool to straighten and align a region.
      1. Try the **Elastic Deform** tool to stretch and pull multiple vertices.

         <video controls muted src="../../../assets/art/avatar/basic-creation/Sculpting_03.mp4" width="100%"></video>

   1. Extend the bridge of the nose and expand the size of the brow.

      <video controls src="../../../assets/art/avatar/basic-creation/Sculpting_04.mp4" width="100%" muted></video>

   1. Broaden the chin so it prominently protrudes.

      <video controls src="../../../assets/art/avatar/basic-creation/Sculpting_06.mp4" width="100%" muted></video>

1. Perform a refinement pass to add final details, polish, and accentuate your main features, such as:
   - Adding details in the outer and inner ears
   - Adding more detail to chin and cheeks
   - Improving edge lines and spacing in areas with crowded vertices

     <video controls src="../../../assets/art/avatar/basic-creation/Sculpting_07.mp4" width="100%"></video>

<Alert severity = 'success'>
For a comparison reference, you can download [this version of the tutorial project with sculpting completed](../../../assets/art/reference-files/checkpoint/1_Goblin-sculpted.blend).
</Alert>


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
- [[external/roblox-creator-docs/art/characters/creating/template-files]] - Template files.
- [[external/roblox-creator-docs/art/characters/creating/head-objects]] - Template head structure.
- [[external/roblox-creator-docs/art/characters/creating/texturing-eyes]] - Texturing eyes.
- [[external/roblox-creator-docs/art/characters/creating/texturing-face]] - Texturing face.
- [[external/roblox-creator-docs/art/characters/creating/texturing-setup]] - Texturing setup.
- ...and 1 more local docs.
