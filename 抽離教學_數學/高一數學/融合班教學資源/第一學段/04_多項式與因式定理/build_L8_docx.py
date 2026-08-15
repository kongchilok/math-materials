# -*- coding: utf-8 -*-
"""高一 L8《二次函數與一元二次不等式》講義／練習 docx 產檔。

教學設計：D2 手順卡（主）＋ D5 圖文雙軌對照、D12 自我核對（輔）
鷹架密度：全班共用（Tier 1）
取材：教學簡報 簡報_L8_一元二次不等式.pptx 的「四步走」，本份擴成五步——
      把「畫草圖」獨立成一步，因為使用者要求學生在練習裡也要能模仿畫圖。
house-style：範例段一律 worked_example_table()＋eq_row/or_row/span_row/answer_row。

⚠ 集合建構式不能用半形 {x | ...} 寫：`{}` 是數學標記的界定符，`|` 會被當成
   絕對值而拋 MathParseError（實測）。一律用全形 ｛ ｜ ｝，只把不等式本身
   包進 {} 標記裡。
"""
import os
import sys

SKILL = r'C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts'
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _tbl, _PAGE_CONTENT_WIDTH  # star-import 跳過底線開頭的名字
import design_svg as ds

BASE = os.path.dirname(os.path.abspath(__file__))
SUBJ = '高一數學'
UNIT = '二次函數與一元二次不等式'
FOOT = '高一數學．二次函數與一元二次不等式'

# ---------------------------------------------------------------- 草圖（暫存 PNG，收尾刪）
FIGS = {}


def fig(name, **kw):
    """產一張草圖 PNG，回傳路徑。檔名一律 _tmp 前綴＝暫存紀律。"""
    path = os.path.join(BASE, f'_tmp_L8_{name}.png')
    if name not in FIGS:
        ds.svg_to_png(ds.sketch_parabola(**kw), path, scale=3)
        FIGS[name] = path
    return path


# ---------------------------------------------------------------- 手順卡（D2 主設計）
CARD = dict(
    title='解一元二次不等式　五步',
    trigger='題目是 ax²+bx+c ＞ 0（或 ＜、≥、≤）這種二次不等式',
    steps=[
        ('把所有項搬到一邊，讓右邊變成 0', '過等號要變號；右邊不是 0 就不能往下做'),
        ('看二次項係數 a 的正負；a 是負數就整條乘 −1', '乘負數，不等號一定要反向——這一步最易漏'),
        ('把不等號換成等號，解方程求根，數清楚有幾個根', '因式分解或用公式；Δ 決定有 2 個、1 個還是 0 個根'),
        ('畫草圖：開口向上，在 x 軸標出根', '只畫 x 軸和拋物線，不用畫 y 軸、不用畫格線'),
        ('對照草圖挑範圍，用「∴」寫成解集', '大於取兩邊，小於取中間'),
    ],
    fading='完整五步卡 → 只留「先變 0、再看 a、畫草圖」三句 → 只問「這題的草圖長什麼樣」→ 移除',
)

# D12 自我核對清單——**放在練習端**（teaching-designs.md D12：講義長相「不出現」，
# 練習長相「每個 A／B／C 區塊末尾一個核對清單；區塊之間放核對點分隔」）。
# 項目一律可觀察、能自己判定，不寫「我有認真做」這種無法自我判定的話。
CHECK_A = [
    '每題都寫了算式，不是只寫答案',
    '每題都畫了草圖：有 x 軸、有拋物線、根已標在軸上',
    '解集用 ｛x ｜ … ｝ 寫；分成兩段的中間有寫「或」',
]
CHECK_B = [
    '每題都先算了 Δ',
    '數清楚有幾個根（2 個、1 個、還是 0 個），草圖也照樣畫',
    '「無解」和「全部實數」沒有寫反',
]
# C 區的清單刻意壓成兩項：第 9 題框之後頁底只剩約一行半的空間，三項會把整塊
# 推到下一頁、留一頁近乎全白（實測）。合併前兩項比犧牲作答行數划算。
CHECK_C = [
    'a 是負數的題目，已經乘 −1 並反向；草圖畫的是乘完之後那一條',
    '應用題的答案有寫回一段時間，不是只留一個不等式',
]


