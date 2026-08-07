# -*- coding: utf-8 -*-
"""練習_冪函數的性質_高一數學.docx"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

HERE = os.path.dirname(os.path.abspath(__file__))

P = []
P.append(masthead('高一數學', '冪函數的性質', '課堂練習'))
P.append(student_info_row())
P.append(para('作答前先回頭看《冪函數的性質 課堂講義》的性質表與兩個範例，照同樣的步驟框架完成下面練習A、B、C。'))

# ---------------- 練習A ----------------
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(problem_box([
    para('1．下列哪一個是冪函數？（單選）'),
    para('（A）{y=2x^2}　（B）{y=x^4}　（C）{y=3^x}'),
    para('提示：冪函數的形式一定是 {y=x^α}，係數必須是 1、指數是常數；x 跑到指數上的是指數函數。'),
] + write_lines(2)))

P.append(problem_box([
    para('2．對照講義的性質表，填空：'),
    para('（1）{y=x^2} 的定義域是＿＿＿＿，值域是＿＿＿＿。'),
    para('（2）{y=x^3} 是＿＿＿函數（填「奇」或「偶」）。'),
    para('（3）五個常見冪函數的圖象都經過同一個點，這個點是＿＿＿＿。'),
] + write_lines(3)))

P.append(problem_box([
    para('3．求下列各式的值：'),
    para('（1）{9^{frac(1,2)}}＝＿＿　（2）{8^{frac(1,3)}}＝＿＿　（3）{4^{-1}}＝＿＿'),
    para('提示：{a^{frac(1,2)}=sqrt(a)}、{a^{frac(1,3)}=sqrt[3](a)}、{a^{-1}=frac(1,a)}。'),
] + write_lines(2)))

# ---------------- 練習B ----------------
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(problem_box([
    para('4．分數指數冪與根式的化簡（下面都假設 {a>0}）：'),
    para('（1）把 {sqrt[3](x^2)} 寫成分數指數冪。'),
    para('（2）求 {16^{frac(3,4)}} 的值。'),
    para('（3）化簡 {(a^{frac(1,2)})^4}。'),
    para('提示：{a^{frac(m,n)}=sqrt[n](a^m)}；{(a^m)^n=a^{m×n}}。'),
] + write_lines(5)))

P.append(problem_box([
    para('5．利用冪函數的單調性比較大小（不必算出實際數值，寫出理由）：'),
    para('（1）比較 {1.5^3} 與 {1.4^3} 的大小。'),
    para('（2）比較 {(-1.5)^3} 與 {(-1.4)^3} 的大小。'),
    para('提示：{y=x^3} 在整個 R 上遞增，x 大則 y 大。'),
] + write_lines(4)))

P.append(problem_box([
    para('6．已知冪函數 {y=x^α} 的圖象經過點 (2, 8)，求 α 的值。'),
    para('提示：把點的坐標代入 {y=x^α}，得到 {2^α=8}，再把 8 寫成 2 的次方。'),
] + write_lines(4)))

# ---------------- 練習C ----------------
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(problem_box([
    para('7．已知冪函數 {f(x)=x^α} 的圖象經過點 (3, {frac(1,9)})。'),
    para('（1）求 {f(x)} 的解析式。'),
    para('（2）寫出 {f(x)} 的定義域，並判斷它的奇偶性與單調性。'),
    para('提示：先代點求 α（把 {frac(1,9)} 寫成 3 的次方）；{x^{-2}=frac(1,x^2)}。'),
] + write_lines(5)))

P.append(problem_box([
    para('8．仿講義範例，用單調性定義證明冪函數 {f(x)=sqrt(x)} 在 [0, +∞) 上是增函數。'),
    para('提示：照「①取值 ②作差 ③變形 ④定號 ⑤結論」五步驟；作差後把 {sqrt(x_1)-sqrt(x_2)} '
         '乘以 {frac(sqrt(x_1)+sqrt(x_2),sqrt(x_1)+sqrt(x_2))} 分子有理化。'),
] + write_lines(5)))

P.append(problem_box([
    para('9．氣體從圓管流出的流量 Q，與圓管半徑 r 的四次方成正比。'),
    para('（1）寫出 Q 關於 r 的函數關係式（用 k 表示比例常數）。'),
    para('（2）若半徑變為原來的 2 倍，流量會變為原來的幾倍？'),
    para('提示：「與 r 的四次方成正比」表示 {Q=k×r^4}，k 是常數。'),
] + write_lines(4), trailing_blank=False))

# ---------------- 參考答案 ----------------
P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('練習A'))
P.append(para('1．（B）。{y=2x^2} 係數是 2、{y=3^x} 是指數函數，都不是冪函數；只有 {y=x^4} 符合 {y=x^α}。'))
P.append(para('2．（1）定義域 R，值域 [0, +∞)。（2）奇函數。（3）點 (1, 1)。'))
P.append(para('3．（1）{9^{frac(1,2)}=sqrt(9)=3}。（2）{8^{frac(1,3)}=sqrt[3](8)=2}。（3）{4^{-1}=frac(1,4)}。'))
P.append(para('練習B'))
P.append(para('4．（1）{sqrt[3](x^2)=x^{frac(2,3)}}。（2）{16^{frac(3,4)}=(sqrt[4](16))^3=2^3=8}。'
              '（3）{(a^{frac(1,2)})^4=a^{frac(1,2)×4}=a^2}。'))
P.append(para('5．（1）{y=x^3} 在 R 上遞增，因 {1.5>1.4}，所以 {1.5^3>1.4^3}。'
              '（2）同樣遞增，因 {-1.5<-1.4}，所以 {(-1.5)^3<(-1.4)^3}。'))
P.append(para('6．代入得 {2^α=8=2^3}，所以 {α=3}。'))
P.append(para('練習C'))
P.append(para('7．（1）代入 {3^α=frac(1,9)=3^{-2}}，得 {α=-2}，所以 {f(x)=x^{-2}=frac(1,x^2)}。'
              '（2）定義域 x ≠ 0；{f(-x)=frac(1,(-x)^2)=frac(1,x^2)=f(x)}，是偶函數；'
              '在 (0, +∞) 上遞減，在 (−∞, 0) 上遞增。'))
P.append(para('8．①取值：設 {0<=x_1<x_2}。'
              '②作差、③變形：{sqrt(x_1)-sqrt(x_2)=frac(x_1-x_2,sqrt(x_1)+sqrt(x_2))}。'
              '④定號：{x_1-x_2<0}，且 {sqrt(x_1)+sqrt(x_2)>0}，所以差 {<0}。'
              '⑤結論：{f(x_1)<f(x_2)}，故 {f(x)=sqrt(x)} 在 [0, +∞) 上是增函數。'))
P.append(para('9．（1）{Q=k×r^4}。（2）半徑變 2 倍：{Q\'=k×(2r)^4=16×k×r^4=16Q}，流量變為原來的 16 倍。'))

out = build_docx(P, os.path.join(HERE, '練習_冪函數的性質_高一數學.docx'),
                 footer_text='高一數學．冪函數的性質')
print('practice built')
