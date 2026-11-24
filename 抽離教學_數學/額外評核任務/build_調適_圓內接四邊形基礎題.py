# -*- coding: utf-8 -*-
r"""
build_調適_圓內接四邊形基礎題.py — 初三〈圓內接四邊形 基礎題〉調適版（投影講解用，2026-11-24）

使用者：原卷《初三圓內接四邊形基礎題.pdf》（10 題，同資料夾）太難；出一份調適，
不用留作答空間，只投影給學生講解。

調適做法：
- 一題一頁，頁面改成 16:9 簡報尺寸（25.4 × 14.29 cm），字級 ×5/4（本文 15pt）：全頁投影時
  15pt ≈ 簡報 20pt（記憶 classroom_projection_min_font：抽離小組 22pt 即可）。
- 每題重畫準確示意圖（circ()，點位按題目度數計算），步驟用 worked_example_table
  （等號對齊、右欄寫理由）；學生版把關鍵數值留「＿＿」給老師講解時口頭提問，
  教師答案版同一頁面全部填好。
- 剔除：原 1（要用垂徑定理＋外心，丙班沒教垂徑、外心屬單元 09）；原 4(1) 證明。
- 證明題 3(1)／8(1) 改成第 6 題「發現外角＝內對角」填空推導（講義沒有這條，
  但原 3(2)、7、8(2) 都要用）。原 4(2) 把 (1) 的結論當已知，作挑戰題。
- 題序由易到難重排；教師答案版末頁附「調適版 ↔ 原卷」對照。
教學設計：沿用單元 08 修訂版 主 D7 提示卡＋輔 D2 手順卡（步驟表）。
逐題驗算見《驗算_圓內接四邊形基礎題調適.md》；--verify 以座標重算。
"""
import io
import math
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '初三數學', '融合班講義練習',
                                                  '08_圓的有關性質', '新修訂')))
import circle_common as cc  # noqa: E402
from circle_common import circ  # noqa: E402
import omml_docx as od  # noqa: E402
from omml_docx import (para, heading, masthead, build_docx, shaded_multi_box, eq_row, span_row,  # noqa: E402
                       answer_row, worked_example_table, aside_layout, MediaRegistry, _tbl)

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

cc.FIG = os.path.join(HERE, '_tmp_fig_調適')
os.makedirs(cc.FIG, exist_ok=True)

BASE = '調適練習_初三數學_圓內接四邊形基礎題'
SUBJ = '初三數學'
UNIT = '圓內接四邊形基礎題（調適・投影講解）'
FOOT = '初三數學．圓內接四邊形基礎題（調適）'
# 頁面＝標準 16:9 簡報尺寸 25.4 × 14.29 cm（14400 × 8100 twips，邊界 284）。
# 第一版用 21 × 11.81 cm，一題放不進一頁（34 頁、表格被截），改大頁＋左右兩欄。
PAGE_W, PAGE_H = 14400, 8100
od._PAGE_CONTENT_WIDTH = PAGE_W - 568     # 共用建構器讀模組常數定表寬
W = od._PAGE_CONTENT_WIDTH
MAIN_PCT = 0.38   # 左欄：題目＋圖＋提示；右欄：步驟表
B = '＿＿'


# ============================ 幾何（單位圓，度數 0° 在右、逆時針） ============================
def P(deg):
    a = math.radians(deg)
    return (math.cos(a), math.sin(a))


def meet(p1, p2, p3, p4):
    """直線 p1p2 與 p3p4 的交點。"""
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def ext(a, b, t):
    """由 a 經 b 延長，超出 b 的長度＝ t × ab。"""
    return (b[0] + t * (b[0] - a[0]), b[1] + t * (b[1] - a[1]))


