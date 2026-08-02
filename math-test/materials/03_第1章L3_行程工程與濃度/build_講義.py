# -*- coding: utf-8 -*-
"""
第1章 特殊數學應用專題．L3 行程、工程效率與濃度 —— 課堂講義 build script
主設計 D4 三欄式引導工作紙；輔助 D1 條形／線段圖（只用於行程的相遇追及與濃度的加水）、
D8 關鍵字對譯表（一般對譯＋陷阱詞）。鷹架密度：抽離小班 (Tier 2)。
產出：講義_行程工程與濃度_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403
import design_svg as ds                      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.path.join(HERE, "figs")
os.makedirs(FIGS, exist_ok=True)
BASE = "講義_行程工程與濃度_抽離小班共用版"
UNIT = "第1章 特殊數學應用專題．L3 行程、工程效率與濃度"
FOOT = "高三數學．第1章 特殊數學應用專題．L3 行程、工程效率與濃度"

# ---------------------------------------------------------------- 圖形（D1）
# 範例A：相遇——一整條是全程，兩段各是一輛車走的路程，兩段合起來剛好等於全程
BARS_A = [
    {"label": "全程", "cells": [("客車走的（80×2）", 80), ("貨車走的（100×2）", 100)],
     "brace": "360 公里"},
]
SVG_A = ds.bar_model(BARS_A, width=580, label_w=84,
                     title="一整條 ＝ 甲乙兩地全程；相遇時，兩段合起來剛好是全程")
PNG_A = os.path.join(FIGS, "ex_a_bar.png")
ds.svg_to_png(SVG_A, PNG_A)
ds.save_svg(SVG_A, os.path.join(FIGS, "ex_a_bar.svg"))

# 範例C：加水稀釋——三條並排，鹽那一段寬度完全一樣（＝溶質不變），只有水那一段變長
BARS_C = [
    {"label": "原來", "cells": [("鹽 30 克", 30), ("水 170 克", 170)], "brace": "200 克"},
    {"label": "加 50 克水", "cells": [("鹽 30 克", 30), ("水 220 克", 220)], "brace": "250 克"},
    {"label": "加 100 克水", "cells": [("鹽 30 克", 30), ("水 270 克", 270)], "brace": "300 克"},
]
SVG_C = ds.bar_model(BARS_C, width=580, label_w=84,
                     title="三條的「鹽」那一段一樣長——加水只令整條變長，鹽沒有變")
PNG_C = os.path.join(FIGS, "ex_c_bar.png")
ds.svg_to_png(SVG_C, PNG_C)
ds.save_svg(SVG_C, os.path.join(FIGS, "ex_c_bar.svg"))

# ---------------------------------------------------------------- 文字內容
INTRO = [
    "這一課有三種題目：行程（追車、相遇、追及）、工程效率（幾多日做完）、濃度"
    "（鹽水加水、兩種溶液混合）。三種題目的情境完全不同，但骨架是同一條——"
    "都是「率 × 量 ＝ 總量」。",
    "行程題的率是速度，工程題的率是工作效率，濃度題的率是濃度。認出這一點之後，"
    "三種題目就不必分開背三套方法，只要每次問自己同樣的兩句話："
    "「這一題的三個量是哪三個？」「這一題由頭到尾，哪一個量沒有變？」",
    "第二句是本課的關鍵。列方程需要一條等式，那條等式就是從「不變的那個量」寫出來的："
    "相遇題不變的是兩段路程的和，追及題不變的是兩段路程的差，工程題不變的是整項工程"
    "（當作 1），濃度題不變的是溶質（鹽、糖）的質量。",
    "所以這一課的做法，是把每一題都填進一張三欄表：第①欄只做讀題（把已知抄出來、"
    "把不變量寫出來），第②欄只做列式（不計算），第③欄才動手算並反過來檢核。"
    "讀題、列式、計算三件事分開做，就不會一邊讀題一邊算而漏掉條件。",
]

# 三種題型的三量對照（本課的骨架表）
FRAME_PAIRS = [
    ("行程題\n（相遇、追及、分段行駛）",
     "路程 ＝ 速度 × 時間\n"
     "不變量：相遇 → 兩段路程的和 ＝ 全程；追及 → 兩段路程的差 ＝ 一開始的領先距離"),
    ("工程效率題\n（單獨做、合做、接力做）",
     "工作量 ＝ 工作效率 × 日數\n"
     "不變量：整項工程 ＝ 1；單獨 n 天做完，效率就是 {frac(1,n)}"),
    ("濃度題\n（加水、蒸發、混合）",
     "溶質 ＝ 溶液 × 濃度\n"
     "不變量：加水或蒸發時，溶質（鹽／糖）的質量不變；混合時，混合後的溶質 ＝ 兩邊溶質相加"),
]

# D8 關鍵字對譯（一般對譯／陷阱詞分開列）
KW_GENERAL = [
    ("速度 × 時間", "＝ 路程。三個量知其中兩個，第三個就求得出"),
    ("工作效率 × 日數", "＝ 工作量。整項工程當作 1"),
    ("濃度 × 溶液質量", "＝ 溶質質量（鹽或糖本身的質量）"),
    ("「同時出發、相向而行」", "兩者一起縮短中間的距離 → 速度相加"),
    ("「同向而行，去追前面的」", "後者一點一點吃掉領先距離 → 速度相減"),
    ("「單獨做要 n 天完成」", "效率 ＝ {frac(1,n)}，即每日完成整項工程的 {frac(1,n)}"),
    ("「加入清水」", "溶質不變、溶液變多 → 濃度下降"),
    ("「蒸發掉水分」", "溶質不變、溶液變少 → 濃度上升"),
]

KW_TRAPS = [
    ("「相遇」", "是兩段路程的「和」等於全程，速度要相加；不要寫成相減"),
    ("「追上」", "是兩段路程的「差」等於領先距離，速度要相減；不要寫成相加"),
    ("「甲先走 5 分鐘」", "先算出他領先了多少距離（速度 × 5），不是把 5 分鐘從時間裡減掉"),
    ("「兩隊合做」", "把兩個「效率」相加；不可以把兩個「日數」相加，也不可以取平均"),
    ("「甲 20 天、乙 30 天，合做要幾天」",
     "答案一定比 20 更小（合做一定比任何一人單獨做快）；答 25 天必錯"),
    ("「濃度 15% 的鹽水 200 克」", "200 克是鹽水（溶液）的質量，不是鹽的質量；鹽 ＝ 200 × 15%"),
    ("「加水稀釋」", "分母（溶液）變大、分子（溶質）不變；不可以把兩個濃度相加"),
    ("「兩種鹽水混合」", "混合後的溶質 ＝ 兩邊溶質相加；濃度不是兩個濃度的平均"),
]

# ---------------------------------------------------------------- 三個範例
EXAMPLE_A = ("【範例A・行程】甲、乙兩地相距 360 公里。一輛客車由甲地開出，時速 80 公里；"
             "同時一輛貨車由乙地開出，時速 100 公里，兩車相向而行。"
             "問（a）幾小時後兩車相遇？（b）相遇處距甲地多少公里？")

COL_A = (
    ["已知：兩地相距 360 公里（全程）。",
     "已知：客車 80 公里／小時，貨車 100 公里／小時。",
     "已知：同時出發、相向而行。",
     "所求：（a）相遇需時（b）相遇處距甲地的路程。",
     "※ 這一題不變的是：兩車走的路程「和」＝ 全程 360 公里。"],
    ["三量關係：路程 ＝ 速度 × 時間。",
     "相向而行，兩車一起縮短中間的距離，速度可以合併：",
     "合速度 ＝ {80+100=180}（公里／小時）。",
     "設相遇需時 {t} 小時：",
     "{80t+100t=360}，即 {180t=360}。",
     "（b）相遇處距甲地 ＝ 客車走的路程 ＝ {80t}。"],
    ["（a）{t=360/180=2}（小時）。",
     "（b）距甲地 ＝ {80*2=160}（公里）。",
     "檢核：貨車走了 {100*2=200} 公里；",
     "{160+200=360}，與全程相符。",
     "合理性：客車較慢，走得較少（160 小於 200），"
     "相遇點應該較接近甲地——與答案相符。"],
)

EXAMPLE_B = ("【範例B・工程效率】一項工程，甲隊單獨做 20 天完成，乙隊單獨做 30 天完成。"
             "甲隊先單獨做 5 天，之後兩隊一起做。問還要多少天才能完成？")

COL_B = (
    ["已知：甲隊單獨 20 天完成整項工程。",
     "已知：乙隊單獨 30 天完成整項工程。",
     "已知：甲先做 5 天，之後兩隊合做。",
     "所求：合做還需要的日數。",
     "※ 題目由頭到尾沒有講工程有多少立方米、多少件——"
     "工程量沒有數值，這一類題把整項工程當作 1。",
     "※ 這一題不變的是：整項工程 ＝ 1。"],
    ["三量關係：工作量 ＝ 工作效率 × 日數。",
     "甲的效率 ＝ {frac(1,20)}",
     "乙的效率 ＝ {frac(1,30)}",
     "甲先做 5 天：{5*frac(1,20)=frac(1,4)}",
     "餘下：{1-frac(1,4)=frac(3,4)}",
     "合做效率 ＝ {frac(1,20)+frac(1,30)}",
     "　　　　＝ {frac(3,60)+frac(2,60)=frac(1,12)}",
     "設還要 {t} 天：{frac(1,12)*t=frac(3,4)}"],
    ["{t=frac(3,4)/frac(1,12)}",
     "　＝ {frac(3,4)*12=9}（天）。",
     "檢核：這 9 天甲做了 {frac(9,20)}，",
     "乙做了 {frac(9,30)=frac(3,10)}。",
     "甲一共做了 {frac(5,20)+frac(9,20)=frac(7,10)}，",
     "而 {frac(7,10)+frac(3,10)=1}，剛好做完。",
     "合理性：若一開始就合做只需 12 天；本題甲自己先做了 5 天，"
     "總日數 {5+9=14} 天，比 12 天多——合理。"],
)

EXAMPLE_C = ("【範例C・濃度】有 200 克濃度 15% 的鹽水。"
             "問（a）加入 50 克清水之後，鹽水的濃度變成多少？"
             "（b）若要把原來那 200 克鹽水的濃度降到 10%，應加入多少克清水？")

COL_C = (
    ["已知：鹽水 200 克，濃度 15%。",
     "已知：（a）加入 50 克清水（b）目標濃度 10%。",
     "所求：（a）新的濃度（b）要加入的清水質量。",
     "※ 加入的是清水——沒有加鹽，也沒有拿走鹽。",
     "※ 這一題不變的是：鹽（溶質）的質量。"],
    ["三量關係：溶質 ＝ 溶液 × 濃度。",
     "鹽的質量 ＝ {200*0.15=30}（克）。這 30 克在（a）（b）兩問都不變。",
     "（a）新溶液 ＝ {200+50=250}（克）；",
     "　　新濃度 ＝ {frac(30,250)}。",
     "（b）設加入 {w} 克清水，新溶液 ＝ {200+w}（克）：",
     "　　{frac(30,200+w)=0.1}。"],
    ["（a）{frac(30,250)=0.12}，即 12%。",
     "（b）30 ÷ 0.1 ＝ 300，即 {200+w=300}，",
     "　　所以 {w=100}（克）。",
     "檢核（a）：{250*0.12=30} 克鹽，與原來一樣。",
     "檢核（b）：{300*0.1=30} 克鹽，與原來一樣。",
     "合理性：加水只會令濃度下降，15% → 12% → 10%，"
     "加得越多降得越多——與答案相符。"],
)

ACTIONS = [
    "動作 1　認出題型，先寫下三個量。行程題 → 路程／速度／時間；"
    "工程題 → 工作量／工作效率／日數；濃度題 → 溶質／溶液／濃度。"
    "三個位置先寫出來，再把題目給的數填進去，就看得出缺哪一個。",
    "動作 2　找出不變量，寫在第①欄最後一行的 ※ 後面。"
    "相遇 → 路程的和；追及 → 路程的差；工程 → 整項工程 ＝ 1；濃度 → 溶質的質量。"
    "不變量就是等號的其中一邊。",
    "動作 3　在第②欄列式，不要計算。用「率 × 量 ＝ 總量」把每一段寫出來，"
    "再用不變量把它們接成一條等式。這一欄只寫式，不寫答案。",
    "動作 4　在第③欄算，算完反推檢核。把答案代回去，重新算一次那個不變量，"
    "看看是否等於題目給的數；再看一次答案大小合不合常理。",
]

TN = dict(
    main_design="D4 三欄式引導工作紙——三欄固定為 ① 語意擷取 ② 關係式建構 ③ 運算與檢核",
    aux_designs=("D1 條形／線段圖（只用於行程的相遇與濃度的加水稀釋兩處）",
                 "D8 關鍵字對譯表（一般對譯＋陷阱詞分開列）"),
    reason=(
        "本課題源自題庫 A1 應用題文字題中的行程、工程效率與濃度類（約 29 題），"
        "與 L1、L2 同屬 teaching-designs.md 的 S1 文字應用題結構。"
        "但本課的認知瓶頸與前兩課不同：L1 卡在「讀不出比例關係」，L2 卡在「哪一個量是 100%」，"
        "本課卡在「三種情境要各自認出自己的三量關係，並先判斷哪一個量不變才列得出等式」。"
        "由於困難在「讀題→列式」這一段的程序本身，而不是缺一張圖，故主設計改用 S1 的備選 "
        "D4 三欄式引導，把讀題、列式、計算三種互相干擾的認知活動在版面上物理分開；"
        "同時這也是 L2 教師說明頁已寫明的 D1 褪除時程——D1 由主設計降為輔助，"
        "只保留在真正需要圖的兩處（相遇的路程和、加水稀釋時鹽段不變）。"
        "D8 沿用但改為完整重印一般對譯＋陷阱詞：本課一次過引入三種新情境，"
        "術語量比前兩課大（相遇／追及／效率／溶質／稀釋），需要重新給一次對譯表。"),
    density="抽離小班（Tier 2）",
    fading=(
        "三欄式（D4）：本課講義三個範例都是填好的三欄表 → 練習A 第①②欄已填一半、"
        "第③欄全空 → 練習B 三欄全空但欄位還在 → 練習C 只給題目，欄位由學生自己畫 → "
        "L4 起不再印欄位，只在題目旁留一句「先做第①欄」→ 之後完全移除。｜"
        "條形／線段圖（D1）：L1 給半成品圖、L2 給空白格線，本課起不再給任何圖框，"
        "只在行程與濃度題保留一句「請先在空白處畫線段圖」 → L4 移除該句。｜"
        "關鍵字對譯（D8）：本課講義給完整對譯表＋陷阱詞，並印成工具卡讓學生放桌面 → "
        "練習A 的第①欄已把關鍵字抄進表格 → 練習B 由學生自己抄進第①欄 → 練習C 不提示 → "
        "L4 起只保留陷阱詞卡，一般對譯不再印。"),
    flows=("F5 課前流程預告（今天四件事：三量骨架 → 範例A 行程 → 範例B 工程 → 範例C 濃度）",
           "F4 過程導向回饋與分步計分（第①欄的不變量判斷單獨給分；"
           "不變量判斷正確而後續算術筆誤者，不重複扣分——對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點", "a5 放大字體", "a6 增加行距",
               "a7 調整計分標準（三欄各自給分，不以最後答案一刀切）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，只調整呈現方式與鷹架密度，未刪減內容。"),
           ("與 L1、L2 的銜接",
            "本課假設學生已完成《L1 比例與分配》與《L2 利潤、折扣與費率階梯》，"
            "已有「先畫圖／先定基準再列式」的習慣。本課把那個習慣制度化成三欄表。"
            "若學生未上過前兩課，可先用範例A 帶一次三欄表的填法再進入其餘兩個範例。"),
           ("為何不另加自我核對清單（D12）",
            "本課的核對動作已經內建在三欄式的第③欄「運算與檢核」，"
            "另外再加 D12 會令學生同時操作的外部工具超過「主 1＋輔 2」的上限，"
            "鷹架本身反而變成新的認知負荷。核對要求改為寫進第③欄的填寫規定。"),
           ("配套文件",
            "《第1章 L3 行程、工程效率與濃度　課堂練習》（練習A／B／C ＋參考答案）、"
            "《第1章 L3 行程、工程效率與濃度　工具卡》"
            "（三量關係卡、不變量卡、陷阱詞卡、解題四動作卡，學生剪下護貝放桌面）。")),
)


# ---------------------------------------------------------------- docx
def _mp(lines):
    return [para(t) for t in lines]


def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、三種題型，同一條骨架"))
    P.append(para("下表左欄是題型，右欄是那一種題的三量關係與不變量。"
                  "讀題之後第一件事，就是對照這張表認出自己在做哪一種。"))
    P.append(dual_track_table([(_mp(a.split("\n")), _mp(b.split("\n")))
                               for a, b in FRAME_PAIRS],
                              headers=("這一課的三種題型", "三量關係 → 這一題的不變量")))

    P.append(heading("三、關鍵字對譯"))
    P.append(para("上半部是可以照字面翻成算式的說法；下半部的陷阱詞不可以照字面翻，"
                  "讀到時要在題目上劃雙底線，停一停再寫。"))
    P.append(keyword_table(KW_GENERAL, KW_TRAPS))

    P.append(heading("四、範例A・行程：兩段路程的和", page_break_before=True))
    P.append(problem_box([para(EXAMPLE_A)]))
    P.append(image_para(PNG_A, width_cm=13.5,
                        caption="相遇時，客車走的那一段加貨車走的那一段，剛好是全程"))
    P.append(three_column_table([(_mp(COL_A[0]), _mp(COL_A[1]), _mp(COL_A[2]))],
                                row_h=2600))
    P.append(shaded_box("※ 相遇題把兩輛車的速度加起來，是因為它們一起在縮短中間那段距離。"
                        "追及題剛好相反：兩者同向，後面的每分鐘只吃掉「速度差」那麼多，所以速度要相減。"))

    P.append(heading("五、範例B・工程效率：整項工程當作 1", page_break_before=True))
    P.append(problem_box([para(EXAMPLE_B)]))
    P.append(three_column_table([(_mp(COL_B[0]), _mp(COL_B[1]), _mp(COL_B[2]))],
                                row_h=2900))
    P.append(shaded_box("※ 工程題不給工程量的數值，是故意的——因為答案與工程有多大無關。"
                        "把整項工程當作 1，「單獨 n 天完成」就是每日完成 {frac(1,n)}，"
                        "合做就把幾個 {frac(1,n)} 加起來。"))

    P.append(heading("六、範例C・濃度：鹽的質量不會變", page_break_before=True))
    P.append(problem_box([para(EXAMPLE_C)]))
    P.append(image_para(PNG_C, width_cm=13.5,
                        caption="三條的鹽段一樣長：加水只令整條變長，鹽的質量始終是 30 克"))
    P.append(three_column_table([(_mp(COL_C[0]), _mp(COL_C[1]), _mp(COL_C[2]))],
                                row_h=2600))
    P.append(shaded_box("※ 濃度題最常見的錯，是把題目給的溶液質量當成溶質質量。"
                        "看到「濃度 15% 的鹽水 200 克」，先寫一句「鹽 ＝ 200 × 15% ＝ 30 克」，"
                        "之後整題都用這個 30 克。"))

    P.append(heading("七、自己動手時的四個動作", page_break_before=True))
    for t in ACTIONS:
        P.append(shaded_box(t))

    P.append(heading("八、接下來"))
    P.append(para("請拿出《第1章 L3 行程、工程效率與濃度　課堂練習》，"
                  "依照上面四個動作完成練習A、練習B、練習C。"
                  "練習A 的三欄表第①②欄已經填了一半，補完之後在第③欄計算；"
                  "練習B 的三欄全空，欄位還在；"
                  "練習C 連欄位都沒有，請自己在作答空間畫出三欄再填。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ---------------------------------------------------------------- HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


def _tex(m):
    import re
    m = m.strip()
    body = m
    # frac(a,b) → \frac{a}{b}（可巢狀出現多次）
    for _ in range(6):
        new = re.sub(r"frac\(([^(),]+),([^(),]+)\)", r"\\frac{\1}{\2}", body)
        if new == body:
            break
        body = new
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    # 分子分母都要吃小數點——寫成 (\d+)/(\d+) 會把 30/0.1 讀成 30/0 再多出一個 .1，
    # 與 omml_core 的 _NUM_RE（本來就吃小數）不一致，docx 對而 HTML 錯（2026-07-27 實錄）。
    body = re.sub(r"(?<![\\{\w.])(\d+(?:\.\d+)?)/(\d+(?:\.\d+)?)(?![}\w.])",
                  r"\\frac{\1}{\2}", body)
    body = body.replace("%", r"\%")
    return r"\(%s\)" % body


def _h(s):
    import re
    out, i = [], 0
    for m in re.finditer(r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", s):
        out.append(_esc(s[i:m.start()]))
        out.append(_tex(m.group(1)))
        i = m.end()
    out.append(_esc(s[i:]))
    return "".join(out)


def _cell(lines):
    return "".join("<div>%s</div>" % _h(t) for t in lines)


def _svg_inline(svg):
    return svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', "")


def _three_col(cols):
    return ('<table class="d-tbl three-col">'
            '<tr><th>① 語意擷取（圈已知、劃所求）</th>'
            '<th>② 關係式建構</th><th>③ 運算與檢核</th></tr>'
            '<tr><td>%s</td><td>%s</td><td>%s</td></tr></table>'
            % (_cell(cols[0]), _cell(cols[1]), _cell(cols[2])))


def build_html_file():
    frame_rows = "".join(
        "<tr><td>%s</td><td>%s</td></tr>" % (_cell(a.split("\n")), _cell(b.split("\n")))
        for a, b in FRAME_PAIRS)

    kw_rows = ("".join("<tr><td>%s</td><td>%s</td></tr>" % (_h(k), _h(v))
                       for k, v in KW_GENERAL)
               + '<tr class="trap"><td colspan="2">⚠ 陷阱詞（不可以照字面翻成算式）</td></tr>'
               + "".join("<tr><td>%s</td><td>%s</td></tr>" % (_h(k), _h(v))
                         for k, v in KW_TRAPS))

    intro = "".join("<div>%s</div>" % _h(t) for t in INTRO)
    actions = "".join('<div class="hint-card">%s</div>' % _h(t) for t in ACTIONS)

    tn_rows = [("本份採用的主設計", TN["main_design"]),
               ("輔助設計", "、".join(TN["aux_designs"])),
               ("選用理由", TN["reason"]),
               ("鷹架密度", TN["density"]),
               ("褪除路徑", TN["fading"]),
               ("課堂實施流程", "、".join(TN["flows"])),
               ("對應官方輔助措施代碼", "、".join(TN["iep_codes"]))]
    tn_rows += list(TN["extra"])
    tn = "".join("<tr><td>%s</td><td>%s</td></tr>" % (_esc(k), _esc(v)) for k, v in tn_rows)

    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", "講義：" + UNIT)
    # 只補列印分頁規則（提示框／圖／表列不得被切開、區塊標題不得與內容拆散）；
    # 不動 @page 邊界與 .footer 的 position，QB-15c 的計數維持 1。
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
</style>
</head>""")

    body = """
<body>
<div class="page">

  <div class="masthead"><span>科目：高三數學</span><span>單元：%s</span><span>類型：課堂講義</span></div>

  <div class="ws-meta">姓名：<span class="u">&nbsp;</span>班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>日期：<span class="u">&nbsp;</span></div>

  <div class="section-h">一、這一課要做到的事</div>
  %s

  <div class="section-h">二、三種題型，同一條骨架</div>
  <div>下表左欄是題型，右欄是那一種題的三量關係與不變量。讀題之後第一件事，就是對照這張表認出自己在做哪一種。</div>
  <table class="d-tbl dual-track">
    <tr><th>這一課的三種題型</th><th>三量關係 → 這一題的不變量</th></tr>
    %s
  </table>

  <div class="section-h">三、關鍵字對譯</div>
  <div>上半部是可以照字面翻成算式的說法；下半部的<span class="kw-trap">陷阱詞</span>不可以照字面翻，讀到時要在題目上劃雙底線，停一停再寫。</div>
  <table class="d-tbl kw-table">
    <tr><th>題目說…</th><th>就寫成…</th></tr>
    %s
  </table>

  <div class="section-h page-break">四、範例A・行程：兩段路程的和</div>
  <div class="problem">%s</div>
  <div class="fig">%s
    <div class="cap">相遇時，客車走的那一段加貨車走的那一段，剛好是全程</div>
  </div>
  %s
  <div class="hint-card">※ 相遇題把兩輛車的速度加起來，是因為它們一起在縮短中間那段距離。追及題剛好相反：兩者同向，後面的每分鐘只吃掉「速度差」那麼多，所以速度要相減。</div>

  <div class="section-h page-break">五、範例B・工程效率：整項工程當作 1</div>
  <div class="problem">%s</div>
  %s
  <div class="hint-card">※ 工程題不給工程量的數值，是故意的——因為答案與工程有多大無關。把整項工程當作 1，「單獨 n 天完成」就是每日完成 %s，合做就把幾個 %s 加起來。</div>

  <div class="section-h page-break">六、範例C・濃度：鹽的質量不會變</div>
  <div class="problem">%s</div>
  <div class="fig">%s
    <div class="cap">三條的鹽段一樣長：加水只令整條變長，鹽的質量始終是 30 克</div>
  </div>
  %s
  <div class="hint-card">※ 濃度題最常見的錯，是把題目給的溶液質量當成溶質質量。看到「濃度 15%% 的鹽水 200 克」，先寫一句「鹽 ＝ 200 × 15%% ＝ 30 克」，之後整題都用這個 30 克。</div>

  <div class="section-h page-break">七、自己動手時的四個動作</div>
  %s

  <div class="section-h">八、接下來</div>
  <div>請拿出《第1章 L3 行程、工程效率與濃度　課堂練習》，依照上面四個動作完成練習A、練習B、練習C。練習A 的三欄表第①②欄已經填了一半，補完之後在第③欄計算；練習B 的三欄全空，欄位還在；練習C 連欄位都沒有，請自己在作答空間畫出三欄再填。</div>

  <div class="footer">%s</div>

  <div class="teacher-notes">
    <div class="section-h">教師實施說明（本頁供教師參考，列印給學生時可不印）</div>
    <table class="d-tbl">
      %s
    </table>
  </div>

</div>
</body>
</html>
""" % (_esc(UNIT), intro, frame_rows, kw_rows,
       _h(EXAMPLE_A), _svg_inline(SVG_A), _three_col(COL_A),
       _h(EXAMPLE_B), _three_col(COL_B), _h("{frac(1,n)}"), _h("{frac(1,n)}"),
       _h(EXAMPLE_C), _svg_inline(SVG_C), _three_col(COL_C),
       actions, _esc(FOOT), tn)

    path = os.path.join(HERE, BASE + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body)
    return path


if __name__ == "__main__":
    print(build_docx_file())
    print(build_html_file())
