# -*- coding: utf-8 -*-
r"""
build_check01_quadratic.py — 初三數學 單元小檢測 01（一元二次方程・概念與三種解法）

需求（2026-09-11 使用者當次指定＋AskUserQuestion 四項裁決）：
- 約 30 分鐘；範圍＝單元 01，**不考因式分解法**；教材依據＝人教版九上 21.1–21.2.2
  ＋ 本工作區 `初三數學\融合班講義練習\01_一元二次方程_概念與三種解法\`。
- 必考：①判別一元二次方程（含分式方程、無理方程易錯項）②化為一般式（標準式），
  寫出各項及係數的中文名稱，分清「項」與「係數」③直接開平方法 ④配方法 ⑤公式法。
- 題目藍圖照使用者確認版；滿分 50。
- 卷 S＝標準版；卷 A＝輔助版：**同題同分**（調整支援，不是課程剪裁），
  教學設計＝主 D2 手順卡（步驟框架）＋輔 D7 提示卡＋輔 D12 自我核對。
- 教師卷一份，兩版共用。檔名前綴 `小檢測_`（QA 的 GENRE_RE 不收，QB-6 會 FAIL，已知）。

house-style 偏離說明（測驗卷文類，刻意）：
1. 不用 ★ 三層難度標籤——全班同卷、每題有分值，沒有分層概念。
2. masthead 類型寫「抽離課堂檢測」；兩版學生卷 masthead 相同，不在學生紙面印「輔助版」
   字樣（避免標籤化），只在頁尾以「卷 S／卷 A」小字區分，方便教師分派與收卷。
3. 卷 A 的步驟框架沿用講義範例表（左算式＋等號對齊／右步驟提示），右欄就是提示欄；
   表格型題目（第一、二大題）與提示卡才另開 aside 側欄，核對清單能放側欄就放側欄（省頁）。
"""
import sys, os, re

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _run, _tbl, _PAGE_CONTENT_WIDTH  # star-import 跳過底線開頭的名稱

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學'
UNIT = '一元二次方程・概念與三種解法'
BASE = '抽離課堂檢測_初三數學_01_一元二次方程概念與三種解法'
W = _PAGE_CONTENT_WIDTH

_PPR = re.compile(r'<w:pPr>((?:(?!</w:pPr>).)*?)</w:pPr>', re.S)


def tighten(xml):
    """para(spacing=False) 並不是零行距：它不寫 <w:spacing>，於是繼承 Word Normal 的
    段後 8pt（記憶 docx_spacing_false_is_not_zero）。表格格內每段多 8pt，第一版輔助版
    因此脹到 10 頁、兩頁只剩一個核對框。這裡把「沒有寫 spacing 的段落」補上零段距。
    插在 <w:jc> 之前——pPr 子元素 schema 次序是 …pBdr, shd, spacing, ind, jc。"""
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


def lines(n, row_sz=32):
    """作答橫線。不直接用 write_lines()：它產生的 n 段框線設定完全相同，Word 會把相鄰
    同框線段落併成一組，只畫最後一條下框線（第一版 PDF 實測：5 條線只見 1 條）。
    逐行交替 w:space 與 1 twip 右縮排，令相鄰兩段的框線設定不同，就不會被合併。"""
    out = []
    for i in range(n):
        ppr = ('<w:pPr><w:pBdr>'
               f'<w:bottom w:val="single" w:sz="5" w:space="{4 + i % 2}" w:color="{LINE_GREY}"/>'
               '</w:pBdr><w:spacing w:line="360" w:lineRule="auto" w:before="60" w:after="0"/>'
               f'<w:ind w:right="{i % 2}"/></w:pPr>')
        run = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
               '<w:t xml:space="preserve"> </w:t></w:r>')
        out.append(f'<w:p>{ppr}{run}</w:p>')
    return out


# ============================ 共用小構件 ============================
def mc(markup, jc='left', bold=False, sz=BODY_SZ):
    """表格格內的數學段落。前置空白 run：整段只有一條公式時 Word 會當 display
    math 置中（house-style 範例段坑一）。"""
    segs = text_to_segments(markup)
    return para([('t', ' ')] + list(segs), jc=jc, bold=bold, sz=sz, spacing=False)


def tc(text, jc='left', bold=False, sz=22):
    return para(text, jc=jc, bold=bold, sz=sz, spacing=False)


def hdr_cell(text, jc='left'):
    return {'p': [tc(text, jc=jc, bold=True)], 'shd': GREY_FILL, 'va': 'center'}


def q(text, keep=True):
    """題幹段落；keep_next 讓題幹不會與下面的作答區分頁分離。"""
    return para(text, keep_next=keep)


def frame_table(rows, headers=('我的算式', '步驟提示'), why_pct=0.36, h=680, col_frac=None):
    """卷 A 的步驟框架＝講義範例表的「留空版」：等號已印好並上下對齊，
    左式／右式留空給學生寫，右欄是該步提示（D2 手順卡落在題目上）。

    worked_example_table() 沒有列高參數，手寫需要約 1.2cm 一行，
    所以在輸出 XML 上為每一個非表頭列補 trHeight（atLeast，公式高時會自動撐高）。
    trPr 子元素順序：cantSplit → trHeight → tblHeader（schema 固定）。"""
    frac = col_frac or (0.30, 0.05, 0.22, 0.06, 0.14, 0.05)
    xml = keep_table(tight_header(worked_example_table(rows, headers=headers, why_pct=why_pct, col_frac=frac)))
    return xml.replace('<w:trPr><w:cantSplit/></w:trPr>',
                       f'<w:trPr><w:cantSplit/><w:trHeight w:val="{h}" w:hRule="atLeast"/></w:trPr>')


