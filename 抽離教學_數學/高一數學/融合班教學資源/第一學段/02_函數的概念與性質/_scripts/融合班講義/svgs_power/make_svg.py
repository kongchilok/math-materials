# -*- coding: utf-8 -*-
"""Generate the single 五個常見冪函數 overlay diagram as a hand-built coordinate
SVG (same house style as ../svgs_monotone/make_svgs.py: black/grey strokes only,
light-grey grid, dashed guide lines — no colour so it reads fine in B&W print).
Five curves y=x, y=x^2, y=x^3, y=sqrt(x), y=1/x sketched together, each labelled
inline, with (1,1) marked as the shared point."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

W, H = 420, 420
ox, oy = 170, 260   # pixel origin (x=0,y=0)
s = 62               # px per unit (equal x/y scale so shapes aren't skewed)

X_MIN, X_MAX = -2.6, 2.7
Y_MIN, Y_MAX = -2.6, 3.0


def P(x, y):
    return (ox + s * x, oy - s * y)


def clip_polylines(xs_ys):
    """Split a list of (x,y) samples into polyline segments wherever y goes
    outside [Y_MIN, Y_MAX] (or x outside [X_MIN, X_MAX]), so a curve like
    y=1/x or y=x^3 doesn't shoot off the canvas."""
    segs = []
    cur = []
    for x, y in xs_ys:
        if X_MIN <= x <= X_MAX and Y_MIN <= y <= Y_MAX:
            cur.append(P(x, y))
        else:
            if len(cur) >= 2:
                segs.append(cur)
            cur = []
    if len(cur) >= 2:
        segs.append(cur)
    return segs


def polyline_svg(segs, stroke_width=2.2, dasharray=None):
    da = f' stroke-dasharray="{dasharray}"' if dasharray else ''
    out = []
    for seg in segs:
        pts = ' '.join(f'{px:.1f},{py:.1f}' for px, py in seg)
        out.append(f'<polyline points="{pts}" fill="none" stroke="#1a1a1a" '
                    f'stroke-width="{stroke_width}"{da}/>')
    return '\n  '.join(out)


def sample(fn, x0, x1, n=240):
    pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        try:
            y = fn(x)
        except (ValueError, ZeroDivisionError):
            continue
        pts.append((x, y))
    return pts


parts = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" '
         f'font-family="Microsoft JhengHei, Arial, sans-serif">']

# ---- grid ----
for gx in range(-2, 3):
    px, _ = P(gx, 0)
    parts.append(f'<line x1="{px}" y1="14" x2="{px}" y2="{H-30}" stroke="#e6e6e6" stroke-width="1"/>')
for gy in range(-2, 4):
    _, py = P(0, gy)
    parts.append(f'<line x1="14" y1="{py}" x2="{W-14}" y2="{py}" stroke="#e6e6e6" stroke-width="1"/>')

# ---- axes ----
ax0, ay0 = P(X_MIN + 0.1, 0)
ax1, ay1 = P(X_MAX - 0.1, 0)
parts.append(f'<line x1="{ax0}" y1="{oy}" x2="{ax1}" y2="{oy}" stroke="#333" stroke-width="1.5"/>')
parts.append(f'<polygon points="{ax1},{oy} {ax1-8},{oy-4} {ax1-8},{oy+4}" fill="#333"/>')
bx0, by0 = P(0, Y_MIN + 0.1)
bx1, by1 = P(0, Y_MAX - 0.1)
parts.append(f'<line x1="{ox}" y1="{by0}" x2="{ox}" y2="{by1}" stroke="#333" stroke-width="1.5"/>')
parts.append(f'<polygon points="{ox},{by1} {ox-4},{by1+8} {ox+4},{by1+8}" fill="#333"/>')
parts.append(f'<text x="{ax1-10}" y="{oy+16}" font-size="13" fill="#333">x</text>')
parts.append(f'<text x="{ox+8}" y="{by1+14}" font-size="13" fill="#333">y</text>')
parts.append(f'<text x="{ox-14}" y="{oy+16}" font-size="11" fill="#666">O</text>')

