# -*- coding: utf-8 -*-
"""
build_調適練習.py — 高三文數學大測一 測驗工作紙 調適練習（學生版＋教師答案版）

來源：同資料夾《高三測驗工作紙.pdf》（24 題：單選 1–20、解答 21–24）。
使用者 2026-09-22 指定：
  1. 沿用高一文／理調適練習做法（題目照錄、題下灰底、只給方法不洩答、另出教師答案版），
     但要調得更多：每題題下直接列「公式」，並加「框架」——
     選擇題加簡短步驟框架、適合的題加表格／數線式框架、解答題用步驟填空骨架＋作答分區；
  2. 原稿兩處筆誤改正（第 3 題 g(2027)→g(2025)；第 24 題點 (4, 16/5)→(4, 12/5)），教師版註明；
  3. 21(b)、23(b) 題目照印，教師版標記「建議抽離生略過」；
  4. 高三甲班文組抽離，考前複習；無對應測驗卷，不做高相似題標記；
  5. 盡量壓在 6 頁內。
教學設計：主 D7 提示卡（逐題公式）＋輔 D2 手順卡（步驟填空框架）＋輔 D9 草稿分區（解答題作答分區）。
逐題驗算見《驗算_高三文數學大測一.md》。
"""
import os
from sheet_common import *  # noqa

OUT = HERE
UNIT = '大測一測驗工作紙（綜合複習）'
FOOTER = '高三數學．文科大測一測驗工作紙調適練習'
BASE = '調適練習_高三文數學大測一工作紙'
MEDIA = MediaRegistry()
B = '＿＿＿'        # 填空位
OPT = '【可選題】'    # 使用者 2026-09-22 指定的可選題（原位標記，不搬位）
P = []


# ============================ 圖 ============================
def _mpl():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams['font.family'] = ['Microsoft JhengHei', 'DejaVu Sans']
    return plt


def fig_grid(path):
    """第 18 題：空白坐標格（0–6），給學生自己畫三條邊界線。"""
    if os.path.exists(path):
        return path
    plt = _mpl()
    fig, ax = plt.subplots(figsize=(2.3, 2.3), dpi=220)
    ax.set_xlim(-0.4, 6.4); ax.set_ylim(-0.4, 6.4); ax.set_aspect('equal')
    for k in range(7):
        ax.plot([k, k], [0, 6], color='#BBBBBB', lw=0.6)
        ax.plot([0, 6], [k, k], color='#BBBBBB', lw=0.6)
    ax.annotate('', xy=(6.4, 0), xytext=(-0.3, 0), arrowprops=dict(arrowstyle='->', lw=1.1))
    ax.annotate('', xy=(0, 6.4), xytext=(0, -0.3), arrowprops=dict(arrowstyle='->', lw=1.1))
    for k in range(1, 6):
        ax.text(k, -0.32, str(k), ha='center', va='top', fontsize=7)
        ax.text(-0.18, k, str(k), ha='right', va='center', fontsize=7)
    ax.text(6.35, -0.3, 'x', fontsize=9, style='italic', family='serif', va='top')
    ax.text(-0.3, 6.3, 'y', fontsize=9, style='italic', family='serif', ha='right')
    ax.text(-0.18, -0.2, 'O', fontsize=7, ha='right', va='top', style='italic', family='serif')
    ax.axis('off')
    fig.savefig(path, dpi=220, bbox_inches='tight', pad_inches=0.02, facecolor='white')
    plt.close(fig)
    return path


def fig_tree(path):
    """第 22 題：兩次不放回抽球樹狀圖，分支機率留空（分母已給，提醒「不放回」）。"""
    if os.path.exists(path):
        return path
    plt = _mpl()
    fig, ax = plt.subplots(figsize=(4.6, 2.3), dpi=220)
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis('off')
    kw = dict(ha='center', va='center', fontsize=9)
    ax.text(0.5, 2.5, '開始', **kw)
    first = [(3.4, 3.8, '紅'), (3.4, 1.2, '綠')]
    for x, y, t in first:
        ax.plot([1.05, x - 0.35], [2.5, y], color='black', lw=0.9)
        ax.text(x, y, t, **kw)
        ax.text((1.05 + x) / 2 - 0.1, (2.5 + y) / 2 + (0.3 if y > 2.5 else -0.3), '＿/5', fontsize=8, ha='center', va='center')
        for dy, t2 in ((0.65, '紅'), (-0.65, '綠')):
            y2 = y + dy
            ax.plot([x + 0.35, 6.3], [y, y2], color='black', lw=0.9)
            ax.text(6.6, y2, t2, **kw)
            ax.text((x + 6.3) / 2 + 0.2, (y + y2) / 2 + (0.25 if dy > 0 else -0.25), '＿/4', fontsize=8, ha='center', va='center')
            ax.text(8.6, y2, '→ 機率＝＿＿，X＝＿', fontsize=8, ha='center', va='center')
    ax.text(3.4, 4.85, '第 1 次', fontsize=8, ha='center', color='#444444')
    ax.text(6.6, 4.85, '第 2 次', fontsize=8, ha='center', color='#444444')
    fig.savefig(path, dpi=220, bbox_inches='tight', pad_inches=0.02, facecolor='white')
    plt.close(fig)
    return path


FIG_GRID = fig_grid(os.path.join(HERE, '_fig_q18_grid.png'))
FIG_TREE = fig_tree(os.path.join(HERE, '_fig_q22_tree.png'))


