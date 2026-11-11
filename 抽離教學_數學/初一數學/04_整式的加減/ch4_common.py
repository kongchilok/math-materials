# -*- coding: utf-8 -*-
r"""
ch4_common.py — 初一數學（代課）第四章〈整式的加減〉六份「講義＋練習」的共用版面層。

使用者 2026-11-10 裁決：
- 講義與練習合一個檔（偏離 house-style「分兩檔」，使用者當次明說）。
- 全章按課時切 6 份；鷹架密度＝全班共用。
- 教學設計：4.1＝D6 主＋D13、D11 輔；4.2＝D2 主＋D11、D14 輔。
- 每份要「科任已講＝重溫、未講＝新授」兩用，所以每份開頭有「先重溫」。
只放版面小工具；題目內容在 build_ch4.py。底層一律用 skill 的 omml_docx。
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.expanduser('~'), '.claude', 'skills',
                                'inclusive-math-worksheet-generator', 'scripts'))
from omml_docx import (  # noqa: E402,F401
    para, heading, masthead, student_info_row, shaded_box, shaded_multi_box,
    build_docx, problem_box, write_lines, star_label, step_card, teacher_notes,
    worked_example_table, eq_row, span_row, answer_row, dual_track_table,
    aside_layout, hint_lines, _tbl, _PAGE_CONTENT_WIDTH, GREY_FILL, CHECKBOX)

W = _PAGE_CONTENT_WIDTH
W_IN = W - 520          # 題框內巢狀表的可用寬度
SUBJ = '初一數學'
FOOT = '初一數學．第四章 整式的加減'
BLANK = '＿＿＿＿'
TINY = ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="20" '
        'w:lineRule="exact"/></w:pPr></w:p>')

GAP = ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="150" '
       'w:lineRule="exact"/></w:pPr></w:p>')   # 框與框之間的小間距（取代 1.5 行高的 blank()）
_SP = '<w:spacing w:line="360" w:lineRule="auto" w:after="80"/>'


def tight(xml, line=300, after=20):
    """把段落行距由 1.5 倍收窄（只用在表格格內、參考答案、教師說明頁——不是學生的本文）。"""
    return xml.replace(_SP, f'<w:spacing w:line="{line}" w:lineRule="auto" w:after="{after}"/>')


def nm(s):
    """整段只有公式時 Word 會當 display math 置中——以公式開頭的字串前面補一個不斷行空白 run。"""
    return ' ' + s if isinstance(s, str) and s.startswith('{') else s


_PPR_RE = re.compile(r'<w:pPr>(.*?)</w:pPr>', re.S)


def keep_together(xml):
    """短表除最後一列外每段加 keepNext，免得 Word 在列與列之間分頁。"""
    i = xml.rfind('<w:tr>')
    if i <= 0:
        return xml
    head, tail = xml[:i], xml[i:]
    head = _PPR_RE.sub(lambda m: m.group(0) if '<w:keepNext/>' in m.group(1)
                       else f'<w:pPr><w:keepNext/>{m.group(1)}</w:pPr>', head)
    head = re.sub(r'<w:p>(?!<w:pPr>)', '<w:p><w:pPr><w:keepNext/></w:pPr>', head)
    return head + tail


def pbox(paras, last=False):
    """problem_box；題框以表格收尾時補一個 1pt 段落（否則 Word 報毀損）。
    last=True：後面緊接另起一頁的標題，不補間距段（否則可能多出一頁空白）。"""
    paras = list(paras)
    if paras and paras[-1].lstrip().startswith('<w:tbl'):
        paras.append(TINY)
    return problem_box(paras, trailing_blank=False) + ('' if last else GAP)


def _cell(c, sz=23, bold=False):
    if isinstance(c, dict):
        return c
    if isinstance(c, list):
        return c
    return [tight(para(nm(c), sz=sz, bold=bold))]


def grid(rows, widths, head=True, inner=False, sz=23, row_h=0, keep=True):
    """通用小表。rows 的格可以是 {} 標記字串／段落 list／_tc dict。
    head=True：第一列灰底粗體並跨頁重印。inner=True：放在題框內（不補尾段）。"""
    out = []
    for i, r in enumerate(rows):
        if head and i == 0:
            out.append({'hdr': True, 'cells': [
                {'p': [tight(para(nm(c), bold=True, sz=sz))], 'shd': GREY_FILL} for c in r]})
        else:
            cells = [_cell(c, sz) for c in r]
            out.append({'cells': cells, 'h': row_h} if row_h else cells)
    x = _tbl(out, widths, trailing_blank=False)
    x = keep_together(x) if keep else x
    return x if inner else x + GAP


def cols(n, total=None, first=None):
    """平均分欄寬；first＝第一欄寬度。"""
    total = total or W
    if first:
        w = (total - first) // (n - 1)
        return [first] + [w] * (n - 2) + [total - first - w * (n - 2)]
    w = total // n
    return [w] * (n - 1) + [total - w * (n - 1)]


def frayer(term, definition, features, examples, nonexamples):
    """D13 弗雷爾概念模型：中央術語＋定義／特徵／例／非例四象限。"""
    h = W // 2

    def quad(title, lines):
        return [tight(para(title, bold=True, sz=23))] + [tight(para(nm(x), sz=23)) for x in lines]
    rows = [
        [{'p': [para(term, bold=True, sz=28, jc='center')], 'shd': GREY_FILL, 'span': 2}],
        [quad('定義', definition), quad('特徵（三個都要符合）', features)],
        [quad('例（是）', examples), quad('非例（不是）——差在哪個特徵', nonexamples)],
    ]
    return keep_together(_tbl(rows, [h, W - h], trailing_blank=False)) + GAP


def think_table(rows, headers=('做什麼', '寫下來', '我心裡說的話')):
    """D6「我做」：每列一步＋放聲思考引號句。"""
    w1, w2 = int(W * 0.24), int(W * 0.30)
    return grid([headers] + [list(r) for r in rows], [w1, w2, W - w1 - w2])


def contrast(pairs, note):
    """D14 錯誤分析對比：左「常見寫法」留白、右「正確寫法」灰底，逐列橫向對齊。"""
    h = W // 2
    rows = [{'hdr': True, 'cells': [
        {'p': [para('常見寫法', bold=True, sz=23)]},
        {'p': [para('正確寫法', bold=True, sz=23)], 'shd': GREY_FILL}]}]
    for a, b in pairs:
        rows.append([{'p': [tight(para(nm(a)))]}, {'p': [tight(para(nm(b)))], 'shd': GREY_FILL}])
    rows.append([{'p': [tight(para(f'※ 差在這裡：{note}', bold=True, sz=23))], 'span': 2}])
    return keep_together(_tbl(rows, [h, W - h], trailing_blank=False)) + GAP


def q(lines, n=3, hint=None, hint_title='步驟', extra=(), last=False):
    """一題：題目＋作答線；hint 有值時放右側欄（題目在左、提示在右）。"""
    body = [para(nm(x)) if isinstance(x, str) else x for x in lines] + list(extra)
    if hint:
        return aside_layout(body + write_lines(n), hint_lines(hint, title=hint_title),
                            main_pct=0.66, boxed=True)
    return pbox(body + write_lines(n), last=last)


def qparts(title, parts, n=2, split=3, last=False):
    """多小題計算題：每小題下面各自有作答線；小題多時拆成兩個框，免得一個大框被整個推到下一頁。"""
    def blk(ps):
        out = []
        for p in ps:
            out += [para(nm(p))] + write_lines(n)
        return out
    if len(parts) <= split:
        return pbox([para(title)] + blk(parts), last=last)
    return pbox([para(title)] + blk(parts[:split])) + pbox(blk(parts[split:]), last=last)


def card(*a, **k):
    """手順卡＋逐列 keepNext（不讓 Word 在步驟之間分頁）。"""
    return keep_together(step_card(*a, **k))


def answers(title_lines):
    """教師用參考答案（另起一頁）。"""
    P = [heading('教師用參考答案（本頁供教師參考，列印給學生時可不印）', page_break_before=True)]
    P += [tight(para(x, sz=22), line=320, after=40) for x in title_lines]
    return P


def notes(main, aux, reason, fading, bac, pages, use):
    return [tight(x, line=290, after=10) for x in teacher_notes(
        main, aux, reason=reason, density='全班共用', fading=fading,
        flows=('F1 師徒制對話四步',),
        iep_codes=('a3 提示題目重點', 'a6 增加行距／放大作答欄'),
        extra=[('本單元對應的正規教學目標', bac),
               ('課本頁次', pages),
               ('兩用方式（科任已講／未講）', use),
               ('調整性質', '調整支援：只調整呈現方式與鷹架，核心概念與年級標準不變。')])]
