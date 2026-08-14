# -*- coding: utf-8 -*-
"""重建《講義_二次函數的圖像與性質_融合版》：忠實保留原有 §一~§四（含原有
兩張嵌入圖），插入新 §三 平移階梯（D5 圖文雙軌＋D11 標記對應）與新 §六
待定係數法（決策表＋worked_example_table），其餘章節重新編號。
原三→四、原四→五；新三＝平移階梯、新六＝待定係數法。"""
import sys, os
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *
from omml_docx import _tbl, _PAGE_CONTENT_WIDTH
import design_svg as ds

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, 'figs')
os.makedirs(FIGS, exist_ok=True)
ORIG_IMG1 = os.path.join(HERE, '_orig_img1.png')   # y=x² vs y=-x²（開口方向，原有）
ORIG_IMG2 = os.path.join(HERE, '_orig_img2.png')   # y=x²-4x+3（配方範例，原有）

media = MediaRegistry()

# ---------------- 新圖：平移階梯 3 張（黑白，虛線=原圖／實線=結果／點線=陷阱對照） ----------------
svg1 = ds.parabola_graph(
    curves=[
        {'f': lambda x: x * x, 'style': 'dashed', 'label': {'x': -2.5, 'y': 5.6, 'text': 'y=x²（原）', 'anchor': 'start'}},
        {'f': lambda x: x * x + 2, 'style': 'solid', 'label': {'x': 1.5, 'y': 6.1, 'text': 'y=x²+2', 'anchor': 'start'}},
    ],
    points=[{'x': 0, 'y': 0, 'label': '(0,0)', 'dx': -10, 'dy': 30, 'anchor': 'end'},
            {'x': 0, 'y': 2, 'label': '(0,2)', 'dx': 10, 'dy': 4}],
    xrange=(-3, 3), yrange=(-1, 7), xstep=1, ystep=1, width=300, height=250,
)
ds.svg_to_png(svg1, os.path.join(FIGS, 'p31.png'))

svg2 = ds.parabola_graph(
    curves=[
        {'f': lambda x: x * x, 'style': 'dashed', 'label': {'x': -4.7, 'y': 5.6, 'text': 'y=x²（原）', 'anchor': 'start'}},
        {'f': lambda x: (x - 3) ** 2, 'style': 'solid', 'label': {'x': 3.6, 'y': 5.2, 'text': 'y=(x−3)²', 'anchor': 'start'}},
        {'f': lambda x: (x + 2) ** 2, 'style': 'dotted', 'label': {'x': -6.4, 'y': 4.6, 'text': 'y=(x+2)²', 'anchor': 'start'}},
    ],
    points=[{'x': 3, 'y': 0, 'label': '(3,0)', 'dx': 6, 'dy': 30},
            {'x': -2, 'y': 0, 'label': '(−2,0)', 'dx': -6, 'dy': 30, 'anchor': 'end'}],
    xrange=(-6.5, 6.5), yrange=(-1, 6.5), xstep=1, ystep=1, width=340, height=270,
)
ds.svg_to_png(svg2, os.path.join(FIGS, 'p32.png'))

svg3 = ds.parabola_graph(
    curves=[
        {'f': lambda x: 2 * x * x, 'style': 'dashed', 'label': {'x': -2.15, 'y': 7.6, 'text': 'y=2x²（原）', 'anchor': 'start'}},
        {'f': lambda x: 2 * (x - 1) ** 2 + 3, 'style': 'solid', 'label': {'x': 1.9, 'y': 8.6, 'text': 'y=2(x−1)²+3', 'anchor': 'start'}},
    ],
    points=[{'x': 0, 'y': 0, 'label': '(0,0)', 'dx': -10, 'dy': 30, 'anchor': 'end'},
            {'x': 1, 'y': 0, 'label': '(1,0)', 'dx': 10, 'dy': 30},
            {'x': 1, 'y': 3, 'label': '頂點(1,3)', 'dx': 10, 'dy': -12}],
    vlines=[{'x': 1, 'label': 'x=1'}],
    xrange=(-2.3, 3.3), yrange=(-1, 9), xstep=1, ystep=1, width=320, height=270,
)
ds.svg_to_png(svg3, os.path.join(FIGS, 'p33.png'))

# ==================== 組裝內容 ====================
P = []
P.append(masthead('初三數學', '二次函數的圖像與性質', '課堂講義'))
P.append(student_info_row())

# ---- 一、二次函數的概念（原有，忠實保留） ----
P.append(heading('一、二次函數的概念'))
P.append(para('一般地，{y=ax^2+bx+c}（a≠0）叫做二次函數，它的圖像是一條拋物線。'))

# ---- 二、開口方向（原有，忠實保留，含原有圖1） ----
P.append(heading('二、開口方向'))
P.append(para('a ＞ 0 開口向上，a ＜ 0 開口向下；|a| 越大，開口越窄。'))
P.append(image_para(ORIG_IMG1, width_cm=7.5, caption='圖：y=x²（向上）與 y=−x²（向下）'))

