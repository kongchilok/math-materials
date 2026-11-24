# -*- coding: utf-8 -*-
r"""
build_check02_circle.py — 初三數學 抽離課堂檢測 02（圓的有關性質：至圓內接四邊形）

需求（2026-11-24 使用者當次指定，「全程自動」）：
- 內容＝圓的有關性質，由基本概念到圓內接四邊形；限時 20 分鐘。
- 沿用抽離課堂檢測 01 的格式：卷 S 標準版＋卷 A 輔助版（同題同分，調整支援）＋教師卷一份。

範圍＝乙、丙兩班教案交集（CLAUDE.md 路由表：必須逐週對兩班教案取交集）：
- 乙班 12/10 基本概念、12/14 垂徑定理、12/16 圓周角定理、01/04 圓內接四邊形
- 丙班 12/09 基本概念、12/11 圓周角（一）、12/15 圓周角（二）＋圓內接四邊形、12/16 綜合
- → 交集＝基本概念、圓周角定理（含三推論）、圓內接四邊形；**垂徑定理只有乙班教，不考**。
- 「弧、弦、圓心角的關係」（修訂版講義第三節）兩班教案仍未排課時；修訂版講義建議併入
  「圓的基本概念」同一課時（丙 12/09、乙 12/10），本卷按此出第二大題（4 分），
  教師卷註明：若該節未教，第二大題不計分，滿分改為 26 分。
- 施測時間：兩班都教完之後（乙班 01/04 之後）。

教學設計（自動模式下由我選定，沿用單元 08 修訂版講義）：
主 D7 提示卡＋輔 D2 手順卡（步驟格）、D14 錯誤分析對比（三(4) 改錯題）。

house-style 偏離說明（測驗卷文類，刻意，與檢測 01 相同）：
1. 不用 ★ 三層難度標籤——全班同卷、每題有分值。
2. masthead 類型寫「抽離課堂檢測」；學生紙面不印「輔助版」，只在頁尾小字「卷 S／卷 A」。
逐題驗算見《驗算_抽離課堂檢測02_圓.md》；python build_check02_circle.py --verify 重算座標。
"""
import io
import math
import re
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CIRCLE = os.path.join(HERE, '..', '..', '初三數學', '融合班講義練習', '08_圓的有關性質', '新修訂')
sys.path.insert(0, os.path.normpath(CIRCLE))
import circle_common as cc  # noqa: E402  （先 import：它負責找到可用的 omml_docx 路徑）
from circle_common import circ, GAP  # noqa: E402
sys.path.insert(0, HERE)
import build_check01_quadratic as c1  # noqa: E402  （借用檢測 01 已目視驗收過的版面小構件）
from omml_docx import *  # noqa: E402,F401,F403
from omml_docx import MediaRegistry, _PAGE_CONTENT_WIDTH, _tbl  # noqa: E402

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

cc.FIG = os.path.join(HERE, '_tmp_fig')      # 圖檔放本資料夾 _tmp_fig，收尾刪
os.makedirs(cc.FIG, exist_ok=True)

OUT = HERE
SUBJECT = '初三數學'
UNIT = '圓的有關性質（至圓內接四邊形）'
BASE = '抽離課堂檢測_初三數學_02_圓的有關性質至圓內接四邊形'
W = _PAGE_CONTENT_WIDTH
TIME_LINE = '限時 20 分鐘　　共四大題　　滿分 30 分　　　　得分：＿＿＿＿ / 30'

lines, why, tc, hdr_cell, frame_table = c1.lines, c1.why, c1.tc, c1.hdr_cell, c1.frame_table


def save(P, name, footer, media):
    build_docx([c1.tighten(x) for x in P], os.path.join(OUT, name), footer_text=footer, media=media)


