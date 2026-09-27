# -*- coding: utf-8 -*-
"""
figs_面積問題.py — 面積問題調適練習的 D5 標圖（黑白灰階）

每張圖都有兩個版本：
  fill=False（學生版）：已知量照印，要學生用 x 表示的邊長畫成「空白方格」；
  fill=True （教師版）：同一個方格內填上正確式子，方便批改時對照。
圖以實際列印尺寸（cm）繪製，插入 docx 時用同一個寬度，圖上的字就是真實 11pt。
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon, FancyArrowPatch

plt.rcParams['font.family'] = ['Microsoft JhengHei']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.unicode_minus'] = False

FS = 11          # 圖上字級（pt），與本文 12pt 相近
LW = 1.3         # 主線
GREY = '#BDBDBD'
LIGHT = '#E6E6E6'
HERE = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(HERE, '圖_面積問題')


def _canvas(w, h):
    fig = plt.figure(figsize=(w / 2.54, h / 2.54), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax


def _save(fig, name, fill):
    os.makedirs(FIG_DIR, exist_ok=True)
    path = os.path.join(FIG_DIR, f'{name}_{"教師" if fill else "學生"}.png')
    fig.savefig(path, dpi=300, facecolor='white')
    plt.close(fig)
    return path


def given(ax, x, y, s, **kw):
    """已知量：直接印（白底避免壓線）。"""
    ax.text(x, y, s, fontsize=FS, ha='center', va='center', zorder=6,
            bbox=dict(fc='white', ec='none', pad=0.6), **kw)


def slot(ax, x, y, ans, fill, w=1.5, h=0.62):
    """待填方格：學生版空白，教師版填入答案。方格一律保留，兩版位置一致。"""
    ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, fc='white', ec='black',
                           lw=0.9, zorder=5))
    if fill:
        ax.text(x, y, ans, fontsize=FS, ha='center', va='center', zorder=7)


def dim(ax, p, q, **kw):
    """尺寸線（兩端箭頭）。"""
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='<|-|>', mutation_scale=7,
                                 lw=0.8, color='black', zorder=3, **kw))


def ext(ax, p, q):
    """尺寸界線（細虛線）。"""
    ax.plot([p[0], q[0]], [p[1], q[1]], lw=0.6, color='black', ls=(0, (2, 2)), zorder=2)


# ------------------------------------------------------------------ 第 1 題
def q1(fill):
    fig, ax = _canvas(6.4, 3.6)
    A, B, C = (1.9, 0.9), (5.9, 0.9), (1.9, 2.57)       # 直角在 A；AB＝12、AC＝5 的比例
    ax.add_patch(Polygon([A, B, C], closed=True, fc='white', ec='black', lw=LW))
    s = 0.22
    ax.plot([A[0] + s, A[0] + s, A[0]], [A[1], A[1] + s, A[1] + s], lw=0.9, color='black')
    given(ax, 4.1, 2.05, '斜邊 $c$')
    slot(ax, 3.9, 0.42, '$c-1$', fill)
    slot(ax, 1.05, 1.73, '$c-8$', fill)
    return _save(fig, 'Q1', fill)


# ------------------------------------------------------------------ 第 2 題
def q2(fill):
    fig, ax = _canvas(6.0, 3.6)
    x0, y0, L, W = 1.5, 1.0, 4.0, 2.3
    ax.add_patch(Rectangle((x0, y0), L, W, fc='white', ec='black', lw=LW))
    given(ax, x0 + L / 2, y0 + W / 2, '面積 110 cm²')
    given(ax, 0.9, y0 + W / 2, '寬 $x$')
    ax.text(x0 + L / 2 - 1.25, 0.45, '長', fontsize=FS, ha='center', va='center')
    slot(ax, x0 + L / 2 + 0.1, 0.45, '$x+1$', fill)
    return _save(fig, 'Q2', fill)


# ------------------------------------------------------------------ 第 3 題
def q3(fill):
    fig, ax = _canvas(6.9, 4.2)
    cx, cy, a, b = 2.9, 2.45, 2.2, 1.3                   # 橫對角線較長
    P = [(cx - a, cy), (cx, cy + b), (cx + a, cy), (cx, cy - b)]
    ax.add_patch(Polygon(P, closed=True, fc='white', ec='black', lw=LW))
    ax.plot([cx - a, cx + a], [cy, cy], lw=0.9, color='black', ls=(0, (4, 2)))
    ax.plot([cx, cx], [cy - b, cy + b], lw=0.9, color='black', ls=(0, (4, 2)))
    # 橫對角線尺寸（下方）
    yd = 0.45
    ext(ax, (cx - a, cy - 0.1), (cx - a, yd - 0.1))
    ext(ax, (cx + a, cy - 0.1), (cx + a, yd - 0.1))
    dim(ax, (cx - a, yd), (cx + a, yd))
    given(ax, cx, yd, '較長對角線 $x$')
    # 直對角線尺寸（右方）
    xd = 6.05
    ext(ax, (cx + 0.1, cy + b), (xd + 0.1, cy + b))
    ext(ax, (cx + 0.1, cy - b), (xd + 0.1, cy - b))
    dim(ax, (xd, cy - b), (xd, cy + b))
    slot(ax, xd, cy, '$x-2$', fill, w=1.3)
    given(ax, 0.9, 3.85, '面積 4')
    return _save(fig, 'Q3', fill)


# ------------------------------------------------------------------ 第 4 題
def q4(fill):
    fig, ax = _canvas(6.6, 4.2)
    cx, cy, r, R = 2.2, 2.1, 1.2, 1.8                    # 10 : 15 ＝ 2 : 3
    ax.add_patch(Circle((cx, cy), R, fc=LIGHT, ec='black', lw=LW))
    ax.add_patch(Circle((cx, cy), r, fc=GREY, ec='black', lw=LW))
    ax.plot([cx], [cy], 'o', ms=2.5, color='black')
    # 向右：小圓半徑 x，再延長 5
    ax.plot([cx, cx + R], [cy, cy], lw=1.0, color='black')
    ax.plot([cx + r], [cy], 'o', ms=2.5, color='black')
    given(ax, cx + r / 2, cy + 0.3, '$x$')
    given(ax, cx + r + (R - r) / 2, cy + 0.3, '5')
    # 向右下：大圓半徑（待填）
    import math
    t = math.radians(-55)
    ex, ey = cx + R * math.cos(t), cy + R * math.sin(t)
    ax.plot([cx, ex], [cy, ey], lw=1.0, color='black')
    mx, my = cx + 0.62 * R * math.cos(t), cy + 0.62 * R * math.sin(t)
    ax.plot([mx, 4.55], [my, 0.75], lw=0.6, color='black')
    ax.text(5.35, 1.35, '大圓半徑', fontsize=FS, ha='center', va='center')
    slot(ax, 5.35, 0.75, '$x+5$', fill)
    return _save(fig, 'Q4', fill)


# ------------------------------------------------------------------ 第 6、7 題（靠牆）
def wall(name, wall_txt, inside, fill, ans_side, ans_par):
    fig, ax = _canvas(6.6, 4.2)
    ax.add_patch(Rectangle((0.3, 3.2), 6.0, 0.55, fc=GREY, ec='black', lw=LW))
    ax.text(3.3, 3.47, wall_txt, fontsize=FS, ha='center', va='center')
    x0, x1, y0, y1 = 1.6, 5.0, 1.0, 3.2
    ax.plot([x0, x0, x1, x1], [y1, y0, y0, y1], lw=2.0, color='black')   # 籬笆三邊（粗線）
    ax.text((x0 + x1) / 2, (y0 + y1) / 2, inside, fontsize=FS, ha='center', va='center')
    given(ax, 1.1, (y0 + y1) / 2, '$x$')
    slot(ax, 5.75, (y0 + y1) / 2, ans_side, fill, w=1.0)
    slot(ax, (x0 + x1) / 2, 0.45, ans_par, fill, w=1.9)
    ax.text(0.35, 0.45, '粗線＝籬笆', fontsize=9, ha='left', va='center')
    return _save(fig, name, fill)


def q6(fill):
    return wall('Q6', '牆（長 8 m）', '生物園', fill, '$x$', '$16-2x$')


def q7(fill):
    return wall('Q7', '房屋後牆（長 18 m）', '雞場', fill, '$x$', '$35-2x$')


# ------------------------------------------------------------------ 第 8 題
def q8(fill):
    fig, ax = _canvas(6.2, 4.9)
    X0, Y0, S, s = 1.9, 1.0, 3.4, 2.0                    # 小正方形放左下角，邊長增加 5 看得見
    ax.add_patch(Rectangle((X0, Y0), S, S, fc='white', ec='black', lw=LW))
    ax.add_patch(Rectangle((X0, Y0), s, s, fc=LIGHT, ec='black', lw=LW))
    ax.text(X0 + s / 2, Y0 + s / 2, '小花壇', fontsize=FS, ha='center', va='center')
    ax.text(X0 + S - 0.72, Y0 + S - 0.4, '大花壇', fontsize=FS, ha='center', va='center')
    yd = 0.45
    ext(ax, (X0, Y0 - 0.1), (X0, yd - 0.15))
    ext(ax, (X0 + s, Y0 - 0.1), (X0 + s, yd - 0.15))
    ext(ax, (X0 + S, Y0 - 0.1), (X0 + S, yd - 0.15))
    dim(ax, (X0, yd), (X0 + s, yd))
    dim(ax, (X0 + s, yd), (X0 + S, yd))
    given(ax, X0 + s / 2, yd, '$x$')
    given(ax, X0 + s + (S - s) / 2, yd, '5')
    xd = 1.2
    ext(ax, (X0 - 0.1, Y0), (xd - 0.15, Y0))
    ext(ax, (X0 - 0.1, Y0 + S), (xd - 0.15, Y0 + S))
    dim(ax, (xd, Y0), (xd, Y0 + S))
    slot(ax, xd, Y0 + S / 2, '$x+5$', fill, w=1.3)
    return _save(fig, 'Q8', fill)


# ------------------------------------------------------------------ 第 9、10 題（十字路）
def roads(name, L, W, pw, ph, vx, hy, fill):
    """左：原圖；右：把兩條路推到邊上，剩下的種植地拼成一個長方形。
    pw, ph＝圖上長方形的長寬（cm）；vx, hy＝直路／橫路在原圖的位置（比例）。"""
    rw = 0.32                                             # 路寬（圖上）
    gap = 3.4
    x0, y0 = 1.3, 1.0
    fig, ax = _canvas(x0 + 2 * pw + gap + 0.25, y0 + ph + 1.05)
    # ---------- 左圖 ----------
    ax.add_patch(Rectangle((x0, y0), pw, ph, fc='white', ec='black', lw=LW))
    vx0 = x0 + vx * pw
    hy0 = y0 + hy * ph
    ax.add_patch(Rectangle((vx0, y0), rw, ph, fc=GREY, ec='black', lw=0.9))
    ax.add_patch(Rectangle((x0, hy0), pw, rw, fc=GREY, ec='black', lw=0.9))
    given(ax, x0 + pw / 2, 0.45, f'{L} m')
    given(ax, x0 - 0.62, y0 + ph / 2, f'{W} m')
    given(ax, vx0 + rw / 2, y0 + ph + 0.3, '路寬 $x$')
    ax.text(x0 + pw / 2, y0 + ph + 0.75, '原圖', fontsize=FS, ha='center', va='center')
    # ---------- 箭頭 ----------
    ya = y0 + ph - 0.1                                    # 箭頭放上方，下方留位給待填方格
    ax.add_patch(FancyArrowPatch((x0 + pw + 0.3, ya), (x0 + pw + gap - 0.3, ya),
                                 arrowstyle='-|>', mutation_scale=12, lw=1.2, color='black'))
    ax.text(x0 + pw + gap / 2, ya + 0.35, '把路推到邊上', fontsize=9, ha='center', va='center')
    # ---------- 右圖 ----------
    X0 = x0 + pw + gap
    ax.add_patch(Rectangle((X0, y0), pw, ph, fc='white', ec='black', lw=LW))
    ax.add_patch(Rectangle((X0 + pw - rw, y0), rw, ph, fc=GREY, ec='black', lw=0.9))
    ax.add_patch(Rectangle((X0, y0 + ph - rw), pw, rw, fc=GREY, ec='black', lw=0.9))
    ax.text(X0 + (pw - rw) / 2, y0 + (ph - rw) / 2, '剩下的\n種植地', fontsize=FS,
            ha='center', va='center', linespacing=1.3)
    ax.text(X0 + pw / 2, y0 + ph + 0.75, '移動後', fontsize=FS, ha='center', va='center')
    slot(ax, X0 + (pw - rw) / 2, 0.45, f'${L}-x$', fill, w=1.5)
    slot(ax, X0 - 0.95, y0 + (ph - rw) / 2, f'${W}-x$', fill, w=1.5)
    return _save(fig, name, fill)


def q9(fill):
    return roads('Q9', 20, 16, 3.75, 3.0, 0.62, 0.42, fill)


def q10(fill):
    return roads('Q10', 60, 32, 4.2, 2.24, 0.2, 0.48, fill)


ALL = {1: q1, 2: q2, 3: q3, 4: q4, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10}


def make_all():
    """回傳 {題號: (學生版路徑, 教師版路徑)}。"""
    return {n: (f(False), f(True)) for n, f in ALL.items()}


if __name__ == '__main__':
    for n, (a, b) in make_all().items():
        print(n, a)
