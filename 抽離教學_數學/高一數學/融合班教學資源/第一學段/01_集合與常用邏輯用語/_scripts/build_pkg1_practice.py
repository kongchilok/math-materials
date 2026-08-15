# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *
from omml_docx import _PAGE_CONTENT_WIDTH

SUBJECT = '高一數學'
UNIT = '集合的概念與基本關係'

def worked_example_box(paragraphs):
    tbl = (
        '<w:tbl><w:tblPr>'
        f'<w:tblW w:w="{_PAGE_CONTENT_WIDTH}" w:type="dxa"/>'
        '<w:tblBorders>'
        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{RULE_GREY}"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{GREY_BORDER}"/>'
        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{RULE_GREY}"/>'
        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="{RULE_GREY}"/>'
        '</w:tblBorders>'
        '<w:tblLayout w:type="fixed"/></w:tblPr>'
        f'<w:tblGrid><w:gridCol w:w="{_PAGE_CONTENT_WIDTH}"/></w:tblGrid>'
        '<w:tr><w:trPr><w:cantSplit/></w:trPr><w:tc><w:tcPr>'
        f'<w:tcW w:w="{_PAGE_CONTENT_WIDTH}" w:type="dxa"/>'
        f'<w:shd w:val="clear" w:color="auto" w:fill="{GREY_FILL}"/>'
        '<w:tcMar><w:top w:w="80" w:type="dxa"/><w:left w:w="160" w:type="dxa"/>'
        '<w:bottom w:w="80" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>'
        '</w:tcPr>' + ''.join(paragraphs) + '</w:tc></w:tr></w:tbl>'
    )
    return tbl + blank()

P = []
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(para([('t', '提示：忘記怎麼做可以先回頭看《集合的概念與基本關係課堂講義》的範例四步驟。')]))

# ---------------- 練習A ★☆☆ ----------------
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(problem_box([
    para([('t', '1．下列哪些敘述「能」組成集合？請在能／不能中打勾。')]),
    para([('t', '(1) 全班身高超過170公分的同學　　　能（　）　不能（　）')], ind=200),
    para([('t', '(2) 很聰明的同學　　　能（　）　不能（　）')], ind=200),
    para([('t', '(3) 1到5之間的偶數　　　能（　）　不能（　）')], ind=200),
] + [shaded_box([('t', '提示：能組成集合的關鍵是「元素確定」——能不能明確判斷「誰在裡面、誰不在」。')])]
  + write_lines(1)))

P.append(problem_box([
    para([('t', '2．集合 '), ('m', omath(mr('{x '), mr(' ∈ '), mr('N+ | x < 5}'))),
          ('t', ' 用列舉法表示為 {1, 2, ____, ____}，請填出缺少的兩個數。')]),
    para([('t', '提示：N+表示正整數（1,2,3,…），由小到大排列。')], sz=22),
] + write_lines(2)))

P.append(problem_box([
    para([('t', '3．判斷下列敘述是否正確，正確打✓，錯誤打✗。')]),
    para([('t', '(1) 3 ∈ {1, 2, 3, 4}　（　）')], ind=200),
    para([('t', '(2) 0 ∈ ∅　（　）')], ind=200),
    para([('t', '(3) {1, 2} ⊆ {1, 2, 3}　（　）')], ind=200),
] + write_lines(1)))

# ---------------- 練習B ★★☆ ----------------
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(problem_box([
    para([('t', '4．用適當的方法（列舉法或描述法）表示下列集合：')]),
    para([('t', '(1) 所有能被3整除的整數；')], ind=200),
    para([('t', '(2) 方程 '), ('m', omath(sup(mr('x'), mr('2')), mr(' − 5x + 6 = 0'))), ('t', ' 的解集。')], ind=200),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '5．已知集合 M = {−2, 0, 2}，N = {x ∈ Z | −3 < x < 3}，判斷 M 與 N 的關係，並說明理由。')]),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '6．寫出集合 {a, b}（a ≠ b）的所有子集，共有幾個？')]),
] + write_lines(3)))

# ---------------- 練習C ★★★ ----------------
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(problem_box([
    para([('t', '7．已知集合 '), ('m', omath(mr('A = {x | '), sup(mr('x'), mr('2')), mr(' − 3x + 2 = 0}'))),
          ('t', '，B = {1, a}。若 A = B，求 a 的值。（先求出A的元素，再比較）')]),
] + write_lines(5)))

P.append(problem_box([
    para([('t', '8．請你自己寫出一個集合 A（元素個數不少於3個），並寫出它的其中兩個「真」子集，說明為什麼它們是A的真子集而不是A本身。')]),
] + write_lines(4)))

P.append(problem_box([
    para([('t', '9．探索規律：集合{1}有2個子集，集合{1,2}有4個子集，集合{1,2,3}有8個子集。')]),
    para([('t', '(1) 猜想：一個有 n 個元素的集合，子集個數共有多少個？')], ind=200),
    para([('t', '(2) 請用集合 {1,2,3,4} 驗證你的猜想（列出所有子集或說明理由）。')], ind=200),
] + write_lines(4)))

P.append(pagebreak())

# ---------------- 教師用參考答案 ----------------
P.append(heading('教師用參考答案'))
P.append(para([('t', '1．(1) 能　(2) 不能（「聰明」標準不確定）　(3) 能')]))
P.append(para([('t', '2．{1, 2, 3, 4}')]))
P.append(para([('t', '3．(1) ✓　(2) ✗（∅沒有任何元素）　(3) ✓')]))
P.append(para([('t', '4．(1) {x ∈ Z | x是3的倍數}　(2) 解 (x−2)(x−3)=0，得 x=2 或 x=3，解集為 {2, 3}')]))
P.append(para([('t', '5．N = {−2, −1, 0, 1, 2}。M中每個元素（−2,0,2）都在N中，但N還有−1、1不在M中，所以 M ⊊ N（M是N的真子集）。')]))
P.append(para([('t', '6．子集共4個：∅、{a}、{b}、{a, b}。')]))
P.append(para([('t', '7．先解 x²−3x+2=0 得 (x−1)(x−2)=0，x=1或2，所以 A={1,2}。由 A=B 得 B={1,2}，比對 B={1,a}，得 a=2。')]))
P.append(para([('t', '8．答案不唯一，能自圓其說即可，例如 A={1,2,3}，真子集 {1}、{1,2} 都是A的真子集，因為它們是A的子集且都不等於A本身。')]))
P.append(para([('t', '9．(1) 猜想：2的n次方個（2ⁿ）。(2) {1,2,3,4}的子集共 2⁴=16 個：∅、{1}、{2}、{3}、{4}、{1,2}、{1,3}、{1,4}、{2,3}、{2,4}、{3,4}、{1,2,3}、{1,2,4}、{1,3,4}、{2,3,4}、{1,2,3,4}，驗證共16個，與猜想相符。')]))

out = build_docx(P, r'C:\Users\KongChiLok\notebookLM\新任務2\output\練習_集合的概念與基本關係.docx',
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
