# -*- coding: utf-8 -*-
r"""
build_extra_20260916_quadratic.py — 初三數學補救班 額外評核任務（2026-09-16）

來源：使用者提供的原卷 `2026年9月16日初中数学作业.docx`（人教版題庫格式、簡體、
12 題、數學式全部是 MathType OLE 物件＋PNG）。本腳本**只重整順序與版面**，題目
數字與設問一字不改；全部數學式重新以原生 OMML 打出（鐵律 1），簡體轉繁體 zh-TW。

使用者當次裁決（2026-09-16，AskUserQuestion 四項）：
- 版本＝學生卷＋教師卷（單一版本，不出輔助版）
- 用途＝帶回家做、下一節訂正 → 作答空間放闊、每題加「改正」欄
- 教學設計＝不用（無手順卡／提示卡／核對清單，純題目卷）
- 配分＝按題型定，滿分 50

重整依據（概念 → 結構 → 根的意義 → 配方鋪墊 → 解法 → 判別式 → 綜合），對應
補救班 IEP 短期目標 1-1～1-3（直接開平方法／因式分解法／判別式）：
  一 原①｜二 原④→原②｜三 原③→原⑧｜四 原⑦→原⑤
  五 原⑩→原⑪｜六 原⑥→原⑨｜七 原⑫
原④排在原②之前（讀係數比化一般式少一步）；原⑦排在原⑤之前（補常數是配方第一步）。

配分：一 3｜二 6｜三 7｜四 6｜五 16｜六 7｜七 5 ＝ 50

house-style 偏離說明（評核卷文類，刻意）：
1. 不用 ★ 三層難度標籤——全班同卷、每題有分值，沒有分層概念。
2. masthead 類型寫「課後補救教學」；檔案室要跟「抽離課堂檢測」「額外評核」分開。
3. 每題框內多一條「改正：」欄——帶回家做、下一節訂正，訂正要留在同一張紙上
   （對應補救班 IEP 短期目標「能在錯題本記錄錯誤成因，並在下一節前完成訂正」）。
"""
import sys, os, re

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _run, _tbl, _PAGE_CONTENT_WIDTH

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學（補救班）'
UNIT = '一元二次方程・概念與三種解法'
BASE = '課後補救教學_初三數學補救班_20260916_一元二次方程'
W = _PAGE_CONTENT_WIDTH

_PPR = re.compile(r'<w:pPr>((?:(?!</w:pPr>).)*?)</w:pPr>', re.S)


def tighten(xml):
    """para(spacing=False) 並不是零行距：它不寫 <w:spacing>，於是繼承 Word Normal
    的段後 8pt（記憶 docx_spacing_false_is_not_zero）。這裡補上零段距。"""
    def fix(m):
        inner = m.group(1)
        if '<w:spacing' in inner or '<w:jc ' not in inner or '<w:ind' in inner:
            return m.group(0)
        inner = inner.replace('<w:jc ', '<w:spacing w:before="0" w:after="0" w:line="276" '
                                        'w:lineRule="auto"/><w:jc ', 1)
        return f'<w:pPr>{inner}</w:pPr>'
    return _PPR.sub(fix, xml)


def save(P, name, footer):
    build_docx([tighten(x) for x in P], os.path.join(OUT, name), footer_text=footer)


def ruled(label='', sz=22, row_sz=28):
    """一條書寫線，標籤直接寫在線上（不另起一段，免吃 Word Normal 的段後 8pt）。"""
    ppr = ('<w:pPr><w:spacing w:line="320" w:lineRule="auto" w:before="70" w:after="0"/>'
           f'<w:pBdr><w:bottom w:val="single" w:sz="5" w:space="4" w:color="{LINE_GREY}"/>'
           '</w:pBdr></w:pPr>')
    run = _run(label + ' ', sz=sz) if label else ''
    pad = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
           '<w:t xml:space="preserve"> </w:t></w:r>')
    return f'<w:p>{ppr}{run}{pad}</w:p>'