def fig_numline(path):
    """第 7 題：穿針引線法用的空白數線（使用者 2026-09-22 指定此法）。
    零點不預先標出，只在右上方標「起點」，讓學生自己標點、畫曲線。"""
    if os.path.exists(path):
        return path
    plt = _mpl()
    fig, ax = plt.subplots(figsize=(6.2, 1.25), dpi=220)
    ax.set_xlim(0, 10); ax.set_ylim(-1.1, 1.3); ax.axis('off')
    ax.annotate('', xy=(9.9, 0), xytext=(0.1, 0), arrowprops=dict(arrowstyle='->', lw=1.2))
    ax.text(9.85, -0.28, 'x', fontsize=10, style='italic', family='serif', va='top')
    ax.plot([9.1], [0.95], marker='o', ms=4, color='black')
    ax.text(9.1, 1.12, '起點（從這裏向左畫）', fontsize=8, ha='right', va='bottom')
    ax.text(0.2, 0.55, '上方＝正', fontsize=8, color='#555555')
    ax.text(0.2, -0.75, '下方＝負', fontsize=8, color='#555555')
    fig.savefig(path, dpi=220, bbox_inches='tight', pad_inches=0.02, facecolor='white')
    plt.close(fig)
    return path


FIG_NUMLINE = fig_numline(os.path.join(HERE, '_fig_q7_numline.png'))


def img(path, w):
    return expand_image(image_para(path, width_cm=w, jc='left'), MEDIA)


# 第 19 題：平均數 x̄（底層 {} 標記沒有 overline，直接用 OMML accent 組）
XBAR = '<m:acc><m:accPr><m:chr m:val="̄"/></m:accPr><m:e>' + mr('x') + '</m:e></m:acc>'


def _dev(i):
    return sup(mr('(') + sub(mr('x'), mr(i)) + mr('−') + XBAR + mr(')'), mr('2'))


Q19_FORMULA = dense(tight(shaded_box(
    [('t', '公式：平均數 '), ('m', omath(XBAR + mr('=') + frac(fn('數據總和'), mr('n')))),
     ('t', '；方差 '), ('m', omath(sup(mr('s'), mr('2')) + mr('=') + frac(mr('1'), mr('n')) + mr('[')
                                  + _dev('1') + mr('+') + _dev('2') + mr('+⋯+') + _dev('n') + mr(']'))),
     ('t', '。')], sz=22)))


# ============================ 組裝 helper ============================
def item(n, stem, options=None, formula=(), steps=(), extra=(), work=0, cols=None, formula_xml=(), opt=False):
    """一題＝題幹（原文）＋選項＋公式／框架灰底條＋（表格等）額外框架＋作答線，整格一個框。"""
    body = [tight(para(f'{n}．' + (OPT if opt else '') + stem))]
    if options:
        body.append(opts(options, cols=cols))
    body += list(formula_xml)
    body += scaf(formula, steps)
    body += list(extra)
    if work:
        body += lines(work)
    P.append(box(body))


def zones(rows):
    """解答題作答分區（D9）：左欄分區名、右欄步驟填空骨架。rows＝[(分區名, [行, …]), …]"""
    tr = []
    for lab, ls in rows:
        tr.append([lab, [x if x.lstrip().startswith('<') else dense(tight(para(x, sz=22))) for x in ls]])
    return grid(tr, [1250, INNER_W - 1250 - 300], sz=22, head_row=False, head_col=True, jc='left')


def long_item(n, stem, parts, opt=False):
    """解答題：題幹＋各小題（小題題幹、公式、分區骨架）。"""
    body = [tight(para(f'{n}．' + (OPT if opt else '') + stem))]
    for sstem, formula, zrows in parts:
        body.append(tight(para(sstem)))
        body += scaf(formula, ())
        body.append(zones(zrows))
        body.append(spacer(80))
    P.append(box(body, keep=False))


def section(t, pb=False):
    return tight(para([('t', t)], bold=True, sz=HEADING_SZ, page_break_before=pb)).replace(
        '<w:pPr>', '<w:pPr><w:keepNext/>', 1)


# ============================ 卷首 ============================
P += [masthead(SUBJECT, UNIT, '調適練習'),
      tight(student_info_row()),
      tight(para([('t', '使用方法：每題下面的灰底有「公式」和「框架」。先看公式，再沿著框架一步一步填空（＿＿），'
                   '填完就是答案。選擇題最後把答案寫進題目的（　）。標有【可選題】的題目可以留到最後，有時間才做。')], sz=22)),
      spacer(100)]

# ============================ 一、單選題 ============================
P.append(section('一、單選題'))

item(1, '設全集 {U}＝' + L('1,2,3,4,5,6') + '，集合 {A}＝' + S('x', 'x^2-7x+10=0') + '，{B}＝' + S('x', '2x-8<0') +
     '，則 {∁_U (A∩B)}＝（    ）',
     [L('1,2,5,6'), L('3,4,6'), L('1,3,4,6'), L('2,5'), L('1,3,4,5,6')],
     formula=['補集 {∁_U M}＝在 {U} 裏面、但不在 {M} 裏面的元素。'],
     steps=[f'① {{x^2-7x+10=(x-{B})(x-{B})=0}} → {{A}}＝｛{B}｝　② {{2x-8<0}} → {{x<{B}}}',
            f'③ {{A∩B}}＝｛{B}｝（{{A}} 中哪些數小於 ② 的數？）　④ {{∁_U (A∩B)}}＝｛{B}{B}{B}｝'], opt=True)

item(2, '多項式 {Q(x)} 除以 {x-2} 餘數為 7，除以 {x+1} 餘數為 {-2}，若 {Q(x)} 除以 {(x-2)(x+1)} 的餘式為 {ax+b}，則 {a+b}＝（    ）',
     ['1', '2', '3', '4', '5'],
     formula=['餘式定理：{Q(x)} 除以 {x-c} 的餘數＝{Q(c)}。　寫成 {Q(x)=(x-2)(x+1)⋅q(x)+ax+b}。'],
     steps=[f'① 代 {{x=2}}：{{2a+b}}＝{B}　② 代 {{x=-1}}：{B}{{a+b}}＝{B}　③ 兩式相減解出 {{a}}＝{B}，{{b}}＝{B}，{{a+b}}＝{B}'], opt=True)

