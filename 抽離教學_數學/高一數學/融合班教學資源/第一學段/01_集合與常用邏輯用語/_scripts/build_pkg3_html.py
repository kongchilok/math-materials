# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from html_helpers import *

SUBJECT = '高一數學'
UNIT = '充分條件與必要條件'
SVG_DIR = os.path.join(os.path.dirname(__file__), 'svgs')

impl_svg = read_svg(os.path.join(SVG_DIR, 'implication.svg'))

# ================= 講義 =================
lecture = []
lecture.append(page_head(f'{UNIT}．課堂講義'))
lecture.append(masthead(SUBJECT, UNIT, '課堂講義'))
lecture.append(ws_meta())

lecture.append(section_h('一、核心概念'))
lecture.append('<p>1．命題：可以判斷真假的陳述句。中學數學中的命題常寫成「若p，則q」的形式，p稱為條件，q稱為結論。</p>')
lecture.append('<p>2．若「若p，則q」為真命題（即p成立可以推出q成立），記作 \\(p \\Rightarrow q\\)，這時我們說：p是q的充分條件，q是p的必要條件。</p>')
lecture.append('<p>3．若「若p，則q」為假命題（由p不能推出q，可以舉出一個反例），記作 \\(p \\not\\Rightarrow q\\)，這時p不是q的充分條件，q也不是p的必要條件。</p>')
lecture.append('<p>4．若同時有 \\(p \\Rightarrow q\\) 和 \\(q \\Rightarrow p\\)，則稱p是q的充要條件，記作 \\(p \\Leftrightarrow q\\)。</p>')
lecture.append('<p>5．圖解：若p對應的x所成的集合是P，q對應的x所成的集合是Q，那麼 p⇒q 恰好對應 P⊆Q（回顧1.2節子集的概念）。</p>')
lecture.append(f'<div class="diagram">{impl_svg}</div>')

lecture.append(section_h('二、範例'))
lecture.append('<p>題目：判斷「x = 2」是否為「\\(x^2 = 4\\)」的充分條件？是否為必要條件？</p>')
lecture.append('<div class="worked-example">'
               '<p>① 理解題意：p：「x = 2」，q：「\\(x^2 = 4\\)」。</p>'
               '<p>② 檢驗 p⇒q：x = 2 時，\\(x^2 = 4\\) 成立，所以 p⇒q 為真，p是q的充分條件。</p>'
               '<p>③ 檢驗 q⇒p：\\(x^2 = 4\\) 時，x = 2 或 x = −2，舉反例：x = −2 時 \\(x^2 = 4\\) 成立但 x ≠ 2，所以 q⇏p，p不是q的必要條件。</p>'
               '<p>④ 下結論：p是q的充分不必要條件。</p>'
               '</div>')
lecture.append('<p>接下來請拿《充分條件與必要條件課堂練習》，依這套框架完成練習A、B、C。</p>')
lecture.append(footer(f'{SUBJECT}．{UNIT}　第 1 頁'))
lecture.append(TAIL)

with open(os.path.join(os.path.dirname(__file__), '講義_充分條件與必要條件.html'), 'w', encoding='utf-8') as f:
    f.write(''.join(lecture))
print('lecture html written')

# ================= 練習 =================
p = []
p.append(page_head(f'{UNIT}．課堂練習'))
p.append(masthead(SUBJECT, UNIT, '課堂練習'))
p.append(ws_meta())
p.append('<p>提示：忘記怎麼做可以先回頭看《充分條件與必要條件課堂講義》的範例四步驟。</p>')

p.append(section_h(f'一、練習A（{stars(1)}）'))
p.append('<div class="problem">'
    '<p>1．已知 p：「四邊形是正方形」，q：「四邊形是矩形」。判斷 p⇒q 是否成立？</p>'
    '<p class="indent">成立（　）　不成立（　）</p>'
    '<p>若成立，p是q的什麼條件？<span class="ans-box"></span>條件</p>'
    + write_lines(2) + '</div>')

p.append('<div class="problem">'
    '<p>2．已知 p：「a = 3」，q：「\\(a^2 = 9\\)」。請完成下列判斷：</p>'
    '<p class="indent">p⇒q？　成立（　）　不成立（　）</p>'
    '<p class="indent">q⇒p？　成立（　）　不成立（　）（提示：a = −3 時 a²=9 但 a ≠ 3）</p>'
    '<p>所以p是q的<span class="ans-box"></span>條件。</p>'
    + write_lines(1) + '</div>')

