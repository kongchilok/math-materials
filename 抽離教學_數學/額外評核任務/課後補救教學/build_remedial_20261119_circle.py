# -*- coding: utf-8 -*-
r"""
build_remedial_20261119_circle.py — 初三數學補救班 課後補救教學（2026-11-19，週四）
範圍：圓（基本概念）→ 垂徑定理 → 弧、弦、圓心角 → 圓周角定理及推論

使用者 2026-11-17：「最後出課後補救教學（內容是圓一直到圓周角定理）」，題目來源＝
`初三數學\融合班講義練習\08_圓的有關性質\新修訂\` 內的往年講義、練習、測驗、考卷。
本份照課後補救教學慣例「題目由使用者提供，我只重整＋套 house-style」：17 題全部是往年原題，
數據不改，出處逐題寫在教師卷答案表；只補畫圖（原稿圖為截圖／手寫）與加知識點回顧。

日期：使用者 2026-11-17 指定 2026-11-19（週四）實施（初版擬 12/17，已改）。
同日要求：學生卷控制在 8 頁內；練 3–5（垂徑定理）放同一頁；每個知識點回顧框旁邊配圖。
版面層：import `..\..\初三數學\融合班講義練習\08_圓的有關性質\新修訂\circle_common.py`（跨資料夾依賴）。
逐題驗算見《驗算_課後補救教學20261119_圓到圓周角定理.md》。
"""
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(
    HERE, '..', '..', '初三數學', '融合班講義練習', '08_圓的有關性質', '新修訂')))
from circle_common import *  # noqa: E402,F401,F403
from omml_docx import MediaRegistry, _tbl  # noqa: E402,F401

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

OUT = HERE
FIG = os.path.join(HERE, '_tmp_fig_circle')
import circle_common as cc  # noqa: E402
cc.FIG = FIG
SUBJ_R = '初三數學（補救班）'
UNIT = '圓：基本概念、垂徑定理、弧弦圓心角、圓周角定理'
BASE = '課後補救教學_初三數學補救班_20261119_圓到圓周角定理'
FOOT_R = '初三數學補救班．課後補救教學 2026-11-19'
PAREN = '（　　　）'


def deg_of(x, y):
    return math.degrees(math.atan2(y, x)) % 360