# ================================================================ 講義
def build_handout():
    P, media = [], MediaRegistry()
    P.append(masthead(SUBJ, UNIT, '課堂講義'))
    P.append(student_info_row())

    # ---- 導入：從方程到不等式
    P.append(heading('一、由「等於 0」走到「大於 0」'))
    P.append(para('上一課解過方程 {x^2-5x+6=0}，答案是 {x_1=2} 或 {x_2=3}——兩個數。'))
    P.append(para('這一課問的是不等式 {x^2-5x+6>0}。答案不再是幾個數，而是一整段範圍。'))
    P.append(shaded_box('解一元二次不等式 ＝ 看二次函數的圖象落在 x 軸的哪一邊。'))
    P.append(problem_box([
        para('圖象在 x 軸上方　→　y ＞ 0', spacing=False),
        para('圖象在 x 軸下方　→　y ＜ 0', spacing=False),
        para('圖象碰到 x 軸　　→　y ＝ 0（那一點就是根）', spacing=False),
    ]))

    # ---- 二、草圖怎麼畫、怎麼讀（D5 圖文雙軌）
    P.append(heading('二、草圖怎麼畫、怎麼讀'))
    P.append(para('草圖只要三樣東西：一條 x 軸、一條拋物線、軸上的根。'
                  '不用畫 y 軸、不用畫格線、不用算頂點——三秒畫得完才有用。'))
    P.append(para('以 {y=x^2-5x+6} 為例（根是 2 和 3，{a=1>0} 所以開口向上）：',
                  keep_next=True))
    P.append(dual_track_table([
        (image_para(fig('read_pos', roots=(2, 3), opening='up', show_sign=True,
                        caption='兩根之外：線在 x 軸上方'), width_cm=6.4),
         [para('{x<2} 或 {x>3} 這兩段，線在 x 軸上方', spacing=False),
          para('所以 {y>0}', bold=True, spacing=False)]),
        (image_para(fig('read_neg', roots=(2, 3), opening='up', solution='inside',
                        caption='兩根之間：線在 x 軸下方'), width_cm=6.4),
         [para('{2<x<3} 這一段，線在 x 軸下方', spacing=False),
          para('所以 {y<0}', bold=True, spacing=False)]),
    ], media=media, headers=('草圖上看到什麼', '寫成什麼')))
    P.append(blank())
    P.append(shaded_box('所以同一幅草圖可以回答兩種問題：問 ＞ 0 就取兩邊，問 ＜ 0 就取中間。'))

    # ---- 三、根有幾個：Δ 決定草圖長什麼樣
    P.append(heading('三、根有幾個？判別式 Δ 決定草圖長什麼樣', page_break_before=True))
    P.append(para('待會手順卡的第 3 步要「數清楚有幾個根」，靠的就是判別式 '
                  '{Δ=b^2-4ac}（此處 {a>0}）：'))
    P.append(_delta_table(media))
    P.append(blank())
    P.append(shaded_box('Δ ＝ 0 和 Δ ＜ 0 這兩欄，答案常常是「全部實數」或「無解」，'
                        '不要以為一定要寫出兩個數才叫答案。'))

    # ---- 四、手順卡
    P.append(heading('四、手順卡：解一元二次不等式五步', page_break_before=True))
    P.append(step_card(**CARD))
    P.append(blank())

    # ---- 五、範例一
    P.append(heading('五、範例'))
    P.append(para('★ 範例一：解 {x^2-5x+6>0}', bold=True, keep_next=True))
    P.append(worked_example_table([
        eq_row('{x^2-5x+6}', '{0}',
               '第 1 步：右邊已經是 0，不用搬。第 2 步：{a=1}，是正數，不用乘 −1',
               rel='{>}'),
        eq_row('{x^2-5x+6}', '{0}', '第 3 步：把不等號換成等號，先求根'),
        eq_row('{(x-2)(x-3)}', '{0}', '因式分解'),
        or_row('{x-2}', '{0}', '{x-3}', '{0}', '分成兩支寫，中間寫「或」'),
        or_row('{x_1}', '{2}', '{x_2}', '{3}', '兩個不相等的根'),
    ], why_pct=0.40))
    P.append(_fig_step45(media, 'ex1', dict(roots=(2, 3), opening='up', solution='outside',
                                            caption='開口向上，根是 2 和 3'),
                         '第 4 步：畫草圖，標出兩個根',
                         '第 5 步：問的是 ＞ 0，取 x 軸上方那兩段（粗線）'))
    P.append(worked_example_table([
        answer_row('解集為 ｛x ｜ {x<2} 或 {x>3}｝', '作答：最後一行用「∴」寫出解集'),
    ], why_pct=0.40))
    P.append(blank())

    # ---- 範例二（a 是負數）
    P.append(para('★ 範例二：解 {-x^2+4x-3>0}（二次項係數是負數）', bold=True,
                  keep_next=True, page_break_before=True))
    P.append(worked_example_table([
        eq_row('{-x^2+4x-3}', '{0}', '第 1 步：右邊已經是 0', rel='{>}'),
        span_row('{a=-1}',
                 '第 2 步：a 是負數 → 整條乘 −1，而且不等號要反向。這一步最易漏'),
        eq_row('{x^2-4x+3}', '{0}', '乘 −1 之後：＞ 變成 ＜', rel='{<}'),
        eq_row('{x^2-4x+3}', '{0}', '第 3 步：把不等號換成等號，先求根'),
        eq_row('{(x-1)(x-3)}', '{0}', '因式分解'),
        or_row('{x-1}', '{0}', '{x-3}', '{0}', '分成兩支寫，中間寫「或」'),
        or_row('{x_1}', '{1}', '{x_2}', '{3}', '兩個不相等的根'),
    ], why_pct=0.40))
    P.append(_fig_step45(media, 'ex2', dict(roots=(1, 3), opening='up', solution='inside',
                                            caption='乘 −1 之後 a ＞ 0，開口向上'),
                         '第 4 步：畫的是乘 −1 之後那條的草圖',
                         '第 5 步：現在問的是 ＜ 0，取 x 軸下方那一段（粗線）'))
    P.append(worked_example_table([
        answer_row('解集為 ｛x ｜ {1<x<3}｝', '作答：只有一段，不用寫「或」'),
    ], why_pct=0.40))
    P.append(blank())

    P.append(para('接下來請拿《二次函數與一元二次不等式 —— 課堂練習》，'
                  '依這套五步框架完成練習 A、B、C。'))

    # ---- 教師實施說明
    P += teacher_notes(
        main_design='D2 手順卡（五步）',
        aux_designs=('D5 圖文雙軌對照（草圖 ↔ 解集逐列對齊）', 'D12 自我核對清單'),
        reason='本課屬 S2 多步驟程序運算（序列崩潰、漏「乘負數要反向」）疊 S4 函數與圖像'
               '（圖象與解集的對應無法內化）。瓶頸在前端的程序序列，故主設計取 D2；'
               '草圖是本課判斷解集的唯一依據，故 D5 升為輔助之首，並把「畫草圖」'
               '獨立成手順卡第 4 步，使它成為不可跳過的動作。',
        density='全班共用',
        fading='本份紙面上已經做出三級：練習A 每題重印 ①②③ 提示 → 練習B 只在區塊'
               '開頭放一次共用提示 → 練習C 完全不放。（草圖框三層都保留：畫草圖是'
               '本課的核心動作，不是鷹架。）下一課起草圖框也撤走，只問「這題的草圖'
               '長什麼樣」→ 最後連手順卡一併移除。',
        flows=('F1 師徒制對話四步（老師畫一次草圖、學生說出取哪一邊）',
               'F2 番茄鐘分段（A／B／C 三段，每段末的自我核對清單就是收口，段間有核對點）'),
        iep_codes=('a3 提示題目重點', 'a6 增加行距', 'b5 提供步驟提示卡'),
        extra=[('與教學簡報的對應',
                '簡報_L8_一元二次不等式 用的是「四步走」；本份把「畫草圖」由第 3 步'
                '拆出來獨立成第 4 步，共五步。簡報只處理兩個相異實根，本份補回 Δ＝0、'
                'Δ＜0 兩種情況（見第三節）——上課用簡報帶完四步後，用本份第三節補這兩欄。')],
    )

    out = build_docx(P, os.path.join(BASE, '講義_二次函數與一元二次不等式_融合版.docx'),
                     footer_text=FOOT, media=media)
    return out


