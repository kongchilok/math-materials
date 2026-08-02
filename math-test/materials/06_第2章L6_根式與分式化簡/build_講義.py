# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L6 根式、分式的化簡與有理化 —— 課堂講義 build script
主設計 D2 手順卡（三張：根式化簡／分母有理化／分式化簡，每步附 ※ 易錯點）；
輔助 D9 草稿分區（四格作答區，取代書寫行）、D12 自我核對清單＋核對點。
鷹架密度：抽離小班 (Tier 2)。
產出：講義_根式與分式化簡_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_根式與分式化簡_抽離小班共用版"
UNIT = "第2章 中學基礎數學應用．L6 根式、分式的化簡與有理化"
FOOT = "高三數學．" + UNIT

# ================================================================ 文字內容
INTRO = [
    "上一課（L5）用一張四步卡處理對數。這一課同樣是多步驟的程序運算，"
    "但失分的原因不同：根式與分式的題目，多數人不是不會做，而是草稿寫得亂"
    "——係數與根號混在一起、通分時漏了一個負號、約分時把「項」當成「因式」約掉。",
    "所以本課除了手順卡之外，再加兩件事。第一，作答區不再是一行行的橫線，"
    "而是劃成四個格子，每一格只做一件事，寫在哪一格就代表你正在做哪一步。"
    "第二，每一個練習區塊做完之後有一張核對清單，四個項目全部是"
    "「看一眼就答得出」的問題，不是「我有沒有認真」這種無法自己判斷的問題。",
    "本課的內容分三種：把根號內的數化到最簡（根式化簡）、把分母的根號消走（有理化）、"
    "把幾個分式合併成一個（分式化簡）。三種各有一張手順卡，"
    "但它們共用同一個習慣——先看清楚結構，再動筆；每寫完一步，回頭看一眼上一步。",
    "特別提醒一件事：分式化簡到最後，一定要寫出「x 不可以等於甚麼」。"
    "化簡之後的式子看起來沒有問題，但原式的分母限制不會因為化簡而消失"
    "——這一點是本課最容易整份漏掉的分數。",
]

# ---------------------------------------------------------------- D2 三張手順卡
CARD1 = dict(
    title="手順卡一・根式化簡",
    trigger="題目出現根號，而根號內的數不是完全平方（例如 {sqrt(20)}、{sqrt(48)}）。",
    steps=[
        ("把根號內的數拆成「完全平方 × 剩餘」。",
         "完全平方是 4、9、16、25、36、49、64、81、100…。要拆到剩餘部分再沒有"
         "完全平方因數為止，例如 {sqrt(48)} 要拆成 {sqrt(16*3)}，不是 {sqrt(4*12)}。"),
        ("開方：完全平方那一部分開出來，搬到根號外面。",
         "{sqrt(4*5)=2sqrt(5)}，不是 {4sqrt(5)}——4 開方之後是 2。"
         "搬出來的數要與原本的係數相乘。"),
        ("合併同類根式（根號內完全相同的才可以加減）。",
         "{sqrt(5)} 與 {sqrt(10)} 不是同類，加不起來，答案就保留兩項。"
         "合併時只加係數，根號部分不變：{2sqrt(5)+3sqrt(5)=5sqrt(5)}。"),
    ],
    fading="完整三步卡 → 只留關鍵詞（拆、開、併）→ 只留「這題有三步」→ 完全移除。",
)

CARD2 = dict(
    title="手順卡二・分母有理化",
    trigger="分母出現根號（例如 {frac(1,sqrt(3))}、{frac(1,2+sqrt(3))}），"
            "或者題目直接問「有理化因式是甚麼」。",
    steps=[
        ("看分母是一項還是兩項：一項就乘那個根號本身；"
         "兩項（{a+sqrt(b)} 這種）就乘它的共軛。",
         "共軛只把中間那個符號調轉：{a+sqrt(b)} 的共軛是 {a-sqrt(b)}；"
         "前後兩項本身不動，也不要連正負號一起搬。"),
        ("分子分母同乘那一項，分母用平方差公式展開。",
         "{(a+sqrt(b))(a-sqrt(b))=a^2-b}。這一步之後分母一定是有理數；"
         "如果分母還有根號，就是共軛寫錯了，回上一步。"),
        ("約簡：分子分母有公因數才約。",
         "只約其中一項是最常見的錯，例如 {frac(2+2sqrt(3),2)} 要約成 {1+sqrt(3)}，"
         "不是 {2+sqrt(3)}——分子兩項都要除以 2。"),
    ],
    fading="完整三步卡 → 只留一句「分母有根號就乘共軛」→ 完全移除。",
)

