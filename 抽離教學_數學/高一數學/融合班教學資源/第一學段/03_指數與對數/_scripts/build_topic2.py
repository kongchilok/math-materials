# -*- coding: utf-8 -*-
"""Build 講義_指對數運算 + 練習_指對數運算 (docx, house style)."""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

# 2026-08-21：腳本搬入 _scripts/ 後，OUT 仍指向腳本自己那層，會把交付檔寫錯位置。
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBJECT = '高一數學'
UNIT = '指對數運算（轉換、化簡、定義域值域）'

def eq(*parts):
    return ('m', omath(*parts))

# ============================================================ 講義 ============================================================
P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、指數式與對數式互換'))
P.append(problem_box([
    para([eq(sup(mr('a'), mr('b')), mr('=N')), ('t', '　⟺　'), eq(sub(mr('log'), mr('a')), mr('N=b'))]),
    para([('t', '（a>0，a≠1，N>0）　　　　讀作：以 a 為底 N 的對數等於 b')]),
]))

P.append(heading('二、對數運算性質'))
P.append(problem_box([
    para([eq(sub(mr('log'), mr('a')), mr('(MN)='), sub(mr('log'), mr('a')), mr('M+'), sub(mr('log'), mr('a')), mr('N'))]),
    para([eq(sub(mr('log'), mr('a')), mr('('), frac(mr('M'), mr('N')), mr(')='), sub(mr('log'), mr('a')), mr('M-'), sub(mr('log'), mr('a')), mr('N'))]),
    para([eq(sub(mr('log'), mr('a')), sup(mr('M'), mr('n')), mr('=n'), sub(mr('log'), mr('a')), mr('M'))]),
    para([('t', '恆等式：'), eq(sup(mr('a'), sub(mr('log'), mr('a')) + mr('N')), mr('=N'))]),
]))

P.append(heading('三、範例'))
P.append(shaded_multi_box([
    para([('t', '例：求 '), eq(sub(mr('log'), mr('2')), sqrt(mr('2'))), ('t', ' 的值')]),
    para([('t', '步驟①　把根式寫成分數指數冪：'), eq(sqrt(mr('2')), mr('='), sup(mr('2'), frac(mr('1'), mr('2'))))]),
    para([('t', '步驟②　代入：'), eq(sub(mr('log'), mr('2')), sqrt(mr('2')), mr('='), sub(mr('log'), mr('2')), sup(mr('2'), frac(mr('1'), mr('2'))))]),
    para([('t', '步驟③　用 '), eq(sub(mr('log'), mr('a')), sup(mr('M'), mr('n')), mr('=n'), sub(mr('log'), mr('a')), mr('M')), ('t', '：'), eq(mr('='), frac(mr('1'), mr('2')), sub(mr('log'), mr('2')), mr('2'))]),
    para([('t', '步驟④　'), eq(sub(mr('log'), mr('2')), mr('2=1')), ('t', '，所以：'), eq(mr('='), frac(mr('1'), mr('2')))]),
]))

P.append(blank())
P.append(para([('t', '接下來請拿《練習_指對數運算》，依這套框架完成練習A、B、C。')]))

out1 = build_docx(P, os.path.join(OUT, '講義_指對數運算_融合版.docx'), footer_text='高一數學．指對數運算')
print('講義 ->', out1)

# ============================================================ 練習 ============================================================
Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para([('t', '提示：先回頭看《講義》的範例四步驟，再開始練習。')]))

# ---------- 練習A ----------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(shaded_box([para([eq(sup(mr('a'), mr('b')), mr('=N')), ('t', '　⟺　'), eq(sub(mr('log'), mr('a')), mr('N=b')), ('t', '　　　鷹架：先找出 a、b、N 各是誰，再代入公式。')])], kind='hint'))

Q.append(problem_box([
    para([('t', '1．把 '), eq(sup(mr('32'), frac(mr('2'), mr('5'))), mr('=4')), ('t', ' 寫成對數形式。')]),
] + write_lines(2)))
Q.append(problem_box([
    para([('t', '2．把 '), eq(sub(mr('log'), mr('3')), mr('(') + frac(mr('1'), mr('9')) + mr(')'), mr('=-2')), ('t', ' 寫成指數式。')]),
] + write_lines(2)))
Q.append(problem_box([
    para([('t', '3．把 '), eq(sub(mr('log'), frac(mr('1'), mr('2'))), mr('32=-5')), ('t', ' 寫成指數式。')]),
] + write_lines(2)))
Q.append(problem_box([
    para([('t', '4．求值（提示：'), eq(sup(mr('a'), sub(mr('log'), mr('a')) + mr('N')), mr('=N')), ('t', '）：'), eq(sup(mr('3'), sub(mr('log'), mr('3')) + mr('5')), mr('='))]),
    para([eq(sub(mr('log'), mr('3')), mr('('), sub(mr('log'), mr('3')), mr('3)='))]),
] + write_lines(3)))

