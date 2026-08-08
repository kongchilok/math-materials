# -*- coding: utf-8 -*-
"""高一 4.2 指數函數 融合版：講義／練習／工具卡 三份 docx（原生 OMML）。

教學設計（SKILL 步驟 2.5，使用者 2026-08-08 選定）：
  主設計  D5 圖文雙軌對照
  輔助①  D7 提示卡 → 另出《工具卡_4.2指數函數》（教案第 1、2 節指名要發的「指數圖像卡」）
  輔助②  D14 錯誤分析對比（簡報 L3 第 9 頁的三個易錯位）
  鷹架密度 抽離小班（Tier 2）：A／B／C 各 2 題、作答空間標準＋1 行、出工具卡
"""
import os
import sys

SKILL = r'C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts'
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
FIGS = os.path.join(OUT, '_figs')

SUBJ, UNIT = '高一數學', '4.2 指數函數'
FOOT = '高一數學．4.2 指數函數'


def fig(name, cm):
    return image_para(os.path.join(FIGS, f'{name}.png'), width_cm=cm)


# ══════════════════════════════════════════════════════════════════
# 講義
# ══════════════════════════════════════════════════════════════════
def build_handout():
    media = MediaRegistry()
    P = [masthead(SUBJ, UNIT, '課堂講義'), student_info_row()]

    # ── 一、定義 ──────────────────────────────────────────────
    P.append(heading('一、什麼是指數函數'))
    P.append(problem_box([
        para('　指數函數的一般式', bold=True),
        para('　{y=a^x}', jc='center'),
        para('　其中 {a>0} 且 {a!=1}，x 可以是任何實數。'),
    ]))
    P.append(shaded_box('a 叫做底數（寫在下面），x 叫做指數（寫在上面）。'))
    P.append(shaded_box('為什麼規定 {a>0}？　若 a ＝ −4，當 x ＝ 0.5 時 {(-4)^0.5} '
                        '就是 −4 的平方根，在實數範圍內沒有意義。'))
    P.append(shaded_box('為什麼規定 {a!=1}？　{1^x} 無論 x 是多少都等於 1，'
                        '畫出來是一條水平直線，不是指數函數。'))

    # ── 二、兩型的圖 ──────────────────────────────────────────
    P.append(heading('二、兩型指數函數的圖'))
    P.append(expand_image(fig('two_types', 11.4), media))
    P.append(para('　實線是 {y=2^x}（底數大於 1），虛線是 {y=(frac(1,2))^x}（底數在 0 與 1 之間）。'
                  '兩條線都穿過同一點。', sz=21))

    # ── 三、D5 圖文雙軌（主設計）──────────────────────────────
    P.append(heading('三、圖上看到什麼，算式就寫什麼'))
    P.append(dual_track_table([
        (fig('dt_point', 6.1),
         [para('兩條線都穿過 (0, 1)。', bold=True),
          para('因為 {a^0=1}（任何非零數的 0 次方都是 1），'),
          para('所以不論底數 a 是多少，圖必定經過定點 (0, 1)。')]),
        (fig('dt_above', 6.1),
         [para('線越向左走越貼近 x 軸，但永遠碰不到。', bold=True),
          para('{2^-1=0.5}　{2^-2=0.25}　{2^-3=0.125}'),
          para('值越來越細但不會變成 0，所以值域是 {y>0}。')]),
        (fig('dt_inc', 6.1),
         [para('由左下升到右上：x 每加 1，y 變成 2 倍。', bold=True),
          para('{2^0=1} → {2^1=2} → {2^2=4}'),
          para('底數 {a>1} 時遞增：x 越大，y 越大。')]),
        (fig('dt_dec', 6.1),
         [para('由左上跌到右下：x 每加 1，y 減一半。', bold=True),
          para('{(frac(1,2))^0=1} → {(frac(1,2))^1=0.5} → {(frac(1,2))^2=0.25}'),
          para('底數 {0<a<1} 時遞減：x 越大，y 越細。')]),
    ], media=media, headers=('圖形上看到什麼', '算式上寫什麼')))

    # ── 四、範例一 ────────────────────────────────────────────
    P.append(heading('四、範例一：不用計算機，比較 2^0.5 與 2^0.3 的大小'))
    P.append(worked_example_table([
        span_row('{y=2^x}', '兩個數都是 2 的次方，先認出它們屬於同一條線'),
        span_row('底數 {2>1}', '對照第三節第三列：a > 1 型 → 遞增'),
        eq_row('{0.5}', '{0.3}', '先比指數（x）誰大', rel='{>}'),
        eq_row('{2^0.5}', '{2^0.3}', '遞增：x 大的，y 也大', rel='{>}'),
        answer_row('{2^0.5>2^0.3}', why='作答：最後一行用「∴」寫出結論'),
    ], why_pct=0.36))

    # ── 五、範例二 ────────────────────────────────────────────
    P.append(heading('五、範例二：已知圖經過 (2, 9)，求底數 a'))
    P.append(worked_example_table([
        span_row('把點 (2, 9) 代入', '「圖經過某點」就是把該點坐標代入函數式'),
        eq_row('{a^2}', '{9}', '得到一條關於 a 的方程'),
        or_row('{a}', '{3}', '{a}', '{-3}', '兩邊開平方，分成兩支寫'),
        span_row('底數規定 {a>0}', '所以 a ＝ −3 要捨去（底數不能是負數）'),
        span_row('{3>1}', '對照第三節第三列：a > 1 型 → 遞增'),
        answer_row('{a=3}，圖由左下升到右上', why='作答：最後一行用「∴」寫出答案'),
    ], why_pct=0.36))

    # ── 六、D14 錯誤對比（輔助設計②）─────────────────────────
    P.append(heading('六、這一課最容易錯的三個位'))
    P.append(dual_track_table([
        ([para('{y=2^x} 的值域是所有實數。')],
         [para('※ 差在這裡：圖永遠在 x 軸上方，取不到 0 也取不到負數。',
               shd=GREY_FILL),
          para('值域是 {y>0}。', bold=True, shd=GREY_FILL)]),
        ([para('{y=1^x} 都算是指數函數。')],
         [para('※ 差在這裡：定義規定 {a!=1}。', shd=GREY_FILL),
          para('{1^x=1} 畫出來是一條水平直線，不是指數函數。',
               bold=True, shd=GREY_FILL)]),
        ([para('{a^0=0}，所以圖經過 (0, 0)。')],
         [para('※ 差在這裡：任何非零數的 0 次方都等於 1。', shd=GREY_FILL),
          para('{a^0=1}，所以圖經過 (0, 1)。', bold=True, shd=GREY_FILL)]),
    ], headers=('常見寫法', '正確寫法')))

    P.append(blank())
    P.append(para('　接下來請拿《課堂練習——4.2 指數函數》，'
                  '依照上面「圖上看到什麼、算式就寫什麼」這套框架，完成練習 A、B、C。'))

    # ── 教師實施說明頁 ───────────────────────────────────────
    P += teacher_notes(
        main_design='D5 圖文雙軌對照',
        aux_designs=('D7 提示卡（另出《工具卡_4.2指數函數》：指數圖像卡兩型）',
                     'D14 錯誤分析對比（第六節，對應簡報 L3 第 9 頁三個易錯位）'),
        reason='數學結構 S4「函數與圖像」，核心瓶頸是「底數 a ↔ 圖形走勢」的對應建立不起來；'
               'D5 把左邊的圖與右邊的算式逐列橫向對齊，學生每看懂圖上一件事，'
               '立刻在同一列看到它寫成什麼算式。',
        density='抽離小班（A／B／C 各 2 題、作答空間標準＋1 行、出工具卡）',
        fading='D5：練習A 圖已給、只需讀圖填答 → 練習B 只給算式，圖由學生自己描點畫出 → '
               '練習C 圖與式皆不給，學生自己決定要不要畫草圖。'
               'D7 圖像卡：教案第 1 節先發 a > 1 型 → 第 2 節補齊兩型 → '
               '第 3 課（4.3 反函數）起收起卡片，改為口頭提問「這條是哪一型」→ 測考不帶入。'
               'D14：第一次見到三欄對比 → 之後只給「常見寫法」一欄要學生自己改正 → '
               '最後只問一句「這題有一個常見陷阱，是什麼」。',
        flows=('F5 課前流程預告（配合簡報 L3 第 2 頁的四件事）',
               'F4 過程導向回饋：比大小題把「認出型」與「比指數」分開給分'),
        iep_codes=('a3 提示題目重點（指數圖像卡）', 'a6 增加行距／放大作答欄',
                   'a7 調整計分標準（步驟分）'))

    out = os.path.join(OUT, '講義_4.2指數函數_融合版.docx')
    build_docx(P, out, footer_text=FOOT, media=media)
    return out