CARD3 = dict(
    title="手順卡三・分式化簡",
    trigger="題目有兩個或以上的分式要相加減，或者分母是多項式（例如 {x^2-1}）。",
    steps=[
        ("先把每一個分母因式分解，找出公分母。",
         "{1-x} 與 {x-1} 不同號：{1-x=-(x-1)}。見到這一對一定要先統一，"
         "否則通分之後整項的正負號會反過來。"),
        ("每一項乘到同一個分母，分子跟著乘。",
         "分子是多項式時，先加括號再乘：{-x(x+1)} 要整個展開成 {-x^2-x}，"
         "漏了括號就只有第一項變號。"),
        ("分子合併同類項，再看分子分母有沒有公因式可以約。",
         "約分只可以約因式（整個括號），不可以約項。"
         "{frac(x+2,x+3)} 的 x 不能約掉，因為 x 是項不是因式。"),
        ("寫出使原式有意義的限制：原來每一個分母都不可以等於 0。",
         "化簡之後的式子看起來沒問題，但限制來自原式，不會因為化簡而消失。"
         "整份練習最常見的整題失分，就是漏了這一行。"),
    ],
    fading="完整四步卡 → 只留關鍵詞（分解、通分、合併約分、寫限制）→ "
           "只留「記得寫限制」→ 完全移除。",
)
CARDS_D2 = [CARD1, CARD2, CARD3]

# ---------------------------------------------------------------- D9 草稿分區
QUAD_LABELS = ("① 抄下原式，圈出要先處理的部分",
               "② 拆開／通分：寫出中間式",
               "③ 計算並合併同類項",
               "④ 檢查：根號內還有完全平方嗎？分母還有根號嗎？")

# ---------------------------------------------------------------- 範例
EX, SOL, NOTE = {}, {}, {}

EX["A"] = ("【範例A・根式化簡】一個三角形的三邊長分別是 {sqrt(20)} 厘米、"
           "{sqrt(40)} 厘米、{sqrt(45)} 厘米。求它的周長。")
SOL["A"] = [
    "第 1 步（拆）：{20=4*5}、{40=4*10}、{45=9*5}。"
    "三個都拆到剩餘部分再沒有完全平方因數。",
    "第 2 步（開）：{sqrt(20)=sqrt(4*5)=2sqrt(5)}；"
    "{sqrt(40)=sqrt(4*10)=2sqrt(10)}；{sqrt(45)=sqrt(9*5)=3sqrt(5)}。",
    "第 3 步（併）：周長 {=2sqrt(5)+2sqrt(10)+3sqrt(5)}。"
    "{sqrt(5)} 與 {sqrt(5)} 是同類，係數相加得 {5sqrt(5)}；"
    "{sqrt(10)} 沒有同類，保留。",
    "周長 {=5sqrt(5)+2sqrt(10)}（厘米）。",
    "檢核（取近似值）：{sqrt(20)≈4.472}、{sqrt(40)≈6.325}、{sqrt(45)≈6.708}，"
    "三者相加 {≈17.505}；而 {5sqrt(5)+2sqrt(10)≈11.180+6.325=17.505}——相符。",
]
NOTE["A"] = ("※ 答案有兩項是正常的。{sqrt(5)} 與 {sqrt(10)} 根號內不同，"
             "永遠加不成一項，硬要寫成 {7sqrt(15)} 之類是錯的。"
             "「不能再合併」本身就是最簡形式。")

EX["B"] = ("【範例B・有理化因式】（a）寫出 {10+sqrt(5)} 與 {3-sqrt(2)} 的有理化因式，"
           "並算出各自相乘之後的值。（b）化簡 {frac(1,2+sqrt(3))}。")