def work_lines(n):
    """列式作答的橫線。不用 write_lines()：它產生的 n 段框線設定完全相同，Word 會把
    相鄰同框線段落併成一組、只畫最後一條（記憶 docx_adjacent_border_paras_merge）。
    逐行交替 w:space 與 1 twip 右縮排，令相鄰兩段的框線設定不同。"""
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
    """大題標題下的說明／配分段。keep_next 令它跟著標題與下一個題目框走——
    否則 Word 會把「標題＋說明」孤零零留在頁尾（記憶 fix_heading_keepnext_pagination）。"""
    return para(text, keep_next=True)


def qhead(text):
    """題幹；keep_next 令題幹不會與下面的作答區被分頁拆開。"""
    return para(text, keep_next=True)


def opts(items, per_line=4):
    """選項段：每行 per_line 個，用全形空白拉開。"""
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
    P = [masthead(SUBJECT, UNIT, '課後補救教學'), student_info_row()]
    P.append(para('帶回家完成　　共七大題（12 小題）　　滿分 50 分　　'
                  '得分：＿＿＿＿ / 50', bold=True))
    P.append(para('第五、七大題須寫出計算過程。老師批改後，請在每題的「改正」欄完成訂正，'
                  '下一節帶回。'))

    P.append(heading('一、判別一元二次方程（3 分）'))
    P.append(mcbox('1．下列方程中，是關於 {x} 的一元二次方程的是（　　　）',
                   ['{x^2+5x-1=0}', '{1/x^2=1}', '{y^2+2x=1}', '{2x+b=0}']))

    P.append(heading('二、一般式、項與係數（6 分）'))
    P.append(note('每題 3 分。'))
    P.append(mcbox('2．一元二次方程 {x^2-6x-2=0} 的二次項係數、一次項係數和常數項'
                   '分別是（　　　）',
                   ['1，6，2', '1，−6，−2', '0，−6，−2', '1，−6，2']))
    P.append(mcbox('3．將方程 {4x^2+x=5} 化為一般形式後，{a}、{b}、{c} 的值'
                   '分別是（　　　）',
                   ['{a=4}，{b=1}，{c=5}', '{a=1}，{b=4}，{c=5}',
                    '{a=4}，{b=1}，{c=-5}', '{a=4}，{b=-5}，{c=1}'], per_line=2))

    P.append(heading('三、根的意義（7 分）'))
    P.append(note('第 4 題 3 分，第 5 題 4 分。'))
    P.append(mcbox('4．已知方程 {x^2+kx-6=0} 的一個根是 2，則 {k} 的值為（　　　）',
                   ['2', '1', '3', '−3']))
    P.append(fillbox('5．一元二次方程 {x^2-x+m=0} 的一個解為 {x=2}，'
                     '則 {m} 的值為＿＿＿＿＿＿＿＿。'))

    P.append(heading('四、配方法的關鍵一步（6 分）'))
    P.append(note('每題 3 分。'))
    P.append(mcbox('6．用配方法解方程 {x^2+6x=1} 時，要使等號左邊變成一個完全平方式，'
                   '等號兩邊應同時加上（　　　）', ['12', '9', '6', '3']))
    P.append(mcbox('7．用配方法解一元二次方程 {x^2-4x=-1}，變形後的結果'
                   '正確的是（　　　）',
                   ['{(x+2)^2=3}', '{(x-2)^2=3}', '{(x+2)^2=5}', '{(x-2)^2=5}'],
                   last=True))

    P.append(heading('五、解一元二次方程（16 分）', page_break_before=True))
    P.append(note('每小題 4 分，須寫出計算過程。有兩個根的，兩支要分開寫、中間寫「或」，'
                  '最後用「∴」寫答句。'))
    P.append(solvebox(['8．解方程：', '(1) {x^2-4x=0}', '(2) {x^2-4x-5=0}'],
                      [0, 6, 6]))
    P.append(solvebox(['9．解方程：', '(1) {x^2-2x=5}', '(2) {2x^2-x=2-4x}'],
                      [0, 7, 7]))

    P.append(heading('六、判別式（7 分）'))
    P.append(note('第 10 題 3 分，第 11 題 4 分。'))
    P.append(mcbox('10．一元二次方程 {x^2-4x+2=0} 的根的判別式的值為（　　　）',
                   ['−12', '12', '−8', '8']))
    P.append(fillbox('11．關於 {x} 的一元二次方程 {2x^2+x-k=0} 有兩個相等的實數根，'
                     '則 {k} 的值為＿＿＿＿＿＿＿＿。'))

    P.append(heading('七、綜合題（5 分）'))
    P.append(note('第 (1) 小題 3 分，第 (2) 小題 2 分。'))
    P.append(solvebox(['12．已知關於 {x} 的一元二次方程 {x^2-(m+2)x+2m=0}。',
                       '(1) 求證：不論 {m} 為何值，該方程總有兩個實數根。',
                       '(2) 若方程的一個根是 1，求 {m} 的值及方程的另一個根。'],
                      [0, 5, 6], last=True))
    save(P, BASE + '_學生卷.docx', '初三數學補救班．課後補救教學 2026-09-16')


