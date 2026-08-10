# -*- coding: utf-8 -*-
"""Unit 4（坐標與坐標運算）用嘅圖：正方體疊加空間直角坐標系，D為原點。"""
import os
from space_diagram import Scene, render_png

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(HERE, '_assets')
os.makedirs(FIGDIR, exist_ok=True)

sc = Scene(width=440, height=400, origin=(120, 320))
sc.axes(xlen=1.0, ylen=3.3, zlen=3.3, origin_label=None)
sc.box(2, 2, 2, show_dots=True)
p = sc.save(os.path.join(FIGDIR, 'u4_fig1.svg'))
render_png(p, os.path.join(FIGDIR, 'u4_fig1.png'), sc.width, sc.height)
print('u4_fig1 done')
