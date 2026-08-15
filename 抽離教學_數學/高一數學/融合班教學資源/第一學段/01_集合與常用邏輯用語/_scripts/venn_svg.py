# -*- coding: utf-8 -*-
"""Small standalone SVG generator for set-relation diagrams (Venn-style),
grayscale only per house style (black lines / light-grey shading, no colour).
Mirrors the approach used for coordinate-plane diagrams in this skill family:
build inline SVG, screenshot via headless Chrome to PNG for docx embedding,
and reuse the raw SVG string directly inside the HTML/PDF track.
"""

FONT = "Noto Sans TC, Microsoft JhengHei, Arial, sans-serif"
GREY_FILL = "#e3e3e3"
BLACK = "#1a1a1a"

def _svg_open(w=320, h=220):
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" font-family="{FONT}">'

def subset_diagram(inner_label='A', outer_label='B', caption=None, w=320, h=220):
    """Small circle (inner_label) fully inside a big circle (outer_label) -> A⊆B."""
    s = [_svg_open(w, h)]
    s.append(f'<rect x="1" y="1" width="{w-2}" height="{h-2}" fill="none" stroke="none"/>')
    cx, cy = w*0.55, h*0.5
    s.append(f'<circle cx="{cx}" cy="{cy}" r="85" fill="#fff" stroke="{BLACK}" stroke-width="1.5"/>')
    s.append(f'<text x="{cx+70}" y="{cy-65}" font-size="16" fill="{BLACK}">{outer_label}</text>')
    icx, icy = cx-18, cy
    s.append(f'<circle cx="{icx}" cy="{icy}" r="42" fill="{GREY_FILL}" stroke="{BLACK}" stroke-width="1.5"/>')
    s.append(f'<text x="{icx-6}" y="{icy+5}" font-size="16" fill="{BLACK}" text-anchor="middle">{inner_label}</text>')
    if caption:
        s.append(f'<text x="{w/2}" y="{h-8}" font-size="13" fill="#555" text-anchor="middle">{caption}</text>')
    s.append('</svg>')
    return ''.join(s)

_RECT_TOP = 10
_RECT_BOTTOM = 190  # fixed rect bottom regardless of total canvas height, so caption never overlaps it

def _two_circles(w, h):
    cy = (_RECT_TOP + _RECT_BOTTOM) / 2
    cx1, cy1, r1 = w*0.40, cy, 62
    cx2, cy2, r2 = w*0.60, cy, 62
    return cx1, cy1, r1, cx2, cy2, r2

def two_set_diagram(mode, label_a='A', label_b='B', universal=True, u_label='U', caption=None, w=320, h=230):
    """mode: 'union' | 'intersection' | 'onlyA' | 'onlyB' | 'plain'
    Shading approximated with clip-paths so only the requested region is grey."""
    cx1, cy1, r1, cx2, cy2, r2 = _two_circles(w, h)
    s = [_svg_open(w, h)]
    uid = f"clipA{abs(hash((mode,label_a,label_b)))%10000}"
    if universal:
        s.append(f'<rect x="10" y="{_RECT_TOP}" width="{w-20}" height="{_RECT_BOTTOM-_RECT_TOP}" fill="#fff" stroke="{BLACK}" stroke-width="1.5"/>')
        s.append(f'<text x="20" y="28" font-size="14" fill="{BLACK}">{u_label}</text>')
    s.append(f'<defs>'
             f'<clipPath id="circA_{uid}"><circle cx="{cx1}" cy="{cy1}" r="{r1}"/></clipPath>'
             f'<clipPath id="circB_{uid}"><circle cx="{cx2}" cy="{cy2}" r="{r2}"/></clipPath>'
             f'</defs>')
    if mode == 'union':
        s.append(f'<circle cx="{cx1}" cy="{cy1}" r="{r1}" fill="{GREY_FILL}"/>')
        s.append(f'<circle cx="{cx2}" cy="{cy2}" r="{r2}" fill="{GREY_FILL}"/>')
    elif mode == 'intersection':
        s.append(f'<circle cx="{cx2}" cy="{cy2}" r="{r2}" fill="{GREY_FILL}" clip-path="url(#circA_{uid})"/>')
    elif mode == 'onlyA':
        s.append(f'<circle cx="{cx1}" cy="{cy1}" r="{r1}" fill="{GREY_FILL}"/>')
        s.append(f'<circle cx="{cx2}" cy="{cy2}" r="{r2}" fill="#fff" clip-path="url(#circA_{uid})"/>')
    elif mode == 'onlyB':
        s.append(f'<circle cx="{cx2}" cy="{cy2}" r="{r2}" fill="{GREY_FILL}"/>')
        s.append(f'<circle cx="{cx1}" cy="{cy1}" r="{r1}" fill="#fff" clip-path="url(#circB_{uid})"/>')
    s.append(f'<circle cx="{cx1}" cy="{cy1}" r="{r1}" fill="none" stroke="{BLACK}" stroke-width="1.5"/>')
    s.append(f'<circle cx="{cx2}" cy="{cy2}" r="{r2}" fill="none" stroke="{BLACK}" stroke-width="1.5"/>')
    s.append(f'<text x="{cx1-38}" y="{cy1-40}" font-size="16" fill="{BLACK}">{label_a}</text>')
    s.append(f'<text x="{cx2+30}" y="{cy2-40}" font-size="16" fill="{BLACK}">{label_b}</text>')
    if caption:
        s.append(f'<text x="{w/2}" y="{_RECT_BOTTOM+20}" font-size="13" fill="#555" text-anchor="middle">{caption}</text>')
    s.append('</svg>')
    return ''.join(s)

