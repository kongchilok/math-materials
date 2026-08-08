#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 讀取 HTML 範本
template_path = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\assets\worksheet-template.html"
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# ===== 指數函數講義 HTML =====
exponential_lecture_html = template.replace(
    "[標題]", "4.2 指數函數"
).replace(
    "[副標題]", "課堂講義"
).replace(
    "[內容]", """
<h2 class="section-h">一、指數函數的定義</h2>
<p>指數函數是形如 \\( y = a^x \\) 的函數，其中底數 \\( a > 0 \\) 且 \\( a ≠ 1 \\)。</p>
<p>我們已經學過指數運算（例如 \\( 2^3 = 8 \\)），現在要研究當 \\( x \\) 是任意實數時，\\( a^x \\) 如何變化。</p>

<h2 class="section-h">二、指數函數的性質</h2>
<p>1. 定義域：所有實數 \\( \\mathbb{R} \\)</p>
<p>2. 值域：所有正實數 \\( (0, +∞) \\)（注意：\\( a^x > 0 \\) 對所有 \\( x \\) 恆成立）</p>
<p>3. 必過定點：所有指數函數圖像都過點 \\( (0, 1) \\)（因為 \\( a^0 = 1 \\)）</p>
<p>4. 單調性：</p>
<ul>
  <li>當 \\( a > 1 \\) 時，\\( y = a^x \\) 單調遞增（\\( x \\) 越大，函數值越大）</li>
  <li>當 \\( 0 < a < 1 \\) 時，\\( y = a^x \\) 單調遞減（\\( x \\) 越大，函數值越小）</li>
</ul>

<h2 class="section-h">三、已完成範例</h2>
<div class="hint-card">
  <strong>例題：計算 \\( 2^5 · 2^{-1} \\)</strong>
  <p><strong>步驟1：</strong>依指數運算法則，同底相乘時指數相加<br/>
     \\( 2^5 · 2^{-1} = 2^{5+(-1)} = 2^4 \\)</p>
  <p><strong>步驟2：</strong>計算 \\( 2^4 = 16 \\)</p>
  <p><strong>答案：</strong>16</p>
</div>

<p>接下來請拿《課堂練習——指數函數》，依照上面四個性質和這個範例的步驟框架，完成練習A、B、C。</p>
""")

