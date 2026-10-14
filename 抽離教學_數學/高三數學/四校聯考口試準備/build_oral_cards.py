# -*- coding: utf-8 -*-
r"""
build_oral_cards.py — 高三甲（文）融合生：四校聯考 2020／2021 正卷選擇題「課堂口試講解」準備卡

背景（使用者 2026-10-14）：大班活動要求學生自主完成 2020、2021 四校聯考正卷選擇題（30 題）並寫解答過程，
再於課堂抽籤口試講解（評分：解答過程 20%＋口試 80%，脫稿／對稿 × 向全班／只向老師分級封頂）。
抽離老師不入大班課室，評分規則盡量不調整，抽離課有 2–3 堂準備。

使用者裁決（2026-10-14）：
- 保底題組 8 題：2020 Q1、Q5、Q11、Q13；2021 Q1、Q3、Q5、Q12
  （選題依據：甲班 IEP 高頻單元「基本概念／二次方程及二次函數／數列」＋第一學段抽離已複習單元＋入門難度；
   佔 30 題 27%，在 2026-07-18 調適申請「內容調適不多於原卷 40%」之內——向科任商量抽籤範圍時引用）。
- 只出「口試講解卡」一份；教學設計＝主 D6 明確教學（放聲思考）＋輔 D2 手順卡。

每張卡一頁（使用者 2026-10-14 定：只出正面）：題目 → 一、講稿（手順＋放聲思考引號句，※ 易錯點）→ 二、寫在紙上的算式（等號對齊）。
（初版另有背面：脫稿提示＋老師追問＋作答線，已按使用者指示拿走，資料仍在 CARDS 內。）
題目原文取自 worksheet-tools\data\ALL.json；答案逐題 sympy 驗算，見 驗算_四校聯考口試講解卡.md。
"""
import sys, os, re

SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _tbl, _PAGE_CONTENT_WIDTH

OUT = os.path.dirname(os.path.abspath(__file__))
BASE = '工具卡_四校聯考2020-2021選擇題口試講解'
SUBJECT = '高三數學（抽離）'
UNIT = '四校聯考 2020–2021 正卷選擇題・口試準備'
FOOT = '高三數學．四校聯考選擇題口試講解卡'
W = _PAGE_CONTENT_WIDTH
STEP_COL = int(W * 0.17)


# ---------------- 版面零件 ----------------
def label(text):
    # 小標：段前 6pt、段後 2pt，不套 1.5 倍行距（一張卡要擠進一頁）
    return para([('t', text)], bold=True, keep_next=True, spacing=False).replace(
        '<w:keepNext/>', '<w:keepNext/><w:spacing w:before="120" w:after="40"/>', 1)


def options(opts):
    """(A)–(E) 選項：短選項一行排完，長選項每行 3 個／2 個。"""
    letters = 'ABCDE'
    items = [f'({letters[i]}) {o}' for i, o in enumerate(opts)]
    longest = max(len(o) for o in opts)
    n = 5 if longest <= 9 else (3 if longest <= 22 else 2)
    rows = ['　　　'.join(items[i:i + n]) for i in range(0, len(items), n)]
    return [para(r, spacing=False) for r in rows]


def wrap(markup):
    """eq_row／or_row 的左右式要自己包 {}（否則當純文字，集合的大括號還會被吃掉）。"""
    return '{' + markup + '}' if markup else ''


def wrap_rows(rows):
    out = []
    for r in rows:
        r = dict(r)
        if r['k'] in ('eq', 'or'):
            for k in ('lhs', 'rhs', 'lhs2', 'rhs2'):
                if k in r:
                    r[k] = wrap(r[k])
        out.append(r)
    return out


# para(spacing=False) 並不是零行距（記憶 docx_spacing_false_is_not_zero）：表格內會被
# Word Normal 的段後 8pt 撐高。做法照 build_remedial_20261015 的 tighten()。
_PPR = re.compile(r'<w:pPr>((?:(?!</w:pPr>).)*?)</w:pPr>', re.S)
_SPACER = '<w:p><w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr></w:p>'
_SPACER_SLIM = ('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="160" '
                'w:lineRule="exact"/></w:pPr></w:p>')


