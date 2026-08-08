# -*- coding: utf-8 -*-
"""Build 講義_4.1指數運算 + 練習_4.1指數運算 (docx, house style)."""
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '高一數學'
UNIT = '4.1 指數運算（n次方根與分數指數冪）'

def eq(*parts):
    """One inline equation as a para() segment."""
    return ('m', omath(*parts))

def frline(*segs, sz=BODY_SZ):
    """A paragraph mixing ('t',...)/eq(...) segments, normal weight."""
    return para(list(segs), sz=sz)

def numbered_box(num, lines, n_write=3):
    """A problem_box: number + text on first line, then more lines, then write space."""
    return problem_box([para([('t', num)] + lines[0])] + [para(l) for l in lines[1:]] + write_lines(n_write))

# ============================================================ 講義 ============================================================
P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、n 次方根'))
P.append(para([('t', '如果 '), eq(sup(mr('x'), mr('n')), mr('=a')), ('t', '（n>1，n為正整數），那麼 x 叫做 a 的 n 次方根，記作 '), eq(nthroot(mr('a'), mr('n'))), ('t', '。')]))
P.append(problem_box([
    para([('t', '奇數次（n是奇數）：')], bold=True),
    para([('t', '　'), eq(mr('a>0')), ('t', ' → x>0　　'), eq(mr('a<0')), ('t', ' → x<0（唯一一個 x）')]),
    para([('t', '偶數次（n是偶數）：')], bold=True),
    para([('t', '　'), eq(mr('a>0')), ('t', ' → x 有兩個：'), eq(mr('x='), mr('±'), nthroot(mr('a'), mr('n')))]),
    para([('t', '　'), eq(mr('a<0')), ('t', ' → 沒有偶次方根（負數沒有偶次方根）')]),
    para([('t', '　0 的任何次方根都是 0。')]),
]))

P.append(heading('二、根式的性質'))
P.append(problem_box([
    para([('t', '① '), eq(sup(mr('(') + nthroot(mr('a'), mr('n')) + mr(')'), mr('n')), mr('=a'))]),
    para([('t', '② n為奇數時：'), eq(nthroot(sup(mr('a'), mr('n')), mr('n')), mr('=a'))]),
    para([('t', '　　n為偶數時：'), eq(nthroot(sup(mr('a'), mr('n')), mr('n')), mr('=')), ('t', '|a|')]),
]))

P.append(heading('三、分數指數冪'))
P.append(problem_box([
    para([eq(sup(mr('a'), frac(mr('m'), mr('n'))), mr('='), nthroot(sup(mr('a'), mr('m')), mr('n')))]),
    para([eq(sup(mr('a'), mr('-') + frac(mr('m'), mr('n'))), mr('='), frac(mr('1'), nthroot(sup(mr('a'), mr('m')), mr('n'))))]),
    para([('t', '（a>0，m、n為正整數，n>1）')]),
]))

P.append(heading('四、範例'))
P.append(shaded_multi_box([
    para([('t', '例：求 '), eq(sup(mr('8'), frac(mr('2'), mr('3')))), ('t', ' 的值')]),
    para([('t', '步驟①　先把底數寫成同一個數的次方：'), eq(mr('8='), sup(mr('2'), mr('3')))]),
    para([('t', '步驟②　代入分數指數冪定義：'), eq(sup(mr('8'), frac(mr('2'), mr('3'))), mr('='), sup(mr('(') + sup(mr('2'), mr('3')) + mr(')'), frac(mr('2'), mr('3'))))]),
    para([('t', '步驟③　指數相乘（3×'), eq(frac(mr('2'), mr('3'))), ('t', '=2）：'), eq(mr('='), sup(mr('2'), mr('2')))]),
    para([('t', '步驟④　算出答案：'), eq(mr('=4'))]),
]))

P.append(blank())
P.append(para([('t', '接下來請拿《練習_4.1指數運算》，依這套框架完成練習A、B、C。')]))

out1 = build_docx(P, os.path.join(OUT, '講義_4.1指數運算_融合版.docx'), footer_text='高一數學．4.1指數運算')
print('講義 ->', out1)

