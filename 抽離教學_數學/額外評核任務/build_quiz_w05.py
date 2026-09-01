# -*- coding: utf-8 -*-
"""
build_quiz_w05.py — 初三抽離小班 課堂小測 W05（單元 01 一元二次方程・概念與三種解法）

規格來源：工作筆記「📋 需求確認 → 🟢 現行規格卡」（2026-09-01 經 RDQ 訪談確認）
- 每週 1 次、抽離課堂課內、限時 5 分鐘、5 題、每題 20%（單次滿分 5 分）
- 題型：3 題基礎概念 ＋ 2 題常見錯誤糾正
- 命題範圍＝上週已教完（隔一週鞏固）；進度基準＝丙班；兩班共用同一份卷
- 產出：學生卷（含改正欄）＋ 教師答案卷，各 docx＋PDF

house-style 偏離說明（本次刻意，已在規格卡授權範圍內）：
1. masthead 類型寫「課堂小測」（不是 skill 預設的「課後練習」）——檔案室分類需要區分。
2. 不用 ★ 三層難度標籤。小測 5 題全班同卷、每題等分，沒有分層概念；
   星星是講義／練習的分層語彙，套在這裡會誤導學生以為某幾題可以不做。
3. 每題框內多一條「改正：」欄——計分規則含「改正後」，訂正必須留在同一張紙上，
   否則學段末結算時無從核對。
"""
import sys, os

SKILL = r"C:\Users\KongChiLok\.claude\skills\similar-practice-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _run  # star-import 跳過底線開頭的名稱

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學'
UNIT = 'W05・一元二次方程・概念與三種解法'
FOOTER = '初三數學．課堂小測 W05'
BASE = '小測_初三數學_W05_一元二次方程概念與三種解法'


def ruled(label='', sz=22, row_sz=26):
    """一條書寫線，標籤直接寫在線上（不另起一段）。

    為什麼不用 write_lines() ＋ 獨立標籤段：
    ① 標籤段用 spacing=False 會繼承 Word Normal 的段後 8pt（見記憶
       `docx_spacing_false_is_not_zero`），框內累積起來把學生卷推到第 2 頁；
    ② write_lines() 的 before=120twips＋row_sz=32 對 5 分鐘小測太鬆。
    合併成一段後，學生卷由 2 頁收回 1 頁，書寫空間不變。"""
    ppr = ('<w:pPr><w:spacing w:line="300" w:lineRule="auto" w:before="60" w:after="0"/>'
           f'<w:pBdr><w:bottom w:val="single" w:sz="5" w:space="4" w:color="{LINE_GREY}"/>'
           '</w:pBdr></w:pPr>')
    run = _run(label + ' ', sz=sz) if label else ''
    pad = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
           '<w:t xml:space="preserve"> </w:t></w:r>')
    return f'<w:p>{ppr}{run}{pad}</w:p>'


def answer_line(n=1):
    """作答欄：第一條帶「作答：」標籤，其餘留空。"""
    return [ruled('作答：')] + [ruled() for _ in range(n - 1)]


def fix_line():
    """改正欄（計分含改正後，訂正必須留在同一張紙上）。"""
    return [ruled('改正：')]


def qbox(paragraphs, last=False):
    """小測專用題目框：沿用 problem_box 的統一細框，但收窄框內上下內邊距
    （80→40 twips）並改用矮身分隔段。

    為什麼要自建而不直接用 problem_box()：problem_box() 的 trailing_blank
    是一個 1.5 行距的完整空段（約 24pt），5 個框累積約 3.4cm，正正就是把
    學生卷推到第 2 頁那一截。字級與框線一律不動（跟記憶
    `table_doc_page_saving_order`：先收內邊距，不縮字）。"""
    tbl = problem_box(paragraphs, trailing_blank=False)
    tbl = tbl.replace('<w:top w:w="80" w:type="dxa"/>', '<w:top w:w="40" w:type="dxa"/>')
    tbl = tbl.replace('<w:bottom w:w="80" w:type="dxa"/>', '<w:bottom w:w="40" w:type="dxa"/>')
    if last:
        return tbl
    # Word 要求連續兩個表格之間有段落；用矮身段代替 blank()
    return tbl + ('<w:p><w:pPr><w:spacing w:line="120" w:lineRule="auto" '
                  'w:before="0" w:after="0"/></w:pPr>'
                  '<w:r><w:rPr><w:sz w:val="8"/><w:szCs w:val="8"/></w:rPr>'
                  '<w:t xml:space="preserve"> </w:t></w:r></w:p>')


# ============================ 學生卷 ============================
S = []
S.append(masthead(SUBJECT, UNIT, '課堂小測'))
S.append(student_info_row())
S.append(para([('t', '限時 5 分鐘　　共 5 題　　每題 1 分（20%）　　滿分 5 分'
                     '　　　　得分：＿＿＿ / 5')], bold=True, sz=22))

# 第 1 題 — 基礎概念：化一般式、讀係數
S.append(qbox([
    para('1．將 {3x^2=5x−2} 化為一般式後，一次項係數 b 的值是（　　）'),
    para([('t', 'A．5　　　B．−5　　　C．3　　　D．2')], ind=300),
] + answer_line() + fix_line()))

