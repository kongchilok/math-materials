# -*- coding: utf-8 -*-
r"""複數單元（人教B必修四 第十章 10.1–10.2）共用產檔層。

一份內容（block list）→ 同時渲染 docx（原生 OMML，教師可編輯）與 HTML（MathJax，
→ PDF 正式列印版）。兩版同源，house-style「docx 版與 HTML 版的同名元件外觀必須一致」
靠這個保證，不用每課各寫兩份。

數學一律用 omml_core 的 `{}` 標記寫；HTML 版由 tex() 轉成 LaTeX。
⚠ 虛數單位 i：課本註①規定 i 一律印正體。標記裡照常寫 i，兩個渲染器各自轉：
   docx → fn(i)（OMML 正體 run）；HTML → \mathrm{i}。
   因此 {} 內**不要**寫 lim／pi／sin 這類含小寫 i 的關鍵字（本單元用不到）。
⚠ HTML 數學式內不准出現裸 < >：tex() 一律轉成 \lt \gt。
"""
import os
import re
import sys
import hashlib
import html as _html
import subprocess
import shutil
import time

SKILL = r'C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator'
sys.path.insert(0, os.path.join(SKILL, 'scripts'))
import omml_docx as D            # noqa: E402
import design_svg as ds          # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, '_assets')
SUBJECT = '高三數學'
FOOTER = '高三數學．複數單元'


# ====================================================================== 標記前處理
def _math_spans(text):
    """切出最外層 {…}，回傳 [(is_math, str), ...]。"""
    out, buf, i, n = [], [], 0, len(text)
    while i < n:
        c = text[i]
        if c == '{':
            depth, j = 0, i
            while j < n:
                if text[j] == '{':
                    depth += 1
                elif text[j] == '}':
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j >= n:
                raise ValueError(f'{{ 不成對：{text!r}')
            if buf:
                out.append((False, ''.join(buf)))
                buf = []
            out.append((True, text[i + 1:j]))
            i = j + 1
        else:
            buf.append(c)
            i += 1
    if buf:
        out.append((False, ''.join(buf)))
    return out


_FN_RE = re.compile(r'fn\([^()]*\)')


def _upright_i(m):
    """數學段內的小寫 i → fn(i)（fn(...) 內容先保護起來）。"""
    keep = []

    def stash(mo):
        keep.append(mo.group(0))
        return f'\x00{len(keep) - 1}\x00'
    m = _FN_RE.sub(stash, m)
    m = m.replace('i', 'fn(i)')
    return re.sub('\x00(\\d+)\x00', lambda mo: keep[int(mo.group(1))], m)


def dx(text):
    """docx 用：把字串內每個 {} 數學段的 i 改成正體。"""
    if not isinstance(text, str):
        return text
    return ''.join('{' + _upright_i(s) + '}' if is_m else s
                   for is_m, s in _math_spans(text))


# ====================================================================== {} 標記 → LaTeX
_PRE = [('->', '→'), ('<=', '≤'), ('>=', '≥'), ('!=', '≠'), ('+-', '±'), ('*', '×')]
_CH = {'→': r'\to ', '≤': r'\le ', '≥': r'\ge ', '≠': r'\ne ', '±': r'\pm ',
       '×': r'\times ', '−': '-', '<': r'\lt ', '>': r'\gt ', 'π': r'\pi ',
       'Δ': r'\Delta ', 'θ': r'\theta ', '∈': r'\in ', '∴': r'\therefore ',
       '·': r'\cdot ', '…': r'\cdots ', '⇔': r'\Leftrightarrow ', '%': r'\%',
       '°': r'^{\circ}', '#': r'\#', '&': r'\&', '~': r'\sim ', '∠': r'\angle ',
       '△': r'\triangle ', '⊆': r'\subseteq ', '⊂': r'\subset '}


def _close(s, i, o, c):
    d = 0
    for j in range(i, len(s)):
        if s[j] == o:
            d += 1
        elif s[j] == c:
            d -= 1
            if d == 0:
                return j
    raise ValueError(f'括號不成對：{s!r}')


def _split(s, sep):
    d, parts, cur = 0, [], []
    for c in s:
        if c in '([{':
            d += 1
        elif c in ')]}':
            d -= 1
        if c == sep and d == 0:
            parts.append(''.join(cur))
            cur = []
        else:
            cur.append(c)
    parts.append(''.join(cur))
    return parts


def _is_cjk(c):
    return ord(c) > 0x2E80 and c not in _CH