item(3, '定義在 {ℝ} 的函數滿足 {g(x+6)=g(x)}，已知 {g(3)=-4}，則 {g(2025)}＝（    ）',
     ['{-4}', '{-2}', '0', '3', '4'],
     formula=['{g(x+6)=g(x)} 表示每隔 6 就重複一次（週期 6）：{g(x+6k)=g(x)}。'],
     steps=[f'① {{2025÷6}}＝{B} 餘 {B}　② {{g(2025)=g({B})}}＝{B}'])

item(4, '若 {frac(1,x)+frac(2,y)=3}，其中 {x>0, y>0}，則 {2x+y} 的最小值為（    ）',
     ['{frac(8,3)}', '3', '{frac(10,3)}', '4', '{frac(14,3)}'],
     formula=['均值不等式：{a, b>0} 時 {a+b≥2sqrt(ab)}（{a=b} 時取等號）。',
              '「乘 1」技巧：{frac(1,3)(frac(1,x)+frac(2,y))=1}，所以 {2x+y=frac(1,3)(2x+y)(frac(1,x)+frac(2,y))}。'],
     steps=[f'① 展開 {{(2x+y)(frac(1,x)+frac(2,y))}}＝{B}＋{{frac(4x,y)+frac(y,x)}}＋{B}',
            f'② {{frac(4x,y)+frac(y,x)≥2sqrt(frac(4x,y)⋅frac(y,x))}}＝{B}　③ {{2x+y≥frac(1,3)×({B}+{B})}}＝{B}'], opt=True)

item(5, '7 個人排一列照相，若甲、乙兩人不相鄰，丙不在最左邊，則排列方法共有多少種（    ）',
     ['2400', '2880', '3120', '3600', '4320'],
     formula=['{n} 個人排一列：{n!} 種。　甲乙「相鄰」：把甲乙捆成一個人，再乘 2（甲乙可對調）。',
              '「不相鄰」＝全部－相鄰。'],
     steps=[f'① 甲乙不相鄰：{{7!-2×{B}!}}＝{B}',
            f'② 其中「丙在最左邊」而甲乙不相鄰：丙固定後剩 6 人，{{6!-2×{B}!}}＝{B}',
            f'③ 答案＝① － ②＝{B}'])

item(6, '等比數列 {a_n}，{a_1+a_2=12}，{a_3+a_4=48}，則 {a_7+a_8}＝（    ）',
     ['192', '384', '768', '1024', '1536'],
     formula=['等比數列：{a_n=a_1 r^{n-1}}，每往後 1 項就乘 {r}。'],
     steps=[f'① {{a_3+a_4}} 比 {{a_1+a_2}} 每項多乘了 {{r}} 的 {B} 次方 → {{r^2}}＝{B}',
            f'② {{a_7+a_8}} 比 {{a_1+a_2}} 每項多乘了 {{r}} 的 {B} 次方 → {{a_7+a_8=12×}}{B}＝{B}'])

item(7, '不等式 {frac(x^2-4,x-1)≤0} 的解集為（    ）',
     ['({-∞, -2}]{∪}[{1, 2}]', '({-∞, -2}]{∪}({1, 2}]', '[{-2, 1}){∪}[{2, +∞})',
      '[{-2, 1}]{∪}[{2, +∞})', '({-∞, -2}]{∪}[{2, +∞})'], cols=3,
     formula=['穿針引線法：分式 {frac(A,B)≤0} 與 {A⋅B≤0} 的正負相同（但 {B≠0}），所以把分子、分母的因式全部拆開，'
              '每個因式寫成 {(x-□)} 的樣子（{x} 的係數為正）。',
              '在數線上標出所有零點，從「最右邊的上方」開始，由右向左畫一條曲線，每遇到一個零點就穿過數線一次。'
              '曲線在數線上方＝正（{>0}），在下方＝負（{<0}）。',
              '端點：分母的零點一定不取（空心 ○、圓括號）；分子的零點在「{≤}」時要取（實心 ●、方括號）。'],
     steps=[f'① {{frac(x^2-4,x-1)=frac((x+{B})(x-{B}),x-1)}}：分子零點 {{x}}＝{B}、{B}（實心）；分母零點 {{x}}＝{B}（空心）',
            '② 在下面數線上由小到大標出三個零點，從右上方的「起點」開始穿針引線：'],
     extra=[img(FIG_NUMLINE, 12.5),
            dense(tight(shaded_box('　　　③「{≤0}」取曲線在數線「下方」的部分，連同實心點 → 解集＝' + B + B + B, sz=22)))])

item(8, '若 {fn(log)_2 3=m}，{fn(log)_3 5=n}，則 {fn(log)_15 24}＝（    ）',
     ['{frac(m+3,mn+m+1)}', '{frac(3m+1,mn+1)}', '{frac(m+3,mn+m)}', '{frac(3m+1,mn+m+1)}', '{frac(2m+3,mn+m+1)}'],
     formula=['換底：{fn(log)_a b=frac(fn(log)_c b,fn(log)_c a)}；{fn(log)_a b⋅fn(log)_b c=fn(log)_a c}；'
              '{fn(log)(MN)=fn(log) M+fn(log) N}；{fn(log)_2 8=3}。'],
     steps=[f'① {{fn(log)_2 5=fn(log)_2 3⋅fn(log)_3 5}}＝{B}（用 {{m, n}} 表示）',
            f'② 全部換成以 2 為底：{{fn(log)_15 24=frac(fn(log)_2 24,fn(log)_2 15)}}',
            f'③ {{fn(log)_2 24=fn(log)_2 (8×3)}}＝{B}＋{B}；{{fn(log)_2 15=fn(log)_2 (3×5)}}＝{B}＋{B}　④ 對照選項'])

