// =====================================================================
// A/B 對比示範 deck：用新 token + kit 重建單元04 代表性頁面
// 對照組＝ 04_分式方程無理方程與二元二次方程組\簡報_*.pptx（舊版，不動）
//
// 內容逐字沿用舊版，只換視覺系統 —— 令比較只反映排版差異，不混入內容差異。
// 執行：  $env:NODE_PATH="<已驗證的 node_modules>" ; node build_demo_deck.js
// =====================================================================
const { Deck, T } = require("./deck-kit.js");
const { color, type, comp, layout, leading, space, radius } = T;

const d = new Deck({
  title: "分式方程・無理方程・二元二次方程組（融合抽離版・美化試驗）",
  author: "初三數學抽離小組",
  footerText: "初三數學 · 分式方程・無理方程・二元二次方程組（抽離小組·融合版）",
  strict: true, // 版面違規即丟錯
});
const M = layout.marginX;
const CW = layout.contentW;

// =====================================================================
// S1 封面
// 改動：去除多餘裝飾帶，改用一條主色細線分隔「識別」與「主標」；
//       主標與副標拉開層級（56 / 30），站別列改為帶編號的節奏列。
// =====================================================================
(function () {
  const s = d.slide({ dark: true, noFooter: true });
  // 全頁深底 → 文字一律走 darkText（微灰白＋加大 2pt＋加字距，抗光暈）
  d.band(s, M, 1.24, 3.55, 0.68, color.accent.solid, radius.pill);
  s.addText("初三數學 · 抽離小組", {
    x: M, y: 1.24, w: 3.55, h: 0.68, align: "center", valign: "middle",
    fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, bold: true,
    color: color.ink.onSolid, charSpacing: 0.8,
  });

  s.addText("三種新方程", {
    x: M, y: 2.16, w: CW, h: 1.05, align: "left", valign: "middle",
    fontFace: type.hero.fontFace, fontSize: type.hero.fontSize, bold: true,
    color: color.ink.onDark, charSpacing: 1.2,
  });
  s.addText("把未知數放出來", {
    x: M, y: 3.26, w: CW, h: 0.72, align: "left", valign: "middle",
    fontFace: type.subtitle.fontFace, fontSize: type.subtitle.fontSize, bold: true,
    color: color.ink.onDarkMuted, charSpacing: 1.0,
  });

  d.seg(s, M, 4.24, M + 2.2, 4.24, { color: color.accent.decor, width: 3 });

  // 站別列：28pt（26+2）＋字距，這是使用者最擔心的白字襯深底處
  const stations = ["站① 分式方程", "站② 無理方程", "站③ 二元二次方程組"];
  let sx = M;
  stations.forEach((t, i) => {
    d.darkText(s, t, {
      x: sx, y: 4.46, w: 3.75, h: 0.56, align: "left", valign: "middle",
      fontSize: type.bodySm.fontSize, margin: 0, wrap: false,
    });
    sx += 3.95;
    if (i < stations.length - 1) {
      s.addText("→", {
        x: sx - 0.46, y: 4.46, w: 0.42, h: 0.56, align: "center", valign: "middle",
        fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.accent.decor,
      });
    }
  });

  d.band(s, M, 5.36, 9.4, 0.86, color.surface.darkBand);
  d.darkText(s, "三站共用同一條生死線：驗根", {
    x: M + space.md, y: 5.36, w: 9.0, h: 0.86, align: "left", valign: "middle",
    fontFace: type.headline.fontFace, fontSize: type.headline.fontSize, bold: true,
  });
  s.addNotes("開場定調：今天學三種新方程，看似不同，其實同一個念頭——把未知數放出來。但放出來有代價，所以每一站最後都要驗根。三站節奏一致，做完一站休息一下。");
})();