# ============================================================ 練習 ============================================================
Q = []
Q.append(masthead(SUBJECT, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para([('t', '提示：先回頭看《講義》的範例四步驟，再開始練習。')]))

# ---------- 練習A ----------
Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(shaded_multi_box([para([('t', '鷹架：先判斷 n 是奇數還是偶數，再套用規則填空。')])]))

a_items = [
    ('1．', eq(sup(mr('x'), mr('2')), mr('=9')), 'n=2 是＿＿數，x=＿＿'),
    ('2．', eq(sup(mr('x'), mr('3')), mr('=8')), 'n=3 是＿＿數，x=＿＿'),
    ('3．', eq(sup(mr('x'), mr('3')), mr('=-8')), 'n=3 是＿＿數，x=＿＿'),
    ('4．', eq(sup(mr('x'), mr('5')), mr('=-1')), 'n=5 是＿＿數，x=＿＿'),
    ('5．', eq(sup(mr('x'), mr('5')), mr('=0')), 'x=＿＿'),
]
for num, equ, hint in a_items:
    Q.append(problem_box([
        para([('t', num), equ]),
        para([('t', hint)], sz=22),
    ] + write_lines(2)))

# ---------- 練習B ----------
Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(shaded_multi_box([para([('t', '提示：('), eq(nthroot(mr('a'), mr('n'))), ('t', ')ⁿ=a；偶數次要注意絕對值；'), eq(sup(mr('a'), frac(mr('m'), mr('n'))), mr('='), nthroot(sup(mr('a'), mr('m')), mr('n')))])]))

Q.append(problem_box([
    para([('t', '1．計算下列各式：')]),
    para([eq(sup(mr('(') + sqrt(mr('5')) + mr(')'), mr('2')), mr('='))]),
    para([eq(sup(mr('(') + nthroot(mr('-5'), mr('3')) + mr(')'), mr('3')), mr('='))]),
    para([eq(nthroot(sup(mr('(a-b)'), mr('2')), mr('2')), mr('='))]),
] + write_lines(3)))

Q.append(problem_box([
    para([('t', '2．把根式寫成分數指數冪：')]),
    para([eq(nthroot(sup(mr('a'), mr('2')), mr('3')), mr('='))]),
    para([eq(sqrt(mr('a')), mr('='))]),
] + write_lines(2)))

Q.append(problem_box([
    para([('t', '3．計算 '), eq(sup(mr('(') + frac(mr('4'), mr('9')) + mr(')'), frac(mr('1'), mr('2'))), mr('='))]),
] + write_lines(3)))

Q.append(problem_box([
    para([('t', '4．設 a>0，把 '), eq(nthroot(mr('a'), mr('4')), mr('×'), nthroot(mr('a'), mr('12'))), ('t', ' 化為分數指數冪。')]),
] + write_lines(3)))

Q.append(problem_box([
    para([('t', '5．(a>0) 用分數指數冪表示：')]),
    para([eq(sqrt(sup(mr('a'), mr('3'))), mr('='))]),
    para([eq(frac(mr('1'), nthroot(sup(mr('a'), mr('5')), mr('3'))), mr('='))]),
] + write_lines(2)))

Q.append(problem_box([
    para([('t', '6．已知 a=4，求 '), eq(sup(mr('a'), frac(mr('1'), mr('6'))), mr('⋅'), sup(mr('a'), frac(mr('2'), mr('3'))), mr('÷'), sup(mr('a'), frac(mr('1'), mr('3')))), ('t', ' 的值。')]),
] + write_lines(4)))

# ---------- 練習C ----------
Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(shaded_multi_box([para([('t', '提示：先各別化簡每一項，出現「同一個值減同一個值」時，答案往往會變得很簡單。')])]))

Q.append(problem_box([
    para([('t', '1．下面四個等式，哪一個是對的？其餘三個各錯在哪裡？請逐一說明。')]),
    para([('t', '(A) '), eq(mr('3'), sup(mr('a'), mr('-2')), mr('='), frac(mr('1'), mr('3') + sup(mr('a'), mr('2'))))]),
    para([('t', '(B) '), eq(sup(mr('a'), frac(mr('2'), mr('3'))), mr('÷'), sup(mr('a'), frac(mr('1'), mr('3'))), mr('='), sup(mr('a'), frac(mr('1'), mr('3'))))]),
    para([('t', '(C) '), eq(nthroot(sup(mr('(-8)'), mr('6')), mr('6')), mr('=-8'))]),
    para([('t', '(D) '), eq(nthroot(sup(mr('2'), mr('4')), mr('3')), mr('='), sup(mr('2'), frac(mr('3'), mr('4'))))]),
] + write_lines(6)))

Q.append(problem_box([
    para([('t', '2．化簡：'), eq(mr('4'), sup(mr('a'), frac(mr('2'), mr('3'))), sup(mr('b'), mr('-') + frac(mr('1'), mr('3'))), mr('÷'), mr('('), mr('-') + frac(mr('2'), mr('3')), sup(mr('a'), mr('-') + frac(mr('1'), mr('3'))), sup(mr('b'), mr('-') + frac(mr('1'), mr('3'))), mr(')'))]),
] + write_lines(5)))

Q.append(problem_box([
    para([('t', '3．開放題：請自己選一個 a>0 的值，寫出一組「根式」與「分數指數冪」的等價互換式（例如 '), eq(nthroot(sup(mr('a'), mr('2')), mr('3')), mr('='), sup(mr('a'), frac(mr('2'), mr('3')))), ('t', '），並代入你選的 a 驗算兩邊是否相等。')]),
] + write_lines(5)))

# ---------- 教師用參考答案 ----------
Q.append(pagebreak())
Q.append(masthead(SUBJECT, UNIT, '教師用參考答案'))

Q.append(heading('練習A 參考答案'))
Q.append(para([('t', '1．n=2 是偶數，x=±3　　2．n=3 是奇數，x=2　　3．n=3 是奇數，x=-2　　4．n=5 是奇數，x=-1　　5．x=0')]))

Q.append(heading('練習B 參考答案'))
Q.append(para([('t', '1．'), eq(sup(mr('(') + sqrt(mr('5')) + mr(')'), mr('2')), mr('=5')), ('t', '；'), eq(sup(mr('(') + nthroot(mr('-5'), mr('3')) + mr(')'), mr('3')), mr('=-5')), ('t', '；'), eq(nthroot(sup(mr('(a-b)'), mr('2')), mr('2')), mr('=|a-b|'))]))
Q.append(para([('t', '2．'), eq(nthroot(sup(mr('a'), mr('2')), mr('3')), mr('='), sup(mr('a'), frac(mr('2'), mr('3')))), ('t', '；'), eq(sqrt(mr('a')), mr('='), sup(mr('a'), frac(mr('1'), mr('2'))))]))
Q.append(para([('t', '3．'), eq(sup(mr('(') + frac(mr('4'), mr('9')) + mr(')'), frac(mr('1'), mr('2'))), mr('='), frac(mr('2'), mr('3')))]))
Q.append(para([('t', '4．指數 1/4+1/12=1/3，所以 '), eq(nthroot(mr('a'), mr('4')), mr('×'), nthroot(mr('a'), mr('12')), mr('='), sup(mr('a'), frac(mr('1'), mr('3'))))]))
Q.append(para([('t', '5．'), eq(sqrt(sup(mr('a'), mr('3'))), mr('='), sup(mr('a'), frac(mr('3'), mr('2')))), ('t', '；'), eq(frac(mr('1'), nthroot(sup(mr('a'), mr('5')), mr('3'))), mr('='), sup(mr('a'), mr('-') + frac(mr('5'), mr('3'))))]))
Q.append(para([('t', '6．指數＝1/6+2/3-1/3=1/2，'), eq(sup(mr('4'), frac(mr('1'), mr('2'))), mr('=2'))]))

Q.append(heading('練習C 參考答案'))
Q.append(para([('t', '1．正確答案是 (B)。')]))
Q.append(para([('t', '(A)錯：3a⁻²＝3÷a²，3不會跟著進分母，正確應是 3/a²，不是 1/(3a²)。')]))
Q.append(para([('t', '(C)錯：偶次方根要取絕對值，⁶√((-8)⁶)＝|-8|＝8，不是-8。')]))
Q.append(para([('t', '(D)錯：³√(2⁴)＝2的4/3次方，不是2的3/4次方（根指數3在下面當分母，被開方數的指數4在上面當分子）。')]))
Q.append(para([('t', '2．4÷(-2/3)=-6；a的指數 2/3-(-1/3)=1；b的指數 -1/3-(-1/3)=0。答案＝-6a')]))
Q.append(para([('t', '3．（開放題，只要學生代入驗算成立即可，例如取a=8：³√(8²)=³√64=4，8的2/3次方=(2³)的2/3次方=2的2次方=4，兩邊相等）')]))

out2 = build_docx(Q, os.path.join(OUT, '練習_4.1指數運算_融合版.docx'), footer_text='高一數學．4.1指數運算')
print('練習 ->', out2)
