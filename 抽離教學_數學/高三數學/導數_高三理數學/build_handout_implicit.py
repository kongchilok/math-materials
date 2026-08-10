# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 隱函數求導（進度表補充內容，課本未涵蓋，自編）
# 2026-08-10 重出：範例改用 worked_example_table（house-style 書寫規範）。
# 教學設計（主題級）：主D5＋輔D2＋輔D14——本課屬 S2 多步驟程序運算，以 D2
# 手順卡落地（見《工具卡_導數運算與判定手順卡》）。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '隱函數求導'
FOOTER = '高三數學．導數補充單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、顯函數 vs 隱函數'))
P.append(para('以前見開嘅 {y=x^2+1} 呢種，y 已經直接用 x 表示出嚟，叫「顯函數」。'))
P.append(para('但好似 {x^2+y^2=25}（一個圓）呢種，y 冇直接解出嚟，x 同 y 混埋一齊——呢種叫「隱函數」。y 其實都係 x 嘅函數，只係冇明寫出嚟。'))
P.append(blank())

P.append(heading('二、點做隱函數求導'))
P.append(para('做法好簡單：兩邊同時對 x 求導。淨係要記住一件事——遇到 y 嘅項，要當佢係 x 嘅函數，用返鏈式法則，求導時要多乘一個 {y\'}：'))
P.append(shaded_box('公式卡（y 項求導，規律同冪法則一樣，但每次都要多乘一個 {y\'}）：{y^2} 求導 → {2y*y\'}　　{y^3} 求導 → {3y^2*y\'}　　{5y} 求導 → {5y\'}'))
P.append(para('求完之後，將所有 {y\'} 嘅項移埋一邊，解出 {y\'}。'))
P.append(blank())

P.append(heading('三、範例：求圓方程的 y\''))
P.append(para('設 {x^2+y^2=25}，求 {y\'}：'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架，不用重新想。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
P.append(worked_example_table([
    eq_row('{2x+2y*y\'}', '{0}', '① 兩邊對 x 求導：{x^2}→{2x}；{y^2}→{2y*y\'}；右邊 {25}→{0}'),
    eq_row('{2y*y\'}', '{-2x}', '② 移項，將 {y\'} 的項放一邊'),
    eq_row('{y\'}', '{-frac(2x,2y)}', '③ 兩邊除以 {2y}'),
    answer_row('{y\'=-frac(x,y)}', '化簡'),
    span_row('④ 驗算（選）：在 {(3,4)} 這點（{3^2+4^2=25}，在圓上）：{y\'=-frac(3,4)}', '代入檢查'),
], why_pct=0.36))
P.append(blank())

P.append(shaded_box('接下來請拿《隱函數求導——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D2 手順卡',
    aux_designs=('D5 圖文雙軌',),
    reason='S2 多步驟程序運算：「見到 y 項要多乘 y\'」是本課唯一但最容易漏的步驟，'
           '以《工具卡_導數運算與判定手順卡》落地手順卡；D5 圖文雙軌留給單調性、凹凸性兩課。',
    density='抽離小班（Tier 2）',
    fading='工具卡完整版 → 只留步驟數量提示 → 移除',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_隱函數求導_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