// =====================================================================
// S2 流程預告頁（ASD 可預測性）
// 改動：去掉每張卡的陰影（原版三張卡疊陰影令畫面變濁），改由框線分隔；
//       徽章與標題基線對齊。
// =====================================================================
(function () {
  const s = d.slide();
  d.title(s, "今日課堂流程");
  const rows = [
    ["站①", "分式方程", "未知數在分母裡 → 去分母 → 驗根（怕增根）"],
    ["站②", "無理方程", "未知數在根號裡 → 兩邊平方 → 驗根（怕假根）"],
    ["站③", "二元二次方程組", "兩條方程 → 代入消元 → 回代求另一個未知數"],
  ];
  let y = 1.86;
  const rowH = 1.30, rowGap = 0.20;
  rows.forEach((r) => {
    d.card(s, M, y, CW, rowH);
    d.stationBadge(s, r[0], M + 0.28, y + (rowH - 0.62) / 2);
    s.addText(r[1], {
      x: M + 2.32, y: y + 0.16, w: CW - 2.6, h: 0.52, align: "left", valign: "middle",
      fontFace: type.headline.fontFace, fontSize: type.headline.fontSize, bold: true, color: color.ink.primary,
    });
    s.addText(r[2], {
      x: M + 2.32, y: y + 0.68, w: CW - 2.6, h: 0.46, align: "left", valign: "middle",
      fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, color: color.ink.secondary,
    });
    y += rowH + rowGap;
  });
  s.addText("每一站都一樣：學一招 → 看範例 → 挑星星練習 ★", {
    x: M, y: 6.42, w: CW, h: 0.46, align: "left", valign: "middle",
    fontFace: type.kicker.fontFace, fontSize: type.kicker.fontSize, bold: true, color: color.ink.accent,
  });
  s.addNotes("先給地圖：讓學生知道整節課的結構，減少焦慮。三站的第一步都不同，但最後一步都是驗根——這句話今天要重複三次。");
})();

// =====================================================================
// S3 全課主線頁
// 改動：三張概念卡改用「淺色塊標頭 + 白卡身」；主張橫幅用 accent.strong
//       （白字 8.15:1），警示欄用暖砂色而非低對比灰。
// =====================================================================
(function () {
  const s = d.slide();
  d.title(s, "三種方程，同一個念頭", "全課主線");
  const boxes = [
    { lab: "分式方程", sub: "未知數在分母裡", segs: [{ n: "3", d: "x" }, { t: " = x - 2" }] },
    { lab: "無理方程", sub: "未知數在根號裡", txt: "√(x + 2) = x" },
    { lab: "方程組", sub: "被另一條方程綁住", txt: "y = x + 1\nx² + y² = 25" },
  ];
  const gap = space.md;
  const w = (CW - gap * 2) / 3;
  const top = 1.92, cardH = 2.04;
  boxes.forEach((b, i) => {
    const x = M + i * (w + gap);
    d.card(s, x, top, w, cardH);
    d.band(s, x, top, w, 0.60, color.accent.tint);
    s.addText(b.lab, {
      x, y: top, w, h: 0.60, align: "center", valign: "middle",
      fontFace: type.headline.fontFace, fontSize: 22, bold: true, color: color.ink.primary,
    });
    s.addText(b.sub, {
      x, y: top + 0.64, w, h: 0.40, align: "center", valign: "middle",
      fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, color: color.ink.secondary,
    });
    if (b.segs) d.fracRow(s, x + 0.90, top + 1.10, 0.78, b.segs, { fontSize: 21, fracFontSize: 17 });
    else s.addText(b.txt, {
      x: x + space.sm, y: top + 1.08, w: w - space.sm * 2, h: 0.82, align: "center", valign: "middle",
      fontFace: type.math.fontFace, fontSize: type.bodySm.fontSize, bold: true, color: color.ink.primary,
      lineSpacingMultiple: leading.tight,
    });
  });

  d.calloutBand(s, M, 4.26, CW, "做法都一樣：想辦法把未知數放出來，變回會解的一元二次方程", 0.95);

  d.cautionBox(s, M, 5.42, CW, 1.02, [
    { text: "但放出來有代價：", options: { fontFace: type.body.fontFace, fontSize: type.body.fontSize, bold: true, color: color.ink.caution } },
    { text: "去分母、平方，都可能多生出「假的解」。所以三站的最後一步都是——驗根。", options: { fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.ink.primary } },
  ]);
  s.addNotes("這一頁是全課的錨。三個方框只是「未知數被關在哪」的差別，做法同一個念頭。最後那句「放出來有代價」要講慢——它解釋了為什麼今天每題都要驗根，而不是老師囉嗦。");
})();

