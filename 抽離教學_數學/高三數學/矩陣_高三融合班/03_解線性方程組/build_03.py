# -*- coding: utf-8 -*-
"""Unit 3：矩陣的應用 — 解線性方程組（融合班三層共用版）。"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '矩陣的應用：解線性方程組'
FOOTER = '高三數學．矩陣：解線性方程組'

# ================= 講義 =================
P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、把方程組寫成矩陣'))
P.append(para('一個方程組，例如 {x+2y=5} 和 {3x-y=1}，可以把「係數」和「常數」排成一個矩陣：'))
P.append(para('增廣矩陣 {mat(1,2,5;3,-1,1)}（豎線左邊是係數，右邊是等號後的常數）。'))
P.append(shaded_box('目標：對「橫行」做加減，把左半變成 {mat(1,0;0,1)}，右半那一列就是答案 {x}、{y}。'))

P.append(heading('二、範例1：二元一次方程組（高斯消元）'))
P.append(para('解 {x+2y=5}、{3x-y=1}。增廣矩陣 {mat(1,2,5;3,-1,1)}。'))
P.append(para('R2−3·R1：{mat(1,2,5;0,-7,-14)}；R2÷(−7)：{mat(1,2,5;0,1,2)}。'))
P.append(para('R1−2·R2：{mat(1,0,1;0,1,2)}。所以 {x=1}、{y=2}。'))
P.append(shaded_box('檢驗：{1+2*2=5} ✓；{3*1-2=1} ✓。'))

P.append(heading('三、範例2：三元一次方程組'))
P.append(para('解 {x+y+z=6}、{2x-y+z=3}、{x+2y-z=2}。增廣矩陣 {mat(1,1,1,6;2,-1,1,3;1,2,-1,2)}。'))
P.append(para('用第 1 橫行消去第 2、3 行的 x，再一步步把左半化成單位矩陣，最後得到：'))
P.append(para('{x=1}、{y=2}、{z=3}。'))
P.append(shaded_box('檢驗：{1+2+3=6} ✓；{2-2+3=3} ✓；{1+4-3=2} ✓。'))

P.append(heading('四、範例3：克拉瑪法則（用行列式，適合二元）'))
P.append(para('解 {2x+y=5}、{x-y=1}。'))
P.append(para('主行列式 {Δ=det(2,1;1,-1)=2*(-1)-1*1=-3}。'))
P.append(para('把 x 那一列換成常數：{Δx=det(5,1;1,-1)=-6}；把 y 那一列換成常數：{Δy=det(2,5;1,1)=-3}。'))
P.append(para('{x=frac(Δx,Δ)=frac(-6,-3)=2}，{y=frac(Δy,Δ)=frac(-3,-3)=1}。'))

P.append(blank())
P.append(para('接下來請拿《解線性方程組課堂練習》，依這套框架完成練習 A、B、C。'))
out1 = build_docx(P, os.path.join(OUT, '講義_矩陣的應用_解線性方程組_融合班.docx'), footer_text=FOOTER)
print(out1)

# ================= 練習 =================
Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('作答前，先回頭看《課堂講義》：增廣矩陣＋高斯消元、以及克拉瑪法則。每題都寫出過程。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．把方程組 {2x+3y=7}、{x-y=1} 寫成增廣矩陣。'),
    shaded_box('提示：左半放係數，右半放常數：{mat(?,?,?;?,?,?)}。'),
] + write_lines(2)))
Q.append(problem_box([
    para('2．用消元法解 {x+y=5}、{x-y=1}。'),
    shaded_box('提示：增廣 {mat(1,1,5;1,-1,1)}，用 R2−R1 先消去 x。'),
] + write_lines(4)))
Q.append(problem_box([
    para('3．用克拉瑪法則解 {x+2y=8}、{3x-y=3}。'),
    shaded_box('提示：{Δ=det(1,2;3,-1)}、{Δx=det(8,2;3,-1)}、{Δy=det(1,8;3,3)}，再算 {x=frac(Δx,Δ)}、{y=frac(Δy,Δ)}。'),
] + write_lines(4)))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem_box([para('4．解 {3x+y=7}、{2x-y=3}。')] + write_lines(4)))
Q.append(problem_box([para('5．用高斯消元解 {x+y+z=2}、{x-y+2z=3}、{2x+y-z=1}。')] + write_lines(6)))
Q.append(problem_box([para('6．用克拉瑪法則解 {4x+3y=18}、{2x-y=4}。')] + write_lines(5)))
Q.append(problem_box([
    para('7．（應用）買 2 支筆和 3 本簿共 13 元；買 1 支筆和 2 本簿共 8 元。求筆、簿的單價。'),
    shaded_box('提示：設筆 {x} 元、簿 {y} 元，列出兩條方程式再解。'),
] + write_lines(5)))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([para('8．用高斯消元解 {x+2y+z=8}、{2x+y-z=1}、{x-y+2z=9}。')] + write_lines(6)))
Q.append(problem_box([
    para('9．（應用）三種文具：1 筆＋1 尺＋1 膠＝12 元；2 筆＋1 尺＝11 元；1 尺＋3 膠＝17 元。求三者單價。'),
] + write_lines(6)))
Q.append(problem_box([
    para('10．請你寫出一個解為 {x=1}、{y=2} 的二元一次方程組（兩條方程式），並用增廣矩陣驗證。'),
] + write_lines(5), trailing_blank=False))

# 參考答案
Q.append(heading('參考答案（教師用）', page_break_before=True))
Q.append(para('1．{mat(2,3,7;1,-1,1)}。'))
Q.append(para('2．R2−R1 得 {y=2}，回代 {x=3}。答：{x=3}、{y=2}。'))
Q.append(para('3．{Δ=-7}、{Δx=-14}、{Δy=-21}；{x=2}、{y=3}。'))
Q.append(para('4．兩式相加 {5x=10}，{x=2}、{y=1}。'))
Q.append(para('5．{x=1}、{y=0}、{z=1}。'))
Q.append(para('6．{Δ=-10}、{Δx=-30}、{Δy=-20}；{x=3}、{y=2}。'))
Q.append(para('7．{2x+3y=13}、{x+2y=8}；筆 {x=2} 元、簿 {y=3} 元。'))
Q.append(para('8．{x=2}、{y=1}、{z=4}。'))
Q.append(para('9．{x+y+z=12}、{2x+y=11}、{y+3z=17}；筆 3 元、尺 5 元、膠 4 元。'))
Q.append(para('10．答案不唯一。例如 {x+y=3}、{x-y=-1}，增廣 {mat(1,1,3;1,-1,-1)} 消元得 {x=1}、{y=2}。'))
out2 = build_docx(Q, os.path.join(OUT, '練習_矩陣的應用_解線性方程組_融合班.docx'), footer_text=FOOTER)
print(out2)
