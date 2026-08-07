# -*- coding: utf-8 -*-
"""講義_函數的表示方法與分段函數_高一數學.docx 產生腳本。
主題：函數的三種表示法（解析法／列表法／圖象法）＋分段函數的概念（人教A版必修一 3.1節後半+3.4節）。
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *
from omml_docx import _PAGE_CONTENT_WIDTH

SUBJECT = '高一數學'
UNIT = '函數的表示方法與分段函數'
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(OUT_DIR), '_assets')


def worked_example_box(paragraphs):
    """灰底＋左側粗條的「範例」框，可放多段落（shaded_box 只吃單段，多步驟示範要用這個）。"""
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


def data_table(headers, rows):
    """簡單多欄資料表（列表法用）：首列表頭灰底粗體，其餘置中，細框線。"""
    n = len(headers)
    col_w = _PAGE_CONTENT_WIDTH // n

    def cell(text, bold=False, shd=None):
        shd_xml = f'<w:shd w:val="clear" w:color="auto" w:fill="{shd}"/>' if shd else ''
        tcpr = (f'<w:tcPr><w:tcW w:w="{col_w}" w:type="dxa"/>{shd_xml}'
                '<w:tcMar><w:top w:w="60" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
                '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tcMar>'
                '<w:vAlign w:val="center"/></w:tcPr>')
        p = para(str(text), bold=bold, sz=BODY_SZ, jc='center', spacing=False)
        return f'<w:tc>{tcpr}{p}</w:tc>'

    border = (
        '<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
    )
    tbl = (f'<w:tbl><w:tblPr><w:tblW w:w="{_PAGE_CONTENT_WIDTH}" w:type="dxa"/>'
           f'<w:tblBorders>{border}</w:tblBorders><w:tblLayout w:type="fixed"/></w:tblPr>'
           f'<w:tblGrid>{"".join(f"<w:gridCol w:w=" + chr(34) + str(col_w) + chr(34) + "/>" for _ in range(n))}</w:tblGrid>')
    tbl += '<w:tr><w:trPr><w:cantSplit/></w:trPr>' + ''.join(cell(h, bold=True, shd=GREY_FILL) for h in headers) + '</w:tr>'
    for row in rows:
        tbl += '<w:tr><w:trPr><w:cantSplit/></w:trPr>' + ''.join(cell(v) for v in row) + '</w:tr>'
    tbl += '</w:tbl>'
    return tbl + blank()


P = []
P.append(masthead(SUBJECT, UNIT, '課堂講義'))
P.append(student_info_row())

# ================= 情境引入：三種表示法 =================
P.append(heading('情境：文具店影印收費'))
P.append(para('文具店影印每張收 0.5 元，影印 x 張（x 為正整數）要付 y 元。同一件事，可以用三種方式表示：'))

P.append(shaded_box('①解析法（用式子表示）：{y=0.5x}　（x 為正整數）'))
P.append(para('②列表法（用表格表示）：把幾個具體的 x、y 值列成表格，一眼看到對應關係：'))
P.append(data_table(
    ['x（張）', '1', '2', '3', '4', '5'],
    [['y（元）', '0.5', '1', '1.5', '2', '2.5']],
))
P.append(para('③圖象法（用圖形表示）：把 (1,0.5)(2,1)(3,1.5)(4,2)(5,2.5) 這些點描在坐標平面上。'
              '因為 x 只能取正整數，圖象是一顆一顆分開的點，不連成直線——這說明「定義域」會影響圖象的樣子。'))
P.append(para('三種表示法其實是同一個函數的不同「面孔」，互相對應、可以互相轉換，選哪一種只是看哪一種最方便。'))

# ================= 一、分段函數的概念 =================
P.append(heading('一、分段函數的概念'))
P.append(para('想一想函數 {y=|x|}（x 的絕對值）。你已經知道：正數的絕對值是它自己，負數的絕對值是它的相反數，即：'))
P.append(para('　•  當 x≥0 時，{y=x}'))
P.append(para('　•  當 x<0 時，{y=-x}'))
P.append(para('同一個函數 {y=|x|}，卻要分成兩種情況、用兩條不同的式子才能寫清楚——'
              '像這樣，把定義域分成幾段，每一段各自用不同解析式表示的函數，就稱為分段函數。'
              '下圖是 {y=|x|} 的圖象，由兩條「射線」拼接而成 V 字形：'))
P.append(image_para(os.path.join(ASSETS, 'v_shape_graph.png'), width_cm=6.5,
                     caption='圖：y=|x| 的圖象——x≥0 是向右上的射線，x<0 是向左上的射線'))
P.append(para('分段函數在生活中很常見，例如：的士跳錶收費、個人所得稅、公車票價——'
              '「不同範圍用不同規則計算」，正是分段函數的實際應用。'))

# ================= 二、範例（四步驟框架） =================
P.append(heading('二、範例：停車場收費（四步驟框架）'))
P.append(para('某停車場的收費方案，以泊車時間 t（小時）計算，收費 y（元）如下：'))
P.append(para('　•  首 1 小時（含）：免費，即 {0≤t≤1} 時，{y=0}'))
P.append(para('　•  超過 1 小時至 3 小時（含）的部分：每小時 10 元，即 {1<t≤3} 時，{y=10(t-1)}'))
P.append(para('　•  超過 3 小時的部分：每小時 15 元，即 {t>3} 時，{y=20+15(t-3)}'))
P.append(para('題目：小明泊車 5 小時，需要付停車費多少元？'))
P.append(worked_example_box([
    para([('t', '①判斷 t=5 落在哪一段：因為 5>3，所以屬於第三段（')]
         + text_to_segments('{t>3}') + [('t', '）；')]),
    para([('t', '②選取對應公式：')] + text_to_segments('{y=20+15(t-3)}')),
    para([('t', '③代入計算：')] + text_to_segments('{y=20+15(5-3)=20+15×2=20+30=50}')),
    para([('t', '④檢查結果是否合理：首 1 小時免費；第 1～3 小時（共 2 小時）每小時 10 元，'
                '合共 20 元；第 3～5 小時（共 2 小時）每小時 15 元，合共 30 元；20+30=50，'
                '與直接代入的結果一致，答案合理。')]),
    para([('t', '結論：小明需要付 ')] + text_to_segments('{50}') + [('t', ' 元。')]),
]))

P.append(para('接下來請拿《函數的表示方法與分段函數課堂練習》，依這套「判斷屬於哪一段→代入對應公式→計算→檢查」'
              '的框架完成練習A、B、C。'))

out = build_docx(P, os.path.join(OUT_DIR, '講義_函數的表示方法與分段函數_高一數學.docx'),
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
