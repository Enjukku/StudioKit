---
title: Reassign textures
description: To import custom makeup, replace the existing textures on the head template with your custom textures.
tags: [roblox, documentation, external-reference, priority-reference, avatar, makeup]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [makeup/reassign-textures.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/makeup/reassign-textures.md). Published page: [https://create.roblox.com/docs/makeup/reassign-textures](https://create.roblox.com/docs/makeup/reassign-textures).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/makeup/reassign-textures]]. Kept locally so existing links keep working; read that page for current information.

To import custom makeup textures, use Blender or Maya to reassign the existing textures on the reference template head to your custom texture images. After replacing the textures, export the entire head model, then [[external/roblox-creator-docs/makeup/import|import]] it into Roblox Studio.

<Alert severity = 'warning'>
The following information is **specific for applying makeup textures to the Roblox provided head reference**, which already has PBR texture nodes assigned. For more information on assigning textures from scratch, see [[external/roblox-creator-docs/art/modeling/assign-textures|Assign textures in Blender and Maya]].
</Alert>

## Blender

<iframe width="800" height="450" src="https://www.youtube-nocookie.com/embed/B0y5fLlwkF0" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe><br /><br />

<Alert severity ='info'>
The video presenter opts to clear all existing image links by navigating to **File** > **External Data** > **Unpack Resources** and selecting **Remove Pack**. This is a method to unassign all images instead of individually unassigning textures like step #5 in the following instructions.
</Alert>

To reassign textures in Blender:

1. Unzip and open the [[external/roblox-creator-docs/makeup/index#template-heads|Blender reference head file]].
2. Switch to the **Shading** tab.
3. In the Outliner, expand the Makeup collection and select the face region you intend to replace textures for.

    <img src="../assets/makeup/resources/Blender-Select-Region.png" width="40%" />

4. In the node graph, select the texture image you intend to update, such as `Neutral_FaceDecal_ALB.png`
5. Click the **X** to remove the existing image assignment.

    <img src="../assets/makeup/resources/Blender-Unlink-Image.png" width="40%" />

6. Click the folder icon to browse for a new image.

    <img src="../assets/makeup/resources/Blender-Assign-New.png" width="40%" />

7. Repeat for all PBR textures that you intend to replace.
8. Delete any texture nodes you are not using.
9.  Verify your final node graph looks similar to the original reference with nothing unintentionally missing.
    <img src="../assets/makeup/resources/Blender-Expected-Nodes.png" width="90%" />

<Alert severity ='info'>
After replacing your PBR textures, export the entire template file as a `.fbx`or `.gltf`. All 3D modeling [[external/roblox-creator-docs/art/modeling/export-requirements|export requirements]] apply, but there are a few makeup-specific settings you must configure:

   1. In the export file brower window, navigate to the **Include** section, then enable the **Custom Properties** toggle for makeup UV data transfer data purposes.
   1. In the **Armature** section, enable **Only Deform Bones** to ensure your export file includes skinning data for eyebrows and eyelashes.

       <figure><img src="../assets/makeup/Blender-MakeupExport.png" /><figcaption>All necessary Blender export settings for makeup</figcaption></figure>

</Alert>

## Maya

<iframe width="800" height="450" src="https://www.youtube-nocookie.com/embed/JaX5rcsStvQ" title="YouTube video player" frameborder="0" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen></iframe><br /><br />

To reassign textures in Blender:

1. Unzip and open the Maya [[external/roblox-creator-docs/makeup/index#template-heads|reference head file]].
2. In the Status Line near the top of the default layout, click on the Hypershade icon.

   <img src="../assets/makeup/resources/Maya-Select-Hypershade.png" width="65%" />

3. Move your mouse over the material's texture you intend to replace.
4. Click and hold right mouse-click and drag the selector to **Graph Network**.
  
   <img src="../assets/makeup/resources/Maya-Select-Graph-Network.png" width="65%" />

5. In the newly displayed node graph, click on the Texture Node you intend to replace, such as `Neutral_Eyes_ALB.png`.
6. In the right Property Editor, navigate to Image Name and click the folder icon. A file browser displays.

  <img src="../assets/makeup/resources/Maya-Replace-Texture.png" width="90%" />

1. Select the texture image file you want to use as a replacement.
2. Repeat for all PBR textures that you intend to replace.
3. Delete any texture nodes you are not using.
4.  Verify your final node graph looks similar to the original reference with nothing unintentionally missing.

  <img src="../assets/makeup/resources/Maya-Expected-Nodes.png" width="90%" />
  
<Alert severity ='info'>
After replacing your PBR textures, export the entire template file as a `.fbx`or `.gltf`. All 3D modeling [[external/roblox-creator-docs/art/modeling/export-requirements|export requirements]] apply, but there are a few makeup-specific settings you must configure:

   1. In the export file brower window, navigate to the **Deformed Models** section.
   1. Enable the **Skins** toggle to ensure your export file includes skinning data for eyebrows and eyelashes.

       <img src="../assets/makeup/Maya-MakeupExport.png" />

</Alert>


## Related Files

- [[external/roblox-creator-docs/art/modeling/assign-textures]] - Blender and Maya texture settings.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/makeup/import]] - Import into Studio.
- [[external/roblox-creator-docs/makeup/index]] - Makeup.
- [[external/roblox-creator-docs/makeup/specifications]] - Makeup specifications.
