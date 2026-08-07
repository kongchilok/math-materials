# -*- coding: utf-8 -*-
"""練習_複合函數_高一數學.docx（課本無此節，補充教材，自行設計）"""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

HERE = os.path.dirname(os.path.abspath(__file__))

P = []
P.append(masthead('高一數學', '複合函數（補充）', '課堂練習'))
P.append(student_info_row())
P.append(para('作答前先回頭看《複合函數（補充）課堂講義》的機器串聯圖與三個範例，'
              '記住「把 f(x) 裡的每個 x 換成整個 g(x)」這句口訣，完成下面練習A、B、C。'))

# ---------------- 練習A ----------------
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(problem_box([
    para('1．已知 {f(x)=2x+1}，{g(x)=x^2}，求下列各值（先算裡面、再算外面）：'),
    para('（1）{f(g(1))}＝＿＿（先算 {g(1)=} ＿＿，再算 f(那個值)）'),
    para('（2）{g(f(1))}＝＿＿（先算 {f(1)=} ＿＿，再算 g(那個值)）'),
    para('提示：括號裡面的先算完，得到一個數，再拿去代進外面那個函數。'),
] + write_lines(3)))

P.append(problem_box([
    para('2．已知 {f(x)=x^2}，則 f(x+1) 等於下面哪一個？（單選）'),
    para('（A）{x^2+1}　（B）{(x+1)^2}　（C）{x^2+x}'),
    para('提示：把 {f(x)} 裡的 x 整個換成 (x+1)。'),
] + write_lines(2)))

P.append(problem_box([
    para('3．已知 {f(x)=x+3}，{g(x)=2x}，求 f(g(x)) 的解析式。'),
    para('提示：把 {f(x)=x+3} 裡的 x 換成 g(x)=2x。'),
] + write_lines(2)))

# ---------------- 練習B ----------------
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(problem_box([
    para('4．已知 {f(x)=x^2+3x+2}，{g(x)=x+1}，求 f(g(x)) 的解析式。'),
    para('提示：把每個 x 換成 (x+1)，再展開整理；照講義範例一的四步驟寫。'),
] + write_lines(5)))

P.append(problem_box([
    para('5．已知 {f(x)=3x-1}，{g(x)=x^2+2}。'),
    para('（1）求 f(g(x)) 的解析式。（2）求 g(f(x)) 的解析式。（3）這兩個結果一樣嗎？'),
    para('提示：(1) 把 g(x) 代進 f；(2) 把 f(x) 代進 g；算完比對兩個式子。'),
] + write_lines(5)))

P.append(problem_box([
    para('6．已知 {f(x)=sqrt(x)}，{g(x)=x-3}，求 f(g(x)) 的解析式，並寫出它的定義域。'),
    para('提示：先寫出 {sqrt(x-3)}；再由「根號裡 {>=0}」求定義域。'),
] + write_lines(4)))

# ---------------- 練習C ----------------
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(problem_box([
    para('7．已知 {f(x)=frac(1,x+1)}，{g(x)=x^2}，求 f(g(x)) 的解析式，並寫出它的定義域。'),
    para('提示：把 f 裡的 x 換成 {x^2}，得 {frac(1,x^2+1)}；再想想分母 {x^2+1} 會不會等於 0。'),
] + write_lines(5)))

P.append(problem_box([
    para('8．已知 {f(x+1)=x^2+2x+3}，求 {f(x)} 的解析式。'),
    para('提示：設 {t=x+1}，則 {x=t-1}；把右邊的 x 都換成 (t-1) 算出 f(t)，最後把 t 改寫回 x。'),
] + write_lines(5)))

P.append(problem_box([
    para('9．已知 {f(x)=2x-1}。'),
    para('（1）求 f(f(x)) 的解析式。（2）求 f(f(f(0))) 的值。'),
    para('提示：f(f(x)) 就是把 f 自己代進自己；(2) 從最裡面 f(0) 一層一層往外算。'),
] + write_lines(4), trailing_blank=False))

# ---------------- 參考答案 ----------------
P.append(heading('參考答案與解析', page_break_before=True))
P.append(para('練習A'))
P.append(para('1．（1）{g(1)=1^2=1}，{f(1)=2×1+1=3}，所以 {f(g(1))=3}。'
              '（2）{f(1)=3}，{g(3)=3^2=9}，所以 {g(f(1))=9}。'
              '（兩個答案不同，正好說明複合的順序會影響結果。）'))
P.append(para('2．（B）。把 {f(x)=x^2} 裡的 x 換成 (x+1)，得 {f(x+1)=(x+1)^2}。'))
P.append(para('3．{f(g(x))=g(x)+3=2x+3}。'))
P.append(para('練習B'))
P.append(para('4．{f(g(x))=(x+1)^2+3(x+1)+2=x^2+2x+1+3x+3+2=x^2+5x+6}。'))
P.append(para('5．（1）{f(g(x))=3(x^2+2)-1=3x^2+5}。（2）{g(f(x))=(3x-1)^2+2=9x^2-6x+3}。'
              '（3）不一樣，因為複合的順序不同。'))
P.append(para('6．{f(g(x))=sqrt(x-3)}；根號裡要 {>=0}，即 {x-3>=0}，定義域為 {x>=3}。'))
P.append(para('練習C'))
P.append(para('7．{f(g(x))=frac(1,x^2+1)}；因為 {x^2+1>=1>0} 永遠不等於 0，'
              '所以分母恆有意義，定義域是全體實數 R。'))
P.append(para('8．設 {t=x+1}，則 {x=t-1}，{f(t)=(t-1)^2+2(t-1)+3=t^2-2t+1+2t-2+3=t^2+2}，'
              '所以 {f(x)=x^2+2}。（驗算：{f(x+1)=(x+1)^2+2=x^2+2x+3}，正確。）'))
P.append(para('9．（1）{f(f(x))=2(2x-1)-1=4x-3}。'
              '（2）{f(0)=-1}，{f(-1)=-3}，{f(-3)=-7}，所以 {f(f(f(0)))=-7}。'))

out = build_docx(P, os.path.join(HERE, '練習_複合函數_高一數學.docx'),
                 footer_text='高一數學．複合函數（補充）')
print('practice built')
