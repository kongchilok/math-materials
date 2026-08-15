# -*- coding: utf-8 -*-
"""坐標圖 / 數線 SVG helper（供線性規劃＋解不等式融合班講義用）。
- 產生 SVG 字串（HTML 內嵌用）
- svg_to_png(): headless Chrome 截圖轉 PNG（docx image_para 內嵌用）
黑白列印優先：半平面／區域用淺灰填色（非難度色），界線黑色，虛實線表示邊界屬否。
"""
import os
import subprocess

CHROME = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
          r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]


def _chrome():
    for c in CHROME:
        if os.path.exists(c):
            return c
    raise RuntimeError("Chrome not found")


def svg_to_png(svg, png_path, scale=3):
    """把 SVG 字串截圖成 PNG。寬高由 svg 的 data-w/data-h 屬性讀取。"""
    import re
    w = int(re.search(r'data-w="(\d+)"', svg).group(1))
    h = int(re.search(r'data-h="(\d+)"', svg).group(1))
    html = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            f'html,body{{margin:0;padding:0;overflow:hidden;background:#fff;}}'
            f'.wrap{{width:{w}px;height:{h}px;}}svg{{width:{w}px;height:{h}px;}}'
            f'</style></head><body><div class="wrap">{svg}</div></body></html>')
    html_path = png_path + '.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    uri = 'file:///' + os.path.abspath(html_path).replace('\\', '/')
    subprocess.run([_chrome(), '--headless', '--disable-gpu', '--no-sandbox',
                    '--disable-dev-shm-usage', '--hide-scrollbars',
                    f'--force-device-scale-factor={scale}',
                    f'--window-size={w},{h}',
                    f'--screenshot={os.path.abspath(png_path)}', uri],
                   capture_output=True)
    try:
        os.remove(html_path)
    except OSError:
        pass
    if not os.path.exists(png_path) or os.path.getsize(png_path) < 500:
        raise RuntimeError('screenshot failed: ' + png_path)


def _clip_halfplane(poly, a, b, c, keep_le):
    """Sutherland-Hodgman：把多邊形 poly 對半平面 a*x+b*y (<=|>=) c 裁剪。"""
    def f(p):
        return a * p[0] + b * p[1] - c
    out = []
    n = len(poly)
    for i in range(n):
        cur, nxt = poly[i], poly[(i + 1) % n]
        fc, fn = f(cur), f(nxt)
        ci = (fc <= 1e-9) if keep_le else (fc >= -1e-9)
        ni = (fn <= 1e-9) if keep_le else (fn >= -1e-9)
        if ci:
            out.append(cur)
        if ci != ni:
            t = fc / (fc - fn)
            out.append((cur[0] + t * (nxt[0] - cur[0]),
                        cur[1] + t * (nxt[1] - cur[1])))
    return out


