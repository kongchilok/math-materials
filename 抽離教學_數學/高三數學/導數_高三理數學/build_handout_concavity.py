# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 二階導數與函數的凹凸性、拐點（進度表補充內容，課本未涵蓋，自編）
# 2026-08-10 重出：①原本用文字覆述「像碗一樣」「倒扣的碗」兩張沒畫出來的圖，
# 違反「講圖就要出圖」鐵律，改用實際函數圖 ②範例改用 worked_example_table
# （house-style 書寫規範）③新增 D14 錯誤分析對比（同一題材已存在於練習C第6題，
# 現在提升到講義正文明確教一次）。
# 教學設計（主題級）：主D5圖文雙軌＋輔D2手順卡＋輔D14錯誤對比，本課S4函數與
# 圖像，D5／D14 在此課完整落地。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '二階導數與函數的凹凸性、拐點'
FOOTER = '高三數學．導數補充單元'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、什麼是「二階導數」'))
P.append(para('導數 {f\'(x)} 本身都係一個函數，所以都可以再求一次導數——呢個「導數的導數」就叫「二階導數」，寫成 {f\'\'(x)} 或 {y\'\'}。'))
P.append(shaded_box('例如：{f(x)=x^3-2x}，先求 {f\'(x)=3x^2-2}，再對 {f\'(x)} 求多一次導數：{f\'\'(x)=6x}。'))
P.append(blank())

P.append(heading('二、二階導數告訴我們「圖象的彎法」——凹凸性'))
P.append(para('一階導數 {f\'(x)} 話俾我哋知圖象「向上爬定向下滑」；二階導數 {f\'\'(x)} 就話俾我哋知圖象「點樣彎」：'))
P.append(image_para(os.path.join(FIG, 'fig_concavity.png'), width_cm=9.0,
                    caption='f(x)=x³−3x²：x=1 之前是「凸」（曲線往下彎，像倒扣的碗）、'
                            'x=1 之後是「凹」（曲線往上彎，像盛水的碗）——拐點就是彎法轉變的那一點。'))
P.append(shaded_box('① {f\'\'(x) > 0}　→　圖象是「凹」的（像碗一樣，會盛到水）'))
P.append(shaded_box('② {f\'\'(x) < 0}　→　圖象是「凸」的（像倒扣的碗，水會流走）'))
P.append(para('小提示：凹凸性同單調性（遞增／遞減）係兩件唔同嘅事——遞增的圖象可以是凹的，都可以是凸的，要分開看。'))
P.append(blank())

P.append(heading('三、拐點——凹凸性「轉變」的點'))
P.append(para('如果圖象喺某一點左右兩側，凹凸性由「凹」變「凸」（或由「凸」變「凹」），呢一點就叫「拐點」（inflection point）。'))
P.append(shaded_box('搵拐點嘅步驟：①求 {f\'\'(x)}　②解 {f\'\'(x)=0}，搵出可能嘅 x 值　③檢查呢個 x 左右兩側 {f\'\'(x)} 是否真係變號——變咗號先係拐點，冇變號就唔算。'))
P.append(blank())

P.append(heading('四、範例：求三次函數的凹凸區間與拐點'))
P.append(para('設 {f(x)=x^3-3x^2}：'))
P.append(shaded_box('跟著這四個固定步驟，之後每一題都用同一套框架，不用重新想。這套框架接下來會用在《練習》的每一題上。', kind='worked'))
P.append(worked_example_table([
    eq_row('{f\'(x)}', '{3x^2-6x}', '① 求一階導數'),
    eq_row('{f\'\'(x)}', '{6x-6}', '　再求二階導數'),
    eq_row('{6x-6}', '{0}', '② 令 f\'\'(x)=0，解可能拐點'),
    span_row('解得 {x=1}（候選拐點，仲未確定）', ''),
    span_row('③ {x<1}（如 {x=0}）：{f\'\'(0)=6*0-6=-6<0} → 凸', '檢查候選點左右正負'),
    span_row('　{x>1}（如 {x=2}）：{f\'\'(2)=6*2-6=6>0} → 凹', ''),
    answer_row('{x<1} 時凸、{x>1} 時凹，左右變號，拐點為 {(1,f(1))=(1,-2)}',
               '④ 正負真的變號，寫結論；拐點 y 坐標 {f(1)=1-3=-2}'),
], why_pct=0.32))
P.append(blank())

P.append(heading('五、常見錯誤 vs 正確寫法：f\'\'(x₀)=0 唔一定係拐點'))
P.append(dual_track_table([
    ([para('✗ 只要 {f\'\'(x_0)=0}，就直接寫：'),
      para('「{(x_0,f(x_0))} 一定是拐點」——'),
      para('冇檢查左右正負是否真的變號。')],
     [para('✓ {f\'\'(x_0)=0} 只是拐點的「必要條件」，', shd=GREY_FILL),
      para('※ 仲要檢查左右正負係咪真係變咗——', shd=GREY_FILL),
      para('例如 {f(x)=x^4}：{f\'\'(x)=12x^2}，{f\'\'(0)=0}，但 0 左右 {f\'\'(x)} 都 {>=0}（冇變號），', shd=GREY_FILL),
      para('所以 {x=0} 唔係拐點。', shd=GREY_FILL)]),
], headers=('✗ 常見寫法', '✓ 正確寫法')))
P.append(blank())

P.append(shaded_box('接下來請拿《二階導數與函數的凹凸性、拐點——課堂練習》，依這套框架完成練習A、B、C。', kind='worked'))

P += teacher_notes(
    main_design='D5 圖文雙軌',
    aux_designs=('D2 手順卡', 'D14 錯誤分析對比'),
    reason='S4 函數與圖像：凹凸性的核心正是「圖象點樣彎」，原本用文字覆述「像碗」「倒扣的碗」'
           '兩張沒畫出來的圖，違反「講圖就要出圖」，改用實際函數圖直接呈現；D14 專治'
           '「f\'\'(x₀)=0 就當一定是拐點」這個已知高頻錯誤（原本只藏在練習C第6題答案，'
           '現在提升到講義正文明確教一次）。',
    density='抽離小班（Tier 2）',
    fading='圖＋完整步驟卡＋D14對比框 → 只給圖，步驟自己寫 → 只給空白數線，自己畫段測正負',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a11 提供公式卡'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_二階導數與函數的凹凸性拐點_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
