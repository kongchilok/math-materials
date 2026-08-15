# -*- coding: utf-8 -*-
"""解不等式 組2：分式不等式 ＋ 絕對值不等式 —— 講義＋練習（docx＋html）。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")

import dgm
import htmlkit as H
from omml_docx import *  # noqa

OUT = os.path.abspath(os.path.join(HERE, '..', '解不等式'))
ASSET = os.path.join(HERE, 'iq2_assets')
os.makedirs(ASSET, exist_ok=True)
SUBJ, UNIT = '高二數學', '分式與絕對值不等式'
FOOT = '高二數學．分式與絕對值不等式'


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


SVG_NL1 = dgm.nl_interval(-4, 4, [(-2, 1, False, True)])   # −2<x≤1
PNG_NL1 = savepng(SVG_NL1, 'nl1.png')
SVG_NL2 = dgm.nl_interval(-3, 4, [(-1, 2, False, False)])  # −1<x<2
PNG_NL2 = savepng(SVG_NL2, 'nl2.png')

# ================= 講義 docx =================
P = []
P.append(masthead(SUBJ, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、分式不等式'))
P.append(para('解分式不等式的關鍵：先把式子整理成「右邊等於 0」，左邊通分成一個分式 {frac(P(x),Q(x))}，'
              '再把它轉成整式（多項式）不等式來看符號：'))
P.append(para('•　{frac(P(x),Q(x))>0} 等價於 {P(x)×Q(x)>0}；　{frac(P(x),Q(x))<0} 等價於 {P(x)×Q(x)<0}。'))
P.append(shaded_box('最重要提醒：分母不可以為 0！所以分母的根一定「空心」（不可取）。'
                    '若是 {>=0} 或 {<=0}，分子的根可取（實心），但分母的根仍然不可取。'))
P.append(para('範例1：解 {frac(x-1,x+2)<=0}。', bold=True))
P.append(para('①　轉成整式：{frac(x-1,x+2)<=0} 等價於 {(x-1)(x+2)<=0}（且 {x+2!=0}）。'))
P.append(para('②　{(x-1)(x+2)<=0} 得 {-2<=x<=1}；但 {x=-2} 令分母為 0，必須排除。'))
P.append(para('③　所以 {x=1} 可取（實心）、{x=-2} 不可取（空心），如下方數線。'))
P.append(image_para(PNG_NL1, width_cm=10.0))
P.append(sset('-2<x<=1'))

P.append(heading('二、絕對值不等式'))
P.append(para('絕對值不等式的兩條基本規則（設 {a>0}）：'))
P.append(para('•　{|x|<a} 等價於 {-a<x<a}（「小於取中間」）。'))
P.append(para('•　{|x|>a} 等價於 {x<-a} 或 {x>a}（「大於取兩邊」）。'))
P.append(para('把 {x} 換成一個式子也一樣：{|f(x)|<a} 即 {-a<f(x)<a}；{|f(x)|>a} 即 {f(x)<-a} 或 {f(x)>a}。'))
P.append(shaded_box('遇到兩個以上絕對值相加（例如 {|x-1|+|x+2|}），用「零點分段法」：'
                    '在每個絕對值為 0 的點把數線分段，逐段去掉絕對值符號後再解。'))
P.append(para('範例2：解 {|2x-1|<3}。', bold=True))
P.append(para('①　依「小於取中間」：{|2x-1|<3} 即 {-3<2x-1<3}。'))
P.append(para('②　三邊各加 1：{-2<2x<4}；再各除以 2：{-1<x<2}，如下方數線。'))
P.append(image_para(PNG_NL2, width_cm=10.0))
P.append(sset('-1<x<2'))

P.append(heading('三、換你試'))
P.append(para('接下來請取出《分式與絕對值不等式　課堂練習》，完成練習A、B、C。'))
print(build_docx(P, os.path.join(OUT, '講義_分式與絕對值不等式.docx'), footer_text=FOOT))

# ================= 練習 docx =================
Q = []
Q.append(masthead(SUBJ, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('提示：分式先化成「一邊為 0」再轉整式，分母的根永遠空心；'
              '絕對值「小於取中間、大於取兩邊」。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．解 {frac(x+1,x-2)>0}。'),
    shaded_box('鷹架：轉成整式 {(x+1)(x-2)>0}，兩根（　）、（　），取兩根之外；'
               '分母根 {x=2} 空心。'),
] + write_lines(2)))
Q.append(problem_box([
    para('2．解 {|x-3|<=2}。'),
    shaded_box('鷹架：依「小於取中間」，{-2<=x-3<=2}，三邊各加 3 得（　）{<=x<=}（　）。'),
] + write_lines(2)))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem_box([
    para('3．解 {frac(2x+1,x-1)>=1}。'),
    shaded_box('提示：先移項成一邊為 0——{frac(2x+1,x-1)-1>=0}，通分後再判斷符號。'),
] + write_lines(4)))
Q.append(problem_box([
    para('4．解 {|2x+1|>5}。'),
] + write_lines(3)))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([
    para('5．解 {frac(x-4,x+1)<=2}。'),
    shaded_box('提示：移項通分後，若兩邊乘以負數，不等號方向要改變。'),
] + write_lines(4)))
Q.append(problem_box([
    para('6．解 {|x-1|+|x+2|<=5}。（用零點分段法）'),
    shaded_box('提示：零點為 {x=-2} 與 {x=1}，把數線分成 {x<-2}、{-2<=x<1}、{x>=1} 三段討論。'),
] + write_lines(5)))

Q.append(heading('參考答案與解析', page_break_before=True))
Q.append(para('練習A', bold=True))
Q.append(para('1．{(x+1)(x-2)>0}，兩根 {-1}、{2}，取兩根之外；分母根 {x=2} 本已在範圍外。'))
Q.append(sset('x<-1', 'x>2'))
Q.append(para('2．{-2<=x-3<=2} → 各加 3 → {1<=x<=5}。'))
Q.append(sset('1<=x<=5', joiner=''))
Q.append(para('練習B', bold=True))
Q.append(para('3．{frac(2x+1,x-1)-1>=0} → {frac(2x+1-(x-1),x-1)>=0} → {frac(x+2,x-1)>=0}，'
              '即 {(x+2)(x-1)>=0} 且 {x!=1}。分子根 {x=-2} 可取，分母根 {x=1} 不可取。'))
Q.append(sset('x<=-2', 'x>1'))
Q.append(para('4．{|2x+1|>5} → {2x+1<-5} 或 {2x+1>5} → {2x<-6} 或 {2x>4} → {x<-3} 或 {x>2}。'))
Q.append(sset('x<-3', 'x>2'))
Q.append(para('練習C', bold=True))
Q.append(para('5．{frac(x-4,x+1)-2<=0} → {frac(x-4-2(x+1),x+1)<=0} → {frac(-x-6,x+1)<=0}；'
              '同乘 {-1}（變號）得 {frac(x+6,x+1)>=0}，即 {(x+6)(x+1)>=0} 且 {x!=-1}。'))
Q.append(sset('x<=-6', 'x>-1'))
Q.append(para('6．零點分段法（零點 {x=-2}、{x=1}）：'))
Q.append(para('•　{x<-2}：{-(x-1)-(x+2)=-2x-1<=5} → {x>=-3}，取 {-3<=x<-2}。'))
Q.append(para('•　{-2<=x<1}：{-(x-1)+(x+2)=3<=5} 恆成立，取 {-2<=x<1}。'))
Q.append(para('•　{x>=1}：{(x-1)+(x+2)=2x+1<=5} → {x<=2}，取 {1<=x<=2}。'))
Q.append(para('三段合併：'))
Q.append(sset('-3<=x<=2', joiner=''))
print(build_docx(Q, os.path.join(OUT, '練習_分式與絕對值不等式.docx'), footer_text=FOOT))

# ================= 講義 HTML =================
b = ''
b += H.section_h('一、分式不等式')
b += r'''  <p class="lead">解分式不等式的關鍵：先把式子整理成「右邊等於 0」，左邊通分成一個分式 \(\dfrac{P(x)}{Q(x)}\)，再把它轉成整式（多項式）不等式來看符號：</p>
  <ul class="steps-list">
    <li>•　\(\dfrac{P(x)}{Q(x)} \gt 0\) 等價於 \(P(x)\cdot Q(x) \gt 0\)；　\(\dfrac{P(x)}{Q(x)} \lt 0\) 等價於 \(P(x)\cdot Q(x) \lt 0\)。</li>
  </ul>
  <div class="hint-card"><b>最重要提醒：</b>分母不可以為 0！所以分母的根一定「空心」（不可取）。若是 \(\ge 0\) 或 \(\le 0\)，分子的根可取（實心），但分母的根仍然不可取。</div>
  <div class="worked-example">
    <div class="st"><b>範例1：</b>解 \(\dfrac{x-1}{x+2} \le 0\)。</div>
    <div class="st"><b>①</b> 轉成整式：\(\dfrac{x-1}{x+2} \le 0\) 等價於 \((x-1)(x+2) \le 0\)（且 \(x+2 \ne 0\)）。</div>
    <div class="st"><b>②</b> \((x-1)(x+2) \le 0\) 得 \(-2 \le x \le 1\)；但 \(x=-2\) 令分母為 0，必須排除。</div>
    <div class="st"><b>③</b> 所以 \(x=1\) 可取（實心）、\(x=-2\) 不可取（空心），如下方數線。</div>
  </div>
'''
b += H.fig(SVG_NL1)
b += r'''  <p class="lead">解集：\(\{\,x \mid -2 \lt x \le 1\,\}\)。</p>
'''
b += H.section_h('二、絕對值不等式')
b += r'''  <p class="lead">絕對值不等式的兩條基本規則（設 \(a \gt 0\)）：</p>
  <ul class="steps-list">
    <li>•　\(|x| \lt a\) 等價於 \(-a \lt x \lt a\)（「小於取中間」）。</li>
    <li>•　\(|x| \gt a\) 等價於 \(x \lt -a\) 或 \(x \gt a\)（「大於取兩邊」）。</li>
  </ul>
  <p class="lead">把 \(x\) 換成一個式子也一樣：\(|f(x)| \lt a\) 即 \(-a \lt f(x) \lt a\)；\(|f(x)| \gt a\) 即 \(f(x) \lt -a\) 或 \(f(x) \gt a\)。</p>
  <div class="hint-card">遇到兩個以上絕對值相加（例如 \(|x-1|+|x+2|\)），用「零點分段法」：在每個絕對值為 0 的點把數線分段，逐段去掉絕對值符號後再解。</div>
  <div class="worked-example">
    <div class="st"><b>範例2：</b>解 \(|2x-1| \lt 3\)。</div>
    <div class="st"><b>①</b> 依「小於取中間」：\(|2x-1| \lt 3\) 即 \(-3 \lt 2x-1 \lt 3\)。</div>
    <div class="st"><b>②</b> 三邊各加 1：\(-2 \lt 2x \lt 4\)；再各除以 2：\(-1 \lt x \lt 2\)，如下方數線。</div>
  </div>
'''
b += H.fig(SVG_NL2)
b += r'''  <p class="lead">解集：\(\{\,x \mid -1 \lt x \lt 2\,\}\)。</p>
'''
b += H.section_h('三、換你試')
b += r'''  <p class="lead">接下來請取出《分式與絕對值不等式　課堂練習》，完成練習A、B、C。</p>
'''
open(os.path.join(OUT, '講義_分式與絕對值不等式.html'), 'w', encoding='utf-8').write(
    H.build('講義：分式與絕對值不等式', SUBJ, UNIT, '課堂講義', b, FOOT))

# ================= 練習 HTML =================
b = r'''  <p class="lead">提示：分式先化成「一邊為 0」再轉整式，分母的根永遠空心；絕對值「小於取中間、大於取兩邊」。</p>
'''
b += H.section_h('一、練習A', '★☆☆')
b += H.problem(
    r'<div class="q">1．解 \(\dfrac{x+1}{x-2} \gt 0\)。</div>'
    r'<div class="hint-card">鷹架：轉成整式 \((x+1)(x-2) \gt 0\)，兩根（　）、（　），取兩根之外；分母根 \(x=2\) 空心。</div>'
    + H.wlines(2))
b += H.problem(
    r'<div class="q">2．解 \(|x-3| \le 2\)。</div>'
    r'<div class="hint-card">鷹架：依「小於取中間」，\(-2 \le x-3 \le 2\)，三邊各加 3 得（　）\(\le x \le\)（　）。</div>'
    + H.wlines(2))

b += H.section_h('二、練習B', '★★☆')
b += H.problem(
    r'<div class="q">3．解 \(\dfrac{2x+1}{x-1} \ge 1\)。</div>'
    r'<div class="hint-card">提示：先移項成一邊為 0——\(\dfrac{2x+1}{x-1}-1 \ge 0\)，通分後再判斷符號。</div>'
    + H.wlines(4))
b += H.problem(r'<div class="q">4．解 \(|2x+1| \gt 5\)。</div>' + H.wlines(3))

b += H.section_h('三、練習C', '★★★')
b += H.problem(
    r'<div class="q">5．解 \(\dfrac{x-4}{x+1} \le 2\)。</div>'
    r'<div class="hint-card">提示：移項通分後，若兩邊乘以負數，不等號方向要改變。</div>'
    + H.wlines(4))
b += H.problem(
    r'<div class="q">6．解 \(|x-1|+|x+2| \le 5\)。（用零點分段法）</div>'
    r'<div class="hint-card">提示：零點為 \(x=-2\) 與 \(x=1\)，把數線分成 \(x \lt -2\)、\(-2 \le x \lt 1\)、\(x \ge 1\) 三段討論。</div>'
    + H.wlines(5))

b += '  <div class="section-h page-break">參考答案與解析</div>\n<div class="ans">\n'
b += r'''  <p><b>練習A</b></p>
  <p>1．\((x+1)(x-2) \gt 0\)，兩根 \(-1\)、\(2\)，取兩根之外。解集 \(\{\,x \mid x \lt -1 \text{ 或 } x \gt 2\,\}\)。</p>
  <p>2．\(-2 \le x-3 \le 2\) → 各加 3 → \(1 \le x \le 5\)。解集 \(\{\,x \mid 1 \le x \le 5\,\}\)。</p>
  <p><b>練習B</b></p>
  <p>3．\(\dfrac{2x+1}{x-1}-1 \ge 0 \Rightarrow \dfrac{x+2}{x-1} \ge 0\)，即 \((x+2)(x-1) \ge 0\) 且 \(x \ne 1\)。分子根 \(x=-2\) 可取，分母根 \(x=1\) 不可取。解集 \(\{\,x \mid x \le -2 \text{ 或 } x \gt 1\,\}\)。</p>
  <p>4．\(|2x+1| \gt 5 \Rightarrow 2x+1 \lt -5\) 或 \(2x+1 \gt 5 \Rightarrow x \lt -3\) 或 \(x \gt 2\)。解集 \(\{\,x \mid x \lt -3 \text{ 或 } x \gt 2\,\}\)。</p>
  <p><b>練習C</b></p>
  <p>5．\(\dfrac{x-4}{x+1}-2 \le 0 \Rightarrow \dfrac{-x-6}{x+1} \le 0\)；同乘 \(-1\)（變號）得 \(\dfrac{x+6}{x+1} \ge 0\)，即 \((x+6)(x+1) \ge 0\) 且 \(x \ne -1\)。解集 \(\{\,x \mid x \le -6 \text{ 或 } x \gt -1\,\}\)。</p>
  <p>6．零點分段（零點 \(x=-2\)、\(x=1\)）：</p>
  <p>•　\(x \lt -2\)：\(-(x-1)-(x+2)=-2x-1 \le 5 \Rightarrow x \ge -3\)，取 \(-3 \le x \lt -2\)。</p>
  <p>•　\(-2 \le x \lt 1\)：\(-(x-1)+(x+2)=3 \le 5\) 恆成立，取 \(-2 \le x \lt 1\)。</p>
  <p>•　\(x \ge 1\)：\((x-1)+(x+2)=2x+1 \le 5 \Rightarrow x \le 2\)，取 \(1 \le x \le 2\)。</p>
  <p>三段合併：解集 \(\{\,x \mid -3 \le x \le 2\,\}\)。</p>
</div>
'''
open(os.path.join(OUT, '練習_分式與絕對值不等式.html'), 'w', encoding='utf-8').write(
    H.build('練習：分式與絕對值不等式', SUBJ, UNIT, '課堂練習', b, FOOT))

print('ineq2 done')