def _run_tex(run):
    out, cjk = [], []
    for c in run:
        if _is_cjk(c):
            cjk.append(c)
            continue
        if cjk:
            out.append(r'\text{' + ''.join(cjk) + '}')
            cjk = []
        out.append(_CH.get(c, c))
    if cjk:
        out.append(r'\text{' + ''.join(cjk) + '}')
    return ''.join(out)


def _t_atom(s, i):
    for kw, fmt in (('frac(', None), ('sqrt[', None), ('sqrt(', r'\sqrt{%s}'),
                    ('vec(', r'\overrightarrow{%s}'), ('bar(', r'\overline{%s}')):
        if s.startswith(kw, i):
            if kw == 'frac(':
                j = _close(s, i + 4, '(', ')')
                a, b = _split(s[i + 5:j], ',')
                return r'\dfrac{%s}{%s}' % (_t_seq(a), _t_seq(b)), j + 1
            if kw == 'sqrt[':
                j = _close(s, i + 4, '[', ']')
                k = _close(s, j + 1, '(', ')')
                return r'\sqrt[%s]{%s}' % (_t_seq(s[i + 5:j]), _t_seq(s[j + 2:k])), k + 1
            j = _close(s, i + len(kw) - 1, '(', ')')
            return fmt % _t_seq(s[i + len(kw):j]), j + 1
    if s.startswith('cases(', i):
        j = _close(s, i + 5, '(', ')')
        rows = [' & '.join(_t_seq(c) for c in _split(r, ','))
                for r in _split(s[i + 6:j], ';')]
        return r'\begin{cases}' + r' \\ '.join(rows) + r'\end{cases}', j + 1
    if s.startswith('fn(', i):
        j = _close(s, i + 2, '(', ')')
        return r'\mathrm{%s}' % s[i + 3:j].strip(), j + 1
    c = s[i]
    if c == '|':
        j = s.find('|', i + 1)
        inner = _t_seq(s[i + 1:j])
        if r'\dfrac' in inner or r'\sqrt' in inner:   # 有分數／根號才放大
            return r'\left|%s\right|' % inner, j + 1
        return r'\lvert %s\rvert ' % inner, j + 1
    if c == '(':
        j = _close(s, i, '(', ')')
        inner = _t_seq(s[i + 1:j])
        if 'frac' in inner or r'\sqrt' in inner:     # 有分數／根號才放大括號
            return r'\left(%s\right)' % inner, j + 1
        return '(%s)' % inner, j + 1
    m = re.compile(r'[0-9]+(?:\.[0-9]+)?').match(s, i)
    if m:
        return m.group(0), m.end()
    if c.isascii() and c.isalpha():
        return (r'\mathrm{i}' if c == 'i' else c), i + 1
    j = i
    while j < len(s):
        cj = s[j]
        if cj in '^_/|(){},' or (cj.isascii() and cj.isalnum()):
            break
        j += 1
    if j == i:
        return _run_tex(s[i]), i + 1
    return _run_tex(s[i:j]), j


def _t_arg(s, i):
    if s[i] == '{':
        j = _close(s, i, '{', '}')
        return _t_seq(s[i + 1:j]), j + 1
    return _t_atom(s, i)


def _t_post(s, i, slash=True):
    a, i = _t_atom(s, i)
    while i < len(s):
        c = s[i]
        if c == '^':
            arg, i = _t_arg(s, i + 1)
            a = '{%s}^{%s}' % (a, arg)
        elif c == '_':
            arg, i = _t_arg(s, i + 1)
            a = '{%s}_{%s}' % (a, arg)
        elif c == '/' and slash:
            den, i = _t_post(s, i + 1, slash=False)
            a = r'\frac{%s}{%s}' % (a, den)
        else:
            break
    return a, i


def _t_seq(s):
    out, i = [], 0
    while i < len(s):
        a, i = _t_post(s, i)
        out.append(a)
    return ''.join(out)


def tex(m):
    for a, b in _PRE:
        m = m.replace(a, b)
    m = m.replace('-', '−')
    return _t_seq(m)


def H(text):
    """混排字串（文字＋{}數學）→ HTML 片段。"""
    if text is None:
        return ''
    out = []
    for is_m, s in _math_spans(text):
        if is_m:
            out.append(r'\(' + _html.escape(tex(s), quote=False) + r'\)')
        else:
            out.append(_html.escape(s, quote=False).replace('\n', '<br>'))
    return ''.join(out)


# ====================================================================== 複平面圖（黑白）
_MK = [0]


