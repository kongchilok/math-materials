# -*- coding: utf-8 -*-
"""
第4章 L16 圖形規律推理——本課專用圖形元件。
design_svg.py 冇提供幾何圖案（多邊形／圓點）嘅繪製，本課題型（B2 圖形規律推理）
需要畫「一格一格嘅圖案序列」，屬本課獨有需求，仿 L14 figs.py 慣例另外自建，
唔動 design_svg.py 呢個共用模組（CLAUDE.md 鐵律4：共用底層先可以改，版面層各自處理）。
黑白列印優先：多邊形用「空心／實心」區分，唔用顏色。
"""
import math
import os
import sys

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from design_svg import INK, _txt, _rect, _svg, svg_to_png, save_svg  # noqa: E402

BOX = 118   # 每格面板大小


def _poly_points(cx, cy, r, n, rotate=-90):
    """正 n 邊形頂點座標，rotate=-90 令第一個頂點在正上方（三角形視覺上尖朝上）。"""
    pts = []
    for i in range(n):
        a = math.radians(rotate + i * 360 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def polygon(cx, cy, r, n, solid=False, sw=2.6):
    """正 n 邊形（n=3 三角形…n=6 六邊形…本課只用到 3~6）。
    solid=True 為實心（黑白列印用純黑），False 為空心（白底黑框）。"""
    pts = _poly_points(cx, cy, r, n)
    d = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    fill = INK if solid else '#ffffff'
    return f'<polygon points="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"/>'


def dot(cx, cy, r=9, solid=True):
    fill = INK if solid else '#ffffff'
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="2"/>'


def dot_row(cx, cy, n, r=9, gap=24, solid=True, safe_w=None):
    """一格入面排 n 個圓點（用於「數量遞增」類題目），置中排列。
    n 大時（本課用到最多 6 粒）固定 gap=24 會令圓點排出 BOX 框外——
    自動按 n 收窄 gap／半徑，令成排圓點闊度唔會超過面板嘅安全闊度。"""
    if safe_w is None:
        safe_w = BOX - 26
    if n > 1:
        gap = min(gap, safe_w / (n - 1))
    r = min(r, max(5, gap * 0.4))
    x0 = cx - (n - 1) * gap / 2
    return ''.join(dot(x0 + i * gap, cy, r=r, solid=solid) for i in range(n))


def arrow(cx, cy, r=32, angle=0):
    """箭嘴圖案，angle=0 指向上，90 指向右，180 指向下，270 指向左（順時針）。"""
    a = math.radians(angle - 90)
    tip = (cx + r * math.cos(a), cy + r * math.sin(a))
    back = math.radians(angle - 90 + 180)
    tail = (cx + r * 0.55 * math.cos(back), cy + r * 0.55 * math.sin(back))
    wa1 = math.radians(angle - 90 + 150)
    wa2 = math.radians(angle - 90 - 150)
    w1 = (tip[0] + r * 0.5 * math.cos(wa1), tip[1] + r * 0.5 * math.sin(wa1))
    w2 = (tip[0] + r * 0.5 * math.cos(wa2), tip[1] + r * 0.5 * math.sin(wa2))
    line = (f'<line x1="{tail[0]:.1f}" y1="{tail[1]:.1f}" x2="{tip[0]:.1f}" y2="{tip[1]:.1f}" '
            f'stroke="{INK}" stroke-width="4"/>')
    head = (f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {w1[0]:.1f},{w1[1]:.1f} '
            f'{w2[0]:.1f},{w2[1]:.1f}" fill="{INK}"/>')
    return line + head


def arrow_row(cx, cy, n, angle, r=18, gap=32, safe_w=None):
    """一格入面排 n 支同方向嘅箭嘴（用於「數量＋方向」雙重規律題），置中排列。
    同 dot_row 一樣，n 大時要收窄 gap／半徑，唔可以排出 BOX 框外。"""
    if safe_w is None:
        safe_w = BOX - 40
    if n > 1:
        gap = min(gap, safe_w / (n - 1))
    r = min(r, max(10, gap * 0.55))
    x0 = cx - (n - 1) * gap / 2
    return ''.join(arrow(x0 + i * gap, cy, r=r, angle=angle) for i in range(n))


def _cell(x, y, size, content, is_q):
    g = _rect(x, y, size, size, fill='#ffffff', stroke=INK, sw=2)
    if is_q:
        g += _txt(x + size / 2, y + size / 2, '？', size=42, bold=True)
    elif content:
        g += f'<g transform="translate({x},{y})">{content}</g>'
    return g


def panel_row(panels, gap=22, sep='→'):
    """panels: [(content_svg_or_None, label_or_None, is_question), ...]
    橫排面板，之間用箭頭分隔，回傳完整 SVG 字串（含外框尺寸）。
    content_svg 座標假設面板原點在 (0,0)，函式內部會自動平移到正確格位。"""
    size = BOX
    n = len(panels)
    cell_h = size + 26
    total_w = n * size + (n - 1) * gap
    body = ''
    x = 0
    for i, (content, label, is_q) in enumerate(panels):
        body += _cell(x, 0, size, content, is_q)
        if label:
            body += _txt(x + size / 2, size + 18, label, size=15, bold=True)
        if i < n - 1:
            body += _txt(x + size + gap / 2, size / 2, sep, size=22, bold=True)
        x += size + gap
    return _svg(total_w, cell_h, body)


def two_row_grid(top_panels, bottom_panels, row_label_top='上排', row_label_bottom='下排',
                 gap=22, row_gap=34, label_w=64):
    """兩排面板（模仿題庫「六格分兩組，上下排各若干符號」格式），列與列之間唔畫箭頭。
    top_panels／bottom_panels: [(content_svg_or_None, is_question), ...]"""
    size = BOX
    n = max(len(top_panels), len(bottom_panels))
    row_w = n * size + (n - 1) * gap
    total_w = label_w + row_w
    h = size * 2 + row_gap

    def row(panels, y0):
        body = ''
        x = label_w
        for content, is_q in panels:
            body += _cell(x, y0, size, content, is_q)
            x += size + gap
        return body

    out = _txt(label_w - 10, size / 2, row_label_top, size=15, bold=True, anchor='end')
    out += row(top_panels, 0)
    out += _txt(label_w - 10, size + row_gap + size / 2, row_label_bottom, size=15,
               bold=True, anchor='end')
    out += row(bottom_panels, size + row_gap)
    return _svg(total_w, h, out)


def save(name, svg, folder):
    figs = os.path.join(folder, 'figs')
    os.makedirs(figs, exist_ok=True)
    png = os.path.join(figs, name + '.png')
    svg_to_png(svg, png)
    save_svg(svg, os.path.join(figs, name + '.svg'))
    return png
