# -*- coding: utf-8 -*-
r"""
build_remedial_20261015_quadratic_vertex_form.py — 初三數學補救班 課後補救教學（2026-10-15）

來源（使用者 2026-10-09 提供）：
1. `F:\新USB_1.1\公司\題庫_講義_練習_模擬_測驗\初三\練習_二次函數性質_初三數學.docx`
   （課後輔導講義，原稿日期 2024.4.10，2 頁：y = a(x − h)²、y = a(x − h)² + k 兩張圖像性質表
   ＋例 1、例 2＋練 1–9），全部收錄。
2. 同資料夾 `練習_二次函數(配方法)_初三數學.docx`（2024.4.24）——使用者指定只要最後幾題：
   例 5、練 5、例 6、練 6（配方化為頂點式並寫出開口方向、對稱軸、頂點坐標）。
3. 使用者在對話貼上的截圖 9 小題（截圖原題號 3、4、5、9、10、11、16、17(1)、17(2)）。

使用者 2026-10-09 裁決（四項都選建議做法）：
- 配方法題幹寫「化為頂點式 y = a(x − h)² + k」（使用者口頭講「一般式」，但課本的一般式是
  y = ax² + bx + c，即原題本身）。
- 配方法鷹架照原稿褪除：前三題保留 ∆／∎ 填格，最後一題（原練 6）只留作答線。
- 截圖 17(2)「利用公式求」→ 卷內加頂點公式框，題目照原文。
- 其餘照 10-08 那份：例題全部改為練習、全卷設分值、滿分 100、學生卷＋教師卷、每題「改正」欄。

使用者 2026-10-13 第二輪（看過 24 題版後）：
- 初版練 1–5 刪去；初版練 6、7 及練 8–18（含截圖 3、4、5、9、10、11、17(1)）
  **學生已做過一次**，全部改為我仿同題型新命的相似題（現練 1–13，逐題 sympy 驗算）。
- 配方法 4 題、截圖 17(2)、截圖 16 照原稿（現練 14–19）。
- 「配方法示範和開頭練習盡可能放同一頁」→ 練 14／15、練 16／17 照原稿「例｜練」左右並排
  （pair_box）；公式框以 info_box 鎖住下一題，不會孤留頁尾。
- 共 19 題；分值：一 8＋二 36＋三 16＋四 40＝100（明細見驗算紀錄）。

使用者 2026-10-13 第三輪：刪去 y = a(x − h)² 性質表（連第一大題）；原練 1、2 移到原練 9 之後（現練 8、9）。
全卷三大題：一 y = a(x − h)² + k 44＋二 平移 16＋三 頂點式 40＝100。

版面：
1. 兩張性質表改成 a > 0／a < 0 決策表，圖以 matplotlib 黑白重畫（每欄一張，照原稿第二張
   表的做法：具體曲線＋「頂點 (h, k)」「對稱軸 x = h」的一般標註）。
2. 配方法的 ∆／∎ 填格用共用層新增的 {slot(∆)} 標記重現（結構照原稿 OMML）。
3. 提示框：三、平移規律（由性質表推得，原稿無）；四、完全平方公式（原稿第 1 行）＋頂點公式
   （使用者裁決）。
4. 作答線逐行交替框線設定（記憶 docx_adjacent_border_paras_merge）。
"""
import sys, os, re

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _run, _tbl, _PAGE_CONTENT_WIDTH
from omml_core import MediaRegistry, expand_image

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學（補救班）'
UNIT = '二次函數・y = a(x − h)² + k 的圖像及配方法'
BASE = '課後補救教學_初三數學補救班_20261015_二次函數頂點式'
FOOT = '初三數學補救班．課後補救教學 2026-10-15'
W = _PAGE_CONTENT_WIDTH
FIGS = {k: os.path.join(OUT, f'_tmp_fig_{k}.png') for k in ('h_up', 'h_dn', 'hk_up', 'hk_dn')}
BLANK = '＿＿＿＿＿＿＿＿'
SHORT = '＿＿＿＿'
MID = '＿＿＿＿＿＿'

_PPR = re.compile(r'<w:pPr>((?:(?!</w:pPr>).)*?)</w:pPr>', re.S)


def tighten(xml):
    """para(spacing=False) 並不是零行距（記憶 docx_spacing_false_is_not_zero）。"""
    def fix(m):
        inner = m.group(1)
        if '<w:spacing' in inner or '<w:jc ' not in inner or '<w:ind' in inner:
            return m.group(0)
        inner = inner.replace('<w:jc ', '<w:spacing w:before="0" w:after="0" w:line="276" '
                                        'w:lineRule="auto"/><w:jc ', 1)
        return f'<w:pPr>{inner}</w:pPr>'
    return _PPR.sub(fix, xml)


_SPACER = '<w:p><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr></w:p>'
_SPACER_SLIM = ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="200" '
                'w:lineRule="exact"/></w:pPr></w:p>')


