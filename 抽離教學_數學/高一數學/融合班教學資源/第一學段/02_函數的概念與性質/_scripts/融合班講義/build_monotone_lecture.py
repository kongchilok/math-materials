# -*- coding: utf-8 -*-
"""講義_單調性與奇偶性_高一數學.docx"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

HERE = os.path.dirname(os.path.abspath(__file__))
SVGDIR = os.path.join(HERE, 'svgs_monotone')
D1 = os.path.join(SVGDIR, 'diagram1_monotone_intro.png')
D2 = os.path.join(SVGDIR, 'diagram2_parity_intro.png')

P = []
P.append(masthead('高一數學', '單調性與奇偶性', '課堂講義'))
P.append(student_info_row())

# ---------------- 一、單調性 ----------------
P.append(heading('一、單調性'))
P.append(para('觀察下面的圖象：從左到右看，如果曲線一直往下滑，x越大y越小，這一段就是「遞減」；'
              '如果曲線一直往上爬，x越大y越大，這一段就是「遞增」。曲線的最低點，就是這個函數的最小值。'))
P.append(image_para(D1, width_cm=8, caption='圖1：先遞減後遞增的函數圖象'))

P.append(para('把這個直觀說法寫成嚴謹的代數定義：'))
P.append(shaded_box('設函數f(x)的定義域為D，區間I⊆D。如果對區間I內任意{x_1},{x_2}，'
                     '當{x_1<x_2}時都有{f(x_1)<f(x_2)}，那麼稱f(x)在I上單調遞增；'
                     '如果都有{f(x_1)>f(x_2)}，那麼稱f(x)在I上單調遞減。'))
P.append(shaded_box('整個定義域上都遞增／都遞減，就分別叫做增函數／減函數，I叫做這個函數的單調區間。'))

P.append(heading('範例：證明一次函數的單調性', sz=BODY_SZ))
P.append(para('證明：函數 {f(x)=2x+1} 在R上是增函數。'))
P.append(problem_box([
    para('①取值：設 {x_1},{x_2} 為R內任意兩個實數，且 {x_1<x_2}。'),
    para('②作差：{f(x_1)-f(x_2)=(2x_1+1)-(2x_2+1)=2x_1-2x_2}'),
    para('③變形：{f(x_1)-f(x_2)=2(x_1-x_2)}'),
    para('④定號：因為 {x_1<x_2}，所以 {x_1-x_2<0}，於是 {2(x_1-x_2)<0}，即 {f(x_1)-f(x_2)<0}。'),
    para('⑤結論：所以 {f(x_1)<f(x_2)}，即 f(x) 在R上為增函數。'),
], trailing_blank=True))
P.append(shaded_box('這五個步驟「①取值 ②作差 ③變形 ④定號 ⑤結論」是證明單調性的標準格式，'
                     '之後每一題證明單調性都照這個框架寫，不用另外想寫法。'))

# ---------------- 二、奇偶性 ----------------
P.append(heading('二、奇偶性'))
P.append(para('如果一個函數的圖象以y軸為對稱軸（把圖象向左向右對摺會重合），就稱它為偶函數；'
              '如果圖象以原點為對稱中心（把圖象繞原點旋轉180°會重合），就稱它為奇函數。'))
P.append(image_para(D2, width_cm=13, caption='圖2：偶函數（y軸對稱，左）與奇函數（原點對稱，右）'))

P.append(shaded_box('偶函數：設f(x)的定義域為D。若對任意x∈D都有-x∈D，且 {f(-x)=f(x)} 恆成立，則稱f(x)為偶函數。'))
P.append(shaded_box('奇函數：若對任意x∈D都有-x∈D，且 {f(-x)=-f(x)} 恆成立，則稱f(x)為奇函數。'))
P.append(shaded_box('判斷前要先檢查定義域是否關於原點對稱——不對稱就直接判斷為非奇非偶函數。'))

P.append(heading('範例：判斷函數的奇偶性', sz=BODY_SZ))
P.append(para('判斷函數 {f(x)=x+frac(1,x)} 的奇偶性。'))
P.append(problem_box([
    para('①求定義域：{f(x)=x+frac(1,x)} 要求 {x!=0}，所以定義域是所有不等於0的實數。'),
    para('②驗證對稱：定義域關於原點對稱（x≠0時，-x也滿足-x≠0），可以繼續判斷。'),
    para('③代入f(-x)：{f(-x)=-x+frac(1,-x)=-x-frac(1,x)}'),
    para('④比對：{f(-x)=-(x+frac(1,x))=-f(x)}'),
    para('⑤結論：所以 f(x) 是奇函數。'),
], trailing_blank=True))
P.append(shaded_box('判斷奇偶性的標準格式：①求定義域 ②驗證定義域關於原點對稱 ③代入f(-x)計算 '
                     '④跟f(x)、-f(x)比對 ⑤下結論（偶函數／奇函數／非奇非偶函數）。'))

P.append(para('接下來請拿《單調性與奇偶性 課堂練習》，依這套框架完成練習A、B、C。'))

out = build_docx(P, os.path.join(HERE, '講義_單調性與奇偶性_高一數學.docx'),
                  footer_text='高一數學．單調性與奇偶性')
print('OK', out)
