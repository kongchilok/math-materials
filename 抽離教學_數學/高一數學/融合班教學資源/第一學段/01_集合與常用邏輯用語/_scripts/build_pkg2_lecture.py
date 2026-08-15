# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *
from omml_docx import _PAGE_CONTENT_WIDTH

SUBJECT = '高一數學'
UNIT = '集合的基本運算'
SVG_DIR = r"C:\Users\KongChiLok\notebookLM\新任務2\output\svgs"

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
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、核心概念'))
P.append(para([('t', '1．並集：由所有屬於A或屬於B的元素組成，記作 '),
               ('m', omath(mr('A '), mr(' ∪ '), mr('B'))),
               ('t', '，即 '), ('m', omath(mr('A '), mr(' ∪ '), mr('B = {x | x ∈ A 或 x ∈ B}'))), ('t', '。')]))
P.append(image_para(f'{SVG_DIR}/union.png', width_cm=8.0, caption='圖1：A∪B（灰色部分）'))

P.append(para([('t', '2．交集：由所有既屬於A又屬於B的元素組成，記作 '),
               ('m', omath(mr('A '), mr(' ∩ '), mr('B'))),
               ('t', '，即 '), ('m', omath(mr('A '), mr(' ∩ '), mr('B = {x | x ∈ A 且 x ∈ B}'))), ('t', '。')]))
P.append(image_para(f'{SVG_DIR}/intersection.png', width_cm=8.0, caption='圖2：A∩B（灰色部分）'))

P.append(para([('t', '3．全集與補集：若全集為U，A的補集 '), ('m', omath(sub(mr('∁'), mr('U')), mr('A'))),
               ('t', ' 是U中所有不屬於A的元素組成的集合。')]))
P.append(image_para(f'{SVG_DIR}/complement.png', width_cm=8.0, caption='圖3：∁ᵤA（灰色部分）'))

P.append(para([('t', '4．常用運算性質：'), ('m', omath(mr('A ∪ A = A，A ∪ ∅ = A，A ∩ A = A，A ∩ ∅ = ∅'))), ('t', '；'),
               ('m', omath(mr('A ∪ ('), sub(mr('∁'), mr('U')), mr('A) = U，A ∩ ('), sub(mr('∁'), mr('U')), mr('A) = ∅'))), ('t', '。')]))

P.append(heading('二、範例'))
P.append(para([('t', '題目：已知全集 U = {1,2,3,4,5,6}，A = {1,2,3}，B = {2,3,4}，求 A∪B、A∩B、∁ᵤ(A∪B)。')]))
P.append(worked_example_box([
    para([('t', '① 理解題意：先寫出U、A、B的元素，方便逐一核對。')]),
    para([('t', '② 求A∪B：把A、B的元素合併，重複只算一次 → A∪B = {1, 2, 3, 4}。')]),
    para([('t', '③ 求A∩B：找出A、B共同的元素 → A∩B = {2, 3}。')]),
    para([('t', '④ 求∁ᵤ(A∪B)：從U中去掉A∪B的元素 → U − {1,2,3,4} = {5, 6}。')]),
]))

P.append(para([('t', '接下來請拿《集合的基本運算課堂練習》，依這套框架完成練習A、B、C。')]))

out = build_docx(P, r'C:\Users\KongChiLok\notebookLM\新任務2\output\講義_集合的基本運算.docx',
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
