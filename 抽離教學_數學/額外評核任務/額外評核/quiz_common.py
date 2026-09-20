# -*- coding: utf-8 -*-
"""
quiz_common.py — 額外評核（初三抽離小班 5 分鐘小測）共用版面層

抽自 build_quiz_w05.py：W05 一張卷嘅時候版面 helper 直接寫喺 script 入面，
由 W06 開始一次過出 11 張，再複製 11 份就等於同一段排版邏輯有 11 個真相。
依 CLAUDE.md §2.4「共用底層只有一份」，版面 helper 集中喺呢度；
各週 build_quiz_wNN.py 只負責題目內容。

OMML／docx 封裝底層仍然係 similar-practice-generator\\scripts\\omml_docx.py，
本檔唔複製嗰層嘅任何嘢，只做小測專用嘅框與線。

house-style 偏離說明（沿用 W05 規格卡授權範圍）：
1. masthead 類型寫「額外評核」——檔案室分類需要同「課後練習」區分。
2. 不用 ★ 三層難度標籤：5 題全班同卷、每題等分，冇分層概念。
3. 每題框內多一條「改正：」欄——計分含「改正後」，訂正必須留喺同一張紙。
"""
import sys, os

SKILL = r"C:\Users\KongChiLok\.claude\skills\similar-practice-generator\scripts"
if SKILL not in sys.path:
    sys.path.insert(0, SKILL)

from omml_docx import *          # noqa: F401,F403
from omml_docx import _run       # star-import 跳過底線開頭嘅名

SUBJECT = '初三數學'


def ruled(label='', sz=22, row_sz=26):
    """一條書寫線，標籤直接寫喺線上（唔另起一段）。

    點解唔用 write_lines() ＋ 獨立標籤段：
    ① 標籤段用 spacing=False 會繼承 Word Normal 嘅段後 8pt（見記憶
       `docx_spacing_false_is_not_zero`），框內累積起嚟把學生卷推到第 2 頁；
    ② write_lines() 嘅 before=120twips＋row_sz=32 對 5 分鐘小測太鬆。
    合併成一段之後，學生卷由 2 頁收返 1 頁，書寫空間不變。

    🔴 `<w:between>` 唔可以省（2026-09-20 實測踩坑）：
    Word 對**連續、邊框設定完全相同**嘅段落會當成一個 group，
    只喺 group 最頂畫 `w:top`、最底畫 `w:bottom`，中間嗰幾條唔會畫。
    所以「作答：」同「改正：」兩段孖住擺嗰陣，PDF 上只剩「改正：」下面嗰一條，
    「作答：」下面嗰條會消失。段與段之間嗰條要靠 `w:between` 先畫得出。
    CT_PBdr 嘅 schema 次序係 top, left, bottom, right, between, bar，
    所以 `w:between` 一定要排喺 `w:bottom` 後面，掉轉會令 Word 當檔案損毀。"""
    ppr = ('<w:pPr><w:spacing w:line="300" w:lineRule="auto" w:before="0" w:after="0"/>'
           f'<w:pBdr><w:bottom w:val="single" w:sz="5" w:space="4" w:color="{LINE_GREY}"/>'
           f'<w:between w:val="single" w:sz="5" w:space="0" w:color="{LINE_GREY}"/>'
           '</w:pBdr></w:pPr>')
    run = _run(label + ' ', sz=sz) if label else ''
    pad = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
           '<w:t xml:space="preserve"> </w:t></w:r>')
    return f'<w:p>{ppr}{run}{pad}</w:p>'


def answer_line(n=1):
    """作答欄：第一條帶「作答：」標籤，其餘留空。"""
    return [ruled('作答：')] + [ruled() for _ in range(n - 1)]


def fix_line():
    """改正欄（計分含改正後，訂正必須留喺同一張紙上）。"""
    return [ruled('改正：')]


