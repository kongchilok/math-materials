# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 空間向量的數量積（對應課本 1.1.1 後半）
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間向量的數量積'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、兩個向量的夾角'))
P.append(para('兩個非零向量 {vec(a)}、{vec(b)}，將佢哋移到同一個起點，中間嗰隻角就叫「夾角」，記做 {⟨vec(a),vec(b)⟩}，範圍是 0° 到 180° 之間（包含 0° 和 180°）。'))
P.append(blank())

P.append(heading('二、數量積的定義'))
P.append(shaded_box('{vec(a)·vec(b)=|vec(a)|*|vec(b)|*fn(cos)⟨vec(a),vec(b)⟩}'))
P.append(para('注意：數量積嘅結果係一個數（純量），唔係向量！呢點好易同「數乘」（{λ*vec(a)}，結果係向量）攪混，要分清楚。'))
P.append(para('特別情況：{vec(a)·vec(a)=|vec(a)|^2}（即係模嘅平方）；零向量同任何向量嘅數量積都是 0。'))
P.append(blank())

P.append(heading('三、數量積的重要性質'))
P.append(shaded_box('① 交換律：{vec(a)·vec(b)=vec(b)·vec(a)}　　② 分配律：{vec(a)·(vec(b)+vec(c))=vec(a)·vec(b)+vec(a)·vec(c)}'))
P.append(shaded_box('③ 數乘結合：{(λ*vec(a))·vec(b)=λ*(vec(a)·vec(b))}　　④ 【最重要】{vec(a)⊥vec(b)} ⟺ {vec(a)·vec(b)=0}（{vec(a)}、{vec(b)} 都不是零向量）'))
P.append(para('性質④之後成日用嚟判斷垂直、或者已知垂直去化簡計算，一定要記熟。'))
P.append(blank())

P.append(heading('四、範例：用分配律求夾角'))
P.append(para('正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為 {a}，求 {vec(AB)} 與 {vec(AC_1)} 的夾角餘弦值。'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
media = MediaRegistry()
P.append(dual_track_table([
    (image_para(os.path.join(FIG, 'u1_fig1.png'), width_cm=6.5),
     '已知：正方體棱長 a，AC₁ 拆做 AB+BC+CC₁ 三條互相垂直的棱（圖中粗箭嘴）。要求：AB 與 AC₁ 的夾角餘弦值。'),
], media=media))
P.append(worked_example_table([
    span_row('① 用返上一課學過嘅拆法：{vec(AC_1)=vec(AB)+vec(BC)+vec(CC_1)}'),
    span_row('② 求 {vec(AB)·vec(AC_1)}，用分配律展開，並用性質④（互相垂直的邊，數量積為0）：'
              '{vec(AB)·vec(AC_1)=vec(AB)·vec(AB)+vec(AB)·vec(BC)+vec(AB)·vec(CC_1)=a^2+0+0=a^2}'
              '（{vec(AB)} 與 {vec(BC)} 垂直、{vec(AB)} 與 {vec(CC_1)} 垂直，都是正方體相鄰的棱）'),
    eq_row('{|vec(AC_1)|^2}', '{a^2+a^2+a^2=3*a^2}', '③ 求 {|vec(AC_1)|}：因為三條棱互相垂直'),
    span_row('所以 {|vec(AC_1)|=sqrt(3)*a}'),
    answer_row('{fn(cos)⟨vec(AB),vec(AC_1)⟩=frac(vec(AB)·vec(AC_1),|vec(AB)|*|vec(AC_1)|)=frac(a^2,a*sqrt(3)*a)=frac(1,sqrt(3))=frac(sqrt(3),3)}',
               '④ 代入定義式，反推餘弦值'),
], why_pct=0.36))
P.append(blank())

P.append(shaded_box('接下來請拿《空間向量的數量積——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D5 圖文雙軌',
    aux_designs=('D2 手順卡',),
    reason='S9 立體幾何與空間：分配律展開靠「邊與邊互相垂直」呢個空間事實去消去交叉項，'
           '純睇代數式睇唔出邊兩條係垂直，一定要對住圖先睇到；四步驟固定框架以D2手順卡落地。',
    density='抽離小班（Tier 2）',
    fading='圖文雙軌完整版 → 只給圖，步驟自己寫 → 不給圖，只憑向量式自己畫',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_空間向量的數量積_抽離小班共用版.docx'),
    footer_text=FOOTER,
    media=media,
)
print(out)