def tighten(xml):
    def fix(m):
        inner = m.group(1)
        if '<w:spacing' in inner or '<w:jc ' not in inner or '<w:ind' in inner:
            return m.group(0)
        inner = inner.replace('<w:jc ', '<w:spacing w:before="20" w:after="20" w:line="264" '
                                        'w:lineRule="auto"/><w:jc ', 1)
        return f'<w:pPr>{inner}</w:pPr>'
    xml = _PPR.sub(fix, xml).replace(_SPACER, _SPACER_SLIM)
    # 儲存格上下內邊距 70 → 30 twips（記憶 table_doc_page_saving_order：只動留白，不縮字級）
    return (xml.replace('<w:top w:w="70" w:type="dxa"/>', '<w:top w:w="30" w:type="dxa"/>')
               .replace('<w:bottom w:w="70" w:type="dxa"/>', '<w:bottom w:w="30" w:type="dxa"/>'))


def script_table(steps):
    """D2＋D6：左欄手順（一個核心動作），右欄放聲思考講稿；※ 易錯點接在講稿下。"""
    rows = [{'hdr': True, 'cells': [
        {'p': [para('手順', bold=True, sz=22, spacing=False)], 'shd': GREY_FILL},
        {'p': [para('講稿（先照讀，再背出來）', bold=True, sz=22, spacing=False)], 'shd': GREY_FILL}]}]
    for i, st in enumerate(steps, 1):
        act, words = st[0], st[1]
        pit = st[2] if len(st) > 2 else None
        # 講稿可給多句（list）：一句一行，公式就不會被 Word 從中間斷行
        sents = [words] if isinstance(words, str) else list(words)
        sents[0] = '「' + sents[0]
        sents[-1] = sents[-1] + '」'
        right = [para(t, spacing=False) for t in sents]
        if pit:
            right.append(para(f'※ {pit}', sz=21, spacing=False))
        rows.append({'cells': [
            {'p': [para(f'{marker(i)} {act}', bold=True, spacing=False)], 'va': 'center'},
            {'p': right, 'va': 'center'}]})
    return _tbl(rows, [STEP_COL, W - STEP_COL])


def followups(qas):
    ps = []
    for q, a in qas:
        ps.append(para([('c', '問：', '000000')] + text_to_segments(q), spacing=False))
        ps.append(para([('t', '答：')] + text_to_segments(a), spacing=False))
    return shaded_multi_box(ps)


def card(no, src, title, body, opts, steps, rows, qas, cue, first=False, col_frac=None, why_pct=0.34):
    P = [heading(f'講解卡 {no}｜{src}　{title}', page_break_before=not first)]
    P.append(problem_box([para(body)] + options(opts)))
    P.append(label('一、講稿'))
    P.append(script_table(steps))
    P.append(label('二、寫在紙上的算式'))
    P.append(worked_example_table(wrap_rows(rows), why_pct=why_pct, col_frac=col_frac))
    # 使用者 2026-10-14：只出正面、不要背面。qas（老師追問）／cue（脫稿提示）資料保留在
    # CARDS 內、驗算檔已覆核，日後要加回只需在這裡重新排版。
    return P


# ---------------- 8 張卡 ----------------
CARDS = []

