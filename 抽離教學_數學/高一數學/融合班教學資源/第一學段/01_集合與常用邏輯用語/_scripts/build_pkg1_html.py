# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from html_helpers import *

SUBJECT = '高一數學'
UNIT = '集合的概念與基本關係'
SVG_DIR = os.path.join(os.path.dirname(__file__), 'svgs')

subset_svg = read_svg(os.path.join(SVG_DIR, 'subset.svg'))

# ================= 講義 =================
lecture = []
lecture.append(page_head(f'{UNIT}．課堂講義'))
lecture.append(masthead(SUBJECT, UNIT, '課堂講義'))
lecture.append(ws_meta())

lecture.append(section_h('一、核心概念'))
lecture.append('<p>1．集合的三要素：確定性（元素是或不是，必須清楚）、互異性（同一集合中元素不重複）、無序性（元素排列先後不影響集合本身）。</p>')
lecture.append('<p>2．元素與集合的關係：若 a 是集合 A 的元素，記作 \\(a \\in A\\)（讀作「屬於」）；若不是，記作 \\(a \\notin A\\)。</p>')
lecture.append('<p>3．常用數集符號：N（自然數集，含0）、N+ 或 N*（正整數集）、Z（整數集）、Q（有理數集）、R（實數集）。</p>')
lecture.append('<p>4．集合的表示法：</p>')
lecture.append('<p class="indent">列舉法：把元素一一列出，例如 \\(\\{1, 2, 3\\}\\)。</p>')
lecture.append('<p class="indent">描述法：用「元素所滿足的條件」描述，例如 \\(\\{x \\in \\mathbb{R} \\mid x &gt; 1\\}\\)。</p>')
lecture.append('<p>5．集合間的基本關係：</p>')
lecture.append('<p class="indent">子集 \\(A \\subseteq B\\)：A中每一個元素都屬於B。</p>')
lecture.append('<p class="indent">真子集 \\(A \\subsetneq B\\)：\\(A \\subseteq B\\) 且 A ≠ B（B中至少有一個元素不在A中）。</p>')
lecture.append('<p class="indent">相等 A = B：\\(A \\subseteq B\\) 且 \\(B \\subseteq A\\)。</p>')
lecture.append('<p class="indent">規定：空集 ∅ 是任何集合的子集。</p>')
lecture.append(f'<div class="diagram">{subset_svg}</div>')

lecture.append(section_h('二、範例'))
lecture.append('<p>題目：已知集合 \\(A = \\{x \\in \\mathbb{N} \\mid x &lt; 4\\}\\)，B = {0, 1, 2, 3, 4}，判斷 A 與 B 的關係，並用列舉法表示 A。</p>')
lecture.append('<div class="worked-example">'
               '<p>① 理解題意：A是「小於4的自然數」全體，先確定範圍。</p>'
               '<p>② 列舉A：A = {0, 1, 2, 3}。</p>'
               '<p>③ 逐一比對：A中每個元素（0,1,2,3）都在B中；但B多了元素4，不在A中。</p>'
               '<p>④ 下結論：A⊆B 且 A≠B，所以 A⊊B（A是B的真子集）。</p>'
               '</div>')
lecture.append('<p>接下來請拿《集合的概念與基本關係課堂練習》，依這套框架完成練習A、B、C。</p>')
lecture.append(footer(f'{SUBJECT}．{UNIT}　第 1 頁'))
lecture.append(TAIL)

with open(os.path.join(os.path.dirname(__file__), '講義_集合的概念與基本關係.html'), 'w', encoding='utf-8') as f:
    f.write(''.join(lecture))
print('lecture html written')

# ================= 練習 =================
p = []
p.append(page_head(f'{UNIT}．課堂練習'))
p.append(masthead(SUBJECT, UNIT, '課堂練習'))
p.append(ws_meta())
p.append('<p>提示：忘記怎麼做可以先回頭看《集合的概念與基本關係課堂講義》的範例四步驟。</p>')

p.append(section_h(f'一、練習A（{stars(1)}）'))
p.append('<div class="problem">'
    '<p>1．下列哪些敘述「能」組成集合？請在能／不能中打勾。</p>'
    '<p class="indent">(1) 全班身高超過170公分的同學　　能（　）　不能（　）</p>'
    '<p class="indent">(2) 很聰明的同學　　能（　）　不能（　）</p>'
    '<p class="indent">(3) 1到5之間的偶數　　能（　）　不能（　）</p>'
    '<div class="hint-card">提示：能組成集合的關鍵是「元素確定」——能不能明確判斷「誰在裡面、誰不在」。</div>'
    + write_lines(1) + '</div>')

