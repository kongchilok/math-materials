# -*- coding: utf-8 -*-
# 練習（三層 A/B/C）—— 空間向量的數量積
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間向量的數量積'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(blank())
P.append(shaded_box('公式卡：{vec(a)·vec(b)=|vec(a)|*|vec(b)|*fn(cos)⟨vec(a),vec(b)⟩}　　記住：{vec(a)⊥vec(b)} ⟺ {vec(a)·vec(b)=0}'))
P.append(blank())

P.append(heading(f'練習A（{star_label(1)}）—— 定義直接應用'))
P.append(problem_box([
    para('1．正方體中，{vec(AB)} 與 {vec(AD)} 是相鄰兩條棱所在的向量。求 {vec(AB)·vec(AD)}。'),
] + write_lines(3)))
P.append(problem_box([
    para('2．已知 {|vec(a)|=3}，{|vec(b)|=4}，{vec(a)⊥vec(b)}，求 {vec(a)·vec(b)}。'),
] + write_lines(3)))
P.append(problem_box([
    para('3．已知 {|vec(a)|=2}，{|vec(b)|=5}，{⟨vec(a),vec(b)⟩=60°}，求 {vec(a)·vec(b)}。'),
] + write_lines(3)))

P.append(heading(f'練習B（{star_label(2)}）—— 分配律與逆用定義'))
P.append(problem_box([
    para('4．正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為 2，求 {vec(AB)·vec(AC)}。'),
    shaded_box('提示：先將 {vec(AC)} 拆做 {vec(AB)+vec(BC)}，再用分配律展開。'),
] + write_lines(5)))
P.append(problem_box([
    para('5．已知 {vec(a)·vec(b)=6}，{|vec(a)|=3}，{|vec(b)|=4}，求 {⟨vec(a),vec(b)⟩}。'),
] + write_lines(4)))
P.append(problem_box([
    para('6．判斷正誤並說明理由：「若 {vec(a)·vec(b)=0}，則一定有 {vec(a)=vec(0)} 或 {vec(b)=vec(0)}。」'),
    shaded_box('提示：諗下「垂直」呢個情況。'),
] + write_lines(4)))

P.append(heading(f'練習C（{star_label(3)}）—— 綜合應用'))
P.append(problem_box([
    para('7．正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為 2，M 是 {vec(BB_1)} 的中點。求 {vec(AM)} 與 {vec(AC_1)} 的夾角餘弦值。'),
    shaded_box('提示：設 {vec(DA)=vec(p)}，{vec(DC)=vec(q)}，{vec(DD_1)=vec(r)}（三條互相垂直），先用 {vec(p)}、{vec(q)}、{vec(r)} 分別表示 {vec(AM)} 和 {vec(AC_1)}，再逐項用分配律計算數量積（垂直項=0）。'),
] + write_lines(9)))
P.append(problem_box([
    para('8．求證：{|vec(a)+vec(b)|^2=|vec(a)|^2+2*vec(a)·vec(b)+|vec(b)|^2}'),
    shaded_box('提示：{|vec(a)+vec(b)|^2} 即係 {(vec(a)+vec(b))·(vec(a)+vec(b))}，直接展開（用分配律）。'),
] + write_lines(6), trailing_blank=False))

P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('1．{0}（{vec(AB)⊥vec(AD)}，正方體相鄰兩棱互相垂直）'))
P.append(para('2．{0}（{vec(a)⊥vec(b)}，用性質④）'))
P.append(para('3．{vec(a)·vec(b)=2*5*fn(cos)60°=10*frac(1,2)=5}'))
P.append(para('4．{4}（{vec(AB)·vec(AC)=vec(AB)·(vec(AB)+vec(BC))=vec(AB)·vec(AB)+vec(AB)·vec(BC)=4+0=4}）'))
P.append(para('5．{⟨vec(a),vec(b)⟩=60°}（{fn(cos)⟨vec(a),vec(b)⟩=frac(6,3*4)=frac(1,2)}）'))
P.append(para('6．錯。反例：{vec(a)⊥vec(b)} 且兩者都不是零向量時，{vec(a)·vec(b)=0} 都成立——數量積為0唔代表任何一個向量係零向量，仲可能係兩者垂直。'))
P.append(para('7．{fn(cos)⟨vec(AM),vec(AC_1)⟩=frac(sqrt(15),5)}（{vec(AM)·vec(AC_1)=6}，{|vec(AM)|=sqrt(5)}，{|vec(AC_1)|=2*sqrt(3)}，詳見驗算記錄）'))
P.append(para('8．證明：{|vec(a)+vec(b)|^2=(vec(a)+vec(b))·(vec(a)+vec(b))=vec(a)·vec(a)+vec(a)·vec(b)+vec(b)·vec(a)+vec(b)·vec(b)}'))
P.append(para('　{=|vec(a)|^2+2*vec(a)·vec(b)+|vec(b)|^2}（因為 {vec(a)·vec(b)=vec(b)·vec(a)}，交換律）　　得證。'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_空間向量的數量積_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
