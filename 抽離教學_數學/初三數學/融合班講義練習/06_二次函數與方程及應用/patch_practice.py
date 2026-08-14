# -*- coding: utf-8 -*-
"""在《練習_二次函數與方程及應用_融合版.docx》原有練習 A／B／C 之後、參考答案之前，
插入「四、圖像法解一元二次不等式（丙班加節）」共 5 題（由圖讀解集 3 題＋由式畫圖
再讀解集 2 題），並在答案頁末補上第 9～13 題的教師參考答案。

三層鷹架密度必須有差（house-style 2026-08-07）：
  4-A ★☆☆  圖已畫好並標交點 ＋ 四步提示全文（第 10 題起改成半填空）
  4-B ★★☆  第 11 題圖已給但提示只剩關鍵詞；第 12 題只給虛線空框＋步驟名
  4-C ★★★  只給虛線空框，不放任何提示
"""
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from patch_common import *      # noqa: F401,F403
from patch_common import seeded_registry, para_start, patch, guard
import design_svg as ds

FIGS = os.path.join(HERE, 'figs')
os.makedirs(FIGS, exist_ok=True)
DOCX = os.path.join(HERE, '練習_二次函數與方程及應用_融合版.docx')
guard(DOCX, '四、圖像法解一元二次不等式')

W, H = 300, 158


def fig(name, svg):
    p = os.path.join(FIGS, name)
    ds.svg_to_png(svg, p)
    return p


f_q9 = fig('p9.png', ds.sketch_parabola(roots=('−2', '1'), opening='up', width=W, height=H))
f_q10 = fig('p10.png', ds.sketch_parabola(roots=('1', '4'), opening='up', width=W, height=H))
f_q11 = fig('p11.png', ds.sketch_parabola(roots=('−1', '3'), opening='down', width=W, height=H))
f_blank12 = fig('p12.png', ds.sketch_parabola(blank=True, width=W, height=200))
f_blank13 = fig('p13.png', ds.sketch_parabola(blank=True, width=W, height=200))

media, N_SEED = seeded_registry([])          # 原練習檔沒有圖，rIdImg1 起

# ==================== 新練習區塊 ====================
P = []
P.append(heading('四、圖像法解一元二次不等式（丙班加節）', page_break_before=True))
P.append(shaded_box('固定四步：畫草圖 → 標兩交點 → 看開口 → 讀區間。'
                    '不肯定就先看《課堂講義》§三 的範例一。'))

# ---- 4-A ★☆☆ 由圖讀解集 ----
P.append(heading(f'4-A　由圖讀解集（{star_label(1)}）'))
P.append(aside_layout(
    [para('9．右圖是 {y=x^2+x-2} 的草圖，它與 x 軸交於 x ＝ −2 及 x ＝ 1。'),
     para('由圖寫出 {x^2+x-2<0} 的解集。')] + write_lines(3),
    [image_para(f_q9, width_cm=7.4, caption='圖：y = x²+x−2'),
     *hint_lines(['① 畫草圖：圖已經畫好',
                  '② 標兩交點：−2 和 1',
                  '③ 看開口：a ＝ 1 ＞ 0，開口向上',
                  '④ 讀區間：要 y ＜ 0，讀 x 軸下方那一段'],
                 title='四步手順')],
    media=media, boxed=True))
P.append(blank())

P.append(aside_layout(
    [para('10．右圖是 {y=x^2-5x+4} 的草圖，它與 x 軸交於 x ＝ 1 及 x ＝ 4。'),
     para('由圖寫出 {x^2-5x+4>0} 的解集。')] + write_lines(3),
    [image_para(f_q10, width_cm=7.4, caption='圖：y = x²−5x+4'),
     *hint_lines(['① 畫草圖：圖已經畫好',
                  '② 標兩交點：＿＿ 和 ＿＿',
                  '③ 看開口：a ＝ ＿＿，開口向＿＿',
                  '④ 讀區間：要 y ＿ 0，讀 x 軸＿＿方'],
                 title='四步手順（自己填）')],
    media=media, boxed=True))