DEG = {   # 各題點位（度數）；推導見驗算檔
    1: {'A': 90, 'B': 210, 'C': 330, 'D': 270},
    2: {'A': 90, 'B': 210, 'C': 330, 'D': 50},   # D 不可在 30°：弧 CA 的等弧記號正好壓在 D 上
    3: {'A': 180, 'B': 0, 'C': 75, 'D': 140},
    4: {'A': 180, 'B': 0, 'C': 80, 'D': 160},
    5: {'A': 130, 'B': 240, 'C': 300, 'D': 90},  # A 不可在 160°：弧 DB 的等弧記號在 165°
    6: {'A': 0, 'B': 40, 'C': 100, 'D': 200},
    7: {'A': 0, 'B': 40, 'C': 100, 'D': 200},
    8: {'A': 70, 'B': 250, 'C': 290, 'D': 330},
    9: {'A': 210, 'B': 310, 'C': 0, 'D': 80},
    10: {'A': 200, 'B': 340, 'C': 20, 'D': 80},
}


def coords(n):
    c = {k: P(v) for k, v in DEG[n].items()}
    c['O'] = (0.0, 0.0)
    if n in (6, 7):
        c['G'] = ext(c['D'], c['C'], 0.42)
    if n == 8:
        c['E'] = meet(c['A'], c['D'], c['B'], c['C'])
    if n == 9:
        c['E'] = ext(c['B'], c['C'], 0.55)
    if n == 10:
        c['E'] = meet(c['A'], c['D'], c['B'], c['C'])
        c['F'] = meet(c['A'], c['B'], c['D'], c['C'])
    return c


def xy(pt, off=(12, -10)):
    return ('xy', pt[0], pt[1], off)


def fig_svg(n):
    d = {k: (v, 1.1) for k, v in DEG[n].items()}
    c = coords(n)
    if n == 1:
        return circ(d, segs=[('A', 'B'), ('A', 'C'), ('B', 'D'), ('D', 'C'), ('O', 'B'), ('O', 'C')],
                    angles=[('D', 'B', 'C', '120°', 18)], olab=(-4, -12))
    if n == 2:
        return circ(d, segs=[('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D'), ('D', 'C')],
                    arcs=[('A', 'B', {'w': 1.8, 'tick': 1}), ('C', 'A', {'w': 1.8, 'tick': 1})],
                    angles=[('C', 'A', 'B', '60°', 22)], olab=(8, 15))
    if n in (3, 4):
        return circ(d, segs=[('A', 'B'), ('A', 'D'), ('D', 'C'), ('C', 'B'), ('D', 'B')],
                    angles=[('C', 'B', 'D', '110°' if n == 3 else '100°', 16)], olab=(-4, 18))
    if n == 5:
        return circ(d, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('B', 'D')],
                    arcs=[('C', 'D', {'w': 1.8, 'tick': 1}), ('D', 'B', {'w': 1.8, 'tick': 1})],
                    angles=[('A', 'B', 'D', '105°', 18)], olab=(10, 4))
    if n == 6:
        d['G'] = xy(c['G'], (10, -10))
        return circ(d, segs=[('A', 'B'), ('B', 'C'), ('D', 'G'), ('D', 'A')],
                    angles=[('A', 'B', 'D', '', 18), ('C', 'G', 'B', '', 16)], olab=(-18, -8),
                    r=95, size=(300, 340))   # G 在圓外上方，畫布要加高，否則被截
    if n == 7:
        d['G'] = xy(c['G'], (10, -10))
        return circ(d, segs=[('A', 'B'), ('B', 'C'), ('D', 'G'), ('D', 'A'), ('A', 'C'), ('B', 'D')],
                    angles=[('B', 'D', 'A', '80°', 26), ('D', 'C', 'A', '50°', 34)], olab=(-18, -8),
                    r=95, size=(300, 340))
    if n == 8:
        d['E'] = xy(c['E'], (14, 6))
        return circ(d, segs=[('A', 'B'), ('B', 'E'), ('A', 'E'), ('C', 'D')],
                    angles=[('A', 'B', 'E', '40°', 34)], olab=(-16, 4))
    if n == 9:
        d['E'] = xy(c['E'], (12, -6))
        return circ(d, segs=[('A', 'B'), ('B', 'E'), ('C', 'D'), ('D', 'A'), ('A', 'C'), ('B', 'D')],
                    angles=[('A', 'B', 'D', '65°', 26)], olab=(-4, 18))
    if n == 10:
        d['E'] = xy(c['E'], (12, -6))
        d['F'] = xy(c['F'], (10, 14))
        return circ(d, segs=[('A', 'E'), ('B', 'E'), ('A', 'F'), ('D', 'F')],
                    angles=[('E', 'A', 'B', '40°', 22), ('F', 'A', 'D', '40°', 26)], olab=(-14, 4),
                    r=80, size=(360, 360))   # E 在 1.9r 高、F 在 1.75r 右
    raise KeyError(n)


