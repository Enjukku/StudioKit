> Author: J018 maker modeler · claude-opus-5-5 · high · 2026-10-22. Part of `modeling-craft`; built also from the owner's Riot transcripts (J018). The exact command lines behind `modeling-craft` §7 for the measurements `tools/art/look_check.py` does not make itself. Each was run on 2026-10-22 on the inputs it names: a flat-background Blender render, its black-fill, a full game-camera frame (1600x720, small model) and an in-scene capture with sky and ground (repair round 3: §2-§4 fixed, every line re-run). Before trusting a number, ask what would make it wrong with no error: background in the measure, a frame of the wrong scale, the image border. `<checks>` = `content/models/<asset-id>/renders/checks/`. Numbers marked PROPOSAL are starting values a check may change.

# Command lines for measuring the read

## 1. Region mask (upper vs lower body, focal zone, one material)
Cut the region out of the black-fill, so background pixels never count:
```
python -c "import sys;from PIL import Image,ImageChops;m=Image.open(sys.argv[1]).convert('L');x0,y0,x1,y1=map(int,sys.argv[2].split(','));b=Image.new('L',m.size,255);b.paste(0,(x0,y0,x1,y1));ImageChops.lighter(m,b).save(sys.argv[3])" <checks>/<name>.silhouette.png x0,y0,x1,y1 <checks>/<region>.mask.png
```
Then `python tools/art/look_check.py value <render> --mask <checks>/<region>.mask.png --out-dir <checks>/<region>` (or `palette --mask` for CL5). The box only limits the fill. Box edges: from the projection recipe (`blender-recipes.md` §6: the waist line from the belt or hip part, the head box from the head part), never by eye; on a Studio capture, from `workspace.CurrentCamera:WorldToViewportPoint` of the same parts (`execute_luau` while the capture camera is still set), scaled by the capture width ÷ `Camera.ViewportSize.X`, checked once against the mask image. Never use `--box` or `--compare-subjects` on a render: every background pixel in the box counts.

## 2. Top 5 % (value or colour)
```
python -c "import sys,numpy as n;from PIL import Image,ImageFilter as F;i=Image.open(sys.argv[1]);a=n.asarray(i.convert('RGB')).astype(int);l=a.max(2)-a.min(2) if sys.argv[4]=='S' else n.asarray(i.convert('L'));m=n.asarray(Image.open(sys.argv[2]).convert('L').filter(F.MaxFilter(5)))<128;t=n.percentile(l[m],95);k=m&(l>=t);u=m&(l>t);s=k.sum()/m.sum();k=u if s>0.1 and u.sum()>=0.001*m.sum() else k;print('p95 share',round(s,3),'marked share',round(k.sum()/m.sum(),4));Image.fromarray(n.where(k,0,255).astype('uint8')).save(sys.argv[3])" <image> <mask> <checks>/<name>.top5.png L
```
- `L`: `<image>` = the luminance image (`<name>.luminance.png`). `S`: `<image>` = the colour render or capture, output `<name>.sat5.png`; channel S is chroma (max minus min of R, G, B: how colourful a pixel looks), not HSV saturation, which is high on any tinted near-black pixel and would put the peak on dark boots and shadows. `<mask>` = the black-fill, or the capture's mask (same size as `<image>`).
- Black = the brightest (L) or most colourful (S) pixels of the model. The mask is shrunk by 2 px first, so edge pixels mixed with the sky or ground never count. Parts under about 5 px wide in the image drop out with them: for a thin item (a blade, a staff) run the line on a close `review_renders.py` view as well.
- Ties: on flat-region renders many pixels share one level, and the top 5 % can mark a whole large region. When it would mark more than 10 % of the model, the line marks only the pixels above that level, unless they are fewer than 0.1 % of the model (a few edge pixels): then it keeps the tied level. Record both printed shares. (Tests: a flat torso plus a small brighter accent: the accent alone; a flat red torso and near-black boots, channel S: torso pixels only, no boot pixel.)

## 3. Detail density (DT10)
```
python -c "import sys,numpy as n;from PIL import Image,ImageOps as O,ImageFilter as F;g=Image.open(sys.argv[1]).convert('L');k=Image.open(sys.argv[2]).convert('L');s=int(sys.argv[3])/g.height;y,x=n.nonzero(n.asarray(k)<128);b=(x.min(),y.min(),x.max()+1,y.max()+1);w,h=max(1,round((b[2]-b[0])*s)),max(1,round((b[3]-b[1])*s));z=lambda i,f:O.expand(i.crop(b).resize((w,h),Image.BOX),2,fill=f);g,k=z(g,0),z(k,255);m=n.asarray(k.filter(F.MaxFilter(5)))<128;e=(n.asarray(g.filter(F.FIND_EDGES))>24)&m;c=max(2,h//10);C=[(y,x,e[y:y+c,x:x+c].sum()/m[y:y+c,x:x+c].sum()) for y in range(2,h+2,c) for x in range(2,w+2,c) if m[y:y+c,x:x+c].mean()>=0.3];d=[v for _,_,v in C];t=2*max(float(n.median(d)) if d else 0,1e-3);H=n.full(m.shape,255,n.uint8);[H.__setitem__((slice(y,y+c),slice(x,x+c)),0 if v>t else int(235-150*v/max(max(d),1e-3))) for y,x,v in C];Image.fromarray(H).resize((H.shape[1]*8,H.shape[0]*8),Image.NEAREST).save(sys.argv[4]);print('model at phone size',w,'x',h,'px; cells',len(C),'busy share',round(sum(v>t for _,_,v in C)/max(len(C),1),2),'busy rows at % of height',sorted({round(100*(y-2+c/2)/h) for y,x,v in C if v>t}))" <game-camera render or capture> <its black-fill or mask> <phone viewport height> <checks>/<name>.detail.png
```
- Input: a game-camera render (or a Studio capture) taller than the phone viewport, its black-fill (or the mask from its mask capture), and the smallest phone viewport height from the game profile (360 for 800x360). FieldOfView is vertical, so the frame scales by phone height ÷ frame height at any frame aspect. The line crops to the model's box and box-averages it by that factor, so the background never counts and detail that vanishes on a phone does not count. Edges are counted only 2 px or more inside the outline, so the silhouette edge never makes a thin part look busy. Not for orthographic or close views.
- Output: `<name>.detail.png`, the cell grid at 8 times the phone size: black = busy cells (more than twice the median edge share), grey = the other cells (darker = more edges), white = outside the model. Printed: the model's size on the phone (check it against the read plan's on-screen height), the busy share and the busy rows (% of the model's height, 0 = top).
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
