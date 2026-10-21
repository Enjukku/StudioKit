# Ambience map: fixture-stage · revision 1

Test fixture for tools/tests/test_scene_audit.py. Format: templates/environment/ambience-map.md.

## B. Zones (one record per zone; zone IDs never change)
```yaml
- zone: Z-FALLS                  # stable id
  env:
    feeling: loud water landmark
    neighbors: [Z-SWAMP, Z-CAVE]
- zone: Z-CAVE
  env:
    feeling: damp and close
- zone: Z-SWAMP
  env:
    feeling: reeds and frogs
```

## C. Point sources and moving things (one record per source; ids never change)
```yaml
- id: FALL-MAIN
  kind: sound                    # sound / effect / sound+effect / moving prop
  env:
    anchor: impact point
- id: RIVER-OUT
  kind: sound+effect
- id: CAVE-DRIP
  kind: sound
- id: BIRDS
  kind: sound
- id: CAVE-DRIP
  kind: sound
```

```text
- id: NOT-A-SOURCE   # outside a yaml block: ignored
```

## D. Shared environment state
- zone: Z-IGNORED (not in §B)
