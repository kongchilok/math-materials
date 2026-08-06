# -*- coding: utf-8 -*-
"""單元 04 講義／練習／工具卡 docx 產檔。

教學設計：D2 手順卡（主）＋ D12 自我核對、D14 錯誤分析對比（輔）
鷹架密度：抽離小班（Tier 2）
house-style：範例段一律 worked_example_table()＋eq_row/or_row/span_row/answer_row
"""
import sys
import os

SKILL = r'C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts'
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _tbl, _PAGE_CONTENT_WIDTH  # star-import 跳過底線開頭的名字

BASE = os.path.dirname(os.path.abspath(__file__))
SUBJ = '初三數學'
UNIT = '分式方程、無理方程與二元二次方程組'
FOOT = '初三數學．分式方程、無理方程與二元二次方程組'

# ---------------------------------------------------------------- 手順卡定義
CARD_FRAC = dict(
    title='分式方程 四步',
    trigger='方程裡有分母，而且分母含有未知數',
    steps=[
        ('把每個分母因式分解，找出最簡公分母', '分母是 {x^2-4} 要先拆成 {(x+2)(x-2)}'),
        ('兩邊同乘最簡公分母，去分母', '每一項都要乘，包括沒有分母的那一項'),
        ('解這條整式方程', '照一元二次方程的做法：移項、因式分解、分兩支'),
        ('驗根：把每個解代回原方程的分母', '令分母 {=0} 的叫增根，一定要捨去'),
    ],
    fading='完整四步卡 → 只留「※ 驗根」一句 → 只問「這題有幾步」→ 移除',
)

CARD_SURD = dict(
    title='無理方程 四步',
    trigger='未知數被關在根號裡面',
    steps=[
        ('移項，讓根號單獨留在一邊', '根號要孤立，才能一次平方掉'),
        ('兩邊平方，去根號', '右邊是整體平方：{(x-3)^2} 不等於 {x^2-9}'),
        ('解這條整式方程', '照一元二次方程的做法：移項、因式分解、分兩支'),
        ('驗根：把每個解代回原方程', '平方會多出假根；左右不相等的一定要捨去'),
    ],
    fading='完整四步卡 → 只留「※ 驗根」一句 → 只問「這題有幾步」→ 移除',
)

CARD_SYS = dict(
    title='二元二次方程組 四步',
    trigger='兩條方程、兩個未知數，其中一條是二次',
    steps=[
        ('找出那條一次方程', '一次方程才好用來「用一個字母表示另一個」'),
        ('從一次方程解出一個未知數', '例如寫成 {y=x+1}，準備代入'),
        ('代入二次方程，解出第一個未知數', '代入後只剩一個字母，就變回熟悉的一元二次方程'),
        ('每個解都要回代，求出另一個未知數', '答案要成對寫：有幾個 {x} 就有幾對 {(x,y)}'),
    ],
    fading='完整四步卡 → 只留「※ 記得回代」一句 → 只問「這題有幾步」→ 移除',
)