# ================================ 圖（全部按原稿描述重畫） ================================
FIGS = {
    # 知識點回顧配圖（與修訂版講義同一組圖）
    'r1': lambda: circ({'A': (100, 1), 'B': (190, 1.1), 'C': (10, 1.1), 'D': (238, 1), 'E': (302, 1)},
                       segs=[('B', 'C'), ('O', 'A'), ('D', 'E')], arcs=[('D', 'E', {'w': 4.6})], olab=(-4, -14)),
    'r2': lambda: circ({'C': (90, 1), 'D': (270, 1), 'A': (208, 1.1), 'B': (-28, 1.1),
                        'M': ('xy', 0, -0.47, (13, 14))},
                       segs=[('C', 'D'), ('A', 'B'), ('O', 'A', {'dash': 1})], right=[('M', 'O', 'B')], olab=(-18, 4)),
    'r3': lambda: circ({'A': (200, 1.1), 'B': (300, 1.1), "A'": (60, 1.1), "B'": (160, 1.1)},
                       segs=[('O', 'A'), ('O', 'B'), ('A', 'B', {'tick': 1}),
                             ('O', "A'"), ('O', "B'"), ("A'", "B'", {'tick': 1})],
                       arcs=[('A', 'B', {'w': 4.6, 'tick': 2}), ("A'", "B'", {'w': 4.6, 'tick': 2})],
                       angles=[('O', 'A', 'B', '', 16), ('O', "A'", "B'", '', 16)], olab=(10, -4)),
    'r4': lambda: circ({'C': (90, 1), 'A': (215, 1.1), 'B': (325, 1.1)},
                       segs=[('C', 'A'), ('C', 'B'), ('O', 'A', {'dash': 1}), ('O', 'B', {'dash': 1})],
                       arcs=[('A', 'B', {'w': 4.6})],
                       angles=[('C', 'A', 'B', '', 22), ('O', 'A', 'B', '', 16)], olab=(10, -6)),
    # 練 3：r＝5、AB＝8，OC⊥AB 於 C（原圖沒有畫 OA）
    'q3': lambda: circ({'A': (208, 1.1), 'B': (-28, 1.1), 'C': ('xy', 0, -0.47, (13, 14))},
                       segs=[('A', 'B'), ('O', 'C')], right=[('C', 'O', 'B')], olab=(8, -4)),
    # 練 4：AB 直徑（水平），CD⊥AB 於 E，AE＝2、BE＝8（E 在 A 與 O 之間，OE＝0.6r）
    'q4': lambda: circ({'A': (180, 1.1), 'B': (0, 1.1), 'C': (126.87, 1), 'D': (233.13, 1),
                        'E': ('xy', -0.6, 0, (12, 14))},
                       segs=[('A', 'B'), ('C', 'D')], right=[('E', 'C', 'B')], olab=(-4, 18)),
    # 練 5：直徑 AB⊥弦 CD 於 E，CD＝16、OE＝6（r＝10）
    'q5': lambda: circ({'A': (90, 1), 'B': (270, 1), 'C': (216.87, 1.1), 'D': (323.13, 1.1),
                        'E': ('xy', 0, -0.6, (13, 14))},
                       segs=[('A', 'B'), ('C', 'D')], right=[('E', 'O', 'D')], olab=(9, 2)),
    # 練 7：AB 直徑，弧 BC＝CD＝DE，∠AOE＝60°（每段 40°）
    'q7': lambda: circ({'A': (180, 1.1), 'B': (0, 1.1), 'C': (40, 1), 'D': (80, 1), 'E': (120, 1)},
                       segs=[('A', 'B'), ('O', 'C'), ('O', 'D'), ('O', 'E')],
                       arcs=[('B', 'C', {'w': 1.8, 'tick': 1}), ('C', 'D', {'w': 1.8, 'tick': 1}),
                             ('D', 'E', {'w': 1.8, 'tick': 1})], olab=(-4, 18)),
    # 練 9：上弧由左至右 A、C、B、D，O 在下方；弧 AB＝弧 CD
    'q9': lambda: circ({'A': (155, 1.1), 'C': (115, 1), 'B': (65, 1), 'D': (25, 1.1)},
                       segs=[('O', 'A'), ('O', 'C'), ('O', 'B'), ('O', 'D')], olab=(-6, 18)),
    # 練 10：A 左上、C 右上、D 左下、B 右下，弦 AB、CD 相交，AB＝CD
    'q10': lambda: circ({'A': (120, 1.1), 'C': (60, 1.1), 'D': (200, 1.1), 'B': (-20, 1.1)},
                        segs=[('A', 'B'), ('C', 'D'), ('A', 'D'), ('B', 'C')], olab=(-4, 20)),
    # 練 12：∠A＝45°，求 ∠BOC
    'q12': lambda: circ({'A': (100, 1), 'B': (225, 1.1), 'C': (315, 1.1)},
                        segs=[('A', 'B'), ('A', 'C'), ('O', 'B'), ('O', 'C')], olab=(10, -4)),
    # 練 13：AD 為鉛直直徑，B 左、C 右上；∠BCA 與 ∠BDA 同對弧 AB
    'q13': lambda: circ({'D': (90, 1), 'A': (270, 1), 'B': (170, 1.1), 'C': (35, 1.1)},
                        segs=[('A', 'D'), ('C', 'B'), ('C', 'A'), ('D', 'B')], olab=(9, 4)),
    # 練 14：AB 直徑，∠ACD＝36°，求 ∠BAD
    'q14': lambda: circ({'A': (180, 1.1), 'B': (0, 1.1), 'D': (108, 1), 'C': (250, 1)},
                        segs=[('A', 'B'), ('A', 'C'), ('C', 'D'), ('A', 'D'), ('B', 'D')],
                        olab=(4, 18)),
    # 練 15：B 左、A 右（AB 直徑），C 頂、D 底
    'q15': lambda: circ({'B': (180, 1.1), 'A': (0, 1.1), 'C': (110, 1), 'D': (270, 1)},
                        segs=[('A', 'B'), ('C', 'B'), ('C', 'A'), ('C', 'D'), ('D', 'A')],
                        olab=(-18, 16)),
    # 練 16：AB⊥AC，AB＝8、AC＝6，BC 沒有畫（B、C 在直徑兩端）
    'q16': lambda: circ({'B': (200, 1.1), 'C': (20, 1.1), 'A': (93.74, 1)},
                        segs=[('A', 'B'), ('A', 'C')], right=[('A', 'B', 'C')], olab=(8, 15)),
}


