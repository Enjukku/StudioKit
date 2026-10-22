> Author: J018 maker modeler · claude-opus-5-5 · high · 2026-10-22. Part of `modeling-craft`; built also from the owner's Riot transcripts (J018). The command lines behind `modeling-craft` §7 (§1-§3 are `look_check.py` modes since J019 G3-P8). Each was run on 2026-10-22 on the inputs it names: a flat-background Blender render, its black-fill, a full game-camera frame (1600x720, small model) and an in-scene capture with sky and ground (repair round 3: §2-§4 fixed, every line re-run). Before trusting a number, ask what would make it wrong with no error: background in the measure, a frame of the wrong scale, the image border. `<checks>` = `content/models/<asset-id>/renders/checks/`. Numbers marked PROPOSAL are starting values a check may change.

# Command lines for measuring the read

## 1. Region mask (upper vs lower body, focal zone, one material)
Cut the region out of the black-fill with `--mask-box` (any `look_check` mode that takes `--mask`), so background pixels never count:
```
python tools/art/look_check.py value <render> --mask <checks>/<name>.silhouette.png --mask-box x0,y0,x1,y1 --out-dir <checks>/<region>
```
The box only limits the mask. Box edges: from the projection recipe (`blender-recipes.md` §6: the waist line from the belt or hip part, the head box from the head part), never by eye; on a Studio capture, from `workspace.CurrentCamera:WorldToViewportPoint` of the same parts (`execute_luau` while the capture camera is still set), scaled by the capture width ÷ `Camera.ViewportSize.X`, checked once against the mask image. Never use `--box` or `--compare-subjects` on a render: every background pixel in the box counts.

## 2. Top 5 % (value or colour)
```
python tools/art/look_check.py peaks <image> --mask <mask> --channel luminance|chroma --out-dir <checks>
```
- `luminance`: `<image>` = the colour render (the mode computes the luminance). `chroma`: `<image>` = the colour render or capture; chroma (max minus min of R, G, B: how colourful a pixel looks), not HSV saturation, which is high on any tinted near-black pixel and would put the peak on dark boots and shadows. `<mask>` = the black-fill, or the capture's mask (same size as `<image>`).
- Black = the brightest (L) or most colourful (S) pixels of the model. The mask is shrunk by 2 px first, so edge pixels mixed with the sky or ground never count. Parts under about 5 px wide in the image drop out with them: for a thin item (a blade, a staff) run the line on a close `review_renders.py` view as well.
- Ties: on flat-region renders many pixels share one level, and the top 5 % can mark a whole large region. When it would mark more than 10 % of the model, the line marks only the pixels above that level, unless they are fewer than 0.1 % of the model (a few edge pixels): then it keeps the tied level. Record both printed shares. (Tests: a flat torso plus a small brighter accent: the accent alone; a flat red torso and near-black boots, channel S: torso pixels only, no boot pixel.)