p.append('<div class="problem">'
    '<p>3．判斷下列說法是否正確，正確打✓，錯誤打✗。</p>'
    '<p class="indent">(1) 若p是q的充分條件，則q一定是p的必要條件。　（　）</p>'
    '<p class="indent">(2) 若p⇒q為假，則p一定不是q的充分條件。　（　）</p>'
    + write_lines(1) + '</div>')

p.append(section_h(f'二、練習B（{stars(2)}）'))
p.append('<div class="problem">'
    '<p>4．判斷下列命題中，p是否為q的充分條件：</p>'
    '<p class="indent">(1) 若兩個三角形的三邊成比例，則這兩個三角形相似；</p>'
    '<p class="indent">(2) 若 a = b，則 \\(a^2 = b^2\\)；</p>'
    '<p class="indent">(3) 若 x、y 為無理數，則 x + y 為無理數。</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>5．判斷「a&gt;0 且 b&gt;0」是「a+b&gt;0」的什麼條件？請說明理由。</p>'
    + write_lines(4) + '</div>')

p.append('<div class="problem">'
    '<p>6．判斷「四邊形的對角線互相垂直」是「四邊形是菱形」的什麼條件？請說明理由。</p>'
    + write_lines(4) + '</div>')

p.append(section_h(f'三、練習C（{stars(3)}）'))
p.append('<div class="problem">'
    '<p>7．已知 p：「x∈A」，q：「x∈B」，其中 A⊆B。請用集合包含關係說明為什麼 p 是 q 的充分條件。</p>'
    + write_lines(4) + '</div>')

p.append('<div class="problem">'
    '<p>8．請你自己寫出一個「若p，則q」形式的真命題，並判斷 p 是 q 的充分、必要或充要條件，說明理由。</p>'
    + write_lines(4) + '</div>')

p.append('<div class="problem">'
    '<p>9．已知 p 是 q 的必要不充分條件，且 q 是 r 的充要條件。請問 p 與 r 之間有什麼關係？請舉一個具體例子說明。</p>'
    + write_lines(5) + '</div>')

p.append(footer(f'{SUBJECT}．{UNIT}　第 1 頁'))

p.append('<div class="page-break">')
p.append(section_h('教師用參考答案'))
p.append('<p>1．成立。p是q的充分條件（正方形一定是矩形）。</p>')
p.append('<p>2．p⇒q成立；q⇒p不成立（a=−3時a²=9但a≠3）。所以p是q的充分不必要條件。</p>')
p.append('<p>3．(1) ✓　(2) ✓</p>')
p.append('<p>4．(1) 是（三邊成比例是三角形相似的判定定理，p⇒q為真）(2) 是（等式性質，a=b可推出a²=b²）(3) 不是（舉反例：x=√2，y=−√2，x+y=0為有理數，p⇏q）</p>')
p.append('<p>5．充分不必要條件。a&gt;0且b&gt;0時a+b&gt;0成立(充分)；但a+b&gt;0不代表a、b都&gt;0，例如a=3,b=−1時a+b=2&gt;0但b&lt;0(不必要)。</p>')
p.append('<p>6．必要不充分條件。菱形的對角線一定互相垂直(必要)；但對角線互相垂直的四邊形不一定是菱形，例如某些風箏形(不充分)。</p>')
p.append('<p>7．因為A⊆B，A中每個元素都在B中，所以只要x∈A，就一定有x∈B，即p成立能推出q成立，p⇒q為真，故p是q的充分條件。</p>')
p.append('<p>8．答案不唯一，例如「若x&gt;2，則x&gt;1」，p⇒q為真(x&gt;2一定x&gt;1)，但q⇒p不成立(x=1.5&gt;1但不&gt;2)，所以p是q的充分不必要條件。</p>')
p.append('<p>9．p是q的必要不充分條件，即q⇒p（但p⇏q）；q是r的充要條件，即q⇔r。合併可得 r⇒q⇒p，所以 r⇒p，即p是r的必要條件。例如：設q「x是4的倍數」，r「x=4k，k為整數」（與q等價），p「x是偶數」。則q⇒p成立但p⇏q（如x=2是偶數但不是4的倍數），且q⇔r。驗證：r成立時x是4的倍數，一定是偶數，即r⇒p成立，與推論相符。</p>')
p.append(footer(f'{SUBJECT}．{UNIT}　第 2 頁'))
p.append('</div>')
p.append(TAIL)

with open(os.path.join(os.path.dirname(__file__), '練習_充分條件與必要條件.html'), 'w', encoding='utf-8') as f:
    f.write(''.join(p))
print('practice html written')
