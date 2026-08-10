# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 空間向量的概念與線性運算
# 對應課本 1.1.1 前半；開首「複習：平面向量」段落係進度表1.1目標第1點要求嘅
# 自編橋接內容（課本1.1.1一開始就假設識平面向量，直接推廣到空間，冇重教）。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '空間向量的概念與線性運算'
FOOTER = '高三數學．空間向量單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、複習：平面向量（自編橋接內容，課本沒有）'))
P.append(para('向量：既有大小、又有方向的量，記做 {vec(a)} 或 {vec(AB)}（由 A 指向 B）。'))
P.append(shaded_box('相等向量：大小相等、方向相同（起點在哪裡不影響）　　相反向量：大小相等、方向相反，記做 {-vec(a)}　　零向量：大小為0，記做 {vec(0)}'))
P.append(para('三角形法則（首尾相接）：{vec(AB)+vec(BC)=vec(AC)}　　數乘 {λ*vec(a)}：方向與 {vec(a)} 相同（λ>0）或相反（λ<0），大小是 {|λ|*|vec(a)|}'))
P.append(para('共線向量：{vec(b)=λ*vec(a)}（{vec(a)≠vec(0)}），λ 是實數。'))
P.append(blank())

P.append(heading('二、從平面推廣到空間'))
P.append(para('以上定義搬到空間（3D）完全一樣用得——向量只看大小同方向，同起點放在哪裡、活在平面定空間無關。'))
P.append(shaded_box('新概念「共面向量」：幾個向量的起點放在同一點之後，如果它們都落在同一個平面上，就叫共面向量。這件事在平面（2D）裡必然成立（整個世界得一個平面），但在空間（3D）裡不一定成立——所以「共面向量」是空間才有意義的新概念。'))
P.append(blank())

P.append(heading('三、範例：用向量加法化簡'))
P.append(para('在正方體 {ABCD}-{A_1B_1C_1D_1} 中，化簡：{vec(AB)+vec(BC)+vec(CC_1)}'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
media = MediaRegistry()
P.append(dual_track_table([
    (image_para(os.path.join(FIG, 'u1_fig1.png'), width_cm=6.5),
     '已知：正方體 ABCD-A₁B₁C₁D₁，要化簡 AB+BC+CC₁ 這條「首尾相接」的向量鏈。粗箭嘴 AC₁ 就是最終答案（體對角線）。'),
], media=media))
P.append(worked_example_table([
    eq_row('{vec(AB)+vec(BC)}', '{vec(AC)}', '① 先合併前兩項，用三角形法則（首尾相接：A→B→C）'),
    eq_row('{vec(AC)+vec(CC_1)}', '{vec(AC_1)}', '② 再同第三項相加，再用一次三角形法則（首尾相接：A→C→C₁）'),
    answer_row('{vec(AB)+vec(BC)+vec(CC_1)=vec(AC_1)}', '③ 合併結果'),
    span_row('④ 睇返個圖，{vec(AC_1)} 正正就是正方體嘅「體對角線」——由 A 一直去到對面嗰隻角 {C_1}（圖中粗箭嘴）。'),
], why_pct=0.4))
P.append(blank())

P.append(heading('四、中點公式'))
P.append(para('若 M 是 {vec(AB)} 的中點，O 是空間中任意一點，則：'))
P.append(shaded_box('{vec(OM)=frac(1,2)*(vec(OA)+vec(OB))}'))
P.append(para('呢條公式好有用，之後求「中點坐標」都係靠佢，記住佢嘅樣。'))
P.append(blank())

P.append(shaded_box('接下來請拿《空間向量的概念與線性運算——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D5 圖文雙軌',
    aux_designs=('D2 手順卡',),
    reason='S9 立體幾何與空間：向量鏈式加法（首尾相接）純用符號推導，學生難以想像「AB+BC+CC₁」'
           '最終變成一條對角線，用正方體圖與代數步驟逐列對齊，把抽象的向量運算釘進具體的3D空間位置；'
           '四步驟固定框架以D2手順卡落地，之後每一題都套同一套流程。',
    density='抽離小班（Tier 2）',
    fading='圖文雙軌完整版 → 只給圖，步驟自己寫 → 不給圖，只憑向量式自己畫',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_空間向量的概念與線性運算_抽離小班共用版.docx'),
    footer_text=FOOTER,
    media=media,
)
print(out)
