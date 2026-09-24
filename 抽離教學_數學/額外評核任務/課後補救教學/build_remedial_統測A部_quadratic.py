# -*- coding: utf-8 -*-
r"""
build_remedial_統測A部_quadratic.py — 初三數學補救班 課後補救教學（統測舊卷 A 部）

來源：使用者提供的原卷 `24-25_初三甲_第一學段_數學科_統測_原卷.docx`
（2024/2025 學年第一學段統測，A 部 80 分＋B 部 40 分）。使用者 2026-09-24 指示：
**只要 A 部（第 1–16 題），不要 B 部**。

課後補救教學＝題目由使用者自己搵，我只重整＋套 house-style：題目數字與設問一字不改，
全部數學式以原生 OMML 重打（鐵律 1）；第 16 題附圖以 matplotlib 重畫（黑白）。

沿用 2026-09-16 補救班那份的使用者裁決（build_remedial_20260916_quadratic.py）：
- 學生卷＋教師卷；帶回家做、下一節訂正 → 每題加「改正」欄
- 不用教學設計（純題目卷）、不用 ★ 標籤（全班同卷、每題有分值）
- 題序比照 09-16 那份按概念梯級重整（使用者 2026-09-24「其他規則按這裏要求」）：
  概念與一般式 → 根的意義 → 直接開平方 → 因式分解 → 公式法 → 判別式 →
  根與係數的關係 → 應用題，共八大題 18 題；新舊題號對照見驗算紀錄。
- 分值：原卷已有每題分值，照搬不另定（09-16 那份原稿無分值才要自定），滿分 80。

刪去原卷的「請在答題卡上作答」「不可使用計算機」注意事項（補救作業直接寫在卷上）。
"""
import sys, os, re

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _run, _tbl, _PAGE_CONTENT_WIDTH
from omml_core import MediaRegistry

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學（補救班）'
UNIT = '一元二次方程・第一學段統測 A 部'
BASE = '課後補救教學_初三數學補救班_統測A部_一元二次方程'
FOOT = '初三數學補救班．課後補救教學（統測 A 部）'
W = _PAGE_CONTENT_WIDTH
FIG = os.path.join(OUT, '_tmp_fig_q16.png')

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


def save(P, name, footer, media=None):
    P = [x if hasattr(x, 'png_path') else tighten(x) for x in P]
    build_docx(P, os.path.join(OUT, name), footer_text=footer, media=media)


def draw_fig():
    """第 16 題：30 m × 20 m 矩形，一橫一縱兩條同寬道路（陰影）。照原圖比例重畫。"""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    plt.rcParams['font.family'] = ['Microsoft JhengHei', 'Calibri']
    fig, ax = plt.subplots(figsize=(3.6, 2.7), dpi=220)
    ax.add_patch(Rectangle((0, 0), 30, 20, fill=False, lw=1.4, ec='black'))
    ax.add_patch(Rectangle((0, 8.5), 30, 3, fc='#555555', ec='none'))     # 橫向道路
    ax.add_patch(Rectangle((19, 0), 3, 20, fc='#555555', ec='none'))      # 縱向道路
    ax.add_patch(Rectangle((0, 0), 30, 20, fill=False, lw=1.4, ec='black'))
    # 尺寸線
    ax.annotate('', xy=(0, 22), xytext=(30, 22),
                arrowprops=dict(arrowstyle='<->', lw=0.9))
    ax.text(15, 22.6, '30 m', ha='center', va='bottom', fontsize=11)
    ax.annotate('', xy=(-2, 0), xytext=(-2, 20),
                arrowprops=dict(arrowstyle='<->', lw=0.9))
    ax.text(-2.6, 10, '20 m', ha='right', va='center', fontsize=11)
    ax.set_xlim(-9, 31)
    ax.set_ylim(-1, 25.5)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.savefig(FIG, bbox_inches='tight', pad_inches=0.04)
    plt.close(fig)