# ══════════════════════════════════════════════════════════════════
# 練習
# ══════════════════════════════════════════════════════════════════
def build_practice():
    media = MediaRegistry()
    P = [masthead(SUBJ, UNIT, '課堂練習'), student_info_row()]
    P.append(para('　做之前先翻開《課堂講義——4.2 指數函數》第三節，'
                  '照「圖上看到什麼、算式就寫什麼」那張表的方法做。'))

    # ── 練習A：圖已給，讀圖填答 ──────────────────────────────
    P.append(heading(f'一、練習A（{star_label(1)}）'))
    P.append(aside_layout(
        [para('1．右圖是 {y=3^x} 的圖。'),
         para('（a）這條線與 y 軸交在哪一點？'),
         para('（b）由左至右，這條線是升還是跌？'),
         para('（c）填空：x 越大，y 越＿＿＿＿。')] + write_lines(4),
        [fig('p_3x', 7.4)] + hint_lines([
            '① 先看這條線在 y 軸上的高度',
            '② 底數 3 ＞ 1，對照講義第三節哪一列',
            '③ 用手指由左行到右，看是上還是下',
        ], title='讀圖三步'),
        media=media, boxed=True))

    P.append(aside_layout(
        [para('2．右圖是 {y=(frac(1,3))^x} 的圖。'),
         para('（a）f(0) ＝ ＿＿＿＿'),
         para('（b）這條線會不會碰到 x 軸？'),
         para('（c）這個函數的值域是＿＿＿＿（填 {y>0} 或「y 是所有實數」）')] + write_lines(4),
        [fig('p_1_3x', 7.4)] + hint_lines([
            '① f(0) 就是 x ＝ 0 時的 y',
            '② 看線的左右兩端與 x 軸的距離',
            '③ 值域＝這條線的 y 可以取到哪些數',
        ], title='讀圖三步'),
        media=media, boxed=True))

    # ── 練習B：只給算式，圖由學生畫 ──────────────────────────
    P.append(heading(f'二、練習B（{star_label(2)}）'))
    P.append(aside_layout(
        [para('3．已知 {y=2^x}。'),
         para('（a）計算下面四個 y 值：'),
         para('　　x ＝ −1 時，y ＝ ＿＿＿＿＿＿'),
         para('　　x ＝ 0 時，　y ＝ ＿＿＿＿＿＿'),
         para('　　x ＝ 1 時，　y ＝ ＿＿＿＿＿＿'),
         para('　　x ＝ 2 時，　y ＝ ＿＿＿＿＿＿'),
         para('（b）把這四點畫在右邊的坐標格上，再連成一條平滑曲線。'),
         para('（c）這條線經過哪一個定點？')] + write_lines(4),
        [fig('p_blank', 7.4)] + hint_lines([
            '① 負指數：{2^-1=frac(1,2^1)}',
            '② 先描點，再由左至右連線',
            '③ 定點看 x ＝ 0 那一點',
        ], title='作圖三步'),
        media=media, boxed=True))

    P.append(problem_box([
        para('4．在下面每題的橫線上填 ＞ 或 ＜，並寫出你用了哪一型（{a>1} 還是 {0<a<1}）。'),
        para('　（a）{3^1.2}　＿＿＿＿　{3^0.7}'),
        para('　（b）{(frac(1,2))^1.5}　＿＿＿＿　{(frac(1,2))^0.9}'),
        para('　（c）任揀一題，畫一條草圖說明你的判斷。'),
    ] + write_lines(6)))

    # ── 練習C：圖與式皆不給 ──────────────────────────────────
    P.append(heading(f'三、練習C（{star_label(3)}）'))
    P.append(problem_box([
        para('5．已知指數函數 {y=a^x} 的圖經過點 (3, 8)。'),
        para('　（a）求 a。'),
        para('　（b）判斷這條線是升還是跌，並寫出理由。'),
        para('　（c）不用計算機，比較 {a^0.4} 與 {a^0.6} 誰大，並寫出理由。'),
    ] + write_lines(7)))

    P.append(problem_box([
        para('6．小明說：「{y=a^x} 的圖一定是由左下升到右上。」'),
        para('　你同意嗎？請自己畫一張草圖，並寫出理由；'),
        para('　若不同意，請舉出一個反例。'),
    ] + write_lines(7), trailing_blank=False))

    # ── 參考答案（教師用，另起一頁）──────────────────────────
    P.append(heading('參考答案（教師用）', page_break_before=True))
    A = [
        ('1（a）', '(0, 1)。因為 {3^0=1}。'),
        ('1（b）', '升（遞增）。底數 {3>1}。'),
        ('1（c）', '越大。'),
        ('2（a）', '{f(0)=(frac(1,3))^0=1}'),
        ('2（b）', '不會。線越向右走越貼近 x 軸，但 y 永遠大於 0。'),
        ('2（c）', '{y>0}'),
        ('3（a）', 'x ＝ −1 時 {y=frac(1,2)}；x ＝ 0 時 y ＝ 1；'
                  'x ＝ 1 時 y ＝ 2；x ＝ 2 時 y ＝ 4。'),
        ('3（b）', '四點為 {(-1,frac(1,2))}、(0, 1)、(1, 2)、(2, 4)，連成由左下升到右上的平滑曲線。'),
        ('3（c）', '(0, 1)。'),
        ('4（a）', '＞。底數 {3>1} 屬 {a>1} 型（遞增）；{1.2>0.7}，所以 {3^1.2>3^0.7}。'),
        ('4（b）', '＜。底數 {frac(1,2)} 屬 {0<a<1} 型（遞減）；{1.5>0.9}，'
                  '指數大反而值細，所以 {(frac(1,2))^1.5<(frac(1,2))^0.9}。'),
        ('4（c）', '草圖只需一條 x 軸、一條曲線與 (0, 1)：(a) 畫升型，(b) 畫跌型；'
                  '在線上標出兩個指數對應的高度即可。'),
        ('5（a）', '{a^3=8}，所以 {a=2}。'),
        ('5（b）', '升（遞增）。因為 {2>1}，屬 {a>1} 型。'),
        ('5（c）', '{2^0.4<2^0.6}。遞增：指數大的，值也大，而 {0.4<0.6}。'),
        ('6', '不同意。當 {0<a<1} 時圖是由左上跌到右下。反例：{y=(frac(1,2))^x}，'
              'x 越大 y 越細。草圖：過 (0, 1)、在 x 軸上方、由左上跌向右下。'),
    ]
    for k, v in A:
        P.append(para(f'{k}　{v}', sz=22))

    out = os.path.join(OUT, '練習_4.2指數函數_融合版.docx')
    build_docx(P, out, footer_text=FOOT, media=media)
    return out


