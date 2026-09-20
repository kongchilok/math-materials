# -*- coding: utf-8 -*-
"""
build_quiz_w04.py — 初三抽離小班 額外評核 W04（單元 01 一元二次方程・三種解法鞏固）

規格來源：工作筆記「📋 需求確認 → 🟢 現行規格卡」（2026-09-01 經 RDQ 訪談確認），
與 `build_quiz_w05.py` 同一份規格：
- 每週 1 次、抽離課堂課內、限時 5 分鐘、5 題、每題 20%（單次滿分 5 分）
- 題型：3 題基礎概念 ＋ 2 題常見錯誤糾正
- 命題範圍＝上週已教完（隔一週鞏固）；進度基準＝丙班；兩班共用同一份卷
- 產出：學生卷（含改正欄）＋ 教師答案卷，各 docx＋PDF

本卷週次：W04＝2026/09/21–09/25（依 `抽離教學_數學\\校曆_26-27_上課日曆.md`）。
命題範圍＝W03（09/14–09/18）已教完的內容：
  丙班 09/15 公式法（一）、09/16 公式法（二）、09/18 因式分解法（二）＋常見錯誤辨析
  乙班 09/14 公式法（一）、09/16 公式法（二）、09/17 因式分解法（一）
再補回 W05 卷教師頁自行標明「未覆蓋、留待下次」的配方法與十字交乘型因式分解。

house-style 偏離說明（沿用 W05 卷，不另立新規）：
1. masthead 類型寫「額外評核」（不是 skill 預設的「課後練習」）——檔案室分類需要區分。
2. 不用 ★ 三層難度標籤：5 題全班同卷、每題等分，沒有分層概念。
3. 每題框內多一條「改正：」欄——計分規則含「改正後」，訂正必須留在同一張紙上。
"""
import sys, os

SKILL = r"C:\Users\KongChiLok\.claude\skills\similar-practice-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *  # noqa
from omml_docx import _run  # star-import 跳過底線開頭的名稱

OUT = os.path.dirname(os.path.abspath(__file__))
SUBJECT = '初三數學'
UNIT = 'W04・一元二次方程・三種解法鞏固'
FOOTER = '初三數學．額外評核 W04'
BASE = '額外評核_初三數學_W04_一元二次方程三種解法鞏固'


def ruled(label='', sz=22, row_sz=26, alt=False):
    """一條書寫線，標籤直接寫在線上（不另起一段）。理由見 build_quiz_w05.py 同名函式。

    `alt`：相鄰兩段若框線設定完全相同，Word 會把它們合併成一條可見線
    （記憶 `docx_adjacent_border_paras_merge`——W05 卷第 3–5 題的第二條作答線
    就是這樣不見了）。因此第二條起交替 w:space 並加 1 twip 右縮排破解。"""
    space, ind = ('3', '<w:ind w:right="1"/>') if alt else ('4', '')
    ppr = ('<w:pPr><w:spacing w:line="300" w:lineRule="auto" w:before="20" w:after="0"/>'
           f'{ind}'
           f'<w:pBdr><w:bottom w:val="single" w:sz="5" w:space="{space}" w:color="{LINE_GREY}"/>'
           f'<w:between w:val="single" w:sz="5" w:space="0" w:color="{LINE_GREY}"/>'
           '</w:pBdr></w:pPr>')
    run = _run(label + ' ', sz=sz) if label else ''
    pad = (f'<w:r><w:rPr><w:sz w:val="{row_sz}"/><w:szCs w:val="{row_sz}"/></w:rPr>'
           '<w:t xml:space="preserve"> </w:t></w:r>')
    return f'<w:p>{ppr}{run}{pad}</w:p>'


def lines(*labels):
    """一組書寫線，逐條交替 alt 以免被 Word 合併。空字串＝無標籤的續行。
    「改正：」欄是計分規則的一部分（含改正後），訂正必須留在同一張紙上。"""
    return [ruled(lb, alt=(i % 2 == 1)) for i, lb in enumerate(labels)]