def ruled(label='', sz=22, row_sz=28):
    ppr = ('<w:pPr><w:spacing w:line="320" w:lineRule="auto" w:before="70" w:after="0"/>'
           f'<w:pBdr><w:bottom w:val="single" w:sz="5" w:space="4" w:color="{LINE_GREY}"/>'
           '</w:pBdr></w:pPr>')
    run = _run(label + ' ', sz=sz) if label else ''
    pad = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
           '<w:t xml:space="preserve"> </w:t></w:r>')
    return f'<w:p>{ppr}{run}{pad}</w:p>'


def work_lines(n):
    """逐行交替框線設定，免 Word 合併相鄰同框線段落（記憶 docx_adjacent_border_paras_merge）。"""
    out = []
    for i in range(n):
        ppr = ('<w:pPr><w:pBdr>'
               f'<w:bottom w:val="single" w:sz="5" w:space="{4 + i % 2}" w:color="{LINE_GREY}"/>'
               '</w:pBdr><w:spacing w:line="360" w:lineRule="auto" w:before="80" w:after="0"/>'
               f'<w:ind w:right="{i % 2}"/></w:pPr>')
        run = ('<w:r><w:rPr><w:sz w:val="30"/><w:szCs w:val="30"/></w:rPr>'
               '<w:t xml:space="preserve"> </w:t></w:r>')
        out.append(f'<w:p>{ppr}{run}</w:p>')
    return out


def note(text):
    return para(text, keep_next=True)


def qhead(text):
    return para(text, keep_next=True)


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


def fillbox(stem, last=False):
    return problem_box([qhead(stem), ruled('改正：')], trailing_blank=not last)


def solvebox(stems, lines_each, fix_lines=2, last=False):
    body = []
    for p, n in zip(stems, lines_each):
        body.append(qhead(p))
        body += work_lines(n)
    body += [ruled('改正：')] + [ruled() for _ in range(fix_lines - 1)]
    return problem_box(body, trailing_blank=not last)


