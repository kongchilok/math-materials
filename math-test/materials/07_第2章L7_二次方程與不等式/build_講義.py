# -*- coding: utf-8 -*-
"""
第2章 中學基礎數學應用．L7 一元二次方程與二次不等式 —— 課堂講義 build script
主設計 D2 手順卡（三張：解一元二次方程／判別式判根／解二次不等式，每步附 ※ 易錯點）；
輔助 D5 圖文雙軌（範例D 的二次不等式：左拋物線／符號線、右代數判斷，逐列對齊）、
D14 錯誤分析對比（兩個高頻錯：把不等式當方程解、乘負數不轉向）。
鷹架密度：抽離小班 (Tier 2)。
產出：講義_二次方程與不等式_抽離小班共用版.docx / .html（.pdf 由 html_to_pdf.ps1 轉）
"""
import os
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8")
SKILL = r"C:\Users\KongChiLok\.claude\skills\inclusive-math-worksheet-generator\scripts"
sys.path.insert(0, SKILL)
from omml_docx import *                      # noqa: E402,F403
import design_svg as ds                      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "講義_二次方程與不等式_抽離小班共用版"
UNIT = "第2章 中學基礎數學應用．L7 一元二次方程與二次不等式"
FOOT = "高三數學．" + UNIT


# ================================================================ 拋物線／符號線 SVG
# design_svg 沒有拋物線元件，照 L4 clock_svg 的做法自建（回傳完整 SVG 字串）。
# 用於 D5 範例D：一條開口向上的拋物線過兩根，可標三段正負、可在 x 軸標解區間。
def parabola_svg(r1, r2, opens_up=True, signs=False, shade=None, strict=True,
                 w=340, h=224):
    """r1<r2 兩根；opens_up 開口方向；signs=True 標三段的 ＋／−；
    shade ∈ {None,'outside','inside'} 在 x 軸標解區間（outside 兩邊帶箭頭）；
    strict=True 端點空心（>／<），False 端點實心（≥／≤）。"""
    padL = padR = 30
    padT, padB = 22, 46
    axis_y = h - padB - 40
    span = r2 - r1
    m = max(1.4, span * 0.72)
    xlo, xhi = r1 - m, r2 + m

    def px(x):
        return padL + (x - xlo) / (xhi - xlo) * (w - padL - padR)

    a = 1.0 if opens_up else -1.0

    def yv(x):
        return a * (x - r1) * (x - r2)

    vals = [yv(xlo), yv(xhi), yv((r1 + r2) / 2)]
    ymax, ymin = max(vals), min(vals)
    up_room, dn_room = axis_y - padT, (h - padB) - axis_y
    sup = up_room / ymax if ymax > 0 else 1e9
    sdn = dn_room / (-ymin) if ymin < 0 else 1e9
    sc = min(sup, sdn) * 0.86

    def py(y):
        return axis_y - y * sc

    b = [f'<defs><marker id="pa" markerWidth="9" markerHeight="9" refX="7" refY="3" '
         f'orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="{ds.INK}"/></marker></defs>']
    b.append(ds._line(padL - 8, axis_y, w - padR + 8, axis_y, sw=1.5))
    b.append(ds._txt(w - padR + 10, axis_y, "x", size=12, anchor="start"))
    pts = []
    for i in range(61):
        x = xlo + (xhi - xlo) * i / 60
        pts.append("%.1f,%.1f" % (px(x), py(yv(x))))
    b.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>'
             % (" ".join(pts), ds.INK))
    for r in (r1, r2):
        fill = ds.INK if not strict else "#ffffff"
        b.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s" stroke="%s" '
                 'stroke-width="1.5"/>' % (px(r), axis_y, fill, ds.INK))
        b.append(ds._txt(px(r), axis_y + 18, ("%g" % r).replace("-", "−"), size=12))
    if signs:
        for xx in ((xlo + r1) / 2, (r1 + r2) / 2, (r2 + xhi) / 2):
            s = "＋" if yv(xx) > 0 else "−"
            yy = axis_y - 15 if s == "＋" else axis_y + 35
            b.append(ds._txt(px(xx), yy, s, size=15, bold=True, halo=True))
    if shade:
        fill = ds.INK if not strict else "#ffffff"

        def ep(x):
            return ('<circle cx="%.1f" cy="%.1f" r="5" fill="%s" stroke="%s" '
                    'stroke-width="1.6"/>' % (px(x), axis_y, fill, ds.INK))
        if shade == "inside":
            b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                     'stroke-width="4.5"/>' % (px(r1), axis_y, px(r2), axis_y, ds.INK))
        elif shade == "outside":
            # 由根向外畫，marker-end 自動朝外（左段朝左、右段朝右）
            b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                     'stroke-width="4.5" marker-end="url(#pa)"/>'
                     % (px(r1), axis_y, px(xlo), axis_y, ds.INK))
            b.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                     'stroke-width="4.5" marker-end="url(#pa)"/>'
                     % (px(r2), axis_y, px(xhi), axis_y, ds.INK))
        b.append(ep(r1))
        b.append(ep(r2))
    return ds._svg(w, h, "".join(b))


