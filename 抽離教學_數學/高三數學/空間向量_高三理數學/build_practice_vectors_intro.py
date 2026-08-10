# -*- coding: utf-8 -*-
# 練習（三層 A/B/C）—— 空間向量的概念與線性運算
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間向量的概念與線性運算'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(blank())
P.append(para('下面全部題目都用返呢個正方體 {ABCD}-{A_1B_1C_1D_1}：'))
P.append(image_para(os.path.join(FIG, 'u1_fig2.png'), width_cm=6.5))
P.append(blank())

P.append(heading(f'練習A（{star_label(1)}）—— 向量加法基本運用'))
P.append(problem_box([
    para('1．化簡：{vec(DA)+vec(AB)}'),
] + write_lines(3)))
P.append(problem_box([
    para('2．化簡：{vec(DC)+vec(CC_1)}'),
] + write_lines(3)))
P.append(problem_box([
    para('3．已知 M 是 AB 的中點，設 {vec(DA)=vec(a)}，{vec(DB)=vec(b)}，用 {vec(a)}、{vec(b)} 表示 {vec(DM)}。'),
] + write_lines(4)))

P.append(heading(f'練習B（{star_label(2)}）—— 較長的化簡與判斷'))
P.append(problem_box([
    para('4．化簡：{vec(AB)+vec(BC)+vec(CC_1)+vec(C_1D_1)}'),
    shaded_box('提示：一步步用三角形法則「首尾相接」，逐項合併，唔使一次過諗晒成條式。'),
] + write_lines(5)))
P.append(problem_box([
    para('5．化簡：{vec(AB)+vec(CD)}'),
    shaded_box('提示：先睇下 {vec(AB)} 和 {vec(CD)} 的方向、大小有咩關係（睇返個正方體），未必要硬套三角形法則。'),
] + write_lines(4)))
P.append(problem_box([
    para('6．{vec(DB_1)} 是正方體的體對角線，M 是 {vec(DB_1)} 的中點。設 {vec(DA)=vec(a)}，{vec(DC)=vec(b)}，{vec(DD_1)=vec(c)}，用 {vec(a)}、{vec(b)}、{vec(c)} 表示 {vec(DM)}。'),
    shaded_box('提示：先用 {vec(a)}、{vec(b)}、{vec(c)} 表示 {vec(DB_1)}（睇下由 D 去 B₁ 點樣行），再用中點公式。'),
] + write_lines(5)))

P.append(heading(f'練習C（{star_label(3)}）—— 綜合應用'))
P.append(problem_box([
    para('7．空間四邊形 ABCD（四點不一定在同一平面），M、N 分別是對角線 AC、BD 的中點。求證：'),
    shaded_box('{vec(MN)=frac(1,2)*(vec(AB)+vec(CD))}'),
] + write_lines(8)))
P.append(problem_box([
    para('8．在正方體 {ABCD}-{A_1B_1C_1D_1} 中，P 是 {vec(CC_1)} 的中點。設 {vec(DA)=vec(a)}，{vec(DC)=vec(b)}，{vec(DD_1)=vec(c)}，用 {vec(a)}、{vec(b)}、{vec(c)} 表示 {vec(AP)}。'),
] + write_lines(6), trailing_blank=False))

P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('1．{vec(DB)}　　2．{vec(DC_1)}　　3．{vec(DM)=frac(1,2)*(vec(a)+vec(b))}'))
P.append(para('4．{vec(AD_1)}（四項首尾相接，逐步合併：AB+BC=AC，AC+CC₁=AC₁，AC₁+C₁D₁=AD₁）'))
P.append(para('5．{vec(0)}（因為 ABCD 是正方形，{vec(AB)} 與 {vec(CD)} 大小相等、方向相反，即 {vec(CD)=-vec(AB)}）'))
P.append(para('6．{vec(DM)=frac(1,2)*(vec(a)+vec(b)+vec(c))}（先由 {vec(DB_1)=vec(DA)+vec(AB)+vec(BB_1)=vec(a)+vec(b)+vec(c)}，再用中點公式取一半）'))
P.append(para('7．證明：設 O 為空間任意一點。M 是 AC 中點：{vec(OM)=frac(1,2)*(vec(OA)+vec(OC))}；N 是 BD 中點：{vec(ON)=frac(1,2)*(vec(OB)+vec(OD))}。'))
P.append(para('　　{vec(MN)=vec(ON)-vec(OM)=frac(1,2)*[(vec(OB)-vec(OA))+(vec(OD)-vec(OC))]=frac(1,2)*(vec(AB)+vec(CD))}　　得證。'))
P.append(para('8．{vec(AP)=-vec(a)+vec(b)+frac(1,2)*vec(c)}（P 是 C、C₁ 中點，先用 {vec(a)}、{vec(b)}、{vec(c)} 分別表示 {vec(DC_1)}，再算 {vec(AP)=vec(DP)-vec(DA)}）'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_空間向量的概念與線性運算_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
