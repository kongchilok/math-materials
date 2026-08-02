# -*- coding: utf-8 -*-
"""坐標平面繪圖工具（L8 直線與圓自建，L9 圓錐曲線可沿用）。

design_svg 只有數線、條形圖、天平等，沒有二維坐標系元件，
所以照 L7 parabola_svg 的做法自建：直接組 SVG 字串，共用 design_svg 的
_txt/_line/_svg 與 INK/RULE 常數，確保線寬、字型、灰階與其他圖一致。

x、y 用同一個 unit（等比例），否則圓會畫成橢圓、垂直線看起來不垂直
——本課正是要靠圖看出「垂直」與「圓」，比例一失真整個 D5 設計就失效。

item 格式（list of dict，t 指定種類）：
  {'t':'point','x':3,'y':2,'label':'A(3, 2)','filled':True,'lp':'ne'}
  {'t':'line','a':1,'b':-1,'c':2,'label':'x−y+2=0','dash':None}   # ax+by+c=0
  {'t':'circle','cx':1,'cy':0,'r':2,'label':'圓 C'}
  {'t':'seg','x1':0,'y1':0,'x2':3,'y2':2,'dash':'4,3','label':'5'}
  {'t':'ra','x':3,'y':0}                      # 直角記號（開口朝左上）
  {'t':'note','x':2,'y':4,'text':'…'}         # 圖上的文字註記

L9 圓錐曲線（2026-07-28 補）：
  {'t':'ellipse','cx':0,'cy':0,'a':5,'b':3}                    # x²/a²+y²/b²=1
  {'t':'hyper','a':4,'b':3,'orient':'h','asym':True}           # 'h' 橫向、'v' 縱向
  {'t':'parab','k':1,'vx':0,'vy':0,'dir':'up'}                 # dir: up/down/left/right
      # up/down: y = vy ± k(x−vx)²；left/right: x = vx ± k(y−vy)²
"""
import os
import sys

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
if SKILL not in sys.path:
    sys.path.insert(0, SKILL)
import design_svg as ds                        # noqa: E402

PAD = 24
LB = 13.5   # 圖上標籤字級（12 太小，3x 截圖再縮排版後中文筆畫會糊成方框）
TK = 12     # 刻度數字字級


def _n(v):
    """數字轉顯示字串：負號用 U+2212（跟 house-style 其餘圖一致）。"""
    s = ("%g" % v)
    return s.replace("-", "−")