# ================================================================ 講義
def build_handout():
    P = []
    P.append(masthead(SUBJ, UNIT, '課堂講義'))
    P.append(student_info_row())

    # ---- 導入
    P.append(heading('這一課要學三種新方程'))
    P.append(para('前面學過的一元二次方程，未知數都是「光著身」的。這一課的三種方程，'
                  '未知數分別被關在三個地方：'))
    P.append(problem_box([
        para('分母裡　→　分式方程　　例：{frac(3,x)=x-2}', spacing=False),
        para('根號裡　→　無理方程　　例：{sqrt(x+2)=x}', spacing=False),
        para('另一條方程裡　→　二元二次方程組　　例：{y=x+1} 與 {x^2+y^2=25}', spacing=False),
    ]))
    P.append(para('三種方程的做法都是同一個念頭：'))
    P.append(shaded_box('想辦法把未知數「放出來」，變回會解的一元二次方程。'))
    P.append(para('但放出來是有代價的——'))
    P.append(shaded_box('去分母、平方，這兩個動作都可能多生出「假的解」。'
                        '所以這一課每一題最後都要驗根。', accent_color=GREY_BORDER))

    # ---- 一、分式方程
    P.append(heading('一、分式方程'))
    P.append(step_card(**CARD_FRAC))
    P.append(blank())
    P.append(para('★ 範例一：解 {frac(3,x)=x-2}', bold=True, keep_next=True))
    P.append(worked_example_table([
        eq_row('{frac(3,x)}', '{x-2}', '原方程。分母有 {x}，所以先寫低 {x!=0}'),
        span_row('最簡公分母是 {x}', '分母只有一個，最簡公分母就是它'),
        eq_row('{3}', '{x(x-2)}', '兩邊同乘 {x}，去分母'),
        eq_row('{3}', '{x^2-2x}', '展開右邊'),
        eq_row('{x^2-2x-3}', '{0}', '移項，化成一般式'),
        eq_row('{(x-3)(x+1)}', '{0}', '因式分解'),
        or_row('{x-3}', '{0}', '{x+1}', '{0}', '兩個因式各自等於 0，分兩支寫'),
        or_row('{x_1}', '{3}', '{x_2}', '{-1}', '兩支各自解出'),
        span_row('驗根 {x_1=3}：代入分母 {x} 得 {3}', '不等於 0，保留'),
        span_row('驗根 {x_2=-1}：代入分母 {x} 得 {-1}', '不等於 0，保留'),
        answer_row('{x_1=3} 或 {x_2=-1}', '作答：最後一行用「∴」寫出兩個根'),
    ], why_pct=0.36))

    # ---- 二、無理方程
    P.append(heading('二、無理方程'))
    P.append(step_card(**CARD_SURD))
    P.append(blank())
    P.append(para('★ 範例二：解 {sqrt(x+2)=x}', bold=True, keep_next=True))
    P.append(worked_example_table([
        eq_row('{sqrt(x+2)}', '{x}', '原方程。根號已經單獨在左邊，可以直接平方'),
        eq_row('{x+2}', '{x^2}', '兩邊平方，去根號'),
        eq_row('{x^2-x-2}', '{0}', '移項，化成一般式'),
        eq_row('{(x-2)(x+1)}', '{0}', '因式分解'),
        or_row('{x-2}', '{0}', '{x+1}', '{0}', '兩個因式各自等於 0，分兩支寫'),
        or_row('{x_1}', '{2}', '{x_2}', '{-1}', '兩支各自解出'),
        span_row('驗根 {x_1=2}：左邊 {sqrt(2+2)=2}，右邊 {2}', '左右相等，保留'),
        span_row('驗根 {x_2=-1}：左邊 {sqrt(-1+2)=1}，右邊 {-1}',
                 '根號算出來一定不是負數，左右不相等，捨去'),
        answer_row('{x=2}', '作答：只有一個根通過驗根，就只寫一個'),
    ], why_pct=0.38))

    # ---- 三、二元二次方程組
    P.append(heading('三、二元二次方程組'))
    P.append(step_card(**CARD_SYS))
    P.append(blank())
    P.append(para('★ 範例三：解方程組 {y=x+1}　與　{x^2+y^2=25}', bold=True, keep_next=True))
    P.append(worked_example_table([
        span_row('已知：{y=x+1}（一次）　與　{x^2+y^2=25}（二次）',
                 '一次那條已經解好 {y}，可以直接代入'),
        eq_row('{x^2+(x+1)^2}', '{25}', '把 {y} 換成 {x+1}，代入二次方程'),
        eq_row('{x^2+x^2+2x+1}', '{25}', '展開 {(x+1)^2}'),
        eq_row('{2x^2+2x-24}', '{0}', '移項，合併同類項'),
        eq_row('{x^2+x-12}', '{0}', '兩邊除以 2，數字變細'),
        eq_row('{(x-3)(x+4)}', '{0}', '因式分解'),
        or_row('{x-3}', '{0}', '{x+4}', '{0}', '兩個因式各自等於 0，分兩支寫'),
        or_row('{x_1}', '{3}', '{x_2}', '{-4}', '兩支各自解出 {x}'),
        or_row('{y_1}', '{4}', '{y_2}', '{-3}', '回代 {y=x+1}：這一步最容易漏'),
        answer_row('{(x_1,y_1)=(3,4)} 或 {(x_2,y_2)=(-4,-3)}',
                   '作答：方程組的答案要成對寫'),
    ], why_pct=0.36))

    # ---- 四、D14 錯誤分析對比
    P.append(heading('四、這一課最容易錯的一步'))
    P.append(para('下面兩欄，前三行一模一樣，分歧在第四行。'))
    P.append(para('題目：解 {frac(2,x-3)=frac(x-1,x-3)}', bold=True, keep_next=True))
    P.append(dual_track_table([
        ('兩邊乘 {(x-3)}，去分母',
         [para('兩邊乘 {(x-3)}，去分母', shd=GREY_FILL, spacing=False)]),
        ('{2=x-1}',
         [para('{2=x-1}', shd=GREY_FILL, spacing=False)]),
        ('{x=3}',
         [para('{x=3}', shd=GREY_FILL, spacing=False)]),
        ([para('答：{x=3}', spacing=False)],
         [para('※ 驗根：{x=3} 令分母 {x-3=0}，分式沒有意義 → 增根，捨去',
               shd=GREY_FILL, spacing=False)]),
        ('',
         [para('∴ 原方程無解', bold=True, shd=GREY_FILL, spacing=False)]),
    ], headers=('常見寫法', '正確寫法')))
    P.append(shaded_box('※ 差在這裡：解出來的數字一定要代回分母檢查。'
                        '令分母等於 0 的數叫「增根」，它不是原方程的解。'))

    # ---- 收尾
    P.append(heading('接下來'))
    P.append(para('請拿本單元的《課堂練習》，照上面三張手順卡完成練習 A、B、C。'
                  '做每一題時，把對應的那張手順卡放在旁邊，'
                  '手指指住你正在做的那一步。'))

    # ---- 教師頁
    P += teacher_notes(
        main_design='D2 手順卡（日本特別支援教育小步子原則）',
        aux_designs=('D12 自我核對清單＋分段結構', 'D14 錯誤分析對比（正誤雙欄）'),
        reason='本單元三個子題（分式方程／無理方程／二元二次方程組）全部屬 S2 多步驟程序運算，'
               '核心瓶頸是序列性步驟在工作記憶中崩潰、漏步驟。三種方程的步驟不同但都是固定序列，'
               '正是手順卡的標準適用情境。輔助設計對準本單元唯一的高頻固定錯法——漏驗根／不捨增根：'
               'D12 把「驗根了嗎」變成可自我判定的核對項，D14 把增根從隱性錯誤變成可指認的對象。',
        density='抽離小班（Tier 2）',
        fading='第一輪：三張手順卡完整給，練習 A 每題旁重印精簡步驟號。'
               '第二輪：手順卡只留「※ 驗根」一句，練習 B 只在區塊開頭放一次。'
               '第三輪：只問「這題有幾步」，練習 C 不放任何步驟提示。'
               '第四輪：完全移除，改由學生自己在草稿上先寫四步再動筆。',
        flows=('F1 師徒制對話四步（我做→我們做→你做→你教我）',
               'F2 番茄鐘分段：每完成一個區塊停下來對自我核對清單'),
        iep_codes=('a3 提示題目重點', 'a5 分段作答', 'a6 增加行距／放大作答欄',
                   'b5 可使用計算機'),
        extra=(('工具卡', '本單元另出《工具卡_三種方程手順卡》，'
                          '三張卡剪下護貝後放桌面，解題時手指實時跟蹤。'),),
    )

    out = build_docx(P, os.path.join(BASE, '講義_分式方程無理方程與二元二次方程組_融合版.docx'),
                     footer_text=FOOT)
    return out


