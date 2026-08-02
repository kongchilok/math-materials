# -*- coding: utf-8 -*-
"""直角三角形繪圖工具（L12 三角函數自建）。

design_svg 沒有三角形元件，coord_svg 畫出來的三角形一定帶坐標軸與網格——
本課卡一要的是「一個乾淨的直角三角形」，有軸反而讓學生以為邊長要看刻度。
所以照 L8 coord_svg 的做法自建，共用 design_svg 的 _txt/_line/_svg 與 INK 常數，
線寬、字型、灰階與其他圖一致。

擺法固定（六個三角比的定義全部靠這個擺法講，中途不可改）：
    A 在左上、C 在左下（直角）、B 在右下。
    左邊豎邊 AC ＝ b（∠B 的對邊）；底邊 CB ＝ a（∠A 的對邊）；斜邊 AB ＝ c。

right_tri(focus='A')  在 A 角畫弧，並把三條邊標成「對邊／鄰邊／斜邊」——
                      focus 換成 'B' 時同一條邊的身份會對調，這正是本課要看見的事。
right_tri(sides=(...)) 三條邊改標數字（(a, b, c) 的顯示字串，None ＝不標）。
"""
import os
import sys

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
if SKILL not in sys.path:
    sys.path.insert(0, SKILL)
import design_svg as ds                        # noqa: E402

PAD = 30
LB = 13.5


def _arc(cx, cy, r, a0, a1):
    """在 (cx, cy) 畫一段弧（角度用度，SVG 的 y 向下所以取負）。"""
    import math
    x0 = cx + r * math.cos(math.radians(a0))
    y0 = cy - r * math.sin(math.radians(a0))
    x1 = cx + r * math.cos(math.radians(a1))
    y1 = cy - r * math.sin(math.radians(a1))
    return ('<path d="M%.1f,%.1f A%.1f,%.1f 0 0 %d %.1f,%.1f" fill="none" '
            'stroke="%s" stroke-width="1.2"/>'
            % (x0, y0, r, r, 0 if a1 > a0 else 1, x1, y1, ds.INK))


def right_tri(w=150, h=112, focus=None, sides=(None, None, None),
              verts=("A", "B", "C"), angle_label=None, raw=False):
    """畫一個 ∠C＝90° 的直角三角形。

    focus       : 'A' 或 'B'——在該角畫弧，三條邊改標「對邊／鄰邊／斜邊」
    sides       : (a, b, c) 三條邊要標的字串；a＝底邊 CB、b＝左豎邊 AC、c＝斜邊 AB
    angle_label : 焦點角旁邊的文字（預設用 focus 的頂點名）
    """
    W, H = w + 2 * PAD, h + 2 * PAD
    Cx, Cy = PAD, PAD + h            # 左下（直角）
    Ax, Ay = PAD, PAD                # 左上
    Bx, By = PAD + w, PAD + h        # 右下

    b = ['<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="none" '
         'stroke="%s" stroke-width="1.9"/>'
         % (Ax, Ay, Bx, By, Cx, Cy, ds.INK)]

    # 直角記號（開口朝右上，貼住 C）
    s = 11.0
    b.append(ds._line(Cx, Cy - s, Cx + s, Cy - s, sw=1.2))
    b.append(ds._line(Cx + s, Cy - s, Cx + s, Cy, sw=1.2))

    # 頂點名
    b.append(ds._txt(Ax - 12, Ay - 2, verts[0], size=LB, bold=True))
    b.append(ds._txt(Bx + 12, By + 2, verts[1], size=LB, bold=True))
    b.append(ds._txt(Cx - 12, Cy + 4, verts[2], size=LB, bold=True))

    # 焦點角的弧。A 角夾在「往下的 AC」與「往右下的 AB」之間，
    # 換算成數學角就是 −90° 到 atan(−h/w)；B 角夾在「往左的 BC」與「往左上的 BA」之間。
    import math
    slope = math.degrees(math.atan2(h, w))
    if focus == "A":
        b.append(_arc(Ax, Ay, 28, -90, -(90 - slope)))
        b.append(ds._txt(Ax + 20, Ay + 34, angle_label or verts[0], size=12))
    elif focus == "B":
        b.append(_arc(Bx, By, 28, 180, 180 - slope))
        b.append(ds._txt(Bx - 40, By - 15, angle_label or verts[1], size=12))

    # 三條邊的標籤（對邊／鄰邊／斜邊 或 數字）
    names = {"A": ("對邊", "鄰邊", "斜邊"), "B": ("鄰邊", "對邊", "斜邊")}
    tags = names.get(focus, (None, None, None))
    lab_a = sides[0] or tags[0]      # 底邊 CB
    lab_b = sides[1] or tags[1]      # 左豎邊 AC
    lab_c = sides[2] or tags[2]      # 斜邊 AB
    if lab_a:
        b.append(ds._txt((Cx + Bx) / 2, Cy + 15, lab_a, size=LB, halo=True))
    if lab_b:
        b.append(ds._vtext(Ax - 16, (Ay + Cy) / 2, lab_b, size=LB))
    if lab_c:
        b.append(ds._txt((Ax + Bx) / 2 + 14, (Ay + By) / 2 - 10, lab_c,
                         size=LB, halo=True))

    body = "".join(b)
    if raw:
        return {"w": W, "h": H, "body": body}
    return ds._svg(W, H, body)


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    ds.svg_to_png(right_tri(focus="A"), os.path.join(here, "_probe_a.png"), scale=3)
    ds.svg_to_png(right_tri(focus="B"), os.path.join(here, "_probe_b.png"), scale=3)
    ds.svg_to_png(right_tri(sides=("8", "6", "10")),
                  os.path.join(here, "_probe_n.png"), scale=3)
    print("ok")