SOL["B"] = [
    "（a）第 1 步：兩個都是「兩項」的形式，取共軛——只調中間的符號。"
    "{10+sqrt(5)} 的有理化因式是 {10-sqrt(5)}；{3-sqrt(2)} 的是 {3+sqrt(2)}。",
    "（a）第 2 步（平方差）：{(10+sqrt(5))(10-sqrt(5))=100-5=95}；"
    "{(3-sqrt(2))(3+sqrt(2))=9-2=7}。兩個乘積都是有理數，正確。",
    "（b）第 1 步：分母 {2+sqrt(3)} 是兩項，共軛是 {2-sqrt(3)}。",
    "（b）第 2 步：分子分母同乘 {2-sqrt(3)}——"
    "分母 {=(2+sqrt(3))(2-sqrt(3))=4-3=1}；分子 {=1*(2-sqrt(3))=2-sqrt(3)}。",
    "（b）第 3 步（約簡）：分母是 1，不必再約，答案是 {2-sqrt(3)}。",
    "檢核（b）：{frac(1,2+sqrt(3))≈frac(1,3.732)≈0.268}；"
    "而 {2-sqrt(3)≈2-1.732=0.268}——相符。",
]
NOTE["B"] = ("※ 「有理化因式」問的只是那一個要乘上去的式子，不是問乘完之後的答案。"
             "題目問「有理化因式是甚麼」就答 {10-sqrt(5)}；"
             "題目問「化簡」才要把整個乘法做完。讀清楚問的是哪一個。")

EX["C"] = ("【範例C・根式運算】計算 {sqrt(9x)+6sqrt(frac(x,4))-2xsqrt(frac(1,x))}"
           "（其中 {x>0}）。")
SOL["C"] = [
    "逐項處理。第一項：{sqrt(9x)=sqrt(9)*sqrt(x)=3sqrt(x)}。",
    "第二項：{sqrt(frac(x,4))=frac(sqrt(x),sqrt(4))=frac(sqrt(x),2)}，"
    "所以 {6sqrt(frac(x,4))=6*frac(sqrt(x),2)=3sqrt(x)}。",
    "第三項：{sqrt(frac(1,x))=frac(1,sqrt(x))}，"
    "所以 {2xsqrt(frac(1,x))=frac(2x,sqrt(x))}。"
    "把 {x} 寫成 {sqrt(x)*sqrt(x)}，約去一個 {sqrt(x)}，得 {2sqrt(x)}。",
    "第 3 步（併）：三項的根號內都是 {x}，是同類根式，係數相加減："
    "{3sqrt(x)+3sqrt(x)-2sqrt(x)=4sqrt(x)}。",
    "檢核：取 {x=4}——原式 {=sqrt(36)+6sqrt(1)-8sqrt(frac(1,4))=6+6-4=8}；"
    "而 {4sqrt(4)=8}——相符。",
]
NOTE["C"] = ("※ 第三項的 {frac(2x,sqrt(x))} 是最多人卡住的地方。"
             "記住 {frac(x,sqrt(x))=sqrt(x)}——因為 {x=(sqrt(x))^2}，"
             "上下約去一個 {sqrt(x)} 就剩一個。用數字驗一次就記得住："
             "{frac(9,sqrt(9))=frac(9,3)=3=sqrt(9)}。")

EX["D"] = "【範例D・分式化簡】化簡 {1+frac(x,1-x)-frac(2x,x^2-1)}，並寫出 x 的限制。"
SOL["D"] = [
    "第 1 步（分解與統一符號）：{x^2-1=(x-1)(x+1)}；"
    "而 {1-x=-(x-1)}，所以第二項 {frac(x,1-x)=frac(-x,x-1)}。"
    "公分母取 {(x-1)(x+1)}。",
    "第 2 步（通分，分子記得加括號）："
    "{1=frac((x-1)(x+1),(x-1)(x+1))}；"
    "{frac(-x,x-1)=frac(-x(x+1),(x-1)(x+1))}；"
    "{frac(2x,x^2-1)=frac(2x,(x-1)(x+1))}。",
    "第 3 步（合併分子）：分子 {=(x^2-1)-x(x+1)-2x}"
    "{=x^2-1-x^2-x-2x=-3x-1}。",
    "所以原式 {=frac(-3x-1,(x-1)(x+1))}，也可以寫成 {frac(-(3x+1),x^2-1)}。"
    "分子 {-(3x+1)} 與分母沒有公因式，不能再約。",
    "第 4 步（限制）：原式的分母是 {1-x} 與 {x^2-1}，"
    "所以 {x!=1} 且 {x!=-1}。",
    "檢核：取 {x=2}——原式 {=1+frac(2,-1)-frac(4,3)=1-2-frac(4,3)=-frac(7,3)}；"
    "而 {frac(-(3*2+1),4-1)=frac(-7,3)}——相符。",
]
NOTE["D"] = ("※ 第 2 步的括號是本題成敗的關鍵。"
             "{-x(x+1)} 展開是 {-x^2-x}；如果漏了括號寫成 {-x*x+1}，"
             "第二項的正負號就會反過來，之後全錯而且很難查出。"
             "習慣做法：只要分子前面是減號，就先把整個分子括起來再展開。")