# ================================================================ 練習
def _combined_steps():
    """練習B 的褪除版：三張手順卡合成一張三欄對照表。

    原本三張獨立的 compact 卡會被分頁切開（QA 實測：兩張留在上一頁、
    一張跟題目跑到下一頁，學生要翻頁看提示，違背「區塊開頭放一次」的原意）。
    併成一張表既省版面，也讓三種方程的步驟橫向可比。
    """
    cards = (CARD_FRAC, CARD_SURD, CARD_SYS)
    w = _PAGE_CONTENT_WIDTH // 3
    widths = [w, w, _PAGE_CONTENT_WIDTH - 2 * w]
    rows = [{'hdr': True,
             'cells': [{'p': [para(c['title'], bold=True, sz=21, spacing=False)],
                        'shd': GREY_FILL} for c in cards]}]
    for i in range(4):
        rows.append({'cells': [
            [para(f'{i + 1}. {c["steps"][i][0]}', sz=20, spacing=False)]
            for c in cards]})
    return _tbl(rows, widths)


def build_exercise():
    P = []
    P.append(masthead(SUBJ, UNIT, '課堂練習'))
    P.append(student_info_row())
    P.append(para('做題之前，先回頭看《課堂講義》的三個範例，'
                  '並把《工具卡》的三張手順卡放在桌面。'))

    # ---------------- 練習 A
    P.append(heading(f'一、練習A（{star_label(1)}）'))
    P.append(para('每題旁邊都印了步驟號，跟著填。'))

    P.append(problem_box([
        para('1．解分式方程 {frac(4,x)=x-3}', bold=True),
        para('（步驟 1）最簡公分母是 ＿＿＿＿＿', spacing=False),
        para('（步驟 2）兩邊乘最簡公分母，去分母，得 {4=x(x-3)}', spacing=False),
        para('（步驟 3）展開、移項，得 {x^2-3x-4=0}', spacing=False),
        para('　　　　　因式分解，得 {(x-4)(x+1)=0}', spacing=False),
        para('　　　　　分兩支：{x_1} ＝ ＿＿＿＿　或　{x_2} ＝ ＿＿＿＿', spacing=False),
        para('（步驟 4）驗根：把兩個解代入分母 {x}，都不等於 ＿＿＿＿，所以都保留',
             spacing=False),
        para('∴ ', bold=True),
    ] + write_lines(2)))

    P.append(problem_box([
        para('2．解無理方程 {sqrt(x+3)=x-3}', bold=True),
        para('（步驟 1）根號已經單獨在左邊，可以直接平方', spacing=False),
        para('（步驟 2）兩邊平方，得 {x+3=x^2-6x+9}', spacing=False),
        para('（步驟 3）移項，得 {x^2-7x+6=0}', spacing=False),
        para('　　　　　因式分解，得 {(x-1)(x-6)=0}', spacing=False),
        para('　　　　　分兩支：{x_1} ＝ ＿＿＿＿　或　{x_2} ＝ ＿＿＿＿', spacing=False),
        para('（步驟 4）驗根——這題一定有一個要捨：', spacing=False),
        para(f'　　　{{x=1}}：左 ＝ ＿＿＿＿，右 ＝ ＿＿＿＿　'
             f'{CHECKBOX} 相等　{CHECKBOX} 不相等', spacing=False),
        para(f'　　　{{x=6}}：左 ＝ ＿＿＿＿，右 ＝ ＿＿＿＿　'
             f'{CHECKBOX} 相等　{CHECKBOX} 不相等', spacing=False),
        para('∴ ', bold=True),
    ] + write_lines(2)))

    P.append(problem_box([
        para('3．解方程組 {y=x-1}　與　{x^2+y^2=13}', bold=True),
        para('（步驟 1、2）一次方程已經解好 {y}，可以直接代入', spacing=False),
        para('（步驟 3）代入，得 {x^2+(x-1)^2=13}', spacing=False),
        para('　　　　　展開、整理、兩邊除以 2，得 {x^2-x-6=0}', spacing=False),
        para('　　　　　因式分解，得 {(x-3)(x+2)=0}', spacing=False),
        para('　　　　　分兩支：{x_1} ＝ ＿＿＿＿　或　{x_2} ＝ ＿＿＿＿', spacing=False),
        para('（步驟 4）回代 {y=x-1}：{y_1} ＝ ＿＿＿＿　或　{y_2} ＝ ＿＿＿＿',
             spacing=False),
        para('∴ ', bold=True),
    ] + write_lines(2)))

    P.append(selfcheck_list([
        '每題都寫出了步驟 1 到步驟 4，沒有跳步',
        '去分母／平方之後，每一項都處理過了',
        '每個解都代回原方程（或分母）檢查過',
        '最後一行用「∴」寫了答句',
    ]))
    P.append(checkpoint_rule())

    # ---------------- 練習 B
    P.append(heading(f'二、練習B（{star_label(2)}）'))
    P.append(para('這一區塊的步驟提示只放這一次，做題時自己回想。'))
    P.append(_combined_steps())
    P.append(blank())

    P.append(problem_box([
        para('4．解分式方程 {frac(x,x-2)-frac(3,x)=1}', bold=True),
    ] + write_lines(6)))

    P.append(problem_box([
        para('5．解無理方程 {sqrt(2x+1)=x-1}', bold=True),
    ] + write_lines(6)))

    P.append(problem_box([
        para('6．解方程組 {x+y=5}　與　{xy=6}', bold=True),
    ] + write_lines(6)))

    P.append(selfcheck_list([
        '驗根是寫在紙上的，不是心裡想一想就跳過',
        '捨去的根有寫明為什麼捨（令分母為 0／左右不相等）',
        '方程組的答案成對寫，每個 x 都配了對應的 y',
        '最後一行用「∴」寫了答句',
    ]))
    P.append(checkpoint_rule())

    # ---------------- 練習 C
    P.append(heading(f'三、練習C（{star_label(3)}）'))

    P.append(problem_box([
        para('7．甲、乙兩地相距 30 公里。小明騎單車從甲地到乙地，比開車多用 1 小時。'
             '已知開車速度是單車速度的 3 倍，求單車的速度。', bold=True),
        para('（先寫「設……」，再列方程）', sz=21, spacing=False),
    ] + write_lines(7)))

    P.append(problem_box([
        para('8．找錯題：小美解無理方程 {sqrt(x+6)=x}，過程如下——', bold=True),
        para('　　兩邊平方，得 {x+6=x^2}', spacing=False),
        para('　　整理，得 {x^2-x-6=0}', spacing=False),
        para('　　因式分解，得 {(x-3)(x+2)=0}', spacing=False),
        para('　　所以 {x=3} 或 {x=-2}', spacing=False),
        para('（一）小美漏了哪一步？', spacing=False),
    ] + write_lines(2) + [
        para('（二）正確答案是什麼？請寫出完整過程。', spacing=False),
    ] + write_lines(5)))

    P.append(problem_box([
        para('9．請你自己出一條分式方程，要求：解整式方程後會得到兩個數，'
             '但其中一個是增根、必須捨去。', bold=True),
        para('（一）寫出你的方程', spacing=False),
    ] + write_lines(2) + [
        para('（二）寫出完整解法（包括驗根）', spacing=False),
    ] + write_lines(5) + [
        para('（三）用一句話說明那個數為什麼要捨去', spacing=False),
    ] + write_lines(2)))

    P.append(selfcheck_list([
        '應用題有寫「設 x 是什麼」，而且答案有寫單位',
        '算出的答案代回題目情境檢查過，合乎現實',
        '找錯題有明確指出是哪一步漏了',
        '最後一行用「∴」寫了答句',
    ]))

    # ---------------- 答案
    P.append(heading('參考答案（教師用）', page_break_before=True))

    P.append(para('練習A', bold=True))
    P.append(worked_example_table([
        span_row('1．{frac(4,x)=x-3}', '分式方程'),
        eq_row('{4}', '{x(x-3)}', '兩邊乘 {x}'),
        eq_row('{x^2-3x-4}', '{0}', '移項'),
        or_row('{x-4}', '{0}', '{x+1}', '{0}', '因式分解，分兩支'),
        or_row('{x_1}', '{4}', '{x_2}', '{-1}', '解出兩支'),
        span_row('驗根：{4!=0}，{-1!=0}', '兩根都保留'),
        answer_row('{x_1=4} 或 {x_2=-1}', ''),
    ], why_pct=0.30))

    P.append(worked_example_table([
        span_row('2．{sqrt(x+3)=x-3}', '無理方程'),
        eq_row('{x+3}', '{x^2-6x+9}', '兩邊平方'),
        eq_row('{x^2-7x+6}', '{0}', '移項'),
        or_row('{x-1}', '{0}', '{x-6}', '{0}', '因式分解，分兩支'),
        or_row('{x_1}', '{1}', '{x_2}', '{6}', '解出兩支'),
        span_row('驗根 {x=1}：左 {sqrt(4)=2}，右 {-2}', '不相等，捨去'),
        span_row('驗根 {x=6}：左 {sqrt(9)=3}，右 {3}', '相等，保留'),
        answer_row('{x=6}', ''),
    ], why_pct=0.30))

    P.append(worked_example_table([
        span_row('3．{y=x-1} 與 {x^2+y^2=13}', '方程組'),
        eq_row('{x^2+(x-1)^2}', '{13}', '代入'),
        eq_row('{x^2-x-6}', '{0}', '展開、整理、除以 2'),
        or_row('{x-3}', '{0}', '{x+2}', '{0}', '因式分解，分兩支'),
        or_row('{x_1}', '{3}', '{x_2}', '{-2}', '解出 {x}'),
        or_row('{y_1}', '{2}', '{y_2}', '{-3}', '回代 {y=x-1}'),
        answer_row('{(3,2)} 或 {(-2,-3)}', ''),
    ], why_pct=0.30))

    P.append(para('練習B', bold=True))
    P.append(worked_example_table([
        span_row('4．{frac(x,x-2)-frac(3,x)=1}', '最簡公分母 {x(x-2)}'),
        eq_row('{x^2-3(x-2)}', '{x(x-2)}', '兩邊乘 {x(x-2)}'),
        eq_row('{x^2-3x+6}', '{x^2-2x}', '展開'),
        eq_row('{6}', '{x}', '消去 {x^2}，移項'),
        span_row('驗根：{6!=0}，{6-2=4!=0}', '保留'),
        answer_row('{x=6}', '註：此題降為一次，只有一個解'),
    ], why_pct=0.34))

    P.append(worked_example_table([
        span_row('5．{sqrt(2x+1)=x-1}', '無理方程'),
        eq_row('{2x+1}', '{x^2-2x+1}', '兩邊平方'),
        eq_row('{x^2-4x}', '{0}', '移項'),
        or_row('{x}', '{0}', '{x-4}', '{0}', '因式分解，分兩支'),
        or_row('{x_1}', '{0}', '{x_2}', '{4}', '解出兩支'),
        span_row('驗根 {x=0}：左 {sqrt(1)=1}，右 {-1}', '不相等，捨去'),
        span_row('驗根 {x=4}：左 {sqrt(9)=3}，右 {3}', '相等，保留'),
        answer_row('{x=4}', ''),
    ], why_pct=0.30))

    P.append(worked_example_table([
        span_row('6．{x+y=5} 與 {xy=6}', '用代入消元，不用韋達定理'),
        eq_row('{y}', '{5-x}', '從一次方程解出 {y}'),
        eq_row('{x(5-x)}', '{6}', '代入'),
        eq_row('{x^2-5x+6}', '{0}', '整理'),
        or_row('{x-2}', '{0}', '{x-3}', '{0}', '因式分解，分兩支'),
        or_row('{x_1}', '{2}', '{x_2}', '{3}', '解出 {x}'),
        or_row('{y_1}', '{3}', '{y_2}', '{2}', '回代 {y=5-x}'),
        answer_row('{(2,3)} 或 {(3,2)}', ''),
    ], why_pct=0.30))

    P.append(para('練習C', bold=True))
    P.append(worked_example_table([
        span_row('7．設單車速度為 {x} km/h（{x>0}），開車速度 {3x} km/h', '應用題'),
        eq_row('{frac(30,x)-frac(30,3x)}', '{1}', '單車用時 − 開車用時 ＝ 1 小時'),
        eq_row('{90-30}', '{3x}', '兩邊乘 {3x}'),
        eq_row('{60}', '{3x}', '左邊相減'),
        eq_row('{x}', '{20}', '兩邊除以 3'),
        span_row('驗根：{20!=0}，且 {x>0} 合乎情境', '單車 1.5 小時、開車 0.5 小時，差 1 小時'),
        answer_row('單車的速度是 20 km/h', '應用題答句要寫單位'),
    ], why_pct=0.36))

    P.append(problem_box([
        para('8．（一）漏了驗根。兩邊平方是不可逆運算，可能多出不合原方程的根，'
             '每個解都要代回原方程檢查。'),
        para('（二）驗根：{x=3} 時左 {sqrt(9)=3}、右 {3}，相等，保留；'
             '{x=-2} 時左 {sqrt(4)=2}、右 {-2}，不相等，捨去。', spacing=False),
        para('∴ {x=3}', bold=True),
        para('※ 小美前四步的代數運算全部正確，唯一缺失是驗根。', sz=21, spacing=False),
    ]))

    P.append(problem_box([
        para('9．學生答案只要符合「有一個增根要捨」即可。參考其中一種：'),
        para('方程：{frac(x^2,x-1)=frac(1,x-1)}', spacing=False),
        para('兩邊乘 {(x-1)} 得 {x^2=1}；移項得 {x^2-1=0}；'
             '因式分解得 {(x-1)(x+1)=0}；分兩支得 {x_1=1} 或 {x_2=-1}', spacing=False),
        para('驗根：{x=1} 令分母 {x-1=0}，增根捨去；'
             '{x=-1} 時分母 {-1-1=-2}，不等於 0，保留', spacing=False),
        para('∴ {x=-1}', bold=True),
        para('（三）{x=1} 會令原方程的分母等於 0，分式在該處無意義，'
             '所以它不是原方程的解。', spacing=False),
    ], trailing_blank=False))

    out = build_docx(P, os.path.join(BASE, '練習_分式方程無理方程與二元二次方程組_融合版.docx'),
                     footer_text=FOOT)
    return out


