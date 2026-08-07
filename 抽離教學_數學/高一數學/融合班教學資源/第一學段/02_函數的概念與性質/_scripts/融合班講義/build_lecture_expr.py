# -*- coding: utf-8 -*-
"""講義_函數的表示方法與分段函數_高一數學.docx 產生腳本（2026-08-07 按最新規則重出）。
主題：函數的三種表示法（解析法／列表法／圖象法）＋分段函數的概念（人教A版必修一 3.1 後半 + 3.4）。
教學設計：主 D5 圖文雙軌對照（圖象法直接出圖；y=|x| 逐段「圖上看到什麼→算式上寫成什麼」）
         ＋輔 D2 手順卡（分段函數求值四步驟）＋輔 D12 自我核對清單（練習端，見 build_practice_expr.py）。
版面新規：分段函數一律用 cases() 大括號寫成一條式，不再寫成「當 x≥0 時…」的散文條列。
題目內容與舊版完全相同，只換教學設計與版面。
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *
from omml_docx import _PAGE_CONTENT_WIDTH

SUBJECT = '高一數學'
UNIT = '函數的表示方法與分段函數'
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(OUT_DIR, 'svgs_expr_piecewise')
MEDIA = MediaRegistry()


def img(name, width_cm, caption=None):
    return image_para(os.path.join(ASSETS, name + '.png'), width_cm=width_cm, caption=caption)


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
P.append(para('文具店影印每張收 0.5 元，影印 x 張（x 為正整數）要付 y 元。'
              '同一件事，可以用三種方式表示：'))

P.append(shaded_box('① 解析法（用式子表示）：{y=0.5x}　（x 為正整數）'))
P.append(para('② 列表法（用表格表示）：'))
P.append(data_table(
    ['x（張）', '1', '2', '3', '4', '5'],
    [['y（元）', '0.5', '1', '1.5', '2', '2.5']],
))
P.append(expand_image(
    img('copy_scatter', 12.6,
        caption='圖：x 只取正整數，所以圖象是一顆一顆分開的點，不連成直線——定義域會影響圖象的樣子'),
    MEDIA))
P.append(para('三種表示法是同一個函數的不同「面孔」，可以互相轉換；'
              '選哪一種，只看哪一種最方便。'))

# ================= 一、分段函數的概念（D5 圖文雙軌） =================
P.append(heading('一、分段函數的概念'))
P.append(para('函數 {y=|x|}：正數的絕對值是它自己，負數的絕對值是它的相反數。'
              '同一個函數要分成兩段、用兩條不同的式子才寫得清楚——'
              '把定義域分成幾段、每一段各自用不同解析式表示的函數，就叫分段函數。'))
P.append(dual_track_table([
    (img('abs_right', 7.6),
     [para('當 {x>=0} 時，圖象是向右上的射線，'),
      para('算式寫成　{y=x}')]),
    (img('abs_left', 7.6),
     [para('當 {x<0} 時，圖象是向左上的射線，'),
      para('算式寫成　{y=-x}')]),
    (img('abs_full', 7.6),
     [para('兩段合起來是 V 字形，'),
      para('一條式子寫齊兩段：'),
      para('　{y=cases(x, x>=0; -x, x<0)}')]),
], media=MEDIA))
P.append(shaded_box('分段函數的標準寫法：函數名 ＝ 一個大括號，'
                     '括號內逐行寫「算式，這一行管哪一段 x」——'
                     '一行一段，不要寫成一句一句的文字。'))
P.append(para('分段函數在生活中很常見：的士跳錶收費、個人所得稅、電費——'
              '「不同範圍用不同規則計算」，正是分段函數的應用。'))

# ================= 二、求分段函數的值：四步驟（D2 手順卡） =================
P.append(heading('二、求分段函數的值　四步驟'))
P.append(step_card(
    '分段函數求值　手順卡',
    steps=[
        ('看清楚題目給的 x 是多少，判斷它落在大括號的哪一行。',
         '邊界值（例如 x=0、t=3）要看清楚是「≥」還是「＞」，等號在哪一行就屬於哪一行。'),
        ('把那一行的算式整條抄下來。',
         '只抄一行；抄錯行的話後面全部白做。'),
        ('把算式裡的每一個 x（或 t）都換成題目的數值，再計算。',
         '同一條式子裡出現兩次 x，兩處都要換。'),
        ('回頭檢查：答案的大小、單位是否合理。',
         '收費、電費類的題目可以分段累加驗一次，兩種算法要一致。'),
    ],
    trigger='題目給了一個分段函數，並要你求某個 x 的函數值時',
    fading='本課：手順卡完整呈現，每步都寫出動作與易錯點。'
           '練習B 起：只在區塊開頭重印一次精簡版（步驟數字＋關鍵詞）。'
           '練習C 起：不再重印卡片，改由學生口述四步驟。',
))

# ================= 三、範例：停車場收費 =================
P.append(heading('三、範例：停車場收費'))
P.append(para('某停車場按泊車時間 t（小時）收費 y（元）：首 1 小時（含）免費；'
              '超過 1 小時至 3 小時（含）的部分每小時 10 元；超過 3 小時的部分每小時 15 元。'
              '寫成分段函數就是：'))
P.append(para('　{y=cases(0, 0<=t<=1; 10(t-1), 1<t<=3; 20+15(t-3), t>3)}'))
P.append(para('題目：小明泊車 5 小時，需要付停車費多少元？'))
P.append(worked_example_table([
    span_row('　{t=5}', why='① 判斷：5 比 3 大，所以落在大括號最下面那一行（{t>3}）。'),
    eq_row('{y}', '{20+15(t-3)}', why='② 抄下那一行的算式。'),
    eq_row('{y}', '{20+15(5-3)}', why='③ 代入：式子裡的 t 全部換成 5。'),
    eq_row('{y}', '{20+15×2}', why='先算括號。'),
    eq_row('{y}', '{20+30}', why='再算乘法。'),
    eq_row('{y}', '{50}', why='最後做加法。'),
    span_row('④ 檢查',
             why='首 1 小時免費；1～3 小時共 2 小時，每小時 10 元＝20 元；'
                 '3～5 小時共 2 小時，每小時 15 元＝30 元；20＋30＝50，與代入的結果一致。'),
    answer_row('小明需要付 50 元', why='作答：最後一行用「∴」寫出結論'),
], why_pct=0.42))

P.append(para('接下來請拿《函數的表示方法與分段函數課堂練習》，'
              '依同一套四步驟框架完成練習A、B、C。'))

# ================= 教師實施說明頁 =================
P.extend(teacher_notes(
    main_design='D5 圖文雙軌對照（圖象法直接出圖；y=|x| 逐段「圖上看到什麼→算式上寫成什麼」）',
    aux_designs=('D2 手順卡（分段函數求值四步驟）', 'D12 自我核對清單（練習端）'),
    reason='本課的核心瓶頸是「同一個函數的三種面孔（式／表／圖）互相對不上」，'
           '屬 S4 函數與圖像，建議主設計為 D5 圖文雙軌；分段函數的求值則是有固定程序的'
           '多步驟運算（S2），降為輔助設計 D2 手順卡。兩個瓶頸依序出現，'
           '主設計取較前端的 S4（先看得懂圖與式是同一件事，才談得上代入求值）。',
    density='全班共用',
    fading='D5：本課圖與式逐段並排；練習A 側欄只留數線分段圖（式子照印）；'
           '練習B 側欄的分段圖只畫界線、每段用哪條式由學生自己寫；練習C 不再給圖。'
           'D2：本課手順卡完整呈現；練習B 起精簡成區塊開頭一次重印；'
           '練習C 起完全不重印，改由學生口述四步驟。',
    flows=('F5 課前流程預告', 'F3 褪除計劃'),
    iep_codes=('a3 提示題目重點', 'a6 增加行距／放大作答欄'),
))

out = build_docx(P, os.path.join(OUT_DIR, '講義_函數的表示方法與分段函數_高一數學.docx'),
                  footer_text=f'{SUBJECT}．{UNIT}', media=MEDIA)
print(out)
