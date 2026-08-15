# -*- coding: utf-8 -*-
"""Shared HTML scaffolding for the 講義/練習 HTML->PDF track, mirroring
assets/worksheet-template.html's CSS exactly (house style: 12pt body/14pt
headings, 0.5cm margins, masthead+footer, star-based difficulty, uniform
thin .problem borders, break-inside:avoid). Reused across all 4 packages
so the CSS only needs to be right once.
"""

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
    font-size: 12pt;
    line-height: 1.5;
    color: #1a1a1a;
    background: #fff;
    margin: 0;
    padding: 0;
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
  .steps {{ margin: 6px 0; padding-left: 0; list-style: none; }}
  .steps li {{ margin: 4px 0; padding-left: 1.6em; text-indent: -1.6em; }}
  .steps li::before {{ content: attr(data-n) "\\3000"; font-weight: 700; }}
  .write-lines {{ margin-top: 4px; }}
  .write-lines .line {{ height: 0.9cm; border-bottom: 1px solid #aaa; }}
  .write-lines .line:last-child {{ border-bottom: none; }}
  .ans-box {{ display: inline-block; min-width: 110px; border-bottom: 1.5px solid #1a1a1a; height: 1.1em; vertical-align: bottom; }}
  .choices span {{ display: inline-block; margin-right: 22px; }}
  .page-break {{ break-before: page; }}
  .footer {{ font-size: 9pt; color: #666; text-align: center; border-top: 1px solid #999; padding-top: 3px; margin-top: 14px; }}
  .diagram {{ text-align: center; margin: 10px 0; }}
  .diagram svg {{ max-width: 320px; height: auto; }}
  .indent {{ margin-left: 1.4em; }}
</style>
</head>
<body>
<div class="page">
"""

TAIL = """</div>
</body>
</html>
"""

def masthead(subject, unit, doc_type):
    return (f'<div class="masthead"><span>科目：{subject}</span>'
            f'<span>單元：{unit}</span><span>類型：{doc_type}</span></div>')

def ws_meta():
    return ('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>'
            '學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>')

def footer(text):
    return f'<div class="footer">{text}</div>'

def write_lines(n):
    return '<div class="write-lines">' + '<div class="line"></div>' * n + '</div>'

def section_h(text):
    return f'<div class="section-h">{text}</div>'

def stars(level, total=3):
    return f'<span class="stars">{"★"*level}{"☆"*(total-level)}</span>'

def page_head(title):
    return HEAD.format(title=title)

def read_svg(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