item(9, '{(x-frac(1,sqrt(x)))^6} 的展開式中，常數項為（    ）',
     ['{-15}', '{-24}', '320', '24', '15'],
     formula=['二項式通項：{(a+b)^n} 的第 {k+1} 項 {T_{k+1}=C_n^k a^{n-k} b^k}。　{frac(1,sqrt(x))=x^{-frac(1,2)}}。'],
     steps=[f'① {{T_{{k+1}}=C_6^k x^{{6-k}}(-x^{{-frac(1,2)}})^k=(-1)^k C_6^k x^(…)}}，{{x}} 的指數＝{B}（用 {{k}} 表示）',
            f'② 常數項 → {{x}} 的指數＝0 → {{k}}＝{B}　③ 常數項＝{{(-1)^k C_6^k}}＝{B}'])

item(10, '已知 {fn(sin )α=-frac(3,5)}，{α} 在第三象限，則 {fn(tan )(α+frac(π,4))}＝（    ）',
     ['{-frac(1,7)}', '{frac(1,7)}', '{-7}', '7', '{-frac(4,3)}'],
     formula=['{fn(sin)^2 α+fn(cos)^2 α=1}；{fn(tan )α=frac(fn(sin )α,fn(cos )α)}；'
              '{fn(tan )(A+B)=frac(fn(tan )A+fn(tan )B,1-fn(tan )A fn(tan )B)}；{fn(tan )frac(π,4)=1}。'],
     steps=[f'① 第三象限：{{fn(cos )α}} 取 {B} 號，{{fn(cos )α}}＝{B}　② {{fn(tan )α}}＝{B}（第三象限 tan 是正還是負？）',
            f'③ {{fn(tan )(α+frac(π,4))}}＝（{B}＋1）÷（1－{B}）＝{B}'])

item(11, '等差數列 {b_n} 中，前 {n} 項和 {T_n}，若 {T_11=99}，則 {b_1+b_3+b_5+b_7+b_9+b_11}＝（    ）',
     ['45', '54', '63', '72', '81'],
     formula=['等差數列前 {n} 項和 {T_n=frac(n(b_1+b_n),2)}。　下標和相等，兩項和就相等：{b_1+b_11=b_3+b_9=b_5+b_7=2b_6}。'],
     steps=[f'① {{T_11=frac(11(b_1+b_11),2)=11b_6}}＝99 → {{b_6}}＝{B}',
            f'② 六項配成 3 對，每對＝{{2b_6}}＝{B} → 總和＝{{3×}}{B}＝{B}'])

item(12, '設 {x+frac(1,x)=4}，則 {x^3+frac(1,x^3)}＝（    ）',
     ['52', '56', '60', '64', '68'],
     formula=['立方和：{a^3+b^3=(a+b)^3-3ab(a+b)}。'],
     steps=[f'① 取 {{a=x}}，{{b=frac(1,x)}}：{{ab}}＝{B}，{{a+b}}＝{B}',
            f'② {{x^3+frac(1,x^3)=({B})^3-3×{B}×{B}}}＝{B}'], opt=True)

item(13, '橢圓 {frac(x^2,25)+frac(y^2,9)=1}，點 {P} 在橢圓上，{F_1, F_2} 為兩焦點，則 {|PF_1|⋅|PF_2|} 的最大值為（    ）',
     ['9', '16', '25', '34', '50'],
     formula=['橢圓 {frac(x^2,a^2)+frac(y^2,b^2)=1}（{a>b>0}）上任一點：{|PF_1|+|PF_2|=2a}。',
              '兩正數的和固定時，兩數相等積最大：{pq≤(frac(p+q,2))^2}。'],
     steps=[f'① {{a^2=25}} → {{a}}＝{B}，{{|PF_1|+|PF_2|}}＝{B}　② {{|PF_1|⋅|PF_2|≤}}（{B}÷2）²＝{B}'], opt=True)

item(14, '在 {△ABC} 中，{a=3, b=4, ∠C=60°}，則 {△ABC} 的面積為（    ）',
     ['{3sqrt(3)}', '{6sqrt(3)}', '{frac(3sqrt(3),2)}', '12', '6'],
     formula=['兩邊夾一角的面積：{S=frac(1,2)ab fn( sin )C}。　{fn(sin )60°=frac(sqrt(3),2)}。'],
     steps=[f'① {{S=frac(1,2)×{B}×{B}×}}{B}＝{B}'], opt=True)

item(15, '擲兩顆公正骰子，點數和為質數的機率為（    ）',
     ['{frac(7,18)}', '{frac(5,12)}', '{frac(4,9)}', '{frac(1,2)}', '{frac(11,36)}'],
     extra=[side_by_side(
         [grid([['和'] + [str(k) for k in range(1, 7)]] + [[str(r)] + [''] * 6 for r in range(1, 7)],
               [560] * 7, sz=20, row_h=300, ind=0)],
         scaf(['機率＝符合的結果數 ÷ 全部結果數；兩顆骰共有 {6×6=36} 個結果。',
               '質數：只有 1 和自己兩個因數，例如 2、3、5、7、11（2 也是質數）。'],
              ['① 在左表每格填上兩顆骰子的點數和。',
               f'② 把是質數的格圈起來，共 {B} 格。',
               f'③ 機率＝{B}÷36＝{B}（約簡）']),
         560 * 7 + 200, INNER_W - 560 * 7 - 200 - 300)])

