# -*- coding: utf-8 -*-
# 練習（練習A/B/C＋教師用答案）—— 基本初等函數的導數與運算法則
# 2026-08-12：從舊資料夾 inclusive-derivative-intro_高三數學 搬入本資料夾，
# 順道改用 {} 標記語法統一風格（原為手寫 omath()），並修正輸出路徑（原本誤指
# 向已停用的舊碟舊資料夾 C:\Users\KongChiLok\notebookLM\...，改寫回本檔所在資料夾）。
# 內容與答案數值完全不變。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '基本初等函數的導數與運算法則'
FOOTER = '高三數學．導數運算法則單元'

P = []

P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(shaded_box('請先讀《基本初等函數的導數與運算法則——課堂講義》的「範例」，練習B會用到同一套四步驟框架。'))
P.append(blank())

# 練習A（初階）
P.append(heading(f'一、練習A（{star_label(1)}）—— 直接套公式（選擇題，3選項）'))
P.append(problem_box([
    para('1．{f(x)=x^3} 的導數為（　　）'),
    para('　　A．{3x^2}　　B．{x^2}　　C．{3x}'),
] + write_lines(2)))
P.append(problem_box([
    para('2．{f(x)=e^x} 的導數為（　　）'),
    para('　　A．{e^x}　　B．{x*e^{x-1}}　　C．{1}'),
] + write_lines(2)))
P.append(problem_box([
    para('3．已知 {f(x)=fn(ln) x}，求 {f\'(x)=}'),
] + write_lines(2)))
P.append(problem_box([
    para('4．已知 {f(x)=fn(sin) x}，求 {f\'(x)=}'),
] + write_lines(2)))

# 練習B（中階）
P.append(heading(f'二、練習B（{star_label(2)}）—— 和差、乘除法則（依「講義」範例的四步驟框架作答）'))
P.append(problem_box([
    para('5．求 {f(x)=x^2+x^3+x} 的導數。'),
] + write_lines(5)))
P.append(problem_box([
    para('6．求 {y=fn(ln) x*e^x} 的導數。'),
] + write_lines(5)))
P.append(problem_box([
    para('7．求 {y=frac(x^2+1,x)} 的導數。'),
] + write_lines(5)))

# 練習C（高階）
P.append(heading(f'三、練習C（{star_label(3)}）—— 鏈式法則與切線方程'))
P.append(problem_box([
    para('8．求 {(3x+5)^3} 的導數。'),
] + write_lines(4)))
P.append(problem_box([
    para('9．求 {y=fn(ln)(2x-1)} 的導數。'),
] + write_lines(4)))
P.append(problem_box([
    para('10．求曲線 {y=x^2+frac(3,x)} 在點 (1，4) 的切線方程。'),
] + write_lines(4), trailing_blank=False))

P.append(pagebreak())
P.append(heading('教師用：參考答案'))
P.append(para('1．A（{3x^2}）　2．A（{e^x}）　3．{f\'(x)=1/x}　4．{f\'(x)=fn(cos) x}'))
P.append(para('5．{f\'(x)=2x+3x^2+1}'))
P.append(para('6．{y\'=e^x*(1/x+fn(ln) x)}　【乘法法則：{(fn(ln) x)\'*e^x+fn(ln) x*(e^x)\'=frac(1,x)*e^x+fn(ln) x*e^x}】'))
P.append(para('7．{y\'=1-1/x^2}　【除法法則：{frac(2x*x-(x^2+1)*1,x^2)=frac(x^2-1,x^2)}】'))
P.append(para('8．{y\'=9(3x+5)^2}　【令 {u=3x+5}，{y=u^3}，{y\'=3u^2*3}】'))
P.append(para('9．{y\'=frac(2,2x-1)}　【令 {u=2x-1}，{y=fn(ln) u}，{y\'=frac(1,u)*2}】'))
P.append(para('10．{y\'=2x-3/x^2}，於 {x=1} 斜率 {=2-3=-1}；切線方程：{y=-x+5}'))

out = build_docx(
    P,
    os.path.join(OUT, '練習_基本初等函數的導數與運算法則_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