_SPACER_TINY = ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="20" '
                'w:lineRule="exact"/><w:rPr><w:sz w:val="2"/></w:rPr></w:pPr></w:p>')


def save(P, name, footer, media=None):
    """框與框之間的 blank() 換成 10pt 固定行高的細間隔（10-08 那份的做法）。"""
    P = [x if hasattr(x, 'png_path') else tighten(x).replace(_SPACER, _SPACER_SLIM)
         for x in P]
    # 最後一個表格之後的間隔段改成 1pt：文件不能以表格結尾，但 10pt 那段剛好溢出時會
    # 多出一張只有頁尾的空白頁（教師卷實測）
    if not hasattr(P[-1], 'png_path') and P[-1].endswith(_SPACER_SLIM):
        P[-1] = P[-1][:-len(_SPACER_SLIM)] + _SPACER_TINY
    build_docx(P, os.path.join(OUT, name), footer_text=footer, media=media)


# ================================ 圖 ================================
def _pgraph(f, xr, yr, path, vertex, vlab, vlab_xy, axlab_y):
    """性質表用的單曲線黑白圖：淺灰格線、帶箭頭的 x／y 軸、對稱軸用點劃線、
    頂點實心點＋一般標註（照原稿：具體曲線、標「頂點 (h, k)」「對稱軸 x = h」）。"""
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams['font.family'] = ['Calibri', 'Microsoft JhengHei']
    plt.rcParams['mathtext.fontset'] = 'stix'
    fig, ax = plt.subplots(figsize=(2.4, 2.3), dpi=300)
    ax.set_xlim(xr[0] - 0.3, xr[1] + 0.6)
    ax.set_ylim(yr[0] - 0.3, yr[1] + 0.6)
    ax.set_xticks(range(xr[0], xr[1] + 1))
    ax.set_yticks(range(yr[0], yr[1] + 1))
    ax.grid(True, color='#c8c8c8', lw=0.6)
    ax.set_axisbelow(True)
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_position(('data', 0))
        ax.spines[s].set_linewidth(1.1)
    ax.plot(1, 0, '>k', ms=5, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, '^k', ms=5, transform=ax.get_xaxis_transform(), clip_on=False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=0)
    box = dict(fc='white', ec='none', pad=0.6)
    for t in range(xr[0], xr[1] + 1):
        if t:
            ax.text(t, -0.16, str(t).replace('-', '−'), ha='center', va='top',
                    fontsize=7, bbox=box, zorder=1.5)
    for t in range(yr[0], yr[1] + 1):
        if t:
            ax.text(-0.14, t, str(t).replace('-', '−'), ha='right', va='center',
                    fontsize=7, bbox=box, zorder=1.5)
    ax.text(xr[1] + 0.55, 0.15, '$x$', ha='right', va='bottom', fontsize=12)
    ax.text(0.18, yr[1] + 0.55, '$y$', ha='left', va='top', fontsize=12)
    ax.text(-0.14, -0.16, '$O$', ha='right', va='top', fontsize=10)
    h, k = vertex
    ax.plot([h, h], [yr[0] - 0.3, yr[1] + 0.3], color='black', ls='-.', lw=1.0, zorder=2)
    ax.text(h + 0.15, axlab_y, '對稱軸\n$x=h$', ha='left', va='center', fontsize=9,
            bbox=dict(fc='white', ec='none', pad=1.0), zorder=3)
    xs = np.linspace(xr[0], xr[1], 400)
    ys = f(xs)
    ys = np.where((ys < yr[0] - 0.3) | (ys > yr[1] + 0.3), np.nan, ys)
    ax.plot(xs, ys, color='black', lw=1.9, zorder=4)
    ax.plot(h, k, 'o', color='black', ms=5, mec='white', mew=0.8, zorder=5)
    # 「頂點」（正黑體）與 $(h,k)$（mathtext）分兩個 TextArea 橫排——
    # 同一字串混 $…$ 的話，$ 外的中文會走 mathtext 字型變方塊
    from matplotlib.offsetbox import TextArea, HPacker, AnnotationBbox
    lab = HPacker(children=[TextArea('頂點', textprops=dict(fontsize=9)),
                            TextArea(vlab, textprops=dict(fontsize=9))],
                  align='baseline', pad=0, sep=3)
    ab = AnnotationBbox(lab, (h, k), xybox=vlab_xy, xycoords='data', boxcoords='data',
                        box_alignment=(0, 0.5), frameon=True, pad=0.15,
                        bboxprops=dict(fc='white', ec='none'),
                        arrowprops=dict(arrowstyle='-', lw=0.8, color='black'))
    ab.set_zorder(6)
    ax.add_artist(ab)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)