item(16, '已知 {t>0}，{t^2-3t+1=0}，求 {t^{frac(1,2)}+t^{-frac(1,2)}} 的值（    ）',
     ['{sqrt(5)}', '{sqrt(7)}', '3', '{sqrt(11)}', '4'],
     formula=['{(a+b)^2=a^2+2ab+b^2}；{t^{frac(1,2)}⋅t^{-frac(1,2)}=t^0=1}；{(t^{frac(1,2)})^2=t}。'],
     steps=[f'① 方程兩邊除以 {{t}}：{{t-3+frac(1,t)=0}} → {{t+frac(1,t)}}＝{B}',
            f'② {{(t^{{frac(1,2)}}+t^{{-frac(1,2)}})^2=t+2+frac(1,t)}}＝{B}　③ 原式大於 0，開方取正 → {B}'])

item(17, '函數 {y=2fn( sin )(2x-frac(π,3))+1} 的最小正週期與最大值分別為（    ）',
     ['{π, 3}', '{2π, 3}', '{π, 2}', '{2π, 2}', '{frac(π,2), 3}'],
     formula=['{y=Afn( sin )(ωx+φ)+k}：週期 {T=frac(2π,|ω|)}；最大值＝{|A|+k}（因為 {fn(sin )} 最大是 1）。'],
     steps=[f'① {{ω}}＝{B} → {{T}}＝{B}　② {{A}}＝{B}，{{k}}＝{B} → 最大值＝{B}'], opt=True)

item(18, '實數 {x, y} 滿足 {cases(x≥1; y≥1; x+y≤5)}，則 {z=2x-y} 的最大值為（    ）',
     ['1', '3', '5', '7', '9'],
     formula=['線性規劃：可行域是一個多邊形，{z} 的最大值、最小值一定出現在「頂點」。'],
     steps=['① 在左圖畫出 {x=1}、{y=1}、{x+y=5} 三條線，塗出三個條件同時成立的三角形。',
            '② 求三個頂點，逐個代入 {z=2x-y}，最大的就是答案：'],
     extra=[side_by_side(
         [img(FIG_GRID, 4.0)],
         [grid([['頂點', '由哪兩條線相交', '坐標', '{z=2x-y}'],
                ['①', '{x=1} 與 {y=1}', '(　　,　　)', ''],
                ['②', '{y=1} 與 {x+y=5}', '(　　,　　)', ''],
                ['③', '{x=1} 與 {x+y=5}', '(　　,　　)', '']],
               [700, 2500, 1500, 1300], sz=22, row_h=420, ind=0)],
         2500, INNER_W - 2500 - 300)])

item(19, '樣本數據 {2, 4, 6, 8, a} 的算術平均數為 5，則此組數據的方差為（    ）',
     ['4', '4.8', '5.2', '6', '6.4'],
     steps=[f'① {{2+4+6+8+a=5×5}} → {{a}}＝{B}　② 填下表：'],
     formula_xml=[Q19_FORMULA],
     extra=[grid([['{x}', '2', '4', '6', '8', '{a}＝'],
                  ['{x-5}', '', '', '', '', ''],
                  ['{(x-5)^2}', '', '', '', '', '']],
                 [1500, 1100, 1100, 1100, 1100, 1300], sz=22, row_h=380),
            tight(shaded_box(f'　　　③ 最後一列相加＝{B}，{{s^2}}＝{B}÷5＝{B}', sz=22))])

item(20, '函數 {f(x)=frac(sqrt(4-x^2),x-1)} 的定義域為（    ）',
     ['[{-2, 2}]', '[{-2, 1}){∪}({1, 2}]', '({-2, 1}){∪}({1, 2})', '({-2, 2}]', '[{-2, 1}){∪}[{1, 2}]'], cols=3,
     formula=['定義域兩條規則：根號內 {≥0}；分母 {≠0}。兩個條件要同時成立。'],
     steps=[f'① {{4-x^2≥0}} → {{x^2≤4}} → {B}{{≤x≤}}{B}　② {{x-1≠0}} → {{x≠}}{B}',
            '③ 在數線上畫出 ① 的一段，再挖走 ② 的點（空心）→ 對照選項'])

# ============================ 二、解答題 ============================
P.append(section('二、解答題'))

long_item(21, '已知 {γ, δ∈(0, π)}，{fn(cos )γ=-frac(5,13)}，{fn(sin )(γ-δ)=frac(33,65)}。', [
    ('(a) 求 {fn(sin )γ}、{fn(tan )γ}。',
     ['{fn(sin)^2 γ+fn(cos)^2 γ=1}；{γ∈(0, π)} 時 {fn(sin )γ>0}；{fn(tan )γ=frac(fn(sin )γ,fn(cos )γ)}。'],
     [('① 已知', [f'{{fn(cos )γ=-frac(5,13)}}，{{γ}} 在第 {B} 象限（cos 負、在 {{(0, π)}} 內）']),
      ('② 列式', [f'{{fn(sin )γ=sqrt(1-({B})^2)}}　　{{fn(tan )γ=frac(fn(sin )γ,fn(cos )γ)}}']),
      ('③ 答', [f'{{fn(sin )γ}}＝{B}{B}　　{{fn(tan )γ}}＝{B}{B}'])]),
    ('(b) 若 {γ-δ} 為銳角，求 {fn(cos )2δ}。',
     ['把 {δ} 寫成 {δ=γ-(γ-δ)}：{fn(cos )δ=fn(cos )γ fn(cos )(γ-δ)+fn(sin )γ fn(sin )(γ-δ)}。',
      '二倍角：{fn(cos )2δ=2fn(cos)^2 δ-1}。'],
     [('① 已知', [f'{{γ-δ}} 是銳角 → {{fn(cos )(γ-δ)>0}}，{{fn(cos )(γ-δ)=sqrt(1-(frac(33,65))^2)}}＝{B}']),
      ('② 列式', [f'{{fn(cos )δ=({B})({B})+({B})({B})}}＝{B}{B}']),
      ('③ 計算', [f'{{fn(cos )2δ=2({B}{B})^2-1}}＝{B}{B}', '']),
      ('④ 答', [f'{{fn(cos )2δ}}＝{B}{B}{B}'])]),
], opt=True)