def qbox(paragraphs, last=False):
    """小測專用題目框：收窄框內上下內邊距並改用矮身分隔段，令學生卷收在 1 頁。
    理由見 build_quiz_w05.py 同名函式（記憶 `table_doc_page_saving_order`）。"""
    # 2026-09-20 同 quiz_common.qbox() 對齊：拿掉題目段落嘅段後 8pt。
    # 行距 w:line="360"（1.5 倍，house-style 硬規定、讀寫障礙友善）唔郁。
    paragraphs = [p if 'w:pBdr' in p else
                  p.replace('<w:spacing w:line="360" w:lineRule="auto" w:after="80"/>',
                            '<w:spacing w:line="360" w:lineRule="auto" w:after="0"/>')
                  for p in paragraphs]
    tbl = problem_box(paragraphs, trailing_blank=False)
    tbl = tbl.replace('<w:top w:w="80" w:type="dxa"/>', '<w:top w:w="20" w:type="dxa"/>')
    tbl = tbl.replace('<w:bottom w:w="80" w:type="dxa"/>', '<w:bottom w:w="20" w:type="dxa"/>')
    if last:
        return tbl
    return tbl + ('<w:p><w:pPr><w:spacing w:line="60" w:lineRule="auto" '
                  'w:before="0" w:after="0"/></w:pPr>'
                  '<w:r><w:rPr><w:sz w:val="4"/><w:szCs w:val="4"/></w:rPr>'
                  '<w:t xml:space="preserve"> </w:t></w:r></w:p>')


# ============================ 學生卷 ============================
S = []
S.append(masthead(SUBJECT, UNIT, '額外評核'))
S.append(student_info_row())
S.append(para([('t', '限時 5 分鐘　　共 5 題　　每題 1 分（20%）　　滿分 5 分'
                     '　　　　得分：＿＿＿ / 5')], bold=True, sz=22))

# 第 1 題 — 基礎概念：配方法的關鍵一步
S.append(qbox([
    para('1．用配方法解 {x^2−8x+3=0}，移項後等號兩邊應同時加上（　　）'),
    para([('t', 'A．4　　　B．8　　　C．16　　　D．64')], ind=300),
] + lines('作答：', '改正：')))

# 第 2 題 — 基礎概念：公式法
S.append(qbox([
    para('2．用公式法解方程 {2x^2−5x+2=0}，它的解是（　　）'),
    para('A．{x_1=2} 或 {x_2=1/2}　　　B．{x_1=4} 或 {x_2=1}', ind=300),
    para('C．{x_1=7/2} 或 {x_2=−1}　　　D．無實數根', ind=300),
] + lines('作答：', '改正：')))

# 第 3 題 — 基礎概念：因式分解法（十字交乘型）
S.append(qbox([
    para('3．用因式分解法解方程 {x^2−5x+6=0}。'),
] + lines('作答：', '', '改正：')))

# 第 4 題 — 常見錯誤糾正：判別式代入時漏了 c 的負號
S.append(qbox([
    para('4．小強解 {x^2−3x−4=0}：{Δ=(−3)^2−4(1)(−4)=9−16=−7}，∴ 無實數根。'
         '他錯在哪？正確答案？'),
] + lines('作答：', '', '改正：')))

# 第 5 題 — 常見錯誤糾正：右邊不是 0 就拆因式
S.append(qbox([
    para('5．小玲解 {(x−1)(x+2)=4}：{x−1=4} 或 {x+2=4}，得 {x=5} 或 {x=2}。'
         '她錯在哪？寫出正確的解。'),
] + lines('作答：', '', '改正：'), last=True))

build_docx(S, os.path.join(OUT, f'{BASE}_學生卷.docx'), footer_text=FOOTER)


# ============================ 教師卷 ============================
T = []
T.append(masthead(SUBJECT, UNIT, '額外評核・教師卷'))
T.append(para([('t', '本頁供教師批改與訂正指導使用，不發給學生。')], sz=22))
T.append(para([('t', '實施提示：學生卷版面已滿，訂正規則請口頭交代——'
                     '答錯的題目在該題「改正：」一欄訂正，訂正正確計入累積正確率。')], sz=22))