# 1｜2020 Q1
CARDS.append(dict(
    src='2020 年第 1 題', title='集合的交集與聯集',
    body='若 {P={0,1,2}}，{Q={0,2,3}}，{R={1,2,3,4}}，則 {P∩(Q∪R)=}',
    opts=['{{0,1,2}}', '{{0,1,2,3,4}}', '{{2}}', '{∅}', '以上皆非'],
    steps=[
        ('說考點', '這題考集合的交集和聯集。'),
        ('定次序', '括號先做，所以我先算 {Q∪R}，再和 {P} 取交集。',
         '聯集＝兩個集合的元素全部合起來；交集＝兩邊都有的元素'),
        ('講計算', ['{Q∪R} 把元素合起來，重複的只寫一次，得 {{0,1,2,3,4}}。',
                    '再和 {P} 取共同元素，得 {{0,1,2}}。']),
        ('講答案', '所以答案是 A。'),
    ],
    rows=[
        eq_row('Q∪R', '{0,2,3}∪{1,2,3,4}', '先做括號'),
        eq_row('', '{0,1,2,3,4}', '合併元素，2、3 只寫一次'),
        eq_row('P∩(Q∪R)', '{0,1,2}∩{0,1,2,3,4}', '代入 {P}'),
        eq_row('', '{0,1,2}', '取兩邊都有的元素'),
        answer_row('選 (A)', '作答'),
    ],
    qas=[
        ('為什麼不是 C {{2}}？',
         '{{2}} 是三個集合都有的元素，即 {P∩Q∩R}；但題目中 {Q} 和 {R} 之間是聯集，不是交集。'),
        ('如果題目改成 {(P∩Q)∪R}，答案一樣嗎？',
         '不一樣。{P∩Q={0,2}}，再和 {R} 取聯集得 {{0,1,2,3,4}}，即選 B。'),
    ],
    cue='先算括號 {Q∪R} → 再和 {P} 取交集 → 選 A',
))

# 2｜2020 Q5
CARDS.append(dict(
    src='2020 年第 5 題', title='含絕對值的不等式',
    body='若 {|-3x-5|<=4}，則',
    opts=['{-frac(1,3)<=x<=3}', '{frac(1,3)<=x<=3}', '{-3<=x<=-frac(1,3)}',
          '{-3<=x<=frac(1,3)}', '{x<=-3} 或 {x>=-frac(1,3)}'],
    steps=[
        ('說考點', '這題考含絕對值的不等式。'),
        ('拆絕對值', ['絕對值小於或等於 4，表示裡面的式子夾在 {-4} 和 {4} 之間。',
                      '所以寫成 {-4<=-3x-5<=4}。'],
         '「小於或等於」是夾在中間；「大於或等於」才是分成兩邊'),
        ('講計算', ['三邊同時加 5，得 {1<=-3x<=9}。',
                    '再三邊同時除以 {-3}，不等號要反轉，整理得 {-3<=x<=-frac(1,3)}。'],
         '除以負數，不等號要反轉'),
        ('講答案', '所以答案是 C。'),
    ],
    rows=[
        eq_row('-4', '-3x-5<=4', '去絕對值：夾在 {-4} 和 {4} 之間', rel='{<=}'),
        eq_row('1', '-3x<=9', '三邊同時加 5', rel='{<=}'),
        eq_row('-frac(1,3)', 'x>=-3', '三邊同時除以 {-3}，不等號反轉', rel='{>=}'),
        eq_row('-3', 'x<=-frac(1,3)', '由小到大重寫', rel='{<=}'),
        answer_row('{-3<=x<=-frac(1,3)}，選 (C)', '作答'),
    ],
    qas=[
        ('為什麼不等號要反轉？',
         '因為除以負數。例如 {2<3}，兩邊除以 {-1} 會變成 {-2>-3}。'),
        ('如果題目是 {|-3x-5|>=4}，答案是哪一個？',
         '變成分成兩邊：{-3x-5<=-4} 或 {-3x-5>=4}，得 {x>=-frac(1,3)} 或 {x<=-3}，即選 E。'),
    ],
    cue='小於或等於 → 夾中間 → 三邊加 5 → 除以 {-3} 要反轉 → 選 C',
))