// =====================================================================
// S4 站別分隔頁
// =====================================================================
(function () {
  const s = d.slide({ dark: true });
  d.band(s, M, 2.02, 2.6, 1.08, color.accent.solid, radius.pill);
  s.addText("站①", {
    x: M, y: 2.02, w: 2.6, h: 1.08, align: "center", valign: "middle",
    fontFace: type.display.fontFace, fontSize: type.display.fontSize, bold: true,
    color: color.ink.onSolid, charSpacing: 1.0,
  });
  s.addText("分式方程", {
    x: M + 2.95, y: 2.02, w: CW - 2.95, h: 1.08, align: "left", valign: "middle",
    fontFace: type.display.fontFace, fontSize: type.display.fontSize, bold: true,
    color: color.ink.onDark, charSpacing: 1.2,
  });
  d.band(s, M, 3.62, CW, 1.28, color.surface.darkBand);
  const gs = type.headline.fontSize + 2; // 深底補償
  s.addText([
    { text: "目標：", options: { fontFace: type.headline.fontFace, fontSize: gs, bold: true, color: color.accent.decor, charSpacing: 0.8 } },
    { text: "把未知數從分母裡放出來，並且知道為什麼一定要驗根", options: { fontFace: type.headline.fontFace, fontSize: gs, color: color.ink.onDark, charSpacing: 0.8 } },
  ], { x: M + space.md, y: 3.62, w: CW - space.md * 2, h: 1.28, align: "left", valign: "middle" });
  s.addNotes("站①開始。先講目標，讓學生知道這一段要帶走什麼。");
})();

// =====================================================================
// S5 方法頁：左手順卡（D2 主設計）＋ 右範例
// 改動：兩欄改為等高對齊；手順卡標題帶白字對比由 2.85 → 5.87；
//       範例算式改用等寬字並讓等號成欄對齊。
// =====================================================================
(function () {
  const s = d.slide();
  d.title(s, "分式方程：四步做完", "站① 方法");
  // 25pt 之下「兩邊同乘公分母，去掉分母」佔兩行需 0.90"（守衛實測），
  // 故行高要 ≥0.90 → 卡高 4.62、內容上移至 1.80
  const top = 1.80, H = 4.62;
  const lw = 5.2, rw = CW - lw - space.lg;
  const rx = M + lw + space.lg;

  // 左：手順卡
  d.card(s, M, top, lw, H);
  const lBody = d.bandHeader(s, M, top, lw, "手順卡 · 照住做");
  const steps = ["找出最簡公分母", "兩邊同乘公分母，去掉分母", "解出這條整式方程", "把答案代回原方程驗根"];
  const rowH = (H - (lBody - top) - space.md) / steps.length;
  let ly = lBody + space.sm;
  steps.forEach((st, i) => {
    d.stepBadge(s, M + 0.26, ly + (rowH - 0.46) / 2, i + 1, 0.46);
    d.text(s, st, {
      x: M + 0.88, y: ly, w: lw - 1.14, h: rowH, align: "left", valign: "middle",
      fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.ink.primary,
      lineSpacingMultiple: leading.tight, _floor: type.bodySm.fontSize,
    });
    ly += rowH;
  });

  // 右：範例
  d.card(s, rx, top, rw, H);
  const rBody = d.bandHeader(s, rx, top, rw, "範例 · 一行一個等號");
  // 首行含分數 → 用原生疊字分數（鐵律 1：禁止 "3/x" 斜線寫法）
  const lines = [
    [{ segs: [{ n: "3", d: "x" }, { t: " = x - 2" }] }, "原方程"],
    ["3 = x(x - 2)", "兩邊乘 x"],
    ["x² - 2x - 3 = 0", "整理"],
    ["(x - 3)(x + 1) = 0", "因式分解"],
    ["x = 3　或　x = -1", "分兩支寫"],
    ["∴ x = 3 或 x = -1", "驗根後作答"],
  ];
  const eqRowH = (H - (rBody - top) - space.md) / lines.length;
  let ry = rBody + space.sm;
  lines.forEach(([expr, note]) => {
    if (typeof expr === "string") {
      s.addText(expr, {
        x: rx + space.sm, y: ry, w: rw * 0.62, h: eqRowH, align: "left", valign: "middle",
        margin: 0, wrap: false,
        fontFace: type.math.fontFace, fontSize: type.bodySm.fontSize, bold: true, color: color.ink.primary,
      });
    } else {
      d.fracRow(s, rx + space.sm, ry, eqRowH, expr.segs, { fontSize: type.bodySm.fontSize, fracFontSize: 18 });
    }
    // 步驟說明屬實質內容，須達 25pt 底線（原本 15pt 在 5 m 外只有 15.5 角分，讀不到）
    s.addText(note, {
      x: rx + rw * 0.64, y: ry, w: rw * 0.34, h: eqRowH, align: "left", valign: "middle",
      fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, color: color.ink.secondary,
    });
    ry += eqRowH;
  });
  s.addText("驗根：x = -1 代回原方程，分母不為 0，兩根都保留", {
    x: M, y: 6.44, w: CW, h: 0.40, align: "left", valign: "middle",
    fontFace: type.kicker.fontFace, fontSize: type.kicker.fontSize, bold: true, color: color.ink.accent,
  });
  s.addNotes("左邊手順卡逐字沿用講義，令簡報與講義同一套措辭。右邊範例示範書寫規範：一行一個等號、分兩支寫「或」、末行用「∴」。");
})();

