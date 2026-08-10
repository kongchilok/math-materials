# -*- coding: utf-8 -*-
# 練習（練習A/B/C＋教師用答案）—— 基本初等函數的導數與運算法則
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

P = []

P.append(masthead('高三數學', '基本初等函數的導數與運算法則', '課堂練習'))
P.append(student_info_row())
P.append(shaded_box([('t', '請先讀《基本初等函數的導數與運算法則——課堂講義》的「範例」，練習B會用到同一套四步驟框架。')], kind='hint'))

# 練習A（初階）
P.append(heading(f'一、練習A（{star_label(1)}）—— 直接套公式（選擇題，3選項）'))
P.append(problem_box([
    para([('t', '1．'), ('m', omath(mr('f(x)='), sup(mr('x'), mr('3')))), ('t', ' 的導數為（　　）')]),
    para([('t', 'A．'), ('m', omath(mr('3'), sup(mr('x'), mr('2'))))]),
    para([('t', 'B．'), ('m', omath(sup(mr('x'), mr('2'))))]),
    para([('t', 'C．'), ('m', omath(mr('3x')))]),
] + write_lines(2)))
P.append(problem_box([
    para([('t', '2．'), ('m', omath(mr('f(x)='), sup(mr('e'), mr('x')))), ('t', ' 的導數為（　　）')]),
    para([('t', 'A．'), ('m', omath(sup(mr('e'), mr('x'))))]),
    para([('t', 'B．'), ('m', omath(mr('x'), sup(mr('e'), mr('x-1'))))]),
    para([('t', 'C．'), ('m', omath(mr('1')))]),
] + write_lines(2)))
P.append(problem_box([
    para([('t', '3．已知 f(x) = ln x，求 '), ('m', omath(mr("f'(x)=")))]),
] + write_lines(2)))
P.append(problem_box([
    para([('t', '4．已知 f(x) = sin x，求 '), ('m', omath(mr("f'(x)=")))]),
] + write_lines(2)))

# 練習B（中階）
P.append(heading(f'二、練習B（{star_label(2)}）—— 和差、乘除法則（依「講義」範例的四步驟框架作答）'))
P.append(problem_box([
    para([('t', '5．求 '), ('m', omath(mr('f(x)='), sup(mr('x'), mr('2')), mr('+'), sup(mr('x'), mr('3')), mr('+x'))), ('t', ' 的導數。')]),
] + write_lines(5)))
P.append(problem_box([
    para([('t', '6．求 '), ('m', omath(mr('y=ln x·'), sup(mr('e'), mr('x')))), ('t', ' 的導數。')]),
] + write_lines(5)))
P.append(problem_box([
    para([('t', '7．求 '), ('m', omath(mr('y='), frac(sup(mr('x'), mr('2')) + mr('+1'), mr('x')))), ('t', ' 的導數。')]),
] + write_lines(5)))

# 練習C（高階）
P.append(heading(f'三、練習C（{star_label(3)}）—— 鏈式法則與切線方程'))
P.append(problem_box([
    para([('t', '8．求 '), ('m', omath(sup(mr('(3x+5)'), mr('3')))), ('t', ' 的導數。')]),
] + write_lines(4)))
P.append(problem_box([
    para([('t', '9．求 y = ln(2x−1) 的導數。')]),
] + write_lines(4)))
P.append(problem_box([
    para([('t', '10．求曲線 '), ('m', omath(mr('y='), sup(mr('x'), mr('2')), mr('+'), frac(mr('3'), mr('x')))),
          ('t', ' 在點 (1，4) 的切線方程。')]),
] + write_lines(4)))

P.append(pagebreak())
P.append(heading('教師用：參考答案'))
P.append(para([('t', '1．A（3x²）　2．A（eˣ）　3．f\'(x)=1/x　4．f\'(x)=cos x')]))
P.append(para([('t', '5．f\'(x)=2x+3x²+1')]))
P.append(para([('t', '6．y\'=eˣ(1/x + ln x)　【乘法法則：(ln x)\'·eˣ + ln x·(eˣ)\' = (1/x)eˣ + ln x·eˣ】')]))
P.append(para([('t', '7．y\'=1−1/x²　【除法法則：[2x·x−(x²+1)·1]/x² = (x²−1)/x²】')]))
P.append(para([('t', '8．y\'=9(3x+5)²　【令 u=3x+5，y=u³，y\'=3u²·3】')]))
P.append(para([('t', '9．y\'=2/(2x−1)　【令 u=2x−1，y=ln u，y\'=(1/u)·2】')]))
P.append(para([('t', '10．y\'=2x−3/x²，於 x=1 斜率=2−3=−1；切線方程：y=−x+5')]))

out = build_docx(
    P,
    r'C:\Users\KongChiLok\notebookLM\inclusive-derivative-intro_高三數學\練習_基本初等函數的導數與運算法則_抽離小班共用版.docx',
    footer_text='高三數學．導數運算法則單元',
)
print(out)