# 3｜2020 Q11
CARDS.append(dict(
    src='2020 年第 11 題', title='拋物線的平移',
    body='若將拋物線 {y=(x+1)^2} 的圖形向右平移 4 個單位，再向下移動 5 個單位，所得的拋物線方程為何？',
    opts=['{y=(x-3)^2-5}', '{y=(x+5)^2-5}', '{y=(x-5)^2+3}', '{y=(x+3)^2-5}', '{y=(x+4)^2-5}'],
    steps=[
        ('說考點', '這題考拋物線的平移。'),
        ('說規則', ['向右平移 4 個單位，是把 {x} 換成 {x-4}。',
                    '向下平移 5 個單位，是在整條式子後面減 5。'],
         '向右是「減」，向左才是「加」'),
        ('講計算', '{(x+1)} 換成 {(x-4+1)}，即 {(x-3)}；再減 5，得 {y=(x-3)^2-5}。'),
        ('講答案', '所以答案是 A。'),
    ],
    rows=[
        eq_row('y', '(x+1)^2', '原拋物線'),
        eq_row('y', '(x-4+1)^2', '向右 4：{x} 換成 {x-4}'),
        eq_row('y', '(x-3)^2', '化簡括號'),
        eq_row('y', '(x-3)^2-5', '向下 5：整條式子減 5'),
        answer_row('{y=(x-3)^2-5}，選 (A)', '作答'),
    ],
    qas=[
        ('你怎樣檢查答案？',
         '看頂點。原頂點是 {(-1,0)}，向右 4、向下 5，得 {(3,-5)}；{y=(x-3)^2-5} 的頂點正是 {(3,-5)}。'),
        ('為什麼不是 D {y=(x+3)^2-5}？',
         'D 的頂點是 {(-3,-5)}，即是向左移了 2 個單位，方向錯了。'),
    ],
    cue='右 4 → {x} 換 {x-4} → 下 5 → 整條減 5 → 選 A',
))

# 4｜2020 Q13
CARDS.append(dict(
    src='2020 年第 13 題', title='等差數列有多少項為正',
    body='在等差數列 {{a_n}_{n>=1}} 中，{a_2=22} 及 {a_5=13}，此數列中有多少項為正值？',
    opts=['{6}', '{7}', '{8}', '{9}', '{10}'],
    steps=[
        ('說考點', '這題考等差數列的通項公式 {a_n=a_1+(n-1)d}。'),
        ('求 d 和 a₁', ['第 2 項到第 5 項相差 3 個公差，所以 {3d=13-22}，得 {d=-3}。',
                       '再由 {a_2=a_1+d}，得 {a_1=25}。'],
         '第 2 項到第 5 項是 3 個公差，不是 5 個'),
        ('列不等式', ['要正值，就是 {a_n>0}，即 {28-3n>0}。',
                      '得 {n<frac(28,3)}，即 {n} 小於 {9 frac(1,3)}。'],
         '{n} 是項數，只可以取正整數'),
        ('講答案', '{n} 可以是 1 到 9，共 9 項，所以答案是 D。'),
    ],
    rows=[
        eq_row('3d', '13-22', '第 2 項到第 5 項：3 個公差'),
        eq_row('d', '-3', ''),
        eq_row('a_1', '22-(-3)', '由 {a_2=a_1+d}'),
        eq_row('a_1', '25', ''),
        eq_row('a_n', '25+(n-1)(-3)', '代入通項公式'),
        eq_row('a_n', '28-3n', '展開整理'),
        eq_row('28-3n', '0', '正值：{a_n>0}', rel='{>}'),
        eq_row('-3n', '-28', '移項', rel='{>}'),
        eq_row('n', 'frac(28,3)', '除以 {-3}，不等號反轉', rel='{<}'),
        answer_row('{n=1,2,…,9}，共 9 項，選 (D)', '{frac(28,3)=9 frac(1,3)}，{n} 取正整數'),
    ],
    qas=[
        ('為什麼不是 10 項？',
         '第 10 項 {a_{10}=28-30=-2} 是負數；第 9 項 {a_9=28-27=1} 才是最後一個正數。'),
        ('公差為什麼是負數？',
         '數列由 22 減少到 13，越來越小，所以公差是負的。'),
    ],
    cue='差 3 個公差 → {d=-3}、{a_1=25} → {a_n=28-3n>0} → {n<=9} → 選 D',
))