# D5 三格（範例D：x²−2x−3，兩根 −1、3，開口向上）
D5_SVGS = [parabola_svg(-1, 3, signs=False, shade=None),
           parabola_svg(-1, 3, signs=True, shade=None),
           parabola_svg(-1, 3, signs=True, shade="outside")]
D5_HEADERS = ("拋物線／符號線（看得見）", "代數上怎樣判斷（寫得出）")
D5_RIGHT = [
    "第 1 步（求根）：解 {x^2-2x-3=0} → {(x-3)(x+1)=0} → 兩根 {x=-1}、{x=3}。"
    "{x^2} 的係數是正的，所以拋物線開口向上。",
    "第 2 步（看正負）：開口向上時，兩根之間落在 x 軸下方（值為負，標 −）；"
    "兩根外側落在 x 軸上方（值為正，標 ＋）。",
    "第 3 步（取區間）：要 {x^2-2x-3>0}（正），就取兩個 ＋ 的部分＝兩根外側，"
    "得 {x<-1} 或 {x>3}。若改問 {x^2-2x-3<=0}，就取中間那一段：{-1<=x<=3}。",
]

# ================================================================ 文字內容
INTRO = [
    "這一課把一元二次的兩件事一次收齊：把方程解出來（求根），"
    "以及不解出根也能判斷「有幾個實根」（判別式）；"
    "再進一步，把「等於 0」換成「大於 0／小於 0」，就是二次不等式。"
    "三件事共用同一個起手式——先把式子整理成「一邊是 0」的標準式 {ax^2+bx+c=0}。",
    "和前兩課一樣，本課是多步驟的程序運算，所以主工具仍然是手順卡：三張卡分別管"
    "解方程、判別式、解不等式，每一步下面都標了那一步最容易錯的地方（※）。",
    "但本課多了一個前兩課沒有的難點：二次不等式。多數人不是解不出根，"
    "而是求了兩根之後，不知道答案應該「取哪一段」——這不是算術問題，是看圖的問題。"
    "所以本課加一個圖文雙軌：左邊畫拋物線與符號線，右邊寫對應的代數判斷，"
    "把「要取哪一段」由背口訣變成看得見的圖。",
    "最後把兩個每年都有人中招的錯法挑出來正誤對照：一個是把不等式當方程解、"
    "答成兩個點；一個是兩邊乘負數卻忘了把不等號轉向。"
    "看清楚這兩步分歧在哪裡，比多做十題更有用。",
]

