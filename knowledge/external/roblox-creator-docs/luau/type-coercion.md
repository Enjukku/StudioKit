---
title: Type coercion
description: Type coercion in Luau allows for arithmetic, concatenation, and assignment of differently typed values.
tags: [roblox, documentation, external-reference, priority-reference, luau, scripting]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [luau/type-coercion.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/luau/type-coercion.md). Published page: [https://create.roblox.com/docs/luau/type-coercion](https://create.roblox.com/docs/luau/type-coercion).

If Luau tries to use a value or [[external/roblox-creator-docs/luau/variables|variable]] in an operation, such as [arithmetic](#arithmetic), [concatenation](#concatenation), or [assignment](#assignment), but the value isn't the type that the operation expects, then Luau converts (**coerces**) the value to change its data type. Coercion happens at run time for that operation and doesn't change the value of a variable.

## Arithmetic

Luau coerces strings to numbers in [[external/roblox-creator-docs/luau/operators#arithmetic|arithmetic operations]]. This behavior is built into Luau. If the types are incompatible for arithmetic, Luau throws an error and doesn't run the rest of the script. For example, you can't add a string to a number if the string does not represent a number.

```lua
print(100 + "7") -- 107
print(100 - "7") -- 93
print("1000" + 234) -- 1234
print("1000" - 234) -- 766
print("hello" + 234) -- error: attempt to perform arithmetic (add) string and number
```

## Concatenation

In concatenation, Luau coerces numbers to strings. To convert a number to a string without using coercion, use the `Library.string.format()` function.

```lua
print("Pi is " .. math.pi) --> Pi is 3.1415926535898
print("Pi is " .. 3.1415927) --> Pi is 3.1415927

-- Rounds to three decimal places
print("Pi is " .. string.format("%.3f", 3.1415927)) -- Pi is 3.142
```

## Assignment

Some properties expect certain data types, such as an [Enum](#enums) or string, but you can assign a value of a different type to it and Luau converts the value to the type the property expects.

### Enums

Luau coerces numbers and strings of enum values into the full enum name. For example, you can name the value of the `Class.Part.Material` property using a number, string, or full enum name, and the `print()` function always prints the full enum name. It's best practice to be explicit and use the full enum name. For more information on Enums, see [[external/roblox-creator-docs/luau/enums|Enums]].

```lua
local Workspace = game:GetService("Workspace")

local part1 = Instance.new("Part")
part1.Material = 816
part1.Parent = Workspace
print(part1.Material) -- Enum.Material.Concrete

local part2 = Instance.new("Part")
part2.Material = "Concrete"
part2.Parent = Workspace
print(part2.Material) -- Enum.Material.Concrete

-- This is best practice because it's the most explicit
local part3 = Instance.new("Part")
part3.Material = Enum.Material.Concrete
part3.Parent = Workspace
print(part3.Material) -- Enum.Material.Concrete
```

### Time of day

The `Class.Lighting.TimeOfDay` property, which defines whether it is night, day, or any other time, is a string representation of the `Datatype.DateTime` data type. If you assign a number to `Class.Lighting.TimeOfDay`, Luau converts it to the string representation of `Datatype.DateTime`.

```lua
local Lighting = game:GetService("Lighting")

Lighting.TimeOfDay = "05:00:00"
print(Lighting.TimeOfDay) -- 05:00:00

Lighting.TimeOfDay = 5
print(Lighting.TimeOfDay) -- 05:00:00
```


## Related Files

- [[external/roblox-creator-docs/luau/booleans]] - Booleans.
- [[external/roblox-creator-docs/luau/control-structures]] - Control structures.
- [[external/roblox-creator-docs/luau/enums]] - Enums.
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
- ...and 5 more local docs.