T.append(heading('一、參考答案'))
T.append(problem_box([
    para('1．C（16）'),
    para('　移項：{x^2−8x=−3}；一次項係數 −8 的一半是 −4，再平方得 {(−4)^2=16}。'),
    para('　配方後：{(x−4)^2=13}。'),
    para('　誘答 A：只取了「一半」{(−8)÷2=−4} 的數值 4，忘記再平方。'),
    para('　誘答 D：把一次項係數直接平方 {(−8)^2=64}，漏了先除以 2。'),
]))
T.append(problem_box([
    para('2．A（{x_1=2} 或 {x_2=1/2}）'),
    para('　a＝2、b＝−5、c＝2；{Δ=(−5)^2−4(2)(2)=25−16=9}。'),
    para('　代入求根公式：{x=(5+3)/4=2} 或 {x=(5−3)/4=1/2}。'),
    para('　誘答 B：分母寫成 2 而不是 2a＝4，得 4 或 1（最常見）。'),
    para('　誘答 C：忘記把 Δ 開平方，直接用 9 代入，得 7/2 或 −1。'),
]))
T.append(problem_box([
    para('3．{x_1=2} 或 {x_2=3}'),
    para('　兩數之積 6、兩數之和 −5 → −2 與 −3：{(x−2)(x−3)=0}'),
    para('　{x−2=0} 或 {x−3=0}'),
    para('　∴ {x_1=2} 或 {x_2=3}'),
    para('　評分：只寫出分解式未寫出兩個根，不給分（本卷考完整解題）。'),
]))
T.append(problem_box([
    para('4．錯在「{−4ac} 的符號」這一步。'),
    para('　這裡 c＝−4，{−4(1)(−4)=+16}，負負得正，小強當成了 −16。'),
    para('　正確：{Δ=(−3)^2−4(1)(−4)=9+16=25}，{Δ>0}，有兩個不相等的實數根。'),
    para('　{x=(3+5)/2=4} 或 {x=(3−5)/2=−1}'),
    para('　∴ {x_1=4} 或 {x_2=−1}'),
]))
T.append(problem_box([
    para('5．小玲錯在「右邊不是 0 就拆開因式」。'),
    para('　「其中一個因式＝0」這條規則，只在右邊是 0 的時候才成立；'
         '右邊是 4 時，兩個因式可以是 1 與 4、2 與 2、−1 與 −4……，不能逐個等於 4。'),
    para('　正確做法：先展開，移項令右邊為 0。'),
    para('　{(x−1)(x+2)=4}'),
    para('　{x^2+x−2=4}'),
    para('　{x^2+x−6=0}'),
    para('　{(x+3)(x−2)=0}'),
    para('　{x+3=0} 或 {x−2=0}'),
    para('　∴ {x_1=−3} 或 {x_2=2}'),
]))

T.append(heading('二、計分與結算'))
T.append(para([('t', '單次：每題 20%，答對 1 題得 1 分，單次滿分 5 分。')], sz=22))
T.append(para([('t',
    '學段末：以每名學生本學段全部小測的累積正確率（包含改正後答對的題目）'
    '乘以 20，折算為平時平均分之加分，上限 20 分。')], sz=22))
T.append(para([('t', '例：全學段共 60 題，累積答對（含改正後）51 題 → '
                     '正確率 85% → 加分 ＝ 0.85 × 20 ＝ 17 分。')], sz=22))

T.append(heading('三、命題說明'))
T.append(para([('t',
    '第 1–3 題為基礎概念題，分別考配方法的關鍵一步、公式法的完整代入、'
    '因式分解法（十字交乘型）——正是上一份卷（W05）教師頁標明「未覆蓋、'
    '留待下次」的配方法與十字交乘型。')], sz=22))
T.append(para([('t',
    '第 4 題錯誤原型：判別式代入時漏了 c 的負號（−4ac 一項中 c＜0）。'
    '第 5 題錯誤原型：右邊不是 0 就拆因式——即丙班 09/18、乙班 09/21 課堂'
    '「覆核移項使右邊為 0 這一步不可漏」的指定易錯點。')], sz=22))
T.append(para([('t',
    '※ 進度基準為丙班（09/18 已上完「方法四（二）應用練習＋常見錯誤辨析」）。'
    '乙班同一節排在 09/21（週一），故本卷宜安排在 09/21 之後實施，兩班無落差。')], sz=22))
T.append(para([('t',
    '※ 本次未覆蓋「四種方法怎麼選」（丙班 09/22–09/23、乙班 09/23 才上）'
    '與單元 02 判別式分類，留待下一份卷。')], sz=22))

build_docx(T, os.path.join(OUT, f'{BASE}_教師卷.docx'), footer_text=FOOTER)

print('OK')
