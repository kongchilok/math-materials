# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

SUBJECT = '高一數學'
UNIT = '集合的基本運算'
SVG_DIR = r"C:\Users\KongChiLok\notebookLM\新任務2\output\svgs"

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(para([('t', '提示：忘記怎麼做可以先回頭看《集合的基本運算課堂講義》的範例四步驟。')]))

# ---------------- 練習A ★☆☆ ----------------
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(problem_box([
    para([('t', '1．已知 A = {1, 2, 3}，B = {3, 4, 5}。已經幫你抄好A的元素，請把B獨有的元素接著寫完成 A∪B：')]),
    para([('t', 'A∪B = {1, 2, 3, ____, ____}')]),
] + write_lines(2)))

P.append(problem_box([
    para([('t', '2．已知 A = {2, 4, 6, 8}，B = {4, 8, 12}。求 A∩B。')]),
    para([('t', '提示：交集就是兩個集合「都有」的元素。')], sz=22),
] + write_lines(2)))

P.append(problem_box([
    para([('t', '3．已知 U = {1, 2, 3, 4, 5}，A = {2, 4}。求 '), ('m', omath(sub(mr('∁'), mr('U')), mr('A'))), ('t', '。')]),
    para([('t', '提示：把U中不是A的元素挑出來。')], sz=22),
] + write_lines(2)))

# ---------------- 練習B ★★☆ ----------------
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(problem_box([
    para([('t', '4．設集合 '), ('m', omath(mr('A = {x | −1 < x < 2}'))), ('t', '，'),
          ('m', omath(mr('B = {x | 1 < x < 3}'))), ('t', '，求 A∪B、A∩B。')]),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '5．已知 U = {1, 2, 3, 4, 5}，A = {1, 2, 3}，B = {2, 3, 4}，求 '),
          ('m', omath(mr('('), sub(mr('∁'), mr('U')), mr('A) ∩ B'))), ('t', '。')]),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '6．已知 U = {1, 2, 3, 4, 5}，A = {1, 2, 3}，B = {2, 3, 4}，如下圖，灰色部分（屬於A但不屬於B）表示的集合是什麼？')]),
]))
P.append(image_para(f'{SVG_DIR}/onlyA_notB.png', width_cm=7.5))
P.append(problem_box(write_lines(3)))

# ---------------- 練習C ★★★ ----------------
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(problem_box([
    para([('t', '7．已知 '), ('m', omath(mr('A = {x | x < 1 或 x > 4}'))), ('t', '，'),
          ('m', omath(mr('B = {x | a ≤ x ≤ a + 2}'))),
          ('t', '。若 A∩B = ∅，求 a 的取值範圍。（提示：A∩B=∅表示B必須完全落在[1,4]之內）')]),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '8．請你自己設計兩個用描述法表示的集合 A、B（與不等式有關），使得 '),
          ('m', omath(mr('A ∩ B = {x | 2 < x < 3}'))), ('t', '，並說明你的設計方式。')]),
] + write_lines(4)))

P.append(problem_box([
    para([('t', '9．已知 A∪B = A。這個等式蘊含 A、B 之間有什麼關係？請說明理由，並舉一個具體例子驗證。')]),
] + write_lines(4)))

P.append(pagebreak())

# ---------------- 教師用參考答案 ----------------
P.append(heading('教師用參考答案'))
P.append(para([('t', '1．A∪B = {1, 2, 3, 4, 5}')]))
P.append(para([('t', '2．A∩B = {4, 8}')]))
P.append(para([('t', '3．U中不屬於A(={2,4})的元素為1,3,5，所以 ∁ᵤA = {1, 3, 5}')]))
P.append(para([('t', '4．A∪B = {x | −1 < x < 3}；A∩B = {x | 1 < x < 2}')]))
P.append(para([('t', '5．∁ᵤA = {4, 5}，再與B={2,3,4}取交集，得 (∁ᵤA)∩B = {4}')]))
P.append(para([('t', '6．圖中陰影是屬於A但不屬於B的部分：A中元素{1,2,3}扣掉同時在B中的{2,3}，得 {1}')]))
P.append(para([('t', '7．A∩B=∅表示B={x|a≤x≤a+2}中所有元素都不在A中，即都落在[1,4]內，所以需要 a≥1 且 a+2≤4，解得 1≤a≤2')]))
P.append(para([('t', '8．答案不唯一，例如 A={x|x>2}，B={x|x<3}，則 A∩B={x|2<x<3}，恰好符合要求。')]))
P.append(para([('t', '9．A∪B=A 蘊含 B⊆A（B是A的子集）。例如 A={1,2,3}，B={1,2}，A∪B={1,2,3}=A，且確實 B⊆A。')]))

out = build_docx(P, r'C:\Users\KongChiLok\notebookLM\新任務2\output\練習_集合的基本運算.docx',
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