# 5｜2021 Q1
CARDS.append(dict(
    src='2021 年第 1 題', title='二次不等式與集合',
    body='若集合 {P={1,2,3,5,7,11}}，{Q=}｛{x}：{x^2-15x+36<0}｝，求 {P∩Q} 中元素的個數。',
    opts=['{2}', '{3}', '{4}', '{5}', '{1}'],
    steps=[
        ('說考點', '這題考解二次不等式，再取集合的交集。'),
        ('求兩根', ['先把 {x^2-15x+36} 因式分解成 {(x-3)(x-12)}。',
                    '令它等於 0，得 {x=3} 或 {x=12}。']),
        ('定範圍', '題目是小於 0，拋物線開口向上，小於 0 取兩根中間，所以 {3<x<12}。',
         '不包括 3 和 12'),
        ('講答案', '{P} 之中在 3 和 12 之間的有 5、7、11，共 3 個，所以答案是 B。',
         '3 不在範圍內，不可以數'),
    ],
    rows=[
        eq_row('x^2-15x+36', '0', '{Q} 的條件', rel='{<}'),
        eq_row('x^2-15x+36', '0', '先把不等號換成等號，求兩根'),
        eq_row('(x-3)(x-12)', '0', '因式分解'),
        or_row('x-3', '0', 'x-12', '0', ''),
        or_row('x_1', '3', 'x_2', '12', ''),
        span_row('{3<x<12}', '開口向上、小於 0：取兩根中間'),
        eq_row('P∩Q', '{5,7,11}', '在 {P} 之中揀出 {3<x<12} 的元素'),
        answer_row('{P∩Q} 有 3 個元素，選 (B)', '作答'),
    ],
    qas=[
        ('為什麼 3 不算？',
         '不等號是「小於」，不是「小於或等於」。{x=3} 時式子等於 0，不小於 0。'),
        ('為什麼取中間，不是取兩邊？',
         '拋物線開口向上，兩根之間的部分在 {x} 軸下方，即 {y<0}。'),
    ],
    cue='因式分解 → 兩根 3、12 → 小於 0 取中間 → 5、7、11 → 選 B',
    col_frac=(0.300, 0.055, 0.170, 0.070, 0.150, 0.055),
))

# 6｜2021 Q3
CARDS.append(dict(
    src='2021 年第 3 題', title='由前 n 項和求第 n 項',
    body='有一等差數列前 {n} 項之總和為 {n^2}，求此數列的第 10 項。',
    opts=['{19}', '{21}', '{28}', '{31}', '{40}'],
    steps=[
        ('說考點', '這題考數列『前 {n} 項和 {S_n}』與『第 {n} 項 {a_n}』的關係。'),
        ('說方法', '第 10 項等於前 10 項的和減去前 9 項的和，即 {a_{10}=S_{10}-S_9}。',
         '不是 {S_{10}} 本身——{S_{10}=100} 是前 10 項加起來'),
        ('講計算', '{S_{10}=100}，{S_9=81}，相減得 19。'),
        ('講答案', '所以答案是 A。'),
    ],
    rows=[
        eq_row('a_{10}', 'S_{10}-S_9', '前 10 項和減去前 9 項和，剩下第 10 項'),
        eq_row('a_{10}', '10^2-9^2', '代入 {S_n=n^2}'),
        eq_row('a_{10}', '100-81', ''),
        eq_row('a_{10}', '19', ''),
        answer_row('{a_{10}=19}，選 (A)', '作答'),
    ],
    qas=[
        ('為什麼 {a_{10}=S_{10}-S_9}？',
         '{S_{10}=a_1+…+a_9+a_{10}}，{S_9=a_1+…+a_9}，兩者相減只剩 {a_{10}}。'),
        ('有沒有另一個方法？',
         '{a_1=S_1=1}，{a_2=S_2-S_1=3}，所以公差是 2，{a_{10}=1+9×2=19}。'),
    ],
    cue='{a_{10}=S_{10}-S_9} → {100-81} → 19 → 選 A',
))