# ══════════════════════════════════════════════════════════════════
# 工具卡（D7）——教案第 1、2 節指名要發的「指數圖像卡」
# ══════════════════════════════════════════════════════════════════
def build_toolcard():
    media = MediaRegistry()
    P = [masthead(SUBJ, UNIT, '工具卡（剪下護貝，放在桌面）')]
    P.append(para('　沿虛線剪開。教案第 1 節先發左邊「a ＞ 1 型」，'
                  '第 2 節補發右邊「0 ＜ a ＜ 1 型」，兩張並排貼在桌面。', sz=21))

    def card(title, trigger, egs, png, lines, symbol):
        # 觸發語拆兩行：第一行一條公式，第二行放例子。
        # 一行塞四條公式喺窄欄會逐條被擠落新行，整句讀唔成句（HTML 版實測）。
        return ([para(f'▍{title}', bold=True, sz=HEADING_SZ),
                 para(f'什麼時候翻我：{trigger}', sz=20),
                 para(f'　例如　{egs}', sz=20),
                 expand_image(fig(png, 6.2), media)]
                + [para(f'{marker(i + 1)} {t}', sz=21, spacing=False)
                   for i, t in enumerate(lines)]
                + [blank(), para(symbol, bold=True, sz=22)])

    up = card('指數圖像卡（a ＞ 1 型）',
              '題目出現 {y=a^x}，而底數 {a>1}',
              '{2^x}　{3^x}　{10^x}',
              'card_up',
              ['圖必過定點 (0, 1)',
               '全條線在 x 軸上方：{y>0}',
               '由左下升到右上：x 越大，y 越大'],
              '{a>1} → 遞增')

    down = card('指數圖像卡（0 ＜ a ＜ 1 型）',
                '題目出現 {y=a^x}，而底數 {0<a<1}',
                '{(frac(1,2))^x}　{(frac(1,3))^x}　{0.4^x}',
                'card_down',
                ['圖必過定點 (0, 1)',
                 '全條線在 x 軸上方：{y>0}',
                 '由左上跌到右下：x 越大，y 越細'],
                '{0<a<1} → 遞減')

    # 一張 A4 只排一套（兩張卡）：要幾多份就印幾多份。
    # 原本一版印兩套，第二套冇任何標示，睇落似重複咗，而且逼出第二頁令頁尾浮喺半空。
    P.append(toolcard_sheet([up, down], cols=2, card_h=7600))

    out = os.path.join(OUT, '工具卡_4.2指數函數.docx')
    build_docx(P, out, footer_text=FOOT, media=media)
    return out


if __name__ == '__main__':
    for f in (build_handout(), build_practice(), build_toolcard()):
        print('OK', os.path.basename(f))
