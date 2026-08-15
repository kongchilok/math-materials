# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *
from omml_docx import _PAGE_CONTENT_WIDTH

SUBJECT = '高一數學'
UNIT = '全稱量詞與存在量詞'

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
P.append(para([('t', '1．全稱量詞：「所有的」「任意一個」「每一個」等詞，符號記作 ∀。含有全稱量詞的命題叫全稱量詞命題，一般形式為：'),
               ('m', omath(mr('∀x ∈ M, p(x)'))), ('t', '。')]))
P.append(para([('t', '2．存在量詞：「存在一個」「至少有一個」「有些」「有一個」等詞，符號記作 ∃。含有存在量詞的命題叫存在量詞命題，一般形式為：'),
               ('m', omath(mr('∃x ∈ M, p(x)'))), ('t', '。')]))
P.append(para([('t', '3．判斷全稱量詞命題真假：M中每一個x都要驗證p(x)成立，才是真命題；只要找到一個反例（某個x₀使p(x₀)不成立），就是假命題（舉反例法）。')]))
P.append(para([('t', '4．判斷存在量詞命題真假：只要在M中找到一個x使p(x)成立，就是真命題；M中每一個元素都使p(x)不成立，才是假命題。')]))
P.append(para([('t', '5．命題的否定：全稱量詞命題 '), ('m', omath(mr('∀x ∈ M, p(x)'))), ('t', ' 的否定是存在量詞命題 '),
               ('m', omath(mr('∃x ∈ M, ¬p(x)'))), ('t', '；存在量詞命題 '), ('m', omath(mr('∃x ∈ M, p(x)'))),
               ('t', ' 的否定是全稱量詞命題 '), ('m', omath(mr('∀x ∈ M, ¬p(x)'))), ('t', '（換量詞、否定結論）。')]))

P.append(heading('二、範例'))
P.append(para([('t', '題目：判斷全稱量詞命題「所有的素數都是奇數」的真假，並寫出它的否定。')]))
P.append(worked_example_box([
    para([('t', '① 理解題意：M是「所有素數」，p(x)是「x是奇數」，要判斷 ∀x∈M, p(x) 的真假。')]),
    para([('t', '② 舉反例檢驗：2是素數，但2不是奇數，找到反例。')]),
    para([('t', '③ 下結論：原命題為假命題（因為找到了反例2）。')]),
    para([('t', '④ 寫出否定：原命題的否定是存在量詞命題「存在一個素數不是奇數」，且此否定命題為真命題（2就是這樣的例子）。')]),
]))

P.append(para([('t', '接下來請拿《全稱量詞與存在量詞課堂練習》，依這套框架完成練習A、B、C。')]))

out = build_docx(P, r'C:\Users\KongChiLok\notebookLM\新任務2\output\講義_全稱量詞與存在量詞.docx',
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