long_item(22, '一袋中有 5 顆球，2 顆紅球，3 顆綠球，每次隨機取出一球後不放回。', [
    ('(a) 抽取 2 次，求至多出現一次綠球的機率。',
     ['不放回：第 2 次時袋中只剩 4 顆。　沿樹狀圖一條路徑：機率相乘。',
      '「至多一次」＝0 次或 1 次＝1 －（兩次都是綠的機率）。'],
     [('① 樹狀圖', [img(FIG_TREE, 8.6)]),
      ('② 列式', [f'兩次都是綠的機率＝{{frac(3,5)×}}{B}＝{B}']),
      ('③ 答', [f'至多一次綠的機率＝{{1-}}{B}＝{B}'])]),
    ('(b) 抽取 2 次，求綠球數量 {X} 的數學期望。',
     ['數學期望 {E(X)=x_1 p_1+x_2 p_2+⋯}（每個值 × 它的機率，再相加）。'],
     [('① 分佈', [grid([['{X}', '0', '1', '2'], ['{P(X)}', '', '', '']],
                        [1300, 1500, 1500, 1500], sz=22, row_h=420, ind=0),
                  tight(para('（三個機率加起來要等於 1，可用來檢查）', sz=20))]),
      ('② 答', [f'{{E(X)=0×{B}+1×{B}+2×}}{B}＝{B}'])]),
])

long_item(23, '數列 {a_n} 前 {n} 項和 {S_n=3n^2+2n}。正項等比數列 {b_n}，{b_1=4, b_3=36}。', [
    ('(a) 求 {a_n, b_n} 的通項。',
     ['{a_1=S_1}；{n≥2} 時 {a_n=S_n-S_{n-1}}（求完要檢查 {n=1} 是否也符合）。　等比 {b_n=b_1 q^{n-1}}。'],
     [('① {a_n}', [f'{{a_1=S_1}}＝{B}　　{{S_{{n-1}}=3(n-1)^2+2(n-1)}}＝{B}{B}{B}',
                   f'{{a_n=S_n-S_{{n-1}}}}＝{B}{B}　（代 {{n=1}} 檢查：＝{B}，與 {{a_1}} 相同嗎？）']),
      ('② {b_n}', [f'{{b_3=b_1 q^2}} → {{q^2}}＝{B}，正項 → {{q}}＝{B}　　{{b_n}}＝{B}{B}'])]),
    (OPT + '(b) 令 {d_n=a_n-b_n}，證明 {d_n} 前 {n} 項和 {T_n<0} 對足夠大 {n} 成立，並寫出 {T_n} 表達式。',
     ['{T_n}＝（{a_n} 的前 {n} 項和）－（{b_n} 的前 {n} 項和）；等比數列和 {frac(b_1(q^n-1),q-1)}。'],
     [('① 列式', [f'代入 {{b_1}}＝{B}、{{q}}＝{B}：{{b_n}} 的前 {{n}} 項和＝{B}{B}',
                  f'{{T_n}}＝{B}{B}{B}{B}']),
      ('② 試數', [f'{{T_1}}＝{B}，{{T_2}}＝{B}，{{T_3}}＝{B}，{{T_4}}＝{B}']),
      ('③ 說明', ['從第 ＿ 項起 {T_n<0}，因為 {3^n} 增長得比 {n^2} 快：', ''])]),
])

long_item(24, '已知橢圓 {C:frac(x^2,m^2)+frac(y^2,n^2)=1 (m>n>0)}，離心率 {e=frac(3,5)}，且點 {(4, frac(12,5))} 在曲線 {C} 上。', [
    ('(a) 求橢圓 {C} 的標準方程。',
     ['長軸在 {x} 軸：{e=frac(c,m)}，{m^2=n^2+c^2}。　點在曲線上＝把坐標代入方程會成立。'],
     [('① 設', [f'{{e=frac(3,5)}} → 設 {{m=5k}}，{{c=3k}}，則 {{n}}＝{B}{{k}}']),
      ('② 代入', [f'把點 {{(4, frac(12,5))}} 代入 {{frac(x^2,m^2)+frac(y^2,n^2)=1}}（{{m}}、{{n}} 用 ① 的結果）→ {{k}}＝{B}']),
      ('③ 答', [f'{{C}}：{B}{B}{B}'])]),
    (OPT + '(b) 直線 {y=tx+2} 與曲線 {C} 交於兩點 {M, N}，若 {t=1}，求弦 {MN} 的長。',
     ['弦長 {|MN|=sqrt(1+t^2)⋅|x_1-x_2|}；二次方程 {Ax^2+Bx+C=0} 的兩根差 {|x_1-x_2|=frac(sqrt(Δ),|A|)}，{Δ=B^2-4AC}。'],
     [('① 代入', [f'把 {{y=x+2}} 代入 (a) 的方程，去分母整理：{B}{{x^2+{B}x+{B}=0}}']),
      ('② 計算', [f'{{Δ}}＝{B}{B}，{{|x_1-x_2|}}＝{B}{B}']),
      ('③ 答', [f'{{|MN|=sqrt(1+1^2)×}}{B}{B}＝{B}{B}'])]),
])

