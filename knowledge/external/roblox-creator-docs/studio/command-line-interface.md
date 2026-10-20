---
title: Studio command-line interface
description: Roblox Studio supports command-line arguments that let you start Studio in a variety of ways and access special Studio functionality.
tags: [roblox, documentation, external-reference, priority-reference, studio, debugging]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [studio/command-line-interface.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/studio/command-line-interface.md). Published page: [https://create.roblox.com/docs/studio/command-line-interface](https://create.roblox.com/docs/studio/command-line-interface).

Roblox Studio supports command-line arguments that let you launch it with special functionality, such as opening a specific place or script when Studio starts. The Roblox Studio executable is typically installed in the following locations:

<table>
  <thead>
    <tr>
      <th>OS</th>
      <th>Location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Windows</td>
      <td>`%localappdata%\Roblox\Versions\[version]\RobloxStudioBeta.exe`</td>
    </tr>
    <tr>
      <td>Mac</td>
      <td>`/Applications/RobloxStudio.app/Contents/MacOS/RobloxStudio`</td>
    </tr>
  </tbody>
</table>

When launched from the command line, Studio pipes verbose logs to `stdout` that are more detailed than what appears in the **Output** window. Arguments use a double-dash prefix and are case-insensitive. File paths that contain spaces must be quoted.

<Alert severity="info">
Any arguments not documented here are for internal use only and are subject to change without notice.
</Alert>

## Open a place

To open a published place, specify the place ID, universe ID, and a task.

### Required arguments

<table>
  <thead>
    <tr>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>--placeId &lt;placeId&gt;</code></td>
      <td>The numeric ID of the place to open.</td>
    </tr>
    <tr>
      <td><code>--universeId &lt;universeId&gt;</code></td>
      <td>The universe that owns the place.</td>
    </tr>
    <tr>
      <td><code>--task &lt;taskName&gt;</code></td>
      <td>Specifies how Studio opens the place based on the given task. See the [supported tasks](#supported-tasks) table below for more information.</td>
    </tr>
  </tbody>
</table>

### Supported tasks

<table>
  <thead>
    <tr>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>EditPlace</code></td>
      <td>Opens the latest published version of the place for editing.</td>
    </tr>
    <tr>
      <td><code>EditPlaceRevision</code></td>
      <td>Opens a specific previous version of the place. Requires <code>--placeVersion &lt;versionNumber&gt;</code> to specify the version.</td>
    </tr>
  </tbody>
</table>

### Optional arguments

<table>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>--targetInstanceId &lt;guid&gt;</code></td>
    <td>Moves the Studio camera to focus on the instance with this GUID after the place loads.</td>
  </tr>
  <tr>
    <td><code>--annotationId &lt;guid&gt;</code></td>
    <td>Opens the annotation with this GUID after the place loads.</td>
  </tr>
</tbody>
</table>

### Examples

```shell
# Open the latest version of a place
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708

# Open a specific previous version
RobloxStudio.exe --task EditPlaceRevision --placeId 74265016723074 --universeId 7127583708 --placeVersion 2
```

## Open a local file

To open a local place, use `--task EditFile` with the following argument.

<table>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>--localPlaceFile &lt;path&gt;</code></td>
    <td>Absolute path to a local <code>.rbxl</code> or <code>.rbxlx</code> place file to open.</td>
  </tr>
</tbody>
</table>

You can also open a local place file by passing the file path as the first positional argument without a flag name.

### Examples

```shell
# Open a local place file
RobloxStudio.exe --task EditFile --localPlaceFile "Projects\MyGame.rbxl"

# Shorthand
RobloxStudio.exe "Projects\MyGame.rbxl"
```

## Open a script

To open a script, specify the place ID, universe ID, and task as described in the [open a place](#open-a-place) section. Then
provide one of the following arguments depending on how you want to open the script.

<table>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>--openScriptPath &lt;path&gt;</code></td>
    <td>The path to the script. Must use `/` as separators and follow absolute `require-by-string` semantics.</td>
  </tr>
  <tr>
    <td><code>--openScriptFromId &lt;uniqueId&gt;</code></td>
    <td>The unique ID of the script to open.</td>
  </tr>
</tbody>
</table>

### Optional highlighting

Optionally, highlight specific lines or a character range when opening the script.

<table>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>--startLine &lt;n&gt;</code></td>
    <td>Starting line of the highlight range. 1-based and inclusive.</td>
  </tr>
  <tr>
    <td><code>--endLine &lt;n&gt;</code></td>
    <td>Ending line of the highlight range. 1-based and exclusive.</td>
  </tr>
  <tr>
    <td><code>--startCharacter &lt;n&gt;</code></td>
    <td>Starting character position within the line. 1-based.</td>
  </tr>
  <tr>
    <td><code>--endCharacter &lt;n&gt;</code></td>
    <td>Ending character position within the line. 1-based and exclusive.</td>
  </tr>
</tbody>
</table>

### Examples

```shell
# Open a script by path
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708 --openScriptPath Workspace/MyFolder/MyScript

# Open a script by ID
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708 --openScriptFromId 604a6aa2-04cc-c820-09b3-a1dc0000537f

# Open a script and highlight specific lines
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708 --openScriptPath Workspace/MyFolder/MyScript --startLine 1 --endLine 5

# Open a script and highlight a character range
RobloxStudio.exe --task EditPlace --placeId 74265016723074 --universeId 7127583708 --openScriptPath Workspace/MyFolder/MyScript --startLine 1 --endLine 1 --startCharacter 1 --endCharacter 6
```

## Run a script

Use `--task RunScript` to execute a Luau script after a place finishes loading. Scripts run at the same permission level as the Studio command bar. You can combine this with `--placeId` and `--universeId` to run the script in a specific game, or `--localPlaceFile` to run the script in a local place file. If those arguments are omitted, Studio opens the default empty baseplate template and runs the script there.

### Required arguments

<table>
  <thead>
    <tr>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>--runScriptFile &lt;path&gt;</code></td>
      <td>Absolute path to a <code>.lua</code> or <code>.luau</code> file to execute.</td>
    </tr>
  </tbody>
</table>

### Optional arguments

<table>
  <thead>
    <tr>
      <th>Argument</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>--outputFile &lt;path&gt;</code></td>
      <td>Path to a file where script output is written.</td>
    </tr>
    <tr>
      <td><code>--quitAfterExecution</code></td>
      <td>If provided, Studio closes after the script finishes executing.</td>
    </tr>
  </tbody>
</table>

### Examples

```shell
# Run a script in a specific game and exit when done
RobloxStudio.exe --task RunScript --placeId 74265016723074 --universeId 7127583708 --runScriptFile smokeTest.luau --outputFile out.log --quitAfterExecution

# Run a script in the default Baseplate
RobloxStudio.exe --task RunScript --runScriptFile smokeTest.luau
```

## Try an asset

Use `--task TryAsset` to insert a specific asset into a baseplate template and open it for editing.

### Required arguments

<table>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>--assetId &lt;id&gt;</code></td>
    <td>The asset ID to insert.</td>
  </tr>
</tbody>
</table>

### Example

```shell
RobloxStudio.exe --task TryAsset --assetId 53326
```

## API dump

Use `--api`, `--fullApi`, or `--apiV2` to write the Roblox API surface to a file and exit.

<table>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>--api &lt;path&gt;</code></td>
    <td>Writes the Luau scripting API as JSON to the specified file.</td>
  </tr>
  <tr>
    <td><code>--fullApi &lt;path&gt;</code></td>
    <td>Writes the full API surface as JSON to the specified file.</td>
  </tr>
  <tr>
    <td><code>--apiV2 &lt;path&gt;</code></td>
    <td>Writes the full API as JSON in the V2 schema format to the specified file.</td>
  </tr>
</tbody>
</table>

### Examples

```shell
RobloxStudio.exe --api "Desktop/output.json"

RobloxStudio.exe --fullApi "Desktop/output.json"

RobloxStudio.exe --apiV2 "Desktop/output.json"
```


## Related Files

- [[external/roblox-creator-docs/studio/align-tool]] - Align tool.
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
- ...and 8 more local docs.
