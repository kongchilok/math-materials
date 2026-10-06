# -*- coding: utf-8 -*-
r"""高一 04 多項式 v2 的版面層（docx＋HTML 兩版渲染器＋無頭 Chrome 轉 PDF）。

沿用 v1 `04_多項式與因式定理／build_L1-L6_講義練習.py` 的渲染器（內容只寫一次，{} 標記→
docx OMML／HTML LaTeX），2026-10-06 抽成獨立模組，並加：
  - SYN2：⋆ 除式為二次式的綜合除法（poly_division.synthetic2_*）
  - html_to_pdf()：無頭 Chrome、獨立 profile，不殺使用者的 Chrome（見 memory）
"""
import html as _html
import os
import re
import sys
from fractions import Fraction as Fr

SKILL = r'C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator'
sys.path.insert(0, os.path.join(SKILL, 'scripts'))
from omml_docx import *  # noqa
from omml_docx import _tbl, _PAGE_CONTENT_WIDTH  # noqa
import poly_division as pd

BASE = os.path.dirname(os.path.abspath(__file__))
SUBJ = '高一數學'


# ================================================================ {} 標記 → LaTeX
_TEX_SYM = [('<=', r'\le '), ('>=', r'\ge '), ('!=', r'\ne '), ('<', r'\lt '), ('>', r'\gt '),
            ('·', r'\cdot '), ('⋯', r'\cdots '), ('⟺', r'\Leftrightarrow '), ('→', r'\to '),
            ('÷', r'\div '), ('×', r'\times '), ('±', r'\pm '), ('∓', r'\mp '), ('Δ', r'\Delta '),
            ('−', '-')]


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


def _split2(s):
    d = 0
    for j, ch in enumerate(s):
        if ch in '({':
            d += 1
        elif ch in ')}':
            d -= 1
        elif ch == ',' and d == 0:
            return s[:j], s[j + 1:]
    raise ValueError(f'frac 需要兩個參數：{s!r}')


def tex(s):
    out, i = [], 0
    while i < len(s):
        if s.startswith('frac(', i):
            j = _close(s, i + 4, '(', ')')
            a, b = _split2(s[i + 5:j])
            out.append(rf'\frac{{{tex(a)}}}{{{tex(b)}}}')
            i = j + 1
            continue
        c = s[i]
        if c in '^_':
            i += 1
            if s[i] == '{':
                j = _close(s, i, '{', '}')
                arg = tex(s[i + 1:j])
                i = j + 1
            else:
                m = re.match(r'[0-9]+|[A-Za-z]', s[i:])
                arg = m.group(0)
                i += len(arg)
            out.append(f'{c}{{{arg}}}')
            continue
        for a, b in _TEX_SYM:
            if s.startswith(a, i):
                out.append(b)
                i += len(a)
                break
        else:
            if ord(c) > 0x2E80:          # 中文 → \text{}
                j = i
                while j < len(s) and ord(s[j]) > 0x2E80:
                    j += 1
                out.append(rf'\text{{{s[i:j]}}}')
                i = j
            else:
                out.append(c)
                i += 1
    return ''.join(out)


def H(s):
    r"""含 {} 標記的一段文字 → HTML（文字轉義；數學轉 \(…\)）。"""
    out, i = [], 0
    while i < len(s):
        if s[i] == '{':
            j = _close(s, i, '{', '}')
            out.append(r'\(' + tex(s[i + 1:j]) + r'\)')
            i = j + 1
        else:
            j = s.find('{', i)
            j = len(s) if j < 0 else j
            out.append(_html.escape(s[i:j], quote=False))
            i = j
    return ''.join(out)