# ============================ 三、補充題（相似題） ============================
# 使用者 2026-09-22 追加：仿四校聯考 2024 選擇 1、14 題及 2023 選擇 2 題出相似題（改數字，
# 2023 第 2 題的問法改為兩個函數值相加、函數名改用 g），調適做法同上。
P.append(section('三、補充題'))

item(25, '設集合 {A}＝' + S('x', 'x^2-2x-8≤0') + '，{B}＝' + S('x', '2x+a≥0') + '，且 {A∩B}＝' + S('x', '1≤x≤4') + '，求 {a}。',
     ['{-4}', '{-2}', '{-1}', '2', '4'],
     formula=['二次不等式「{≤0}」取兩根之間（包含兩根）。　交集＝兩個範圍在數線上重疊的部分。'],
     steps=[f'① {{x^2-2x-8=(x-{B})(x+{B})≤0}} → {{A}}：{B}{{≤x≤}}{B}',
            f'② {{2x+a≥0}} → {{x≥frac(-a,2)}}　③ 交集的左端點 1 由 {{B}} 決定：{{frac(-a,2)}}＝{B} → {{a}}＝{B}'])

item(26, '已知 {x^2-4x+1=0}，求 {x^4+frac(1,x^4)}。',
     ['14', '194', '196', '198', '256'],
     formula=['{(x+frac(1,x))^2=x^2+2+frac(1,x^2)}；{(x^2+frac(1,x^2))^2=x^4+2+frac(1,x^4)}。'],
     steps=[f'① 方程兩邊除以 {{x}}：{{x+frac(1,x)}}＝{B}',
            f'② {{x^2+frac(1,x^2)=({B})^2-2}}＝{B}　③ {{x^4+frac(1,x^4)=({B})^2-2}}＝{B}'])

item(27, '若多項式 {g(x)} 除以 {x^2-2x-8}，餘式為 {2x+5}，求 {g(4)+g(-2)}。',
     ['4', '10', '13', '14', '18'],
     formula=['除法原理：{g(x)=}（除式）{⋅Q(x)+}（餘式）。代入除式的根，除式那一項變成 0，只剩餘式。'],
     steps=[f'① {{x^2-2x-8=(x-{B})(x+{B})}}，除式的根 {{x}}＝{B}、{B}',
            f'② {{g(4)=2×4+5}}＝{B}　③ {{g(-2)}}＝{B}　④ {{g(4)+g(-2)}}＝{B}'])

P.append(tail_stub())
build_docx(P, os.path.join(OUT, f'{BASE}_學生版.docx'), footer_text=FOOTER, media=MEDIA)

# ============================ 教師答案版 ============================
T = [masthead(SUBJECT, UNIT, '調適練習・教師答案版'),
     tight(para([('t', '本版供教師批改使用，不發給學生。題號＝原工作紙題號；原稿無參考答案，全部答案為獨立驗算所得。')], sz=22)),
     heading('一、單選題答案（1–20）')]

MC = dict(zip(range(1, 21), 'EDAACCBCEDBACABAADAB'))
mc_lines = ['　　'.join(f'{n}．{MC[n]}' for n in range(r, r + 10)) for r in (1, 11)]
T.append(box([tight(para([('t', x)])) for x in mc_lines], keep=False))

T.append(heading('二、單選題要點（對應框架各步）'))
KEY = [
    '1．{A}＝' + L('2,5') + '，{B}：{x<4}，{A∩B}＝' + L('2') + '，補集 ' + L('1,3,4,5,6') + '。',
    '2．{2a+b=7}，{-a+b=-2} → {a=3}，{b=1}，{a+b=4}。',
    '3．（題目已改為 {g(2025)}）{2025=6×337+3}，{g(2025)=g(3)=-4}。',
    '4．{(2x+y)(frac(1,x)+frac(2,y))=4+frac(4x,y)+frac(y,x)≥4+4=8}，{2x+y≥frac(8,3)}（{y=2x}，即 {x=frac(2,3)}，{y=frac(4,3)} 時取等號）。',
    '5．{7!-2×6!=3600}；{6!-2×5!=480}；{3600-480=3120}。',
    '6．{r^2=4}，{a_7+a_8=12×r^6=12×64=768}。',
    '7．穿針引線：零點 {-2}、1、2，由右上方起穿，曲線由左至右依次在下、上、下、上；取下方兩段，{x=±2} 實心取、{x=1} 空心不取 → ({-∞, -2}]{∪}({1, 2}]。',
    '8．{fn(log)_2 5=mn}；{fn(log)_15 24=frac(3+m,m+mn)}。',
    '9．{x} 的指數 {6-frac(3k,2)=0} → {k=4}，{C_6^4=15}。',
    '10．{fn(cos )α=-frac(4,5)}，{fn(tan )α=frac(3,4)}，{frac(1+frac(3,4),1-frac(3,4))=7}。',
    '11．{b_6=9}，三對各 18，和 54。　12．{4^3-3×1×4=52}。',
    '13．{a=5}，和 10，積 {≤25}（{P} 在短軸端點時取等號）。　14．{frac(1,2)×3×4×frac(sqrt(3),2)=3sqrt(3)}。',
    '15．和為 2、3、5、7、11 的格數：1＋2＋4＋6＋2＝15，{frac(15,36)=frac(5,12)}。',
    '16．{t+frac(1,t)=3}，平方＝5，取 {sqrt(5)}。　17．{T=frac(2π,2)=π}，最大值 {2+1=3}。',
    '18．頂點 {(1,1)}、{(4,1)}、{(1,4)}：{z=1}、7、{-2}，最大 7。',
    '19．{a=5}；偏差平方 9、1、1、9、0，和 20，{s^2=4}（按 {frac(1,n)} 定義；若用 {frac(1,n-1)} 得 5，不在選項中）。',
    '20．{-2≤x≤2} 且 {x≠1}。',
]
T.append(box([tight(para(x)) for x in KEY], keep=False))

