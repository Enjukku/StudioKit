---
title: Texturing setup
description: Set up Blender to optimize your project for texturing the eyes and face of your template.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
next: /art/characters/creating/texturing-eyes
prev: /art/characters/creating/sculpting
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/characters/creating/texturing-setup.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/characters/creating/texturing-setup.md). Published page: [https://create.roblox.com/docs/art/characters/creating/texturing-setup](https://create.roblox.com/docs/art/characters/creating/texturing-setup).

**Texturing** is the process of customizing the color, tone, and shading of your model's surface. Custom meshes and models use a 2D image, known as a texture map, to project various surface appearance elements onto your 3D object.

<GridContainer numColumns="2">
  <figure><img src="../../../assets/art/avatar/basic-creation/Pre-Texturing.png" />  <figcaption>Model after custom sculpting</figcaption></figure>

  <figure><img src="../../../assets/art/avatar/basic-creation/Post-Texturing.png" /><figcaption>Model after texturing</figcaption></figure>
</GridContainer>

Each template comes with a color texture map, which you can alter and modify using Blender's texture editing tools. Since most Roblox avatars can take advantage of custom skin tones, it's important to understand how to [[external/roblox-creator-docs/art/characters/creating/blender-configurations#preview-skin-tones|preview custom skin tones]] in Blender to verify how your final asset will look in a Roblox game.

For the purpose of demonstrating the basic texturing process, this tutorial goes over basic texture painting setup, applies a completely opaque texture over parts of the character eyes, and partially opaque details over the face. You can apply these same techniques to other parts of your character geometry.

<Alert severity = 'warning'>
When texturing parts of your character model's body, ensure that your character model includes a modesty layer over sensitive regions. For more information, see [[external/roblox-creator-docs/marketplace/marketplace-policy#modesty-layers|Marketplace policy - Modesty layers]].
</Alert>

## Texture settings

If you're using a Blender downloadable template, it's important to keep in mind that Blender requires you to **manually** save your textures in the Texture Paint tab's 2D view window. If you just save your `.blend` project file, your textures do **_not_** save with it. This can cause you to lose hours of work if you don't periodically save your progress as you go.

<img src="../../../assets/art/avatar/basic-creation/Blender-Save-Image.png" width="80%"/>

Blender 5.2 and later versions offer a texture setting to override this behavior:

1. In the topbar, navigate to **Edit** > **Preferences**. The **Preferences** window displays.
1. In the vertical navigation, select the **Save & Load** tab.
1. In the **Blend Files** section, set **Save Modified Images** to **Always Save**.

   <img src="../../../assets/art/avatar/basic-creation/Blender-Always-Save-Setting.png" width="80%"/>

## Set texture resolution

Roblox Studio supports a texture resolution of **1024 x 1024** for albedo texture maps. When using applications like Blender or Maya to texture paint directly on a model, extremely fine details may not paint as expected due to the resolution and level of detail of the painting.

<GridContainer numColumns="2">
  <figure><img src="../../../assets/art/avatar/basic-creation/Texture-Resolution-A.png" />  <figcaption>Texture painting at 1024 x 1024 resolution</figcaption></figure>

  <figure><img src="../../../assets/art/avatar/basic-creation/Texture-Resolution-B.png" /><figcaption>Texture painting at 2048 x 2048 resolution</figcaption></figure>
</GridContainer>

When adding fine details to your texture, increase the image resolution of your texture map temporarily to **2048 x 2048** or **4096 x 4096**. After completing your texturing, change the image resolution back to **1024 x 1024** to bake in the changes.

To change your texture image resolution:

1. In the **Layout** tab, select the `Head_Geo`.
1. Switch to the **Texture Paint** tab, then in the 2D view window, select **Image** > **Resize**.
1. Set the texture size:
   - Use **2048** or **4096** for a higher resolution when creating detailed texture work.
   - Use **1024** for the default Roblox-supported resolution.

      <video controls src="../../../assets/art/avatar/basic-creation/Texturing_09.mp4" width="100%"></video>


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
- [[external/roblox-creator-docs/art/characters/creating/head-objects]] - Template head structure.
- [[external/roblox-creator-docs/art/characters/creating/texturing-eyes]] - Texturing eyes.
- [[external/roblox-creator-docs/art/characters/creating/texturing-face]] - Texturing face.
- ...and 1 more local docs.
