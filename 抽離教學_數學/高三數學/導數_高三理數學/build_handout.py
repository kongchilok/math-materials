# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 導數的概念及其意義
# 2026-08-10 重出：範例改用 worked_example_table（house-style 書寫規範）＋
# 新增割線→切線圖（D5 圖文雙軌，教學設計：主D5＋輔D2手順卡＋輔D14錯誤對比，
# 本課屬 S10 全新概念導入，D14「不要用在全新概念第一次教學」故本課不放 D14）。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(OUT, '_assets')
SUBJECT, UNIT = '高三數學', '導數的概念及其意義'
FOOTER = '高三數學．導數單元'


def avg_rate_formula():
    X2 = sub(mr('x'), mr('2'))
    X1 = sub(mr('x'), mr('1'))
    num = mr('f(') + X2 + mr(')-f(') + X1 + mr(')')
    den = X2 + mr('-') + X1
    return omath(frac(num, den))


def deriv_def_formula():
    X0 = sub(mr('x'), mr('0'))
    num = mr('f(') + X0 + mr('+Δx)-f(') + X0 + mr(')')
    den = mr('Δx')
    return omath(mr("f'("), X0, mr(')='), lim('Δx→0'), frac(num, den))


P = []

P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、先想一想：什麼是「變化率」？'))
P.append(para([('t', '想像你在看車速表：從第1秒到第4秒，車子平均每秒跑多快？這就是「平均變化率」——路程改變量除以時間改變量。')]))
P.append(shaded_box([
    ('t', '公式卡（平均變化率／割線斜率）：'), ('m', avg_rate_formula()),
], kind='hint'))
P.append(para([('t', '如果我們把「時間改變量」壓縮到幾乎是 0（也就是只看「這一瞬間」），就得到「瞬時變化率」——這就是「導數」，幾何上就是切線的斜率。')]))
P.append(shaded_box([
    ('t', '公式卡（導數的定義）：'), ('m', deriv_def_formula()),
], kind='hint'))
P.append(blank())

P.append(heading('二、範例：用定義求 f(x)=x² 的導數'))
P.append(image_para(os.path.join(FIG, 'fig_concept_tangent.png'), width_cm=8.0,
                    caption='由割線（虛線，連接兩點的平均變化率）到切線（實線貼著曲線那一條）——'
                            '導數就是「Δx 壓縮到 0」之後，割線變成的那條切線的斜率。'))
P.append(shaded_box([('t', '跟著這四個固定步驟，之後每一題都用同一套框架，不用重新想。這套框架接下來會用在《練習》講義的每一題上。')], kind='hint'))
P.append(worked_example_table([
    eq_row('{f(x+Δx)}', '{(x+Δx)^2}', '① 先把 x+Δx 代入 f'),
    eq_row('{f(x+Δx)-f(x)}', '{(x+Δx)^2-x^2}', '② 相減，準備展開'),
    eq_row('{f(x+Δx)-f(x)}', '{2xΔx+Δx^2}', '　展開化簡'),
    eq_row('{frac(f(x+Δx)-f(x),Δx)}', '{2x+Δx}', '③ 兩邊除以 Δx，化簡'),
    span_row('④ 令 {Δx->0}：{lim(Δx->0,(2x+Δx))=2x}', '把 Δx 壓縮到 0，這就是「瞬時」變化率'),
    answer_row('{f\'(x)=2x}'),
], why_pct=0.38))
P.append(blank())

P.append(heading('三、順便一提：導數也可以用來「線性估計」'))
P.append(para('如果 {Δx} 很小，切線幾乎貼著曲線，所以可以用切線去估計 {f(x_0+Δx)}：'))
P.append(shaded_box([('t', '公式卡（線性估計）：'), ('m', omath(mr('f('), sub(mr('x'), mr('0')), mr('+Δx)'), mr(' ≈ '), mr('f('), sub(mr('x'), mr('0')), mr(')+'), mr("f'("), sub(mr('x'), mr('0')), mr(')·Δx')))], kind='hint'))
P.append(para('例如：{f(x)=sqrt(x)}，已知 {f(4)=2}、{f\'(4)=frac(1,4)}，估計 {sqrt(4.1)}：'))
P.append(para('{sqrt(4.1)≈2+frac(1,4)*0.1=2.025}　（實際值約 2.0248，非常接近）'))
P.append(blank())

P.append(shaded_box([('t', '接下來請拿《導數的概念及其意義——課堂練習》，依這套框架完成練習A、B、C。')], kind='worked'))

P += teacher_notes(
    main_design='D5 圖文雙軌',
    aux_designs=('D2 手順卡',),
    reason='S10 全新概念導入：導數的定義純用代數符號（極限式）學生無法建立心像，'
           '用「割線→切線」的圖直接呈現「瞬時變化率」是什麼、避免只靠符號憑空想像。'
           '本課是全新概念的第一課，依 teaching-designs.md D14 條目「不要用在全新概念的第一次教學」，'
           '本課不放錯誤分析對比，留到單調性／凹凸性兩課（學生已有導數概念後）才用。',
    density='抽離小班（Tier 2）',
    fading='完整割線→切線圖＋四步驟框架 → 只給圖，四步驟自己寫 → 只給定義式，自己畫圖說明',
    iep_codes=('a3 提示題目重點（公式卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_導數的概念及其意義_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
