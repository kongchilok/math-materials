# -*- coding: utf-8 -*-
"""共用輔助：路徑、OMML 簡寫、版型小工具"""
import sys, os
SKILL_SCRIPTS = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL_SCRIPTS)
from omml_docx import *  # noqa

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 交付檔資料夾（build/ 的上一層）
FIG = os.path.join(BASE, "figs")
OUT = BASE

def fig(name):
    return os.path.join(FIG, name)

# ---- OMML 簡寫 ----
def M(*parts):
    """('m', omath(...)) segment"""
    return ('m', omath(*parts))

def T(s):
    return ('t', s)

def _frag(x):
    """字串若已是 OMML 片段（以 <m: 開頭）直接用，否則包成 math run"""
    if isinstance(x, str) and not x.lstrip().startswith('<m:'):
        return mr(x)
    return x

def F(a, b):
    """分數，參數可為字串或 OMML 片段"""
    return frac(_frag(a), _frag(b))

def R(s):
    """根號，參數可為字串或片段"""
    return sqrt(_frag(s))

def S2(base):
    """sin²α 這類：base 字串如 'sin'，回傳 sin^2"""
    return sup(mr(base), mr('2'))

# 常用片段
SINA = mr('sin α')
COSA = mr('cos α')
TANA = mr('tan α')

def mc3(a, b, c):
    """三選項選擇題選項列（精簡至3個選項）"""
    segs = []
    for label, opt in zip(('A．', '　　B．', '　　C．'), (a, b, c)):
        segs.append(('t', label))
        if isinstance(opt, str) and opt.lstrip().startswith('<m:'):
            segs.append(('m', opt))
        else:
            segs.append(('t', opt))
    return para(segs)

def hint(segs):
    """單段落提示卡（shaded_box 只能吃一個段落）"""
    return shaded_box([('t', '提示：')] + segs, kind='hint')

def problem(paras, lines=0):
    body = list(paras)
    if lines:
        body += write_lines(lines)
    return problem_box(body)

def tail_to_practice(name):
    return para([('t', f'接下來請拿《{name}》，依照講義範例的四個步驟完成練習A、B、C。')], bold=True)

def head_from_lecture(name):
    return para([('t', f'開始前，先回頭看《{name}》的範例，照著同樣的步驟做。')], bold=True)
