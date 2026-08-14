# -*- coding: utf-8 -*-
"""06 單元補充內容的共用工具：直接 patch 現有 .docx，不重建整份文件。

做法（與 2026-08-12 改範例段書寫規範同一手法）：
1. 讀原 .docx 的 zip，全部 entry 讀入記憶體；
2. 用單一 <w:t> run 做錨點，`re.finditer(r'<w:t[^>]*>([^<]*)</w:t>', xml)` 找真實
   run 邊界，再往前回溯到該 run 所屬的 <w:p> 開頭 → 插入點；
3. 新內容用 omml_docx 建好；圖片走 MediaRegistry，但**要先把原檔已用的 rIdImgN
   佔位**（不然新圖會拿到 rIdImg1 撞號，Word 會把新圖畫成舊圖）；
4. 重新打包：document.xml、新增的 word/media/*、word/_rels/document.xml.rels，
   [Content_Types].xml 只在原檔沒宣告該副檔名時才補。

原有段落一個字都不改——只在錨點前／sectPr 前插入新的 <w:p>/<w:tbl>。
"""
import os
import re
import shutil
import sys
import zipfile

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
if SKILL not in sys.path:
    sys.path.insert(0, SKILL)

from omml_docx import *                      # noqa: F401,F403
from omml_docx import _tbl, _PAGE_CONTENT_WIDTH  # noqa: F401

_REL_TMPL = ('<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/'
             'officeDocument/2006/relationships/image" Target="media/{rid}.{ext}"/>')


def seeded_registry(existing_rids):
    """建一個已佔位的 MediaRegistry：原檔已用的 rIdImg1..N 先塞進去，
    新圖自然從 rIdImg(N+1) 開始，不會撞號。回傳 (registry, 佔位數)。"""
    media = MediaRegistry()
    for _ in existing_rids:
        media.items.append((f'rIdImg{len(media.items) + 1}', None, 'png'))
    return media, len(existing_rids)


def para_start(xml, run_text, occurrence=0):
    """找出「內容剛好等於 run_text 的那個 <w:t> run」所屬 <w:p> 的起始索引。"""
    hits = [m for m in re.finditer(r'<w:t[^>]*>([^<]*)</w:t>', xml)
            if m.group(1) == run_text]
    if not hits:
        raise SystemExit(f'錨點找不到：{run_text!r}')
    if len(hits) <= occurrence:
        raise SystemExit(f'錨點 {run_text!r} 只有 {len(hits)} 個，取不到第 {occurrence} 個')
    m = hits[occurrence]
    p = xml.rfind('<w:p>', 0, m.start())
    p2 = xml.rfind('<w:p ', 0, m.start())
    start = max(p, p2)
    if start < 0:
        raise SystemExit(f'錨點 {run_text!r} 找不到所屬 <w:p>')
    return start


def guard(src, marker):
    """防呆：同一個補丁跑第二次會變成插兩份。偵測到就直接停。"""
    with zipfile.ZipFile(src) as z:
        xml = z.read('word/document.xml').decode('utf-8')
    if marker in xml:
        raise SystemExit(f'已經含有「{marker}」，補丁已套過一次，不再重複插入。')
    return xml


def patch(src, out, inserts, media, n_seed, backup=True):
    """inserts: [(插入點索引, 新 XML 字串), ...]（索引以原 xml 計，會由後往前插）。"""
    with zipfile.ZipFile(src) as z:
        entries = {n: z.read(n) for n in z.namelist()}

    xml = entries['word/document.xml'].decode('utf-8')
    for pos, frag in sorted(inserts, key=lambda t: -t[0]):
        xml = xml[:pos] + frag + xml[pos:]
    entries['word/document.xml'] = xml.encode('utf-8')

    # --- 新增的圖片檔 ---
    exts = set()
    for i, (rid, path, ext) in enumerate(media.items):
        exts.add(ext)
        if i < n_seed:
            continue                       # 佔位項：原檔已有，原封不動保留
        with open(path, 'rb') as f:
            entries[f'word/media/{rid}.{ext}'] = f.read()

    # --- rels：補上新圖 ---
    rels = entries['word/_rels/document.xml.rels'].decode('utf-8')
    add = ''.join(_REL_TMPL.format(rid=rid, ext=ext)
                  for i, (rid, _p, ext) in enumerate(media.items) if i >= n_seed)
    if add:
        rels = rels.replace('</Relationships>', add + '</Relationships>')
        entries['word/_rels/document.xml.rels'] = rels.encode('utf-8')

    # --- Content_Types：只補原本沒宣告的副檔名 ---
    ct = entries['[Content_Types].xml'].decode('utf-8')
    for ext in sorted(exts):
        if f'Extension="{ext}"' not in ct:
            ctype = 'image/jpeg' if ext in ('jpg', 'jpeg') else f'image/{ext}'
            ct = ct.replace('</Types>',
                            f'<Default Extension="{ext}" ContentType="{ctype}"/></Types>')
    entries['[Content_Types].xml'] = ct.encode('utf-8')

    if backup and os.path.abspath(src) == os.path.abspath(out):
        bak = os.path.splitext(src)[0] + '._tmp_before_patch.docx'
        shutil.copy2(src, bak)

    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in entries.items():
            z.writestr(name, data)
    return out
