# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from html_helpers import *

SUBJECT = '高一數學'
UNIT = '集合的基本運算'
SVG_DIR = os.path.join(os.path.dirname(__file__), 'svgs')

union_svg = read_svg(os.path.join(SVG_DIR, 'union.svg'))
inter_svg = read_svg(os.path.join(SVG_DIR, 'intersection.svg'))
comp_svg = read_svg(os.path.join(SVG_DIR, 'complement.svg'))
onlyA_svg = read_svg(os.path.join(SVG_DIR, 'onlyA_notB.svg'))

# ================= 講義 =================
lecture = []
lecture.append(page_head(f'{UNIT}．課堂講義'))
lecture.append(masthead(SUBJECT, UNIT, '課堂講義'))
lecture.append(ws_meta())

lecture.append(section_h('一、核心概念'))
lecture.append('<p>1．並集：由所有屬於A或屬於B的元素組成，記作 \\(A \\cup B\\)，即 \\(A \\cup B = \\{x \\mid x \\in A \\text{ 或 } x \\in B\\}\\)。</p>')
lecture.append(f'<div class="diagram">{union_svg}</div>')
lecture.append('<p>2．交集：由所有既屬於A又屬於B的元素組成，記作 \\(A \\cap B\\)，即 \\(A \\cap B = \\{x \\mid x \\in A \\text{ 且 } x \\in B\\}\\)。</p>')
lecture.append(f'<div class="diagram">{inter_svg}</div>')
lecture.append('<p>3．全集與補集：若全集為U，A的補集 \\(\\complement_U A\\) 是U中所有不屬於A的元素組成的集合。</p>')
lecture.append(f'<div class="diagram">{comp_svg}</div>')
lecture.append('<p>4．常用運算性質：\\(A \\cup A = A\\)，\\(A \\cup \\varnothing = A\\)，\\(A \\cap A = A\\)，\\(A \\cap \\varnothing = \\varnothing\\)；\\(A \\cup (\\complement_U A) = U\\)，\\(A \\cap (\\complement_U A) = \\varnothing\\)。</p>')

lecture.append(section_h('二、範例'))
lecture.append('<p>題目：已知全集 U = {1,2,3,4,5,6}，A = {1,2,3}，B = {2,3,4}，求 A∪B、A∩B、\\(\\complement_U(A \\cup B)\\)。</p>')
lecture.append('<div class="worked-example">'
               '<p>① 理解題意：先寫出U、A、B的元素，方便逐一核對。</p>'
               '<p>② 求A∪B：把A、B的元素合併，重複只算一次 → A∪B = {1, 2, 3, 4}。</p>'
               '<p>③ 求A∩B：找出A、B共同的元素 → A∩B = {2, 3}。</p>'
               '<p>④ 求\\(\\complement_U(A \\cup B)\\)：從U中去掉A∪B的元素 → U − {1,2,3,4} = {5, 6}。</p>'
               '</div>')
lecture.append('<p>接下來請拿《集合的基本運算課堂練習》，依這套框架完成練習A、B、C。</p>')
lecture.append(footer(f'{SUBJECT}．{UNIT}　第 1 頁'))
lecture.append(TAIL)

with open(os.path.join(os.path.dirname(__file__), '講義_集合的基本運算.html'), 'w', encoding='utf-8') as f:
    f.write(''.join(lecture))
print('lecture html written')

# ================= 練習 =================
p = []
p.append(page_head(f'{UNIT}．課堂練習'))
p.append(masthead(SUBJECT, UNIT, '課堂練習'))
p.append(ws_meta())
p.append('<p>提示：忘記怎麼做可以先回頭看《集合的基本運算課堂講義》的範例四步驟。</p>')

p.append(section_h(f'一、練習A（{stars(1)}）'))
p.append('<div class="problem">'
    '<p>1．已知 A = {1, 2, 3}，B = {3, 4, 5}。已經幫你抄好A的元素，請把B獨有的元素接著寫完成 A∪B：</p>'
    '<p>A∪B = {1, 2, 3, ____, ____}</p>'
    + write_lines(2) + '</div>')

