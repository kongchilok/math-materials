# -*- coding: utf-8 -*-
"""練習_函數的表示方法與分段函數_高一數學.docx 產生腳本。
三層次（A初階/B中階/C高階）同源同概念：分段函數代入求值＋分段函數應用建模＋表示法互換。
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *
from omml_docx import _PAGE_CONTENT_WIDTH

SUBJECT = '高一數學'
UNIT = '函數的表示方法與分段函數'
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


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
P.append(masthead(SUBJECT, UNIT, '課堂練習'))
P.append(student_info_row())
P.append(para('請先複習《函數的表示方法與分段函數課堂講義》的範例，再依同一套'
              '「①判斷屬於哪一段→②代入對應公式→③計算→④檢查」的框架完成以下練習。'))

# ================= 練習A（初階） =================
P.append(heading(f'一、練習A（{star_label(1)}）'))

P.append(para('已知分段函數：當 {x<0} 時，{f(x)=x+3}；當 {x≥0} 時，{f(x)=x^2-1}。'
              '請跟著提示的步驟，求下列函數值：'))

P.append(para('1．求 f(-2)：'))
P.append(problem_box(
    [para('(1) x=-2 是 {x<0} 還是 {x≥0}？屬於第＿段：')] + write_lines(2)
    + [para('(2) 代入對應的公式，f(-2)=＿＿＿：')] + write_lines(2)
))
P.append(shaded_box('提示卡：先比較 x 和 0 的大小，決定用哪一行的公式，才可以代入計算。'))

P.append(para('2．求 f(0)：'))
P.append(problem_box(
    [para('(1) x=0 是 {x<0} 還是 {x≥0}？屬於第＿段：')] + write_lines(2)
    + [para('(2) 代入對應的公式，f(0)=＿＿＿：')] + write_lines(2)
))
P.append(shaded_box('提示卡：x=0 符合「{x≥0}」這個條件（0 本身也算在內），所以用第二行的公式。'))

P.append(para('3．求 f(4)：'))
P.append(problem_box(
    [para('(1) x=4 是 {x<0} 還是 {x≥0}？屬於第＿段：')] + write_lines(2)
    + [para('(2) 代入對應的公式，f(4)=＿＿＿：')] + write_lines(2)
))
P.append(shaded_box('提示卡：判斷完屬於哪一段之後，記得把整條式子的 x 都換成同一個數值。'))

P.append(para('4．求 f(-6)：'))
P.append(problem_box(
    [para('(1) x=-6 是 {x<0} 還是 {x≥0}？屬於第＿段：')] + write_lines(2)
    + [para('(2) 代入對應的公式，f(-6)=＿＿＿：')] + write_lines(2)
))
P.append(shaded_box('提示卡：負數一定符合「{x<0}」，用第一行的公式。'))

# ================= 練習B（中階） =================
P.append(heading(f'二、練習B（{star_label(2)}）'))

P.append(para('5．某的士（計程車）車資按行駛距離 x（公里）分段計算：首 2 公里（含）收 24 元；'
              '超過 2 公里至 10 公里（含）的部分，每公里加收 6 元；超過 10 公里的部分，每公里加收 9 元。'))
P.append(problem_box(
    [para('(1) 請寫出車資 y（元）關於 x 的完整解析式（分三段列出）：')] + write_lines(5)
    + [para('(2) 求行駛 6 公里的車資：')] + write_lines(3)
    + [para('(3) 求行駛 15 公里的車資：')] + write_lines(3)
))
P.append(shaded_box('提示卡：先確定每一段的 x 範圍界線（2 公里、10 公里），再分別寫出「起步價＋超出部分×單價」的算式，'
                     '後面幾段要在前一段的基礎上累加。'))

P.append(para('6．已知 {f(x)=2x-1}。這一題的「x」不是一個數字，而是一段算式——把它當成一個整體代入就可以了：'))
P.append(problem_box(
    [para('(1) 求 f(a+1)（用 a 表示，結果化簡）：')] + write_lines(3)
    + [para('(2) 求 f(3b)（用 b 表示，結果化簡）：')] + write_lines(3)
))
P.append(shaded_box('提示卡：把 f(x)=2x-1 裡面每一個 x，都換成題目給的那段算式（a+1 或 3b），再展開化簡。'))

P.append(para('7．某快遞公司按包裹重量 x（公斤）分段收費，收費表（列表法）如下：'))
P.append(data_table(
    ['包裹重量 x（公斤）', '收費 y（元）'],
    [['0<x≤1', '20'], ['1<x≤3', '35'], ['3<x≤5', '50']],
))
P.append(problem_box(
    [para('根據上表，把「列表法」改寫成「解析法」——寫出 y 關於 x 的分段函數解析式：')] + write_lines(4)
))
P.append(shaded_box('提示卡：表格裡每一行就是分段函數的「一段」，把每一段的 x 範圍和對應的 y 值直接抄成一行解析式。'))

# ================= 練習C（高階） =================
P.append(heading(f'三、練習C（{star_label(3)}）'))

P.append(para('8．已知分段函數：當 {x≥0} 時，{f(x)=3x-1}；當 {x<0} 時，{f(x)=x^2+2}。求 f[f(-1)]：'))
P.append(problem_box(
    [para('(1) 先算內層 f(-1)：判斷 x=-1 屬於哪一段，代入對應公式，得 f(-1)=＿＿＿：')]
    + write_lines(3)
    + [para('(2) 把①的結果當作新的 x，判斷這個值屬於哪一段，代入對應公式，得最終答案：')]
    + write_lines(3)
))
P.append(shaded_box('提示卡：f[f(-1)] 要「由內到外」算兩次——先算出 f(-1) 是多少，再把這個結果當作新的輸入值，'
                     '重新判斷一次它屬於哪一段，才能代入第二次。'))

P.append(para('9．某住宅每月用電量 x（度）電費 y（元）分段收費：首 100 度（含）每度 1 元；'
              '超過 100 度至 300 度（含）的部分每度 1.5 元；超過 300 度至 600 度（含）的部分每度 2 元；'
              '超過 600 度的部分每度 2.5 元。'))
P.append(problem_box(
    [para('(1) 請寫出電費 y（元）關於用電量 x（度）的完整解析式（分四段列出）：')] + write_lines(6)
    + [para('(2) 求用電量 450 度的電費：')] + write_lines(3)
    + [para('(3) 求用電量 700 度的電費：')] + write_lines(3)
))
P.append(shaded_box('提示卡：四段的界線是 100、300、600 度；每一段都要在前面所有段的基礎上累加，'
                     '寫完解析式後，先檢查相鄰兩段在交界處（例如 x=100）算出來的電費是否銜接一致，再代入計算。'))

P.append(para('10．請你自己設計一個「三段式」收費方案（例如：停車場、的士、快遞、電話費……任何情境皆可），'
              '寫出完整的分段函數解析式：'))
P.append(problem_box(
    [para('你的情境與收費規則說明：')] + write_lines(3)
    + [para('你的解析式（分三段列出）：')] + write_lines(4),
    trailing_blank=False,
))
P.append(shaded_box('提示卡：自我檢查清單——①每一段的 x 範圍有沒有清楚界定，沒有重疊也沒有漏掉？'
                     '②相鄰兩段在交界處是否合理銜接（不會忽然變便宜或跳號）？③每一段的解析式有沒有寫清楚？'))

# ================= 參考答案與解析 =================
P.append(heading('參考答案與解析', page_break_before=True))

P.append(heading('練習A', sz=BODY_SZ))
P.append(para('1．(1) x=-2<0，屬於第一段。(2) {f(-2)=-2+3=1}。'))
P.append(para('2．(1) x=0≥0，屬於第二段（等於 0 也符合「≥0」）。(2) {f(0)=0^2-1=-1}。'))
P.append(para('3．(1) x=4≥0，屬於第二段。(2) {f(4)=4^2-1=16-1=15}。'))
P.append(para('4．(1) x=-6<0，屬於第一段。(2) {f(-6)=-6+3=-3}。'))

P.append(heading('練習B', sz=BODY_SZ))
P.append(para('5．(1) 解析式：當 {0<x≤2} 時，{y=24}；當 {2<x≤10} 時，{y=24+6(x-2)}；'
              '當 {x>10} 時，{y=24+6×8+9(x-10)=72+9(x-10)}。'
              '(2) x=6 屬於第二段：{y=24+6(6-2)=24+24=48}，車資 48 元。'
              '(3) x=15 屬於第三段：{y=72+9(15-10)=72+45=117}，車資 117 元。'))
P.append(para('6．(1) {f(a+1)=2(a+1)-1=2a+2-1=2a+1}。(2) {f(3b)=2(3b)-1=6b-1}。'))
P.append(para('7．解析式：當 {0<x≤1} 時，{y=20}；當 {1<x≤3} 時，{y=35}；當 {3<x≤5} 時，{y=50}。'))

P.append(heading('練習C', sz=BODY_SZ))
P.append(para('8．(1) x=-1<0，屬於第一段：{f(-1)=(-1)^2+2=1+2=3}。'
              '(2) 把 3 當作新的 x：3≥0，屬於第二段：{f(3)=3×3-1=9-1=8}。所以 {f[f(-1)]=8}。'))
P.append(para('9．(1) 解析式：當 {0<x≤100} 時，{y=x}；當 {100<x≤300} 時，{y=100+1.5(x-100)}；'
              '當 {300<x≤600} 時，{y=400+2(x-300)}（因為 100+1.5×200=400）；'
              '當 {x>600} 時，{y=1000+2.5(x-600)}（因為 400+2×300=1000）。'
              '(2) x=450 屬於第三段：{y=400+2(450-300)=400+300=700}，電費 700 元。'
              '(3) x=700 屬於第四段：{y=1000+2.5(700-600)=1000+250=1250}，電費 1250 元。'))
P.append(para('10．本題無固定答案。教師驗收標準：情境合理、三段的 x 範圍清楚不重疊、'
              '相鄰兩段在交界處銜接一致（不會出現交界處收費忽然變便宜的不合理情況）、'
              '每一段的解析式都完整寫出。'))

out = build_docx(P, os.path.join(OUT_DIR, '練習_函數的表示方法與分段函數_高一數學.docx'),
                  footer_text=f'{SUBJECT}．{UNIT}')
print(out)
