# -*- coding: utf-8 -*-
"""Build 講義_對數方程 + 練習_對數方程一題多練 (docx, house style)."""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

# 2026-08-21：腳本搬入 _scripts/ 後，OUT 仍指向腳本自己那層，會把交付檔寫錯位置。
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBJECT = '高一數學'
UNIT = '對數方程一題多練'

def eq(*parts):
    return ('m', omath(*parts))

# ============================================================ 講義 ============================================================
P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、解法一：直接轉換'))
P.append(problem_box([
    para([eq(sub(mr('log'), mr('a')), mr('(...)=b')), ('t', '　⟹　(...)='), eq(sup(mr('a'), mr('b')))]),
    para([('t', '例：'), eq(sub(mr('log'), mr('2')), mr('(x+5)=3')), ('t', ' ⟹ '), eq(mr('x+5='), sup(mr('2'), mr('3')), mr('=8')), ('t', ' ⟹ x=3')]),
    para([('t', '★ 解完一定要「檢驗」：把 x 代回去，確認「真數」（log 括號裡的東西）大於 0！')], bold=True),
]))

P.append(heading('二、解法二：合併對數'))
P.append(problem_box([
    para([eq(sub(mr('log'), mr('a')), mr('M+'), sub(mr('log'), mr('a')), mr('N='), sub(mr('log'), mr('a')), mr('(MN)'))]),
    para([('t', '先把等號一邊的 log 合併成一個，兩邊底數相同時，真數也要相等。')]),
]))

P.append(heading('三、解法三：換底比較'))
P.append(problem_box([
    para([('t', '當兩個 log 底數不同（如 '), eq(sub(mr('log'), mr('2')), mr('x='), sub(mr('log'), mr('8')), mr('27')), ('t', '）時，把底數大的一方用換底公式化成底數小的，變成同底再比較真數。')]),
]))

P.append(heading('四、解法四：換元法（設 t=logₐx）'))
P.append(problem_box([
    para([('t', '當方程式出現 '), eq(sup(mr('(') + sub(mr('log'), mr('a')) + mr('x') + mr(')'), mr('2'))), ('t', ' 和 '), eq(sub(mr('log'), mr('a')), mr('x')), ('t', ' 兩種形式，且像二次方程時，設 '), eq(mr('t='), sub(mr('log'), mr('a')), mr('x'))]),
    para([('t', '轉化成關於 t 的一元二次方程，解出 t 之後，再代回 '), eq(sub(mr('log'), mr('a')), mr('x=t')), ('t', ' 解 x，並記得檢驗真數（或底數）是否大於 0。')]),
]))

P.append(heading('五、範例'))
P.append(shaded_multi_box([
    para([('t', '例：解方程 '), eq(sub(mr('log'), mr('2')), mr('(3x)-'), sub(mr('log'), mr('2')), mr('(x-1)=3'))]),
    para([('t', '步驟①　合併對數：'), eq(sub(mr('log'), mr('2')), mr('('), frac(mr('3x'), mr('x-1')), mr(')=3'))]),
    para([('t', '步驟②　轉換成指數式：'), eq(frac(mr('3x'), mr('x-1')), mr('='), sup(mr('2'), mr('3')), mr('=8'))]),
    para([('t', '步驟③　解方程：'), eq(mr('3x=8(x-1)')), ('t', ' ⟹ '), eq(mr('3x=8x-8')), ('t', ' ⟹ '), eq(mr('x='), frac(mr('8'), mr('5')))]),
    para([('t', '步驟④　檢驗：x=8/5 時，3x=24/5>0，x-1=3/5>0，都合法，所以 '), eq(mr('x='), frac(mr('8'), mr('5'))), ('t', ' 是方程的解。')]),
]))

P.append(blank())
P.append(para([('t', '接下來請拿《練習_對數方程一題多練》，依這套框架完成練習A、B、C。')]))

out1 = build_docx(P, os.path.join(OUT, '講義_對數方程_融合版.docx'), footer_text='高一數學．對數方程一題多練')
print('講義 ->', out1)

