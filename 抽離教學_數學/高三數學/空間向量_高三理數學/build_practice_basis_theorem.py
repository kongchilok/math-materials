# -*- coding: utf-8 -*-
# 練習（三層 A/B/C）—— 空間向量基本定理
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間向量基本定理'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(blank())
P.append(shaded_box('空間向量基本定理：若 {vec(a)}、{vec(b)}、{vec(c)} 不共面，則空間任一向量 {vec(p)} 都可【唯一】表示做 {vec(p)=x*vec(a)+y*vec(b)+z*vec(c)}'))
P.append(blank())

P.append(heading(f'練習A（{star_label(1)}）—— 認識基底表示法'))
P.append(problem_box([
    para('1．已知 {vec(a)}、{vec(b)}、{vec(c)} 構成空間一個基底，{vec(p)=3*vec(a)-2*vec(b)+vec(c)}，直接寫出用基底表示 {vec(p)} 時的三個係數 x、y、z。'),
] + write_lines(3)))
P.append(problem_box([
    para('2．正方體中，設 {vec(DA)=vec(a)}，{vec(DC)=vec(b)}，{vec(DD_1)=vec(c)}，用 {vec(a)}、{vec(b)}、{vec(c)} 表示體對角線 {vec(DB_1)}。'),
] + write_lines(3)))
P.append(problem_box([
    para('3．判斷：{vec(a)}、{vec(b)}、{vec(0)}（最後一個是零向量）呢三個向量，能否作為空間的一個基底？說明理由。'),
    shaded_box('提示：諗下基底嘅定義要求三個向量之間有咩關係。'),
] + write_lines(4)))

P.append(heading(f'練習B（{star_label(2)}）—— 中點與重心'))
P.append(problem_box([
    para('4．正方體 {ABCD}-{A_1B_1C_1D_1} 中，設 {vec(DA)=vec(a)}，{vec(DC)=vec(b)}，{vec(DD_1)=vec(c)}，N 是 {A_1D_1} 的中點，用 {vec(a)}、{vec(b)}、{vec(c)} 表示 {vec(DN)}。'),
] + write_lines(5)))
P.append(problem_box([
    para('5．已知空間四點 O、A、B、C，{vec(OA)=vec(a)}，{vec(OB)=vec(b)}，{vec(OC)=vec(c)}（{vec(a)}、{vec(b)}、{vec(c)} 不共面）。P 是三角形 ABC 的重心，用 {vec(a)}、{vec(b)}、{vec(c)} 表示 {vec(OP)}。'),
    shaded_box('提示：平面幾何學過「重心是三條中線的交點，把每條中線分成2:1」，呢個結論喺空間都一樣用得——試下由某一條中線出發。'),
] + write_lines(6)))
P.append(problem_box([
    para('6．已知 {vec(a)}、{vec(b)}、{vec(c)} 構成空間一個基底，且 {x*vec(a)+y*vec(b)+z*vec(c)=vec(0)}。根據基本定理嘅「唯一性」，可以推出 x、y、z 分別等於多少？為什麼？'),
] + write_lines(4)))

P.append(heading(f'練習C（{star_label(3)}）—— 綜合應用'))
P.append(problem_box([
    para('7．斜三棱柱 {ABC}-{A_1B_1C_1} 中，設 {vec(AB)=vec(a)}，{vec(AC)=vec(b)}，{vec(AA_1)=vec(c)}，用 {vec(a)}、{vec(b)}、{vec(c)} 表示 {vec(BC_1)}。'),
    shaded_box('提示：{vec(BC_1)=vec(BC)+vec(CC_1)}，先分別用 {vec(a)}、{vec(b)}、{vec(c)} 表示呢兩段（斜棱柱嘅側棱都互相平行且相等：{vec(CC_1)=vec(AA_1)}）。'),
] + write_lines(6)))
P.append(problem_box([
    para('8．平行六面體 {ABCD}-{A_1B_1C_1D_1}（注意：呢度唔一定係正方體，四邊形只要求對邊平行）中，設 {vec(AB)=vec(a)}，{vec(AD)=vec(b)}，{vec(AA_1)=vec(c)}。分別用 {vec(a)}、{vec(b)}、{vec(c)} 表示體對角線 {vec(AC_1)} 和 {vec(BD_1)}。'),
    shaded_box('提示：先用 {vec(a)}、{vec(b)} 表示 {vec(AC)}（ABCD 是平行四邊形），再各自加返個 {vec(c)} 方向嘅段。'),
] + write_lines(6), trailing_blank=False))

P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('1．{x=3}，{y=-2}，{z=1}（已經是基底表示式，直接讀出係數）'))
P.append(para('2．{vec(DB_1)=vec(a)+vec(b)+vec(c)}'))
P.append(para('3．不能。基底要求三個向量不共面，但零向量與任何向量都視為共面（線性相關），所以含零向量的一組向量不能作基底。'))
P.append(para('4．{vec(DN)=frac(1,2)*vec(a)+vec(c)}（{N} 是 {A_1D_1} 中點，{vec(DA_1)=vec(a)+vec(c)}，{vec(DD_1)=vec(c)}，{vec(DN)=frac(1,2)*(vec(DA_1)+vec(DD_1))=frac(1,2)*(vec(a)+2*vec(c))=frac(1,2)*vec(a)+vec(c)}）'))
P.append(para('5．{vec(OP)=frac(1,3)*(vec(a)+vec(b)+vec(c))}（重心公式由2D推廣到3D依然成立，詳見驗算記錄的中線法推導）'))
P.append(para('6．{x=0}，{y=0}，{z=0}。因為零向量本身已經有一種寫法 {vec(0)=0*vec(a)+0*vec(b)+0*vec(c)}，根據基本定理嘅唯一性，呢個係【唯一】嘅表示法，所以 x、y、z 一定全部是0。'))
P.append(para('7．{vec(BC_1)=-vec(a)+vec(b)+vec(c)}（{vec(BC)=vec(AC)-vec(AB)=vec(b)-vec(a)}，{vec(CC_1)=vec(AA_1)=vec(c)}，相加得 {vec(BC_1)=vec(b)-vec(a)+vec(c)}）'))
P.append(para('8．{vec(AC_1)=vec(a)+vec(b)+vec(c)}；{vec(BD_1)=-vec(a)+vec(b)+vec(c)}（兩條對角線係數唔同，唔可以死記「全部加埋」，要逐條想清楚由邊點行去邊點）'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_空間向量基本定理_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
