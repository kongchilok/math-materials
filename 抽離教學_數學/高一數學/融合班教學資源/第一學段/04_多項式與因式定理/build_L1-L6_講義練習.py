# -*- coding: utf-8 -*-
r"""高一 04《多項式與因式定理》前三對講義／練習（對應簡報 L1–L6）一次產出 docx＋HTML。

  講義／練習_多項式除法_融合版            ← 簡報 L1 除法原理與長除法、L2 綜合除法
  講義／練習_餘式定理與因式定理_融合版    ← 簡報 L3 餘式定理、L4 因式定理
  講義／練習_牛頓定理與多項式基本定理_融合版 ← 簡報 L5 牛頓定理、L6 多項式基本定理

2026-09-25 使用者要求重做（原檔是 2026-07-12 舊管線：公式塞在灰底框當純文字、
沒有長除法直式、沒有教師說明頁、標題 x³+2x²+3x+1 ÷ (x−1) 漏了被除式括號）。
使用者裁決：講義＋練習一齊重出；主 D2 手順卡＋輔 D7 提示卡；綜合除法 c 放左邊（跟簡報）。
長除法版面照使用者給的課本式樣本（見 poly_division.py 檔頭），範例二就是那一題。

寫法：內容只寫一次（{} 數學標記＝docx 語法），HTML 版由 tex() 自動轉 LaTeX——
兩版內容不會各自漂移。長除法／綜合除法的每一格數字都由 poly_division 的引擎算，
不手打。

執行：python build_L1-L6_講義練習.py  → 6 個 .docx ＋ 6 個 .html（PDF 由 HTML 轉）
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
def WK(rows, why_pct=0.36):        return ('worked', rows, why_pct)
def LD(dd, dv, blanks=()):         return ('ldiv', dd, dv, blanks)
def SYN(co, c, blanks=(), labels=True): return ('syn', co, c, blanks, labels)
def FIGN(fig, notes, title='每一步在做什麼'): return ('fign', fig, notes, title)
def TBL(headers, rows, fr=None):   return ('tbl', headers, rows, fr)
def LINES(n):                      return ('lines', n)
def SPACE(cm):                     return ('space', cm)
def Q(no, stem, work, hint=None, hint_title='提示'): return ('q', no, stem, work, hint, hint_title)
def ANS(label, items):             return ('ans', label, items)


def EQ(l, r, why=''):  return ('eq', l, r, why)
def SP(t, why=''):     return ('sp', t, why)
def AN(t, why='作答：最後一行用「∴」寫出答案'): return ('an', t, why)


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
    return pd.synthetic_docx(f[1], f[2], blanks=f[3], labels=f[4])


def _docx_work(items):
    out = []
    for it in items:
        k = it[0]
        if k in ('ldiv', 'syn'):
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
            P.append(step_card(e[1], e[3], trigger=e[2], fading=e[4]))
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
            P.append(worked_example_table(_docx_rows(e[1]), why_pct=e[2]))
        elif k in ('ldiv', 'syn'):
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
    return pd.synthetic_html(f[1], f[2], blanks=f[3], labels=f[4])


def _html_work(items):
    out = []
    for it in items:
        k = it[0]
        if k in ('ldiv', 'syn'):
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
        elif k in ('ldiv', 'syn'):
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


# ================================================================ 共用：手順卡與精簡提示
IEP = ('a3 提示題目重點', 'a6 增加行距', 'b5 提供步驟提示卡')
FLOWS = ('F1 師徒制對話四步（老師做第一個範例、學生口述第二個範例的每一步）',
         'F2 番茄鐘分段（練習 A／B／C 三段）')

CARD_LD = STEP('長除法　四步', '除式是一次或以上的多項式，要求商式和餘式', [
    ('除：拿剩下那條式的最高次項，除以除式的最高次項', '商寫在「同次項」那一欄的正上方'),
    ('乘：把這一項商乘回整個除式，寫在下面', '每一項對齊同次的那一欄'),
    ('減：上下相減，再把下一項帶下來', '減的是整條式，每一項都要變號'),
    ('重複：直到剩下的次數比除式低，那就是餘式', '次數還沒比除式低，不可以停'),
], fading='完整四步卡 → 只留「除 → 乘 → 減 → 重複」四個字 → 只問「這題要做幾輪」→ 移除')
CARD_SYN = STEP('綜合除法　四步', '除式是一次式 {x-a} 或 {ax-b}，想快一點求商式和餘式', [
    ('寫係數：由高次到低次排成一列', '缺的項要補 0'),
    ('令除式 ＝ 0，解出的數 c 寫在左邊', '{x+1} 用 {-1}；{x-2} 用 {2}'),
    ('第一個係數直接抄下；之後每一格先乘 c，再往下加', '乘的是左下方剛算出來的那個數'),
    ('讀答案：最後一格是餘式，前面是商式係數', '商式比被除式低一次'),
], fading='完整四步卡 → 只留「補 0、變號、先乘後加」三句 → 只問「c 是多少」→ 移除')
HINT_LD = ['① 除：只看最高次項', '② 乘：商乘回整個除式', '③ 減：每一項都變號，再帶下一項',
           '④ 重複：直到次數比除式低']
HINT_SYN = ['① 係數由高到低，缺項補 0', '② 令除式 ＝ 0 → c', '③ 第一個抄下，之後先乘後加',
            '④ 最後一格是餘式']

CARD_REM = STEP('用餘式定理求餘式　四步', '題目只問餘式、不問商式', [
    ('令除式 ＝ 0，解出要代入的 x', '{x+2} 要代 {-2}；{2x-1} 要代 {frac(1,2)}'),
    ('把這個數代入 {f(x)}，負數和分數都加括號', '先算次方，再乘係數'),
    ('逐項算出每一項的值', '一項一項寫，不要心算一整條'),
    ('加起來就是餘式', '答案是一個數；算出含 x 就是錯了'),
], fading='完整四步卡 → 只留「令除式 ＝ 0 → 代入 → 逐項算」→ 只問「要代哪個數」→ 移除')
CARD_FAC = STEP('用因式定理求未知係數　四步', '題目說「{(x-c)} 是因式」或「能被 {(x-c)} 整除」', [
    ('每個因式寫一條「代入 ＝ 0」的式', '{(x+2)} 要代 {-2}：令括號內 ＝ 0'),
    ('代入第一條，化簡成方程 ①', '整理到只剩未知數和常數'),
    ('代入第二條，化簡成方程 ②', '有幾個未知數，就要幾條方程'),
    ('聯立 ①、② 解出未知數，再代回檢查', '代回後應該得 0'),
], fading='完整四步卡 → 只留「一個因式一條式」→ 只問「要列幾條式」→ 移除')
HINT_REM = ['① 令除式 ＝ 0，得要代的數', '② 代入，負數加括號', '③ 逐項算', '④ 加起來＝餘式']

CARD_NEW = STEP('找整係數一次因式　四步', '要因式分解三次或以上的多項式，又找不到公因式', [
    ('看最高次項係數，列出它的因數 → {a}', '係數是 1 時，{a} 只有 1'),
    ('看常數項，列出它的因數 → {b}', '正負都要列：6 的因數是 {±1}、{±2}、{±3}、{±6}'),
    ('組合出所有候選因式 {(ax-b)}', '首項係數不是 1 時，要試分數 {frac(b,a)}'),
    ('逐個代入：{f(frac(b,a))} 等於 0 就是因式', 'n 次式最多 n 個一次因式，找夠就停'),
], fading='完整四步卡 → 只留「a 除首項，b 除常數項」→ 只問「候選有幾個」→ 移除')
CARD_FUN = STEP('已知零點寫出多項式　四步', '題目給出幾個令 {f(x)=0} 的 x，再給多一個點', [
    ('寫出樣子：每個零點寫一個括號，前面乘 {a}', '零點是 1 → 寫 {(x-1)}；零點是 {-5} → 寫 {(x+5)}'),
    ('代入另外給的那一點', '那一點不是零點，算出來不是 0'),
    ('先算括號，再解出 {a}', '{a} 不可以是 0'),
    ('把 {a} 代回，寫出完整答案', '題目要求時再展開'),
], fading='完整四步卡 → 只留「先寫樣子，再求 a」→ 只問「有幾個零點」→ 移除')
HINT_NEW = ['① 首項係數的因數 → a', '② 常數項的因數 → b（連負數）', '③ 組合候選', '④ 逐個代入，得 0 的就是']
HINT_FUN = ['① 每個零點寫一個括號，前面乘 a', '② 代入另外那一點', '③ 解出 a', '④ 代回寫答案']


# ================================================================ 1 講義：多項式除法
UNIT1 = '多項式除法（長除法與綜合除法）'
FOOT1 = '高一數學．多項式除法'

HANDOUT1 = dict(file='講義_多項式除法_融合版', unit=UNIT1, type='課堂講義', foot=FOOT1, body=[
    HD('一、從「數的除法」談起'),
    P_('小學學過 17 ÷ 5 ＝ 3 餘 2。把它寫成一條乘法，就是：'),
    FML('{17=5×3+2}'),
    P_('被除數 ＝ 除數 × 商 ＋ 餘數，而且餘數 2 比除數 5 小。'
       '多項式的除法是同一個道理，只是把「數」換成「x 的式子」。'),

    HD('二、除法原理'),
    REF('除法原理', '題目要求商式、餘式，或要把一個多項式寫成「除式 × 商式 ＋ 餘式」', [
        FML('{f(x)=g(x)·q(x)+r(x)}'),
        P_('其中 {r(x)=0}，或 {r(x)} 的次數比 {g(x)} 的次數低。'),
        TBL(('名稱', '寫法', '在 17 ÷ 5 裡'), [
            ('被除式', '{f(x)}', '17'), ('除式', '{g(x)}', '5'),
            ('商式', '{q(x)}', '3'), ('餘式', '{r(x)}', '2')], fr=(0.3, 0.3, 0.4)),
    ]),

    HD('三、長除法的手順卡'),
    CARD_LD,
    SH('動筆前先做一件事：被除式由高次到低次排好，缺的項補 0。'
       '例如 {x^3+1} 要寫成 {x^3+0x^2+0x+1}。'),

    HD('四、範例一：長除法', brk=True),
    P_('★ 範例一：求 {(x^3+2x^2+3x+1)÷(x-1)} 的商式及餘式。', bold=True, keep=True),
    FIGN(LD([1, 2, 3, 1], [1, -1]), [
        '① 除：{x^3÷x=x^2}，寫在 {x^2} 那一欄上面',
        '② 乘：{x^2(x-1)=x^3-x^2}',
        '③ 減：相減得 {3x^2}，帶下 {+3x}',
        '④ 重複：{3x^2÷x=3x}，再乘、再減，帶下 {+1}',
        '　 再重複：{6x÷x=6}，再乘、再減',
        '剩下 7，次數比 {x-1} 低，停。',
    ]),
    WK([SP('檢查：{(x-1)(x^2+3x+6)+7=x^3+2x^2+3x+1}', '除式 × 商式 ＋ 餘式，應該變回被除式'),
        AN('商式為 {x^2+3x+6}，餘式為 {7}')]),

    P_('★ 範例二：求 {(x^3-12x^2-42)÷(x-3)} 的商式及餘式。', bold=True, keep=True),
    P_('被除式沒有 x 項——先補成 {x^3-12x^2+0x-42}，每一欄才對得齊。', keep=True),
    FIGN(LD([1, -12, 0, -42], [1, -3]), [
        '① 補 0：{+0x} 佔住 x 那一欄',
        '② 第一輪：{x^3÷x=x^2}；乘回得 {x^3-3x^2}；相減得 {-9x^2}，帶下 {+0x}',
        '③ 第二輪：{-9x^2÷x=-9x}；乘回得 {-9x^2+27x}；相減得 {-27x}，帶下 {-42}',
        '④ 第三輪：{-27x÷x=-27}；乘回得 {-27x+81}；相減得 {-123}',
        '{-123} 是常數，停。',
    ]),
    WK([SP('檢查：{(x-3)(x^2-9x-27)-123=x^3-12x^2-42}', '除式 × 商式 ＋ 餘式，應該變回被除式'),
        AN('商式為 {x^2-9x-27}，餘式為 {-123}')]),

    HD('五、綜合除法的手順卡', brk=True),
    P_('長除法每一輪都要抄一次 {x^3}、{x^2}、{x}……其實次方是跟著「位置」走的，'
       '只寫係數就夠了——這就是綜合除法。'),
    CARD_SYN,

    HD('六、範例三：綜合除法'),
    P_('★ 範例三：求 {(x^2+3x+6)÷(x+1)} 的商式及餘式。', bold=True, keep=True),
    FIGN(SYN([1, 3, 6], -1), [
        '① 寫係數：1，3，6',
        '② 令 {x+1=0}，得 {c=-1}，寫在左邊',
        '③ 第一個 1 直接抄下',
        '　 {1×(-1)=-1}，寫在 3 下面；{3+(-1)} 得 2',
        '　 {2×(-1)=-2}，寫在 6 下面；{6+(-2)} 得 4',
        '④ 讀答案：1，2 是商式係數 → {x+2}；4 是餘式',
    ]),
    WK([SP('檢查：{(x+1)(x+2)+4=x^2+3x+6}', '除式 × 商式 ＋ 餘式，應該變回被除式'),
        AN('商式為 {x+2}，餘式為 {4}')]),

    HD('七、範例四：除式 x 的係數不是 1', brk=True),
    SH('除式是 {ax-b} 時：用 {c=frac(b,a)} 做綜合除法，得出的商式係數要再除以 {a}；餘式不用除。'),
    P_('★ 範例四：求 {(4x^3+4x^2-x-3)÷(2x+1)} 的商式及餘式。', bold=True, keep=True),
    FIGN(SYN([4, 4, -1, -3], Fr(-1, 2)), [
        '① 令 {2x+1=0}，得 {c=-frac(1,2)}',
        '② 做法跟範例三一樣：先乘 c，再往下加',
        '③ 得出 4，2，{-2} 是「除以 {x+frac(1,2)}」的商式係數',
        '④ {2x+1} 是 {x+frac(1,2)} 的 2 倍，所以商式係數要再除以 2：2，1，{-1}',
        '餘式 {-2} 不用除。',
    ]),
    WK([SP('檢查：{(2x+1)(2x^2+x-1)-2=4x^3+4x^2-x-3}', '除式 × 商式 ＋ 餘式，應該變回被除式'),
        AN('商式為 {2x^2+x-1}，餘式為 {-2}')]),

    P_('接下來請拿《多項式除法 —— 課堂練習》，依這兩張手順卡完成練習 A、B、C。'),
], notes=dict(
    main='D2 手順卡（長除法四步、綜合除法四步）',
    aux=('D7 提示卡（除法原理）',),
    reason='本課屬 S2 多步驟程序運算：長除法每一輪都是「除 → 乘 → 減 → 帶下一項」，'
           '學生最常在「減」漏變號、在缺項處錯欄，工作記憶一滿就整條崩。主設計取 D2，'
           '並用「一欄一個次數」的直式版面把同次項對齊外顯化；除法原理是之後餘式定理的根，'
           '故以 D7 提示卡框出，寫明何時翻用。',
    fading='本份練習紙面已做三級：練習A 半成品格子＋每題重印四步 → 練習B 只在區塊開頭放一次'
           '四步 → 練習C 不放任何提示。下一份（餘式定理）起，長除法只留「除乘減重複」四字 → 移除。',
    flows=FLOWS, iep=IEP,
    extra=[('正規教學目標（本單元對應）',
            'A—2—2 瞭解多項式的綜合除法；理解餘式定理（本份涵蓋前半：綜合除法）。'
            '長除法（多項式除以多項式）屬基力以外：校本，作為綜合除法與餘式定理的先備。'),
           ('與教學簡報的對應',
            '簡報_L1_除法原理與長除法、簡報_L2_綜合除法。兩張手順卡的步驟與簡報「長除法四步走」'
            '「綜合除法四步走」一致；簡報 L1 只有逐步表、沒有直式，本份補上直式版面（範例一、二），'
            '上課可直接投影。範例二是使用者提供的直式樣本題。綜合除法的 c 寫在左邊，與簡報 L2 相同。')]))

# ================================================================ 1 練習：多項式除法
FILL = P_('商式：＿＿＿＿＿＿＿＿　　餘式：＿＿＿＿')
EXERCISE1 = dict(file='練習_多項式除法_融合版', unit=UNIT1, type='課堂練習', foot=FOOT1, body=[
    P_('忘記做法就先回頭看《多項式除法 —— 課堂講義》第三節（長除法）和第五節（綜合除法）的手順卡。'),
    HD(f'一、練習A（{star_label(1)}）—— 照格子填空'),
    Q(1, '用長除法求 {(x^2+5x+6)÷(x+2)} 的商式及餘式。',
      [LD([1, 5, 6], [1, 2], blanks={('q', 0), ('prod', 1, 1), ('prod', 1, 0), ('diff', 1, 0)}),
       FILL], HINT_LD, '長除法四步'),
    Q(2, '用綜合除法求 {(2x^2+3x-2)÷(x+2)} 的商式及餘式。',
      [SYN([2, 3, -2], -2, blanks={('mul', 1), ('mul', 2), ('res', 0), ('res', 1), ('res', 2)}),
       FILL], HINT_SYN, '綜合除法四步'),
    Q(3, '用綜合除法求 {(x^2-x-6)÷(x-3)} 的商式及餘式。',
      [SYN([1, -1, -6], 3, blanks={('mul', 1), ('mul', 2), ('res', 0), ('res', 1), ('res', 2)}),
       FILL], HINT_SYN, '綜合除法四步'),

    HD(f'二、練習B（{star_label(2)}）—— 自己畫格子', brk=True),
    SH('長除法：除 → 乘 → 減 → 重複。綜合除法：寫係數（缺項補 0）→ 令除式 ＝ 0 得 c → '
       '先乘後加 → 最後一格是餘式。'),
    Q(4, '用長除法求 {(x^3-1)÷(x-1)} 的商式及餘式。', [SPACE(6.0), FILL]),
    Q(5, '用綜合除法求 {(3x^3-2x^2+5x-4)÷(x-2)} 的商式及餘式。', [SPACE(3.6), FILL]),
    Q(6, '用綜合除法求 {(2x^3+x^2-4x-5)÷(2x-3)} 的商式及餘式。', [SPACE(3.6), FILL]),

    HD(f'三、練習C（{star_label(3)}）—— 挑戰題', brk=True),
    Q(7, '求 {(2x^4-7x^3+14x+4)÷(x+2)} 的商式及餘式。', [SPACE(4.4), FILL]),
    Q(8, '在一個多項式除法中，被除式為 {2x^3-4x^2+x-4}，商式為 {2x^2-2x-1}，'
         '餘式為 {-5}。求除式。', [SPACE(8.0), P_('除式：＿＿＿＿＿＿＿＿')]),

    HD('教師用參考答案', brk=True),
    ANS('1．長除法', [LD([1, 5, 6], [1, 2]), P_('∴ 商式為 {x+3}，餘式為 {0}')]),
    ANS('2．{c=-2}', [SYN([2, 3, -2], -2), P_('∴ 商式為 {2x-1}，餘式為 {0}')]),
    ANS('3．{c=3}', [SYN([1, -1, -6], 3), P_('∴ 商式為 {x+2}，餘式為 {0}')]),
    ANS('4．補 0 後為 {x^3+0x^2+0x-1}', [LD([1, 0, 0, -1], [1, -1]),
                                          P_('∴ 商式為 {x^2+x+1}，餘式為 {0}')]),
    ANS('5．{c=2}', [SYN([3, -2, 5, -4], 2), P_('∴ 商式為 {3x^2+4x+13}，餘式為 {22}')]),
    ANS('6．令 {2x-3=0}，{c=frac(3,2)}', [
        SYN([2, 1, -4, -5], Fr(3, 2)),
        P_('商式係數 2，4，2 再除以 2 → 1，2，1；餘式不用除'),
        P_('∴ 商式為 {x^2+2x+1}，餘式為 {-2}')]),
    ANS('7．{c=-2}（{x^2} 項補 0）', [SYN([2, -7, 0, 14, 4], -2),
                                  P_('∴ 商式為 {2x^3-11x^2+22x-30}，餘式為 {64}')]),
    ANS('8．被除式 − 餘式 ＝ 除式 × 商式', [
        P_('{2x^3-4x^2+x-4-(-5)=2x^3-4x^2+x+1}，再除以商式 {2x^2-2x-1}：'),
        LD([2, -4, 1, 1], [2, -2, -1]),
        P_('∴ 除式為 {x-1}')]),
])

# ================================================================ 2 講義：餘式定理與因式定理
UNIT2 = '餘式定理與因式定理'
FOOT2 = '高一數學．餘式定理與因式定理'
HANDOUT2 = dict(file='講義_餘式定理與因式定理_融合版', unit=UNIT2, type='課堂講義', foot=FOOT2, body=[
    HD('一、餘式定理：不用做除法，也知道餘式'),
    P_('上一份講義用綜合除法求餘式。如果題目只問餘式、不問商式，還有更快的方法。'),
    REF('餘式定理', '題目只問「餘式」，不問商式', [
        FML('{f(x)÷(x-a)} 的餘式 ＝ {f(a)}'),
        P_('為什麼：由除法原理 {f(x)=(x-a)·q(x)+r}，把 {x=a} 代入，'
           '{(a-a)} 是 0，前面整項消失，只剩下 {r}。'),
    ]),

    HD('二、用餘式定理求餘式的手順卡'),
    CARD_REM,

    HD('三、範例一', brk=True),
    P_('★ 範例一：{f(x)=x^3-3x^2+2x-5}，求 {f(x)} 除以 {(x-2)} 的餘式。', bold=True, keep=True),
    WK([EQ('{x-2}', '{0}', '第 1 步：令除式 ＝ 0'),
        EQ('{x}', '{2}', '要代入的數是 2'),
        EQ('{f(2)}', '{2^3-3(2)^2+2(2)-5}', '第 2 步：代入'),
        EQ('{f(2)}', '{8-12+4-5}', '第 3 步：逐項算'),
        EQ('{f(2)}', '{-5}', '第 4 步：加起來'),
        AN('餘式為 {-5}')]),
    FIGN(SYN([1, -3, 2, -5], 2), [
        '用綜合除法核對：最後一格也是 {-5}。',
        '餘式定理只是跳過了前面那幾格。',
        '兩個方法答案一樣——考試時可以用其中一個檢查另一個。',
    ], title='兩個方法，同一個餘式'),

    HD('四、除式是 ax − b 的情形'),
    SH('除式是 {ax-b} 時，一樣令除式 ＝ 0：{ax-b=0}，所以要代入 {x=frac(b,a)}。'),
    P_('★ 範例二：{g(x)=2x^3-x^2+3x-1}，求 {g(x)} 除以 {(2x-1)} 的餘式。', bold=True, keep=True),
    WK([EQ('{2x-1}', '{0}', '第 1 步：令除式 ＝ 0'),
        EQ('{x}', '{frac(1,2)}', '要代入的數是 {frac(1,2)}'),
        EQ('{g(frac(1,2))}', '{2(frac(1,2))^3-(frac(1,2))^2+3(frac(1,2))-1}', '第 2 步：代入，分數加括號'),
        EQ('{g(frac(1,2))}', '{frac(1,4)-frac(1,4)+frac(3,2)-1}', '第 3 步：逐項算'),
        EQ('{g(frac(1,2))}', '{frac(1,2)}', '第 4 步：加起來'),
        AN('餘式為 {frac(1,2)}')], why_pct=0.30),
    SH('{f(a)} 有兩個身份：它是函數在 {x=a} 的值，也是 {f(x)} 除以 {(x-a)} 的餘式。'),

    HD('五、因式定理：餘式剛好是 0', brk=True),
    REF('因式定理', '題目說「{(x-c)} 是因式」或「能被 {(x-c)} 整除」', [
        FML('{(x-c)} 是 {f(x)} 的因式 {⟺} {f(c)=0}'),
        P_('因式定理就是餘式定理中「餘式剛好是 0」的情形。反過來用，可以求多項式裡的未知係數。'),
    ]),
    CARD_FAC,

    HD('六、範例三'),
    P_('★ 範例三：設 {f(x)=x^3+px^2+qx-6} 有因式 {(x-1)} 及 {(x-2)}，求 {p}、{q} 的值。',
       bold=True, keep=True),
    WK([SP('{f(1)=0}，{f(2)=0}', '第 1 步：兩個因式，各寫一條「代入 ＝ 0」'),
        EQ('{1+p+q-6}', '{0}', '第 2 步：代入 {f(1)=0}'),
        EQ('{p+q}', '{5}', '化簡，記作 ①'),
        EQ('{8+4p+2q-6}', '{0}', '第 3 步：代入 {f(2)=0}'),
        EQ('{4p+2q}', '{-2}', '移項'),
        EQ('{2p+q}', '{-1}', '兩邊除以 2，記作 ②'),
        EQ('{p}', '{-6}', '第 4 步：② − ①'),
        EQ('{q}', '{11}', '代回 ①：{-6+q=5}'),
        AN('{p=-6}，{q=11}')]),
    SH('檢查：代回得 {f(x)=x^3-6x^2+11x-6}。{f(1)}：{1-6+11-6}，得 0；'
       '{f(2)}：{8-24+22-6}，也得 0。✓'),

    P_('接下來請拿《餘式定理與因式定理 —— 課堂練習》，依這兩張手順卡完成練習 A、B、C。'),
], notes=dict(
    main='D2 手順卡（求餘式四步、求未知係數四步）',
    aux=('D7 提示卡（餘式定理、因式定理）',),
    reason='本課屬 S2 多步驟程序運算：代入求值要連續做「定代入值 → 代入 → 次方 → 乘係數 → 加總」，'
           '學生最常錯在 (x + 2) 代成 2、負數不加括號。主設計取 D2；兩條定理用 D7 提示卡框出並寫明'
           '「什麼時候翻我」，因為學生常分不清題目該用哪一條。範例一後附綜合除法核對，把上一份講義的'
           '直式接過來，讓學生看見餘式定理只是「跳過前面幾格」。',
    fading='本份練習紙面已做三級：練習A 每題重印四步 → 練習B 只在區塊開頭放一次提示 → 練習C 不放。'
           '下一份（牛頓定理）起只留「令除式 ＝ 0 → 代入」一句 → 移除。',
    flows=FLOWS, iep=IEP,
    extra=[('正規教學目標（本單元對應）',
            'A—2—2 瞭解多項式的綜合除法；理解餘式定理（本份涵蓋後半：餘式定理）；'
            'A—2—4 能夠運用數值代入法和比較係數法求待定係數（範例三、練習 B、C 用數值代入法）。'),
           ('與教學簡報的對應',
            '簡報_L3_餘式定理（例題一、二＝本份範例一、二）、簡報_L4_因式定理（例題＝本份範例三）。'
            '兩張手順卡的四步與簡報「四步算」「求未知係數四步走」一致。')]))

EXERCISE2 = dict(file='練習_餘式定理與因式定理_融合版', unit=UNIT2, type='課堂練習', foot=FOOT2, body=[
    P_('忘記做法就先回頭看《餘式定理與因式定理 —— 課堂講義》第二節和第五節的手順卡。'),
    HD(f'一、練習A（{star_label(1)}）—— 直接代入求餘式'),
    Q(1, '設 {f(x)=x^2-4x+1}，求 {f(x)} 除以 {(x-3)} 的餘式。', [LINES(5)], HINT_REM, '求餘式四步'),
    Q(2, '設 {f(x)=x^3-2x+3}，求 {f(x)} 除以 {(x+2)} 的餘式。', [LINES(5)], HINT_REM, '求餘式四步'),
    Q(3, '設 {f(x)=x^3+2x^2-x+4}，求 {f(x)} 除以 {(x+1)} 的餘式。', [LINES(5)], HINT_REM, '求餘式四步'),

    HD(f'二、練習B（{star_label(2)}）—— 因式定理，以及除式是 ax − b', brk=True),
    SH('「{(x-c)} 是因式」→ 寫 {f(c)=0}。除式是 {ax-b} → 代入 {x=frac(b,a)}。'),
    Q(4, '已知 {x^2+kx+9} 有因式 {(x-3)}，求 {k} 的值。', [LINES(5)]),
    Q(5, '已知 {x^2-5x+a} 有因式 {(x+2)}，求 {a} 的值。', [LINES(5)]),
    Q(6, '設 {f(x)=8x^3-4x^2+2x+1}，求 {f(x)} 除以 {(2x-1)} 的餘式。', [LINES(5)]),

    HD(f'三、練習C（{star_label(3)}）—— 挑戰題'),
    Q(7, '{f(x)} 除以 {(x-1)} 的餘式為 5，除以 {(x-4)} 的餘式為 2。'
         '求 {f(x)} 除以 {(x-1)(x-4)} 的餘式。', [LINES(6)]),
    Q(8, '設 {f(x)=x^3+ax^2+bx+4} 有因式 {(x+1)} 及 {(x-2)}，求 {a+b} 的值。', [LINES(6)]),

    HD('教師用參考答案', brk=True),
    ANS('1．', [P_('令 {x-3=0}，代入 {x=3}：{f(3)=9-12+1}'), P_('∴ 餘式為 {-2}')]),
    ANS('2．', [P_('令 {x+2=0}，代入 {x=-2}：{f(-2)=-8+4+3}'), P_('∴ 餘式為 {-1}')]),
    ANS('3．', [P_('令 {x+1=0}，代入 {x=-1}：{f(-1)=-1+2+1+4}'), P_('∴ 餘式為 {6}')]),
    ANS('4．', [P_('{f(3)=0}：{9+3k+9=0}，即 {3k=-18}'), P_('∴ {k=-6}（回代：{x^2-6x+9=(x-3)^2} ✓）')]),
    ANS('5．', [P_('{f(-2)=0}：{4+10+a=0}'), P_('∴ {a=-14}（回代：{x^2-5x-14=(x+2)(x-7)} ✓）')]),
    ANS('6．', [P_('令 {2x-1=0}，代入 {x=frac(1,2)}：{f(frac(1,2))=1-1+1+1}'),
               P_('∴ 餘式為 {2}（綜合除法 {c=frac(1,2)} 核對：最後一格也是 2 ✓）')]),
    ANS('7．', [P_('除式是二次，餘式最多一次，設餘式為 {ax+b}。'),
               P_('{f(1)=5}：{a+b=5}　①；{f(4)=2}：{4a+b=2}　②'),
               P_('② − ①：{3a=-3}，{a=-1}；代回 ①：{b=6}'),
               P_('∴ 餘式為 {-x+6}')]),
    ANS('8．', [P_('{f(-1)=0}：{-1+a-b+4=0}，即 {a-b=-3}　①'),
               P_('{f(2)=0}：{8+4a+2b+4=0}，即 {2a+b=-6}　②'),
               P_('① ＋ ②：{3a=-9}，{a=-3}；代回 ①：{b=0}'),
               P_('∴ {a+b=-3}')]),
])

# ================================================================ 3 講義：牛頓定理與多項式基本定理
UNIT3 = '牛頓定理與多項式基本定理'
FOOT3 = '高一數學．牛頓定理與多項式基本定理'
HANDOUT3 = dict(file='講義_牛頓定理與多項式基本定理_融合版', unit=UNIT3, type='課堂講義', foot=FOOT3, body=[
    HD('一、牛頓定理：去哪裡找一次因式'),
    P_('要因式分解一個三次或以上的多項式，第一步是先找到「一個」一次因式。'
       '牛頓定理告訴我們候選因式只有幾個，不用整條數線亂猜。'),
    REF('牛頓定理（整係數一次因式檢驗法）', '要因式分解三次或以上的多項式，又找不到公因式', [
        P_('設 {f(x)} 是整係數多項式。若 {(ax-b)} 是 {f(x)} 的一次因式（{a}、{b} 互質），則：'),
        FML('{a} 整除 最高次項係數　　　{b} 整除 常數項'),
        P_('口訣：a 除首項，b 除常數項。'),
    ]),
    CARD_NEW,

    HD('二、範例一', brk=True),
    P_('★ 範例一：求 {f(x)=x^3-2x^2-5x+6} 的所有整係數一次因式。', bold=True, keep=True),
    WK([SP('最高次項係數 1 的因數：{±1}', '第 1 步：{a} 只有 1'),
        SP('常數項 6 的因數：{±1}，{±2}，{±3}，{±6}', '第 2 步：正負都要列'),
        SP('候選：{(x-1)}，{(x+1)}，{(x-2)}，{(x+2)}，{(x-3)}，{(x+3)}，{(x-6)}，{(x+6)}', '第 3 步：共 8 個')],
       why_pct=0.30),
    P_('第 4 步：逐個代入。', keep=True),
    TBL(('代入 {x=}', '逐項計算 {f(x)}', '得', '結論'), [
        ('{1}', '{1-2-5+6}', '{0}', '是因式：{(x-1)}'),
        ('{-1}', '{-1-2+5+6}', '{8}', '不是'),
        ('{2}', '{8-8-10+6}', '{-4}', '不是'),
        ('{-2}', '{-8-8+10+6}', '{0}', '是因式：{(x+2)}'),
        ('{3}', '{27-18-15+6}', '{0}', '是因式：{(x-3)}'),
    ], fr=(0.14, 0.36, 0.12, 0.38)),
    SH('三次多項式最多只有 3 個一次因式，已經找到 3 個，後面的不用再試。'),
    WK([AN('{f(x)} 的整係數一次因式為 {(x-1)}，{(x+2)}，{(x-3)}')], why_pct=0.30),

    P_('★ 更快的做法：找到第一個因式後，用綜合除法降次。', bold=True, keep=True),
    FIGN(SYN([1, -2, -5, 6], 1), [
        '① {f(1)=0}，所以用 {c=1} 做綜合除法',
        '② 餘式是 0，再次確認 {(x-1)} 是因式',
        '③ 商式 {x^2-x-6} 只剩二次，可以直接因式分解',
        '④ {x^2-x-6=(x+2)(x-3)}',
    ], title='找到一個，就降一次'),
    WK([AN('{f(x)=(x-1)(x+2)(x-3)}')], why_pct=0.30),

    HD('三、多項式基本定理', brk=True),
    REF('多項式基本定理', '題目給出幾個令 {f(x)=0} 的 x（零點），要你寫出 {f(x)}', [
        P_('定理一：若 n 次多項式 {f(x)} 有 n 個不同的數 {b_1}，{b_2}，…，{b_n} 使 {f(x)=0}，則'),
        FML('{f(x)=a_0(x-b_1)(x-b_2)⋯(x-b_n)}'),
        P_('定理二：若 n 次多項式對 n ＋ 1 個不同的數都等於 0，則 {f(x)} 每一項的係數都是 0。'),
        P_('白話：知道所有零點，就寫得出多項式的樣子（只差前面一個倍數 {a_0}）。'),
    ]),
    CARD_FUN,

    HD('四、範例二'),
    P_('★ 範例二：二次多項式 {f(x)} 滿足 {f(1)=0}，{f(4)=0}，且 {f(2)=-6}。求 {f(x)}。',
       bold=True, keep=True),
    WK([EQ('{f(x)}', '{a(x-1)(x-4)}', '第 1 步：零點 1、4 各寫一個括號'),
        EQ('{f(2)}', '{a(2-1)(2-4)}', '第 2 步：代入 {x=2}'),
        EQ('{-6}', '{a(1)(-2)}', '第 3 步：先算括號'),
        EQ('{-6}', '{-2a}', ''),
        EQ('{a}', '{3}', '兩邊除以 {-2}'),
        EQ('{f(x)}', '{3(x-1)(x-4)}', '第 4 步：把 {a} 代回'),
        EQ('{f(x)}', '{3x^2-15x+12}', '展開'),
        AN('{f(x)=3x^2-15x+12}')]),

    P_('接下來請拿《牛頓定理與多項式基本定理 —— 課堂練習》，依這兩張手順卡完成練習 A、B、C。'),
], notes=dict(
    main='D2 手順卡（找一次因式四步、已知零點寫多項式四步）',
    aux=('D7 提示卡（牛頓定理、多項式基本定理）',),
    reason='本課屬 S2 多步驟程序運算：列因數 → 組合候選 → 逐個代入，候選一多就漏負數、漏分數。'
           '主設計取 D2，並把「逐個代入」改成決策表（每列一個候選、一條算式、一個結論），'
           '避免一段長句塞五條算式。兩條定理以 D7 提示卡框出；範例一後接上一份的綜合除法降次，'
           '讓三份講義的除法版面前後一致。',
    fading='本份練習紙面已做三級：練習A 每題重印四步 → 練習B 只在區塊開頭放一次提示 → 練習C 不放。'
           '之後只留口訣「a 除首項，b 除常數項」→ 移除。',
    flows=FLOWS, iep=IEP,
    extra=[('正規教學目標（本單元對應）',
            'A—2—3 瞭解多項式的基本定理（定理一、定理二）；A—2—6 體會多項式知識在求方程的根中的應用'
            '（練習 C5 求根）。牛頓定理（整係數一次因式檢驗法）本身屬基力以外：校本，服務 A—2—6。'),
           ('與教學簡報的對應',
            '簡報_L5_牛頓定理（例題＝本份範例一）、簡報_L6_多項式基本定理（例題＝本份範例二）。'
            '兩張手順卡的四步與簡報兩個「四步走」一致。')]))

EXERCISE3 = dict(file='練習_牛頓定理與多項式基本定理_融合版', unit=UNIT3, type='課堂練習', foot=FOOT3, body=[
    P_('忘記做法就先回頭看《牛頓定理與多項式基本定理 —— 課堂講義》的兩張手順卡。'),
    HD(f'一、練習A（{star_label(1)}）'),
    Q(1, '求 {f(x)=x^3-4x^2+x+6} 的所有整係數一次因式。', [LINES(6)],
      HINT_NEW + ['（首項係數是 1，只要試常數項 6 的因數）'], '找一次因式四步'),
    Q(2, '二次多項式 {f(x)} 滿足 {f(0)=0}，{f(-5)=0}，且 {f(1)=9}。求 {f(x)}。', [LINES(5)],
      HINT_FUN, '已知零點四步'),

    HD(f'二、練習B（{star_label(2)}）', brk=True),
    SH('找一次因式：{a} 除首項，{b} 除常數項，首項不是 1 要試分數。已知零點：先寫樣子，再代點求 {a}。'),
    Q(3, '求 {f(x)=2x^4+x^3-x^2+8x-4} 的所有整係數一次因式。', [LINES(7)]),
    Q(4, '三次多項式 {f(x)} 滿足 {f(1)=f(-2)=f(3)=0}，且 {f(0)=12}。求 {f(x)}。', [LINES(5)]),

    HD(f'三、練習C（{star_label(3)}）—— 挑戰題'),
    Q(5, '求 {f(x)=x^4-x^3-7x^2+x+6} 的所有整係數一次因式，並求方程 {f(x)=0} 的所有根。', [LINES(7)]),
    Q(6, '三次多項式 {g(x)} 滿足 {g(1)=g(2)=g(3)=5}，且 {g(4)=11}。求 {g(x)}。', [LINES(7)]),

    HD('教師用參考答案', brk=True),
    ANS('1．', [P_('候選 {x=±1}，{±2}，{±3}，{±6}：{f(-1)=0}，{f(2)=0}，{f(3)=0}'),
               P_('∴ 整係數一次因式為 {(x+1)}，{(x-2)}，{(x-3)}')]),
    ANS('2．', [P_('{f(x)=ax(x+5)}；代入 {f(1)=9}：{6a=9}，{a=frac(3,2)}'),
               P_('∴ {f(x)=frac(3,2)x^2+frac(15,2)x}')]),
    ANS('3．', [P_('{a} 可為 1，2；{b} 可為 {±1}，{±2}，{±4}：{f(-2)=0}，{f(frac(1,2))=0}'),
               P_('降次：{f(x)=(x+2)(2x-1)(x^2-x+2)}，而 {x^2-x+2} 的判別式 {Δ=-7}，沒有實數根'),
               P_('∴ 整係數一次因式為 {(x+2)}，{(2x-1)}')]),
    ANS('4．', [P_('{f(x)=a(x-1)(x+2)(x-3)}；代入 {f(0)=12}：{a(-1)(2)(-3)=12}，{6a=12}，{a=2}'),
               P_('∴ {f(x)=2x^3-4x^2-10x+12}')]),
    ANS('5．', [P_('{f(1)=0}，{f(-1)=0}，{f(-2)=0}，{f(3)=0}；四次多項式最多 4 個一次因式，找夠即停'),
               P_('∴ 整係數一次因式為 {(x-1)}，{(x+1)}，{(x+2)}，{(x-3)}'),
               P_('　 方程 {f(x)=0} 的根為 1，{-1}，{-2}，3')]),
    ANS('6．', [P_('設 {h(x)=g(x)-5}，則 1，2，3 都是 {h(x)} 的零點，所以 {h(x)=a(x-1)(x-2)(x-3)}'),
               P_('{h(4)=11-5}，所以 {a(3)(2)(1)=6}，{a=1}'),
               P_('{g(x)=(x-1)(x-2)(x-3)+5}'),
               P_('∴ {g(x)=x^3-6x^2+11x-1}')]),
])

DOCS = [HANDOUT1, EXERCISE1, HANDOUT2, EXERCISE2, HANDOUT3, EXERCISE3]

if __name__ == '__main__':
    only = sys.argv[1:]
    for d in DOCS:
        if only and not any(o in d['file'] for o in only):
            continue
        print(build_docx_file(d))
        print(build_html_file(d))