def _delta_table(media):
    """Δ 三分類決策表：左欄 Δ、中欄草圖、右欄解集寫法。
    house-style「多選一的規則改成決策表」——不要寫成四句條列散文。"""
    w = [int(_PAGE_CONTENT_WIDTH * 0.13), int(_PAGE_CONTENT_WIDTH * 0.30),
         int(_PAGE_CONTENT_WIDTH * 0.27)]
    w.append(_PAGE_CONTENT_WIDTH - sum(w))
    rows = [{'hdr': True, 'cells': [
        {'p': [para('判別式', bold=True, sz=22)], 'shd': GREY_FILL},
        {'p': [para('草圖長這樣', bold=True, sz=22)], 'shd': GREY_FILL},
        {'p': [para('問 ＞ 0 時', bold=True, sz=22)], 'shd': GREY_FILL},
        {'p': [para('問 ＜ 0 時', bold=True, sz=22)], 'shd': GREY_FILL},
    ]}]
    spec = [
        ('{Δ>0}', 'd_pos', dict(roots=('x₁', 'x₂'), opening='up',
                                    caption='交 x 軸兩點'),
         ['取兩邊', '｛x ｜ {x<x_1} 或 {x>x_2}｝'],
         ['取中間', '｛x ｜ {x_1<x<x_2}｝']),
        ('{Δ=0}', 'd_zero', dict(roots=('x₀',), opening='up',
                                     caption='碰 x 軸一點'),
         ['除了那一點，全部都是解', '｛x ｜ {x!=x_0}｝'],
         ['無解', '（圖象沒有一段在 x 軸下方）']),
        ('{Δ<0}', 'd_neg', dict(roots=(), opening='up',
                                    caption='不碰 x 軸'),
         ['全部實數都是解', '｛x ｜ x 是任何實數｝'],
         ['無解', '（整條都在 x 軸上方）']),
    ]
    for d, key, kw, gt, lt in spec:
        rows.append({'cells': [
            {'p': [para(d, bold=True)], 'va': 'center'},
            {'p': [expand_image(image_para(fig(key, **kw), width_cm=5.0), media)],
             'va': 'center'},
            {'p': [para(gt[0], sz=21, spacing=False), para(gt[1], sz=21, spacing=False)],
             'va': 'center'},
            {'p': [para(lt[0], sz=21, spacing=False), para(lt[1], sz=21, spacing=False)],
             'va': 'center'},
        ]})
    return _tbl(rows, w)


