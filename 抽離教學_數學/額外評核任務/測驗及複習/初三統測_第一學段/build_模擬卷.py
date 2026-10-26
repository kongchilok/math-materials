# -*- coding: utf-8 -*-
r"""
build_模擬卷.py — 初三數學統測（第一學段，2026-11-09 實施）模擬卷（學生卷＋教師卷）

來源：同資料夾《2627初三數學科統測 (調40%).docx》（與「調50%」那份 document.xml 逐位元組相同）。
使用者 2026-10-26 指定：
  1. 出第 1–27 題（A 部 1–26 共 95 分＋B 部第 27 題 8 分＝103 分）；第 28、29 題不出。
  2. 照原卷題型與鷹架改數字（第 5 題判別式提示、第 22 題四步框、第 23／24／26 題「解：設…」框照留）。
  3. 第 27 題加框架（讀係數 → Δ → 範圍；兩根和積 → 代入 → 檢驗）。
我另外定的：
  - 選擇題正確選項的位置刻意與原卷錯開（13 題無一相同），學生背模擬卷答案字母不會「撞中」統測；
    第 5、13 題因此重排了選項次序。
  - 原卷第 26(2) 題框「再把點 (3,0) 代入」是抄錯（拱橋水面寬 4 米，應是 B(2,0)）；
    模擬卷改為「再把點 B（＿, ＿）代入」，由學生自己填。
  - 限時 70 分鐘（原卷 80 分鐘／120 分，本卷少了 17 分）。
逐題驗算見《驗算_初三數學統測.md》。

版面層借用 課後補救教學 資料夾 10-15／10-22 兩份腳本的元件（同為初三、同一套題框樣式）。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REMEDIAL = os.path.normpath(os.path.join(HERE, '..', '..', '課後補救教學'))
sys.path.insert(0, REMEDIAL)
from build_remedial_20261015_quadratic_vertex_form import (  # noqa: E402
    para, heading, masthead, student_info_row, image_para, expand_image, build_docx,
    MediaRegistry, _tbl, W, BLANK, SHORT, MID, ruled_ind, qhead, sub_line, note,
    cpara, ans_tbl as _ans_tbl, sub_title, worked_example_table, keep_rows_together, eq_row, span_row, answer_row, GREY_FILL,
    tighten, _SPACER, _SPACER_SLIM, _SPACER_TINY)
from build_remedial_20261022_mock_test import (  # noqa: E402
    problem_box, opts, img_row, grid_figure, _plt, _arrow_axes)

SUBJECT = '初三數學'
UNIT = '統測模擬卷（一元二次方程、二次函數）'
BASE = '模擬卷_初三數學統測'
FOOT = '初三數學．統測模擬卷'
MINUTES = 70
PAREN = '（　　　）'
FIG = {k: os.path.join(HERE, f'_tmp_fig_{k}.png')
       for k in ('q7', 'q8', 'q10A', 'q10B', 'q10C', 'q10D', 'q13', 'q17', 'q25', 'q26')}


def save(P, name, footer, media=None):
    """同 10-15 那份的 save()，但輸出到本資料夾。"""
    P = [x if hasattr(x, 'png_path') else tighten(x).replace(_SPACER, _SPACER_SLIM) for x in P]
    if not hasattr(P[-1], 'png_path') and P[-1].endswith(_SPACER_SLIM):
        P[-1] = P[-1][:-len(_SPACER_SLIM)] + _SPACER_TINY
    build_docx(P, os.path.join(HERE, name), footer_text=footer, media=media)


# ================================ 圖 ================================
def lawn_figure(path):
    """第 7 題：24 m × 14 m 空地，四周等寬草坪帶（灰）圍住中間的表演區。"""
    from matplotlib.patches import Rectangle, FancyArrowPatch
    plt = _plt()
    fig, ax = plt.subplots(figsize=(3.0, 2.0), dpi=300)
    ax.set_xlim(-2.2, 24.6); ax.set_ylim(-4.0, 14.6); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Rectangle((0, 0), 24, 14, fc='#c8c8c8', ec='black', lw=1.2))
    ax.add_patch(Rectangle((3, 3), 18, 8, fc='white', ec='black', lw=1.0))
    ax.text(12, 7, '表演區', ha='center', va='center', fontsize=11)
    kw = dict(arrowstyle='<|-|>', mutation_scale=8, lw=0.8, color='black')
    ax.add_patch(FancyArrowPatch((0, -1.4), (24, -1.4), **kw))
    ax.text(12, -1.9, '24', ha='center', va='top', fontsize=10, bbox=dict(fc='white', ec='none', pad=0.5))
    ax.add_patch(FancyArrowPatch((-1.0, 0), (-1.0, 14), **kw))
    ax.text(-1.0, 7, '14', ha='center', va='center', fontsize=10, bbox=dict(fc='white', ec='none', pad=0.8))
    fig.savefig(path, bbox_inches='tight', pad_inches=0.03); plt.close(fig)


def road_figure(path):
    """第 8 題：60 m × 40 m 矩形場地，一橫一縱兩條等寬道路（灰）。"""
    from matplotlib.patches import Rectangle
    plt = _plt()
    fig, ax = plt.subplots(figsize=(2.9, 2.1), dpi=300)
    ax.set_xlim(-6, 61); ax.set_ylim(-6, 41); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Rectangle((40, 0), 4, 40, fc='#b4b4b4', ec='none'))
    ax.add_patch(Rectangle((0, 22), 60, 4, fc='#b4b4b4', ec='none'))
    ax.add_patch(Rectangle((0, 0), 60, 40, fc='none', ec='black', lw=1.2))
    ax.text(30, -1.5, '60 米', ha='center', va='top', fontsize=9)
    ax.text(-1.5, 20, '40 米', ha='right', va='center', fontsize=9)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.03); plt.close(fig)


def option_sketch(kind, path, size=1.5):
    """第 10 題選項示意圖（照原卷四款：拋物線上／下、橫放拋物線、兩條射線），無刻度。"""
    import numpy as np
    plt = _plt()
    xr, yr = (-3.2, 3.2), (-4.6, 4.6)
    fig, ax = plt.subplots(figsize=(size, size * 1.05), dpi=300)
    ax.set_xlim(*xr); ax.set_ylim(*yr)
    if kind == 'up':
        xs = np.linspace(-1.2, 1.2, 300); ys = 3 * xs ** 2; o = (-0.18, -0.25)
    elif kind == 'down':
        xs = np.linspace(-1.2, 1.2, 300); ys = -3 * xs ** 2; o = (-0.18, 0.25)
    elif kind == 'side':
        ys = np.linspace(-1.75, 1.75, 300); xs = ys ** 2; o = (-0.18, -0.25)
    else:  # 'vdown'：兩條由原點向下的射線
        xs = np.array([-1.1, 0, 1.1]); ys = np.array([-4.3, 0, -4.3]); o = (-0.18, 0.25)
    _arrow_axes(ax, xr, yr, fs=11, o_pos=o)
    ys = np.where((ys < yr[0] + 0.1) | (ys > yr[1] - 0.3), np.nan, ys)
    ax.plot(xs, ys, color='black', lw=1.6)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.03); plt.close(fig)


def roots_figure(path):
    """第 13 題：開口向下、與 x 軸交於 x1 < 0 < x2 的拋物線（不標數值）。"""
    import numpy as np
    plt = _plt()
    xr, yr = (-3.2, 3.6), (-2.6, 3.4)
    fig, ax = plt.subplots(figsize=(2.0, 1.8), dpi=300)
    ax.set_xlim(*xr); ax.set_ylim(*yr)
    _arrow_axes(ax, xr, yr, fs=11, o_pos=(-0.12, -0.18))
    xs = np.linspace(-2.6, 3.4, 300); ys = -0.6 * (xs + 1.5) * (xs - 2.3)
    ax.plot(xs, np.where(ys < yr[0] + 0.1, np.nan, ys), color='black', lw=1.6)
    # 標籤放在兩根「之間」的 x 軸下方：那裏沒有曲線
    ax.text(-1.35, -0.2, '$x_1$', ha='left', va='top', fontsize=11)
    ax.text(2.15, -0.2, '$x_2$', ha='right', va='top', fontsize=11)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.03); plt.close(fig)


def neg_square_figure(path):
    """第 17 題：y = −x² 的圖像（照原卷第 17 題圖的樣式：無刻度、過原點）。"""
    import numpy as np
    plt = _plt()
    xr, yr = (-2.6, 2.6), (-4.4, 1.2)
    fig, ax = plt.subplots(figsize=(1.7, 1.8), dpi=300)
    ax.set_xlim(*xr); ax.set_ylim(*yr)
    _arrow_axes(ax, xr, yr, fs=11, o_pos=(-0.12, 0.12))
    xs = np.linspace(-2.05, 2.05, 300)
    ax.plot(xs, -xs ** 2, color='black', lw=1.6)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.03); plt.close(fig)


def bridge_figure(path):
    """第 26 題：拋物線拱橋，拱頂 C 距水面 4、水面寬 8；坐標系原點在水面中點，A、B 在 x 軸上。"""
    import numpy as np
    from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle
    plt = _plt()
    fig, ax = plt.subplots(figsize=(3.4, 2.5), dpi=300)
    ax.set_xlim(-7.4, 7.8); ax.set_ylim(-3.2, 6.6); ax.set_aspect('equal'); ax.axis('off')
    f = lambda t: -0.25 * t ** 2 + 4
    # 橋身（灰）＋拱洞（白）：拱線延到水面下 1.6 單位
    ax.add_patch(Rectangle((-6.4, -1.6), 12.8, 7.0, fc='#d2d2d2', ec='black', lw=1.0))
    xb = np.sqrt((4 + 1.6) / 0.25)
    xs = np.linspace(-xb, xb, 300)
    ax.add_patch(Polygon(np.c_[xs, f(xs)], closed=True, fc='white', ec='black', lw=1.4))
    for yy in (-0.8, -1.25):
        ax.plot([-4.2, 4.2], [yy, yy], color='black', lw=0.7, ls=(0, (4, 2)))
    # 坐標軸
    ax.add_patch(FancyArrowPatch((-7.2, 0), (7.6, 0), arrowstyle='-|>', mutation_scale=9, lw=0.9))
    ax.add_patch(FancyArrowPatch((0, -3.0), (0, 6.4), arrowstyle='-|>', mutation_scale=9, lw=0.9))
    ax.text(7.6, -0.25, '$x$', ha='right', va='top', fontsize=11)
    ax.text(0.25, 6.4, '$y$', ha='left', va='top', fontsize=11)
    ax.text(0.2, -0.12, '$O$', ha='left', va='top', fontsize=10)
    ax.text(-4.15, 0.2, '$A$', ha='right', va='bottom', fontsize=11)
    ax.text(4.15, 0.2, '$B$', ha='left', va='bottom', fontsize=11)
    ax.text(0.25, 4.15, '$C$', ha='left', va='bottom', fontsize=11)
    kw = dict(arrowstyle='<|-|>', mutation_scale=7, lw=0.8, color='black')
    ax.add_patch(FancyArrowPatch((-1.0, 0), (-1.0, 4), **kw))
    ax.text(-1.25, 2.0, '4', ha='right', va='center', fontsize=10)
    ax.add_patch(FancyArrowPatch((-4, -2.3), (4, -2.3), **kw))
    ax.plot([-4, -4], [-2.6, 0], color='black', lw=0.5)
    ax.plot([4, 4], [-2.6, 0], color='black', lw=0.5)
    ax.text(1.0, -2.45, '8', ha='center', va='top', fontsize=10,
            bbox=dict(fc='white', ec='none', pad=0.4))
    fig.savefig(path, bbox_inches='tight', pad_inches=0.03); plt.close(fig)


def draw_figs():
    lawn_figure(FIG['q7'])
    road_figure(FIG['q8'])
    for c, kind in zip('ABCD', ('up', 'down', 'side', 'vdown')):
        option_sketch(kind, FIG[f'q10{c}'])
    roots_figure(FIG['q13'])
    neg_square_figure(FIG['q17'])
    grid_figure(FIG['q25'], xr=(-5, 5), yr=(-5, 5))
    bridge_figure(FIG['q26'])


# ================================ 元件 ================================
def mc(n, stem, options, per_line=4):
    return problem_box([qhead(f'{n}．{stem}{PAREN}')] + opts(options, per_line))


def side(left, img, media, width_cm, pct=0.62):
    """左文右圖（無框）。"""
    inner = W - 260
    wl = int(inner * pct)
    return _tbl([[{'p': left, 'va': 'center'},
                  {'p': [expand_image(image_para(img, width_cm=width_cm), media)]}]],
                [wl, inner - wl], border='none', trailing_blank=False)


def end(xml):
    """題框最後一段拿走 keepNext：否則整個題框會黏住下一題一齊跳頁（初版 10 頁有 4 頁只用半頁）。"""
    return xml.replace('<w:keepNext/>', '')


def wtbl(rows, why_pct=0.34):
    """教師卷算式表：沒有「或」兩支並排，左式欄放闊（預設 0.23 會把 (x−2)(x−4) 擠斷行）。"""
    return keep_rows_together(worked_example_table(
        rows, headers=('算式', '說明與建議評分'), why_pct=why_pct,
        col_frac=(0.40, 0.05, 0.47, 0.03, 0.02, 0.02)))


def _txt(a):
    """純數學式的段落 Word 會當 display math 置中；前面補一個文字空白就靠左。"""
    return ' ' + a if a.startswith('{') else a


def ans_tbl(rows):
    return _ans_tbl([(n, [_txt(x) for x in a] if isinstance(a, list) else _txt(a), why)
                     for n, a, why in rows])


def lines(n, ind=560):
    return [ruled_ind('', ind=ind) for _ in range(n)]


def sub(text):
    """小題題幹（縮排、keepNext）。"""
    return para(text, ind=280, keep_next=True)


def value_table(xs):
    inner = W - 260
    w0 = int(inner * 0.12)
    cols = ['…'] + [f'{{{t}}}' for t in xs] + ['…']
    wr = (inner - w0) // len(cols)
    widths = [w0] + [wr] * (len(cols) - 1) + [inner - w0 - wr * (len(cols) - 1)]
    rows = [[{'p': [cpara('{x}', bold=True)], 'shd': GREY_FILL}]
            + [{'p': [cpara(t)], 'va': 'center'} for t in cols],
            {'cells': [{'p': [cpara('{y}', bold=True)], 'shd': GREY_FILL, 'va': 'center'}]
             + [{'p': [cpara('…' if t == '…' else '')], 'va': 'center'} for t in cols],
             'h': 620}]
    return _tbl(rows, widths, trailing_blank=False)


# ================================ 學生卷 ================================
def student():
    media = MediaRegistry()
    P = [masthead(SUBJECT, UNIT, '模擬卷'), student_info_row()]
    P.append(para(f'全卷 103 分　　限時 {MINUTES} 分鐘　　得分：＿＿＿＿ / 103', bold=True))
    P.append(para('選擇題把字母寫在題目的括號內；填空題寫在橫線上；解答題要寫出詳細解題過程，'
                  '答案要化到最簡。不可使用計算機。'))

    P.append(heading('A 部（共 95 分）'))
    # ---------------- 單選題 ----------------
    P.append(heading('一、單選題（共 26 分，每題 2 分）'))
    P.append(mc(1, '方程 {3x^2-4x+7=0} 的二次項係數 ({a})、一次項係數 ({b})、常數項 ({c}) 分別為',
                ['{3}，{-4}，{7}', '{4}，{3}，{7}', '{3}，{-4}，{-7}', '{3}，{4}，{-7}']))
    P.append(mc(2, '將方程 {x^2+4x-5=2x} 化成一元二次方程的一般形式，正確的是',
                ['{x^2+6x-5=0}', '{x^2-2x-5=0}', '{x^2+2x-5=0}', '{x^2+2x+5=0}'], 2))
    P.append(mc(3, '已知 {(m+2)x^2-3x+1=0} 是關於 {x} 的一元二次方程，則實數 {m} 的取值範圍是',
                ['{m≥-2}', '{m≠2}', '{m≤-2}', '{m≠-2}']))
    P.append(mc(4, '一元二次方程 {x(x+4)=0} 的根是',
                ['{x_1=0}，{x_2=4}', '{x_1=0}，{x_2=-4}',
                 '{x_1=0}，{x_2=frac(1,4)}', '{x_1=0}，{x_2=-frac(1,4)}'], 2))
    P.append(mc(5, '一元二次方程 {x^2+3x-4=0} 的根的情況是（提示：利用判別式）',
                ['沒有實數根', '有兩個相等的實數根', '有兩個不相等的實數根', '只有一個實數根'], 2))
    P.append(mc(6, '若用公式法解關於 {x} 的一元二次方程 {3x^2+5x-2=0}，則其根為',
                ['{x=frac(5±sqrt(5^2-4×3×(-2)),2×3)}', '{x=frac(-5±sqrt(5^2-4×3×(-2)),2×3)}',
                 '{x=frac(-5±sqrt((-2)^2-4×3×5),2×3)}', '{x=frac(-5±sqrt(5^2-4×3×(-2)),2)}'], 2))
    P.append(problem_box([
        qhead('7．某活動計劃在會議中心前方一塊長 24 米、寬 14 米的矩形空地上佈置一個矩形的表演區，'
              '表演區四周鋪設寬度相等的草坪帶（如圖陰影部分）。若要求表演區的面積為 200 平方米，'
              f'設草坪帶的寬度為 {{x}} 米，則下列方程正確的是{PAREN}'),
        side(opts(['{(24-2x)(14-2x)=200}', '{(24-x)(14-x)=200}',
                   '{(24-2x)(14-x)=200}', '{(24-x)(14-2x)=200}'], 1), FIG['q7'], media, 5.2)]))
    P.append(problem_box([
        qhead('8．如圖，在長為 60 米、寬為 40 米的矩形場地上修建兩條寬度相等且互相垂直的道路，'
              '剩餘部分進行綠化，要使綠化面積為 2109 平方米，則道路的寬應為多少米？'
              f'設道路的寬為 {{x}} 米，則可列方程為{PAREN}'),
        side(opts(['{60×40-60x-40x=2109}', '{(60-x)(40-x)+x^2=2109}',
                   '{60x+40x=60×40-2109}', '{(60-x)(40-x)=2109}'], 1), FIG['q8'], media, 5.0)]))
    P.append(mc(9, '下列函數是二次函數的是',
                ['{y=frac(2,x^2)}', '{y=4x-3}', '{y=frac(3,5x)}', '{y=-x^2+1}']))
    P.append(problem_box([qhead(f'10．下列圖像中，可能是二次函數 {{y=-3x^2}} 的圖像的是{PAREN}'),
                          img_row([FIG[f'q10{c}'] for c in 'ABCD'], media, 3.3)]))
    P.append(mc(11, '拋物線 {y=2x^2-3} 的開口方向是', ['向上', '向下', '向左', '向右']))
    P.append(mc(12, '二次函數 {y=(x+3)^2-4} 的最小值是', ['{3}', '{-3}', '{4}', '{-4}']))
    P.append(problem_box([
        qhead(f'13．若拋物線 {{y=ax^2+bx+c}} 的圖像如右圖所示，則方程 {{ax^2+bx+c=0}} '
              f'的實數根的情況是{PAREN}'),
        side(opts(['方程有兩個相等的實數根', '方程有兩個不相等的實數根',
                   '方程沒有實數根', '方程的實數根情況不確定'], 1), FIG['q13'], media, 3.6)]))

    # ---------------- 填空題 ----------------
    P.append(heading('二、填空題（共 26 分，每格 2 分）　答案要化到最簡'))
    P.append(problem_box([qhead(f'14．一元二次方程 {{x^2=25}} 的解是 {{x_1=}}{MID}，{{x_2=}}{MID}。')]))
    P.append(problem_box([qhead(f'15．若 {{x_1}}、{{x_2}} 是方程 {{x^2+7x-3=0}} 的兩個根，則 '
                                f'{{x_1+x_2=}}{MID}，{{x_1x_2=}}{MID}。')]))
    P.append(problem_box([qhead(f'16．已知兩個數的和等於 10，積等於 16，若設其中一個數為 {{x}}，'
                                f'可列出方程為{BLANK}。')]))
    P.append(problem_box([side(
        [para('17．如圖，是二次函數 {y=-x^2} 的圖像。'),
         para(f'當 {{x>0}} 時，{{y}} 隨 {{x}} 增大而{MID}（填「增大」或「減少」）。')],
        FIG['q17'], media, 2.6, pct=0.80)]))
    P.append(problem_box([
        qhead(f'18．二次函數 {{y=(x-2)^2-3}} 的開口方向{MID}，頂點坐標為{MID}，'),
        sub_line(f'對稱軸是 {{x=}}{MID}，有最{SHORT}（填「大」或「小」）值{MID}。')]))
    P.append(problem_box([qhead('19．利用配方法把二次函數 {y=x^2-6x+4} 變形為 {y=a(x-h)^2+k} 為'
                                f'{BLANK}{SHORT}。')] + lines(2)))
    P.append(problem_box([qhead('20．把拋物線 {y=x^2} 向上平移 5 個單位，平移後拋物線的函數式為'
                                f'{BLANK}{SHORT}。')]))

    # ---------------- 解答題 ----------------
    P.append(heading('三、解答題（共 43 分）　需要有詳細解答過程和答案，答案要化到最簡'))
    inner = W - 260
    P.append(problem_box([
        qhead('21．用適當方法解下列方程：'),
        _tbl([[{'p': [para('(1) {x^2-6x+8=0}　（4 分）', keep_next=True)] + lines(6, ind=0)},
               {'p': [para('(2) {2x^2+6x+3=0}　（4 分）', keep_next=True)] + lines(6, ind=0)}]],
             [inner // 2, inner - inner // 2], border='none', trailing_blank=False)]))
    P.append(problem_box([
        qhead('22．若兩個連續正偶數的積為 80，求這兩個偶數。　（7 分）'),
        sub(f'① 設未知數：較小的正偶數為 {{x}}，較大的正偶數為{BLANK}'),
        sub(f'② 列方程：{MID} × {MID} ＝ 80'),
        sub('③ 解方程：')] + lines(3) + [
        sub('④ 檢驗並作答：'),
        sub_line(f'兩個根：{SHORT}、{SHORT}；捨去：{MID}；'),
        end(sub_line(f'答：{BLANK}{BLANK}'))]))
    P.append(problem_box([
        qhead('23．已知二次函數的圖像經過 {(-1,8)}、{(1,2)}、{(0,3)} 三點，求這個二次函數的解析式。'
              '　（7 分）'),
        sub(f'解：設二次函數的解析式為 {{y=}}{BLANK}'),
        sub('把點 {(-1,8)}、{(1,2)}、{(0,3)} 代入得'),
        sub(' {cases(＿＿＿＿＿＿＿＿＿＿=8; ＿＿＿＿＿＿＿＿＿＿=2; c=3)}'),
        sub('請續寫完整計算過程。（否則視為 0 分）')] + lines(4) + [
        end(sub(f'∴ 這個二次函數的解析式為 {{y=}}{BLANK}{SHORT}。'))]))
    P.append(problem_box([
        qhead('24．已知二次函數的頂點坐標為 {(2,-8)}，且經過點 {(4,0)}，求這個二次函數的解析式。'
              '　（7 分）'),
        sub(f'解：設二次函數的頂點式為 {{y=}}{BLANK}'),
        sub(f'把頂點 {{(2,-8)}} 代入得 {{y=}}{BLANK}'),
        sub('再把點 {(4,0)} 代入得'),
        sub('請續寫完整計算過程。（否則視為 0 分）')] + lines(3) + [
        end(sub(f'∴ 這個二次函數的解析式為 {{y=}}{BLANK}{SHORT}。'))]))
    P.append(problem_box([
        qhead('25．畫出二次函數 {y=(x-1)^2-3} 的圖像（要求列表、描點）。　（7 分）'),
        value_table((-1, 0, 1, 2, 3)),
        para('', spacing=False, keep_next=True),
        expand_image(image_para(FIG['q25'], width_cm=7.8), media)], trailing_blank=True))
    P.append(problem_box([
        qhead('26．如圖，有一拋物線形拱橋，當拱頂到水面的距離為 4 米時，水面寬度為 8 米。'
              '當水位上升到水面距離拱橋頂 1 米時，此時的水位為警戒水位。求：'),
        expand_image(image_para(FIG['q26'], width_cm=7.2), media),
        sub(f'(1) 寫出拋物線的頂點 {{C}}、點 {{A}}、{{B}} 的坐標；　（3 分）'),
        sub_line(f'{{C}}（{SHORT}，{SHORT}）　{{A}}（{SHORT}，{SHORT}）　{{B}}（{SHORT}，{SHORT}）'),
        sub('(2) 在如圖所示的坐標系中，求拋物線的解析式；　（3 分）'),
        sub(f'解：設二次函數的頂點式為 {{y=}}{BLANK}'),
        sub(f'把頂點 {{C}}（{SHORT}，{SHORT}）代入得 {{y=}}{BLANK}'),
        sub(f'再把點 {{B}}（{SHORT}，{SHORT}）代入得'),
        sub('請續寫完整計算過程。（否則視為 0 分）')] + lines(3) + [
        sub(f'∴ 這個二次函數的解析式為 {{y=}}{BLANK}{SHORT}。'),
        sub('(3) 水位達到警戒水位時的水面寬度是多少米？　（1 分）')] + lines(3)))  # 尾段是作答線，無 keepNext

    P.append(heading('B 部（共 8 分）', page_break_before=True))
    P.append(heading('四、解答題（共 8 分）　需要有詳細解答過程和答案，答案要化到最簡'))
    P.append(problem_box([
        qhead('27．已知關於 {x} 的方程 {x^2-2kx+k^2+3k-6=0} 有兩個實數根 {x_1}、{x_2}，求：'),
        sub('(1) 利用判別式求實數 {k} 的取值範圍；　（3 分）'),
        sub(f'解：{{a=1}}，{{b=}}{MID}，{{c=}}{MID}'),
        sub(f'{{Δ=b^2-4ac=}}{BLANK}{BLANK}'),
        sub(f'∵ 方程有兩個實數根，∴ {{Δ}}{SHORT}{{0}}（填「{{>}}」或「{{≥}}」）'),
        sub('即')] + lines(2) + [
        sub(f'∴ 實數 {{k}} 的取值範圍是{BLANK}。'),
        sub('(2) 若 {2x_1x_2+(x_1+x_2)+2=32}，試求實數 {k} 的值。　（5 分）'),
        sub(f'解：{{x_1+x_2=-frac(b,a)=}}{MID}，{{x_1x_2=frac(c,a)=}}{MID}'),
        sub('代入 {2x_1x_2+(x_1+x_2)+2=32} 得')] + lines(2) + [
        sub('解方程：')] + lines(3) + [
        sub(f'檢驗：{{k}} 要符合 (1) 的範圍，捨去 {{k=}}{SHORT}'),
        end(sub(f'∴ {{k=}}{MID}。'))], trailing_blank=False))
    P.append(para('～ 全卷完 ～', bold=True, jc='center'))
    save(P, BASE + '_學生卷.docx', FOOT, media=media)


# ================================ 教師卷 ================================
def teacher():
    P = [masthead(SUBJECT, UNIT, '模擬卷・教師卷')]
    P.append(para('本卷供教師批改使用，不發給學生。題號、題型、配分與統測原卷第 1–27 題一致，只改了數字；'
                  f'第 28、29 題不設，全卷 103 分（A 部 95 分＋B 部 8 分），限時 {MINUTES} 分鐘。'
                  '選擇題正確選項的位置刻意與原卷錯開；逐題驗算見同資料夾《驗算_初三數學統測.md》。'))

    P.append(heading('一、單選題（每題 2 分，共 26 分）'))
    P.append(ans_tbl([
        ('1．（2）', 'A', '{a=3}，{b=-4}，{c=7}；係數連符號一起讀。B 把 {a}、{b} 對調；C、D 符號錯'),
        ('2．（2）', 'C', '移項：{x^2+4x-2x-5=0}，即 {x^2+2x-5=0}。A 把 {2x} 加了上去'),
        ('3．（2）', 'D', '一元二次方程的二次項係數不為 0：{m+2≠0}，{m≠-2}'),
        ('4．（2）', 'B', '{x=0} 或 {x+4=0}，{x_2=-4}。※ 易錯：A 漏了負號'),
        ('5．（2）', 'C', '{Δ=3^2-4×1×(-4)=25>0}，有兩個不相等的實數根。（選項次序與原卷不同）'),
        ('6．（2）', 'B', '{a=3}，{b=5}，{c=-2}；{x=frac(-b±sqrt(b^2-4ac),2a)}。A 漏了 {-b} 的負號；'
                       'C 把 {b}、{c} 對調；D 分母漏了 {a}'),
        ('7．（2）', 'A', '四周都有草坪帶，長、寬各減兩個 {x}：{(24-2x)(14-2x)=200}（解得 {x=2}）'),
        ('8．（2）', 'D', '把路推到邊上，綠化地是 {(60-x)} 乘 {(40-x)}（解得 {x=3}）。'
                       'A 少加回重疊的 {x^2}'),
        ('9．（2）', 'D', 'A、C 的 {x} 在分母；B 是一次函數'),
        ('10．（2）', 'B', '{a=-3<0} 開口向下、頂點在原點。A 開口向上；C 不是函數圖像；D 是兩條直線'),
        ('11．（2）', 'A', '{a=2>0}，開口向上'),
        ('12．（2）', 'D', '頂點式 {k=-4}，{a=1>0}，最小值 {-4}。※ 易錯：C 漏了負號'),
        ('13．（2）', 'B', '圖像與 {x} 軸有兩個交點 → 方程有兩個不相等的實數根。'
                        '（本卷改為開口向下、選項次序與原卷不同）'),
    ]))

    P.append(heading('二、填空題（每格 2 分，共 26 分）'))
    P.append(ans_tbl([
        ('14．（4）', ['{x_1=5}', '{x_2=-5}'], '直接開平方；兩根次序可對調'),
        ('15．（4）', ['{x_1+x_2=-7}', '{x_1x_2=-3}'], '{-frac(b,a)}、{frac(c,a)}。※ 易錯：和寫成 7'),
        ('16．（2）', '{x(10-x)=16}', '另一數 {10-x}；寫成 {x^2-10x+16=0} 亦可（兩數為 2、8）'),
        ('17．（2）', '減少', '{a=-1<0}，對稱軸是 {y} 軸，右邊下降'),
        ('18．（10）', ['開口：向上', '頂點：{(2,-3)}', '對稱軸：{x=2}', '最小值：{-3}'],
         '共 5 格：「小」與「{-3}」各 2 分。{a=1>0}；頂點 {(h,k)}'),
        ('19．（2）', '{y=(x-3)^2-5}', '{x^2-6x+9-9+4}；加減 {(frac(6,2))^2=9}'),
        ('20．（2）', '{y=x^2+5}', '上加下減，加在整個式子後面'),
    ]))

    P.append(heading('三、解答題（共 43 分）'))
    P.append(sub_title('21．（8 分）'))
    P.append(wtbl([
        span_row('(1) {x^2-6x+8=0}'),
        eq_row('{(x-2)(x-4)}', '{0}', '因式分解 2 分'),
        answer_row('{x_1=2}，{x_2=4}', '兩根各 1 分'),
        span_row('(2) {2x^2+6x+3=0}：{a=2}，{b=6}，{c=3}', '讀係數'),
        eq_row('{Δ}', '{6^2-4×2×3=12}', '1 分'),
        eq_row('{x}', '{frac(-6±sqrt(12),4)=frac(-6±2sqrt(3),4)}', '代入公式 2 分'),
        answer_row('{x_1=frac(-3+sqrt(3),2)}，{x_2=frac(-3-sqrt(3),2)}', '化簡 1 分（未約分扣 1 分）'),
    ], why_pct=0.32))
    P.append(sub_title('22．（7 分）'))
    P.append(wtbl([
        span_row('① 較大的正偶數為 {x+2}', '1 分'),
        eq_row('② {x(x+2)}', '{80}', '列方程 2 分'),
        eq_row('{x^2+2x-80}', '{0}', ''),
        eq_row('{(x+10)(x-8)}', '{0}', '解方程 2 分'),
        span_row('{x_1=8}，{x_2=-10}；{-10} 不是正數，捨去', '檢驗 1 分'),
        answer_row('這兩個偶數是 8 和 10', '作答 1 分'),
    ], why_pct=0.32))
    P.append(sub_title('23．（7 分）'))
    P.append(wtbl([
        span_row('設 {y=ax^2+bx+c}', '1 分'),
        span_row('代入：{cases(a-b+c=8; a+b+c=2; c=3)}', '代入三點 3 分（每式 1 分）'),
        span_row('把 {c=3} 代入：{a-b=5}，{a+b=-1}', ''),
        span_row('兩式相加：{2a=4}，{a=2}；{b=-1-2=-3}', '解出 {a}、{b} 2 分'),
        answer_row('{y=2x^2-3x+3}', '1 分'),
    ], why_pct=0.32))
    P.append(sub_title('24．（7 分）'))
    P.append(wtbl([
        span_row('設 {y=a(x-h)^2+k}', '1 分'),
        span_row('代入頂點：{y=a(x-2)^2-8}', '代入頂點 2 分'),
        eq_row('{0}', '{a(4-2)^2-8}', '代入 {(4,0)} 2 分'),
        eq_row('{4a}', '{8}，{a=2}', '1 分'),
        answer_row('{y=2(x-2)^2-8}', '1 分（寫成 {y=2x^2-8x} 亦可）'),
    ], why_pct=0.32))
    P.append(ans_tbl([
        ('25．（7）', ['{x}：{-1}，0，1，2，3', '{y}：1，{-2}，{-3}，{-2}，1'],
         '列表 3 分（錯一格扣 1 分，扣完為止）；描點 2 分；用平滑曲線連線 2 分（連成折線或尖底扣 1 分）。'
         '頂點 {(1,-3)}、對稱軸 {x=1}，左右點對稱可作自我檢查'),
    ]))
    P.append(sub_title('26．（7 分）'))
    P.append(wtbl([
        span_row('(1) {C(0,4)}，{A(-4,0)}，{B(4,0)}', '每點 1 分'),
        span_row('(2) 設 {y=a(x-0)^2+4}，即 {y=ax^2+4}', '代入頂點 1 分'),
        eq_row('{0}', '{a×4^2+4}', '代入 {B(4,0)} 1 分'),
        answer_row('{a=-frac(1,4)}，{y=-frac(1,4)x^2+4}', '1 分'),
        span_row('(3) 警戒水位離拱頂 1 米 → {y=4-1=3}', ''),
        eq_row('{-frac(1,4)x^2+4}', '{3}，{x^2=4}，{x=±2}', ''),
        answer_row('水面寬度 {2-(-2)=4} 米', '1 分'),
    ], why_pct=0.32))
    P.append(para('※ 原卷第 26(2) 題框寫「再把點 (3,0) 代入」，與水面寬 4 米不符（應是 B(2,0)），'
                  '本卷已改為由學生填 B 點坐標。', sz=22))

    P.append(heading('四、B 部解答題（共 8 分）'))
    P.append(sub_title('27．（8 分）'))
    P.append(wtbl([
        span_row('(1) {a=1}，{b=-2k}，{c=k^2+3k-6}', ''),
        eq_row('{Δ}', '{(-2k)^2-4(k^2+3k-6)}', ''),
        eq_row('', '{24-12k}', '1 分'),
        eq_row('{24-12k}', '{0}', '有兩個實數根 {Δ≥0} 1 分（寫 {>} 扣 1 分）', rel='{≥}'),
        answer_row('{k≤2}', '1 分'),
        span_row('(2) {x_1+x_2=2k}，{x_1x_2=k^2+3k-6}', '兩根和、積 2 分'),
        eq_row('{2(k^2+3k-6)+2k+2}', '{32}', '代入 1 分'),
        eq_row('{k^2+4k-21}', '{0}', ''),
        eq_row('{(k+7)(k-3)}', '{0}', '解出 {k=-7} 或 {k=3}：1 分'),
        answer_row('{k=3>2} 捨去，{k=-7}', '檢驗 1 分。驗：{k=-7} 時 {Δ=108>0}'),
    ], why_pct=0.36))
    save(P, BASE + '_教師卷.docx', FOOT + '（教師卷）')


if __name__ == '__main__':
    draw_figs()
    student()
    teacher()
    print('OK')
