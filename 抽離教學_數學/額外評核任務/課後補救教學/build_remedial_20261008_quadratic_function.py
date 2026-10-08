# -*- coding: utf-8 -*-
r"""
build_remedial_20261008_quadratic_function.py — 初三數學補救班 課後補救教學（2026-10-08）

來源：使用者提供的 `新任務\練習_二次函數2_初三數學.pdf`（課後輔導講義，原稿日期 2024.3.27，
2 頁：二次函數定義＋例 1–4／練 1–10＋「y = ax²」「y = ax² + k」兩張圖像性質表），
另加使用者對話中貼上的 5 題截圖（原題號 1、2、3、16、17）。

使用者 2026-10-08 指示：只把講義風格統一（套 house-style），**不改題目**；
截圖的 5 題放到適合的位置。

課後補救教學＝題目由使用者自己搵，我只重整＋套 house-style（記憶 extra_assessment_three_categories）。
沿用 09-16／09-24 兩份的做法：學生卷＋教師卷、每題「改正」欄、不用 ★、不用教學設計。
原稿是「例＋練」形式的課後輔導講義、沒有分值。使用者 2026-10-08 第二輪指示：
**例題全部改為練習**（原例 1–4 併入練題連續編號，練 1–19）、**全部設分值，滿分 80 或 100
由我決定** → 滿分 100：選擇題 4 分、單空／雙空填充 5 分、三空填充 6 分、五行填充 10 分
（每行 2 分）；一 26＋二 35＋三 39＝100。

版面改動（只動版面，不動設問與數字）：
1. 兩張性質表改成決策表：欄＝a > 0／a < 0，列＝開口方向／頂點／對稱軸／開口大小
   （house-style「多選一的規則改成決策表」）；原表的圖以 matplotlib 黑白重畫，
   曲線靠線型（實線／虛線／點線）＋圖例區分，不靠顏色。
2. 練 7／練 8（原例 3／原練 3）的五個填空一空一行（house-style「一行講一件事」），字句不變。
3. 例題改為練題，連續重新編號（練 1–19），新舊題號對照見驗算紀錄。
4. 明顯錯字／漏字修正（見驗算紀錄 §一）：「隋」→「隨」、「系數」→「係數」、
   「圖象」→「圖像」、「座標」→「坐標」；原例 1／原練 1 選項 B 原稿漏寫「y =」，補上。
"""
import sys, os, re

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _run, _tbl, _PAGE_CONTENT_WIDTH
from omml_core import MediaRegistry, expand_image

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學（補救班）'
UNIT = '二次函數・概念與 y = ax²、y = ax² + k 的圖像'
BASE = '課後補救教學_初三數學補救班_20261008_二次函數'
FOOT = '初三數學補救班．課後補救教學 2026-10-08'
W = _PAGE_CONTENT_WIDTH
FIG_A = os.path.join(OUT, '_tmp_fig_ax2.png')
FIG_K = os.path.join(OUT, '_tmp_fig_ax2k.png')
BLANK = '＿＿＿＿＿＿＿＿'
SHORT = '＿＿＿＿'

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


def save(P, name, footer, media=None):
    """框與框之間的 blank() 會繼承 Word Normal 的段後 8pt，每個間隔約 1.1 cm；
    本卷 20 多個框，累積起來最後一題被擠到第 6 頁獨佔一頁。改成 10pt 固定行高的細間隔。"""
    P = [x if hasattr(x, 'png_path') else tighten(x).replace(_SPACER, _SPACER_SLIM)
         for x in P]
    build_docx(P, os.path.join(OUT, name), footer_text=footer, media=media)


# ================================ 圖 ================================
def _graph(curves, xr, yr, path, dots=()):
    """黑白座標圖：淺灰格線、帶箭頭的 x／y 軸、曲線靠線型區分、圖例放在圖右外側
    （放圖內一定會壓到其中一條曲線）。"""
    import numpy as np
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams['font.family'] = ['Calibri', 'Microsoft JhengHei']
    plt.rcParams['mathtext.fontset'] = 'stix'
    fig, ax = plt.subplots(figsize=(4.6, 3.5), dpi=220)
    # 軸比刻度範圍多出 0.6 格，箭頭才不會壓住最後一個刻度數字
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
                    fontsize=9, bbox=box, zorder=1.5)
    for t in range(yr[0], yr[1] + 1):
        if t:
            ax.text(-0.14, t, str(t).replace('-', '−'), ha='right', va='center',
                    fontsize=9, bbox=box, zorder=1.5)
    ax.text(xr[1] + 0.55, 0.15, '$x$', ha='right', va='bottom', fontsize=13)
    ax.text(0.18, yr[1] + 0.55, '$y$', ha='left', va='top', fontsize=13)
    ax.text(-0.14, -0.16, '$O$', ha='right', va='top', fontsize=11)
    xs = np.linspace(xr[0], xr[1], 400)
    for f, ls, lab in curves:
        ax.plot(xs, f(xs), color='black', ls=ls, lw=1.9, label=lab)
    for (x, y) in dots:
        ax.plot(x, y, 'o', color='black', ms=4.2, mec='white', mew=0.8, zorder=5)
    leg = ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1.0), fontsize=12,
                    handlelength=3.0, frameon=True, edgecolor='black', fancybox=False)
    leg.get_frame().set_linewidth(0.8)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)