def draw_figs():
    # 頂點標註一律放在曲線「外側」的空位（開口向上放頂點下方、向下放上方），引線不貼曲線
    _pgraph(lambda x: (x - 2) ** 2, (-1, 5), (-1, 6), FIGS['h_up'],
            (2, 0), '$(h,0)$', (2.45, -0.95), 4.6)
    _pgraph(lambda x: -(x - 2) ** 2, (-1, 5), (-6, 1), FIGS['h_dn'],
            (2, 0), '$(h,0)$', (2.45, 0.95), -4.6)
    _pgraph(lambda x: (x - 2) ** 2 + 1, (-1, 5), (-1, 6), FIGS['hk_up'],
            (2, 1), '$(h,k)$', (2.45, 0.58), 5.0)
    _pgraph(lambda x: -(x - 2) ** 2 + 3, (-1, 5), (-3, 4), FIGS['hk_dn'],
            (2, 3), '$(h,k)$', (2.45, 4.0), -1.8)


# ================================ 元件 ================================
_RULE_K = [0]


def _ruled_ppr(line, before, ind_left=0):
    """作答線段落格式。Word 會把框線設定完全相同的相鄰段落併成一組、只畫最底一條
    （記憶 docx_adjacent_border_paras_merge；10-08 那份「作答／改正」就中了這個坑）。
    照共用層 write_lines() 的破法：逐行交替 w:space（4/5）與右縮排（0/1 twip）。
    pPr 子元素次序照 schema：pBdr → spacing → ind。"""
    k = _RULE_K[0] = _RULE_K[0] + 1
    return (f'<w:pPr><w:pBdr><w:bottom w:val="single" w:sz="5" w:space="{4 + k % 2}" '
            f'w:color="{LINE_GREY}"/></w:pBdr>'
            f'<w:spacing w:line="{line}" w:lineRule="auto" w:before="{before}" w:after="0"/>'
            f'<w:ind w:left="{ind_left}" w:right="{k % 2}"/></w:pPr>')


def ruled(label='', sz=22, row_sz=28):
    run = _run(label + ' ', sz=sz) if label else ''
    pad = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
           '<w:t xml:space="preserve"> </w:t></w:r>')
    return f'<w:p>{_ruled_ppr(320, 70)}{run}{pad}</w:p>'


def ruled_ind(label, ind=560, row_sz=28):
    """縮排的作答線（配方推導續寫用），開頭放「＝」等記號。"""
    pad = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
           '<w:t xml:space="preserve"> </w:t></w:r>')
    run = _run(label + ' ') if label else ''
    return f'<w:p>{_ruled_ppr(360, 90, ind)}{run}{pad}</w:p>'


def qhead(text):
    return para(text, keep_next=True)


def sub_line(text):
    """多空填充題的一空一行（縮排對齊題幹文字）。"""
    # 行距 1.35 倍（house-style 本文 1.5 倍）：填空行已有底線，略收緊讓練 1 能接在第 1 頁性質表之後
    return para(text, ind=560, keep_next=True).replace(
        '<w:spacing w:line="360" w:lineRule="auto" w:after="80"/>',
        '<w:spacing w:line="324" w:lineRule="auto" w:after="60"/>')


def opts(items, per_line=4):
    out, labels, k = [], 'ABCD', 0
    for r in range(0, len(items), per_line):
        segs = []
        for it in items[r:r + per_line]:
            segs.append(f'{labels[k]}．{it}')
            k += 1
        out.append(para('　　　　'.join(segs), ind=280, spacing=False, keep_next=True))
    return out


def mcbox(stem, options, per_line=4, last=False):
    return problem_box([qhead(stem)] + opts(options, per_line)
                       + [ruled('作答：'), ruled('改正：')], trailing_blank=not last)


def fillbox(lines, last=False):
    if isinstance(lines, str):
        lines = [lines]
    return problem_box([qhead(lines[0])] + [sub_line(t) for t in lines[1:]]
                       + [ruled('改正：')], trailing_blank=not last)


def workbox(head, body, last=False):
    """有推導過程的題：題幹＋推導行（已排好的段落）＋改正。"""
    return problem_box([qhead(head)] + body + [ruled('改正：')], trailing_blank=not last)


def note(text):
    """大題標題下的配分說明；keep_next 免「標題＋說明」孤留頁尾。"""
    return para(text, keep_next=True)


def keep_rows_together(xml):
    """表格除最後一列外，每段加 keepNext——整張表不會被分頁拆開（記憶 docx_table_rows_need_keepnext）。"""
    rows = xml.split('</w:tr>')
    for i in range(len(rows) - 2):
        rows[i] = rows[i].replace('<w:pPr>', '<w:pPr><w:keepNext/>')
    return '</w:tr>'.join(rows)


def cpara(text, bold=False):
    return para(text, bold=bold, jc='center', spacing=False)


