# -*- coding: utf-8 -*-
r"""單元 04 講義／練習 HTML（→PDF 正式列印版）。

⚠ 全檔的 LaTeX 一律寫成 raw string（r'...'）——普通字串會把 \r（\right）
   變成回車字元，MathJax 靜默渲染失敗、PDF 印出 ight)^2。
⚠ 數學式內不准出現裸 < >，一律 \lt \gt（瀏覽器會當成 HTML 標籤吞掉整段）。
"""
import os
import re

SKILL_ASSETS = (r'C:\Users\KongChiLok\.claude\skills'
                r'\inclusive-math-worksheet-generator\assets\worksheet-template.html')
BASE = os.path.dirname(os.path.abspath(__file__))
FOOT = '初三數學．分式方程、無理方程與二元二次方程組'

# 直接沿用範本的 head+CSS（house-style 唯一真相），只換 title
with open(SKILL_ASSETS, encoding='utf-8') as f:
    _tpl = f.read()
HEAD = _tpl[:_tpl.index('</head>') + len('</head>')]


def page(title, body):
    head = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', HEAD, count=1)
    return (head + '\n<body>\n<table class="sheet">\n'
            f'  <tfoot><tr><td><div class="footer">{FOOT}</div></td></tr></tfoot>\n'
            '  <tbody><tr><td>\n' + body +
            '\n  </td></tr></tbody>\n</table>\n</body>\n</html>\n')


def masthead(doc_type):
    return ('  <div class="masthead"><span>科目：初三數學</span>'
            '<span>單元：分式方程、無理方程與二元二次方程組</span>'
            f'<span>類型：{doc_type}</span></div>\n'
            '  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
            '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
            '日期：<span class="u">&nbsp;</span></div>\n')


def h(t):
    return f'  <div class="section-h">{t}</div>\n'


def p(t):
    return f'  <div>{t}</div>\n'


def lines(n):
    return ('  <div class="write-lines">' + '<div class="line"></div>' * n
            + '</div>\n')


def problem(inner):
    return f'  <div class="problem">\n{inner}  </div>\n'


def shaded(t):
    return f'  <div class="hint-card">{t}</div>\n'


# ---------------- 範例表（house-style 七小欄） ----------------
def eqrow(lhs, rhs, why=''):
    return (f'    <tr><td class="ec1">\\({lhs}\\)</td><td class="ec2">\\(=\\)</td>'
            f'<td class="ec3" colspan="5">\\({rhs}\\)</td>'
            f'<td class="why">{why}</td></tr>\n')


def orrow(l1, r1, l2, r2, why=''):
    return (f'    <tr><td class="ec1">\\({l1}\\)</td><td class="ec2">\\(=\\)</td>'
            f'<td class="ec3">\\({r1}\\)</td><td class="ec4">或</td>'
            f'<td class="ec5">\\({l2}\\)</td><td class="ec6">\\(=\\)</td>'
            f'<td class="ec7">\\({r2}\\)</td>'
            f'<td class="why">{why}</td></tr>\n')


def spanrow(t, why='', ans=False):
    cls = 'ecs ans' if ans else 'ecs'
    return (f'    <tr><td class="{cls}" colspan="7">{t}</td>'
            f'<td class="why">{why}</td></tr>\n')


def ansrow(t, why='作答：最後一行用「∴」寫出答案'):
    return spanrow(r'\(\therefore\) ' + t, why, ans=True)


def worked(lead, rows):
    return (f'  <div class="sub-h lead"><b>{lead}</b></div>\n'
            '  <table class="d-tbl worked long">\n'
            '    <thead><tr><th colspan="7">算式</th>'
            '<th class="why">這一步在做什麼</th></tr></thead>\n'
            '    <tbody>\n' + ''.join(rows) + '    </tbody>\n  </table>\n')


# ---------------- D2 手順卡 ----------------
def step_card(title, trigger, steps, compact=False):
    out = ['  <table class="d-tbl step-card">\n',
           f'    <tr><th colspan="2">{title}</th></tr>\n']
    if not compact:
        out.append('    <tr><td colspan="2" style="font-weight:400">'
                   f'什麼時候用：{trigger}</td></tr>\n')
    for i, (act, pit) in enumerate(steps, 1):
        if compact:
            out.append(f'    <tr><td colspan="2">{i}. {act}</td></tr>\n')
        else:
            out.append(f'    <tr><td>{i}. {act}</td>'
                       f'<td class="pitfall">※ {pit}</td></tr>\n')
    out.append('  </table>\n')
    return ''.join(out)


