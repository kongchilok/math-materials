# -*- coding: utf-8 -*-
"""L12 三角函數：講義與練習共用的圖。集中放這裡，兩個 build script 都 import，
避免 docx 版與 HTML 版的圖畫得不一樣（QB-V5 會查兩版同名元件外觀一致）。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coord_svg import coord_svg                # noqa: E402
from tri_svg import right_tri                  # noqa: E402

_QP = {1: (1.55, 1.25), 2: (-1.55, 1.25), 3: (-1.55, -1.25), 4: (1.55, -1.25)}
_QS = {1: ("x 是正", "y 是正"), 2: ("x 是負", "y 是正"),
       3: ("x 是負", "y 是負"), 4: ("x 是正", "y 是負")}


def quad_sign():
    """象限符號盤（卡二的圖）：四個象限各寫明哪幾個三角函數是正。"""
    return coord_svg(
        [{"t": "circle", "cx": 0, "cy": 0, "r": 2.0},
         {"t": "note", "x": 2.85, "y": 2.85, "text": "一：全部正", "bold": True},
         {"t": "note", "x": -2.85, "y": 2.85, "text": "二：只有 sin 正", "bold": True},
         {"t": "note", "x": -2.85, "y": -2.85, "text": "三：只有 tan 正", "bold": True},
         {"t": "note", "x": 2.85, "y": -2.85, "text": "四：只有 cos 正", "bold": True}],
        xlo=-4.4, xhi=4.4, ylo=-4.4, yhi=4.4, unit=24, grid=False, tick=0)


def quad_point(q):
    """某一象限上的一點 P，畫出 x、y 與半徑 r 三者的關係（D5 左欄用）。"""
    px, py = _QP[q]
    sx, sy = _QS[q]
    return coord_svg(
        [{"t": "circle", "cx": 0, "cy": 0, "r": 2.0},
         {"t": "seg", "x1": 0, "y1": 0, "x2": px, "y2": py, "sw": 1.9,
          "label": "r", "dx": -6 if px > 0 else 6, "dy": -6},
         {"t": "seg", "x1": px, "y1": py, "x2": px, "y2": 0, "dash": "4,3"},
         {"t": "point", "x": px, "y": py, "label": "P",
          "lp": "ne" if px > 0 else "nw"},
         # 兩行符號說明左右分開放：擺在 x＝0 會被 y 軸的直線由中間穿過（實測）
         {"t": "note", "x": -1.45, "y": -3.1, "text": sx},
         {"t": "note", "x": 1.45, "y": -3.1, "text": sy}],
        xlo=-3.0, xhi=3.0, ylo=-3.5, yhi=3.0, unit=23, grid=False, tick=0)


# 直角三角形：同一個三角形，focus 換一個角，三條邊的身份就全部對調
def tri_A():
    return right_tri(focus="A", angle_label="∠A")


def tri_B():
    return right_tri(focus="B", angle_label="∠B")


def tri_num(a="8", b="6", c="10"):
    return right_tri(sides=(a, b, c))


def tri_blank():
    return right_tri()


# ---- 練習用（D5 褪除：A 給半成品圖＋空欄，B 只給空白圖，C 不給）
def tri_qA():
    """練習A 第 1 題：兩條邊給了數字、斜邊留 ?，弧標在 ∠A。"""
    return right_tri(focus="A", sides=("8", "6", "?"), angle_label="∠A")


def tri_qB():
    return right_tri(focus="B", sides=("8", "6", "?"), angle_label="∠B")


def quad_blank():
    """練習B 用的空白象限圖：只有軸與圓，正負由學生自己標。"""
    return coord_svg([{"t": "circle", "cx": 0, "cy": 0, "r": 2.0}],
                     xlo=-3.0, xhi=3.0, ylo=-3.0, yhi=3.0,
                     unit=23, grid=False, tick=0)


if __name__ == "__main__":
    import design_svg as ds
    here = os.path.dirname(os.path.abspath(__file__))
    for name, svg in [("q", quad_sign()), ("q1", quad_point(1)),
                      ("q2", quad_point(2)), ("q3", quad_point(3)),
                      ("q4", quad_point(4)), ("tn", tri_num())]:
        ds.svg_to_png(svg, os.path.join(here, "_probe_%s.png" % name), scale=3)
    print("ok")
