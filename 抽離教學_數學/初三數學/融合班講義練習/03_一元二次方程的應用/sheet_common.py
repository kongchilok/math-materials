# -*- coding: utf-8 -*-
"""
sheet_common.py — 初三一元二次方程「數字問題」調適練習 版面層

由高三文資料夾同名檔複製而來（2026-09-24），唯一改動：SUBJECT。
OMML／docx 封裝底層沿用 similar-practice-generator\\scripts\\omml_docx.py
（→ _shared-math-docx\\omml_core.py），本檔不複製底層任何嘢。

集合記號慣例（跟 house-style「集合建構式」一節）：
  建構式 ｛x｜條件｝ 的大括號與豎線用全形，只把變數與條件包進 {}。
  列舉式 ｛1, 2, 3｝ 同樣用全形大括號，元素包進 {}（負號才會變數學減號）。
"""
import os
import re
import sys

SKILL = r"C:\Users\KongChiLok\.claude\skills\similar-practice-generator\scripts"
if SKILL not in sys.path:
    sys.path.insert(0, SKILL)

from omml_docx import *          # noqa: F401,F403
from omml_docx import _run       # noqa: F401  star-import 跳過底線開頭嘅名

HERE = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學'
INNER_W = 11338 - 240            # problem_box 內容寬（左右內邊距各 120）


# ---------------- 集合記號 ----------------
def S(var, cond):
    """建構式：S('x', '0≤x<3') → '｛{x}｜{0≤x<3}｝'。
    cond 內可用「或」「且」等中文，會自動拆開只把算式包進 {}。"""
    parts = re.split(r'(或|且)', cond)
    body = ''.join(p if p in ('或', '且') else '{' + p.strip() + '}'
                   for p in parts if p.strip())
    body = body.replace('}或{', '} 或 {').replace('}且{', '} 且 {')
    return f'｛{{{var}}}｜{body}｝'


def L(items):
    """列舉式：L('-2, -1, 0') → '｛{−2, −1, 0}｝'。"""
    return f'｛{{{items}}}｝'


# ---------------- 選項 ----------------
def _plain_len(s):
    """估算選項顯示寬度（中文／全形算 2，其他算 1）。"""
    t = re.sub(r'frac\(([^,]*),([^)]*)\)', r'\1\2', s)
    t = t.replace('{', '').replace('}', '').replace('sqrt', '√')
    return sum(2 if ord(c) > 0x2E7F else 1 for c in t)