# ---------------------------------------------------------------- D2 三張手順卡
CARD1 = dict(
    title="手順卡一・解一元二次方程",
    trigger="題目是 {ax^2+bx+c=0} 這種、要你「解方程」或「求 x」。",
    steps=[
        ("先整理成標準式：一邊是 0，{ax^2+bx+c=0}。",
         "移項要變號；不要兩邊直接除以 x——那樣會把 {x=0} 這個根丟掉。"),
        ("試因式分解：能分解成 {(px+q)(rx+s)=0} 就令每個括號分別為 0。",
         "兩個括號各給一個根，不要只解一個。{x^2=9} 要寫成 {(x-3)(x+3)=0}，"
         "得 {x=3} 和 {x=-3}，不是只有 {x=3}。"),
        ("分解不到就用公式法 {x=frac(-b+-sqrt(b^2-4ac),2a)}。",
         "先算 {b^2-4ac}；{-b} 的負號不要漏；整條式子的分母是 {2a}，不是 {a}。"),
    ],
    fading="完整三步卡 → 只留關鍵詞（標準式、試分解、公式法）→ "
           "只留「先化成一邊為 0」→ 完全移除。",
)
CARD2 = dict(
    title="手順卡二・判別式判根",
    trigger="題目問「根的情況」「有沒有實根／有幾個實根」「k 為何值時有兩相等根」，"
            "但不要求你把根解出來。",
    steps=[
        ("化成標準式，抄出 {a}、{b}、{c}（連正負號一起抄）。",
         "{c} 是常數項，符號要跟著抄；{b} 是一次項係數。"),
        ("算判別式 {Δ=b^2-4ac}。",
         "{b^2} 一定是非負的（負數平方也變正）；{-4ac} 的正負看 {ac} 的乘積。"),
        ("看 Δ 的正負零：{Δ>0} 兩相異實根；{Δ=0} 兩相等實根（重根）；{Δ<0} 無實根。",
         "{Δ=0} 是「兩個相等」不是「沒有根」——它有一個重根，別答成無解。"),
    ],
    fading="完整三步卡 → 只留一句「{Δ=b^2-4ac}，正兩根、零重根、負無根」→ 完全移除。",
)
CARD3 = dict(
    title="手順卡三・解二次不等式",
    trigger="題目是 {ax^2+bx+c>0}（或 {<0}、{>=0}、{<=0}）這種、要你求 x 的範圍。",
    steps=[
        ("整理成一邊為 0，並讓 {x^2} 的係數是正的（若為負，兩邊乘 −1）。",
         "兩邊乘或除以負數，不等號一定要轉向（> 變 <、≥ 變 ≤）——這是本課最高頻的錯。"),
        ("把它先當等式，解出兩根 {r_1<r_2}（用因式分解或公式法）。",
         "先求根才畫得出線；求不到實根時（{Δ<0}）另作判斷，本課題目都有實根。"),
        ("畫開口向上的拋物線／符號線，按不等號取區間。",
         "口訣（開口向上時）：大於取兩邊、小於取中間。> / < 端點空心，≥ / ≤ 端點實心。"),
    ],
    fading="完整三步卡 → 只留口訣「大於取兩邊、小於取中間」→ "
           "只留「先求根、再看拋物線」→ 完全移除。",
)
CARDS_D2 = [CARD1, CARD2, CARD3]

# ---------------------------------------------------------------- 範例
EX, SOL, NOTE = {}, {}, {}

EX["A"] = ("【範例A・因式分解解方程】解下列方程："
           "（a）{x^2-5x+6=0}　（b）{2x^2+3x-2=0}。")
SOL["A"] = [
    "（a）第 1 步（標準式）：已經是 {x^2-5x+6=0}，一邊為 0，可直接分解。",
    "（a）第 2 步（分解）：找兩數之積 6、之和 5 → 2 與 3，所以 {x^2-5x+6=(x-2)(x-3)}。"
    "令 {(x-2)(x-3)=0} → {x=2} 或 {x=3}。",
    "（b）首項係數不是 1，用十字交乘：{2x^2+3x-2=(2x-1)(x+2)}"
    "（展開檢查 {(2x-1)(x+2)=2x^2+4x-x-2=2x^2+3x-2}，正確）。",
    "（b）令每個括號為 0：{2x-1=0} → {x=frac(1,2)}；{x+2=0} → {x=-2}。",
    "檢核：把 {x=2}、{x=3} 代回 (a) 都得 0；把 {x=frac(1,2)}、{x=-2} 代回 (b) 都得 0。",
]
NOTE["A"] = ("※ 令括號為 0 這一步，兩個括號各給一個根，一定有兩個答案"
             "（除非兩個括號相同，那才是重根）。只寫一個 {x=2} 是漏根。")

