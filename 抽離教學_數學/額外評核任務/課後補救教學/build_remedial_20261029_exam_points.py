# -*- coding: utf-8 -*-
r"""
build_remedial_20261029_exam_points.py — 初三數學補救班 課後補救教學（2026-10-29）

使用者 2026-10-27 指示：
- 考點＝`測驗及複習\初三統測_第一學段\模擬卷_初三數學統測_學生卷.pdf` 的第 13、21、23、24、26 題
  （統測 2026-11-09 實施）；練習「不要一模一樣」，由我設計對應的練習。
- 參考 10-08 那份：做題之前有知識點回顧（第 21 題除外——解方程之前已做過）。
- 應用題（第 26 題拱橋）沒有知識點回顧，改給框架，之後的題目取消框架。

課後補救教學一般是「題目由使用者自己搵」，本份例外：使用者明確要我命題。
數字全部重新命題，已逐一對過原卷（2627 統測調 40%）與模擬卷，沒有一題撞數字；逐題驗算見
《驗算_課後補救教學20261029_統測考點練習.md》。

我定的：
- 五大題對應五個考點，次序照卷面題號；三、四、五大題鷹架三級褪除
  （完整框架 → 半框架 → 只留作答線）。
- 滿分 100：一 26＋二 16＋三 18＋四 18＋五 22；每題「改正」欄、帶回家完成（照 10-08／10-15）。
- 知識點回顧的示範一律用等號對齊的算式表（house-style「數學算式的書寫規範」）。
版面層沿用 10-15／10-22 兩份腳本的元件。
"""
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_remedial_20261015_quadratic_vertex_form import (  # noqa: E402
    para, heading, masthead, student_info_row, image_para, expand_image,
    MediaRegistry, _tbl, W, BLANK, SHORT, MID, save, ruled, ruled_ind, qhead, sub_line, note,
    cpara, info_box, ans_tbl as _ans_tbl, sub_title, keep_rows_together,
    worked_example_table, eq_row, or_row, answer_row, span_row, GREY_FILL)
from build_remedial_20261022_mock_test import (  # noqa: E402
    problem_box, opts, _plt, _arrow_axes)

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學（補救班）'
UNIT = '統測考點練習・根的情況、解方程、求解析式、拱橋應用'
BASE = '課後補救教學_初三數學補救班_20261029_統測考點練習'
FOOT = '初三數學補救班．課後補救教學 2026-10-29'
PAREN = '（　　　）'

# 第 13 題型：判別式三種情況 × 開口方向（知識點回顧表）＋練 1–3 的圖
TAB = {'up_2': (0.8, 0, -1.6), 'up_1': (0.8, 0, 0), 'up_0': (0.8, 0, 1.2),
       'dn_2': (-0.8, 0, 1.6), 'dn_1': (-0.8, 0, 0), 'dn_0': (-0.8, 0, -1.2)}
Q13 = {'q1': (0.8, 1.0, 0), 'q2': (-0.7, -0.6, -1.0), 'q3': (0.8, 1.6, -0.9)}
# 第 26 題型：(拱頂到水面的距離, 水面寬)
BRIDGE = {'q14': (4, 4), 'q15': (9, 12), 'q16': (8, 8)}
FIG = {k: os.path.join(OUT, f'_tmp_fig_{k}.png') for k in list(TAB) + list(Q13) + list(BRIDGE)}


# ================================ 圖 ================================
def root_sketch(a, h, k, path, size=1.5):
    """無刻度示意圖：只看開口方向與跟 x 軸有幾個公共點。頂點落在 x 軸上時畫實心點，
    一眼看出「碰到一點」而不是「差少少未到」（記憶 graph_must_not_contradict_text）。"""
    import numpy as np
    plt = _plt()
    xr, yr = (-3.0, 3.4), (-3.0, 3.0)
    fig, ax = plt.subplots(figsize=(size, size * 0.95), dpi=300)
    ax.set_xlim(*xr)
    ax.set_ylim(*yr)
    # 「O」放在原點四角之中離曲線最遠的一角
    f = lambda t: a * (t - h) ** 2 + k
    o_pos = max(((sx * 0.15, sy * 0.2) for sx in (-1, 1) for sy in (-1, 1)),
                key=lambda p: abs(f(p[0] * 3) - p[1] * 3))
    _arrow_axes(ax, xr, yr, fs=10, o_pos=o_pos)
    xs = np.linspace(xr[0] + 0.1, xr[1] - 0.3, 400)
    ys = f(xs)
    ys = np.where((ys < yr[0] + 0.1) | (ys > yr[1] - 0.3), np.nan, ys)
    ax.plot(xs, ys, color='black', lw=1.6)
    if k == 0:
        ax.plot(h, 0, 'o', color='black', ms=3.6, zorder=5)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.03)
    plt.close(fig)


