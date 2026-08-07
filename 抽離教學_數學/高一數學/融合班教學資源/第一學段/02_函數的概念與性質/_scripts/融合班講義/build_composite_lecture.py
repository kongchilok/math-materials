# -*- coding: utf-8 -*-
"""講義_複合函數_高一數學.docx（課本無此節，補充教材，自行設計）"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

HERE = os.path.dirname(os.path.abspath(__file__))
DIAG = os.path.join(HERE, 'svgs_composite', 'machine_series.png')

P = []
P.append(masthead('高一數學', '複合函數（補充）', '課堂講義'))
P.append(student_info_row())

# ---------------- 一、什麼是複合函數 ----------------
P.append(heading('一、什麼是複合函數'))
P.append(para('把一個函數的輸出，當作另一個函數的輸入，接連運算兩次，就得到「複合函數」。'
              '可以想成兩台機器串在一起：'))
P.append(image_para(DIAG, width_cm=14, caption='圖：x 先經過 g 機器，再經過 f 機器'))
P.append(shaded_box('一般地，設 {y=f(u)}，而 {u=g(x)}，把 {u=g(x)} 代進去就得到 {y=f(g(x))}，'
                    '這個函數叫做由 f 和 g 複合而成的複合函數。其中 g 是內層、f 是外層，u 叫中間變量。'))
P.append(shaded_box('求 f(g(x)) 的解析式，方法只有一句話：把 f(x) 式子裡的每一個 x，'
                    '整個換成 g(x)。'))

P.append(heading('範例一：求複合函數的解析式', sz=BODY_SZ))
P.append(para('已知 {f(x)=x^2+3x+2}，{g(x)=x+1}，求 f(g(x)) 的解析式。'))
P.append(problem_box([
    para('①認內外層：內層 {g(x)=x+1}，外層 {f(x)=x^2+3x+2}。'),
    para('②代入：把 {f(x)} 裡的每個 x 換成 (x+1)，得 {f(g(x))=(x+1)^2+3(x+1)+2}。'),
    para('③展開：{(x+1)^2=x^2+2x+1}，{3(x+1)=3x+3}，合起來 {=x^2+2x+1+3x+3+2}。'),
    para('④整理：{f(g(x))=x^2+5x+6}。'),
], trailing_blank=True))

# ---------------- 二、兩件要小心的事 ----------------
P.append(heading('二、兩件要小心的事'))

P.append(para('（1）複合的順序會影響結果——f(g(x)) 通常不等於 g(f(x))。'))
P.append(heading('範例二：換個順序，答案不一樣', sz=BODY_SZ))
P.append(para('已知 {f(x)=2x}，{g(x)=x+3}。'))
P.append(problem_box([
    para('先 g 後 f：{f(g(x))=2(x+3)=2x+6}。'),
    para('先 f 後 g：{g(f(x))=2x+3}（把 g 裡的 x 換成 f(x)=2x）。'),
    para('兩者不同，所以做複合函數一定要先看清楚「誰在裡面、誰在外面」。'),
], trailing_blank=True))

P.append(para('（2）複合函數的定義域——x 要能讓內層 g(x) 算得出來，算出的 g(x) 還要落在外層 f 的定義域裡。'))
P.append(heading('範例三：帶定義域的複合函數', sz=BODY_SZ))
P.append(para('已知 {f(x)=sqrt(x)}，{g(x)=x-3}，求 f(g(x)) 的解析式與定義域。'))
P.append(problem_box([
    para('①解析式：{f(g(x))=sqrt(x-3)}。'),
    para('②定義域：根號裡要 {>=0}，即 {x-3>=0}，解得 {x>=3}。'),
    para('③結論：{f(g(x))=sqrt(x-3)}，定義域是 {x>=3}。'),
], trailing_blank=True))

P.append(para('接下來請拿《複合函數（補充）課堂練習》，依這套方法完成練習A、B、C。'))

out = build_docx(P, os.path.join(HERE, '講義_複合函數_高一數學.docx'),
                 footer_text='高一數學．複合函數（補充）')
print('lecture built')