def cplane(xr=(-4, 4), yr=(-4, 4), width=300, points=(), vecs=(), segs=(),
           circles=(), labels=(), polys=(), grid=True, ticks=True, blank=False):
    """複平面座標圖（黑白，側欄原生 300px）。
    points : (x, y, 文字, 方位)  方位 ∈ n/s/e/w/ne/nw/se/sw
    vecs   : (x1, y1, x2, y2[, 'dash'])  帶箭頭的向量
    segs   : (x1, y1, x2, y2)  虛線輔助線（不帶箭頭）
    circles: (cx, cy, r, 'solid'|'dash')
    labels : (x, y, 文字, 方位)  不畫點的標籤
    polys  : ([(x,y),...], 'dash'|'solid')  多邊形外框（不填色）
    blank  : True → 只有格線與軸，給學生描點用，外加虛線框表示作答區
    """
    _MK[0] += 1
    mid = f'ah{_MK[0]}'
    pad = 24
    u = (width - 2 * pad) / (xr[1] - xr[0])
    height = int(round(u * (yr[1] - yr[0]) + 2 * pad))

    def X(x):
        return pad + (x - xr[0]) * u

    def Y(y):
        return pad + (yr[1] - y) * u

    b = []
    b.append(f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" '
             'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
             '<path d="M0,0 L10,5 L0,10 z" fill="#000"/></marker></defs>')
    b.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="#fff"/>')
    if grid:
        for k in range(xr[0], xr[1] + 1):
            b.append(f'<line x1="{X(k):.1f}" y1="{Y(yr[0]):.1f}" x2="{X(k):.1f}" '
                     f'y2="{Y(yr[1]):.1f}" stroke="#c8c8c8" stroke-width="0.8"/>')
        for k in range(yr[0], yr[1] + 1):
            b.append(f'<line x1="{X(xr[0]):.1f}" y1="{Y(k):.1f}" x2="{X(xr[1]):.1f}" '
                     f'y2="{Y(k):.1f}" stroke="#c8c8c8" stroke-width="0.8"/>')
    # 軸
    b.append(f'<line x1="{X(xr[0]) - 6:.1f}" y1="{Y(0):.1f}" x2="{X(xr[1]) + 14:.1f}" '
             f'y2="{Y(0):.1f}" stroke="#000" stroke-width="1.4" marker-end="url(#{mid})"/>')
    b.append(f'<line x1="{X(0):.1f}" y1="{Y(yr[0]) + 6:.1f}" x2="{X(0):.1f}" '
             f'y2="{Y(yr[1]) - 14:.1f}" stroke="#000" stroke-width="1.4" marker-end="url(#{mid})"/>')
    font = 'font-family="Microsoft JhengHei, Calibri, sans-serif"'

    def txt(x, y, s, size=12, anchor='middle', bold=False):
        w = ' font-weight="700"' if bold else ''
        s = _html.escape(s)
        return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" {font}{w} '
                f'text-anchor="{anchor}" dominant-baseline="middle" '
                f'stroke="#fff" stroke-width="3.2" paint-order="stroke" fill="#000">{s}</text>')

    b.append(txt(X(xr[1]) + 13, Y(0) - 11, '實軸', 11, 'end'))
    b.append(txt(X(0) + 6, Y(yr[1]) - 10, '虛軸', 11, 'start'))
    b.append(txt(X(0) - 7, Y(0) + 10, 'O', 11))
    if ticks:
        for k in range(xr[0], xr[1] + 1):
            if k:
                b.append(txt(X(k), Y(0) + 11, str(k).replace('-', '−'), 10))
        for k in range(yr[0], yr[1] + 1):
            if k:
                b.append(txt(X(0) - 5, Y(k), str(k).replace('-', '−'), 10, 'end'))
    for c in circles:
        cx, cy, r = c[:3]
        dash = ' stroke-dasharray="5 4"' if (len(c) > 3 and c[3] == 'dash') else ''
        b.append(f'<circle cx="{X(cx):.1f}" cy="{Y(cy):.1f}" r="{r * u:.1f}" fill="none" '
                 f'stroke="#000" stroke-width="1.6"{dash}/>')
    for pts, style in polys:
        d = ' '.join(f'{X(x):.1f},{Y(y):.1f}' for x, y in pts)
        dash = ' stroke-dasharray="5 4"' if style == 'dash' else ''
        b.append(f'<polygon points="{d}" fill="none" stroke="#000" stroke-width="1.2"{dash}/>')
    for s in segs:
        b.append(f'<line x1="{X(s[0]):.1f}" y1="{Y(s[1]):.1f}" x2="{X(s[2]):.1f}" '
                 f'y2="{Y(s[3]):.1f}" stroke="#000" stroke-width="1.2" stroke-dasharray="5 4"/>')
    for v in vecs:
        dash = ' stroke-dasharray="6 4"' if (len(v) > 4 and v[4] == 'dash') else ''
        # 箭頭尖收短 1.5px，免得蓋住終點的圓點
        b.append(f'<line x1="{X(v[0]):.1f}" y1="{Y(v[1]):.1f}" x2="{X(v[2]):.1f}" '
                 f'y2="{Y(v[3]):.1f}" stroke="#000" stroke-width="2"{dash} '
                 f'marker-end="url(#{mid})"/>')
    off = {'n': (0, -13, 'middle'), 's': (0, 14, 'middle'), 'e': (8, 0, 'start'),
           'w': (-8, 0, 'end'), 'ne': (6, -11, 'start'), 'nw': (-6, -11, 'end'),
           'se': (6, 12, 'start'), 'sw': (-6, 12, 'end')}
    for p in points:
        x, y, s = p[:3]
        a = p[3] if len(p) > 3 else 'ne'
        b.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="3.6" fill="#000" '
                 'stroke="#fff" stroke-width="1"/>')
        dx_, dy_, an = off[a]
        if s:
            b.append(txt(X(x) + dx_, Y(y) + dy_, s, 12, an, bold=True))
    for p in labels:
        x, y, s = p[:3]
        a = p[3] if len(p) > 3 else 'ne'
        dx_, dy_, an = off[a]
        b.append(txt(X(x) + dx_, Y(y) + dy_, s, 12, an))
    if blank:
        b.append(f'<rect x="2" y="2" width="{width - 4}" height="{height - 4}" fill="none" '
                 'stroke="#000" stroke-width="1" stroke-dasharray="6 4"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}">' + ''.join(b) + '</svg>')