def _fig_step45(media, key, kw, cap4, cap5):
    """範例中的第 4、5 步：草圖擺左、兩句說明擺右，跟上面的算式表接在一起。"""
    w1 = int(_PAGE_CONTENT_WIDTH * 0.42)
    return _tbl([[
        {'p': [expand_image(image_para(fig(key, **kw), width_cm=6.6), media)],
         'va': 'center'},
        {'p': [para(cap4, sz=21, spacing=False), blank(),
               para(cap5, sz=21, spacing=False)], 'va': 'center'},
    ]], [w1, _PAGE_CONTENT_WIDTH - w1])


# ================================================================ 練習
def _q(media, no, stem, hint=None, n_lines=5):
    """一題：題目與作答空間在左，草圖框與提示在右（house-style 2026-08-05 定案）。
    hint=None 時右欄只剩空白草圖框——這就是 D2 的褪除梯度：A 每題重印提示、
    B 只在區塊開頭放一次、C 不放（teaching-designs.md D2）。
    草圖框三層都保留，因為「每題都要畫草圖」是本課的核心動作，不是鷹架。"""
    aside = [expand_image(image_para(fig(f'blank_{no}', blank=True,
                                         caption='草圖畫這裡'), width_cm=7.2), media)]
    if hint:
        aside += hint_lines(hint, title='提示')
    return aside_layout(
        [para(f'{no}．{stem}')] + write_lines(n_lines),
        aside, main_pct=0.60, media=media, boxed=True)


