# -*- coding: utf-8 -*-
"""Unit 1：矩陣的概念與運算 —— 融合班三層共用版（講義＋練習 docx）。
矩陣式一律用共用底層 omml_core 的 {mat(...;...)} / {det(...)} 標記。
本教材沿用原稿慣例：橫排＝行(row)、直行＝列(column)。"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '矩陣（概念與運算）'
FOOTER = '高三數學．矩陣：概念與運算'

# ================= 講義 =================
P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、矩陣是什麼'))
P.append(para('把一堆數字排成長方形的表，再用中括號框住，就是一個「矩陣」。'))
P.append(para('橫的一排叫「行(row)」，直的一列叫「列(column)」。有 m 行、n 列的矩陣，稱為 m×n 階矩陣。'))
P.append(para('例如 {A=mat(3,-1,0;2,5,-4)} 有 2 橫行、3 直列，所以 A 是 2×3 階矩陣。'))
P.append(shaded_box('關鍵詞：元素 {a_ij}＝第 i 行、第 j 列那個數。上例中 {a_21=2}（第 2 行第 1 列）、{a_13=0}（第 1 行第 3 列）。'))
P.append(para('幾個常見的特殊矩陣：'))
P.append(para('．零矩陣：所有元素都是 0。　　．單位矩陣 {I}：對角線都是 1、其餘都是 0，例如 {mat(1,0;0,1)}。'))
P.append(para('．轉置矩陣 {A^T}：把「行」和「列」互換（橫的變直、直的變橫）。'))

P.append(heading('二、範例1：加法與減法（同階才可以做）'))
P.append(para('設 {A=mat(2,-1;3,4)}，{B=mat(1,5;-2,0)}，求 {A+B} 與 {A-B}。'))
P.append(shaded_box('步驟：①先看階數是否相同（都是 2×2，可以做）②同一格對同一格，逐格相加或相減。'))
P.append(para('{A+B=mat(2+1,-1+5;3+(-2),4+0)=mat(3,4;1,4)}'))
P.append(para('{A-B=mat(2-1,-1-5;3-(-2),4-0)=mat(1,-6;5,4)}'))

P.append(heading('三、範例2：數乘（一個數乘整個矩陣）'))
P.append(para('設 {A=mat(3,-2;1,4)}，求 {-2A}。'))
P.append(shaded_box('步驟：把矩陣裡「每一格」都乘上那個數。'))
P.append(para('{-2A=mat(-2*3,-2*(-2);-2*1,-2*4)=mat(-6,4;-2,-8)}'))

P.append(heading('四、範例3：矩陣乘法（最重要，跟著四步驟做）'))
P.append(para('設 {A=mat(1,2;3,-1)}，{B=mat(2,0;1,4)}，求 {AB}。'))
P.append(shaded_box('四步驟：①看階數：(2×2)·(2×2)，中間兩數相同 → 可以乘，答案是 2×2。'
                    '②答案第 i 行第 j 列＝A 的「第 i 橫行」對上 B 的「第 j 直列」，對應相乘再相加。'))
P.append(para('{c_11=1*2+2*1=4}　　{c_12=1*0+2*4=8}'))
P.append(para('{c_21=3*2+(-1)*1=5}　　{c_22=3*0+(-1)*4=-4}'))
P.append(para('所以 {AB=mat(4,8;5,-4)}。（提醒：一般情況 {AB} 不一定等於 {BA}）'))

P.append(heading('五、範例4：轉置矩陣'))
P.append(para('設 {A=mat(1,2,3;4,5,6)}，求 {A^T}。'))
P.append(shaded_box('步驟：原本的「第一橫行」變成答案的「第一直列」，依此類推。2×3 轉置後變 3×2。'))
P.append(para('{A^T=mat(1,4;2,5;3,6)}'))

P.append(blank())
P.append(para('接下來請拿《矩陣（概念與運算）課堂練習》，依這套框架完成練習 A、B、C。'))
out1 = build_docx(P, os.path.join(OUT, '講義_矩陣_概念與運算_融合班.docx'), footer_text=FOOTER)
print(out1)

# ================= 練習 =================
Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('作答前，先回頭看《課堂講義》的四個範例（加減、數乘、乘法、轉置）。每題都把逐步算式寫出來。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．設 {A=mat(3,-1,0;2,5,-4)}。'),
    para('（1）A 是 ＿＿ × ＿＿ 階矩陣。'),
    para('（2）{a_13=}＿＿＿；{a_21=}＿＿＿；{a_23=}＿＿＿。'),
] + write_lines(2)))
Q.append(problem_box([
    para('2．設 {A=mat(2,3;1,4)}，{B=mat(5,-1;0,6)}，求 {A+B}。'),
    shaded_box('提示：{A+B=mat(2+5,3+(-1);1+0,4+6)=mat(?,?;?,?)}'),
] + write_lines(3)))
Q.append(problem_box([
    para('3．設 {A=mat(1,-2;3,0)}，求 {3A}。'),
    shaded_box('提示：每一格都乘 3。'),
] + write_lines(3)))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem_box([para('4．設 {A=mat(4,1,-2;3,0,5)}，{B=mat(-1,2,3;6,-4,1)}，求 {A-B}。')] + write_lines(4)))
Q.append(problem_box([para('5．設 {A=mat(2,-1;0,3)}，{B=mat(1,4;-2,5)}，求 {2A+B}。')] + write_lines(5)))
Q.append(problem_box([
    para('6．設 {A=mat(1,2;3,0)}，{B=mat(2,-1;4,5)}，求 {AB}。'),
    shaded_box('提示：先確認階數 (2×2)·(2×2)＝2×2；再逐格「橫行 × 直列」。'),
] + write_lines(5)))
Q.append(problem_box([para('7．設 {A=mat(2,1;1,3)}，{B=mat(1,0,-2;4,3,1)}，求 {AB}。（答案是幾階？）')] + write_lines(5)))
Q.append(problem_box([para('8．設 {A=mat(2,-1,3;0,5,4)}，求 {A^T}。')] + write_lines(3)))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([
    para('9．設 {A=mat(1,2;0,1)}，{B=mat(1,0;3,1)}，分別求 {AB} 與 {BA}，並說明兩者是否相等。'),
] + write_lines(5)))
Q.append(problem_box([para('10．設 {A=mat(3,1;2,4)}，{B=mat(5,-1;0,2)}，若 {2X=A-B}，求矩陣 {X}。')] + write_lines(5)))
Q.append(problem_box([
    para('11．請你自己設計兩個 2×2 矩陣 {A}、{B}，使得 {A+B=mat(4,4;4,4)}。寫出你的 A、B，並驗算。'),
] + write_lines(4), trailing_blank=False))

# 參考答案（分頁）
Q.append(heading('參考答案（教師用）', page_break_before=True))
Q.append(para('1．A 是 2×3 階；{a_13=0}、{a_21=2}、{a_23=-4}。'))
Q.append(para('2．{A+B=mat(7,2;1,10)}。'))
Q.append(para('3．{3A=mat(3,-6;9,0)}。'))
Q.append(para('4．{A-B=mat(5,-1,-5;-3,4,4)}。'))
Q.append(para('5．{2A=mat(4,-2;0,6)}，{2A+B=mat(5,2;-2,11)}。'))
Q.append(para('6．{AB=mat(10,9;6,-3)}。'))
Q.append(para('7．{AB=mat(6,3,-3;13,9,1)}，是 2×3 階。'))
Q.append(para('8．{A^T=mat(2,0;-1,5;3,4)}。'))
Q.append(para('9．{AB=mat(7,2;3,1)}，{BA=mat(1,2;3,7)}，{AB!=BA}（矩陣乘法不具交換律）。'))
Q.append(para('10．{A-B=mat(-2,2;2,2)}，{X=mat(-1,1;1,1)}。'))
Q.append(para('11．答案不唯一。例如 {A=mat(1,2;3,0)}、{B=mat(3,2;1,4)}；只要每組對應元素相加都等於 4 即可。'))
out2 = build_docx(Q, os.path.join(OUT, '練習_矩陣_概念與運算_融合班.docx'), footer_text=FOOTER)
print(out2)
