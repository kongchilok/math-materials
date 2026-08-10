# -*- coding: utf-8 -*-
# 講義（概念導入＋範例）—— 基本初等函數的導數與運算法則
# 2026-08-10 重出：範例改用 worked_example_table（house-style 書寫規範）。
# 教學設計（主題級）：主D5圖文雙軌＋輔D2手順卡＋輔D14錯誤對比——本課數學結構
# 屬 S2 多步驟程序運算（純公式代入，無可畫的圖形對象），故本課以 D2 手順卡
# 落地（見同資料夾 工具卡_導數運算與判定手順卡），D5／D14 留給單調性、凹凸性
# 兩課（真正有圖可畫、有已知高頻錯法）落地。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '基本初等函數的導數與運算法則'
FOOTER = '高三數學．導數運算法則單元'

P = []

P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())
P.append(blank())

P.append(heading('一、公式卡：基本初等函數的導數'))
P.append(para([('t', '這些是「查表就能用」的固定公式，之後每一題都是套用這些公式，不用重新推導。')]))
P.append(shaded_box([('t', '① f(x)=c（c為常數） → '), ('m', omath(mr("f'(x)=0")))], kind='hint'))
P.append(shaded_box([('t', '② '), ('m', omath(mr('f(x)='), sup(mr('x'), mr('a')))), ('t', ' → '),
                      ('m', omath(mr("f'(x)=a"), sup(mr('x'), mr('a-1'))))], kind='hint'))
P.append(shaded_box([('t', '③ '), ('m', omath(mr('f(x)='), sup(mr('e'), mr('x')))), ('t', ' → '),
                      ('m', omath(mr("f'(x)="), sup(mr('e'), mr('x'))))], kind='hint'))
P.append(shaded_box([('t', '④ f(x)=ln x → '), ('m', omath(mr("f'(x)="), frac(mr('1'), mr('x'))))], kind='hint'))
P.append(shaded_box([('t', '⑤ f(x)=sin x → '), ('m', omath(mr("f'(x)=cos x")))], kind='hint'))
P.append(shaded_box([('t', '⑥ f(x)=cos x → '), ('m', omath(mr("f'(x)=-sin x")))], kind='hint'))
P.append(blank())

P.append(heading('二、公式卡：導數的運算法則'))
P.append(shaded_box([('t', '加減法則：'), ('m', omath(mr("[f(x)±g(x)]' = f'(x)±g'(x)")))], kind='hint'))
P.append(shaded_box([('t', '乘法法則：'), ('m', omath(mr("[f(x)g(x)]' = f'(x)g(x)+f(x)g'(x)")))], kind='hint'))
P.append(shaded_box([('t', '除法法則：'), ('m', omath(mr('['), frac(mr('f(x)'), mr('g(x)')), mr("]' = "),
                                              frac(mr("f'(x)g(x)-f(x)g'(x)"), sup(mr('[g(x)]'), mr('2')))))], kind='hint'))
P.append(shaded_box([('t', '鏈式法則（複合函數）：若 y=f(u)，u=g(x)，則 '),
                      ('m', omath(sub(mr("y'"), mr('x')), mr(' = '), sub(mr("y'"), mr('u')), mr(' · '), sub(mr("u'"), mr('x'))))],
                     kind='hint'))
P.append(blank())

P.append(heading('三、範例：用乘法法則求 y = x²eˣ 的導數'))
P.append(shaded_box([('t', '跟著這四個固定步驟，之後每一題都用同一套框架，不用重新想。這套框架接下來會用在《練習》的每一題上。')], kind='worked'))
P.append(worked_example_table([
    span_row('拆解：{f(x)=x^2}，{g(x)=e^x}', '① 辨識哪兩個函數相乘'),
    span_row('分別求導：{f\'(x)=2x}，{g\'(x)=e^x}', '② 各自套用公式卡'),
    eq_row('{y\'}', '{f\'(x)g(x)+f(x)g\'(x)}', '③ 套用乘法法則'),
    eq_row('{y\'}', '{2x*e^x+x^2*e^x}', '　代入'),
    answer_row('{y\'=(x^2+2x)e^x}', '④ 化簡：提出公因式 eˣ'),
], why_pct=0.36))
P.append(blank())

P.append(shaded_box([('t', '接下來請拿《基本初等函數的導數與運算法則——課堂練習》，依這套框架完成練習A、B、C。')], kind='worked'))

P += teacher_notes(
    main_design='D2 手順卡',
    aux_designs=('D5 圖文雙軌',),
    reason='S2 多步驟程序運算：六條公式＋四條法則要在序列步驟中不漏用、不用錯，'
           '本課以《工具卡_導數運算與判定手順卡》的「求導四步卡」落地；'
           'D5 圖文雙軌留給本主題另外兩課（單調性、凹凸性）真正有圖形對象時使用。',
    density='抽離小班（Tier 2）',
    fading='工具卡完整版（放桌面）→ 只留步驟數量提示（「呢題要做四步」）→ 移除',
    iep_codes=('a3 提示題目重點（公式卡＋手順卡）', 'a6 增加行距（書寫空間已加寬）'),
)

out = build_docx(
    P,
    os.path.join(OUT, '講義_基本初等函數的導數與運算法則_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