# ---------------- D12 自我核對 ----------------
def selfcheck(items, title='做完先自己核對一次'):
    body = ''.join(f'    <div>☐ {t}</div>\n' for t in items)
    return (f'  <div class="selfcheck">\n    <div><b>{title}</b></div>\n'
            + body + '  </div>\n')


def checkpoint():
    return ('  <div class="checkpoint">【核對點】做到這裡先停，'
            '對照上面的清單檢查一次再往下</div>\n')


# ================================================================ 手順卡資料
CARD_FRAC = ('分式方程 四步', '方程裡有分母，而且分母含有未知數', [
    ('把每個分母因式分解，找出最簡公分母',
     r'分母是 \(x^2-4\) 要先拆成 \((x+2)(x-2)\)'),
    ('兩邊同乘最簡公分母，去分母', '每一項都要乘，包括沒有分母的那一項'),
    ('解這條整式方程', '照一元二次方程的做法：移項、因式分解、分兩支'),
    ('驗根：把每個解代回原方程的分母', '令分母等於 0 的叫增根，一定要捨去'),
])

CARD_SURD = ('無理方程 四步', '未知數被關在根號裡面', [
    ('移項，讓根號單獨留在一邊', '根號要孤立，才能一次平方掉'),
    ('兩邊平方，去根號',
     r'右邊是整體平方：\((x-3)^2\) 不等於 \(x^2-9\)'),
    ('解這條整式方程', '照一元二次方程的做法：移項、因式分解、分兩支'),
    ('驗根：把每個解代回原方程', '平方會多出假根；左右不相等的一定要捨去'),
])

CARD_SYS = ('二元二次方程組 四步', '兩條方程、兩個未知數，其中一條是二次', [
    ('找出那條一次方程', '一次方程才好用來「用一個字母表示另一個」'),
    ('從一次方程解出一個未知數', r'例如寫成 \(y=x+1\)，準備代入'),
    ('代入二次方程，解出第一個未知數', '代入後只剩一個字母，就變回熟悉的一元二次方程'),
    ('每個解都要回代，求出另一個未知數',
     r'答案要成對寫：有幾個 \(x\) 就有幾對 \((x,y)\)'),
])