def bridge_figure(path, H, Wd):
    """拋物線拱橋示意圖（照模擬卷第 26 題的畫法）：原點在水面中點，A、B 在 x 軸上，C 是拱頂。
    圖上只標兩個已知量；畫圖比例統一（半寬 4 單位），高度隨 H／半寬略作伸縮。"""
    import numpy as np
    from matplotlib.patches import FancyArrowPatch, Polygon, Rectangle
    plt = _plt()
    top = 3.0 + H / (Wd / 2)               # 4/2 → 5.0；9/6 → 4.5；8/4 → 5.0
    fig, ax = plt.subplots(figsize=(3.2, 2.5), dpi=300)
    ax.set_xlim(-7.4, 7.8); ax.set_ylim(-3.2, top + 2.6); ax.set_aspect('equal'); ax.axis('off')
    f = lambda t: -top / 16 * t ** 2 + top
    ax.add_patch(Rectangle((-6.4, -1.6), 12.8, top + 3.0, fc='#d2d2d2', ec='black', lw=1.0))
    xb = np.sqrt((top + 1.6) / (top / 16))
    xs = np.linspace(-xb, xb, 300)
    ax.add_patch(Polygon(np.c_[xs, f(xs)], closed=True, fc='white', ec='black', lw=1.4))
    for yy in (-0.8, -1.25):
        ax.plot([-4.2, 4.2], [yy, yy], color='black', lw=0.7, ls=(0, (4, 2)))
    ax.add_patch(FancyArrowPatch((-7.2, 0), (7.6, 0), arrowstyle='-|>', mutation_scale=9, lw=0.9))
    ax.add_patch(FancyArrowPatch((0, -3.0), (0, top + 2.4), arrowstyle='-|>', mutation_scale=9,
                                 lw=0.9))
    ax.text(7.6, -0.25, '$x$', ha='right', va='top', fontsize=11)
    ax.text(0.25, top + 2.4, '$y$', ha='left', va='top', fontsize=11)
    ax.text(0.2, -0.12, '$O$', ha='left', va='top', fontsize=10)
    ax.text(-4.15, 0.2, '$A$', ha='right', va='bottom', fontsize=11)
    ax.text(4.15, 0.2, '$B$', ha='left', va='bottom', fontsize=11)
    ax.text(0.25, top + 0.15, '$C$', ha='left', va='bottom', fontsize=11)
    kw = dict(arrowstyle='<|-|>', mutation_scale=7, lw=0.8, color='black')
    ax.add_patch(FancyArrowPatch((-1.0, 0), (-1.0, top), **kw))
    ax.text(-1.25, top / 2, str(H), ha='right', va='center', fontsize=10)
    ax.add_patch(FancyArrowPatch((-4, -2.3), (4, -2.3), **kw))
    ax.plot([-4, -4], [-2.6, 0], color='black', lw=0.5)
    ax.plot([4, 4], [-2.6, 0], color='black', lw=0.5)
    ax.text(1.0, -2.45, str(Wd), ha='center', va='top', fontsize=10,
            bbox=dict(fc='white', ec='none', pad=0.4))
    fig.savefig(path, bbox_inches='tight', pad_inches=0.03)
    plt.close(fig)


def draw_figs():
    for k, (a, h, kk) in list(TAB.items()) + list(Q13.items()):
        root_sketch(a, h, kk, FIG[k], size=1.5 if k in TAB else 1.7)
    for k, (H, Wd) in BRIDGE.items():
        bridge_figure(FIG[k], H, Wd)


# ================================ 元件 ================================
def side(left, img, media, width_cm, pct=0.64):
    """左文右圖（無框）：題目在左、圖在右（house-style）。"""
    inner = W - 260
    wl = int(inner * pct)
    return _tbl([[{'p': left, 'va': 'center'},
                  {'p': [expand_image(image_para(img, width_cm=width_cm), media)]}]],
                [wl, inner - wl], border='none', trailing_blank=False)


def sub(text):
    """小題／框架行（縮排、keepNext）；行距收成 1.35 倍（同 10-15 的 sub_line），
    題框不能跨頁，框架題太高會成個跳去下一頁留下半頁空白。"""
    return para(text, ind=280, keep_next=True).replace(
        '<w:spacing w:line="360" w:lineRule="auto" w:after="80"/>',
        '<w:spacing w:line="324" w:lineRule="auto" w:after="60"/>')


def lines(n, ind=560):
    return [ruled_ind('', ind=ind) for _ in range(n)]


def end(xml):
    """題框最後一段拿走 keepNext：否則整個題框會黏住下一題一齊跳頁。"""
    return xml.replace('<w:keepNext/>', '')


def wtbl(rows, why_pct=0.34, col_frac=(0.36, 0.05, 0.40, 0.05, 0.07, 0.04)):
    return keep_rows_together(worked_example_table(
        rows, headers=('算式', '這一步在做什麼'), why_pct=why_pct, col_frac=col_frac))


