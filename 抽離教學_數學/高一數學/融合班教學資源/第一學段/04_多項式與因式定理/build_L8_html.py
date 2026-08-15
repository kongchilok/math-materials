# -*- coding: utf-8 -*-
r"""高一 L8《二次函數與一元二次不等式》講義／練習 HTML（→PDF 正式列印版）。

內容與 build_L8_docx.py 一一對應（house-style：docx 版與 HTML 版的同名元件外觀必須一致）。

⚠ 全檔的 LaTeX 一律寫成 raw string（r'...'）——普通字串會把 \r（\right）
   變成回車字元，MathJax 靜默渲染失敗、PDF 印出 ight)^2。
⚠ 數學式內不准出現裸 < >，一律 \lt \gt（瀏覽器會當成 HTML 標籤吞掉整段）。
"""
import os
import re
import sys

SKILL = r'C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator'
sys.path.insert(0, os.path.join(SKILL, 'scripts'))
import design_svg as ds

BASE = os.path.dirname(os.path.abspath(__file__))
FOOT = '高一數學．二次函數與一元二次不等式'

with open(os.path.join(SKILL, 'assets', 'worksheet-template.html'), encoding='utf-8') as f:
    _tpl = f.read()
HEAD = _tpl[:_tpl.index('</head>') + len('</head>')]


def page(title, body):
    head = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', HEAD, count=1)
    return (head + '\n<body>\n<table class="sheet">\n'
            f'  <tfoot><tr><td><div class="footer">{FOOT}</div></td></tr></tfoot>\n'
            '  <tbody><tr><td>\n' + body +
            '\n  </td></tr></tbody>\n</table>\n</body>\n</html>\n')


def masthead(doc_type):
    return ('  <div class="masthead"><span>科目：高一數學</span>'
            '<span>單元：二次函數與一元二次不等式</span>'
            f'<span>類型：{doc_type}</span></div>\n'
            '  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
            '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
            '日期：<span class="u">&nbsp;</span></div>\n')


def h(t, brk=False):
    """區塊標題。`break-after:avoid` 防標題孤立在頁尾——練習拿掉強制分頁、
    改讓內容自然流之後，這個保險就變成必要的（沒有它，標題會跟第一題分家）。"""
    cls = 'section-h page-break' if brk else 'section-h'
    return (f'  <div class="{cls}" style="break-after:avoid;'
            f'page-break-after:avoid">{t}</div>\n')


def p(t):
    return f'  <div>{t}</div>\n'


def lines(n):
    return ('  <div class="write-lines">' + '<div class="line"></div>' * n
            + '</div>\n')


def problem(inner):
    return f'  <div class="problem">\n{inner}  </div>\n'


def shaded(t):
    return f'  <div class="hint-card">{t}</div>\n'


def defbox(items):
    body = ''.join(f'    <div>{t}</div>\n' for t in items)
    return f'  <div class="problem">\n{body}  </div>\n'


# ---------------- 範例表（house-style 七小欄） ----------------
def eqrow(lhs, rhs, why='', rel='='):
    return (f'    <tr><td class="ec1">\\({lhs}\\)</td><td class="ec2">\\({rel}\\)</td>'
            f'<td class="ec3" colspan="5">\\({rhs}\\)</td>'
            f'<td class="why">{why}</td></tr>\n')


def orrow(l1, r1, l2, r2, why='', rel='='):
    return (f'    <tr><td class="ec1">\\({l1}\\)</td><td class="ec2">\\({rel}\\)</td>'
            f'<td class="ec3">\\({r1}\\)</td><td class="ec4">或</td>'
            f'<td class="ec5">\\({l2}\\)</td><td class="ec6">\\({rel}\\)</td>'
            f'<td class="ec7">\\({r2}\\)</td>'
            f'<td class="why">{why}</td></tr>\n')