# ---- 三、平移階梯（新） ----
P.append(heading('三、平移階梯：從 {y=ax^2} 到完整頂點式'.replace('{y=ax^2}', 'y=ax²')))
P.append(para('頂點式不是一步到位——先學「上下移」，再學「左右移」，最後把兩個動作合成一次做完。'))

P.append(para('3.1　上下移動：{y=ax^2} → {y=ax^2+k}', bold=True, keep_next=True))
P.append(dual_track_table([
    (image_para(os.path.join(FIGS, 'p31.png'), width_cm=7.4),
     [para(f'加上一個常數 {param_mark(3)}k：'),
      para('　{y=ax^2+k}'),
      blank(),
      para(f'{param_mark(3)}k ＝ 2 ＞ 0 → 向上移 2 個單位'),
      para('頂點：(0, 0) → (0, 2)；開口方向與寬窄不變（a 沒變）')]),
], media=media))

P.append(para('3.2　左右移動：{y=ax^2} → {y=a(x-h)^2}', bold=True, keep_next=True))
P.append(dual_track_table([
    (image_para(os.path.join(FIGS, 'p32.png'), width_cm=8.2),
     [para(f'把 x 換成 (x−{param_mark(2)}h)：'),
      para('　{y=a(x-h)^2}'),
      blank(),
      para(f'{param_mark(2)}h ＝ 3 ＞ 0 → 向右移 3；頂點 (0,0)→(3,0)'),
      shaded_box(f'⚠ 陷阱：{{y=(x+2)^2}} 要先寫成 {{y=(x-(-2))^2}} 才看得出 {param_mark(2)}h ＝ −2（不是 2）→ 向左移 2；頂點 (0,0)→(−2,0)')]),
], media=media))

P.append(para('3.3　合成：{y=a(x-h)^2+k}（先左右移，後上下移）', bold=True, keep_next=True))
P.append(dual_track_table([
    (image_para(os.path.join(FIGS, 'p33.png'), width_cm=7.8),
     [para(f'{param_mark(1)}a 不變，先移 {param_mark(2)}h，後移 {param_mark(3)}k：'),
      para('　{y=2x^2} → {y=2(x-1)^2} → {y=2(x-1)^2+3}'),
      blank(),
      para('頂點路徑：(0,0) → (1,0) → (1,3)'),
      para('對稱軸 x ＝ 1；開口向上（a=2＞0，比 a=1 窄）')]),
], media=media))

P.append(heading('平移路徑總結表', page_break_before=True))
_w = _PAGE_CONTENT_WIDTH // 4
_widths = [_w, _w, _w, _PAGE_CONTENT_WIDTH - 3 * _w]
_summary_rows = [
    {'hdr': True, 'cells': [{'p': [para(h, bold=True, sz=22)], 'shd': GREY_FILL}
                            for h in ('起點', '動作', '終點', '頂點變化')]},
    {'cells': [[para('{y=ax^2}')], [para('上下移 k')], [para('{y=ax^2+k}')], [para('(0,0) → (0,k)')]]},
    {'cells': [[para('{y=ax^2}')], [para('左右移 h')], [para('{y=a(x-h)^2}')], [para('(0,0) → (h,0)')]]},
    {'cells': [[para('{y=ax^2}')], [para('先左右移h、後上下移k')], [para('{y=a(x-h)^2+k}')], [para('(0,0) → (h,k)')]]},
]
P.append(_tbl(_summary_rows, _widths))

# ---- 四、頂點式與平移（原三，忠實保留，內容不變只改編號） ----
P.append(heading('四、頂點式與平移'))
P.append(para('頂點式 {y=a(x-h)^2+k} 的頂點是 (h, k)，對稱軸是直線 x=h；它由 {y=ax^2} 平移得到。'))

# ---- 五、一般式化頂點式（配方）（原四，忠實保留，含原有圖2） ----
P.append(heading('五、一般式化頂點式（配方）'))
P.append(para('把 {y=ax^2+bx+c} 配方後，對稱軸 {x=-frac(b,2a)}。'))
P.append(shaded_box('範例：把 {y=x^2-4x+3} 化頂點式並畫圖。'))
P.append(para('配方：{y=x^2-4x+3=(x-2)^2-1}'))
P.append(para('→ 開口向上，對稱軸 x=2，頂點 (2, −1)。'))
P.append(para('與 x 軸交點：{(x-1)(x-3)=0} → (1, 0)、(3, 0)；與 y 軸交點 (0, 3)。'))
P.append(image_para(ORIG_IMG2, width_cm=8.0, caption='圖：y=x²−4x+3 的圖像'))

# ---- 六、待定係數法（新） ----
P.append(heading('六、待定係數法：由部分資訊反求解析式', page_break_before=True))
P.append(para('已知圖像的部分資訊（頂點、交點、或幾個點），可以反過來求出二次函數的解析式。用哪一個式子，看已知資訊決定：'))