// =====================================================================
// S6 CRA 三階頁
// =====================================================================
(function () {
  const s = d.slide();
  d.title(s, "為什麼會多出「假的解」", "站① 概念");
  // 三欄在 22pt 下每行僅容約 10 個中文字，必須自己控制斷行，
  // 否則「。」「，」會被推到行首（守衛會提示）
  d.craRow(s, M, 1.92, CW, 3.05, [
    { text: "3 個餅分給 x 個人。\n若 x = 0，\n這句話講不通。" },
    { text: "數線上把 x = 0\n挖走，變成空心點。" },
    { text: "x ≠ 0 是原方程\n自帶的限制。\n去分母後就消失了。" },
  ]);
  d.calloutBand(s, M, 5.20, CW, "去分母令方程「變寬」了：新方程的解，不一定是原方程的解", 0.92);
  s.addNotes("CRA 序：具體（分餅）→ 表徵（數線挖點）→ 抽象（x≠0 的限制）。抽象階仍保留前一階的視覺線索。");
})();

// =====================================================================
// S7 分層任務頁（★ 難度只用星星，不用顏色）
// 改動：舊版每項固定步進，遇上 3 行題目就疊字；
//       改為「題目區固定高」，超出即 build 時報錯。
// =====================================================================
(function () {
  const s = d.slide();
  d.title(s, "挑一個開始做", "站① 練習");
  // 分數一律走原生疊字（鐵律 1）；blocks 讓文字段落與分數行混排
  // 欄高 3.95：22pt 內文下，練習 A 需 2.55" 內容高（守衛實測），3.60 會壓穿框線
  d.tierColumns(s, M, 1.92, CW, 3.95, [
    {
      stars: "★☆☆", label: "練習 A", blocks: [
        { type: "text", text: "解：" },
        { type: "math", segs: [{ n: "2", d: "x" }, { t: " = 4" }] },
        { type: "text", text: "提示：先兩邊乘 x" },
      ],
    },
    {
      stars: "★★☆", label: "練習 B", blocks: [
        { type: "text", text: "解：" },
        { type: "math", segs: [{ n: "5", d: "x-1" }, { t: " = x + 1" }] },
        { type: "text", text: "記得驗根。" },
      ],
    },
    {
      stars: "★★★", label: "練習 C", blocks: [
        { type: "text", text: "設計一條分式方程，\n去分母後有兩個解，\n其中一個是增根。" },
      ],
    },
  ]);
  d.cautionBox(s, M, 6.02, CW, 0.72, "做完先自己核對：分母有沒有變成 0？有的話那個解要刪走。");
  s.addNotes("三層同頁呈現、學生自選，不由教師點名分派（減少標籤化）。C 層開放式，留空間給能力較強的學生。");
})();

