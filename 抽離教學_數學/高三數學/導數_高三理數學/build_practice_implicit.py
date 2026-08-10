# -*- coding: utf-8 -*-
# 練習（練習A/B/C＋教師用答案）—— 隱函數求導
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '隱函數求導'
FOOTER = '高三數學．導數補充單元'

Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(shaded_box('請先讀《隱函數求導——課堂講義》的「範例」，練習B會用到同一套四步驟框架。'))
Q.append(blank())

Q.append(heading(f'一、練習A（{star_label(1)}）—— y 項求導（選擇題，3選項，先練呢個基本功再做完整隱函數求導）'))
Q.append(problem_box([
    para('1．{y^3} 對 x 求導＝（　　）'),
    para('　　A．{3y^2}　　B．{3y^2*y\'}　　C．{y^2}'),
] + write_lines(2)))
Q.append(problem_box([
    para('2．{5y} 對 x 求導＝（　　）'),
    para('　　A．{5}　　B．{5y\'}　　C．{5y}'),
] + write_lines(2)))

Q.append(heading(f'二、練習B（{star_label(2)}）—— 求隱函數的 y\'（依「講義」範例的四步驟框架作答）'))
Q.append(problem_box([para('3．求 {x^2+y^2=9} 的 {y\'}。')] + write_lines(6)))
Q.append(problem_box([para('4．求 {x^2-4y^2=16} 的 {y\'}。')] + write_lines(6)))

Q.append(heading(f'三、練習C（{star_label(3)}）—— 混合項／應用'))
Q.append(problem_box([
    para('5．求 {xy+y^2=4} 的 {y\'}。（提示：{xy} 要用乘法法則——兩個都係變量）'),
] + write_lines(6)))
Q.append(problem_box([
    para('6．求圓 {x^2+y^2=25} 在點 {(3,4)} 嘅切線方程。（先用隱函數求導求斜率，再用點斜式）'),
] + write_lines(6), trailing_blank=False))

Q.append(pagebreak())
Q.append(heading('教師用：參考答案'))
Q.append(para('1．B（{y^3} 求導要多乘 {y\'}）　　2．B（{5y} 求導要多乘 {y\'}）'))
Q.append(para('3．{2x+2y*y\'=0} → {y\'=-frac(2x,2y)=-frac(x,y)}'))
Q.append(para('4．{2x-8y*y\'=0} → {y\'=frac(2x,8y)=frac(x,4y)}'))
Q.append(para('5．{xy} 用乘法法則求導得 {y+x*y\'}；{y^2} 求導得 {2y*y\'}。合埋：{y+x*y\'+2y*y\'=0} → {y\'(x+2y)=-y} → {y\'=-frac(y,x+2y)}'))
Q.append(para('6．由 {x^2+y^2=25}：{2x+2y*y\'=0} → {y\'=-frac(x,y)}；喺 {(3,4)}：{y\'=-frac(3,4)}。'))
Q.append(para('　點斜式：{y-4=-frac(3,4)(x-3)}，化簡得 {3x+4y=25}。（驗算：{3*3+4*4=9+16=25} 確在圓上）'))

out = build_docx(
    Q,
    os.path.join(OUT, '練習_隱函數求導_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