# ============================ 圖（點的位置＝度數，0° 在右、逆時針；兩版共用） ============================
PTS = {
    'f1': {'A': (160, 1.1), 'B': (340, 1.1), 'C': (70, 1), 'D': (210, 1.1), 'E': (280, 1)},
    # A／C、B／D 相差 150°（不可 180°：否則 OA＋OC 看起來是一條直徑）
    'f2': {'A': (220, 1.1), 'B': (285, 1.1), 'C': (10, 1.1), 'D': (75, 1)},
    'f3a': {'C': (90, 1), 'A': (210, 1.1), 'B': (330, 1.1)},
    'f3b': {'A': (180, 1.1), 'B': (0, 1.1), 'C': (70, 1)},
    'f3c': {'A': (200, 1.1), 'B': (340, 1.1), 'C': (115, 1), 'D': (55, 1)},
    'f3d': {'C': (90, 1), 'A': (230, 1.1), 'B': (310, 1.1)},
    'f4a': {'A': (150, 1.1), 'B': (230, 1.1), 'C': (290, 1.1), 'D': (20, 1.1)},
    'f4b': {'A': (110, 1), 'B': (220, 1.1), 'C': (290, 1.1), 'D': (0, 1.1)},
}


def F(key):
    p = PTS[key]
    if key == 'f1':
        return circ(p, segs=[('A', 'B'), ('O', 'C'), ('C', 'D'), ('C', 'E')],
                    arcs=[('D', 'E', {'w': 4.6})], olab=(-18, 16))
    if key == 'f2':
        return circ(p, segs=[('O', 'A'), ('O', 'B'), ('O', 'C'), ('O', 'D'), ('A', 'B'), ('C', 'D')],
                    arcs=[('A', 'B', {'w': 4.2, 'tick': 1}), ('C', 'D', {'w': 4.2, 'tick': 1})],
                    angles=[('O', 'A', 'B', '65°', 18)], olab=(8, -10))
    if key == 'f3a':
        return circ(p, segs=[('C', 'A'), ('C', 'B'), ('O', 'A'), ('O', 'B')],
                    angles=[('O', 'A', 'B', '120°', 16), ('C', 'A', 'B', '', 22)], olab=(10, -6))
    if key == 'f3b':
        return circ(p, segs=[('A', 'B'), ('A', 'C'), ('B', 'C')],
                    angles=[('A', 'B', 'C', '35°', 34)], olab=(-4, 18))
    if key == 'f3c':
        return circ(p, segs=[('C', 'A'), ('C', 'B'), ('D', 'A'), ('D', 'B'), ('O', 'A'), ('O', 'B')],
                    angles=[('C', 'A', 'B', '70°', 22)], olab=(-4, 18))
    if key == 'f3d':
        return circ(p, segs=[('C', 'A'), ('C', 'B'), ('O', 'A'), ('O', 'B')],
                    angles=[('C', 'A', 'B', '40°', 24), ('O', 'A', 'B', '', 16)], olab=(10, -6))
    if key == 'f4a':
        return circ(p, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')],
                    angles=[('A', 'B', 'D', '75°', 20), ('B', 'C', 'A', '110°', 20)], olab=(8, 15))
    if key == 'f4b':
        return circ(p, segs=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('O', 'B'), ('O', 'D')],
                    angles=[('O', 'B', 'D', '140°', 16)], olab=(-4, -12))
    raise KeyError(key)


def pic(key, w=4.8):
    return cc.fig(F(key), key, w)


