# -*- coding: utf-8 -*-
"""Build 講義_指數方程 + 練習_指數方程一題多練 (docx, house style)."""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

# 2026-08-21：腳本搬入 _scripts/ 後，OUT 仍指向腳本自己那層，會把交付檔寫錯位置。
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBJECT = '高一數學'
UNIT = '指數方程一題多練'

def eq(*parts):
    return ('m', omath(*parts))

# ============================================================ 講義 ============================================================
P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、解法一：化同底比指數'))
P.append(problem_box([
    para([eq(sup(mr('a'), mr('x')), mr('='), sup(mr('a'), mr('y'))), ('t', '　⟹　x=y　　（a>0，a≠1）')]),
    para([('t', '例：'), eq(sup(mr('2'), mr('x')), mr('=16')), ('t', ' ⟹ '), eq(sup(mr('2'), mr('x')), mr('='), sup(mr('2'), mr('4'))), ('t', ' ⟹ x=4')]),
]))

P.append(heading('二、解法二：合併同類項'))
P.append(problem_box([
    para([('t', '把方程式中同樣是 '), eq(sup(mr('a'), mr('x'))), ('t', ' 的項先合併（提公因式），再化同底比指數。')]),
    para([('t', '例：'), eq(sup(mr('3'), mr('x')), mr('+'), sup(mr('3'), mr('x')), mr('=54')), ('t', ' ⟹ '), eq(mr('2⋅'), sup(mr('3'), mr('x')), mr('=54')), ('t', ' ⟹ '), eq(sup(mr('3'), mr('x')), mr('=27='), sup(mr('3'), mr('3'))), ('t', ' ⟹ x=3')]),
]))

P.append(heading('三、解法三：換元法（設 t=aˣ）'))
P.append(problem_box([
    para([('t', '當方程式出現 '), eq(sup(mr('a'), mr('2x'))), ('t', ' 和 '), eq(sup(mr('a'), mr('x'))), ('t', ' 兩種指數，且形式像二次方程時，設 '), eq(mr('t='), sup(mr('a'), mr('x')), mr(', t>0'))]),
    para([('t', '轉化成關於 t 的一元二次方程，解出 t 之後，再代回 '), eq(sup(mr('a'), mr('x')), mr('=t')), ('t', ' 解 x。'), ]),
    para([('t', '★ 因為 '), eq(sup(mr('a'), mr('x'))), ('t', ' 恆大於 0，解出的 t 若是負數或 0，一定要捨去！')], bold=True),
]))

P.append(heading('四、範例'))
P.append(shaded_multi_box([
    para([('t', '例：解方程 '), eq(sup(mr('2'), mr('2x')), mr('-'), sup(mr('2'), mr('x')), mr('-6=0'))]),
    para([('t', '步驟①　設 '), eq(mr('t='), sup(mr('2'), mr('x')), mr(', t>0')), ('t', '，原方程變成：'), eq(sup(mr('t'), mr('2')), mr('-t-6=0'))]),
    para([('t', '步驟②　因式分解：'), eq(mr('(t-3)(t+2)=0')), ('t', ' ⟹ t=3 或 t=-2')]),
    para([('t', '步驟③　t=-2 不合（t 必須大於 0），只留 t=3，代回：'), eq(sup(mr('2'), mr('x')), mr('=3'))]),
    para([('t', '步驟④　'), eq(sup(mr('2'), mr('x')), mr('=3')), ('t', ' 不是整數次方，答案寫成：'), eq(mr('x='), sub(mr('log'), mr('2')), mr('3'))]),
]))

P.append(blank())
P.append(para([('t', '接下來請拿《練習_指數方程一題多練》，依這套框架完成練習A、B、C。')]))

out1 = build_docx(P, os.path.join(OUT, '講義_指數方程_融合版.docx'), footer_text='高一數學．指數方程一題多練')
print('講義 ->', out1)

# ============================================================ 練習 ============================================================
Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para([('t', '提示：先回頭看《講義》的範例四步驟，再開始練習。')]))

# ---------- 練習A ----------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(shaded_box([para([('t', '鷹架：先把方程式右邊的數字寫成跟左邊「同一個底數」的次方，再比較指數。')])], kind='hint'))

a_list = ['16', '64', '81(3^{x})', '64(4^{x})']
Q.append(problem_box([para([('t', '1．'), eq(sup(mr('2'), mr('x')), mr('=16'))]), para([('t', '鷹架：16＝2的幾次方？x=＿＿')])] + write_lines(2)))
Q.append(problem_box([para([('t', '2．'), eq(sup(mr('2'), mr('x')), mr('=64'))])] + write_lines(2)))
Q.append(problem_box([para([('t', '3．'), eq(sup(mr('3'), mr('x')), mr('=81'))])] + write_lines(2)))
Q.append(problem_box([para([('t', '4．'), eq(sup(mr('4'), mr('x')), mr('=64'))])] + write_lines(2)))
Q.append(problem_box([para([('t', '5．'), eq(sup(mr('2'), mr('x+2')), mr('=32'))])] + write_lines(2)))
Q.append(problem_box([para([('t', '6．'), eq(sup(mr('9'), mr('x')), mr('=3'))]), para([('t', '鷹架：9可以寫成3的幾次方？')], sz=22)] + write_lines(3)))

# ---------- 練習B ----------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(shaded_box([para([('t', '提示：根式先化成分數指數冪；同底的項先合併，再化同底比指數。')])], kind='hint'))

