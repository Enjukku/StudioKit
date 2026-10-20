---
title: Enums
description: A fixed list of items (enumeration).
tags: [roblox, documentation, external-reference, priority-reference, luau, scripting]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [luau/enums.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/luau/enums.md). Published page: [https://create.roblox.com/docs/luau/enums](https://create.roblox.com/docs/luau/enums).

<Alert severity="info">
Enums are not a [built-in Luau type](https://luau.org/typecheck#builtin-types) and they exist only in Roblox, but they're conceptually similar to other Luau data types and are something you'll work with frequently in Roblox development.
</Alert>

The **enumeration** data type, or `Datatype.Enum`, is a fixed list of items. You can access enums through the global object called `Datatype.Enum`. For a full list and their respective items, see [Enums](/reference/engine/enums).

## Enum items

To get all items of an enum, call the `Datatype.Enum:GetEnumItems()|GetEnumItems()` method on it. The following code sample demonstrates how to call `Datatype.Enum:GetEnumItems()|GetEnumItems()` on the `Enum.PartType` enum.

```lua
local partTypes = Enum.PartType:GetEnumItems()

for index, enumItem in partTypes do
	print(enumItem)
end

--[[
	Enum.PartType.Ball
	Enum.PartType.Block
	Enum.PartType.Cylinder
	Enum.PartType.Wedge
	Enum.PartType.CornerWedge
]]
```

## Data type

The `Datatype.EnumItem` is the data type for items in enums. An `Datatype.EnumItem` has three properties:

- `Name` — The name of the `Datatype.EnumItem`.
- `Value` — The numerical index of the `Datatype.EnumItem`.
- `EnumType` — The parent `Datatype.Enum` of the `Datatype.EnumItem`.

Some properties of objects can only be items of certain enums. For example, the `Class.Part.Shape|Shape` property of a `Class.Part` object is an item of the `Enum.PartType` enum. The following code sample demonstrates how to print the properties of the `Enum.PartType.Cylinder` enum item.

```lua
print(Enum.PartType.Cylinder.Name) --> "Cylinder"
print(Enum.PartType.Cylinder.Value) --> 2
print(Enum.PartType.Cylinder.EnumType) --> PartType
```

To assign an `Datatype.EnumItem` as the value of a property, use the full `Datatype.Enum` declaration. You can also use the item's `Datatype.EnumItem.Name|Name` property as a string.

```lua
local Workspace = game:GetService("Workspace")

local part = Instance.new("Part") -- Create a new part

part.Shape = Enum.PartType.Cylinder -- By full enum item declaration (best practice)
part.Shape = "Cylinder" -- By enum item's name as a string

part.Parent = Workspace
```


## Related Files

- [[external/roblox-creator-docs/luau/booleans]] - Booleans.
- [[external/roblox-creator-docs/luau/control-structures]] - Control structures.
- [[external/roblox-creator-docs/luau/functions]] - Functions.
- [[external/roblox-creator-docs/luau/index]] - Luau.
- [[external/roblox-creator-docs/luau/luau-csharp-comparison]] - Luau and C# comparison.
- [[external/roblox-creator-docs/luau/comments]] - Luau comments.
- [[external/roblox-creator-docs/luau/metatables]] - Metatables.
- [[external/roblox-creator-docs/luau/native-code-gen]] - Native code generation.
- [[external/roblox-creator-docs/luau/nil]] - Nil.
- [[external/roblox-creator-docs/luau/numbers]] - Numbers.
- [[external/roblox-creator-docs/luau/operators]] - Operators.
- [[external/roblox-creator-docs/luau/queues]] - Queues.
- [[external/roblox-creator-docs/luau/scope]] - Scope.
- [[external/roblox-creator-docs/luau/stacks]] - Stacks.
- [[external/roblox-creator-docs/luau/strings]] - Strings.
- [[external/roblox-creator-docs/luau/tables]] - Tables.
- ...and 5 more local docs.
