# -*- coding: utf-8 -*-
"""公切線長度推導示意圖（兩圓外公切線／內公切線的輔助線construction）。

沿用 design_svg.py 的黑白列印風格（INK 黑線、RULE 淺灰、虛線＝輔助線），
自建一個雙面板圖：左＝外公切線（過小圓心 O2 作 O1A 的平行線，交 O1A 於 C，
O1C=R−r）、右＝內公切線（同法但 O2 的半徑指向 O1 對面，O1C=R+r）。
每面板都畫出「圓心→切點的半徑（垂直切線）→過小圓心作大圓半徑的平行線→
直角三角形 O1O2C」呢條輔助線，對應鐵律1（數學式／幾何論證要原生、唔靠純文字）。

幾何（數學座標，y 向上為正；畫圖時再轉成 screen 座標 y 向下）：
O1=(0,0)（大圓，半徑 R）、O2=(d,0)（小圓，半徑 r）。
外公切線：公用方向 u=(cosβ,sinβ)，cosβ=(R−r)/d；A=O1+Ru，B=O2+ru（同向）。
內公切線：方向 u'=(cosβ',sinβ')，cosβ'=(R+r)/d；A=O1+Ru'，B=O2−ru'（反向，切線穿過兩圓中間）。
兩種情況都取 C=O1+(R∓r)u（沿 O1 的半徑方向），令 O2C ⟂ u（即 O2C ∥ 切線 AB），
三角形 O1-O2-C 直角在 C，斜邊 O1O2=d，兩股 (R∓r) 與 L——這就是勾股定理推出
L=√(d²−(R∓r)²) 的來源。內公切線的 C 喺 O1A 延長線上（因為 R+r > R），會伸出
大圓之外，計版面 bounding box 時要連 C 一齊計，唔可以淨睇圓本身。
"""
import math
import os
import sys

sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
import design_svg as ds

INK = ds.INK
RULE = ds.RULE


def _circle(cx, cy, rad, sw=1.6):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{rad:.1f}" fill="none" stroke="{INK}" stroke-width="{sw}"/>'


def _dot(cx, cy, rad=2.8):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{rad}" fill="{INK}"/>'


def _rt_mark(px, py, d1, d2, size=9):
    """喺 (px,py) 畫直角記號；d1、d2 係兩條邊離開呢點嘅單位方向向量（screen 座標）。"""
    ax, ay = px + d1[0] * size, py + d1[1] * size
    cx, cy = px + d2[0] * size, py + d2[1] * size
    bx, by = ax + d2[0] * size, ay + d2[1] * size
    return (f'<path d="M {ax:.1f} {ay:.1f} L {bx:.1f} {by:.1f} L {cx:.1f} {cy:.1f}" '
            f'fill="none" stroke="{INK}" stroke-width="1.1"/>')


def _norm(vx, vy):
    n = math.hypot(vx, vy) or 1.0
    return vx / n, vy / n


def _panel_points(R, r, d, mode):
    """純數學：回傳 (O1,O2,A,B,C) 喺「數學座標」(y 向上為正、O1 在原點) 嘅座標。"""
    k = R - r if mode == 'ext' else R + r
    cosb = k / d
    sinb = math.sqrt(max(0.0, 1 - cosb * cosb))
    ux, uy = cosb, sinb
    O1 = (0.0, 0.0)
    O2 = (d, 0.0)
    A = (R * ux, R * uy)
    if mode == 'ext':
        B = (d + r * ux, r * uy)
    else:
        B = (d - r * ux, -r * uy)
    C = (k * ux, k * uy)
    return O1, O2, A, B, C, R, r