def draw_figs():
    _graph([(lambda x: x ** 2, '-', r'$y=x^2$'),
            (lambda x: -x ** 2, '--', r'$y=-x^2$')],
           (-3, 3), (-4, 4), FIG_A)
    _graph([(lambda x: x ** 2 + 1, '-', r'$y=x^2+1$'),
            (lambda x: x ** 2, '--', r'$y=x^2$'),
            (lambda x: x ** 2 - 1, ':', r'$y=x^2-1$')],
           (-3, 3), (-2, 5), FIG_K, dots=((0, 1), (0, 0), (0, -1)))


# ================================ 元件 ================================
def ruled(label='', sz=22, row_sz=28):
    ppr = ('<w:pPr><w:spacing w:line="320" w:lineRule="auto" w:before="70" w:after="0"/>'
           f'<w:pBdr><w:bottom w:val="single" w:sz="5" w:space="4" w:color="{LINE_GREY}"/>'
           '</w:pBdr></w:pPr>')
    run = _run(label + ' ', sz=sz) if label else ''
    pad = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
           '<w:t xml:space="preserve"> </w:t></w:r>')
    return f'<w:p>{ppr}{run}{pad}</w:p>'


def qhead(text):
    return para(text, keep_next=True)


def sub_line(text):
    """多空填充題的一空一行（縮排對齊題幹文字）。"""
    return para(text, ind=560, keep_next=True)


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


def property_table(title, fig, vertex, media):
    """原稿的「圖像及性質」表，改成 a > 0／a < 0 決策表。"""
    w0 = int(W * 0.20)
    w1 = (W - w0) // 2
    widths = [w0, w1, W - w0 - w1]
    rows = [
        [{'p': [cpara(title, bold=True)], 'shd': GREY_FILL, 'span': 3}],
        [{'p': [expand_image(image_para(fig, width_cm=9.6), media)], 'span': 3}],
        [{'p': [cpara('')], 'shd': GREY_FILL},
         {'p': [cpara('{a>0}', bold=True)], 'shd': GREY_FILL},
         {'p': [cpara('{a<0}', bold=True)], 'shd': GREY_FILL}],
        [{'p': [cpara('開口方向', bold=True)], 'va': 'center'},
         {'p': [cpara('開口向上')], 'va': 'center'},
         {'p': [cpara('開口向下')], 'va': 'center'}],
        [{'p': [cpara('頂點坐標', bold=True), cpara(vertex, bold=True)], 'va': 'center'},
         {'p': [cpara('頂點是拋物線的最低點')], 'va': 'center'},
         {'p': [cpara('頂點是拋物線的最高點')], 'va': 'center'}],
        [{'p': [cpara('對稱軸', bold=True)], 'va': 'center'},
         {'p': [cpara('{y} 軸（{x=0}）')], 'va': 'center', 'span': 2}],
        [{'p': [cpara('開口大小', bold=True)], 'va': 'center'},
         {'p': [cpara('{|a|} 越大，拋物線的開口越小')], 'va': 'center', 'span': 2}],
    ]
    return keep_rows_together(_tbl(rows, widths))


def five_blanks(lead):
    """原例 3／原練 3：五個填空一空一行（字句照原稿）。"""
    return [lead,
            f'它的對稱軸是：{BLANK}；',
            f'頂點坐標：{BLANK}；',
            f'開口方向：{BLANK}；',
            f'當 {{x>0}} 時，{{y}} 隨 {{x}} 的增大而{BLANK}；',
            f'當 {{x=}}{SHORT} 時，函數 {{y}} 的最{SHORT}值是{BLANK}。']