EX["B"] = "【範例B・公式法】解 {x^2-4x+1=0}（分解不到，用公式法）。"
SOL["B"] = [
    "第 1 步（抄係數）：{a=1}、{b=-4}、{c=1}。",
    "第 2 步（判別式）：{Δ=b^2-4ac=(-4)^2-4*1*1=16-4=12}，大於 0，有兩相異實根。",
    "第 3 步（代公式）：{x=frac(-b+-sqrt(Δ),2a)=frac(4+-sqrt(12),2)}。"
    "把 {sqrt(12)} 化到最簡：{sqrt(12)=sqrt(4*3)=2sqrt(3)}。",
    "第 4 步（約簡）：{x=frac(4+-2sqrt(3),2)=2+-sqrt(3)}"
    "（分子兩項都要除以 2）。",
    "所以 {x=2+sqrt(3)} 或 {x=2-sqrt(3)}。",
    "檢核（韋達定理）：兩根之和 {=(2+sqrt(3))+(2-sqrt(3))=4}，等於 {frac(-b,a)=4}；"
    "兩根之積 {=(2+sqrt(3))(2-sqrt(3))=4-3=1}，等於 {frac(c,a)=1}——相符。",
]
NOTE["B"] = ("※ {-b} 的負號最容易漏：{b=-4}，所以 {-b=4}，不是 {-4}。"
             "還有 {sqrt(12)} 一定要化成 {2sqrt(3)}，再與分母的 2 約簡；"
             "停在 {frac(4+-sqrt(12),2)} 不算做完。")

EX["C"] = ("【範例C・判別式判根】不必解出根，只判斷根的情況："
           "（a）{x^2-6x+9=0}　（b）{2x^2-3x+4=0}　"
           "（c）{x^2+kx+4=0} 有兩個相等實根，求 k。")
SOL["C"] = [
    "（a）{a=1}、{b=-6}、{c=9}。{Δ=(-6)^2-4*1*9=36-36=0} → 兩個相等實根。"
    "（其實 {x^2-6x+9=(x-3)^2}，只有 {x=3} 一個重根，與 {Δ=0} 相符。）",
    "（b）{a=2}、{b=-3}、{c=4}。{Δ=(-3)^2-4*2*4=9-32=-23<0} → 沒有實數根。",
    "（c）「兩個相等實根」即 {Δ=0}：{Δ=k^2-4*1*4=k^2-16=0} → {k^2=16} → "
    "{k=4} 或 {k=-4}（兩個值都要寫）。",
    "檢核（c）：{k=4} 時 {x^2+4x+4=(x+2)^2}，是重根；"
    "{k=-4} 時 {x^2-4x+4=(x-2)^2}，也是重根——兩個都符合。",
]
NOTE["C"] = ("※ 判別式題只看 Δ 的正負零，不必真的把根解出來。"
             "求參數的題（c）常見漏了一個解——{k^2=16} 有 {k=4} 和 {k=-4} 兩個。")

EX["D"] = ("【範例D・二次不等式】用符號線解 {x^2-2x-3>0}，"
           "並順帶寫出 {x^2-2x-3<=0} 的解。")
