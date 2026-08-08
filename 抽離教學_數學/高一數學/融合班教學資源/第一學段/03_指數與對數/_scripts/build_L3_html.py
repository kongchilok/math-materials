# -*- coding: utf-8 -*-
"""高一 4.2 指數函數 融合版：講義／練習／工具卡 三份 HTML（→ PDF 正式列印版）。

內容與 build_L3_docx.py 一一對應（同名元件兩版外觀必須一致）。

HTML 版專屬地雷（house-style 實測記錄，兩版要分開驗）：
  ① 數學式內不准有裸 `<` `>`，一律寫 \\lt \\gt——否則瀏覽器當成標籤，吞走成段。
  ② LaTeX 一律用 raw string 寫，否則 `\\right` 的 \\r 變回車，MathJax 整條渲染失敗。
  ③ 內嵌 SVG 要保留 width／height 屬性，少了它 <img> 尺寸變 0。
  ④ 頁尾用 <tfoot> 逐頁重印（會佔位），不用 position:fixed（不佔位、會遮字）。
"""
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
FIGS = os.path.join(OUT, '_figs')

SUBJ, UNIT = '高一數學', '4.2 指數函數'
FOOT = '高一數學．4.2 指數函數'

CSS_EXTRA = """
  /* 工具卡成品頁：格線＝虛線裁切線，剪下護貝放桌面 */
  .toolcards { width: 100%; border-collapse: collapse; margin-top: 10px; }
  .toolcards td { border: 1px dashed #666; padding: 12px 14px; width: 50%;
                  vertical-align: top; break-inside: avoid; }
  .toolcards .ct { font-size: 14pt; font-weight: 700; margin-bottom: 3px; }
  .toolcards .cg { font-size: 10.5pt; color: #444; margin-bottom: 6px; }
  .toolcards .cl { font-size: 11.5pt; margin: 3px 0; }
  .toolcards .cs { font-size: 12pt; font-weight: 700; margin-top: 8px; }
  /* 兩張卡並排，觸發語行數唔同會令兩幅圖高度唔一致——鎖死觸發語區塊高度 */
  .toolcards .cghead { min-height: 3.6em; }
  .def-box { border: 0.75pt solid #000; padding: 8px 12px; margin: 10px 0;
             break-inside: avoid; }
  .def-box .dt { font-weight: 700; }
  .def-box .df { text-align: center; margin: 8px 0; }
  .cap-line { font-size: 10.5pt; color: #555; margin-top: 2px; }
  /* 側欄鎖死闊度：唔鎖死嘅話，兩題嘅左主欄闊度唔同，
     作答橫線長度就會一題長一題短（實測 490pt vs 760pt） */
  .aside-side { flex: 0 0 40%; width: 40%; }
  /* 題幹／小題懸掛縮排：換行後唔會頂到左邊界，對齊返小題編號 */
  .q { padding-left: 1.7em; text-indent: -1.7em; margin: 2px 0; }

  /* ⚠⚠ 用 `>` 子選擇器鎖住 design_svg 嗰啲插圖 —— 千祈唔好寫 `.aside-side svg`
     或者 `.toolcards svg` 咁樣嘅後代選擇器：MathJax 嘅 SVG 輸出本身就係
     <mjx-container><svg>…</svg></mjx-container>，後代選擇器會連每一條公式一齊命中。
     實測後果：`.toolcards svg{display:block;margin:auto}` 令工具卡每條公式變成
     獨立置中一行，成句觸發語畀切成 6 截；`.aside-side svg{width:100%}` 令提示框入面
     嗰條 2⁻¹=1/2¹ 放大到 26pt（本文 4 倍），成個灰底框爆晒版。
     插圖係 .aside-side／td 嘅直屬子元素，公式唔係——所以 `>` 分得開。 */
  .aside-side > svg { width: 100%; height: auto; }
  .toolcards td > svg { max-width: 100%; height: auto; display: block;
                        margin: 6px auto; }
  /* 再加一層保險：任何情況下都唔准改動 MathJax 自己嗰個 svg 嘅尺寸同流向 */
  mjx-container > svg { width: auto; height: auto; max-width: none;
                        display: inline; margin: 0; }

  /* 工具卡得一頁，tfoot 會緊貼內容尾——撐高內容格等頁尾落到頁底 */
  .onepage > tbody > tr > td { height: 26.5cm; }
"""


def svg(name):
    """內嵌 design_svg 產的 SVG（保留自帶 width/height，否則尺寸變 0）。"""
    with io.open(os.path.join(FIGS, f'{name}.svg'), encoding='utf-8') as f:
        return f.read()