def opts(items, cols=None, sz=BODY_SZ):
    """選項（4 或 5 個）排成無框表格。cols 不指定時按最長選項自動揀欄數。"""
    labels = 'ABCDE'
    if cols is None:
        m = max(_plain_len(x) for x in items)
        n = len(items)
        cols = n if m <= (14 if n == 4 else 11) else (3 if m <= 24 and n == 5 else (2 if m <= 40 else 1))
    w = INNER_W // cols
    rows = [items[i:i + cols] for i in range(0, len(items), cols)]
    trs = ''
    for r_i, r in enumerate(rows):
        tcs = ''
        for c_i, it in enumerate(r):
            lab = labels[r_i * cols + c_i]
            p = para(f'{lab}．{it}', sz=sz, ind=0)
            p = p.replace('w:after="80"', 'w:after="0"')
            tcs += (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/></w:tcPr>{p}</w:tc>')
        for _ in range(cols - len(r)):
            tcs += f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/></w:tcPr><w:p/></w:tc>'
        trs += f'<w:tr>{tcs}</w:tr>'
    grid = ''.join(f'<w:gridCol w:w="{w}"/>' for _ in range(cols))
    return ('<w:tbl><w:tblPr>'
            f'<w:tblW w:w="{w * cols}" w:type="dxa"/>'
            '<w:tblInd w:w="300" w:type="dxa"/>'
            '<w:tblBorders><w:top w:val="nil"/><w:left w:val="nil"/><w:bottom w:val="nil"/>'
            '<w:right w:val="nil"/><w:insideH w:val="nil"/><w:insideV w:val="nil"/></w:tblBorders>'
            '<w:tblLayout w:type="fixed"/>'
            '<w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="60" w:type="dxa"/></w:tblCellMar>'
            f'</w:tblPr><w:tblGrid>{grid}</w:tblGrid>{trs}</w:tbl>')


def tight(p):
    """拿掉 para() 預設段後 8pt，行距 1.5 倍不動。"""
    return p.replace('w:after="80"', 'w:after="0"')


def hint(text):
    """提示條：淺灰底＋深灰左粗條（house-style 提示卡樣式），11pt。"""
    return tight(shaded_box('提示：' + text, sz=22))


def hint_multi(lines):
    """多行提示：第一行冠「提示：」，其餘縮排對齊。"""
    out = [tight(shaded_box('提示：' + lines[0], sz=22))]
    for ln in lines[1:]:
        out.append(tight(shaded_box('　　　' + ln, sz=22)))
    return out


# ---------------- 題框 ----------------
def box(paragraphs, thick=False, keep=True):
    """題框。thick=True → 粗框（2.25pt）用來標記「與大測高度相似」的題目
    （使用者 2026-09-21 指定：相似題用粗框框住）。
    keep=True → 整格不跨頁（cantSplit），避免題目與提示被分到兩頁。"""
    # 確保儲存格最後一個元素是段落（Word 規定）
    if paragraphs and paragraphs[-1].lstrip().startswith('<w:tbl'):
        paragraphs = paragraphs + ['<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="120" w:lineRule="auto"/></w:pPr></w:p>']
    tbl = problem_box(paragraphs, trailing_blank=False)
    if thick:
        tbl = tbl.replace('<w:tblBorders>', '<w:tblBorders>', 1)
        head, rest = tbl.split('</w:tblBorders>', 1)
        head = head.replace('w:sz="4"', 'w:sz="18"')
        tbl = head + '</w:tblBorders>' + rest
    if keep:
        tbl = tbl.replace('<w:tr><w:tc>', '<w:tr><w:trPr><w:cantSplit/></w:trPr><w:tc>', 1)
    return tbl + spacer()


def spacer(h=160):
    return (f'<w:p><w:pPr><w:spacing w:line="{h}" w:lineRule="exact" '
            'w:before="0" w:after="0"/></w:pPr></w:p>')


def lines(n):
    return write_lines(n)


def tail_stub():
    return ('<w:p><w:pPr><w:spacing w:line="100" w:lineRule="auto" '
            'w:before="0" w:after="0"/></w:pPr>'
            '<w:r><w:rPr><w:sz w:val="2"/><w:szCs w:val="2"/></w:rPr>'
            '<w:t xml:space="preserve"> </w:t></w:r></w:p>')


# ---------------- 文氏圖 ----------------
def venn_png(path, corner='U', corner_pos='tl'):
    """陰影＝A 去掉 B（A∩∁B）的文氏圖，黑白灰階。corner＝全集標籤。"""
    if os.path.exists(path):
        return path
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle, Rectangle
    fig, ax = plt.subplots(figsize=(3.0, 1.9), dpi=200)
    ax.set_xlim(0, 3.0); ax.set_ylim(0, 1.9); ax.axis('off')
    ax.add_patch(Rectangle((0.05, 0.05), 2.9, 1.8, fill=False, lw=1.2, ec='black'))
    ca, cb = (1.15, 0.95), (1.85, 0.95)
    r = 0.62
    ax.add_patch(Circle(ca, r, fc='#C8C8C8', ec='none'))
    ax.add_patch(Circle(cb, r, fc='white', ec='none'))
    ax.add_patch(Circle(ca, r, fill=False, ec='black', lw=1.2))
    ax.add_patch(Circle(cb, r, fill=False, ec='black', lw=1.2))
    kw = dict(fontsize=15, fontstyle='italic', family='serif', ha='center', va='center')
    ax.text(0.85, 0.95, 'A', **kw)
    ax.text(2.15, 0.95, 'B', **kw)
    cx, cy = (0.22, 1.66) if corner_pos == 'tl' else (0.22, 0.24)
    ax.text(cx, cy, corner, fontsize=14, family='serif',
            fontstyle='italic' if corner == 'U' else 'normal', ha='center', va='center')
    fig.savefig(path, dpi=200, bbox_inches='tight', pad_inches=0.02, facecolor='white')
    plt.close(fig)
    return path


# ---------------- 框架（高三文調適練習新增） ----------------
def dense(p):
    """鷹架段落行距 1.5 → 1.2 倍（題幹仍保持 house-style 1.5 倍），使用者要求壓頁數。"""
    return p.replace('w:line="360"', 'w:line="288"')

def scaf(formula=(), steps=(), fsz=22):
    """題下灰底條：先列「公式」，再列「框架」（步驟填空）。
    相鄰灰底段落 Word 會合併成一塊，正是想要的效果。"""
    out = []
    for i, f in enumerate(formula):
        out.append(dense(tight(shaded_box(('公式：' if i == 0 else '　　　') + f, sz=fsz))))
    for i, t in enumerate(steps):
        out.append(dense(tight(shaded_box(('框架：' if i == 0 else '　　　') + t, sz=fsz))))
    return out


def _cell(content, w, sz, jc, shade=False, vmid=True):
    if isinstance(content, str):
        ps = dense(tight(para(content, sz=sz, jc=jc))) if content else '<w:p/>'
    else:  # 已是段落 XML 清單
        ps = ''.join(content) or '<w:p/>'
    tcpr = f'<w:tcW w:w="{w}" w:type="dxa"/>'
    if shade:
        tcpr += '<w:shd w:val="clear" w:color="auto" w:fill="EDEDED"/>'
    if vmid:
        tcpr += '<w:vAlign w:val="center"/>'
    return f'<w:tc><w:tcPr>{tcpr}</w:tcPr>{ps}</w:tc>'


def grid(rows, widths, sz=22, head_row=True, head_col=True, row_h=None, jc='center', ind=300):
    """框架表格（單線框）。rows＝list of list（字串可含 {} 數學；'' ＝留空給學生填）。
    head_row／head_col：首列／首欄加淺灰底當表頭。row_h：固定列高（twips）。"""
    trs = ''
    for r_i, r in enumerate(rows):
        tcs = ''
        for c_i, c in enumerate(r):
            shade = (head_row and r_i == 0) or (head_col and c_i == 0)
            tcs += _cell(c, widths[c_i], sz, jc, shade=shade)
        trpr = f'<w:trPr><w:trHeight w:val="{row_h}" w:hRule="atLeast"/></w:trPr>' if row_h else ''
        trs += f'<w:tr>{trpr}{tcs}</w:tr>'
    gridc = ''.join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    b = 'w:val="single" w:sz="4" w:space="0" w:color="000000"'
    return ('<w:tbl><w:tblPr>'
            f'<w:tblW w:w="{sum(widths)}" w:type="dxa"/>'
            f'<w:tblInd w:w="{ind}" w:type="dxa"/>'
            f'<w:tblBorders><w:top {b}/><w:left {b}/><w:bottom {b}/><w:right {b}/>'
            f'<w:insideH {b}/><w:insideV {b}/></w:tblBorders>'
            '<w:tblLayout w:type="fixed"/>'
            '<w:tblCellMar><w:left w:w="60" w:type="dxa"/><w:right w:w="60" w:type="dxa"/></w:tblCellMar>'
            f'</w:tblPr><w:tblGrid>{gridc}</w:tblGrid>{trs}</w:tbl>')


def side_by_side(left, right, wl, wr, ind=300):
    """左右兩格、無框線。left／right 為段落或表格 XML 清單。
    儲存格若以表格結尾，Word 規定要補一個空段落。"""
    def fix(xs):
        xs = list(xs)
        if not xs or xs[-1].lstrip().startswith('<w:tbl'):
            xs.append('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="120" w:lineRule="auto"/></w:pPr></w:p>')
        return ''.join(xs)
    return ('<w:tbl><w:tblPr>'
            f'<w:tblW w:w="{wl + wr}" w:type="dxa"/><w:tblInd w:w="{ind}" w:type="dxa"/>'
            '<w:tblBorders><w:top w:val="nil"/><w:left w:val="nil"/><w:bottom w:val="nil"/>'
            '<w:right w:val="nil"/><w:insideH w:val="nil"/><w:insideV w:val="nil"/></w:tblBorders>'
            '<w:tblLayout w:type="fixed"/>'
            '<w:tblCellMar><w:left w:w="0" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tblCellMar>'
            f'</w:tblPr><w:tblGrid><w:gridCol w:w="{wl}"/><w:gridCol w:w="{wr}"/></w:tblGrid>'
            f'<w:tr><w:tc><w:tcPr><w:tcW w:w="{wl}" w:type="dxa"/><w:vAlign w:val="center"/></w:tcPr>{fix(left)}</w:tc>'
            f'<w:tc><w:tcPr><w:tcW w:w="{wr}" w:type="dxa"/><w:vAlign w:val="center"/></w:tcPr>{fix(right)}</w:tc></w:tr></w:tbl>')
