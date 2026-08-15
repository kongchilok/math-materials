# -*- coding: utf-8 -*-
"""machine_series.svg -> PNG（headless Chrome 截圖）供 docx image_para 內嵌。"""
import os, subprocess, glob

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

def find_chrome():
    for c in CHROME_CANDIDATES:
        if os.path.exists(c):
            return c
    raise RuntimeError("Chrome not found")

def render(svg_path, png_path, w, h, scale=3):
    with open(svg_path, 'r', encoding='utf-8') as f:
        svg = f.read()
    html_path = svg_path + '.html'
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
    html,body{{margin:0;padding:0;overflow:hidden;background:#fff;}}
    .wrap{{width:{w}px;height:{h}px;}}
    svg{{width:{w}px;height:{h}px;}}
    </style></head><body><div class="wrap">{svg}</div></body></html>"""
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    chrome = find_chrome()
    uri = 'file:///' + os.path.abspath(html_path).replace('\\', '/')
    cmd = [chrome, '--headless', '--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage',
           '--hide-scrollbars', f'--force-device-scale-factor={scale}',
           f'--window-size={w},{h}', f'--screenshot={os.path.abspath(png_path)}', uri]
    subprocess.run(cmd, capture_output=True)
    os.remove(html_path)
    if not os.path.exists(png_path) or os.path.getsize(png_path) < 500:
        raise RuntimeError(f'screenshot failed for {svg_path}')

if __name__ == '__main__':
    indir = os.path.dirname(os.path.abspath(__file__))
    for svg_path in glob.glob(os.path.join(indir, '*.svg')):
        name = os.path.basename(svg_path)
        png_path = os.path.join(indir, name.replace('.svg', '.png'))
        render(svg_path, png_path, 540, 150)
        print('rendered', os.path.basename(png_path))