_dw = int(_PAGE_CONTENT_WIDTH * 0.30)
_decision_rows = [
    {'hdr': True, 'cells': [{'p': [para(h, bold=True, sz=22)], 'shd': GREY_FILL}
                            for h in ('已知資訊', '用哪個式', '為什麼')]},
    {'cells': [[para('頂點 (h,k) ＋ 另一點')], [para('頂點式 {y=a(x-h)^2+k}')], [para('只欠 a，代一點就夠')]]},
    {'cells': [[para('三個一般點')], [para('一般式 {y=ax^2+bx+c}')], [para('三個未知數，要列三條方程')]]},
    {'cells': [[para('與 x 軸兩交點 ＋ 另一點')], [para('交點式 {y=a(x-x_1)(x-x_2)}')], [para('兩根已知，只欠 a')]]},
]
P.append(_tbl(_decision_rows, [_dw, _dw, _PAGE_CONTENT_WIDTH - 2 * _dw]))

# 範例1：頂點式
P.append(shaded_box('範例1（頂點式）：已知頂點 (2, −3)，且過點 (4, 5)，求解析式。', keep_next=True))
P.append(worked_example_table([
    span_row('設 {y=a(x-2)^2-3}', '頂點式：頂點(h,k)先代入'),
    eq_row('{5}', '{a(4-2)^2-3}', '把 x=4, y=5 代入'),
    eq_row('{5}', '{4a-3}', '化簡右式'),
    eq_row('{4a}', '{8}', '移項'),
    eq_row('{a}', '{2}', '兩邊除以 4'),
    answer_row('{y=2(x-2)^2-3}', why='頂點式答案；展開得一般式 {y=2x^2-8x+5}'),
]))

# 範例2：一般式
P.append(shaded_box('範例2（一般式）：已知圖像過 (0, 1)、(1, 4)、(2, 11) 三點，求解析式。', keep_next=True, page_break_before=True))
P.append(worked_example_table([
    span_row('設 {y=ax^2+bx+c}', '一般式：三個未知數，要列三條方程'),
    eq_row('{c}', '{1}', '代入 (0,1)：x=0 時 y=c'),
    eq_row('{a+b+c}', '{4}', '代入 (1,4)'),
    eq_row('{4a+2b+c}', '{11}', '代入 (2,11)'),
    span_row('c=1 代入後：a+b=3……①　　2a+b=5……②（4a+2b=10 化簡）', '消去 c，剩兩式兩未知數'),
    eq_row('{(2a+b)-(a+b)}', '{5-3}', '② − ①，消去 b'),
    eq_row('{a}', '{2}', '化簡'),
    eq_row('{b}', '{3-2}', '代回①：a+b=3'),
    eq_row('{b}', '{1}', '化簡'),
    answer_row('{y=2x^2+x+1}', why='一般式答案'),
], why_pct=0.30))

# 範例3：交點式
P.append(shaded_box('範例3（交點式）：已知圖像與 x 軸交於 (1, 0)、(4, 0)，且過 (0, 8)，求解析式。', keep_next=True))
P.append(worked_example_table([
    span_row('設 {y=a(x-1)(x-4)}', '交點式：兩根已知，只欠 a'),
    eq_row('{8}', '{a(0-1)(0-4)}', '把 (0,8) 代入'),
    eq_row('{8}', '{4a}', '化簡右式'),
    eq_row('{a}', '{2}', '兩邊除以 4'),
    answer_row('{y=2(x-1)(x-4)}', why='交點式答案；展開得一般式 {y=2x^2-10x+8}'),
]))

P.append(para('接下來請拿本單元《課堂練習》，完成練習 A、B、C。'))

# ---- 教師實施說明頁 ----
P.extend(teacher_notes(
    main_design='D5 圖文雙軌對照',
    aux_designs=['D11 標記對應（a/h/k 用 ⓐⓑⓒ）'],
    reason='本單元屬 S4 函數與圖像，核心瓶頸是參數(a/h/k)與圖形特徵的對應關係無法內化。'
           '平移階梯段落用左圖右式逐步對齊，讓「加k」「換h」的動作直接對到圖像變化；'
           '待定係數法段落改用決策表＋worked_example_table（house-style 版面密度慣例，'
           '非獨立教學設計代號），因為那裡的瓶頸是「憑已知資訊選對公式」，不是圖形對應。',
    density='抽離小班',
    fading='圖文雙軌對照：先給完整雙軌表（圖＋算式都給）→ 只給圖、算式自己寫 → 只給文字描述、'
           '圖自己畫 → 移除鷹架直接讀頂點式。標記字元 ⓐⓑⓒ：貫穿本節 → 只在總結表出現 → 移除。',
    flows=['F5 課前流程預告（今天三件事：上下移 → 左右移 → 合成）'],
    iep_codes=['a3 提示題目重點', 'a6 增加行距／放大作答欄'],
))

out = build_docx(P, os.path.join(HERE, '講義_二次函數的圖像與性質_融合版.docx'),
                 footer_text='初三數學．二次函數的圖像與性質單元', media=media)
print(out)