def build_exercise():
    P, media = [], MediaRegistry()
    P.append(masthead(SUBJ, UNIT, '課堂練習'))
    P.append(student_info_row())
    P.append(para('忘記做法就先回頭看《…課堂講義》第四節的五步手順卡。'
                  '每題都要畫草圖——畫得出草圖，範圍就挑得中。'))

    P.append(heading(f'一、練習A（{star_label(1)}）—— 先求根，再照草圖挑範圍'))
    P.append(_q(media, 1, '求不等式 {(x-1)(x-4)>0} 的解集。',
                ['① 已經分解好，直接讀出兩個根', '② 開口向上（{a=1}）',
                 '③ 問 ＞ 0 → 取兩邊']))
    P.append(_q(media, 2, '求不等式 {x^2-x-6<0} 的解集。',
                ['① 先因式分解求根', '② 開口向上', '③ 問 ＜ 0 → 取中間']))
    P.append(_q(media, 3, '求不等式 {x^2-7x+10>0} 的解集。',
                ['① 先因式分解求根', '② 開口向上', '③ 問 ＞ 0 → 取兩邊']))
    P.append(selfcheck_list(CHECK_A, '練習A 做完，先自己核對一次'))
    P.append(checkpoint_rule())

    # B、C 不強制分頁：硬分頁會把核對清單＋核對點單獨丟到一頁上（實測近乎全白）
    P.append(heading(f'二、練習B（{star_label(2)}）—— 根不一定有兩個'))
    P.append(shaded_box('這一區的題目不一定有兩個根。每題先算 {Δ}：{Δ>0} 兩個根、'
                        '{Δ=0} 一個根、{Δ<0} 沒有根——草圖跟著變，解集也跟著變。'))
    P.append(_q(media, 4, '求不等式 {x^2-6x+9<=0} 的解集。'))
    P.append(_q(media, 5, '求不等式 {x^2-2x+5>0} 的解集。'))
    P.append(_q(media, 6, '求不等式 {2x^2-3x-2<0} 的解集。'))
    P.append(selfcheck_list(CHECK_B, '練習B 做完，先自己核對一次'))
    P.append(checkpoint_rule())

    P.append(heading(f'三、練習C（{star_label(3)}）—— a 是負數、以及應用題'))
    P.append(_q(media, 7, '求不等式 {-x^2+3x+4>0} 的解集。'))
    P.append(_q(media, 8, '求不等式 {x^2-4x+4>0} 的解集。'))
    P.append(_q(media, 9, '一個球向上拋出，{t} 秒後的高度是 {h=16t-t^2}（公尺）。'
                          '問在哪一段時間內，球的高度超過 60 公尺？', n_lines=6))
    P.append(selfcheck_list(CHECK_C, '練習C 做完，先自己核對一次'))

    # ---- 教師用參考答案
    P.append(heading('教師用參考答案', page_break_before=True))
    for t in _ANSWERS:
        P.append(problem_box([para(x, spacing=False) for x in t], trailing_blank=False))
        P.append(blank())

    out = build_docx(P, os.path.join(BASE, '練習_二次函數與一元二次不等式_融合版.docx'),
                     footer_text=FOOT, media=media)
    return out


_ANSWERS = [
    ['A1　{(x-1)(x-4)=0} → {x_1=1} 或 {x_2=4}；{a>0} 開口向上，問 ＞ 0 取兩邊',
     '∴ 解集為 ｛x ｜ {x<1} 或 {x>4}｝'],
    ['A2　{x^2-x-6=(x+2)(x-3)}；令它等於 0 → {x_1=-2} 或 {x_2=3}；問 ＜ 0 取中間',
     '∴ 解集為 ｛x ｜ {-2<x<3}｝'],
    ['A3　{x^2-7x+10=(x-2)(x-5)}；令它等於 0 → {x_1=2} 或 {x_2=5}；問 ＞ 0 取兩邊',
     '∴ 解集為 ｛x ｜ {x<2} 或 {x>5}｝'],
    ['B4　{Δ=36-36=0}，重根 {x=3}（即 {(x-3)^2<=0}）；開口向上，只有頂點碰到 x 軸',
     '{(x-3)^2} 永遠 ≥ 0，所以「≤ 0」只在頂點成立',
     '∴ 解集為 ｛x ｜ {x=3}｝'],
    ['B5　{Δ=4-20=-16<0}，沒有實根；{a=1>0} 開口向上，整條在 x 軸上方',
     '∴ 解集為 ｛x ｜ x 是任何實數｝'],
    ['B6　{2x^2-3x-2=(2x+1)(x-2)}；令它等於 0 → {x_1=-frac(1,2)} 或 {x_2=2}；'
     '{a=2>0}，問 ＜ 0 取中間',
     '∴ 解集為 ｛x ｜ {-frac(1,2)<x<2}｝'],
    ['C7　{a=-1<0}，整條乘 −1 並把不等號反向：{x^2-3x-4<0}',
     '{(x+1)(x-4)=0} → {x_1=-1} 或 {x_2=4}；問 ＜ 0 取中間',
     '∴ 解集為 ｛x ｜ {-1<x<4}｝'],
    ['C8　{Δ=16-16=0}，重根 {x=2}（即 {(x-2)^2>0}）；開口向上，只有頂點碰到 x 軸',
     '除了 {x=2} 那一點之外，其餘每一點都在 x 軸上方',
     '∴ 解集為 ｛x ｜ {x!=2}｝'],
    ['C9　{16t-t^2>60} → 搬到一邊：{-t^2+16t-60>0} → 乘 −1 並反向：{t^2-16t+60<0}',
     '{(t-6)(t-10)=0} → {t_1=6} 或 {t_2=10}；問 ＜ 0 取中間',
     '∴ 解集為 ｛t ｜ {6<t<10}｝，即第 6 秒到第 10 秒之間'],
]


if __name__ == '__main__':
    for f in (build_handout, build_exercise):
        print(f())
