# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

SUBJECT = '高一數學'
UNIT = '全稱量詞與存在量詞'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(para([('t', '提示：忘記怎麼做可以先回頭看《全稱量詞與存在量詞課堂講義》的範例四步驟。')]))

# ---------------- 練習A ★☆☆ ----------------
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(problem_box([
    para([('t', '1．判斷下列詞語是「全稱量詞」還是「存在量詞」，請打勾。')]),
    para([('t', '(1) 所有的　　全稱（　）　存在（　）')], ind=200),
    para([('t', '(2) 有一個　　全稱（　）　存在（　）')], ind=200),
    para([('t', '(3) 任意一個　　全稱（　）　存在（　）')], ind=200),
] + write_lines(1)))

P.append(problem_box([
    para([('t', '2．命題「'), ('m', omath(mr('∀x ∈ R, |x| ≥ 0'))), ('t', '」的意思是：對＿＿＿＿實數x，|x|都＿＿＿＿0。')]),
    para([('t', '提示：填入「所有的」和「大於等於」。')], sz=22),
] + write_lines(1)))

P.append(problem_box([
    para([('t', '3．判斷命題「所有的正方形都是四邊形」的真假。')]),
    para([('t', '真（　）　假（　）')], ind=200),
] + write_lines(2)))

# ---------------- 練習B ★★☆ ----------------
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(problem_box([
    para([('t', '4．用符號「∀」與「∃」表示下列命題，並判斷真假：')]),
    para([('t', '(1) 任意實數的平方大於或等於0；')], ind=200),
    para([('t', '(2) 存在整數x，使得 2x + 1 = 0。')], ind=200),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '5．判斷下列全稱量詞命題的真假：')]),
    para([('t', '(1) 對任意實數a，二次函數 '), ('m', omath(mr('y = '), sup(mr('x'), mr('2')), mr(' + a'))), ('t', ' 的圖象關於y軸對稱；')], ind=200),
    para([('t', '(2) 所有的無理數，平方後都是無理數。')], ind=200),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '6．寫出下列命題的否定，並判斷原命題與否定命題的真假：')]),
    para([('t', '命題：'), ('m', omath(mr('∃x ∈ Z, '), sup(mr('x'), mr('2')), mr(' = 2'))), ('t', '（存在一個整數，其平方等於2）')]),
] + write_lines(4)))

# ---------------- 練習C ★★★ ----------------
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(problem_box([
    para([('t', '7．已知命題 p：「'), ('m', omath(mr('∀x ∈ R, '), sup(mr('x'), mr('2')), mr(' − 2x + m ≥ 0'))),
          ('t', '」為真命題，求m的取值範圍。（提示：先把 '), ('m', omath(sup(mr('x'), mr('2')), mr(' − 2x + m'))),
          ('t', ' 配方成 (x−1)² + (m−1) 的形式）')]),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '8．請你自己寫出一個全稱量詞命題和一個存在量詞命題（各一個），並分別判斷真假。')]),
] + write_lines(4)))

P.append(problem_box([
    para([('t', '9．命題「'), ('m', omath(mr('∀x ∈ M, p(x)'))), ('t', '」為假命題，那麼「'), ('m', omath(mr('∃x ∈ M, ¬p(x)'))),
          ('t', '」是否一定為真？請說明理由。')]),
] + write_lines(4)))

P.append(pagebreak())

# ---------------- 教師用參考答案 ----------------
P.append(heading('教師用參考答案'))
P.append(para([('t', '1．(1) 全稱　(2) 存在　(3) 全稱')]))
P.append(para([('t', '2．對「所有的」實數x，|x|都「大於等於」0。')]))
P.append(para([('t', '3．真（正方形一定滿足四邊形的定義）')]))
P.append(para([('t', '4．(1) '), ('m', omath(mr('∀x ∈ R, '), sup(mr('x'), mr('2')), mr(' ≥ 0'))), ('t', '，真命題（任何實數平方都不小於0）')]))
P.append(para([('t', '　(2) '), ('m', omath(mr('∃x ∈ Z, 2x + 1 = 0'))), ('t', '，假命題（解得x=−0.5，不是整數）')]))
P.append(para([('t', '5．(1) 真（不論a為何值，二次函數y=x²+a的圖象都關於y軸對稱）')]))
P.append(para([('t', '　(2) 假（舉反例：√2是無理數，但(√2)²=2是有理數）')]))
P.append(para([('t', '6．原命題是假命題（沒有整數的平方等於2，1²=1、2²=4之間沒有整數）。否定命題：'),
               ('m', omath(mr('∀x ∈ Z, '), sup(mr('x'), mr('2')), mr(' ≠ 2'))), ('t', '，為真命題。')]))
P.append(para([('t', '7．'), ('m', omath(sup(mr('x'), mr('2')), mr(' − 2x + m = '), sup(mr('(x−1)'), mr('2')), mr(' + (m−1)'))),
               ('t', '。由於 (x−1)² ≥ 0 對所有x恆成立，要使整個式子恆 ≥ 0，只需 m−1 ≥ 0，解得 m ≥ 1。')]))
P.append(para([('t', '8．答案不唯一，例如全稱量詞命題「∀x∈R, x²≥0」為真命題；存在量詞命題「∃x∈R, x+1=0」為真命題（x=−1）。')]))
P.append(para([('t', '9．一定為真。因為一個命題與它的否定命題必定「一真一假」，原命題為假，否定命題就一定為真。')]))

out = build_docx(P, r'C:\Users\KongChiLok\notebookLM\新任務2\output\練習_全稱量詞與存在量詞.docx',
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
