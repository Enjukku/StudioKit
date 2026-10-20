---
title: Export character model
description: Export your character model from Blender using the correct settings and processes.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
prev: /art/characters/creating/export-textures
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/creating/export-character.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/creating/export-character.md). Published page: [https://create.roblox.com/docs/art/characters/creating/export-character](https://create.roblox.com/docs/art/characters/creating/export-character).

<Alert severity = 'warning'>
It's important to test your assets multiple times at every point of the asset creation process, whether it is within Blender or after importing into Studio. See [[external/roblox-creator-docs/avatar/character-bodies/test|Test characters]] for more information.
</Alert>

Whether you are exporting your character for testing, or are performing a final export out of Blender, you must apply the appropriate export settings to ensure that Blender exports the proper character data.

To export your character:

1. In the topbar, navigate to **File** > **Export** > **FBX (.fbx)**. The Blender file browser window displays.
1. Set **Path Mode** to **Copy** and enable the **Embed Textures** icon.
1. In the **Include** section, enable **Custom Properties**.
1. Expand the **Armature** section and disable **Add Leaf Bones**.
1. Enable **Bake Animation**, expand the section, then:

   1. Disable **NLA Strips**, **All Actions**, and **Force Start/End Keyframes**.
   1. Set **Simplify** to **0.0**.

1. Click the **Export FBX** button and save the `.fbx` to the directory of your choice.

<img src="../../../assets/art/avatar/basic-creation/Export-Settings.png" width = "60%" />

<Alert severity = 'warning'>
After exporting your .fbx file, see [[external/roblox-creator-docs/avatar/character-bodies/test|Test character bodies]] for steps on importing your character model into a test place and verifying your avatar and related components.
</Alert>

<Alert severity = 'success'>
After importing the `Class.Model` character to Studio, you can now perform the following with this asset:

- [[external/roblox-creator-docs/marketplace/publish-to-marketplace|Upload the character]] to the Marketplace.
- Use the humanoid character on an existing game by applying a [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|HumanoidDescription]]to the `Class.Model` object.
- Save the asset to your [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] to share or use within any of your games.

</Alert>


## Related Files

- [[external/roblox-creator-docs/art/characters/creating/blender-configurations]] - Blender configuration.
- [[external/roblox-creator-docs/art/characters/creating/caging]] - Caging character head.
- [[external/roblox-creator-docs/art/characters/creating/combine-head-geometry]] - Combine head geometry.
- [[external/roblox-creator-docs/art/characters/creating/index]] - Create with templates.
- [[external/roblox-creator-docs/art/characters/creating/export-textures]] - Export textures.
- [[external/roblox-creator-docs/art/characters/creating/final-checks]] - Final checks.
- [[external/roblox-creator-docs/art/characters/creating/modeling-best-practices]] - Modeling best practices.
- [[external/roblox-creator-docs/art/characters/creating/modeling-tips]] - Modeling tips.
- [[external/roblox-creator-docs/art/characters/creating/texturing-pbr]] - PBR textures (optional).
- [[external/roblox-creator-docs/art/characters/creating/remove-extra-bones]] - Remove extra bones.
- [[external/roblox-creator-docs/art/characters/creating/sculpting]] - Sculpt the head.
- [[external/roblox-creator-docs/art/characters/creating/template-files]] - Template files.
- [[external/roblox-creator-docs/art/characters/creating/head-objects]] - Template head structure.
- [[external/roblox-creator-docs/art/characters/creating/texturing-eyes]] - Texturing eyes.
- [[external/roblox-creator-docs/art/characters/creating/texturing-face]] - Texturing face.
- [[external/roblox-creator-docs/art/characters/creating/texturing-setup]] - Texturing setup.
- ...and 1 more local docs.
