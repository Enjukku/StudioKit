# ui-ux-designer memory (craft only; game facts go to knowledge/)

- Figma API: after `setBoundVariableForPaint`, reassign the paint with its opacity (`{...node.fills[0], opacity}`); binding resets opacity to 1. (J002-T07)
- Figma API: TEXT property defaults are per component set; set text per instance with `setProperties`. Constraints enum is MIN/CENTER/MAX/STRETCH/SCALE. Look up colour variables with `getLocalVariablesAsync('COLOR')` (names can repeat across collections).
- Depth block that resizes: backing rectangles (halo, outline) + face + lip with STRETCH constraints; gloss inside a `clipsContent` frame with the same radius; highlight bars as SVG parallelograms; half-tone flips via `relativeTransform [[-1,0,w],[0,1,0]]`.
- Phone check first: at 0.347x, outline < 5 px, lip < 8 px and text < 30 px stop reading. Grayscale capture: white utility buttons can outshine green primary; drop their gloss.
- Generated icons: flat key colour absent from the subject → local key (Pillow, `python -P -E`) → `upload_assets` multipart. Clean edges.
- State frames: clone the finished main frame, add the popup; cover the shop's close button with the popup's close (same x,y).
- [Vectors, library, images (T09)](craft_vectors_library_images.md) — createVector stroke, opacity read-back, clone relink, library alpha + 420 px, Codex image route