def coord_svg(items, xlo=-5, xhi=5, ylo=-4, yhi=5, unit=24, grid=True,
              tick=1, axis_label=True, raw=False):
    W = (xhi - xlo) * unit + 2 * PAD
    H = (yhi - ylo) * unit + 2 * PAD

    def px(x):
        return PAD + (x - xlo) * unit

    def py(y):
        return PAD + (yhi - y) * unit

    b = ['<defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="3" '
         'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker></defs>' % ds.INK]

    # ---- 網格
    if grid:
        for i in range(int(xlo), int(xhi) + 1):
            b.append(ds._line(px(i), py(ylo), px(i), py(yhi), stroke="#d0d0d0", sw=0.7))
        for j in range(int(ylo), int(yhi) + 1):
            b.append(ds._line(px(xlo), py(j), px(xhi), py(j), stroke="#d0d0d0", sw=0.7))

    # ---- 圖形（先畫，讓軸壓在上面；點與標籤最後畫）
    late = []
    for it in items:
        t = it["t"]
        if t == "circle":
            b.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="%s" '
                     'stroke-width="1.9"/>'
                     % (px(it["cx"]), py(it["cy"]), it["r"] * unit, ds.INK))
            b.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>'
                     % (px(it["cx"]), py(it["cy"]), ds.INK))
            if it.get("label"):
                lx = it.get("lx", it["cx"])
                ly = it.get("ly", it["cy"] + it["r"])
                late.append(ds._txt(px(lx), py(ly) - 11, it["label"],
                                    size=LB, halo=True))
        elif t == "line":
            a, bb, c = it["a"], it["b"], it["c"]
            pts, eps = [], 1e-7
            if abs(bb) > eps:
                for x in (xlo, xhi):
                    y = -(a * x + c) / bb
                    if ylo - eps <= y <= yhi + eps:
                        pts.append((x, y))
            if abs(a) > eps:
                for y in (ylo, yhi):
                    x = -(bb * y + c) / a
                    if xlo - eps <= x <= xhi + eps:
                        pts.append((x, y))
            uniq = []
            for p in pts:
                if not any(abs(p[0] - q[0]) < 1e-6 and abs(p[1] - q[1]) < 1e-6
                           for q in uniq):
                    uniq.append(p)
            if len(uniq) >= 2:
                (x1, y1), (x2, y2) = uniq[0], uniq[1]
                b.append(ds._line(px(x1), py(y1), px(x2), py(y2), sw=1.9,
                                  dash=it.get("dash")))
                if it.get("label"):
                    # 標籤位置：預設放靠上那一端往內縮 22%；自動猜位常跟其他標籤
                    # 互撞（實測圓標籤與直線標籤疊在一起），可用 at=<x值> 指定。
                    if "at" in it:
                        lx = it["at"]
                        ly = (-(a * lx + c) / bb if abs(bb) > eps else (y1 + y2) / 2)
                    else:
                        if y1 < y2:
                            (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
                        lx, ly = x1 + (x2 - x1) * 0.22, y1 + (y2 - y1) * 0.22
                    late.append(ds._txt(px(lx) + it.get("ldx", 4),
                                        py(ly) + it.get("ldy", -9), it["label"],
                                        size=LB, anchor=it.get("lan", "start"),
                                        halo=True))
        elif t == "ellipse":
            # SVG 原生 <ellipse>，比採樣精確；x、y 同 unit 所以 a=b 時自動變成圓
            b.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="none" '
                     'stroke="%s" stroke-width="1.9"/>'
                     % (px(it.get("cx", 0)), py(it.get("cy", 0)),
                        it["a"] * unit, it["b"] * unit, ds.INK))
            if it.get("center", True):
                b.append('<circle cx="%.1f" cy="%.1f" r="2.4" fill="%s"/>'
                         % (px(it.get("cx", 0)), py(it.get("cy", 0)), ds.INK))
        elif t == "hyper":
            import math
            A, B = it["a"], it["b"]
            cx, cy = it.get("cx", 0), it.get("cy", 0)
            horiz = it.get("orient", "h") == "h"
            # 參數式 (a cosh t, b sinh t)；t 上限由視窗算出，兩支各畫一條 polyline
            lim = (xhi - cx) / A if horiz else (yhi - cy) / A
            tmax = math.acosh(max(1.02, abs(lim)))
            for sgn in (1, -1):
                pts = []
                for i in range(61):
                    t_ = -tmax + 2 * tmax * i / 60
                    u, v = A * math.cosh(t_) * sgn, B * math.sinh(t_)
                    X, Y = (cx + u, cy + v) if horiz else (cx + v, cy + u)
                    if xlo - 0.5 <= X <= xhi + 0.5 and ylo - 0.5 <= Y <= yhi + 0.5:
                        pts.append("%.1f,%.1f" % (px(X), py(Y)))
                if len(pts) > 1:
                    b.append('<polyline points="%s" fill="none" stroke="%s" '
                             'stroke-width="1.9"/>' % (" ".join(pts), ds.INK))
            if it.get("asym"):
                # 漸近線：橫向 y=±(b/a)x、縱向 y=±(a/b)x（都過中心）
                m = (B / A) if horiz else (A / B)
                for sm in (m, -m):
                    b.append(ds._line(px(xlo), py(cy + sm * (xlo - cx)),
                                      px(xhi), py(cy + sm * (xhi - cx)),
                                      sw=1.2, dash="5,4"))
            if it.get("center", True):
                b.append('<circle cx="%.1f" cy="%.1f" r="2.4" fill="%s"/>'
                         % (px(cx), py(cy), ds.INK))
        elif t == "parab":
            k, vx, vy = it["k"], it.get("vx", 0), it.get("vy", 0)
            dr = it.get("dir", "up")
            pts = []
            for i in range(81):
                if dr in ("up", "down"):
                    x = xlo + (xhi - xlo) * i / 80
                    y = vy + (k if dr == "up" else -k) * (x - vx) ** 2
                else:
                    y = ylo + (yhi - ylo) * i / 80
                    x = vx + (k if dr == "right" else -k) * (y - vy) ** 2
                if ylo - 0.5 <= y <= yhi + 0.5 and xlo - 0.5 <= x <= xhi + 0.5:
                    pts.append("%.1f,%.1f" % (px(x), py(y)))
            if len(pts) > 1:
                b.append('<polyline points="%s" fill="none" stroke="%s" '
                         'stroke-width="1.9"/>' % (" ".join(pts), ds.INK))
        elif t == "seg":
            b.append(ds._line(px(it["x1"]), py(it["y1"]), px(it["x2"]), py(it["y2"]),
                              sw=it.get("sw", 1.6), dash=it.get("dash")))
            if it.get("label"):
                mx, my = (it["x1"] + it["x2"]) / 2, (it["y1"] + it["y2"]) / 2
                late.append(ds._txt(px(mx) + it.get("dx", 0),
                                    py(my) + it.get("dy", -10),
                                    it["label"], size=LB, halo=True))
        elif t == "ra":
            s = 8.0
            sx = -1 if it.get("open", "lu") in ("lu", "ld") else 1
            sy = -1 if it.get("open", "lu") in ("lu", "ru") else 1
            X, Y = px(it["x"]), py(it["y"])
            b.append(ds._line(X + sx * s, Y, X + sx * s, Y + sy * s, sw=1.2))
            b.append(ds._line(X + sx * s, Y + sy * s, X, Y + sy * s, sw=1.2))

    # ---- 坐標軸
    if ylo <= 0 <= yhi:
        b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="1.5" marker-end="url(#ar)"/>'
                 % (px(xlo) - 8, py(0), px(xhi) + 10, py(0), ds.INK))
        if axis_label:
            b.append(ds._txt(px(xhi) + 16, py(0) + 1, "x", size=13, anchor="middle"))
    if xlo <= 0 <= xhi:
        b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                 'stroke-width="1.5" marker-end="url(#ar)"/>'
                 % (px(0), py(ylo) + 8, px(0), py(yhi) - 10, ds.INK))
        if axis_label:
            b.append(ds._txt(px(0) - 1, py(yhi) - 17, "y", size=13))

    # ---- 刻度數字
    if tick and ylo <= 0 <= yhi:
        for i in range(int(xlo), int(xhi) + 1):
            if i == 0 or i % tick:
                continue
            b.append(ds._line(px(i), py(0) - 3, px(i), py(0) + 3, sw=1.2))
            b.append(ds._txt(px(i), py(0) + 13, _n(i), size=TK, halo=True))
    if tick and xlo <= 0 <= xhi:
        for j in range(int(ylo), int(yhi) + 1):
            if j == 0 or j % tick:
                continue
            b.append(ds._line(px(0) - 3, py(j), px(0) + 3, py(j), sw=1.2))
            b.append(ds._txt(px(0) - 10, py(j), _n(j), size=TK, anchor="end", halo=True))
    if tick and xlo <= 0 <= xhi and ylo <= 0 <= yhi:
        # anchor=end 並多退 3px：置中時 O 會跟 x 軸的 −1 刻度貼在一起（實測 unit≤20）
        b.append(ds._txt(px(0) - 12, py(0) + 14, "O", size=TK, anchor="end",
                         halo=True))

    # ---- 點與延後的標籤
    for it in items:
        if it["t"] != "point":
            continue
        X, Y = px(it["x"]), py(it["y"])
        fill = "#ffffff" if it.get("filled") is False else ds.INK
        b.append('<circle cx="%.1f" cy="%.1f" r="4.2" fill="%s" stroke="%s" '
                 'stroke-width="1.6"/>' % (X, Y, fill, ds.INK))
        if it.get("label"):
            # lp：ne/nw/se/sw 四角，另加 n/s 正上下方——點正好在軸上或線上時，
            # 四角都會壓到刻度或線，只有正上／正下逃得掉（範例E 的交點 (1,3) 實測）。
            lp = it.get("lp", "ne")
            if lp in ("n", "s"):
                ox, oy, an = 0, (-12 if lp == "n" else 15), "middle"
            else:
                ox = -9 if "w" in lp else 9
                oy = -11 if "n" in lp else 13
                an = "end" if "w" in lp else "start"
            b.append(ds._txt(X + ox, Y + oy, it["label"], size=LB, anchor=an, halo=True))
    for it in items:
        if it["t"] == "note":
            b.append(ds._txt(px(it["x"]), py(it["y"]), it["text"],
                             size=it.get("size", LB), halo=True,
                             anchor=it.get("anchor", "middle"),
                             bold=it.get("bold", False)))
    b += late

    body = "".join(b)
    if raw:
        return {"w": W, "h": H, "body": body}
    return ds._svg(W, H, body)