def complement_diagram(label_a='A', u_label='U', caption=None, w=320, h=230):
    """Universal-set rectangle shaded grey except a hole for circle A -> complement of A."""
    cx, cy, r = w*0.5, (_RECT_TOP + _RECT_BOTTOM) / 2, 60
    uid = f"holeA{abs(hash((label_a,u_label)))%10000}"
    s = [_svg_open(w, h)]
    s.append(f'<defs><mask id="{uid}"><rect x="0" y="0" width="{w}" height="{h}" fill="#fff"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#000"/></mask></defs>')
    s.append(f'<rect x="10" y="{_RECT_TOP}" width="{w-20}" height="{_RECT_BOTTOM-_RECT_TOP}" fill="#fff" stroke="{BLACK}" stroke-width="1.5"/>')
    s.append(f'<rect x="10" y="{_RECT_TOP}" width="{w-20}" height="{_RECT_BOTTOM-_RECT_TOP}" fill="{GREY_FILL}" mask="url(#{uid})"/>')
    s.append(f'<rect x="10" y="{_RECT_TOP}" width="{w-20}" height="{_RECT_BOTTOM-_RECT_TOP}" fill="none" stroke="{BLACK}" stroke-width="1.5"/>')
    s.append(f'<text x="20" y="28" font-size="14" fill="{BLACK}">{u_label}</text>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{BLACK}" stroke-width="1.5"/>')
    s.append(f'<text x="{cx-5}" y="{cy+5}" font-size="16" fill="{BLACK}" text-anchor="middle">{label_a}</text>')
    if caption:
        s.append(f'<text x="{w/2}" y="{_RECT_BOTTOM+20}" font-size="13" fill="#555" text-anchor="middle">{caption}</text>')
    s.append('</svg>')
    return ''.join(s)

DIAGRAMS = {
    'subset': lambda: subset_diagram('A', 'B', caption='A⊆B：A是B的子集'),
    'implication': lambda: subset_diagram('P', 'Q', caption='p⇒q 對應 P⊆Q（p成立則q一定成立）'),
    'union': lambda: two_set_diagram('union', 'A', 'B', caption='A∪B（灰色部分）'),
    'intersection': lambda: two_set_diagram('intersection', 'A', 'B', caption='A∩B（灰色部分）'),
    'complement': lambda: complement_diagram('A', 'U', caption='∁ᵤA（灰色部分）'),
    'onlyA_notB': lambda: two_set_diagram('onlyA', 'A', 'B', caption='屬於A但不屬於B（灰色部分）'),
}

if __name__ == '__main__':
    import sys, os
    outdir = sys.argv[1] if len(sys.argv) > 1 else '.'
    os.makedirs(outdir, exist_ok=True)
    for name, fn in DIAGRAMS.items():
        svg = fn()
        with open(os.path.join(outdir, f'{name}.svg'), 'w', encoding='utf-8') as f:
            f.write(svg)
        print('wrote', name)
