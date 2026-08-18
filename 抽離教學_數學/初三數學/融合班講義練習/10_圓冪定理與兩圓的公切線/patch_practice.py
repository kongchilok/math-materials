# -*- coding: utf-8 -*-
"""在《練習_圓冪定理與兩圓的公切線_融合版.docx》原有練習 A／B／C（第 1～8 題）之後、
參考答案之前，插入「四、公切線長度」共 2 題，並在答案頁末補上第 9～10 題的教師參考答案。

對應講義新增的「四、兩圓的公切線長度」（同一份 patch_common.py 手法，2026-08-18）。
第 1～8 題與原有「參考答案（教師用）」一個字不改。

三層鷹架密度必須有差（house-style）：
  4-A ★★☆　直接代公式（跟練習B 同級：給齊 R、r、d，套外公切線公式）
  4-B ★★★　三問合一（先判位置關係、再分別求外／內公切線——呼應概念框
             「內公切線只喺 d＞R+r 先有」，逼學生自己判斷兩條公式都用得到）

數值全部揀過乾淨嘅畢氏三數，驗算見同資料夾 驗算_圓冪定理與兩圓的公切線.md：
  第9題：R=13、r=4、d=15 → R−r=9 → L=√(15²−9²)=√144=12
  第10題：R=11、r=4、d=25 → R−r=7、R+r=15 → 外公切線=√(25²−7²)=√576=24；
          內公切線=√(25²−15²)=√400=20（d=25＞R+r=15，外離，兩種公切線都有）
"""
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from patch_common import *      # noqa: F401,F403
from patch_common import seeded_registry, patch, guard

DOCX = os.path.join(HERE, '練習_圓冪定理與兩圓的公切線_融合版.docx')
guard(DOCX, '四、公切線長度')

media, N_SEED = seeded_registry([])          # 原練習檔沒有圖，rIdImg1 起（其實用不到）

# ==================== 新練習區塊 ====================
P = []
P.append(heading('四、公切線長度', page_break_before=True))
P.append(shaded_box('提示：外公切線長 {L=sqrt(d^2-(R-r)^2)}；內公切線長 '
                    '{L=sqrt(d^2-(R+r)^2)}（只喺兩圓外離，即 d＞R+r 時先有）。'))

P.append(heading(f'4-A　套用公式（{star_label(2)}）'))
P.append(problem_box([
    para('9．兩圓半徑 R=13、r=4，圓心距 d=15，求外公切線的長度。'),
] + write_lines(3)))

P.append(heading(f'4-B　綜合運用（{star_label(3)}）'))
P.append(problem_box([
    para('10．兩圓半徑 R=11、r=4，圓心距 d=25。（1）判斷兩圓的位置關係；'
        '（2）求外公切線的長度；（3）求內公切線的長度。'),
] + write_lines(6), trailing_blank=False))

new_section = ''.join(P)

# ==================== 參考答案（接在原答案之後） ====================
A = []
A.append(heading('公切線長度（第 9～10 題）'))
A.append(para('9．{R-r=13-4=9}；{L^2=d^2-(R-r)^2=15^2-9^2=225-81=144} → '
             '{L=12}（外公切線長 12）。'))
A.append(para('10．(1) {R+r=11+4=15}，{d=25}＞15 → 兩圓外離（外、內公切線都存在）。'
             '(2) 外公切線：{L^2=d^2-(R-r)^2=25^2-7^2=625-49=576} → {L=24}。'
             '(3) 內公切線：{L^2=d^2-(R+r)^2=25^2-15^2=625-225=400} → {L=20}。'))
answers = ''.join(A)

# ==================== 插入 ====================
with zipfile.ZipFile(DOCX) as z:
    xml = z.read('word/document.xml').decode('utf-8')

# 參考答案前面有一個獨立的分頁段落，要插在那個分頁之前（沿用 06 同一手法）
PB = ('<w:p><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr>'
      '<w:r><w:br w:type="page"/></w:r></w:p>')
assert xml.count(PB) == 1, f'分頁段落不是唯一（{xml.count(PB)} 個），錨點要重挑'
pos_section = xml.index(PB)
pos_answers = xml.index('<w:sectPr>')

patch(DOCX, DOCX, [(pos_section, new_section), (pos_answers, answers)], media, N_SEED)
sys.stdout.buffer.write(('OK ' + DOCX + ' figs: ' + str(len(media.items) - N_SEED) + '\n').encode('utf-8'))