with open(r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\講義_4.2指數函數_融合版.html', 'w', encoding='utf-8') as f:
    f.write(exponential_lecture_html)

# ===== 反函數講義 HTML =====
inverse_lecture_html = template.replace(
    "[標題]", "4.3 反函數"
).replace(
    "[副標題]", "課堂講義"
).replace(
    "[內容]", """
<h2 class="section-h">一、反函數的概念</h2>
<p>如果函數 \\( f \\) 和函數 \\( g \\) 互為反函數，那麼它們有特殊關係：</p>
<ul>
  <li>\\( f(g(x)) = x \\)（用 \\( g \\) 的輸出去用 \\( f \\)，回到原本的 \\( x \\)）</li>
  <li>\\( g(f(x)) = x \\)（用 \\( f \\) 的輸出去用 \\( g \\)，也回到原本的 \\( x \\)）</li>
</ul>
<p>簡單說：反函數「撤銷」了原函數的作用。</p>

<h2 class="section-h">二、反函數的性質</h2>
<p>1. 定義域和值域互換：</p>
<ul>
  <li>反函數的定義域 = 原函數的值域</li>
  <li>反函數的值域 = 原函數的定義域</li>
</ul>
<p>2. 圖像對稱：反函數的圖像與原函數的圖像關於直線 \\( y = x \\) 對稱</p>
<p>3. 坐標互換：若點 \\( (a, b) \\) 在原函數上，則點 \\( (b, a) \\) 在反函數上</p>

<h2 class="section-h">三、求反函數的步驟</h2>
<p>對函數 \\( y = f(x) \\)，求其反函數 \\( y = f^{-1}(x) \\) 的方法：</p>
<p>步驟1：令 \\( y = f(x) \\)<br/>
步驟2：對調 \\( x \\) 和 \\( y \\)：\\( x = f(y) \\)<br/>
步驟3：用 \\( y \\) 表示 \\( x \\)（解出 \\( y \\)）<br/>
步驟4：寫成 \\( y = f^{-1}(x) \\)</p>

<h2 class="section-h">四、已完成範例</h2>
<div class="hint-card">
  <strong>例題：已知 \\( f(x) = 2x + 1 \\)，求其反函數 \\( f^{-1}(x) \\)</strong>
  <p><strong>步驟1：</strong>令 \\( y = 2x + 1 \\)<br/>
     <strong>步驟2：</strong>對調 \\( x, y \\)：\\( x = 2y + 1 \\)<br/>
     <strong>步驟3：</strong>用 \\( y \\) 表示：\\( 2y = x - 1 \\)，\\( y = \\frac{x-1}{2} \\)<br/>
     <strong>步驟4：</strong>反函數為 \\( f^{-1}(x) = \\frac{x-1}{2} \\)</p>
  <p><strong>驗證：</strong> \\( f(f^{-1}(x)) = f(\\frac{x-1}{2}) = 2 · \\frac{x-1}{2} + 1 = x - 1 + 1 = x \\) ✓</p>
</div>

<p>接下來請拿《課堂練習——反函數》，依照上面四個性質和這個範例的步驟框架，完成練習A、B、C。</p>
""")

with open(r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\講義_4.3反函數_融合版.html', 'w', encoding='utf-8') as f:
    f.write(inverse_lecture_html)

# ===== 對數函數講義 HTML =====
logarithm_lecture_html = template.replace(
    "[標題]", "4.4 對數函數"
).replace(
    "[副標題]", "課堂講義"
).replace(
    "[內容]", """
<h2 class="section-h">一、對數的定義</h2>
<p>對數是一個反向思考的工具。</p>
<p><strong>問題：</strong>「2的多少次方等於8？」</p>
<p><strong>答案用對數表示：</strong> \\( \\log_2 8 = 3 \\)（因為 \\( 2^3 = 8 \\)）</p>
<p>一般地，如果 \\( a^x = N \\)（其中 \\( a > 0, a ≠ 1, N > 0 \\)），<br/>
那麼 \\( x = \\log_a N \\)（讀作「以 \\( a \\) 為底 \\( N \\) 的對數」）</p>

<h2 class="section-h">二、對數函數的定義</h2>
<p>對數函數是形如 \\( y = \\log_a x \\) 的函數，其中 \\( a > 0 \\) 且 \\( a ≠ 1 \\)。</p>
<p>特別地，對數函數 \\( y = \\log_a x \\) 是指數函數 \\( y = a^x \\) 的反函數。</p>

<h2 class="section-h">三、對數函數的性質</h2>
<p>1. 定義域：\\( (0, +∞) \\)（注意：\\( x \\) 必須大於0）<br/>
2. 值域：所有實數 \\( \\mathbb{R} \\)<br/>
3. 必過定點：所有對數函數圖像都過點 \\( (1, 0) \\)（因為 \\( \\log_a 1 = 0 \\)）<br/>
4. 單調性：<br/>
   &nbsp;&nbsp;• 當 \\( a > 1 \\) 時，\\( y = \\log_a x \\) 單調遞增<br/>
   &nbsp;&nbsp;• 當 \\( 0 < a < 1 \\) 時，\\( y = \\log_a x \\) 單調遞減<br/>
5. 與指數函數的對稱性：\\( y = \\log_a x \\) 與 \\( y = a^x \\) 的圖像關於 \\( y = x \\) 對稱</p>

<h2 class="section-h">四、對數運算法則</h2>
<p>若 \\( M > 0, N > 0, a > 0, a ≠ 1 \\)，則：</p>
<ul>
  <li>\\( \\log_a(M·N) = \\log_a M + \\log_a N \\)（乘積變和）</li>
  <li>\\( \\log_a \\frac{M}{N} = \\log_a M - \\log_a N \\)（商變差）</li>
  <li>\\( \\log_a M^n = n · \\log_a M \\)（冪變係數）</li>
</ul>

<h2 class="section-h">五、已完成範例</h2>
<div class="hint-card">
  <strong>例題：計算 \\( \\log_2 8 \\)</strong>
  <p><strong>步驟1：</strong>問題轉化：\\( \\log_2 8 = ? \\) 意思是「2的多少次方等於8？」<br/>
     <strong>步驟2：</strong>列方程：\\( 2^x = 8 \\)<br/>
     <strong>步驟3：</strong>求解：\\( 2^x = 2^3 \\)，所以 \\( x = 3 \\)<br/>
     <strong>步驟4：</strong>答案：\\( \\log_2 8 = 3 \\)</p>
</div>

<p>接下來請拿《課堂練習——對數函數》，依照上面的運算法則和這個範例的步驟框架，完成練習A、B、C。</p>
""")

with open(r'C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義\講義_4.4對數函數_融合版.html', 'w', encoding='utf-8') as f:
    f.write(logarithm_lecture_html)

print("✓ 三份講義 HTML 已產出")