# 7｜2021 Q5
CARDS.append(dict(
    src='2021 年第 5 題', title='韋達定理：倒數根的新方程',
    body='已知 {-2x^2+3x-7=0} 的根為 {α} 和 {β}。下列哪一個方程的根為 {frac(1,α)} 和 {frac(1,β)}？',
    opts=['{x^2-3x+7=0}', '{7x^2-3x+2=0}', '{7x^2+3x+2=0}', '{2x^2-3x-7=0}', '以上皆非'],
    steps=[
        ('說考點', '這題考韋達定理：兩根之和 {=-frac(b,a)}，兩根之積 {=frac(c,a)}。'),
        ('原方程', '{a=-2}，{b=3}，{c=-7}，所以 {α+β=frac(3,2)}，{αβ=frac(7,2)}。',
         '{-frac(b,a)=-frac(3,-2)=frac(3,2)}，留意兩個負號'),
        ('新兩根', ['新兩根之和 {frac(1,α)+frac(1,β)}，通分得 {frac(α+β,αβ)=frac(3,7)}。',
                    '新兩根之積 {frac(1,αβ)=frac(2,7)}。']),
        ('講答案', ['新方程是 {x^2-}（和）{x+}（積）{=0}，即 {x^2-frac(3,7)x+frac(2,7)=0}。',
                    '兩邊乘以 7，得 {7x^2-3x+2=0}，所以答案是 B。']),
    ],
    rows=[
        span_row('{a=-2}，{b=3}，{c=-7}', '讀係數'),
        eq_row('α+β', 'frac(3,2)', '兩根之和 {=-frac(b,a)}'),
        eq_row('αβ', 'frac(7,2)', '兩根之積 {=frac(c,a)}'),
        eq_row('frac(1,α)+frac(1,β)', 'frac(α+β,αβ)', '通分'),
        eq_row('', 'frac(3,7)', '代入：{frac(3,2)÷frac(7,2)}'),
        eq_row('frac(1,α)×frac(1,β)', 'frac(1,αβ)', ''),
        eq_row('', 'frac(2,7)', '代入：{1÷frac(7,2)}'),
        eq_row('x^2-frac(3,7)x+frac(2,7)', '0', '{x^2-}（和）{x+}（積）{=0}'),
        eq_row('7x^2-3x+2', '0', '兩邊乘以 7'),
        answer_row('選 (B)', '作答'),
    ],
    qas=[
        ('為什麼不用先求出 {α}、{β}？',
         '判別式 {3^2-4(-2)(-7)=-47<0}，原方程沒有實數根；但韋達定理只需要和與積，照樣可以用。'),
        ('有沒有快捷方法？',
         '根變成倒數時，把係數次序倒轉：{-7x^2+3x-2=0}，乘以 {-1} 得 {7x^2-3x+2=0}。'),
    ],
    cue='和 {frac(3,2)}、積 {frac(7,2)} → 新和 {frac(3,7)}、新積 {frac(2,7)} → '
        '{x^2-}（和）{x+}（積）{=0} → 乘 7 → 選 B',
    col_frac=(0.380, 0.050, 0.140, 0.060, 0.110, 0.050), why_pct=0.30,
))

# 8｜2021 Q12
CARDS.append(dict(
    src='2021 年第 12 題', title='垂直平分線的方程',
    body='已知點 {P(-1,-3)} 和 {Q(5,-1)}，求 {PQ} 的垂直平分線的方程。',
    opts=['{x+3y-4=0}', '{x-3y+4=0}', '{x+3y+4=0}', '{3x-y-4=0}', '{3x+y-4=0}'],
    steps=[
        ('說考點', '垂直平分線有兩個條件：經過 {PQ} 的中點，而且和 {PQ} 垂直。'),
        ('求中點', '中點的坐標是兩點坐標的平均，得 {M(2,-2)}。'),
        ('求斜率', ['{PQ} 的斜率是 {frac(2,6)=frac(1,3)}。',
                    '互相垂直的直線斜率相乘等於 {-1}，所以垂直平分線的斜率是 {-3}。'],
         '負倒數：{frac(1,3)} 變 {-3}，要變號又要倒轉'),
        ('講答案', '用點斜式 {y-(-2)=-3(x-2)}，整理得 {3x+y-4=0}，所以答案是 E。'),
    ],
    rows=[
        eq_row('M', '(frac(-1+5,2), frac(-3+(-1),2))', '中點公式'),
        eq_row('M', '(2,-2)', ''),
        eq_row('m_{PQ}', 'frac(-1-(-3),5-(-1))', '斜率公式'),
        eq_row('m_{PQ}', 'frac(1,3)', ''),
        eq_row('m', '-3', '垂直：斜率相乘 {=-1}'),
        eq_row('y-(-2)', '-3(x-2)', '點斜式，經過 {M(2,-2)}'),
        eq_row('y+2', '-3x+6', '展開'),
        eq_row('3x+y-4', '0', '移項，整理成一般式'),
        answer_row('選 (E)', '作答'),
    ],
    qas=[
        ('你怎樣檢查答案？',
         '把中點 {(2,-2)} 代入 {3x+y-4}，得 {6-2-4=0}，所以直線經過中點。'),
        ('為什麼斜率是 {-3}，不是 {3}？',
         '互相垂直的兩條直線斜率相乘等於 {-1}，而 {frac(1,3)×(-3)=-1}。'),
    ],
    cue='中點 {(2,-2)} → 斜率 {frac(1,3)} → 負倒數 {-3} → 點斜式 → 選 E',
))


