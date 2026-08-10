# -*- coding: utf-8 -*-
# 練習（練習A/B/C＋教師用答案）—— 二階導數與函數的凹凸性、拐點
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT, UNIT = '高三數學', '二階導數與函數的凹凸性、拐點'
FOOTER = '高三數學．導數補充單元'

Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(shaded_box('請先讀《二階導數與函數的凹凸性、拐點——課堂講義》的「範例」，練習B會用到同一套四步驟框架。'))
Q.append(blank())

Q.append(heading(f'一、練習A（{star_label(1)}）—— 求二階導數（選擇題，3選項）'))
Q.append(problem_box([
    para('1．{f(x)=x^3}，{f\'\'(x)}＝（　　）'),
    para('　　A．{3x^2}　　B．{6x}　　C．{6}'),
] + write_lines(2)))
Q.append(problem_box([
    para('2．{f(x)=2x^2-5x+1}，{f\'\'(x)}＝（　　）'),
    para('　　A．{4x-5}　　B．{4}　　C．{2}'),
] + write_lines(2)))

Q.append(heading(f'二、練習B（{star_label(2)}）—— 求凹凸區間與拐點（依「講義」範例的四步驟框架作答）'))
Q.append(problem_box([
    para('3．求 {f(x)=x^3-6x^2} 的凹凸區間與拐點。'),
] + write_lines(6)))
Q.append(problem_box([
    para('4．求 {f(x)=-x^3+3x} 的凹凸區間與拐點。'),
] + write_lines(6)))

Q.append(heading(f'三、練習C（{star_label(3)}）—— 較多轉折 ／概念判斷'))
Q.append(problem_box([
    para('5．求 {f(x)=x^4-4x^3} 的凹凸區間與拐點。（提示：{f\'\'(x)=0} 可能唔止一個根，記得逐段檢查正負）'),
] + write_lines(7)))
Q.append(problem_box([
    para('6．判斷對錯，並舉例說明：「只要 {f\'\'(x_0)=0}，{(x_0,f(x_0))} 就一定是拐點。」'),
    shaded_box('提示：試吓 {f(x)=x^4} 喺 {x=0} 嗰點——先求 {f\'\'(x)}，再睇下佢喺 0 左右係咪真係變號。'),
] + write_lines(4), trailing_blank=False))

Q.append(pagebreak())
Q.append(heading('教師用：參考答案'))
Q.append(para('1．B（{f\'(x)=3x^2}，{f\'\'(x)=6x}）　　2．B（{f\'(x)=4x-5}，{f\'\'(x)=4}）'))
Q.append(para('3．{f\'(x)=3x^2-12x}，{f\'\'(x)=6x-12=0→x=2}。{x<2}（如{x=0}）：{f\'\'(0)=-12<0}凸；{x>2}（如{x=3}）：{f\'\'(3)=6>0}凹。左右變號，拐點為 {(2,f(2))=(2,-16)}。'))
Q.append(para('4．{f\'(x)=-3x^2+3}，{f\'\'(x)=-6x=0→x=0}。{x<0}（如{x=-1}）：{f\'\'(-1)=6>0}凹；{x>0}（如{x=1}）：{f\'\'(1)=-6<0}凸。左右變號，拐點為 {(0,f(0))=(0,0)}。'))
Q.append(para('5．{f\'(x)=4x^3-12x^2}，{f\'\'(x)=12x^2-24x=12x(x-2)=0→x=0} 或 {x=2}。{x<0}（如{x=-1}）：{f\'\'(-1)=36>0}凹；{0<x<2}（如{x=1}）：{f\'\'(1)=-12<0}凸；{x>2}（如{x=3}）：{f\'\'(3)=36>0}凹。兩處都變號，共兩個拐點：{(0,0)} 與 {(2,-16)}。'))
Q.append(para('6．錯。反例：{f(x)=x^4}，{f\'(x)=4x^3}，{f\'\'(x)=12x^2}，{f\'\'(0)=0}，但 {f\'\'(x)=12x^2} 喺 {x=0} 左右都是 {>=0}（0附近兩側都是凹，冇變號），所以 {x=0} 唔係拐點——{f\'\'(x_0)=0} 只是拐點的「必要條件」，仲要檢查正負係咪真係變咗先算。'))

out = build_docx(
    Q,
    os.path.join(OUT, '練習_二階導數與函數的凹凸性拐點_抽離小班共用版.docx'),
    footer_text=FOOTER,
)
print(out)
