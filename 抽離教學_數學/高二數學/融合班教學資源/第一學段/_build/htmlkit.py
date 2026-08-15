# -*- coding: utf-8 -*-
"""HTML 列印版骨架：套用 inclusive-math house-style（見 skill 的 worksheet-template.html）。
math 用 \\( \\)／\\[ \\]；不等號一律 \\lt \\gt \\le \\ge（避開 QB-14 未轉義 < 檢查）；
公式內中文包 \\text{...}；整份文件只放一個 position:fixed 的 .footer（QB-15c）。"""

HEAD = r'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<title>%%TITLE%%</title>
<script>
  MathJax = {
    tex: { inlineMath: [['\\(', '\\)']], displayMath: [['\\[', '\\]']] },
    svg: { fontCache: 'local', displayAlign: 'left', displayIndent: '0', mtextInheritFont: true },
    options: { enableMenu: false }
  };
</script>
<script>
(function loadMathJax(urls) {
  if (!urls.length) return;
  var s = document.createElement('script');
  s.src = urls[0];
  s.onerror = function () { loadMathJax(urls.slice(1)); };
  document.head.appendChild(s);
})([
  'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-svg.js',
  'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js',
  'https://unpkg.com/mathjax@3/es5/tex-mml-svg.js'
]);
</script>
<style>
  @page { size: A4; margin: 0.5cm; }
  * { box-sizing: border-box; }
  body {
    font-family: "Noto Sans TC", "Microsoft JhengHei", "PingFang TC", Arial, Verdana, sans-serif;
    font-size: 12pt; line-height: 1.5; color: #1a1a1a; background: #fff; margin: 0; padding: 0;
  }
  .page { max-width: 720px; margin: 0 auto; padding: 6px 10px 40px; }
  .masthead {
    font-size: 10pt; color: #555; border-top: 1px solid #999; border-bottom: 3px double #999;
    padding: 3px 0 4px; margin-bottom: 8px; display: flex; gap: 24px;
  }
  .ws-meta { font-size: 12pt; margin-bottom: 10px; }
  .ws-meta .u { display: inline-block; min-width: 90px; border-bottom: 1px solid #1a1a1a; margin-right: 20px; }
  .section-h { font-size: 14pt; font-weight: 700; margin: 16px 0 8px; }
  .stars { font-size: 12pt; letter-spacing: 1px; }
  .lead { margin: 6px 0 10px; }
  .steps-list { margin: 6px 0; padding-left: 0; list-style: none; }
  .steps-list li { margin: 6px 0; }
  .problem { margin: 12px 0; padding: 8px 12px; background: #fff; border: 0.75pt solid #000; break-inside: avoid; page-break-inside: avoid; }
  .problem .q { font-weight: 600; }
  .hint-card, .worked-example { font-size: 11.5pt; background: #f0f0f0; border-left: 3px solid #555; padding: 6px 12px; margin: 8px 0; break-inside: avoid; }
  .worked-example .st { margin: 5px 0; }
  .fig { text-align: center; margin: 10px 0 4px; break-inside: avoid; }
  .fig svg { width: auto; max-width: 340px; height: auto; }
  .cap { font-size: 10.5pt; color: #555; text-align: center; margin-bottom: 6px; }
  .write-lines { margin-top: 6px; }
  .write-lines .line { height: 0.9cm; border-bottom: 1px solid #aaa; }
  .write-lines .line:last-child { border-bottom: none; }
  .ans .problem { border-color: #333; }
  .page-break { break-before: page; page-break-before: always; }
  .footer { position: fixed; bottom: 0; left: 0; right: 0; max-width: 720px; margin: 0 auto; background: #fff; font-size: 9pt; color: #666; text-align: center; border-top: 1px solid #999; padding: 3px 0 2px; }
</style>
</head>
<body>
<div class="page">
'''

FOOT = '''  <div class="footer">%%FOOTER%%</div>
</div>
</body>
</html>'''


def masthead(subject, unit, doctype):
    return (f'  <div class="masthead"><span>科目：{subject}</span>'
            f'<span>單元：{unit}</span><span>類型：{doctype}</span></div>\n')


META = ('  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
        '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
        '日期：<span class="u">&nbsp;</span></div>\n')


def section_h(title, stars=None):
    st = f'（<span class="stars">{stars}</span>）' if stars else ''
    return f'  <div class="section-h">{title}{st}</div>\n'


def wlines(n):
    return '<div class="write-lines">' + ''.join('<div class="line"></div>' for _ in range(n)) + '</div>'


def problem(inner):
    return f'  <div class="problem">{inner}</div>\n'


def fig(svg, cap=None):
    c = f'<div class="cap">{cap}</div>' if cap else ''
    return f'  <div class="fig">{svg}</div>{c}\n'


def build(title, subject, unit, doctype, body, footer):
    html = HEAD.replace('%%TITLE%%', title)
    html += masthead(subject, unit, doctype) + META + body + FOOT.replace('%%FOOTER%%', footer)
    return html
