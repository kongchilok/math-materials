# -*- coding: utf-8 -*-
"""
build_cover.py — 抽離小班「課堂講義／練習」合訂本封面（初三／高一／高三各一份）。

設計：2026-09-01 與使用者敲定
  - 風格 A「極簡線條」：沿用 house-style 的細線／雙線語彙，純黑白、無外框、留白為主。
    （house-style 明文「內頁不要放獨立大標題」，封面必然偏離；本次偏離幅度經使用者選定。）
  - 固定放：年級＋「數學」、課堂講義／練習、學年、姓名／班別／學號填寫欄、
    本冊使用說明三行、任教老師（刻意細字低調）。
  - 校名：使用者本次未選，預設關閉。要加返把 SCHOOL 設成字串即可。
  - 不放頁尾頁碼——封面只有一頁，頁碼是噪音。

輸出：<年級資料夾>\封面_<年級>數學_講義練習.docx
"""
import os
import sys

_SKILL = os.path.join(os.environ.get('USERPROFILE', ''), '.claude', 'skills',
                      'inclusive-math-worksheet-generator', 'scripts')
sys.path.insert(0, _SKILL)

from omml_docx import para, blank, build_docx, RULE_GREY, _tbl  # noqa: E402
from omml_docx import _run  # noqa: E402  （star-import 跳過底線開頭的名字）

# ---------------------------------------------------------------- 可調參數

SCHOOL = None            # 設成 '聖若瑟教區中學第五校．學生支援組' 就會印校名
YEAR = '2026 ／ 2027 學年'
TEACHER = '任教老師：江志樂'
DOC_TYPE = '課堂講義／練習'

USAGE = [
    '一、每堂帶齊本冊。講義用來看範例，練習用來做題目，兩部分要一起帶。',
    # ⚠️ 每行上限約 46 字（11pt、左縮 1100 twips）。超出會斷行，尾巴兩三個字孤行落單，
    # 封面上特別礙眼——改字時數住字數，留 3～4 字餘裕。
    '二、做錯的題目當日訂正，在原題旁寫出正確做法；不要擦走原來的寫法，錯在哪裡才最有用。',
    '三、每題都要寫出列式，不可以只寫答案；看不懂就翻回講義的範例段對照。',
]

GRADES = [
    ('初三', '初三數學'),
    ('高一', '高一數學'),
    ('高三', '高三數學'),
]

BASE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- 版面小工具


def vspace(twips):
    """固定高度的空白段落（lineRule=exact，不受字級影響）。"""
    return ('<w:p><w:pPr>'
            f'<w:spacing w:line="{twips}" w:lineRule="exact" w:before="0" w:after="0"/>'
            '</w:pPr></w:p>')


def rule(style='single', sz=4, color=RULE_GREY):
    """一條橫線（只有下框線的空段落）。style='double' 出雙線。"""
    return ('<w:p><w:pPr>'
            '<w:spacing w:line="120" w:lineRule="exact" w:before="0" w:after="0"/>'
            f'<w:pBdr><w:bottom w:val="{style}" w:sz="{sz}" w:space="0" w:color="{color}"/></w:pBdr>'
            '</w:pPr></w:p>')


def tight(text, sz, jc='center', bold=False, color=None, track=None):
    """一行文字，行距與段前後距全部明寫為零。

    ⚠️ **不要用 `para(..., spacing=False)` 代替**。`spacing=False` 只是「不寫
    w:spacing」，段落於是繼承 Word 內建 Normal 樣式的**段後 8pt ＋ 行距 1.08**，
    不是零。放進表格儲存格時這 8pt 會把儲存格撐高，下框線隨格底走，線就離
    標籤 21pt 遠——v2～v4 三輪都以為是 vAlign 或列高的問題，其實是這個（實測）。

    track = 字距（1/20 pt）。標題撐字距用它，不要用全形空格拼「初　三　數　學」：
    全形空格在字元之間同字組之間一樣闊，「初三」（年級）同「數學」（科目）就分不出組。
    """
    body = _run(text, bold=bold, sz=sz, color=color, track=track)
    ppr = ('<w:pPr><w:spacing w:line="240" w:lineRule="auto" w:before="0" w:after="0"/>'
           f'<w:jc w:val="{jc}"/></w:pPr>')
    return f'<w:p>{ppr}{body}</w:p>'


