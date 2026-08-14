# -*- coding: utf-8 -*-
"""《工具卡_圖像法解不等式手順卡》——D2 手順卡的本體（teaching-designs.md §D2：
「工具卡：要出——這是本設計的本體，學生要能放在桌面」）。

A4 一張排 2×2 ＝兩套（每套：手順卡＋決策卡），虛線＝裁切線，
不放學生資訊列（不是要交回來的作業）。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *      # noqa: F401,F403

OUT = os.path.join(HERE, '工具卡_圖像法解不等式手順卡.docx')

_S = 22          # 卡片本文 11pt
_P = 20          # 易錯點 10pt


def card_steps():
    return [
        para('▍四步手順：圖像法解一元二次不等式', bold=True, sz=HEADING_SZ, spacing=False),
        para('什麼時候翻我：題目出現 ＞ 或 ＜，而式子裡有 {x^2} 時', sz=_P, spacing=False),
        blank(),
        para('① 畫草圖', bold=True, sz=_S, spacing=False),
        para('　把不等號換成等號，解方程求兩個根', sz=_S, spacing=False),
        para('　※ 換成等號只為求交點，這一步還未解完', sz=_P, spacing=False),
        para('② 標兩交點', bold=True, sz=_S, spacing=False),
        para('　兩個根由小到大標在 x 軸上', sz=_S, spacing=False),
        para('　※ 排反了，讀出來的區間就相反', sz=_P, spacing=False),
        para('③ 看開口', bold=True, sz=_S, spacing=False),
        para('　看 {x^2} 的係數 a 是正還是負', sz=_S, spacing=False),
        para('　※ {-x^2+4x-3} 的 a 是 −1，不是 1', sz=_P, spacing=False),
        para('④ 讀區間', bold=True, sz=_S, spacing=False),
        para('　要 {y>0} 讀 x 軸上方，要 {y<0} 讀下方', sz=_S, spacing=False),
        para('　※ 兩段之間寫「或」；一段寫成 p ＜ x ＜ q', sz=_P, spacing=False),
    ]


def card_decision():
    return [
        para('▍決策卡：開口 × 不等號', bold=True, sz=HEADING_SZ, spacing=False),
        para('什麼時候翻我：草圖畫好了，要決定讀哪一段時', sz=_P, spacing=False),
        para('（p、q 是兩個根，p ＜ q）', sz=_P, spacing=False),
        blank(),
        para('開口向上　＋　＞ 0　→　取兩邊', bold=True, sz=_S, spacing=False),
        para('　　x ＜ p 或 x ＞ q', sz=_S, spacing=False),
        para('開口向上　＋　＜ 0　→　取中間', bold=True, sz=_S, spacing=False),
        para('　　p ＜ x ＜ q', sz=_S, spacing=False),
        para('開口向下　＋　＞ 0　→　取中間', bold=True, sz=_S, spacing=False),
        para('　　p ＜ x ＜ q', sz=_S, spacing=False),
        para('開口向下　＋　＜ 0　→　取兩邊', bold=True, sz=_S, spacing=False),
        para('　　x ＜ p 或 x ＞ q', sz=_S, spacing=False),
        blank(),
        para('※ 核對用的記法：向上配 ＞ 0、向下配 ＜ 0 就取兩邊；'
             '配不起來就取中間。', sz=_P, spacing=False),
        para('※ 記法只用來核對，答題仍然先畫草圖。', sz=_P, spacing=False),
    ]


P = [masthead('初三數學', '二次函數與方程及應用', '工具卡'),
     para('沿虛線剪下、護貝，做題時放在作業本旁邊，手指指住正在做的那一步。'
          '（每張 A4 兩套，可供兩位同學使用）', sz=_P),
     toolcard_sheet([card_steps(), card_decision(),
                     card_steps(), card_decision()], cols=2, card_h=4200)]

print(build_docx(P, OUT, footer_text='初三數學．二次函數與方程及應用單元'))