# ================================================================ 內容元件（兩版共用的資料）
# 每個元件是 tuple，第一格是種類。docx() 與 html() 各自把同一份清單畫出來。
def HD(t, brk=False):              return ('h', t, brk)
def P_(t, bold=False, keep=False): return ('p', t, bold, keep)
def SH(t):                         return ('shade', t)
def FML(t):                        return ('fml', t)         # 公式獨立成行（置中）
def STEP(title, trig, steps, fading=None): return ('step', title, trig, steps, fading)
def REF(title, trig, body):        return ('ref', title, trig, body)   # body = 元件清單
def WK(rows, why_pct=0.36, col_frac=None): return ('worked', rows, why_pct, col_frac)
def LD(dd, dv, blanks=()):         return ('ldiv', dd, dv, blanks)
def SYN(co, c, blanks=(), labels=True): return ('syn', co, c, blanks, labels)
def SYN2(co, p, q):                return ('syn2', co, p, q)   # ⋆ 除式 x²+px+q
def FIGN(fig, notes, title='每一步在做什麼'): return ('fign', fig, notes, title)
def TBL(headers, rows, fr=None):   return ('tbl', headers, rows, fr)
def LINES(n):                      return ('lines', n)
def SPACE(cm):                     return ('space', cm)
def Q(no, stem, work, hint=None, hint_title='提示'): return ('q', no, stem, work, hint, hint_title)
def ANS(label, items):             return ('ans', label, items)


def EQ(l, r, why=''):  return ('eq', l, r, why)
def SP(t, why=''):     return ('sp', t, why)
def AN(t, why='作答：最後一行用「∴」寫出答案'): return ('an', t, why)


# ================================================================ docx：整張表不被分頁切開
_PPR_RE = re.compile(r'<w:pPr>(.*?)</w:pPr>', re.S)


def keep_together(xml):
    """表格除最後一列外，每個段落加 keepNext——Word 只有 cantSplit（單列不切）時，
    手順卡／範例表仍會在列與列之間被分頁切開（2026-10-06 v2 驗收：三步卡第 2、3 步
    掉到下一頁；答案表只剩表頭留在頁底）。只用在短表（手順卡、範例表）。"""
    i = xml.rfind('<w:tr>')
    head, tail = xml[:i], xml[i:]
    head = _PPR_RE.sub(lambda m: m.group(0) if '<w:keepNext/>' in m.group(1)
                       else f'<w:pPr><w:keepNext/>{m.group(1)}</w:pPr>', head)
    head = re.sub(r'<w:p>(?!<w:pPr>)', '<w:p><w:pPr><w:keepNext/></w:pPr>', head)
    return head + tail


# ================================================================ docx renderer
def _docx_rows(rows):
    out = []
    for r in rows:
        if r[0] == 'eq':
            out.append(eq_row(r[1], r[2], r[3] or None))
        elif r[0] == 'sp':
            out.append(span_row(r[1], r[2] or None))
        else:
            out.append(answer_row(r[1], r[2]))
    return out


def _docx_fig(f):
    if f[0] == 'ldiv':
        return pd.long_division_docx(f[1], f[2], blanks=f[3])
    if f[0] == 'syn2':
        return pd.synthetic2_docx(f[1], f[2], f[3])
    return pd.synthetic_docx(f[1], f[2], blanks=f[3], labels=f[4])


def _docx_work(items):
    out = []
    for it in items:
        k = it[0]
        if k in ('ldiv', 'syn', 'syn2'):
            out += [_docx_fig(it), blank()]
        elif k == 'lines':
            out += write_lines(it[1])
        elif k == 'space':
            # 長除法要一大片「空白」寫直式——橫線會跟直式的減線打架，所以不用 write_lines
            out += [blank() for _ in range(int(round(it[1] / 0.64)))]
        elif k == 'p':
            out.append(para(it[1], bold=it[2]))
        else:
            raise ValueError(k)
    return out


def _docx_tbl(headers, rows, fr):
    n = len(headers)
    fr = fr or [1 / n] * n
    w = [int(_PAGE_CONTENT_WIDTH * f) for f in fr[:-1]]
    w.append(_PAGE_CONTENT_WIDTH - sum(w))
    out = [{'hdr': True, 'cells': [{'p': [para(h, bold=True, sz=22, spacing=False)],
                                    'shd': GREY_FILL} for h in headers]}]
    for r in rows:
        out.append({'cells': [{'p': [para(c, sz=22, spacing=False)], 'va': 'center'}
                              for c in r]})
    return _tbl(out, w)