def twbl(rows, why_pct=0.36, col_frac=(0.30, 0.05, 0.22, 0.06, 0.12, 0.05)):
    """教師卷算式表：右欄＝說明與建議評分。"""
    return keep_rows_together(worked_example_table(
        rows, headers=('算式', '說明與建議評分'), why_pct=why_pct, col_frac=col_frac))


def _txt(a):
    """純數學式的段落 Word 會當 display math 置中；前面補一個文字空白就靠左。"""
    return ' ' + a if a.startswith('{') else a


def ans_tbl(rows):
    return _ans_tbl([(n, [_txt(x) for x in a] if isinstance(a, list) else _txt(a), why)
                     for n, a, why in rows])


def mcfig(n, stem, options, fig, media):
    """第 13 題型：題幹＋左選項、右圖＋作答／改正。"""
    return problem_box([side([qhead(f'練 {n}．{stem}{PAREN}')] + opts(options, 2),
                             FIG[fig], media, 2.7, pct=0.80),
                        ruled('改正：')])


def roots_table(media):
    """知識點回顧：判別式 × 開口方向 → 與 x 軸公共點個數 → 方程的根（決策表）。"""
    w0 = int(W * 0.19)
    w1 = (W - w0) // 3
    widths = [w0, w1, w1, W - w0 - 2 * w1]
    img = lambda k: {'p': [expand_image(image_para(FIG[k], width_cm=2.3), media)]}
    lab = lambda t: {'p': [cpara(t, bold=True)], 'va': 'center'}
    mid = lambda t: {'p': [cpara(t)], 'va': 'center'}
    rows = [
        [{'p': [cpara('二次函數 {y=ax^2+bx+c} 的圖像與方程 {ax^2+bx+c=0} 的根', bold=True)],
          'shd': GREY_FILL, 'span': 4}],
        [{'p': [cpara('')], 'shd': GREY_FILL},
         {'p': [cpara('{Δ>0}', bold=True)], 'shd': GREY_FILL},
         {'p': [cpara('{Δ=0}', bold=True)], 'shd': GREY_FILL},
         {'p': [cpara('{Δ<0}', bold=True)], 'shd': GREY_FILL}],
        [lab('{a>0}'), img('up_2'), img('up_1'), img('up_0')],
        [lab('{a<0}'), img('dn_2'), img('dn_1'), img('dn_0')],
        [lab('與 {x} 軸的公共點'), mid('2 個'), mid('1 個'), mid('沒有')],
        [lab('方程的根'), mid('兩個不相等的實數根'), mid('兩個相等的實數根'), mid('沒有實數根')],
    ]
    return keep_rows_together(_tbl(rows, widths))