class Fig:
    """一張圖：HTML 直接內嵌 SVG；docx 轉 PNG（_assets\\，SVG 沒變就沿用舊 PNG）。"""
    def __init__(self, name, svg, width_cm=7.4, caption=None):
        self.name, self.svg, self.width_cm, self.caption = name, svg, width_cm, caption

    def png(self):
        os.makedirs(ASSETS, exist_ok=True)
        p = os.path.join(ASSETS, self.name + '.png')
        h = hashlib.md5(self.svg.encode('utf-8')).hexdigest()
        stamp = p + '.md5'
        if not (os.path.exists(p) and os.path.exists(stamp)
                and open(stamp, encoding='ascii').read() == h):
            ds.svg_to_png(self.svg, p)
            with open(stamp, 'w', encoding='ascii') as f:
                f.write(h)
        return p

    def ref(self):
        return D.image_para(self.png(), width_cm=self.width_cm, caption=self.caption)

    def html(self):
        cap = f'<div class="cap">{H(self.caption)}</div>' if self.caption else ''
        return f'<div class="fig">{self.svg}{cap}</div>'


# ====================================================================== blocks
# 每個 block 是 (kind, dict)。內容字串一律是 {} 標記混排文字。
def h(t, brk=False):
    return ('h', dict(t=t, brk=brk))


def p(t, bold=False):
    return ('p', dict(t=t, bold=bold))


def shade(t):
    return ('shade', dict(t=t))


def defbox(lines):
    return ('def', dict(lines=lines))


def table(headers, rows, pct=None, long=False):
    """通用表格。cell 可以是字串或字串 list（多行）。"""
    return ('tbl', dict(headers=headers, rows=rows, pct=pct, long=long))


def worked(lead, rows, why_pct=0.36, col_frac=None, fig=None):
    """範例表。fig＝這個範例配的圖：放在引言之後、算式表之前，
    HTML 版三者包進同一個 break-inside:avoid，免得圖和算式被分頁拆開。"""
    return ('wk', dict(lead=lead, rows=rows, why_pct=why_pct, col_frac=col_frac, fig=fig))


eq, orr, span, ans = D.eq_row, D.or_row, D.span_row, D.answer_row


def dual(pairs, headers=('圖上看到什麼', '算式上寫什麼')):
    return ('dual', dict(pairs=pairs, headers=headers))


def fig(f):
    return ('fig', dict(f=f))


def frayer(term, q1, q2, q3, q4, n_blank=2):
    """D13 弗雷爾四象限。q1 定義／q2 特徵／q3 例／q4 非例；
    某格傳 None 就留空白作答線（n_blank 行）。"""
    return ('frayer', dict(term=term, q=[q1, q2, q3, q4], n=n_blank))


def step(title, trigger, steps, compact=False):
    return ('step', dict(title=title, trigger=trigger, steps=steps, compact=compact))


