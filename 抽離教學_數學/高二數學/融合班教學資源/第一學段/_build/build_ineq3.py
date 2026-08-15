# -*- coding: utf-8 -*-
"""解不等式 組3：無理不等式 ＋ 指數對數不等式 —— 講義＋練習（docx＋html）。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")

import dgm
import htmlkit as H
from omml_docx import *  # noqa

OUT = os.path.abspath(os.path.join(HERE, '..', '解不等式'))
ASSET = os.path.join(HERE, 'iq3_assets')
os.makedirs(ASSET, exist_ok=True)
SUBJ, UNIT = '高二數學', '無理與指數對數不等式'
FOOT = '高二數學．無理與指數對數不等式'


def savepng(svg, name):
    path = os.path.join(ASSET, name)
    dgm.svg_to_png(svg, path)
    return path


def sset(*conds, joiner='，或 '):
    segs = [('t', '解集：{ x ｜ ')]
    for i, c in enumerate(conds):
        if i > 0:
            segs.append(('t', joiner))
        segs.append(('m', omath(math_to_omml(c))))
    segs.append(('t', ' }'))
    return para(segs)


SVG_NL3 = dgm.nl_interval(-1, 6, [(None, 3, False, False)])   # x<3
PNG_NL3 = savepng(SVG_NL3, 'nl3.png')
SVG_NL4 = dgm.nl_interval(-1, 11, [(1, 9, False, False)])     # 1<x<9
PNG_NL4 = savepng(SVG_NL4, 'nl4.png')

# ================= 講義 docx =================
P = []
P.append(masthead(SUBJ, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、無理不等式'))
P.append(para('含有根號的（無理）不等式，主要用「平方去根號」，但一定要同時照顧兩件事：'
              '根號內 {>=0}（定義域），以及平方前兩邊的正負。常見三種型（設 {c} 為常數）：'))
P.append(para('•　{sqrt(f(x))<c}（需 {c>0}）：等價於 {0<=f(x)<c^2}。'))
P.append(para('•　{sqrt(f(x))>c}（{c>=0}）：等價於 {f(x)>c^2}；若 {c<0}，則只需 {f(x)>=0}。'))
P.append(para('•　{sqrt(f(x))<sqrt(g(x))}：等價於 {0<=f(x)<g(x)}。'))
P.append(shaded_box('關鍵：平方之前先確定兩邊都非負才可以平方；根號內必須 {>=0}，這一步不能漏。'))
P.append(para('範例1：解 {sqrt(2x+1)<3}。', bold=True))
P.append(para('①　定義域：{2x+1>=0}，即 {x>=-frac(1,2)}。'))
P.append(para('②　兩邊皆非負，可平方：{2x+1<9}，得 {x<4}。'))
P.append(para('③　取交集：{-frac(1,2)<=x<4}。'))
P.append(sset('-frac(1,2)<=x<4', joiner=''))
P.append(para('範例2：解 {sqrt(x+3)<sqrt(2x-1)}。', bold=True))
P.append(para('①　依 {sqrt(f)<sqrt(g)} 型：需 {0<=x+3<2x-1}。'))
P.append(para('②　由 {x+3<2x-1} 得 {x>4}；此時 {x+3>=0} 自動成立。'))
P.append(sset('x>4', joiner=''))

P.append(heading('二、指數與對數不等式'))
P.append(para('比較指數或對數的大小，先化成「同底」，再看底數 {a} 決定不等號方向：'))
P.append(para('•　指數（{a>1}）：{a^m<a^n} 等價於 {m<n}（同向）；'
              '（{0<a<1}）：{a^m<a^n} 等價於 {m>n}（反向）。'))
P.append(para('•　對數（{a>1}）：{fn(log)_a M<fn(log)_a N} 等價於 {0<M<N}；'
              '（{0<a<1}）：等價於 {M>N>0}。'))
P.append(shaded_box('對數不等式一定要先寫「定義域」：真數必須 {>0}。底數 {0<a<1} 時，去對數／去指數後'
                    '不等號要「反向」，這是最常錯的一步。'))
P.append(para('範例3：解 {3^x<27}。', bold=True))
P.append(para('①　化同底：{27=3^3}，故 {3^x<3^3}。'))
P.append(para('②　底 {3>1}（同向）：{x<3}，如下方數線。'))
P.append(image_para(PNG_NL3, width_cm=9.5))
P.append(sset('x<3', joiner=''))
P.append(para('範例4：解 {fn(log)_2(x-1)<3}。', bold=True))
P.append(para('①　定義域：真數 {x-1>0}，即 {x>1}。'))
P.append(para('②　化同底：{3=fn(log)_2 8}，故 {fn(log)_2(x-1)<fn(log)_2 8}。'))
P.append(para('③　底 {2>1}（同向）：{x-1<8}，即 {x<9}。取交集 {1<x<9}，如下方數線。'))
P.append(image_para(PNG_NL4, width_cm=10.5))
P.append(sset('1<x<9', joiner=''))

P.append(heading('三、換你試'))
P.append(para('接下來請取出《無理與指數對數不等式　課堂練習》，完成練習A、B、C。'))
print(build_docx(P, os.path.join(OUT, '講義_無理與指數對數不等式.docx'), footer_text=FOOT))

# ================= 練習 docx =================
Q = []
Q.append(masthead(SUBJ, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('提示：無理式先寫定義域再平方；指對數先化同底，{0<a<1} 時不等號要反向，對數的真數要 {>0}。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．解 {sqrt(x-2)<4}。'),
    shaded_box('鷹架：定義域 {x-2>=0} 即 {x>=}（　）；平方得 {x-2<16} 即 {x<}（　）；取交集。'),
] + write_lines(2)))
Q.append(problem_box([
    para('2．解 {2^x>16}。'),
    shaded_box('鷹架：{16=2^4}，故 {2^x>2^4}；底 {2>1} 同向，得 {x>}（　）。'),
] + write_lines(2)))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem_box([
    para('3．解 {sqrt(3x+1)>=4}。'),
] + write_lines(4)))
Q.append(problem_box([
    para('4．解 {fn(log)_3(2x-1)<2}。'),
    shaded_box('提示：先寫定義域（真數 {>0}），再把 {2} 化成 {fn(log)_3 9}。'),
] + write_lines(4)))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([
    para('5．解 {(1/2)^x>4}。'),
    shaded_box('提示：{4=(1/2)^{-2}}；底 {0<a<1}，去指數後不等號要反向。'),
] + write_lines(4)))
Q.append(problem_box([
    para('6．解 {fn(log)_{1/2}(x+1)>-1}。'),
    shaded_box('提示：先寫定義域；{-1=fn(log)_{1/2} 2}；底 {0<a<1}，反向。'),
] + write_lines(4)))

Q.append(heading('參考答案與解析', page_break_before=True))
Q.append(para('練習A', bold=True))
Q.append(para('1．定義域 {x>=2}；平方 {x-2<16} 得 {x<18}。取交集。'))
Q.append(sset('2<=x<18', joiner=''))
Q.append(para('2．{16=2^4}，{2^x>2^4}，底 {2>1} 同向。'))
Q.append(sset('x>4', joiner=''))
Q.append(para('練習B', bold=True))
Q.append(para('3．定義域 {3x+1>=0} 即 {x>=-frac(1,3)}；右邊 {4>=0}，平方 {3x+1>=16}，得 {x>=5}。'
              '（{x>=5} 已滿足定義域。）'))
Q.append(sset('x>=5', joiner=''))
Q.append(para('4．定義域 {2x-1>0} 即 {x>frac(1,2)}；{2=fn(log)_3 9}，底 {3>1} 同向，{2x-1<9} 得 {x<5}。'
              '取交集 {frac(1,2)<x<5}。'))
Q.append(sset('frac(1,2)<x<5', joiner=''))
Q.append(para('練習C', bold=True))
Q.append(para('5．{4=(1/2)^{-2}}，{(1/2)^x>(1/2)^{-2}}，底 {0<a<1} 反向，得 {x<-2}。'))
Q.append(sset('x<-2', joiner=''))
Q.append(para('6．定義域 {x+1>0} 即 {x>-1}；{-1=fn(log)_{1/2} 2}，底 {0<a<1} 反向，得 {x+1<2}，即 {x<1}。'
              '取交集 {-1<x<1}。'))
Q.append(sset('-1<x<1', joiner=''))
print(build_docx(Q, os.path.join(OUT, '練習_無理與指數對數不等式.docx'), footer_text=FOOT))

# ================= 講義 HTML =================
b = ''
b += H.section_h('一、無理不等式')
b += r'''  <p class="lead">含有根號的（無理）不等式，主要用「平方去根號」，但一定要同時照顧兩件事：根號內 \(\ge 0\)（定義域），以及平方前兩邊的正負。常見三種型（設 \(c\) 為常數）：</p>
  <ul class="steps-list">
    <li>•　\(\sqrt{f(x)} \lt c\)（需 \(c \gt 0\)）：等價於 \(0 \le f(x) \lt c^2\)。</li>
    <li>•　\(\sqrt{f(x)} \gt c\)（\(c \ge 0\)）：等價於 \(f(x) \gt c^2\)；若 \(c \lt 0\)，則只需 \(f(x) \ge 0\)。</li>
    <li>•　\(\sqrt{f(x)} \lt \sqrt{g(x)}\)：等價於 \(0 \le f(x) \lt g(x)\)。</li>
  </ul>
  <div class="hint-card"><b>關鍵：</b>平方之前先確定兩邊都非負才可以平方；根號內必須 \(\ge 0\)，這一步不能漏。</div>
  <div class="worked-example">
    <div class="st"><b>範例1：</b>解 \(\sqrt{2x+1} \lt 3\)。</div>
    <div class="st"><b>①</b> 定義域：\(2x+1 \ge 0\)，即 \(x \ge -\tfrac{1}{2}\)。</div>
    <div class="st"><b>②</b> 兩邊皆非負，可平方：\(2x+1 \lt 9\)，得 \(x \lt 4\)。</div>
    <div class="st"><b>③</b> 取交集：\(-\tfrac{1}{2} \le x \lt 4\)。解集 \(\{\,x \mid -\tfrac{1}{2} \le x \lt 4\,\}\)。</div>
  </div>
  <div class="worked-example">
    <div class="st"><b>範例2：</b>解 \(\sqrt{x+3} \lt \sqrt{2x-1}\)。</div>
    <div class="st"><b>①</b> 依 \(\sqrt{f} \lt \sqrt{g}\) 型：需 \(0 \le x+3 \lt 2x-1\)。</div>
    <div class="st"><b>②</b> 由 \(x+3 \lt 2x-1\) 得 \(x \gt 4\)；此時 \(x+3 \ge 0\) 自動成立。解集 \(\{\,x \mid x \gt 4\,\}\)。</div>
  </div>
'''
b += H.section_h('二、指數與對數不等式')
b += r'''  <p class="lead">比較指數或對數的大小，先化成「同底」，再看底數 \(a\) 決定不等號方向：</p>
  <ul class="steps-list">
    <li>•　指數（\(a \gt 1\)）：\(a^m \lt a^n\) 等價於 \(m \lt n\)（同向）；（\(0 \lt a \lt 1\)）：\(a^m \lt a^n\) 等價於 \(m \gt n\)（反向）。</li>
    <li>•　對數（\(a \gt 1\)）：\(\log_a M \lt \log_a N\) 等價於 \(0 \lt M \lt N\)；（\(0 \lt a \lt 1\)）：等價於 \(M \gt N \gt 0\)。</li>
  </ul>
  <div class="hint-card">對數不等式一定要先寫「定義域」：真數必須 \(\gt 0\)。底數 \(0 \lt a \lt 1\) 時，去對數／去指數後不等號要「反向」，這是最常錯的一步。</div>
  <div class="worked-example">
    <div class="st"><b>範例3：</b>解 \(3^x \lt 27\)。</div>
    <div class="st"><b>①</b> 化同底：\(27=3^3\)，故 \(3^x \lt 3^3\)。</div>
    <div class="st"><b>②</b> 底 \(3 \gt 1\)（同向）：\(x \lt 3\)，如下方數線。</div>
  </div>
'''
b += H.fig(SVG_NL3)
b += r'''  <p class="lead">解集：\(\{\,x \mid x \lt 3\,\}\)。</p>
  <div class="worked-example">
    <div class="st"><b>範例4：</b>解 \(\log_2(x-1) \lt 3\)。</div>
    <div class="st"><b>①</b> 定義域：真數 \(x-1 \gt 0\)，即 \(x \gt 1\)。</div>
    <div class="st"><b>②</b> 化同底：\(3=\log_2 8\)，故 \(\log_2(x-1) \lt \log_2 8\)。</div>
    <div class="st"><b>③</b> 底 \(2 \gt 1\)（同向）：\(x-1 \lt 8\)，即 \(x \lt 9\)。取交集 \(1 \lt x \lt 9\)，如下方數線。</div>
  </div>
'''
b += H.fig(SVG_NL4)
b += r'''  <p class="lead">解集：\(\{\,x \mid 1 \lt x \lt 9\,\}\)。</p>
'''
b += H.section_h('三、換你試')
b += r'''  <p class="lead">接下來請取出《無理與指數對數不等式　課堂練習》，完成練習A、B、C。</p>
'''
open(os.path.join(OUT, '講義_無理與指數對數不等式.html'), 'w', encoding='utf-8').write(
    H.build('講義：無理與指數對數不等式', SUBJ, UNIT, '課堂講義', b, FOOT))

# ================= 練習 HTML =================
b = r'''  <p class="lead">提示：無理式先寫定義域再平方；指對數先化同底，\(0 \lt a \lt 1\) 時不等號要反向，對數的真數要 \(\gt 0\)。</p>
'''
b += H.section_h('一、練習A', '★☆☆')
b += H.problem(
    r'<div class="q">1．解 \(\sqrt{x-2} \lt 4\)。</div>'
    r'<div class="hint-card">鷹架：定義域 \(x-2 \ge 0\) 即 \(x \ge\)（　）；平方得 \(x-2 \lt 16\) 即 \(x \lt\)（　）；取交集。</div>'
    + H.wlines(2))
b += H.problem(
    r'<div class="q">2．解 \(2^x \gt 16\)。</div>'
    r'<div class="hint-card">鷹架：\(16=2^4\)，故 \(2^x \gt 2^4\)；底 \(2 \gt 1\) 同向，得 \(x \gt\)（　）。</div>'
    + H.wlines(2))

b += H.section_h('二、練習B', '★★☆')
b += H.problem(r'<div class="q">3．解 \(\sqrt{3x+1} \ge 4\)。</div>' + H.wlines(4))
b += H.problem(
    r'<div class="q">4．解 \(\log_3(2x-1) \lt 2\)。</div>'
    r'<div class="hint-card">提示：先寫定義域（真數 \(\gt 0\)），再把 \(2\) 化成 \(\log_3 9\)。</div>'
    + H.wlines(4))

b += H.section_h('三、練習C', '★★★')
b += H.problem(
    r'<div class="q">5．解 \(\left(\tfrac{1}{2}\right)^x \gt 4\)。</div>'
    r'<div class="hint-card">提示：\(4=\left(\tfrac{1}{2}\right)^{-2}\)；底 \(0 \lt a \lt 1\)，去指數後不等號要反向。</div>'
    + H.wlines(4))
b += H.problem(
    r'<div class="q">6．解 \(\log_{1/2}(x+1) \gt -1\)。</div>'
    r'<div class="hint-card">提示：先寫定義域；\(-1=\log_{1/2} 2\)；底 \(0 \lt a \lt 1\)，反向。</div>'
    + H.wlines(4))

b += '  <div class="section-h page-break">參考答案與解析</div>\n<div class="ans">\n'
b += r'''  <p><b>練習A</b></p>
  <p>1．定義域 \(x \ge 2\)；平方 \(x-2 \lt 16\) 得 \(x \lt 18\)。取交集：解集 \(\{\,x \mid 2 \le x \lt 18\,\}\)。</p>
  <p>2．\(16=2^4\)，\(2^x \gt 2^4\)，底 \(2 \gt 1\) 同向。解集 \(\{\,x \mid x \gt 4\,\}\)。</p>
  <p><b>練習B</b></p>
  <p>3．定義域 \(3x+1 \ge 0\) 即 \(x \ge -\tfrac{1}{3}\)；右邊 \(4 \ge 0\)，平方 \(3x+1 \ge 16\)，得 \(x \ge 5\)。（\(x \ge 5\) 已滿足定義域。）解集 \(\{\,x \mid x \ge 5\,\}\)。</p>
  <p>4．定義域 \(2x-1 \gt 0\) 即 \(x \gt \tfrac{1}{2}\)；\(2=\log_3 9\)，底 \(3 \gt 1\) 同向，\(2x-1 \lt 9\) 得 \(x \lt 5\)。取交集：解集 \(\{\,x \mid \tfrac{1}{2} \lt x \lt 5\,\}\)。</p>
  <p><b>練習C</b></p>
  <p>5．\(4=\left(\tfrac{1}{2}\right)^{-2}\)，\(\left(\tfrac{1}{2}\right)^x \gt \left(\tfrac{1}{2}\right)^{-2}\)，底 \(0 \lt a \lt 1\) 反向，得 \(x \lt -2\)。解集 \(\{\,x \mid x \lt -2\,\}\)。</p>
  <p>6．定義域 \(x+1 \gt 0\) 即 \(x \gt -1\)；\(-1=\log_{1/2} 2\)，底 \(0 \lt a \lt 1\) 反向，得 \(x+1 \lt 2\)，即 \(x \lt 1\)。取交集：解集 \(\{\,x \mid -1 \lt x \lt 1\,\}\)。</p>
</div>
'''
open(os.path.join(OUT, '練習_無理與指數對數不等式.html'), 'w', encoding='utf-8').write(
    H.build('練習：無理與指數對數不等式', SUBJ, UNIT, '課堂練習', b, FOOT))

print('ineq3 done')