def wl(n):
    return ('<div class="write-lines">'
            + '<div class="line"></div>' * n + '</div>')


def hintcard(title, lines):
    body = ''.join(f'<div>{t}</div>' for t in lines)
    return f'<div class="hintcard"><div class="ht">{title}</div>{body}</div>'


def aside(main, side):
    return ('<div class="aside-wrap boxed">'
            f'<div class="aside-main">{main}</div>'
            f'<div class="aside-side">{side}</div></div>')


# ── 範例段：七小欄，等號上下對齊成一條垂直線 ──────────────────────
def eqrow(lhs, rhs, why, rel=r'='):
    return (f'<tr><td class="ec1">\\({lhs}\\)</td><td class="ec2">\\({rel}\\)</td>'
            f'<td class="ec3">\\({rhs}\\)</td><td class="ec4"></td><td class="ec5"></td>'
            f'<td class="ec6"></td><td class="ec7"></td><td class="why">{why}</td></tr>')


def orrow(l1, r1, l2, r2, why, rel=r'='):
    return (f'<tr><td class="ec1">\\({l1}\\)</td><td class="ec2">\\({rel}\\)</td>'
            f'<td class="ec3">\\({r1}\\)</td><td class="ec4">或</td>'
            f'<td class="ec5">\\({l2}\\)</td><td class="ec6">\\({rel}\\)</td>'
            f'<td class="ec7">\\({r2}\\)</td><td class="why">{why}</td></tr>')


def spanrow(text, why, ans=False):
    cls = 'ecs ans' if ans else 'ecs'
    return (f'<tr><td class="{cls}" colspan="7">{text}</td>'
            f'<td class="why">{why}</td></tr>')


def worked(title, rows):
    return (f'<div class="section-h lead">{title}</div>'
            # 唔加 .long：短範例表要整張推落下一頁，唔可以由中間切開——
            # 一切開，等號就唔再對齊成一條垂直線（D5／書寫規範的命根）
            '<table class="d-tbl worked">'
            '<thead><tr><th colspan="7">算式</th><th>這一步在做什麼</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>')


def page(title, doc_type, body, sheet_cls=''):
    return f"""<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<script>
  MathJax = {{
    tex: {{ inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] }},
    svg: {{ fontCache: 'local', displayAlign: 'left', displayIndent: '0',
           mtextInheritFont: true }},
    options: {{ enableMenu: false }}
  }};
</script>
<script>
(function loadMathJax(urls) {{
  if (!urls.length) return;
  var s = document.createElement('script');
  s.src = urls[0];
  s.onerror = function () {{ loadMathJax(urls.slice(1)); }};
  document.head.appendChild(s);
}})([
  'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-svg.js',
  'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js',
  'https://unpkg.com/mathjax@3/es5/tex-mml-svg.js'
]);
</script>
<style>
{BASE_CSS}
{CSS_EXTRA}
</style>
</head>
<body>
<table class="sheet {sheet_cls}">
  <tfoot><tr><td><div class="footer">{FOOT}</div></td></tr></tfoot>
  <tbody><tr><td>

  <div class="masthead"><span>科目：{SUBJ}</span><span>單元：{UNIT}</span><span>類型：{doc_type}</span></div>
{body}

  </td></tr></tbody>
</table>
</body>
</html>
"""


META = ('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
        '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
        '日期：<span class="u">&nbsp;</span></div>')

# CSS 由範本原樣抄過來（不要為了「好看」自行改字體／配色／格線寫法）
with io.open(os.path.join(
        r'C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator',
        'assets', 'worksheet-template.html'), encoding='utf-8') as f:
    _tpl = f.read()
BASE_CSS = _tpl.split('<style>', 1)[1].split('</style>', 1)[0]