def refcard(title, trigger, lines):
    return ('ref', dict(title=title, trigger=trigger, lines=lines))


def q(no, stem, hint=None, f=None, n=4, hint_title='提示'):
    """一題。stem：字串或字串 list。有 hint 或圖 → 題目在左、圖與提示在右；
    兩者都沒有 → 整頁寬題框。"""
    if isinstance(stem, str):
        stem = [stem]
    return ('q', dict(no=no, stem=stem, hint=hint, f=f, n=n, ht=hint_title))


def selfcheck(items, title='做完先自己核對一次'):
    return ('sc', dict(items=items, title=title))


def checkpoint():
    return ('cp', {})


def lines_(n):
    return ('lines', dict(n=n))


def answers(groups, title='參考答案（教師用）'):
    return ('ans', dict(groups=groups, title=title))


def teacher(main, aux, reason, density, fading, flows, codes, goal, extra=()):
    return ('tn', dict(main=main, aux=aux, reason=reason, density=density,
                       fading=fading, flows=flows, codes=codes, goal=goal, extra=extra))


# ====================================================================== docx 渲染
def _dpara(t, bold=False, **kw):
    return D.para(dx(t), bold=bold, **kw)


def _dcell(x, media):
    if isinstance(x, Fig):
        return [D.expand_image(x.ref(), media)]
    if x is None:
        return [D.blank()]
    if isinstance(x, str):
        return [_dpara(x, spacing=False)]
    out = []
    for y in x:
        out += _dcell(y, media)
    return out


def _drow(r):
    r = dict(r)
    for k in ('lhs', 'rhs', 'lhs2', 'rhs2', 'text', 'rel'):
        if r.get(k):
            r[k] = dx(r[k])
    if isinstance(r.get('why'), str):
        r['why'] = dx(r['why'])
    return r


def render_docx(blocks, unit, doc_type, out_path):
    media = D.MediaRegistry()
    W = D._PAGE_CONTENT_WIDTH
    P = [D.masthead(SUBJECT, unit, doc_type), D.student_info_row()]
    for kind, a in blocks:
        if kind == 'h':
            P.append(D.heading(a['t'], page_break_before=a['brk']))
        elif kind == 'p':
            P.append(_dpara(a['t'], bold=a['bold']))
        elif kind == 'shade':
            P.append(D.shaded_box(dx(a['t'])))
        elif kind == 'def':
            P.append(D.problem_box([_dpara(t) for t in a['lines']]))
        elif kind == 'tbl':
            n = len(a['headers'])
            pct = a['pct'] or [1 / n] * n
            ws = [int(W * x) for x in pct[:-1]]
            ws.append(W - sum(ws))
            rows = [{'hdr': True, 'cells': [{'p': [_dpara(x, bold=True, sz=22, spacing=False)],
                                             'shd': D.GREY_FILL} for x in a['headers']]}]
            for r in a['rows']:
                rows.append({'cells': [{'p': _dcell(c, media), 'va': 'center'} for c in r]})
            P.append(D._tbl(rows, ws))
        elif kind == 'wk':
            P.append(_dpara(a['lead'], bold=True, keep_next=True))
            if a['fig']:
                P.append(a['fig'].ref())
            P.append(D.worked_example_table([_drow(r) for r in a['rows']],
                                            why_pct=a['why_pct'], col_frac=a['col_frac']))
        elif kind == 'dual':
            pairs = [(_dcell(l, media), _dcell(r, media)) for l, r in a['pairs']]
            P.append(D.dual_track_table(pairs, media=media, headers=a['headers']))
        elif kind == 'fig':
            P.append(a['f'].ref())
        elif kind == 'frayer':
            labels = ['① 定義（用自己的話）', '② 特徵（必要條件）', '③ 例（是）',
                      '④ 非例（不是——差在哪個特徵）']

            def fc(i):
                body = a['q'][i]
                inner = [_dpara(labels[i], bold=True, sz=22, spacing=False, shd=D.GREY_FILL)]
                if body is None:
                    inner += D.write_lines(a['n'])
                else:
                    inner += [_dpara(t, spacing=False) for t in body]
                return {'p': inner}
            half = W // 2
            rows = [{'cells': [{'p': [_dpara(a['term'], bold=True, sz=D.HEADING_SZ, jc='center')],
                                'span': 2, 'shd': D.GREY_FILL}]},
                    {'cells': [fc(0), fc(1)]}, {'cells': [fc(2), fc(3)]}]
            P.append(D._tbl(rows, [half, W - half]))
        elif kind == 'step':
            steps = [(dx(s[0]), dx(s[1])) if isinstance(s, tuple) else dx(s) for s in a['steps']]
            P.append(D.step_card(a['title'], steps, trigger=dx(a['trigger']), compact=a['compact']))
        elif kind == 'ref':
            inner = [D.para(f'▍{a["title"]}', bold=True, sz=D.HEADING_SZ),
                     _dpara(f'什麼時候翻我：{a["trigger"]}', sz=21)]
            inner += [_dpara(t) for t in a['lines']]
            P.append(D._tbl([[{'p': inner}]], [W]))
        elif kind == 'q':
            main = [_dpara(f'{a["no"]}．' + a['stem'][0])] + [_dpara(t) for t in a['stem'][1:]]
            main += D.write_lines(a['n'])
            if a['hint'] or a['f']:
                side = []
                if a['f']:
                    side.append(a['f'].ref())
                if a['hint']:
                    side += D.hint_lines([dx(t) for t in a['hint']], title=a['ht'])
                P.append(D.aside_layout(main, side, media=media, boxed=True))
            else:
                P.append(D.problem_box(main))
        elif kind == 'sc':
            P.append(D.selfcheck_list([dx(t) for t in a['items']], title=a['title']))
        elif kind == 'cp':
            P.append(D.checkpoint_rule())
        elif kind == 'lines':
            P.extend(D.write_lines(a['n']))
        elif kind == 'ans':
            P.append(D.heading(a['title'], page_break_before=True))
            for g in a['groups']:
                P.append(D.problem_box([_dpara(t) for t in g]))
        elif kind == 'tn':
            extra = [('本單元對應的正規教學目標', a['goal'])] + list(a['extra'])
            P.extend(D.teacher_notes(a['main'], a['aux'], reason=a['reason'],
                                     density=a['density'], fading=a['fading'],
                                     flows=a['flows'], iep_codes=a['codes'], extra=extra))
        else:
            raise ValueError(kind)
    return D.build_docx(P, out_path, footer_text=FOOTER, media=media)