def why(*lines):
    """右欄多行提示（第一行是步驟，其後是 ※ 易錯點）。"""
    return [para(t, sz=21, spacing=False) for t in lines]


def check(items):
    """selfcheck_list() 去掉尾隨空段——那個空段會溢出成一整張空白頁（第二版實測）。"""
    x = selfcheck_list(items)
    return x[:-len(blank())] if x.endswith(blank()) else x


def tight_header(xml):
    """範例／框架表的表頭段落用 1.5 倍行距＋段後，表頭列比內容列還高；只收第一列。"""
    i = xml.find('</w:tr>')
    return xml[:i].replace('<w:spacing w:line="360" w:lineRule="auto" w:after="80"/>',
                           '<w:spacing w:before="0" w:after="0" w:line="276" w:lineRule="auto"/>') + xml[i:]


def keep_table(xml):
    """整張範例／框架表不准被分頁切開：除最後一列外，每段加 keepNext（Word 的做法——
    表格沒有「整表不分頁」屬性）。第三版教師卷 五(2) 的表被切成兩頁，此函數修正。
    keepNext 是 pPr 第一個子元素（本檔不用 pStyle），插在 <w:pPr> 之後即合 schema。"""
    i = xml.rfind('<w:tr>')
    head = re.sub(r'<w:pPr>(?!<w:keepNext/>)', '<w:pPr><w:keepNext/>', xml[:i])
    head = re.sub(r'<w:p>(?!<w:pPr>)', '<w:p><w:pPr><w:keepNext/></w:pPr>', head)
    return head + xml[i:]


def label_para(name, hint):
    """卷 A 表格名稱格：名稱（粗）＋同一行小字 ※ 提示，一列只佔一行高。"""
    body = _run(name, bold=True, sz=22) + _run('　※ ', sz=19)
    for sg in text_to_segments(hint):
        body += _run(sg[1], sz=19) if sg[0] == 't' else size_math(sg[1], 19)
    return f'<w:p><w:pPr><w:jc w:val="left"/></w:pPr>{body}</w:p>'


def aside_check(items):
    """D12 核對清單的側欄版（段落 list）——selfcheck_list() 寫死整頁寬，塞進 aside 會爆欄。"""
    return ([para(' ', sz=12, spacing=False),
             para('做完先自己核對一次', bold=True, sz=21, spacing=False, shd=GREY_FILL)]
            + [para(f'{CHECKBOX} {t}', sz=20, spacing=False, shd=GREY_FILL) for t in items])


CODES = [
    para('原因代碼', bold=True, sz=22, spacing=False),
    para('A：含兩個未知數　　　　B：分母含未知數（分式方程）', sz=22, spacing=False),
    para('C：根號內含未知數（無理方程）　　D：整理後未知數的最高次數不是 2', sz=22, spacing=False),
    para('E：不能確定二次項係數不是 0', sz=22, spacing=False),
]

EQ1 = [  # 第一大題 8 條方程（兩版共用）
    '{3x^2-5=0}',
    '{x^2+frac(1,x)=2}',
    '{2x^2+sqrt(3)x-1=0}',
    '{x^2+sqrt(x)-1=0}',
    '{frac(x^2,3)-x=1}',
    '{x^2-2xy+1=0}',
    '{(x-1)(x+2)=x^2}',
    '{ax^2+bx+c=0}（x 為未知數）',
]
EQ2 = ['{5x^2=3-2x}', '{2x(x-3)=x+4}', '{x(x+4)=4x+7}']
STMT = [
    '方程 {3x^2-4x+1=0} 的一次項是 {-4}。',
    '方程 {2x^2+x-5=0} 的二次項係數是 {2x^2}。',
    '方程 {x^2-6=0} 的一次項係數是 0。',
]
NAMES = ['一般式', '二次項', '二次項係數', '一次項', '一次項係數', '常數項']


def judge_table(total_w):
    """第一大題作答表。total_w＝表格總寬（放進 aside 左欄時要扣掉儲存格內距）。"""
    ws = [int(total_w * f) for f in (0.07, 0.53, 0.20)]
    ws.append(total_w - sum(ws))
    rows = [{'hdr': True, 'cells': [hdr_cell('題', 'center'), hdr_cell('方程'),
                                     hdr_cell('圈一個', 'center'), hdr_cell('原因代碼')]}]
    for i, e in enumerate(EQ1):
        rows.append({'h': 620, 'cells': [
            {'p': [tc(marker(i + 1), jc='center', sz=24)], 'va': 'center'},
            {'p': [mc(e)], 'va': 'center'},
            {'p': [tc('是　不是', jc='center', sz=24)], 'va': 'center'},
            {'p': [blank()]}]})
    return _tbl(rows, ws, trailing_blank=False)