# ============================================================ 練習 ============================================================
Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para([('t', '提示：先回頭看《講義》的範例四步驟，再開始練習。每題解完都要檢驗真數是否大於0！')]))

# ---------- 練習A ----------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(shaded_box([para([eq(sub(mr('log'), mr('a')), mr('(...)=b')), ('t', '　⟹　(...)='), eq(sup(mr('a'), mr('b'))), ('t', '　　　鷹架：先找出 a、b，再把(...)那一整塊當成未知數解出來。')])], kind='hint'))

Q.append(problem_box([para([('t', '1．'), eq(sub(mr('log'), mr('2')), mr('(x+5)=3'))])] + write_lines(3)))
Q.append(problem_box([para([('t', '2．'), eq(sub(mr('log'), mr('5')), mr('(4x-3)=2'))])] + write_lines(3)))
Q.append(problem_box([para([('t', '3．'), eq(sub(mr('log'), mr('3')), mr('(5x-1)=1'))])] + write_lines(3)))
Q.append(problem_box([para([('t', '4．'), eq(sub(mr('log'), mr('2')), mr('(2x+1)=2'))])] + write_lines(3)))

# ---------- 練習B ----------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(shaded_box([para([('t', '提示：同底的 log 先合併成一個；換底時把底數大的那個換成底數小的。合併/換底完別忘了檢驗。')])], kind='hint'))

Q.append(problem_box([para([('t', '1．'), eq(sub(mr('log'), mr('3')), mr('(2x+1)+'), sub(mr('log'), mr('3')), mr('4=3'))])] + write_lines(4)))
Q.append(problem_box([para([('t', '2．'), eq(sub(mr('log'), mr('5')), mr('(10x)-'), sub(mr('log'), mr('5')), mr('2=2'))])] + write_lines(3)))
Q.append(problem_box([para([('t', '3．'), eq(sub(mr('log'), mr('6')), mr('(x-3)+'), sub(mr('log'), mr('6')), mr('(x-2)=1'))])] + write_lines(4)))
Q.append(problem_box([para([('t', '4．'), eq(sub(mr('log'), mr('4')), mr('(x-1)+'), sub(mr('log'), mr('4')), mr('(x+2)=1'))])] + write_lines(4)))
Q.append(problem_box([para([('t', '5．'), eq(sub(mr('log'), mr('3')), mr('x='), sub(mr('log'), mr('9')), mr('25'))])] + write_lines(4)))

# ---------- 練習C ----------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(shaded_box([para([('t', '提示：出現 '), eq(sup(mr('(') + sub(mr('log'), mr('a')) + mr('x') + mr(')'), mr('2'))), ('t', ' 和 '), eq(sub(mr('log'), mr('a')), mr('x')), ('t', ' 時，設 t=logₐx 轉成二次方程；底數含未知數（如 log_x2）時，先用換底公式把它變成 1/t。')])], kind='hint'))

Q.append(problem_box([
    para([('t', '1．'), eq(sup(mr('(') + sub(mr('log'), mr('2')) + mr('x)'), mr('2')), mr('-'), sub(mr('log'), mr('2')), mr('x=2'))]),
] + write_lines(5)))
Q.append(problem_box([
    para([('t', '2．'), eq(sup(mr('(') + sub(mr('log'), mr('2')) + mr('x)'), mr('2')), mr('-4'), sub(mr('log'), mr('2')), mr('x+3=0'))]),
] + write_lines(4)))
Q.append(problem_box([
    para([('t', '3．'), eq(sub(mr('log'), mr('2')), mr('x-4'), sub(mr('log'), mr('x')), mr('2+3=0'))]),
] + write_lines(5)))
Q.append(problem_box([
    para([('t', '4．'), eq(sub(mr('log'), mr('9')), mr('(x+5)='), sub(mr('log'), mr('27')), mr('125'))]),
] + write_lines(5)))
Q.append(problem_box([
    para([('t', '5．綜合題：'), eq(sup(mr('9'), mr('x')), mr('-'), sup(mr('3'), mr('x')), mr('-6=0')), ('t', '（提示：這題要先設 '), eq(mr('t='), sup(mr('3'), mr('x'))), ('t', '，因為 '), eq(sup(mr('9'), mr('x')), mr('='), sup(mr('(') + sup(mr('3'), mr('x')) + mr(')'), mr('2'))), ('t', '）')]),
] + write_lines(5)))