P.append(blank())

# ---- 4-B ★★☆ ----
P.append(heading(f'4-B　由圖讀解集與由式畫圖（{star_label(2)}）'))
P.append(aside_layout(
    [para('11．右圖是 {y=-x^2+2x+3} 的草圖，它與 x 軸交於 x ＝ −1 及 x ＝ 3。'),
     para('（1）寫出 {-x^2+2x+3>0} 的解集。')] + write_lines(2)
    + [para('（2）寫出 {-x^2+2x+3<0} 的解集。')] + write_lines(2),
    [image_para(f_q11, width_cm=7.4, caption='圖：y = −x²+2x+3'),
     *hint_lines(['先看 a 是正還是負', '再決定「取兩邊」還是「取中間」'], title='提示')],
    media=media, boxed=True))
P.append(blank())

P.append(aside_layout(
    [para('12．解不等式 {x^2-x-6>0}。'),
     para('先在右邊的虛線框內畫草圖、標出兩個交點，再讀出解集。')] + write_lines(5),
    [image_para(f_blank12, width_cm=7.4, caption='作圖區'),
     *hint_lines(['① 畫草圖　② 標兩交點', '③ 看開口　④ 讀區間'], title='四步')],
    media=media, boxed=True))
P.append(blank())

# ---- 4-C ★★★ ----
P.append(heading(f'4-C　由式畫圖再讀解集（{star_label(3)}）'))
P.append(aside_layout(
    [para('13．解不等式 {-x^2+4x-3>0}。'),
     para('先在右邊的虛線框內畫草圖，再讀出解集；'
          '並用一句話說明：開口方向如何決定你讀哪一段。')] + write_lines(6),
    [image_para(f_blank13, width_cm=7.4, caption='作圖區')],
    media=media, boxed=True))

new_section = ''.join(P)

# ==================== 參考答案（接在原答案之後） ====================
A = []
A.append(heading('圖像法解一元二次不等式（第 9～13 題）'))
A.append(para('9．−2 ＜ x ＜ 1　（a ＝ 1 ＞ 0 開口向上，要 y ＜ 0 → 取兩根之間）'))
A.append(para('10．x ＜ 1 或 x ＞ 4　（開口向上，要 y ＞ 0 → 取兩根之外）'))
A.append(para('11．(1) −1 ＜ x ＜ 3　(2) x ＜ −1 或 x ＞ 3　'
              '（a ＝ −1 ＜ 0 開口向下，讀法與開口向上剛好相反）'))
A.append(para('12．{x^2-x-6=0} → {(x-3)(x+2)=0} → 兩根 −2、3；'
              'a ＝ 1 ＞ 0 開口向上，要 y ＞ 0 取兩根之外 → 解集 x ＜ −2 或 x ＞ 3。'))
A.append(para('13．{-x^2+4x-3=0} → 兩邊乘 −1 得 {x^2-4x+3=0} → {(x-1)(x-3)=0} → 兩根 1、3；'
              'a ＝ −1 ＜ 0 開口向下，圖在 x 軸上方的只有兩根之間那一段 → 解集 1 ＜ x ＜ 3。'))
A.append(para('　說明句參考：開口向下時拋物線只有中間一段升到 x 軸上方，'
              '所以 ＞ 0 取中間；開口向上則相反。'))
answers = ''.join(A)

# ==================== 插入 ====================
with zipfile.ZipFile(DOCX) as z:
    xml = z.read('word/document.xml').decode('utf-8')

# 參考答案前面有一個獨立的分頁段落，要插在那個分頁之前
PB = ('<w:p><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr>'
      '<w:r><w:br w:type="page"/></w:r></w:p>')
assert xml.count(PB) == 1, f'分頁段落不是唯一（{xml.count(PB)} 個），錨點要重挑'
pos_section = xml.index(PB)
pos_answers = xml.index('<w:sectPr>')

patch(DOCX, DOCX, [(pos_section, new_section), (pos_answers, answers)], media, N_SEED)
print('OK', DOCX, 'figs:', len(media.items) - N_SEED)