# ============================ 題目＋步驟 ============================
# 每列：(lhs, 完整右式, 理由, 學生版右式)；學生版右式 None＝照印完整右式。
# 'span' 列：('span', 文字, 理由, 學生版文字)。最後一列一律是 ∴ 答句（學生版留空）。
ITEMS = [
    dict(n=1, title='第 1 題', src='原 10',
         q='如圖，點 A、B、C、D 在 {⊙O} 上，{∠BDC=120°}。求 {∠BOC}。',
         tip='先找 {∠BDC} 的對角，再想它和 {∠BOC} 對著哪一條弧。',
         rows=[('{∠A}', '{180°-∠BDC}', '四邊形 ABDC 內接於 {⊙O}，對角互補', None),
               ('{∠A}', '{180°-120°}', '代入', None),
               ('{∠A}', '{60°}', '', B),
               ('{∠BOC}', '{2∠A}', '同弧 BC：圓心角是圓周角的 2 倍', None),
               ('{∠BOC}', '{120°}', '', B)],
         ans='{∠BOC=120°}'),
    dict(n=2, title='第 2 題', src='原 9',
         q='如圖，四邊形 ABCD 內接於 {⊙O}，{arc(AB)=arc(AC)}，{∠ACB=60°}。求 {∠D}。',
         tip='等弧 → 等弦 → 等腰三角形。',
         rows=[('span', 'AB ＝ AC', '在同圓中，等弧所對的弦相等', None),
               ('{∠ABC}', '{∠ACB}', 'AB ＝ AC，等邊對等角', None),
               ('{∠ABC}', '{60°}', '', B),
               ('{∠D}', '{180°-∠ABC}', '圓內接四邊形對角互補', None),
               ('{∠D}', '{120°}', '', B)],
         ans='{∠D=120°}'),
    dict(n=3, title='第 3 題', src='原 5',
         q='如圖，四邊形 ABCD 內接於 {⊙O}，AB 是 {⊙O} 的直徑，{∠BCD=110°}。求 {∠ABD}。',
         tip='兩個工具：對角互補；直徑所對的圓周角是 {90°}。',
         rows=[('{∠A}', '{180°-∠BCD}', '圓內接四邊形對角互補', None),
               ('{∠A}', '{70°}', '', B),
               ('{∠ADB}', '{90°}', '直徑所對的圓周角是直角', B),
               ('{∠ABD}', '{180°-90°-70°}', '{△ABD} 內角和', '{180°-}＿＿{-}＿＿'),
               ('{∠ABD}', '{20°}', '', B)],
         ans='{∠ABD=20°}'),
    dict(n=4, title='第 4 題（到你了）', src='原 6',
         q='如圖，四邊形 ABCD 內接於 {⊙O}，AB 是 {⊙O} 的直徑，{∠BCD=100°}。求 {∠ABD}。',
         tip='和第 3 題一樣的三步，只是數字不同。',
         rows=[('{∠A}', '{180°-100°}', '圓內接四邊形對角互補', B),
               ('{∠A}', '{80°}', '', B),
               ('{∠ADB}', '{90°}', '直徑所對的圓周角是直角', B),
               ('{∠ABD}', '{180°-90°-80°}', '{△ABD} 內角和', B),
               ('{∠ABD}', '{10°}', '', B)],
         ans='{∠ABD=10°}'),
    dict(n=5, title='第 5 題', src='原 2',
         q='如圖，四邊形 ABCD 內接於 {⊙O}，連接 BD，{∠BAD=105°}，{arc(BD)=arc(DC)}。求 {∠BDC}。',
         tip='先求 {∠BCD}；再看 {△BDC} 是甚麼三角形。',
         rows=[('{∠BCD}', '{180°-105°}', '圓內接四邊形對角互補', None),
               ('{∠BCD}', '{75°}', '', B),
               ('span', 'BD ＝ DC，所以 {∠DBC=∠BCD=75°}', '等弧對等弦；等邊對等角', 'BD ＝ DC，所以 {∠DBC=∠BCD=}＿＿'),
               ('{∠BDC}', '{180°-75°-75°}', '{△BDC} 內角和', None),
               ('{∠BDC}', '{30°}', '', B)],
         ans='{∠BDC=30°}'),
    dict(n=6, title='第 6 題（新工具）', src='原 3(1)、8(1)',
         q='如圖，四邊形 ABCD 內接於 {⊙O}，點 G 在 DC 的延長線上。說明為甚麼 {∠BAD=∠GCB}。',
         tip='兩個角都和 {∠BCD} 湊成 {180°}。',
         rows=[('{∠BAD+∠BCD}', '{180°}', '圓內接四邊形對角互補', B),
               ('{∠GCB+∠BCD}', '{180°}', 'D、C、G 在同一直線上（平角）', B),
               ('span', '兩條式都是「＋ {∠BCD} ＝ {180°}」', '', None)],
         ans='{∠BAD=∠GCB}',
         ans_why='圓內接四邊形的外角＝內對角'),
    dict(n=7, title='第 7 題', src='原 3(2)',
         q='同上圖，連接 AC、BD。若 {∠DBA=80°}，{∠CDA=50°}，求 {∠CAD}。',
         tip='{∠DBA} 和 {∠DCA} 對著同一條弧 AD。',
         rows=[('{∠DCA}', '{∠DBA}', '同弧 AD 所對的圓周角相等', None),
               ('{∠DCA}', '{80°}', '', B),
               ('{∠CAD}', '{180°-80°-50°}', '{△ACD} 內角和', '{180°-}＿＿{-50°}'),
               ('{∠CAD}', '{50°}', '', B)],
         ans='{∠CAD=50°}'),
    dict(n=8, title='第 8 題', src='原 7',
         q='如圖，四邊形 ABCD 內接於 {⊙O}，延長 AD、BC 交於點 E，且 CE ＝ CD。已知 {∠BAE=40°}，求 {∠CDE}。',
         tip='設 {∠CDE=x}。用第 6 題的新工具，再用等腰三角形。',
         rows=[('{∠ABC}', '{x}', '外角＝內對角（{∠CDE} 的內對角是 {∠ABC}）', B),
               ('{∠E}', '{x}', 'CE ＝ CD，等邊對等角', B),
               ('{40°+x+x}', '{180°}', '{△ABE} 內角和', None),
               ('{2x}', '{140°}', '', B),
               ('{x}', '{70°}', '', B)],
         ans='{∠CDE=70°}'),
    dict(n=9, title='第 9 題', src='原 8(2)',
         q='如圖，四邊形 ABCD 內接於圓，延長 BC 到點 E，連接 AC、BD。若 {∠DAB=65°}，CD 平分 {∠ACE}，求 {∠ADB}。',
         tip='外角＝內對角 → 平分 → 平角 → 同弧。',
         rows=[('{∠DCE}', '{65°}', '外角＝內對角', B),
               ('{∠ACE}', '{130°}', 'CD 平分 {∠ACE}', B),
               ('{∠ACB}', '{180°-130°}', 'B、C、E 共線（平角）', '{180°-}＿＿'),
               ('{∠ACB}', '{50°}', '', B),
               ('{∠ADB}', '{50°}', '同弧 AB，圓周角相等', B)],
         ans='{∠ADB=50°}'),
    dict(n=10, title='第 10 題（挑戰）', src='原 4(2)',
         q='如圖，{⊙O} 的內接四邊形 ABCD 兩組對邊的延長線分別交於點 E、F，{∠E=∠F=40°}。'
           '這時 {∠ADC=∠ABC}（不用證明）。求 {∠A}。',
         tip='{∠ADC} 和 {∠ABC} 是對角，又相等，各是多少度？',
         rows=[('{∠ADC+∠ABC}', '{180°}', '圓內接四邊形對角互補', None),
               ('{∠ABC}', '{90°}', '兩角相等，各佔一半', B),
               ('{∠A}', '{180°-90°-40°}', '{△ABE} 內角和', '{180°-}＿＿{-40°}'),
               ('{∠A}', '{50°}', '', B)],
         ans='{∠A=50°}'),
]