// =====================================================================
// S8 圖表組件示範（方向 3）
// 內容取自「概率初步」單元——圖表在該處才是真正需要，不硬塞進本單元。
// 依 dataviz 規範：直接標值、文字穿文字色、色彩不單獨承載語意、細筆觸網格退居背景。
// =====================================================================
(function () {
  const s = d.slide();
  d.title(s, "抽 60 次的實驗結果", "圖表組件示範（概率初步）");
  d.card(s, M, 1.92, 8.1, 3.95);
  d.barChart(s, M + 0.55, 2.30, 7.0, 3.20, [
    { label: "紅球", value: 27, display: "27 次" },
    { label: "藍球", value: 21, display: "21 次" },
    { label: "黃球", value: 12, display: "12 次" },
  ]);
  d.statTile(s, M + 8.45, 1.92, CW - 8.45, 1.85, { value: "60", label: "總抽取次數", note: "每次抽完放回" });
  d.statTile(s, M + 8.45, 3.99, CW - 8.45, 1.88, { value: "0.45", label: "紅球的頻率", note: "27 ÷ 60" });
  s.addText("每根柱都直接標了次數 —— 就算印黑白、或看不清顏色，資料仍然讀得到", {
    x: M, y: 6.06, w: CW, h: 0.46, align: "left", valign: "middle",
    fontFace: type.kicker.fontFace, fontSize: type.kicker.fontSize, bold: true, color: color.ink.accent,
  });
  s.addNotes("圖表規範：類別上限 3（多過就合併「其他」）、每根柱直接標值、文字永不穿系列色。三個系列色已通過色盲安全驗證。");
})();

// =====================================================================
// S9 總結頁（帶走一句話 ＋ 保底版）
// =====================================================================
(function () {
  const s = d.slide();
  d.title(s, "今日帶走");
  d.calloutBand(s, M, 1.92, CW, "三種方程，同一個念頭：把未知數放出來，代價是可能生出假解", 1.05);

  const items = [
    ["站①", "分母裡 → 去分母 → 驗根"],
    ["站②", "根號裡 → 兩邊平方 → 驗根"],
    ["站③", "兩條方程 → 代入消元 → 回代"],
  ];
  let y = 3.22;
  items.forEach(([b, t]) => {
    d.card(s, M, y, CW, 0.82);
    d.stationBadge(s, b, M + 0.24, y + 0.10, 1.5, 0.62);
    s.addText(t, {
      x: M + 2.05, y, w: CW - 2.35, h: 0.82, align: "left", valign: "middle",
      fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.ink.primary,
    });
    y += 0.96;
  });

  d.band(s, M, 6.14, CW, 0.72, color.accent.tint);
  s.addText([
    { text: "保底版：", options: { fontFace: type.body.fontFace, fontSize: type.body.fontSize, bold: true, color: color.ink.accent } },
    { text: "解完之後，一定要把答案代回原本那條方程檢查一次。", options: { fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.ink.primary } },
  ], { x: M + space.md, y: 6.14, w: CW - space.md * 2, h: 0.72, align: "left", valign: "middle" });
  s.addNotes("帶走一句話＋保底版：保底版更具體、更操作性，是融合生至少要能說出的版本。");
})();

// =====================================================================
d.save("簡報_美化試驗_單元04.pptx").then((r) => {
  console.log(`\n✓ 已產出 ${r.file}（${r.slides} 頁）`);
  console.log(r.issues.length ? `⚠ 版面問題 ${r.issues.length} 項` : "✓ 版面守衛：無問題");
  const a = T.audit({ print: false, strict: true });
  console.log(`✓ Token 自檢：${a.rows.length} 項全過`);
});
