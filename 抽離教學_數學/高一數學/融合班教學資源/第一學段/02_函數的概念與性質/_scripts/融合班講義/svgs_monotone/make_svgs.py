# -*- coding: utf-8 -*-
"""Generate the 3 diagrams for 單調性與奇偶性 as hand-built coordinate SVGs."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------- diagram 1: 講義／單調性 intro — simple V-shaped piecewise graph ----------
def diagram1():
    W, H = 340, 240
    ox, oy = 170, 140   # pixel origin (x=0,y=0)
    sx, sy = 35, 25      # px per unit

    def P(x, y):
        return ox + sx * x, oy - sy * y

    A = P(-3, 1)
    B = P(0, -2)
    C = P(3, 2)

    svg = f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Microsoft JhengHei, Arial, sans-serif">
  <!-- axes -->
  <line x1="20" y1="{oy}" x2="320" y2="{oy}" stroke="#333" stroke-width="1.5"/>
  <polygon points="320,{oy} 312,{oy-4} 312,{oy+4}" fill="#333"/>
  <line x1="{ox}" y1="20" x2="{ox}" y2="220" stroke="#333" stroke-width="1.5"/>
  <polygon points="{ox},20 {ox-4},28 {ox+4},28" fill="#333"/>
  <text x="322" y="{oy+14}" font-size="13" fill="#333">x</text>
  <text x="{ox+8}" y="26" font-size="13" fill="#333">y</text>

  <!-- turning point dashed guide -->
  <line x1="{B[0]}" y1="{B[1]}" x2="{B[0]}" y2="{oy}" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- the piecewise curve -->
  <polyline points="{A[0]},{A[1]} {B[0]},{B[1]} {C[0]},{C[1]}" fill="none" stroke="#1a1a1a" stroke-width="2.5"/>
  <circle cx="{A[0]}" cy="{A[1]}" r="3" fill="#1a1a1a"/>
  <circle cx="{B[0]}" cy="{B[1]}" r="3" fill="#1a1a1a"/>
  <circle cx="{C[0]}" cy="{C[1]}" r="3" fill="#1a1a1a"/>

  <!-- labels -->
  <text x="{(A[0]+B[0])/2-30}" y="{(A[1]+B[1])/2-6}" font-size="14" fill="#1a1a1a">遞減 ↘</text>
  <text x="{(B[0]+C[0])/2-6}" y="{(B[1]+C[1])/2-10}" font-size="14" fill="#1a1a1a">↗ 遞增</text>
  <text x="{B[0]-10}" y="{oy+16}" font-size="12" fill="#555">最低點</text>
  <text x="8" y="16" font-size="12" fill="#555">O</text>
</svg>'''
    with open(os.path.join(OUT, 'diagram1_monotone_intro.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)


# ---------- diagram 2: 講義／奇偶性 intro — even (y-axis sym) vs odd (origin sym) ----------
def diagram2():
    W, H = 520, 220

    # left panel: y = 0.32 x^2, even function, y-axis symmetric
    lox, loy = 120, 190
    lsx, lsy = 15, 14
    xs = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    left_pts = []
    for x in xs:
        y = 0.32 * x * x
        left_pts.append((lox + lsx * x, loy - lsy * y))
    left_path = ' '.join(f'{px},{py}' for px, py in left_pts)

    # right panel: y = 0.04 x^3, odd function, origin symmetric
    rox, roy = 380, 110
    rsx, rsy = 15, 9
    right_pts = []
    for x in xs:
        y = 0.04 * x ** 3
        right_pts.append((rox + rsx * x, roy - rsy * y))
    right_path = ' '.join(f'{px},{py}' for px, py in right_pts)
    # symmetric point pair to illustrate 180-degree rotation
    xa = 4
    ya = 0.04 * xa ** 3
    PA = (rox + rsx * xa, roy - rsy * ya)
    PB = (rox - rsx * xa, roy + rsy * ya)

    svg = f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Microsoft JhengHei, Arial, sans-serif">
  <!-- left panel: even function -->
  <line x1="10" y1="{loy}" x2="230" y2="{loy}" stroke="#333" stroke-width="1.2"/>
  <line x1="{lox}" y1="15" x2="{lox}" y2="205" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <polyline points="{left_path}" fill="none" stroke="#1a1a1a" stroke-width="2.5"/>
  <text x="{lox-14}" y="{H-4}" font-size="13" fill="#333">y = x²（偶函數）</text>
  <text x="8" y="14" font-size="12" fill="#555">y軸對稱</text>

  <!-- divider -->
  <line x1="255" y1="10" x2="255" y2="210" stroke="#ccc" stroke-width="1"/>

  <!-- right panel: odd function -->
  <line x1="270" y1="{roy}" x2="500" y2="{roy}" stroke="#333" stroke-width="1.2"/>
  <line x1="{rox}" y1="15" x2="{rox}" y2="205" stroke="#333" stroke-width="1.2"/>
  <polyline points="{right_path}" fill="none" stroke="#1a1a1a" stroke-width="2.5"/>
  <circle cx="{rox}" cy="{roy}" r="2.5" fill="#1a1a1a"/>
  <circle cx="{PA[0]}" cy="{PA[1]}" r="3" fill="#1a1a1a"/>
  <circle cx="{PB[0]}" cy="{PB[1]}" r="3" fill="#1a1a1a"/>
  <line x1="{PA[0]}" y1="{PA[1]}" x2="{PB[0]}" y2="{PB[1]}" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="{rox-30}" y="{H-4}" font-size="13" fill="#333">y = x³（奇函數）</text>
  <text x="272" y="14" font-size="12" fill="#555">原點對稱（轉180°重合）</text>
</svg>'''
    with open(os.path.join(OUT, 'diagram2_parity_intro.svg'), 'w', encoding='utf-8') as f:
        f.write(svg)


# ---------- diagram 3: 練習A讀圖 — piecewise line through (-3,3),(0,-3),(4,1) with grid ----------
def diagram3():
    W, H = 380, 320
    ox, oy = 130, 210
    s = 25

    def P(x, y):
        return ox + s * x, oy - s * y

    svg_parts = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Microsoft JhengHei, Arial, sans-serif">']

    # grid lines
    for x in range(-4, 6):
        px, _ = P(x, 0)
        svg_parts.append(f'<line x1="{px}" y1="10" x2="{px}" y2="300" stroke="#e0e0e0" stroke-width="1"/>')
    for y in range(-4, 5):
        _, py = P(0, y)
        svg_parts.append(f'<line x1="30" y1="{py}" x2="255" y2="{py}" stroke="#e0e0e0" stroke-width="1"/>')

    # axes
    svg_parts.append(f'<line x1="25" y1="{oy}" x2="260" y2="{oy}" stroke="#333" stroke-width="1.5"/>')
    svg_parts.append(f'<polygon points="260,{oy} 252,{oy-4} 252,{oy+4}" fill="#333"/>')
    svg_parts.append(f'<line x1="{ox}" y1="15" x2="{ox}" y2="305" stroke="#333" stroke-width="1.5"/>')
    svg_parts.append(f'<polygon points="{ox},15 {ox-4},23 {ox+4},23" fill="#333"/>')
    svg_parts.append(f'<text x="262" y="{oy+14}" font-size="12" fill="#333">x</text>')
    svg_parts.append(f'<text x="{ox+8}" y="22" font-size="12" fill="#333">y</text>')

    # axis tick labels
    for x in range(-4, 6):
        if x == 0:
            continue
        px, _ = P(x, 0)
        svg_parts.append(f'<text x="{px-4}" y="{oy+16}" font-size="10" fill="#666">{x}</text>')
    for y in range(-4, 5):
        if y == 0:
            continue
        _, py = P(0, y)
        svg_parts.append(f'<text x="{ox+6}" y="{py+3}" font-size="10" fill="#666">{y}</text>')
    svg_parts.append(f'<text x="{ox-14}" y="{oy+14}" font-size="10" fill="#666">O</text>')

    A, Bp, C = P(-3, 3), P(0, -3), P(4, 1)
    svg_parts.append(f'<polyline points="{A[0]},{A[1]} {Bp[0]},{Bp[1]} {C[0]},{C[1]}" fill="none" stroke="#1a1a1a" stroke-width="2.5"/>')
    for (px, py), label, dx, dy in [(A, '(-3,3)', -34, -6), (Bp, '(0,-3)', 6, 16), (C, '(4,1)', 6, -8)]:
        svg_parts.append(f'<circle cx="{px}" cy="{py}" r="3.2" fill="#1a1a1a"/>')
        svg_parts.append(f'<text x="{px+dx}" y="{py+dy}" font-size="11" fill="#1a1a1a">{label}</text>')

    svg_parts.append('</svg>')
    with open(os.path.join(OUT, 'diagram3_practiceA_graph.svg'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_parts))


if __name__ == '__main__':
    diagram1()
    diagram2()
    diagram3()
    print('svgs written to', OUT)