# ================================================================ 工具卡
def build_toolcards():
    P = []
    P.append(masthead(SUBJ, UNIT, '工具卡'))
    P.append(para('沿虛線剪下，護貝後放在桌面。解題時把對應的那張卡放在作業本旁邊，'
                  '手指指住你正在做的那一步。', sz=21))
    P.append(blank())

    def card(c):
        out = [para(f'▍{c["title"]}', bold=True, sz=HEADING_SZ, spacing=False),
               para(f'什麼時候翻我：{c["trigger"]}', sz=20, spacing=False),
               blank()]
        for i, (act, pit) in enumerate(c['steps'], 1):
            out.append(para(f'{i}. {act}', bold=True, sz=21, spacing=False))
            out.append(para(f'※ {pit}', sz=19, spacing=False))
        return out

    verify_card = [
        para('▍驗根小卡（三種方程共用）', bold=True, sz=HEADING_SZ, spacing=False),
        para('什麼時候翻我：算出答案之後、寫「∴」之前', sz=20, spacing=False),
        blank(),
        para('分式方程：把解代入原方程的分母', bold=True, sz=21, spacing=False),
        para('※ 分母算出來是 0 → 增根，捨去', sz=19, spacing=False),
        para('無理方程：把解代入原方程，左右各自算一次', bold=True, sz=21, spacing=False),
        para('※ 左右不相等 → 假根，捨去', sz=19, spacing=False),
        para('方程組：把每一對 {(x,y)} 代入兩條方程', bold=True, sz=21, spacing=False),
        para('※ 兩條都成立才算對', sz=19, spacing=False),
        blank(),
        para('捨去的時候要寫明理由，不要只寫「捨」。', sz=19, spacing=False),
    ]

    P.append(toolcard_sheet([card(CARD_FRAC), card(CARD_SURD),
                             card(CARD_SYS), verify_card], cols=2, card_h=5200))

    out = build_docx(P, os.path.join(BASE, '工具卡_三種方程手順卡.docx'),
                     footer_text=FOOT)
    return out


if __name__ == '__main__':
    for f in (build_handout, build_exercise, build_toolcards):
        print(f())