def cut_tail(xml):
    """aside_layout() 內部用 _tbl(trailing_blank=True)，表後自帶一個 1.5 行空段（約 50pt）；
    剪走，改由 GAP／GAPK 做框距（兩個表之間仍有段落，Word 不會報毀損）。"""
    i = xml.rfind('</w:tbl>')
    return xml[:i + len('</w:tbl>')]


def F(media, key, w=5.6):
    return expand_image(fig(FIGS[key](), 'r_' + key, w), media)


def review(media, key, lines_, w=4.2):
    """知識點回顧：左欄一行一件事（灰底），右欄配定理圖（使用者 2026-11-17：每條定理旁都配圖）。
    整塊加 keepNext 黐住下一題，不孤留頁尾。"""
    left = [para('知識點回顧', bold=True, spacing=False, shd=GREY_FILL)]
    left += [tight(para(nm(x), shd=GREY_FILL, sz=22), line=290, after=30) for x in lines_]
    xml = cut_tail(aside_layout(left, [F(media, key, w)], main_pct=0.68, media=media, boxed=True))
    xml = keep_together(xml).replace('<w:pPr>', '<w:pPr><w:keepNext/>').replace(
        '<w:keepNext/><w:keepNext/>', '<w:keepNext/>')
    return xml + GAPK


_RULE_PPR = ('<w:pPr><w:pBdr><w:bottom w:val="single" w:sz="5" w:space="4" w:color="808080"/>'
             '<w:between w:val="single" w:sz="5" w:space="4" w:color="808080"/></w:pBdr>'
             '<w:spacing w:before="0" w:after="0" w:line="420" w:lineRule="exact"/></w:pPr>')


def ruled(label=''):
    """一條書寫線（行高 21pt≈7.4mm）。連續幾段邊框設定相同，Word 會合併成一組，
    所以一定要有 w:between 才會每行都畫線（記憶 docx_adjacent_border_paras_merge）。"""
    run = (f'<w:r><w:rPr><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>'
           f'<w:t xml:space="preserve">{label}</w:t></w:r>') if label else ''
    return f'<w:p>{_RULE_PPR}{run}</w:p>'


def lines_fix(n):
    """n 條作答線＋最後一條「改正：」線（使用者 2026-11-17：全卷控制在 8 頁）。"""
    return [ruled() for _ in range(n)] + [ruled('改正：')]


def Q(media, head, body=(), key=None, n=3, w=3.9, opts_=None, pct=0.68, fill=False):
    main = [tight(para(head, keep_next=True), line=320, after=40)] + [tight(para(nm(x)), line=320, after=40) for x in body]
    if opts_:
        main += [tight(para(x, ind=300), line=320, after=40) for x in opts_]
    if fill:      # 純填空題：不留過程橫線，只留改正線（使用者 2026-11-17：練 11、12）
        main += lines_fix(0)
    else:
        main += lines_fix(n if key in ('q3', 'q4', 'q5') else n + 1)   # 垂徑三題要擠同一頁，其餘多給一行
    if key:
        return cut_tail(aside_layout(main, [F(media, key, w)], main_pct=pct, media=media, boxed=True)) + GAP
    return pbox(main)


