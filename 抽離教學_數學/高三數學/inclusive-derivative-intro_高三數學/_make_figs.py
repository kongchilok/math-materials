# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
import design_svg as ds

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
os.makedirs(FIG, exist_ok=True)

# 圖1：概念——割線 -> 切線
svg1 = ds.parabola_graph(
    curves=[
        {'f': lambda x: x*x, 'style': 'solid', 'label': {'x': 1.55, 'y': 4.9, 'text': 'f(x)=x²', 'anchor': 'start'}},
        {'f': lambda x: 2*x - 1, 'style': 'dashed', 'label': {'x': 1.75, 'y': 2.2, 'text': '切線 y=2x−1', 'anchor': 'start'}},
    ],
    points=[{'x': 1, 'y': 1, 'label': '(1,1)', 'dx': -36, 'dy': 16}],
    xrange=(-0.5, 3.4), yrange=(-0.5, 5.5), xstep=1, ystep=1,
    width=340, height=250,
)
ds.save_svg(svg1, os.path.join(FIG, 'fig_concept_tangent.svg'))
ds.svg_to_png(svg1, os.path.join(FIG, 'fig_concept_tangent.png'))

# 圖2：單調性與極值
def f2(x):
    return x**3/3 - x**2/2 - 2*x + 1
svg2 = ds.parabola_graph(
    curves=[{'f': f2, 'style': 'solid'}],
    points=[
        {'x': -1, 'y': f2(-1), 'label': '極大 (−1, 13/6)', 'dx': -10, 'dy': -16, 'anchor': 'end'},
        {'x': 2, 'y': f2(2), 'label': '極小 (2, −7/3)', 'dx': 10, 'dy': 20},
    ],
    vlines=[{'x': -1, 'label': 'x=−1'}, {'x': 2, 'label': 'x=2'}],
    xrange=(-3.2, 4.2), yrange=(-7.5, 8), xstep=1, ystep=2,
    width=360, height=300,
)
ds.save_svg(svg2, os.path.join(FIG, 'fig_monotonicity.svg'))
ds.svg_to_png(svg2, os.path.join(FIG, 'fig_monotonicity.png'))

# 圖3：凹凸性與拐點
def f3(x):
    return x**3 - 3*x**2
svg3 = ds.parabola_graph(
    curves=[{'f': f3, 'style': 'solid'}],
    points=[{'x': 1, 'y': f3(1), 'label': '拐點 (1, −2)', 'dx': 10, 'dy': -8}],
    vlines=[{'x': 1, 'label': 'x=1'}],
    xrange=(-1.5, 3.5), yrange=(-5.5, 8), xstep=1, ystep=2,
    width=360, height=300,
)
ds.save_svg(svg3, os.path.join(FIG, 'fig_concavity.svg'))
ds.svg_to_png(svg3, os.path.join(FIG, 'fig_concavity.png'))

print('regenerated')
