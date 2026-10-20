---
title: Remove extra bones
description: When creating characters in Blender, you must remove the extra head bones included in the template.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
next: /art/characters/creating/verify-attachments
prev: /art/characters/creating/combine-head-geometry
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/creating/remove-extra-bones.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/creating/remove-extra-bones.md). Published page: [https://create.roblox.com/docs/art/characters/creating/remove-extra-bones](https://create.roblox.com/docs/art/characters/creating/remove-extra-bones).

The helper bones used to help place the head geometries also require removal to validate correctly. While these extra bones do not include any skinning data, do not delete any of the facial animation bones parented within DynamicHead, as these include important skinning data that drives facial animation.

<Alert severity = 'error'>
Failure to [[external/roblox-creator-docs/art/characters/creating/combine-head-geometry|combine head geometry]] and remove head bones will cause issues with validation, as the character will no longer adhere to the standard [[external/roblox-creator-docs/avatar/character-bodies/specifications#body-parts|geometry]] and [[external/roblox-creator-docs/avatar/character-bodies/specifications#rigging|joint hierarchy]].
</Alert>

Remove the additional head bones by selecting them and deleting them in edit mode:

1. If required for your template, toggle visibility on your **Armature** object. The bones display in the viewport.
1. In the Outliner, expand the character's armature object and find the **Joints** object that parents the bone structure of the character.

   <img src="../../../assets/art/avatar/basic-creation/Select-Joint-Objects.png" />

1. Expand the **Joints** object's hierarchy by holding <kbd>Shift</kbd> and clicking the expansion dropdown.
1. In the viewport, select any bone and switch to **Edit** mode.
1. Under the `Head` joint, hold <kbd>Shift</kbd> and select all the head child joints except `DynamicHead`.

   <img src="../../../assets/art/avatar/basic-creation/Select-Bone-Objects.png" />

1. With the extra head bones selected, right-click in the viewport and select **Delete Selected Bones** from the contextual menu.

   <video controls src="../../../assets/art/avatar/basic-creation/Cleanup_01-1.mp4" width="100%"></video>


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
- [[external/roblox-creator-docs/art/characters/creating/sculpting]] - Sculpt the head.
- [[external/roblox-creator-docs/art/characters/creating/template-files]] - Template files.
- [[external/roblox-creator-docs/art/characters/creating/head-objects]] - Template head structure.
- [[external/roblox-creator-docs/art/characters/creating/texturing-eyes]] - Texturing eyes.
- [[external/roblox-creator-docs/art/characters/creating/texturing-face]] - Texturing face.
- [[external/roblox-creator-docs/art/characters/creating/texturing-setup]] - Texturing setup.
- ...and 1 more local docs.