TOOLS = [
    '① 圓內接四邊形的對角互補（相加 {180°}）',
    '② 同弧所對的圓周角相等',
    '③ 圓周角 ＝ {frac(1,2)} × 同弧所對的圓心角',
    '④ 直徑所對的圓周角是 {90°}',
    '⑤ 在同圓中，等弧所對的弦相等',
    '⑥ 三角形內角和 {180°}；等腰三角形兩底角相等',
    '★ 第 6 題會發現：圓內接四邊形的外角 ＝ 內對角',
]


def steps_table(it, teacher):
    rows = []
    for r in it['rows']:
        if r[0] == 'span':
            txt = r[1] if teacher or r[3] is None else r[3]
            rows.append(span_row(txt, r[2] or None))
        else:
            lhs, rhs, why, blank = r
            rows.append(eq_row(lhs, rhs if teacher or blank is None else blank, why or None))
    rows.append(answer_row(it['ans'] if teacher else '', why=it.get('ans_why', '')))
    tw = int(W * (1 - MAIN_PCT)) - 230
    old = od._PAGE_CONTENT_WIDTH
    od._PAGE_CONTENT_WIDTH = tw          # worked_example_table 以模組常數定寬度：暫借主欄寬
    try:
        x = worked_example_table(rows, headers=('算式', '理由'), why_pct=0.40,
                                 col_frac=(0.42, 0.06, 0.22, 0.06, 0.12, 0.06))
    finally:
        od._PAGE_CONTENT_WIDTH = old
    return x