def property_table(title, fig_up, fig_dn, vertex, k, media):
    """原稿的「圖像及性質」表，改成 a > 0／a < 0 決策表；表內文字照原稿
    （「減少」統一為「減小」）。"""
    w0 = int(W * 0.18)
    w1 = (W - w0) // 2
    widths = [w0, w1, W - w0 - w1]
    img = lambda f: expand_image(image_para(f, width_cm=4.1), media)
    mid = lambda t: {'p': [cpara(t)], 'va': 'center'}
    rows = [
        [{'p': [cpara(title, bold=True)], 'shd': GREY_FILL, 'span': 3}],
        [{'p': [cpara('')], 'shd': GREY_FILL},
         {'p': [cpara('{a>0}', bold=True)], 'shd': GREY_FILL},
         {'p': [cpara('{a<0}', bold=True)], 'shd': GREY_FILL}],
        [{'p': [cpara('圖像', bold=True)], 'va': 'center'},
         {'p': [img(fig_up)]}, {'p': [img(fig_dn)]}],
        [{'p': [cpara('開口方向', bold=True)], 'va': 'center'},
         mid('開口向上'), mid('開口向下')],
        [{'p': [cpara('頂點坐標', bold=True)], 'va': 'center'},
         {'p': [cpara(vertex, bold=True)], 'va': 'center', 'span': 2}],
        [{'p': [cpara('對稱軸', bold=True)], 'va': 'center'},
         {'p': [cpara('直線 {x=h}', bold=True)], 'va': 'center', 'span': 2}],
        [{'p': [cpara('最值', bold=True)], 'va': 'center'},
         mid(f'當 {{x=h}} 時，函數 {{y}} 有最小值 {k}'),
         mid(f'當 {{x=h}} 時，函數 {{y}} 有最大值 {k}')],
        [{'p': [cpara('增減性', bold=True)], 'va': 'center'},
         {'p': [cpara('當 {x<h} 時，{y} 隨 {x} 的增大而減小'),
                cpara('當 {x>h} 時，{y} 隨 {x} 的增大而增大')], 'va': 'center'},
         {'p': [cpara('當 {x<h} 時，{y} 隨 {x} 的增大而增大'),
                cpara('當 {x>h} 時，{y} 隨 {x} 的增大而減小')], 'va': 'center'}],
    ]
    return keep_rows_together(_tbl(rows, widths))


def six_lines(lead, xv=None):
    """原例 1／練 1（xv＝固定的 x 值）與原例 2／練 6（xv=None：x 的分界也要填）。
    字句照原稿；短的兩空（對稱軸、頂點坐標）同一行，其餘一行一件事。"""
    lt = f'{{x<{xv}}}' if xv is not None else f'{{x<}}{SHORT}'
    gt = f'{{x>{xv}}}' if xv is not None else f'{{x>}}{SHORT}'
    return [lead,
            f'它的對稱軸是：{BLANK}；　頂點坐標：{BLANK}；',
            f'開口方向：{BLANK}；',
            f'當 {lt} 時，{{y}} 隨 {{x}} 的增大而{BLANK}；',
            f'當 {gt} 時，{{y}} 隨 {{x}} 的增大而{BLANK}；',
            f'當 {{x=}}{SHORT} 時，函數 {{y}} 的最{SHORT}值是{BLANK}。']


def three_props():
    return [sub_line(f'開口方向：{MID}；　對稱軸：{MID}；　頂點坐標：{MID}')]


def pair_box(left, right):
    """配方法兩題並排（照原稿「例｜練」左右兩欄的版式）：示範與對應練習必定同一頁。
    left／right：該欄段落 list（題號＋推導行＋作答線＋性質），每欄底部各自有「改正」。"""
    half = W // 2
    bd = ('single', 'single', 'single', 'single')
    cell = lambda ps: {'p': ps + [ruled('改正：')], 'bd': bd}
    return keep_rows_together(_tbl([[cell(left), cell(right)]], [half, W - half]))


def col_q(n, f, derive, n_lines):
    """並排欄內的一題：題號＋函數、推導行、續寫線、三項性質一項一行。"""
    out = [para(f'練 {n}．{{y={f}}}', bold=True, keep_next=True)]
    out += [para(' ' + m, ind=200, keep_next=True) for m in derive]
    out += [ruled_ind('＝', ind=200) for _ in range(n_lines)]
    out += [para(f'{t}：{MID}', ind=200, keep_next=True) for t in ('開口方向', '對稱軸', '頂點坐標')]
    return out


def mline(markup):
    """推導行（縮排；開頭混一個文字空白 run，免 Word 當 display math 置中）。"""
    return para(' ' + markup, ind=560, keep_next=True)


def ratio_table(funcs):
    """原練 7 的三列表格（版式照原稿），放在題框內。"""
    inner = W - 260
    w0 = int(inner * 0.34)
    wr = (inner - w0) // 3
    widths = [w0, wr, wr, inner - w0 - 2 * wr]
    hdr = [{'p': [cpara(t, bold=True)], 'shd': GREY_FILL}
           for t in ('二次函數', '開口方向', '對稱軸', '頂點坐標')]
    rows = [hdr]
    for f in funcs:
        rows.append({'cells': [{'p': [cpara(f)], 'va': 'center'}, {'p': []}, {'p': []},
                               {'p': []}], 'h': 760})
    return _tbl(rows, widths, trailing_blank=False)