def centered(text, sz, bold=False, color=None, track=None):
    return tight(text, sz, 'center', bold, color, track)


def fill_in_fields(labels, sz=32, gap=420):
    """姓名／班別／學號填寫欄：標籤 + 一條真正的下框線。回傳段落 list。

    ⚠️ 兩個踩過的坑，改動前先讀：
    1. 不要用全形底線字元「＿＿＿」——微軟正黑體→Word→PDF 這條管線上每個 ＿
       之間有肉眼可見的斷口，印出來是一串虛線而不是一條線。
    2. 不要用「一張三列表格＋固定 trHeight＋vAlign」——行高一鎖死，標籤就浮在
       格的上半、下框線畫在格的最底，兩者差成半格，看起來像標籤同線各自為政
       （vAlign='bottom' 補救不了，實測）。正解是**每欄一張獨立單列表格、
       不設行高**，讓線自然貼住文字基線，欄與欄之間用 vspace() 拉開。
    3. 線格要放一個同字級的空白 run（不是 blank()），兩格高度才一致——
       否則 12pt 的空段落配 16pt 的標籤，線會偏高。
    """
    widths = [2500, 1500, 5100, 2238]      # 合計 = _PAGE_CONTENT_WIDTH 11338
    out = []
    for i, lb in enumerate(labels):
        if i:
            out.append(vspace(gap))
        # 4 格一律用 tight()（行距／段距明寫為零、同字級），列高才等於一行文字，
        # 下框線就緊貼標籤基線。見 tight() 的註解。
        pad = tight(' ', sz)
        row = [
            {'p': [pad]},
            {'p': [tight(f'{lb}：', sz, jc='right')]},
            {'p': [pad], 'bd': ('none', 'none', 'single', 'none')},
            {'p': [pad]},
        ]
        out.append(_tbl([row], widths, border='none', trailing_blank=False))
    return out


# ---------------------------------------------------------------- 組版


def build_one(grade, folder):
    P = []

    if SCHOOL:
        P.append(vspace(600))
        P.append(rule('single', 4))
        P.append(vspace(120))
        P.append(centered(SCHOOL, sz=24))
        P.append(vspace(80))
        P.append(rule('double', 6))
        P.append(vspace(1100))
    else:
        P.append(vspace(1700))

    # 主標題區：年級與「數學」之間留一個全形空格分組，字距靠 track 撐
    P.append(centered(f'{grade}　數學', sz=88, bold=True, track=140))
    P.append(vspace(300))
    P.append(centered(DOC_TYPE, sz=36, track=20))
    P.append(vspace(220))
    P.append(centered(YEAR, sz=26, color='555555'))

    # 填寫區
    P.append(vspace(1000))
    P.append(rule('single', 4))
    P.append(vspace(560))
    P.extend(fill_in_fields(('姓　名', '班　別', '學　號')))
    P.append(vspace(620))
    P.append(rule('double', 12))

    # 使用說明
    P.append(vspace(360))
    P.append(para([('t', '本冊使用說明')], bold=True, sz=24, ind=1100))
    P.append(vspace(160))
    for line in USAGE:
        P.append(para([('t', line)], sz=22, ind=1100))

    # 任教老師（刻意細字、低調）
    P.append(vspace(520))
    P.append(centered(TEACHER, sz=20, color='777777'))

    out = os.path.join(BASE, folder, f'封面_{grade}數學_講義練習.docx')
    build_docx(P, out)
    return out


if __name__ == '__main__':
    for grade, folder in GRADES:
        path = build_one(grade, folder)
        print('OK', path, os.path.getsize(path), 'bytes')