NEWPAGE = ('<w:p><w:pPr><w:pageBreakBefore/><w:spacing w:before="0" w:after="0" w:line="20" '
           'w:lineRule="exact"/></w:pPr></w:p>')
TINY = ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="40" w:lineRule="exact"/></w:pPr></w:p>')


def page(M, it, teacher):
    # 標題不用 heading()：它會被 keepNext 留在上一頁獨佔一頁（第二版實測）。改成左欄第一行，
    # 並在這一段加 pageBreakBefore（獨立的換頁段落會令 cantSplit 表格再被推多一頁，第三版實測）。
    title = para(it['title'], bold=True, sz=26, spacing=False).replace('<w:pPr>', '<w:pPr><w:pageBreakBefore/>', 1)
    out = []
    left = [title, para(it['q'], spacing=False), cc.fig(fig_svg(it['n']), f"q{it['n']}", 4.5),
            para('提示：' + it['tip'], sz=21, spacing=False, shd=od.GREY_FILL)]
    right = [steps_table(it, teacher), TINY]
    x = aside_layout(left, right, main_pct=MAIN_PCT, media=M)
    if x.endswith(od.blank()):       # 表後 1.5 行高的空段會被擠到下一頁成空白頁
        x = x[:-len(od.blank())] + TINY
    out.append(x)
    return out