EX_ORDER = ["A", "B", "C", "D"]
EX_HEAD = {"A": "四、範例A・根式化簡：拆、開、併",
           "B": "五、範例B・有理化：共軛只調中間的符號",
           "C": "六、範例C・根式運算：逐項化到最簡再合併",
           "D": "七、範例D・分式化簡：通分、合併，最後寫限制"}
EX_BREAK = {"A": True, "B": False, "C": True, "D": True}

# ---------------------------------------------------------------- D12 示範清單
DEMO_CHECK = ["根號內已經沒有完全平方因數",
              "同類根式已經合併，不同類的沒有硬加在一起",
              "分母已經沒有根號",
              "分式題已經寫出 x 不可以等於甚麼",
              "每一題都有中間步驟，不是只寫一個答案"]

# ---------------------------------------------------------------- 教師實施說明
TN = dict(
    main_design="D2 手順卡——三張：《根式化簡》（拆／開／併）、《分母有理化》"
                "（取共軛／平方差／約簡）、《分式化簡》（分解／通分／合併約分／寫限制），"
                "每一步下方附該步最易出錯的關鍵點（※ 前綴），另出工具卡讓學生放桌面",
    aux_designs=("D9 草稿分區——練習A、B 的作答區由四格取代書寫橫線，"
                 "每格印上格名（抄原式／拆或通分／計算合併／檢查），格名與空間在同一格內",
                 "D12 自我核對清單＋核對點——每個練習區塊末尾一張 ☐ 清單，"
                 "項目全部可觀察、能自己判定；區塊之間放【核對點】細線"),
    reason=(
        "本課取自題庫 A4 代數運算中的根式與分式組（根式化簡與有理化約 12 題、"
        "分式化簡約 5 題），與 L5 同屬 teaching-designs.md 的 S2 多步驟程序運算，"
        "所以主設計沿用 D2 手順卡——但三種題型各有自己的固定程序，因此出三張卡而不是一張。"
        "輔助設計取 S2 表列的另外兩個（D9 草稿分區、D12 自我核對），"
        "理由是本課的失分結構與 L5 不同：L5 錯在漏步驟（尤其是驗真數），"
        "本課錯在草稿排版——係數與根號混寫、通分時漏括號導致整項變號、"
        "約分時把「項」當「因式」約掉。這三種都是視覺—運動整合與版面問題，"
        "正是 D9 針對的失分原因（研究②澳門 IEP 短期目標的「草稿紙版面分區卡」）。"
        "D12 則負責把「化簡到底算不算完」變成四個看得出來的問題，"
        "取代學生自己說不清楚的「應該做完了」。"
        "本課沒有再用 D14 錯誤分析對比：本課的高頻錯法不只一個"
        "（漏括號、約項、忘記寫限制），逐一做正誤雙欄會超過「主 1＋輔 2」的上限，"
        "改為把每一個錯法寫進手順卡對應那一步的 ※ 易錯點，"
        "以及自我核對清單的對應項目。"),
    density="抽離小班（Tier 2）",
    fading=(
        "手順卡（D2）：本課講義印出三張完整卡（每步附易錯點），另出工具卡放桌面 → "
        "練習A 每題旁重印該題用得著的那一張的關鍵詞 → 練習B 只在區塊開頭印一次 → "
        "練習C 不印 → 之後只留一句「記得寫限制」→ 完全移除。"
        "L5 的《對數四步卡》本課起只保留「驗真數」一項，已併入本課的自我核對清單。｜"
        "草稿分區（D9）：練習A、B 的作答區是四格並印上格名 → "
        "練習C 回到一般作答行，只在開頭寫一句「請自己分四步寫」→ "
        "之後不提示 → 移除（格子本身是作答空間，不會變成永久依賴，"
        "但要確認學生在沒有格線時仍然分得出四步）。｜"
        "自我核對（D12）：本課每個區塊末尾一張四項清單 → 下一課減為兩項"
        "（只留「寫了限制嗎」「約的是因式嗎」）→ 之後改由學生自己說出兩項 → 移除。"),
    flows=("F5 課前流程預告（今天四件事：三張手順卡 → 四個範例 → 練習A／B／C → 每區核對）",
           "F2 番茄鐘分段（本課三種題型各有自己的程序，"
           "建議每做完一個練習區塊就停一次，對照清單核對之後才進入下一種題型）",
           "F4 過程導向回饋與分步計分（四個格子各自給分；"
           "特別是分式題的「寫出限制」要獨立計分，寫了就給分——對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點（三張手順卡即為此項，"
               "若獲准帶入測考需寫入 IEP 第 9 點）",
               "a5 放大字體",
               "a6 增加行距／放大作答欄（草稿分區的四格即為此項）",
               "a7 調整計分標準（拆／開／併或分解／通分／合併／限制分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，"
            "只調整呈現方式與鷹架密度，未刪減內容。"),
           ("與 L5 的銜接",
            "L5 與本課都是 S2 多步驟程序運算，主設計同樣是 D2 手順卡，"
            "所以學生已經熟悉「一步一步、做完一步才做下一步」的節奏。"
            "差別在輔助設計：L5 的困難是漏步驟，本課的困難是草稿排版，"
            "所以本課把作答區換成四格。第 6 題刻意接回 L5 的對數"
            "（求 {fn(log) sqrt[3](a^2+b^2)}），讓兩課的內容接得上。"),
           ("為何三張卡而不是一張",
            "根式化簡、有理化、分式化簡的程序完全不同（拆／開／併 對 取共軛／平方差／約簡 "
            "對 分解／通分／合併／限制），硬併成一張會變成一張十步的卡，"
            "違反 teaching-designs.md 對 D2「每張卡只呈現一個核心動作」的微觀規範。"
            "三張卡仍然是同一個設計（D2），不佔輔助設計的名額。"),
           ("題量說明",
            "本課練習共 6 題（練習A／B／C 各 2 題），合共 10 個小問，"
            "涵蓋根式化簡、根式加減、有理化因式、有理化計算、兩個分式相加、"
            "分式相減與限制、以及一題接回 L5 對數的整合題。"),
           ("配套文件",
            "《第2章 L6 根式、分式的化簡與有理化　課堂練習》（練習A／B／C ＋ 參考答案）、"
            "《第2章 L6 根式、分式的化簡與有理化　工具卡》"
            "（三張手順卡 ＋ 自我核對卡，學生剪下護貝放桌面）。")),
)


