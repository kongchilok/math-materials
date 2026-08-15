# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *
from omml_docx import _PAGE_CONTENT_WIDTH

SUBJECT = '高一數學'
UNIT = '集合的概念與基本關係'
SVG_DIR = r"C:\Users\KongChiLok\notebookLM\新任務2\output\svgs"

def worked_example_box(paragraphs):
    """Multi-paragraph grey callout box (house-style 範例/提示卡 fill, no colour)."""
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
P.append(para([('t', '1．集合的三要素：確定性（元素是或不是，必須清楚）、互異性（同一集合中元素不重複）、無序性（元素排列先後不影響集合本身）。')]))
P.append(para([('t', '2．元素與集合的關係：若 a 是集合 A 的元素，記作 '),
               ('m', omath(mr('a'), mr(' ∈ '), mr('A'))), ('t', '（讀作「屬於」）；若不是，記作 '),
               ('m', omath(mr('a'), mr(' ∉ '), mr('A'))), ('t', '。')]))
P.append(para([('t', '3．常用數集符號：N（自然數集，含0）、N+ 或 N*（正整數集）、Z（整數集）、Q（有理數集）、R（實數集）。')]))
P.append(para([('t', '4．集合的表示法：')]))
P.append(para([('t', '　列舉法：把元素一一列出，例如 '), ('m', omath(mr('{1, 2, 3}'))), ('t', '。')], ind=200))
P.append(para([('t', '　描述法：用「元素所滿足的條件」描述，例如 '), ('m', omath(mr('{x '), mr(' ∈ '), mr('R | x > 1}'))), ('t', '。')], ind=200))
P.append(para([('t', '5．集合間的基本關係：')]))
P.append(para([('t', '　子集 '), ('m', omath(mr('A '), mr(' ⊆ '), mr('B'))), ('t', '：A中每一個元素都屬於B。')], ind=200))
P.append(para([('t', '　真子集 '), ('m', omath(mr('A '), mr(' ⊊ '), mr('B'))), ('t', '：'),
               ('m', omath(mr('A '), mr(' ⊆ '), mr('B'))), ('t', ' 且 A ≠ B（B中至少有一個元素不在A中）。')], ind=200))
P.append(para([('t', '　相等 A = B：'), ('m', omath(mr('A '), mr(' ⊆ '), mr('B'))), ('t', ' 且 '),
               ('m', omath(mr('B '), mr(' ⊆ '), mr('A'))), ('t', '。')], ind=200))
P.append(para([('t', '　規定：空集 ∅ 是任何集合的子集。')], ind=200))
P.append(image_para(f'{SVG_DIR}/subset.png', width_cm=8.5, caption='圖1：A⊆B 的 Venn 圖表示——B的圓完全包住A的圓'))

P.append(heading('二、範例'))
P.append(para([('t', '題目：已知集合 '), ('m', omath(mr('A = {x '), mr(' ∈ '), mr('N | x < 4}'))),
               ('t', '，B = {0, 1, 2, 3, 4}，判斷 A 與 B 的關係，並用列舉法表示 A。')]))
P.append(worked_example_box([
    para([('t', '① 理解題意：A是「小於4的自然數」全體，先確定範圍。')]),
    para([('t', '② 列舉A：A = {0, 1, 2, 3}。')]),
    para([('t', '③ 逐一比對：A中每個元素（0,1,2,3）都在B中；但B多了元素4，不在A中。')]),
    para([('t', '④ 下結論：A⊆B 且 A≠B，所以 A⊊B（A是B的真子集）。')]),
]))

P.append(para([('t', '接下來請拿《集合的概念與基本關係課堂練習》，依這套框架完成練習A、B、C。')]))

out = build_docx(P, r'C:\Users\KongChiLok\notebookLM\新任務2\output\講義_集合的概念與基本關係.docx',
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