def info_box(paragraphs):
    """提示框（平移規律、公式）：框內每段加 keepNext，框後間隔段也 keepNext——
    整個框會跟住下一題同頁，不會孤零零留在頁尾（使用者 2026-10-13：示範與開頭練習放同一頁）。"""
    xml = problem_box(paragraphs)
    xml = xml.replace('<w:pPr>', '<w:pPr><w:keepNext/>').replace('<w:keepNext/><w:keepNext/>',
                                                                '<w:keepNext/>')
    return xml.replace(_SPACER, '<w:p><w:pPr><w:keepNext/><w:spacing w:before="0" w:after="0" '
                                'w:line="200" w:lineRule="exact"/></w:pPr></w:p>')


# ================================ 學生卷 ================================
def student():
    media = MediaRegistry()
    P = [masthead(SUBJECT, UNIT, '課後補救教學'), student_info_row()]
    P.append(para('帶回家完成　　共三大題（19 題）　　滿分 100 分　　'
                  '得分：＿＿＿＿ / 100', bold=True))
    P.append(para('老師批改後，請在每題的「改正」欄完成訂正，下一節帶回。'))

    # ---------------- 二 ----------------
    P.append(heading('一、二次函數 y = a(x − h)² + k 的圖像及性質（44 分）'))
    P.append(note('練 1、練 2 每題 6 分（每行 1 分）；練 3 為 9 分（每格 1 分）；'
                  '選擇題（練 4、5、9）每題 4 分；練 6 為 3 分；練 7、練 8 每題 4 分。'))
    P.append(property_table('二次函數 {y=a(x-h)^2+k} 的圖像及性質',
                            FIGS['hk_up'], FIGS['hk_dn'], '{(h,k)}', '{k}', media))
    P.append(fillbox(six_lines('練 1．已知函數 {y=3(x-4)^2-5}，')))
    P.append(fillbox([f'練 2．函數 {{y=-1/3(x+2)^2+7}}：',
                      f'開口向{MID}；　對稱軸是{MID}；　頂點坐標是{MID}；',
                      f'當 {{x<}}{SHORT} 時，{{y}} 隨 {{x}} 的增大而{BLANK}；',
                      f'當 {{x>}}{SHORT} 時，{{y}} 隨 {{x}} 的增大而{BLANK}；',
                      f'當 {{x=}}{SHORT} 時，函數 {{y}} 的最{SHORT}值是{BLANK}。']))
    P.append(problem_box([qhead('練 3．填寫下表。'),
                          ratio_table(('{y=1/3(x+4)^2}', '{y=-3x^2+5}', '{y=-(x-1)^2-2}')),
                          ruled('改正：')]))
    P.append(mcbox('練 4．拋物線 {y=2(x+3)^2-1} 的開口方向和頂點坐標分別是（　　　）',
                   ['向上，{(3,-1)}', '向上，{(-3,-1)}', '向下，{(-3,-1)}', '向下，{(3,1)}'],
                   per_line=2))
    P.append(mcbox('練 5．二次函數 {y=4(x-5)^2+3} 的對稱軸為（　　　）',
                   ['直線 {x=-5}', '直線 {x=5}', '直線 {x=3}', '直線 {x=-3}'], per_line=2))
    P.append(fillbox(f'練 6．二次函數 {{y=2x^2-8}} 有最{SHORT}值{BLANK}。'))
    P.append(fillbox(['練 7．已知二次函數 {y=2(x-3)^2-4}，寫出二次函數的開口方向、對稱軸、'
                      '頂點坐標及最值。',
                      f'開口方向：{MID}；　對稱軸：{MID}；　頂點坐標：{MID}',
                      f'最值：{BLANK}{BLANK}']))

    P.append(fillbox(f'練 8．若點 {{(4,a)}}、{{(6,b)}} 都在二次函數 {{y=-(x-3)^2}} 的圖像上，'
                     f'則 {{a}}{SHORT}{{b}}（填「＞」、「＜」或「＝」）。'))
    P.append(mcbox('練 9．關於二次函數 {y=3(x+2)^2} 的圖像和性質，下列說法正確的是（　　　）',
                   ['開口方向向上，頂點坐標為 {(2,0)}', '當 {x=-2} 時，函數有最大值 {0}',
                    '當 {x>-2} 時，{y} 隨 {x} 的增大而增大', '開口方向向上，對稱軸為 {y} 軸'],
                   per_line=2))

    # ---------------- 二 ----------------
    P.append(heading('二、拋物線的平移（16 分）'))
    P.append(info_box([
        para('▍平移與頂點', bold=True, keep_next=True),
        para('把 {y=ax^2} 的圖像平移，使頂點由 {(0,0)} 移到 {(h,k)}，'
             '就得到 {y=a(x-h)^2+k} 的圖像。', keep_next=True),
        para('左右看 {h}：{h>0} 向右平移，{h<0} 向左平移。'
             '　上下看 {k}：{k>0} 向上平移，{k<0} 向下平移。', ind=280),
    ]))
    P.append(note('練 10、11、12 每題 4 分；選擇題（練 13）4 分。'))
    P.append(fillbox(f'練 10．函數 {{y=(x+2)^2-5}} 的圖像可由函數 {{y=x^2}} 的圖像向{SHORT}'
                     f'平移 2 個單位，再向{SHORT}平移 5 個單位得到。'))
    P.append(fillbox(f'練 11．已知函數 {{y=-2(x-4)^2+1}} 是由 {{y=-2x^2}} 向{SHORT}平移{SHORT}'
                     f'個單位，再向{SHORT}平移{SHORT}個單位得到的。'))
    P.append(fillbox(f'練 12．函數 {{y=-3x^2}} 向上平移 2 個單位，再向右平移 1 個單位，'
                     f'得到拋物線的函數解析式為{BLANK}{SHORT}。'))
    P.append(mcbox('練 13．將拋物線 {y=(x+1)^2+3} 向右平移 2 個單位，再向下平移 4 個單位，'
                   '得到拋物線的函數解析式為（　　　）',
                   ['{y=(x+3)^2-1}', '{y=(x-1)^2+7}', '{y=(x-1)^2-1}', '{y=(x+3)^2+7}'],
                   per_line=2))

    # ---------------- 三 ----------------
    P.append(heading('三、化為頂點式及求解析式（40 分）'))
    P.append(problem_box([
        para('▍完全平方公式', bold=True, keep_next=True),
        para(' {a^2+2a slot(∆,b)+slot(∎,b^2)=(a+slot(∆,b))^2}　　'
             '{a^2-2a slot(∆,b)+slot(∎,b^2)=(a-slot(∆,b))^2}', jc='center', keep_next=True),
        para('配方時：同一個 ∆ 填同一個數，∎ 是 ∆ 的平方。', ind=280),
    ]))
    P.append(note('練 14、15、16 每題 6 分；練 17、練 18 每題 7 分；練 19 為 8 分。'))
    P.append(qhead('練 14–17．把下列函數化為頂點式 {y=a(x-h)^2+k}，並寫出開口方向、對稱軸及頂點坐標。'))
    P.append(pair_box(
        col_q(14, '2x^2+8x', ['{=2(x^2+4x)}', '{=2(x^2+2·x·slot(∆)+slot(∎)-slot(∎))}',
                              '{=2[(x+slot(∆))^2-slot(∎)]}'], 1),
        col_q(15, '2x^2+4x', ['{=2(x^2+2x)}', '{=2(x^2+2·x·slot(∆)+slot(∎)-slot(∎))}',
                              '{=2[(x+slot(∆))^2-slot(∎)]}'], 1)))
    P.append(pair_box(
        col_q(16, '2x^2+8x-6', ['{=2(x^2+4x)-6}', '{=2(x^2+2·x·slot(∆)+slot(∎)-slot(∎))-6}',
                                '{=2[(x+slot(∆))^2-slot(∎)]-6}'], 2),
        col_q(17, '-2x^2+8x-6', ['{=-2(x^2-4x)-6}'], 4)))
    P.append(info_box([
        para('▍頂點公式', bold=True, keep_next=True),
        para('二次函數 {y=ax^2+bx+c} 的對稱軸是直線 {x=-frac(b,2a)}，', keep_next=True),
        para('頂點坐標是 {(-frac(b,2a),frac(4ac-b^2,4a))}。', ind=280),
    ]))
    P.append(workbox('練 18．已知二次函數 {y=x^2+4x-6}，利用公式求二次函數的開口方向、對稱軸、'
                     '頂點坐標及最值。',
                     [ruled_ind('') for _ in range(3)]
                     + three_props() + [sub_line(f'最值：{BLANK}{BLANK}')]))
    P.append(workbox('練 19．已知拋物線的頂點為 {(1,2)} 且過 {(0,-1)}，求拋物線的解析式。',
                     [ruled_ind('') for _ in range(4)]
                     + [sub_line(f'答：拋物線的解析式為{BLANK}{BLANK}。')], last=True))
    save(P, BASE + '_學生卷.docx', FOOT, media=media)