def docx_elems(E):
    P = []
    for e in E:
        k = e[0]
        if k == 'h':
            P.append(heading(e[1], page_break_before=e[2]))
        elif k == 'p':
            P.append(para(e[1], bold=e[2], keep_next=e[3]))
        elif k == 'shade':
            P.append(shaded_box(e[1]))
        elif k == 'fml':
            P.append(para(e[1], jc='center'))
        elif k == 'step':
            P.append(keep_together(step_card(e[1], e[3], trigger=e[2], fading=e[4])))
        elif k == 'ref':
            inner = [para(f'▍{e[1]}', bold=True, sz=HEADING_SZ, spacing=False),
                     para(f'什麼時候翻我：{e[2]}', sz=21)]
            for b in e[3]:
                if b[0] == 'tbl':
                    inner += [_docx_tbl(b[1], b[2], b[3])]
                else:
                    inner += docx_elems([b])
            if inner[-1].rstrip().endswith('</w:tbl>'):
                inner.append(blank())
            P.append(_tbl([[{'p': inner}]], [_PAGE_CONTENT_WIDTH]))
        elif k == 'worked':
            P.append(keep_together(worked_example_table(_docx_rows(e[1]), why_pct=e[2],
                                                        col_frac=e[3])))
        elif k in ('ldiv', 'syn', 'syn2'):
            P += [_docx_fig(e), blank()]
        elif k == 'fign':
            P.append(aside_layout([_docx_fig(e[1])], hint_lines(e[2], title=e[3]),
                                  main_pct=0.55, boxed=True))
        elif k == 'tbl':
            P.append(_docx_tbl(e[1], e[2], e[3]))
        elif k == 'q':
            main = [para(f'{e[1]}．{e[2]}')] + _docx_work(e[3])
            if e[4]:
                P.append(aside_layout(main, hint_lines(e[4], title=e[5]),
                                      main_pct=0.62, boxed=True))
            else:
                P.append(problem_box(main))
        elif k == 'ans':
            inner = [para(f'{e[1]}', bold=True, spacing=False)] + _docx_work(e[2])
            if inner[-1].rstrip().endswith('</w:tbl>'):
                inner.append(blank())
            P.append(problem_box(inner))
        elif k == 'raw':
            P += e[1]
        else:
            raise ValueError(k)
    return P


def build_docx_file(doc):
    P = [masthead(SUBJ, doc['unit'], doc['type']), student_info_row()]
    P += docx_elems(doc['body'])
    if doc.get('notes'):
        n = doc['notes']
        P += teacher_notes(main_design=n['main'], aux_designs=n['aux'], reason=n['reason'],
                           density='全班共用', fading=n['fading'], flows=n['flows'],
                           iep_codes=n['iep'], extra=n['extra'])
    out = os.path.join(BASE, doc['file'] + '.docx')
    build_docx(P, out, footer_text=doc['foot'])
    return out


# ================================================================ HTML renderer
with open(os.path.join(SKILL, 'assets', 'worksheet-template.html'), encoding='utf-8') as f:
    _tpl = f.read()
_HEAD = _tpl[:_tpl.index('</head>') + len('</head>')]
_EXTRA_CSS = pd.DIVISION_CSS + r"""
  .fml { text-align: center; margin: 4px 0; }
  .ref-card .rt { font-size: 14pt; font-weight: 700; }
  .ref-card .d-tbl { margin: 6px 0 2px; }
  .ans-box2 { border: 0.75pt solid #000; padding: 6px 12px; margin: 10px 0; break-inside: avoid; page-break-inside: avoid; }
  .work-space { border: none; }
  .aside-wrap.fign .aside-main { flex: 1 1 55%; }
  .aside-wrap.fign .aside-side { flex: 0 0 43%; }
"""
_HEAD = _HEAD.replace('</style>', _EXTRA_CSS + '</style>')