p.append('<div class="problem">'
    '<p>2．集合 \\(\\{x \\in \\mathbb{N}^+ \\mid x &lt; 5\\}\\) 用列舉法表示為 {1, 2, ____, ____}，請填出缺少的兩個數。</p>'
    '<div class="hint-card">提示：N+表示正整數（1,2,3,…），由小到大排列。</div>'
    + write_lines(2) + '</div>')

p.append('<div class="problem">'
    '<p>3．判斷下列敘述是否正確，正確打✓，錯誤打✗。</p>'
    '<p class="indent">(1) 3 ∈ {1, 2, 3, 4}　（　）</p>'
    '<p class="indent">(2) 0 ∈ ∅　（　）</p>'
    '<p class="indent">(3) {1, 2} ⊆ {1, 2, 3}　（　）</p>'
    + write_lines(1) + '</div>')

p.append(section_h(f'二、練習B（{stars(2)}）'))
p.append('<div class="problem">'
    '<p>4．用適當的方法（列舉法或描述法）表示下列集合：</p>'
    '<p class="indent">(1) 所有能被3整除的整數；</p>'
    '<p class="indent">(2) 方程 \\(x^2 - 5x + 6 = 0\\) 的解集。</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>5．已知集合 M = {−2, 0, 2}，N = {x ∈ Z | −3 &lt; x &lt; 3}，判斷 M 與 N 的關係，並說明理由。</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>6．寫出集合 {a, b}（a ≠ b）的所有子集，共有幾個？</p>'
    + write_lines(3) + '</div>')

p.append(section_h(f'三、練習C（{stars(3)}）'))
p.append('<div class="problem">'
    '<p>7．已知集合 \\(A = \\{x \\mid x^2 - 3x + 2 = 0\\}\\)，B = {1, a}。若 A = B，求 a 的值。（先求出A的元素，再比較）</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>8．請你自己寫出一個集合 A（元素個數不少於3個），並寫出它的其中兩個「真」子集，說明為什麼它們是A的真子集而不是A本身。</p>'
    + write_lines(4) + '</div>')

p.append('<div class="problem">'
    '<p>9．探索規律：集合{1}有2個子集，集合{1,2}有4個子集，集合{1,2,3}有8個子集。</p>'
    '<p class="indent">(1) 猜想：一個有 n 個元素的集合，子集個數共有多少個？</p>'
    '<p class="indent">(2) 請用集合 {1,2,3,4} 驗證你的猜想（列出所有子集或說明理由）。</p>'
    + write_lines(4) + '</div>')

p.append(footer(f'{SUBJECT}．{UNIT}　第 1 頁'))

p.append('<div class="page-break">')
p.append(section_h('教師用參考答案'))
p.append('<p>1．(1) 能　(2) 不能（「聰明」標準不確定）　(3) 能</p>')
p.append('<p>2．{1, 2, 3, 4}</p>')
p.append('<p>3．(1) ✓　(2) ✗（∅沒有任何元素）　(3) ✓</p>')
p.append('<p>4．(1) {x ∈ Z | x是3的倍數}　(2) 解 (x−2)(x−3)=0，得 x=2 或 x=3，解集為 {2, 3}</p>')
p.append('<p>5．N = {−2, −1, 0, 1, 2}。M中每個元素（−2,0,2）都在N中，但N還有−1、1不在M中，所以 M ⊊ N（M是N的真子集）。</p>')
p.append('<p>6．子集共4個：∅、{a}、{b}、{a, b}。</p>')
p.append('<p>7．先解 x²−3x+2=0 得 (x−1)(x−2)=0，x=1或2，所以 A={1,2}。由 A=B 得 B={1,2}，比對 B={1,a}，得 a=2。</p>')
p.append('<p>8．答案不唯一，能自圓其說即可，例如 A={1,2,3}，真子集 {1}、{1,2} 都是A的真子集，因為它們是A的子集且都不等於A本身。</p>')
p.append('<p>9．(1) 猜想：2的n次方個（2ⁿ）。(2) {1,2,3,4}的子集共 2⁴=16 個：∅、{1}、{2}、{3}、{4}、{1,2}、{1,3}、{1,4}、{2,3}、{2,4}、{3,4}、{1,2,3}、{1,2,4}、{1,3,4}、{2,3,4}、{1,2,3,4}，驗證共16個，與猜想相符。</p>')
p.append(footer(f'{SUBJECT}．{UNIT}　第 2 頁'))
p.append('</div>')
p.append(TAIL)

with open(os.path.join(os.path.dirname(__file__), '練習_集合的概念與基本關係.html'), 'w', encoding='utf-8') as f:
    f.write(''.join(p))
print('practice html written')
