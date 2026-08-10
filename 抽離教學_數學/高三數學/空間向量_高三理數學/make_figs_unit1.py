# -*- coding: utf-8 -*-
"""Unit 1（空間向量的概念與線性運算）用嘅圖：正方體 + 向量加法鏈（AB+BC+CC1=AC1體對角線）。"""
import os
from space_diagram import Scene, render_png

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(HERE, '_assets')
os.makedirs(FIGDIR, exist_ok=True)

# fig1：講義例——正方體，AB/BC/CC1 三段用細箭頭疊加標示，再畫粗箭頭AC1做結果
sc = Scene(width=420, height=380, origin=(110, 300))
verts = sc.box(2, 2, 2, show_dots=True)
sc.vec3(verts['A'], verts['C1'], color='#000', width=2.6)  # 結果向量 AC1（體對角線），較粗
p = sc.save(os.path.join(FIGDIR, 'u1_fig1.svg'))
render_png(p, os.path.join(FIGDIR, 'u1_fig1.png'), sc.width, sc.height)
print('u1_fig1 done')

# fig2：練習用——普通正方體，冇加畫任何向量，畀學生自己標
sc2 = Scene(width=380, height=340, origin=(100, 270))
sc2.box(2, 2, 2, show_dots=True)
p2 = sc2.save(os.path.join(FIGDIR, 'u1_fig2.svg'))
render_png(p2, os.path.join(FIGDIR, 'u1_fig2.png'), sc2.width, sc2.height)
print('u1_fig2 done')