# ================================================================ docx
def build_docx_file():
    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、三張手順卡", page_break_before=True))
    P.append(para("三種題型各有自己的程序。做題時先認出這是哪一種，"
                  "再把對應那一張卡放在旁邊，用手指指住正在做的那一步。"))
    for c in CARDS_D2:
        P.append(step_card(c["title"], c["steps"],
                           trigger=c["trigger"], fading=c["fading"]))
        P.append(blank())

    P.append(heading("三、草稿要怎樣寫", page_break_before=True))
    P.append(para("本課的失分，多數不是不會做，而是草稿寫得亂。"
                  "由這一課開始，作答區劃成四個格子，每一格只做一件事"
                  "——寫在哪一格，就代表你正在做哪一步。下面是空白的樣式，"
                  "練習卷上每一題都是這個格式。"))
    P.append(quadrant_workspace(QUAD_LABELS, cell_h=1500))
    P.append(para("每一個練習區塊做完之後，還有一張核對清單。"
                  "五個項目全部是看一眼就答得出的問題："))
    P.append(selfcheck_list(DEMO_CHECK, title="化簡題的通用核對清單"))

    for k in EX_ORDER:
        P.append(heading(EX_HEAD[k], page_break_before=EX_BREAK[k]))
        P.append(problem_box([para(EX[k])]))
        for t in SOL[k]:
            P.append(para(t))
        P.append(shaded_box(NOTE[k]))

    P.append(heading("八、接下來"))
    P.append(para("請拿出《第2章 L6 根式、分式的化簡與有理化　課堂練習》，"
                  "並把《工具卡》剪下來放在桌面。練習A、練習B 的作答區是四個格子，"
                  "題目旁邊有該題用得著的那一張卡的關鍵詞；"
                  "練習C 回到一般作答行，卡片與關鍵詞都不再印，"
                  "但四個步驟仍然要分開寫。每一區做完，先對照核對清單再往下。"))

    P += teacher_notes(**TN)
    return build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT)


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


