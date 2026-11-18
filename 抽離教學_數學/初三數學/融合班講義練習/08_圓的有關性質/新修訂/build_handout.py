# -*- coding: utf-8 -*-
r"""
build_handout.py — 初三數學 單元 08〈圓的有關性質〉修訂版「講義」＋「練習」（2026-11-17）

修訂原因（使用者 2026-11-17）：今年教初三時發現「圓心角、弧、弦的關係」很少提到——
舊版講義（2026-08-12）四節：基本概念／垂徑定理／圓周角定理／圓內接四邊形，完全沒有這一節，
乙、丙兩班教案也沒有獨立課時。本修訂版依人教九上 24.1.3（課本 p.83–85，PDF 第 89–91 頁）
補成獨立一節（第三節），其餘四節沿用舊版範例數據，並補齊教師實施說明頁。

教學設計：主 D7 提示卡＋輔 D2 手順卡、D14 錯誤分析對比（S5 幾何定理；抽離小班）。
逐題驗算見《驗算_圓的有關性質_修訂版.md》。
用法：python build_handout.py   （產出講義、練習兩個 docx）
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circle_common import *  # noqa: E402,F401,F403
from omml_docx import MediaRegistry, expand_image, image_para, keyword_table, checkpoint_rule, _tbl  # noqa: E402,F401

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

OUT = os.path.dirname(os.path.abspath(__file__))
UNIT = '圓的有關性質（修訂版）'
NAME_H = '講義_圓的有關性質_融合版_修訂版'
NAME_P = '練習_圓的有關性質_融合版_修訂版'


# ---------------------------------------------------------------- 圖
def F_parts():
    return circ({'A': (100, 1), 'B': (190, 1.1), 'C': (10, 1.1), 'D': (238, 1), 'E': (302, 1)},
                segs=[('B', 'C'), ('O', 'A'), ('D', 'E')],
                arcs=[('D', 'E', {'w': 4.6})], olab=(-4, -14))


def F_central_inscribed():
    return circ({'C': (90, 1), 'A': (215, 1.1), 'B': (325, 1.1)},
                segs=[('C', 'A'), ('C', 'B'), ('O', 'A', {'dash': 1}), ('O', 'B', {'dash': 1})],
                arcs=[('A', 'B', {'w': 4.6})],
                angles=[('C', 'A', 'B', '', 22), ('O', 'A', 'B', '', 16)], olab=(10, -6))


def F_perp():
    return circ({'C': (90, 1), 'D': (270, 1), 'A': (208, 1.1), 'B': (-28, 1.1),
                 'M': ('xy', 0, -0.47, (13, 14))},
                segs=[('C', 'D'), ('A', 'B'), ('O', 'A', {'dash': 1})],
                right=[('M', 'O', 'B')], olab=(-18, 4))


def F_rotate(eqtick=True):
    return circ({'A': (200, 1.1), 'B': (300, 1.1), "A'": (60, 1.1), "B'": (160, 1.1)},
                segs=[('O', 'A'), ('O', 'B'), ('A', 'B', {'tick': 1}),
                      ('O', "A'"), ('O', "B'"), ("A'", "B'", {'tick': 1})],
                arcs=[('A', 'B', {'w': 4.6, 'tick': 2}), ("A'", "B'", {'w': 4.6, 'tick': 2})],
                angles=[('O', 'A', 'B', '', 16), ('O', "A'", "B'", '', 16)], olab=(10, -4))


def F_semi():
    """AB 是直徑，弧 BC＝CD＝DE，∠COD＝35°（課本 p.85 練習 2 的圖，數據相同）。"""
    return circ({'A': (180, 1.1), 'B': (0, 1.1), 'C': (35, 1), 'D': (70, 1), 'E': (105, 1)},
                segs=[('A', 'B'), ('O', 'C'), ('O', 'D'), ('O', 'E')],
                arcs=[('B', 'C', {'w': 1.8, 'tick': 1}), ('C', 'D', {'w': 1.8, 'tick': 1}),
                      ('D', 'E', {'w': 1.8, 'tick': 1})],
                olab=(-4, 18))


def F_equilateral():
    """弧 AB＝弧 AC，∠ACB＝60°（課本 p.84 例 3 的圖）。"""
    return circ({'A': (90, 1), 'B': (210, 1.1), 'C': (330, 1.1)},
                segs=[('A', 'B'), ('B', 'C'), ('C', 'A'), ('O', 'A'), ('O', 'B'), ('O', 'C')],
                olab=(9, 4))


def F_cross(full=True):
    """弦 AB、CD 相交且 AB＝CD（25-26 初三丙考試第 26 題同型；點位對稱，弧 BC＝弧 AD＝80°）。"""
    segs = [('A', 'B'), ('C', 'D')] + ([('A', 'D', {'dash': 1}), ('B', 'C', {'dash': 1})] if full else [])
    return circ({'A': (120, 1.1), 'C': (60, 1.1), 'D': (200, 1.1), 'B': (-20, 1.1)}, segs=segs,
                olab=(-4, 20))


def F_quad():
    return circ({'A': (150, 1.1), 'B': (215, 1.1), 'C': (320, 1.1), 'D': (55, 1)},
                segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')],
                angles=[('A', 'B', 'D', '', 18), ('C', 'D', 'B', '', 18)], center=True, olab=(8, 15))


def F_two_circles():
    """大圓、小圓同一個 60° 圓心角，弦不相等（D14：前提「同圓或等圓」）。"""
    import math as m
    out = []
    for cx, R, nm_ in ((80, 62, 'O'), (225, 38, 'P')):
        cy = 95
        a1, a2 = m.radians(-30), m.radians(30)
        p1 = (cx + R * m.cos(a1), cy - R * m.sin(a1))
        p2 = (cx + R * m.cos(a2), cy - R * m.sin(a2))
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#000" stroke-width="1.8"/>')
        for p in (p1, p2):
            out.append(f'<line x1="{cx}" y1="{cy}" x2="{p[0]:.1f}" y2="{p[1]:.1f}" stroke="#000" stroke-width="1.8"/>')
        out.append(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" '
                   f'stroke="#000" stroke-width="3.2"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="#000"/>')
        out.append(f'<text x="{cx - 14}" y="{cy + 5}" font-size="16" font-style="italic" '
                   f'font-family="Times New Roman">{nm_}</text>')
        out.append(f'<text x="{cx + 18}" y="{cy + 4}" font-size="13" font-family="Calibri">60°</text>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="300" height="170" viewBox="0 0 300 170">'
            '<rect width="300" height="170" fill="#fff"/>' + ''.join(out) + '</svg>')


def figrow(media, items, w=4.6):
    """並排的圖＋圖說（無框）。items: [(svg, 檔名, 圖說), ...]"""
    n = len(items)
    cells = []
    for svg, name, cap in items:
        cells.append({'p': [expand_image(fig(svg, name, w), media),
                            para(cap, sz=21, jc='center', spacing=False)]})
    return _tbl([cells], cols(n), border='none', trailing_blank=False) + GAP


def defbox(lines):
    """定理／重要結論：獨立細框，一行一句，粗體。"""
    return pbox([para(nm(x), bold=True) for x in lines])


def hint(lines):
    return shaded_multi_box([para(nm(x), spacing=False) for x in lines], trailing_blank=False) + GAP


def sol(rows, why_pct=0.42):
    return keep_together(worked_example_table(rows, why_pct=why_pct)) + GAP


def decision(rows, head=('已知（在同圓或等圓中）', '就可以推出'), inner=False):
    def cell(c):
        return [tight(para(nm(x), sz=23)) for x in c.split('｜')] if '｜' in c else c
    return grid([list(head)] + [[cell(c) for c in r] for r in rows],
                cols(2, first=int(W * 0.42)) if not inner else cols(2, total=W_IN, first=int(W_IN * 0.42)),
                inner=inner)


# ================================================================ 講義
def handout():
    M = MediaRegistry()
    P = [masthead(SUBJ, UNIT, '課堂講義'), student_info_row()]

    # ---------------- 一、基本概念
    P.append(heading('一、圓的基本概念：先認名稱'))
    P.append(figrow(M, [(F_parts(), 'h_parts', '圖 1　圓的各部分'),
                        (F_central_inscribed(), 'h_angles', '圖 2　圓心角與圓周角')]))
    P.append(grid([
        ('名稱', '意思', '圖中的例子'),
        ('圓心', '圓的中心。圓心是 O 的圓記作 {⊙O}，讀作「圓 O」', '點 O'),
        ('半徑', '連接圓心和圓上一點的線段', '圖 1：OA、OB、OC'),
        ('弦', '連接圓上任意兩點的線段', '圖 1：DE、BC'),
        ('直徑', '經過圓心的弦；直徑＝2 個半徑，是最長的弦', '圖 1：BC'),
        ('弧', '圓上任意兩點之間的部分。弧 DE 記作 {arc(DE)}', '圖 1：粗線 {arc(DE)}'),
        ('半圓、優弧、劣弧', '直徑把圓分成兩個半圓；比半圓大的弧叫優弧（用三個字母記，如 {arc(DAE)}），'
         '比半圓小的弧叫劣弧', '圖 1：{arc(DE)} 是劣弧'),
        ('等圓、等弧', '能夠重合的兩個圓叫等圓；在同圓或等圓中，能夠重合的弧叫等弧', '—'),
        ('圓心角', '頂點在圓心的角', '圖 2：{∠AOB}'),
        ('圓周角', '頂點在圓上，而且兩邊都和圓相交的角', '圖 2：{∠ACB}'),
    ], [int(W * 0.17), int(W * 0.58), W - int(W * 0.17) - int(W * 0.58)]))
    P.append(hint(['※ 半徑不是弦：弦的兩個端點都要在圓上，半徑只有一個端點在圓上。',
                   '※ 認角先看頂點：頂點在圓心＝圓心角；頂點在圓上＝圓周角。']))

    # ---------------- 二、垂徑定理
    P.append(heading('二、垂徑定理', page_break_before=True))
    P.append(aside_layout(
        [para('垂徑定理', bold=True),
         para('垂直於弦的直徑，平分這條弦，並且平分弦所對的兩條弧。', bold=True),
         para('如圖，CD 是直徑，{CD⊥AB}，垂足是 M：'),
         para(' {AM=BM}，{arc(AC)=arc(BC)}，{arc(AD)=arc(BD)}'),
         para('連接 OA，就得到直角三角形 OMA：'),
         para(' 半徑² ＝ 半弦² ＋ 圓心到弦的距離²')],
        [fig(F_perp(), 'h_perp', 5.2)], main_pct=0.60, media=M, boxed=True) + GAP)
    P.append(card('手順卡：求圓心到弦的距離', [
        ('由圓心向弦作垂線，垂足 M', '垂線會平分弦：半弦＝弦 ÷ 2'),
        ('連接半徑 OA，找出直角三角形 OMA', '斜邊是半徑，不是半弦'),
        ('用勾股定理列式', '距離² ＝ 半徑² － 半弦²'),
        ('開平方，寫答句', '長度取正數，不用分兩支'),
    ], trigger='題目有「弦長」「半徑」「圓心到弦的距離」其中兩個，求第三個時') + GAP)
    P.append(para('範例　{⊙O} 的半徑是 5，弦 AB＝8，求圓心 O 到弦 AB 的距離。', bold=True, keep_next=True))
    P.append(sol([
        span_row('半徑 {OA=5}，弦 {AB=8}', '先記下已知'),
        eq_row('{AM}', '{8÷2}', '垂徑定理：OM⊥AB，平分弦'),
        eq_row('{AM}', '{4}'),
        eq_row('{OM^2}', '{OA^2-AM^2}', '△OMA 是直角三角形，用勾股定理'),
        eq_row('{OM^2}', '{5^2-4^2}', '代入半徑和半弦'),
        eq_row('{OM^2}', '{9}', '先算平方再相減：25 − 16'),
        eq_row('{OM}', '{3}', '開平方；長度取正'),
        answer_row('圓心 O 到弦 AB 的距離是 3'),
    ]))

    # ---------------- 三、弧、弦、圓心角
    P.append(heading('三、弧、弦、圓心角的關係（本單元重點）', page_break_before=True))
    P.append(aside_layout(
        [para('想一想', bold=True),
         para('把圓繞圓心 O 轉動任意一個角度，轉完的圓和原來的圓完全重合。'),
         para('如圖，如果 {∠AOB=∠A\'OB\'}，把 {∠AOB} 連同 {arc(AB)} 一起繞 O 轉動，'
              '使 OA 落在 OA′ 上：'),
         para('　因為兩個角相等，OB 就會落在 OB′ 上；'),
         para('　又因為 {OA=OA\'}，{OB=OB\'}（都是半徑），'),
         para('　點 A 與 A′ 重合，點 B 與 B′ 重合。'),
         para('所以 {arc(AB)} 和 {arc(A\'B\')} 重合，弦 AB 和弦 A′B′ 也重合：'),
         para(' {arc(AB)=arc(A\'B\')}，{AB=A\'B\'}')],
        [fig(F_rotate(), 'h_rotate', 5.8),
         para('圖中：一條短線＝兩條弦相等；兩條短線＝兩條弧相等', sz=20)],
        main_pct=0.60, media=M, boxed=True) + GAP)
    P.append(defbox(['定理：在同圓或等圓中，相等的圓心角所對的弧相等，所對的弦也相等。',
                     '推論一：在同圓或等圓中，如果兩條弧相等，那麼它們所對的圓心角相等，所對的弦也相等。',
                     '推論二：在同圓或等圓中，如果兩條弦相等，那麼它們所對的圓心角相等，'
                     '所對的優弧和劣弧分別相等。']))
    P.append(hint(['補充：弧的度數＝它所對的圓心角的度數。例如 {∠AOB=50°}，就說 {arc(AB)} 是 {50°} 的弧；'
                   '整個圓是 {360°}，半圓是 {180°}。']))
    P.append(pbox([para('▍提示卡：知一推二', bold=True, sz=28),
                   para('什麼時候翻我：題目出現「相等的弧」「相等的弦」或「相等的圓心角」時', sz=21),
                   decision([
                       ('① 圓心角相等：{∠AOB=∠COD}', '② 弧相等：{arc(AB)=arc(CD)}｜③ 弦相等：{AB=CD}'),
                       ('② 弧相等：{arc(AB)=arc(CD)}', '① 圓心角相等：{∠AOB=∠COD}｜③ 弦相等：{AB=CD}'),
                       ('③ 弦相等：{AB=CD}', '① 圓心角相等：{∠AOB=∠COD}｜② 劣弧相等、優弧也相等'),
                   ], inner=True),
                   para('三個量 ①②③ 綁在一起：知道其中一組相等，另外兩組也相等。', sz=22)]))
    P.append(heading('常見錯誤：先看清楚再用', keep_next=True))
    P.append(contrast([
        ('兩個圓的圓心角都是 60°，所以兩條弦相等。',
         '先問：是不是同一個圓，或者兩個圓一樣大？大圓和小圓的 60° 圓心角，所對的弦不相等（見下圖）。'),
        ('{AB=CD}，所以 {arc(AB)} 等於 {arc(CD)} 的優弧。',
         '一條弦對著兩條弧（一條劣弧、一條優弧），要配對：劣弧對劣弧，優弧對優弧。'),
    ], '「在同圓或等圓中」是這組定理的前提，寫理由時不可省略。'))
    P.append(image_para(fig(F_two_circles(), 'h_two', 6.4).png_path, width_cm=6.4,
                        caption='同樣是 60° 的圓心角，大圓的弦較長'))

    P.append(heading('範例一　用等弧求角（課本練習改編）', page_break_before=True))
    P.append(aside_layout(
        [para('如圖，AB 是 {⊙O} 的直徑，{arc(BC)=arc(CD)=arc(DE)}，{∠COD=35°}，求 {∠AOE} 的度數。'),
         para('思路：等弧 → 等圓心角；直徑 → 平角 180°。', sz=22)],
        [fig(F_semi(), 'h_semi', 4.8)], main_pct=0.56, media=M, boxed=True) + GAP)
    P.append(sol([
        eq_row('{∠BOC}', '{35°}', '{arc(BC)=arc(CD)}，等弧所對的圓心角相等'),
        eq_row('{∠DOE}', '{35°}', '{arc(DE)=arc(CD)}，同一個理由'),
        eq_row('{∠AOE}', '{180°-∠BOC-∠COD-∠DOE}', 'AB 是直徑，{∠AOB} 是平角 180°'),
        eq_row('{∠AOE}', '{180°-35°-35°-35°}', '代入'),
        eq_row('{∠AOE}', '{75°}'),
        answer_row('{∠AOE=75°}'),
    ], why_pct=0.40))
    P.append(heading('範例二　用等弧證明（課本例 3）', page_break_before=True))
    P.append(aside_layout(
        [para('如圖，在 {⊙O} 中，{arc(AB)=arc(AC)}，{∠ACB=60°}。'),
         para('求證：{∠AOB=∠BOC=∠AOC}。'),
         para('思路：等弧 → 等弦 → 三角形三邊相等 → 再用「等弦對等圓心角」。', sz=22)],
        [fig(F_equilateral(), 'h_equi', 4.4)], main_pct=0.60, media=M, boxed=True) + GAP)
    P.append(sol([
        span_row('∵ {arc(AB)=arc(AC)}', '已知'),
        span_row('∴ {AB=AC}', '等弧所對的弦相等'),
        span_row('∴ △ABC 是等腰三角形', '兩邊相等'),
        span_row('又 {∠ACB=60°}', '已知'),
        span_row('∴ △ABC 是等邊三角形，{AB=BC=CA}', '有一個角是 60° 的等腰三角形是等邊三角形'),
        answer_row('{∠AOB=∠BOC=∠AOC}', '等弦所對的圓心角相等'),
    ], why_pct=0.44))

    P.append(heading('範例三　等弦 → 等弧 → 減去公共弧（考試常見證明）', page_break_before=True))
    P.append(aside_layout(
        [para('如圖，A、B、C、D 是 {⊙O} 上的四點，弦 AB、CD 相交，{AB=CD}。'),
         para('求證：{AD=BC}。'),
         para('思路：①等弦 → 等弧；②兩條弧都減去同一段 {arc(AC)}；③等弧 → 等弦。', sz=22),
         para('三個字母的弧：{arc(ACB)} 是由 A 經過 C 到 B 的弧。', sz=22)],
        [fig(F_cross(), 'h_cross', 5.0)], main_pct=0.60, media=M, boxed=True) + GAP)
    P.append(sol([
        span_row('∵ {AB=CD}', '已知'),
        span_row('∴ {arc(ACB)=arc(CAD)}', '同圓中，等弦所對的劣弧相等'),
        span_row('∴ {arc(ACB)-arc(AC)=arc(CAD)-arc(AC)}', '兩邊都減去公共的 {arc(AC)}'),
        span_row('即 {arc(BC)=arc(AD)}', ''),
        answer_row('{AD=BC}', '同圓中，等弧所對的弦相等'),
    ], why_pct=0.42))
    P.append(hint(['※ 每一步的理由都要寫「同圓中」或「在同圓或等圓中」——這是評分點。']))

    # ---------------- 四、圓周角定理
    P.append(heading('四、圓周角定理', page_break_before=True))
    P.append(aside_layout(
        [para('圓周角定理', bold=True),
         para('一條弧所對的圓周角，等於它所對的圓心角的一半。', bold=True),
         para('如圖，{arc(AB)} 所對的圓周角是 {∠ACB}，圓心角是 {∠AOB}：'),
         para(' {∠ACB=frac(1,2)∠AOB}'),
         para('認角：頂點在圓上的 ÷ 2，頂點在圓心的 × 2。', sz=22)],
        [fig(F_central_inscribed(), 'h_insc', 5.4)], main_pct=0.60, media=M, boxed=True) + GAP)
    P.append(decision([
        ('同一條弧（或相等的弧）所對的幾個圓周角', '都相等'),
        ('直徑（半圓）所對的圓周角', '是直角 {90°}'),
        ('{90°} 的圓周角所對的弦', '是直徑'),
    ], head=('看到……', '就想到……（三個推論）')))
    P.append(hint(['※ 和第三節連起來：相等的弧 → 相等的圓心角 → 相等的圓周角。']))
    P.append(para('範例　在 {⊙O} 中，{arc(AB)} 所對的圓心角 {∠AOB=100°}，求同弧所對的圓周角 {∠ACB}。',
                  bold=True, keep_next=True))
    P.append(sol([
        eq_row('{∠ACB}', '{frac(1,2)∠AOB}', '同弧所對的圓周角是圓心角的一半'),
        eq_row('{∠ACB}', '{frac(1,2)×100°}', '代入'),
        eq_row('{∠ACB}', '{50°}'),
        answer_row('{∠ACB=50°}'),
    ]))

    # ---------------- 五、圓內接四邊形
    P.append(heading('五、圓內接四邊形', keep_next=True))
    P.append(aside_layout(
        [para('四個頂點都在同一個圓上的四邊形，叫圓內接四邊形。'),
         para('圓內接四邊形的對角互補。', bold=True),
         para(' {∠A+∠C=180°}，{∠B+∠D=180°}'),
         para('※ 對角是「隔一個」的角：A 對 C，B 對 D；A 和 B 是鄰角，不互補。', sz=22)],
        [fig(F_quad(), 'h_quad', 5.8)], main_pct=0.60, media=M, boxed=True) + GAP)
    P.append(para('範例　圓內接四邊形 ABCD 中，{∠A=80°}，求 {∠C}。', bold=True, keep_next=True))
    P.append(sol([
        eq_row('{∠C}', '{180°-∠A}', '圓內接四邊形對角互補'),
        eq_row('{∠C}', '{180°-80°}', '代入'),
        eq_row('{∠C}', '{100°}'),
        answer_row('{∠C=100°}'),
    ]))
    P.append(para('接下來請拿《練習_圓的有關性質_融合版_修訂版》，用講義的提示卡和範例完成練習 A、B、C。'))

    # ---------------- 教師實施說明
    P += [tight(x, line=290, after=10) for x in teacher_notes(
        'D7 提示卡（文字＋圖＋符號三件套；第三節「知一推二」卡）',
        ('D2 手順卡（求圓心到弦的距離）', 'D14 錯誤分析對比（同圓或等圓前提、優弧劣弧配對）'),
        reason=('S5 幾何定理：瓶頸是「定理多、看圖時想不起用哪一條」。提示卡配「什麼時候翻我」；'
                '弧、弦、圓心角用 ①②③ 綁成「知一推二」決策表。D14 針對今年觀察到的漏洞：'
                '漏寫「在同圓或等圓中」、弦配錯優弧／劣弧。'),
        density='抽離小班',
        fading=('練習 A：每題右側附提示卡關鍵句（用哪條定理＋怎樣寫）；練習 B：只給一個詞提示'
                '（例如「等弧」「直徑」）；練習 C：不給提示。第二次上課起，課堂開始時請學生'
                '先默寫「知一推二」卡的三列，默寫得出就收起講義的提示卡。'),
        flows=('F1 師徒制對話四步',),
        iep_codes=('a3 提示題目重點', 'a6 增加行距／放大作答欄'),
        extra=[('本單元對應的正規教學目標',
                'B—4—1　理解圓、弧、弦、圓心角、圓周角的概念\n'
                'B—4—3　掌握垂徑定理，能利用定理證明有關的命題\n'
                'B—4—4　知道圓周角與圓心角及其所對弧的關係，瞭解並證明圓周角定理及其推論：'
                '圓周角的度數等於它所對弧上的圓心角度數的一半；直徑所對的圓周角是直角；'
                '90° 的圓周角所對的弦是直徑；圓內接四邊形的對角互補\n'
                '（第三節沒有獨立條目，屬 B—4—1＋B—4—4 的前置。）'),
               ('課本頁次', '人教九上第二十四章 24.1.1–24.1.4（課本 p.79–88）；第三節依 24.1.3（p.83–85）'),
               ('本次修訂改了什麼', '新增第三節（定理＋兩推論、知一推二卡、弧的度數、兩個常見錯誤、三個範例）；'
                '第一節補等圓、等弧、優弧、劣弧與弧的記號；第二節補手順卡。舊版範例數據不變。'),
               ('建議課時安排', '第三節放在「圓的基本概念」同一課時（只需認圖和推理，不用計算），'
                '乙班 12/10、丙班 12/09。丙班全學段沒有垂徑定理節，可略過第二節；第三節不依賴第二節。'
                '額外評核 W16 修訂版即按此安排出題。'),
               ('調整性質', '調整支援：只調整呈現方式與鷹架，核心概念與年級標準不變。')])]
    print(build_docx(P, os.path.join(OUT, NAME_H + '.docx'), footer_text=FOOT, media=M))


# ================================================================ 練習
def side_q(M, body, svg, name, n=3, hint_=None, hint_title='提示', w=4.8, pct=0.62):
    """題目在左（作答線跟住題目）、圖與提示在右。"""
    aside = [fig(svg, name, w)] if svg else []
    if hint_:
        aside += hint_lines(hint_, title=hint_title)
    main = [para(nm(x)) if isinstance(x, str) else x for x in body] + write_lines(n)
    return aside_layout(main, aside, main_pct=pct, media=M, boxed=True) + GAP


def practice():
    M = MediaRegistry()
    P = [masthead(SUBJ, UNIT, '課堂練習'), student_info_row()]
    P.append(hint(['做題前先翻講義：提示卡「知一推二」、手順卡「求圓心到弦的距離」和四個範例。']))

    # ---------------- 練習 A
    P.append(heading(f'練習A（{star_label(1)}）', keep_next=True))
    P.append(side_q(M, ['A1．看圖填空（圖中 BC 經過圓心 O）。',
                        '(1) 圖中的直徑是＿＿＿＿；半徑有＿＿＿＿＿＿＿＿。',
                        '(2) 圖中的弦有＿＿＿＿＿＿＿＿；{∠AOC} 是＿＿＿＿角。',
                        '(3) {arc(DE)} 是＿＿＿＿弧（填「優」或「劣」）。'],
                    F_parts(), 'p_a1', n=1,
                    hint_=['弦：兩端都在圓上', '直徑：經過圓心的弦', '頂點在圓心＝圓心角'], hint_title='提示卡'))
    P.append(side_q(M, ['A2．如圖，AB、CD 是 {⊙O} 的兩條弦，O 是圓心。看圖填空：',
                        '(1) 如果 {∠AOB=∠COD}，那麼 {arc(AB)=} ＿＿＿＿，{AB=} ＿＿＿＿。',
                        '(2) 如果 {arc(AB)=arc(CD)}，那麼 {∠AOB=} ＿＿＿＿，{AB=} ＿＿＿＿。',
                        '(3) 如果 {AB=CD}，那麼 {∠AOB=} ＿＿＿＿，{arc(AB)=} ＿＿＿＿。'],
                    circ({'A': (150, 1.1), 'B': (60, 1.1), 'C': (-60, 1.1), 'D': (230, 1.1)},
                         segs=[('A', 'B'), ('C', 'D'), ('O', 'A'), ('O', 'B'), ('O', 'C'), ('O', 'D')],
                         olab=(-22, 4)),
                    'p_a2', n=1, hint_=['知一推二：①圓心角 ②弧 ③弦', '知道一組相等，另外兩組也相等'],
                    hint_title='提示卡'))
    P.append(side_q(M, ['A3．在 {⊙O} 中，{arc(AB)=arc(CD)}，{∠AOB=50°}，弦 {AB=6}。'
                        '求 {∠COD}、弦 CD 的長，以及 {arc(CD)} 的度數。'],
                    None, 'p_a3', n=3, hint_=['等弧 → 等圓心角', '等弧 → 等弦', '弧的度數＝圓心角的度數']))
    P.append(side_q(M, ['A4．{⊙O} 的半徑是 10，弦 AB＝16，求圓心 O 到 AB 的距離。'],
                    F_perp(), 'p_a4', n=5,
                    hint_=['① 半弦＝16 ÷ 2', '② 距離²＝半徑²－半弦²', '③ 開平方，寫答句'], hint_title='手順卡'))
    P.append(side_q(M, ['A5．看圖填空（O 是圓心）。',
                        '(1) {∠AOB=80°}，則同弧所對的圓周角 {∠ACB=} ＿＿＿＿。',
                        '(2) 圓周角 {∠ACB=35°}，則圓心角 {∠AOB=} ＿＿＿＿。',
                        '(3) 若 AB 是直徑，則 {∠ACB=} ＿＿＿＿。'],
                    F_central_inscribed(), 'p_a5', n=1,
                    hint_=['頂點在圓上 ÷ 2', '頂點在圓心 × 2', '直徑對的圓周角＝90°'], hint_title='提示卡'))
    P.append(checkpoint_rule())

    # ---------------- 練習 B
    P.append(heading(f'練習B（{star_label(2)}）', page_break_before=True))
    P.append(side_q(M, ['B1．如圖，AB 是 {⊙O} 的直徑，{arc(BC)=arc(CD)=arc(DE)}，{∠COD=40°}，'
                        '求 {∠AOE} 的度數。'],
                    circ({'A': (180, 1.1), 'B': (0, 1.1), 'C': (40, 1), 'D': (80, 1), 'E': (120, 1)},
                         segs=[('A', 'B'), ('O', 'C'), ('O', 'D'), ('O', 'E')],
                         arcs=[('B', 'C', {'w': 1.8, 'tick': 1}), ('C', 'D', {'w': 1.8, 'tick': 1}),
                               ('D', 'E', {'w': 1.8, 'tick': 1})], olab=(-4, 18)),
                    'p_b1', n=5, hint_=['等弧'], hint_title='提示'))
    P.append(side_q(M, ['B2．在 {⊙O} 中，弦 {AB=CD}，{∠AOB=72°}。',
                        '(1) 求 {∠COD}。',
                        '(2) 弦 AB 所對的劣弧所對的圓心角是 {72°}，那麼它所對的優弧所對的圓心角是多少度？'],
                    None, 'p_b2', n=4, hint_=['等弦', '一周角＝360°'], hint_title='提示'))
    P.append(side_q(M, ['B3．{⊙O} 的半徑是 13，圓心 O 到弦 AB 的距離是 5，求弦 AB 的長。'],
                    None, 'p_b3', n=5, hint_=['半弦'], hint_title='提示'))
    P.append(side_q(M, ['B4．AB 是 {⊙O} 的直徑，C 是圓上一點，{∠A=28°}，求 {∠ACB} 和 {∠B}。'],
                    circ({'A': (180, 1.1), 'B': (0, 1.1), 'C': (118, 1)}, segs=[('A', 'B'), ('A', 'C'), ('C', 'B')],
                         olab=(-4, 18)),
                    'p_b4', n=4, hint_=['直徑'], hint_title='提示'))
    P.append(side_q(M, ['B5．如圖，弦 AB、CD 相交，{AB=CD}。填上理由，完成「求證 {arc(AD)=arc(BC)}」：',
                        '∵ {AB=CD}　　　　（已知）',
                        '∴ {arc(ACB)=arc(CAD)}　（＿＿＿＿＿＿＿＿＿＿＿＿）',
                        '∴ {arc(ACB)-arc(AC)=arc(CAD)-arc(AC)}　（兩邊減去＿＿＿＿）',
                        '∴ {arc(BC)=} ＿＿＿＿'],
                    F_cross(False), 'p_b5x', n=1, hint_=['範例三'], hint_title='提示', w=5.4, pct=0.64))
    P.append(side_q(M, ['B6．圓內接四邊形 ABCD 中，{∠A=110°}，{∠B=75°}，求 {∠C} 和 {∠D}。'],
                    F_quad(), 'p_b6', n=4, hint_=['對角'], hint_title='提示'))
    P.append(checkpoint_rule())

    # ---------------- 練習 C
    P.append(heading(f'練習C（{star_label(3)}）', page_break_before=True))
    P.append(side_q(M, ['C1．如圖，在 {⊙O} 中，{arc(AB)=arc(AC)}，{∠ACB=60°}。',
                        '(1) 求 {∠AOB} 的度數。',
                        '(2) 小明說：「因為 {∠AOB=∠AOC}，所以 {arc(AB)=arc(AC)}。」'
                        '他少寫了哪一個前提？'],
                    F_equilateral(), 'p_c1', n=5, w=5.4))
    P.append(side_q(M, ['C2．大圓的圓心角 {∠AOB=50°}，小圓的圓心角 {∠CPD=50°}（O、P 分別是兩圓的圓心）。'
                        '小芳說：「兩個圓心角相等，所以弦 {AB=CD}。」她說得對嗎？說明理由。'],
                    F_two_circles(), 'p_c2', n=4, w=6.0))
    P.append(side_q(M, ['C3．在 {⊙O} 中，弦 AB 把圓分成兩條弧，劣弧 {arc(AB)} 所對的圓心角是 {100°}。'
                        'C 在優弧上，D 在劣弧上（C、D 都不與 A、B 重合）。求 {∠ACB} 和 {∠ADB}。'],
                    circ({'A': (215, 1.1), 'B': (325, 1.1), 'C': (100, 1), 'D': (270, 1.2)},
                         segs=[('O', 'A', {'dash': 1}), ('O', 'B', {'dash': 1}), ('C', 'A'), ('C', 'B'),
                               ('D', 'A'), ('D', 'B')], olab=(10, -6)),
                    'p_c3', n=6, w=5.6))
    P.append(side_q(M, ['C4．自己出一題：畫一個圓，標出兩條相等的弦，'
                        '用「知一推二」寫出你能推出的兩個結論（記得寫前提）。'],
                    None, 'p_c4', n=5, pct=1.0) if False else
             pbox([para('C4．自己出一題：畫一個圓，標出兩條相等的弦，用「知一推二」寫出你能推出的兩個結論'
                        '（記得寫前提）。')] + write_lines(6)))

    # ---------------- 參考答案
    P += answers([
        '練習A',
        'A1．(1) 直徑 BC；半徑 OA、OB、OC　(2) 弦 DE、BC；圓心角　(3) 劣',
        'A2．(1) {arc(CD)}；CD　(2) {∠COD}；CD　(3) {∠COD}；{arc(CD)}（劣弧）',
        'A3．等弧所對的圓心角相等：{∠COD=50°}；等弧所對的弦相等：{CD=6}；{arc(CD)} 是 {50°} 的弧。',
        'A4．半弦＝16 ÷ 2＝8；距離²＝10²－8²＝100－64＝36；距離＝6。（垂徑定理；丙班如未教可略）',
        'A5．(1) {40°}　(2) {70°}　(3) {90°}',
        '練習B',
        'B1．等弧對等圓心角：{∠BOC=∠DOE=40°}；{∠AOE=180°-40°×3=60°}。',
        'B2．(1) 等弦對等圓心角：{∠COD=72°}。(2) {360°-72°=288°}。',
        'B3．半弦²＝13²－5²＝169－25＝144，半弦＝12；{AB=24}。（垂徑定理；丙班如未教可略）',
        'B4．直徑所對的圓周角是直角：{∠ACB=90°}；{∠B=180°-90°-28°=62°}。',
        'B5．同圓中，等弦所對的劣弧相等；公共弧 {arc(AC)}；{arc(AD)}。',
        'B6．對角互補：{∠C=180°-110°=70°}；{∠D=180°-75°=105°}。',
        '練習C',
        'C1．(1) 由講義範例二，△ABC 是等邊三角形，三條弦相等，{∠AOB=∠BOC=∠AOC}，'
        '三個角合成一周角：{∠AOB=360°÷3=120°}。(2) 少寫「在同圓或等圓中」'
        '（本題 A、B、C 在同一個 {⊙O} 上，前提成立，但理由要寫出來）。',
        'C2．不對。兩個圓大小不同，不是「同圓或等圓」，相等的圓心角所對的弦不一定相等；'
        '大圓的弦 AB 較長。',
        'C3．C 在優弧上：{∠ACB} 對劣弧 {arc(AB)}，{∠ACB=100°÷2=50°}。'
        'D 在劣弧上：{∠ADB} 對優弧，優弧所對的圓心角＝{360°-100°=260°}，{∠ADB=260°÷2=130°}。'
        '（驗：A、C、B、D 四點構成圓內接四邊形 ACBD，對角 {50°+130°=180°} ✓）',
        'C4．開放題。例：{AB=CD}，在同圓中 → {∠AOB=∠COD}，劣弧 {arc(AB)=arc(CD)}。'
        '評分看三點：圖上兩弦相等有標記、結論是另外兩個量、寫了「在同圓或等圓中」。',
    ])
    print(build_docx(P, os.path.join(OUT, NAME_P + '.docx'), footer_text=FOOT, media=M))


if __name__ == '__main__':
    handout()
    practice()