# ============================ 題目（兩版共用同一組字串，數字不可能不一致） ============================
Q1_STEM = '如圖，AB 經過圓心 O。根據圖回答下列各題。（6 分）'
Q1_ITEMS = [
    '(1) 圖中的直徑是＿＿＿＿＿。（1 分）',
    '(2) 寫出圖中所有的半徑：＿＿＿＿＿＿＿＿。（1 分）',
    '(3) {∠BOC} 是＿＿＿＿角；{∠DCE} 是＿＿＿＿角。（2 分）',
    '(4) 粗線部分 {arc(DE)} 是＿＿＿＿弧（填「優」或「劣」）。（1 分）',
    '(5) 判斷：「半徑 OC 也是圓的一條弦。」　對　／　錯（圈一個）（1 分）',
]
Q2 = '如圖，在 {⊙O} 中，{arc(AB)=arc(CD)}，{∠AOB=65°}，弦 AB ＝ 4 cm。求 {∠COD} 的度數和弦 CD 的長，並寫出理由。（4 分）'
Q3 = [
    ('(1) 如圖，點 A、B、C 在 {⊙O} 上，{∠AOB=120°}。求 {∠ACB}，並寫出理由。（3 分）', 'f3a'),
    ('(2) 如圖，AB 是 {⊙O} 的直徑，點 C 在 {⊙O} 上，{∠CAB=35°}。求 {∠ABC}，並寫出理由。（3 分）', 'f3b'),
    ('(3) 如圖，點 A、B、C、D 在 {⊙O} 上，{∠ACB=70°}。求 {∠ADB} 和 {∠AOB}，並寫出理由。（3 分）', 'f3c'),
    ('(4) 如圖，{∠ACB} 和 {∠AOB} 都對著 {arc(AB)}，{∠ACB=40°}。小明這樣寫：'
     '「{∠AOB=frac(1,2)×40°=20°}」。小明對不對？如果不對，寫出正確的算式和結果。（3 分）', 'f3d'),
]
Q4 = [
    ('(1) 如圖，四邊形 ABCD 內接於 {⊙O}，{∠A=75°}，{∠B=110°}。求 {∠C} 和 {∠D}，並寫出理由。（4 分）', 'f4a'),
    ('(2) 如圖，四邊形 ABCD 內接於 {⊙O}，{arc(BCD)} 所對的圓心角 {∠BOD=140°}。'
     '求 {∠A} 和 {∠C}，並寫出理由。（4 分）', 'f4b'),
]


def keep_all(xml):
    """整塊題框（單列表格）每段加 keepNext，令題框黏住下面的步驟格——
    第一版卷 A 題框留在上頁、步驟格跑到下頁，7 頁裡有 4 處拆開。"""
    xml = re.sub(r'<w:pPr>(?!<w:keepNext/>)', '<w:pPr><w:keepNext/>', xml)
    return re.sub(r'<w:p>(?!<w:pPr>)', '<w:p><w:pPr><w:keepNext/></w:pPr>', xml)


def side(M, main, key, aside_extra=(), w=4.8, pct=0.62, keep=False):
    """題目在左（作答線跟住題目）、圖與提示在右（記憶 question_layout_aside_right）。
    keep=True：卷 A 用，題框黏住下面的步驟格。"""
    x = cc.aside_layout(main, [pic(key, w)] + list(aside_extra), main_pct=pct, media=M, boxed=True)
    return keep_all(x) + cc.GAPK if keep else x + GAP


# ============================ 卷 S：標準版 ============================
def build_standard():
    M = MediaRegistry()
    P = [masthead(SUBJECT, UNIT, '抽離課堂檢測'), student_info_row(),
         para(TIME_LINE, bold=True, sz=22),
         para('第二至四大題須寫出計算過程及理由（用了哪一條性質）。', sz=22)]

    P.append(heading('一、圓的基本概念（6 分）'))
    P.append(side(M, [para(Q1_STEM)] + [para(t) for t in Q1_ITEMS], 'f1', w=5.0))

    P.append(heading('二、弧、弦、圓心角的關係（4 分）'))
    P.append(side(M, [para(Q2)] + lines(5), 'f2'))

    P.append(heading('三、圓周角定理（12 分）'))
    for t, k in Q3:
        P.append(side(M, [para(t)] + lines(4), k, w=4.4))

    P.append(heading('四、圓內接四邊形（8 分）'))
    for t, k in Q4:
        P.append(side(M, [para(t)] + lines(4), k, w=4.6))  # 5 行時最後一框貼頁尾，多出一張空白頁
    save(P, f'{BASE}_標準版.docx', '初三數學．抽離課堂檢測 02（卷 S）', M)


# ============================ 卷 A：輔助版 ============================
CARD_NAMES = hint_lines([
    '直徑：經過圓心的弦',
    '半徑：圓心連到圓上一點',
    '弦：兩個端點都在圓上',
    '頂點在圓心 → 圓心角',
    '頂點在圓上 → 圓周角',
    '比半圓小 → 劣弧；比半圓大 → 優弧',
], title='提示卡：認名稱')
CARD_KNOW = hint_lines([
    '在同圓或等圓中，下面三樣',
    '知道一樣相等，另外兩樣也相等：',
    '① 弧　② 圓心角　③ 弦',
], title='提示卡：知一推二')
CARD_INSC = [
    '圓周角 ＝ {frac(1,2)} × 同弧所對的圓心角',
    '同弧所對的圓周角相等',
    '直徑所對的圓周角是 {90°}',
]
CARD_QUAD = hint_lines([
    '圓內接四邊形的對角互補（相加 {180°}）',
    '對角＝「隔一個」的角：A 對 C，B 對 D',
    '※ 相鄰的角（如 A 和 B）不互補',
], title='提示卡：圓內接四邊形')


