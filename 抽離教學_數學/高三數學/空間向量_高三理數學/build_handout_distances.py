# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 空間中的距離（對應課本 1.2.5）
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間中的距離'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、複習：兩點間的距離'))
P.append(para('已知 {A(x_1,y_1,z_1)}、{B(x_2,y_2,z_2)}：{|AB|=sqrt((x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2)}（第4課學過）'))
P.append(blank())

P.append(heading('二、點到平面的距離'))
P.append(para('已知平面 α 的法向量是 {vec(n)}，A 是平面內任意一點，P 是平面外一點：'))
P.append(shaded_box('{d=frac(|vec(AP)·vec(n)|,|vec(n)|)}'))
P.append(para('呢條公式嘅諗法：{vec(AP)} 呢個向量入面，真正「垂直於平面」嘅分量先係我哋要嘅距離；用 {vec(AP)} 同單位法向量做數量積，就係將 {vec(AP)} 投影到法向量方向，攞到嘅正正就係垂直距離。'))
P.append(blank())

P.append(heading('三、點到直線的距離（了解）'))
P.append(para('已知直線 l 過點 A，方向向量係 {vec(v)}，P 是直線外一點。将 {vec(AP)} 分做「沿住 {vec(v)} 方向」同「垂直於 {vec(v)}」兩個分量，垂直嗰個分量嘅長度就係距離：'))
P.append(shaded_box('{d=sqrt(|vec(AP)|^2-frac((vec(AP)·vec(v))^2,|vec(v)|^2))}'))
P.append(para('（呢條式其實係畢氏定理：{|vec(AP)|} 係斜邊，投影長 {frac(vec(AP)·vec(v),|vec(v)|)} 係一條直角邊，距離 d 係另一條直角邊）'))
P.append(blank())

P.append(heading('四、線面平行、面面平行時的距離'))
P.append(shaded_box('若直線 l 平行於平面 α，求 l 到 α 嘅距離，可以喺 l 上面隨便揀一點，改做求呢一點到 α 嘅距離（一條線平行於一個平面，線上面每一點到平面嘅距離都相等）。'))
P.append(blank())

P.append(heading('五、範例：求點到平面的距離'))
P.append(para('正方體 {ABCD}-{A_1B_1C_1D_1} 棱長為2，以 D 為原點建系（同之前幾課一樣）。求 {B_1} 到平面 {ACD_1} 的距離。'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
media = MediaRegistry()
P.append(dual_track_table([
    (image_para(os.path.join(FIG, 'u4_fig1.png'), width_cm=6.5),
     '已知：正方體棱長2，平面ACD₁的法向量n=(1,1,1)（上一課求過）。要求：B₁到平面ACD₁的距離d。'),
], media=media))
P.append(worked_example_table([
    span_row('① 平面 {ACD_1} 上兩課求過法向量 {vec(n)=(1,1,1)}，喺平面內揀一個已知點：{A(2,0,0)}'),
    eq_row('{vec(AB_1)}', '{B_1(2,2,2)}，{vec(AB_1)=(0,2,2)}', '② 寫出 B₁ 坐標，求 AB₁'),
    answer_row('{d=frac(|vec(AB_1)·vec(n)|,|vec(n)|)=frac(|0+2+2|,sqrt(3))=frac(4,sqrt(3))=frac(4*sqrt(3),3)}', '③ 代入公式'),
    span_row('④ 所以距離是 {frac(4*sqrt(3),3)}（約2.31）。可以換平面內另一點 {C(0,2,0)} 驗算：{vec(CB_1)=(2,0,2)}，{vec(CB_1)·vec(n)=2+0+2=4}，結果一樣，證明公式同揀邊個平面內嘅點無關。'),
], why_pct=0.36))
P.append(blank())

P.append(shaded_box('接下來請拿《空間中的距離——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D5 圖文雙軌',
    aux_designs=('D7 判定定理卡', 'D2 手順卡'),
    reason='S9 立體幾何與空間：點到平面距離公式要靠圖先睇到「邊個係平面內嘅已知點」「B₁喺平面邊一側」，'
           '圖文雙軌把公式同空間位置對應埋一齊；點到平面／點到直線兩條公式易撞埋，'
           '沿用上一課嘅D7判定定理卡（觸發語＋公式）幫學生分清楚幾時用邊條，並以D2手順卡落地四步驟。',
    density='抽離小班（Tier 2）',
    fading='圖文雙軌完整版 → 只給圖，步驟自己寫 → 不給圖，只憑法向量與坐標自己判斷',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_空間中的距離_抽離小班共用版.docx'),
    footer_text=FOOTER,
    media=media,
)
print(out)