# ================================ 學生卷 ================================
def student():
    M = MediaRegistry()
    P = [masthead(SUBJ_R, UNIT, '課後補救教學'), student_info_row()]
    P.append(para('建議 45–50 分鐘完成　　共四大題（17 題）　　滿分 100 分　　得分：＿＿＿＿ / 100', bold=True))
    P.append(para('每大題先讀「知識點回顧」再做；老師批改後，在「改正」欄完成訂正。'))

    # ---------------- 一 ----------------
    P.append(heading('一、圓的基本概念（10 分，每題 5 分）'))
    P.append(review(M, 'r1', ['弦：連接圓上兩點的線段。直徑：經過圓心的弦，是最長的弦，等於 2 個半徑。',
                     '弧：圓上兩點之間的部分；比半圓大的叫優弧，比半圓小的叫劣弧。',
                     '等圓：能夠重合的兩個圓（半徑相等）。',
                     '右圖：OA 是半徑，BC 是直徑，DE 是弦，粗線是劣弧 {arc(DE)}。']))
    P.append(Q(M, '練 1．下列說法：① 直徑是最長的弦；② 半圓是最長的弧；③ 面積相等的圓是等圓。'
                  '其中正確的是＿＿＿＿＿＿。', n=1))
    P.append(Q(M, f'練 2．已知 {{⊙O}} 的半徑是 6 cm，則 {{⊙O}} 的弦長可能是{PAREN}',
               opts_=['A．24 cm　　B．18 cm　　C．13 cm　　D．12 cm'], n=1))

    # ---------------- 二 ----------------
    P.append(heading('二、垂徑定理（24 分，每題 8 分）', page_break_before=True))
    P.append(review(M, 'r2', ['垂直於弦的直徑，平分這條弦，並且平分弦所對的兩條弧。',
                     '半徑、半弦、圓心到弦的距離組成直角三角形：半徑² ＝ 半弦² ＋ 距離²。',
                     '右圖：直徑 {CD⊥AB} 於 M → {AM=BM}；連 OA 得直角三角形 OMA（圖上沒有半徑就自己連）。']))
    P.append(Q(M, '練 3．如圖，{⊙O} 的半徑是 5，弦 {AB=8}，{OC⊥AB} 於 C，求 OC 的長。', key='q3', n=3))
    P.append(Q(M, '練 4．如圖，AB 是 {⊙O} 的直徑，弦 {CD⊥AB} 於 E，{BE=8}，{AE=2}。',
               ['(1) 求 OE 的長；', '(2) 求 CD 的長。'], key='q4', n=3))
    P.append(Q(M, '練 5．如圖，在 {⊙O} 中，直徑 {AB⊥CD} 於 E，弦 {CD=16}，{OE=6}，求 {⊙O} 的半徑。'
                  '（提示：連 OC）', key='q5', n=3))

    # ---------------- 三 ----------------
    P.append(heading('三、弧、弦、圓心角（30 分）'))
    P.append(review(M, 'r3', ['在同圓或等圓中：圓心角相等 ⇔ 弧相等 ⇔ 弦相等（知一推二）。',
                     '由弦推弧時，劣弧對劣弧、優弧對優弧。',
                     '弧的度數＝它所對的圓心角的度數；半圓是 180°。',
                     '證明格式：等弦 → 等弧 → 兩邊減去公共弧 → 等弧 → 等弦。',
                     "右圖：{∠AOB=∠A'OB'} → 弧相等（雙短線）、弦相等（單短線）。"]))
    P.append(Q(M, '練 6．（4 分）在 {⊙O} 中，{arc(AB)=arc(CD)}，{∠AOB=35°}，則 {∠COD=} ＿＿＿＿。', n=1))
    P.append(Q(M, f'練 7．（6 分）如圖，AB 是 {{⊙O}} 的直徑，{{arc(BC)=arc(CD)=arc(DE)}}，{{∠AOE=60°}}，'
                  f'則 {{∠BOC}} 的度數是{PAREN}',
               opts_=['A．{40°}　　B．{45°}　　C．{50°}　　D．{60°}'], key='q7', n=2))
    P.append(Q(M, '練 8．（6 分）在 {⊙O} 中，弦 {AB=3}，弦 AB 所對的圓心角 {∠AOB=60°}，'
                  '則 {⊙O} 的半徑是＿＿＿＿。', n=3))
    P.append(Q(M, f'練 9．（6 分）如圖，在 {{⊙O}} 中，{{arc(AB)=arc(CD)}}。下列結論：'
                  f'① {{AB=CD}}；② {{AC=BD}}；③ {{∠AOC=∠BOD}}；④ {{arc(AC)=arc(BD)}}。'
                  f'正確的有{PAREN}',
               opts_=['A．1 個　　B．2 個　　C．3 個　　D．4 個'], key='q9', n=2))
    P.append(Q(M, '練 10．（8 分）如圖，A、B、C、D 是 {⊙O} 上的四點，{AB=CD}。',
               ['(1) 求證：{arc(AB)=arc(CD)}；（2 分）',
                '(2) 求證：{arc(AD)=arc(BC)}；（3 分）',
                '(3) 求證：{AD=BC}。（3 分）'], key='q10', n=7))

    # ---------------- 四 ----------------
    P.append(heading('四、圓周角定理及推論（36 分）'))
    P.append(review(M, 'r4', ['一條弧所對的圓周角＝它所對的圓心角的一半（頂點在圓上 ÷ 2，頂點在圓心 × 2）。',
                     '同弧或等弧所對的圓周角相等。',
                     '直徑所對的圓周角是 90°；90° 的圓周角所對的弦是直徑。',
                     '一條弦對兩條弧，所以一條弦所對的圓周角可能有兩個。',
                     '右圖：{∠ACB} 與 {∠AOB} 同對粗線 {arc(AB)}，{∠ACB=frac(1,2)∠AOB}。']))
    P.append(Q(M, '練 11．（4 分）在 {⊙O} 中，圓周角 {∠ACB=43°}，則同弧所對的圓心角 {∠AOB=} ＿＿＿＿。', fill=True))
    P.append(Q(M, '練 12．（4 分）如圖，A、B、C 在 {⊙O} 上，{∠A=45°}，則 {∠BOC=} ＿＿＿＿。', key='q12', w=3.2, pct=0.76, fill=True))
    P.append(Q(M, '練 13．（5 分）如圖，AD 是 {⊙O} 的直徑，{∠BCA=50°}，則 {∠BDA=} ＿＿＿＿。', key='q13', n=1,
               ))
    P.append(Q(M, '練 14．（5 分）如圖，AB 是 {⊙O} 的直徑，{∠ACD=36°}，則 {∠BAD=} ＿＿＿＿。', key='q14',
               n=2))
    P.append(Q(M, '練 15．（5 分）如圖，AB 是 {⊙O} 的直徑，{∠CAB=35°}，則 {∠D=} ＿＿＿＿。', key='q15', n=2,
               ))
    P.append(Q(M, '練 16．（6 分）如圖，A、B、C 在 {⊙O} 上，{AB⊥AC}，{AB=8}，{AC=6}，求 {⊙O} 的半徑。',
               key='q16', n=4, ))
    P.append(Q(M, '練 17．（7 分）{⊙O} 的一條弦所對的圓心角是 {30°}，'
                  '則這條弦所對的圓周角是＿＿＿＿＿＿。', n=3))
    out = os.path.join(OUT, BASE + '_學生卷.docx')
    print(build_docx(P, out, footer_text=FOOT_R, media=M))