# 範例D 的解在下面用 D5 圖文雙軌呈現（build 時插入），這裡只放收束與檢核
SOL["D"] = [
    "把三步對照下面的「拋物線／符號線」看：左邊每一格是圖上發生的事，"
    "右邊是同一步在算式上怎樣寫。",
]
NOTE["D"] = ("※ 「大於取兩邊、小於取中間」只在開口向上（{x^2} 係數為正）時成立。"
             "若係數是負的，先照手順卡三第 1 步兩邊乘 −1（記得轉向）變成正的再用這口訣。"
             "另外：> / < 用空心點（不含端點），≥ / ≤ 用實心點（含端點）。")

EX_ORDER = ["A", "B", "C", "D"]
EX_HEAD = {"A": "三、範例A・因式分解解方程",
           "B": "四、範例B・公式法：先算判別式，根號化到最簡",
           "C": "五、範例C・判別式判根：只看 Δ 的正負零",
           "D": "六、範例D・二次不等式：用符號線看要取哪一段"}
EX_BREAK = {"A": True, "B": False, "C": True, "D": True}

# ---------------------------------------------------------------- D14 兩個錯誤對比
ERR1 = dict(
    title="錯法一・把不等式當方程解（答成兩個點）",
    problem="解 {x^2-x-6>0}。",
    rows=[("因式分解 {(x-3)(x+2)>0}，求出 {x=3}、{x=-2}。",
           "因式分解求根：{x=-2}、{x=3}（兩根，開口向上）。"),
          ("答：{x=3} 或 {x=-2}。",
           "答：取兩根外側 {x<-2} 或 {x>3}。")],
    note="※ 差在這裡：不等式問的是「哪些 x 使式子 {>0}」，答案是一段範圍，"
         "不是兩個點。兩個根只是分界線，真正的解在兩根的外側（開口向上、要正）。",
)
ERR2 = dict(
    title="錯法二・兩邊乘負數，不等號沒有轉向",
    problem="解 {-x^2+4x-3>=0}。",
    rows=[("兩邊乘 −1：{x^2-4x+3>=0}（不等號照抄）。",
           "兩邊乘 −1，不等號轉向：{x^2-4x+3<=0}。"),
          ("{(x-1)(x-3)>=0} → {x<=1} 或 {x>=3}。",
           "{(x-1)(x-3)<=0} → 取中間 {1<=x<=3}。")],
    note="※ 差在這裡：兩邊乘或除以負數，不等號一定要轉向（{>=} 變 {<=}）。"
         "這一步錯，後面全部跟着錯，而且很難查出來。",
)
ERRS = [ERR1, ERR2]