def spanrow(t, why='', ans=False):
    cls = 'ecs ans' if ans else 'ecs'
    return (f'    <tr><td class="{cls}" colspan="7">{t}</td>'
            f'<td class="why">{why}</td></tr>\n')


def ansrow(t, why='作答：最後一行用「∴」寫出解集'):
    return spanrow(r'\(\therefore\) ' + t, why, ans=True)


def worked(lead, rows):
    return (f'  <div class="sub-h lead"><b>{lead}</b></div>\n'
            '  <table class="d-tbl worked long">\n'
            '    <thead><tr><th colspan="7">算式</th>'
            '<th class="why">這一步在做什麼</th></tr></thead>\n'
            '    <tbody>\n' + ''.join(rows) + '    </tbody>\n  </table>\n')


def example(lead, rows, fig_kw, cap4, cap5, ans):
    """一個完整範例＝算式表＋草圖（第4、5步）＋∴ 答句，三者**必須綁在同一塊**。
    分開放三張 .d-tbl 的話，日後只要算式多一列，草圖或答句就會被分頁切走
    ——那正是上一版退稿的病（使用者截圖：解題過程與圖被拆到兩頁）。"""
    return ('  <div style="break-inside:avoid;page-break-inside:avoid">\n'
            + worked(lead, rows)
            + _fig45(fig_kw, cap4, cap5)
            + '  <table class="d-tbl worked">\n    <tbody>\n' + ans
            + '    </tbody>\n  </table>\n  </div>\n')


def step_card(title, trigger, steps):
    out = ['  <table class="d-tbl step-card">\n',
           f'    <tr><th colspan="2">{title}</th></tr>\n',
           '    <tr><td colspan="2" style="font-weight:400">'
           f'什麼時候用：{trigger}</td></tr>\n']
    for i, (act, pit) in enumerate(steps, 1):
        out.append(f'    <tr><td>{i}. {act}</td>'
                   f'<td class="pitfall">※ {pit}</td></tr>\n')
    out.append('  </table>\n')
    return ''.join(out)


def selfcheck(items, title='做完先自己核對一次'):
    body = ''.join(f'    <div>☐ {t}</div>\n' for t in items)
    return (f'  <div class="selfcheck">\n    <div><b>{title}</b></div>\n'
            + body + '  </div>\n')


def checkpoint():
    return ('  <div class="checkpoint">【核對點】做到這裡先停，'
            '對照上面的清單檢查一次再往下</div>\n')


def aside(main, side):
    return ('  <div class="aside-wrap boxed">\n'
            f'    <div class="aside-main">\n{main}    </div>\n'
            f'    <div class="aside-side">\n{side}    </div>\n'
            '  </div>\n')


def hintcard(lines_, title='提示'):
    body = ''.join(f'      <div>{t}</div>\n' for t in lines_)
    return (f'      <div class="hintcard">\n        <div class="ht">{title}</div>\n'
            + body + '      </div>\n')


def sketch(**kw):
    """內嵌 SVG（不轉 PNG）——側欄用 design_svg 的原生尺寸畫，不要拿大圖硬縮。"""
    return '      ' + ds.sketch_parabola(**kw) + '\n'


# ================================================================ 共用內容
CARD = ('解一元二次不等式　五步',
        r'題目是 \(ax^2+bx+c \gt 0\)（或 \(\lt\)、\(\ge\)、\(\le\)）這種二次不等式', [
            ('把所有項搬到一邊，讓右邊變成 0', '過等號要變號；右邊不是 0 就不能往下做'),
            ('看二次項係數 a 的正負；a 是負數就整條乘 −1',
             '乘負數，不等號一定要反向——這一步最易漏'),
            ('把不等號換成等號，解方程求根，數清楚有幾個根',
             r'因式分解或用公式；\(\Delta\) 決定有 2 個、1 個還是 0 個根'),
            ('畫草圖：開口向上，在 x 軸標出根', '只畫 x 軸和拋物線，不用畫 y 軸、不用畫格線'),
            ('對照草圖挑範圍，用「∴」寫成解集', '大於取兩邊，小於取中間'),
        ])

