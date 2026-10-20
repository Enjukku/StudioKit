---
title: Return values from tables
description: Learn how to write a search function using pairs and ipairs to return values from tables in Luau.
tags: [roblox, documentation, external-reference, priority-reference, tutorials]
next: /tutorials/fundamentals/coding-6/landing
prev: /tutorials/fundamentals/coding-5/pairs-and-ipairs
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [tutorials/fundamentals/coding-5/return-values-from-tables.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/tutorials/fundamentals/coding-5/return-values-from-tables.md). Published page: [https://create.roblox.com/docs/tutorials/fundamentals/coding-5/return-values-from-tables](https://create.roblox.com/docs/tutorials/fundamentals/coding-5/return-values-from-tables).

A common need in many data structures is to return values. This article will cover searching a table using `pairs()` or `ipairs()` for half of any table element, such as the key or value, to find and return the other half.

The example uses an array listing ships waiting to be repaired. `ipairs()` is used to return a ship's place in line.

```lua
local shipToFind = "Void Racer"

-- Ships waiting for repair
local waitingShips = {"Battle Sun", "Void Racer", "The Big Slow"}

-- Get place in line
local function getPlaceInLine(shipName)
	for placeInLine, ship in ipairs(waitingShips) do
		if ship == shipName then
			return placeInLine
		end
	end
end

--Print place in line
local placeInLine = getPlaceInLine(shipToFind)
print("Your place in line is " .. placeInLine)
```

## Dictionary search example

Have you ever searched for a lost pet in house going room by room? On your own code a function to search through a dictionary named house to see which room holds a lost puppy.

1. Copy the dictionary below to act as the house.

   ```lua
   local house = {
   	kitchen = "pile of Junk",
   	livingRoom = "kitten",
   	bedroom1 = "nobody there",
   	bedroom2 = "puppy",
   }
   ```

2. Create a new function called `findPet()` to search the dictionary. Include parameters for what dictionary to search, and what value to search for.
3. Use `pairs()` to iterate through the dictionary. Try coding your own before checking your work in the solution below.

   ```lua
   local function findPet(whereToSearch, searchFor)
   	for place, value in pairs(whereToSearch) do

   	end
   end
   ```

4. As the for loop iterates through the dictionary, use `return` to pass back the room where the pet was found.

   ```lua
   local function findPet(whereToSearch, searchFor)
   	for place, value in pairs(whereToSearch) do
   		if value == searchFor then
   			return place
   		end
   	end
   end
   ```


## Related Files

- [[external/roblox-creator-docs/tutorials/fundamentals/coding-5/landing]] - Arrays and dictionaries.
- [[external/roblox-creator-docs/tutorials/fundamentals/coding-5/intro-to-arrays]] - Intro to arrays.
- [[external/roblox-creator-docs/tutorials/fundamentals/coding-5/intro-to-dictionaries]] - Intro to dictionaries.
- [[external/roblox-creator-docs/tutorials/fundamentals/coding-5/loops-and-arrays]] - Loops and arrays.
- [[external/roblox-creator-docs/tutorials/fundamentals/coding-5/make-changes-to-arrays]] - Make changes to arrays.
- [[external/roblox-creator-docs/tutorials/fundamentals/coding-5/pairs-and-ipairs]] - pairs and ipairs.