p.append('<div class="problem">'
    '<p>2．已知 A = {2, 4, 6, 8}，B = {4, 8, 12}。求 A∩B。</p>'
    '<div class="hint-card">提示：交集就是兩個集合「都有」的元素。</div>'
    + write_lines(2) + '</div>')

p.append('<div class="problem">'
    '<p>3．已知 U = {1, 2, 3, 4, 5}，A = {2, 4}。求 \\(\\complement_U A\\)。</p>'
    '<div class="hint-card">提示：把U中不是A的元素挑出來。</div>'
    + write_lines(2) + '</div>')

p.append(section_h(f'二、練習B（{stars(2)}）'))
p.append('<div class="problem">'
    '<p>4．設集合 \\(A = \\{x \\mid -1 &lt; x &lt; 2\\}\\)，\\(B = \\{x \\mid 1 &lt; x &lt; 3\\}\\)，求 A∪B、A∩B。</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>5．已知 U = {1, 2, 3, 4, 5}，A = {1, 2, 3}，B = {2, 3, 4}，求 \\((\\complement_U A) \\cap B\\)。</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>6．已知 U = {1, 2, 3, 4, 5}，A = {1, 2, 3}，B = {2, 3, 4}，如下圖，灰色部分（屬於A但不屬於B）表示的集合是什麼？</p>'
    f'<div class="diagram">{onlyA_svg}</div>'
    + write_lines(2) + '</div>')

p.append(section_h(f'三、練習C（{stars(3)}）'))
p.append('<div class="problem">'
    '<p>7．已知 \\(A = \\{x \\mid x &lt; 1 \\text{ 或 } x &gt; 4\\}\\)，\\(B = \\{x \\mid a \\le x \\le a+2\\}\\)。若 A∩B = ∅，求 a 的取值範圍。（提示：A∩B=∅表示B必須完全落在[1,4]之內）</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>8．請你自己設計兩個用描述法表示的集合 A、B（與不等式有關），使得 \\(A \\cap B = \\{x \\mid 2 &lt; x &lt; 3\\}\\)，並說明你的設計方式。</p>'
    + write_lines(4) + '</div>')

p.append('<div class="problem">'
    '<p>9．已知 A∪B = A。這個等式蘊含 A、B 之間有什麼關係？請說明理由，並舉一個具體例子驗證。</p>'
    + write_lines(4) + '</div>')

p.append(footer(f'{SUBJECT}．{UNIT}　第 1 頁'))

p.append('<div class="page-break">')
p.append(section_h('教師用參考答案'))
p.append('<p>1．A∪B = {1, 2, 3, 4, 5}</p>')
p.append('<p>2．A∩B = {4, 8}</p>')
p.append('<p>3．U中不屬於A(={2,4})的元素為1,3,5，所以 \\(\\complement_U A\\) = {1, 3, 5}</p>')
p.append('<p>4．A∪B = {x | −1 &lt; x &lt; 3}；A∩B = {x | 1 &lt; x &lt; 2}</p>')
p.append('<p>5．\\(\\complement_U A\\) = {4, 5}，再與B={2,3,4}取交集，得 \\((\\complement_U A) \\cap B\\) = {4}</p>')
p.append('<p>6．圖中陰影是屬於A但不屬於B的部分：A中元素{1,2,3}扣掉同時在B中的{2,3}，得 {1}</p>')
p.append('<p>7．A∩B=∅表示B={x|a≤x≤a+2}中所有元素都不在A中，即都落在[1,4]內，所以需要 a≥1 且 a+2≤4，解得 1≤a≤2</p>')
p.append('<p>8．答案不唯一，例如 A={x|x&gt;2}，B={x|x&lt;3}，則 A∩B={x|2&lt;x&lt;3}，恰好符合要求。</p>')
p.append('<p>9．A∪B=A 蘊含 B⊆A（B是A的子集）。例如 A={1,2,3}，B={1,2}，A∪B={1,2,3}=A，且確實 B⊆A。</p>')
p.append(footer(f'{SUBJECT}．{UNIT}　第 2 頁'))
p.append('</div>')
p.append(TAIL)

with open(os.path.join(os.path.dirname(__file__), '練習_集合的基本運算.html'), 'w', encoding='utf-8') as f:
    f.write(''.join(p))
print('practice html written')
