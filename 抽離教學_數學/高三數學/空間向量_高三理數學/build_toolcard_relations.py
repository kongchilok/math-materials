# -*- coding: utf-8 -*-
# 工具卡（D7 判定定理卡）—— 空間向量判定定理卡
# 2026-08-10 新增：向量法判斷直線與平面的位置關係／空間角／空間中的距離
# 三課共用，四張卡涵蓋線面、面面的平行與垂直判定，配合教學設計主D7使用。
import sys, os
sys.path.insert(0, r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts")
from omml_docx import *

OUT = os.path.dirname(os.path.abspath(__file__))
FOOTER = '高三數學．空間向量單元．工具卡'

P = []
P.append(masthead('高三數學', '空間向量判定定理卡', '工具卡'))
P.append(blank())

cards = [
    [reference_card(
        '線面垂直判定',
        '題目要求／已知「直線 l ⊥ 平面 α」',
        '直線 l 的方向向量 {vec(v)} 與平面 α 的法向量 {vec(n)} 平行：',
        '{vec(v)∥vec(n)} ⟺ {l⊥α}',
    )],
    [reference_card(
        '線面平行判定',
        '題目要求／已知「直線 l ∥ 平面 α」（且 l 不在 α 內）',
        '直線 l 的方向向量 {vec(v)} 與平面 α 的法向量 {vec(n)} 垂直：',
        '{vec(v)·vec(n)=0} ⟺ {l∥α}　（要另外確認 l 不在 α 內）',
    )],
    [reference_card(
        '面面垂直判定',
        '題目要求／已知「平面 α ⊥ 平面 β」',
        '兩平面的法向量 {vec(n_1)}、{vec(n_2)} 互相垂直：',
        '{vec(n_1)·vec(n_2)=0} ⟺ {α⊥β}',
    )],
    [reference_card(
        '面面平行判定',
        '題目要求／已知「平面 α ∥ 平面 β」',
        '兩平面的法向量 {vec(n_1)}、{vec(n_2)} 互相平行：',
        '{vec(n_1)∥vec(n_2)} ⟺ {α∥β}',
    )],
]
P.append(toolcard_sheet(cards, cols=2))
P.append(blank())
P.append(shaded_box('※ 四張卡的共通提醒：法向量／方向向量都不是唯一的（任何非零倍數都仍然是），但「方向」是唯一確定的——判斷平行/垂直只看方向，不用管長度或正負號。', kind='worked'))

out = build_docx(
    P,
    os.path.join(OUT, '工具卡_空間向量判定定理卡.docx'),
    footer_text=FOOTER,
)
print(out)