# ====================================================================== HTML 渲染
with open(os.path.join(SKILL, 'assets', 'worksheet-template.html'), encoding='utf-8') as _f:
    _TPL = _f.read()
_EXTRA_CSS = r'''
<style>
  /* 保險：MathJax 的公式本身也是 <svg>，任何後代選擇器都會誤中（house-style 2026-08-08） */
  mjx-container > svg { width:auto; height:auto; max-width:none; display:inline; margin:0; }
  .aside-side > svg { width:100%; height:auto; }
  .dual-track td > svg { max-width:100%; height:auto; }
  .frayer td { width:50%; }
  .frayer .flab { background:#f0f0f0; margin:-6px -9px 6px; padding:3px 9px; font-weight:700; font-size:11pt; }
  .frayer .term { text-align:center; font-size:14pt; font-weight:700; background:#f0f0f0; }
  .def-line { margin:2px 0; }
  .teacher-notes td:first-child { width:30%; white-space:nowrap; }
</style>
'''
_HEAD = _TPL[:_TPL.index('</head>')] + _EXTRA_CSS + '</head>'


def _hlines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + '</div>'


def _hcell(x):
    if isinstance(x, Fig):
        return x.svg
    if x is None:
        return ''
    if isinstance(x, str):
        return f'<div>{H(x)}</div>'
    return ''.join(_hcell(y) for y in x)


def _hrow(r):
    k = r['k']
    why = r.get('why')
    why = H(why) if isinstance(why, str) else ''
    if k == 'span':
        cls = 'ecs ans' if r.get('bold') else 'ecs'
        return f'<tr><td class="{cls}" colspan="7">{H(r["text"])}</td><td class="why">{why}</td></tr>'
    rel = r.get('rel', '{=}')
    rel = H(rel if rel.startswith('{') else '{' + rel + '}')

    def m(x):
        return H(x) if x else ''
    if k == 'or':
        return (f'<tr><td class="ec1">{m(r["lhs"])}</td><td class="ec2">{rel}</td>'
                f'<td class="ec3">{m(r["rhs"])}</td><td class="ec4">或</td>'
                f'<td class="ec5">{m(r["lhs2"])}</td><td class="ec6">{rel}</td>'
                f'<td class="ec7">{m(r["rhs2"])}</td><td class="why">{why}</td></tr>')
    return (f'<tr><td class="ec1">{m(r["lhs"])}</td><td class="ec2">{rel}</td>'
            f'<td class="ec3" colspan="5">{m(r["rhs"])}</td><td class="why">{why}</td></tr>')


