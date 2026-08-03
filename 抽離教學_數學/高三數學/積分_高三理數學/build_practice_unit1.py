# -*- coding: utf-8 -*-
# 練習（A/B/C三層＋答案）—— 不定積分（13.1 定義 + 13.2 運算法則）
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '不定積分（定義與運算法則）'
FOOTER = '高三數學．不定積分單元'

Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('作答前，先回頭看《課堂講義》的公式卡與「我做／我們做」範例。每題都把逐步算式寫出來，不要跳步。'))

# ---------------- 練習A（★☆☆）—— 已完成範例並排對照 ----------------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(shaded_box("範例（已完成，對照右邊自己填）：已知 {(x^6)'=6x^5}，所以 {∫6x^5 dx=x^6+C}", kind='worked'))
Q.append(problem_box(
    [para("1．已知 {(x^7)'=7x^6}，所以 {∫7x^6 dx=?}")] + write_lines(2)
))
Q.append(problem_box(
    [para('2．求 {∫x^3 dx}（套用公式卡第2條：n=3，n+1=？）')] + write_lines(2)
))

# ---------------- 練習B（★★☆）—— 手順卡精簡版放區塊開頭一次 ----------------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(step_card(
    '求不定積分的四個步驟（精簡版，做題時對照）',
    ['拆項——看清楚是幾項相加減', '提係數——常數倍法則，把係數整個提出來',
     '套公式——查講義公式卡', '合併——只加一個C'],
    compact=True,
))
Q.append(problem_box(
    [para('3．求 {∫(①3x^2②−2x③+5) dx}（已標好①②③三項，對照步驟做）')] + write_lines(5)
))
Q.append(problem_box(
    [para('4．求 {∫(①4e^x②+fn(cos) x) dx}')] + write_lines(5)
))

# ---------------- 練習C（★★★）—— 保留但降低開放度 ----------------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box(
    [para("5．已知 {F'(x)=6x^2−4x+1}，且 {F(0)=3}，求 F(x)。"),
     shaded_box('提示：先求出「一般解」（含C的式子），再代入 F(0)=3 求出 C 的值。')]
    + write_lines(5)
))
Q.append(problem_box(
    [para('6．錯誤分析：某同學求 {∫x^{−1} dx} 時，直接套公式卡第2條，寫成 {∫x^{−1} dx=frac(x^0,0)+C}。'),
     para('請你用自己的話說明：這位同學錯在哪一步？公式卡第2條有什麼限制被他忽略了？正確答案應該是什麼？')]
    + write_lines(5),
    trailing_blank=False,
))

# ---------------- 參考答案（教師用，分頁） ----------------
Q.append(heading('參考答案（教師用）', page_break_before=True))
Q.append(para("1．{(x^7)'=7x^6}，所以 {∫7x^6 dx=x^7+C}。"))
Q.append(para('2．{∫x^3 dx=frac(x^4,4)+C}（n=3，n+1=4）。'))
Q.append(para('3．{∫(3x^2−2x+5) dx=x^3−x^2+5x+C}。'))
Q.append(para('4．{∫(4e^x+fn(cos) x) dx=4e^x+fn(sin) x+C}。'))
Q.append(para('5．一般解：{F(x)=2x^3−2x^2+x+C}；代入 {F(0)=3} 得 {C=3}；所以 {F(x)=2x^3−2x^2+x+3}。'))
Q.append(para('6．錯在：公式卡第2條 {∫x^n dx=frac(x^{n+1},n+1)+C} 限定「n≠−1」，因為 n=−1 時分母 n+1=0，除以零無意義，'
             '所以不能直接套用這條公式。本題 n=−1，被積函數其實是 {frac(1,x)}，應改用公式卡第3條：'
             '{∫x^{−1} dx=∫frac(1,x) dx=fn(ln)|x|+C}。'))

out2 = build_docx(Q, os.path.join(OUT, '練習_不定積分_抽離小班共用版.docx'), footer_text=FOOTER)
print(out2)
