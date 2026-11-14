# -*- coding: utf-8 -*-
r"""
ch5_common.py — 初一數學（代課）第五章〈一元一次方程〉「講義＋練習」的共用版面層。
由 ch4_common.py 複製，版面工具不變。

使用者 2026-11-13 裁決：
- 沿用第四章決策：講義與練習合一個檔、按課時切份、全班共用密度、每份開頭「先重溫」（兩用）。
- 教學設計「按你提議」：由我按數學結構選定，不再逐課問（設計見 build_ch5.py 各課的 notes()）。
只放版面小工具；題目內容在 build_ch5.py。底層一律用 skill 的 omml_docx。
"""
import os
import re
import sys

# ~\.claude\skills 是指向 2ndBrain\_claude-skills 的 junction；2026-11-13 發現 junction 仍指舊路徑
# 「G:\我的雲端硬碟\...」而斷開，所以先找 junction，找不到再直接用雲端硬碟的原檔。
_SK = [os.path.join(os.path.expanduser('~'), '.claude', 'skills'),
       r'G:\My Drive\2ndBrain\_claude-skills', r'G:\我的雲端硬碟\2ndBrain\_claude-skills']
for _d in _SK:
    _p = os.path.join(_d, 'inclusive-math-worksheet-generator', 'scripts')
    if os.path.isfile(os.path.join(_p, 'omml_docx.py')):
        sys.path.insert(0, _p)
        break
SCRIPTS = sys.path[0]
from omml_docx import (  # noqa: E402,F401
    para, heading, masthead, student_info_row, shaded_box, shaded_multi_box,
    build_docx, problem_box, write_lines, star_label, step_card, teacher_notes,
    worked_example_table, eq_row, span_row, answer_row, dual_track_table,
    aside_layout, hint_lines, _tbl, _PAGE_CONTENT_WIDTH, GREY_FILL, CHECKBOX)

W = _PAGE_CONTENT_WIDTH
W_IN = W - 520          # 題框內巢狀表的可用寬度
SUBJ = '初一數學'
FOOT = '初一數學．第五章 一元一次方程'
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


# ---------------------------------------------------------------- 第五章新增：圖形（D10 天平、D1 條形模型）
import design_svg as ds  # noqa: E402
from omml_docx import MediaRegistry, expand_image, image_para, three_column_table, keyword_table, selfcheck_list, dual_track_table  # noqa: E402,F401

FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_tmp_fig')


def _pad(svg, px=70, py=320):
    """headless Chrome 截圖會把矮的 SVG 截短（2026-11-13 實測：兩列條形圖只剩頂部一線），
    天平盒子多時也會伸出左邊界。外面再包一層較大的畫布（內層 overflow 可見），截完再裁白邊。"""
    import re as _re
    w = int(_re.search(r'width="(\d+)"', svg).group(1))
    h = int(_re.search(r'height="(\d+)"', svg).group(1))
    inner = svg.replace('<svg ', f'<svg x="{px}" y="0" overflow="visible" ', 1)
    W2, H2 = w + 2 * px, h + py
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W2}" height="{H2}" viewBox="0 0 {W2} {H2}">'
            f'<rect width="{W2}" height="{H2}" fill="#ffffff"/>{inner}</svg>')


def fig(svg, name, w=8.0):
    """SVG → PNG（放 _tmp_fig，收尾刪）→ ImageRef。頂層段落可直接放；放進表格／題框要用 figx()。"""
    png = ds.svg_to_png(_pad(svg), os.path.join(FIG, name + '.png'))
    from PIL import Image, ImageChops
    im = Image.open(png).convert('RGB')
    box = ImageChops.difference(im, Image.new('RGB', im.size, 'white')).getbbox()
    if box:   # 裁掉四周白邊（天平圖上方約三分一是空白），再留 20px
        l, t, r, b = box
        im.crop((max(l - 20, 0), max(t - 20, 0), min(r + 20, im.width), min(b + 20, im.height))).save(png)
    return image_para(png, width_cm=w)


def figx(media, svg, name, w=8.0):
    """放進題框、表格格內的圖：先展開成 XML 並登記到 media。"""
    return expand_image(fig(svg, name, w), media)


def bal(left, right):
    """天平：left／right 用簡寫，'x' 表示一個盒，其他字串表示砝碼。"""
    conv = lambda xs: [('box', 'x') if s == 'x' else ('unit', s) for s in xs]
    svg = ds.balance(conv(left), conv(right))
    return svg.replace('font-size="12"', 'font-size="18"').replace('font-size="11"', 'font-size="15"')


def tcol(rows, row_h=1300):
    """D4 三欄式；整張表跟題框一樣加尾段間距。"""
    return keep_together(three_column_table(rows, row_h=row_h)) + GAP


# ---------------------------------------------------------------- 第五章版面修正（2026-11-14 目視驗收後）
GAPK = ('<w:p><w:pPr><w:keepNext/><w:spacing w:before="0" w:after="0" w:line="150" '
        'w:lineRule="exact"/></w:pPr></w:p>')


def stem(*texts):
    """應用題題幹框：黏住下面的條形圖／三欄表，不讓 Word 把題幹留在上一頁。"""
    return problem_box([para(''.join(texts), keep_next=True)], trailing_blank=False) + GAPK


def q(lines, n=3, hint=None, hint_title='步驟', extra=(), last=False):
    """覆寫 ch4 版：提示一律放在題框底部（不再用右側欄，免得題幹被擠斷、作答線變窄）。"""
    body = [para(nm(x)) if isinstance(x, str) else x for x in lines] + list(extra) + write_lines(n)
    if hint:
        body += hint_lines(hint, title=hint_title)
    return pbox(body, last=last)


def qparts(title, parts, n=2, split=3, last=False):
    """覆寫 ch4 版：拆成兩框時，第二框開頭寫「（第 N 題續）」，免得學生以為是另一題。"""
    def blk(ps):
        out = []
        for p_ in ps:
            out += [para(nm(p_))] + write_lines(n)
        return out
    if len(parts) <= split:
        return pbox([para(title)] + blk(parts), last=last)
    no = title.split('．')[0]
    return (pbox([para(title)] + blk(parts[:split]))
            + pbox([para(f'（第 {no} 題續）', bold=True)] + blk(parts[split:]), last=last))
