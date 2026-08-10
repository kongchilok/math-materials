# -*- coding: utf-8 -*-
# 練習（三層 A/B/C）—— 空間角的計算：線面角與二面角
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間角的計算'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(blank())
P.append(shaded_box('線面角：{sinθ=frac(|vec(v)·vec(n)|,|vec(v)|*|vec(n)|)}（用sin）　　二面角：{|fn(cos)θ|=frac(|vec(n_1)·vec(n_2)|,|vec(n_1)|*|vec(n_2)|)}（要另外判斷銳鈍角）'))
P.append(blank())

P.append(heading(f'練習A（{star_label(1)}）—— 公式直接應用'))
P.append(problem_box([
    para('1．直線方向向量 {vec(v)=(1,1,2)}，平面法向量 {vec(n)=(0,0,1)}，求線面角的正弦值。'),
] + write_lines(4)))
P.append(problem_box([
    para('2．直線方向向量 {vec(v)=(1,0,0)}，平面法向量 {vec(n)=(0,1,1)}，求 {vec(v)·vec(n)}，並判斷線面角是多少度。'),
] + write_lines(4)))
P.append(problem_box([
    para('3．二面角兩個面的法向量 {vec(n_1)=(1,0,0)}、{vec(n_2)=(0,1,0)}，求 {|fn(cos)⟨vec(n_1),vec(n_2)⟩|}，並判斷二面角是多少度。'),
] + write_lines(4)))

P.append(heading(f'練習B（{star_label(2)}）—— 求線面角'))
P.append(problem_box([
    para('4．正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2，以 D 為原點建系（同講義一樣）。求體對角線 {vec(AC_1)} 與底面 {ABCD} 所成角的正弦值。'),
] + write_lines(6)))
P.append(problem_box([
    para('5．同一正方體中，求 {vec(AC_1)} 與側面 {ABB_1A_1} 所成角的正弦值。'),
    shaded_box('提示：側面 {ABB_1A_1} 是 {x=2} 平面，法向量可以直接取 {vec(n)=(1,0,0)}。'),
] + write_lines(6)))
P.append(problem_box([
    para('6．二面角兩個面的法向量 {vec(n_1)=(1,1,0)}、{vec(n_2)=(1,-1,0)}，求 {|fn(cos)⟨vec(n_1),vec(n_2)⟩|}，並判斷二面角是多少度。'),
] + write_lines(4)))

P.append(heading(f'練習C（{star_label(3)}）—— 綜合應用'))
P.append(problem_box([
    para('7．正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2，以 D 為原點建系。求二面角 A-BD₁-C 的大小。'),
    shaded_box('提示：先求平面 {ABD_1} 和平面 {CBD_1} 的法向量，再判斷銳鈍角（睇下 A、C 分別喺邊，張開嘅角大概幾多度）。'),
] + write_lines(9)))
P.append(problem_box([
    para('8．同一正方體中，求 {vec(A_1C)} 與平面 {BDD_1B_1} 所成角的正弦值。'),
    shaded_box('提示：平面 {BDD_1B_1} 要先自己求法向量——喺呢個平面內揾兩個向量（例如 {vec(BD)} 和 {vec(BD_1)}）列方程。'),
] + write_lines(8), trailing_blank=False))

P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('1．{sinθ=frac(|2|,sqrt(6)*1)=frac(2,sqrt(6))=frac(sqrt(6),3)}'))
P.append(para('2．{vec(v)·vec(n)=0}，所以 {sinθ=0}，線面角 {=0°}（即直線平行於平面或在平面內）。'))
P.append(para('3．{|fn(cos)⟨vec(n_1),vec(n_2)⟩|=0}，二面角 {=90°}（{fn(cos)}為0時冇銳鈍角歧義，因為90°的補角都是90°）。'))
P.append(para('4．{sinθ=frac(sqrt(3),3)}（{vec(AC_1)=(-2,2,2)}，{vec(n)=(0,0,1)}，{sinθ=frac(|2|,2*sqrt(3)*1)=frac(1,sqrt(3))=frac(sqrt(3),3)}）'))
P.append(para('5．{sinθ=frac(sqrt(3),3)}（{vec(AC_1)=(-2,2,2)}，{vec(n)=(1,0,0)}，{sinθ=frac(|-2|,2*sqrt(3)*1)=frac(1,sqrt(3))=frac(sqrt(3),3)}，同第4題數值一樣但係唔同平面，唔係巧合抄錯）'))
P.append(para('6．{|fn(cos)⟨vec(n_1),vec(n_2)⟩|=0}，二面角 {=90°}'))
P.append(para('7．二面角 {=120°}。詳細求法向量過程同銳鈍角判斷見驗算記錄。'))
P.append(para('8．{sinθ=frac(sqrt(6),3)}。詳細求法向量過程見驗算記錄。'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_空間角的計算_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
