---
title: Align tool
description: The Align tool lets you align objects or groups of objects along the X, Y, or Z axes.
tags: [roblox, documentation, external-reference, priority-reference, studio, debugging]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [studio/align-tool.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/studio/align-tool.md). Published page: [https://create.roblox.com/docs/studio/align-tool](https://create.roblox.com/docs/studio/align-tool).

The **Align** tool, accessible from Studio's **Model** tab toolbar or the **Window**&nbsp;⟩ **3D** menu,  lets you align objects or groups of objects along the **X**, **Y**, or **Z** axes.

<img src="../assets/studio/general/Toolbar-Align.png" width="800" alt="Align tool highlighted in Studio's toolbar." />

Primary benefits include:

- Aligning the center or edge of multiple objects in one action.
- Aligning entire `Class.Model|Models` or parts within them relative to other parts, all while keeping the model intact.
- Dynamically previewing the point of alignment before confirming.

## Mode

You can set the alignment mode to either **Min**, **Center**, or **Max**.

<Grid container spacing={3}>
	<Grid item>
		<figure>
    <img src="../assets/studio/align-tool/Icon-Min.png" width="80" alt="The Min icon in the toolbar." />
    <center><figcaption>Min</figcaption></center>
  	</figure>
	</Grid>
	<Grid item>
		<figure>
    <img src="../assets/studio/align-tool/Icon-Center.png" width="80" alt="The Center icon in the toolbar." />
    <center><figcaption>Center</figcaption></center>
  	</figure>
	</Grid>
	<Grid item>
		<figure>
    <img src="../assets/studio/align-tool/Icon-Max.png" width="80" alt="The Max icon in the toolbar." />
    <center><figcaption>Max</figcaption></center>
  	</figure>
	</Grid>
</Grid>

<Tabs>
<TabItem label="Min">
<img src="../assets/studio/align-tool/Mode-Min.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Min button on the world Z axis. A translucent orange rectangle represents where the objects align in context to each other." />
</TabItem>
<TabItem label="Center">
<img src="../assets/studio/align-tool/Mode-Center.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Center button on the world Z axis. A translucent orange rectangle represents where the objects align in context to each other." />
</TabItem>
<TabItem label="Max">
<img src="../assets/studio/align-tool/Mode-Max.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on the world Z axis. A translucent orange rectangle represents where the objects align in context to each other." />
</TabItem>
</Tabs>

## Align In

The **World** or **Local** option specifies which relative coordinates to align on. This is especially useful for aligning parts which don't share the same orientation or rotation.

The **X**, **Y**, and **Z** checkboxes let you select which axes to align on. Note that you can select multiple axes in a single alignment operation.

<Tabs>
<TabItem label="Before Alignment">
<img src="../assets/studio/align-tool/Align-In-Before.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are unaligned." />
</TabItem>
<TabItem label="Max / World Z">
<img src="../assets/studio/align-tool/Align-In-World-Z.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on the world Z axis. A translucent orange rectangle represents where the objects align in context to each other." />
</TabItem>
<TabItem label="Max / Local Z">
<img src="../assets/studio/align-tool/Align-In-Local-Z.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on their local Z axis. A translucent orange rectangle represents where the objects align in context to each other." />
</TabItem>
</Tabs>

## Relative To

An alignment operation can be relative to either the **Selection Bounds** or the **Active Object**.

### Selection Bounds

**Selection Bounds** aligns the selected objects relative to the bounding box around them.

<Tabs>
<TabItem label="Before Alignment">
<img src="../assets/studio/align-tool/Relative-To-Selection-Bounds-Before.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are unaligned. A translucent red rectangle represents where the objects' collective bounding box." />
</TabItem>
<TabItem label="Min / World X">
<img src="../assets/studio/align-tool/Relative-To-Selection-Bounds-Min-X.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Min button on the world X axis relative to their collective bounding box. A translucent red rectangle represents where the objects' collective bounding box." />
</TabItem>
<TabItem label="Max / World X">
<img src="../assets/studio/align-tool/Relative-To-Selection-Bounds-Max-X.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on the world X axis relative to their collective bounding box. A translucent red rectangle represents where the objects' collective bounding box." />
</TabItem>
</Tabs>

### Active Object

**Active Object** aligns the objects relative to the **last selected object**. This object is outlined in orange and it will not move during the operation. While parts are selected, you can switch the active object by clicking on a different object.

<Tabs>
<TabItem label="Before Alignment">
<img src="../assets/studio/align-tool/Relative-To-Active-Object-Before.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are unaligned. The large blue cube has a yellow outline to represent that it's the active object." />
</TabItem>
<TabItem label="Min / World X">
<img src="../assets/studio/align-tool/Relative-To-Active-Object-Min-X.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Min button on the world X axis relative to the active object. The large blue cube has a yellow outline to represent that it's the active object." />
</TabItem>
<TabItem label="Max / World X">
<img src="../assets/studio/align-tool/Relative-To-Active-Object-Max-X.jpg" width="720" height="405" alt="An angled side view of a small red cube, large blue cube, and a small purple cube that are aligned with the Max button on the world X axis relative to the active object. The large blue cube has a yellow outline to represent that it's the active object." />
</TabItem>
</Tabs>


## Related Files

- [[external/roblox-creator-docs/studio/avatar-settings]] - Avatar Settings.
- [[external/roblox-creator-docs/studio/mcp]] - Connect to the Roblox Studio MCP server.
- [[external/roblox-creator-docs/studio/controller-emulator]] - Controller Emulator.
- [[external/roblox-creator-docs/studio/debugging]] - Debugging.
- [[external/roblox-creator-docs/studio/developer-console]] - Developer Console.
- [[external/roblox-creator-docs/studio/device-simulator]] - Device Simulator.
- [[external/roblox-creator-docs/studio/explorer]] - Explorer window.
- [[external/roblox-creator-docs/studio/importer]] - Importer.
- [[external/roblox-creator-docs/studio/material-generator]] - Material Generator.
- [[external/roblox-creator-docs/studio/network-simulator]] - Network Simulator.
- [[external/roblox-creator-docs/studio/output]] - Output.
- [[external/roblox-creator-docs/studio/pivot-tools]] - Pivot tools.
- [[external/roblox-creator-docs/studio/properties]] - Properties window.
- [[external/roblox-creator-docs/studio/rig-builder]] - Rig Generator.
- [[external/roblox-creator-docs/studio/index]] - Roblox Studio.
- [[external/roblox-creator-docs/studio/setup]] - Roblox Studio setup.
- ...and 8 more local docs.