# ══════════════════════════════════════════════════════════════════
def handout():
    b = [META]
    b.append('<div class="section-h">一、什麼是指數函數</div>')
    b.append('<div class="def-box"><div class="dt">指數函數的一般式</div>'
             r'<div class="df">\(y = a^{x}\)</div>'
             r'<div>其中 \(a \gt 0\) 且 \(a \ne 1\)，x 可以是任何實數。</div></div>')
    b.append('<div class="hint-card">a 叫做底數（寫在下面），x 叫做指數（寫在上面）。</div>')
    b.append(r'<div class="hint-card">為什麼規定 \(a \gt 0\)？　若 a ＝ −4，'
             r'當 x ＝ 0.5 時 \((-4)^{0.5}\) 就是 −4 的平方根，在實數範圍內沒有意義。</div>')
    b.append(r'<div class="hint-card">為什麼規定 \(a \ne 1\)？　\(1^{x}\) 無論 x 是多少'
             r'都等於 1，畫出來是一條水平直線，不是指數函數。</div>')

    b.append('<div class="section-h">二、兩型指數函數的圖</div>')
    b.append(f'<div class="fig">{svg("two_types")}'
             r'<div class="cap">實線是 \(y = 2^{x}\)（底數大於 1），'
             r'虛線是 \(y = \left(\frac{1}{2}\right)^{x}\)（底數在 0 與 1 之間）。'
             '兩條線都穿過同一點。</div></div>')

    b.append('<div class="section-h">三、圖上看到什麼，算式就寫什麼</div>')
    rows = [
        ('dt_point',
         '<div><b>兩條線都穿過 (0, 1)。</b></div>'
         r'<div>因為 \(a^{0} = 1\)（任何非零數的 0 次方都是 1），</div>'
         '<div>所以不論底數 a 是多少，圖必定經過定點 (0, 1)。</div>'),
        ('dt_above',
         '<div><b>線越向左走越貼近 x 軸，但永遠碰不到。</b></div>'
         r'<div>\(2^{-1} = 0.5\)　\(2^{-2} = 0.25\)　\(2^{-3} = 0.125\)</div>'
         r'<div>值越來越細但不會變成 0，所以值域是 \(y \gt 0\)。</div>'),
        ('dt_inc',
         '<div><b>由左下升到右上：x 每加 1，y 變成 2 倍。</b></div>'
         r'<div>\(2^{0}=1\) → \(2^{1}=2\) → \(2^{2}=4\)</div>'
         r'<div>底數 \(a \gt 1\) 時遞增：x 越大，y 越大。</div>'),
        ('dt_dec',
         '<div><b>由左上跌到右下：x 每加 1，y 減一半。</b></div>'
         r'<div>\(\left(\frac{1}{2}\right)^{0}=1\) → '
         r'\(\left(\frac{1}{2}\right)^{1}=0.5\) → '
         r'\(\left(\frac{1}{2}\right)^{2}=0.25\)</div>'
         r'<div>底數 \(0 \lt a \lt 1\) 時遞減：x 越大，y 越細。</div>'),
    ]
    b.append('<table class="d-tbl dual-track long">'
             '<thead><tr><th>圖形上看到什麼</th><th>算式上寫什麼</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{svg(n)}</td><td>{t}</td></tr>' for n, t in rows)
             + '</tbody></table>')

    b.append(worked(r'四、範例一：不用計算機，比較 \(2^{0.5}\) 與 \(2^{0.3}\) 的大小', [
        spanrow(r'\(y = 2^{x}\)', '兩個數都是 2 的次方，先認出它們屬於同一條線'),
        spanrow(r'底數 \(2 \gt 1\)', '對照第三節第三列：a &gt; 1 型 → 遞增'),
        eqrow(r'0.5', r'0.3', '先比指數（x）誰大', rel=r'\gt'),
        eqrow(r'2^{0.5}', r'2^{0.3}', '遞增：x 大的，y 也大', rel=r'\gt'),
        spanrow(r'\(\therefore 2^{0.5} \gt 2^{0.3}\)',
                '作答：最後一行用「∴」寫出結論', ans=True),
    ]))

    b.append(worked('五、範例二：已知圖經過 (2, 9)，求底數 a', [
        spanrow('把點 (2, 9) 代入', '「圖經過某點」就是把該點坐標代入函數式'),
        eqrow(r'a^{2}', r'9', '得到一條關於 a 的方程'),
        orrow(r'a', r'3', r'a', r'-3', '兩邊開平方，分成兩支寫'),
        spanrow(r'底數規定 \(a \gt 0\)', '所以 a ＝ −3 要捨去（底數不能是負數）'),
        spanrow(r'\(3 \gt 1\)', '對照第三節第三列：a &gt; 1 型 → 遞增'),
        spanrow(r'\(\therefore a = 3\)，圖由左下升到右上',
                '作答：最後一行用「∴」寫出答案', ans=True),
    ]))

    b.append('<div class="section-h">六、這一課最容易錯的三個位</div>')
    d14 = [
        (r'\(y = 2^{x}\) 的值域是所有實數。',
         '※ 差在這裡：圖永遠在 x 軸上方，取不到 0 也取不到負數。',
         r'值域是 \(y \gt 0\)。'),
        (r'\(y = 1^{x}\) 都算是指數函數。',
         r'※ 差在這裡：定義規定 \(a \ne 1\)。',
         r'\(1^{x} = 1\) 畫出來是一條水平直線，不是指數函數。'),
        (r'\(a^{0} = 0\)，所以圖經過 (0, 0)。',
         '※ 差在這裡：任何非零數的 0 次方都等於 1。',
         r'\(a^{0} = 1\)，所以圖經過 (0, 1)。'),
    ]
    b.append('<table class="d-tbl dual-track long">'
             '<thead><tr><th>常見寫法</th><th>正確寫法</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{a}</td>'
                       f'<td><div class="hint-card"><div>{m}</div>'
                       f'<div><b>{c}</b></div></div></td></tr>'
                       for a, m, c in d14)
             + '</tbody></table>')

    b.append('<p>　接下來請拿《課堂練習——4.2 指數函數》，'
             '依照上面「圖上看到什麼、算式就寫什麼」這套框架，完成練習 A、B、C。</p>')

    tn = [
        ('本份採用的主設計', 'D5 圖文雙軌對照'),
        ('輔助設計', 'D7 提示卡（另出《工具卡_4.2指數函數》：指數圖像卡兩型）、'
                     'D14 錯誤分析對比（第六節，對應簡報 L3 第 9 頁三個易錯位）'),
        ('選用理由', '數學結構 S4「函數與圖像」，核心瓶頸是「底數 a ↔ 圖形走勢」的'
                     '對應建立不起來；D5 把左邊的圖與右邊的算式逐列橫向對齊，'
                     '學生每看懂圖上一件事，立刻在同一列看到它寫成什麼算式。'),
        ('鷹架密度', '抽離小班（A／B／C 各 2 題、作答空間標準＋1 行、出工具卡）'),
        ('褪除路徑',
         'D5：練習A 圖已給、只需讀圖填答 → 練習B 只給算式，圖由學生自己描點畫出 → '
         '練習C 圖與式皆不給，學生自己決定要不要畫草圖。<br>'
         'D7 圖像卡：教案第 1 節先發 a &gt; 1 型 → 第 2 節補齊兩型 → '
         '第 3 課（4.3 反函數）起收起卡片，改為口頭提問「這條是哪一型」→ 測考不帶入。<br>'
         'D14：第一次見到三欄對比 → 之後只給「常見寫法」一欄要學生自己改正 → '
         '最後只問一句「這題有一個常見陷阱，是什麼」。'),
        ('課堂實施流程', 'F5 課前流程預告（配合簡報 L3 第 2 頁的四件事）、'
                         'F4 過程導向回饋：比大小題把「認出型」與「比指數」分開給分'),
        ('對應官方輔助措施代碼', 'a3 提示題目重點（指數圖像卡）、a6 增加行距／放大作答欄、'
                                 'a7 調整計分標準（步驟分）'),
    ]
    b.append('<div class="teacher-notes">'
             '<div class="section-h">教師實施說明（本頁供教師參考，列印給學生時可不印）</div>'
             '<table class="d-tbl long">'
             + ''.join(f'<tr><td>{k}</td><td>{v}</td></tr>' for k, v in tn)
             + '</table></div>')
    return page(f'講義_{UNIT}_融合版', '課堂講義', '\n'.join(b))