def _split_args(s, start):
    """s[start] 必須是 '('。回傳 (頂層逗號分開的引數 list, 收括號後的位置)。"""
    depth, args, cur, i = 0, [], [], start
    while i < len(s):
        c = s[i]
        if c == "(":
            depth += 1
            if depth == 1:
                i += 1
                continue
        elif c == ")":
            depth -= 1
            if depth == 0:
                args.append("".join(cur))
                return args, i + 1
        elif c == "," and depth == 1:
            args.append("".join(cur))
            cur = []
            i += 1
            continue
        cur.append(c)
        i += 1
    return None, start


def _conv(s):
    """遞迴展開 frac(a,b)／sqrt(x)／sqrt[n](x)。**引數可以含括號**——
    用正則 [^(),]+ 抓引數會漏掉 frac(x+1,(x-1)(x+1)) 這種寫法，
    結果 HTML 印出字面 frac(...) 而 docx 正確（2026-07-28 實錄）。"""
    out, i = [], 0
    while i < len(s):
        if s.startswith("frac(", i):
            args, end = _split_args(s, i + 4)
            if args and len(args) == 2:
                out.append("\\frac{%s}{%s}" % (_conv(args[0]), _conv(args[1])))
                i = end
                continue
        if s.startswith("sqrt[", i):
            j = s.find("]", i)
            if j > 0 and j + 1 < len(s) and s[j + 1] == "(":
                args, end = _split_args(s, j + 1)
                if args and len(args) == 1:
                    out.append("\\sqrt[%s]{%s}" % (s[i + 5:j], _conv(args[0])))
                    i = end
                    continue
        if s.startswith("sqrt(", i):
            args, end = _split_args(s, i + 4)
            if args and len(args) == 1:
                out.append("\\sqrt{%s}" % _conv(args[0]))
                i = end
                continue
        out.append(s[i])
        i += 1
    return "".join(out)


def _tex(m):
    """把 {} 標記轉成 MathJax 的 \\( \\)，結果必須與 omml_core 一致。"""
    import re
    body = m.strip()
    # fn(log) → \log，排在 _conv 之前
    body = re.sub(r"fn\((\w+)\)", r"\\\1 ", body)
    body = _conv(body)
    body = re.sub(r"\bpi\b", r"\\pi ", body)
    # 上下標：多字元要包 {}；括號要保留（omml_core 也是照印的）
    body = re.sub(r"\^\(([^()]*)\)", r"^{(\1)}", body)
    body = re.sub(r"_\(([^()]*)\)", r"_{(\1)}", body)
    body = re.sub(r"\^(\w{2,})", r"^{\1}", body)
    body = re.sub(r"_(\w{2,})", r"_{\1}", body)
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
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


def _step_card_html(c):
    rows = "".join('<tr><td>%d. %s</td><td class="pitfall">※ %s</td></tr>'
                   % (i, _h(a), _h(p)) for i, (a, p) in enumerate(c["steps"], 1))
    return ('<table class="d-tbl step-card"><tr><th colspan="2">%s</th></tr>'
            '<tr><td colspan="2">什麼時候用：%s</td></tr>%s'
            '<tr><td colspan="2">（教師）褪除：%s</td></tr></table>'
            % (_esc(c["title"]), _h(c["trigger"]), rows, _esc(c["fading"])))


def _quadrant_html(labels):
    def cell(t):
        return '<td><div class="qlabel">%s</div></td>' % _esc(t)
    rows = "".join("<tr>%s%s</tr>" % (cell(labels[i]), cell(labels[i + 1]))
                   for i in range(0, len(labels), 2))
    return '<table class="d-tbl quadrant">%s</table>' % rows


