# -*- coding: utf-8 -*-
"""線性規劃 組1：二元一次不等式與平面區域 —— 講義＋練習（docx＋html）。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")

import dgm
import htmlkit as H
from omml_docx import *  # noqa

OUT = os.path.abspath(os.path.join(HERE, '..', '線性規劃'))
ASSET = os.path.join(HERE, 'lp1_assets')
os.makedirs(ASSET, exist_ok=True)
SUBJ, UNIT = '高二數學', '二元一次不等式與平面區域'
FOOT = '高二數學．二元一次不等式與平面區域'

# ---------------- diagrams ----------------
g = dgm.Grid(-1, 5, -2, 6, s=24)
g.base()
g.shade(2, 1, 4, keep_le=True)          # 2x+y<4，含原點側
g.line_abc(2, 1, 4, dashed=True)
g.dot(2, 0, '(2,0)', dx=6, dy=-8)
g.dot(0, 4, '(0,4)', dx=8, dy=-4)
g.dot(0, 0, '(0,0)', dx=8, dy=16)
SVG_WORKED = g.svg()

g = dgm.Grid(-2, 5, -2, 5, s=24)
g.base()
g.line_abc(1, 1, 2, dashed=True)
g.dot(2, 0, '(2,0)', dx=6, dy=-8)
g.dot(0, 2, '(0,2)', dx=8, dy=-4)
SVG_A1 = g.svg()

g = dgm.Grid(-5, 5, -5, 5, s=21)
g.base()
SVG_BLANK = g.svg()

PNG_WORKED = os.path.join(ASSET, 'worked.png')
PNG_A1 = os.path.join(ASSET, 'a1.png')
PNG_BLANK = os.path.join(ASSET, 'blank.png')
dgm.svg_to_png(SVG_WORKED, PNG_WORKED)
dgm.svg_to_png(SVG_A1, PNG_A1)
dgm.svg_to_png(SVG_BLANK, PNG_BLANK)

# ================= 講義 docx =================
P = []
P.append(masthead(SUBJ, UNIT, '課堂講義'))
P.append(student_info_row())

P.append(heading('一、概念導入'))
P.append(para('一元一次不等式（例如 {x>1}）的解，在「數線」上是一條射線；而二元一次不等式'
              '（例如 {x+y>1}）的解，畫在「坐標平面」上，是被一條直線分成的其中一整邊——'
              '一個「半平面」區域。'))
P.append(para('要畫出二元一次不等式（{Ax+By+C>0}、{<0}、{>=0} 或 {<=0}）所代表的區域，'
              '固定用下面三個步驟。'))

P.append(heading('二、畫區域的三個步驟'))
P.append(para('步驟①　畫界線：把不等號改成等號，畫出直線 {Ax+By+C=0}。'
              '若原式含 {>=} 或 {<=}，界線畫實線（邊界上的點也是解）；'
              '若含 {>} 或 {<}，界線畫虛線（邊界上的點不是解）。'))
P.append(para('步驟②　選測試點：在界線以外任選一點代入原不等式。'
              '只要界線不經過原點，就用最方便的原點 {(0,0)}。'))
P.append(para('步驟③　定區域：測試點若使不等式成立，測試點那一邊就是解；'
              '若不成立，就取另一邊。把該半平面塗上陰影。'))

P.append(heading('三、範例'))
P.append(para('範例：在坐標平面上，畫出 {2x+y−4<0} 所代表的區域。', bold=True))
P.append(para('步驟①（畫界線）：把 {<} 改成 {=}，得界線 {2x+y=4}，它通過 {(2,0)} 與 {(0,4)}。'
              '因為原式是「{<}」，界線畫成虛線。'))
P.append(para('步驟②（選測試點）：界線不過原點，取原點 {(0,0)} 代入左邊：{2×0+0−4=−4}。'))
P.append(para('步驟③（定區域）：因為 {−4<0} 成立，含原點那一側就是解。'
              '把含原點的半平面（不含界線）塗上陰影，如下圖。'))
P.append(image_para(PNG_WORKED, width_cm=7.4,
                    caption='2x + y − 4 < 0 的區域（虛線界線，陰影為解）'))
P.append(shaded_box('小提醒：虛線代表「界線上的點不算解」。若把原式改成 {2x+y−4<=0}，'
                    '界線就要改畫實線，陰影也包含界線。'))

P.append(heading('四、換你試'))
P.append(para('接下來請取出《二元一次不等式與平面區域　課堂練習》，'
              '依「畫界線 → 選測試點 → 定區域」這三個步驟，完成練習A、B、C。'))
lecture_docx = os.path.join(OUT, '講義_二元一次不等式與平面區域.docx')
print(build_docx(P, lecture_docx, footer_text=FOOT))

# ================= 練習 docx =================
Q = []
Q.append(masthead(SUBJ, UNIT, '課堂練習'))
Q.append(student_info_row())
Q.append(para('提示：先回看《課堂講義》的範例與三步驟（畫界線 → 選測試點 → 定區域），'
              '再完成下列各題。畫圖題請在方格上作答。'))

Q.append(heading(f'一、練習A（{star_label(1)}）'))
Q.append(problem_box([
    para('1．下圖已畫好直線 {x+y=2}（虛線）。請判斷不等式 {x+y>2} 的解落在界線的哪一邊，'
         '並在圖上把該區域塗上陰影。'),
]))
Q.append(image_para(PNG_A1, width_cm=6.8))
Q.append(shaded_box('鷹架：代入原點 {(0,0)}：{0+0=0}。想一想「{0>2}」成立嗎？　'
                    '（　）成立　（　）不成立。　若不成立，解就在「遠離原點」的那一邊。'))
Q.append(problem_box([
    para('2．判斷下列各不等式的界線該用「實線」還是「虛線」，並各寫出界線通過的兩個點。'),
    para('（a）{x−y>=1}　→　界線 {x−y=1}：實線／虛線？　通過（　，　）、（　，　）'),
    para('（b）{3x+2y<6}　→　界線 {3x+2y=6}：實線／虛線？　通過（　，　）、（　，　）'),
] + write_lines(2)))

Q.append(heading(f'二、練習B（{star_label(2)}）'))
Q.append(para('請自己完成三個步驟（畫界線、選測試點、塗陰影），在下面方格圖上畫出各不等式的區域。'))
Q.append(problem_box([para('3．畫出 {x−2y+2>=0} 的區域。')]))
Q.append(image_para(PNG_BLANK, width_cm=7.0))
Q.append(problem_box([para('4．畫出 {3x+2y<6} 的區域。')]))
Q.append(image_para(PNG_BLANK, width_cm=7.0))
Q.append(problem_box([
    para('5．畫出 {y>2x} 的區域。'),
    shaded_box('提示：界線 {y=2x} 通過原點，測試點不能用 {(0,0)}，改用 {(1,0)} 試。'),
]))
Q.append(image_para(PNG_BLANK, width_cm=7.0))

Q.append(heading(f'三、練習C（{star_label(3)}）'))
Q.append(problem_box([
    para('6．在同一個坐標平面上，畫出同時滿足 {x+y<=4}、{x>=0}、{y>=0} 三個條件的「公共區域」，'
         '並寫出這個區域三個頂點的坐標。'),
]))
Q.append(image_para(PNG_BLANK, width_cm=7.0))
Q.append(problem_box([
    para('7．（開放題）請你自己設計一個由三個二元一次不等式組成的不等式組，'
         '使它們的公共區域是一個三角形。寫出你的不等式組，畫出公共區域，並標出三個頂點坐標。'),
]))
Q.append(image_para(PNG_BLANK, width_cm=7.0))

Q.append(heading('參考答案與解析', page_break_before=True))
Q.append(para('練習A', bold=True))
Q.append(para('1．解在「遠離原點」的那一邊（直線 {x+y=2} 的右上方半平面），不含界線（虛線）。'
              '理由：代入原點得 {0>2} 不成立，所以取另一邊。'))
Q.append(para('2．（a）實線（含「{>=}」）；界線 {x−y=1} 通過 {(1,0)}、{(0,−1)}。'
              '（b）虛線（含「{<}」）；界線 {3x+2y=6} 通過 {(2,0)}、{(0,3)}。'))
Q.append(para('練習B', bold=True))
Q.append(para('3．界線 {x−2y+2=0} 通過 {(0,1)}、{(−2,0)}，畫實線；'
              '原點代入 {0−0+2=2}，{2>=0} 成立，取含原點的一側（界線下方）。'))
Q.append(para('4．界線 {3x+2y=6} 通過 {(2,0)}、{(0,3)}，畫虛線；'
              '原點代入得 {0<6} 成立，取含原點的一側（界線左下方）。'))
Q.append(para('5．界線 {y=2x} 通過 {(0,0)}、{(1,2)}，畫虛線；取測試點 {(1,0)}：{0>2} 不成立，'
              '取不含 {(1,0)} 的一側（界線左上方，即 y 軸正向那側）。'))
Q.append(para('練習C', bold=True))
Q.append(para('6．公共區域是以 {(0,0)}、{(4,0)}、{(0,4)} 為頂點的三角形（含三邊）。'))
Q.append(para('7．答案不唯一。例如 {x>=0}、{y>=0}、{x+y<=4}，'
              '公共區域為頂點 {(0,0)}、{(4,0)}、{(0,4)} 的三角形；'
              '或 {x>=1}、{y>=1}、{x+y<=5}，頂點 {(1,1)}、{(4,1)}、{(1,4)}。'
              '只要三條界線圍出一個三角形皆可。'))
practice_docx = os.path.join(OUT, '練習_二元一次不等式與平面區域.docx')
print(build_docx(Q, practice_docx, footer_text=FOOT))

# ================= 講義 HTML =================
lec_body = ''
lec_body += H.section_h('一、概念導入')
lec_body += r'''  <p class="lead">一元一次不等式（例如 \(x \gt 1\)）的解，在「數線」上是一條射線；而二元一次不等式（例如 \(x+y \gt 1\)）的解，畫在「坐標平面」上，是被一條直線分成的其中一整邊——一個「半平面」區域。</p>
  <p class="lead">要畫出二元一次不等式（\(Ax+By+C \gt 0\)、\(\lt 0\)、\(\ge 0\) 或 \(\le 0\)）所代表的區域，固定用下面三個步驟。</p>
'''
lec_body += H.section_h('二、畫區域的三個步驟')
lec_body += r'''  <ol class="steps-list">
    <li><b>步驟①　畫界線：</b>把不等號改成等號，畫出直線 \(Ax+By+C=0\)。若原式含 \(\ge\) 或 \(\le\)，界線畫<b>實線</b>（邊界上的點也是解）；若含 \(\gt\) 或 \(\lt\)，界線畫<b>虛線</b>（邊界上的點不是解）。</li>
    <li><b>步驟②　選測試點：</b>在界線以外任選一點代入原不等式。只要界線不經過原點，就用最方便的原點 \((0,0)\)。</li>
    <li><b>步驟③　定區域：</b>測試點若使不等式成立，測試點那一邊就是解；若不成立，就取另一邊，把該半平面塗上陰影。</li>
  </ol>
'''
lec_body += H.section_h('三、範例')
lec_body += r'''  <div class="worked-example">
    <div class="st"><b>範例：</b>在坐標平面上，畫出 \(2x+y-4 \lt 0\) 所代表的區域。</div>
    <div class="st"><b>步驟①（畫界線）：</b>把 \(\lt\) 改成 \(=\)，得界線 \(2x+y=4\)，通過 \((2,0)\) 與 \((0,4)\)。因為是「\(\lt\)」，界線畫虛線。</div>
    <div class="st"><b>步驟②（選測試點）：</b>界線不過原點，取 \((0,0)\) 代入左邊：\(2\times 0+0-4=-4\)。</div>
    <div class="st"><b>步驟③（定區域）：</b>因為 \(-4 \lt 0\) 成立，含原點那一側就是解，塗上陰影（不含界線），如下圖。</div>
  </div>
'''
lec_body += H.fig(SVG_WORKED, '2x + y − 4 &lt; 0 的區域（虛線界線，陰影為解）')
lec_body += r'''  <div class="hint-card">小提醒：虛線代表「界線上的點不算解」。若把原式改成 \(2x+y-4 \le 0\)，界線就要改畫實線，陰影也包含界線。</div>
'''
lec_body += H.section_h('四、換你試')
lec_body += r'''  <p class="lead">接下來請取出《二元一次不等式與平面區域　課堂練習》，依「畫界線 → 選測試點 → 定區域」這三個步驟，完成練習A、B、C。</p>
'''
html = H.build('講義：二元一次不等式與平面區域', SUBJ, UNIT, '課堂講義', lec_body, FOOT)
open(os.path.join(OUT, '講義_二元一次不等式與平面區域.html'), 'w', encoding='utf-8').write(html)

# ================= 練習 HTML =================
pr_body = r'''  <p class="lead">提示：先回看《課堂講義》的範例與三步驟（畫界線 → 選測試點 → 定區域），再完成下列各題。畫圖題請在方格上作答。</p>
'''
pr_body += H.section_h('一、練習A', '★☆☆')
pr_body += H.problem(
    r'<div class="q">1．下圖已畫好直線 \(x+y=2\)（虛線）。請判斷不等式 \(x+y \gt 2\) 的解落在界線的哪一邊，並在圖上把該區域塗上陰影。</div>'
    + H.fig(SVG_A1)
    + r'<div class="hint-card">鷹架：代入原點 \((0,0)\)：\(0+0=0\)。想一想「\(0 \gt 2\)」成立嗎？（　）成立　（　）不成立。若不成立，解就在「遠離原點」的那一邊。</div>')
pr_body += H.problem(
    r'<div class="q">2．判斷下列各不等式的界線該用「實線」還是「虛線」，並各寫出界線通過的兩個點。</div>'
    r'<div>（a）\(x-y \ge 1\)　→　界線 \(x-y=1\)：實線／虛線？　通過（　，　）、（　，　）</div>'
    r'<div>（b）\(3x+2y \lt 6\)　→　界線 \(3x+2y=6\)：實線／虛線？　通過（　，　）、（　，　）</div>'
    + H.wlines(2))

pr_body += H.section_h('二、練習B', '★★☆')
pr_body += r'''  <p class="lead">請自己完成三個步驟（畫界線、選測試點、塗陰影），在方格圖上畫出各不等式的區域。</p>
'''
pr_body += H.problem(r'<div class="q">3．畫出 \(x-2y+2 \ge 0\) 的區域。</div>' + H.fig(SVG_BLANK))
pr_body += H.problem(r'<div class="q">4．畫出 \(3x+2y \lt 6\) 的區域。</div>' + H.fig(SVG_BLANK))
pr_body += H.problem(
    r'<div class="q">5．畫出 \(y \gt 2x\) 的區域。</div>'
    r'<div class="hint-card">提示：界線 \(y=2x\) 通過原點，測試點不能用 \((0,0)\)，改用 \((1,0)\) 試。</div>'
    + H.fig(SVG_BLANK))

pr_body += H.section_h('三、練習C', '★★★')
pr_body += H.problem(
    r'<div class="q">6．在同一個坐標平面上，畫出同時滿足 \(x+y \le 4\)、\(x \ge 0\)、\(y \ge 0\) 三個條件的「公共區域」，並寫出這個區域三個頂點的坐標。</div>'
    + H.fig(SVG_BLANK))
pr_body += H.problem(
    r'<div class="q">7．（開放題）請你自己設計一個由三個二元一次不等式組成的不等式組，使它們的公共區域是一個三角形。寫出你的不等式組，畫出公共區域，並標出三個頂點坐標。</div>'
    + H.fig(SVG_BLANK))

pr_body += '  <div class="section-h page-break">參考答案與解析</div>\n<div class="ans">\n'
pr_body += r'''  <p><b>練習A</b></p>
  <p>1．解在「遠離原點」的那一邊（直線 \(x+y=2\) 的右上方半平面），不含界線（虛線）。理由：代入原點得 \(0 \gt 2\) 不成立，所以取另一邊。</p>
  <p>2．（a）實線（含「\(\ge\)」）；界線 \(x-y=1\) 通過 \((1,0)\)、\((0,-1)\)。（b）虛線（含「\(\lt\)」）；界線 \(3x+2y=6\) 通過 \((2,0)\)、\((0,3)\)。</p>
  <p><b>練習B</b></p>
  <p>3．界線 \(x-2y+2=0\) 通過 \((0,1)\)、\((-2,0)\)，畫實線；原點代入 \(0-0+2=2\)，\(2 \ge 0\) 成立，取含原點的一側（界線下方）。</p>
  <p>4．界線 \(3x+2y=6\) 通過 \((2,0)\)、\((0,3)\)，畫虛線；原點代入得 \(0 \lt 6\) 成立，取含原點的一側（界線左下方）。</p>
  <p>5．界線 \(y=2x\) 通過 \((0,0)\)、\((1,2)\)，畫虛線；取測試點 \((1,0)\)：\(0 \gt 2\) 不成立，取不含 \((1,0)\) 的一側（界線左上方，即 \(y\) 軸正向那側）。</p>
  <p><b>練習C</b></p>
  <p>6．公共區域是以 \((0,0)\)、\((4,0)\)、\((0,4)\) 為頂點的三角形（含三邊）。</p>
  <p>7．答案不唯一。例如 \(x \ge 0\)、\(y \ge 0\)、\(x+y \le 4\)，公共區域為頂點 \((0,0)\)、\((4,0)\)、\((0,4)\) 的三角形；或 \(x \ge 1\)、\(y \ge 1\)、\(x+y \le 5\)，頂點 \((1,1)\)、\((4,1)\)、\((1,4)\)。只要三條界線圍出一個三角形皆可。</p>
</div>
'''
html = H.build('練習：二元一次不等式與平面區域', SUBJ, UNIT, '課堂練習', pr_body, FOOT)
open(os.path.join(OUT, '練習_二元一次不等式與平面區域.html'), 'w', encoding='utf-8').write(html)

print('lp1 done')
