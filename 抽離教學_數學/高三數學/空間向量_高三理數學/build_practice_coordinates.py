# -*- coding: utf-8 -*-
# 練習（三層 A/B/C）—— 空間向量的坐標與坐標運算
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間向量的坐標與坐標運算'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(blank())
P.append(shaded_box('公式卡：{vec(a)·vec(b)=x_1*x_2+y_1*y_2+z_1*z_2}　　{|vec(a)|=sqrt(x_1^2+y_1^2+z_1^2)}　　{vec(a)⊥vec(b)}⟺數量積=0'))
P.append(blank())

P.append(heading(f'練習A（{star_label(1)}）—— 坐標運算基本功'))
P.append(problem_box([
    para('1．已知 {vec(a)=(1,2,-3)}，{vec(b)=(2,-1,0)}，求 {vec(a)+vec(b)} 和 {vec(a)-vec(b)}。'),
] + write_lines(4)))
P.append(problem_box([
    para('2．已知 {vec(a)=(2,-1,3)}，求 {|vec(a)|}。'),
] + write_lines(3)))
P.append(problem_box([
    para('3．已知 {A(1,2,3)}、{B(4,6,8)}，求 {|AB|} 和 AB 的中點坐標。'),
] + write_lines(4)))

P.append(heading(f'練習B（{star_label(2)}）—— 平行、垂直、夾角'))
P.append(problem_box([
    para('4．已知 {vec(a)=(1,2,-2)}，{vec(b)=(-2,-4,4)}，判斷 {vec(a)}、{vec(b)} 是否平行。'),
] + write_lines(4)))
P.append(problem_box([
    para('5．已知 {vec(a)=(1,-1,2)}，{vec(b)=(3,2,m)}，若 {vec(a)⊥vec(b)}，求 {m}。'),
] + write_lines(4)))
P.append(problem_box([
    para('6．求 {vec(a)=(1,1,0)} 和 {vec(b)=(0,1,1)} 的夾角餘弦值。'),
] + write_lines(5)))

P.append(heading(f'練習C（{star_label(3)}）—— 綜合應用'))
P.append(problem_box([
    para('7．正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2，以 D 為原點建系（同講義一樣：{vec(DA)}沿x軸、{vec(DC)}沿y軸、{vec(DD_1)}沿z軸）。求 {|BD_1|}，並求 {⟨vec(DB),vec(DD_1)⟩} 的夾角餘弦值。'),
    shaded_box('提示：先寫出 B、{D_1} 的坐標，再用距離公式；夾角要先分別寫出 {vec(DB)}、{vec(DD_1)} 的坐標。'),
] + write_lines(8)))
P.append(problem_box([
    para('8．已知空間三點 {A(1,0,-1)}、{B(3,1,2)}、{C(5,2,5)}，求證 A、B、C 三點共線。'),
    shaded_box('提示：求出 {vec(AB)} 和 {vec(AC)} 的坐標，判斷是否平行（一個是另一個的倍數）——若平行且共起點，就代表三點共線。'),
] + write_lines(6), trailing_blank=False))

P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('1．{vec(a)+vec(b)=(3,1,-3)}，{vec(a)-vec(b)=(-1,3,-3)}'))
P.append(para('2．{|vec(a)|=sqrt(4+1+9)=sqrt(14)}'))
P.append(para('3．{|AB|=sqrt(9+16+25)=sqrt(50)=5*sqrt(2)}，中點坐標 {(2.5,4,5.5)}'))
P.append(para('4．平行。因為 {vec(b)=-2*vec(a)}（{-2,-4,4}恰好是{1,2,-2}各分量乘以{-2}）'))
P.append(para('5．{m=-frac(1,2)}（{vec(a)·vec(b)=1*3+(-1)*2+2*m=3-2+2*m=1+2*m=0}，解得 {m=-frac(1,2)}）'))
P.append(para('6．{fn(cos)⟨vec(a),vec(b)⟩=frac(1,2)}（{vec(a)·vec(b)=0+1+0=1}，{|vec(a)|=sqrt(2)}，{|vec(b)|=sqrt(2)}，{frac(1,sqrt(2)*sqrt(2))=frac(1,2)}，即夾角60°）'))
P.append(para('7．{|BD_1|=2*sqrt(3)}；{⟨vec(DB),vec(DD_1)⟩} 的夾角餘弦值 {=0}（即90°）。詳見驗算記錄。'))
P.append(para('8．{vec(AB)=(2,1,3)}，{vec(AC)=(4,2,6)=2*vec(AB)}，兩向量平行且有公共點A，所以A、B、C三點共線。'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_空間向量的坐標與坐標運算_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
