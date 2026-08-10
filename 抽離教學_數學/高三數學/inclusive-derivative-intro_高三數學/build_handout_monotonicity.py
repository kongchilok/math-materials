# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 導數在研究函數中的應用（單調性與極值）
# 2026-08-10 重出：①新增函數圖（design_svg.parabola_graph，原本零圖，違反
# 「講圖就要出圖」鐵律）②範例改用 worked_example_table＋or_row（house-style
# 書寫規範）③新增 D14 錯誤分析對比（「只解 f'(x)=0 就當極值，冇驗證變號」是
# 已知高頻錯誤——教學計劃丙班理組進度表明文列出呢個常見錯）。
# 教學設計（主題級）：主D5圖文雙軌＋輔D2手順卡＋輔D14錯誤對比，本課S4函數與
# 圖像，D5／D14 在此課完整落地。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '導數在研究函數中的應用（單調性與極值）'
FOOTER = '高三數學．單調性與極值單元'

P = []

P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、先想一想：f\'(x) 的正負告訴我們什麼？'))
P.append(para([('t', '把函數的圖形想成一條登山步道的高度：f\'(x) 就是「現在往上爬還是往下滑」。')]))
P.append(shaded_box([('t', '① '), ('m', omath(mr("f'(x) > 0"))), ('t', '　→　f(x) 在該區間內單調「遞增」（往上爬）')], kind='hint'))
P.append(shaded_box([('t', '② '), ('m', omath(mr("f'(x) < 0"))), ('t', '　→　f(x) 在該區間內單調「遞減」（往下滑）')], kind='hint'))
P.append(shaded_box([('t', '③ '), ('m', omath(mr("f'(x) = 0"))),
                      ('t', '　→　「暫時的平地」，若左右正負變號，就是極值（左正右負＝極大點；左負右正＝極小點）')], kind='hint'))
P.append(blank())

P.append(heading('二、範例：求三次函數的單調區間與極值'))
f_ex = omath(mr('f(x)='), frac(mr('1'), mr('3')), sup(mr('x'), mr('3')), mr('−'), frac(mr('1'), mr('2')), sup(mr('x'), mr('2')), mr('−2x+1'))
P.append(para([('t', '設 '), ('m', f_ex), ('t', '，先睇圖形上「爬升／落斜」對應邊段，再逐步用代數確認：')]))
P.append(image_para(os.path.join(FIG, 'fig_monotonicity.png'), width_cm=9.0,
                    caption='由圖直接睇到：x=−1 之前爬升、x=−1 到 x=2 之間落斜、x=2 之後再爬升——'
                            '接下來的代數步驟，就是把這幅圖「算出來」。'))
P.append(shaded_box([('t', '跟著這四個固定步驟，之後每一題都用同一套框架，不用重新想。這套框架接下來會用在《練習》的每一題上。')], kind='worked'))
P.append(worked_example_table([
    span_row('{f(x)} 是多項式函數，定義域為全體實數 R', '① 確定定義域'),
    eq_row('{f\'(x)}', '{x^2-x-2}', '② 求導數'),
    eq_row('{(x-2)(x+1)}', '{0}', '因式分解 {f\'(x)=0}'),
    or_row('{x-2}', '{0}', '{x+1}', '{0}', '兩個因式各自等於 0，分兩支寫'),
    or_row('{x_1}', '{2}', '{x_2}', '{-1}', '兩支各自解出'),
    span_row('③ {x<-1}（如 {x=-2}）：{f\'(-2)=4+2-2=4>0} → 遞增', '用臨界點分段，逐段代入測正負'),
    span_row('　{-1<x<2}（如 {x=0}）：{f\'(0)=0-0-2=-2<0} → 遞減', ''),
    span_row('　{x>2}（如 {x=3}）：{f\'(3)=9-3-2=4>0} → 遞增', ''),
    answer_row('遞增區間 {(-∞,-1)} 與 {(2,+∞)}；遞減區間 {(-1,2)}；'
               '極大值 {f(-1)=frac(13,6)}；極小值 {f(2)=-frac(7,3)}',
               '④ 正負真的變號（正→負、負→正），寫結論'),
], why_pct=0.30))
P.append(blank())

P.append(heading('三、常見錯誤 vs 正確寫法：判斷極值前一定要驗證變號'))
P.append(dual_track_table([
    ([para('✗ 解得 {f\'(x)=0} 的 {x=-1} 和 {x=2}，直接寫：'),
      para('「{x=-1} 和 {x=2} 就是極值點」——'),
      para('冇檢查左右正負是否真的變號。')],
     [para('✓ 解出 {f\'(x)=0} 之後，一定要用三段區間分別代入 {f\'(x)} 測正負，', shd=GREY_FILL),
      para('※ 正負真的變號，先算極值——', shd=GREY_FILL),
      para('如果冇變號（例如 {f(x)=x^4} 在 {x=0}），連極值都唔係。', shd=GREY_FILL)]),
], headers=('✗ 常見寫法', '✓ 正確寫法')))
P.append(blank())

P.append(shaded_box([('t', '接下來請拿《導數在研究函數中的應用（單調性與極值）——課堂練習》，依這套框架完成練習A、B、C。')], kind='worked'))

P += teacher_notes(
    main_design='D5 圖文雙軌',
    aux_designs=('D2 手順卡', 'D14 錯誤分析對比'),
    reason='S4 函數與圖像：符號表（f\'(x)正負）↔圖形趨勢（遞增/遞減/極值）的對應是本課核心瓶頸，'
           '原本零圖只靠文字覆述，改用實際函數圖直接呈現；D14 專治「只解 f\'(x)=0 就當極值、'
           '漏驗證變號」這個已知高頻錯誤（教學計劃丙班理組進度表已明文列出）。',
    density='抽離小班（Tier 2）',
    fading='圖＋完整步驟卡＋D14對比框 → 只給圖，步驟自己寫 → 只給空白數線，自己畫段測正負',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a11 提供公式卡'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_導數在研究函數中的應用(單調性與極值)_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