def _selfcheck_html(items, title="做完先自己核對一次"):
    return ('<div class="selfcheck"><div style="font-weight:700">%s</div>%s</div>'
            % (_esc(title),
               "".join("<div>&#9744; %s</div>" % _esc(t) for t in items)))


def build_html_file():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", "講義：" + UNIT)
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .selfcheck, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
</style>
</head>""")

    parts = []
    parts.append('<div class="masthead"><span>科目：高三數學</span><span>單元：'
                 + _esc(UNIT) + '</span><span>類型：課堂講義</span></div>')
    parts.append('<div class="ws-meta">姓名：<span class="u">&nbsp;</span>'
                 '班別：<span class="u">&nbsp;</span>學號：<span class="u">&nbsp;</span>'
                 '日期：<span class="u">&nbsp;</span></div>')

    parts.append('<div class="section-h">一、這一課要做到的事</div>')
    parts += ["<div>%s</div>" % _h(t) for t in INTRO]

    parts.append('<div class="section-h page-break">二、三張手順卡</div>')
    parts.append('<div>三種題型各有自己的程序。做題時先認出這是哪一種，'
                 '再把對應那一張卡放在旁邊，用手指指住正在做的那一步。</div>')
    parts += [_step_card_html(c) for c in CARDS_D2]

    parts.append('<div class="section-h page-break">三、草稿要怎樣寫</div>')
    parts.append('<div>本課的失分，多數不是不會做，而是草稿寫得亂。'
                 '由這一課開始，作答區劃成四個格子，每一格只做一件事'
                 '——寫在哪一格，就代表你正在做哪一步。下面是空白的樣式，'
                 '練習卷上每一題都是這個格式。</div>')
    parts.append(_quadrant_html(QUAD_LABELS))
    parts.append('<div>每一個練習區塊做完之後，還有一張核對清單。'
                 '五個項目全部是看一眼就答得出的問題：</div>')
    parts.append(_selfcheck_html(DEMO_CHECK, "化簡題的通用核對清單"))

    for k in EX_ORDER:
        parts.append('<div class="section-h%s">%s</div>'
                     % (" page-break" if EX_BREAK[k] else "", _esc(EX_HEAD[k])))
        parts.append('<div class="problem">%s</div>' % _h(EX[k]))
        parts += ["<div>%s</div>" % _h(t) for t in SOL[k]]
        parts.append('<div class="hint-card">%s</div>' % _h(NOTE[k]))

    parts.append('<div class="section-h">八、接下來</div>')
    parts.append('<div>請拿出《第2章 L6 根式、分式的化簡與有理化　課堂練習》，'
                 '並把《工具卡》剪下來放在桌面。練習A、練習B 的作答區是四個格子，'
                 '題目旁邊有該題用得著的那一張卡的關鍵詞；'
                 '練習C 回到一般作答行，卡片與關鍵詞都不再印，'
                 '但四個步驟仍然要分開寫。每一區做完，先對照核對清單再往下。</div>')

    parts.append('<div class="footer">' + _esc(FOOT) + '</div>')

    tn_rows = [("本份採用的主設計", TN["main_design"]),
               ("輔助設計", "、".join(TN["aux_designs"])),
               ("選用理由", TN["reason"]),
               ("鷹架密度", TN["density"]),
               ("褪除路徑", TN["fading"]),
               ("課堂實施流程", "、".join(TN["flows"])),
               ("對應官方輔助措施代碼", "、".join(TN["iep_codes"]))]
    tn_rows += list(TN["extra"])
    tn = "".join("<tr><td>%s</td><td>%s</td></tr>" % (_esc(k), _h(v)) for k, v in tn_rows)
    parts.append('<div class="teacher-notes">'
                 '<div class="section-h">教師實施說明（本頁供教師參考，列印給學生時可不印）</div>'
                 '<table class="d-tbl">%s</table></div>' % tn)

    body = ("\n<body>\n<div class=\"page\">\n\n" + "\n\n".join(parts)
            + "\n\n</div>\n</body>\n</html>\n")
    path = os.path.join(HERE, BASE + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + body)
    return path


if __name__ == "__main__":
    print(build_docx_file())
    print(build_html_file())
