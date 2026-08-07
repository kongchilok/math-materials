# -*- coding: utf-8 -*-
"""練習_單調性與奇偶性_高一數學.docx"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

HERE = os.path.dirname(os.path.abspath(__file__))
SVGDIR = os.path.join(HERE, 'svgs_monotone')
D3 = os.path.join(SVGDIR, 'diagram3_practiceA_graph.png')

P = []
P.append(masthead('高一數學', '單調性與奇偶性', '課堂練習'))
P.append(student_info_row())
P.append(para('先回頭看《單調性與奇偶性 課堂講義》的兩個範例，再嘗試以下練習。'))

# ==================== 練習A ====================
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(problem_box([
    para('1．右圖是函數 y=f(x) 的圖象，觀察圖象後完成下列填空：'),
]))
P.append(image_para(D3, width_cm=8))
P.append(problem_box([
    para('(a) 函數在區間 ___________ 上單調遞減；'),
] + write_lines(2) + [
    para('(b) 函數在區間 ___________ 上單調遞增；'),
] + write_lines(2) + [
    para('(c) 函數的最小值是 _______，在 x = _______ 時取得。'
         '（單選：A. −3　B. 0　C. 3）'),
] + write_lines(2)))
P.append(shaded_box('提示：y隨x增大而變小 → 遞減；y隨x增大而變大 → 遞增；圖象最低點的y坐標就是最小值。'))

P.append(problem_box([
    para('2．根據奇偶函數的定義，完成下列填空：'),
    para('(a) 已知函數f(x)為奇函數，且f(2025)=6，則f(−2025) = ___________。'),
] + write_lines(2) + [
    para('(b) 已知函數g(x)為偶函數，且g(−8)=11，則g(8) = ___________。'),
] + write_lines(2)))
P.append(shaded_box('提示：奇函數 {f(-x)=-f(x)}（圖象繞原點轉180°會重合）；'
                     '偶函數 {g(-x)=g(x)}（圖象以y軸為對稱軸）。'))

P.append(problem_box([
    para('3．如果函數y=f(x)的圖象關於y軸對稱，這個函數是：（單選）'),
    para('（A）奇函數　　（B）偶函數　　（C）非奇非偶函數'),
] + write_lines(2), trailing_blank=True))
P.append(shaded_box('提示：偶函數的圖象特徵就是「以y軸為對稱軸」——把圖象向左右對摺會完全重合。'))

# ==================== 練習B ====================
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(problem_box([
    para('1．已知一次函數 {y=(k-1)x+b} 在R上是增函數，求k的取值範圍。'),
] + write_lines(2)))
P.append(shaded_box('提示：一次函數y=mx+c，係數m>0時遞增、m<0時遞減（見講義範例的結論）。'))

P.append(problem_box([
    para('2．依「取值-作差-變形-定號-結論」的格式，證明函數 {f(x)=-2x+5} 在R上為減函數。'
         '請把下面的證明補寫完整：'),
    para('①取值：設 {x_1},{x_2}∈R，且 {x_1<x_2}。'),
    para('②作差：{f(x_1)-f(x_2)} = ___________________________'),
] + write_lines(2) + [
    para('③變形：= ___________________________'),
] + write_lines(2) + [
    para('④定號：因為 {x_1<x_2}，所以 {x_1-x_2} ___ 0（填 > 或 <），於是 {f(x_1)-f(x_2)} ___ 0（填 > 或 <）。'),
] + write_lines(2) + [
    para('⑤結論：所以 f(x₁) ___ f(x₂)（填 > 或 <），即 f(x) 在R上為 ___________函數。'),
] + write_lines(2)))
P.append(shaded_box('提示卡（五步驟）：①取值 ②作差 ③變形（提出公因數）④定號（判斷正負）'
                     '⑤結論（對照定義寫出遞增或遞減）。'))

P.append(problem_box([
    para('3．判斷下列函數的奇偶性，每小題都要先求定義域，再代入f(−x)比較：'),
    para('(a) {f(x)=x^6-2x^2+1}'),
] + write_lines(3) + [
    para('(b) {f(x)=x^3-x}'),
] + write_lines(3) + [
    para('(c) {f(x)=x^2+x}'),
] + write_lines(3), trailing_blank=True))
P.append(shaded_box('提示：定義域 → 代入f(−x) → 比較：等於f(x)是偶函數；等於−f(x)是奇函數；'
                     '兩者都不等於就是非奇非偶函數。'))

# ==================== 練習C ====================
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(problem_box([
    para('1．證明函數 {y=x+frac(4,x)} 在 (2,+∞) 上單調遞增。（仿講義範例的五步驟格式作答，注意分式要通分）'),
] + write_lines(5)))
P.append(shaded_box('提示卡（五步驟）：①取值 ②作差 ③變形（通分、提公因式）④定號（留意 x₁x₂>4）⑤結論。'))

P.append(problem_box([
    para('2．已知二次函數 {f(x)=x^2-mx+m-1}，且 {f(0)=f(2)}。'),
    para('(a) 求m的值。'),
] + write_lines(2) + [
    para('(b) 求f(x)在區間 [−2,2] 上的最小值。'),
] + write_lines(3)))
P.append(shaded_box('提示：{f(0)=f(2)} 代表拋物線的對稱軸在x=1；配方後找出頂點，'
                     '再判斷頂點是否落在[−2,2]這個區間內。'))

P.append(problem_box([
    para('3．已知函數f(x)是偶函數，且在 [0,+∞) 上單調遞增。比較 f(−3) 與 f(2) 的大小，並說明理由。'),
] + write_lines(4), trailing_blank=False))
P.append(shaded_box('提示：先用偶函數的性質把f(−3)換成f(3)，再比較3和2誰更靠右——'
                     '在[0,+∞)遞增時，自變量越大函數值越大。', ))

# ==================== 參考答案 ====================
P.append(heading('參考答案與解析', page_break_before=True))

P.append(heading('練習A', sz=BODY_SZ))
P.append(problem_box([
    para('1．(a) 遞減區間為 [−3,0]；(b) 遞增區間為 [0,4]；(c) 最小值為 −3（選A），在x=0時取得（圖象上的點(0,−3)為最低點）。'),
    para('2．(a) f(−2025) = −f(2025) = −6。(b) g(8) = g(−8) = 11。'),
    para('3．（B）偶函數——圖象以y軸為對稱軸正是偶函數的定義特徵。'),
]))

P.append(heading('練習B', sz=BODY_SZ))
P.append(problem_box([
    para('1．一次函數遞增 ⟺ 一次項係數 > 0，所以 {k-1>0}，即 {k>1}。'),
]))
P.append(problem_box([
    para('2．①取值：設 {x_1},{x_2}∈R，且 {x_1<x_2}。'),
    para('②作差：{f(x_1)-f(x_2)=(-2x_1+5)-(-2x_2+5)=-2x_1+2x_2}'),
    para('③變形：{f(x_1)-f(x_2)=-2(x_1-x_2)}'),
    para('④定號：因為 {x_1<x_2}，所以 {x_1-x_2<0}，於是 {-2(x_1-x_2)>0}，即 {f(x_1)-f(x_2)>0}。'),
    para('⑤結論：所以 {f(x_1)>f(x_2)}，即 f(x) 在R上為減函數。'),
]))
P.append(problem_box([
    para('3．(a) 定義域為R。{f(-x)=x^6-2x^2+1=f(x)}，是偶函數。'),
    para('(b) 定義域為R。{f(-x)=-x^3+x=-f(x)}，是奇函數。'),
    para('(c) 定義域為R。{f(-x)=x^2-x}，既不等於 {f(x)=x^2+x}，也不等於 {-f(x)=-x^2-x}，是非奇非偶函數。'),
]))

P.append(heading('練習C', sz=BODY_SZ))
P.append(problem_box([
    para('1．①取值：設 {x_1},{x_2}∈(2,+∞)，且 {x_1<x_2}。'),
    para('②作差：{y_1-y_2=(x_1-x_2)+(frac(4,x_1)-frac(4,x_2))}'),
    para('③變形：{y_1-y_2=(x_1-x_2)+frac(4(x_2-x_1),x_1x_2)=(x_1-x_2)(1-frac(4,x_1x_2))=frac((x_1-x_2)(x_1x_2-4),x_1x_2)}'),
    para('④定號：{x_1,x_2>2} 所以 {x_1x_2>4}，即 {x_1x_2-4>0}；又 {x_1x_2>0}，{x_1-x_2<0}，'
         '三者相乘（負×正÷正）得 {y_1-y_2<0}。'),
    para('⑤結論：所以 {y_1<y_2}，即函數在(2,+∞)上單調遞增。'),
]))
P.append(problem_box([
    para('2．(a) {f(0)=m-1}，{f(2)=4-2m+m-1=3-m}。由 {f(0)=f(2)}：{m-1=3-m}，解得 {m=2}。'),
    para('(b) 代入m=2：{f(x)=x^2-2x+1=(x-1)^2}，對稱軸x=1，且1∈[−2,2]，開口向上，'
         '所以最小值在x=1處取得：{f(1)=0}，最小值為0。'),
]))
P.append(problem_box([
    para('3．f是偶函數，所以 {f(-3)=f(3)}。又f在[0,+∞)上遞增，且 {3>2}，所以 {f(3)>f(2)}。'
         '因此 {f(-3)>f(2)}。'),
], trailing_blank=False))

out = build_docx(P, os.path.join(HERE, '練習_單調性與奇偶性_高一數學.docx'),
                  footer_text='高一數學．單調性與奇偶性')
print('OK', out)
