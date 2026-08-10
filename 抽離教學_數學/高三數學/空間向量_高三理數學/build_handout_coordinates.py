# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 空間向量的坐標與坐標運算（對應課本 1.1.3）
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間向量的坐標與坐標運算'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、空間直角坐標系'))
P.append(para('喺空間入面搵一點 O 做原點，畫三條互相垂直嘅數線：x軸、y軸、z軸，就構成「空間直角坐標系」，記做 {Oxyz}。'))
P.append(para('若 {vec(i)}、{vec(j)}、{vec(k)} 分別是 x、y、z 軸方向嘅單位向量（長度為1、互相垂直），咁任何向量 {vec(p)} 都可以寫成 {vec(p)=x*vec(i)+y*vec(j)+z*vec(k)}，({x,y,z}) 就叫做 {vec(p)} 嘅「坐標」。'))
P.append(blank())

P.append(heading('二、坐標運算公式'))
P.append(para('已知 {vec(a)=(x_1,y_1,z_1)}，{vec(b)=(x_2,y_2,z_2)}：'))
P.append(shaded_box('加減：{vec(a)+-vec(b)=(x_1+-x_2,y_1+-y_2,z_1+-z_2)}　　數乘：{λ*vec(a)=(λ*x_1,λ*y_1,λ*z_1)}'))
P.append(shaded_box('數量積：{vec(a)·vec(b)=x_1*x_2+y_1*y_2+z_1*z_2}　　模長：{|vec(a)|=sqrt(x_1^2+y_1^2+z_1^2)}'))
P.append(shaded_box('平行：{vec(a)∥vec(b)} ⟺ {x_1=λ*x_2}、{y_1=λ*y_2}、{z_1=λ*z_2}（分量成比例）'))
P.append(shaded_box('垂直：{vec(a)⊥vec(b)} ⟺ {x_1*x_2+y_1*y_2+z_1*z_2=0}'))
P.append(para('呢組公式最大用處：以前要用分配律逐項展開先計到嘅數量積、要用基底湊出嚟嘅模長，而家淨係代坐標入公式，一步到位。'))
P.append(blank())

P.append(heading('三、兩點距離與中點坐標'))
P.append(para('已知 {A(x_1,y_1,z_1)}、{B(x_2,y_2,z_2)}：'))
P.append(shaded_box('距離：{|AB|=sqrt((x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2)}　　中點：{(frac(x_1+x_2,2),frac(y_1+y_2,2),frac(z_1+z_2,2))}'))
P.append(blank())

P.append(heading('四、範例：建坐標系＋求距離'))
P.append(para('正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2。以 D 為原點建立空間直角坐標系（{vec(DA)} 沿 x 軸、{vec(DC)} 沿 y 軸、{vec(DD_1)} 沿 z 軸），求體對角線 {|AC_1|}。'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
media = MediaRegistry()
P.append(dual_track_table([
    (image_para(os.path.join(FIG, 'u4_fig1.png'), width_cm=6.5),
     '已知：正方體棱長2，D 為原點，DA/DC/DD₁ 分別沿 x/y/z 軸。要求：體對角線 |AC₁|。'),
], media=media))
P.append(worked_example_table([
    span_row('① 寫出各頂點坐標：{D(0,0,0)}、{A(2,0,0)}、{B(2,2,0)}、{C(0,2,0)}、{D_1(0,0,2)}、{A_1(2,0,2)}、{B_1(2,2,2)}、{C_1(0,2,2)}'),
    eq_row('{vec(AC_1)}', '{(0-2,2-0,2-0)=(-2,2,2)}', '② 求 AC₁ 的坐標（終點坐標減起點坐標）'),
    answer_row('{|AC_1|=sqrt((-2)^2+2^2+2^2)=sqrt(4+4+4)=sqrt(12)=2*sqrt(3)}', '③ 代入距離公式'),
    span_row('④ 對比：呢個結果同之前用「向量分解＋分配律」方法算出嚟嘅 {|AC_1|=sqrt(3)*a}（{a=2}時即 {2*sqrt(3)}）完全一致——坐標法係另一條路，殊途同歸，但快好多。'),
], why_pct=0.36))
P.append(blank())

P.append(shaded_box('接下來請拿《空間向量的坐標與坐標運算——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D5 圖文雙軌',
    aux_designs=('D2 手順卡',),
    reason='S9 立體幾何與空間：建坐標系呢步係「圖上邊個頂點對應邊組數字」嘅純空間判斷，'
           '離開圖就冇辦法寫出頂點坐標；四步驟固定框架以D2手順卡落地。',
    density='抽離小班（Tier 2）',
    fading='圖文雙軌完整版 → 只給圖，坐標自己寫 → 不給圖，只憑棱長自己畫坐標系',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_空間向量的坐標與坐標運算_抽離小班共用版.docx'),
    footer_text=FOOTER,
    media=media,
)
print(out)