# ══════════════════════════════════════════════════════════════════
def practice():
    b = [META]
    b.append('<p>　做之前先翻開《課堂講義——4.2 指數函數》第三節，'
             '照「圖上看到什麼、算式就寫什麼」那張表的方法做。</p>')

    b.append('<div class="section-h">一、練習A（<span class="stars">★☆☆</span>）</div>')
    b.append(aside(
        r'<div class="q">1．右圖是 \(y = 3^{x}\) 的圖。</div>'
        '<div class="q">（a）這條線與 y 軸交在哪一點？</div>'
        '<div class="q">（b）由左至右，這條線是升還是跌？</div>'
        '<div class="q">（c）填空：x 越大，y 越＿＿＿＿。</div>' + wl(4),
        svg('p_3x') + hintcard('讀圖三步', [
            '① 先看這條線在 y 軸上的高度',
            '② 底數 3 ＞ 1，對照講義第三節哪一列',
            '③ 用手指由左行到右，看是上還是下'])))

    b.append(aside(
        r'<div class="q">2．右圖是 \(y = \left(\frac{1}{3}\right)^{x}\) 的圖。</div>'
        '<div class="q">（a）f(0) ＝ ＿＿＿＿</div>'
        '<div class="q">（b）這條線會不會碰到 x 軸？</div>'
        r'<div class="q">（c）這個函數的值域是＿＿＿＿（填 \(y \gt 0\) 或「y 是所有實數」）</div>' + wl(4),
        svg('p_1_3x') + hintcard('讀圖三步', [
            '① f(0) 就是 x ＝ 0 時的 y',
            '② 看線的左右兩端與 x 軸的距離',
            '③ 值域＝這條線的 y 可以取到哪些數'])))

    b.append('<div class="section-h">二、練習B（<span class="stars">★★☆</span>）</div>')
    b.append(aside(
        r'<div class="q">3．已知 \(y = 2^{x}\)。</div>'
        '<div class="q">（a）計算下面四個 y 值：</div>'
        '<div>　　x ＝ −1 時，y ＝ ＿＿＿＿＿＿</div>'
        '<div>　　x ＝ 0 時，　y ＝ ＿＿＿＿＿＿</div>'
        '<div>　　x ＝ 1 時，　y ＝ ＿＿＿＿＿＿</div>'
        '<div>　　x ＝ 2 時，　y ＝ ＿＿＿＿＿＿</div>'
        '<div class="q">（b）把這四點畫在右邊的坐標格上，再連成一條平滑曲線。</div>'
        '<div class="q">（c）這條線經過哪一個定點？</div>' + wl(4),
        svg('p_blank') + hintcard('作圖三步', [
            r'① 負指數：\(2^{-1} = \frac{1}{2^{1}}\)',
            '② 先描點，再由左至右連線',
            '③ 定點看 x ＝ 0 那一點'])))

    b.append('<div class="problem">'
             r'<div class="q">4．在下面每題的橫線上填 ＞ 或 ＜，並寫出你用了哪一型'
             r'（\(a \gt 1\) 還是 \(0 \lt a \lt 1\)）。</div>'
             r'<div class="q">　（a）\(3^{1.2}\)　＿＿＿＿　\(3^{0.7}\)</div>'
             r'<div class="q">　（b）\(\left(\frac{1}{2}\right)^{1.5}\)　＿＿＿＿　'
             r'\(\left(\frac{1}{2}\right)^{0.9}\)</div>'
             '<div class="q">　（c）任揀一題，畫一條草圖說明你的判斷。</div>' + wl(6) + '</div>')

    b.append('<div class="section-h">三、練習C（<span class="stars">★★★</span>）</div>')
    b.append('<div class="problem">'
             r'<div class="q">5．已知指數函數 \(y = a^{x}\) 的圖經過點 (3, 8)。</div>'
             '<div class="q">　（a）求 a。</div>'
             '<div class="q">　（b）判斷這條線是升還是跌，並寫出理由。</div>'
             r'<div class="q">　（c）不用計算機，比較 \(a^{0.4}\) 與 \(a^{0.6}\) 誰大，並寫出理由。</div>'
             + wl(7) + '</div>')
    b.append('<div class="problem">'
             r'<div class="q">6．小明說：「\(y = a^{x}\) 的圖一定是由左下升到右上。」</div>'
             '<div>　你同意嗎？請自己畫一張草圖，並寫出理由；</div>'
             '<div>　若不同意，請舉出一個反例。</div>' + wl(7) + '</div>')

    ans = [
        ('1（a）', r'(0, 1)。因為 \(3^{0} = 1\)。'),
        ('1（b）', r'升（遞增）。底數 \(3 \gt 1\)。'),
        ('1（c）', '越大。'),
        ('2（a）', r'\(f(0) = \left(\frac{1}{3}\right)^{0} = 1\)'),
        ('2（b）', '不會。線越向右走越貼近 x 軸，但 y 永遠大於 0。'),
        ('2（c）', r'\(y \gt 0\)'),
        ('3（a）', r'x ＝ −1 時 \(y = \frac{1}{2}\)；x ＝ 0 時 y ＝ 1；'
                  'x ＝ 1 時 y ＝ 2；x ＝ 2 時 y ＝ 4。'),
        ('3（b）', r'四點為 \(\left(-1, \frac{1}{2}\right)\)、(0, 1)、(1, 2)、(2, 4)，'
                  '連成由左下升到右上的平滑曲線。'),
        ('3（c）', '(0, 1)。'),
        ('4（a）', r'＞。底數 \(3 \gt 1\) 屬 \(a \gt 1\) 型（遞增）；\(1.2 \gt 0.7\)，'
                  r'所以 \(3^{1.2} \gt 3^{0.7}\)。'),
        ('4（b）', r'＜。底數 \(\frac{1}{2}\) 屬 \(0 \lt a \lt 1\) 型（遞減）；'
                  r'\(1.5 \gt 0.9\)，指數大反而值細，'
                  r'所以 \(\left(\frac{1}{2}\right)^{1.5} \lt '
                  r'\left(\frac{1}{2}\right)^{0.9}\)。'),
        ('4（c）', '草圖只需一條 x 軸、一條曲線與 (0, 1)：(a) 畫升型，(b) 畫跌型；'
                  '在線上標出兩個指數對應的高度即可。'),
        ('5（a）', r'\(a^{3} = 8\)，所以 \(a = 2\)。'),
        ('5（b）', r'升（遞增）。因為 \(2 \gt 1\)，屬 \(a \gt 1\) 型。'),
        ('5（c）', r'\(2^{0.4} \lt 2^{0.6}\)。遞增：指數大的，值也大，而 \(0.4 \lt 0.6\)。'),
        ('6', r'不同意。當 \(0 \lt a \lt 1\) 時圖是由左上跌到右下。'
              r'反例：\(y = \left(\frac{1}{2}\right)^{x}\)，x 越大 y 越細。'
              '草圖：過 (0, 1)、在 x 軸上方、由左上跌向右下。'),
    ]
    b.append('<div class="page-break"><div class="section-h">參考答案（教師用）</div>'
             + ''.join(f'<div>{k}　{v}</div>' for k, v in ans) + '</div>')
    return page(f'練習_{UNIT}_融合版', '課堂練習', '\n'.join(b))