def _html_rows(rows):
    out = []
    for r in rows:
        if r[0] == 'eq':
            out.append(f'<tr><td class="ec1">{H(r[1])}</td><td class="ec2">\\(=\\)</td>'
                       f'<td class="ec3" colspan="5">{H(r[2])}</td>'
                       f'<td class="why">{H(r[3])}</td></tr>')
        elif r[0] == 'sp':
            out.append(f'<tr><td class="ecs" colspan="7">{H(r[1])}</td>'
                       f'<td class="why">{H(r[2])}</td></tr>')
        else:
            out.append(f'<tr><td class="ecs ans" colspan="7">\\(\\therefore\\) {H(r[1])}</td>'
                       f'<td class="why">{H(r[2])}</td></tr>')
    return '\n'.join(out)


def _html_fig(f):
    if f[0] == 'ldiv':
        return pd.long_division_html(f[1], f[2], blanks=f[3])
    if f[0] == 'syn2':
        return pd.synthetic2_html(f[1], f[2], f[3])
    return pd.synthetic_html(f[1], f[2], blanks=f[3], labels=f[4])


def _html_work(items):
    out = []
    for it in items:
        k = it[0]
        if k in ('ldiv', 'syn', 'syn2'):
            out.append(_html_fig(it))
        elif k == 'lines':
            out.append('<div class="write-lines">' + '<div class="line"></div>' * it[1] + '</div>')
        elif k == 'space':
            out.append(f'<div class="work-space" style="height:{it[1]}cm"></div>')
        elif k == 'p':
            out.append(f'<div>{"<b>" if it[2] else ""}{H(it[1])}{"</b>" if it[2] else ""}</div>')
    return '\n'.join(out)


def _html_tbl(headers, rows, fr):
    n = len(headers)
    fr = fr or [1 / n] * n
    th = ''.join(f'<th style="width:{f * 100:.0f}%">{H(h)}</th>' for h, f in zip(headers, fr))
    body = ''.join('<tr>' + ''.join(f'<td style="vertical-align:middle">{H(c)}</td>' for c in r)
                   + '</tr>' for r in rows)
    return f'<table class="d-tbl"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table>'


def _hintcard(lines, title):
    return ('<div class="hintcard"><div class="ht">' + H(title) + '</div>'
            + ''.join(f'<div>{H(t)}</div>' for t in lines) + '</div>')


def html_elems(E):
    B = []
    for e in E:
        k = e[0]
        if k == 'h':
            cls = 'section-h page-break' if e[2] else 'section-h'
            B.append(f'<div class="{cls}">{H(e[1])}</div>')
        elif k == 'p':
            t = H(e[1])
            if e[2]:
                t = f'<b>{t}</b>'
            B.append(f'<div class="{"lead" if e[3] else ""}">{t}</div>')
        elif k == 'shade':
            B.append(f'<div class="hint-card">{H(e[1])}</div>')
        elif k == 'fml':
            B.append(f'<div class="fml">{H(e[1])}</div>')
        elif k == 'step':
            rows = [f'<tr><th colspan="2">{H(e[1])}</th></tr>',
                    f'<tr><td colspan="2" style="font-weight:400">什麼時候用：{H(e[2])}</td></tr>']
            for i, (act, pit) in enumerate(e[3], 1):
                rows.append(f'<tr><td>{i}. {H(act)}</td><td class="pitfall">※ {H(pit)}</td></tr>')
            if e[4]:
                rows.append(f'<tr><td colspan="2" style="font-weight:400;font-size:9.5pt;'
                            f'background:#f0f0f0">（教師）褪除：{H(e[4])}</td></tr>')
            B.append('<table class="d-tbl step-card">' + ''.join(rows) + '</table>')
        elif k == 'ref':
            inner = [f'<div class="rt">▍{H(e[1])}</div>',
                     f'<div class="trigger">什麼時候翻我：{H(e[2])}</div>']
            for b in e[3]:
                inner.append(_html_tbl(b[1], b[2], b[3]) if b[0] == 'tbl' else html_elems([b]))
            B.append('<div class="ref-card">' + '\n'.join(inner) + '</div>')
        elif k == 'worked':
            B.append('<table class="d-tbl worked"><thead><tr><th colspan="7">算式</th>'
                     '<th class="why">這一步在做什麼</th></tr></thead><tbody>'
                     + _html_rows(e[1]) + '</tbody></table>')
        elif k in ('ldiv', 'syn', 'syn2'):
            B.append(_html_fig(e))
        elif k == 'fign':
            B.append('<div class="aside-wrap boxed fign"><div class="aside-main">'
                     + _html_fig(e[1]) + '</div><div class="aside-side">'
                     + _hintcard(e[2], e[3]) + '</div></div>')
        elif k == 'tbl':
            B.append(_html_tbl(e[1], e[2], e[3]))
        elif k == 'q':
            main = f'<div><b>{e[1]}．</b>{H(e[2])}</div>' + _html_work(e[3])
            if e[4]:
                B.append('<div class="aside-wrap boxed"><div class="aside-main">' + main
                         + '</div><div class="aside-side">' + _hintcard(e[4], e[5])
                         + '</div></div>')
            else:
                B.append(f'<div class="problem">{main}</div>')
        elif k == 'ans':
            B.append(f'<div class="ans-box2"><div><b>{H(e[1])}</b></div>'
                     + _html_work(e[2]) + '</div>')
        else:
            raise ValueError(k)
    return '\n'.join(B)