def build(teacher):
    M = MediaRegistry()
    kind = '調適練習・教師答案版' if teacher else '調適練習・投影講解'
    P_ = [masthead(SUBJ, UNIT, kind),
          heading('今天用到的工具'),
          shaded_multi_box([para(t, spacing=False) for t in TOOLS], trailing_blank=False),
          para('看圖 → 想「這兩個角有甚麼關係？」→ 選工具 → 寫算式和理由。', bold=True)]
    for it in ITEMS:
        P_ += page(M, it, teacher)
    if teacher:
        P_.append(heading('教師參考：調適版與原卷對照', page_break_before=True))
        ws = [int(W * f) for f in (0.14, 0.16, 0.30)]
        ws.append(W - sum(ws))
        rows = [{'hdr': True, 'cells': [{'p': [para(h, bold=True, spacing=False, sz=21)], 'shd': od.GREY_FILL}
                                        for h in ('調適版', '原卷', '答案', '怎樣調')]}]
        notes = {1: '先給「找對角」的方向', 2: '補一步「等弧→等弦」', 3: '示範三步', 4: '同型練習，全部留空',
                 5: '拆成先求 {∠BCD}', 6: '證明題改填空推導，帶出新工具', 7: '只做 (2)，(1) 已在第 6 題',
                 8: '設 x，列一條方程', 9: '四個工具串連，逐步列出', 10: '(1) 的結論作已知，只做 (2)'}
        for it in ITEMS:
            rows.append([{'p': [para(f"第 {it['n']} 題", sz=21, spacing=False)]},
                         {'p': [para(it['src'], sz=21, spacing=False)]},
                         {'p': [para(it['ans'], sz=21, spacing=False)]},
                         {'p': [para(notes[it['n']], sz=21, spacing=False)]}])
        rows.append([{'p': [para('—', sz=21, spacing=False)]},
                     {'p': [para('原 1、原 4(1)', sz=21, spacing=False)]},
                     {'p': [para('剔除', sz=21, spacing=False)]},
                     {'p': [para('原 1 要用垂徑定理＋外心（丙班未教垂徑定理）；原 4(1) 證明題', sz=21, spacing=False)]}])
        P_.append(_tbl(rows, ws, trailing_blank=False))
    name = f"{BASE}_{'教師答案版' if teacher else '學生版'}.docx"
    path = os.path.join(HERE, name)
    build_docx(P_, path, footer_text=FOOT + ('（教師答案版）' if teacher else '（投影版）'), media=M)
    to_projection(path)
    print('OK', name)


_PPR = re.compile(r'<w:pPr>((?:(?!</w:pPr>).)*?)</w:pPr>', re.S)


def zero_spacing(xml):
    """沒有寫 <w:spacing> 的段落會繼承 Word Normal 的段後 8pt（記憶 docx_spacing_false_is_not_zero），
    步驟表每列因此高一倍、一題撐出一頁。補上零段距；schema 次序 spacing 在 ind／jc／rPr 之前。"""
    def fix(m):
        inner = m.group(1)
        if '<w:spacing' in inner:
            return m.group(0)
        sp = '<w:spacing w:before="0" w:after="0" w:line="264" w:lineRule="auto"/>'
        for tag in ('<w:ind', '<w:jc', '<w:rPr'):
            i = inner.find(tag)
            if i >= 0:
                return f'<w:pPr>{inner[:i]}{sp}{inner[i:]}</w:pPr>'
        return f'<w:pPr>{inner}{sp}</w:pPr>'
    return _PPR.sub(fix, xml)


