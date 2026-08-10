# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 空間向量基本定理（對應課本 1.1.2）
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間向量基本定理'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、複習：平面向量基本定理'))
P.append(para('若 {vec(e_1)}、{vec(e_2)} 是同一平面內兩個不共線的向量，咁呢個平面內任何一個向量 {vec(a)} 都可以【唯一】咁樣表示做：'))
P.append(shaded_box('{vec(a)=x*vec(e_1)+y*vec(e_2)}　（x、y 是實數）'))
P.append(para('{vec(e_1)}、{vec(e_2)} 就叫做呢個平面嘅一組「基底」。'))
P.append(blank())

P.append(heading('二、共面向量定理（新）'))
P.append(para('若 {vec(a)}、{vec(b)} 不共線，咁向量 {vec(p)} 與 {vec(a)}、{vec(b)} 共面 ⟺ 存在【唯一】一對實數 x、y，使得：'))
P.append(shaded_box('{vec(p)=x*vec(a)+y*vec(b)}'))
P.append(blank())

P.append(heading('三、空間向量基本定理'))
P.append(para('若三個向量 {vec(a)}、{vec(b)}、{vec(c)} 不共面，咁空間入面任何一個向量 {vec(p)} 都可以【唯一】咁樣表示做：'))
P.append(shaded_box('{vec(p)=x*vec(a)+y*vec(b)+z*vec(c)}　（x、y、z 是實數）'))
P.append(para('{vec(a)}、{vec(b)}、{vec(c)} 就叫做空間嘅一組「基底」。'))
P.append(para('注意：基底唔需要互相垂直，都唔需要長度相等——淨係要求三個向量唔喺同一個平面（唔共面）就得。之前幾課用嘅正方體三條棱，只係一種方便、常見嘅特殊情況。'))
P.append(blank())

P.append(heading('四、範例：用基底表示向量'))
P.append(para('正方體 {ABCD}-{A_1B_1C_1D_1} 中，設 {vec(DA)=vec(a)}，{vec(DC)=vec(b)}，{vec(DD_1)=vec(c)}（{vec(a)}、{vec(b)}、{vec(c)} 是一組基底）。M 是 {A_1C_1} 的中點，用 {vec(a)}、{vec(b)}、{vec(c)} 表示 {vec(DM)}。'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
media = MediaRegistry()
P.append(dual_track_table([
    (image_para(os.path.join(FIG, 'u1_fig2.png'), width_cm=6.0),
     '已知：a=DA、b=DC、c=DD₁ 是一組基底，M 是 A₁C₁ 的中點。要求：用 a、b、c 表示 DM。'),
], media=media))
P.append(worked_example_table([
    span_row('① 先用基底表示 {A_1}、{C_1} 的位置向量（以 D 為參考點）：{vec(DA_1)=vec(DA)+vec(AA_1)=vec(a)+vec(c)}（{vec(AA_1)=vec(DD_1)=vec(c)}，正方體對邊平行且相等）；同理：{vec(DC_1)=vec(DC)+vec(CC_1)=vec(b)+vec(c)}'),
    eq_row('{vec(DM)}', '{frac(1,2)*(vec(DA_1)+vec(DC_1))}', '② 用中點公式'),
    span_row('代入①嘅結果：{vec(DA_1)+vec(DC_1)=(vec(a)+vec(c))+(vec(b)+vec(c))=vec(a)+vec(b)+2*vec(c)}'),
    answer_row('{vec(DM)=frac(1,2)*(vec(a)+vec(b)+2*vec(c))=frac(1,2)*vec(a)+frac(1,2)*vec(b)+vec(c)}', '③ 化簡'),
    span_row('④ 所以 {x=frac(1,2)}、{y=frac(1,2)}、{z=1}——根據基本定理，呢組係數係【唯一】嘅，冇第二種寫法。'),
], why_pct=0.36))
P.append(blank())

P.append(shaded_box('接下來請拿《空間向量基本定理——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D5 圖文雙軌',
    aux_designs=('D2 手順卡',),
    reason='S9 立體幾何與空間：基底分解（DA₁=DA+AA₁）需要同時追蹤「代數式子」同「圖上邊嘅對應關係」'
           '（例如AA₁=DD₁靠正方體對邊平行相等），圖文雙軌把兩者釘在一起；四步驟固定框架以D2手順卡落地。',
    density='抽離小班（Tier 2）',
    fading='圖文雙軌完整版 → 只給圖，步驟自己寫 → 不給圖，只憑向量式自己畫',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_空間向量基本定理_抽離小班共用版.docx'),
    footer_text=FOOTER,
    media=media,
)
print(out)