def _panel_svg(pts, ox, oy, title):
    """把數學座標的一組點轉做 screen 座標並畫出嚟；ox,oy = O1 嘅 screen 座標。
    回傳 (svg片段, 本面板喺 screen 座標嘅 bbox (x0,y0,x1,y1) 包括標題)。"""
    O1m, O2m, Am, Bm, Cm, R, r, mode = pts

    def ts(pm):
        return (ox + pm[0], oy - pm[1])

    O1, O2, A, B, C = ts(O1m), ts(O2m), ts(Am), ts(Bm), ts(Cm)

    body = [_circle(*O1, R), _circle(*O2, r)]
    body.append(ds._line(O1[0], O1[1], O2[0], O2[1], stroke=INK, sw=1.3))
    dlx = O1[0] + (O2[0] - O1[0]) * 0.28
    body.append(ds._txt(dlx, O1[1] + 15, 'd', size=13, halo=True))
    body.append(ds._line(O1[0], O1[1], A[0], A[1], stroke=INK, sw=1.2))
    body.append(ds._line(O2[0], O2[1], B[0], B[1], stroke=INK, sw=1.2))
    body.append(ds._line(A[0], A[1], B[0], B[1], stroke=INK, sw=2.2))
    body.append(ds._line(O2[0], O2[1], C[0], C[1], stroke=INK, sw=1.2, dash='4 3'))

    u_s = _norm(A[0] - O1[0], A[1] - O1[1])
    t_s = _norm(B[0] - A[0], B[1] - A[1])
    body.append(_rt_mark(A[0], A[1], (-u_s[0], -u_s[1]), t_s))
    v_s = _norm(B[0] - O2[0], B[1] - O2[1])
    body.append(_rt_mark(B[0], B[1], (-v_s[0], -v_s[1]), (-t_s[0], -t_s[1])))
    oc_s = _norm(O2[0] - C[0], O2[1] - C[1])
    body.append(_rt_mark(C[0], C[1], (-u_s[0], -u_s[1]), oc_s))

    # C 嘅標籤唔可以用 -u_s 方向（會退返去撞 A／O1C 嗰段）；改用垂直於 O1A 方向，
    # 揀「遠離切線 t_s」嗰一側，先唔好同 A、AB 疊埋。
    perp = (u_s[1], -u_s[0])
    if perp[0] * t_s[0] + perp[1] * t_s[1] > 0:   # 揀背向切線嗰一側
        perp = (-perp[0], -perp[1])
    # C 嘅標籤只用 perp（垂直於 O1A）方向推開，唔沿住 O1A 線本身推——
    # 沿線推無論邊個方向都會撞到別的嘢：推向 A 嗰邊（+u_s）會撞 A 個標籤
    # （外公切線 C、A 本身企得好近）；推向 O1 嗰邊（-u_s）又會撞埋
    # 「R−r」個標籤（佢都係擺喺 O1-C 線上）。純橫向推開先兩邊都唔撞。
    label_pts = [
        (O1, 'O₁', (-9, 18)), (O2, 'O₂', (9, 18)),
        (A, 'A', (-u_s[0] * 16 - 4, -u_s[1] * 16 - 4)),
        (B, 'B', (t_s[1] * 16, -t_s[0] * 16 + 4)),
        (C, 'C', (perp[0] * 20, perp[1] * 20)),
    ]
    for (px, py), lab, off in label_pts:
        body.append(_dot(px, py))
        body.append(ds._txt(px + off[0], py + off[1], lab, size=13, bold=True, halo=True))

    # 0.3 而非中點：內公切線嗰面 O1C=R+r 比較長，若擺喺 0.42 會同 A 嘅
    # 標籤（往 O1 方向偏移 16）逼得太埋；擺近 O1 啲兩個標籤先分得開。
    mcx = O1[0] + (C[0] - O1[0]) * 0.3
    mcy = O1[1] + (C[1] - O1[1]) * 0.3
    krlabel = 'R−r' if mode == 'ext' else 'R+r'
    body.append(ds._txt(mcx + perp[0] * 20, mcy + perp[1] * 20, krlabel, size=12, halo=True))
    # L 標喺切線 AB 靠近 B 嘅六成處（唔用中點）——內公切線嘅中點貼近 O1O2 線，
    # 會同 'd' 標籤疊埋；靠近 B 嗰段離開 O1O2 線較遠，讀得清楚啲。
    mtx, mty = A[0] + (B[0] - A[0]) * 0.62, A[1] + (B[1] - A[1]) * 0.62
    lperp = (-t_s[1], t_s[0])
    if lperp[0] * perp[0] + lperp[1] * perp[1] < 0:   # 同 C 嘅標籤揀同一側，唔好兩側亂跳
        lperp = (-lperp[0], -lperp[1])
    body.append(ds._txt(mtx + lperp[0] * 15, mty + lperp[1] * 15, 'L', size=13, bold=True, halo=True))

    xs = [p[0] for p, _, _ in label_pts] + [O1[0] - R, O2[0] + r]
    ys = [p[1] for p, _, _ in label_pts] + [O1[1] - R, O1[1] + R]
    bbox = (min(xs) - 24, min(ys) - 34, max(xs) + 24, max(ys) + 22)

    if title:
        ty = bbox[1] - 10
        body.append(ds._txt((bbox[0] + bbox[2]) / 2, ty, title, size=13, bold=True))
        bbox = (bbox[0], ty - 16, bbox[2], bbox[3])

    return ''.join(body), bbox


