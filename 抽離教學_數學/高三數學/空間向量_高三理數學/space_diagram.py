# -*- coding: utf-8 -*-
r"""space_diagram.py —— 空間向量／立體幾何示意圖產生器（斜二測畫法）

自建工具：jh-math-geometry 的 solid_3d／coordinate_plane 係兩種獨立圖形類型，
冇「立體圖形疊加空間直角坐標軸」呢種本章教材的招牌畫法，所以自己起呢個小工具，
做法比照之前 2D 解析幾何用嘅 grid_svg.py 套路（自建 SVG → Chrome headless 截圖 PNG）。

投影規則：z軸向上、y軸向右，x軸（深度軸）以45°向左下方畫，並乘 X_FORESHORTEN
縮短，模擬「軸伸向讀者」的透視感——呢個係人教版課本畫空間直角坐標系嘅標準畫法。

隱藏線規則：對於一個由 origin3d 沿 +x(a)/+y(b)/+z(c) 張開嘅長方體/正方體，
遠端頂點（同時用晒 +x+y+z 三個方向嗰隻角，即示例入面嘅 B1）相連嘅 3 條棱係
「睇唔到」嗰面，用虛線畫；其餘 9 條棱實線——呢個規則由面法向量可見性推導
（兩個相鄰面都背向觀察者，條邊先會被擋，得返呢 3 條符合），唔係憑感覺畫。

用法（例）：
    from space_diagram import Scene, render_png
    sc = Scene()
    sc.axes()
    verts = sc.box(2, 2, 2)                      # 正方體，D 在原點
    sc.save(r'.\_assets\demo.svg')
    render_png(r'.\_assets\demo.svg', r'.\_assets\demo.png', sc.width, sc.height)
"""
import math
import os
import subprocess

SCALE = 60                     # 每單位長度的像素數（y、z 軸方向的「真實」比例）
X_FORESHORTEN = 0.55           # x 軸（深度軸）的縮短比例
X_ANGLE = math.radians(30)     # x 軸畫喺左下 30°（刻意唔用45°：cos45°=sin45°會令部分
                                # 圖形嘅體對角線投影後啱啱好穿過另一頂點，造成誤導，
                                # 已用代數驗證過 kx≠ky 先唔會撞——見下面 project() 附註）

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def find_chrome():
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    raise RuntimeError("搵唔到 Chrome，請確認已安裝")


def render_png(svg_path, png_path, w, h, scale=3):
    """把 SVG 包成一個貼身 HTML 頁，用 headless Chrome 截圖做 PNG（image_para 只食 PNG）。"""
    with open(svg_path, 'r', encoding='utf-8') as f:
        svg = f.read()
    html_path = svg_path + '.html'
    html = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>'
            f'html,body{{margin:0;padding:0;overflow:hidden;background:#fff;}}'
            f'.wrap{{width:{w}px;height:{h}px;}}</style></head>'
            f'<body><div class="wrap">{svg}</div></body></html>')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    chrome = find_chrome()
    uri = 'file:///' + os.path.abspath(html_path).replace('\\', '/')
    cmd = [chrome, '--headless', '--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage',
           '--hide-scrollbars', f'--force-device-scale-factor={scale}',
           f'--window-size={w},{h}', f'--screenshot={os.path.abspath(png_path)}', uri]
    subprocess.run(cmd, capture_output=True)
    os.remove(html_path)
    if not os.path.exists(png_path) or os.path.getsize(png_path) < 500:
        raise RuntimeError(f'截圖失敗：{svg_path}')
    return png_path


def project(x, y, z, ox, oy):
    """3D 座標 -> 2D 螢幕像素座標（SVG，y 向下為正）。ox,oy = 3D 原點喺畫面上的像素位置。"""
    sx = ox + y * SCALE - x * SCALE * X_FORESHORTEN * math.cos(X_ANGLE)
    sy = oy - z * SCALE + x * SCALE * X_FORESHORTEN * math.sin(X_ANGLE)
    return sx, sy


def midpoint(p1, p2):
    return tuple((a + b) / 2 for a, b in zip(p1, p2))


def lerp3(p1, p2, t):
    """p1 + t*(p2-p1)，t=0→p1，t=1→p2，可以用嚟攞任一條棱上嘅分點。"""
    return tuple(a + t * (b - a) for a, b in zip(p1, p2))


