# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from html_helpers import *

SUBJECT = '高一數學'
UNIT = '全稱量詞與存在量詞'

# ================= 講義 =================
lecture = []
lecture.append(page_head(f'{UNIT}．課堂講義'))
lecture.append(masthead(SUBJECT, UNIT, '課堂講義'))
lecture.append(ws_meta())

lecture.append(section_h('一、核心概念'))
lecture.append('<p>1．全稱量詞：「所有的」「任意一個」「每一個」等詞，符號記作 ∀。含有全稱量詞的命題叫全稱量詞命題，一般形式為：\\(\\forall x \\in M, p(x)\\)。</p>')
lecture.append('<p>2．存在量詞：「存在一個」「至少有一個」「有些」「有一個」等詞，符號記作 ∃。含有存在量詞的命題叫存在量詞命題，一般形式為：\\(\\exists x \\in M, p(x)\\)。</p>')
lecture.append('<p>3．判斷全稱量詞命題真假：M中每一個x都要驗證p(x)成立，才是真命題；只要找到一個反例（某個x₀使p(x₀)不成立），就是假命題（舉反例法）。</p>')
lecture.append('<p>4．判斷存在量詞命題真假：只要在M中找到一個x使p(x)成立，就是真命題；M中每一個元素都使p(x)不成立，才是假命題。</p>')
lecture.append('<p>5．命題的否定：全稱量詞命題 \\(\\forall x \\in M, p(x)\\) 的否定是存在量詞命題 \\(\\exists x \\in M, \\lnot p(x)\\)；存在量詞命題 \\(\\exists x \\in M, p(x)\\) 的否定是全稱量詞命題 \\(\\forall x \\in M, \\lnot p(x)\\)（換量詞、否定結論）。</p>')

lecture.append(section_h('二、範例'))
lecture.append('<p>題目：判斷全稱量詞命題「所有的素數都是奇數」的真假，並寫出它的否定。</p>')
lecture.append('<div class="worked-example">'
               '<p>① 理解題意：M是「所有素數」，p(x)是「x是奇數」，要判斷 ∀x∈M, p(x) 的真假。</p>'
               '<p>② 舉反例檢驗：2是素數，但2不是奇數，找到反例。</p>'
               '<p>③ 下結論：原命題為假命題（因為找到了反例2）。</p>'
               '<p>④ 寫出否定：原命題的否定是存在量詞命題「存在一個素數不是奇數」，且此否定命題為真命題（2就是這樣的例子）。</p>'
               '</div>')
lecture.append('<p>接下來請拿《全稱量詞與存在量詞課堂練習》，依這套框架完成練習A、B、C。</p>')
lecture.append(footer(f'{SUBJECT}．{UNIT}　第 1 頁'))
lecture.append(TAIL)

with open(os.path.join(os.path.dirname(__file__), '講義_全稱量詞與存在量詞.html'), 'w', encoding='utf-8') as f:
    f.write(''.join(lecture))
print('lecture html written')

# ================= 練習 =================
p = []
p.append(page_head(f'{UNIT}．課堂練習'))
p.append(masthead(SUBJECT, UNIT, '課堂練習'))
p.append(ws_meta())
p.append('<p>提示：忘記怎麼做可以先回頭看《全稱量詞與存在量詞課堂講義》的範例四步驟。</p>')

p.append(section_h(f'一、練習A（{stars(1)}）'))
p.append('<div class="problem">'
    '<p>1．判斷下列詞語是「全稱量詞」還是「存在量詞」，請打勾。</p>'
    '<p class="indent">(1) 所有的　　全稱（　）　存在（　）</p>'
    '<p class="indent">(2) 有一個　　全稱（　）　存在（　）</p>'
    '<p class="indent">(3) 任意一個　　全稱（　）　存在（　）</p>'
    + write_lines(1) + '</div>')

p.append('<div class="problem">'
    '<p>2．命題「\\(\\forall x \\in \\mathbb{R}, |x| \\ge 0\\)」的意思是：對____實數x，|x|都____0。</p>'
    '<div class="hint-card">提示：填入「所有的」和「大於等於」。</div>'
    + write_lines(1) + '</div>')

