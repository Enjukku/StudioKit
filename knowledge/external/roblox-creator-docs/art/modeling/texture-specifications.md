---
title: Texture specifications
description: Texture Specifications lists the specific technical requirements and best practices for custom textures created outside of Studio.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/modeling/texture-specifications.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/modeling/texture-specifications.md). Published page: [https://create.roblox.com/docs/art/modeling/texture-specifications](https://create.roblox.com/docs/art/modeling/texture-specifications).

A **texture** is a digital image applied to the surface of a 3D object to simulate and enhance its visual appearance. Roblox supports various texture types that you import with a custom 3D object, or upload directly as individual image files. For details on implementing basic textures, see [[external/roblox-creator-docs/parts/textures-decals|textures and decals]].

Roblox also supports [[external/roblox-creator-docs/art/modeling/surface-appearance|physically-based rendering (PBR) textures]] which override a mesh's existing `Class.MeshPart.TextureID|TextureID` and can be used to create immersive environments and objects.

<Alert severity = 'info'>
For information on how to properly connect textures to your model in Blender and Maya for import into Studio, see [[external/roblox-creator-docs/art/modeling/assign-textures|Blender / Maya texture settings]].
</Alert>

See the following requirements when creating your own basic and advanced textures:

- **File formats** — File formats for textures that are uploaded separately in Studio must be submitted as a `.png`, `.jpg`, `.tga`, or `.bmp`.

- **Resolution** — Roblox supports up to 4096×4096 pixel texture resolutions (4K). As a game loads, the engine automatically starts with lower quality versions of the texture and ramps up quality based on device resources. Even still, manually sizing textures before you upload them can improve memory usage in some situations. Consider the following general guidance:

  - For smaller 5×5 stud objects, use 256×256 texture resolutions.
  - For medium 10×10 stud objects, use 512×512 texture resolutions.
  - For larger 20×20 stud objects, use 1024×1024 texture resolutions.
  - See [PBR texture budgets](#surface-appearance) for similar guidances with PBR texture maps.

- **Single material** — Mesh objects can only have one material assigned.

<Alert severity ='info'>
Roblox default [[external/roblox-creator-docs/parts/materials|materials]] follow a similar texel resolution pattern:
- Parts display a 1024×1024 on an 8×8 stud face.
- Terrain displays 512×512 across 8×8 studs.
</Alert>

## Surface appearance

You can add a [[external/roblox-creator-docs/art/modeling/surface-appearance|surface appearance]] to your mesh in Studio to add PBR texture options. The `Class.SurfaceAppearance` instance uses UV mapping, a form of texture mapping, to accurately map 2D images onto the mesh object.

<Alert severity = 'info'>
For information on how to properly connect PBR textures to your model in Blender and Maya for import into Studio, see [[external/roblox-creator-docs/art/modeling/assign-textures|Blender / Maya texture settings]].
</Alert>

See the following requirements for `Class.SurfaceAppearance` assets:

<Tabs>
<TabItem label="Texture Files">
When possible, texture files should include the appropriate name affix and follow the appropriate image details:

<table>
  <thead>
    <tr>
      <th>Texture&nbsp;type</th>
      <th>Texture image details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[[external/roblox-creator-docs/art/modeling/surface-appearance#color-albedo|Albedo]]</td>
      <td>RGB (24-bit)</td>
    </tr>
    <tr>
      <td>[[external/roblox-creator-docs/art/modeling/surface-appearance#normal|Normal]]</td>
      <td>RGB (24-bit); Roblox only supports **OpenGL format - Tangent Space** normal maps</td>
    </tr>
    <tr>
      <td>[[external/roblox-creator-docs/art/modeling/surface-appearance#roughness|Roughness]]</td>
      <td>Single Channel Grayscale (8-bit)</td>
    </tr>
    <tr>
      <td>[[external/roblox-creator-docs/art/modeling/surface-appearance#metalness|Metalness]]</td>
      <td>Single Channel Grayscale (8-bit)</td>
    </tr>
    <tr>
      <td>[[external/roblox-creator-docs/art/modeling/surface-appearance#emissive-mask|Emissive Mask]]</td>
      <td>Single Channel Grayscale (8-bit)</td>
    </tr>
  </tbody>
</table>
</TabItem>
<TabItem label="PBR Texture Budget">
Use an appropriate texture map size based on the asset you are texturing to optimize for visual quality and performance. As a general guideline, each asset should have a texture resolution of 256×256 for every 2×2×2 unit space the asset occupies. If larger than a 2×2×2 cube, use the next highest resolution. The following are some baseline texture sizing examples:

<table>
	<thead>
	<tr>
		<th>Recommended map size</th>
		<th>Approximate asset size (unit cube)</th>
		<th>Example assets</th>
	</tr>
	</thead>
	<tbody>
	<tr>
		<td>64×64–128×128</td>
		<td>1×1×1</td>
		<td>Jewelry, sunglasses, eyebrows, mustaches.</td>
	</tr>
	<tr>
		<td>256×256</td>
		<td>2×2×2</td>
		<td>Hair, shoes, tank tops, t-shirts, shorts, short skirts. <br/><br/>256x256 is the **maximum budget** for non-albedo maps for [[external/roblox-creator-docs/avatar/rigid-accessories/specifications#textures|rigid accessories]].</td>
	</tr>
	<tr>
		<td>512×512</td>
		<td>4×4×4</td>
		<td>Jackets, pants, overalls, long-sleeve shirts, long skirts.</td>
	</tr>
	<tr>
		<td>1024×1024 (maximum)</td>
		<td>8×8×8</td>
		<td>Full body clothing (onesies, robes), humanoid characters.</td>
	</tr>
	</tbody>
</table>

<Alert severity = 'info'>
When rendering many textures at the same time, Roblox may downsample textures to optimize for performance.
</Alert>
</TabItem>
</Tabs>

## UV mapping

All textures use UV mapping, a 3D modeling process to project a 3D model's surface to a 2D image, or UV atlas. See the following requirements for UV mapping, especially if you're manually editing or optimizing your UV atlas:

- **Single UV Set** — Use a single UV set for each component, such as a humanoid or accessory. Studio doesn't allow for multiple UV sets.
- **Coordinates** — All UVs must be created within a 0:1 space.
- **Overlaps** — Overlapping UVs are allowed.
- **Maximum Texture Resolution** — Roblox supports up to 1024×1024 pixel spaces for texture maps.


## Related Files

- [[external/roblox-creator-docs/art/modeling/gltf-export]] - 3D Export.
- [[external/roblox-creator-docs/art/modeling/assign-textures]] - Blender and Maya texture settings.
- [[external/roblox-creator-docs/art/modeling/calisthenics-tool]] - Calisthenics Tool.
- [[external/roblox-creator-docs/art/modeling/index]] - Custom 3D assets.
- [[external/roblox-creator-docs/art/modeling/export-requirements]] - Export settings.
- [[external/roblox-creator-docs/art/modeling/specifications]] - General specifications.
- [[external/roblox-creator-docs/art/modeling/material-reference]] - Material references.
- [[external/roblox-creator-docs/art/modeling/project-files]] - Modeling project files and references.
- [[external/roblox-creator-docs/art/modeling/surface-appearance]] - PBR textures.
- [[external/roblox-creator-docs/art/modeling/reimport]] - Reimport.
- [[external/roblox-creator-docs/art/modeling/rig-a-humanoid-model]] - Rig a humanoid model.
- [[external/roblox-creator-docs/art/modeling/rig-a-simple-mesh]] - Rig a simple mesh.
- [[external/roblox-creator-docs/art/modeling/rigging]] - Rigging and skinning.
- [[external/roblox-creator-docs/art/modeling/roblox-blender-plugin]] - Roblox Blender plugin.
- [[external/roblox-creator-docs/art/modeling/skin-a-humanoid-model]] - Skin a humanoid model.
- [[external/roblox-creator-docs/art/modeling/skin-a-simple-mesh]] - Skin a simple mesh.
