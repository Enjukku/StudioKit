# J015-T06 probe p08: the paper's maths, computed. Plain Python 3 (no Blender needed): python p08_maths.py
import math, random
from fractions import Fraction as F
def out(k, v): print("PROBE p08", k, "=", v)
D = math.degrees
# --- FOV formulas (BL-07, BL-09)
S, f = 36.0, 50.0
H = 2 * math.atan(S / (2 * f))
out("H = 2atan(36/(2*50)) deg", "%.6f" % D(H))
out("V (Sy=24) = 2atan(24/(2*50)) deg", "%.6f" % D(2 * math.atan(24 / (2 * f))))
for a, label in ((16 / 9, "16:9"), (9 / 16, "9:16")):
    V = 2 * math.atan(math.tan(H / 2) / a)
    out("V from H=39.5978 with a=%s: V=2atan(tan(H/2)/a) deg" % label, "%.6f" % D(V))
    out("identity tan(H/2) - a*tan(V/2) for a=%s" % label, "%.3e" % (math.tan(H / 2) - a * math.tan(V / 2)))
out("sensor 36mm, f=50 -> tan(H/2)", math.tan(H / 2))
# range: angle strictly in (0, pi)
out("angle bounds: f->0+ (f=1e-6) H deg / f->inf (f=1e9) H deg", "%.6f / %.3e" % (D(2 * math.atan(36 / (2e-6))), D(2 * math.atan(36 / 2e9))))
# --- projection and dolly+zoom (BL-10)
X, Z, fl = 1.0, 10.0, 50.0
out("x_image = f X/Z (X=1,Z=10,f=50)", fl * X / Z)
# match close subject size: move camera back so subject at Z2=20 and raise f to 100: subject X image same, but background at Z+50 changes
for (Zs, Zb, fl2) in ((10, 40, 50), (20, 50, 100)):
    out("subject depth %g f=%g: subject image size for 1 m | background (1 m at depth %g)" % (Zs, fl2, Zb), "%.4f | %.4f  ratio bg/subject=%.4f" % (fl2 / Zs, fl2 / Zb, Zs / Zb))
# --- smoothstep (BL-18..20)
L, T = 10.0, 2.0
s = lambda u: 3 * u**2 - 2 * u**3
speed = lambda u: (L / T) * (6 * u - 6 * u**2)
h = 1e-6
num = lambda u: (L * s(u + h) - L * s(u - h)) / (2 * h * T)
errs = max(abs(num(u) - speed(u)) for u in [i / 50 for i in range(1, 50)])
out("smoothstep speed analytic vs numeric derivative, max err (u in 0.02..0.98, L=10,T=2)", "%.2e" % errs)
out("average speed L/T", L / T)
out("peak speed analytic 3L/(2T) at u=0.5 / speed(0.5) / max over grid", "%.6f / %.6f / %.6f" % (1.5 * L / T, speed(0.5), max(speed(i / 10000) for i in range(10001))))
out("endpoint velocity u=0 / u=1", (speed(0), speed(1)))
acc = lambda u: (L / T**2) * (6 - 12 * u)
out("endpoint acceleration (L/T^2)(6-12u) at u=0 and u=1 (L=10,T=2)", (acc(0), acc(1)))
out("peak/average speed ratio", 1.5)
# --- time arithmetic (BL-30..32)
def t(k, k0, r): return (F(k) - F(k0)) / r
r30 = F(30)
out("t(31) with k0=1 at 30 fps (s)", t(31, 1, r30))
out("intervals between positions 1 and 31", 31 - 1)
out("inclusive samples 1..31", 31 - 1 + 1)
out("duration of 31 samples at 30 fps", "%s s = %.9f s" % (F(31, 30), 31 / 30))
out("one frame at 30 fps (ms)", "%s = %.9f" % (F(1000, 30), 1000 / 30))
out("one frame at 60 fps (ms)", "%s = %.9f" % (F(1000, 60), 1000 / 60))
out("33 ms and 16 ms exact?", (F(1000, 30) == 33, F(1000, 60) == 16))
r2997 = F(30000, 1001)
out("30000/1001 fps one frame (ms)", "%s = %.9f ; rate = %.12f" % (F(1001 * 1000, 30000), 1001 * 1000 / 30000, 30000 / 1001))
out("30000/1001 vs 29.97 relative difference", "%.3e" % (float(r2997) / 29.97 - 1))
out("108000 frames (1 h at 30 fps) played at 30000/1001 last this many seconds MORE than 3600", "%.4f s" % (108000 * 1001 / 30000 - 3600))
# half-open cut list: shot [1,31) at 30fps = 30 frames = 1 s
out("cut list [1,31) frames / seconds at 30fps", (31 - 1, F(31 - 1, 30)))
# --- basis conversion algebra (BL-24)
def rotz(a): c, s_ = math.cos(a), math.sin(a); return [[c, -s_, 0], [s_, c, 0], [0, 0, 1]]
def rotx(a): c, s_ = math.cos(a), math.sin(a); return [[1, 0, 0], [0, c, -s_], [0, s_, c]]
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def mv(A, v): return [sum(A[i][k] * v[k] for k in range(3)) for i in range(3)]
def inv(Q): return [[Q[j][i] for j in range(3)] for i in range(3)]   # Q orthogonal
random.seed(1)
R = mm(rotz(0.7), mm(rotx(-1.1), rotz(2.3)))
Qz2y = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]       # (x,y,z)->(x,z,-y): Z-up -> Y-up, det +1
Qflip = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]       # swap y,z: det -1 (handedness change)
for name, Q in (("Z-up->Y-up (det+1)", Qz2y), ("swap y/z (det-1)", Qflip)):
    Rt = mm(Q, mm(R, inv(Q)))
    v = [0.3, -1.2, 2.2]
    lhs = mv(Rt, mv(Q, v)); rhs = mv(Q, mv(R, v))
    out("R_target(Qv) == Q(Rv) for %s, max abs diff" % name, "%.2e" % max(abs(a - b) for a, b in zip(lhs, rhs)))
    det = (Rt[0][0] * (Rt[1][1] * Rt[2][2] - Rt[1][2] * Rt[2][1]) - Rt[0][1] * (Rt[1][0] * Rt[2][2] - Rt[1][2] * Rt[2][0]) + Rt[0][2] * (Rt[1][0] * Rt[2][1] - Rt[1][1] * Rt[2][0]))
    out("det(R_target) for %s" % name, round(det, 6))