def build_assist():
    M = MediaRegistry()
    P = [masthead(SUBJECT, UNIT, '抽離課堂檢測'), student_info_row(),
         para(TIME_LINE, bold=True, sz=22),
         shaded_box('右邊灰色是提示卡。計算題已經畫好步驟格：等號已印好，跟著右欄一步一步寫；'
                    '右欄有＿＿的，把理由填完整。', sz=22)]

    # ---- 一 ----
    P.append(heading('一、圓的基本概念（6 分）'))
    P.append(side(M, [para(Q1_STEM)] + [para(t) for t in Q1_ITEMS], 'f1', CARD_NAMES, w=4.6))

    # ---- 二 ----
    P.append(heading('二、弧、弦、圓心角的關係（4 分）'))
    P.append(side(M, [para(Q2)], 'f2', CARD_KNOW, w=4.4, keep=True))
    P.append(frame_table([
        eq_row('{∠COD}', '', why('① 寫出度數',
                                 '理由：在同圓中，相等的弧所對的＿＿＿＿相等')),
        eq_row('{CD}', '', why('② 寫出長度（記得單位 cm）',
                               '理由：在同圓中，相等的弧所對的＿＿＿＿相等')),
        answer_row('', why=why('③ 用「∴」寫答句')),
    ], headers=('我的算式', '步驟提示／理由填空'), h=480))

    # ---- 三 ----
    P.append(heading('三、圓周角定理（12 分）', keep_next=True))
    t, k = Q3[0]   # 圓周角定理提示卡放 (1) 右欄（獨立一塊時會孤留上頁底，第三版實測）
    P.append(side(M, [para(t)], k, hint_lines(CARD_INSC, title='提示卡：圓周角定理'), w=4.0, keep=True))
    P.append(frame_table([
        eq_row('{∠ACB}', '', why('① 圓周角 ＝ 圓心角的幾分之幾？',
                                 '理由：同弧所對的圓周角是圓心角的＿＿＿')),
        eq_row('{∠ACB}', '', why('② 代入 {∠AOB} 的度數')),
        eq_row('{∠ACB}', '', why('③ 算出')),
    ], headers=('我的算式', '步驟提示／理由填空'), h=480))
    t, k = Q3[1]
    P.append(side(M, [para(t)], k, w=4.0, keep=True))
    P.append(frame_table([
        eq_row('{∠ACB}', '', why('① AB 是直徑 → {∠ACB} 是幾度？',
                                 '理由：直徑所對的圓周角是＿＿＿＿')),
        eq_row('{∠ABC}', '', why('② 三角形內角和 {180°}：減去另外兩個角')),
        eq_row('{∠ABC}', '', why('③ 算出')),
    ], headers=('我的算式', '步驟提示／理由填空'), h=480))
    t, k = Q3[2]
    P.append(side(M, [para(t)], k, w=4.0, keep=True))
    P.append(frame_table([
        eq_row('{∠ADB}', '', why('① {∠ADB} 和 {∠ACB} 對著同一條弧',
                                 '理由：同弧所對的圓周角＿＿＿')),
        eq_row('{∠AOB}', '', why('② 圓心角 ＝ 圓周角 × ＿＿')),
        eq_row('{∠AOB}', '', why('③ 算出')),
    ], headers=('我的算式', '步驟提示／理由填空'), h=480))
    t, k = Q3[3]
    P.append(side(M, [para(t)], k,
                  hint_lines(['先認頂點：{∠AOB} 的頂點在哪裡？',
                              '圓心角和圓周角，哪一個比較大？'], title='想一想'), w=4.0, keep=True))
    P.append(frame_table([
        span_row('小明：☐ 對　☐ 不對', why('① 先判斷，剔一個')),
        eq_row('{∠AOB}', '', why('② 寫出正確的關係式')),
        eq_row('{∠AOB}', '', why('③ 代入並算出')),
    ], headers=('我的算式', '步驟提示'), h=480))

    # ---- 四 ----
    P.append(heading('四、圓內接四邊形（8 分）', keep_next=True))
    t, k = Q4[0]
    P.append(side(M, [para(t)], k, CARD_QUAD, w=4.4, keep=True))
    P.append(frame_table([
        eq_row('{∠C}', '', why('① {∠C} 的對角是 ∠＿＿',
                               '理由：圓內接四邊形的對角＿＿＿')),
        eq_row('{∠C}', '', why('② 代入並算出')),
        eq_row('{∠D}', '', why('③ {∠D} 的對角是 ∠＿＿')),
        eq_row('{∠D}', '', why('④ 代入並算出')),
        answer_row('', why=why('⑤ 用「∴」寫答句')),
    ], headers=('我的算式', '步驟提示／理由填空'), h=480))
    t, k = Q4[1]
    P.append(side(M, [para(t)], k,
                  hint_lines(['{∠A} 和 {∠BOD} 都對著 {arc(BCD)}'], title='提示'), w=4.4, keep=True))
    P.append(frame_table([
        eq_row('{∠A}', '', why('① 圓周角 ＝ 圓心角的幾分之幾？',
                               '理由：同弧所對的圓周角是圓心角的＿＿＿')),
        eq_row('{∠A}', '', why('② 代入並算出')),
        eq_row('{∠C}', '', why('③ 用對角互補', '理由：圓內接四邊形的對角＿＿＿')),
        eq_row('{∠C}', '', why('④ 代入並算出')),
        answer_row('', why=why('⑤ 用「∴」寫答句')),
    ], headers=('我的算式', '步驟提示／理由填空'), h=480))
    P.append(para('（全卷完）', jc='center', sz=22))
    save(P, f'{BASE}_輔助版.docx', '初三數學．抽離課堂檢測 02（卷 A）', M)


