---
title: Layered clothing
description: Layered clothing are cosmetic accessories that stretch, fit, and layer over any body type simulating real-life clothing.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/accessories/layered-clothing.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/accessories/layered-clothing.md). Published page: [https://create.roblox.com/docs/art/accessories/layered-clothing](https://create.roblox.com/docs/art/accessories/layered-clothing).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/layered-accessories/index]]. Kept locally so existing links keep working; read that page for current information.

<Grid container spacing={2} style={{ marginBottom: 24, width: '100%' }}>
<Grid item xs={6} style={{ padding: 16 }}>
<Grid item container wrap="nowrap" direction="column" style={{ gap: 8, flex: 1 }}>

<div
className="container"
style={{ position: "relative", paddingBottom: "56.25%", height: 0, marginBottom: 12 }} >
<iframe
src="https://www.youtube-nocookie.com/embed/gXXukd6yOSs"
title="YouTube video player"
frameBorder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowFullScreen
style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%" }} ></iframe>
</div>
<Typography variant="body1">
A high-level overview of 3D clothing on Roblox.
</Typography>

</Grid>
</Grid>

<Grid item xs={6} style={{ padding: 16 }}>
<Grid item container wrap="nowrap" direction="column" style={{ gap: 8, flex: 1 }}>

<div
className="container"
style={{ position: "relative", paddingBottom: "56.25%", height: 0, marginBottom: 12 }} >
<iframe
src="https://www.youtube-nocookie.com/embed/C-DwGRBHvmE"
title="YouTube video player"
frameBorder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowFullScreen
style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%" }} ></iframe>
</div>
<Typography variant="body1">
Create and sell your first basic layered clothing.
</Typography>
</Grid>
</Grid>
</Grid>

Layered clothing accessories are 3D cosmetic items that users can equip and wear on their avatar body, such as pants, t-shirt, jackets, dresses, and more. Unlike [[external/roblox-creator-docs/art/accessories/index|rigid accessories]] that only attach to a specific point on a character, layered clothing stretches and fits over any body type and existing clothing.

To create a custom Roblox accessory for your own experience or to sell on the Marketplace, it's important to start with the following:

- A general background with 3D modeling tools such as [Blender](https://www.blender.org/) or [Maya](https://www.autodesk.com/products/maya/overview).
- An understanding of the [components that make up a layered accessory](#components-of-a-layered-clothing-accessory).
- An understanding of the general [clothing creation process](#creation-process).
- Review Roblox's official tutorials to create your own accessories:
  - [[external/roblox-creator-docs/art/accessories/creating-rigid/index|Rigid accessory creation tutorial]] - covers each process required for converting a 3D model to a rigid accessory and publishing it to the Marketplace.
  - [[external/roblox-creator-docs/art/accessories/creating/index|Clothing creation tutorial]] - a step-by-step process of creating your own avatar-ready clothing from scratch in Blender.
- [Additional tools, resources, and guides](#resources) provided by Roblox to standardize and expedite the creation process.

<Alert severity = 'warning'>
If you are a developer and are looking for information on manually equipping or configuring layered clothing accessories within an experience, including [[external/roblox-creator-docs/characters/appearance#layered-clothing-on-non-r15|implementing layered clothing on a non-standard character model]], see [[external/roblox-creator-docs/characters/appearance|Character appearance]].
</Alert>

Roblox also supports [classic clothing](#classic-clothing), 2D images that can be applied to your character's surface.

## Components of a layered clothing accessory

All accessory models are made up of the same base components of a [mesh object](#mesh-part), [textures](#textures), and [attachment](#attachments). Layered clothing requires additional components, such as a [poseable rig](#rigging-armature), and an [inner and outer cage](#inner-and-outer-cages), to allow the asset to stretch, fit, and layer over a target character and existing clothing items.

When [creating accessories](#creation-process), all of the components are created first in your modeling software, then converted to their appropriate Roblox Studio instance on import.

### Mesh part

<GridContainer numColumns="2">

<figure><img src="../../assets/art/accessories/Mesh-Example.png"/>  <figcaption>T-shirt clothing mesh object</figcaption></figure>

<figure><img src="../../assets/art/accessories/Mesh-Bow-Example.png" /><figcaption>Bow accessory mesh object</figcaption></figure>
</GridContainer>

<Alert severity = 'warning'>
Simple accessories, such as the bow, are [[external/roblox-creator-docs/art/accessories/index|rigid accessories]] do not require the rigging and caging components that allow it to stretch and fit over a target.
</Alert>

All accessories require a single mesh object that represents the geometry of the accessory object. In Studio, this mesh object is represented as a `Class.MeshPart` nested under a single `Class.Model`

### Textures

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/accessories/Texture-Example.png" />  <figcaption>2D texture map for the t-shirt model</figcaption></figure>

  <figure><img src="../../assets/art/accessories/Texture-Applied-Example.png" /><figcaption>T-shirt model with texture applied</figcaption></figure>
</GridContainer>

Textures are image files that define the surface appearance of your accessory. You can create textures within a texture painting program or a 3D modeling software. In Studio, textures images are imported as image assets and are set to `Class.MeshPart` objects by a child `Class.SurfaceAppearance` object or a `Class.MeshPart.TextureID` property.

### Attachments

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/accessories/Attachment-Example.png" />  <figcaption>Attachment geometry defines where the attachment connects with the character</figcaption></figure>

  <figure><img src="../../assets/art/accessories/Attachment-Data-Model-Example.png" width="80%"/><figcaption>Geometry with the "_Att" suffix automatically convert to `Class.Attachment` objects in Studio</figcaption></figure>
</GridContainer>

For layered clothing, the attachment point is used to associate with the correct body part when the body ragdolls or is dismembered. In Studio, attachments are represented by `Class.Attachment` objects.

Attachments for clothing items are automatically generated in Studio using the [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]].

### Rigging armature

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/accessories/Rigging-Example.png" />  <figcaption>To ensure natural movement of the clothing item, it must be weighted to a character rig</figcaption></figure>

  <figure><img src="../../assets/art/accessories/Rigging-Pose-Example.png" /><figcaption>When the rig is properly set up, the layered model can move and bend with the character rig</figcaption></figure>
</GridContainer>

A rigging armature defines how a layered asset can move with a character model. Using rigging and skinning techniques, you can set the areas of your clothes to move naturally with a character model's joints, such as ensuring a shirt sleeve correctly follows the movement of the elbow and shoulder. In Studio, this rigging and skinning data is saved to the mesh geometry.

### Inner and outer cages

<GridContainer numColumns="2">
  <figure><img src="../../assets/art/accessories/Inner-Cage-Example.png" />  <figcaption>The inner cage defines the inner surface of the clothing item where the clothes wrap over</figcaption></figure>

  <figure><img src="../../assets/art/accessories/Outer-Cage-Example.png" /><figcaption>The outer cage defines the outer surface of the clothing item where any additional clothes can wrap and layer over</figcaption></figure>
</GridContainer>

Cage meshes indicate the inner and outer surfaces of a layered accessory. The inside cage of a t-shirt defines how the t-shirt stretches and fits over a character body. The outer cage of a t-shirt defines how additional layered clothing fit over the t-shirt. In Studio, these cages are represented by `Class.WrapLayer` objects.

## Creation process

Custom accessories are first created in 3D modeling programs, such as [Blender](https://www.blender.org/) or [Maya](https://www.autodesk.com/products/maya/overview), before importing the `.fbx` or `.gltf` model into Studio.
To get started creating your first avatar asset, see [[external/roblox-creator-docs/avatar/tutorials|Avatar Tutorials]].

Depending on the type of asset you are creating, the creation process follows these high-level workflows:

<GridContainer numColumns="2">
  <figure><figcaption><center>Layered Accessory Workflow</center></figcaption><br /><img src="../../assets/art/accessories/Workflow-Layered.png"/></figure>  
  
  <figure>  <figcaption><center>Rigid Accessory Workflow</center></figcaption><br /><img src="../../assets/art/accessories/Workflow-Rigid.png" /></figure>

</GridContainer>

<Alert severity = 'info'>
Since 3D creation isn't a linear process and always requires reiteration and testing, the process of creating an accessory can differ between individuals and various creation workflows.
</Alert>

## Resources

There are a variety of resources available for creators of all backgrounds to get started with accessory creation.

If you are interested in specific avatar creation topics, use the following table to find guides and resources that best match your needs:

<table>
<thead>
  <tr>
    <th>Topic</th>
    <th>Resources</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Tutorials</td>
    <td>[[external/roblox-creator-docs/art/accessories/creating-rigid/index|Rigid accessory creation]] <br /><br />[[external/roblox-creator-docs/art/accessories/creating/index|Basic clothing creation]]</td>
  </tr>
  <tr>
    <td>Reference files</td>
    <td>[[external/roblox-creator-docs/art/modeling/project-files|Accessory and clothing reference files]]</td>
  </tr>
  <tr>
    <td>Technical specs</td>
    <td>[[external/roblox-creator-docs/art/modeling/export-requirements|.FBX export settings]]<br /><br />[[external/roblox-creator-docs/art/modeling/specifications|General mesh specifications]]<br /><br />[[external/roblox-creator-docs/art/accessories/specifications|Accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]]</td>
  </tr>
  <tr>
    <td>Cosmetic creation</td>
    <td>[[external/roblox-creator-docs/art/accessories/specifications|Accessories overview]]<br /><br />[[external/roblox-creator-docs/art/accessories/index|Layered clothing overview]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-face-accessories|Create face accessories]]<br /><br />[[external/roblox-creator-docs/art/accessories/accessory-fitting-tool|Accessory Fitting Tool]]<br /><br />[[external/roblox-creator-docs/art/accessories/specifications|Accessory specifications]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace requirements]]</td>
  </tr>
  <tr>
    <td>Texturing</td>
    <td>[[external/roblox-creator-docs/art/modeling/texture-specifications|Texturing requirements]]<br /><br />[[external/roblox-creator-docs/art/modeling/surface-appearance|PBR textures]]</td>
  </tr>
  <tr>
    <td>Rigging and skinning</td>
    <td>[[external/roblox-creator-docs/art/modeling/rigging|Rigging and skinning overview]]<br /><br />[[external/roblox-creator-docs/art/characters/specifications#rigging|Humanoid rigging requirements]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#rigging|Rigging facial bones]]<br /><br />[[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer|Auto skin transfer]]<br /><br />[[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads#skin-face-bones|Skin facial bones]]</td>
  </tr>
  <tr>
    <td>Testing and validation</td>
    <td>[[external/roblox-creator-docs/art/modeling/calisthenics-tool|Calisthenics tool]]<br /><br />[[external/roblox-creator-docs/art/accessories/validation-tool|Clothing validation tool]]</td>
  </tr>
  <tr>
    <td>Publishing and Marketplace</td>
    <td>[[external/roblox-creator-docs/marketplace/publish-to-marketplace|Upload to Marketplace]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-policy|Marketplace policy]]<br /><br />[[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions|Fees and commissions]]</td>
  </tr>
</tbody>
</table>

## Classic clothing

Classic clothing assets are 2D images that you can apply to the surface of an avatar body as t-shirts, shirts, or pants. You can design these assets in any image processing software, test the textures in Studio, and then upload the designs to the Marketplace to sell. See [[external/roblox-creator-docs/art/classic-clothing|Classic clothing]] for more information on creating, uploading, and selling these assets.

<img src="../../assets/accessories/classic-clothing/Block-Avatar-Dressed.jpg" width="800" />


## Related Files

- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/accessories/from-existing]] - Accessories from an existing model.
- [[external/roblox-creator-docs/art/accessories/accessory-fitting-tool]] - Accessory Fitting Tool.
- [[external/roblox-creator-docs/art/accessories/project-files]] - Accessory project files and references.
- [[external/roblox-creator-docs/art/accessories/automatic-skinning-transfer]] - Automatic Skinning Transfer.
- [[external/roblox-creator-docs/art/accessories/creating/index]] - Basic clothing creation.
- [[external/roblox-creator-docs/art/accessories/body-scale]] - Body scale and proportions.
- [[external/roblox-creator-docs/art/accessories/caging-best-practices]] - Caging best practices.
- [[external/roblox-creator-docs/art/modeling/calisthenics-tool]] - Calisthenics Tool.
- [[external/roblox-creator-docs/characters/appearance]] - Character appearance.
- [[external/roblox-creator-docs/art/characters/specifications]] - Character specifications.
- [[external/roblox-creator-docs/art/classic-clothing]] - Classic clothing.
- [[external/roblox-creator-docs/art/accessories/clothing-specifications]] - Clothing specifications.
- [[external/roblox-creator-docs/art/accessories/validation-tool]] - Clothing Validation Tool.
- [[external/roblox-creator-docs/art/characters/facial-animation/create-basic-heads]] - Create basic heads.
- [[external/roblox-creator-docs/art/characters/facial-animation/create-face-accessories]] - Create face accessories.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions]] - Marketplace fees and commissions.
- [[external/roblox-creator-docs/marketplace/marketplace-policy]] - Marketplace policy.
- ...and 9 more local docs.
