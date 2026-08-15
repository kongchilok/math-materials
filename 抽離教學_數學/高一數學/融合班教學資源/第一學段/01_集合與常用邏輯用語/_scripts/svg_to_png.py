# -*- coding: utf-8 -*-
"""Wrap each .svg in a tight HTML page and screenshot it with headless Chrome
to produce a PNG usable for docx embedding (image_para in omml_docx.py)."""
import os, sys, subprocess, glob

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

def find_chrome():
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    raise RuntimeError("Chrome not found")

def render(svg_path, png_path, w=340, h=240, scale=3):
    with open(svg_path, 'r', encoding='utf-8') as f:
        svg = f.read()
    html_path = svg_path + '.html'
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    html,body{{margin:0;padding:0;overflow:hidden;background:#fff;}}
    .wrap{{width:{w}px;height:{h}px;}}
    </style></head><body><div class="wrap">{svg}</div></body></html>"""
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    chrome = find_chrome()
    uri = 'file:///' + os.path.abspath(html_path).replace('\\', '/')
    cmd = [chrome, '--headless', '--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage',
           '--hide-scrollbars', f'--force-device-scale-factor={scale}',
           f'--window-size={w},{h}', f'--screenshot={os.path.abspath(png_path)}', uri]
    subprocess.run(cmd, check=True, capture_output=True)
    os.remove(html_path)

if __name__ == '__main__':
    indir = sys.argv[1] if len(sys.argv) > 1 else 'svgs'
    outdir = sys.argv[2] if len(sys.argv) > 2 else 'svgs'
    for svg_path in glob.glob(os.path.join(indir, '*.svg')):
        name = os.path.splitext(os.path.basename(svg_path))[0]
        png_path = os.path.join(outdir, f'{name}.png')
        render(svg_path, png_path)
        print('rendered', png_path)