# ---------------------------------------------------------------- 教師實施說明
TN = dict(
    main_design="D2 手順卡——三張：《解一元二次方程》（化標準式／試因式分解／不行就公式法）、"
                "《判別式判根》（抄 a、b、c／算 {Δ=b^2-4ac}／依正負零判斷）、"
                "《解二次不等式》（化標準式且使 x² 係數為正／求兩根／畫符號線取區間），"
                "每步下方附該步最易出錯的關鍵點（※ 前綴），另出工具卡讓學生放桌面",
    aux_designs=("D5 圖文雙軌——範例D 的二次不等式用左圖（拋物線／符號線）、"
                 "右式（同一步的代數判斷）逐列橫向對齊，把「要取哪一段」由背口訣"
                 "變成看得見的圖；練習C 的不等式題褪成學生自己畫符號線",
                 "D14 錯誤分析對比——講義「最容易錯的兩步」放兩個正誤雙欄，"
                 "只針對本課兩個教科書級高頻錯（把不等式當方程解、乘負數不轉向），"
                 "每個只標一個分歧步驟；練習第 6 題給一份錯解要學生圈出分歧步驟並改正"),
    reason=(
        "本課取自題庫 A4 代數運算的二次方程與二次不等式組（判別式判根、公式法、"
        "二次不等式解集，對照 MATH-030、MOCK2-026／029／090、MOCK2-157／174 等題），"
        "與 L5、L6 同屬 teaching-designs.md 的 S2 多步驟程序運算，"
        "所以主設計沿用 D2 手順卡；但解方程、判別式、解不等式三種程序不同，故出三張卡。"
        "輔助設計不沿用 L6 的 D9／D12，改用 D5＋D14，理由是本課的認知瓶頸與前兩課不同："
        "解方程與判別式是純程序（D2 已覆蓋），但二次不等式的失分不在算不出根，"
        "而在「求了根之後不知道要取哪一段」——這是代數結果↔幾何（拋物線開口與符號線）的"
        "雙軌對應問題，屬 S4／S6 結構，正是 D5 圖文雙軌針對的瓶頸。"
        "又因本課是高三複習性質、且有兩個已知高頻的固定錯法（把不等式當方程解、"
        "乘負數不轉向），符合 D14 的觸發條件（D14 不可用於全新概念的第一課，"
        "但複習／訂正課正是它的主場）。三種設計＝主 D2 ＋ 輔 D5、D14，未超過「主1＋輔2」上限。"),
    density="抽離小班（Tier 2）",
    fading=(
        "手順卡（D2）：講義印三張完整卡（每步附易錯點），另出工具卡放桌面 → "
        "練習A 每題旁重印該題用得著的那一張的關鍵詞 → 練習B 只在區塊開頭印一次 → "
        "練習C 不印 → 之後只留一句「先化成一邊為 0」→ 完全移除。｜"
        "圖文雙軌（D5）：講義範例D 左圖右式全給 → 練習C 的不等式題只給「請自己畫符號線」"
        "與空白作圖區（右式由學生自己寫）→ 之後改成口頭講出「開口向上、取哪一段」→ 移除。｜"
        "錯誤對比（D14）：講義給完整正誤雙欄 → 練習只給錯解要學生圈出分歧步驟並改正（第 6 題）"
        "→ 之後只給一句「這題有一個常見陷阱，是什麼」→ 移除。"),
    flows=("F5 課前流程預告（今天五件事：三張手順卡 → 範例A～C → 範例D 看符號線 → "
           "最容易錯的兩步 → 練習A／B／C）",
           "F2 番茄鐘分段（解方程、判別式、不等式三塊各自是一段，"
           "做完一塊對照核對清單再進入下一塊）",
           "F4 過程導向回饋與分步計分（判別式題把「抄對 a、b、c」「算對 Δ」「判斷正確」"
           "分三步各給分；不等式題把「求根」「判斷開口與區間」「寫對含不含端點」分開給分"
           "——對應官方代碼 a7）"),
    iep_codes=("a3 提示題目重點（三張手順卡即為此項，若獲准帶入測考需寫入 IEP 第 9 點）",
               "a5 放大字體",
               "a6 增加行距／放大作答欄",
               "a7 調整計分標準（求根／判別式／取區間分步給分）"),
    extra=(("本份文件性質",
            "調整支援（Accommodation）——核心概念與年級標準不變，"
            "只調整呈現方式與鷹架密度，未刪減內容。"),
           ("與 L5、L6 的銜接",
            "三課都是 S2 多步驟程序運算、主設計同為 D2 手順卡，學生已熟悉"
            "「一步一步、做完一步才做下一步」的節奏。差別在輔助設計："
            "L5 補 D13／D14 管術語與錯法、L6 補 D9／D12 管草稿排版，"
            "本課補 D5／D14 管「二次不等式要取哪一段」這個看圖判斷。"),
           ("為何三張卡而不是一張",
            "解方程、判別式、解不等式三種程序的核心動作各不相同"
            "（試分解／算 Δ／畫符號線取區間），硬併成一張會變成一張九步的卡，"
            "違反 teaching-designs.md 對 D2「每張卡只呈現一個核心動作」的規範。"
            "三張卡仍是同一個設計（D2），不佔輔助設計名額。"),
           ("題量說明",
            "本課練習共 6 題（練習A／B／C 各 2 題），合共 11 個小問，"
            "涵蓋因式分解解方程、平方差、判別式（Δ=0／Δ<0）、公式法、求參數 k、"
            "二次不等式（取中間／取兩邊）、以及一題乘負數轉向的找錯題。"),
           ("配套文件",
            "《第2章 L7 一元二次方程與二次不等式　課堂練習》（練習A／B／C ＋ 參考答案）、"
            "《第2章 L7 一元二次方程與二次不等式　工具卡》"
            "（三張手順卡 ＋ 判別式速查卡，學生剪下護貝放桌面）。")),
)