def qbox(paragraphs, last=False):
    """小測專用題目框：沿用 problem_box 嘅統一細框，但收窄框內上下內邊距
    （80→40 twips）並改用矮身分隔段。

    點解自建而唔直接用 problem_box()：problem_box() 嘅 trailing_blank 係一個
    1.5 行距嘅完整空段（約 24pt），5 個框累積約 3.4cm，正正就係把學生卷推到
    第 2 頁嗰一截。字級同框線一律唔郁（跟記憶 `table_doc_page_saving_order`：
    先收內邊距，唔縮字）。"""
    # 題目文字段落：拿掉 para() 預設嘅段後 8pt（w:after="80"）。
    # 🔴 行距 w:line="360"（1.5 倍）唔准郁——house-style 第 17 行明訂，
    # 而且 1.5 倍行距係讀寫障礙友善嘅硬需求，唔可以攞嚟省版面。
    # 段後空白同行距係兩件事：框線本身已經做咗視覺分隔，段後 8pt 喺框內係多餘嘅。
    paragraphs = [p if 'w:pBdr' in p else
                  p.replace('<w:spacing w:line="360" w:lineRule="auto" w:after="80"/>',
                            '<w:spacing w:line="360" w:lineRule="auto" w:after="0"/>')
                  for p in paragraphs]
    tbl = problem_box(paragraphs, trailing_blank=False)
    tbl = tbl.replace('<w:top w:w="80" w:type="dxa"/>', '<w:top w:w="40" w:type="dxa"/>')
    tbl = tbl.replace('<w:bottom w:w="80" w:type="dxa"/>', '<w:bottom w:w="40" w:type="dxa"/>')
    if last:
        return tbl
    # Word 要求連續兩個表格之間有段落；用矮身段代替 blank()
    return tbl + ('<w:p><w:pPr><w:spacing w:line="100" w:lineRule="auto" '
                  'w:before="0" w:after="0"/></w:pPr>'
                  '<w:r><w:rPr><w:sz w:val="4"/><w:szCs w:val="4"/></w:rPr>'
                  '<w:t xml:space="preserve"> </w:t></w:r></w:p>')


def _tight(p):
    """拿掉 para() 預設嘅段後 8pt（`w:after="80"`），行距唔郁。
    學生卷得一頁位，頭三段慳返嘅 8pt × 2 就係最後嗰條「改正：」線嘅生死。"""
    return p.replace('<w:spacing w:line="360" w:lineRule="auto" w:after="80"/>',
                     '<w:spacing w:line="360" w:lineRule="auto" w:after="0"/>')


def tail_stub():
    """文件最後一個元素係表格嗰陣，Word 會自動補一個 Normal 樣式嘅空段落
    （12pt ＋ 段後 8pt ≈ 24pt）。如果最後一個題框啱啱貼住頁底，
    呢個隱形段落就足以迫出一版**完全空白**嘅第 2 頁（2026-09-20 實測 W14／W20 中招）。
    自己補一個 1pt 高嘅空段落，Word 就唔會再補，慳返嗰 22pt。"""
    return ('<w:p><w:pPr><w:spacing w:line="100" w:lineRule="auto" '
            'w:before="0" w:after="0"/></w:pPr>'
            '<w:r><w:rPr><w:sz w:val="2"/><w:szCs w:val="2"/></w:rPr>'
            '<w:t xml:space="preserve"> </w:t></w:r></w:p>')


def student_head(unit):
    """學生卷開頭三段：masthead、學生資料列、計分說明。"""
    return [
        masthead(SUBJECT, unit, '額外評核'),
        _tight(student_info_row()),
        _tight(para([('t', '限時 5 分鐘　　共 5 題　　每題 1 分（20%）　　滿分 5 分'
                          '　　　　得分：＿＿＿ / 5')], bold=True, sz=22)),
    ]


def teacher_head(unit):
    """教師卷開頭三段。"""
    return [
        masthead(SUBJECT, unit, '額外評核・教師卷'),
        para([('t', '本頁供教師批改與訂正指導使用，不發給學生。')], sz=22),
        para([('t', '實施提示：學生卷版面已滿，訂正規則請口頭交代——'
                    '答錯的題目在該題「改正：」一欄訂正，訂正正確計入累積正確率。')], sz=22),
    ]


def scoring_block():
    """教師卷「二、計分與結算」——全學段 11 張卷口徑一致，集中一份。"""
    return [
        heading('二、計分與結算'),
        para([('t', '單次：每題 20%，答對 1 題得 1 分，單次滿分 5 分。')], sz=22),
        para([('t',
               '學段末：以每名學生本學段全部小測的累積正確率（包含改正後答對的題目）'
               '乘以 20，折算為平時平均分之加分，上限 20 分。')], sz=22),
        para([('t', '例：第一學段共 13 次小測、合計 65 題，累積答對（含改正後）55 題 → '
                    '正確率 約 84.6% → 加分 ＝ 0.846 × 20 ≈ 16.9 分。')], sz=22),
    ]


def emit(student_paras, teacher_paras, base, footer, out_dir):
    """寫出兩份 docx。學生卷結尾自動補 tail_stub()，見該函式註解。"""
    if student_paras and student_paras[-1].lstrip().startswith('<w:tbl'):
        student_paras = student_paras + [tail_stub()]
    build_docx(student_paras, os.path.join(out_dir, f'{base}_學生卷.docx'),
               footer_text=footer)
    build_docx(teacher_paras, os.path.join(out_dir, f'{base}_教師卷.docx'),
               footer_text=footer)
    print(f'OK  {base}')