# ---------- 教師用參考答案 ----------
Q.append(pagebreak())
Q.append(masthead(SUBJECT, UNIT, '教師用參考答案'))

Q.append(heading('練習A 參考答案'))
Q.append(para([('t', '1．x+5=8 ⟹ x=3（檢驗：x+5=8>0 ✓）')]))
Q.append(para([('t', '2．4x-3=25 ⟹ x=7（檢驗：4x-3=25>0 ✓）')]))
Q.append(para([('t', '3．5x-1=3 ⟹ x=4/5（檢驗：5x-1=3>0 ✓）')]))
Q.append(para([('t', '4．2x+1=4 ⟹ x=3/2（檢驗：2x+1=4>0 ✓）')]))

Q.append(heading('練習B 參考答案'))
Q.append(para([('t', '1．合併：'), eq(sub(mr('log'), mr('3')), mr('[4(2x+1)]=3')), ('t', ' ⟹ 4(2x+1)=27 ⟹ x=23/8（檢驗：2x+1=27/4>0 ✓）')]))
Q.append(para([('t', '2．合併：'), eq(sub(mr('log'), mr('5')), mr('(5x)=2')), ('t', ' ⟹ 5x=25 ⟹ x=5（檢驗：10x=50>0、5x=25>0 ✓）')]))
Q.append(para([('t', '3．合併：(x-3)(x-2)=6 ⟹ x²-5x=0 ⟹ x=0 或 x=5。定義域要求 x>3，所以 x=0 捨去，只留 x=5。')]))
Q.append(para([('t', '4．合併：(x-1)(x+2)=4 ⟹ x²+x-6=0 ⟹ (x+3)(x-2)=0 ⟹ x=-3 或 x=2。定義域要求 x>1，x=-3 捨去，只留 x=2。')]))
Q.append(para([('t', '5．換底：'), eq(sub(mr('log'), mr('9')), mr('25=')), ('t', ' log_(3²)5² = log₃5，所以 log₃x=log₃5 ⟹ x=5（檢驗：x=5>0 ✓）')]))

Q.append(heading('練習C 參考答案'))
Q.append(para([('t', '1．設t=log₂x：t²-t-2=0 ⟹ (t-2)(t+1)=0 ⟹ t=2 或 t=-1。log₂x=2⟹x=4；log₂x=-1⟹x=1/2。兩個都是x>0，都合法。')]))
Q.append(para([('t', '2．設t=log₂x：t²-4t+3=0 ⟹ (t-1)(t-3)=0 ⟹ t=1 或 3 ⟹ x=2 或 x=8。')]))
Q.append(para([('t', '3．設t=log₂x，則log_x2=1/t：t-4/t+3=0 ⟹ t²+3t-4=0 ⟹ (t+4)(t-1)=0 ⟹ t=-4 或 1。log₂x=-4⟹x=1/16；log₂x=1⟹x=2。定義域x>0且x≠1，兩個都合法。')]))
Q.append(para([('t', '4．換底：log₂₇125=log_(3³)5³=log₃5；log₉(x+5)=(1/2)log₃(x+5)。所以(1/2)log₃(x+5)=log₃5 ⟹ log₃(x+5)=2log₃5=log₃25 ⟹ x+5=25 ⟹ x=20（檢驗：x+5=25>0 ✓）')]))
Q.append(para([('t', '5．設t=3ˣ(t>0)：t²-t-6=0 ⟹ (t-3)(t+2)=0 ⟹ t=3 或 t=-2（捨去，t必須>0）。t=3 ⟹ 3ˣ=3 ⟹ x=1。')]))

out2 = build_docx(Q, os.path.join(OUT, '練習_對數方程一題多練_融合版.docx'), footer_text='高一數學．對數方程一題多練')
print('練習 ->', out2)