def tangent_construction_fig():
    """回傳完整 SVG 字串：左面板外公切線、右面板內公切線（bbox 驅動排版，避免裁切）。"""
    R1, r1, d1 = 58, 26, 118
    R2, r2, d2 = 48, 24, 118
    O1m, O2m, Am, Bm, Cm, R, r = _panel_points(R1, r1, d1, 'ext')
    pts_ext = (O1m, O2m, Am, Bm, Cm, R, r, 'ext')
    O1m2, O2m2, Am2, Bm2, Cm2, R2_, r2_ = _panel_points(R2, r2, d2, 'int')
    pts_int = (O1m2, O2m2, Am2, Bm2, Cm2, R2_, r2_, 'int')

    # 先用暫定原點畫，量出各自 bbox 相對於「O1 screen 座標」嘅位移，再正式排版
    tmp_left, bbox_l = _panel_svg(pts_ext, 0, 0, '外公切線：O₁C＝R−r')
    tmp_right, bbox_r = _panel_svg(pts_int, 0, 0, '內公切線：O₁C＝R+r')

    margin = 24
    oy = margin - bbox_l[1]                  # 令左面板 bbox 頂端對齊 margin
    oy_r = margin - bbox_r[1]
    oy_final = max(oy, oy_r)                  # 兩面板共用同一條 O1 水平線，取較大者

    ox_left = margin - bbox_l[0]
    left, bbox_l2 = _panel_svg(pts_ext, ox_left, oy_final, '外公切線：O₁C＝R−r')

    ox_right = ox_left + bbox_l[2] - bbox_l[0] + 60 - bbox_r[0]
    right, bbox_r2 = _panel_svg(pts_int, ox_right, oy_final, '內公切線：O₁C＝R+r')

    width = int(bbox_r2[2] + margin)
    height = int(max(bbox_l2[3], bbox_r2[3]) + margin)
    divider_x = (bbox_l2[2] + (ox_right + bbox_r[0])) / 2
    body = (left + right +
            f'<line x1="{divider_x:.1f}" y1="10" x2="{divider_x:.1f}" y2="{height - 10}" '
            f'stroke="{RULE}" stroke-width="1" stroke-dasharray="3 3"/>')
    return ds._svg(width, height, body)


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '_tangent_fig_demo'
    os.makedirs(out, exist_ok=True)
    svg = tangent_construction_fig()
    p = os.path.join(out, 'tangent_construction.svg')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(svg)
    ds.svg_to_png(svg, os.path.join(out, 'tangent_construction.png'))
    print('ok', p)