# ================================================================ docx
def build_docx_file():
    figdir = os.path.join(HERE, "_figtmp")
    os.makedirs(figdir, exist_ok=True)
    MEDIA = MediaRegistry()
    d5_pairs = []
    for i, (svg, rt) in enumerate(zip(D5_SVGS, D5_RIGHT), 1):
        png = os.path.join(figdir, "d5_%d.png" % i)
        ds.svg_to_png(svg, png, scale=3)
        d5_pairs.append((image_para(png, width_cm=7.0), rt))

    P = [masthead("高三數學", UNIT, "課堂講義"), student_info_row()]

    P.append(heading("一、這一課要做到的事"))
    for t in INTRO:
        P.append(para(t))

    P.append(heading("二、三張手順卡", page_break_before=True))
    P.append(para("三種題型的起手式相同（先化成一邊為 0），但接下來的動作不同。"
                  "做題時先認出這是哪一種，再把對應那一張卡放在旁邊，"
                  "用手指指住正在做的那一步。"))
    for c in CARDS_D2:
        P.append(step_card(c["title"], c["steps"],
                           trigger=c["trigger"], fading=c["fading"]))
        P.append(blank())

    for k in EX_ORDER:
        P.append(heading(EX_HEAD[k], page_break_before=EX_BREAK[k]))
        P.append(problem_box([para(EX[k])]))
        for t in SOL[k]:
            P.append(para(t))
        if k == "D":
            P.append(dual_track_table(d5_pairs, media=MEDIA, headers=D5_HEADERS))
        P.append(shaded_box(NOTE[k]))

    P.append(heading("七、最容易錯的兩步（正誤對照）", page_break_before=True))
    P.append(para("下面兩個錯法每年都有人中招。左欄是「很多人會這樣寫」，"
                  "右欄是正確寫法，兩欄同一列對齊，只有一步不同——看清楚那一步。"))
    for e in ERRS:
        P.append(para(e["title"], bold=True))
        P.append(problem_box([para(e["problem"])]))
        P.append(dual_track_table(e["rows"], headers=("常見寫法（很多人會這樣）", "正確寫法")))
        P.append(shaded_box(e["note"]))
        P.append(blank())

    P.append(heading("八、接下來"))
    P.append(para("請拿出《第2章 L7 一元二次方程與二次不等式　課堂練習》，"
                  "並把《工具卡》剪下來放在桌面。練習A 每題旁標明了要用哪一張手順卡；"
                  "練習B 只在開頭重印一次三張卡的關鍵詞；練習C 不再印卡，"
                  "不等式題要自己畫符號線。每一區做完，先對照核對清單再往下。"))

    P += teacher_notes(**TN)
    out = build_docx(P, os.path.join(HERE, BASE + ".docx"), footer_text=FOOT, media=MEDIA)
    shutil.rmtree(figdir, ignore_errors=True)
    return out


# ================================================================ HTML
def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


_TEX_MAP = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to", "+-": r"\pm",
            "*": r"\times"}