# ================================ 學生卷 ================================
def student():
    media = MediaRegistry()
    P = [masthead(SUBJECT, UNIT, '課後補救教學'), student_info_row()]
    P.append(para('帶回家完成　　共三大題（19 題）　　滿分 100 分　　'
                  '得分：＿＿＿＿ / 100', bold=True))
    P.append(para('老師批改後，請在每題的「改正」欄完成訂正，下一節帶回。'))

    # ---------------- 一 ----------------
    P.append(heading('一、二次函數的概念（26 分）'))
    P.append(problem_box([
        para('▍二次函數', bold=True, keep_next=True),
        para('{y=ax^2+bx+c}　（{a}，{b}，{c} 是常數，{a!=0}）', jc='center', keep_next=True),
        para('一般地，形如上式的函數叫做二次函數。其中：', keep_next=True),
        para('{x} 是自變量　　{a} 是二次項係數　　{b} 是一次項係數　　{c} 是常數項',
             ind=280),
    ]))
    P.append(note('選擇題（練 1、2、3、6）每題 4 分；填充題（練 4、5）每題 5 分。'))
    P.append(mcbox('練 1．下列函數中，是二次函數的是（　　　）',
                   ['{y=x+1}', '{y=1/x^2}', '{y=-x^2+1}', '{y=(x+1)^2-x^2}']))
    P.append(mcbox('練 2．下列函數中，是二次函數的是（　　　）',
                   ['{y=x}', '{y=2/x}', '{y=-x^2}', '{y=x-2}']))
    P.append(mcbox('練 3．下列關係式中 {y} 是 {x} 的二次函數的是（　　　）',
                   ['{y=1/3x^2}', '{y=sqrt(x^2-1)}', '{y=1/x^2}', '{y=ax^2}']))
    P.append(fillbox(f'練 4．若 {{y=(1-m)x^{{m^2+1}}}} 是二次函數，則 {{m=}}{BLANK}。'))
    P.append(fillbox(f'練 5．如果函數 {{y=mx^{{m-2}}+x}} 是關於 {{x}} 的二次函數，'
                     f'則 {{m=}}{BLANK}。'))
    P.append(mcbox('練 6．若函數 {y=(a-2)x^{|a|}-x+3} 是關於 {x} 的二次函數，'
                   '則 {a} 的值是（　　　）', ['2', '−2', '±2', '0']))

    # ---------------- 二 ----------------
    P.append(heading('二、二次函數 y = ax² 的圖像及性質（35 分）'))
    P.append(property_table('二次函數 {y=ax^2} 的圖像及性質', FIG_A, '{(0,0)}', media))
    P.append(note('練 7、練 8 每題 10 分（每行 2 分）；練 9、10、11 每題 5 分。'))
    P.append(fillbox(five_blanks('練 7．已知函數 {y=1/3x^2}，不畫圖像，其圖像是拋物線，')))
    P.append(fillbox(five_blanks('練 8．已知函數 {y=-1/3x^2}，不畫圖像，其圖像是拋物線，')))
    P.append(fillbox(f'練 9．拋物線 {{y=3x^2}} 的開口向{SHORT}、對稱軸是{BLANK}。'))
    P.append(fillbox(f'練 10．拋物線 {{y=-1/2x^2}} 的頂點坐標為{BLANK}。'))
    P.append(fillbox(f'練 11．已知拋物線 {{y=ax^2}} 的開口向下，且 {{|a|=3}}，則 {{a=}}{BLANK}。'))

    # ---------------- 三 ----------------
    P.append(heading('三、二次函數 y = ax² + k 的圖像及性質（39 分）'))
    P.append(property_table('二次函數 {y=ax^2+k} 的圖像及性質', FIG_K, '{(0,k)}', media))
    P.append(note('選擇題（練 16、17）每題 4 分；練 15 為 6 分；其餘填充題每題 5 分。'))
    P.append(fillbox(f'練 12．拋物線 {{y=3x^2+2}} 的頂點坐標為{BLANK}；對稱軸是{BLANK}。'))
    P.append(fillbox(f'練 13．拋物線 {{y=3x^2+4}} 的頂點坐標為{BLANK}；對稱軸是{BLANK}。'))
    P.append(fillbox(f'練 14．拋物線 {{y=x^2-9}} 的頂點坐標為{BLANK}。'))
    P.append(fillbox(f'練 15．二次函數 {{y=-1/2x^2+5}} 有最{SHORT}值為{BLANK}；'
                     f'開口向{SHORT}。'))
    P.append(mcbox('練 16．關於拋物線 {y=-x^2+2}，下列說法正確的是（　　　）',
                   ['開口向上', '對稱軸是 {y} 軸', '有最小值',
                    '當 {x<0} 時，函數 {y} 隨 {x} 的增大而減小'], per_line=2))
    P.append(mcbox('練 17．比較二次函數 {y=3x^2} 與 {y=-1/3x^2+1} 的圖像，則（　　　）',
                   ['開口大小相同', '開口方向相同', '對稱軸相同', '頂點坐標相同'],
                   per_line=2))
    P.append(fillbox(f'練 18．已知點 {{M(-1,m)}} 在二次函數 {{y=2x^2+1}} 的圖像上，'
                     f'則 {{m}} 的值為{BLANK}。'))
    P.append(fillbox(f'練 19．已知 {{y=x^2-2x-3}}，則函數與 {{y}} 軸的交點坐標為{BLANK}。',
                     last=True))
    save(P, BASE + '_學生卷.docx', FOOT, media=media)