def to_projection(path):
    """16:9 頁面＋字級 ×5/4（12pt → 15pt；4/3 時表後段落擠出空白頁）。build_docx 寫死 A4，這裡改封裝後的 document.xml／footer。"""
    tmp = path + '._tmp'
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename in ('word/document.xml', 'word/styles.xml'):
                s = data.decode('utf-8')
                s = s.replace('<w:pgSz w:w="11906" w:h="16838"/>', f'<w:pgSz w:w="{PAGE_W}" w:h="{PAGE_H}"/>')
                s = s.replace('w:bottom="284"', 'w:bottom="600"').replace('w:footer="142"', 'w:footer="200"')
                if item.filename == 'word/document.xml':
                    s = zero_spacing(s)
                s = s.replace('w:line="360"', 'w:line="264"')   # 1.5 倍行距 → 1.1 倍，否則一題塞不進一頁
                s = re.sub(r'(<w:sz(?:Cs)? w:val=")(\d+)(")',
                           lambda m: f'{m.group(1)}{round(int(m.group(2)) * 5 / 4)}{m.group(3)}', s)
                data = s.encode('utf-8')
            zout.writestr(item, data)
    os.replace(tmp, path)


# ============================ 座標核對 ============================
def verify():
    def ang(v, a, b):
        u = (a[0] - v[0], a[1] - v[1]); w = (b[0] - v[0], b[1] - v[1])
        c = (u[0] * w[0] + u[1] * w[1]) / (math.hypot(*u) * math.hypot(*w))
        return round(math.degrees(math.acos(max(-1, min(1, c)))), 2)
    c = coords(1); print('1 ∠BDC', ang(c['D'], c['B'], c['C']), '∠A', ang(c['A'], c['B'], c['C']), '∠BOC', ang(c['O'], c['B'], c['C']))
    c = coords(2); print('2 AB', round(math.dist(c['A'], c['B']), 4), 'AC', round(math.dist(c['A'], c['C']), 4),
                         '∠ACB', ang(c['C'], c['A'], c['B']), '∠D', ang(c['D'], c['A'], c['C']))
    for n, v in ((3, 110), (4, 100)):
        c = coords(n); print(n, '∠BCD', ang(c['C'], c['B'], c['D']), '(應', v, ') ∠ADB', ang(c['D'], c['A'], c['B']),
                             '∠ABD', ang(c['B'], c['A'], c['D']))
    c = coords(5); print('5 ∠BAD', ang(c['A'], c['B'], c['D']), 'BD', round(math.dist(c['B'], c['D']), 4),
                         'DC', round(math.dist(c['D'], c['C']), 4), '∠BDC', ang(c['D'], c['B'], c['C']))
    c = coords(6); print('6 ∠BAD', ang(c['A'], c['B'], c['D']), '∠GCB', ang(c['C'], c['G'], c['B']))
    c = coords(7); print('7 ∠DBA', ang(c['B'], c['D'], c['A']), '∠CDA', ang(c['D'], c['C'], c['A']),
                         '∠CAD', ang(c['A'], c['C'], c['D']))
    c = coords(8); print('8 ∠BAE', ang(c['A'], c['B'], c['E']), 'CE', round(math.dist(c['C'], c['E']), 4),
                         'CD', round(math.dist(c['C'], c['D']), 4), '∠CDE', ang(c['D'], c['C'], c['E']),
                         '∠ABC', ang(c['B'], c['A'], c['C']), '∠E', ang(c['E'], c['A'], c['B']))
    c = coords(9); print('9 ∠DAB', ang(c['A'], c['D'], c['B']), '∠ACD', ang(c['C'], c['A'], c['D']),
                         '∠DCE', ang(c['C'], c['D'], c['E']), '∠ADB', ang(c['D'], c['A'], c['B']))
    c = coords(10); print('10 ∠E', ang(c['E'], c['A'], c['B']), '∠F', ang(c['F'], c['A'], c['D']),
                          '∠ADC', ang(c['D'], c['A'], c['C']), '∠ABC', ang(c['B'], c['A'], c['C']),
                          '∠A', ang(c['A'], c['B'], c['D']))


if __name__ == '__main__':
    if '--verify' in sys.argv:
        verify()
    else:
        build(False)
        build(True)