def render_html(blocks, unit, doc_type, out_path):
    B = ['<div class="masthead">'
         f'<span>科目：{SUBJECT}</span><span>單元：{_html.escape(unit)}</span>'
         f'<span>類型：{doc_type}</span></div>',
         '<div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>'
         '學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>']
    for kind, a in blocks:
        if kind == 'h':
            cls = 'section-h page-break' if a['brk'] else 'section-h'
            t = _html.escape(a['t']).replace('★☆☆', '<span class="stars">★☆☆</span>') \
                .replace('★★☆', '<span class="stars">★★☆</span>') \
                .replace('★★★', '<span class="stars">★★★</span>')
            B.append(f'<div class="{cls}" style="break-after:avoid;page-break-after:avoid">{t}</div>')
        elif kind == 'p':
            t = H(a['t'])
            B.append(f'<div><b>{t}</b></div>' if a['bold'] else f'<div>{t}</div>')
        elif kind == 'shade':
            B.append(f'<div class="hint-card">{H(a["t"])}</div>')
        elif kind == 'def':
            B.append('<div class="problem">' + ''.join(
                f'<div class="def-line">{H(t)}</div>' for t in a['lines']) + '</div>')
        elif kind == 'tbl':
            n = len(a['headers'])
            pct = a['pct'] or [1 / n] * n
            cls = 'd-tbl long' if a['long'] else 'd-tbl'
            th = ''.join(f'<th style="width:{x * 100:.0f}%">{H(hh)}</th>'
                         for hh, x in zip(a['headers'], pct))
            body = ''.join('<tr>' + ''.join(f'<td style="vertical-align:middle">{_hcell(c)}</td>'
                                            for c in r) + '</tr>' for r in a['rows'])
            B.append(f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>')
        elif kind == 'wk':
            rows = ''.join(_hrow(r) for r in a['rows'])
            B.append('<div style="break-inside:avoid;page-break-inside:avoid">'
                     f'<div class="sub-h lead" style="margin-top:10px"><b>{H(a["lead"])}</b></div>'
                     + (a['fig'].html() if a['fig'] else '') +
                     '<table class="d-tbl worked"><thead><tr><th colspan="7">算式</th>'
                     f'<th class="why" style="width:{a["why_pct"] * 100:.0f}%">這一步在做什麼</th></tr></thead>'
                     f'<tbody>{rows}</tbody></table></div>')
        elif kind == 'dual':
            th = ''.join(f'<th>{H(x)}</th>' for x in a['headers'])
            body = ''.join(f'<tr><td>{_hcell(l)}</td><td>{_hcell(r)}</td></tr>' for l, r in a['pairs'])
            B.append(f'<table class="d-tbl dual-track long"><thead><tr>{th}</tr></thead>'
                     f'<tbody>{body}</tbody></table>')
        elif kind == 'fig':
            B.append(a['f'].html())
        elif kind == 'frayer':
            labels = ['① 定義（用自己的話）', '② 特徵（必要條件）', '③ 例（是）',
                      '④ 非例（不是——差在哪個特徵）']

            def fc(i):
                body = a['q'][i]
                inner = (_hlines(a['n']) if body is None
                         else ''.join(f'<div>{H(t)}</div>' for t in body))
                return f'<td><div class="flab">{labels[i]}</div>{inner}</td>'
            B.append('<table class="d-tbl frayer">'
                     f'<tr><td class="term" colspan="2">{H(a["term"])}</td></tr>'
                     f'<tr>{fc(0)}{fc(1)}</tr><tr>{fc(2)}{fc(3)}</tr></table>')
        elif kind == 'step':
            rows = [f'<tr><th colspan="2">{_html.escape(a["title"])}</th></tr>']
            if a['trigger']:
                rows.append(f'<tr><td colspan="2" style="font-weight:400">什麼時候用：{H(a["trigger"])}</td></tr>')
            for i, s in enumerate(a['steps'], 1):
                act, pit = s if isinstance(s, tuple) else (s, None)
                if a['compact']:
                    rows.append(f'<tr><td colspan="2" style="font-weight:400">{i}. {H(act)}</td></tr>')
                else:
                    rows.append(f'<tr><td>{i}. {H(act)}</td>'
                                f'<td class="pitfall">{"※ " + H(pit) if pit else ""}</td></tr>')
            B.append('<table class="d-tbl step-card">' + ''.join(rows) + '</table>')
        elif kind == 'ref':
            B.append('<div class="ref-card">'
                     f'<div><b>▍{_html.escape(a["title"])}</b></div>'
                     f'<div class="trigger">什麼時候翻我：{H(a["trigger"])}</div>'
                     + ''.join(f'<div>{H(t)}</div>' for t in a['lines']) + '</div>')
        elif kind == 'q':
            main = (f'<div><b>{a["no"]}．</b>{H(a["stem"][0])}</div>'
                    + ''.join(f'<div>{H(t)}</div>' for t in a['stem'][1:]) + _hlines(a['n']))
            if a['hint'] or a['f']:
                side = a['f'].svg if a['f'] else ''
                if a['hint']:
                    side += (f'<div class="hintcard"><div class="ht">{_html.escape(a["ht"])}</div>'
                             + ''.join(f'<div>{H(t)}</div>' for t in a['hint']) + '</div>')
                B.append('<div class="aside-wrap boxed">'
                         f'<div class="aside-main">{main}</div><div class="aside-side">{side}</div></div>')
            else:
                B.append(f'<div class="problem">{main}</div>')
        elif kind == 'sc':
            B.append(f'<div class="selfcheck"><div><b>{_html.escape(a["title"])}</b></div>'
                     + ''.join(f'<div>☐ {H(t)}</div>' for t in a['items']) + '</div>')
        elif kind == 'cp':
            B.append('<div class="checkpoint">【核對點】做到這裡先停，對照上面的清單檢查一次再往下</div>')
        elif kind == 'lines':
            B.append(_hlines(a['n']))
        elif kind == 'ans':
            B.append(f'<div class="section-h page-break">{_html.escape(a["title"])}</div>')
            for g in a['groups']:
                B.append('<div class="problem">' + ''.join(f'<div>{H(t)}</div>' for t in g) + '</div>')
        elif kind == 'tn':
            rows = [('本份採用的主設計', a['main']),
                    ('輔助設計', '、'.join(a['aux']) or '無'),
                    ('選用理由', a['reason']), ('鷹架密度', a['density']),
                    ('褪除路徑', a['fading']),
                    ('課堂實施流程', '、'.join(a['flows'])),
                    ('對應官方輔助措施代碼', '、'.join(a['codes'])),
                    ('本單元對應的正規教學目標', a['goal'])] + list(a['extra'])
            body = ''.join(f'<tr><td>{_html.escape(k)}</td><td>{H(v)}</td></tr>' for k, v in rows)
            B.append('<div class="teacher-notes"><div class="section-h">教師實施說明'
                     '（本頁供教師參考，列印給學生時可不印）</div>'
                     f'<table class="d-tbl long">{body}</table></div>')
        else:
            raise ValueError(kind)
    title = os.path.splitext(os.path.basename(out_path))[0]
    head = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', _HEAD, count=1)
    doc = (head + '\n<body>\n<table class="sheet">\n'
           f'<tfoot><tr><td><div class="footer">{FOOTER}</div></td></tr></tfoot>\n'
           '<tbody><tr><td>\n' + '\n'.join(B) + '\n</td></tr></tbody>\n</table>\n</body>\n</html>\n')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(doc)
    return out_path


# ====================================================================== HTML → PDF
def html_to_pdf(html_path, pdf_path):
    """無頭 Chrome（獨立 profile，不碰使用者開緊的 Chrome）→ 先印 _tmp 再 replace。"""
    chrome = ds.find_chrome()
    html_path, pdf_path = os.path.abspath(html_path), os.path.abspath(pdf_path)
    d = os.path.dirname(pdf_path)
    tmp = os.path.join(d, '_tmp_' + os.path.basename(pdf_path))
    prof = os.path.join(d, '_tmp_chromeprofile')
    cmd = [chrome, '--headless', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
           f'--user-data-dir={prof}', '--virtual-time-budget=15000',
           '--run-all-compositor-stages-before-draw', f'--print-to-pdf={tmp}',
           'file:///' + os.path.abspath(html_path).replace('\\', '/')]
    subprocess.run(cmd, check=True, capture_output=True, timeout=180)
    for _ in range(10):
        try:
            os.replace(tmp, pdf_path)
            break
        except OSError:
            time.sleep(1.5)
    shutil.rmtree(prof, ignore_errors=True)
    return pdf_path


def build(blocks_handout, blocks_practice, unit, short):
    """產出講義＋練習的 docx 與 html（PDF 另外轉）。short＝檔名用的單元名。"""
    out = []
    for blocks, kind, typ in ((blocks_handout, '講義', '課堂講義'),
                              (blocks_practice, '練習', '課堂練習')):
        stem = os.path.join(BASE, f'{kind}_{short}_抽離小班共用版')
        out.append(render_docx(blocks, unit, typ, stem + '.docx'))
        out.append(render_html(blocks, unit, typ, stem + '.html'))
    return out