class Grid:
    def __init__(self, xmin, xmax, ymin, ymax, s=24, pad=22):
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.s, self.pad = s, pad
        self.W = (xmax - xmin) * s + 2 * pad
        self.H = (ymax - ymin) * s + 2 * pad
        self.ox = pad - xmin * s
        self.oy = pad + ymax * s
        self.p = []

    def P(self, x, y):
        return self.ox + self.s * x, self.oy - self.s * y

    def _open(self):
        return (f'<svg viewBox="0 0 {self.W} {self.H}" data-w="{self.W}" data-h="{self.H}" '
                f'xmlns="http://www.w3.org/2000/svg" '
                f'font-family="Microsoft JhengHei, Noto Sans TC, Arial, sans-serif">')

    def base(self, ticks=True):
        p = self.p
        for x in range(self.xmin, self.xmax + 1):
            x0, y1 = self.P(x, self.ymax)
            _, y2 = self.P(x, self.ymin)
            p.append(f'<line x1="{x0}" y1="{y1}" x2="{x0}" y2="{y2}" stroke="#e4e4e4" stroke-width="1"/>')
        for y in range(self.ymin, self.ymax + 1):
            x1, y0 = self.P(self.xmin, y)
            x2, _ = self.P(self.xmax, y)
            p.append(f'<line x1="{x1}" y1="{y0}" x2="{x2}" y2="{y0}" stroke="#e4e4e4" stroke-width="1"/>')
        ax0, ay = self.P(self.xmin, 0)
        ax1, _ = self.P(self.xmax, 0)
        p.append(f'<line x1="{ax0}" y1="{ay}" x2="{ax1}" y2="{ay}" stroke="#333" stroke-width="1.5"/>')
        p.append(f'<polygon points="{ax1},{ay} {ax1-7},{ay-4} {ax1-7},{ay+4}" fill="#333"/>')
        ax, by0 = self.P(0, self.ymin)
        _, by1 = self.P(0, self.ymax)
        p.append(f'<line x1="{ax}" y1="{by0}" x2="{ax}" y2="{by1}" stroke="#333" stroke-width="1.5"/>')
        p.append(f'<polygon points="{ax},{by1} {ax-4},{by1+7} {ax+4},{by1+7}" fill="#333"/>')
        p.append(f'<text x="{ax1+3}" y="{ay+5}" font-size="12" fill="#333">x</text>')
        p.append(f'<text x="{ax+7}" y="{by1+4}" font-size="12" fill="#333">y</text>')
        p.append(f'<text x="{self.ox-13}" y="{self.oy+14}" font-size="11" fill="#666">O</text>')
        if ticks:
            for x in range(self.xmin, self.xmax + 1):
                if x == 0 or x == self.xmax:
                    continue
                px, _ = self.P(x, 0)
                p.append(f'<text x="{px-3}" y="{self.oy+14}" font-size="10" fill="#777">{x}</text>')
            for y in range(self.ymin, self.ymax + 1):
                if y == 0 or y == self.ymax:
                    continue
                _, py = self.P(0, y)
                anchor = 'end'
                p.append(f'<text x="{self.ox-6}" y="{py+3}" font-size="10" fill="#777" text-anchor="{anchor}">{y}</text>')
        return self

    def line_pts(self, x1, y1, x2, y2, dashed=False, w=2.2):
        (px1, py1), (px2, py2) = self.P(x1, y1), self.P(x2, y2)
        da = ' stroke-dasharray="6,4"' if dashed else ''
        self.p.append(f'<line x1="{px1}" y1="{py1}" x2="{px2}" y2="{py2}" stroke="#111" stroke-width="{w}"{da}/>')
        return self

    def line_abc(self, a, b, c, dashed=False, w=2.2):
        """畫直線 a*x+b*y=c，自動延伸到視窗邊界。"""
        pts = []
        if b != 0:
            for xv in (self.xmin, self.xmax):
                yv = (c - a * xv) / b
                if self.ymin - 0.001 <= yv <= self.ymax + 0.001:
                    pts.append((xv, yv))
        if a != 0:
            for yv in (self.ymin, self.ymax):
                xv = (c - b * yv) / a
                if self.xmin - 0.001 <= xv <= self.xmax + 0.001:
                    pts.append((xv, yv))
        # 去重取兩端
        uniq = []
        for pt in pts:
            if all(abs(pt[0] - u[0]) > 1e-6 or abs(pt[1] - u[1]) > 1e-6 for u in uniq):
                uniq.append(pt)
        if len(uniq) >= 2:
            self.line_pts(uniq[0][0], uniq[0][1], uniq[1][0], uniq[1][1], dashed=dashed, w=w)
        return self

    def shade(self, a, b, c, keep_le, opacity=0.30):
        """填淺灰於半平面 a*x+b*y (<=|>=) c 的一側。"""
        rect = [(self.xmin, self.ymin), (self.xmax, self.ymin),
                (self.xmax, self.ymax), (self.xmin, self.ymax)]
        poly = _clip_halfplane(rect, a, b, c, keep_le)
        if len(poly) >= 3:
            pts = ' '.join(f'{self.P(x, y)[0]},{self.P(x, y)[1]}' for x, y in poly)
            self.p.append(f'<polygon points="{pts}" fill="#8a8f96" fill-opacity="{opacity}" stroke="none"/>')
        return self

    def shade_poly(self, verts, opacity=0.30, stroke=True):
        """填一個以資料座標頂點列表 verts 定義的多邊形（可行域），預設含黑色邊框。"""
        pts = ' '.join(f'{self.P(x, y)[0]},{self.P(x, y)[1]}' for x, y in verts)
        st = ' stroke="#111" stroke-width="1.8"' if stroke else ' stroke="none"'
        self.p.append(f'<polygon points="{pts}" fill="#8a8f96" fill-opacity="{opacity}"{st}/>')
        return self

    def dot(self, x, y, label=None, dx=6, dy=-6, r=3.2):
        px, py = self.P(x, y)
        self.p.append(f'<circle cx="{px}" cy="{py}" r="{r}" fill="#111"/>')
        if label:
            self.p.append(f'<text x="{px+dx}" y="{py+dy}" font-size="11" fill="#111">{label}</text>')
        return self

    def text_at(self, x, y, s, size=12, fill="#111"):
        px, py = self.P(x, y)
        self.p.append(f'<text x="{px}" y="{py}" font-size="{size}" fill="{fill}">{s}</text>')
        return self

    def svg(self):
        return self._open() + ''.join(self.p) + '</svg>'