# ================================ 教師卷 ================================
def ans_tbl(rows, headers=('題（分）', '答案', '解析與評分')):
    w = [int(W * 0.11), int(W * 0.25)]
    w.append(W - sum(w))
    out = [{'cells': [{'p': [para(h, bold=True, sz=22, spacing=False)], 'shd': GREY_FILL}
                      for h in headers], 'hdr': True}]
    for n, a, why in rows:
        a = a if isinstance(a, list) else [a]
        out.append([{'p': [para(n, sz=22, spacing=False)], 'va': 'center'},
                    {'p': [para(x, bold=True, sz=22, spacing=False) for x in a], 'va': 'center'},
                    {'p': [para(why, sz=22, spacing=False)], 'va': 'center'}])
    # 表頭列加 keepNext：免表頭單獨留在頁尾（教師卷第二大題實測）
    xml = _tbl(out, w)
    head, rest = xml.split('</w:tr>', 1)
    return head.replace('<w:pPr>', '<w:pPr><w:keepNext/>') + '</w:tr>' + rest


def wtbl(rows, why_pct=0.40):
    return keep_rows_together(worked_example_table(
        rows, headers=('算式', '說明與建議評分'), why_pct=why_pct))


def sub_title(text):
    return para(text, bold=True, keep_next=True)