class Scene:
    def __init__(self, width=420, height=380, origin=(120, 300)):
        self.width, self.height = width, height
        self.ox, self.oy = origin
        self.els = []  # SVG 元素，按加入順序疊上去（後加者蓋前者）

    def p(self, x, y, z):
        return project(x, y, z, self.ox, self.oy)

    def line(self, p1, p2, dashed=False, width=1.6, color='#000'):
        x1, y1 = p1
        x2, y2 = p2
        dash = ' stroke-dasharray="5,4"' if dashed else ''
        self.els.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                         f'stroke="{color}" stroke-width="{width}"{dash}/>')

    def dot(self, pt, r=2.6, color='#000'):
        x, y = pt
        self.els.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}"/>')

    def label(self, pt, text, dx=6, dy=-6, size=17, italic=True, anchor='start', color='#000'):
        x, y = pt
        style = 'font-style:italic;' if italic else ''
        self.els.append(f'<text x="{x + dx:.1f}" y="{y + dy:.1f}" '
                         f'font-family="Times New Roman, STIXGeneral, serif" font-size="{size}" '
                         f'fill="{color}" style="{style}" text-anchor="{anchor}">{text}</text>')

    def arrow(self, p1, p2, color='#000', width=1.8):
        """帶箭頭的線段（用嚟畫坐標軸或向量）。"""
        x1, y1 = p1
        x2, y2 = p2
        ang = math.atan2(y2 - y1, x2 - x1)
        al, aa = 9, math.radians(20)
        lx1, ly1 = x2 - al * math.cos(ang - aa), y2 - al * math.sin(ang - aa)
        lx2, ly2 = x2 - al * math.cos(ang + aa), y2 - al * math.sin(ang + aa)
        self.els.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                         f'stroke="{color}" stroke-width="{width}"/>')
        self.els.append(f'<polygon points="{x2:.1f},{y2:.1f} {lx1:.1f},{ly1:.1f} {lx2:.1f},{ly2:.1f}" fill="{color}"/>')

    def vec3(self, p1_3d, p2_3d, color='#000', width=1.8):
        """3D 起訖點的向量箭頭（自動投影）。"""
        self.arrow(self.p(*p1_3d), self.p(*p2_3d), color=color, width=width)

    def axes(self, xlen=1.7, ylen=3.6, zlen=3.6, labels=('x', 'y', 'z'), origin_label='O'):
        o = self.p(0, 0, 0)
        self.arrow(o, self.p(xlen, 0, 0))
        self.arrow(o, self.p(0, ylen, 0))
        self.arrow(o, self.p(0, 0, zlen))
        self.label(self.p(xlen, 0, 0), labels[0], dx=-4, dy=18, italic=True)
        self.label(self.p(0, ylen, 0), labels[1], dx=8, dy=4, italic=True)
        self.label(self.p(0, 0, zlen), labels[2], dx=-4, dy=-8, italic=True)
        if origin_label:
            self.label(o, origin_label, dx=-16, dy=14, italic=True)

    def box(self, a, b, c, labels=('D', 'A', 'B', 'C', 'D₁', 'A₁', 'B₁', 'C₁'),
            origin3d=(0, 0, 0), show_dots=True, label_offsets=None):
        """畫一個長方體/正方體：由 origin3d 沿 +x(長a)/+y(長b)/+z(高c) 張開。
        頂點次序 D(原點)-A(+x)-B(+x+y)-C(+y) 為底面，...1 為對應頂面，
        即 DABC-D1A1B1C1 順序繞行成正方形，符合課本 ABCD-A1B1C1D1 標法。
        回傳 8 頂點的 3D 座標 dict（key 用 D/A/B/C/D1/A1/B1/C1，同 labels 一一對應），
        方便呼叫者之後再用 self.p(*verts['A']) 或 midpoint()/lerp3() 加畫額外的點/向量。"""
        ox0, oy0, oz0 = origin3d
        verts = {
            'D': (ox0, oy0, oz0), 'A': (ox0 + a, oy0, oz0),
            'B': (ox0 + a, oy0 + b, oz0), 'C': (ox0, oy0 + b, oz0),
            'D1': (ox0, oy0, oz0 + c), 'A1': (ox0 + a, oy0, oz0 + c),
            'B1': (ox0 + a, oy0 + b, oz0 + c), 'C1': (ox0, oy0 + b, oz0 + c),
        }
        pts2d = {k: self.p(*v) for k, v in verts.items()}
        hidden = {('C1', 'B1'), ('A1', 'B1'), ('B', 'B1')}  # 遠端頂點 B1 相連的 3 條棱（見檔頭說明）
        edges = [('D', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'D'),
                 ('D1', 'A1'), ('A1', 'B1'), ('B1', 'C1'), ('C1', 'D1'),
                 ('D', 'D1'), ('A', 'A1'), ('B', 'B1'), ('C', 'C1')]
        for u, v in edges:
            is_hidden = (u, v) in hidden or (v, u) in hidden
            self.line(pts2d[u], pts2d[v], dashed=is_hidden)
        if show_dots:
            for k in pts2d:
                self.dot(pts2d[k])
        name_map = dict(zip(['D', 'A', 'B', 'C', 'D1', 'A1', 'B1', 'C1'], labels))
        default_offsets = {'D': (-22, 20), 'A': (8, 22), 'B': (10, 10), 'C': (-16, 6),
                            'D1': (-14, -14), 'A1': (-26, 16), 'B1': (10, 2), 'C1': (-16, -8)}
        offsets = label_offsets or default_offsets
        for k, pt in pts2d.items():
            dx, dy = offsets.get(k, (6, -6))
            self.label(pt, name_map[k], dx=dx, dy=dy)
        return verts

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
                f'viewBox="0 0 {self.width} {self.height}">'
                f'<rect width="{self.width}" height="{self.height}" fill="white"/>'
                + ''.join(self.els) + '</svg>')

    def save(self, path):
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.svg())
        return path
