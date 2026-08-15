# -*- coding: utf-8 -*-
"""解不等式 組1：一元二次不等式 ＋ 高次不等式（穿線法）—— 講義＋練習（docx＋html）。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")

import dgm
import htmlkit as H
from omml_docx import *  # noqa

OUT = os.path.abspath(os.path.join(HERE, '..', '解不等式'))
ASSET = os.path.join(HERE, 'iq1_assets')
os.makedirs(ASSET, exist_ok=True)
SUBJ, UNIT = '高二數學', '一元二次與高次不等式'
FOOT = '高二數學．一元二次與高次不等式'


def savepng(svg, name):
    path = os.path.join(ASSET, name)
    dgm.svg_to_png(svg, path)
    return path


def sset(*conds, joiner='，或 '):
    """解集：{ x | cond1 〔joiner〕 cond2 … }，cond 為 {} 標記字串。"""
    segs = [('t', '解集：{ x ｜ ')]
    for i, c in enumerate(conds):
        if i > 0:
            segs.append(('t', joiner))
        segs.append(('m', omath(math_to_omml(c))))
    segs.append(('t', ' }'))
    return para(segs)


# ---- 圖 ----
SVG_NL1 = dgm.nl_interval(-4, 6, [(None, -1, False, False), (4, None, False, False)])
PNG_NL1 = savepng(SVG_NL1, 'nl1.png')
SVG_SERP = dgm.serpentine(-4, 5, [-2, 1, 3])
PNG_SERP = savepng(SVG_SERP, 'serp.png')

# ================= 講義 docx =================
P = []
P.append(masthead(SUBJ, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、一元二次不等式'))
P.append(para('解一元二次不等式（先把二次項係數化為正，即設 {a>0}）：先令 {ax^2+bx+c=0} 求根，'
              '再看判別式 {Δ=b^2-4ac} 分三種情況。'))
P.append(para('•　{Δ>0}（兩相異根 {x_1<x_2}）：要 {>0} 取「兩根之外」（{x<x_1} 或 {x>x_2}）；'
              '要 {<0} 取「兩根之間」（{x_1<x<x_2}）。'))
P.append(para('•　{Δ=0}（重根 {x_0}）：要 {>0} 取 {x!=x_0}；要 {<0} 則無解。'))
P.append(para('•　{Δ<0}（無實根）：要 {>0} 恆成立（解為全體實數）；要 {<0} 則無解。'))
P.append(shaded_box('口訣（當 {a>0}）：「大於零取兩邊，小於零取中間」。'))
P.append(para('範例1：解 {x^2-3x-4>0}。', bold=True))
P.append(para('①　因式分解：{x^2-3x-4=(x-4)(x+1)}，兩根為 {x=-1}、{x=4}（{Δ>0}）。'))
P.append(para('②　因 {a=1>0} 且要 {>0}，取「兩根之外」，如下方數線（空心點表示不含端點）。'))
P.append(image_para(PNG_NL1, width_cm=11.0))
P.append(sset('x<-1', 'x>4'))

P.append(heading('二、高次不等式（穿線法）'))
P.append(para('把高次多項式因式分解成 {(x-a_1)(x-a_2)⋯} 的形式（各一次因式最高次係數為正）後，'
              '用「穿線法」（序軸標根法）：'))
P.append(para('①　令每個因式為 0，求出所有根，由小到大標在數線上。'))
P.append(para('②　從數線「最右上方」起，畫一條曲線蛇形穿過每個根（上、下交替）。'))
P.append(para('③　要 {>0} 取曲線在數線「上方」的區間；要 {<0} 取「下方」的區間。'))
P.append(shaded_box('重根要訣「奇穿偶不穿」：因式 {(x-a)^k} 中，{k} 為奇數時曲線穿過（變號）；'
                    '{k} 為偶數時碰到根就彈回（不變號）。'))
P.append(para('範例2：解 {(x+2)(x-1)(x-3)<0}。', bold=True))
P.append(para('①　三個根 {x=-2}、{1}、{3}，標在數線上。'))
P.append(para('②　由右上方蛇形穿線，各區間符號（由右到左）為 {+}、{-}、{+}、{-}，如下圖。'))
P.append(image_para(PNG_SERP, width_cm=11.5))
P.append(para('③　因要 {<0}，取曲線在「下方」的區間。'))
P.append(sset('x<-2', '1<x<3'))

P.append(heading('三、換你試'))
P.append(para('接下來請取出《一元二次與高次不等式　課堂練習》，完成練習A、B、C。'
              '穿線法的數線與曲線請自己動手畫。'))
print(build_docx(P, os.path.join(OUT, '講義_一元二次與高次不等式.docx'), footer_text=FOOT))

# ================= 練習 docx =================
Q = []
Q.append(masthead(SUBJ, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('提示：一元二次「大於零取兩邊，小於零取中間」；高次用穿線法「右上起、蛇形穿根、奇穿偶不穿」。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．解 {x^2-5x+6>0}。'),
    shaded_box('鷹架：因式分解 {x^2-5x+6=(x-2)(x-3)}，兩根為（　）、（　）；'
               '因 {a>0} 且要 {>0}，取兩根之外。解集 { x ｜ x<（　）或 x>（　）}。'),
] + write_lines(2)))
Q.append(problem_box([
    para('2．解 {(x-1)(x-2)(x-4)>0}。'),
    shaded_box('鷹架：三根 {1}、{2}、{4} 標在數線上；由右上穿線；要 {>0} 取上方區間。'),
] + write_lines(3)))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(problem_box([
    para('3．解下列一元二次不等式：'),
    para('（a）{x^2-2x-8<=0}　　（b）{x^2+x+1>0}'),
] + write_lines(4)))
Q.append(problem_box([
    para('4．解 {x(x+3)(x-2)<=0}。'),
] + write_lines(4)))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([
    para('5．解 {(x+1)(x-2)^2(x-3)<0}。'),
    shaded_box('提示：{(x-2)^2} 是偶次，用「偶不穿」——碰到根 {x=2} 不變號。'),
] + write_lines(4)))
Q.append(problem_box([
    para('6．（逆向題）已知一元二次不等式 {x^2+bx+c<0} 的解集為 { x ｜ -1<x<3 }，求 {b}、{c} 的值。'),
] + write_lines(4)))

Q.append(heading('參考答案與解析', page_break_before=True))
Q.append(para('練習A', bold=True))
Q.append(para('1．{(x-2)(x-3)>0}，兩根 {2}、{3}；取兩根之外。', ))
Q.append(sset('x<2', 'x>3'))
Q.append(para('2．三根 {1}、{2}、{4}；由右到左符號 {+,-,+,-}，要 {>0} 取上方（正）區間。'))
Q.append(sset('1<x<2', 'x>4'))
Q.append(para('練習B', bold=True))
Q.append(para('3．（a）{x^2-2x-8=(x-4)(x+2)<=0}，取兩根之間：{-2<=x<=4}。'
              '（b）{Δ=1-4=-3<0} 且 {a=1>0}，故 {x^2+x+1>0} 恆成立，解為全體實數。'))
Q.append(para('4．三根 {-3}、{0}、{2}；符號由右到左 {+,-,+,-}；要 {<=0} 取下方區間並含根。'))
Q.append(sset('x<=-3', '0<=x<=2'))
Q.append(para('練習C', bold=True))
Q.append(para('5．根 {-1}、{2}（重根，偶不穿）、{3}。因 {(x-2)^2>=0}，式子的正負由 {(x+1)(x-3)} 決定；'
              '{(x+1)(x-3)<0} 得 {-1<x<3}，再扣除令原式為 0 的 {x=2}。'))
Q.append(para([('t', '解集：{ x ｜ '), ('m', omath(math_to_omml('-1<x<3'))),
               ('t', '，且 '), ('m', omath(math_to_omml('x!=2'))), ('t', ' }')]))
Q.append(para('6．由解集 { x ｜ -1<x<3 } 知 {-1}、{3} 是方程 {x^2+bx+c=0} 的兩根。'
              '兩根和 {-1+3=2=-b}，得 {b=-2}；兩根積 {(-1)×3=-3=c}，得 {c=-3}。'))
print(build_docx(Q, os.path.join(OUT, '練習_一元二次與高次不等式.docx'), footer_text=FOOT))

# ================= 講義 HTML =================
b = ''
b += H.section_h('一、一元二次不等式')
b += r'''  <p class="lead">解一元二次不等式（先把二次項係數化為正，即設 \(a \gt 0\)）：先令 \(ax^2+bx+c=0\) 求根，再看判別式 \(\Delta=b^2-4ac\) 分三種情況。</p>
  <ul class="steps-list">
    <li>•　\(\Delta \gt 0\)（兩相異根 \(x_1 \lt x_2\)）：要 \(\gt 0\) 取「兩根之外」（\(x \lt x_1\) 或 \(x \gt x_2\)）；要 \(\lt 0\) 取「兩根之間」（\(x_1 \lt x \lt x_2\)）。</li>
    <li>•　\(\Delta = 0\)（重根 \(x_0\)）：要 \(\gt 0\) 取 \(x \ne x_0\)；要 \(\lt 0\) 則無解。</li>
    <li>•　\(\Delta \lt 0\)（無實根）：要 \(\gt 0\) 恆成立（解為全體實數）；要 \(\lt 0\) 則無解。</li>
  </ul>
  <div class="hint-card">口訣（當 \(a \gt 0\)）：「大於零取兩邊，小於零取中間」。</div>
  <div class="worked-example">
    <div class="st"><b>範例1：</b>解 \(x^2-3x-4 \gt 0\)。</div>
    <div class="st"><b>①</b> 因式分解：\(x^2-3x-4=(x-4)(x+1)\)，兩根為 \(x=-1\)、\(x=4\)（\(\Delta \gt 0\)）。</div>
    <div class="st"><b>②</b> 因 \(a=1 \gt 0\) 且要 \(\gt 0\)，取「兩根之外」，如下方數線（空心點表示不含端點）。</div>
  </div>
'''
b += H.fig(SVG_NL1)
b += r'''  <p class="lead">解集：\(\{\,x \mid x \lt -1 \text{ 或 } x \gt 4\,\}\)。</p>
'''
b += H.section_h('二、高次不等式（穿線法）')
b += r'''  <p class="lead">把高次多項式因式分解成 \((x-a_1)(x-a_2)\cdots\) 的形式（各一次因式最高次係數為正）後，用「穿線法」（序軸標根法）：</p>
  <ol class="steps-list">
    <li><b>①</b> 令每個因式為 0，求出所有根，由小到大標在數線上。</li>
    <li><b>②</b> 從數線「最右上方」起，畫一條曲線蛇形穿過每個根（上、下交替）。</li>
    <li><b>③</b> 要 \(\gt 0\) 取曲線在數線「上方」的區間；要 \(\lt 0\) 取「下方」的區間。</li>
  </ol>
  <div class="hint-card">重根要訣「奇穿偶不穿」：因式 \((x-a)^k\) 中，\(k\) 為奇數時曲線穿過（變號）；\(k\) 為偶數時碰到根就彈回（不變號）。</div>
  <div class="worked-example">
    <div class="st"><b>範例2：</b>解 \((x+2)(x-1)(x-3) \lt 0\)。</div>
    <div class="st"><b>①</b> 三個根 \(x=-2\)、\(1\)、\(3\)，標在數線上。</div>
    <div class="st"><b>②</b> 由右上方蛇形穿線，各區間符號（由右到左）為 \(+,-,+,-\)，如下圖。</div>
  </div>
'''
b += H.fig(SVG_SERP)
b += r'''  <p class="lead"><b>③</b> 因要 \(\lt 0\)，取曲線在「下方」的區間。　解集：\(\{\,x \mid x \lt -2 \text{ 或 } 1 \lt x \lt 3\,\}\)。</p>
'''
b += H.section_h('三、換你試')
b += r'''  <p class="lead">接下來請取出《一元二次與高次不等式　課堂練習》，完成練習A、B、C。穿線法的數線與曲線請自己動手畫。</p>
'''
open(os.path.join(OUT, '講義_一元二次與高次不等式.html'), 'w', encoding='utf-8').write(
    H.build('講義：一元二次與高次不等式', SUBJ, UNIT, '課堂講義', b, FOOT))

# ================= 練習 HTML =================
b = r'''  <p class="lead">提示：一元二次「大於零取兩邊，小於零取中間」；高次用穿線法「右上起、蛇形穿根、奇穿偶不穿」。</p>
'''
b += H.section_h('一、練習A', '★☆☆')
b += H.problem(
    r'<div class="q">1．解 \(x^2-5x+6 \gt 0\)。</div>'
    r'<div class="hint-card">鷹架：因式分解 \(x^2-5x+6=(x-2)(x-3)\)，兩根為（　）、（　）；因 \(a \gt 0\) 且要 \(\gt 0\)，取兩根之外。解集 \(\{\,x \mid x \lt\)（　）\(\text{ 或 } x \gt\)（　）\(\}\)。</div>'
    + H.wlines(2))
b += H.problem(
    r'<div class="q">2．解 \((x-1)(x-2)(x-4) \gt 0\)。</div>'
    r'<div class="hint-card">鷹架：三根 \(1\)、\(2\)、\(4\) 標在數線上；由右上穿線；要 \(\gt 0\) 取上方區間。</div>'
    + H.wlines(3))

b += H.section_h('二、練習B', '★★☆')
b += H.problem(
    r'<div class="q">3．解下列一元二次不等式：</div>'
    r'<div>（a）\(x^2-2x-8 \le 0\)　　（b）\(x^2+x+1 \gt 0\)</div>' + H.wlines(4))
b += H.problem(r'<div class="q">4．解 \(x(x+3)(x-2) \le 0\)。</div>' + H.wlines(4))

b += H.section_h('三、練習C', '★★★')
b += H.problem(
    r'<div class="q">5．解 \((x+1)(x-2)^2(x-3) \lt 0\)。</div>'
    r'<div class="hint-card">提示：\((x-2)^2\) 是偶次，用「偶不穿」——碰到根 \(x=2\) 不變號。</div>'
    + H.wlines(4))
b += H.problem(
    r'<div class="q">6．（逆向題）已知一元二次不等式 \(x^2+bx+c \lt 0\) 的解集為 \(\{\,x \mid -1 \lt x \lt 3\,\}\)，求 \(b\)、\(c\) 的值。</div>'
    + H.wlines(4))

b += '  <div class="section-h page-break">參考答案與解析</div>\n<div class="ans">\n'
b += r'''  <p><b>練習A</b></p>
  <p>1．\((x-2)(x-3) \gt 0\)，兩根 \(2\)、\(3\)；取兩根之外。解集 \(\{\,x \mid x \lt 2 \text{ 或 } x \gt 3\,\}\)。</p>
  <p>2．三根 \(1\)、\(2\)、\(4\)；由右到左符號 \(+,-,+,-\)，要 \(\gt 0\) 取上方（正）區間。解集 \(\{\,x \mid 1 \lt x \lt 2 \text{ 或 } x \gt 4\,\}\)。</p>
  <p><b>練習B</b></p>
  <p>3．（a）\(x^2-2x-8=(x-4)(x+2) \le 0\)，取兩根之間：\(-2 \le x \le 4\)。（b）\(\Delta=1-4=-3 \lt 0\) 且 \(a=1 \gt 0\)，故 \(x^2+x+1 \gt 0\) 恆成立，解為全體實數。</p>
  <p>4．三根 \(-3\)、\(0\)、\(2\)；符號由右到左 \(+,-,+,-\)；要 \(\le 0\) 取下方區間並含根。解集 \(\{\,x \mid x \le -3 \text{ 或 } 0 \le x \le 2\,\}\)。</p>
  <p><b>練習C</b></p>
  <p>5．根 \(-1\)、\(2\)（重根，偶不穿）、\(3\)。因 \((x-2)^2 \ge 0\)，式子的正負由 \((x+1)(x-3)\) 決定；\((x+1)(x-3) \lt 0\) 得 \(-1 \lt x \lt 3\)，再扣除令原式為 0 的 \(x=2\)。解集 \(\{\,x \mid -1 \lt x \lt 3 \text{ 且 } x \ne 2\,\}\)。</p>
  <p>6．由解集 \(\{\,x \mid -1 \lt x \lt 3\,\}\) 知 \(-1\)、\(3\) 是方程 \(x^2+bx+c=0\) 的兩根。兩根和 \(-1+3=2=-b\)，得 \(b=-2\)；兩根積 \((-1)\times3=-3=c\)，得 \(c=-3\)。</p>
</div>
'''
open(os.path.join(OUT, '練習_一元二次與高次不等式.html'), 'w', encoding='utf-8').write(
    H.build('練習：一元二次與高次不等式', SUBJ, UNIT, '課堂練習', b, FOOT))

print('ineq1 done')