# ================================ 學生卷 ================================
def student():
    media = MediaRegistry()
    P = [masthead(SUBJECT, UNIT, '課後補救教學'), student_info_row()]
    P.append(para('帶回家完成　　共八大題（18 題）　　滿分 80 分　　'
                  '得分：＿＿＿＿ / 80', bold=True))
    P.append(para('第 7、8、10、16、18 題須寫出計算過程。老師批改後，請在每題的「改正」欄'
                  '完成訂正，下一節帶回。'))

    P.append(heading('一、一元二次方程的概念與一般式（12 分）'))
    P.append(note('每題 3 分。'))
    P.append(mcbox('1．下列方程中，關於 {x} 的一元二次方程是（　　　）',
                   ['{ax^2-2x-3=0}', '{x^2-2x=x^2}', '{x^2=3}', '{x^2+1/x=1}'],
                   per_line=2))
    P.append(mcbox('2．一元二次方程 {x^2-2x-2021=0} 的二次項係數、一次項係數、常數項'
                   '分別為（　　　）',
                   ['0，−2，−2021', '1，−2，2021', '1，−2，−2021', '0，−2，2021'],
                   per_line=2))
    P.append(mcbox('3．把一元二次方程 {2x^2-3=5x} 化為一般形式得（　　　）',
                   ['{2x^2=5x+3}', '{2x^2-5x-3=0}', '{2x^2+5x-3=0}', '{2x^2-5x=3}'],
                   per_line=2))
    P.append(fillbox('4．用公式法解一元二次方程 {x(x-4)=2-8x} 時，應先將其化成'
                     '「一般形式」為＿＿＿＿＿＿＿＿＿＿＿＿。'))

    P.append(heading('二、根的意義（3 分）'))
    P.append(fillbox('5．關於 {x} 的方程 {x^2-6x+k=0} 的一個根是 2，'
                     '則 {k} 的值是＿＿＿＿＿＿＿＿。'))

    P.append(heading('三、直接開平方法（6 分）'))
    P.append(note('每題 3 分。有兩個根的，兩支要分開寫、中間寫「或」，最後用「∴」寫答句。'))
    P.append(fillbox('6．已知一元二次方程 {(x-2)^2=3} 的兩根為 {a}、{b}，且 {a>b}，'
                     '則 {ab=}＿＿＿＿＿＿＿＿。'))
    P.append(solvebox(['7．解方程：{(6x-1)^2=25}'], [6], fix_lines=1))

    P.append(heading('四、因式分解法（9 分）'))
    P.append(note('第 (1) 小題 4 分，第 (2) 小題 5 分。'))
    P.append(solvebox(['8．解方程：', '(1) {6x(5x+2)=7(5x+2)}', '(2) {x^2-2x-35=0}'],
                      [0, 6, 6]))

    P.append(heading('五、公式法（12 分）'))
    P.append(note('第 9 題 3 分；第 10 題 (1) 4 分、(2) 5 分。'))
    P.append(mcbox('9．已知某一元二次方程的兩根為 {x=frac(-5±sqrt(5^2+4×3×1),2×3)}，'
                   '則此方程可能是（　　　）',
                   ['{3x^2+5x+1=0}', '{3x^2-5x+1=0}', '{3x^2-5x-1=0}', '{3x^2+5x-1=0}'],
                   per_line=2))
    P.append(solvebox(['10．解方程：', '(1) {3x^2+5(2x+1)=0}', '(2) {4x^2-8x-1=0}'],
                      [0, 6, 6], fix_lines=1))

    P.append(heading('六、判別式（6 分）'))
    P.append(note('每題 3 分。'))
    P.append(mcbox('11．一元二次方程 {x^2-6x+9=0} 的根的情況為（　　　）',
                   ['有兩個相等的實數根', '有兩個不相等的實數根', '有一個實數根', '無實數根'],
                   per_line=2))
    P.append(fillbox('12．方程 {x^2-2x=0} 的判別式 Δ＝＿＿＿＿＿＿＿＿。（用數值表示答案）'))

    P.append(heading('七、根與係數的關係（21 分）'))
    P.append(note('第 13–15 題每題 3 分；第 16 題 12 分，須寫出計算過程。'))
    P.append(mcbox('13．方程 {x^2+4x-3=0} 的兩個根是 {x_1} 和 {x_2}，'
                   '則 {x_1+x_2} 的值等於（　　　）', ['4', '−4', '−3', '3']))
    P.append(mcbox('14．一元二次方程 {x^2-2x+1=0} 的兩根分別為 {x_1} 和 {x_2}，'
                   '則 {x_1x_2} 為（　　　）', ['−2', '1', '2', '0']))
    P.append(mcbox('15．已知關於 {x} 的一元二次方程 {x^2-mx-3=0} 的一個根為 3，'
                   '則另一個根為（　　　）', ['1', '−1', '2', '−6']))
    P.append(solvebox(['16．設 {x_1}、{x_2} 是方程 {2x^2+5x-7=0} 的兩個根，'
                       '不解方程，求下列式子的值。',
                       '(1) {x_1+x_2}　（2 分）', '(2) {x_1x_2}　（2 分）',
                       '(3) {x_1^2+x_2^2}　（4 分）', '(4) {x_2/x_1+x_1/x_2}　（4 分）'],
                      [0, 2, 2, 4, 4]))

    P.append(heading('八、應用題（11 分）'))
    P.append(note('第 17 題 3 分，第 18 題 8 分。'))
    P.append(fillbox('17．生物興趣小組的學生，將自己收集的標本向本組其他成員各贈送一件，'
                     '全組共互贈了 132 件。如果全組共有 {x} 名同學，根據題意列出的方程是'
                     '＿＿＿＿＿＿＿＿＿＿＿＿。'))
    main = [qhead('18．如圖，在寬為 20 m、長為 30 m 的矩形地面上修築同樣寬的道路'
                  '（圖中陰影部分），餘下的部分種上草坪。要使草坪的面積為 551 m²，'
                  '求道路的寬。')] + work_lines(9) + [ruled('改正：'), ruled()]
    aside = [para('', spacing=False), image_para(FIG, width_cm=6.4)]
    P.append(aside_layout(main, aside, main_pct=0.62, media=media, boxed=True))
    save(P, BASE + '_學生卷.docx', FOOT, media=media)