# ================================ 教師卷 ================================
def ans_tbl(rows, headers=('題', '答案', '解析與評分')):
    w = [int(W * 0.07), int(W * 0.10)]
    w.append(W - sum(w))
    out = [{'cells': [{'p': [para(h, bold=True, sz=22, spacing=False)], 'shd': GREY_FILL}
                      for h in headers], 'hdr': True}]
    for n, a, why in rows:
        out.append([{'p': [para(n, sz=22, spacing=False)], 'va': 'center'},
                    {'p': [para(a, bold=True, sz=22, spacing=False)], 'va': 'center'},
                    {'p': [para(why, sz=22, spacing=False)], 'va': 'center'}])
    return _tbl(out, w)


def wtbl(rows, why_pct=0.34, col_frac=None):
    return worked_example_table(rows, headers=('算式', '說明與評分'),
                                why_pct=why_pct, col_frac=col_frac)


def teacher():
    P = [masthead(SUBJECT, UNIT, '課後補救教學・教師卷')]
    P.append(para('本卷供教師批改使用，不發給學生。題目、數字、分值與學生卷完全相同，'
                  '滿分 50 分。'))
    P.append(para('本任務為帶回家作業、下一節訂正；學生卷每題設有「改正」欄，'
                  '批改後請學生在原卷訂正，不必另抄。'))

    P.append(heading('一、判別一元二次方程（3 分）'))
    P.append(ans_tbl([('1', 'A', 'B 是分式方程（分母含 x）；C 含 x、y 兩個未知數；'
                                 'D 關於 x 是一元一次方程')]))

    P.append(heading('二、一般式、項與係數（6 分）'))
    P.append(ans_tbl([
        ('2', 'B', '係數要連正負號一起讀：1，−6，−2。※ 易錯：選 A（漏了負號）'),
        ('3', 'C', '先化一般式：4x² + x − 5 = 0，故 a = 4，b = 1，c = −5。'
                   '※ 易錯：選 A（5 移項過去忘了變號）'),
    ]))

    P.append(heading('三、根的意義（7 分）'))
    P.append(ans_tbl([('4', 'B', '把 x = 2 代入：4 + 2k − 6 = 0，得 2k = 2，k = 1')]))
    P.append(para('5．（4 分）把 {x=2} 代入求 {m}：', bold=True, keep_next=True))
    P.append(wtbl([
        span_row('{x^2-x+m=0}', '原方程'),
        eq_row('{(2)^2-(2)+m}', '{0}', '代入 {x=2}　【2 分】'),
        eq_row('{2+m}', '{0}', '先算 4 − 2 = 2'),
        eq_row('{m}', '{-2}', '移項　【2 分】'),
        answer_row('{m=-2}', '答句'),
    ], why_pct=0.34, col_frac=(0.480, 0.060, 0.200, 0.060, 0.100, 0.050)))

    P.append(heading('四、配方法的關鍵一步（6 分）'))
    P.append(ans_tbl([
        ('6', 'B', '一次項係數 6 的一半再平方：(6 ÷ 2)² = 9。'
                   '※ 易錯：選 D（只做了一半，忘記平方）'),
        ('7', 'B', 'x² − 4x + 4 = −1 + 4，即 (x − 2)² = 3。'
                   '※ 易錯：選 A（括號內取了一次項係數的相反號；應為 −4 的一半 −2）'),
    ]))

    P.append(heading('五、解一元二次方程（16 分）'))
    P.append(para('每小題 4 分。評分要點：兩支分開寫、中間寫「或」各 1 分，兩個根各 1 分；'
                  '末行有「∴」答句才算完整作答。'))

    P.append(para('8 (1) {x^2-4x=0}（4 分）', bold=True, keep_next=True))
    P.append(wtbl([
        eq_row('{x^2-4x}', '{0}', '原方程'),
        eq_row('{x(x-4)}', '{0}', ['提取公因式 x　【1 分】',
                                   '※ 不可兩邊同除以 x，會漏掉 x = 0 這個根']),
        or_row('{x}', '{0}', '{x-4}', '{0}', '令兩個因式各自為 0　【1 分】'),
        or_row('{x_1}', '{0}', '{x_2}', '{4}', '兩根各 1 分　【2 分】'),
        answer_row('{x_1=0} 或 {x_2=4}'),
    ], why_pct=0.36))

    P.append(para('8 (2) {x^2-4x-5=0}（4 分）', bold=True, keep_next=True))
    P.append(wtbl([
        eq_row('{x^2-4x-5}', '{0}', '原方程'),
        eq_row('{(x-5)(x+1)}', '{0}', '十字相乘：兩數積 −5、和 −4　【1 分】'),
        or_row('{x-5}', '{0}', '{x+1}', '{0}', '令兩個因式各自為 0　【1 分】'),
        or_row('{x_1}', '{5}', '{x_2}', '{-1}', '兩根各 1 分　【2 分】'),
        answer_row('{x_1=5} 或 {x_2=-1}'),
    ], why_pct=0.34, col_frac=(0.350, 0.050, 0.110, 0.055, 0.160, 0.050)))

    P.append(para('9 (1) {x^2-2x=5}（4 分，配方法）', bold=True, keep_next=True))
    P.append(wtbl([
        eq_row('{x^2-2x}', '{5}', '原方程'),
        eq_row('{x^2-2x+1}', '{5+1}', ['兩邊同加 1　【1 分】',
                                       '※ 一次項係數 −2 的一半是 −1，平方得 1']),
        eq_row('{(x-1)^2}', '{6}', ['左邊寫成完全平方　【1 分】', '※ 6 > 0，可以開平方']),
        or_row('{x-1}', '{sqrt(6)}', '{x-1}', '{-sqrt(6)}', '開平方分兩支'),
        or_row('{x_1}', '{1+sqrt(6)}', '{x_2}', '{1-sqrt(6)}', '兩根各 1 分　【2 分】'),
        answer_row('{x_1=1+sqrt(6)} 或 {x_2=1-sqrt(6)}'),
    ], why_pct=0.32, col_frac=(0.250, 0.055, 0.250, 0.070, 0.135, 0.055)))

    P.append(para('9 (2) {2x^2-x=2-4x}（4 分）', bold=True, keep_next=True))
    P.append(wtbl([
        eq_row('{2x^2-x}', '{2-4x}', '原方程'),
        eq_row('{2x^2-x+4x-2}', '{0}', '全部移到左邊　※ 移項要變號'),
        eq_row('{2x^2+3x-2}', '{0}', '合併同類項，化成一般式　【1 分】'),
        eq_row('{(2x-1)(x+2)}', '{0}', '因式分解　【1 分】'),
        or_row('{2x-1}', '{0}', '{x+2}', '{0}', '令兩個因式各自為 0'),
        or_row('{x_1}', '{1/2}', '{x_2}', '{-2}', '兩根各 1 分　【2 分】'),
        answer_row('{x_1=1/2} 或 {x_2=-2}'),
    ], why_pct=0.32, col_frac=(0.400, 0.050, 0.130, 0.060, 0.110, 0.050)))

    P.append(heading('六、判別式（7 分）'))
    P.append(ans_tbl([('10', 'D', 'a = 1，b = −4，c = 2；Δ = (−4)² − 4(1)(2) = 16 − 8 = 8。'
                                  '※ 易錯：選 C（把 (−4)² 算成 −16）')]))
    P.append(para('11．（4 分）兩個相等的實數根，即 {Δ=0}：', bold=True, keep_next=True))
    P.append(wtbl([
        span_row('{a=2}，{b=1}，{c=-k}', '先讀係數　※ 常數項要連負號一起讀'),
        eq_row('{Δ}', '{b^2-4ac}', '寫判別式公式'),
        eq_row('{Δ}', '{(1)^2-4(2)(-k)}', '代入　【1 分】　※ 負負得正'),
        eq_row('{Δ}', '{1+8k}', '化簡'),
        eq_row('{1+8k}', '{0}', '兩個相等的實數根，令 Δ = 0　【1 分】'),
        eq_row('{8k}', '{-1}', '移項'),
        eq_row('{k}', '{-1/8}', '兩邊除以 8　【2 分】'),
        answer_row('{k=-1/8}', '答句'),
    ], why_pct=0.36))

    P.append(heading('七、綜合題（5 分）'))
    P.append(para('12 (1) 求證：不論 {m} 為何值，該方程總有兩個實數根。（3 分）',
                  bold=True, keep_next=True))
    P.append(wtbl([
        span_row('{a=1}，{b=-(m+2)}，{c=2m}', '先讀係數'),
        eq_row('{Δ}', '{b^2-4ac}', '寫判別式公式'),
        eq_row('{Δ}', '{(m+2)^2-4(1)(2m)}', ['代入　【1 分】',
                                             '※ b 帶負號，平方後變正，可直接寫 (m + 2)²']),
        eq_row('{Δ}', '{m^2+4m+4-8m}', '展開'),
        eq_row('{Δ}', '{m^2-4m+4}', '合併同類項'),
        eq_row('{Δ}', '{(m-2)^2}', '再寫成完全平方　【1 分】'),
        span_row('{(m-2)^2>=0}', '完全平方恆非負　【1 分】'),
        answer_row('{Δ>=0}，故不論 {m} 為何值，方程總有兩個實數根',
                   '答句　※ 只寫 Δ ≥ 0 而未說明理由，此 1 分不給'),
    ], why_pct=0.34, col_frac=(0.330, 0.050, 0.200, 0.060, 0.110, 0.050)))

    P.append(para('12 (2) 若方程的一個根是 1，求 {m} 的值及方程的另一個根。（2 分）',
                  bold=True, keep_next=True))
    P.append(wtbl([
        eq_row('{(1)^2-(m+2)(1)+2m}', '{0}', '把 {x=1} 代入原方程'),
        eq_row('{1-m-2+2m}', '{0}', '展開　※ 括號前是減號，兩項都要變號'),
        eq_row('{m-1}', '{0}', '合併同類項'),
        eq_row('{m}', '{1}', '【1 分】'),
        span_row('{x^2-3x+2=0}', '把 m = 1 代回原方程'),
        eq_row('{(x-1)(x-2)}', '{0}', '因式分解'),
        or_row('{x_1}', '{1}', '{x_2}', '{2}', '其中 x₁ = 1 是題目已給的根'),
        answer_row('{m=1}，另一個根是 {x=2}', '【1 分】'),
    ], why_pct=0.30, col_frac=(0.460, 0.045, 0.120, 0.055, 0.090, 0.045)))
    save(P, BASE + '_教師卷.docx', '初三數學補救班．課後補救教學 2026-09-16（教師卷）')


if __name__ == '__main__':
    student()
    teacher()
    print('OK')