# ══════════════════════════════════════════════════════════════════
def toolcard():
    def card(title, trigger, egs, png, lines, symbol):
        # 觸發語拆兩行。mjx-container 係 inline-block，內部斷唔到行——
        # 一行塞四條公式，喺 9cm 窄卡度會逐條被擠落新行，整句讀唔成句（實測）。
        li = ''.join(f'<div class="cl">{t}</div>' for t in lines)
        return (f'<div class="ct">▍{title}</div>'
                f'<div class="cghead">'
                f'<div class="cg">什麼時候翻我：{trigger}</div>'
                f'<div class="cg">　例如　{egs}</div></div>'
                f'{svg(png)}{li}<div class="cs">{symbol}</div>')

    up = card('指數圖像卡（a ＞ 1 型）',
              r'題目出現 \(y = a^{x}\)，而底數 \(a \gt 1\)',
              r'\(2^{x}\)　\(3^{x}\)　\(10^{x}\)',
              'card_up',
              ['① 圖必過定點 (0, 1)',
               r'② 全條線在 x 軸上方：\(y \gt 0\)',
               '③ 由左下升到右上：x 越大，y 越大'],
              r'\(a \gt 1\) → 遞增')
    down = card('指數圖像卡（0 ＜ a ＜ 1 型）',
                r'題目出現 \(y = a^{x}\)，而底數 \(0 \lt a \lt 1\)',
                r'\(\left(\frac{1}{2}\right)^{x}\)　'
                r'\(\left(\frac{1}{3}\right)^{x}\)　\(0.4^{x}\)',
                'card_down',
                ['① 圖必過定點 (0, 1)',
                 r'② 全條線在 x 軸上方：\(y \gt 0\)',
                 '③ 由左上跌到右下：x 越大，y 越細'],
                r'\(0 \lt a \lt 1\) → 遞減')

    b = ['<p>　沿虛線剪開。教案第 1 節先發左邊「a ＞ 1 型」，'
         '第 2 節補發右邊「0 ＜ a ＜ 1 型」，兩張並排貼在桌面。</p>',
         '<table class="toolcards">'
         f'<tr><td>{up}</td><td>{down}</td></tr>'
         '</table>']
    return page(f'工具卡_{UNIT}', '工具卡（剪下護貝，放在桌面）', '\n'.join(b),
                sheet_cls='onepage')


if __name__ == '__main__':
    jobs = [('講義_4.2指數函數_融合版.html', handout()),
            ('練習_4.2指數函數_融合版.html', practice()),
            ('工具卡_4.2指數函數.html', toolcard())]
    for name, html in jobs:
        p = os.path.join(OUT, name)
        with io.open(p, 'w', encoding='utf-8') as f:
            f.write(html)
        print('OK', name)