# ================================ 教師卷 ================================
def ans_tbl(rows, headers=('題', '答案', '解析與評分')):
    w = [int(W * 0.07), int(W * 0.14)]
    w.append(W - sum(w))
    out = [{'cells': [{'p': [para(h, bold=True, sz=22, spacing=False)], 'shd': GREY_FILL}
                      for h in headers], 'hdr': True}]
    for n, a, why in rows:
        out.append([{'p': [para(n, sz=22, spacing=False)], 'va': 'center'},
                    {'p': [para(a, bold=True, sz=22, spacing=False)], 'va': 'center'},
                    {'p': [para(why, sz=22, spacing=False)], 'va': 'center'}])
    return _tbl(out, w)


LONG = (0.380, 0.050, 0.130, 0.060, 0.160, 0.050)   # 左式是展開式／因式分解式時用


def keep_rows_together(xml):
    """表格除最後一列外，每段加 keepNext——Word 就不會把表頭列孤零零留在頁尾。"""
    rows = xml.split('</w:tr>')
    for i in range(len(rows) - 2):
        rows[i] = rows[i].replace('<w:pPr>', '<w:pPr><w:keepNext/>')
    return '</w:tr>'.join(rows)


def wtbl(rows, why_pct=0.36, col_frac=None):
    return keep_rows_together(worked_example_table(
        rows, headers=('算式', '說明與建議評分'), why_pct=why_pct, col_frac=col_frac))


def sub_title(text):
    return para(text, bold=True, keep_next=True)