def build():
    P = [masthead(SUBJECT, UNIT, '口試講解卡')]
    P.append(shaded_box('用法：① 照讀講稿，手指著對應的算式　→　② 遮住講稿，只看算式講'
                        '　→　③ 只看題目講', sz=22))
    for i, c in enumerate(CARDS, 1):
        P += card(i, c['src'], c['title'], c['body'], c['opts'], c['steps'], c['rows'],
                  c['qas'], c['cue'], first=(i == 1),
                  col_frac=c.get('col_frac'), why_pct=c.get('why_pct', 0.34))
    P += [x.replace('w:line="360" w:lineRule="auto" w:after="80"',
                    'w:line="276" w:lineRule="auto" w:after="40"') for x in teacher_notes(
        'D6 明確教學三階段（I do – We do – You do＋放聲思考）',
        ('D2 手順卡',),
        reason=('口試要求學生「講出解題推理」，正是 D6 放聲思考的引號句；'
                'D2 把每題拆成「說考點 → 拆題 → 講計算 → 講答案」四個固定動作，'
                '讓學生每題用同一個框架開口，減輕臨場組織語言的負荷。'),
        density='抽離小班（高三甲融合生 2 人）',
        fading=('第 1 堂：照讀講稿（對稿）→ 第 2 堂：遮住講稿，只看算式講'
                '（算式欄即 D2 的「只含關鍵詞清單」）→ 第 3 堂：只看題目講，再模擬抽籤口試 → '
                '正式口試：不帶卡（脫稿）。'),
        flows=('F5 課前流程預告（每堂開始先講今天練哪幾張卡）',
               'F4 過程導向回饋（針對手順 ①–④ 哪一步卡住）'),
        extra=(
            ('保底題組', '2020 年 Q1、Q5、Q11、Q13；2021 年 Q1、Q3、Q5、Q12，共 8 題（30 題的 27%）。'
                        '選題依據：甲班 IEP 高頻單元（基本概念、二次方程及二次函數、數列）'
                        '＋第一學段抽離課已複習單元＋入門難度。'),
            ('與科任商量', '評分規則不變，只請科任在抽籤時讓兩位融合生從保底題組中抽題。'
                          '依據：2026-07-18 調適申請已列「題目調適：把最複雜的題型改為基礎題型」，'
                          '內容調適上限為原卷 40%。'),
            ('評分目標', '以「脫稿＋只向老師講解」（最高 65%–75%）為基本目標；'
                        '第 3 堂模擬口試表現穩定者，可鼓勵挑戰「脫稿＋向全班講解」（最高 80%）。'),
            ('三堂建議分配', '第 1 堂：卡 1–4（教師示範 1 張，其餘學生照讀）；'
                            '第 2 堂：卡 5–8＋遮稿練習卡 1–4；'
                            '第 3 堂：抽籤模擬口試，教師可追問「為什麼這樣做」，按手順 ①–④ 給回饋。'),
            ('其餘 22 題', '書面解答過程（佔 20%）仍需交齊 30 題；本卡不涵蓋，可用 '
                          'worksheet-tools 教師版詳解核對。'),
        ),
    )]
    out = os.path.join(OUT, BASE + '.docx')
    build_docx([tighten(x) for x in P], out, footer_text=FOOT)
    print('OK', out)


if __name__ == '__main__':
    build()