def number_line(xmin, xmax, marks, s=40, pad=26, label_y=True):
    """數線：marks 為 [(x, 'label', filled_bool), ...]；filled=實心點含端點，空心=不含。
    回傳 SVG 字串。用於解不等式的解集示意（可含陰影區間）。"""
    W = (xmax - xmin) * s + 2 * pad
    H = 60
    oy = 34
    ox = pad - xmin * s

    def X(v):
        return ox + s * v
    parts = [f'<svg viewBox="0 0 {W} {H}" data-w="{W}" data-h="{H}" '
             f'xmlns="http://www.w3.org/2000/svg" font-family="Microsoft JhengHei, Arial, sans-serif">']
    parts.append(f'<line x1="6" y1="{oy}" x2="{W-6}" y2="{oy}" stroke="#333" stroke-width="1.5"/>')
    parts.append(f'<polygon points="{W-6},{oy} {W-14},{oy-4} {W-14},{oy+4}" fill="#333"/>')
    parts.append(f'<polygon points="6,{oy} 14,{oy-4} 14,{oy+4}" fill="#333"/>')
    for v in range(xmin, xmax + 1):
        px = X(v)
        parts.append(f'<line x1="{px}" y1="{oy-4}" x2="{px}" y2="{oy+4}" stroke="#333" stroke-width="1.2"/>')
        parts.append(f'<text x="{px-3}" y="{oy+18}" font-size="11" fill="#555">{v}</text>')
    for m in marks:
        x, lab, filled = m[0], m[1], m[2]
        px = X(x)
        fill = '#111' if filled else '#fff'
        parts.append(f'<circle cx="{px}" cy="{oy}" r="4.5" fill="{fill}" stroke="#111" stroke-width="1.6"/>')
        if lab:
            parts.append(f'<text x="{px-4}" y="{oy-10}" font-size="11" fill="#111">{lab}</text>')
    parts.append('</svg>')
    return ''.join(parts)