def build_html_file(doc):
    head = re.sub(r'<title>.*?</title>', f'<title>{doc["file"]}</title>', _HEAD, count=1)
    body = ['<div class="masthead"><span>科目：高一數學</span>'
            f'<span>單元：{doc["unit"]}</span><span>類型：{doc["type"]}</span></div>',
            '<div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">'
            '&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>',
            html_elems(doc['body'])]
    if doc.get('notes'):
        n = doc['notes']
        rows = [('本份採用的主設計', n['main']), ('輔助設計', '、'.join(n['aux'])),
                ('選用理由', n['reason']), ('鷹架密度', '全班共用'), ('褪除路徑', n['fading']),
                ('課堂實施流程', '、'.join(n['flows'])),
                ('對應官方輔助措施代碼', '、'.join(n['iep']))] + list(n['extra'])
        body.append('<div class="teacher-notes page-break"><div class="section-h">'
                    '教師實施說明（本頁供教師參考，列印給學生時可不印）</div>'
                    '<table class="d-tbl long">'
                    + ''.join(f'<tr><td>{H(a)}</td><td>{H(b)}</td></tr>' for a, b in rows)
                    + '</table></div>')
    page = (head + '\n<body>\n<table class="sheet">\n'
            f'  <tfoot><tr><td><div class="footer">{doc["foot"]}</div></td></tr></tfoot>\n'
            '  <tbody><tr><td>\n' + '\n'.join(body)
            + '\n  </td></tr></tbody>\n</table>\n</body>\n</html>\n')
    out = os.path.join(BASE, doc['file'] + '.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(page)
    return out



# ================================================================ HTML → PDF
def html_to_pdf(html_path, pdf_path=None):
    """無頭 Chrome（獨立 profile，不碰使用者開緊的 Chrome）→ 先印 _tmp 再 replace。"""
    import shutil
    import subprocess
    import time
    import design_svg as ds
    html_path = os.path.abspath(html_path)
    pdf_path = os.path.abspath(pdf_path or os.path.splitext(html_path)[0] + '.pdf')
    d = os.path.dirname(pdf_path)
    tmp = os.path.join(d, '_tmp_' + os.path.basename(pdf_path))
    prof = os.path.join(d, '_tmp_chromeprofile')
    cmd = [ds.find_chrome(), '--headless', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
           f'--user-data-dir={prof}', '--virtual-time-budget=15000',
           '--run-all-compositor-stages-before-draw', f'--print-to-pdf={tmp}',
           'file:///' + html_path.replace(os.sep, '/')]
    subprocess.run(cmd, check=True, capture_output=True, timeout=180)
    for _ in range(10):
        try:
            os.replace(tmp, pdf_path)
            break
        except OSError:
            time.sleep(1.5)
    shutil.rmtree(prof, ignore_errors=True)
    return pdf_path