def hstack(raws, gap=14, captions=None, cap_size=13):
    """把幾張 raw 圖橫向拼成一張（三種位置關係並排用）。"""
    cap_h = 20 if captions else 0
    W = sum(r["w"] for r in raws) + gap * (len(raws) - 1)
    H = max(r["h"] for r in raws) + cap_h
    parts, x = [], 0
    for i, r in enumerate(raws):
        parts.append('<g transform="translate(%.1f,0)">%s</g>' % (x, r["body"]))
        if captions:
            parts.append(ds._txt(x + r["w"] / 2, r["h"] + 10, captions[i],
                                 size=cap_size, bold=True))
        x += r["w"] + gap
    return ds._svg(W, H, "".join(parts))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_probe.png")
    svg = coord_svg([{"t": "circle", "cx": 1, "cy": 0, "r": 2, "label": "圓 C"},
                     {"t": "line", "a": 1, "b": -1, "c": 2, "label": "x−y+2=0"},
                     {"t": "point", "x": 3, "y": 2, "label": "A(3, 2)"},
                     {"t": "seg", "x1": 0, "y1": 0, "x2": 3, "y2": 2, "dash": "4,3"}],
                    xlo=-4, xhi=5, ylo=-3, yhi=4)
    ds.svg_to_png(svg, out, scale=3)
    print(out)
