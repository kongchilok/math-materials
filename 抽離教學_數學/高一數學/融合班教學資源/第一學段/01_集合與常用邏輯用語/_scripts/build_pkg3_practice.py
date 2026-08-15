# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

SUBJECT = '高一數學'
UNIT = '充分條件與必要條件'

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(para([('t', '提示：忘記怎麼做可以先回頭看《充分條件與必要條件課堂講義》的範例四步驟。')]))

# ---------------- 練習A ★☆☆ ----------------
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(problem_box([
    para([('t', '1．已知 p：「四邊形是正方形」，q：「四邊形是矩形」。判斷 p⇒q 是否成立？')]),
    para([('t', '成立（　）　不成立（　）')], ind=200),
    para([('t', '若成立，p是q的什麼條件？＿＿＿＿＿＿條件')]),
] + write_lines(2)))

P.append(problem_box([
    para([('t', '2．已知 p：「a = 3」，q：「'), ('m', omath(sup(mr('a'), mr('2')), mr(' = 9'))), ('t', '」。請完成下列判斷：')]),
    para([('t', 'p⇒q？　成立（　）　不成立（　）')], ind=200),
    para([('t', 'q⇒p？　成立（　）　不成立（　）（提示：a = −3 時 a²=9 但 a ≠ 3）')], ind=200),
    para([('t', '所以p是q的＿＿＿＿＿＿條件。')]),
] + write_lines(1)))

P.append(problem_box([
    para([('t', '3．判斷下列說法是否正確，正確打✓，錯誤打✗。')]),
    para([('t', '(1) 若p是q的充分條件，則q一定是p的必要條件。　（　）')], ind=200),
    para([('t', '(2) 若p⇒q為假，則p一定不是q的充分條件。　（　）')], ind=200),
] + write_lines(1)))

# ---------------- 練習B ★★☆ ----------------
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(problem_box([
    para([('t', '4．判斷下列命題中，p是否為q的充分條件：')]),
    para([('t', '(1) 若兩個三角形的三邊成比例，則這兩個三角形相似；')], ind=200),
    para([('t', '(2) 若 a = b，則 '), ('m', omath(sup(mr('a'), mr('2')), mr(' = '), sup(mr('b'), mr('2')))), ('t', '；')], ind=200),
    para([('t', '(3) 若 x、y 為無理數，則 x + y 為無理數。')], ind=200),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '5．判斷「a>0 且 b>0」是「a+b>0」的什麼條件？請說明理由。')]),
] + write_lines(4)))

P.append(problem_box([
    para([('t', '6．判斷「四邊形的對角線互相垂直」是「四邊形是菱形」的什麼條件？請說明理由。')]),
] + write_lines(4)))

# ---------------- 練習C ★★★ ----------------
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(problem_box([
    para([('t', '7．已知 p：「x∈A」，q：「x∈B」，其中 A⊆B。請用集合包含關係說明為什麼 p 是 q 的充分條件。')]),
] + write_lines(4)))

P.append(problem_box([
    para([('t', '8．請你自己寫出一個「若p，則q」形式的真命題，並判斷 p 是 q 的充分、必要或充要條件，說明理由。')]),
] + write_lines(4)))

P.append(problem_box([
    para([('t', '9．已知 p 是 q 的必要不充分條件，且 q 是 r 的充要條件。請問 p 與 r 之間有什麼關係？請舉一個具體例子說明。')]),
] + write_lines(5)))

P.append(pagebreak())

# ---------------- 教師用參考答案 ----------------
P.append(heading('教師用參考答案'))
P.append(para([('t', '1．成立。p是q的充分條件（正方形一定是矩形）。')]))
P.append(para([('t', '2．p⇒q成立；q⇒p不成立（a=−3時a²=9但a≠3）。所以p是q的充分不必要條件。')]))
P.append(para([('t', '3．(1) ✓　(2) ✓')]))
P.append(para([('t', '4．(1) 是（三邊成比例是三角形相似的判定定理，p⇒q為真）(2) 是（等式性質，a=b可推出a²=b²）(3) 不是（舉反例：x=√2，y=−√2，x+y=0為有理數，p⇏q）')]))
P.append(para([('t', '5．充分不必要條件。a>0且b>0時a+b>0成立(充分)；但a+b>0不代表a、b都>0，例如a=3,b=−1時a+b=2>0但b<0(不必要)。')]))
P.append(para([('t', '6．必要不充分條件。菱形的對角線一定互相垂直(必要)；但對角線互相垂直的四邊形不一定是菱形，例如某些風箏形(不充分)。')]))
P.append(para([('t', '7．因為A⊆B，A中每個元素都在B中，所以只要x∈A，就一定有x∈B，即p成立能推出q成立，p⇒q為真，故p是q的充分條件。')]))
P.append(para([('t', '8．答案不唯一，例如「若x>2，則x>1」，p⇒q為真(x>2一定x>1)，但q⇒p不成立(x=1.5>1但不>2)，所以p是q的充分不必要條件。')]))
P.append(para([('t', '9．p是q的必要不充分條件，即q⇒p（但p⇏q）；q是r的充要條件，即q⇔r。合併可得 r⇒q⇒p，所以 r⇒p，即p是r的必要條件。例如：設q「x是4的倍數」，r「x=4k，k為整數」（與q等價），p「x是偶數」。則q⇒p成立但p⇏q（如x=2是偶數但不是4的倍數），且q⇔r。驗證：r成立時x是4的倍數，一定是偶數，即r⇒p成立，與推論相符。')]))

out = build_docx(P, r'C:\Users\KongChiLok\notebookLM\新任務2\output\練習_充分條件與必要條件.docx',
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