def form_table(assist=False):
    """第二大題（一）作答表：轉置排法——列＝名稱、欄＝三條方程，
    每條方程有 5.1cm 闊可寫，比「一條方程一列、七欄並排」好寫得多。"""
    lab = int(W * (0.27 if assist else 0.19))
    rest = W - lab
    ws = [lab, rest // 3, rest // 3, rest - 2 * (rest // 3)]
    rows = [{'hdr': True, 'cells': [hdr_cell('※ 全部連正負號寫' if assist else '')] +
             [hdr_cell(f'({i + 1}) {e}') for i, e in enumerate(EQ2)]}]
    hints = {
        '整理過程': '展開 → 移項 → 右邊＝0',
        '一般式': '右邊要是 0',
        '二次項': '連 {x^2} 寫',
        '二次項係數': '{x^2} 前面的數',
        '一次項': '連 x 寫',
        '一次項係數': 'x 前面的數',
        '常數項': '沒有 x 的數',
    }
    for name in ['整理過程'] + NAMES:
        lab_p = [label_para(name, hints[name]) if assist else tc(name, bold=True)]
        rows.append({'h': (1700 if assist else 1900) if name == '整理過程' else 640,
                     'cells': [{'p': lab_p, 'va': 'center', 'shd': GREY_FILL}] +
                              [{'p': [blank()]} for _ in range(3)]})
    return _tbl(rows, ws, trailing_blank=False)


def stmt_table(total_w=W, frac=(0.50, 0.14), sz=24):
    ws = [int(total_w * frac[0]), int(total_w * frac[1])]
    ws.append(total_w - sum(ws))
    rows = [{'hdr': True, 'cells': [hdr_cell('句子'), hdr_cell('圈一個', 'center'),
                                     hdr_cell('改正（只限圈「錯」的）' if total_w == W else '改正')]}]
    for i, s in enumerate(STMT):
        rows.append({'h': 700, 'cells': [
            {'p': [tc(f'{"abc"[i]}．' + s, sz=sz)], 'va': 'center'},
            {'p': [tc('對　　錯' if total_w == W else '對　錯', jc='center', sz=24)], 'va': 'center'},
            {'p': [blank()]}]})
    return _tbl(rows, ws, trailing_blank=False)


def gap():
    """兩個表格之間 Word 必須有段落；用矮身段，不佔一整行。"""
    return ('<w:p><w:pPr><w:spacing w:line="160" w:lineRule="auto" w:before="0" w:after="0"/>'
            '</w:pPr><w:r><w:rPr><w:sz w:val="8"/></w:rPr><w:t xml:space="preserve"> </w:t></w:r></w:p>')


FILL_BLANK = [  # 四(1) 填空：x² − 10x + ＿＿ ＝ (x − ＿＿)²（括號跨越填空位，只能手砌 OMML）
    ('t', '(1) 填空：'),
    ('m', omath(sup(mr('x'), mr('2')), mr('−10x+'))),
    ('t', '＿＿＿＿'),
    ('m', omath(mr('=(x−'))),
    ('t', '＿＿＿＿'),
    ('m', omath(sup(mr(')'), mr('2')))),
    ('t', '　（2 分）'),
]

TIME_LINE = '限時 30 分鐘　　共五大題　　滿分 50 分　　　　得分：＿＿＿＿ / 50'


# ============================ 卷 S：標準版 ============================
def build_standard():
    P = [masthead(SUBJECT, UNIT, '抽離課堂檢測'), student_info_row(),
         para(TIME_LINE, bold=True, sz=22),
         para('第三至五大題須寫出計算過程。', sz=22)]

    P.append(heading('一、判別一元二次方程（8 分）'))
    P.append(q('下列方程是不是一元二次方程？在「是」或「不是」圈一個；'
               '圈「不是」的，再寫出原因代碼。（每題 1 分）'))
    P.append(problem_box(CODES, trailing_blank=False))
    P.append(gap())
    P.append(judge_table(W))
    P.append(blank())

    P.append(heading('二、一般式、項與係數（15 分）', page_break_before=True))
    P.append(q('（一）把下列方程化為一般式（標準式）{ax^2+bx+c=0}，再填寫下表。（每條 4 分）'))
    P.append(form_table())
    P.append(gap())
    P.append(q('（二）判斷下列句子，在「對」或「錯」圈一個；圈「錯」的要改正。（每句 1 分）'))
    P.append(stmt_table())
    P.append(blank())

    P.append(heading('三、直接開平方法（8 分）'))
    P.append(problem_box([para('(1) 用直接開平方法解方程 {2(x+1)^2-18=0}　（4 分）')]
                         + lines(5)))
    P.append(problem_box([para('(2) 用直接開平方法解方程 {3x^2+12=0}　（4 分）')]
                         + lines(4)))

    P.append(heading('四、配方法（7 分）'))
    P.append(problem_box([para(FILL_BLANK)]))
    P.append(problem_box([para('(2) 用配方法解方程 {2x^2-16x+10=0}　（5 分）')]
                         + lines(6)))

    P.append(heading('五、公式法（12 分）'))
    P.append(problem_box([para('(1) 用公式法解方程 {3x^2+5x-2=0}　（5 分）')] + lines(7)))
    P.append(problem_box([para('(2) 用公式法解方程 {x^2=4x-1}　（5 分）')] + lines(7)))
    P.append(problem_box([para('(3) 不解方程，用判別式判斷方程 {x^2+2x+5=0} 根的情況。　（2 分）')]
                         + lines(3)))
    save(P, f'{BASE}_標準版.docx', '初三數學．抽離課堂檢測 01（卷 S）')


# ============================ 卷 A：輔助版 ============================
ABC_ROW = 'a ＝　　　　　b ＝　　　　　c ＝'
DELTA_TICK = '※ 剔一個：☐ Δ＞0　☐ Δ＝0　☐ Δ＜0'
ROOT_TICK = '※ 看右邊：☐ 正數　☐ 零　☐ 負數'


def build_assist():
    P = [masthead(SUBJECT, UNIT, '抽離課堂檢測'), student_info_row(),
         para(TIME_LINE, bold=True, sz=22),
         shaded_box('右邊灰色格是提示。解方程的題目已經畫好步驟格：等號已印好，'
                    '跟著右欄一步一步寫。', sz=22)]

    # ---- 一 ----
    P.append(heading('一、判別一元二次方程（8 分）'))
    P.append(q('下列方程是不是一元二次方程？在「是」或「不是」圈一個；'
               '圈「不是」的，再寫出原因代碼。（每題 1 分）'))
    P.append(problem_box(CODES, trailing_blank=False))
    P.append(gap())
    main_w = int(W * 0.66) - 240
    P.append(aside_layout(
        [judge_table(main_w)],
        hint_lines(['① 分母裡有沒有 x？有 → B',
                    '② 根號裡有沒有 x？有 → C',
                    '③ 除了 x，還有別的字母未知數嗎？有 → A',
                    '④ 展開、移項後，{x^2} 還在嗎？不在 → D',
                    '⑤ {x^2} 前面是字母，不知道是不是 0？→ E',
                    '五問都過關 → 圈「是」',
                    '※ 分母或根號裡只有數字（如 {sqrt(3)}、{frac(x^2,3)}），不算！'],
                   title='判斷五問（由 ① 問到 ⑤）')
        + aside_check(['圈「不是」的每一題都寫了原因代碼',
                       '分母、根號裡只有數字的，沒有誤判成「不是」']),
        main_pct=0.66))

    # ---- 二 ----
    P.append(heading('二、一般式、項與係數（15 分）', page_break_before=True))
    P.append(q('（一）把下列方程化為一般式（標準式）{ax^2+bx+c=0}，再填寫下表。（每條 4 分）'))
    P.append(form_table(assist=True))
    P.append(gap())
    P.append(q('（二）判斷下列句子，在「對」或「錯」圈一個；圈「錯」的要改正。（每句 1 分）'))
    P.append(aside_layout(
        [stmt_table(int(W * 0.66) - 240, frac=(0.50, 0.16), sz=22)],
        hint_lines(['例：{4x^2-9x+2=0}',
                    '二次項 {4x^2}，二次項係數 4',
                    '一次項 {-9x}，一次項係數 −9',
                    '常數項 2',
                    '※「項」連字母寫，「係數」只寫數'], title='提示卡：項 與 係數')
        + aside_check(['一般式的右邊是 0', '正負號跟一般式一致']),
        main_pct=0.66))

    # ---- 三 ----
    P.append(heading('三、直接開平方法（8 分）', page_break_before=True))
    P.append(q('(1) 用直接開平方法解方程 {2(x+1)^2-18=0}　（4 分）'))
    P.append(frame_table([
        eq_row('{2(x+1)^2}', '', why('① 移項：常數過等號要變號')),
        eq_row('{(x+1)^2}', '', why('② 兩邊除以 2', ROOT_TICK)),
        or_row('{x+1}', '', '{x+1}', '',
               why('③ 右邊是正數才做這行：兩邊開平方，分兩支', '※ 右邊是負數 → 跳到 ⑤ 寫「無實數根」')),
        or_row('{x_1}', '', '{x_2}', '', why('④ 兩支各自移項')),
        answer_row('', why=why('⑤ 用「∴」寫答句')),
    ]))
    P.append(q('(2) 用直接開平方法解方程 {3x^2+12=0}　（4 分）'))
    P.append(frame_table([
        eq_row('{3x^2}', '', why('① 移項：常數過等號要變號')),
        eq_row('{x^2}', '', why('② 兩邊除以 3', ROOT_TICK)),
        or_row('{x}', '', '{x}', '',
               why('③ 右邊是正數才做這行：兩邊開平方，分兩支', '※ 右邊是負數 → 跳到 ④ 寫「無實數根」')),
        answer_row('', why=why('④ 用「∴」寫答句')),
    ]))
    P.append(check(['開平方前看過右邊是正、零還是負', '有兩個根的，兩個都寫進「∴」答句']))

    # ---- 四 ----
    P.append(heading('四、配方法（7 分）', page_break_before=True))
    P.append(aside_layout(
        [para(FILL_BLANK)],
        hint_lines(['加的數 ＝（一次項係數的一半）²', '例：{x^2+6x+9=(x+3)^2}'], title='提示'),
        main_pct=0.58, boxed=True))
    P.append(q('(2) 用配方法解方程 {2x^2-16x+10=0}　（5 分）'))
    P.append(frame_table([
        eq_row('', '{0}', why('① 兩邊除以二次項係數 2', '※ 每一項都要除')),
        eq_row('', '', why('② 常數項移到右邊', '※ 移項要變號')),
        eq_row('', '', why('③ 兩邊都加「一次項係數一半的平方」')),
        eq_row('', '', why('④ 左邊配成完全平方，右邊算出一個數')),
        or_row('', '', '', '', why('⑤ 兩邊開平方，分兩支，中間寫「或」')),
        or_row('{x_1}', '', '{x_2}', '', why('⑥ 兩支各自移項')),
        answer_row('', why=why('⑦ 用「∴」寫出兩個根')),
    ]))
    P.append(check(['加的數，等號兩邊都加了', '開平方後分兩支，中間寫了「或」']))

    # ---- 五 ----
    P.append(heading('五、公式法（12 分）', page_break_before=True))
    P.append(aside_layout(
        [q('(1) 用公式法解方程 {3x^2+5x-2=0}　（5 分）')],
        [para('提示卡：公式法', bold=True, sz=21, spacing=False, shd=GREY_FILL),
         para('求根公式', sz=20, spacing=False, shd=GREY_FILL),
         para([('t', ' ')] + list(text_to_segments('{x=frac(-b+-sqrt(b^2-4ac),2a)}')),
              sz=20, spacing=False, shd=GREY_FILL),
         para('判別式 {Δ=b^2-4ac}', sz=20, spacing=False, shd=GREY_FILL),
         para('Δ＞0：有兩個不相等的實數根', sz=20, spacing=False, shd=GREY_FILL),
         para('Δ＝0：有兩個相等的實數根', sz=20, spacing=False, shd=GREY_FILL),
         para('Δ＜0：無實數根', sz=20, spacing=False, shd=GREY_FILL)]
        + aside_check(['a、b、c 有連正負號', '先算 Δ，再決定要不要用公式', '根號化簡了、分數約簡了']),
        main_pct=0.55))
    P.append(frame_table([
        span_row(ABC_ROW, why('① 已是一般式，讀出 a、b、c', '※ 連正負號')),
        eq_row('{Δ}', '{b^2-4ac}', why('② 先寫判別式公式')),
        eq_row('{Δ}', '', why('③ 代入 a、b、c', '※ 負數代入要加括號')),
        eq_row('{Δ}', '', why('④ 算出 Δ', DELTA_TICK)),
        or_row('{x_1}', '{frac(-b+sqrt(Δ),2a)}', '{x_2}', '{frac(-b-sqrt(Δ),2a)}',
               why('⑤ 照抄公式，± 拆成兩支')),
        or_row('{x_1}', '', '{x_2}', '', why('⑥ 代入', '※ −b 是 b 的相反數')),
        or_row('{x_1}', '', '{x_2}', '', why('⑦ 算出並約簡')),
        answer_row('', why=why('⑧ 用「∴」寫出兩個根')),
    ]))
    P.append(para('(2) 用公式法解方程 {x^2=4x-1}　（5 分）', keep_next=True, page_break_before=True))
    P.append(frame_table([
        eq_row('', '{0}', why('① 移項，化成一般式', '※ 右邊要等於 0')),
        span_row(ABC_ROW, why('② 讀出 a、b、c', '※ 連正負號')),
        eq_row('{Δ}', '', why('③ 代入 {Δ=b^2-4ac}')),
        eq_row('{Δ}', '', why('④ 算出 Δ', DELTA_TICK)),
        or_row('{x_1}', '', '{x_2}', '', why('⑤ 代入求根公式，± 拆成兩支')),
        or_row('{x_1}', '', '{x_2}', '', why('⑥ 化簡根號', '※ 例：{sqrt(8)=2sqrt(2)}')),
        or_row('{x_1}', '', '{x_2}', '', why('⑦ 分子每一項都除以分母，約簡')),
        answer_row('', why=why('⑧ 用「∴」寫出兩個根')),
    ]))
    P.append(q('(3) 不解方程，用判別式判斷方程 {x^2+2x+5=0} 根的情況。　（2 分）'))
    P.append(frame_table([
        span_row(ABC_ROW, why('① 讀出 a、b、c')),
        eq_row('{Δ}', '', why('② 代入 {Δ=b^2-4ac}')),
        eq_row('{Δ}', '', why('③ 算出 Δ')),
        span_row('∴ ☐ 兩個不相等的實數根　☐ 兩個相等的實數根　☐ 無實數根',
                 why('④ 看 Δ 的正負，剔一個')),
    ]))
    P.append(para('（全卷完）', jc='center', sz=22))
    save(P, f'{BASE}_輔助版.docx', '初三數學．抽離課堂檢測 01（卷 A）')


# ============================ 教師卷 ============================
T_FRAC = (0.27, 0.05, 0.26, 0.06, 0.14, 0.05)


def key_table(rows):
    return keep_table(tight_header(worked_example_table(rows, headers=('算式', '說明與評分'),
                                                       why_pct=0.36, col_frac=T_FRAC)))


def build_teacher():
    P = [masthead(SUBJECT, UNIT, '抽離課堂檢測・教師卷'),
         para('本卷供教師批改使用，不發給學生。標準版（卷 S）與輔助版（卷 A）題目、數字、'
              '分值完全相同，共用本答案與評分。滿分 50 分。', sz=22)]

    P.append(heading('一、參考答案與評分'))
    # ---- 一 ----
    P.append(para('第一大題　判別一元二次方程（8 分）', bold=True))
    P.append(para('評分：「是」的題目圈對得 1 分；「不是」的題目要圈對且原因代碼正確才得 1 分。', sz=22))
    ans1 = [('是', '', '整式方程、一個未知數、最高次數 2'),
            ('不是', 'B', '分母含 x，是分式方程'),
            ('是', '', '易錯：√3 是係數（數字），根號內沒有未知數'),
            ('不是', 'C', '根號內含 x，是無理方程'),
            ('是', '', '易錯：分母 3 是數字，仍是整式方程'),
            ('不是', 'A', '含 x、y 兩個未知數'),
            ('不是', 'D', '易錯：展開得 {x^2+x-2=x^2}，整理後 {x-2=0}，是一元一次方程'),
            ('不是', 'E', '易錯：沒有注明 {a!=0}；a＝0 時不是二次方程')]
    ws = [int(W * f) for f in (0.06, 0.33, 0.09, 0.07)]
    ws.append(W - sum(ws))
    rows = [{'hdr': True, 'cells': [hdr_cell('題', 'center'), hdr_cell('方程'), hdr_cell('答案', 'center'),
                                     hdr_cell('代碼', 'center'), hdr_cell('說明')]}]
    for i, (e, (a, c, note)) in enumerate(zip(EQ1, ans1)):
        rows.append({'cells': [{'p': [tc(marker(i + 1), jc='center')], 'va': 'center'},
                               {'p': [mc(e, sz=22)], 'va': 'center'},
                               {'p': [tc(a, jc='center', bold=True)], 'va': 'center'},
                               {'p': [tc(c or '—', jc='center', bold=True)], 'va': 'center'},
                               {'p': [tc(note)], 'va': 'center'}]})
    P.append(_tbl(rows, ws))

    # ---- 二 ----
    P.append(para('第二大題　一般式、項與係數（15 分）', bold=True, keep_next=True))
    P.append(para('（一）每條 4 分：一般式 1 分；表格五格共 3 分（全對 3 分，每錯 1 格扣 1 分，扣完為止）。',
                  sz=22, keep_next=True))
    lab = int(W * 0.19)
    rest = W - lab
    ws2 = [lab, rest // 3, rest // 3, rest - 2 * (rest // 3)]
    ans2 = {
        '整理過程': ['移項：{5x^2+2x-3=0}', '展開：{2x^2-6x=x+4}', '展開：{x^2+4x=4x+7}'],
        '一般式': ['{5x^2+2x-3=0}', '{2x^2-7x-4=0}', '{x^2-7=0}'],
        '二次項': ['{5x^2}', '{2x^2}', '{x^2}'],
        '二次項係數': ['5', '2', '1'],
        '一次項': ['{2x}', '{-7x}', '0（或寫「沒有」）'],
        '一次項係數': ['2', '−7', '0'],
        '常數項': ['−3', '−4', '−7'],
    }
    rows = [{'hdr': True, 'cells': [hdr_cell('')] + [hdr_cell(f'({i + 1}) {e}') for i, e in enumerate(EQ2)]}]
    for name in ['整理過程'] + NAMES:
        rows.append({'cells': [{'p': [tc(name, bold=True)], 'shd': GREY_FILL, 'va': 'center'}] +
                              [{'p': [mc(v, sz=22)], 'va': 'center'} for v in ans2[name]]})
    P.append(_tbl(rows, ws2, trailing_blank=False))
    P.append(gap())
    P.append(para('※ 第 (3) 條是兩個陷阱：二次項係數是看不見的 1；一次項消去後一次項係數是 0。', sz=22))
    P.append(para('※ 學生若寫成二次項係數為負的形式（如 {-5x^2-2x+3=0}）而表格各格與之一致，照給分；'
                  '批改時提醒慣例是把二次項係數化為正數。', sz=22))
    P.append(para('（二）每句 1 分；圈「錯」的要改正正確才得分。', sz=22, keep_next=True))
    ws3 = [int(W * 0.44), int(W * 0.10)]
    ws3.append(W - sum(ws3))
    rows = [{'hdr': True, 'cells': [hdr_cell('句子'), hdr_cell('答案', 'center'), hdr_cell('改正／說明')]},
            [{'p': [tc('a．' + STMT[0])]}, {'p': [tc('錯', jc='center', bold=True)]},
             {'p': [tc('一次項是 {-4x}；−4 是一次項係數')]}],
            [{'p': [tc('b．' + STMT[1])]}, {'p': [tc('錯', jc='center', bold=True)]},
             {'p': [tc('二次項係數是 2；{2x^2} 是二次項')]}],
            [{'p': [tc('c．' + STMT[2])]}, {'p': [tc('對', jc='center', bold=True)]},
             {'p': [tc('沒有一次項，一次項係數 b＝0')]}]]
    P.append(_tbl(rows, ws3))

    # ---- 三 ----
    P.append(para('第三大題　直接開平方法（8 分）', bold=True, keep_next=True))
    P.append(para('(1) {2(x+1)^2-18=0}（4 分）', keep_next=True))
    P.append(key_table([
        eq_row('{2(x+1)^2-18}', '{0}', '原方程'),
        eq_row('{2(x+1)^2}', '{18}', '移項'),
        eq_row('{(x+1)^2}', '{9}', why('兩邊除以 2【1 分】', '※ 9＞0，可以開平方')),
        or_row('{x+1}', '{3}', '{x+1}', '{-3}', '開平方分兩支【1 分】'),
        or_row('{x}', '{3-1}', '{x}', '{-3-1}', '兩支各自移項'),
        or_row('{x_1}', '{2}', '{x_2}', '{-4}', '兩根各 1 分【2 分】'),
        answer_row('{x_1=2} 或 {x_2=-4}', why=''),
    ]))
    P.append(para('(2) {3x^2+12=0}（4 分）', keep_next=True))
    P.append(key_table([
        eq_row('{3x^2+12}', '{0}', '原方程'),
        eq_row('{3x^2}', '{-12}', '移項【1 分】'),
        eq_row('{x^2}', '{-4}', why('兩邊除以 3【1 分】', '※ 指出 −4＜0，負數不能開平方【1 分】')),
        answer_row('此方程無實數根', why=why('結論【1 分】', '※ 寫成 {x_1=2} 或 {x_2=-2} 者，後兩分不給')),
    ]))

    # ---- 四 ----
    P.append(para('第四大題　配方法（7 分）', bold=True, keep_next=True))
    P.append(para('(1) 25；5（各 1 分）。驗算：{(x-5)^2=x^2-10x+25}', keep_next=True))
    P.append(para('(2) {2x^2-16x+10=0}（5 分）', keep_next=True))
    P.append(key_table([
        eq_row('{2x^2-16x+10}', '{0}', '原方程'),
        eq_row('{x^2-8x+5}', '{0}', '兩邊除以 2【1 分】'),
        eq_row('{x^2-8x}', '{-5}', '移項'),
        eq_row('{x^2-8x+16}', '{-5+16}', why('兩邊加 16【1 分】', '※ 16＝(−8÷2)²')),
        eq_row('{(x-4)^2}', '{11}', '配成完全平方【1 分】'),
        or_row('{x-4}', '{sqrt(11)}', '{x-4}', '{-sqrt(11)}', '開平方分兩支'),
        or_row('{x_1}', '{4+sqrt(11)}', '{x_2}', '{4-sqrt(11)}', '兩根各 1 分【2 分】'),
        answer_row('{x_1=4+sqrt(11)} 或 {x_2=4-sqrt(11)}', why=''),
    ]))

    # ---- 五 ----
    P.append(para('第五大題　公式法（12 分）', bold=True, keep_next=True))
    P.append(para('(1) {3x^2+5x-2=0}（5 分）', keep_next=True))
    P.append(key_table([
        eq_row('{3x^2+5x-2}', '{0}', '原方程（已是一般式）'),
        span_row('a ＝ 3，b ＝ 5，c ＝ −2', '讀出係數【1 分】'),
        eq_row('{Δ}', '{b^2-4ac}', '判別式'),
        eq_row('{Δ}', '{5^2-4(3)(-2)}', '代入　※ −4(3)(−2)＝＋24'),
        eq_row('{Δ}', '{49}', why('【1 分】', '※ 49＞0，有兩個不相等的實數根')),
        or_row('{x_1}', '{frac(-5+7,6)}', '{x_2}', '{frac(-5-7,6)}', '代入公式分兩支【1 分】'),
        or_row('{x_1}', '{frac(2,6)}', '{x_2}', '{frac(-12,6)}', '算出分子'),
        or_row('{x_1}', '{frac(1,3)}', '{x_2}', '{-2}', '約簡；兩根各 1 分【2 分】'),
        answer_row('{x_1=frac(1,3)} 或 {x_2=-2}', why=''),
    ]))
    P.append(para('(2) {x^2=4x-1}（5 分）', keep_next=True))
    P.append(key_table([
        eq_row('{x^2}', '{4x-1}', '原方程'),
        eq_row('{x^2-4x+1}', '{0}', '移項，化成一般式'),
        span_row('a ＝ 1，b ＝ −4，c ＝ 1', '化一般式並讀出係數【1 分】'),
        eq_row('{Δ}', '{(-4)^2-4(1)(1)}', '代入　※ (−4)²＝16，不是 −16'),
        eq_row('{Δ}', '{12}', '【1 分】'),
        or_row('{x_1}', '{frac(4+sqrt(12),2)}', '{x_2}', '{frac(4-sqrt(12),2)}',
               why('代入公式分兩支', '※ −b＝−(−4)＝4')),
        or_row('{x_1}', '{frac(4+2sqrt(3),2)}', '{x_2}', '{frac(4-2sqrt(3),2)}',
               why('化簡根號【1 分】', '※ {sqrt(12)=2sqrt(3)}')),
        or_row('{x_1}', '{2+sqrt(3)}', '{x_2}', '{2-sqrt(3)}',
               why('兩根各 1 分【2 分】', '※ 分子每一項都除以 2')),
        answer_row('{x_1=2+sqrt(3)} 或 {x_2=2-sqrt(3)}', why=''),
    ]))
    P.append(para('(3) {x^2+2x+5=0}（2 分）', keep_next=True))
    P.append(key_table([
        span_row('a ＝ 1，b ＝ 2，c ＝ 5', '讀出係數'),
        eq_row('{Δ}', '{2^2-4(1)(5)}', '代入'),
        eq_row('{Δ}', '{-16}', '【1 分】'),
        answer_row('此方程無實數根', why='Δ＜0【1 分】'),
    ]))

    # ---- 命題藍圖 ----
    P.append(heading('二、命題藍圖與作答時間', page_break_before=True))
    ws4 = [int(W * f) for f in (0.13, 0.37, 0.08, 0.10)]
    ws4.append(W - sum(ws4))
    blue = [('一', '判別一元二次方程；分式方程、無理方程、整理後降次、a≠0 的易錯項', '8', '約 4 分鐘',
             '人教版九上 21.1 定義「等號兩邊都是整式」；講義 一、即堂練習第 1 題'),
            ('二', '化為一般式（標準式）；二次項／二次項係數／一次項／一次項係數／常數項；項與係數的分別',
             '15', '約 7 分鐘', '人教版九上 21.1 一般形式；講義 一、公式法範例「讀係數」行'),
            ('三', '直接開平方法（含右邊為負數→無實數根）', '8', '約 4 分鐘',
             '講義 二、手順卡①；練習第 5、6 題（負數開平方）'),
            ('四', '配方法（配方填空；二次項係數不是 1 先除）', '7', '約 5 分鐘',
             '講義 三、手順卡②；練習第 10 題（先除以 2）'),
            ('五', '公式法（Δ＞0 整數根、Δ＞0 根式化簡、Δ＜0 判斷）', '12', '約 9 分鐘',
             '講義 四、手順卡③；練習第 17、18、28 題'),
            ('合計', '不考因式分解法（使用者指定）', '50', '約 29 分鐘', '')]
    rows = [{'hdr': True, 'cells': [hdr_cell('大題', 'center'), hdr_cell('考核內容'), hdr_cell('分值', 'center'),
                                     hdr_cell('建議時間'), hdr_cell('依據')]}]
    for b in blue:
        rows.append([{'p': [tc(b[0], jc='center', bold=True)], 'va': 'center'},
                     {'p': [tc(b[1])]}, {'p': [tc(b[2], jc='center')], 'va': 'center'},
                     {'p': [tc(b[3])], 'va': 'center'}, {'p': [tc(b[4])]}])
    P.append(_tbl(rows, ws4))
    P.append(para('※ 題目數字全部是新編，未與《課堂練習》或 W05 小測重複；錯誤原型取自上表所列出處。', sz=22))
    P.append(para('※ 用語依人教版：「一般形式」本卷寫作「一般式（標準式）」，與本單元講義一致。', sz=22))

    # ---- 輔助版調適說明（QB-V5 雙向一致：這裡點名的每個元件，卷 A 上都要印得出來） ----
    P.extend(teacher_notes(
        'D2 手順卡（落在題目上的步驟框架）',
        aux_designs=('D7 提示卡', 'D12 自我核對清單'),
        reason='S2 多步驟程序運算——三種解法都是序列步驟，融合生最常見的失分是漏步驟、'
               '漏分兩支、移項漏變號，而不是不懂方法。卷 A 把本單元講義的手順卡①②③直接變成'
               '題目下方的步驟格（等號已印好並對齊、右欄寫該步動作與 ※ 易錯點），'
               '學生只需逐格填寫。',
        density='抽離小班（兩版同題同分，屬調整支援 Accommodation，不是課程剪裁）',
        fading='本次卷 A：步驟格＋右欄動作提示＋※易錯點＋提示卡 → 下次檢測：步驟格只留等號、'
               '右欄只留步驟編號 → 再下次：只給「這題有幾步」→ 回到卷 S。',
        iep_codes=('a3 提示題目重點', 'a6 增加行距或放大作答欄', 'a11 提供公式卡'),
        extra=[
            ('卷 A 鷹架位置',
             '第一大題：右側「判斷五問」＋核對清單。第二大題：表格每列名稱旁 ※ 提示；'
             '辨析表旁「項與係數」提示卡（附完整例子）＋核對清單。第三至五大題：每題步驟格；'
             '開平方前「看右邊正／零／負」與 Δ 正負的剔選格。第四大題 (1) 旁配方提示。'
             '第五大題提示卡（求根公式、Δ 三情況）＋核對清單。第三、四大題核對清單在大題末。'),
            ('卷 A 刻意不給的東西',
             '步驟格不預先寫出任何一步的結果；第三大題兩題用同一套框架（含「右邊是負數 → 寫無實數根」'
             '的分岔），不因為 (2) 無實數根而少畫格，避免框架本身洩露答案。'),
            ('批改提醒',
             '卷 A 學生在步驟格內寫的算式，按上面評分表同一標準給分；剔選格剔錯但算式對，照算式給分。'),
        ]))
    save(P, f'{BASE}_教師卷.docx', '初三數學．抽離課堂檢測 01（教師卷）')


if __name__ == '__main__':
    build_standard()
    build_assist()
    build_teacher()
    print('OK')