Q.append(problem_box([para([('t', '1．'), eq(sup(mr('2'), mr('x')), mr('='), sqrt(mr('8')))])] + write_lines(3)))
Q.append(problem_box([para([('t', '2．'), eq(sup(mr('9'), mr('x')), mr('='), sqrt(mr('27')))])] + write_lines(3)))
Q.append(problem_box([para([('t', '3．'), eq(sup(mr('3'), mr('x')), mr('+'), sup(mr('3'), mr('x')), mr('=54'))])] + write_lines(3)))
Q.append(problem_box([para([('t', '4．'), eq(sup(mr('4'), mr('x')), mr('+5⋅'), sup(mr('4'), mr('x')), mr('=96'))])] + write_lines(3)))
Q.append(problem_box([para([('t', '5．'), eq(sup(mr('5'), mr('x+1')), mr('-'), sup(mr('5'), mr('x')), mr('=100'))])] + write_lines(4)))
Q.append(problem_box([para([('t', '6．'), eq(sup(mr('3'), mr('x+1')), mr('+'), sup(mr('3'), mr('x')), mr('=4'))])] + write_lines(4)))

# ---------- 練習C ----------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(shaded_box([para([('t', '提示：出現兩種型式的指數項（如 '), eq(sup(mr('2'), mr('2x'))), ('t', ' 和 '), eq(sup(mr('2'), mr('x'))), ('t', '）時，設 t=aˣ 轉成二次方程；解完 t 記得檢查 t>0。')])], kind='hint'))

Q.append(problem_box([
    para([('t', '1．'), eq(sup(mr('2'), mr('2x')), mr('-6⋅'), sup(mr('2'), mr('x')), mr('+8=0'))]),
] + write_lines(5)))
Q.append(problem_box([
    para([('t', '2．'), eq(sup(mr('2'), mr('x+2')), mr('+'), sup(mr('2'), mr('x')), mr('=5'))]),
] + write_lines(4)))
Q.append(problem_box([
    para([('t', '3．'), eq(sup(mr('2'), mr('2x+1')), mr('-'), sup(mr('2'), mr('x+3')), mr('=64'))]),
] + write_lines(5)))
Q.append(problem_box([
    para([('t', '4．開放題：範例中，解出 t=-2 時我們直接捨去了。請說明：如果不檢查 t>0，把 t=-2 也代回 '), eq(sup(mr('2'), mr('x')), mr('=-2')), ('t', ' 繼續解下去，會發生什麼問題？')]),
] + write_lines(4)))

# ---------- 教師用參考答案 ----------
Q.append(pagebreak())
Q.append(masthead(SUBJECT, UNIT, '教師用參考答案'))

Q.append(heading('練習A 參考答案'))
Q.append(para([('t', '1．x=4　　2．x=6　　3．x=4　　4．x=3　　5．x=3（x+2=5）　　6．x=1/2（9=3²，3^(2x)=3¹ ⟹ 2x=1）')]))

Q.append(heading('練習B 參考答案'))
Q.append(para([('t', '1．'), eq(sup(mr('2'), mr('x')), mr('='), sup(mr('2'), frac(mr('3'), mr('2')))), ('t', ' ⟹ x=3/2　　2．'), eq(sup(mr('9'), mr('x')), mr('='), sup(mr('3'), frac(mr('3'), mr('2')))), ('t', ' ⟹ x=3/4')]))
Q.append(para([('t', '3．合併：2⋅3ˣ=54 ⟹ 3ˣ=27=3³ ⟹ x=3')]))
Q.append(para([('t', '4．合併：6⋅4ˣ=96 ⟹ 4ˣ=16=4² ⟹ x=2')]))
Q.append(para([('t', '5．合併：5ˣ(5-1)=100 ⟹ 4⋅5ˣ=100 ⟹ 5ˣ=25=5² ⟹ x=2')]))
Q.append(para([('t', '6．合併：3ˣ(3+1)=4 ⟹ 4⋅3ˣ=4 ⟹ 3ˣ=1=3⁰ ⟹ x=0')]))

Q.append(heading('練習C 參考答案'))
Q.append(para([('t', '1．設t=2ˣ(t>0)：t²-6t+8=0 ⟹ (t-2)(t-4)=0 ⟹ t=2 或 t=4，兩個都>0，都留。t=2⟹x=1；t=4⟹x=2。')]))
Q.append(para([('t', '2．'), eq(sup(mr('2'), mr('x+2')), mr('=4⋅'), sup(mr('2'), mr('x')))]), )
Q.append(para([('t', '所以原式＝4⋅2ˣ+2ˣ=5⋅2ˣ=5 ⟹ 2ˣ=1 ⟹ x=0（這題其實不用設t也能直接合併）')]))
Q.append(para([('t', '3．設t=2ˣ(t>0)：'), eq(sup(mr('2'), mr('2x+1')), mr('=2'), sup(mr('t'), mr('2')))]), )
Q.append(para([('t', '，'), eq(sup(mr('2'), mr('x+3')), mr('=8t')), ('t', '，方程變成 2t²-8t=64 ⟹ t²-4t-32=0 ⟹ (t-8)(t+4)=0 ⟹ t=8 或 t=-4（捨去，t必須>0）。t=8 ⟹ 2ˣ=8=2³ ⟹ x=3。')]))
Q.append(para([('t', '4．（開放題）如果不檢查就把 t=-2 代回 '), eq(sup(mr('2'), mr('x')), mr('=-2')), ('t', '，會發現找不到任何實數 x 能讓 2 的次方變成負數（2的任何次方都是正數），所以這是無解的假root。忽略 t>0 的限制，可能會誤以為方程有兩組解，或在後續計算中出現 log 負數這種沒有定義的運算，導致整題錯誤。')]))

out2 = build_docx(Q, os.path.join(OUT, '練習_指數方程一題多練_融合版.docx'), footer_text='高一數學．指數方程一題多練')
print('練習 ->', out2)
