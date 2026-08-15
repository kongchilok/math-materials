# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *
from omml_docx import _PAGE_CONTENT_WIDTH

SUBJECT = '高一數學'
UNIT = '充分條件與必要條件'
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
P.append(para([('t', '1．命題：可以判斷真假的陳述句。中學數學中的命題常寫成「若p，則q」的形式，p稱為條件，q稱為結論。')]))
P.append(para([('t', '2．若「若p，則q」為真命題（即p成立可以推出q成立），記作 '),
               ('m', omath(mr('p ⇒ q'))), ('t', '，這時我們說：p是q的充分條件，q是p的必要條件。')]))
P.append(para([('t', '3．若「若p，則q」為假命題（由p不能推出q，可以舉出一個反例），記作 '),
               ('m', omath(mr('p ⇏ q'))), ('t', '，這時p不是q的充分條件，q也不是p的必要條件。')]))
P.append(para([('t', '4．若同時有 '), ('m', omath(mr('p ⇒ q'))), ('t', ' 和 '), ('m', omath(mr('q ⇒ p'))),
               ('t', '，則稱p是q的充要條件，記作 '), ('m', omath(mr('p ⇔ q'))), ('t', '。')]))
P.append(para([('t', '5．圖解：若p對應的x所成的集合是P，q對應的x所成的集合是Q，那麼 p⇒q 恰好對應 P⊆Q（回顧1.2節子集的概念）。')]))
P.append(image_para(f'{SVG_DIR}/implication.png', width_cm=8.5, caption='圖1：p⇒q 對應 P⊆Q'))

P.append(heading('二、範例'))
P.append(para([('t', '題目：判斷「x = 2」是否為「'), ('m', omath(sup(mr('x'), mr('2')), mr(' = 4'))), ('t', '」的充分條件？是否為必要條件？')]))
P.append(worked_example_box([
    para([('t', '① 理解題意：p：「x = 2」，q：「'), ('m', omath(sup(mr('x'), mr('2')), mr(' = 4'))), ('t', '」。')]),
    para([('t', '② 檢驗 p⇒q：x = 2 時，'), ('m', omath(sup(mr('x'), mr('2')), mr(' = 4'))), ('t', ' 成立，所以 p⇒q 為真，p是q的充分條件。')]),
    para([('t', '③ 檢驗 q⇒p：'), ('m', omath(sup(mr('x'), mr('2')), mr(' = 4'))), ('t', ' 時，x = 2 或 x = −2，舉反例：x = −2 時 '),
          ('m', omath(sup(mr('x'), mr('2')), mr(' = 4'))), ('t', ' 成立但 x ≠ 2，所以 q⇏p，p不是q的必要條件。')]),
    para([('t', '④ 下結論：p是q的充分不必要條件。')]),
]))

P.append(para([('t', '接下來請拿《充分條件與必要條件課堂練習》，依這套框架完成練習A、B、C。')]))

out = build_docx(P, r'C:\Users\KongChiLok\notebookLM\新任務2\output\講義_充分條件與必要條件.docx',
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
