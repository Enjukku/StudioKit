import sys
from PIL import Image
import numpy as np
src, dst, key, maxside = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
im = np.asarray(Image.open(src).convert('RGB')).astype(np.float32)
R,G,B = im[...,0],im[...,1],im[...,2]
if key=='magenta':
    k = np.minimum(R,B)-G; K=np.array([255,0,255],np.float32)
else:
    k = G-np.maximum(R,B); K=np.array([0,255,0],np.float32)
lo,hi = 70.,190.
a = 1-np.clip((k-lo)/(hi-lo),0,1)
# unmix key from edge pixels
a3=a[...,None]; safe=np.maximum(a3,1e-3)
col = (im-(1-a3)*K)/safe
col = np.where(a3<0.999, col, im)
# despill residual
if key=='magenta':
    m=np.minimum(col[...,0],col[...,2]); g=col[...,1]
    spill=np.clip(m-g-60,0,None)*(a<0.999)
    col[...,0]-=spill; col[...,2]-=spill
else:
    mx=np.maximum(col[...,0],col[...,2]); spill=np.clip(col[...,1]-mx,0,None)
    col[...,1]-=spill
col=np.clip(col,0,255)
out=np.dstack([col,a*255]).astype(np.uint8)
img=Image.fromarray(out,'RGBA')
bb=img.getchannel('A').point(lambda v:255 if v>8 else 0).getbbox()
img=img.crop(bb)
s=maxside/max(img.size)
if s<1: img=img.resize((round(img.size[0]*s),round(img.size[1]*s)),Image.LANCZOS)
img.save(dst)
# halo check sheet
w,h=img.size
sheet=Image.new('RGB',(w*2,h),(255,255,255)); sheet.paste((14,10,40),(0,0,w,h))
sheet.paste(img,(0,0),img); sheet.paste(img,(w,0),img)
sheet.save(dst.replace('.png','_check.jpg'),quality=85)
print(dst,img.size,bb)
