# -*- coding: utf-8 -*-
"""函數的概念與定義域 講義／練習 用圖：全部原生 design_svg.number_line()，不用截圖。"""
import os, sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
import design_svg as ds

OUT = os.path.dirname(os.path.abspath(__file__))

# 講義：區間概念範例——半開半閉區間 [0,5) 在數線上的樣子
svg1 = ds.number_line(
    lo=-2, hi=8, step=1,
    interval=(0, 5, True, False),
    title='範例：區間 [0, 5) 畫在數線上',
    width=520,
)
ds.svg_to_png(svg1, os.path.join(OUT, 'interval_demo.png'))

print('done ->', OUT)
