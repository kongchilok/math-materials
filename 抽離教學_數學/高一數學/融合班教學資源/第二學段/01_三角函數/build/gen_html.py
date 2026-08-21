# -*- coding: utf-8 -*-
"""六份融合版講義/練習的 HTML 列印版產生器（配合 worksheet-template.html 的 house style）"""
import io, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 交付檔資料夾（build/ 的上一層）

HEAD = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<script>
  MathJax = {{
    tex: {{ inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] }},
    svg: {{ fontCache: 'local', displayAlign: 'left', displayIndent: '0' }},
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
  @page {{ size: A4; margin: 0.5cm; }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: "Noto Sans TC", "Microsoft JhengHei", "PingFang TC", Arial, Verdana, sans-serif;
    font-size: 12pt; line-height: 1.5; color: #1a1a1a; background: #fff; margin: 0; padding: 0;
  }}
  .page {{ max-width: 720px; margin: 0 auto; padding: 6px 10px; }}
  .masthead {{
    font-size: 10pt; color: #555; border-top: 1px solid #999; border-bottom: 3px double #999;
    padding: 3px 0 4px; margin-bottom: 8px; display: flex; gap: 24px;
  }}
  .ws-meta {{ font-size: 12pt; margin-bottom: 10px; }}
  .ws-meta .u {{ display: inline-block; min-width: 90px; border-bottom: 1px solid #1a1a1a; margin-right: 20px; }}
  .section-h {{ font-size: 14pt; font-weight: 700; margin: 16px 0 8px; }}
  .stars {{ font-size: 12pt; letter-spacing: 1px; }}
  .problem {{ margin: 12px 0; padding: 8px 12px; background: #fff; border: 0.75pt solid #000; break-inside: avoid; page-break-inside: avoid; }}
  .hint-card, .worked-example {{ font-size: 11.5pt; background: #f0f0f0; border-left: 3px solid #555; padding: 5px 10px; margin: 6px 0; break-inside: avoid; page-break-inside: avoid; }}
  .write-lines {{ margin-top: 4px; }}
  .write-lines .line {{ height: 0.9cm; border-bottom: 1px solid #aaa; }}
  .write-lines .line:last-child {{ border-bottom: none; }}
  .choices span {{ display: inline-block; margin-right: 22px; }}
  .page-break {{ break-before: page; }}
  .figure {{ text-align: center; margin: 8px 0; break-inside: avoid; page-break-inside: avoid; }}
  .figure img {{ max-width: 100%; }}
  .figcap {{ font-size: 10pt; color: #444; margin-top: 2px; }}
  .footer {{ font-size: 9pt; color: #666; text-align: center; border-top: 1px solid #999; padding-top: 3px; margin-top: 14px; }}
</style>
</head>
<body>
<div class="page">
"""

TAIL = """
</div>
</body>
</html>
"""


def masthead(unit, typ):
    return (f'<div class="masthead"><span>科目：高一數學</span>'
            f'<span>單元：{unit}</span><span>類型：{typ}</span></div>\n'
            '<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
            '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
            '日期：<span class="u">&nbsp;</span></div>\n')


def sec(title):
    return f'<div class="section-h">{title}</div>\n'


def sec_star(prefix, letter, stars):
    return (f'<div class="section-h">{prefix}練習{letter}'
            f'（<span class="stars">{stars}</span>）</div>\n')


def prob(inner, lines=0):
    body = inner
    if lines:
        body += ('<div class="write-lines">' +
                 '<div class="line"></div>' * lines + '</div>')
    return f'<div class="problem">{body}</div>\n'


def hint(text):
    return f'<div class="hint-card">提示：{text}</div>'


def lines(n):
    return ('<div class="write-lines">' + '<div class="line"></div>' * n + '</div>')


def fig(name, width=520, cap=None):
    c = f'<div class="figcap">{cap}</div>' if cap else ''
    return (f'<div class="figure"><img src="figs/{name}" '
            f'style="max-width:{width}px; width:100%;">{c}</div>\n')


def mc3(a, b, c):
    return (f'<div class="choices"><span>A．{a}</span>'
            f'<span>B．{b}</span><span>C．{c}</span></div>')


def footer(unit):
    return f'<div class="footer">高一數學．{unit}</div>\n'


def build(fname, title, body):
    path = os.path.join(BASE, fname)
    io.open(path, 'w', encoding='utf-8').write(
        HEAD.format(title=title) + body + TAIL)
    print(path)


# ================================================================ 組① 講義
U1 = '三角函數（一）角與三角函數的概念'
b = masthead(U1, '課堂講義')
b += sec('一、任意角與象限')
b += '<p>角可以想像成一條射線繞著頂點旋轉：逆時針旋轉得到正角，順時針旋轉得到負角。</p>'
b += '<p>把角放在坐標系裡：頂點放在原點，始邊放在 x 軸正方向。終邊落在哪個象限，這個角就是哪個象限的角。</p>'
b += fig('fig1_象限與終邊.png', 400, '圖1：始邊、終邊與四個象限（例：150° 是第二象限角）')
b += r'<p>終邊相同的角：繞多一圈（±360°）終邊不變，所以與角 \(\alpha\) 終邊相同的角可寫成 \(\alpha + k\cdot 360^\circ\)（k 是整數）。</p>'
b += hint('判斷兩個角終邊是否相同，把它們相減，看差是不是 360° 的整數倍。例：390° − 30° = 360°，所以 390° 與 30° 終邊相同。')
b += sec('二、弧度制')
b += r'<p>弧度是角的另一種單位。關鍵只有一條：\(180^\circ = \pi\) rad。</p>'
b += r'<p>度 → 弧度：乘 \(\dfrac{\pi}{180^\circ}\)；　弧度 → 度：乘 \(\dfrac{180^\circ}{\pi}\)。</p>'
b += (r'<p>常用對照：\(30^\circ=\dfrac{\pi}{6}\)、\(45^\circ=\dfrac{\pi}{4}\)、'
      r'\(60^\circ=\dfrac{\pi}{3}\)、\(90^\circ=\dfrac{\pi}{2}\)、\(180^\circ=\pi\)。</p>')
b += (r'<p>半徑 r、圓心角 \(\alpha\)（弧度）的扇形：弧長 \(l = \alpha r\)；'
      r'面積 \(S = \dfrac{1}{2}lr = \dfrac{1}{2}\alpha r^2\)。</p>')
b += sec('三、三角函數的定義')
b += (r'<p>設角 \(\alpha\) 的終邊與單位圓（半徑為 1 的圓）交於點 P(x, y)，規定：'
      r'\(\sin\alpha = y\)、\(\cos\alpha = x\)、\(\tan\alpha = \dfrac{y}{x}\)（x ≠ 0）。</p>')
b += fig('fig2_單位圓定義.png', 380, '圖2：單位圓上的定義——y 是正弦、x 是餘弦')
b += (r'<p>如果終邊經過的點不在單位圓上，例如 P(x, y)，先算 \(r = \sqrt{x^2+y^2}\)，'
      r'然後 \(\sin\alpha = \dfrac{y}{r}\)、\(\cos\alpha = \dfrac{x}{r}\)、\(\tan\alpha = \dfrac{y}{x}\)。</p>')
b += '<p>各象限的正負號：</p>'
b += fig('fig8_符號口訣.png', 400, '圖3：符號口訣——「一全正、二正弦、三正切、四餘弦」')
b += sec('四、同角三角函數的關係')
b += (r'<p>平方關係：\(\sin^2\alpha + \cos^2\alpha = 1\)；　'
      r'商數關係：\(\tan\alpha = \dfrac{\sin\alpha}{\cos\alpha}\)。</p>')
b += hint('知道其中一個函數值＋角所在的象限，就能求出另外兩個。先用平方關係求出第二個，再用商數關係求第三個。')
b += sec('五、範例（跟著四個步驟做）')
b += prob(
    r'<p><b>已知角 \(\alpha\) 的終邊經過點 P(3, −4)，求 \(\sin\alpha\)、\(\cos\alpha\)、\(\tan\alpha\)。</b></p>'
    r'<ul class="steps">'
    r'<li>步驟1　圈出重點：終邊經過 P(3, −4)，所以 x = 3，y = −4。</li>'
    r'<li>步驟2　選公式：點不在單位圓上，先求 \(r = \sqrt{x^2+y^2}\)。</li>'
    r'<li>步驟3　計算：\(r = \sqrt{3^2+(-4)^2} = \sqrt{25} = 5\)；'
    r'\(\sin\alpha = -\dfrac{4}{5}\)、\(\cos\alpha = \dfrac{3}{5}\)、\(\tan\alpha = -\dfrac{4}{3}\)。</li>'
    r'<li>步驟4　檢查：P(3, −4) 在第四象限，第四象限只有 cos 為正——算出來 sin 負、cos 正、tan 負，符合。</li>'
    r'</ul>')
b += '<p><b>接下來請拿《練習_角與三角函數的概念_融合版》，依照上面範例的四個步驟完成練習A、B、C。</b></p>'
b += footer(U1)
build('講義_角與三角函數的概念_融合版_高一數學.html', U1 + '．課堂講義', b)

# ================================================================ 組① 練習
b = masthead(U1, '課堂練習')
b += '<p><b>開始前，先回頭看《講義_角與三角函數的概念_融合版》的範例，照著同樣的步驟做。</b></p>'
b += sec_star('一、', 'A', '★☆☆')
b += prob('<p>A-1．把空格填完整（照著第一行做）：</p>'
          '<p>與 60° 終邊相同的角：60° + 360° = 420°（已完成）</p>'
          '<p>60° − 360° = ＿＿＿＿＿＿</p>'
          '<p>在 90°、−300°、480° 三個角中，與 60° 終邊相同的是 ＿＿＿＿＿＿。</p>'
          + hint('相差 360° 的整數倍，終邊就相同。用「該角 − 60°」檢查。'), lines=2)
b += prob(r'<p>A-2．照著已完成的一格，把換算表填完：</p>'
          r'<p>\(30^\circ = \dfrac{\pi}{6}\)（已完成）　45° = ＿＿＿　60° = ＿＿＿　90° = ＿＿＿</p>'
          r'<p>\(\pi = 180^\circ\)（已完成）　\(\dfrac{\pi}{3}\) = ＿＿＿°　\(\dfrac{\pi}{4}\) = ＿＿＿°</p>'
          + hint(r'度 → 弧度：乘 \(\dfrac{\pi}{180^\circ}\)；弧度 → 度：乘 \(\dfrac{180^\circ}{\pi}\)。'), lines=2)
b += prob(r'<p>A-3．已知角 \(\alpha\) 的終邊與單位圓交於點 \(P\!\left(\dfrac{3}{5},\ \dfrac{4}{5}\right)\)，填空：</p>'
          r'<p>\(\sin\alpha\) = ＿＿＿　\(\cos\alpha\) = ＿＿＿　\(\tan\alpha\) = ＿＿＿</p>'
          + hint(r'單位圓上，\(\sin\alpha\) 就是 y 坐標，\(\cos\alpha\) 就是 x 坐標，\(\tan\alpha = y \div x\)。'), lines=2)
b += prob(r'<p>A-4．已知 \(\sin\alpha &gt; 0\) 且 \(\cos\alpha &lt; 0\)，則 \(\alpha\) 是第幾象限角？（圈出答案）</p>'
          + mc3('第一象限', '第二象限', '第三象限')
          + hint('回頭看講義圖3的符號口訣：sin 為正 → 第一或第二象限；cos 為負 → 第二或第三象限。'), lines=2)
b += sec_star('二、', 'B', '★★☆')
b += prob('<p>B-1．在 0° ~ 360° 範圍內，找出與 750° 終邊相同的角，並說出它是第幾象限角。</p>'
          + hint('先一直減 360°，減到落在 0° ~ 360° 為止。'), lines=3)
b += prob(r'<p>B-2．一個扇形半徑 r = 3，圓心角 \(\alpha = \dfrac{\pi}{6}\)，求弧長 l 和扇形面積 S。</p>'
          + hint(r'\(l = \alpha r\)；\(S = \dfrac{1}{2}lr\)。'), lines=4)
b += prob(r'<p>B-3．已知角 \(\alpha\) 的終邊經過點 P(−4, 3)，求 \(\sin\alpha\)、\(\cos\alpha\)、\(\tan\alpha\)。</p>'
          + hint('照講義範例四步驟：找 x、y → 求 r → 代公式 → 檢查象限符號。'), lines=5)
b += prob(r'<p>B-4．已知 \(\sin\alpha = \dfrac{5}{13}\)，且 \(\alpha\) 為第二象限角，求 \(\cos\alpha\) 和 \(\tan\alpha\)。</p>'
          + hint(r'先用 \(\sin^2\alpha + \cos^2\alpha = 1\) 求 \(\cos\alpha\)（注意第二象限 cos 是負的），再用商數關係求 \(\tan\alpha\)。'), lines=5)
b += prob(r'<p>B-5．已知 \(\tan\alpha = 2\)，求 \(\dfrac{\sin\alpha + 2\cos\alpha}{2\sin\alpha - 3\cos\alpha}\) 的值。</p>'
          + hint(r'分子、分母同時除以 \(\cos\alpha\)，整條式子就只剩下 \(\tan\alpha\)。'), lines=5)
b += sec_star('三、', 'C', '★★★')
b += prob(r'<p>C-1．已知 \(\tan\alpha = 3\)，求 \(\sin^2\alpha - 2\sin\alpha\cos\alpha\) 的值。</p>'
          + hint(r'把式子除以 \(\sin^2\alpha + \cos^2\alpha\)（它等於 1，除了不改變值），再分子分母同除 \(\cos^2\alpha\)。'), lines=5)
b += prob('<p>C-2．一個扇形的周長是 20 cm。半徑取多少時，扇形面積最大？此時圓心角是多少弧度？</p>'
          + hint('周長 = 兩條半徑 + 弧長，所以 l = 20 − 2r。把面積寫成 r 的二次函數再配方。'), lines=6)
b += prob('<p>C-3．自己出一題：仿照練習B第3題，自選一個點 P(a, b)，使 r 是整數'
          '（可選 3 與 4、6 與 8、5 與 12、8 與 15 等組合，正負號自定），寫出題目並完成解答。</p>'
          + hint('出題後記得用步驟4檢查：你的點在第幾象限？三個函數值的正負號對不對？'), lines=6)
b += footer(U1)
b += '<div class="page-break"></div>'
b += sec('教師用參考答案')
b += ('<p>A-1：60° − 360° = −300°；三個角之中，與 60° 終邊相同的只有 −300°。（90° − 60° = 30°、480° − 60° = 420°，都不是 360° 的整數倍；480° 減去 360° 得 120°，其實與 120° 終邊相同）</p>'
      r'<p>A-2：\(45^\circ=\dfrac{\pi}{4}\)、\(60^\circ=\dfrac{\pi}{3}\)、\(90^\circ=\dfrac{\pi}{2}\)；'
      r'\(\dfrac{\pi}{3}=60^\circ\)、\(\dfrac{\pi}{4}=45^\circ\)</p>'
      r'<p>A-3：\(\sin\alpha=\dfrac{4}{5}\)、\(\cos\alpha=\dfrac{3}{5}\)、\(\tan\alpha=\dfrac{4}{3}\)</p>'
      '<p>A-4：B（第二象限）</p>'
      '<p>B-1：750° − 360° − 360° = 30°，第一象限角。</p>'
      r'<p>B-2：\(l = \dfrac{\pi}{6}\times 3 = \dfrac{\pi}{2}\)；'
      r'\(S = \dfrac{1}{2}\times\dfrac{\pi}{2}\times 3 = \dfrac{3\pi}{4}\)</p>'
      r'<p>B-3：r = 5；\(\sin\alpha=\dfrac{3}{5}\)、\(\cos\alpha=-\dfrac{4}{5}\)、\(\tan\alpha=-\dfrac{3}{4}\)。'
      '（P 在第二象限：sin 正、cos 負、tan 負 ✓）</p>'
      r'<p>B-4：\(\cos\alpha=-\dfrac{12}{13}\)；\(\tan\alpha=-\dfrac{5}{12}\)</p>'
      r'<p>B-5：分子分母同除 \(\cos\alpha\)：\(\dfrac{\tan\alpha+2}{2\tan\alpha-3}=\dfrac{2+2}{4-3}=4\)</p>'
      r'<p>C-1：\(\dfrac{\sin^2\alpha-2\sin\alpha\cos\alpha}{\sin^2\alpha+\cos^2\alpha}'
      r'=\dfrac{\tan^2\alpha-2\tan\alpha}{\tan^2\alpha+1}=\dfrac{9-6}{9+1}=\dfrac{3}{10}\)</p>'
      r'<p>C-2：l = 20 − 2r，\(S=\dfrac{1}{2}(20-2r)r = 10r-r^2 = 25-(r-5)^2\)，'
      r'所以 r = 5 cm 時面積最大（25 cm²），此時 l = 10，圓心角 \(\alpha=\dfrac{l}{r}=2\) 弧度。</p>'
      '<p>C-3：開放題。檢查要點——r 計算正確、三個比值正確、象限符號一致。</p>')
b += footer(U1)
build('練習_角與三角函數的概念_融合版_高一數學.html', U1 + '．課堂練習', b)

# ================================================================ 組② 講義
U2 = '三角函數（二）誘導公式與圖像性質'
b = masthead(U2, '課堂講義')
b += sec('一、誘導公式在做什麼？')
b += ('<p>我們只背熟了 30°、45°、60° 這些銳角的三角函數值。誘導公式的工作，'
      '就是把「任意角」一步步變回「銳角」——靠的是單位圓上的對稱。</p>')
b += fig('fig3_誘導公式對稱.png', 430, '圖1：π−α、π+α、−α 的終邊，都是 α 終邊的對稱翻版')
b += sec('二、誘導公式（分組記）')
b += (r'<p>第1組（轉整圈，值不變）：\(\sin(2k\pi+\alpha)=\sin\alpha\)、'
      r'\(\cos(2k\pi+\alpha)=\cos\alpha\)、\(\tan(2k\pi+\alpha)=\tan\alpha\)</p>'
      r'<p>第2組（π + α，關於原點對稱）：\(\sin(\pi+\alpha)=-\sin\alpha\)、'
      r'\(\cos(\pi+\alpha)=-\cos\alpha\)、\(\tan(\pi+\alpha)=\tan\alpha\)</p>'
      r'<p>第3組（−α，關於 x 軸對稱）：\(\sin(-\alpha)=-\sin\alpha\)、'
      r'\(\cos(-\alpha)=\cos\alpha\)、\(\tan(-\alpha)=-\tan\alpha\)</p>'
      r'<p>第4組（π − α，關於 y 軸對稱）：\(\sin(\pi-\alpha)=\sin\alpha\)、'
      r'\(\cos(\pi-\alpha)=-\cos\alpha\)、\(\tan(\pi-\alpha)=-\tan\alpha\)</p>'
      r'<p>第5組：\(\sin\!\left(\dfrac{\pi}{2}-\alpha\right)=\cos\alpha\)、'
      r'\(\cos\!\left(\dfrac{\pi}{2}-\alpha\right)=\sin\alpha\)</p>'
      r'<p>第6組：\(\sin\!\left(\dfrac{\pi}{2}+\alpha\right)=\cos\alpha\)、'
      r'\(\cos\!\left(\dfrac{\pi}{2}+\alpha\right)=-\sin\alpha\)</p>')
b += hint('口訣「奇變偶不變，符號看象限」：看角前面是 π/2 的幾倍——奇數倍就 sin、cos 互換（變），'
          '偶數倍不換（不變）；正負號則把 α 當成銳角，看整個角落在哪個象限、原函數在那裡是正是負。')
b += sec('三、特殊角的值（必背）')
b += prob(r'<p>角度：　0°　30°　45°　60°　90°</p>'
          r'<p>sin：　\(0\)　\(\dfrac{1}{2}\)　\(\dfrac{\sqrt{2}}{2}\)　\(\dfrac{\sqrt{3}}{2}\)　\(1\)</p>'
          r'<p>cos：　\(1\)　\(\dfrac{\sqrt{3}}{2}\)　\(\dfrac{\sqrt{2}}{2}\)　\(\dfrac{1}{2}\)　\(0\)</p>'
          r'<p>tan：　\(0\)　\(\dfrac{\sqrt{3}}{3}\)　\(1\)　\(\sqrt{3}\)　不存在</p>'
          '<p>記法：sin 由左到右遞增、cos 由左到右遞減；分母都是 2，分子依次是 √0、√1、√2、√3、√4。</p>')
b += sec('四、任意角求值三步流程')
b += ('<p>第1步　負角 → 正角：用第3組公式去掉負號。</p>'
      '<p>第2步　大角 → 一圈以內：減 360°（或 2π）直到落在 0° ~ 360°。</p>'
      '<p>第3步　鈍角 → 銳角：寫成 180° ± α 或 360° − α，用第2、4組公式。</p>')
b += sec('五、y = sin x 與 y = cos x 的圖像與性質')
b += fig('fig4_sin_cos曲線.png', 640, '圖2：正弦曲線與餘弦曲線（cos 曲線就是 sin 曲線左移 π/2）')
b += prob(r'<p>共同點：定義域都是 R；值域都是 [−1, 1]；最小正週期都是 2π。</p>'
          r'<p>y = sin x 是奇函數（圖像關於原點對稱）；y = cos x 是偶函數（圖像關於 y 軸對稱）。</p>'
          r'<p>y = sin x 在 \(\left[-\dfrac{\pi}{2}+2k\pi,\ \dfrac{\pi}{2}+2k\pi\right]\) 遞增，'
          r'在 \(\left[\dfrac{\pi}{2}+2k\pi,\ \dfrac{3\pi}{2}+2k\pi\right]\) 遞減。</p>'
          r'<p>y = cos x 在 \([-\pi+2k\pi,\ 2k\pi]\) 遞增，在 \([2k\pi,\ \pi+2k\pi]\) 遞減。（k 為整數）</p>')
b += r'<p>週期公式：\(y = A\sin(\omega x+\varphi)+b\) 的最小正週期 \(T = \dfrac{2\pi}{\omega}\)。</p>'
b += sec('六、五點法畫圖')
b += (r'<p>畫一個週期的正弦型圖像，只需描五個關鍵點——x 依次取 '
      r'\(0\)、\(\dfrac{\pi}{2}\)、\(\pi\)、\(\dfrac{3\pi}{2}\)、\(2\pi\)'
      '（最高點、最低點和三個與中線的交點），再用平滑曲線連起來。</p>')
b += sec('七、範例（跟著四個步驟做）')
b += prob(
    '<p><b>求 cos(−120°) 的值。</b></p>'
    '<ul class="steps">'
    '<li>步驟1　負角 → 正角：cos 是偶函數（第3組），cos(−120°) = cos 120°。</li>'
    '<li>步驟2　鈍角 → 銳角：120° = 180° − 60°，用第4組，cos 120° = −cos 60°。</li>'
    r'<li>步驟3　代特殊角值：\(-\cos 60^\circ = -\dfrac{1}{2}\)。</li>'
    '<li>步驟4　檢查：120° 的終邊在第二象限，第二象限 cos 應為負——答案是負的，合理。</li>'
    '</ul>')
b += '<p><b>接下來請拿《練習_誘導公式與圖像性質_融合版》，依照上面範例的四個步驟完成練習A、B、C。</b></p>'
b += footer(U2)
build('講義_誘導公式與圖像性質_融合版_高一數學.html', U2 + '．課堂講義', b)

# ================================================================ 組② 練習
b = masthead(U2, '課堂練習')
b += '<p><b>開始前，先回頭看《講義_誘導公式與圖像性質_融合版》的範例，照著同樣的步驟做。</b></p>'
b += sec_star('一、', 'A', '★☆☆')
b += prob(r'<p>A-1．填空（每格填 \(\sin\alpha\)、\(\cos\alpha\)、\(\tan\alpha\) 之一，可加負號）：</p>'
          r'<p>\(\sin(\pi+\alpha)\) = ＿＿＿＿　\(\cos(-\alpha)\) = ＿＿＿＿</p>'
          r'<p>\(\tan(\pi-\alpha)\) = ＿＿＿＿　\(\sin\!\left(\dfrac{\pi}{2}-\alpha\right)\) = ＿＿＿＿</p>'
          + hint('回頭看講義「二、誘導公式」的第2、3、4、5組。'), lines=2)
b += prob(r'<p>A-2．照著已完成的第一行，求特殊角的值：</p>'
          r'<p>sin 120° = sin(180° − 60°) = sin 60° = \(\dfrac{\sqrt{3}}{2}\)（已完成）</p>'
          '<p>cos 150° = cos(180° − 30°) = −cos 30° = ＿＿＿＿</p>'
          '<p>tan 225° = tan(180° + 45°) = tan 45° = ＿＿＿＿</p>'
          + hint('先把角寫成 180° ± 銳角，再抄公式、代值。'), lines=2)
b += prob('<p>A-3．看講義圖2的正弦曲線填空：</p>'
          '<p>y = sin x 的最大值是 ＿＿＿，最小值是 ＿＿＿，最小正週期是 ＿＿＿。</p>'
          '<p>y = cos x 是（奇函數 / 偶函數），把答案圈起來。</p>', lines=2)
b += prob('<p>A-4．y = sin x 的值域是？（圈出答案）</p>'
          + mc3('[0, 1]', '[−1, 1]', '全體實數 R')
          + hint('看圖：曲線最高到多少、最低到多少？'), lines=2)
b += sec_star('二、', 'B', '★★☆')
b += prob('<p>B-1．求值：sin(−30°) + cos 225° + tan 405°</p>'
          + hint('三個角分開處理：負角先變正角；225° = 180° + 45°；405° = 360° + 45°。'), lines=5)
b += prob(r'<p>B-2．求值：\(\sin\dfrac{13\pi}{6} + \cos\dfrac{23\pi}{3}\)</p>'
          + hint(r'\(\dfrac{13\pi}{6} = 2\pi+\dfrac{\pi}{6}\)；\(\dfrac{23\pi}{3} = 6\pi+\dfrac{5\pi}{3}\)，'
                 r'再把 \(\dfrac{5\pi}{3}\) 寫成 \(2\pi-\dfrac{\pi}{3}\)。'), lines=5)
b += prob(r'<p>B-3．化簡：\(\dfrac{\cos(\pi-\alpha)\cdot\sin(2\pi-\alpha)}{\sin(\pi+\alpha)\cdot\cos(-\alpha)}\)</p>'
          + hint(r'一項一項換：\(\cos(\pi-\alpha)=-\cos\alpha\)；\(\sin(2\pi-\alpha)=-\sin\alpha\)；'
                 r'\(\sin(\pi+\alpha)=-\sin\alpha\)；\(\cos(-\alpha)=\cos\alpha\)。換完再約分。'), lines=5)
b += prob('<p>B-4．用五點法作出 y = 1 + sin x（0 ≤ x ≤ 2π）的圖像。先填表，再描點連線：</p>'
          '<p>x：　0　　π/2　　π　　3π/2　　2π</p>'
          '<p>sin x：＿＿　＿＿　＿＿　＿＿　＿＿</p>'
          '<p>y = 1 + sin x：＿＿　＿＿　＿＿　＿＿　＿＿</p>'
          + fig('fig5_五點法格線.png', 620, '（在格線上描出五個點，再用平滑曲線連接）'))
b += prob(r'<p>B-5．求下列函數的最小正週期：</p>'
          r'<p>(1) \(f(x) = \cos\!\left(2x+\dfrac{\pi}{8}\right)\)　　(2) \(g(x) = \sin\dfrac{x}{2}\)</p>'
          + hint(r'\(T = \dfrac{2\pi}{\omega}\)，ω 是 x 前面的係數。'), lines=4)
b += prob('<p>B-6．求函數 y = 2 − sin x 的最大值和最小值，並說出各在 sin x 等於多少時取得。</p>'
          + hint('sin x 的範圍是 −1 到 1。sin x 前面是負號——sin x 越小，y 越大。'), lines=4)
b += sec_star('三、', 'C', '★★★')
b += prob(r'<p>C-1．化簡：\(\dfrac{\sin(\pi-\alpha)\cdot\sin\!\left(\dfrac{3\pi}{2}-\alpha\right)}'
          r'{\cos(2\pi-\alpha)\cdot\sin(-\alpha-2\pi)}\)</p>'
          + hint(r'\(\sin\!\left(\dfrac{3\pi}{2}-\alpha\right)=-\cos\alpha\)（口訣：3 是奇數倍 → 變 cos；'
                 r'把 α 當銳角時 \(\dfrac{3\pi}{2}-\alpha\) 在第三象限，sin 為負）。'), lines=6)
b += prob('<p>C-2．寫出 y = sin x 的所有單調遞增區間（用含 k 的一般式表示，k 為整數）。</p>'
          + hint('先看圖找出一個遞增區間，再每隔一個週期 2π 複製一次。'), lines=4)
b += prob('<p>C-3．自己出一題「誘導公式化簡題」：要求至少用到兩條不同組的誘導公式，'
          '寫出題目和完整解答，並讓化簡結果是一個常數或單一函數。</p>'
          + hint('可以模仿 B-3 的樣子：分子放兩個因子、分母放兩個因子，設計成能約分。'), lines=6)
b += footer(U2)
b += '<div class="page-break"></div>'
b += sec('教師用參考答案')
b += (r'<p>A-1：\(-\sin\alpha\)；\(\cos\alpha\)；\(-\tan\alpha\)；\(\cos\alpha\)</p>'
      r'<p>A-2：cos 150° = \(-\dfrac{\sqrt{3}}{2}\)；tan 225° = 1</p>'
      '<p>A-3：最大值 1、最小值 −1、最小正週期 2π；cos x 是偶函數。</p>'
      '<p>A-4：B</p>'
      r'<p>B-1：\(-\dfrac{1}{2}-\dfrac{\sqrt{2}}{2}+1 = \dfrac{1-\sqrt{2}}{2}\)</p>'
      r'<p>B-2：\(\sin\dfrac{\pi}{6}+\cos\dfrac{5\pi}{3} = \dfrac{1}{2}+\dfrac{1}{2} = 1\)</p>'
      r'<p>B-3：\(\dfrac{(-\cos\alpha)(-\sin\alpha)}{(-\sin\alpha)(\cos\alpha)} = -1\)</p>'
      '<p>B-4：sin x 一行：0、1、0、−1、0；y 一行：1、2、1、0、1。圖像如下：</p>'
      + fig('fig5ans_y=1+sinx.png', 540)
      + r'<p>B-5：(1) \(T=\dfrac{2\pi}{2}=\pi\)　(2) \(T=\dfrac{2\pi}{1/2}=4\pi\)</p>'
      '<p>B-6：最大值 3（sin x = −1 時）；最小值 1（sin x = 1 時）。</p>'
      r'<p>C-1：\(\dfrac{\sin\alpha\cdot(-\cos\alpha)}{\cos\alpha\cdot(-\sin\alpha)} = 1\)</p>'
      r'<p>C-2：\(\left[-\dfrac{\pi}{2}+2k\pi,\ \dfrac{\pi}{2}+2k\pi\right]\)，k 為整數。</p>'
      '<p>C-3：開放題。檢查要點——每一步用的公式組正確、符號正確、結果確實化到最簡。</p>')
b += footer(U2)
build('練習_誘導公式與圖像性質_融合版_高一數學.html', U2 + '．課堂練習', b)

# ================================================================ 組③ 講義
U3 = '三角函數（三）公式變換與圖像變換'
b = masthead(U3, '課堂講義')
b += sec('一、兩角和與差的公式')
b += prob(r'<p>\(\cos(\alpha-\beta) = \cos\alpha\cos\beta + \sin\alpha\sin\beta\)</p>'
          r'<p>\(\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta\)</p>'
          r'<p>\(\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta\)</p>'
          r'<p>\(\sin(\alpha-\beta) = \sin\alpha\cos\beta - \cos\alpha\sin\beta\)</p>'
          r'<p>\(\tan(\alpha+\beta) = \dfrac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}\)　　'
          r'\(\tan(\alpha-\beta) = \dfrac{\tan\alpha-\tan\beta}{1+\tan\alpha\tan\beta}\)</p>')
b += hint('記法：cos 的展開是「同名相乘」（cos·cos、sin·sin），中間符號跟原式相反；'
          'sin 的展開是「異名相乘」（sin·cos、cos·sin），中間符號跟原式相同。')
b += ('<p>用途一：算非特殊角。例如 75° = 45° + 30°、15° = 45° − 30°。</p>'
      '<p>用途二：把 sin 20° cos 40° + cos 20° sin 40° 這種展開式「收回去」變成 sin(20° + 40°) = sin 60°。</p>')
b += sec('二、二倍角公式（令 β = α 就得到）')
b += prob(r'<p>\(\sin 2\alpha = 2\sin\alpha\cos\alpha\)</p>'
          r'<p>\(\cos 2\alpha = \cos^2\alpha-\sin^2\alpha = 2\cos^2\alpha-1 = 1-2\sin^2\alpha\)</p>'
          r'<p>\(\tan 2\alpha = \dfrac{2\tan\alpha}{1-\tan^2\alpha}\)</p>')
b += hint('cos 2α 有三種寫法——題目給 sin α 就用「1 − 2sin²α」，給 cos α 就用「2cos²α − 1」，'
          '兩個都給才用「cos²α − sin²α」。')
b += sec('三、輔助角公式（a sin x + b cos x 合成一個 sin）')
b += r'<p>\(a\sin x + b\cos x = \sqrt{a^2+b^2}\,\sin(x+\varphi)\)</p>'
b += (r'<p>常用的兩個結果：\(\sin x+\cos x = \sqrt{2}\,\sin\!\left(x+\dfrac{\pi}{4}\right)\)；　'
      r'\(\sqrt{3}\sin x+\cos x = 2\sin\!\left(x+\dfrac{\pi}{6}\right)\)</p>')
b += hint(r'合成之後，最大值就是前面的係數 \(\sqrt{a^2+b^2}\)，最小值是它加負號——'
          '這就是求「a sin x + b cos x 型」最值的固定套路。')
b += sec('四、y = A sin(ωx + φ) + b 四個參數的作用')
b += (r'<p>A（振幅）：圖像縱向拉伸，最大 A、最小 −A。</p>'
      r'<p>ω：橫向壓縮或拉伸，週期變成 \(T=\dfrac{2\pi}{\omega}\)。</p>'
      '<p>φ：左右平移——「左加右減」：x + φ 是向左移 φ，x − φ 是向右移 φ。</p>'
      '<p>b：整條曲線上下平移 b。</p>')
b += fig('fig6_圖像變換.png', 660, '圖1：四種變換各自的效果（虛線是原來的 y = sin x）')
b += hint('平移量說的是「x 本身」的變化。y = sin(2x + π/3) 要看成 sin 2(x + π/6)——'
          '先提出 2，才能讀出平移量是 π/6。')
b += sec('五、範例（跟著四個步驟做）')
b += prob(
    '<p><b>求 cos 75° 的值。</b></p>'
    '<ul class="steps">'
    '<li>步驟1　拆角：75° 不是特殊角，把它拆成兩個特殊角：75° = 45° + 30°。</li>'
    '<li>步驟2　選公式：拆的是「和」，cos 的和公式中間變減號：cos(α + β) = cos α cos β − sin α sin β。</li>'
    r'<li>步驟3　代入計算：\(\cos 75^\circ = \dfrac{\sqrt{2}}{2}\cdot\dfrac{\sqrt{3}}{2}'
    r'-\dfrac{\sqrt{2}}{2}\cdot\dfrac{1}{2} = \dfrac{\sqrt{6}-\sqrt{2}}{4}\)。</li>'
    '<li>步驟4　檢查：75° 接近 90°，cos 應該接近 0 而且是正的。(2.45 − 1.41) ÷ 4 ≈ 0.26，合理。</li>'
    '</ul>')
b += '<p><b>接下來請拿《練習_公式變換與圖像變換_融合版》，依照上面範例的四個步驟完成練習A、B、C。</b></p>'
b += footer(U3)
build('講義_公式變換與圖像變換_融合版_高一數學.html', U3 + '．課堂講義', b)

# ================================================================ 組③ 練習
b = masthead(U3, '課堂練習')
b += '<p><b>開始前，先回頭看《講義_公式變換與圖像變換_融合版》的範例，照著同樣的步驟做。</b></p>'
b += sec_star('一、', 'A', '★☆☆')
b += prob('<p>A-1．把公式填完整：</p>'
          '<p>cos(α − β) = ＿＿＿＿＿＿ + ＿＿＿＿＿＿</p>'
          '<p>sin(α + β) = ＿＿＿＿＿＿ + ＿＿＿＿＿＿</p>'
          '<p>sin 2α = ＿＿＿＿＿＿</p>'
          + hint('回頭看講義第一、二節的公式框。'), lines=2)
b += prob(r'<p>A-2．照著提示把計算補完：</p>'
          r'<p>sin 15° cos 15° = \(\dfrac{1}{2}\) × (2 sin 15° cos 15°) = \(\dfrac{1}{2}\) × sin ＿＿° = ＿＿＿＿</p>'
          + hint(r'\(2\sin\alpha\cos\alpha\) 就是 \(\sin 2\alpha\)。'), lines=2)
b += prob('<p>A-3．照著範例的拆法補完（15° = 45° − 30°）：</p>'
          '<p>cos 15° = cos(45° − 30°) = cos 45° cos 30° + sin 45° sin 30° = ＿＿＿＿</p>'
          + hint('跟講義範例幾乎一樣，只是中間變成加號。分母都是 4。'), lines=2)
b += prob(r'<p>A-4．要得到 \(y=\sin\!\left(x+\dfrac{\pi}{6}\right)\) 的圖像，'
          '需將 y = sin x 的圖像怎樣移動？（圈出答案）</p>'
          + mc3(r'向左平移 \(\dfrac{\pi}{6}\)', r'向右平移 \(\dfrac{\pi}{6}\)', r'向上平移 \(\dfrac{\pi}{6}\)')
          + hint('口訣「左加右減」：x 加了，向左移。'), lines=2)
b += sec_star('二、', 'B', '★★☆')
b += prob(r'<p>B-1．已知 \(\tan\alpha = 2\)，求 \(\tan\!\left(\alpha+\dfrac{\pi}{4}\right)\) 的值。</p>'
          + hint(r'\(\tan\dfrac{\pi}{4}=1\)，代入 tan 的和公式。'), lines=5)
b += prob(r'<p>B-2．已知 \(\sin\alpha = -\dfrac{3}{5}\)，且 \(\alpha\) 為第四象限角，'
          r'求 \(\cos 2\alpha\) 和 \(\sin 2\alpha\)。</p>'
          + hint(r'\(\cos 2\alpha\) 直接用 \(1-2\sin^2\alpha\)（不用先求 \(\cos\alpha\)）；'
                 r'\(\sin 2\alpha\) 才需要 \(\cos\alpha\)——第四象限 cos 為正。'), lines=5)
b += prob('<p>B-3．求值：sin 20° cos 40° + cos 20° sin 40°</p>'
          + hint('「異名相乘、中間加號」——這是 sin 的和公式展開後的樣子，把它收回去。'), lines=4)
b += prob(r'<p>B-4．把 \(f(x) = \sqrt{3}\sin x+\cos x\) 寫成 \(A\sin(x+\varphi)\) 的形式，'
          '並求 f(x) 的最大值。</p>'
          + hint(r'\(A=\sqrt{a^2+b^2}\)；這一題講義第三節直接給過結果。'), lines=4)
b += prob(r'<p>B-5．函數 \(y = 3\sin\!\left(2x+\dfrac{\pi}{3}\right)\)：</p>'
          '<p>(1) 寫出振幅和最小正週期；</p>'
          '<p>(2) 說明它可由 y = sin x 經過哪些步驟變換得到。</p>'
          + hint(r'平移量要先提出 2：\(2x+\dfrac{\pi}{3} = 2\!\left(x+\dfrac{\pi}{6}\right)\)。'), lines=6)
b += sec_star('三、', 'C', '★★★')
b += prob(r'<p>C-1．已知函數 \(f(x) = \dfrac{1}{2}\sin 2x-\dfrac{\sqrt{3}}{2}\cos 2x\)：</p>'
          '<p>(1) 把 f(x) 寫成 A sin(2x + φ) 的形式；</p>'
          '<p>(2) 求 f(x) 的最大值，以及取得最大值時 x 的值；</p>'
          '<p>(3) 求 f(x) 的最小正週期。</p>'
          + hint(r'係數 \(\dfrac{1}{2}\) 和 \(\dfrac{\sqrt{3}}{2}\) 正好是 cos 60° 和 sin 60°——'
                 '它是 sin(2x − 60°) 的展開。'), lines=7)
b += prob(r'<p>C-2．下圖是函數 \(f(x)=A\sin(\omega x+\varphi)\)（A &gt; 0，ω &gt; 0，'
          r'\(|\varphi| &lt; \dfrac{\pi}{2}\)）的部分圖像：最高點是 \(\left(\dfrac{\pi}{6},\ 2\right)\)，'
          '最小正週期是 π。求 f(x) 的解析式。</p>'
          + fig('fig7_求解析式.png', 560)
          + hint(r'三步：由最高點的 y 讀出 A → 由週期求 ω → 把最高點座標代入 '
                 r'\(\omega x+\varphi=\dfrac{\pi}{2}\) 解出 φ。'), lines=6)
b += prob('<p>C-3．用兩種不同的方法求 sin 75° 的值，並確認兩個結果相同。'
          '（方法可選：45° + 30° 的和公式；90° − 15° 的誘導公式＋A-3 的結果；或其他）</p>', lines=6)
b += footer(U3)
b += '<div class="page-break"></div>'
b += sec('教師用參考答案')
b += ('<p>A-1：cos α cos β + sin α sin β；sin α cos β + cos α sin β；2 sin α cos α</p>'
      r'<p>A-2：sin 30°；\(\dfrac{1}{2}\times\dfrac{1}{2}=\dfrac{1}{4}\)</p>'
      r'<p>A-3：\(\dfrac{\sqrt{2}}{2}\cdot\dfrac{\sqrt{3}}{2}+\dfrac{\sqrt{2}}{2}\cdot\dfrac{1}{2}'
      r'=\dfrac{\sqrt{6}+\sqrt{2}}{4}\)</p>'
      r'<p>A-4：A（向左平移 \(\dfrac{\pi}{6}\)）</p>'
      r'<p>B-1：\(\tan\!\left(\alpha+\dfrac{\pi}{4}\right)=\dfrac{2+1}{1-2\times 1}=\dfrac{3}{-1}=-3\)</p>'
      r'<p>B-2：\(\cos 2\alpha = 1-2\times\dfrac{9}{25}=\dfrac{7}{25}\)；'
      r'第四象限 \(\cos\alpha=\dfrac{4}{5}\)，'
      r'\(\sin 2\alpha = 2\times\!\left(-\dfrac{3}{5}\right)\!\times\dfrac{4}{5}=-\dfrac{24}{25}\)</p>'
      r'<p>B-3：sin(20° + 40°) = sin 60° = \(\dfrac{\sqrt{3}}{2}\)</p>'
      r'<p>B-4：\(f(x)=2\sin\!\left(x+\dfrac{\pi}{6}\right)\)；最大值 2。</p>'
      r'<p>B-5：(1) 振幅 3；\(T=\dfrac{2\pi}{2}=\pi\)。'
      r'(2) 一種答案：先把 y = sin x 向左平移 \(\dfrac{\pi}{3}\) 得 \(y=\sin\!\left(x+\dfrac{\pi}{3}\right)\)；'
      r'再把橫坐標縮為原來的 \(\dfrac{1}{2}\)（縱坐標不變）得 \(y=\sin\!\left(2x+\dfrac{\pi}{3}\right)\)；'
      r'最後縱坐標伸長為 3 倍得 \(y=3\sin\!\left(2x+\dfrac{\pi}{3}\right)\)。'
      r'（先縮後移也可：橫縮 \(\dfrac{1}{2}\) 後只需左移 \(\dfrac{\pi}{6}\)）</p>'
      r'<p>C-1：(1) \(f(x)=\sin\!\left(2x-\dfrac{\pi}{3}\right)\)　'
      r'(2) 最大值 1，此時 \(2x-\dfrac{\pi}{3}=\dfrac{\pi}{2}+2k\pi\)，'
      r'即 \(x=\dfrac{5\pi}{12}+k\pi\)（k 為整數）　(3) T = π</p>'
      r'<p>C-2：A = 2；\(\omega=\dfrac{2\pi}{T}=2\)；'
      r'代最高點：\(2\times\dfrac{\pi}{6}+\varphi=\dfrac{\pi}{2}\)，得 \(\varphi=\dfrac{\pi}{6}\)'
      r'（滿足 |φ| &lt; π/2）。所以 \(f(x)=2\sin\!\left(2x+\dfrac{\pi}{6}\right)\)</p>'
      r'<p>C-3：兩種方法結果都是 \(\dfrac{\sqrt{6}+\sqrt{2}}{4}\)。'
      '方法一：sin 75° = sin 45° cos 30° + cos 45° sin 30°；'
      '方法二：sin 75° = sin(90° − 15°) = cos 15°，即 A-3 的結果。</p>')
b += footer(U3)
build('練習_公式變換與圖像變換_融合版_高一數學.html', U3 + '．課堂練習', b)

print('ALL HTML DONE')