# ================================ 教師卷 ================================
def teacher():
    P = [masthead(SUBJ_R, UNIT, '課後補救教學・教師卷')]
    P.append(para('本卷供教師批改使用，不發給學生。17 題全部是往年原題（數據不改），'
                  '出處見最右欄；分值為建議分配，滿分 100 分。', sz=22))
    P.append(para('實施日期：補救班 2026-11-19（週四）。', sz=22, bold=True))
    w = [int(W * 0.09), int(W * 0.22), int(W * 0.47)]
    w.append(W - sum(w))
    rows = [{'hdr': True, 'cells': [{'p': [tight(para(h, bold=True, sz=21))], 'shd': GREY_FILL}
                                    for h in ('題（分）', '答案', '解析與評分', '原題出處')]}]
    data = [
        ('一', None, None, None),
        ('練 1（5）', '①③', '② 錯：優弧比半圓長。③ 面積相等 → 半徑相等 → 能重合。兩個都選對才給分。',
         '23-24 初三乙幾何統測 第 11 題'),
        ('練 2（5）', 'D', '最長的弦是直徑＝12 cm，弦長不會超過 12 cm。',
         '24-25 初三甲第一學段考試 第 9 題'),
        ('二', None, None, None),
        ('練 3（8）', '{OC=3}', '連 OA（2）；{AC=8÷2=4}（2）；{OC^2=5^2-4^2=9}（2）；{OC=3}（2）。',
         '23-24 統測 第 2 題；複習_圓 無題號題'),
        ('練 4（8）', '(1) {OE=3}　(2) {CD=8}',
         '{AB=10}，{r=5}，{OE=OA-AE=5-2=3}（4）；連 OC，{CE^2=5^2-3^2=16}，{CE=4}，{CD=8}（4）。',
         '24-25 初三甲考試 第 23 題'),
        ('練 5（8）', '半徑 10', '{CE=16÷2=8}（3）；{OC^2=8^2+6^2=100}（3）；{OC=10}（2）。',
         '2425 大測二調卷 第 18 題'),
        ('三', None, None, None),
        ('練 6（4）', '{35°}', '同圓中，等弧所對的圓心角相等。', '25-26 初三丙考試 第 14 題'),
        ('練 7（6）', 'A', '{∠BOE=180°-60°=120°}，三段等弧各 {120°÷3=40°}。',
         '練習_圓 第 2 題'),
        ('練 8（6）', '3', '{OA=OB}，{∠AOB=60°} → △AOB 是等邊三角形 → {OA=AB=3}。',
         '25-26 初三丙考試 第 20 題'),
        ('練 9（6）', 'D', '等弧對等弦得 ①；兩弧都減去公共弧 {arc(CB)} 得 ④；'
         '再由等弧得 ②（等弦）、③（等圓心角）。四個都對。', '23-24 統測 第 4 題'),
        ('練 10（8）', '證明',
         '(1) ∵ {AB=CD} ∴ {arc(AB)=arc(CD)}（同圓中等弦對等弧）（2）'
         '(2) 兩弧都減去公共弧 {arc(AC)}：{arc(AB)-arc(AC)=arc(CD)-arc(AC)}，即 {arc(BC)=arc(AD)}（3）'
         '(3) ∵ {arc(AD)=arc(BC)} ∴ {AD=BC}（同圓中等弧對等弦）（3）。漏寫「同圓中」每處扣 1 分。',
         '25-26 初三丙考試 第 26 題（7%）；同型：23-24 統測 第 20 題'),
        ('四', None, None, None),
        ('練 11（4）', '{86°}', '圓心角＝圓周角 × 2。', '24-25 初三甲考試 第 18 題'),
        ('練 12（4）', '{90°}', '{∠BOC=2∠A=90°}。', '25-26 初三丙考試 第 13 題'),
        ('練 13（5）', '{50°}', '{∠BCA} 與 {∠BDA} 同對 {arc(AB)}，同弧所對的圓周角相等。',
         '24-25 初三甲考試 第 10 題'),
        ('練 14（5）', '{54°}', '連 BD：{∠ABD=∠ACD=36°}（同對 {arc(AD)}）；AB 直徑 → {∠ADB=90°}；'
         '{∠BAD=180°-90°-36°=54°}。', '24-25 初三甲考試 第 11 題'),
        ('練 15（5）', '{55°}', 'AB 直徑 → {∠ACB=90°}，{∠ABC=90°-35°=55°}；'
         '{∠D} 與 {∠ABC} 同對 {arc(AC)}，{∠D=55°}。', '複習_圓 第 1 題'),
        ('練 16（6）', '半徑 5', '{∠BAC=90°} → BC 是直徑（2）；{BC^2=8^2+6^2=100}，{BC=10}（2）；'
         '半徑 {=5}（2）。', '23-24 統測 第 12 題'),
        ('練 17（7）', '{15°} 或 {165°}', '圓周角頂點在劣弧以外：{30°÷2=15°}；'
         '頂點在劣弧上：對著優弧（{360°-30°=330°}），{330°÷2=165°}。只答 15° 給 4 分。',
         '25-26 初三丙考試 第 21 題'),
    ]
    for n_, a, why, src in data:
        if a is None:
            rows.append([{'p': [tight(para(f'{n_}、', bold=True, sz=21))], 'span': 4, 'shd': GREY_FILL}])
            continue
        rows.append([[tight(para(n_, sz=21))], [tight(para(nm(a), bold=True, sz=21))],
                     [tight(para(nm(why), sz=21))], [tight(para(src, sz=20))]])
    P.append(_tbl(rows, w, trailing_blank=False) + GAP)
    P.append(heading('重整說明', keep_next=True))
    for t in ['選題：由 `新修訂\\` 資料夾 8 份往年材料抽出單元 08 範圍內約 80 題，按「圓 → 圓周角定理」'
              '四段各揀最常考的題型；圓內接四邊形不在本份範圍。',
              '第三大題（弧、弦、圓心角）是今年課堂較少提到的一節，往年卷 8 份有 6 份考過，'
              '25-26 初三丙考試約 20 分觸及，故給 30 分並放入完整證明題（練 10）。',
              '圖形：原稿多為截圖或手寫，本卷按原題描述重畫（黑白），已逐題核對數據與原圖位置一致。',
              '原稿有歧義或超範圍而未選：25-26 第 35 題（三等分點題意不清）、調卷第 27(2) 題（答案 169/24，'
              '計算量超出補救班）。']:
        P.append(tight(para(t, sz=21), line=300, after=40))
    out = os.path.join(OUT, BASE + '_教師卷.docx')
    print(build_docx(P, out, footer_text=FOOT_R))


if __name__ == '__main__':
    student()
    teacher()
