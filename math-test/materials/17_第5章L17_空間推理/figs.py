# -*- coding: utf-8 -*-
"""
第5章 L17 空間推理——本課專用圖形元件（摺紙展開圖／立體旋轉三面視圖）。
同 L16 一樣，design_svg.py 冇提供呢類圖案，本課獨立自建，唔動共用模組。
黑白列印優先：面與面用字母/符號區分，唔用顏色。
"""
import os
import sys

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from design_svg import INK, _txt, _rect, _svg, svg_to_png, save_svg  # noqa: E402

CELL = 90


def net_grid(cells, cell=CELL, highlight=()):
    """cells: {(row,col): label}，row/col 可以係任何整數，函式會自動平移到原點。
    highlight: 要加粗框嘅 (row,col) 集合（用嚟標示題目問緊嘅面）。
    冇畫嘅格仔（唔喺 cells 入面）留空白，唔畫框——用嚟砌「十字形」「Z字形」等展開圖形狀。"""
    rows = [r for r, c in cells]
    cols = [c for r, c in cells]
    r0, c0 = min(rows), min(cols)
    w = (max(cols) - c0 + 1) * cell
    h = (max(rows) - r0 + 1) * cell
    body = ''
    for (r, c), label in cells.items():
        x, y = (c - c0) * cell, (r - r0) * cell
        sw = 4.0 if (r, c) in highlight else 2.0
        body += _rect(x, y, cell, cell, fill='#ffffff', stroke=INK, sw=sw)
        body += _txt(x + cell / 2, y + cell / 2, label, size=30, bold=True)
    return _svg(w, h, body)


def face_row(labels, cell=CELL, gap=14, title=None):
    """一橫排標了字母嘅面（用於「呢個角度睇到嘅三個面」呢類視圖，唔畫立體透視，
    改以「同時睇到邊幾個面」嘅列表表示，避免 3D 透視畫錯令規律睇落矛盾）。"""
    n = len(labels)
    w = n * cell + (n - 1) * gap
    h = cell + (30 if title else 0)
    body = ''
    if title:
        body += _txt(w / 2, 16, title, size=15, bold=True)
    y0 = 26 if title else 0
    x = 0
    for label in labels:
        body += _rect(x, y0, cell, cell, fill='#ffffff', stroke=INK, sw=2.4)
        body += _txt(x + cell / 2, y0 + cell / 2, label, size=30, bold=True)
        x += cell + gap
    return _svg(w, h, body)


def save(name, svg, folder):
    figs = os.path.join(folder, 'figs')
    os.makedirs(figs, exist_ok=True)
    png = os.path.join(figs, name + '.png')
    svg_to_png(svg, png)
    save_svg(svg, os.path.join(figs, name + '.svg'))
    return png
