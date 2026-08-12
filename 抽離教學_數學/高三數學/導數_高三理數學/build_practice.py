# -*- coding: utf-8 -*-
# 練習（練習A/B/C + 答案）—— 從原本的共用版拆出，對應同單元的《講義》使用同一套house style
# 2026-08-12：練習C加「切線方程」子項（改編自舊《功課_導數的概念及其意義(變化率問題)》
# 類型三第8、9題，對應教案 2026/09/08「求切線方程」堂），原第9題（水平切線特例）續留
# 在切線方程子項最後；情境應用（火箭）、線性估計題號順延。同時修正輸出路徑（原本誤指
# 向已停用的舊資料夾 inclusive-derivative-intro_高三數學，改寫回本檔所在資料夾）。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))

P = []

P.append(masthead('高三數學', '導數的概念及其意義', '課堂練習'))
P.append(student_info_row())
P.append(shaded_box([('t', '請先讀《導數的概念及其意義——課堂講義》的「範例」，練習B會用到同一套四步驟框架。')], kind='hint'))
P.append(blank())

P.append(heading(f'一、練習A（{star_label(1)}）—— 平均變化率（選擇題，3選項）'))
P.append(problem_box([
    para([('t', '1．函數 '), ('m', omath(mr('y='), sqrt(mr('x')))), ('t', ' 在區間 [1, 4] 上的平均變化率為（　　）')]),
    para([('t', '　　A．1/3　　B．3/5　　C．5/3')], ind=300),
] + write_lines(2)))
P.append(problem_box([
    para([('t', '2．函數 '), ('m', omath(mr('f(x)='), sup(mr('x'), mr('2')), mr('-x'))), ('t', ' 在區間 [1, 3] 上的平均變化率為（　　）')]),
    para([('t', '　　A．6　　B．3　　C．2')], ind=300),
] + write_lines(2)))
P.append(blank())

P.append(heading(f'二、練習B（{star_label(2)}）—— 用定義求導數（依「講義」範例的四步驟框架作答）'))
for n, expr in [
    ('3．', omath(mr('y=3x+4'))),
    ('4．', omath(mr('f(x)='), frac(mr('1'), mr('x')))),
    ('5．', omath(mr('f(x)='), sqrt(mr('x')))),
    ('6．', omath(mr('y='), sup(mr('x'), mr('3')))),
]:
    P.append(problem_box([
        para([('t', n), ('t', '求 '), ('m', expr), ('t', ' 的導數。')]),
    ] + write_lines(5)))

P.append(heading(f'三、練習C（{star_label(3)}）—— 切線方程與情境應用'))
P.append(shaded_box([('t', '（切線方程）先求導數、代入求斜率，再代入點斜式——同「講義」範例的三步驟一樣。')], kind='hint'))
P.append(problem_box([
    para([('t', '7．已知曲線 C：'), ('m', omath(mr('f(x)='), sup(mr('x'), mr('2')), mr('-2x+3'))), ('t', '。')]),
    para([('t', '　(1) 求 '), ('m', omath(mr("f'(2)"))), ('t', ' 的值；')]),
    para([('t', '　(2) 求曲線 C 在點 '), ('m', omath(mr('P(2,f(2))'))), ('t', ' 處的切線方程。')]),
] + write_lines(4)))
P.append(problem_box([
    para([('t', '8．求拋物線 '), ('m', omath(mr('f(x)='), sup(mr('x'), mr('2')), mr('-3'))), ('t', ' 在點 (2, 1) 處的切線斜率與切線方程。')]),
] + write_lines(4)))
P.append(problem_box([
    para([('t', '9．求拋物線 '), ('m', omath(mr('f(x)='), sup(mr('x'), mr('2')), mr('+1'))), ('t', ' 在點 (0, 1) 的切線斜率與切線方程。')]),
] + write_lines(4)))
P.append(blank())

P.append(shaded_box([
    ('t', '（情境應用）火箭發射 t 秒後，高度 '), ('m', omath(mr('h(t)=0.9'), sup(mr('t'), mr('2')))), ('t', '（單位：m）。'),
], kind='hint'))
P.append(problem_box([para([('t', '10．求 1≤t≤2 這段時間，火箭爬高的平均速度。')])] + write_lines(3)))
P.append(problem_box([para([('t', '11．求發射後第 10 秒時，火箭爬高的瞬時速度。')])] + write_lines(3)))
P.append(problem_box([
    para('12．已知 {f(x)=sqrt(x)}，{f(4)=2}，{f\'(4)=frac(1,4)}。利用線性估計公式 {f(x_0+Δx)≈f(x_0)+f\'(x_0)*Δx} 估計 {sqrt(4.1)} 的近似值。'),
] + write_lines(3), trailing_blank=False))

P.append(pagebreak())
P.append(heading('教師用：參考答案'))
answers = [
    '1．A（1/3）　2．B（3）',
    "3．y′=3　4．f′(x)=-1/x²　5．f′(x)=1/(2√x)　6．y′=3x²",
    "7．f′(x)=2x-2；(1) f′(2)=2；(2) f(2)=3，切線方程：y=2x-1",
    "8．f′(x)=2x，k=f′(2)=4；切線方程：y=4x-7",
    '9．f′(x)=2x，於 x=0 斜率=0；切線方程：y=1（水平切線，(0,1) 恰為拋物線頂點）',
    '10．平均速度 = [h(2)-h(1)]/1 = 2.7 m/s',
    '11．瞬時速度 v(t)=h′(t)=1.8t，v(10)=18 m/s',
    '12．√4.1 ≈ 2+(1/4)×0.1 = 2.025（實際值約 2.0248）',
]
for a in answers:
    P.append(para([('t', a)], sz=22))

out = build_docx(
    P,
    os.path.join(OUT, '練習_導數的概念及其意義_抽離小班共用版.docx'),
    footer_text='高三數學．導數單元',
)
print(out)
