# -*- coding: utf-8 -*-
"""4.2 指數函數 融合版：全部圖形（D5 圖文雙軌左欄／練習側欄／D7 工具卡）。

黑白列印優先：兩條曲線靠線型（實線＝正在講的那條／虛線＝對照的另一型）＋
文字標籤區分，不靠顏色。

D5 的四張小圖**刻意各自不同**——同一條 y=2ˣ 印四次等於沒有雙軌對照：
  ① 定點  ：兩型同時出現，只在交點畫一個實心點
  ② 值域  ：放大左尾，三點越貼越近 x 軸（線始終喺軸上面）
  ③ 遞增  ：單條 a>1，標住 (1,2)(2,4) 睇住 y 爬升
  ④ 遞減  ：單條 0<a<1，標住 (1,0.5)(2,0.25) 睇住 y 下跌
小圖只有 232px 闊，中文標籤同座標標籤都好易撞線——數值同座標一律交畀
右欄嘅文字講，圖只負責「睇得見」。呢個分工正正係 D5 的本義。

標籤定位通則（實測踩過）：標籤要擺喺「該高度上曲線唔會穿過」嘅空區——
升型擺右下或左上、降型擺右上；擺喺 y 軸正上方會撞軸刻度。
"""
import os
import sys

SKILL = r'C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts'
sys.path.insert(0, SKILL)
import design_svg as ds  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(os.path.dirname(HERE), '_figs')
os.makedirs(FIGS, exist_ok=True)


def f_up(x):        # y = 2^x
    return 2.0 ** x


def f_down(x):      # y = (1/2)^x
    return 0.5 ** x


def f_3(x):         # y = 3^x
    return 3.0 ** x


def f_1_3(x):       # y = (1/3)^x
    return (1.0 / 3.0) ** x


FIG = {}

# ── 講義 §二：兩型對照大圖 ────────────────────────────────────────
# 曲線標籤一律揀「該高度上曲線右／左側的空區」，唔好擺喺曲線會穿過嘅位。
FIG['two_types'] = ds.parabola_graph(
    curves=[
        {'f': f_up, 'style': 'solid',
         'label': {'x': 1.30, 'y': 3.0, 'text': 'y = 2ˣ', 'anchor': 'end'}},
        {'f': f_down, 'style': 'dashed',
         'label': {'x': -1.30, 'y': 3.0, 'text': 'y = (1/2)ˣ', 'anchor': 'start'}},
    ],
    points=[{'x': 0, 'y': 1, 'label': '(0, 1)', 'dx': 10, 'dy': -36, 'r': 3.2}],
    # xmax 唔對稱：右邊虛線末端要離 x 軸箭頭夠遠，左邊實線末端冇箭頭所以可以行遠啲
    xrange=(-2.6, 2.3), yrange=(-1, 4.0), xstep=1, ystep=1,
    width=430, height=300)

# ── 講義 D5 圖文雙軌：每列一張小圖，左圖右式同列對齊 ────────────────
DT = dict(width=232, height=170, xstep=1)

FIG['dt_point'] = ds.parabola_graph(
    curves=[{'f': f_up, 'style': 'solid'},
            {'f': f_down, 'style': 'dashed'}],
    # 232px 細圖擺唔落「(0, 1)」而唔撞到兩條曲線——交點嘅實心點已經好清楚，
    # 座標由右欄講（D5：圖負責睇得見，字負責寫得出）
    points=[{'x': 0, 'y': 1, 'r': 3.2}],
    xrange=(-2.2, 2.55), yrange=(-0.5, 3.6), ystep=1, **DT)

# 放大左尾：睇住三點越貼越近 x 軸，但始終喺軸上面。
# 數值唔標喺圖上（232px 放唔落三個標籤而唔撞線）——交畀右欄講，正正係 D5 的本義。
FIG['dt_above'] = ds.parabola_graph(
    curves=[{'f': f_up, 'style': 'solid'}],
    # 三點都要離 x 軸有肉眼可見嘅罅——呢一列講緊「貼近但碰唔到」，
    # 個點自己坐咗落軸上面就推翻晒成句。圓點縮細＋縱向放大先夠位。
    points=[{'x': -1, 'y': 0.5, 'r': 3.2}, {'x': -2, 'y': 0.25, 'r': 3.2},
            {'x': -3, 'y': 0.125, 'r': 3.2}],
    xrange=(-4.2, 1.0), yrange=(-0.28, 1.7), ystep=0.5, **DT)

