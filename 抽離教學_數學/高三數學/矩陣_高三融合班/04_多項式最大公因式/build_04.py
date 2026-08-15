# -*- coding: utf-8 -*-
"""Unit 4：矩陣的應用 — 求多項式的最大公因式（※16.6，融合班三層共用版）。"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '矩陣的應用：求多項式最大公因式'
FOOTER = '高三數學．矩陣：多項式最大公因式（※選學）'

# ================= 講義 =================
P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、想法：用「係數行」代表多項式'))
P.append(para('求兩個多項式的最大公因式（HCF），可以把它們的「係數」排成矩陣的橫行，再用行相減來做。'))
P.append(shaded_box('三步驟：①把每個多項式的係數「按次數對齊」寫成一行（缺哪個次方就補 0）。'
                    '②用「行相減」消去最高次項，得到一個次數較低的多項式。'
                    '③把剩下的行約掉常數倍，就是最大公因式。'))

P.append(heading('二、範例1：兩式同次數'))
P.append(para('求 {f(x)=x^2+3x+2} 與 {g(x)=x^2-1} 的最大公因式。'))
P.append(para('①寫成係數行（次數 2、1、0）：{f→mat(1,3,2)}　{g→mat(1,0,-1)}，合起來 {mat(1,3,2;1,0,-1)}。'))
P.append(para('②R1−R2：{mat(0,3,3)}，代表 {3x+3=3(x+1)}。'))
P.append(para('③約掉常數 3，得候選最大公因式 {x+1}。'))
P.append(shaded_box('驗證：{f=(x+1)(x+2)}、{g=(x+1)(x-1)}，兩者都有因式 {x+1}，所以 HCF ={x+1}。'))

P.append(heading('三、範例2：兩式次數不同（先左移對齊）'))
P.append(para('求 {f(x)=x^3-1} 與 {g(x)=x^2-1} 的最大公因式。'))
P.append(para('對齊次數 3、2、1、0：{f→mat(1,0,0,-1)}，{g→mat(0,1,0,-1)}。'))
P.append(para('因為 f 比 g 高一次，先把 g 乘 {x}（係數整列左移一格）：{x*g→mat(1,0,-1,0)}。'))
P.append(para('再算 {f-x*g}：{mat(0,0,1,-1)}，代表 {x-1}。'))
P.append(shaded_box('驗證：{g=(x-1)(x+1)}、{f=(x-1)(x^2+x+1)}，兩者都有因式 {x-1}，所以 HCF ={x-1}。'))

P.append(blank())
P.append(para('接下來請拿《求多項式最大公因式課堂練習》，依這三步驟完成練習 A、B、C。'))
out1 = build_docx(P, os.path.join(OUT, '講義_矩陣的應用_多項式最大公因式_融合班.docx'), footer_text=FOOTER)
print(out1)

# ================= 練習 =================
Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('作答前，先回頭看《課堂講義》的三步驟：對齊係數 → 行相減消最高次 → 約掉常數。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．求 {f(x)=x^2+5x+6}、{g(x)=x^2+2x} 的最大公因式。'),
    shaded_box('提示：係數行 {mat(1,5,6;1,2,0)}，做 R1−R2 後約掉常數。'),
] + write_lines(4)))
Q.append(problem_box([
    para('2．求 {f(x)=x^2+4x+3}、{g(x)=x^2-9} 的最大公因式。'),
    shaded_box('提示：{g=x^2-9} 的係數行是 {mat(1,0,-9)}（一次項補 0）。'),
] + write_lines(4)))
Q.append(problem_box([
    para('3．行相減後得到一行 {mat(0,2,6)}，代表 {2x+6}。約掉常數後，最大公因式的候選是什麼？'),
] + write_lines(2)))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem_box([para('4．求 {f(x)=x^2+7x+12}、{g(x)=x^2+2x-3} 的最大公因式。')] + write_lines(5)))
Q.append(problem_box([para('5．求 {f(x)=x^2-4}、{g(x)=x^2-x-2} 的最大公因式。')] + write_lines(5)))
Q.append(problem_box([para('6．求 {f(x)=2x^2+5x+3}、{g(x)=2x^2-x-3} 的最大公因式。')] + write_lines(5)))
Q.append(problem_box([para('7．求 {f(x)=x^2+2x-8}、{g(x)=x^2+6x+8} 的最大公因式。')] + write_lines(5)))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([
    para('8．求 {f(x)=x^3-1}、{g(x)=x^2-1} 的最大公因式。'),
    shaded_box('提示：次數不同，先算 {x*g}（係數左移一格）再做 {f-x*g}。'),
] + write_lines(5)))
Q.append(problem_box([
    para('9．求 {f(x)=x^3+2x^2-x-2}、{g(x)=x^2-1} 的最大公因式。'),
] + write_lines(5)))
Q.append(problem_box([
    para('10．請你設計一個二次多項式 {g(x)}，使 {f(x)=x^2+3x+2} 與 {g(x)} 的最大公因式為 {x+1}，並用行相減驗證。'),
] + write_lines(5), trailing_blank=False))

# 參考答案
Q.append(heading('參考答案（教師用）', page_break_before=True))
Q.append(para('1．{mat(1,5,6;1,2,0)}，R1−R2={mat(0,3,6)}=3(x+2)，HCF ={x+2}。'))
Q.append(para('2．R1−R2={mat(0,4,12)}=4(x+3)，HCF ={x+3}。'))
Q.append(para('3．{2x+6=2(x+3)}，候選 ={x+3}。'))
Q.append(para('4．R1−R2={mat(0,5,15)}=5(x+3)，HCF ={x+3}。'))
Q.append(para('5．R1−R2={mat(0,1,-2)}={x-2}，HCF ={x-2}。'))
Q.append(para('6．R1−R2={mat(0,6,6)}=6(x+1)，HCF ={x+1}。'))
Q.append(para('7．R1−R2={mat(0,-4,-16)}=−4(x+4)，HCF ={x+4}。'))
Q.append(para('8．{f=mat(1,0,0,-1)}、{x*g=mat(1,0,-1,0)}，{f-x*g=mat(0,0,1,-1)}={x-1}，HCF ={x-1}。'))
Q.append(para('9．{f=mat(1,2,-1,-2)}、{x*g=mat(1,0,-1,0)}，{f-x*g=mat(0,2,0,-2)}=2(x^2-1)，HCF ={x^2-1}。'))
Q.append(para('10．答案不唯一。例如 {g=x^2+4x+3}：[1,3,2]−[1,4,3]={mat(0,-1,-1)}=−(x+1)，HCF ={x+1}。'))
out2 = build_docx(Q, os.path.join(OUT, '練習_矩陣的應用_多項式最大公因式_融合班.docx'), footer_text=FOOTER)
print(out2)
