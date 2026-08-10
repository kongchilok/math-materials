# -*- coding: utf-8 -*-
# 練習（三層 A/B/C）—— 空間中的距離
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間中的距離'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(blank())
P.append(shaded_box('點到平面距離：{d=frac(|vec(AP)·vec(n)|,|vec(n)|)}（A是平面內一點，P是平面外的點）'))
P.append(blank())

P.append(heading(f'練習A（{star_label(1)}）—— 公式直接應用'))
P.append(problem_box([
    para('1．平面 α 的法向量 {vec(n)=(2,-1,2)}，平面內一點 {A(1,0,0)}，平面外一點 {P(3,1,2)}，求 P 到平面 α 的距離。'),
] + write_lines(4)))
P.append(problem_box([
    para('2．已知 {A(1,2,3)}、{B(4,6,15)}，求 {|AB|}。'),
] + write_lines(4)))

P.append(heading(f'練習B（{star_label(2)}）—— 正方體中的距離'))
P.append(problem_box([
    para('3．正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2，以 D 為原點建系。求 {A_1} 到平面 {BDD_1B_1} 的距離。'),
    shaded_box('提示：平面 {BDD_1B_1} 上一課求過法向量 {vec(n)=(1,-1,0)}。'),
] + write_lines(6)))
P.append(problem_box([
    para('4．平面 α 的法向量 {vec(n)=(0,0,1)}，並且過原點 {O(0,0,0)}。求點 {P(2,3,1)} 到平面 α 的距離。'),
] + write_lines(5)))

P.append(heading(f'練習C（{star_label(3)}）—— 綜合應用'))
P.append(problem_box([
    para('5．同一正方體中，求 C 到平面 {ABD_1} 的距離。'),
    shaded_box('提示：先求平面 {ABD_1} 的法向量（用 {vec(AB)} 和 {vec(AD_1)} 列方程）。'),
] + write_lines(7)))
P.append(problem_box([
    para('6．同一正方體中，判斷直線 {A_1B_1} 是否平行於平面 {ABD_1}，如果係，求呢條直線到平面的距離。'),
    shaded_box('提示：先判斷 {vec(A_1B_1)} 是否垂直於平面 {ABD_1} 的法向量（即是否平行於平面）；再喺直線上揀一點，求呢一點到平面的距離。'),
] + write_lines(8), trailing_blank=False))

P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('1．{d=frac(7,3)}（{vec(AP)=(2,1,2)}，{vec(AP)·vec(n)=4-1+4=7}，{|vec(n)|=3}）'))
P.append(para('2．{|AB|=sqrt(9+16+144)=sqrt(169)=13}'))
P.append(para('3．{d=sqrt(2)}（{vec(A_1B)=(0,2,-2)}，{vec(A_1B)·vec(n)=0-2+0=-2}，{|vec(n)|=sqrt(2)}，{d=frac(|-2|,sqrt(2))=sqrt(2)}）'))
P.append(para('4．{d=1}（{vec(OP)=(2,3,1)}，{vec(OP)·vec(n)=0+0+1=1}，{|vec(n)|=1}，直接讀出就是z坐標）'))
P.append(para('5．{d=sqrt(2)}。詳細求法向量過程見驗算記錄。'))
P.append(para('6．平行；距離 {=sqrt(2)}。詳細判斷過程見驗算記錄。（呢三題(3、5、6)啱啱好都係 {sqrt(2)}，源於呢個正方體嘅對稱結構，唔係抄錯，驗算記錄有獨立核實）'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_空間中的距離_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