def serpentine(xmin, xmax, roots, labels=None, s=42, pad=30, amp=24):
    """穿線法（序軸標根法）示意：數線＋一條由右上蛇形穿過各根的曲線。
    roots 由小到大；最右區間為正（曲線在軸上方）。回傳 SVG 字串。"""
    roots = sorted(roots)
    n = len(roots)
    W = (xmax - xmin) * s + 2 * pad
    Hh = 2 * amp + 46
    oy = amp + 20
    ox = pad - xmin * s

    def X(v):
        return ox + s * v
    parts = [f'<svg viewBox="0 0 {W} {Hh}" data-w="{W}" data-h="{Hh}" '
             f'xmlns="http://www.w3.org/2000/svg" font-family="Microsoft JhengHei, Arial, sans-serif">']
    # 數線
    parts.append(f'<line x1="6" y1="{oy}" x2="{W-6}" y2="{oy}" stroke="#333" stroke-width="1.4"/>')
    parts.append(f'<polygon points="{W-6},{oy} {W-14},{oy-4} {W-14},{oy+4}" fill="#333"/>')
    parts.append(f'<polygon points="6,{oy} 14,{oy-4} 14,{oy+4}" fill="#333"/>')
    # sign for interval i (0=最左)：(-1)^(n-i)
    def sgn(i):
        return 1 if ((n - i) % 2 == 0) else -1
    # 蛇形路徑：M 左端 → 逐根 Q(區間極值, 根在軸上)
    bounds = [xmin] + roots + [xmax]
    d = f'M {X(xmin)} {oy - sgn(0)*amp*0.55} '
    for i in range(n):
        mid = (bounds[i] + bounds[i + 1]) / 2
        d += f'Q {X(mid)} {oy - sgn(i)*amp} {X(roots[i])} {oy} '
    mid = (roots[-1] + xmax) / 2
    d += f'Q {X(mid)} {oy - sgn(n)*amp} {X(xmax)} {oy - sgn(n)*amp*0.55} '
    parts.append(f'<path d="{d}" fill="none" stroke="#111" stroke-width="2"/>')
    # 根（空心點）＋標籤
    for idx, r in enumerate(roots):
        px = X(r)
        parts.append(f'<circle cx="{px}" cy="{oy}" r="4" fill="#fff" stroke="#111" stroke-width="1.6"/>')
        lab = labels[idx] if labels else str(r)
        parts.append(f'<text x="{px-4}" y="{oy+18}" font-size="11" fill="#111">{lab}</text>')
    parts.append('</svg>')
    return ''.join(parts)


def nl_interval(xmin, xmax, segments, s=40, pad=26):
    """數線＋粗線標出解區間。segments: [(a, b, a_closed, b_closed)]，用 None 表示 ±∞。"""
    W = (xmax - xmin) * s + 2 * pad
    H = 58
    oy = 32
    ox = pad - xmin * s

    def X(v):
        return ox + s * v
    parts = [f'<svg viewBox="0 0 {W} {H}" data-w="{W}" data-h="{H}" '
             f'xmlns="http://www.w3.org/2000/svg" font-family="Microsoft JhengHei, Arial, sans-serif">']
    parts.append(f'<line x1="6" y1="{oy}" x2="{W-6}" y2="{oy}" stroke="#333" stroke-width="1.4"/>')
    parts.append(f'<polygon points="{W-6},{oy} {W-14},{oy-4} {W-14},{oy+4}" fill="#333"/>')
    parts.append(f'<polygon points="6,{oy} 14,{oy-4} 14,{oy+4}" fill="#333"/>')
    for v in range(xmin, xmax + 1):
        px = X(v)
        parts.append(f'<line x1="{px}" y1="{oy-4}" x2="{px}" y2="{oy+4}" stroke="#333" stroke-width="1.1"/>')
        parts.append(f'<text x="{px-3}" y="{oy+18}" font-size="11" fill="#555">{v}</text>')
    for seg in segments:
        a, b, ac, bc = seg
        xa = 10 if a is None else X(a)
        xb = W - 10 if b is None else X(b)
        parts.append(f'<line x1="{xa}" y1="{oy}" x2="{xb}" y2="{oy}" stroke="#111" stroke-width="3.4"/>')
        if a is not None:
            parts.append(f'<circle cx="{xa}" cy="{oy}" r="4.5" fill="{"#111" if ac else "#fff"}" stroke="#111" stroke-width="1.6"/>')
        if b is not None:
            parts.append(f'<circle cx="{xb}" cy="{oy}" r="4.5" fill="{"#111" if bc else "#fff"}" stroke="#111" stroke-width="1.6"/>')
    parts.append('</svg>')
    return ''.join(parts)
