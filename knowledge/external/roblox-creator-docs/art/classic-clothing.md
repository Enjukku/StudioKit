---
title: Classic clothing
description: Classic clothing are decals you can apply to a classic character model's surface. You can create classic clothing items on Roblox and upload them to the Marketplace.
tags: [roblox, documentation, external-reference, priority-reference, art, assets]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [art/classic-clothing.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/classic-clothing.md). Published page: [https://create.roblox.com/docs/art/classic-clothing](https://create.roblox.com/docs/art/classic-clothing).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/avatar/classic-clothing]]. Kept locally so existing links keep working; read that page for current information.

<Alert severity="warning">
Many user-generated avatars on the Marketplace do not support 2D classic clothing. For information on creating modern 3D cosmetics, including rigid accessories and clothing items, see [[external/roblox-creator-docs/avatar/index|Get started]].
</Alert>

<Grid container spacing={2} style={{ marginBottom: 24, width: '100%' }}>
<Grid item xs={6} style={{ padding: 16 }}>
<Grid item container wrap="nowrap" direction="column" style={{ gap: 8, flex: 1 }}>

<div
className="container"
style={{ position: "relative", paddingBottom: "56.25%", height: 0, marginBottom: 12 }} >
<iframe
src="https://www.youtube-nocookie.com/embed/r_unfGZT5Ps"
title="YouTube video player"
frameBorder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowFullScreen
style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%" }} ></iframe>
</div>
<Typography variant="body1">
Create and sell your first 2D classic clothing item.
</Typography>
</Grid>
</Grid>

<Grid item xs={6} style={{ padding: 16 }}>
<Grid item container wrap="nowrap" direction="column" style={{ gap: 8, flex: 1 }}>

<div
className="container"
style={{ position: "relative", paddingBottom: "56.25%", height: 0, marginBottom: 12 }} >
<iframe
src="https://www.youtube-nocookie.com/embed/EUDSIUmLjxA"
title="YouTube video player"
frameBorder="0"
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
allowFullScreen
style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%" }} ></iframe>
</div>
<Typography variant="body1">
A high-level overview of avatar items on Roblox.
</Typography>

</Grid>
</Grid>
</Grid>

Classic clothing are the most basic type of avatar item available to purchase and sell on Roblox. With any image editor and web browser, you can create classic clothing items and sell them on the [Marketplace](https://www.roblox.com/catalog).

<Alert severity = 'warning'>
To publish and sell assets on the Marketplace, you must meet [[external/roblox-creator-docs/marketplace/marketplace-policy#creator-requirements|creator requirements]].
</Alert>

To create classic clothing items:

1. Decide on the [type of classic clothing](#types-of-classic-clothing) you'd like to create.
2. [Create](#creating-classic-clothing) an image for your asset using an image editor of your choice.
3. [[external/roblox-creator-docs/art/test-classic-clothing|Test]] your creation in Studio to ensure it looks as intended.
4. [[external/roblox-creator-docs/art/upload-classic-clothing|Upload]] the image file to the Marketplace through a web browser.
   1. Adding an item to the Marketplace requires a Robux [[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions#classic-clothing|fee]].
   2. Upon successful moderation, you gain a copy of the asset in your inventory.

## Types of classic clothing

The three types of classic clothing items are **T-shirts**, **Shirts**, and **Pants**. Each has different design and format requirements.

<img src="../assets/accessories/classic-clothing/Types-of-classic-clothing.png" alt="3 different examples of blocky characters with a different type of image displayed on its surface." />

### T-shirts

T-shirts are a square image, such as 512x512 pixels. When properly configured, classic t-shirts display on the front torso of a blocky character.

### Shirts and pants

Classic shirts and pants are image assets that wrap around an avatar's body. Because classic shirts and pants have specific size requirements, download and modify the provided template files to begin creating these assets.

<GridContainer numColumns="2">
  <figure>
    <img src="../assets/accessories/classic-clothing/Template-Shirts-R15.png" />
    <figcaption><center> <a href="../assets/accessories/classic-clothing/Classic-Clothing-Templates.zip" download>Shirt (torso and arms)</a></center></figcaption>

  </figure>
  <figure>
    <img src="../assets/accessories/classic-clothing/Template-Pants-R15.png" />
    <figcaption><center> <a href = "../assets/accessories/classic-clothing/Classic-Clothing-Templates.zip" download>Pants (torso and legs)</a></center></figcaption>
  </figure>
</GridContainer>

<BaseAccordion>
<AccordionSummary>
Table of sizes for each template part
</AccordionSummary>
<AccordionDetails>
<table>
<thead>
  <tr>
    <th>Shape</th>
    <th>Pixel size (width x height)</th>
    <th>Clothing parts</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Large square</td>
    <td>128 &times; 128</td>
    <td><b>FRONT</b> and <b>BACK</b></td>
  </tr>
  <tr>
    <td>Tall rectangle</td>
    <td>64 &times; 128</td>
    <td>Sides of torso (<b>R</b>, <b>L</b>) <br /> Sides of arms and legs (<b>L</b>, <b>B</b>, <b>R</b>, <b>F</b>)</td>
  </tr>
  <tr>
    <td>Wide rectangle</td>
    <td>128 &times; 64</td>
    <td><b>UP</b> and <b>DOWN</b></td>
  </tr>
  <tr>
    <td>Small square</td>
    <td>64 &times; 64</td>
    <td>Top and bottom of arms and legs (<b>U</b>, <b>D</b>)</td>
  </tr>
</tbody>
</table>
</AccordionDetails>
</BaseAccordion>

## Creating classic clothing

To begin creating classic clothing:

1. If you are creating a classic shirt or pants, [download and unzip](../assets/accessories/classic-clothing/Classic-Clothing-Templates.zip) the following clothing templates to use as a canvas for your art.
2. Modify the image in an image editor of your choice.
3. Export the image as a `.png` or `.jpg` before [[external/roblox-creator-docs/art/test-classic-clothing|testing]] or [[external/roblox-creator-docs/art/upload-classic-clothing|uploading]] to Roblox.

When applying clothing to avatars in Roblox, some limits exist with the templates and may require some testing to get right, as shown in the following examples:

<GridContainer numColumns="2">
  <figure>
    <img src="../assets/accessories/classic-clothing/Pants-Template-Good.jpg" />
    <figcaption>The shoe designs in this example are near the bottom of the leg regions (L, B, R, F) but don't extend too far up. This provides a distinct separation between the shoes and the bottom of the jeans.</figcaption>
  </figure>
  <figure>
    <img src="../assets/accessories/classic-clothing/Pants-Template-Bad.jpg" />
    <figcaption>The shoe designs in this example extend too far up the leg regions (L, B, R, F) which make them appear as if they're part of the pants. The same issue may occur near other joints on the avatar's body.</figcaption>
  </figure>
</GridContainer>

<Alert severity = 'success'>
After creating your classic clothing, [[external/roblox-creator-docs/art/test-classic-clothing|test]] your creation in Roblox Studio before [[external/roblox-creator-docs/art/upload-classic-clothing|uploading]] and selling your asset on the Marketplace.
</Alert>


## Related Files

- [[external/roblox-creator-docs/art/overview-studio]] - 3D art and Studio.
- [[external/roblox-creator-docs/art/index]] - 3D art in Roblox.
- [[external/roblox-creator-docs/art/blender]] - Blender.
- [[external/roblox-creator-docs/avatar/index]] - Create avatar items.
- [[external/roblox-creator-docs/marketplace/marketplace-fees-and-commissions]] - Marketplace fees and commissions.
- [[external/roblox-creator-docs/marketplace/marketplace-policy]] - Marketplace policy.
- [[external/roblox-creator-docs/art/reaper]] - Reaper.
- [[external/roblox-creator-docs/art/test-classic-clothing]] - Test classic clothing.
- [[external/roblox-creator-docs/art/upload-classic-clothing]] - Upload classic clothing.
- [[external/roblox-creator-docs/art/validation-errors]] - Validation Errors.
- [[external/roblox-creator-docs/art/overview-dcc]] - Work with third-party software.