# ---------- 練習B ----------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(shaded_box([para([('t', '提示：先化成同底，再用對數運算性質；比較大小時先看函數是遞增還是遞減。')])], kind='hint'))

Q.append(problem_box([
    para([('t', '1．求值：'), eq(sup(mr('(') + frac(mr('4'), mr('9')) + mr(')'), mr('-') + frac(mr('1'), mr('2'))), mr('='))]),
    para([eq(sup(mr('(') + frac(mr('8'), mr('27')) + mr(')'), frac(mr('2'), mr('3'))), mr('='))]),
] + write_lines(3)))
Q.append(problem_box([
    para([('t', '2．已知 '), eq(sub(mr('log'), mr('3')), mr('x=2')), ('t', '，求 x。')]),
] + write_lines(2)))
Q.append(problem_box([
    para([('t', '3．求值：'), eq(sub(mr('log'), mr('5')), mr('3+'), sub(mr('log'), mr('5')), frac(mr('1'), mr('3')))]),
] + write_lines(3)))
Q.append(problem_box([
    para([('t', '4．下列哪一個是「對數函數」？')]),
    para([('t', '(A) '), eq(mr('y='), sub(mr('log'), mr('3')), mr('x')), ('t', '　　(B) '), eq(mr('y='), mr('2'), sub(mr('log'), mr('3')), mr('x+3')), ('t', '　　(C) '), eq(mr('y='), sub(mr('log'), mr('x')), mr('2'))]),
] + write_lines(3)))
Q.append(problem_box([
    para([('t', '5．若 '), eq(sup(mr('a'), mr('b')), mr('=2')), ('t', '（a>0，a≠1），寫成對數式。')]),
] + write_lines(2)))
Q.append(problem_box([
    para([('t', '6．求定義域和值域：'), eq(mr('y='), sub(mr('log'), mr('5')), mr('(x-3)'))]),
] + write_lines(3)))
Q.append(problem_box([
    para([('t', '7．指數函數 '), eq(mr('f(x)')), ('t', ' 的圖像過點 (3, 8)，求 '), eq(mr('f(x)')), ('t', ' 的解析式。')]),
] + write_lines(3)))

# ---------- 練習C ----------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(shaded_box([para([('t', '提示：留意「底數在(0,1)之間會讓函數遞減」；反函數是把 x、y 對調後解出 y。')])], kind='hint'))

Q.append(problem_box([
    para([('t', '1．求定義域和值域：'), eq(mr('y='), sub(mr('log'), mr('2')), mr('('), sup(mr('x'), mr('2')), mr('+1)'))]),
] + write_lines(4)))
Q.append(problem_box([
    para([('t', '2．求值：'), eq(sub(mr('log'), mr('2')), sqrt(mr('2')), mr('+'), sub(mr('log'), mr('9')), mr('27+'), sup(mr('3'), sub(mr('log'), mr('3')) + mr('16')))]),
] + write_lines(4)))
Q.append(problem_box([
    para([('t', '3．求值：'), eq(sub(mr('log'), mr('2')), mr('5×'), sub(mr('log'), mr('3')), mr('2×'), sub(mr('log'), mr('5')), mr('3'))]),
] + write_lines(3)))
Q.append(problem_box([
    para([('t', '4．若 '), eq(mr('y=f(x)')), ('t', ' 是 '), eq(mr('y='), sup(mr('3'), mr('x'))), ('t', ' 的反函數，求 '), eq(mr('f('), frac(mr('1'), mr('2')), mr(')')), ('t', ' 的值。')]),
] + write_lines(3)))
Q.append(problem_box([
    para([('t', '5．開放銜接題：解方程 '), eq(sub(mr('log'), mr('10')), mr('x+'), sub(mr('log'), mr('10')), mr('(9-2x)=1')), ('t', '，並說明為什麼求出兩個 x 之後，還要各別檢查它們是否讓 x>0 且 9-2x>0 都成立。')]),
] + write_lines(5)))

# ---------- 教師用參考答案 ----------
Q.append(pagebreak())
Q.append(masthead(SUBJECT, UNIT, '教師用參考答案'))

