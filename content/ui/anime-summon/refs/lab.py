import sys
def lin(c):
    c/=255; return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def Y(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16) for i in (0,2,4)]
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def L(h):
    y=Y(h); f=y**(1/3) if y>0.008856 else 7.787*y+16/116
    return 116*f-16
def cr(a,b):
    ya,yb=Y(a),Y(b); hi,lo=max(ya,yb),min(ya,yb); return (hi+0.05)/(lo+0.05)
pairs=[l.split() for l in sys.stdin if l.strip()]
for p in pairs:
    if p[0]=='G': print(f"{p[1]:24s} {p[2]} L*{L(p[2]):5.1f} -> {p[3]} L*{L(p[3]):5.1f}  dL*={L(p[2])-L(p[3]):5.1f}")
    else: print(f"{p[1]:24s} {p[2]} vs {p[3]} contrast {cr(p[2],p[3]):5.2f}")