# tick marks at x=1,-1 and y=1,-1
for gx in (-1, 1):
    px, _ = P(gx, 0)
    parts.append(f'<text x="{px-3}" y="{oy+16}" font-size="10" fill="#666">{gx}</text>')
for gy in (-1, 1, 2):
    _, py = P(0, gy)
    parts.append(f'<text x="{ox+6}" y="{py+3}" font-size="10" fill="#666">{gy}</text>')

# ---- five curves, each with a distinct stroke pattern (no colour) ----
segs_x = clip_polylines(sample(lambda x: x, X_MIN, X_MAX))
parts.append(polyline_svg(segs_x, stroke_width=2.0))

segs_x2 = clip_polylines(sample(lambda x: x * x, X_MIN, X_MAX))
parts.append(polyline_svg(segs_x2, stroke_width=2.0, dasharray='6,3'))

segs_x3 = clip_polylines(sample(lambda x: x ** 3, X_MIN, X_MAX))
parts.append(polyline_svg(segs_x3, stroke_width=2.0, dasharray='2,2'))

segs_sqrt = clip_polylines(sample(lambda x: x ** 0.5, 0, X_MAX))
parts.append(polyline_svg(segs_sqrt, stroke_width=2.6))

segs_inv_pos = clip_polylines(sample(lambda x: 1.0 / x, 0.3, X_MAX))
segs_inv_neg = clip_polylines(sample(lambda x: 1.0 / x, X_MIN, -0.3))
parts.append(polyline_svg(segs_inv_pos + segs_inv_neg, stroke_width=2.0, dasharray='8,3,2,3'))

# ---- shared point (1,1) ----
p11 = P(1, 1)
parts.append(f'<line x1="{p11[0]}" y1="{oy}" x2="{p11[0]}" y2="{p11[1]}" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>')
parts.append(f'<line x1="{ox}" y1="{p11[1]}" x2="{p11[0]}" y2="{p11[1]}" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>')
parts.append(f'<circle cx="{p11[0]}" cy="{p11[1]}" r="4" fill="#1a1a1a"/>')
parts.append(f'<rect x="{p11[0]+8}" y="{p11[1]-24}" width="46" height="16" fill="#ffffff"/>')
parts.append(f'<text x="{p11[0]+10}" y="{p11[1]-11}" font-size="12" fill="#1a1a1a">(1,1)</text>')

# ---- inline labels near each curve's end (white backing rect so grid/curve
# lines behind don't collide with the text) ----
def label(x, y, dx, dy, text, w, ha='start'):
    tx, ty = x + dx, y + dy
    rx = tx - (w if ha == 'end' else 2)
    parts.append(f'<rect x="{rx:.1f}" y="{ty-11:.1f}" width="{w}" height="15" fill="#ffffff" opacity="0.85"/>')
    anchor = f' text-anchor="{ha}"' if ha != 'start' else ''
    parts.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="12" fill="#1a1a1a"{anchor}>{text}</text>')

lx, ly = P(2.35, 2.35)
label(lx, ly, -4, -6, 'y=x', 30)

lx, ly = P(1.85, 3.0)
label(lx, ly, 4, 4, 'y=x²', 34)

lx, ly = P(1.05, 2.55)
label(lx, ly, -50, -6, 'y=x³', 34, ha='end')

lx, ly = P(2.5, 2.5 ** 0.5)
label(lx, ly, -48, -10, 'y=√x', 34)

lx, ly = P(-1.7, 1.0 / -1.7)
label(lx, ly, -6, -14, 'y=1/x', 40, ha='end')

parts.append('</svg>')

svg = '\n'.join(parts)
with open(os.path.join(OUT, 'diagram_power_functions.svg'), 'w', encoding='utf-8') as f:
    f.write(svg)
print('written diagram_power_functions.svg')
