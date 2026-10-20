---
title: Test classic clothing
description: How to test your classic clothing items before uploading them to the Marketplace.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/test-classic-clothing.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/test-classic-clothing.md). Published page: [https://create.roblox.com/docs/art/test-classic-clothing](https://create.roblox.com/docs/art/test-classic-clothing).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/classic-clothing]]. Kept locally so existing links keep working; read that page for current information.

<Alert severity="warning">
Many user-generated avatars on the Marketplace do not support 2D classic clothing. For information on creating modern 3D cosmetics, including rigid accessories and clothing items, see [[external/roblox-creator-docs/avatar/index|Get started]].
</Alert>

To ensure the best quality results, you can test your classic clothing before uploading or selling. You can test your clothes without needing to pay any fees by using [[external/roblox-creator-docs/studio/setup|Roblox Studio]].

1. From the toolbar's **Avatar** tab, click **Character**.
2. Choose a **Block Avatar** rig type from the popup menu. An avatar mannequin named **Rig** appears in the 3D workspace.

   <img src="../assets/accessories/classic-clothing/Block-Avatar-Default.jpg" width="800" />

3. In the **Explorer** window, hover over the **Rig** object, click the **&CirclePlus;** button and insert either a **ShirtGraphic** (T‑shirt), **Shirt**, or **Pants** object according to the clothing you want to test.

4. Locate and select the new **Shirt Graphic** or **Clothing** object parented under **Rig**.

   <Grid container spacing={3}>
   <Grid item>
	 <figure>
	 <img src="../assets/studio/explorer/Rig-Shirt-Graphic.png" width="320" />
	 <figcaption>Shirt Graphic (T-shirt)</figcaption>
	 </figure>
	 </Grid>
	 <Grid item>
	 <figure>
	 <img src="../assets/studio/explorer/Rig-Clothing.png" width="320" />
	 <figcaption>Clothing (Shirt/Pants)</figcaption>
	 </figure>
	 </Grid>
	 </Grid>

5. In the **Properties** window, locate the associated property as follows:

	 <table>
	 <thead>
	 <tr>
	   <th>Clothing Type</th>
	   <th>Parent Class</th>
	   <th>Property</th>
	 </tr>
	 </thead>
	 <tbody>
	 <tr>
	   <td>**T-Shirt**</td>
	   <td>`Class.ShirtGraphic`</td>
	   <td>`Class.ShirtGraphic.Graphic|Graphic`</td>
	 </tr>
	 <tr>
	   <td>**Shirt**</td>
	   <td>`Class.Shirt`</td>
	   <td>`Class.Shirt.ShirtTemplate|ShirtTemplate`</td>
	 </tr>
	 <tr>
	   <td>**Pants**</td>
	   <td>`Class.Pants`</td>
	   <td>`Class.Pants.PantsTemplate|PantsTemplate`</td>
	 </tr>
	 </tbody>
	 </table>

6. Click inside the property's row and select the image you uploaded to Roblox. This applies the clothing texture to the **Rig** character.

   <img src="../assets/accessories/classic-clothing/Block-Avatar-Dressed.jpg" width="800" />

<Alert severity="success">
After testing, you can [[external/roblox-creator-docs/art/upload-classic-clothing|upload and sell]] your asset to the Marketplace.
</Alert>


## Related Files

- [[external/roblox-creator-docs/art/overview-studio]] - 3D art and Studio.
- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/blender]] - Blender.
- [[external/roblox-creator-docs/art/classic-clothing]] - Classic clothing.
- [[external/roblox-creator-docs/avatar/index]] - Create avatar items.
- [[external/roblox-creator-docs/art/reaper]] - Reaper.
- [[external/roblox-creator-docs/studio/setup]] - Roblox Studio setup.
- [[external/roblox-creator-docs/art/upload-classic-clothing]] - Upload classic clothing.
- [[external/roblox-creator-docs/art/validation-errors]] - Validation Errors.
- [[external/roblox-creator-docs/art/overview-dcc]] - Work with third-party software.