def grid4(items):
    """第 21 題型：四小題排成 2 × 2，每格題目＋作答線。"""
    inner = W - 260
    cell = lambda t: {'p': [para(t, keep_next=True)] + lines(5, ind=0)}
    return _tbl([[cell(items[0]), cell(items[1])], [cell(items[2]), cell(items[3])]],
                [inner // 2, inner - inner // 2], border='none', trailing_blank=False)


# ================================ 學生卷 ================================
def student():
    media = MediaRegistry()
    P = [masthead(SUBJECT, UNIT, '課後補救教學'), student_info_row()]
    P.append(para('帶回家完成　　共五大題（16 題）　　滿分 100 分　　'
                  '得分：＿＿＿＿ / 100', bold=True))
    P.append(para('老師批改後，請在每題的「改正」欄完成訂正，下一節帶回。'))

    # ---------------- 一、第 13 題型 ----------------
    P.append(heading('一、拋物線與 x 軸的公共點・方程的根（26 分）'))
    P.append(info_box([
        para('▍判別式', bold=True, keep_next=True),
        para('{Δ=b^2-4ac}', jc='center', keep_next=True),
        para('看拋物線 {y=ax^2+bx+c} 與 {x} 軸有幾個公共點，就知道方程 {ax^2+bx+c=0} '
             '有幾個實數根。開口向上或向下都一樣。', ind=280),
    ]))
    P.append(roots_table(media))
    P.append(note('選擇題（練 1、2、3）每題 4 分；練 4、練 5 每題 4 分；練 6 為 6 分。'))
    P.append(mcfig(1, '若拋物線 {y=ax^2+bx+c} 的圖像如右圖，則方程 {ax^2+bx+c=0} 的實數根情況是',
                   ['方程有兩個不相等的實數根', '方程沒有實數根',
                    '方程有兩個相等的實數根', '方程的實數根情況不確定'], 'q1', media))
    P.append(mcfig(2, '若拋物線 {y=ax^2+bx+c} 的圖像如右圖，則方程 {ax^2+bx+c=0} 的實數根情況是',
                   ['方程沒有實數根', '方程有兩個相等的實數根',
                    '方程有兩個不相等的實數根', '方程的實數根情況不確定'], 'q2', media))
    P.append(mcfig(3, '若拋物線 {y=ax^2+bx+c} 的圖像如右圖，則方程 {ax^2+bx+c=0} 的實數根情況是',
                   ['方程有兩個相等的實數根', '方程沒有實數根',
                    '方程的實數根情況不確定', '方程有兩個不相等的實數根'], 'q3', media))
    P.append(problem_box([qhead('練 4．二次函數 {y=x^2-6x+9}：'),
                          sub_line(f'{{Δ=}}{MID}；　圖像與 {{x}} 軸有{SHORT}個公共點。'),
                          qhead('練 5．二次函數 {y=2x^2+3x+5}：'),
                          sub_line(f'{{Δ=}}{MID}；　圖像與 {{x}} 軸有{SHORT}個公共點。'),
                          ruled('改正：')]))
    P.append(problem_box([qhead('練 6．二次函數 {y=-x^2+2x+3}：'),
                          sub_line(f'{{Δ=}}{MID}；　圖像與 {{x}} 軸有{SHORT}個公共點；'),
                          sub_line('令 {y=0}，解方程 {-x^2+2x+3=0}：')] + lines(2) + [
                          sub_line(f'圖像與 {{x}} 軸的公共點坐標是{MID}和{MID}。'),
                          ruled('改正：')]))

    # ---------------- 二、第 21 題型（不設回顧） ----------------
    P.append(heading('二、用適當方法解一元二次方程（16 分）'))
    P.append(note('每小題 4 分。能因式分解就用因式分解；分解不到就用公式法，答案要化到最簡。'))
    P.append(problem_box([
        qhead('練 7．用適當方法解下列方程：'),
        grid4(['(1) {x^2-5x-14=0}', '(2) {2x^2-x-3=0}',
               '(3) {x^2-4x+1=0}', '(4) {3x^2+4x-1=0}']),
        ruled('改正：')]))

    # ---------------- 三、第 23 題型 ----------------
    P.append(heading('三、已知三點求二次函數的解析式（18 分）'))
    P.append(problem_box([
        para('▍一般式', bold=True, keep_next=True),
        para('{y=ax^2+bx+c}', jc='center', keep_next=True),
        para('第 1 步　有一點是 {(0,c)}：{x=0} 時 {y=c}，直接讀出 {c}。', ind=280, keep_next=True),
        para('第 2 步　把另外兩點代入，得到關於 {a}、{b} 的兩條方程 ①、②。', ind=280,
             keep_next=True),
        para('第 3 步　① ＋ ② 消去 {b}，求 {a}；再代回求 {b}。', ind=280, keep_next=True),
        para('第 4 步　寫出解析式，把三點代回去檢查。', ind=280),
    ]))
    P.append(sub_title('示範：二次函數的圖像經過 {(-1,6)}、{(1,2)}、{(0,1)} 三點，求解析式。'))
    P.append(wtbl([
        span_row('設 {y=ax^2+bx+c}'),
        span_row('代入三點：{cases(a-b+c=6; a+b+c=2; c=1)}', '{x=-1} 時 {x^2=1}，{bx=-b}'),
        eq_row('{a-b}', '{5}', '把 {c=1} 代入第一式，移項，記作 ①'),
        eq_row('{a+b}', '{1}', '把 {c=1} 代入第二式，移項，記作 ②'),
        eq_row('{2a}', '{6}', '① ＋ ②，{b} 消去了'),
        eq_row('{a}', '{3}', ''),
        eq_row('{b}', '{1-3}', '把 {a=3} 代入 ②'),
        eq_row('{b}', '{-2}', ''),
        answer_row('{y=3x^2-2x+1}', '檢查：{x=-1} 時 {3+2+1=6}　✔'),
    ]))
    P.append(note('練 8、9、10 每題 6 分。'))
    P.append(problem_box([
        qhead('練 8．已知二次函數的圖像經過 {(-1,0)}、{(1,-4)}、{(0,-3)} 三點，求這個二次函數的解析式。'),
        sub(f'解：設二次函數的解析式為 {{y=}}{BLANK}'),
        sub('把點 {(-1,0)}、{(1,-4)}、{(0,-3)} 代入得'),
        sub(' {cases(＿＿＿＿＿＿＿＿＿＿=0; ＿＿＿＿＿＿＿＿＿＿=-4; c=-3)}'),
        sub(f'把 {{c=-3}} 代入：　① {{a-b=}}{SHORT}　　② {{a+b=}}{SHORT}'),
        sub(f'① ＋ ②：{{2a=}}{SHORT}，{{a=}}{SHORT}；代入 ②：{{b=}}{SHORT}'),
        sub(f'∴ 這個二次函數的解析式為 {{y=}}{BLANK}{SHORT}。'),
        ruled('改正：')]))
    P.append(problem_box([
        qhead('練 9．已知二次函數的圖像經過 {(-1,-1)}、{(1,5)}、{(0,4)} 三點，求這個二次函數的解析式。'),
        sub(f'解：設二次函數的解析式為 {{y=}}{BLANK}'),
        sub('把點 {(-1,-1)}、{(1,5)}、{(0,4)} 代入得'),
        sub('請續寫完整計算過程。')] + lines(4) + [
        sub(f'∴ 這個二次函數的解析式為 {{y=}}{BLANK}{SHORT}。'),
        ruled('改正：')]))
    P.append(problem_box([
        qhead('練 10．已知二次函數的圖像經過 {(0,-1)}、{(1,2)}、{(-1,-2)} 三點，求這個二次函數的解析式。')]
        + lines(5) + [ruled('改正：')]))

    # ---------------- 四、第 24 題型 ----------------
    P.append(heading('四、已知頂點求二次函數的解析式（18 分）'))
    P.append(problem_box([
        para('▍頂點式', bold=True, keep_next=True),
        para('{y=a(x-h)^2+k}　　頂點是 {(h,k)}', jc='center', keep_next=True),
        para('第 1 步　把頂點代入：只剩 {a} 未知。', ind=280, keep_next=True),
        para('第 2 步　把另一點代入，解出 {a}。', ind=280, keep_next=True),
        para('第 3 步　寫出解析式。', ind=280, keep_next=True),
        para('注意：頂點 {(-3,2)} 代入是 {y=a(x+3)^2+2}，括號內 {h} 的符號要反過來。', ind=280),
    ]))
    P.append(sub_title('示範：二次函數的頂點坐標為 {(2,1)}，且經過點 {(0,9)}，求解析式。'))
    P.append(wtbl([
        span_row('設 {y=a(x-h)^2+k}'),
        span_row('代入頂點：{y=a(x-2)^2+1}', '{h=2}，{k=1}'),
        eq_row('{9}', '{a(0-2)^2+1}', '把點 {(0,9)} 代入：{x=0}，{y=9}'),
        eq_row('{9}', '{4a+1}', '計算：{(0-2)^2=4}'),
        eq_row('{4a}', '{8}', ''),
        eq_row('{a}', '{2}', ''),
        answer_row('{y=2(x-2)^2+1}', '檢查：{x=0} 時 {2×4+1=9}　✔'),
    ]))
    P.append(note('練 11、12、13 每題 6 分。'))
    P.append(problem_box([
        qhead('練 11．已知二次函數的頂點坐標為 {(3,-2)}，且經過點 {(5,10)}，求這個二次函數的解析式。'),
        sub(f'解：設二次函數的頂點式為 {{y=}}{BLANK}'),
        sub(f'把頂點 {{(3,-2)}} 代入得 {{y=}}{BLANK}'),
        sub(f'再把點 {{(5,10)}} 代入得 {MID}＝{BLANK}'),
        sub(f'{{a=}}{SHORT}'),
        sub(f'∴ 這個二次函數的解析式為 {{y=}}{BLANK}{SHORT}。'),
        ruled('改正：')]))
    P.append(problem_box([
        qhead('練 12．已知二次函數的頂點坐標為 {(-2,5)}，且經過點 {(0,1)}，求這個二次函數的解析式。'),
        sub(f'解：設二次函數的頂點式為 {{y=}}{BLANK}'),
        sub(f'把頂點 {{(-2,5)}} 代入得 {{y=}}{BLANK}'),
        sub('請續寫完整計算過程。')] + lines(3) + [
        sub(f'∴ 這個二次函數的解析式為 {{y=}}{BLANK}{SHORT}。'),
        ruled('改正：')]))
    P.append(problem_box([
        qhead('練 13．已知二次函數的頂點坐標為 {(-1,-3)}，且經過點 {(2,15)}，求這個二次函數的解析式。')]
        + lines(5) + [ruled('改正：')]))

    # ---------------- 五、第 26 題型（框架 → 取消） ----------------
    P.append(heading('五、拋物線形拱橋（22 分）'))
    P.append(problem_box([
        para('▍拱橋題的解題框架（坐標原點在水面中點）', bold=True, keep_next=True),
        para('第 1 步　寫坐標：拱頂 {C}（0，拱頂到水面的距離）；'
             '{A}、{B} 在 {x} 軸上，各離原點「水面寬 ÷ 2」。', ind=280, keep_next=True),
        para('第 2 步　求解析式：頂點在 {y} 軸上（{h=0}），設 {y=ax^2+k}，代入 {B} 求 {a}。',
             ind=280, keep_next=True),
        para('第 3 步　求水面寬：警戒水位的高度 {y}＝拱頂高 － 離拱頂的距離；'
             '代入解析式解出 {x_1}、{x_2}，水面寬＝{x_2-x_1}。', ind=280),
    ]))
    P.append(note('練 14、練 15 每題 7 分〔(1) 3 分、(2) 3 分、(3) 1 分〕；'
                  '練 16 為 8 分〔(1) 3 分、(2) 3 分、(3) 2 分〕。'))
    P.append(problem_box([
        side([para('練 14．如圖，有一拋物線形拱橋，當拱頂到水面的距離為 4 米時，水面寬度為 4 米。'
                   '當水位上升到水面距離拱橋頂 1 米時，此時的水位為警戒水位。求：',
                   keep_next=True)], FIG['q14'], media, 5.2, pct=0.56),
        sub('(1) 寫出拋物線的頂點 {C}、點 {A}、{B} 的坐標；'),
        sub_line(f'{{C}}（{SHORT}，{SHORT}）　{{A}}（{SHORT}，{SHORT}）　{{B}}（{SHORT}，{SHORT}）'),
        sub('(2) 在如圖所示的坐標系中，求拋物線的解析式；'),
        sub(f'解：設二次函數的頂點式為 {{y=}}{BLANK}'),
        sub(f'把頂點 {{C}}（{SHORT}，{SHORT}）代入得 {{y=}}{BLANK}'),
        sub(f'再把點 {{B}}（{SHORT}，{SHORT}）代入得 {MID}＝{BLANK}'),
        sub(f'{{a=}}{SHORT}　　∴ 拋物線的解析式為 {{y=}}{BLANK}'),
        sub('(3) 水位達到警戒水位時的水面寬度是多少米？'),
        sub(f'警戒水位時，{{y=}}{SHORT}－{SHORT}＝{SHORT}'),
        sub(f'代入解析式：{SHORT}＝{BLANK}'),
        sub(f'{{x^2=}}{SHORT}　　{{x_1=}}{SHORT}　或　{{x_2=}}{SHORT}'),
        sub(f'∴ 水面寬度＝{SHORT}－（{SHORT}）＝{SHORT} 米'),
        ruled('改正：')]))
    P.append(problem_box([
        side([para('練 15．如圖，有一拋物線形拱橋，當拱頂到水面的距離為 9 米時，水面寬度為 12 米。'
                   '當水位上升到水面距離拱橋頂 4 米時，此時的水位為警戒水位。求：',
                   keep_next=True)], FIG['q15'], media, 5.2, pct=0.56),
        sub('(1) 寫出拋物線的頂點 {C}、點 {A}、{B} 的坐標；'),
        sub_line(f'{{C}}（{SHORT}，{SHORT}）　{{A}}（{SHORT}，{SHORT}）　{{B}}（{SHORT}，{SHORT}）'),
        sub('(2) 在如圖所示的坐標系中，求拋物線的解析式；'),
        sub(f'解：設二次函數的頂點式為 {{y=}}{BLANK}'),
        sub('請續寫完整計算過程。')] + lines(3) + [
        sub(f'∴ 拋物線的解析式為 {{y=}}{BLANK}'),
        sub('(3) 水位達到警戒水位時的水面寬度是多少米？'),
        sub(f'警戒水位時，{{y=}}{SHORT}')] + lines(3) + [
        sub(f'答：水面寬度是{SHORT}米。'),
        ruled('改正：')]))
    P.append(problem_box([
        side([para('練 16．如圖，有一拋物線形拱橋，當拱頂到水面的距離為 8 米時，水面寬度為 8 米。'
                   '當水位上升到水面距離拱橋頂 2 米時，此時的水位為警戒水位。求：',
                   keep_next=True)], FIG['q16'], media, 5.2, pct=0.56),
        sub('(1) 寫出拋物線的頂點 {C}、點 {A}、{B} 的坐標；')] + lines(1) + [
        sub('(2) 在如圖所示的坐標系中，求拋物線的解析式；')] + lines(4) + [
        sub('(3) 水位達到警戒水位時的水面寬度是多少米？')] + lines(3) + [
        ruled('改正：')], trailing_blank=False))
    save(P, BASE + '_學生卷.docx', FOOT, media=media)


# ================================ 教師卷 ================================
def teacher():
    P = [masthead(SUBJECT, UNIT, '課後補救教學・教師卷')]
    P.append(para('本卷供教師批改使用，不發給學生。題目、數字、分值與學生卷完全相同，滿分 100 分。'
                  '五大題對應統測模擬卷第 13、21、23、24、26 題的考點，全部重新命題（數字與原卷、'
                  '模擬卷都不同）；分值為建議分配，逐題驗算見同資料夾驗算紀錄。'))
    P.append(para('三、四、五大題的鷹架逐題褪除：第一題完整框架 → 第二題半框架 → 第三題只留作答線'
                  '（第三題的寫法即統測要求的寫法）。'))

    P.append(heading('一、拋物線與 x 軸的公共點・方程的根（26 分）'))
    P.append(ans_tbl([
        ('練 1（4）', 'C', '頂點落在 {x} 軸上，只有 1 個公共點 → 兩個相等的實數根。'
                          '※ 易錯：只見拋物線「碰到」{x} 軸就選 A'),
        ('練 2（4）', 'A', '開口向下、頂點在 {x} 軸下方，與 {x} 軸沒有公共點 → 沒有實數根。'
                          '※ 易錯：以為開口向下就一定穿過 {x} 軸'),
        ('練 3（4）', 'D', '與 {x} 軸有 2 個公共點（兩根都是正數，不影響結論）→ 兩個不相等的實數根'),
        ('練 4（4）', ['{Δ=0}', '1 個'], '每空 2 分。{Δ=(-6)^2-4×1×9=36-36=0}'),
        ('練 5（4）', ['{Δ=-31}', '0 個（沒有）'], '每空 2 分。{Δ=3^2-4×2×5=9-40=-31<0}'),
        ('練 6（6）', ['{Δ=16}，2 個', '{(-1,0)} 和 {(3,0)}'],
         'Δ 與個數各 1 分；兩點坐標各 2 分（次序可對調）。{Δ=2^2-4×(-1)×3=16}；'
         '方程兩邊乘 {-1}：{x^2-2x-3=0}，{(x-3)(x+1)=0}。※ 易錯：坐標寫成 {(0,-1)}、{(0,3)}'),
    ]))

    P.append(heading('二、用適當方法解一元二次方程（16 分）'))
    P.append(sub_title('練 7．每小題 4 分'))
    P.append(twbl([
        span_row('(1) {x^2-5x-14=0}'),
        eq_row('{(x-7)(x+2)}', '{0}', '因式分解 2 分'),
        or_row('{x-7}', '{0}', '{x+2}', '{0}', ''),
        answer_row('{x_1=7}　或　{x_2=-2}', '兩根各 1 分'),
    ]))
    P.append(twbl([
        span_row('(2) {2x^2-x-3=0}'),
        eq_row('{(2x-3)(x+1)}', '{0}', '因式分解 2 分（用公式法：{Δ=25}，亦可）'),
        or_row('{2x-3}', '{0}', '{x+1}', '{0}', ''),
        answer_row('{x_1=frac(3,2)}　或　{x_2=-1}', '兩根各 1 分'),
    ]))
    P.append(twbl([
        span_row('(3) {x^2-4x+1=0}：{a=1}，{b=-4}，{c=1}'),
        eq_row('{Δ}', '{(-4)^2-4×1×1}', ''),
        eq_row('{Δ}', '{12}', '1 分'),
        eq_row('{x}', '{frac(4±sqrt(12),2)}', '代入公式 2 分'),
        eq_row('{x}', '{frac(4±2sqrt(3),2)}', '化簡：{sqrt(12)=2sqrt(3)}'),
        answer_row('{x_1=2+sqrt(3)}　或　{x_2=2-sqrt(3)}', '化簡 1 分（未約分扣 1 分）'),
    ]))
    P.append(twbl([
        span_row('(4) {3x^2+4x-1=0}：{a=3}，{b=4}，{c=-1}'),
        eq_row('{Δ}', '{4^2-4×3×(-1)}', ''),
        eq_row('{Δ}', '{28}', '1 分'),
        eq_row('{x}', '{frac(-4±sqrt(28),6)}', '代入公式 2 分'),
        eq_row('{x}', '{frac(-4±2sqrt(7),6)}', '化簡：{sqrt(28)=2sqrt(7)}'),
        answer_row('{x_1=frac(-2+sqrt(7),3)}　或　{x_2=frac(-2-sqrt(7),3)}',
                   '化簡 1 分（未約分扣 1 分）'),
    ]))

    P.append(heading('三、已知三點求二次函數的解析式（18 分）'))
    for n, pts, cs, e1, e2, a_, b_, ans, chk in [
        (8, '{(-1,0)}、{(1,-4)}、{(0,-3)}', '{cases(a-b+c=0; a+b+c=-4; c=-3)}',
         '3', '-1', '1', '-2', '{y=x^2-2x-3}', '{x=-1}：{1+2-3=0}　✔'),
        (9, '{(-1,-1)}、{(1,5)}、{(0,4)}', '{cases(a-b+c=-1; a+b+c=5; c=4)}',
         '-5', '1', '-2', '3', '{y=-2x^2+3x+4}', '{x=-1}：{-2-3+4=-1}　✔'),
        (10, '{(0,-1)}、{(1,2)}、{(-1,-2)}', '{cases(c=-1; a+b+c=2; a-b+c=-2)}',
         '-1', '3', '1', '2', '{y=x^2+2x-1}', '{x=-1}：{1-2-1=-2}　✔'),
    ]:
        P.append(sub_title(f'練 {n}．經過 {pts}（6 分）'))
        P.append(twbl([
            span_row('設 {y=ax^2+bx+c}', '1 分'),
            span_row(f'代入：{cs}', '代入三點 2 分'),
            eq_row('{a-b}', f'{{{e1}}}', '代入 {c} 後的 ①'),
            eq_row('{a+b}', f'{{{e2}}}', '②'),
            eq_row('{2a}', f'{{{int(e1) + int(e2)}}}', '① ＋ ②'),
            eq_row('{a}', f'{{{a_}}}', '求 {a} 1 分'),
            eq_row('{b}', f'{{{b_}}}', '求 {b} 1 分'),
            answer_row(ans, f'1 分。{chk}'),
        ], col_frac=(0.30, 0.05, 0.40, 0.05, 0.07, 0.04)))
    P.append(para('※ 練 10 三點的次序故意打亂，{(0,-1)} 寫在最前；學生要自己認出哪一點給出 {c}。', sz=22))

    P.append(heading('四、已知頂點求二次函數的解析式（18 分）'))
    for n, v, pt, sub1, e_l, e_r, k4, a_, ans, warn in [
        (11, '{(3,-2)}', '{(5,10)}', '{y=a(x-3)^2-2}', '{10}', '{a(5-3)^2-2}', ('{4a}', '{12}'),
         '{3}', '{y=3(x-3)^2-2}', ''),
        (12, '{(-2,5)}', '{(0,1)}', '{y=a(x+2)^2+5}', '{1}', '{a(0+2)^2+5}', ('{4a}', '{-4}'),
         '{-1}', '{y=-(x+2)^2+5}', '※ 易錯：寫成 {(x-2)^2}（{h} 的符號沒反過來），代入頂點 2 分全扣'),
        (13, '{(-1,-3)}', '{(2,15)}', '{y=a(x+1)^2-3}', '{15}', '{a(2+1)^2-3}', ('{9a}', '{18}'),
         '{2}', '{y=2(x+1)^2-3}', '※ 易錯：{(2+1)^2} 算成 {2^2+1}'),
    ]:
        P.append(sub_title(f'練 {n}．頂點 {v}，經過 {pt}（6 分）'))
        P.append(twbl([
            span_row('設 {y=a(x-h)^2+k}', '1 分'),
            span_row(f'代入頂點：{sub1}', '代入頂點 2 分'),
            eq_row(e_l, e_r, f'代入點 {pt} 1 分'),
            eq_row(k4[0], k4[1], ''),
            eq_row('{a}', a_, '求 {a} 1 分'),
            answer_row(ans, '1 分。' + warn if warn else '1 分'),
        ], col_frac=(0.30, 0.05, 0.40, 0.05, 0.07, 0.04)))

    P.append(heading('五、拋物線形拱橋（22 分）'))
    for n, H, Wd, d, a_txt, y_txt, yw, xx, w, pts in [
        (14, 4, 4, 1, '{-1}', '{y=-x^2+4}', 3, 1, 2, 7),
        (15, 9, 12, 4, '{-frac(1,4)}', '{y=-frac(1,4)x^2+9}', 5, 4, 8, 7),
        (16, 8, 8, 2, '{-frac(1,2)}', '{y=-frac(1,2)x^2+8}', 6, 2, 4, 8),
    ]:
        hw = Wd // 2
        rhs_y = y_txt[3:-1]
        P.append(sub_title(f'練 {n}．拱頂到水面 {H} 米、水面寬 {Wd} 米、警戒水位距拱頂 {d} 米（{pts} 分）'))
        P.append(twbl([
            span_row(f'(1) {{C(0,{H})}}，{{A(-{hw},0)}}，{{B({hw},0)}}', '每點 1 分'),
            span_row(f'(2) 設 {{y=a(x-0)^2+{H}}}，即 {{y=ax^2+{H}}}', '代入頂點 1 分'),
            eq_row('{0}', f'{{a×{hw}^2+{H}}}', f'代入 {{B({hw},0)}} 1 分'),
            eq_row(f'{{{hw * hw}a}}', f'{{-{H}}}', ''),
            eq_row('{a}', a_txt, ''),
            answer_row(y_txt, '1 分'),
            span_row(f'(3) 警戒水位離拱頂 {d} 米 → {{y={H}-{d}={yw}}}', ''),
            eq_row(f'{{{rhs_y}}}', f'{{{yw}}}', '代入解析式'),
            eq_row('{x^2}', f'{{{xx * xx}}}', ''),
            or_row('{x_1}', f'{{{xx}}}', '{x_2}', f'{{-{xx}}}', ''),
            answer_row(f'水面寬度 {{{xx}-(-{xx})={w}}} 米',
                       '1 分' if pts == 7 else '解出 {x} 1 分、寬度 1 分'),
        ]))
    P.append(para('※ 第 (3) 問常見錯誤：① 把「離拱頂 d 米」直接當 {y=d} 代入（應是 {y=}拱頂高 {-d}）；'
                  '② 只寫一個 {x} 就當寬度（寬度是兩根之差）。', sz=22))
    save(P, BASE + '_教師卷.docx', FOOT + '（教師卷）')


if __name__ == '__main__':
    draw_figs()
    student()
    teacher()
    print('OK')