# ================================================================ 講義
def build_handout():
    B = [masthead('課堂講義')]

    B.append(h('這一課要學三種新方程'))
    B.append(p('前面學過的一元二次方程，未知數都是「光著身」的。'
               '這一課的三種方程，未知數分別被關在三個地方：'))
    B.append(problem(
        p(r'分母裡　→　分式方程　　例：\(\dfrac{3}{x}=x-2\)')
        + p(r'根號裡　→　無理方程　　例：\(\sqrt{x+2}=x\)')
        + p(r'另一條方程裡　→　二元二次方程組　　例：\(y=x+1\) 與 \(x^2+y^2=25\)')))
    B.append(p('三種方程的做法都是同一個念頭：'))
    B.append(shaded('想辦法把未知數「放出來」，變回會解的一元二次方程。'))
    B.append(p('但放出來是有代價的——'))
    B.append(shaded('去分母、平方，這兩個動作都可能多生出「假的解」。'
                    '所以這一課每一題最後都要驗根。'))

    # 一、分式方程
    B.append(h('一、分式方程'))
    B.append(step_card(*CARD_FRAC))
    B.append(worked(r'★ 範例一：解 \(\dfrac{3}{x}=x-2\)', [
        eqrow(r'\dfrac{3}{x}', r'x-2',
              r'原方程。分母有 \(x\)，所以先寫低 \(x \neq 0\)'),
        spanrow(r'最簡公分母是 \(x\)', '分母只有一個，最簡公分母就是它'),
        eqrow(r'3', r'x(x-2)', r'兩邊同乘 \(x\)，去分母'),
        eqrow(r'3', r'x^2-2x', '展開右邊'),
        eqrow(r'x^2-2x-3', r'0', '移項，化成一般式'),
        eqrow(r'(x-3)(x+1)', r'0', '因式分解'),
        orrow(r'x-3', r'0', r'x+1', r'0', '兩個因式各自等於 0，分兩支寫'),
        orrow(r'x_1', r'3', r'x_2', r'-1', '兩支各自解出'),
        spanrow(r'驗根 \(x_1=3\)：代入分母 \(x\) 得 \(3\)', '不等於 0，保留'),
        spanrow(r'驗根 \(x_2=-1\)：代入分母 \(x\) 得 \(-1\)', '不等於 0，保留'),
        ansrow(r'\(x_1 = 3\)　或　\(x_2 = -1\)', '作答：最後一行用「∴」寫出兩個根'),
    ]))

    # 二、無理方程
    B.append(h('二、無理方程'))
    B.append(step_card(*CARD_SURD))
    B.append(worked(r'★ 範例二：解 \(\sqrt{x+2}=x\)', [
        eqrow(r'\sqrt{x+2}', r'x', '原方程。根號已經單獨在左邊，可以直接平方'),
        eqrow(r'x+2', r'x^2', '兩邊平方，去根號'),
        eqrow(r'x^2-x-2', r'0', '移項，化成一般式'),
        eqrow(r'(x-2)(x+1)', r'0', '因式分解'),
        orrow(r'x-2', r'0', r'x+1', r'0', '兩個因式各自等於 0，分兩支寫'),
        orrow(r'x_1', r'2', r'x_2', r'-1', '兩支各自解出'),
        spanrow(r'驗根 \(x_1=2\)：左邊 \(\sqrt{2+2}=2\)，右邊 \(2\)',
                '左右相等，保留'),
        spanrow(r'驗根 \(x_2=-1\)：左邊 \(\sqrt{-1+2}=1\)，右邊 \(-1\)',
                '根號算出來一定不是負數，左右不相等，捨去'),
        ansrow(r'\(x = 2\)', '作答：只有一個根通過驗根，就只寫一個'),
    ]))

    # 三、方程組
    B.append(h('三、二元二次方程組'))
    B.append(step_card(*CARD_SYS))
    B.append(worked(r'★ 範例三：解方程組 \(y=x+1\)　與　\(x^2+y^2=25\)', [
        spanrow(r'已知：\(y=x+1\)（一次）　與　\(x^2+y^2=25\)（二次）',
                r'一次那條已經解好 \(y\)，可以直接代入'),
        eqrow(r'x^2+(x+1)^2', r'25', r'把 \(y\) 換成 \(x+1\)，代入二次方程'),
        eqrow(r'x^2+x^2+2x+1', r'25', r'展開 \((x+1)^2\)'),
        eqrow(r'2x^2+2x-24', r'0', '移項，合併同類項'),
        eqrow(r'x^2+x-12', r'0', '兩邊除以 2，數字變細'),
        eqrow(r'(x-3)(x+4)', r'0', '因式分解'),
        orrow(r'x-3', r'0', r'x+4', r'0', '兩個因式各自等於 0，分兩支寫'),
        orrow(r'x_1', r'3', r'x_2', r'-4', r'兩支各自解出 \(x\)'),
        orrow(r'y_1', r'4', r'y_2', r'-3', r'回代 \(y=x+1\)：這一步最容易漏'),
        ansrow(r'\((x_1,y_1)=(3,4)\)　或　\((x_2,y_2)=(-4,-3)\)',
               '作答：方程組的答案要成對寫'),
    ]))

    # 四、D14 錯誤分析
    B.append(h('四、這一課最容易錯的一步'))
    B.append(p('下面兩欄，前三行一模一樣，分歧在第四行。'))
    B.append(p(r'<b>題目：解 \(\dfrac{2}{x-3}=\dfrac{x-1}{x-3}\)</b>'))
    B.append('  <table class="d-tbl dual-track">\n'
             '    <tr><th>常見寫法</th><th>正確寫法</th></tr>\n'
             r'    <tr><td>兩邊乘 \((x-3)\)，去分母</td>'
             r'<td style="background:#f0f0f0">兩邊乘 \((x-3)\)，去分母</td></tr>'
             '\n'
             r'    <tr><td>\(2=x-1\)</td>'
             r'<td style="background:#f0f0f0">\(2=x-1\)</td></tr>' '\n'
             r'    <tr><td>\(x=3\)</td>'
             r'<td style="background:#f0f0f0">\(x=3\)</td></tr>' '\n'
             r'    <tr><td>答：\(x=3\)</td>'
             r'<td style="background:#f0f0f0">※ 驗根：\(x=3\) 令分母 \(x-3=0\)，'
             r'分式沒有意義 → 增根，捨去</td></tr>' '\n'
             '    <tr><td></td>'
             '<td style="background:#f0f0f0"><b>∴ 原方程無解</b></td></tr>\n'
             '  </table>\n')
    B.append(shaded('※ 差在這裡：解出來的數字一定要代回分母檢查。'
                    '令分母等於 0 的數叫「增根」，它不是原方程的解。'))

    B.append(h('接下來'))
    B.append(p('請拿本單元的《課堂練習》，照上面三張手順卡完成練習 A、B、C。'
               '做每一題時，把對應的那張手順卡放在旁邊，手指指住你正在做的那一步。'))

    # 教師頁
    B.append('  <div class="teacher-notes">\n')
    B.append(h('教師實施說明（本頁供教師參考，列印給學生時可不印）'))
    tn = [
        ('本份採用的主設計', 'D2 手順卡（日本特別支援教育小步子原則）'),
        ('輔助設計', 'D12 自我核對清單＋分段結構、D14 錯誤分析對比（正誤雙欄）'),
        ('選用理由',
         '本單元三個子題（分式方程／無理方程／二元二次方程組）全部屬 S2 多步驟程序運算，'
         '核心瓶頸是序列性步驟在工作記憶中崩潰、漏步驟。三種方程的步驟不同但都是固定序列，'
         '正是手順卡的標準適用情境。輔助設計對準本單元唯一的高頻固定錯法——漏驗根／不捨增根：'
         'D12 把「驗根了嗎」變成可自我判定的核對項，D14 把增根從隱性錯誤變成可指認的對象。'),
        ('鷹架密度', '抽離小班（Tier 2）'),
        ('褪除路徑',
         '第一輪：三張手順卡完整給，練習 A 每題旁重印精簡步驟號。'
         '第二輪：手順卡只留「※ 驗根」一句，練習 B 只在區塊開頭放一次。'
         '第三輪：只問「這題有幾步」，練習 C 不放任何步驟提示。'
         '第四輪：完全移除，改由學生自己在草稿上先寫四步再動筆。'),
        ('課堂實施流程',
         'F1 師徒制對話四步（我做→我們做→你做→你教我）、'
         'F2 番茄鐘分段：每完成一個區塊停下來對自我核對清單'),
        ('對應官方輔助措施代碼',
         'a3 提示題目重點、a5 分段作答、a6 增加行距／放大作答欄、b5 可使用計算機'),
        ('工具卡',
         '本單元另出《工具卡_三種方程手順卡》，三張卡剪下護貝後放桌面，解題時手指實時跟蹤。'),
    ]
    B.append('  <table class="d-tbl long">\n' + ''.join(
        f'    <tr><td>{k}</td><td>{v}</td></tr>\n' for k, v in tn) + '  </table>\n')
    B.append('  </div>\n')

    out = os.path.join(BASE, '講義_分式方程無理方程與二元二次方程組_融合版.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(page('講義_分式方程無理方程與二元二次方程組_融合版', ''.join(B)))
    return out


# ================================================================ 練習
def build_exercise():
    B = [masthead('課堂練習')]
    B.append(p('做題之前，先回頭看《課堂講義》的三個範例，'
               '並把《工具卡》的三張手順卡放在桌面。'))

    # ---- 練習A
    B.append(h('一、練習A（<span class="stars">★☆☆</span>）'))
    B.append(p('每題旁邊都印了步驟號，跟著填。'))

    B.append(problem(
        p(r'<b>1．解分式方程 \(\dfrac{4}{x}=x-3\)</b>')
        + p('（步驟 1）最簡公分母是 <span class="ans-box"></span>')
        + p(r'（步驟 2）兩邊乘最簡公分母，去分母，得 \(4=x(x-3)\)')
        + p(r'（步驟 3）展開、移項，得 \(x^2-3x-4=0\)')
        + p(r'　　　　　因式分解，得 \((x-4)(x+1)=0\)')
        + p(r'　　　　　分兩支：\(x_1\) ＝ <span class="ans-box"></span>'
            r'　或　\(x_2\) ＝ <span class="ans-box"></span>')
        + p(r'（步驟 4）驗根：把兩個解代入分母 \(x\)，'
            r'都不等於 <span class="ans-box"></span>，所以都保留')
        + p('<b>∴ </b>') + lines(2)))

    B.append(problem(
        p(r'<b>2．解無理方程 \(\sqrt{x+3}=x-3\)</b>')
        + p('（步驟 1）根號已經單獨在左邊，可以直接平方')
        + p(r'（步驟 2）兩邊平方，得 \(x+3=x^2-6x+9\)')
        + p(r'（步驟 3）移項，得 \(x^2-7x+6=0\)')
        + p(r'　　　　　因式分解，得 \((x-1)(x-6)=0\)')
        + p(r'　　　　　分兩支：\(x_1\) ＝ <span class="ans-box"></span>'
            r'　或　\(x_2\) ＝ <span class="ans-box"></span>')
        + p('（步驟 4）驗根——這題一定有一個要捨：')
        + p(r'　　　\(x=1\)：左 ＝ <span class="ans-box"></span>，'
            r'右 ＝ <span class="ans-box"></span>　　☐ 相等　☐ 不相等')
        + p(r'　　　\(x=6\)：左 ＝ <span class="ans-box"></span>，'
            r'右 ＝ <span class="ans-box"></span>　　☐ 相等　☐ 不相等')
        + p('<b>∴ </b>') + lines(2)))

    B.append(problem(
        p(r'<b>3．解方程組 \(y=x-1\)　與　\(x^2+y^2=13\)</b>')
        + p(r'（步驟 1、2）一次方程已經解好 \(y\)，可以直接代入')
        + p(r'（步驟 3）代入，得 \(x^2+(x-1)^2=13\)')
        + p(r'　　　　　展開、整理、兩邊除以 2，得 \(x^2-x-6=0\)')
        + p(r'　　　　　因式分解，得 \((x-3)(x+2)=0\)')
        + p(r'　　　　　分兩支：\(x_1\) ＝ <span class="ans-box"></span>'
            r'　或　\(x_2\) ＝ <span class="ans-box"></span>')
        + p(r'（步驟 4）回代 \(y=x-1\)：\(y_1\) ＝ <span class="ans-box"></span>'
            r'　或　\(y_2\) ＝ <span class="ans-box"></span>')
        + p('<b>∴ </b>') + lines(2)))

    B.append(selfcheck([
        '每題都寫出了步驟 1 到步驟 4，沒有跳步',
        '去分母／平方之後，每一項都處理過了',
        '每個解都代回原方程（或分母）檢查過',
        '最後一行用「∴」寫了答句',
    ]))
    B.append(checkpoint())

    # ---- 練習B
    B.append(h('二、練習B（<span class="stars">★★☆</span>）'))
    B.append(p('這一區塊的步驟提示只放這一次，做題時自己回想。'))
    # 褪除版：三張手順卡合成一張三欄對照表。三張獨立卡會被分頁切開，
    # 學生要翻回上一頁看提示（QA 實測），併成一張既省版面又能橫向比較。
    cards = (CARD_FRAC, CARD_SURD, CARD_SYS)
    tbl = ['  <table class="d-tbl">\n    <tr>'
           + ''.join(f'<th>{c[0]}</th>' for c in cards) + '</tr>\n']
    for i in range(4):
        tbl.append('    <tr>' + ''.join(
            f'<td>{i + 1}. {c[2][i][0]}</td>' for c in cards) + '</tr>\n')
    tbl.append('  </table>\n')
    B.append(''.join(tbl))

    B.append(problem(
        p(r'<b>4．解分式方程 \(\dfrac{x}{x-2}-\dfrac{3}{x}=1\)</b>') + lines(6)))
    B.append(problem(
        p(r'<b>5．解無理方程 \(\sqrt{2x+1}=x-1\)</b>') + lines(6)))
    B.append(problem(
        p(r'<b>6．解方程組 \(x+y=5\)　與　\(xy=6\)</b>') + lines(6)))

    B.append(selfcheck([
        '驗根是寫在紙上的，不是心裡想一想就跳過',
        '捨去的根有寫明為什麼捨（令分母為 0／左右不相等）',
        '方程組的答案成對寫，每個 x 都配了對應的 y',
        '最後一行用「∴」寫了答句',
    ]))
    B.append(checkpoint())

    # ---- 練習C
    B.append(h('三、練習C（<span class="stars">★★★</span>）'))

    B.append(problem(
        p('<b>7．甲、乙兩地相距 30 公里。小明騎單車從甲地到乙地，比開車多用 1 小時。'
          '已知開車速度是單車速度的 3 倍，求單車的速度。</b>')
        + p('<span style="font-size:11pt">（先寫「設……」，再列方程）</span>')
        + lines(7)))

    B.append(problem(
        p(r'<b>8．找錯題：小美解無理方程 \(\sqrt{x+6}=x\)，過程如下——</b>')
        + p(r'　　兩邊平方，得 \(x+6=x^2\)')
        + p(r'　　整理，得 \(x^2-x-6=0\)')
        + p(r'　　因式分解，得 \((x-3)(x+2)=0\)')
        + p(r'　　所以 \(x=3\) 或 \(x=-2\)')
        + p('（一）小美漏了哪一步？') + lines(2)
        + p('（二）正確答案是什麼？請寫出完整過程。') + lines(5)))

    B.append(problem(
        p('<b>9．請你自己出一條分式方程，要求：解整式方程後會得到兩個數，'
          '但其中一個是增根、必須捨去。</b>')
        + p('（一）寫出你的方程') + lines(2)
        + p('（二）寫出完整解法（包括驗根）') + lines(5)
        + p('（三）用一句話說明那個數為什麼要捨去') + lines(2)))

    B.append(selfcheck([
        '應用題有寫「設 x 是什麼」，而且答案有寫單位',
        '算出的答案代回題目情境檢查過，合乎現實',
        '找錯題有明確指出是哪一步漏了',
        '最後一行用「∴」寫了答句',
    ]))

    # ---- 答案
    B.append('  <div class="page-break"></div>\n')
    B.append(h('參考答案（教師用）'))

    B.append(p('<b>練習A</b>'))
    B.append(worked(r'1．解 \(\dfrac{4}{x}=x-3\)', [
        eqrow(r'4', r'x(x-3)', r'兩邊乘 \(x\)'),
        eqrow(r'x^2-3x-4', r'0', '移項'),
        orrow(r'x-4', r'0', r'x+1', r'0', '因式分解，分兩支'),
        orrow(r'x_1', r'4', r'x_2', r'-1', '解出兩支'),
        spanrow(r'驗根：\(4 \neq 0\)，\(-1 \neq 0\)', '兩根都保留'),
        ansrow(r'\(x_1 = 4\)　或　\(x_2 = -1\)'),
    ]))
    B.append(worked(r'2．解 \(\sqrt{x+3}=x-3\)', [
        eqrow(r'x+3', r'x^2-6x+9', '兩邊平方'),
        eqrow(r'x^2-7x+6', r'0', '移項'),
        orrow(r'x-1', r'0', r'x-6', r'0', '因式分解，分兩支'),
        orrow(r'x_1', r'1', r'x_2', r'6', '解出兩支'),
        spanrow(r'驗根 \(x=1\)：左 \(\sqrt{4}=2\)，右 \(-2\)', '不相等，捨去'),
        spanrow(r'驗根 \(x=6\)：左 \(\sqrt{9}=3\)，右 \(3\)', '相等，保留'),
        ansrow(r'\(x = 6\)'),
    ]))
    B.append(worked(r'3．解 \(y=x-1\) 與 \(x^2+y^2=13\)', [
        eqrow(r'x^2+(x-1)^2', r'13', '代入'),
        eqrow(r'x^2-x-6', r'0', '展開、整理、除以 2'),
        orrow(r'x-3', r'0', r'x+2', r'0', '因式分解，分兩支'),
        orrow(r'x_1', r'3', r'x_2', r'-2', r'解出 \(x\)'),
        orrow(r'y_1', r'2', r'y_2', r'-3', r'回代 \(y=x-1\)'),
        ansrow(r'\((3,2)\)　或　\((-2,-3)\)'),
    ]))

    B.append(p('<b>練習B</b>'))
    B.append(worked(r'4．解 \(\dfrac{x}{x-2}-\dfrac{3}{x}=1\)', [
        spanrow(r'最簡公分母 \(x(x-2)\)', r'限制 \(x \neq 0\) 且 \(x \neq 2\)'),
        eqrow(r'x^2-3(x-2)', r'x(x-2)', r'兩邊乘 \(x(x-2)\)'),
        eqrow(r'x^2-3x+6', r'x^2-2x', '展開'),
        eqrow(r'6', r'x', r'消去 \(x^2\)，移項'),
        spanrow(r'驗根：\(6 \neq 0\)，\(6-2=4 \neq 0\)', '保留'),
        ansrow(r'\(x = 6\)', '註：此題降為一次，只有一個解'),
    ]))
    B.append(worked(r'5．解 \(\sqrt{2x+1}=x-1\)', [
        eqrow(r'2x+1', r'x^2-2x+1', '兩邊平方'),
        eqrow(r'x^2-4x', r'0', '移項'),
        orrow(r'x', r'0', r'x-4', r'0', '因式分解，分兩支'),
        orrow(r'x_1', r'0', r'x_2', r'4', '解出兩支'),
        spanrow(r'驗根 \(x=0\)：左 \(\sqrt{1}=1\)，右 \(-1\)', '不相等，捨去'),
        spanrow(r'驗根 \(x=4\)：左 \(\sqrt{9}=3\)，右 \(3\)', '相等，保留'),
        ansrow(r'\(x = 4\)'),
    ]))
    B.append(worked(r'6．解 \(x+y=5\) 與 \(xy=6\)', [
        eqrow(r'y', r'5-x', r'從一次方程解出 \(y\)（用代入消元，不用韋達定理）'),
        eqrow(r'x(5-x)', r'6', '代入'),
        eqrow(r'x^2-5x+6', r'0', '整理'),
        orrow(r'x-2', r'0', r'x-3', r'0', '因式分解，分兩支'),
        orrow(r'x_1', r'2', r'x_2', r'3', r'解出 \(x\)'),
        orrow(r'y_1', r'3', r'y_2', r'2', r'回代 \(y=5-x\)'),
        ansrow(r'\((2,3)\)　或　\((3,2)\)'),
    ]))

    B.append(p('<b>練習C</b>'))
    B.append(worked('7．應用題', [
        spanrow(r'設單車速度為 \(x\) km/h（\(x \gt 0\)），開車速度 \(3x\) km/h',
                '先設未知數'),
        eqrow(r'\dfrac{30}{x}-\dfrac{30}{3x}', r'1', '單車用時 − 開車用時 ＝ 1 小時'),
        eqrow(r'90-30', r'3x', r'兩邊乘 \(3x\)'),
        eqrow(r'60', r'3x', '左邊相減'),
        eqrow(r'x', r'20', '兩邊除以 3'),
        spanrow(r'驗根：\(20 \neq 0\)，且 \(x \gt 0\) 合乎情境',
                '單車 1.5 小時、開車 0.5 小時，差 1 小時'),
        ansrow('單車的速度是 20 km/h', '應用題答句要寫單位'),
    ]))

    B.append(problem(
        p('<b>8．</b>（一）漏了驗根。兩邊平方是不可逆運算，可能多出不合原方程的根，'
          '每個解都要代回原方程檢查。')
        + p(r'（二）驗根：\(x=3\) 時左 \(\sqrt{9}=3\)、右 \(3\)，相等，保留；'
            r'\(x=-2\) 時左 \(\sqrt{4}=2\)、右 \(-2\)，不相等，捨去。')
        + p(r'<b>∴ \(x=3\)</b>')
        + p('<span style="font-size:11pt">※ 小美前四步的代數運算全部正確，'
            '唯一缺失是驗根。</span>')))

    B.append(problem(
        p('<b>9．</b>學生答案只要符合「有一個增根要捨」即可。參考其中一種：')
        + p(r'方程：\(\dfrac{x^2}{x-1}=\dfrac{1}{x-1}\)')
        + p(r'兩邊乘 \((x-1)\) 得 \(x^2=1\)；移項得 \(x^2-1=0\)；'
            r'因式分解得 \((x-1)(x+1)=0\)；分兩支得 \(x_1=1\) 或 \(x_2=-1\)')
        + p(r'驗根：\(x=1\) 令分母 \(x-1=0\)，增根捨去；'
            r'\(x=-1\) 時分母 \(-1-1=-2\)，不等於 0，保留')
        + p(r'<b>∴ \(x=-1\)</b>')
        + p(r'（三）\(x=1\) 會令原方程的分母等於 0，分式在該處無意義，'
            r'所以它不是原方程的解。')))

    out = os.path.join(BASE, '練習_分式方程無理方程與二元二次方程組_融合版.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(page('練習_分式方程無理方程與二元二次方程組_融合版', ''.join(B)))
    return out


if __name__ == '__main__':
    for fn in (build_handout, build_exercise):
        print(fn())