# ============================ 教師卷 ============================
def key_table(rows):
    return c1.key_table(rows)


def build_teacher():
    M = MediaRegistry()
    P = [masthead(SUBJECT, UNIT, '抽離課堂檢測・教師卷'),
         para('本卷供教師批改使用，不發給學生。標準版（卷 S）與輔助版（卷 A）題目、數字、圖、'
              '分值完全相同，共用本答案與評分。滿分 30 分。', sz=22)]

    P.append(heading('一、參考答案與評分'))
    # ---- 一 ----
    P.append(para('第一大題　圓的基本概念（6 分）', bold=True, keep_next=True))
    ws = [int(W * f) for f in (0.08, 0.30, 0.10)]
    ws.append(W - sum(ws))
    rows = [{'hdr': True, 'cells': [hdr_cell('題', 'center'), hdr_cell('答案'), hdr_cell('分', 'center'),
                                     hdr_cell('說明（常見錯誤）')]}]
    ans1 = [('(1)', 'AB', '1', '只有 AB 經過圓心；CD、CE 是弦但不是直徑'),
            ('(2)', 'OA、OB、OC', '1', '三條都寫才給分。易錯：漏了 OA、OB（它們是直徑的一部分，也是半徑）'),
            ('(3)', '圓心角；圓周角', '2', '各 1 分。認角看頂點：∠BOC 頂點在圓心 O；∠DCE 頂點 C 在圓上'),
            ('(4)', '劣', '1', '{arc(DE)} 小於半圓（約 70° 的弧）'),
            ('(5)', '錯', '1', '弦的兩個端點都要在圓上；半徑只有一個端點 C 在圓上')]
    for a in ans1:
        rows.append([{'p': [tc(a[0], jc='center')], 'va': 'center'},
                     {'p': [tc(a[1], bold=True)], 'va': 'center'},
                     {'p': [tc(a[2], jc='center')], 'va': 'center'},
                     {'p': [c1.mc(a[3], sz=22)], 'va': 'center'}])
    P.append(_tbl(rows, ws))

    # ---- 二 ----
    P.append(para('第二大題　弧、弦、圓心角的關係（4 分）', bold=True, keep_next=True))
    P.append(key_table([
        eq_row('{∠COD}', '{∠AOB}', why('在同圓中，相等的弧所對的圓心角相等【理由 1 分】')),
        eq_row('{∠COD}', '{65°}', '【1 分】'),
        eq_row('{CD}', '{AB}', why('在同圓中，相等的弧所對的弦相等【理由 1 分】')),
        eq_row('{CD}', '4 cm', '【1 分】；漏單位不扣分，但要提醒'),
        answer_row('{∠COD=65°}，CD ＝ 4 cm', why=''),
    ]))
    P.append(para('※ 理由沒有寫「在同圓中」（或「在同圓或等圓中」）的，該理由分不給——'
                  '這是單元 08 修訂版講義第三節的重點（D14 兩個圓的反例）。', sz=22))
    P.append(para('※ 若班上未教「弧、弦、圓心角的關係」（兩班教案未排獨立課時），本大題不計分，滿分改為 26 分。',
                  sz=22, bold=True))

    # ---- 三 ----
    P.append(para('第三大題　圓周角定理（12 分）', bold=True, keep_next=True))
    P.append(para('(1)　（3 分）', keep_next=True))
    P.append(key_table([
        eq_row('{∠ACB}', '{frac(1,2)∠AOB}', why('同弧所對的圓周角是圓心角的一半', '【列式 1 分＋理由 1 分】')),
        eq_row('{∠ACB}', '{frac(1,2)×120°}', '代入'),
        eq_row('{∠ACB}', '{60°}', '【1 分】'),
        answer_row('{∠ACB=60°}', why='誘答：{240°}（乘 2，頂點認錯）'),
    ]))
    P.append(para('(2)　（3 分）', keep_next=True))
    P.append(key_table([
        eq_row('{∠ACB}', '{90°}', why('直徑所對的圓周角是直角', '【1 分＋理由 1 分】')),
        eq_row('{∠ABC}', '{180°-90°-35°}', '三角形內角和'),
        eq_row('{∠ABC}', '{55°}', '【1 分】'),
        answer_row('{∠ABC=55°}', why='誘答：{145°}（漏了 90°）'),
    ]))
    P.append(para('(3)　（3 分）', keep_next=True))
    P.append(key_table([
        eq_row('{∠ADB}', '{∠ACB}', '同弧所對的圓周角相等'),
        eq_row('{∠ADB}', '{70°}', '【1 分】'),
        eq_row('{∠AOB}', '{2∠ACB}', '同弧所對的圓心角是圓周角的 2 倍'),
        eq_row('{∠AOB}', '{2×70°}'),
        eq_row('{∠AOB}', '{140°}', '【1 分】'),
        answer_row('{∠ADB=70°}，{∠AOB=140°}', why='兩個理由都寫對【1 分】；誘答：{∠AOB=35°}'),
    ]))
    P.append(para('(4)　（3 分）', keep_next=True))
    P.append(key_table([
        span_row('小明不對。', '判斷【1 分】'),
        eq_row('{∠AOB}', '{2∠ACB}', why('圓心角是同弧所對圓周角的 2 倍', '【1 分】')),
        eq_row('{∠AOB}', '{2×40°}'),
        eq_row('{∠AOB}', '{80°}', '【1 分】'),
        answer_row('{∠AOB=80°}', why='小明錯在把「圓周角＝圓心角的一半」倒轉來用'),
    ]))

    # ---- 四 ----
    P.append(para('第四大題　圓內接四邊形（8 分）', bold=True, keep_next=True))
    P.append(para('(1)　（4 分）', keep_next=True))
    P.append(key_table([
        eq_row('{∠C}', '{180°-∠A}', why('圓內接四邊形的對角互補', '【1 分】')),
        eq_row('{∠C}', '{180°-75°}'),
        eq_row('{∠C}', '{105°}', '【1 分】'),
        eq_row('{∠D}', '{180°-∠B}', '對角互補【1 分】'),
        eq_row('{∠D}', '{180°-110°}'),
        eq_row('{∠D}', '{70°}', '【1 分】'),
        answer_row('{∠C=105°}，{∠D=70°}', why='誘答：{∠C=70°}、{∠D=105°}（把鄰角當對角）'),
    ]))
    P.append(para('(2)　（4 分）', keep_next=True))
    P.append(key_table([
        eq_row('{∠A}', '{frac(1,2)∠BOD}', why('同弧所對的圓周角是圓心角的一半', '【1 分】')),
        eq_row('{∠A}', '{frac(1,2)×140°}'),
        eq_row('{∠A}', '{70°}', '【1 分】'),
        eq_row('{∠C}', '{180°-∠A}', '圓內接四邊形的對角互補【1 分】'),
        eq_row('{∠C}', '{180°-70°}'),
        eq_row('{∠C}', '{110°}', '【1 分】'),
        answer_row('{∠A=70°}，{∠C=110°}', why='誘答：{∠C=70°}（以為 C 也對著 140°）'),
    ]))
    P.append(para('※ 第二至四大題：理由寫意思對即可（例如「同弧圓周角＝圓心角一半」），不要求一字不差；'
                  '只寫數字、沒有任何理由的，該題最多得一半分（向下取整）。', sz=22))

    # ---- 命題藍圖 ----
    P.append(heading('二、命題藍圖與作答時間', page_break_before=True))
    ws4 = [int(W * f) for f in (0.10, 0.40, 0.08, 0.12)]
    ws4.append(W - sum(ws4))
    blue = [('一', '圓心、半徑、弦、直徑、弧（優弧／劣弧）、圓心角、圓周角的辨認', '6', '約 4 分鐘',
             '講義 一、；練習 A1；兩班第 1 課時'),
            ('二', '在同圓中：等弧 → 等圓心角、等弦（含理由要寫「在同圓中」）', '4', '約 3 分鐘',
             '修訂版講義 三、「知一推二」卡；練習 A2、A3'),
            ('三', '圓周角定理；同弧圓周角相等；直徑所對圓周角是直角；改錯（倒用定理）', '12', '約 7 分鐘',
             '講義 四、；練習 B；乙 12/16、丙 12/11＋12/15'),
            ('四', '圓內接四邊形對角互補（含與圓周角定理綜合）', '8', '約 6 分鐘',
             '講義 五、；練習 C；乙 01/04、丙 12/15'),
            ('合計', '不考垂徑定理（丙班教案沒有此節，兩班交集不含）', '30', '約 20 分鐘', '')]
    rows = [{'hdr': True, 'cells': [hdr_cell('大題', 'center'), hdr_cell('考核內容'), hdr_cell('分值', 'center'),
                                     hdr_cell('建議時間'), hdr_cell('依據')]}]
    for b in blue:
        rows.append([{'p': [tc(b[0], jc='center', bold=True)], 'va': 'center'},
                     {'p': [tc(b[1])]}, {'p': [tc(b[2], jc='center')], 'va': 'center'},
                     {'p': [tc(b[3])], 'va': 'center'}, {'p': [tc(b[4])]}])
    P.append(_tbl(rows, ws4))
    P.append(para('※ 施測時間：兩班都教完圓內接四邊形之後（丙班 12/15、乙班 2027/01/04），即 2027/01/04 之後的抽離課。', sz=22))
    P.append(para('※ 題目數字全部新編，未與講義範例（100°、80°）、練習、額外評核 W16／W16 修訂版（40°、5）重複；'
                  '圖中各點位置按題目度數準確畫出（驗算檔附座標核對）。', sz=22))

    P.extend(teacher_notes(
        'D7 提示卡（定理文字＋圖＋符號）',
        aux_designs=('D2 手順卡（步驟格）', 'D14 錯誤分析對比（第三大題 (4) 改錯）'),
        reason='S5 幾何定理：融合生的瓶頸是「看圖時想不起用哪一條定理」與「理由寫不出」，'
               '而不是不會計算。卷 A 在每題旁放提示卡（認名稱／知一推二／圓周角定理／圓內接四邊形），'
               '題目下方的步驟格把「列式 → 代入 → 算出」拆開，右欄的理由改成填空。',
        density='抽離小班（兩版同題同分，屬調整支援 Accommodation，不是課程剪裁）',
        fading='本次卷 A：提示卡＋步驟格＋理由填空 → 下次：保留提示卡、步驟格只留等號、理由不再填空 → '
               '再下次：只給提示卡 → 回到卷 S。',
        iep_codes=('a3 提示題目重點', 'a6 增加行距或放大作答欄', 'a11 提供公式卡'),
        extra=[
            ('卷 A 鷹架位置',
             '第一大題：右側「提示卡：認名稱」。第二大題：「提示卡：知一推二」＋步驟格（理由填空）。'
             '第三大題：大題開頭「提示卡：圓周角定理」；(1)–(3) 步驟格（理由填空）；(4) 旁「想一想」兩問＋步驟格。'
             '第四大題：「提示卡：圓內接四邊形」；(2) 旁提示「∠A 和 ∠BOD 都對著弧 BCD」；兩題都有步驟格。'),
            ('卷 A 刻意不給的東西',
             '步驟格不預先寫出任何一步的結果；第一大題提示卡不提「直徑的一半也是半徑」（第 (2) 題的考點）；'
             '第三大題 (4) 只問「哪一個比較大」，不直接說「圓心角是圓周角的 2 倍」。'),
            ('批改提醒',
             '卷 A 學生在步驟格內寫的算式和填空的理由，按上面評分表同一標準給分。'),
        ]))
    save(P, f'{BASE}_教師卷.docx', '初三數學．抽離課堂檢測 02（教師卷）', M)