# ================================ 教師卷 ================================
def ans_tbl(rows, headers=('題（分）', '答案', '解析與評分')):
    w = [int(W * 0.11), int(W * 0.22)]
    w.append(W - sum(w))
    out = [{'cells': [{'p': [para(h, bold=True, sz=22, spacing=False)], 'shd': GREY_FILL}
                      for h in headers], 'hdr': True}]
    for n, a, why in rows:
        a = a if isinstance(a, list) else [a]
        out.append([{'p': [para(n, sz=22, spacing=False)], 'va': 'center'},
                    {'p': [para(x, bold=True, sz=22, spacing=False) for x in a], 'va': 'center'},
                    {'p': [para(why, sz=22, spacing=False)], 'va': 'center'}])
    return _tbl(out, w)


def wtbl(rows, why_pct=0.40, col_frac=None):
    return keep_rows_together(worked_example_table(
        rows, headers=('算式', '說明與建議評分'), why_pct=why_pct, col_frac=col_frac))


def sub_title(text):
    return para(text, bold=True, keep_next=True)


COLS = (0.300, 0.060, 0.120, 0.080, 0.140, 0.060)


def teacher():
    P = [masthead(SUBJECT, UNIT, '課後補救教學・教師卷')]
    P.append(para('本卷供教師批改使用，不發給學生。題目、數字、分值與學生卷完全相同，'
                  '滿分 100 分。原稿未附答案與評分準則，以下答案全部自行計算，'
                  '分值為建議分配。新舊題號對照見同資料夾驗算紀錄。'))
    P.append(para('本任務為帶回家作業、下一節訂正；學生卷每題設有「改正」欄，'
                  '批改後請學生在原卷訂正，不必另抄。'))

    P.append(heading('一、二次函數的概念（26 分）'))
    P.append(ans_tbl([
        ('練 1（4）', 'C', 'A 是一次函數；B 分母含 x；D 展開後 (x + 1)² − x² ＝ 2x + 1，'
                          '是一次函數。※ 易錯：選 D（看見平方就以為是二次）'),
        ('練 2（4）', 'C', 'A、D 是一次函數；B 分母含 x'),
        ('練 3（4）', 'A', 'B 根號內含 x；C 分母含 x；D 沒有說明 a ≠ 0，'
                          'a ＝ 0 時不是二次函數。※ 易錯：選 D'),
    ]))
    P.append(sub_title('練 4．{y=(1-m)x^{m^2+1}} 是二次函數，求 {m}（5 分）'))
    P.append(wtbl([
        span_row('二次函數要同時符合：① 指數等於 2　② 二次項係數不等於 0', None),
        eq_row('{m^2+1}', '{2}', '① 指數等於 2'),
        eq_row('{m^2}', '{1}', '移項'),
        or_row('{m_1}', '{1}', '{m_2}', '{-1}', '開平方分兩支'),
        span_row('{1-m!=0}，即 {m!=1}', '② 二次項係數不等於 0'),
        span_row('{m_1=1} 不合，捨去', '代 m ＝ 1 入係數得 0'),
        answer_row('{m=-1}', '檢查：此時 y ＝ 2x²'),
    ], col_frac=COLS))
    P.append(para('※ 填充題只看最後答案：寫 m ＝ −1 給 5 分；寫 m ＝ ±1（漏了檢查係數）給 2 分。',
                  sz=22))
    P.append(ans_tbl([
        ('練 5（5）', 'm ＝ 4', '指數 m − 2 ＝ 2，得 m ＝ 4；二次項係數 m ＝ 4 ≠ 0，符合'
                              '（此時 y ＝ 4x² ＋ x）'),
    ]))
    P.append(sub_title('練 6．{y=(a-2)x^{|a|}-x+3} 是二次函數，求 {a}（4 分）　答：B'))
    P.append(wtbl([
        eq_row('{|a|}', '{2}', '① 指數等於 2'),
        or_row('{a_1}', '{2}', '{a_2}', '{-2}', '絕對值等於 2 的數有兩個'),
        span_row('{a-2!=0}，即 {a!=2}', '② 二次項係數不等於 0'),
        span_row('{a_1=2} 不合，捨去', '※ 易錯：選 C（漏了檢查係數）'),
        answer_row('{a=-2}，選 B', '選擇題答對即給 4 分；檢查：此時 y ＝ −4x² − x ＋ 3'),
    ], col_frac=COLS))

    P.append(heading('二、二次函數 y = ax² 的圖像及性質（35 分）'))
    P.append(ans_tbl([
        ('練 7（10）', ['y 軸（x ＝ 0）', '(0, 0)', '向上', '增大', 'x ＝ 0，最小值 0'],
         '每行 2 分；第五行三空全對才給 2 分。a ＝ 1/3 ＞ 0：開口向上，頂點 (0, 0) 是最低點，'
         '所以 x ＝ 0 時 y 有最小值 0；對稱軸右側（x ＞ 0）圖像上升'),
        ('練 8（10）', ['y 軸（x ＝ 0）', '(0, 0)', '向下', '減小', 'x ＝ 0，最大值 0'],
         '每行 2 分，評分同練 7。a ＝ −1/3 ＜ 0：開口向下，頂點 (0, 0) 是最高點，'
         '所以 x ＝ 0 時 y 有最大值 0；對稱軸右側（x ＞ 0）圖像下降。'
         '※ 與練 7 逐空對照，只差 a 的正負'),
        ('練 9（5）', ['上', 'y 軸（x ＝ 0）'], '開口 2 分、對稱軸 3 分。a ＝ 3 ＞ 0'),
        ('練 10（5）', '(0, 0)', 'y ＝ ax² 的頂點必為原點，與 a 的值無關'),
        ('練 11（5）', 'a ＝ −3', '|a| ＝ 3 → a ＝ 3 或 a ＝ −3；開口向下 → a ＜ 0，取 a ＝ −3。'
                               '寫 ±3 給 2 分'),
    ]))

    P.append(heading('三、二次函數 y = ax² + k 的圖像及性質（39 分）'))
    P.append(ans_tbl([
        ('練 12（5）', ['(0, 2)', 'y 軸（x ＝ 0）'], '頂點 3 分、對稱軸 2 分。k ＝ 2，頂點 (0, k)'),
        ('練 13（5）', ['(0, 4)', 'y 軸（x ＝ 0）'], '頂點 3 分、對稱軸 2 分。k ＝ 4'),
        ('練 14（5）', '(0, −9)', 'k ＝ −9。※ 易錯：寫成 (0, 9)（漏了負號），不給分'),
        ('練 15（6）', ['大', '5', '下'], '每空 2 分。a ＝ −1/2 ＜ 0：開口向下，'
                                         '頂點 (0, 5) 是最高點，最大值為 5'),
        ('練 16（4）', 'B', 'a ＝ −1 ＜ 0：開口向下（A 錯）、有最大值（C 錯）；'
                           '對稱軸左側（x ＜ 0）圖像上升，y 隨 x 的增大而增大（D 錯）'),
        ('練 17（4）', 'C', '兩者對稱軸都是 y 軸。A：|3| ≠ |−1/3|，開口大小不同；'
                           'B：一個向上、一個向下；D：頂點 (0, 0) 與 (0, 1)'),
        ('練 18（5）', 'm ＝ 3', '把 x ＝ −1 代入 y ＝ 2x² ＋ 1：2 × (−1)² ＋ 1 得 3，'
                               '所以 m ＝ 3'),
        ('練 19（5）', '(0, −3)', '與 y 軸相交的點 x ＝ 0；代入得 y ＝ −3。'
                                 '※ 易錯：寫成 (−3, 0)（橫、縱坐標對調），不給分'),
    ]))
    save(P, BASE + '_教師卷.docx', FOOT + '（教師卷）')


if __name__ == '__main__':
    draw_figs()
    student()
    teacher()
    print('OK')