def teacher():
    P = [masthead(SUBJECT, UNIT, '課後補救教學・教師卷')]
    P.append(para('本卷供教師批改使用，不發給學生。題目、數字、分值與學生卷完全相同，'
                  '滿分 100 分。練 1–13 為仿原講義題型新命的相似題（原題學生已做過）；'
                  '練 14–19 照原稿。答案全部自行計算，分值為建議分配；'
                  '題目來源與驗算見同資料夾驗算紀錄。'))
    P.append(para('本任務為帶回家作業、下一節訂正；學生卷每題設有「改正」欄，'
                  '批改後請學生在原卷訂正，不必另抄。'))

    P.append(heading('一、二次函數 y = a(x − h)² + k 的圖像及性質（44 分）'))
    P.append(ans_tbl([
        ('練 1（6）', ['直線 x ＝ 4', '(4, −5)', '向上', 'x ＜ 4，減小', 'x ＞ 4，增大',
                      'x ＝ 4，最小值 −5'],
         '每行 1 分；同一行的空格全對才給分。a ＝ 3 ＞ 0，h ＝ 4，k ＝ −5'),
        ('練 2（6）', ['下', '直線 x ＝ −2', '(−2, 7)', 'x ＜ −2，增大', 'x ＞ −2，減小',
                      'x ＝ −2，最大值 7'],
         '每行 1 分，評分同練 1。a ＝ −1/3 ＜ 0，h ＝ −2，k ＝ 7。'
         '※ 與練 1 對照：a ＜ 0，增減方向剛好相反'),
        ('練 3（9）', ['① 向上｜x ＝ −4｜(−4, 0)', '② 向下｜x ＝ 0（y 軸）｜(0, 5)',
                      '③ 向下｜x ＝ 1｜(1, −2)'],
         '每格 1 分。① k ＝ 0；② 沒有 (x − h)，h ＝ 0，對稱軸是 y 軸；'
         '③ a ＝ −1。※ 易錯：① 寫成 (4, 0)'),
        ('練 4（4）', 'B', 'a ＝ 2 ＞ 0 開口向上；(x ＋ 3)² ＝ (x − (−3))²，頂點 (−3, −1)。'
                          '※ 易錯：選 A（h 的符號看反）'),
        ('練 5（4）', 'B', 'h ＝ 5，對稱軸直線 x ＝ 5。※ 易錯：選 A（符號看反）或 C（看了 k）'),
        ('練 6（3）', ['小', '−8'], '「小」1 分、「−8」2 分。a ＝ 2 ＞ 0，頂點 (0, −8) 是最低點'),
        ('練 7（4）', ['向上', '直線 x ＝ 3', '(3, −4)', '最小值 −4'],
         '每項 1 分。a ＝ 2 ＞ 0，h ＝ 3，k ＝ −4；最值要寫明「最小值」'),
        ('練 8（4）', '＞', '代入：a ＝ −(4 − 3)² ＝ −1，b ＝ −(6 − 3)² ＝ −9，所以 a ＞ b。'
                          '（另法：兩點都在對稱軸 x ＝ 3 右側，開口向下，y 隨 x 增大而減小）'
                          '※ 易錯：只比 x 的大小，答「＜」'),
        ('練 9（4）', 'C', 'a ＝ 3 ＞ 0，h ＝ −2。A：頂點應為 (−2, 0)；B：開口向上，'
                          'x ＝ −2 時有最小值 0；D：對稱軸是直線 x ＝ −2'),
    ]))

    P.append(heading('二、拋物線的平移（16 分）'))
    P.append(ans_tbl([
        ('練 10（4）', ['左', '下'], '每空 2 分。頂點由 (0, 0) 移到 (−2, −5)'),
        ('練 11（4）', ['右', '4', '上', '1'], '每空 1 分。頂點由 (0, 0) 移到 (4, 1)'),
        ('練 12（4）', 'y ＝ −3(x − 1)² ＋ 2',
         '頂點由 (0, 0) 移到 (1, 2)，a 不變。全對 4 分；只做對其中一個方向給 2 分。'
         '※ 易錯：寫成 (x ＋ 1)²'),
        ('練 13（4）', 'C', '頂點 (−1, 3) → 右移 2 → (1, 3) → 下移 4 → (1, −1)，'
                           '得 y ＝ (x − 1)² − 1。A：左右方向看反；B：上下方向看反；D：兩個都反'),
    ]))

    P.append(heading('三、化為頂點式及求解析式（40 分）'))
    P.append(para('練 14–16 評分：∆、∎ 填對 2 分，頂點式 1 分，開口方向、對稱軸、頂點坐標各 1 分。',
                  sz=22, keep_next=True))
    P.append(sub_title('練 14．{y=2x^2+8x}（6 分）'))
    P.append(wtbl([
        eq_row('{y}', '{2x^2+8x}'),
        eq_row('', '{2(x^2+4x)}', '提出二次項係數 2'),
        eq_row('', '{2(x^2+2·x·2+4-4)}', '∆ ＝ 4 ÷ 2 ＝ 2，∎ ＝ 2² ＝ 4（2 分）'),
        eq_row('', '{2[(x+2)^2-4]}', ''),
        eq_row('', '{2(x+2)^2-8}', '頂點式 1 分（乘回 2：−4 × 2 ＝ −8）'),
        answer_row('開口向上；對稱軸直線 {x=-2}；頂點 {(-2,-8)}', '各 1 分'),
    ]))
    P.append(sub_title('練 15．{y=2x^2+4x}（6 分）'))
    P.append(wtbl([
        eq_row('{y}', '{2x^2+4x}'),
        eq_row('', '{2(x^2+2x)}', '提出 2'),
        eq_row('', '{2(x^2+2·x·1+1-1)}', '∆ ＝ 1，∎ ＝ 1（2 分）'),
        eq_row('', '{2[(x+1)^2-1]}', ''),
        eq_row('', '{2(x+1)^2-2}', '頂點式 1 分'),
        answer_row('開口向上；對稱軸直線 {x=-1}；頂點 {(-1,-2)}', '各 1 分'),
    ]))
    P.append(sub_title('練 16．{y=2x^2+8x-6}（6 分）'))
    P.append(wtbl([
        eq_row('{y}', '{2x^2+8x-6}'),
        eq_row('', '{2(x^2+4x)-6}', '只對含 x 的兩項提出 2'),
        eq_row('', '{2(x^2+2·x·2+4-4)-6}', '∆ ＝ 2，∎ ＝ 4（2 分）'),
        eq_row('', '{2[(x+2)^2-4]-6}', ''),
        eq_row('', '{2(x+2)^2-8-6}', ''),
        eq_row('', '{2(x+2)^2-14}', '頂點式 1 分。※ 易錯：忘了乘 2，寫成 −4 − 6 ＝ −10'),
        answer_row('開口向上；對稱軸直線 {x=-2}；頂點 {(-2,-14)}', '各 1 分'),
    ]))
    P.append(sub_title('練 17．{y=-2x^2+8x-6}（7 分）'))
    P.append(wtbl([
        eq_row('{y}', '{-2x^2+8x-6}'),
        eq_row('', '{-2(x^2-4x)-6}', '提出 −2，括號內一次項變號'),
        eq_row('', '{-2(x^2-2·x·2+4-4)-6}', '∆ ＝ 2，∎ ＝ 4'),
        eq_row('', '{-2[(x-2)^2-4]-6}', '配方過程 2 分'),
        eq_row('', '{-2(x-2)^2+8-6}', '−2 × (−4) ＝ ＋8'),
        eq_row('', '{-2(x-2)^2+2}', '頂點式 2 分（過程對、末項算錯給 1 分）'),
        answer_row('開口向下；對稱軸直線 {x=2}；頂點 {(2,2)}', '各 1 分'),
    ]))
    P.append(sub_title('練 18．{y=x^2+4x-6}，用頂點公式（7 分）'))
    P.append(wtbl([
        span_row('{a=1}，{b=4}，{c=-6}', '讀係數'),
        eq_row('{x}', '{-frac(b,2a)=-frac(4,2×1)=-2}', '對稱軸 2 分'),
        eq_row('{y}', '{frac(4ac-b^2,4a)=frac(4×1×(-6)-4^2,4×1)=frac(-40,4)=-10}',
               '頂點坐標 2 分'),
        answer_row('開口向上；對稱軸直線 {x=-2}；頂點 {(-2,-10)}；最小值 {-10}',
                   '開口 1 分、最值 2 分。用配方法 (x ＋ 2)² − 10 求得亦給全分'),
    ], why_pct=0.30))
    P.append(sub_title('練 19．頂點 {(1,2)}，過 {(0,-1)}（8 分）'))
    P.append(wtbl([
        eq_row('{y}', '{a(x-1)^2+2}', '設頂點式 2 分'),
        eq_row('{-1}', '{a(0-1)^2+2}', '代入 (0, −1) 2 分'),
        eq_row('{-1}', '{a+2}', ''),
        eq_row('{a}', '{-3}', '求得 a 2 分'),
        answer_row('{y=-3(x-1)^2+2}', '寫出解析式 2 分（寫成 y ＝ −3x² ＋ 6x − 1 亦可）'),
    ]))
    save(P, BASE + '_教師卷.docx', FOOT + '（教師卷）')


if __name__ == '__main__':
    draw_figs()
    student()
    teacher()
    print('OK')