T.append(heading('三、解答題（21–24）'))
ANS = [
    ['21．(a) {γ} 在第二象限，{fn(sin )γ=frac(12,13)}，{fn(tan )γ=-frac(12,5)}。',
     '　(b) {fn(cos )(γ-δ)=frac(56,65)}；{fn(cos )δ=(-frac(5,13))(frac(56,65))+(frac(12,13))(frac(33,65))=frac(116,845)}；',
     '　{fn(cos )2δ=2(frac(116,845))^2-1=-frac(687113,714025)}（約 {-0.9623}）。',
     '　★ 建議抽離生略過 (b)：數學無誤，但原題數字令答案極繁，考驗的是大數運算而非概念。'],
    ['22．(a) 兩次綠：{frac(3,5)×frac(2,4)=frac(3,10)}；至多一次綠：{1-frac(3,10)=frac(7,10)}。',
     '　(b) {P(X=0)=frac(2,5)×frac(1,4)=frac(1,10)}，{P(X=1)=frac(2,5)×frac(3,4)+frac(3,5)×frac(2,4)=frac(3,5)}，{P(X=2)=frac(3,10)}；',
     '　{E(X)=0+frac(3,5)+frac(6,10)=frac(6,5)}。'],
    ['23．(a) {a_1=5}；{n≥2}：{a_n=6n-1}，{n=1} 亦符合 → {a_n=6n-1}。{q^2=9}，{q=3}，{b_n=4⋅3^{n-1}}。',
     '　(b) {b_n} 前 {n} 項和 {=2(3^n-1)}，{T_n=3n^2+2n-2⋅3^n+2}。',
     '　{T_1=1}，{T_2=0}，{T_3=-19}，{T_4=-104}；{n≥3} 時 {T_n<0}（{3^n} 的增長快於 {3n^2+2n}；嚴格證明可用數學歸納法）。',
     '　★ 建議抽離生略過 (b)：「對足夠大 n 成立」的證明超出抽離生目標；(a) 已涵蓋 {S_n→a_n} 與等比通項兩個核心技能。'],
    ['24．（題目已改：點 {(4, frac(12,5))}）(a) {m=5k}，{c=3k}，{n=4k}；代入得 {frac(16,25k^2)+frac(9,25k^2)=frac(1,k^2)=1}，{k=1}；',
     '　{C}：{frac(x^2,25)+frac(y^2,16)=1}。',
     '　(b) {16x^2+25(x+2)^2=400} → {41x^2+100x-300=0}；{Δ=10000+49200=59200}，{sqrt(Δ)=40sqrt(37)}；',
     '　{|x_1-x_2|=frac(40sqrt(37),41)}，{|MN|=sqrt(2)×frac(40sqrt(37),41)=frac(40sqrt(74),41)}（約 8.39）。'],
]
for blk in ANS:
    T.append(box([tight(para(x)) for x in blk], keep=False))

T.append(heading('四、補充題（25–27，相似題）'))
T.append(box([tight(para(x)) for x in [
    '25．B　{A}：{(x-4)(x+2)≤0} → {-2≤x≤4}；{B}：{x≥-frac(a,2)}；{-frac(a,2)=1} → {a=-2}。（仿 2024 四校聯考選擇第 1 題）',
    '26．B　{x+frac(1,x)=4}，{x^2+frac(1,x^2)=14}，{x^4+frac(1,x^4)=196-2=194}。（仿 2024 選擇第 14 題）',
    '27．D　{x^2-2x-8=(x-4)(x+2)}；{g(4)=13}，{g(-2)=1}，和 14。（仿 2023 選擇第 2 題，問法改為兩值相加）',
]], keep=False))

T.append(heading('五、調適說明'))
for t_ in [
    '1．原稿兩處筆誤已改正（學生版直接印改正後的數字）：'
    '第 3 題 {g(2027)} → {g(2025)}（{2027=6×337+5}，只能化到 {g(5)}，題目未給，原題無解）；'
    '第 24 題點 {(4, frac(16,5))} → {(4, frac(12,5))}（配 {e=frac(3,5)}，原點代入得 {m^2=32}，與「標準方程」題意不符）。',
    '2．其餘題目照錄原稿；原稿第 18、20 題的短橫「‑」按數學減號排版，數值不變。',
    '3．每題題下加灰底「公式」（D7 提示卡）與「框架」（D2 步驟填空）；第 7 題按教師教法用穿針引線法（附空白數線）；第 15、18、19、22 題加表格／坐標格／樹狀圖框架；'
    '解答題 21–24 用左欄分區（已知／列式／計算／答，D9 作答分區）＋步驟填空骨架。',
    '4．21(b)、23(b) 題目照印，建議抽離生略過（理由見上）；如要保留，可只要求完成框架的第 ① 步。',
    '5．本份沒有對應的測驗卷，不做高相似題標記。',
    '6．可選題（使用者指定，原位標記【可選題】，不搬位）：第 1、2、4、12、13、14、17、21 題，及 23(b)、24(b)。',
    '7．第 25–27 題為補充相似題（仿四校聯考 2024 選擇 1、14 題及 2023 選擇 2 題，數字全改），放在卷末，不影響原題號。',
]:
    T.append(tight(para(t_, sz=22)))

build_docx(T, os.path.join(OUT, f'{BASE}_教師答案版.docx'), footer_text=FOOTER)
print('OK', BASE)