# ============================ 座標核對 ============================
def verify():
    def pt(deg):
        a = math.radians(deg)
        return (math.cos(a), math.sin(a))

    def ang(v, a, b):
        (vx, vy), (ax, ay), (bx, by) = v, a, b
        u = (ax - vx, ay - vy); w = (bx - vx, by - vy)
        c = (u[0] * w[0] + u[1] * w[1]) / (math.hypot(*u) * math.hypot(*w))
        return math.degrees(math.acos(max(-1, min(1, c))))

    def P_(key):
        return {k: pt(v[0]) for k, v in PTS[key].items()} | {'O': (0.0, 0.0)}

    p = P_('f1'); print('f1 ∠BOC', round(ang(p['O'], p['B'], p['C']), 2), '弧DE度數', 280 - 210)
    p = P_('f2'); print('f2 ∠AOB', round(ang(p['O'], p['A'], p['B']), 2), '∠COD', round(ang(p['O'], p['C'], p['D']), 2),
                        'AB', round(math.dist(p['A'], p['B']), 4), 'CD', round(math.dist(p['C'], p['D']), 4))
    p = P_('f3a'); print('f3a ∠AOB', round(ang(p['O'], p['A'], p['B']), 2), '∠ACB', round(ang(p['C'], p['A'], p['B']), 2))
    p = P_('f3b'); print('f3b ∠CAB', round(ang(p['A'], p['C'], p['B']), 2), '∠ACB', round(ang(p['C'], p['A'], p['B']), 2),
                         '∠ABC', round(ang(p['B'], p['A'], p['C']), 2))
    p = P_('f3c'); print('f3c ∠ACB', round(ang(p['C'], p['A'], p['B']), 2), '∠ADB', round(ang(p['D'], p['A'], p['B']), 2),
                         '∠AOB', round(ang(p['O'], p['A'], p['B']), 2))
    p = P_('f3d'); print('f3d ∠ACB', round(ang(p['C'], p['A'], p['B']), 2), '∠AOB', round(ang(p['O'], p['A'], p['B']), 2))
    p = P_('f4a'); print('f4a ∠A', round(ang(p['A'], p['B'], p['D']), 2), '∠B', round(ang(p['B'], p['A'], p['C']), 2),
                         '∠C', round(ang(p['C'], p['B'], p['D']), 2), '∠D', round(ang(p['D'], p['A'], p['C']), 2))
    p = P_('f4b'); print('f4b ∠BOD(含C那邊)', 360 - 220, '∠A', round(ang(p['A'], p['B'], p['D']), 2),
                         '∠C', round(ang(p['C'], p['B'], p['D']), 2))


if __name__ == '__main__':
    if '--verify' in sys.argv:
        verify()
    else:
        build_standard()
        build_assist()
        build_teacher()
        print('OK')