# D12 自我核對清單——**放在練習端**（teaching-designs.md D12：講義長相「不出現」，
# 練習長相「每個 A／B／C 區塊末尾一個核對清單；區塊之間放核對點分隔」）。
# 項目一律可觀察、能自己判定，不寫「我有認真做」這種無法自我判定的話。
CHECK_A = [
    '每題都寫了算式，不是只寫答案',
    '每題都畫了草圖：有 x 軸、有拋物線、根已標在軸上',
    r'解集用 \(\{x \mid \ldots\}\) 寫；分成兩段的中間有寫「或」',
]
CHECK_B = [
    r'每題都先算了 \(\Delta\)',
    '數清楚有幾個根（2 個、1 個、還是 0 個），草圖也照樣畫',
    '「無解」和「全部實數」沒有寫反',
]
# C 區的清單刻意壓成兩項：第 9 題框之後頁底只剩約一行半的空間，三項會把整塊
# 推到下一頁、留一頁近乎全白（實測）。合併前兩項比犧牲作答行數划算。
CHECK_C = [
    'a 是負數的題目，已經乘 −1 並反向；草圖畫的是乘完之後那一條',
    '應用題的答案有寫回一段時間，不是只留一個不等式',
]


# ================================================================ 講義
def build_handout():
    B = [masthead('課堂講義')]

    B.append(h('一、由「等於 0」走到「大於 0」'))
    B.append(p(r'上一課解過方程 \(x^2-5x+6=0\)，答案是 \(x_1=2\) 或 \(x_2=3\)——兩個數。'))
    B.append(p(r'這一課問的是不等式 \(x^2-5x+6 \gt 0\)。答案不再是幾個數，而是一整段範圍。'))
    B.append(shaded('解一元二次不等式 ＝ 看二次函數的圖象落在 x 軸的哪一邊。'))
    B.append(defbox([
        r'圖象在 x 軸上方　→　\(y \gt 0\)',
        r'圖象在 x 軸下方　→　\(y \lt 0\)',
        r'圖象碰到 x 軸　　→　\(y = 0\)（那一點就是根）',
    ]))

    B.append(h('二、草圖怎麼畫、怎麼讀'))
    B.append(p('草圖只要三樣東西：一條 x 軸、一條拋物線、軸上的根。'
               '不用畫 y 軸、不用畫格線、不用算頂點——三秒畫得完才有用。'))
    B.append(p(r'以 \(y=x^2-5x+6\) 為例（根是 2 和 3，\(a=1 \gt 0\) 所以開口向上）：'))
    B.append('  <table class="d-tbl dual-track">\n'
             '    <tr><th>草圖上看到什麼</th><th>寫成什麼</th></tr>\n'
             '    <tr><td>'
             + ds.sketch_parabola(roots=(2, 3), opening='up', show_sign=True,
                                  caption='兩根之外：線在 x 軸上方')
             + r'</td><td><div>\(x \lt 2\) 或 \(x \gt 3\) 這兩段，線在 x 軸上方</div>'
               r'<div><b>所以 \(y \gt 0\)</b></div></td></tr>' + '\n'
             '    <tr><td>'
             + ds.sketch_parabola(roots=(2, 3), opening='up', solution='inside',
                                  caption='兩根之間：線在 x 軸下方')
             + r'</td><td><div>\(2 \lt x \lt 3\) 這一段，線在 x 軸下方</div>'
               r'<div><b>所以 \(y \lt 0\)</b></div></td></tr>' + '\n'
             '  </table>\n')
    B.append(shaded('所以同一幅草圖可以回答兩種問題：問 ＞ 0 就取兩邊，問 ＜ 0 就取中間。'))

    B.append(h('三、根有幾個？判別式 Δ 決定草圖長什麼樣', brk=True))
    B.append(p(r'待會手順卡的第 3 步要「數清楚有幾個根」，靠的就是判別式 '
               r'\(\Delta=b^2-4ac\)（此處 \(a \gt 0\)）：'))
    B.append(_delta_table())
    B.append(shaded('Δ ＝ 0 和 Δ ＜ 0 這兩欄，答案常常是「全部實數」或「無解」，'
                    '不要以為一定要寫出兩個數才叫答案。'))

    B.append(h('四、手順卡：解一元二次不等式五步', brk=True))
    B.append(step_card(*CARD))

    B.append(h('五、範例'))
    B.append(example(
        r'★ 範例一：解 \(x^2-5x+6 \gt 0\)',
        [
            eqrow(r'x^2-5x+6', r'0', '第 1 步：右邊已經是 0，不用搬<br>'
                                     r'第 2 步：\(a=1\)，是正數，不用乘 −1', rel=r'\gt'),
            eqrow(r'x^2-5x+6', r'0', '第 3 步：把不等號換成等號，先求根'),
            eqrow(r'(x-2)(x-3)', r'0', '因式分解'),
            orrow(r'x-2', r'0', r'x-3', r'0', '分成兩支寫，中間寫「或」'),
            orrow(r'x_1', r'2', r'x_2', r'3', '兩個不相等的根'),
        ],
        dict(roots=(2, 3), opening='up', solution='outside',
             caption='開口向上，根是 2 和 3'),
        '第 4 步：畫草圖，標出兩個根',
        '第 5 步：問的是 ＞ 0，取 x 軸上方那兩段（粗線）',
        ansrow(r'解集為 \(\{x \mid x \lt 2\) 或 \(x \gt 3\}\)')))

    B.append(example(
        r'★ 範例二：解 \(-x^2+4x-3 \gt 0\)（二次項係數是負數）',
        [
            eqrow(r'-x^2+4x-3', r'0', '第 1 步：右邊已經是 0', rel=r'\gt'),
            spanrow(r'\(a=-1\)',
                    '第 2 步：a 是負數 → 整條乘 −1，而且不等號要反向。這一步最易漏'),
            eqrow(r'x^2-4x+3', r'0', '乘 −1 之後：＞ 變成 ＜', rel=r'\lt'),
            eqrow(r'x^2-4x+3', r'0', '第 3 步：把不等號換成等號，先求根'),
            eqrow(r'(x-1)(x-3)', r'0', '因式分解'),
            orrow(r'x-1', r'0', r'x-3', r'0', '分成兩支寫，中間寫「或」'),
            orrow(r'x_1', r'1', r'x_2', r'3', '兩個不相等的根'),
        ],
        dict(roots=(1, 3), opening='up', solution='inside',
             caption='乘 −1 之後 a ＞ 0，開口向上'),
        '第 4 步：畫的是乘 −1 之後那條的草圖',
        '第 5 步：現在問的是 ＜ 0，取 x 軸下方那一段（粗線）',
        ansrow(r'解集為 \(\{x \mid 1 \lt x \lt 3\}\)', '作答：只有一段，不用寫「或」')))

    B.append(p('接下來請拿《二次函數與一元二次不等式 —— 課堂練習》，'
               '依這套五步框架完成練習 A、B、C。'))

    B.append(_teacher_notes())

    out = os.path.join(BASE, '講義_二次函數與一元二次不等式_融合版.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(page('講義_二次函數與一元二次不等式_融合版', ''.join(B)))
    return out


def _delta_table():
    spec = [
        (r'\(\Delta \gt 0\)', dict(roots=('x₁', 'x₂'), opening='up', width=220,
                                   caption='交 x 軸兩點'),
         ('取兩邊', r'\(\{x \mid x \lt x_1\) 或 \(x \gt x_2\}\)'),
         ('取中間', r'\(\{x \mid x_1 \lt x \lt x_2\}\)')),
        (r'\(\Delta = 0\)', dict(roots=('x₀',), opening='up', width=220,
                                 caption='碰 x 軸一點'),
         ('除了那一點，全部都是解', r'\(\{x \mid x \ne x_0\}\)'),
         ('無解', '（圖象沒有一段在 x 軸下方）')),
        (r'\(\Delta \lt 0\)', dict(roots=(), opening='up', width=220,
                                   caption='不碰 x 軸'),
         ('全部實數都是解', r'\(\{x \mid x\) 是任何實數\(\}\)'),
         ('無解', '（整條都在 x 軸上方）')),
    ]
    out = ['  <table class="d-tbl long">\n    <thead><tr>'
           '<th style="width:13%">判別式</th><th style="width:30%">草圖長這樣</th>'
           '<th style="width:27%">問 ＞ 0 時</th><th>問 ＜ 0 時</th>'
           '</tr></thead>\n    <tbody>\n']
    for d, kw, gt, lt in spec:
        out.append(f'    <tr><td style="vertical-align:middle"><b>{d}</b></td>'
                   f'<td style="vertical-align:middle">{ds.sketch_parabola(**kw)}</td>'
                   f'<td style="vertical-align:middle"><div>{gt[0]}</div><div>{gt[1]}</div></td>'
                   f'<td style="vertical-align:middle"><div>{lt[0]}</div><div>{lt[1]}</div></td>'
                   '</tr>\n')
    out.append('    </tbody>\n  </table>\n')
    return ''.join(out)


def _fig45(kw, cap4, cap5):
    return ('  <table class="d-tbl"><tr>\n'
            f'    <td style="width:42%;vertical-align:middle">{ds.sketch_parabola(**kw)}</td>\n'
            f'    <td style="vertical-align:middle"><div>{cap4}</div>'
            f'<div style="margin-top:8px">{cap5}</div></td>\n'
            '  </tr></table>\n')


def _teacher_notes():
    rows = [
        ('本份採用的主設計', 'D2 手順卡（五步）'),
        ('輔助設計', 'D5 圖文雙軌對照（草圖 ↔ 解集逐列對齊）、D12 自我核對清單'),
        ('選用理由',
         '本課屬 S2 多步驟程序運算（序列崩潰、漏「乘負數要反向」）疊 S4 函數與圖像'
         '（圖象與解集的對應無法內化）。瓶頸在前端的程序序列，故主設計取 D2；'
         '草圖是本課判斷解集的唯一依據，故 D5 升為輔助之首，並把「畫草圖」'
         '獨立成手順卡第 4 步，使它成為不可跳過的動作。'),
        ('鷹架密度', '全班共用'),
        ('褪除路徑',
         '本份紙面上已經做出三級：練習A 每題重印 ①②③ 提示 → 練習B 只在區塊開頭放'
         '一次共用提示 → 練習C 完全不放。（草圖框三層都保留：畫草圖是本課的核心動作，'
         '不是鷹架。）下一課起草圖框也撤走，只問「這題的草圖長什麼樣」→ '
         '最後連手順卡一併移除。'),
        ('課堂實施流程',
         'F1 師徒制對話四步（老師畫一次草圖、學生說出取哪一邊）、'
         'F2 番茄鐘分段（A／B／C 三段，每段末的自我核對清單就是收口，段間有核對點）'),
        ('對應官方輔助措施代碼', 'a3 提示題目重點、a6 增加行距、b5 提供步驟提示卡'),
        ('與教學簡報的對應',
         '簡報_L8_一元二次不等式 用的是「四步走」；本份把「畫草圖」由第 3 步拆出來'
         '獨立成第 4 步，共五步。簡報只處理兩個相異實根，本份補回 Δ＝0、Δ＜0 兩種'
         '情況（見第三節）——上課用簡報帶完四步後，用本份第三節補這兩欄。'),
    ]
    body = ''.join(f'      <tr><td style="width:28%;background:#f0f0f0;font-weight:700">{k}</td>'
                   f'<td>{v}</td></tr>\n' for k, v in rows)
    return ('  <div class="teacher-notes page-break">\n'
            '    <div class="section-h">教師實施說明（本頁供教師參考，列印給學生時可不印）</div>\n'
            '    <table class="d-tbl long">\n' + body + '    </table>\n  </div>\n')


# ================================================================ 練習
def _q(no, stem, hint=None, n_lines=5):
    """一題。hint=None 時右側欄只剩空白草圖框——這就是 D2 的褪除梯度：
    A 每題重印提示、B 只在區塊開頭放一次、C 不放（teaching-designs.md D2）。
    草圖框三層都保留，因為「每題都要畫草圖」是本課的核心動作，不是鷹架。"""
    side = sketch(blank=True, caption='草圖畫這裡')
    if hint:
        side += hintcard(hint)
    return aside(f'      <div><b>{no}．</b>{stem}</div>\n' + '  ' + lines(n_lines), side)


def build_exercise():
    B = [masthead('課堂練習')]
    B.append(p('忘記做法就先回頭看《…課堂講義》第四節的五步手順卡。'
               '每題都要畫草圖——畫得出草圖，範圍就挑得中。'))

    B.append(h('一、練習A（<span class="stars">★☆☆</span>）—— 先求根，再照草圖挑範圍'))
    B.append(_q(1, r'求不等式 \((x-1)(x-4) \gt 0\) 的解集。',
                ['① 已經分解好，直接讀出兩個根', r'② 開口向上（\(a=1\)）',
                 '③ 問 ＞ 0 → 取兩邊']))
    B.append(_q(2, r'求不等式 \(x^2-x-6 \lt 0\) 的解集。',
                ['① 先因式分解求根', '② 開口向上', '③ 問 ＜ 0 → 取中間']))
    B.append(_q(3, r'求不等式 \(x^2-7x+10 \gt 0\) 的解集。',
                ['① 先因式分解求根', '② 開口向上', '③ 問 ＞ 0 → 取兩邊']))
    B.append(selfcheck(CHECK_A, '練習A 做完，先自己核對一次'))
    B.append(checkpoint())

    # B、C 不強制分頁：練習A 三題剛好填滿第 1 頁，硬分頁會把核對清單＋核對點
    # 單獨丟到一頁上（實測第 2 頁只有 3 行、其餘全白）。改讓內容自然流。
    B.append(h('二、練習B（<span class="stars">★★☆</span>）—— 根不一定有兩個'))
    B.append(shaded('這一區的題目不一定有兩個根。每題先算 \\(\\Delta\\)：'
                    '\\(\\Delta \\gt 0\\) 兩個根、\\(\\Delta = 0\\) 一個根、'
                    '\\(\\Delta \\lt 0\\) 沒有根——草圖跟著變，解集也跟著變。'))
    B.append(_q(4, r'求不等式 \(x^2-6x+9 \le 0\) 的解集。'))
    B.append(_q(5, r'求不等式 \(x^2-2x+5 \gt 0\) 的解集。'))
    B.append(_q(6, r'求不等式 \(2x^2-3x-2 \lt 0\) 的解集。'))
    B.append(selfcheck(CHECK_B, '練習B 做完，先自己核對一次'))
    B.append(checkpoint())

    B.append(h('三、練習C（<span class="stars">★★★</span>）—— a 是負數、以及應用題'))
    B.append(_q(7, r'求不等式 \(-x^2+3x+4 \gt 0\) 的解集。'))
    B.append(_q(8, r'求不等式 \(x^2-4x+4 \gt 0\) 的解集。'))
    B.append(_q(9, r'一個球向上拋出，\(t\) 秒後的高度是 \(h=16t-t^2\)（公尺）。'
                   '問在哪一段時間內，球的高度超過 60 公尺？', n_lines=6))
    B.append(selfcheck(CHECK_C, '練習C 做完，先自己核對一次'))

    B.append(h('教師用參考答案', brk=True))
    for t in _ANSWERS:
        B.append(problem(''.join(p(x) for x in t)))

    out = os.path.join(BASE, '練習_二次函數與一元二次不等式_融合版.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(page('練習_二次函數與一元二次不等式_融合版', ''.join(B)))
    return out


_ANSWERS = [
    [r'<b>A1</b>　\((x-1)(x-4)=0\) → \(x_1=1\) 或 \(x_2=4\)；\(a \gt 0\) 開口向上，問 ＞ 0 取兩邊',
     r'<b>∴ 解集為 \(\{x \mid x \lt 1\) 或 \(x \gt 4\}\)</b>'],
    [r'<b>A2</b>　\(x^2-x-6=(x+2)(x-3)\)；令它等於 0 → \(x_1=-2\) 或 \(x_2=3\)；問 ＜ 0 取中間',
     r'<b>∴ 解集為 \(\{x \mid -2 \lt x \lt 3\}\)</b>'],
    [r'<b>A3</b>　\(x^2-7x+10=(x-2)(x-5)\)；令它等於 0 → \(x_1=2\) 或 \(x_2=5\)；問 ＞ 0 取兩邊',
     r'<b>∴ 解集為 \(\{x \mid x \lt 2\) 或 \(x \gt 5\}\)</b>'],
    [r'<b>B4</b>　\(\Delta=36-36=0\)，重根 \(x=3\)（即 \((x-3)^2 \le 0\)）；'
     r'開口向上，只有頂點碰到 x 軸',
     r'\((x-3)^2\) 永遠 \(\ge 0\)，所以「\(\le 0\)」只在頂點成立',
     r'<b>∴ 解集為 \(\{x \mid x=3\}\)</b>'],
    [r'<b>B5</b>　\(\Delta=4-20=-16 \lt 0\)，沒有實根；\(a=1 \gt 0\) 開口向上，整條在 x 軸上方',
     r'<b>∴ 解集為 \(\{x \mid x\) 是任何實數\(\}\)</b>'],
    [r'<b>B6</b>　\(2x^2-3x-2=(2x+1)(x-2)\)；令它等於 0 → \(x_1=-\frac{1}{2}\) 或 \(x_2=2\)；'
     r'\(a=2 \gt 0\)，問 ＜ 0 取中間',
     r'<b>∴ 解集為 \(\{x \mid -\frac{1}{2} \lt x \lt 2\}\)</b>'],
    [r'<b>C7</b>　\(a=-1 \lt 0\)，整條乘 −1 並把不等號反向：\(x^2-3x-4 \lt 0\)',
     r'\((x+1)(x-4)=0\) → \(x_1=-1\) 或 \(x_2=4\)；問 ＜ 0 取中間',
     r'<b>∴ 解集為 \(\{x \mid -1 \lt x \lt 4\}\)</b>'],
    [r'<b>C8</b>　\(\Delta=16-16=0\)，重根 \(x=2\)（即 \((x-2)^2 \gt 0\)）；'
     r'開口向上，只有頂點碰到 x 軸',
     r'除了 \(x=2\) 那一點之外，其餘每一點都在 x 軸上方',
     r'<b>∴ 解集為 \(\{x \mid x \ne 2\}\)</b>'],
    [r'<b>C9</b>　\(16t-t^2 \gt 60\) → 搬到一邊：\(-t^2+16t-60 \gt 0\) → '
     r'乘 −1 並反向：\(t^2-16t+60 \lt 0\)',
     r'\((t-6)(t-10)=0\) → \(t_1=6\) 或 \(t_2=10\)；問 ＜ 0 取中間',
     r'<b>∴ 解集為 \(\{t \mid 6 \lt t \lt 10\}\)</b>，即第 6 秒到第 10 秒之間'],
]


if __name__ == '__main__':
    for fn in (build_handout, build_exercise):
        print(fn())
