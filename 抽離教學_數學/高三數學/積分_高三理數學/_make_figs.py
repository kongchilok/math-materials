# -*- coding: utf-8 -*-
# 定積分單元補圖：曲邊梯形面積、正負區域陷阱示意
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
import design_svg as ds

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_assets')
os.makedirs(OUT, exist_ok=True)

# 圖1：y=x^2 在 [0,2] 的曲邊梯形（對應範例六 S=∫[0,2]x^2 dx=8/3）
svg1 = ds.parabola_graph(
    curves=[{'f': lambda x: x**2, 'style': 'solid'}],
    shade=[{'f': lambda x: x**2, 'xmin': 0, 'xmax': 2}],
    vlines=[{'x': 0, 'label': 'x=0'}, {'x': 2, 'label': 'x=2'}],
    xrange=(-0.6, 3), yrange=(-1, 5), xstep=1, ystep=1, width=340, height=270,
)
ds.svg_to_png(svg1, os.path.join(OUT, 'fig_area_trapezoid.png'))
ds.save_svg(svg1, os.path.join(OUT, 'fig_area_trapezoid.svg'))

# 圖2：y=x 在 [-1,2]，示範正負區域陷阱——陰影一部分在x軸上方、一部分在下方
svg2 = ds.parabola_graph(
    curves=[{'f': lambda x: x, 'style': 'solid'}],
    shade=[{'f': lambda x: x, 'xmin': -1, 'xmax': 2}],
    vlines=[{'x': -1, 'label': 'x=−1'}, {'x': 2, 'label': 'x=2'}],
    xrange=(-2, 3), yrange=(-2, 3), xstep=1, ystep=1, width=340, height=270,
)
ds.svg_to_png(svg2, os.path.join(OUT, 'fig_area_sign_trap.png'))
ds.save_svg(svg2, os.path.join(OUT, 'fig_area_sign_trap.svg'))

print('done')