p.append('<div class="problem">'
    '<p>3．判斷命題「所有的正方形都是四邊形」的真假。</p>'
    '<p class="indent">真（　）　假（　）</p>'
    + write_lines(2) + '</div>')

p.append(section_h(f'二、練習B（{stars(2)}）'))
p.append('<div class="problem">'
    '<p>4．用符號「∀」與「∃」表示下列命題，並判斷真假：</p>'
    '<p class="indent">(1) 任意實數的平方大於或等於0；</p>'
    '<p class="indent">(2) 存在整數x，使得 2x + 1 = 0。</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>5．判斷下列全稱量詞命題的真假：</p>'
    '<p class="indent">(1) 對任意實數a，二次函數 \\(y = x^2 + a\\) 的圖象關於y軸對稱；</p>'
    '<p class="indent">(2) 所有的無理數，平方後都是無理數。</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>6．寫出下列命題的否定，並判斷原命題與否定命題的真假：</p>'
    '<p>命題：\\(\\exists x \\in \\mathbb{Z}, x^2 = 2\\)（存在一個整數，其平方等於2）</p>'
    + write_lines(4) + '</div>')

p.append(section_h(f'三、練習C（{stars(3)}）'))
p.append('<div class="problem">'
    '<p>7．已知命題 p：「\\(\\forall x \\in \\mathbb{R}, x^2 - 2x + m \\ge 0\\)」為真命題，求m的取值範圍。（提示：先把 \\(x^2 - 2x + m\\) 配方成 (x−1)² + (m−1) 的形式）</p>'
    + write_lines(5) + '</div>')

p.append('<div class="problem">'
    '<p>8．請你自己寫出一個全稱量詞命題和一個存在量詞命題（各一個），並分別判斷真假。</p>'
    + write_lines(4) + '</div>')

p.append('<div class="problem">'
    '<p>9．命題「\\(\\forall x \\in M, p(x)\\)」為假命題，那麼「\\(\\exists x \\in M, \\lnot p(x)\\)」是否一定為真？請說明理由。</p>'
    + write_lines(4) + '</div>')

p.append(footer(f'{SUBJECT}．{UNIT}　第 1 頁'))

p.append('<div class="page-break">')
p.append(section_h('教師用參考答案'))
p.append('<p>1．(1) 全稱　(2) 存在　(3) 全稱</p>')
p.append('<p>2．對「所有的」實數x，|x|都「大於等於」0。</p>')
p.append('<p>3．真（正方形一定滿足四邊形的定義）</p>')
p.append('<p>4．(1) \\(\\forall x \\in \\mathbb{R}, x^2 \\ge 0\\)，真命題（任何實數平方都不小於0）</p>')
p.append('<p>　(2) \\(\\exists x \\in \\mathbb{Z}, 2x+1=0\\)，假命題（解得x=−0.5，不是整數）</p>')
p.append('<p>5．(1) 真（不論a為何值，二次函數y=x²+a的圖象都關於y軸對稱）</p>')
p.append('<p>　(2) 假（舉反例：√2是無理數，但(√2)²=2是有理數）</p>')
p.append('<p>6．原命題是假命題（沒有整數的平方等於2，1²=1、2²=4之間沒有整數）。否定命題：\\(\\forall x \\in \\mathbb{Z}, x^2 \\ne 2\\)，為真命題。</p>')
p.append('<p>7．\\(x^2-2x+m=(x-1)^2+(m-1)\\)。由於 (x−1)² ≥ 0 對所有x恆成立，要使整個式子恆 ≥ 0，只需 m−1 ≥ 0，解得 m ≥ 1。</p>')
p.append('<p>8．答案不唯一，例如全稱量詞命題「∀x∈R, x²≥0」為真命題；存在量詞命題「∃x∈R, x+1=0」為真命題（x=−1）。</p>')
p.append('<p>9．一定為真。因為一個命題與它的否定命題必定「一真一假」，原命題為假，否定命題就一定為真。</p>')
p.append(footer(f'{SUBJECT}．{UNIT}　第 2 頁'))
p.append('</div>')
p.append(TAIL)

with open(os.path.join(os.path.dirname(__file__), '練習_全稱量詞與存在量詞.html'), 'w', encoding='utf-8') as f:
    f.write(''.join(p))
print('practice html written')
