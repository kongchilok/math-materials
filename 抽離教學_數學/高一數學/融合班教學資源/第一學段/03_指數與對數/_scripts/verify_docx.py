# -*- coding: utf-8 -*-
"""Round-trip verifier: opens a docx we generated, confirms it's structurally
valid, and renders every OMML equation back to a linear ASCII form so we can
eyeball whether the math content is what we intended. Flags any sSup whose
base is a compound (non-single-run) expression that ISN'T already wrapped in
literal parens -- that's the bug class we keep hitting (exponent placed on a
frac/rad/nested-sup without explicit grouping parens)."""
import sys, zipfile
from lxml import etree
import docx

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def is_simple(el):
    kids = list(el)
    if len(kids) != 1:
        return False
    return etree.QName(kids[0]).localname == 'r'

def render_math(el):
    tag = etree.QName(el).localname
    if tag in ('oMath', 'oMathPara'):
        return ''.join(render_math(c) for c in el)
    if tag == 'r':
        return ''.join(render_math(c) for c in el if etree.QName(c).localname == 't')
    if tag == 't':
        return el.text or ''
    if tag == 'f':
        num = el.find('{*}num'); den = el.find('{*}den')
        return '(' + render_math(num) + ')/(' + render_math(den) + ')'
    if tag in ('num', 'den', 'sub', 'sup', 'deg'):
        return ''.join(render_math(c) for c in el)
    if tag == 'e':
        return ''.join(render_math(c) for c in el)
    if tag == 'sSup':
        e = el.find('{*}e'); sup = el.find('{*}sup')
        base = render_math(e)
        if not is_simple(e):
            base = '[[' + base + ']]'
        return base + '^(' + render_math(sup) + ')'
    if tag == 'sSub':
        e = el.find('{*}e'); sub = el.find('{*}sub')
        return render_math(e) + '_(' + render_math(sub) + ')'
    if tag == 'rad':
        deg = el.find('{*}deg'); e = el.find('{*}e')
        degtxt = render_math(deg) if deg is not None else ''
        return ('sqrt[' + degtxt + '](' if degtxt else 'sqrt(') + render_math(e) + ')'
    return ''.join(render_math(c) for c in el)

def dump(path):
    d = docx.Document(path)
    print(f"[OK] {path}, paragraphs={len(d.paragraphs)}")
    with zipfile.ZipFile(path) as z:
        xml = z.read('word/document.xml')
    root = etree.fromstring(xml)
    flagged = 0
    for p in root.iter(W + 'p'):
        line = []
        for child in p:
            t = etree.QName(child).localname
            if t == 'r':
                for tt in child.findall('.//' + W + 't'):
                    line.append(tt.text or '')
            elif t in ('oMath', 'oMathPara'):
                rendered = render_math(child)
                if '[[' in rendered:
                    flagged += 1
                line.append('$' + rendered + '$')
        txt = ''.join(line).strip()
        if txt:
            print(txt)
    print(f"--- possibly-unparenthesized compound sup bases flagged: {flagged} (inspect above) ---")

if __name__ == '__main__':
    for f in sys.argv[1:]:
        print("=" * 100); print(f); print("=" * 100)
        dump(f)
        print()
