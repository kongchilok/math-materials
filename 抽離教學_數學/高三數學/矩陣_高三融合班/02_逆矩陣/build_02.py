# -*- coding: utf-8 -*-
"""Unit 2：逆矩陣（反矩陣）—— 融合班三層共用版（講義＋練習 docx）。"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '逆矩陣（反矩陣）'
FOOTER = '高三數學．矩陣：逆矩陣'

# ================= 講義 =================
P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、什麼是逆矩陣'))
P.append(para('對一個方陣 {A}，如果找到另一個同階方陣 {B}，使得 {AB=BA=I}（{I} 是單位矩陣），'
              '就說 {A} 可逆，{B} 叫做 {A} 的逆矩陣，記作 {A^{-1}}。'))
P.append(shaded_box('直覺：逆矩陣就像「除法」——原矩陣乘上它的逆矩陣，會還原成單位矩陣 {I}（相當於數字裡的 1）。'))

P.append(heading('二、2×2 反矩陣公式（最常用）'))
P.append(para('設 {A=mat(a,b;c,d)}，先算行列式 {det(a,b;c,d)=ad-bc}。'))
P.append(shaded_box('公式：{A^{-1}=frac(1,ad-bc)*mat(d,-b;-c,a)}。'
                    '口訣：主對角線 a、d 對調，副對角線 b、c 變號，再除以 {ad-bc}。'
                    '若 {ad-bc=0}，則逆矩陣不存在。'))

P.append(heading('三、範例1：用公式求 2×2 逆矩陣'))
P.append(para('設 {A=mat(2,5;1,3)}，求 {A^{-1}}。'))
P.append(para('①行列式 {det(2,5;1,3)=2*3-5*1=1}（不為 0，可逆）。'))
P.append(para('②套公式：{A^{-1}=frac(1,1)*mat(3,-5;-1,2)=mat(3,-5;-1,2)}。'))
P.append(shaded_box('檢驗：{A*A^{-1}=mat(1,0;0,1)=I}，正確。'))

P.append(heading('四、範例2：用初等行變換求逆矩陣'))
P.append(para('設 {A=mat(1,2;2,5)}。把 {A} 和 {I} 併排寫成 {mat(1,2,1,0;2,5,0,1)}（左半是 A，右半是 I），'
              '再對「橫行」做加減，把左半變成 {I}，右半就會變成 {A^{-1}}。'))
P.append(para('R2−2·R1：{mat(1,2,1,0;0,-1,-2,1)}；'))
P.append(para('(−1)·R2、R1−3·R2 後：{mat(1,0,5,-2;0,1,-2,1)}；左半已是 {I}。'))
P.append(para('所以 {A^{-1}=mat(5,-2;-2,1)}。'))

P.append(heading('五、範例3：行列式為 0 → 逆矩陣不存在'))
P.append(para('設 {A=mat(2,4;1,2)}，{det(2,4;1,2)=2*2-4*1=0}，所以 {A} 沒有逆矩陣。'))

P.append(blank())
P.append(para('接下來請拿《逆矩陣課堂練習》，依這套框架完成練習 A、B、C。'))
out1 = build_docx(P, os.path.join(OUT, '講義_逆矩陣_融合班.docx'), footer_text=FOOTER)
print(out1)

# ================= 練習 =================
Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('作答前，先回頭看《課堂講義》：2×2 公式法、初等行變換法、以及「行列式為 0 就不可逆」。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．設 {A=mat(3,1;2,4)}，求行列式 {det(3,1;2,4)}。'),
    shaded_box('提示：{det(3,1;2,4)=3*4-1*2=}＿＿＿。'),
] + write_lines(2)))
Q.append(problem_box([
    para('2．設 {A=mat(4,1;3,1)}，用公式求 {A^{-1}}。'),
    shaded_box('提示：先算 {det=4*1-1*3=}＿＿；再套 {A^{-1}=frac(1,det)*mat(1,-1;-3,4)}。'),
] + write_lines(3)))
Q.append(problem_box([
    para('3．下面兩個矩陣，哪個有逆矩陣？（算行列式是否為 0）'),
    para('{P=mat(2,6;1,3)}　　{Q=mat(2,3;2,4)}'),
] + write_lines(3)))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem_box([para('4．設 {A=mat(4,2;1,1)}，用公式求 {A^{-1}}（答案會出現分數）。')] + write_lines(5)))
Q.append(problem_box([
    para('5．設 {A=mat(1,3;2,5)}，用初等行變換求 {A^{-1}}。'),
    shaded_box('提示：從 {mat(1,3,1,0;2,5,0,1)} 開始，把左半變成單位矩陣。'),
] + write_lines(5)))
Q.append(problem_box([
    para('6．設 {A=mat(2,1;3,2)}，{B=mat(5;8)}，利用 {X=A^{-1}B} 解出 {X}。'),
] + write_lines(5)))
Q.append(problem_box([
    para('7．設 {A=mat(3,5;1,2)}，{B=mat(2,-5;-1,3)}，計算 {AB}，判斷 {B} 是否為 {A} 的逆矩陣。'),
] + write_lines(4)))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([
    para('8．設 {A=mat(1,1,1;0,1,1;0,0,1)}，用初等行變換求 {A^{-1}}。'),
    shaded_box('提示：從 {mat(1,1,1,1,0,0;0,1,1,0,1,0;0,0,1,0,0,1)} 開始（左半 A、右半 {I})。'),
] + write_lines(5)))
Q.append(problem_box([para('9．設 {M=mat(t,4;1,t-3)} 的逆矩陣不存在，求實數 {t}。')] + write_lines(5)))
Q.append(problem_box([
    para('10．已知性質 {(AB)^{-1}=B^{-1}A^{-1}}。請取 {A=mat(1,1;0,1)}、{B=mat(1,0;1,1)}，'
         '分別算出 {(AB)^{-1}} 與 {B^{-1}A^{-1}}，驗證兩者相等。'),
] + write_lines(5), trailing_blank=False))

# 參考答案
Q.append(heading('參考答案（教師用）', page_break_before=True))
Q.append(para('1．{det(3,1;2,4)=3*4-1*2=10}。'))
Q.append(para('2．{det=1}，{A^{-1}=mat(1,-1;-3,4)}。'))
Q.append(para('3．{P}：{det=2*3-6*1=0} → 無逆矩陣；{Q}：{det=2*4-3*2=2!=0} → 有逆矩陣。'))
Q.append(para('4．{det=4*1-2*1=2}，{A^{-1}=frac(1,2)*mat(1,-2;-1,4)=mat(1/2,-1;-1/2,2)}。'))
Q.append(para('5．{A^{-1}=mat(-5,3;2,-1)}。'))
Q.append(para('6．{A^{-1}=mat(2,-1;-3,2)}，{X=A^{-1}B=mat(2;1)}（即 {x=2}、{y=1}）。'))
Q.append(para('7．{AB=mat(1,0;0,1)=I}，所以 {B} 是 {A} 的逆矩陣。'))
Q.append(para('8．{A^{-1}=mat(1,-1,0;0,1,-1;0,0,1)}。'))
Q.append(para('9．{det(M)=t(t-3)-4=t^2-3t-4=0}，即 {(t-4)(t+1)=0}，所以 {t=4} 或 {t=-1}。'))
Q.append(para('10．{AB=mat(2,1;1,1)}，{(AB)^{-1}=mat(1,-1;-1,2)}；{B^{-1}A^{-1}=mat(1,-1;-1,2)}，兩者相等。'))
out2 = build_docx(Q, os.path.join(OUT, '練習_逆矩陣_融合班.docx'), footer_text=FOOTER)
print(out2)
