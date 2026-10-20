---
title: Import character bodies
description: Use the Importer to add third-party models to Studio before testing, using, or uploading the character model.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/import.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/import.md). Published page: [https://create.roblox.com/docs/art/characters/import](https://create.roblox.com/docs/art/characters/import).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/character-bodies/import]]. Kept locally so existing links keep working; read that page for current information.

Studio's 3D Importer lets you import 3D assets into your projects, such as avatar clothing, accessories, and character bodies. The following instructions provide guidance on how to import a full character model into Studio as a `Model` object that you can save to use in your experience, share with others, or upload to the Marketplace.

<Alert severity ='info'>
If you are using a single-mesh character body for the Roblox Auto-Setup tool, see [[external/roblox-creator-docs/avatar-setup/index|Avatar auto-setup]].
</Alert>

While the 3D Importer provides object previews and error-checking to ensure that your asset meets Roblox's [[external/roblox-creator-docs/art/modeling/specifications|general 3D requirements]], it's important to ensure that your character model meets Roblox's [[external/roblox-creator-docs/art/characters/specifications|avatar character specifications]] to use or sell this asset as an avatar-ready character model, otherwise you can encounter errors at different points in the workflow.

To import your asset as a character model:

1. In the **Home** tab, click the **Import** button to open the 3D Importer. A file browser opens.
1. Select your rigged character's `.fbx` or `.gltf` file. The 3D Importer loads a preview of the character model.

    <img src="../../assets/art/avatar/Avatar-3D-Importer.png" width = "60%"/>

   - If textures don't load for your asset, you can manually import your textures later.
   - For additional information on import settings and troubleshooting, see [[external/roblox-creator-docs/studio/importer|3D importer]].

1. In the **Rig General** section,

   1. Set **Rig Scale** to the appropriate [[external/roblox-creator-docs/art/characters/specifications#body-scale|Body Scale]] of your character.
   1. Set **Constraint Type** to **Joint Upgrade**.

   <img src="../../assets/art/avatar/Rig-General.png" width = "60%"/>

1. Select **Import**. The asset populates in your workspace as a `Class.Model` with the appropriate textures applied as a `Class.SurfaceAppearance` or `Class.MeshPart.TextureID`.

<BaseAccordion>
<AccordionSummary>Manually add textures</AccordionSummary>
<AccordionDetails>
 If textures didn't load correctly, add them manually. You may need to save and publish your experience in order to access the [[external/roblox-creator-docs/projects/assets/manager|Asset Manager]].

1.  In the **Asset Manager**, click the **Import** button.
2.  Upload your image files.
3.  After moderation clears for your image, select the `Class.MeshPart` parented within your imported `Class.Model`.
4.  If you are using a single basic texture, set the `Class.MeshPart.TextureID` property to your uploaded texture image.
5.  If you are using PBR textures:

    1. Add a `Class.SurfaceAppearance` child to your `Class.MeshPart`.

       <img src="../../assets/art/avatar/Avatar-Surface-Appearance.png" />

    2. In the `Class.SurfaceAppearance` properties, click each property value and assign the appropriate texture image from the asset dropdown:

       1. Set the **ColorMap** to the **\_ALB** texture image.
       2. Set the **MetalnessMap** to the **\_MTL** texture image.
       3. Set the **NormalMap** to the **\_NOR** texture image.
       4. Set the **RoughnessMap** to the **\_RGH** texture image.

       <img src="../../assets/art/avatar/Avatar-Roughness-Map.png" />

</AccordionDetails>
</BaseAccordion>

<Alert severity = 'success'>
After successful import, your model object should populate in your project as a `Class.Model` with the appropriate textures applied.
</Alert>

After successful fitting and converting, your 3D model should populate in your project as an `Class.Model`.

      <GridContainer numColumns="2">
      <figure>
         <img src="../../assets/art/avatar/Avatar-Studio-Example.png" />
         <figcaption>Avatar-ready character model in Workspace</figcaption>
      </figure>
      <figure>
         <img src="../../assets/art/avatar/Avatar-Data-Model.png" />
         <figcaption>Avatar-ready character model in Explorer</figcaption>
      </figure>
      </GridContainer>

<Alert severity = 'warning'>
Character creation is a complex process that requires lots of testing and iteration. See [[external/roblox-creator-docs/art/characters/testing/index|Test characters]] for steps on importing your character model into a test place and verifying your avatar and related components.
</Alert>

With this new character `Class.Model`, you can perform any of the following:

- Begin the process of [[external/roblox-creator-docs/marketplace/publish-to-marketplace#upload-an-asset|uploading and publishing]] the character model to the Marketplace. This involves some additional validation and moderation steps.
- Use the [[external/roblox-creator-docs/characters/adaptive-animation|Adaptive Animation]] plugin to remap your joints and set a baseline t-pose reference to better support your animations.
- Use the model in your current experience and modify the model's appearance with [[external/roblox-creator-docs/characters/appearance#manually-modify-appearance|HumanoidDescription]].

  - Playtest as the character by renaming the `Class.Model` to `StarterCharacter` and moving the `Class.Model` to the `Class.StarterPlayer` folder in the **Explorer** before play testing.

- Save the model to your [[external/roblox-creator-docs/projects/assets/toolbox|Toolbox]] or make it public on the [[external/roblox-creator-docs/production/creator-store|Creator Store]] to share or use within any of your experiences.


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/characters/adaptive-animation]] - Adaptive Animation.
- [[external/roblox-creator-docs/projects/assets/manager]] - Asset Manager.
- [[external/roblox-creator-docs/art/characters/index]] - Avatar characters.
- [[external/roblox-creator-docs/art/characters/project-files]] - Avatar project files and references.
- [[external/roblox-creator-docs/avatar-setup/index]] - Avatar Setup.
- [[external/roblox-creator-docs/art/characters/validation-tool]] - Blender validation tool.
- [[external/roblox-creator-docs/characters/appearance]] - Character appearance.
- [[external/roblox-creator-docs/art/characters/export-settings]] - Character body export settings.
- [[external/roblox-creator-docs/art/characters/specifications]] - Character specifications.
- [[external/roblox-creator-docs/art/characters/head-comparison]] - Classic and Dynamic head comparison.
- [[external/roblox-creator-docs/production/creator-store]] - Creator Store.
- [[external/roblox-creator-docs/art/characters/export-avatar-animations-from-maya]] - Export avatar animations from Maya.
- [[external/roblox-creator-docs/art/characters/face-caging-best-practices]] - Face caging best practices.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/studio/importer]] - Importer.
- [[external/roblox-creator-docs/marketplace/publish-to-marketplace]] - Publish to Marketplace.
- [[external/roblox-creator-docs/art/characters/testing/index]] - Testing characters.
- [[external/roblox-creator-docs/projects/assets/toolbox]] - Toolbox.