# 第 2 題 — 基礎概念：直接開平方法
S.append(qbox([
    para('2．方程 {(x+1)^2=4} 的根是（　　）'),
    para('A．{x_1=1} 或 {x_2=−3}　　　B．{x_1=3} 或 {x_2=−5}', ind=300),
    para('C．{x_1=2} 或 {x_2=−2}　　　D．無實數根', ind=300),
] + answer_line() + fix_line()))

# 第 3 題 — 基礎概念：判別式與根的個數
S.append(qbox([
    para('3．方程 {x^2−4x+5=0} 的判別式 {Δ=} ＿＿＿＿＿＿，'
         '此方程有 ＿＿＿＿ 個實數根。'),
] + fix_line()))

# 第 4 題 — 常見錯誤糾正：負數不能開平方
S.append(qbox([
    para('4．小明解 {x^2−4=−13}：{x^2=−9}　→　{x_1=3} 或 {x_2=−3}。'
         '他錯在哪一步？正確答案是？'),
    ruled('作答：'), ruled(),
] + fix_line()))

# 第 5 題 — 常見錯誤糾正：兩邊除以 x 漏根
S.append(qbox([
    para('5．小芳解 {x^2=7x}：兩邊同除以 {x}，得 {x=7}，∴ {x=7}。'
         '她漏了什麼？寫出完整的解。'),
    ruled('作答：'), ruled(),
] + fix_line(), last=True))

build_docx(S, os.path.join(OUT, f'{BASE}_學生卷.docx'), footer_text=FOOTER)


# ============================ 教師卷 ============================
T = []
T.append(masthead(SUBJECT, UNIT, '課堂小測・教師卷'))
T.append(para([('t', '本頁供教師批改與訂正指導使用，不發給學生。')], sz=22))
T.append(para([('t', '實施提示：學生卷版面已滿，訂正規則請口頭交代——'
                     '答錯的題目在該題「改正：」一欄訂正，訂正正確計入累積正確率。')], sz=22))

T.append(heading('一、參考答案'))
T.append(problem_box([
    para('1．B（−5）'),
    para('　整理成一般式：{3x^2−5x+2=0}，對照 {ax^2+bx+c=0} 讀出 a＝3、b＝−5、c＝2。'),
    para('　誘答 A：把 5x 移項時漏了變號，直接抄成 +5。'),
]))
T.append(problem_box([
    para('2．A（{x_1=1} 或 {x_2=−3}）'),
    para('　{x+1=2} 或 {x+1=−2}，兩支各自移項得 {x_1=1} 或 {x_2=−3}。'),
    para('　誘答 C：開平方後忘記移項，直接把 {±2} 當成答案（最常見）。'),
]))
T.append(problem_box([
    para('3．{Δ=−4}；有 0 個實數根（無實數根）'),
    para('　{Δ=b^2−4ac=(−4)^2−4(1)(5)=16−20=−4}，{Δ<0} 故無實數根。'),
    para('　常見錯誤：把 {(−4)^2} 算成 −16。'),
]))
T.append(problem_box([
    para('4．錯在「由 {x^2=−9} 直接開平方」這一步。'),
    para('　開平方前必須先看右邊的正負：−9 ＜ 0，負數不能開平方，'),
    para('　所以此方程無實數根，不是 {x_1=3} 或 {x_2=−3}。'),
    para('　（移項那一步小明沒有做錯：{x^2=−13+4=−9}。）'),
]))
T.append(problem_box([
    para('5．小芳漏了 {x=0} 這個根。兩邊都有 {x} 時不可以除以 {x}，因為 {x} 有可能等於 0。'),
    para('　正確做法：{x^2−7x=0}　→　{x(x−7)=0}'),
    para('　{x=0} 或 {x−7=0}'),
    para('　∴ {x_1=0} 或 {x_2=7}'),
]))

T.append(heading('二、計分與結算'))
T.append(para([('t', '單次：每題 20%，答對 1 題得 1 分，單次滿分 5 分。')], sz=22))
T.append(para([('t',
    '學段末：以每名學生本學段全部小測的累積正確率（包含改正後答對的題目）'
    '乘以 20，折算為平時平均分之加分，上限 20 分。')], sz=22))
T.append(para([('t', '例：全學段共 60 題，累積答對（含改正後）51 題 → '
                     '正確率 85% → 加分 ＝ 0.85 × 20 ＝ 17 分。')], sz=22))

T.append(heading('三、命題說明'))
T.append(para([('t',
    '第 1–3 題為基礎概念題，取自《課堂講義》第一至四節（一般式係數、'
    '直接開平方法、判別式判斷根的個數）。')], sz=22))
T.append(para([('t',
    '第 4–5 題為常見錯誤糾正題，錯誤原型取自本單元《課堂練習》第 6 題'
    '（負數開平方）與第 23 題（兩邊除以 x 漏根），數據已更換。')], sz=22))
T.append(para([('t',
    '※ 本次 5 題未覆蓋「配方法」與「因式分解法（十字交乘型）」，'
    '可留待下一次小測。')], sz=22))
T.append(para([('t',
    '※ 進度基準為丙班。本週（W5）乙班亦已於 W4 教完單元 01，兩班無落差。')], sz=22))

build_docx(T, os.path.join(OUT, f'{BASE}_教師卷.docx'), footer_text=FOOTER)

print('OK')