## 3. Detail density (DT10)
```
python tools/art/look_check.py detail <game-camera render or capture> --mask <its black-fill or mask> --phone-height <smallest phone viewport height> --out-dir <checks>
```
- Input: a game-camera render (or a Studio capture) taller than the phone viewport, its black-fill (or the mask from its mask capture), and the smallest phone viewport height from the game profile (360 for 800x360). FieldOfView is vertical, so the frame scales by phone height ÷ frame height at any frame aspect. The line crops to the model's box and box-averages it by that factor, so the background never counts and detail that vanishes on a phone does not count. Edges are counted only 2 px or more inside the outline, so the silhouette edge never makes a thin part look busy. Not for orthographic or close views.
- Output: the `images.cells` file, the cell grid at 8 times the phone size: black = busy cells (more than twice the median edge share), grey = the other cells (darker = more edges), white = outside the model. Measured: `model_px_at_phone` (check it against the read plan's on-screen height), `busy_share` and `busy_rows_pct_of_height` (0 = top); a model under about 30 px tall returns not-measured.
- Read: the busy cells sit on the read plan's detail spots with quiet cells between. A big part line (a waist, a collar) also shows as a busy row: it is not a detail spot. Busy share 0, or busy cells spread over the whole model, is even density: DT10 fails. A model under about 30 px tall on the phone gives too few cells: DT10 is `not verified`; judge it with DT2.
- The edge threshold (24) and the cell size (a tenth of the model's phone height) are starting values (PROPOSAL).

## 4. Phone-aspect crop (Studio captures wider than the phone)
Roblox `Camera.FieldOfView` is vertical: a capture at the game FOV already has the phone's vertical scale, so keep its full height. Only a capture wider than the smallest phone viewport is cropped, in width only, around the centre (the look-at point); a capture as wide or narrower goes to `thumb` uncropped (`thumb` keeps the aspect and pads). Run the line on the capture and on its mask capture, then `silhouette` on the cropped mask capture:
```
python -c "import sys;from PIL import Image;i=Image.open(sys.argv[1]);w,h=i.size;a,b=map(int,sys.argv[2].split('x'));W=min(w,round(h*a/b));x=(w-W)//2;i.crop((x,0,x+W,h)).save(sys.argv[3]);print('cropped' if W<w else 'not cropped (not wider than the phone)',w,'x',h,'->',W,'x',h)" <capture> <phone WxH> <out>
```
Check: `thumb`'s `scale` equals phone viewport height ÷ capture height; a smaller scale means the frame was wider than the phone and not cropped.

## 5. Mirror
```
python -c "from PIL import Image, ImageOps; ImageOps.mirror(Image.open('<render>')).save('<checks>/<name>.mirror.png')"
```

## 6. Reserved hue and hue spread on a model (CL2, CL5)
Both commands have one copy, in `art-review/references/look-check.md` §5 (line 4: reserved hue; line 10: hue spread); run them from the repo root as written there. Both are screening aids: a number that passes never overrides what the colour render shows.
- **Reserved hue (CL2).** `<capture>` = the review set's colour render (front, then back). `<reserved hex>` = the swatch as rendered: `python tools/art/look_check.py contrast --sample <render> --fg-box <inside the face of a gameplay part that wears the hue and faces the camera and the key light like the decoration does, away from its highlight> --bg-box <any box> --out <checks>/<part>-sample.json`, its `measurements.pairs[0].fg_sample.hex` (quote it in a shell: an unquoted `#` starts a comment); a model with no such part: the bible's swatch as rendered in an approved neighbour's render. Distance: the bible's (`art-review/references/art-bible.md` §7 Reserved colours). `<exclude>` = a region mask (§1) whose box holds every part that may wear the hue and no decoration; decoration inside that box is not measured: list it. Read `px`: the flat grey background never counts, so `px` is the count on the model. Pass: 0 px, or the owner's number.
  Tested 2026-10-22 on a `review_renders.py` front render (1600x400; a decorative panel with a thin red stripe, a red gameplay orb), swatch sampled on the orb's camera-facing face: orb excluded, 1,827 px (the stripe); orb and panel excluded, 0. Wrong with no error: the authored hex on a lit render (the studio light moved the red, so the authored swatch found 0 px with the stripe present: a false pass); a swatch sampled on the part's shadow side (0 px with the stripe present: a false pass); an exclusion box smaller than the part (the orb's uncovered rim: 5,666 px, a false fail; the marked image shows it); a Studio capture (sky and ground count, and the place's share is the art director's check on the environment-only capture).
- **Hue spread (CL5).** `<image>` = the colour render, or the three-quarter or a closer render for a small part; the box fully inside one material's lit face, at least 16 px on each side, crossing no part edge, decal or trim. Pass: `hue_sd_deg` above the flat limit (starting value in line 10), with `median_chroma` about 15 or more; a near-neutral material is judged by eye and recorded so. Tested on the same render: flat colour 0.28; a one-hue brick texture painted in sRGB 0.65 (monochrome: fails); the same bricks with hue patches 7.34; a smooth one-hue cylinder with a white highlight 1.4 (the highlight does not raise it); a box across the panel and its stripe 9.8 (a false pass: two materials). The other false readings are in line 10.
