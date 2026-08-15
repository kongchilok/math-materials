# -*- coding: utf-8 -*-
"""函數的表示方法與分段函數 講義／練習用圖：全部原生 design_svg，不用截圖。
每張圖同時輸出 .svg（HTML 內嵌用）與 .png（docx 內嵌用）。
"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
import design_svg as ds

OUT = os.path.dirname(os.path.abspath(__file__))
BIG = 99999.0   # 超出 yrange ⇒ parabola_graph 自動切斷，用嚟畫「半條射線」


def dump(svg, name):
    ds.save_svg(svg, os.path.join(OUT, name + '.svg'))
    ds.svg_to_png(svg, os.path.join(OUT, name + '.png'))
    print('  ->', name)


# ── 講義 情境：圖象法（文具店影印收費，x 只取正整數 ⇒ 一顆一顆分開的點）
pts = [(1, 0.5), (2, 1.0), (3, 1.5), (4, 2.0), (5, 2.5)]
dump(ds.parabola_graph(
    curves=[],
    points=[{'x': x, 'y': y, 'label': f'({x}, {y})', 'dx': 7, 'dy': -12}
            for x, y in pts],
    xrange=(0, 6), yrange=(0, 3), xstep=1, ystep=0.5,
    width=460, height=290,
    title='③ 圖象法：y = 0.5x（x 為正整數）',
), 'copy_scatter')

# ── 講義 §一 D5 圖文雙軌：y=|x| 拆成兩段，逐段對照
ABS_RANGE = dict(xrange=(-4, 4), yrange=(-1, 4), xstep=1, ystep=1,
                 width=300, height=210)
dump(ds.parabola_graph(
    curves=[{'f': lambda x: x if x >= 0 else BIG, 'style': 'solid',
             'label': {'x': 2.2, 'y': 3.4, 'text': 'y = x', 'anchor': 'start'}}],
    **ABS_RANGE), 'abs_right')
dump(ds.parabola_graph(
    curves=[{'f': lambda x: -x if x < 0 else BIG, 'style': 'solid',
             'label': {'x': -2.1, 'y': 3.5, 'text': 'y = −x', 'anchor': 'start'}}],
    **ABS_RANGE), 'abs_left')
dump(ds.parabola_graph(
    curves=[{'f': lambda x: abs(x), 'style': 'solid'}],
    points=[{'x': 0, 'y': 0, 'label': 'O(0, 0)', 'dx': 8, 'dy': -12}],
    **ABS_RANGE), 'abs_full')

# ── 練習A 側欄：0 為分界，兩段各自用哪條式（鷹架最密，式子照印）
dump(ds.domain_segments(
    lo=-4, hi=4, cuts=[0], labels=['f(x) = x+3', 'f(x) = x²−1'],
    width=300, caption='先看 x 落在哪一段，再代入該行'), 'seg_zero')

# ── 練習B 第5題側欄：分界點畫定，但每段用哪條式要學生自己寫（鷹架褪一級）
dump(ds.domain_segments(
    lo=0, hi=14, cuts=[2, 10], labels=['①', '②', '③'], label_size=14,
    width=300, step=2, caption='界線：2 公里、10 公里，共三段'), 'seg_taxi')

print('done ->', OUT)