Q.append(heading('練習A 參考答案'))
Q.append(para([('t', '1．'), eq(sub(mr('log'), mr('32')), mr('4='), frac(mr('2'), mr('5')))]))
Q.append(para([('t', '2．'), eq(sup(mr('3'), mr('-2')), mr('='), frac(mr('1'), mr('9')))]))
Q.append(para([('t', '3．'), eq(sup(mr('(') + frac(mr('1'), mr('2')) + mr(')'), mr('-5')), mr('=32'))]))
Q.append(para([('t', '4．'), eq(sup(mr('3'), sub(mr('log'), mr('3')) + mr('5')), mr('=5')), ('t', '（恆等式直接代入）；'), eq(sub(mr('log'), mr('3')), mr('3=1')), ('t', '，所以 '), eq(sub(mr('log'), mr('3')), mr('(1)=0'))]))

Q.append(heading('練習B 參考答案'))
Q.append(para([('t', '1．'), eq(sup(mr('(') + frac(mr('4'), mr('9')) + mr(')'), mr('-') + frac(mr('1'), mr('2'))), mr('='), frac(mr('3'), mr('2'))), ('t', '；'), eq(sup(mr('(') + frac(mr('8'), mr('27')) + mr(')'), frac(mr('2'), mr('3'))), mr('='), frac(mr('4'), mr('9')))]))
Q.append(para([('t', '2．'), eq(sub(mr('log'), mr('3')), mr('x=2')), ('t', ' ⟹ '), eq(mr('x='), sup(mr('3'), mr('2')), mr('=9'))]))
Q.append(para([('t', '3．合併：'), eq(sub(mr('log'), mr('5')), mr('(3×'), frac(mr('1'), mr('3')), mr(')='), sub(mr('log'), mr('5')), mr('1=0'))]))
Q.append(para([('t', '4．正確答案是 (A)。(B)是對數函數乘2再加3，不是純對數函數；(C)底數放了變數x，對數函數要求底數是常數。')]))
Q.append(para([('t', '5．'), eq(sub(mr('log'), mr('a')), mr('2=b'))]))
Q.append(para([('t', '6．定義域：x>3（真數要大於0）；值域：R（全體實數，log函數的值域是所有實數）')]))
Q.append(para([('t', '7．設 '), eq(mr('f(x)='), sup(mr('a'), mr('x'))), ('t', '，代入(3,8)：'), eq(sup(mr('a'), mr('3')), mr('=8')), ('t', ' ⟹ a=2，所以 '), eq(mr('f(x)='), sup(mr('2'), mr('x')))]))

Q.append(heading('練習C 參考答案'))
Q.append(para([('t', '1．定義域：全體實數（因為'), eq(sup(mr('x'), mr('2')), mr('+1')), ('t', '恆大於0，x取任何值都可以）；值域：'), eq(mr('['), mr('0,+∞)')), ('t', '（因為'), eq(sup(mr('x'), mr('2')), mr('+1≥1')), ('t', '，取log後 ≥0）')]))
Q.append(para([('t', '2．'), eq(sub(mr('log'), mr('2')), sqrt(mr('2')), mr('=')), ('t', '1/2；'), eq(sub(mr('log'), mr('9')), mr('27=')), ('t', '3/2（因為 log_(3²)3³=(3/2)log₃3）；'), eq(sup(mr('3'), sub(mr('log'), mr('3')) + mr('16')), mr('=16')), ('t', '。總和 = 1/2+3/2+16 = 18')]))
Q.append(para([('t', '3．換底展開：（ln5/ln2）×（ln2/ln3）×（ln3/ln5）中間全部消掉 = 1')]))
Q.append(para([('t', '4．'), eq(mr('f(x)='), sub(mr('log'), mr('3')), mr('x')), ('t', '（是'), eq(sup(mr('3'), mr('x'))), ('t', '的反函數）；'), eq(mr('f('), frac(mr('1'), mr('2')), mr(')='), sub(mr('log'), mr('3')), mr('(') + frac(mr('1'), mr('2')) + mr(')')), ('t', ' = -log₃2')]))
Q.append(para([('t', '5．合併：log₁₀[x(9-2x)]=1 ⟹ x(9-2x)=10 ⟹ 2x²-9x+10=0 ⟹ (2x-5)(x-2)=0 ⟹ x=5/2 或 x=2。')]))
Q.append(para([('t', '兩根都要檢查：x=5/2時，9-2x=4>0成立；x=2時，9-2x=5>0成立。兩者都在定義域(0<x<4.5)內，所以兩個都是解——因為log的「真數」規定要大於0，如果只解方程不檢查，可能會把不合法的根當成答案。')]))

out2 = build_docx(Q, os.path.join(OUT, '練習_指對數運算_融合版.docx'), footer_text='高一數學．指對數運算')
print('練習 ->', out2)
