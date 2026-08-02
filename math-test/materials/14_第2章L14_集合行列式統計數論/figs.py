# -*- coding: utf-8 -*-
"""
L14 專用圖形：文氏圖（兩集合／三集合）、折線圖、長條圖。

design_svg.py 沒有這三種（它的 quadrant 是草稿分區、tree_diagram 是機率樹），
所以在本課自建，寫法照 design_svg 的規矩：
  ・回傳完整 SVG 字串，一定要帶 width／height 屬性（少了它 <img> 尺寸會變 0）
  ・純黑白：靠線型（實線／虛線）、填色（深灰／白底）、標記（● ▲）與文字分辨，
    不靠顏色（house-style 鐵律；黑白影印仍要看得出）
  ・同一張圖 docx 與 HTML 共用：docx 走 svg_to_png()＋image_para()，
    HTML 直接內嵌 SVG 字串。

自測：python figs.py <輸出資料夾>
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
import design_svg as ds                                   # noqa: E402

INK = ds.INK
RULE = ds.RULE
FILL = ds.FILL_LIGHT
MID = ds.FILL_MID


def _circle(cx, cy, r, dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<circle cx="%g" cy="%g" r="%g" fill="none" stroke="%s" '
            'stroke-width="1.6"%s/>' % (cx, cy, r, INK, d))


def _num(x, y, v, size=15):
    """區域內的數字（或留空給學生填的底線）。"""
    if v is None or v == "":
        return ('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" '
                'stroke-width="1.1"/>' % (x - 15, y + 5, x + 15, y + 5, RULE))
    return ds._txt(x, y, str(v), size=size, bold=True)


# ------------------------------------------------------------------ 文氏圖
def venn2(a_only, both, b_only, outside, la="A", lb="B",
          universe="全部", title=None):
    """兩集合文氏圖。四個數字：只在 A、兩者都、只在 B、兩者都不。
    傳 None 代表留空（練習用的空白圖）。"""
    b = [ds._rect(8, 8, 324, 204, fill="#ffffff")]
    b.append(ds._txt(24, 24, universe, size=12, anchor="start"))
    b.append(_circle(130, 120, 72))
    b.append(_circle(210, 120, 72))
    b.append(ds._txt(102, 36, la, size=14, bold=True))
    b.append(ds._txt(238, 36, lb, size=14, bold=True))
    b.append(_num(95, 120, a_only))
    b.append(_num(170, 120, both))
    b.append(_num(245, 120, b_only))
    b.append(_num(300, 196, outside))
    body = "".join(b)
    if title:
        body = ds._txt(170, 0, title, size=13, bold=True) + body
    return ds._svg(340, 220, body, pad=6 if not title else 18)


_V3 = dict(A=(112, 115, 68), B=(188, 115, 68), C=(150, 181, 68))
_V3POS = dict(a=(88, 97), b=(212, 97), c=(150, 215), ab=(150, 97),
              ac=(114, 163), bc=(186, 163), abc=(150, 143))


def venn3(regions, outside, labels=("A", "B", "C"), universe="全部", title=None):
    """三集合文氏圖。regions 是 dict，鍵為 a/b/c/ab/ac/bc/abc
    （只在該區的人數，不是總數）；值傳 None 代表留空。"""
    b = [ds._rect(8, 8, 324, 288, fill="#ffffff")]
    b.append(ds._txt(26, 24, universe, size=12, anchor="start"))
    for k in ("A", "B", "C"):
        cx, cy, r = _V3[k]
        b.append(_circle(cx, cy, r))
    b.append(ds._txt(74, 40, labels[0], size=13, bold=True))
    b.append(ds._txt(226, 40, labels[1], size=13, bold=True))
    b.append(ds._txt(150, 268, labels[2], size=13, bold=True))
    for k, (x, y) in _V3POS.items():
        b.append(_num(x, y, regions.get(k)))
    b.append(_num(300, 280, outside))
    body = "".join(b)
    if title:
        body = ds._txt(170, 0, title, size=13, bold=True) + body
    return ds._svg(340, 304, body, pad=6 if not title else 18)


# ------------------------------------------------------------------ 統計圖
_MARK = ("circle", "tri")


def _marker(x, y, kind):
    if kind == "circle":
        return ('<circle cx="%g" cy="%g" r="4.2" fill="%s" stroke="%s" '
                'stroke-width="1"/>' % (x, y, INK, INK))
    return ('<polygon points="%g,%g %g,%g %g,%g" fill="#ffffff" stroke="%s" '
            'stroke-width="1.6"/>' % (x, y - 5, x - 4.8, y + 4, x + 4.8, y + 4, INK))


def line_chart(xlabels, series, ylo=0, yhi=10, ystep=2,
               xtitle="", ytitle="", width=560, height=280):
    """折線圖。series＝[(名稱, 數值list, 'circle'/'tri', 實線或虛線), ...]
    兩條線用「實線＋●」與「虛線＋▲」分辨，不靠顏色。"""
    L, R, T, B = 66, 18, 30, 54
    pw, ph = width - L - R, height - T - B
    n = len(xlabels)
    dx = pw / (n - 1) if n > 1 else pw

    def px(i):
        return L + i * dx

    def py(v):
        return T + ph - (v - ylo) / (yhi - ylo) * ph

    b = [ds._rect(L, T, pw, ph, fill="#ffffff", sw=1.3)]
    v = ylo
    while v <= yhi + 1e-9:
        y = py(v)
        if v > ylo:
            b.append(ds._line(L, y, L + pw, y, stroke=RULE, sw=0.7,
                              dash="3 3" if v < yhi else None))
        b.append(ds._txt(L - 8, y, ("%g" % v), size=11, anchor="end"))
        v += ystep
    for i, lab in enumerate(xlabels):
        b.append(ds._line(px(i), T + ph, px(i), T + ph + 4, sw=1))
        b.append(ds._txt(px(i), T + ph + 15, lab, size=11))
    if ytitle:
        b.append(ds._vtext(16, T + ph / 2, ytitle, size=11))
    if xtitle:
        b.append(ds._txt(L + pw / 2, T + ph + 34, xtitle, size=11))

    lx = L + 4
    for name, vals, mk, dash in series:
        pts = " ".join("%g,%g" % (px(i), py(v)) for i, v in enumerate(vals))
        b.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"%s/>'
                 % (pts, INK, ' stroke-dasharray="6 4"' % () if dash else ""))
        for i, v in enumerate(vals):
            b.append(_marker(px(i), py(v), mk))
        b.append(_marker(lx + 8, T - 14, mk))
        b.append(ds._line(lx, T - 14, lx + 16, T - 14, sw=1.8,
                          dash="6 4" if dash else None))
        b.append(ds._txt(lx + 22, T - 14, name, size=11, anchor="start"))
        lx += 24 + len(name) * 12
    return ds._svg(width, height, "".join(b), pad=6)


def bar_chart(xlabels, series, ylo=0, yhi=10, ystep=2, hline=None,
              xtitle="", ytitle="", width=560, height=280):
    """分組長條圖。series＝[(名稱, 數值list, 'solid'/'open'), ...]
    hline＝[(y值, 標籤, 'solid'/'open'), ...]，用來畫「自身平均線」。
    平均線的標籤放在繪圖區「右邊之外」——放在區內會壓住長條（實測）。"""
    L, R, T, B = 66, (150 if hline else 18), 30, 54
    pw, ph = width - L - R, height - T - B
    n, m = len(xlabels), len(series)
    slot = pw / n
    bw = slot * 0.62 / m

    def py(v):
        return T + ph - (v - ylo) / (yhi - ylo) * ph

    b = [ds._rect(L, T, pw, ph, fill="#ffffff", sw=1.3)]
    v = ylo
    while v <= yhi + 1e-9:
        y = py(v)
        if v > ylo:
            b.append(ds._line(L, y, L + pw, y, stroke=RULE, sw=0.7, dash="3 3"))
        b.append(ds._txt(L - 8, y, ("%g" % v), size=11, anchor="end"))
        v += ystep
    for i, lab in enumerate(xlabels):
        b.append(ds._txt(L + slot * (i + 0.5), T + ph + 16, lab, size=11))
    for j, (name, vals, style) in enumerate(series):
        fill = MID if style == "solid" else "#ffffff"
        for i, val in enumerate(vals):
            x = L + slot * (i + 0.5) - (m * bw) / 2 + j * bw
            y = py(val)
            b.append(ds._rect(x, y, bw, T + ph - y, fill=fill, sw=1.3))
    for y0, lab, style in (hline or []):
        y = py(y0)
        b.append(ds._line(L, y, L + pw + 8, y, sw=1.5,
                          dash="8 4" if style == "open" else "2 3"))
        b.append(ds._txt(L + pw + 12, y, lab, size=10.5, anchor="start"))
    if ytitle:
        b.append(ds._vtext(16, T + ph / 2, ytitle, size=11))
    if xtitle:
        b.append(ds._txt(L + pw / 2, T + ph + 36, xtitle, size=11))
    lx = L + 4
    for name, vals, style in series:
        fill = MID if style == "solid" else "#ffffff"
        b.append(ds._rect(lx, T - 21, 16, 13, fill=fill, sw=1.2))
        b.append(ds._txt(lx + 21, T - 14, name, size=11, anchor="start"))
        lx += 30 + len(name) * 12
    return ds._svg(width, height, "".join(b), pad=6)


# ================================================================ 本課用圖
def fig_venn2_ex():
    """範例B：50 人，A 題對 42、B 題對 31、兩題都錯 4。"""
    return venn2(15, 27, 4, 4, la="答對 A 題", lb="答對 B 題", universe="全班 50 人")


def fig_venn2_blank():
    """練習第 5 題：同型但留空給學生填。
    ⚠ universe 要跟第 5 題的題幹一致（40 人），不是抄範例B 的 50 人——
    圖上的人數與題目對不上，學生會直接用錯（本課實測踩過）。"""
    return venn2(None, None, None, None,
                 la="答對第一條", lb="答對第二條", universe="全班 40 人")


def fig_venn3_ex():
    """範例C：60 人三題小考的七個區域。"""
    return venn3(dict(a=8, b=10, c=15, ab=4, ac=7, bc=5, abc=5), 6,
                 labels=("第一題對", "第二題對", "第三題對"), universe="全班 60 人")


def fig_venn3_blank():
    return venn3({}, None, labels=("第一題對", "第二題對", "第三題對"),
                 universe="全班 60 人")


SCORE = [4, 5, 7, 6, 5, 3, 5, 7, 8, 6, 4, 7]
STAFF = [3, 6, 5, 4, 6, 2, 4, 6, 7, 6, 5, 8]


def fig_line_ex():
    """範例F(a)：某部門 2024 年 1–12 月評分與優秀員工人數。"""
    return line_chart([str(i) for i in range(1, 13)],
                      [("部門評分", SCORE, "circle", False),
                       ("優秀員工人數", STAFF, "tri", True)],
                      ylo=0, yhi=10, ystep=2, xtitle="月份", ytitle="分數／人數")


BRIDGE_A = [6.2, 6.8, 7.0, 7.6, 8.0]
BRIDGE_B = [7.8, 8.0, 7.9, 7.7, 6.6]


def fig_bar_ex():
    """範例F(b)：A 橋與 B 橋 2015–2019 日均車流量（萬輛）。"""
    return bar_chart(["2015", "2016", "2017", "2018", "2019"],
                     [("A 橋", BRIDGE_A, "solid"), ("B 橋", BRIDGE_B, "open")],
                     ylo=6, yhi=8.5, ystep=0.5,
                     hline=[(7.12, "A 橋五年平均 7.12", "solid"),
                            (7.60, "B 橋五年平均 7.60", "open")],
                     xtitle="年份", ytitle="日均車流量（萬輛）")


SHOP_A = [120, 135, 128, 150, 167]
SHOP_B = [155, 168, 160, 149, 138]


def fig_bar_q7():
    """練習第 7 題：甲店與乙店 2020–2024 年銷售額（萬元）。
    平均線不畫——要學生自己算，這是本題的考點。"""
    return bar_chart(["2020", "2021", "2022", "2023", "2024"],
                     [("甲店", SHOP_A, "solid"), ("乙店", SHOP_B, "open")],
                     ylo=100, yhi=180, ystep=20,
                     xtitle="年份", ytitle="銷售額（萬元）")


ALL_FIGS = dict(venn2_ex=fig_venn2_ex, venn2_blank=fig_venn2_blank,
                venn3_ex=fig_venn3_ex, venn3_blank=fig_venn3_blank,
                line_ex=fig_line_ex, bar_ex=fig_bar_ex, bar_q7=fig_bar_q7)


def render_all(outdir):
    os.makedirs(outdir, exist_ok=True)
    made = {}
    for name, fn in ALL_FIGS.items():
        svg = fn()
        png = os.path.join(outdir, name + ".png")
        ds.svg_to_png(svg, png)
        made[name] = png
    return made


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "figs")
    for k, v in render_all(d).items():
        print(k, "->", v)
