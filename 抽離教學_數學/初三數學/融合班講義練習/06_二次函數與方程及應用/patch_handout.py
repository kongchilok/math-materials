# -*- coding: utf-8 -*-
"""在《講義_二次函數與方程及應用_融合版.docx》的 §二 之後、練習指示句之前，
插入新的「三、圖像法解一元二次不等式」（丙班加節，2026/11/12）。

主設計 D5 圖文雙軌對照（左草圖右讀法，逐步橫向對齊）
輔設計 D2 手順卡（畫草圖 → 標兩交點 → 看開口 → 讀區間）
§一、§二 原有內容一字不改。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from patch_common import *      # noqa: F401,F403
from patch_common import (seeded_registry, para_start, patch, guard,
                          _tbl, _PAGE_CONTENT_WIDTH)
import design_svg as ds

FIGS = os.path.join(HERE, 'figs')
os.makedirs(FIGS, exist_ok=True)
DOCX = os.path.join(HERE, '講義_二次函數與方程及應用_融合版.docx')
guard(DOCX, '三、圖像法解一元二次不等式')

W = 300          # 側欄／雙軌左欄用的原生寬度（house-style：不要拿大圖硬縮）
H = 158


def fig(name, svg):
    p = os.path.join(FIGS, name)
    ds.svg_to_png(svg, p)
    return p


# ---------------- 圖：範例一 四步（草圖逐步長出資訊） ----------------
f_step1 = fig('h3_s1.png', ds.sketch_parabola(roots=('', ''), opening='up', width=W, height=H))
f_step2 = fig('h3_s2.png', ds.sketch_parabola(roots=('−1', '3'), opening='up', width=W, height=H))
f_step3 = fig('h3_s3.png', ds.sketch_parabola(roots=('−1', '3'), opening='up', width=W, height=H,
                                              show_sign=True))
f_step4 = fig('h3_s4.png', ds.sketch_parabola(roots=('−1', '3'), opening='up', width=W, height=H,
                                              solution='outside'))
f_ex2 = fig('h3_ex2.png', ds.sketch_parabola(roots=('−1', '3'), opening='up', width=W, height=H,
                                             solution='inside'))

# ---------------- 圖：決策表 4 格（p ＜ q 是兩個根） ----------------
DW, DH = 210, 112
f_d1 = fig('h3_d1.png', ds.sketch_parabola(roots=('p', 'q'), opening='up', width=DW, height=DH,
                                           solution='outside'))
f_d2 = fig('h3_d2.png', ds.sketch_parabola(roots=('p', 'q'), opening='up', width=DW, height=DH,
                                           solution='inside'))
f_d3 = fig('h3_d3.png', ds.sketch_parabola(roots=('p', 'q'), opening='down', width=DW, height=DH,
                                           solution='inside'))
f_d4 = fig('h3_d4.png', ds.sketch_parabola(roots=('p', 'q'), opening='down', width=DW, height=DH,
                                           solution='outside'))

media, N_SEED = seeded_registry(['rIdImg1', 'rIdImg2'])   # 原檔兩張圖先佔位

# ==================== 組裝 §三 ====================
P = []
P.append(heading('三、圖像法解一元二次不等式', page_break_before=True))
P.append(para('一元二次不等式 {ax^2+bx+c>0}，其實是在問：拋物線 {y=ax^2+bx+c} 的哪一段在 x 軸上方。'
              '所以不用死背公式——畫一幅草圖，答案就在圖上讀得出來。'))

_cw = int(_PAGE_CONTENT_WIDTH * 0.46)
P.append(_tbl([
    {'hdr': True, 'cells': [{'p': [para('拋物線的位置', bold=True, sz=22)], 'shd': GREY_FILL},
                            {'p': [para('對應的式子', bold=True, sz=22)], 'shd': GREY_FILL}]},
    {'cells': [[para('在 x 軸上方')], [para('{ax^2+bx+c>0}')]]},
    {'cells': [[para('剛好在 x 軸上（就是兩個交點）')], [para('{ax^2+bx+c=0}')]]},
    {'cells': [[para('在 x 軸下方')], [para('{ax^2+bx+c<0}')]]},
], [_cw, _PAGE_CONTENT_WIDTH - _cw]))

# ---- D2 手順卡 ----
P.append(step_card(
    '手順卡：圖像法解一元二次不等式',
    [('畫草圖：先把不等號換成等號，解 {ax^2+bx+c=0} 求兩個根',
      '換成等號只是為了求交點，這一步還未解完不等式'),
     ('標兩交點：把兩個根由小到大標在 x 軸上',
      '一定要由小到大排，排反了讀出來的區間就相反'),
     ('看開口：看 {x^2} 的係數 a 是正還是負',
      '{-x^2+4x-3} 的 a 是 −1，不是 1'),
     ('讀區間：要 {y>0} 讀 x 軸上方那幾段，要 {y<0} 讀下方那一段',
      '分開兩段的答案中間要寫「或」；中間一段寫成 p ＜ x ＜ q')],
    trigger='題目出現 ＞ 或 ＜，而式子裡有 {x^2} 時',
))

# ---- 範例一：＞ 0 ----
P.append(shaded_box('範例一：解不等式 {x^2-2x-3>0}（延續 §一 用過的 {y=x^2-2x-3}）',
                    keep_next=True))
P.append(para('第一步（代數）：把不等號換成等號，先求出兩個根。', keep_next=True))
P.append(worked_example_table([
    eq_row('{x^2-2x-3}', '{0}', rel='{>}', why='原不等式：問「y 大於 0」的 x 有哪些'),
    eq_row('{x^2-2x-3}', '{0}', rel='{=}', why='① 把不等號換成等號——這一步只求與 x 軸的交點'),
    eq_row('{(x-3)(x+1)}', '{0}', why='因式分解'),
    or_row('{x-3}', '{0}', '{x+1}', '{0}', why='兩個因式各自等於 0，分兩支寫'),
    or_row('{x_1}', '{3}', '{x_2}', '{-1}', why='各自解出來'),
    answer_row('{x_1=3} 或 {x_2=-1}',
               why='這是兩個交點的橫坐標，還不是不等式的解集；畫圖時由小到大排成 −1、3'),
], why_pct=0.36))

P.append(para('第二步（讀圖）：把兩個根畫上草圖，答案就在圖上。', keep_next=True))
P.append(dual_track_table([
    (image_para(f_step1, width_cm=7.4),
     [para('① 畫草圖', bold=True),
      para('{a=1>0} → 開口向上'),
      para('§一 已算出 {Δ=16>0} → 與 x 軸有兩個交點'),
      para('草圖只需要三件事：開口方向、與 x 軸交幾個點、根在哪裡')]),
    (image_para(f_step2, width_cm=7.4),
     [para('② 標兩交點', bold=True),
      para('把第一步求得的根由小到大標上：'),
      para('　左邊 x ＝ −1，右邊 x ＝ 3')]),
    (image_para(f_step3, width_cm=7.4),
     [para('③ 看開口', bold=True),
      para('開口向上 → 兩根之外的部分在 x 軸上方，那裡 {y>0}'),
      para('兩根之間的部分在 x 軸下方，那裡 {y<0}')]),
    (image_para(f_step4, width_cm=7.4),
     [para('④ 讀區間', bold=True),
      para('要 {x^2-2x-3>0}，即是要 {y>0} → 讀 x 軸上方那兩段'),
      para('端點 −1 和 3 令 y ＝ 0，不合 ＞ 0，所以畫空心圈、不包括'),
      para('∴ 解集：{x<-1} 或 {x>3}', bold=True)]),
], media=media, headers=('草圖上看到什麼', '就讀成／寫成什麼')))

# ---- 範例二：＜ 0 ----
P.append(shaded_box('範例二：同一條拋物線，解 {x^2-2x-3<0}', keep_next=True,
                    page_break_before=True))
P.append(para('前三步（畫草圖、標兩交點、看開口）與範例一完全一樣，只有第 ④ 步不同。',
              keep_next=True))
P.append(dual_track_table([
    (image_para(f_ex2, width_cm=7.4),
     [para('④ 讀區間', bold=True),
      para('這次要 {y<0} → 讀 x 軸下方那一段'),
      para('那一段夾在兩個根之間，只有一段，所以不用寫「或」'),
      para('∴ 解集：{-1<x<3}', bold=True)]),
], media=media, headers=('草圖上看到什麼', '就讀成／寫成什麼')))

# ---- 不等號方向與開口的關係（決策表） ----
P.append(heading('不等號方向與開口的關係'))
P.append(shaded_box('⚠ 開口一變，答案的形狀就反過來——「取兩邊」與「取中間」對調。'
                    '所以第 ③ 步「看開口」不能跳過。'))
P.append(para('下表的 p、q 是兩個根，而且 p ＜ q（本表只講與 x 軸有兩個交點的情況）。'))

_w1 = int(_PAGE_CONTENT_WIDTH * 0.15)
_w2 = int(_PAGE_CONTENT_WIDTH * 0.22)
_w3 = int(_PAGE_CONTENT_WIDTH * 0.29)
_dwidths = [_w1, _w2, _w3, _PAGE_CONTENT_WIDTH - _w1 - _w2 - _w3]


def _drow(a_txt, open_txt, ineq, png, ans, how):
    return {'cells': [{'p': [para(a_txt, sz=22, spacing=False),
                             para(open_txt, sz=22, spacing=False)], 'va': 'center'},
                      {'p': [para(ineq)], 'va': 'center'},
                      {'p': [expand_image(image_para(png, width_cm=5.1), media)],
                       'va': 'center'},
                      {'p': [para(ans, sz=22, spacing=False),
                             para(how, sz=22, spacing=False)], 'va': 'center'}]}


P.append(_tbl([
    {'hdr': True, 'cells': [{'p': [para(h, bold=True, sz=22)], 'shd': GREY_FILL}
                            for h in ('開口', '不等式', '草圖', '解集（取哪一段）')]},
    _drow('{a>0}', '開口向上', '{ax^2+bx+c>0}', f_d1, 'x ＜ p 或 x ＞ q', '（取兩邊）'),
    _drow('{a>0}', '開口向上', '{ax^2+bx+c<0}', f_d2, 'p ＜ x ＜ q', '（取中間）'),
    _drow('{a<0}', '開口向下', '{ax^2+bx+c>0}', f_d3, 'p ＜ x ＜ q', '（取中間）'),
    _drow('{a<0}', '開口向下', '{ax^2+bx+c<0}', f_d4, 'x ＜ p 或 x ＞ q', '（取兩邊）'),
], _dwidths))

P.append(shaded_box('看得出規律嗎：開口向上配 ＞ 0、開口向下配 ＜ 0 → 取兩邊；'
                    '一上一下配不起來 → 取中間。'))
P.append(shaded_box('不過規律只是核對用的——考試時仍然畫草圖，圖畫對了就不會記錯。'))

new_section = ''.join(P)

# ==================== 教師實施說明頁（放在全份最後） ====================
TN = ''.join(teacher_notes(
    main_design='D5 圖文雙軌對照（本頁只說明新增的 §三，§一、§二 為原有內容）',
    aux_designs=['D2 手順卡（畫草圖 → 標兩交點 → 看開口 → 讀區間）'],
    reason='§三 屬 S4 函數與圖像：瓶頸是「代數的不等號」與「圖上的哪一段」對不起來，'
           '學生背「大於取兩邊」而不知道為什麼，開口一變就全錯。'
           'D5 用左草圖右讀法逐步橫向對齊，每一步的代數判斷立刻在左邊看到對應的圖形事實；'
           'D2 把四步流程物理化，配合本節唯一要記的固定程序。'
           '對應教案 2026/11/12（四）「圖像法解一元二次不等式」，只丙班上。',
    density='抽離小班',
    fading='手順卡：講義內完整四步＋易錯點（4-A 題旁重印全文）→ 4-A 第 10 題只留關鍵詞與填空 → '
           '4-B 只寫步驟名 → 4-C 完全不放，學生自己數「這題有四步」。'
           '草圖：練習 4-A／4-B 第 11 題圖已畫好並標交點 → 4-B 第 12 題只給虛線空框 → '
           '4-C 只給空框、不給任何提示 → 最終在草稿紙上自畫。',
    flows=['F5 課前流程預告（今天一件事：把不等號讀成「拋物線在 x 軸的哪一邊」）',
           'F1 師徒制對話四步（教師先示範第 ③ 步的自問：「a 是正還是負？」）'],
    iep_codes=['a3 提示題目重點', 'a6 增加行距／放大作答欄'],
))

# ==================== 插入 ====================
import zipfile
with zipfile.ZipFile(DOCX) as z:
    xml = z.read('word/document.xml').decode('utf-8')

pos_section = para_start(xml, '接下來請拿本單元《課堂練習》，完成練習 A、B、C。')
pos_tail = xml.index('<w:sectPr>')

patch(DOCX, DOCX, [(pos_section, new_section), (pos_tail, TN)], media, N_SEED)
print('OK', DOCX, 'figs:', len(media.items) - N_SEED)
