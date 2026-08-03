# -*- coding: utf-8 -*-
# 練習（A/B/C三層＋答案）—— 定積分（13.3 概念與計算 + 13.4 幾何應用，精簡2節版）
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '定積分（概念、計算與幾何應用）'
FOOTER = '高三數學．定積分單元'

Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('作答前，先回頭看《課堂講義》的公式卡與「我做／我們做」範例。每題都把逐步算式寫出來，不要跳步。'))

# ---------------- 練習A（★☆☆）—— 已完成範例並排對照 ----------------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(shaded_box('範例（已完成，對照右邊自己填）：{∫[0,1] 2x dx=F(1)−F(0)=1−0=1}　　（F(x)=x²）', kind='worked'))
Q.append(problem_box(
    [para('1．求 {∫[0,2] x dx}（提示：F(x)=x²/2）')] + write_lines(3)
))
Q.append(problem_box(
    [para('2．求 {∫[1,2] 3 dx}（提示：常數函數，F(x)=3x）')] + write_lines(3)
))

# ---------------- 練習B（★★☆）—— 手順卡精簡版放區塊開頭一次 ----------------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(step_card(
    '求定積分的四個步驟（精簡版，做題時對照）',
    ['求原函數——套不定積分公式卡，不用加C', '代入上限——把上限的數代入原函數',
     '代入下限——把下限的數代入原函數', '相減——上限的值減下限的值，就是答案'],
    compact=True,
))
Q.append(problem_box(
    [para('3．求 {∫[0,2] (3x^2−2x+1) dx}')] + write_lines(5)
))
Q.append(problem_box(
    [para('4．求由 {y=x^2+1}、{x=0}、{x=1}、x軸所圍的面積 S。'),
     shaded_box('提示：先寫出 {S=∫[0,1] (x^2+1) dx}，再照步驟計算。')]
    + write_lines(5)
))

# ---------------- 練習C（★★★）—— 保留但降低開放度 ----------------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box(
    [para('5．求由 {y=x} 與 {y=x^2} 所圍的面積（在 [0,1] 之間，這段 x≥x²）。'),
     shaded_box('提示：面積 {S=∫[0,1] (x−x^2) dx}')]
    + write_lines(5)
))
Q.append(problem_box(
    [para('6．錯誤分析：某同學求「{y=x} 在 {[−1,1]} 與x軸所圍的面積」時，直接計算 {∫[−1,1] x dx=(frac(1,2))−(frac(1,2))=0}，得出面積是0。'),
     para('請你用自己的話說明：這位同學錯在哪一步？正確的面積應該怎麼算？')]
    + write_lines(6),
    trailing_blank=False,
))

# ---------------- 參考答案（教師用，分頁） ----------------
Q.append(heading('參考答案（教師用）', page_break_before=True))
Q.append(para('1．{∫[0,2] x dx=2}。'))
Q.append(para('2．{∫[1,2] 3 dx=3}。'))
Q.append(para('3．{∫[0,2] (3x^2−2x+1) dx=6}。'))
Q.append(para('4．{S=∫[0,1] (x^2+1) dx=frac(4,3)}。'))
Q.append(para('5．{S=∫[0,1] (x−x^2) dx=frac(1,6)}。'))
Q.append(para('6．錯在：{y=x} 在 {[−1,0]} 是負的（圖形在x軸下方），在 {[0,1]} 是正的（圖形在x軸上方）。直接整段積分'
             '正負會互相抵消，算出來的是「帶正負號的淨變化量」，不是面積。求面積要先分段、負的部份取絕對值再相加：'
             '{S=∫[−1,0]|x|dx+∫[0,1] x dx=frac(1,2)+frac(1,2)=1}。（幾何驗證：兩個直角三角形，每個面積1/2，共1）'))

out2 = build_docx(Q, os.path.join(OUT, '練習_定積分_抽離小班共用版.docx'), footer_text=FOOTER)
print(out2)