def _split_args(s, start):
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
    import re
    body = m.strip()
    body = re.sub(r"fn\((\w+)\)", r"\\\1 ", body)
    body = _conv(body)
    body = re.sub(r"\bpi\b", r"\\pi ", body)
    body = body.replace("Δ", r"\Delta ")
    body = re.sub(r"\^\(([^()]*)\)", r"^{(\1)}", body)
    body = re.sub(r"_\(([^()]*)\)", r"_{(\1)}", body)
    body = re.sub(r"\^(\w{2,})", r"^{\1}", body)
    body = re.sub(r"_(\w{2,})", r"_{\1}", body)
    for k, v in _TEX_MAP.items():
        body = body.replace(k, " " + v + " ")
    # 嚴格不等號：轉成 \lt \gt，令 HTML 原始碼不留裸 < >（避免被當標籤，QB-14）
    body = body.replace("<", r" \lt ").replace(">", r" \gt ")
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
            # fading 用 _h 不用 _esc：本課 CARD2 的褪除句含 {Δ=b^2-4ac}，
            # 用 _esc 會把大括號原樣印出來（docx 的 step_card 是 para() 會 parse，
            # 兩版才一致）。L6 的 fading 無數學所以一直沒踩到這個 bug。
            % (_esc(c["title"]), _h(c["trigger"]), rows, _h(c["fading"])))


def _dualtrack_html(pairs, headers):
    def side(x):
        return x if x.lstrip().startswith("<svg") else _h(x)
    head = "<tr><th>%s</th><th>%s</th></tr>" % (_esc(headers[0]), _esc(headers[1]))
    body = "".join("<tr><td>%s</td><td>%s</td></tr>" % (side(l), side(r))
                   for l, r in pairs)
    return '<table class="d-tbl dual-track">%s%s</table>' % (head, body)


def build_html_file():
    tpl = open(os.path.join(SKILL, "..", "assets", "worksheet-template.html"),
               encoding="utf-8").read()
    head = tpl[:tpl.index("</head>") + len("</head>")].replace("[講義標題]", "講義：" + UNIT)
    head = head.replace("</head>", """<style>
  .hint-card, .fig, .selfcheck, .d-tbl tr { break-inside: avoid; }
  .section-h { break-after: avoid; }
  .dual-track td:first-child { text-align: center; }
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
    parts.append('<div>三種題型的起手式相同（先化成一邊為 0），但接下來的動作不同。'
                 '做題時先認出這是哪一種，再把對應那一張卡放在旁邊，'
                 '用手指指住正在做的那一步。</div>')
    parts += [_step_card_html(c) for c in CARDS_D2]

    d5_html_pairs = list(zip(D5_SVGS, D5_RIGHT))
    for k in EX_ORDER:
        parts.append('<div class="section-h%s">%s</div>'
                     % (" page-break" if EX_BREAK[k] else "", _esc(EX_HEAD[k])))
        parts.append('<div class="problem">%s</div>' % _h(EX[k]))
        parts += ["<div>%s</div>" % _h(t) for t in SOL[k]]
        if k == "D":
            parts.append(_dualtrack_html(d5_html_pairs, D5_HEADERS))
        parts.append('<div class="hint-card">%s</div>' % _h(NOTE[k]))

    parts.append('<div class="section-h page-break">七、最容易錯的兩步（正誤對照）</div>')
    parts.append('<div>下面兩個錯法每年都有人中招。左欄是「很多人會這樣寫」，'
                 '右欄是正確寫法，兩欄同一列對齊，只有一步不同——看清楚那一步。</div>')
    for e in ERRS:
        parts.append('<div style="font-weight:700;margin-top:10px">%s</div>' % _esc(e["title"]))
        parts.append('<div class="problem">%s</div>' % _h(e["problem"]))
        parts.append(_dualtrack_html(e["rows"], ("常見寫法（很多人會這樣）", "正確寫法")))
        parts.append('<div class="hint-card">%s</div>' % _h(e["note"]))

    parts.append('<div class="section-h">八、接下來</div>')
    parts.append('<div>請拿出《第2章 L7 一元二次方程與二次不等式　課堂練習》，'
                 '並把《工具卡》剪下來放在桌面。練習A 每題旁標明了要用哪一張手順卡；'
                 '練習B 只在開頭重印一次三張卡的關鍵詞；練習C 不再印卡，'
                 '不等式題要自己畫符號線。每一區做完，先對照核對清單再往下。</div>')

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