FIG['dt_inc'] = ds.parabola_graph(
    curves=[{'f': f_up, 'style': 'solid'}],
    # (0,1) 唔標字：佢啱啱好坐喺 y 軸上，標籤會同軸刻度「1」撞埋一舊
    points=[{'x': 0, 'y': 1, 'r': 3.2},
            {'x': 1, 'y': 2, 'label': '2', 'dx': -7, 'dy': -10, 'anchor': 'end'},
            {'x': 2, 'y': 4, 'label': '4', 'dx': -7, 'dy': -10, 'anchor': 'end'}],
    xrange=(-2.6, 2.6), yrange=(-0.6, 6.0), ystep=1, **DT)

FIG['dt_dec'] = ds.parabola_graph(
    curves=[{'f': f_down, 'style': 'solid'}],
    points=[{'x': 0, 'y': 1, 'r': 3.2},
            {'x': 1, 'y': 0.5, 'label': '0.5', 'dx': 0, 'dy': -13, 'anchor': 'middle'},
            {'x': 2, 'y': 0.25, 'label': '0.25', 'dx': 0, 'dy': -13, 'anchor': 'middle'}],
    xrange=(-1.2, 2.6), yrange=(-0.35, 2.3), ystep=0.5, **DT)

# ── 練習側欄（house-style：側欄圖用 300px 原生寬度畫，唔好縮舊圖）──
SIDE = dict(width=300, height=232, xstep=1, ystep=1)

FIG['p_3x'] = ds.parabola_graph(
    curves=[{'f': f_3, 'style': 'solid',
             'label': {'x': -1.45, 'y': 2.6, 'text': 'y = 3ˣ', 'anchor': 'start'}}],
    xrange=(-1.5, 1.4), yrange=(-0.6, 3.6), **SIDE)

FIG['p_1_3x'] = ds.parabola_graph(
    curves=[{'f': f_1_3, 'style': 'solid',
             'label': {'x': 0.35, 'y': 2.6, 'text': 'y = (1/3)ˣ', 'anchor': 'start'}}],
    xrange=(-1.2, 1.5), yrange=(-0.6, 3.6), **SIDE)

# 練習 B1：空白坐標格，學生自己描點連線。
# ystep=0.5：(a) 算到 y = 1/2，冇 0.5 格線就描唔準——而「自己描點」正正係 B 層嘅核心動作。
FIG['p_blank'] = ds.parabola_graph(
    # ymin 取 −0.5（＝一個 ystep）：再低就會多出一個「−0.5」刻度同「O」黐埋一齊
    curves=[], xrange=(-2.0, 2.6), yrange=(-0.5, 4.5),
    width=300, height=285, xstep=1, ystep=0.5)

# ── D7 工具卡：兩型各一張小圖 ────────────────────────────────────
# 兩張卡用同一組範圍先至對照得到。yrange 收窄係為咗谷高垂直解像度：
# 降型嘅曲線右端要離 x 軸箭頭夠遠，否則睇落似「掂到 x 軸」，同卡上「y > 0」自打嘴巴。
# xmax 亦要離最後一個刻度夠遠，否則刻度「2」會撞到軸名「x」。
CARD = dict(width=252, height=176, xrange=(-2.45, 2.45),
            yrange=(-0.6, 3.6), xstep=1, ystep=1)

FIG['card_up'] = ds.parabola_graph(
    curves=[{'f': f_up, 'style': 'solid'}],
    # 升型：標籤擺右下（x 軸同曲線之間嗰塊空區）。擺右上撞曲線，擺左上撞 y 軸刻度「2」
    points=[{'x': 0, 'y': 1, 'label': '(0, 1)', 'dx': 10, 'dy': 12, 'r': 3.2}], **CARD)

FIG['card_down'] = ds.parabola_graph(
    curves=[{'f': f_down, 'style': 'solid'}],
    points=[{'x': 0, 'y': 1, 'label': '(0, 1)', 'dx': 8, 'dy': -12, 'r': 3.2}], **CARD)


def build():
    for name, svg in FIG.items():
        ds.save_svg(svg, os.path.join(FIGS, f'{name}.svg'))
        ds.svg_to_png(svg, os.path.join(FIGS, f'{name}.png'))
    print(f'{len(FIG)} figures -> _figs')


if __name__ == '__main__':
    build()
