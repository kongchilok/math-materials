# qa_decks.py — 教學簡報批量機械 QA（PyMuPDF）
# 用法：python qa_decks.py [PDF檔名關鍵字...]      不給參數＝掃資料夾內全部 deck PDF
#      python qa_decks.py --png L2:5,11            指定把某 deck 某幾頁出 PNG 俾人目視
#
# 抓四類問題：① 文字塊超出頁面邊界（溢出）② 文字塊貼邊（<0.35" 邊界）
#            ③ 近乎空白頁（<15 字）④ 字元稽核（豆腐格常見的 Unicode 修飾字元）
import sys, os, glob, re

import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
DECK_DIR = os.path.abspath(os.path.join(HERE, '..'))
MARGIN_PT = 0.35 * 72          # 硬規則 0.5"，留 0.35" 作告警線
BAD_CHARS = set('ᵤᵥᵦᵧₐₑₒₓ')   # 三大字型皆無 → 必出豆腐

def audit(pdf_path):
    doc = fitz.open(pdf_path)
    name = os.path.basename(pdf_path)
    issues = []
    for i, page in enumerate(doc, 1):
        R = page.rect
        for b in page.get_text('blocks'):
            x0, y0, x1, y1, txt = b[0], b[1], b[2], b[3], b[4].strip()
            if not txt:
                continue
            head = txt.replace('\n', ' ')[:24]
            if x1 > R.x1 + 1 or x0 < R.x0 - 1 or y1 > R.y1 + 1 or y0 < R.y0 - 1:
                issues.append(f'  p{i:>2} 溢出頁面  「{head}」  bbox=({x0:.0f},{y0:.0f})-({x1:.0f},{y1:.0f})')
            # 頁尾帶（底 0.55"）內嘅文字框橫跨全頁係正常版型（左標籤＋右頁碼），唔當貼邊
            elif y0 < R.y1 - 0.55 * 72 and (x1 > R.x1 - MARGIN_PT or x0 < R.x0 + MARGIN_PT):
                issues.append(f'  p{i:>2} 貼近左右邊界  「{head}」  x=({x0:.0f}..{x1:.0f}) / 頁寬 {R.x1:.0f}')
        t = page.get_text().strip()
        if len(t) < 15:
            issues.append(f'  p{i:>2} 近乎空白（{len(t)} 字）')
        bad = BAD_CHARS & set(t)
        if bad:
            issues.append(f'  p{i:>2} 有豆腐風險字元：{"".join(sorted(bad))}')
    print(f'{name}  [{doc.page_count} 頁]  ' + ('OK' if not issues else f'{len(issues)} 項待查'))
    for s in issues:
        print(s)
    doc.close()
    return len(issues)

def render(spec):
    out = os.path.join(DECK_DIR, '_verify_png')
    os.makedirs(out, exist_ok=True)
    for part in spec.split(';'):
        key, pages = part.split(':')
        hits = glob.glob(os.path.join(DECK_DIR, f'*{key}*.pdf'))
        if not hits:
            print(f'找唔到 {key} 嘅 PDF'); continue
        doc = fitz.open(hits[0])
        for pn in [int(x) for x in pages.split(',')]:
            f = os.path.join(out, f'{key}_p{pn:02d}.png')
            doc[pn - 1].get_pixmap(dpi=110).save(f)
            print('rendered', f)
        doc.close()

if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--png':
        render(args[1])
    else:
        pdfs = sorted(glob.glob(os.path.join(DECK_DIR, '簡報_*.pdf')))
        if args:
            pdfs = [p for p in pdfs if any(a in os.path.basename(p) for a in args)]
        total = sum(audit(p) for p in pdfs)
        print(f'\n=== 共 {len(pdfs)} 份 deck，{total} 項待查 ===')