def teacher():
    P = [masthead(SUBJECT, UNIT, '課後補救教學・教師卷')]
    P.append(para('本卷供教師批改使用，不發給學生。題目、數字、分值與學生卷完全相同，'
                  '滿分 80 分；各題分值沿用原統測卷 A 部。原卷未附評分準則，'
                  '解答題內的【分】為建議分配。'))
    P.append(para('本任務為帶回家作業、下一節訂正；學生卷每題設有「改正」欄，'
                  '批改後請學生在原卷訂正，不必另抄。新舊題號對照見同資料夾驗算紀錄。'))

    P.append(heading('一、一元二次方程的概念與一般式（12 分）'))
    P.append(ans_tbl([
        ('1', 'C', 'A 的 a 可能為 0；B 化簡後是 −2x = 0（一次）；D 分母含 x（分式方程）'),
        ('2', 'C', 'a = 1，b = −2，c = −2021（係數連正負號一起讀）。'
                   '※ 易錯：選 B（漏了常數項的負號）'),
        ('3', 'B', '移項：2x² − 5x − 3 = 0。A、D 未把所有項移到一邊；C 移項忘了變號'),
        ('4', 'x² + 4x − 2 = 0', '展開：x² − 4x = 2 − 8x，全部移到左邊：x² + 4x − 2 = 0'),
    ]))

    P.append(heading('二、根的意義（3 分）'))
    P.append(ans_tbl([('5', 'k = 8', '代入 x = 2：4 − 12 + k = 0，k = 8')]))

    P.append(heading('三、直接開平方法（6 分）'))
    P.append(ans_tbl([('6', 'ab = 1', 'x − 2 = ±√3，a = 2 + √3，b = 2 − √3；ab = 4 − 3 = 1')]))
    P.append(para('解方程題評分要點：兩支分開寫、中間寫「或」，兩個根各 1 分；'
                  '末行有「∴」答句才算完整作答。', keep_next=True))
    P.append(sub_title('7．{(6x-1)^2=25}（3 分）'))
    P.append(wtbl([
        eq_row('{(6x-1)^2}', '{25}', '原方程'),
        or_row('{6x-1}', '{5}', '{6x-1}', '{-5}', '開平方分兩支　【1 分】'),
        or_row('{x_1}', '{1}', '{x_2}', '{-2/3}', '兩根各 1 分　【2 分】'),
        answer_row('{x_1=1} 或 {x_2=-2/3}'),
    ], why_pct=0.30, col_frac=LONG))

    P.append(heading('四、因式分解法（9 分）'))
    P.append(sub_title('8 (1)　{6x(5x+2)=7(5x+2)}（4 分）'))
    P.append(wtbl([
        eq_row('{6x(5x+2)-7(5x+2)}', '{0}', ['移到左邊　【1 分】',
                                             '※ 不可兩邊同除以 (5x + 2)，會漏根']),
        eq_row('{(5x+2)(6x-7)}', '{0}', '提取公因式 (5x + 2)　【1 分】'),
        or_row('{5x+2}', '{0}', '{6x-7}', '{0}', '令兩個因式各自為 0'),
        or_row('{x_1}', '{-2/5}', '{x_2}', '{7/6}', '兩根各 1 分　【2 分】'),
        answer_row('{x_1=-2/5} 或 {x_2=7/6}'),
    ], why_pct=0.30, col_frac=LONG))
    P.append(sub_title('8 (2)　{x^2-2x-35=0}（5 分）'))
    P.append(wtbl([
        eq_row('{x^2-2x-35}', '{0}', '原方程'),
        eq_row('{(x-7)(x+5)}', '{0}', '十字相乘：兩數積 −35、和 −2　【2 分】'),
        or_row('{x-7}', '{0}', '{x+5}', '{0}', '令兩個因式各自為 0　【1 分】'),
        or_row('{x_1}', '{7}', '{x_2}', '{-5}', '兩根各 1 分　【2 分】'),
        answer_row('{x_1=7} 或 {x_2=-5}'),
    ], why_pct=0.30, col_frac=LONG))

    P.append(heading('五、公式法（12 分）'))
    P.append(ans_tbl([('9', 'D', '對照求根公式：a = 3，b = 5，b² − 4ac = 5² + 4×3×1，'
                                 '得 −4ac = 12，c = −1')]))
    P.append(sub_title('10 (1)　{3x^2+5(2x+1)=0}（4 分）'))
    P.append(wtbl([
        eq_row('{3x^2+10x+5}', '{0}', '展開，化成一般式　【1 分】'),
        span_row('{a=3}，{b=10}，{c=5}', '讀係數'),
        eq_row('{Δ}', '{10^2-4(3)(5)=40}', 'Δ > 0，有兩個不相等的實數根　【1 分】'),
        eq_row('{x}', '{frac(-10±sqrt(40),2×3)=frac(-10±2sqrt(10),6)}',
               '代入求根公式；√40 = 2√10'),
        or_row('{x_1}', '{frac(-5+sqrt(10),3)}', '{x_2}', '{frac(-5-sqrt(10),3)}',
               '約分，兩根各 1 分　【2 分】'),
        answer_row('{x_1=frac(-5+sqrt(10),3)} 或 {x_2=frac(-5-sqrt(10),3)}'),
    ], col_frac=(0.300, 0.050, 0.240, 0.060, 0.130, 0.050)))
    P.append(sub_title('10 (2)　{4x^2-8x-1=0}（5 分）'))
    P.append(wtbl([
        span_row('{a=4}，{b=-8}，{c=-1}', '讀係數　※ 常數項連負號一起讀　【1 分】'),
        eq_row('{Δ}', '{(-8)^2-4(4)(-1)=64+16=80}', '負負得正　【1 分】'),
        eq_row('{x}', '{frac(8±sqrt(80),2×4)=frac(8±4sqrt(5),8)}',
               '代入求根公式；√80 = 4√5　【1 分】'),
        or_row('{x_1}', '{frac(2+sqrt(5),2)}', '{x_2}', '{frac(2-sqrt(5),2)}',
               '約分，兩根各 1 分　【2 分】'),
        answer_row('{x_1=frac(2+sqrt(5),2)} 或 {x_2=frac(2-sqrt(5),2)}'),
    ]))

    P.append(heading('六、判別式（6 分）'))
    P.append(ans_tbl([
        ('11', 'A', 'Δ = (−6)² − 4(1)(9) = 36 − 36 = 0'),
        ('12', 'Δ = 4', 'a = 1，b = −2，c = 0；Δ = (−2)² − 4(1)(0) = 4。'
                        '※ 易錯：c = 0 不是「沒有 c」'),
    ]))

    P.append(heading('七、根與係數的關係（21 分）'))
    P.append(ans_tbl([
        ('13', 'B', 'x₁ + x₂ = −b/a = −4/1 = −4。※ 易錯：選 A（忘記負號）'),
        ('14', 'B', 'x₁x₂ = c/a = 1/1 = 1（亦可：(x − 1)² = 0，兩根都是 1）'),
        ('15', 'B', '兩根之積 = c/a = −3，另一根 = −3 ÷ 3 = −1。'
                    '檢查：代 x = 3 得 m = 2，x² − 2x − 3 = (x − 3)(x + 1) ✓'),
    ]))
    P.append(sub_title('16．{2x^2+5x-7=0}（12 分）'))
    P.append(wtbl([
        span_row('{a=2}，{b=5}，{c=-7}', '讀係數'),
        eq_row('(1)　{x_1+x_2}', '{-b/a=-5/2}', '【2 分】'),
        eq_row('(2)　{x_1x_2}', '{c/a=-7/2}', '【2 分】'),
        eq_row('(3)　{x_1^2+x_2^2}', '{(x_1+x_2)^2-2x_1x_2}', '配成和與積的式子　【2 分】'),
        eq_row('', '{(-5/2)^2-2(-7/2)=25/4+7=53/4}', '代入　【2 分】'),
        eq_row('(4)　{x_2/x_1+x_1/x_2}', '{frac(x_1^2+x_2^2,x_1x_2)}', '通分　【2 分】'),
        eq_row('', '{frac(53/4,-7/2)=-53/14}', '用 (3)、(2) 的結果　【2 分】'),
        span_row('檢查：{2x^2+5x-7=(2x+7)(x-1)}，兩根為 1 與 {-7/2}，代回四式皆符合',
                 '教師自行核對用，不要求學生寫'),
    ], why_pct=0.30, col_frac=(0.340, 0.050, 0.280, 0.070, 0.125, 0.055)))

    P.append(heading('八、應用題（11 分）'))
    P.append(ans_tbl([('17', 'x(x − 1) = 132', '每人送給其他 x − 1 人各一件，共 x(x − 1) 件')]))
    P.append(sub_title('18．道路的寬（8 分）'))
    P.append(para('設道路的寬為 {x} m。把兩條道路分別平移到矩形的邊上，'
                  '草坪合成一個長 {(30-x)} m、寬 {(20-x)} m 的矩形。', keep_next=True))
    P.append(wtbl([
        eq_row('{(30-x)(20-x)}', '{551}', '列方程　【3 分】'),
        eq_row('{600-50x+x^2}', '{551}', '展開'),
        eq_row('{x^2-50x+49}', '{0}', '化成一般式　【1 分】'),
        eq_row('{(x-1)(x-49)}', '{0}', '因式分解　【1 分】'),
        or_row('{x_1}', '{1}', '{x_2}', '{49}', '【1 分】'),
        span_row('{x=49>20}，道路比地面還寬，不合題意，捨去', '檢驗取捨　【1 分】'),
        answer_row('道路的寬為 1 m', '答句　【1 分】'),
    ], why_pct=0.30, col_frac=LONG))
    save(P, BASE + '_教師卷.docx', FOOT + '（教師卷）')


if __name__ == '__main__':
    draw_fig()
    student()
    teacher()
    print('OK')
