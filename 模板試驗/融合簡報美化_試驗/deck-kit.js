// =====================================================================
// 融合班教學簡報・組件層（試驗版 v1）
// ---------------------------------------------------------------------
// 規矩：本檔與 build script 只准引用 deck-tokens 的 semantic / component 層，
//       不得出現 raw hex、raw 字級。
//
// 本層要解決的，是工作筆記反覆記錄的三類問題：
//   ① 每份 build_deck.js 各自複製一套 C/card/title/frac → 9 份簡報風格逐漸飄移
//   ② 文字長度推走後續元素 → 「分層任務頁 C 欄疊字」「底部提示壓穿卡片框線」
//      （舊做法靠 QA 肉眼捉；這裡改成 build 時就丟錯）
//   ③ §D 硬規則（≤5 行×18 字、內文 ≥20pt）從來只靠人手抽查
//
// ⚠ 試驗中，未併入 skill。
// =====================================================================
const pptxgen = require("pptxgenjs");
const T = require("./deck-tokens");
const { color, type, comp, layout, leading, darkAdjust, space, radius, RULES } = T;

// =====================================================================
// 文字度量：pptxgenjs 無法量測文字，用字寬啟發式估算
// 中日韓字元約 1.0 em，ASCII 約 0.5 em；等寬字型另計。
// =====================================================================
const CJK = /[　-鿿＀-￯]/;
function charEm(ch, mono) {
  if (mono) return 0.6;
  return CJK.test(ch) ? 1.0 : 0.52;
}
// charSpacing 必須計入 —— 抗光暈用的字距會實質加闊文字，
// 漏算會令估算器以為放得下、實際卻換行溢出（實測：27 字 × 0.8pt ≈ 多 0.3"）
function textWidthIn(text, fontSize, mono, charSpacing = 0) {
  let em = 0, n = 0;
  for (const ch of String(text)) { em += charEm(ch, mono); n++; }
  return em * (fontSize / 72) + n * (charSpacing / 72);
}
// pptxgenjs 文字框左右預設各有約 0.1" 內距
const BOX_INSET = 0.22;
function estimateLines(text, widthIn, fontSize, mono, charSpacing = 0) {
  const usable = widthIn - BOX_INSET;
  let lines = 0;
  for (const para of String(text).split("\n")) {
    if (!para) { lines += 1; continue; }
    lines += Math.max(1, Math.ceil(textWidthIn(para, fontSize, mono, charSpacing) / usable));
  }
  return lines;
}
function maxCJKCharsPerLine(widthIn, fontSize) {
  return Math.floor((widthIn - 0.16) / (fontSize / 72));
}

// =====================================================================
// 鐵律 1 守衛：數學式必須原生，禁止用 "/" 斜線硬湊分數
// 捉「數字或變數 / 數字或變數或左括號」這種寫法，例如 3/x、5/(x-1)、2/3
// 例外：日期、比值文字（如「27 ÷ 60」用除號不受影響）
// =====================================================================
const SLASH_FRACTION = /[0-9A-Za-z\)]\s*\/\s*[0-9A-Za-z\(]/;
function findSlashFraction(text) {
  const m = SLASH_FRACTION.exec(String(text));
  return m ? m[0] : null;
}

// =====================================================================
// Deck：包住 pptxgen，注入 token 預設值 + 版面守衛
// =====================================================================
class Deck {
  constructor({ title, author, footerText, strict = true } = {}) {
    this.p = new pptxgen();
    this.p.layout = "LAYOUT_WIDE";
    this.p.title = title || "";
    this.p.author = author || "";
    this.footerText = footerText || "";
    this.strict = strict;      // true = 版面違規直接丟錯
    this.n = 0;                // 頁碼
    this.issues = [];          // 非 strict 模式下累積問題
    this.advisories = [];      // 建議級提示（不中斷 build）
    T.audit({ print: false, strict: true }); // token 層先自檢，不過就不准開工
  }

  _flag(msg) {
    const line = `第 ${this.n} 頁：${msg}`;
    this.issues.push(line);
    if (this.strict) throw new Error(`[版面守衛] ${line}`);
    else console.warn(`[版面守衛] ${line}`);
  }

  // 建議級：不中斷 build，但一定要讓人看見
  _advise(msg) {
    const line = `第 ${this.n} 頁：${msg}`;
    this.advisories.push(line);
    console.warn(`[版面建議] ${line}`);
  }

  // ---- 新頁 ----
  slide({ dark = false, noFooter = false } = {}) {
    const s = this.p.addSlide();
    s.background = { color: dark ? color.surface.dark : color.surface.page };
    this.n += 1;
    s._dark = dark;
    s._deck = this;
    s._textLines = 0; // 累計內文行數，用於 §D「每頁 ≤5 行」檢查
    if (!noFooter) this.footer(s);
    return s;
  }

  // =====================================================================
  // 核心：受守衛的文字。放不下就先降級（但不得低於 §D 下限），
  // 到下限仍放不下 → 丟錯，逼使用者刪內容而不是縮字。
  // 這正是「內文 ≥20pt」硬規則能真正守住的關鍵。
  // =====================================================================
  text(s, txt, opts) {
    const o = Object.assign({}, opts);
    const mono = o.fontFace === T.font.mono;
    // 鐵律 1：數學式必須原生。斜線分數在此攔截，逼使用 frac()/fracRow()。
    const slash = findSlashFraction(txt);
    if (slash && !o.allowSlash) {
      this._flag(`偵測到斜線分數「${slash}」——鐵律 1 要求原生分數，請改用 frac()／fracRow()`);
    }
    const isBody = o._role === "body";
    // 底線＝§D 20pt 與投影情境要求取其大（見 RULES.projection）
    const floor = isBody ? RULES.floorBodyPt : (o._floor || 0);
    const lead = o.lineSpacingMultiple || leading.normal;
    let fs = o.fontSize;

    const cs = o.charSpacing || 0;
    // ⚠ 曾寫成 `!o.wrap === false`，JS 解讀為 `(!o.wrap) === false`，
    //   undefined 時恆為 false ——整段適配邏輯變死 code。必須是 `o.wrap !== false`。
    if (o.w && o.h && o.wrap !== false) {
      let lines = estimateLines(txt, o.w, fs, mono, cs);
      let needed = lines * (fs / 72) * lead;
      while (needed > o.h && fs - 1 >= floor && floor > 0) {
        fs -= 1;
        lines = estimateLines(txt, o.w, fs, mono, cs);
        needed = lines * (fs / 72) * lead;
      }
      if (needed > o.h) {
        this._flag(
          `文字放不下（需 ${needed.toFixed(2)}" > 框高 ${o.h.toFixed(2)}"，` +
          `字級已到下限 ${fs}pt）。請刪減內容，不要再縮字：「${String(txt).slice(0, 24)}…」`
        );
      }
      // 窄欄警告：PowerPoint 不做中文禁則處理，欄寬不足時
      // 「。」「，」「）」會被推到行首、或單字獨佔一行（實測 CRA 欄與練習欄都中招）。
      // 少於 10 個中文字位就該用明確 \n 自己控制斷行。
      const perLine = maxCJKCharsPerLine(o.w, fs);
      if (perLine < 10 && lines > 1 && !String(txt).includes("\n")) {
        this._advise(
          `欄寬僅容 ${perLine} 個中文字（${o.w.toFixed(2)}" @ ${fs}pt），自動換行會令標點孤行。` +
          `請改用明確斷行：「${String(txt).slice(0, 16)}…」`
        );
      }
      o.fontSize = fs;
      if (isBody) s._textLines += lines;
    }
    s.addText(txt, o);
    return o.fontSize;
  }

  // §D：每頁內文 ≤5 行、每行 ≤18 中文字
  checkTextBudget(s) {
    if (s._textLines > RULES.maxLinesPerSlide) {
      this._flag(`內文 ${s._textLines} 行，超出 §D 上限 ${RULES.maxLinesPerSlide} 行 — 應拆頁`);
    }
  }

  // =====================================================================
  // 深底文字：微灰白 ＋ 加大 2pt ＋ 加字距（抗 halation）
  // 亮面板上淺色字會向外暈開；中文筆畫密，遠距離筆劃會黏在一起。
  // 所有落在 surface.dark / accent.solid / accent.strong 上的文字都應走這裡。
  // =====================================================================
  darkText(s, txt, opts = {}) {
    const o = Object.assign({}, opts);
    o.fontSize = (o.fontSize || type.body.fontSize) + darkAdjust.plusPt;
    o.charSpacing = o.charSpacing !== undefined ? o.charSpacing : darkAdjust.charSpacing;
    o.color = o.color || color.ink.onDark;
    o.fontFace = o.fontFace || type.body.fontFace;
    if (!o.lineSpacingMultiple) o.lineSpacingMultiple = darkAdjust.leading;
    s.addText(txt, o);
    return o.fontSize;
  }

  // ---- 頁尾 ----
  footer(s) {
    const ink = s._dark ? comp.footer.inkOnDark : comp.footer.ink;
    s.addText(this.footerText, {
      x: layout.marginX, y: layout.footerY, w: 10.5, h: 0.32,
      align: "left", valign: "middle",
      fontFace: type.caption.fontFace, fontSize: type.caption.fontSize, color: ink,
    });
    s.addText(String(this.n), {
      x: layout.W - layout.marginX - 0.9, y: layout.footerY, w: 0.9, h: 0.32,
      align: "right", valign: "middle",
      fontFace: type.caption.fontFace, fontSize: type.caption.fontSize, color: ink,
    });
  }

  // ---- 頁標題（可帶 kicker）----
  title(s, txt, kicker) {
    if (kicker) {
      s.addText(kicker, {
        x: layout.marginX, y: layout.kickerY, w: layout.contentW, h: 0.4,
        fontFace: type.kicker.fontFace, fontSize: type.kicker.fontSize, bold: true,
        color: color.ink.accent, align: "left",
      });
      s.addText(txt, {
        x: layout.marginX, y: layout.titleWithKickerY, w: layout.contentW, h: 0.8,
        fontFace: type.title.fontFace, fontSize: type.title.fontSize, bold: true,
        color: s._dark ? color.ink.onDark : color.ink.primary, align: "left",
        charSpacing: s._dark ? darkAdjust.charSpacing : 0,
      });
    } else {
      s.addText(txt, {
        x: layout.marginX, y: layout.titleY, w: layout.contentW, h: 0.9,
        fontFace: type.title.fontFace, fontSize: type.title.fontSize, bold: true,
        color: s._dark ? color.ink.onDark : color.ink.primary, align: "left",
        charSpacing: s._dark ? darkAdjust.charSpacing : 0,
      });
    }
  }

  // =====================================================================
  // 基礎形狀
  // =====================================================================
  card(s, x, y, w, h, { raised = false, fill, line } = {}) {
    const c = raised ? comp.cardRaised : comp.card;
    s.addShape(this.p.ShapeType.roundRect, {
      x, y, w, h, rectRadius: c.radius,
      fill: { color: fill || c.fill },
      line: { color: line || c.line, width: c.lineWidth },
      shadow: c.shadow,
    });
  }

  band(s, x, y, w, h, fillColor, r) {
    s.addShape(this.p.ShapeType.roundRect, {
      x, y, w, h, rectRadius: r === undefined ? radius.md : r,
      fill: { color: fillColor }, line: { type: "none" },
    });
  }

  // 卡片頂部標題帶（承白字，用 accent.solid 5.87:1）
  bandHeader(s, x, y, w, label) {
    const c = comp.bandHeader;
    this.band(s, x, y, w, c.h, c.fill);
    s.addText(label, {
      x, y, w, h: c.h, align: "center", valign: "middle",
      fontFace: type.headline.fontFace, fontSize: type.bodySm.fontSize, bold: true,
      color: c.ink, charSpacing: darkAdjust.charSpacing, // 反白字加字距抗光暈
    });
    return y + c.h;
  }

  // 步驟圓圈（accent.strong 8.15:1）
  stepBadge(s, x, y, n, dia) {
    const d = dia || comp.stepBadge.dia;
    s.addShape(this.p.ShapeType.ellipse, {
      x, y, w: d, h: d, fill: { color: comp.stepBadge.fill }, line: { type: "none" },
    });
    s.addText(String(n), {
      x, y, w: d, h: d, align: "center", valign: "middle",
      fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, bold: true,
      color: comp.stepBadge.ink,
    });
  }

  // 站別膠囊徽章
  stationBadge(s, label, x, y, w, h) {
    const c = comp.stationBadge;
    const ww = w || c.w, hh = h || c.h;
    s.addShape(this.p.ShapeType.roundRect, {
      x, y, w: ww, h: hh, rectRadius: Math.min(radius.pill, hh / 2),
      fill: { color: c.fill }, line: { type: "none" },
    });
    s.addText(label, {
      x, y, w: ww, h: hh, align: "center", valign: "middle",
      fontFace: type.headline.fontFace, fontSize: type.headline.fontSize, bold: true,
      color: c.ink, charSpacing: darkAdjust.charSpacing,
    });
  }

  // 主張橫幅（整堂課的錨句）
  calloutBand(s, x, y, w, txt, h) {
    const c = comp.calloutBand;
    const hh = h || c.h;
    this.band(s, x, y, w, hh, c.fill);
    this.text(s, txt, {
      x: x + space.md, y, w: w - space.md * 2, h: hh, align: "left", valign: "middle",
      fontFace: type.headline.fontFace, fontSize: type.headline.fontSize, bold: true,
      color: c.ink, charSpacing: darkAdjust.charSpacing, _floor: type.bodySm.fontSize,
    });
    return y + hh;
  }

  // 警示／易錯欄（暖砂色，非紅色 —— §D 不以紅綠傳語意）
  cautionBox(s, x, y, w, h, richOrText) {
    const c = comp.cautionBox;
    s.addShape(this.p.ShapeType.roundRect, {
      x, y, w, h, rectRadius: c.radius,
      fill: { color: c.fill }, line: { color: c.line, width: c.lineWidth },
    });
    if (Array.isArray(richOrText)) {
      s.addText(richOrText, { x: x + space.md, y, w: w - space.md * 2, h, align: "left", valign: "middle" });
    } else {
      this.text(s, richOrText, {
        x: x + space.md, y, w: w - space.md * 2, h, align: "left", valign: "middle",
        fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.ink.primary,
        _floor: type.bodySm.fontSize,
      });
    }
    return y + h;
  }

  // =====================================================================
  // 分層任務欄（★ 難度只用星星，§D：不用顏色區分層次）
  // 舊版 bug：每項固定步進遇上 3 行題目就疊字。這裡改「題目區固定高」，
  // 題目放不下即由 text() 丟錯，不會靜靜推走後面元素。
  // =====================================================================
  tierColumns(s, x, y, w, h, tiers) {
    const gap = space.md;
    const cw = (w - gap * (tiers.length - 1)) / tiers.length;
    const headH = 0.86;
    tiers.forEach((t, i) => {
      const cx = x + i * (cw + gap);
      this.card(s, cx, y, cw, h);
      this.band(s, cx, y, cw, headH, comp.tierColumn.headFill);
      s.addText(t.stars, {
        x: cx, y: y + 0.06, w: cw, h: 0.42, align: "center", valign: "middle",
        fontFace: type.headline.fontFace, fontSize: 24, bold: true, color: comp.tierColumn.headInk,
      });
      s.addText(t.label, {
        x: cx, y: y + 0.46, w: cw, h: 0.36, align: "center", valign: "middle",
        fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, bold: true,
        color: color.ink.secondary,
      });
      // 題目區：固定高，不讓內容長度推走版面
      const bx = cx + space.sm, bw = cw - space.sm * 2;
      const bodyTop = y + headH + space.md, bodyH = h - headH - space.md * 2;
      if (t.blocks) {
        // 混排：文字段落 + 原生分數行（鐵律 1）
        let by = bodyTop;
        const lineH = (type.body.fontSize / 72) * leading.loose;
        t.blocks.forEach((b) => {
          if (b.type === "math") {
            this.fracRow(s, bx, by, lineH * 1.6, b.segs, { fontSize: type.bodySm.fontSize, fracFontSize: 17 });
            by += lineH * 1.7;
          } else {
            const lines = estimateLines(b.text, bw, type.body.fontSize, false, 0);
            const hh = lines * lineH;
            this.text(s, b.text, {
              x: bx, y: by, w: bw, h: hh, align: "left", valign: "top",
              fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.ink.primary,
              lineSpacingMultiple: leading.normal, _floor: type.bodySm.fontSize,
            });
            by += hh + (b.gap || 0.10);
          }
        });
        if (by > bodyTop + bodyH) {
          this._flag(`分層任務欄「${t.label}」內容高 ${(by - bodyTop).toFixed(2)}" 超出欄高 ${bodyH.toFixed(2)}" — 會壓穿卡片框線，請刪減`);
        }
      } else {
        this.text(s, t.body, {
          x: bx, y: bodyTop, w: bw, h: bodyH, align: "left", valign: "top",
          fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.ink.primary,
          lineSpacingMultiple: leading.normal, _role: "body",
        });
      }
    });
  }

  // CRA 三階（具體｜表徵｜抽象）
  craRow(s, x, y, w, h, stages) {
    const gap = space.md;
    const cw = (w - gap * 2) / 3;
    ["具體", "表徵", "抽象"].forEach((name, i) => {
      const cx = x + i * (cw + gap);
      this.card(s, cx, y, cw, h);
      this.bandHeader(s, cx, y, cw, name);
      const st = stages[i] || {};
      if (st.render) st.render(cx, y + comp.bandHeader.h, cw, h - comp.bandHeader.h);
      // §D：內文左對齊（置中會令末行孤字掉隊，讀寫障礙學生尤其難讀）
      // 水平內距用 sm 不用 md：26pt 之下三欄每行僅約 9 個中文字，要盡量省回欄寬
      else this.text(s, st.text || "", {
        x: cx + space.sm, y: y + comp.bandHeader.h + space.md, w: cw - space.sm * 2,
        h: h - comp.bandHeader.h - space.md * 2, align: "left", valign: "top",
        fontFace: type.body.fontFace, fontSize: type.body.fontSize, color: color.ink.primary,
        lineSpacingMultiple: leading.normal, _floor: type.bodySm.fontSize,
      });
    });
  }

  // =====================================================================
  // 原生分數（分子／橫線／分母直式疊字）—— 鐵律1：數學式必須原生
  // margin:0 + wrap:false 缺一不可（實測踩過：預設內邊距會令長分子換行散開）
  // =====================================================================
  // +0.22：分數線需比分子／分母略長，但過寬會令「分數 = 右式」之間出現大空隙
  fracWidth(num, den, fs) {
    return Math.max(String(num).length, String(den).length) * (fs * 0.62 / 72) + 0.22;
  }
  frac(s, cx, cy, num, den, size, col) {
    const fs = size || type.body.fontSize;
    const w = this.fracWidth(num, den, fs);
    const hh = fs / 72 * 1.35; // 太緊會令文字溢出蓋到鄰行
    const c = col || color.ink.primary;
    s.addText(String(num), {
      x: cx - w / 2, y: cy - hh - 0.04, w, h: hh, margin: 0, wrap: false,
      align: "center", valign: "bottom", fontFace: type.math.fontFace, fontSize: fs, bold: true, color: c,
    });
    this.seg(s, cx - w / 2 + 0.08, cy, cx + w / 2 - 0.08, cy, { color: c, width: 1.5 });
    s.addText(String(den), {
      x: cx - w / 2, y: cy + 0.04, w, h: hh, margin: 0, wrap: false,
      align: "center", valign: "top", fontFace: type.math.fontFace, fontSize: fs, bold: true, color: c,
    });
    return w;
  }
  // 一行內「文字／分數」混排：segs = [{t:"文字"}] 或 [{n:分子, d:分母}]
  fracRow(s, x, y, h, segs, o = {}) {
    const fs = o.fontSize || type.body.fontSize;
    const ff = o.fontFace || type.math.fontFace;
    const bold = o.bold !== false;
    const col = o.color || color.ink.primary;
    const ffs = o.fracFontSize || fs;
    const cw = fs * (ff === type.math.fontFace ? 0.62 : 1.05) / 72;
    const cy = y + h / 2;
    const pad = o.textPad !== undefined ? o.textPad : 0.25;
    let cx = x;
    segs.forEach((sg) => {
      if (sg.t !== undefined) {
        const tw = sg.t.length * cw + 0.04;
        s.addText(sg.t, {
          x: cx, y, w: tw + pad, h, margin: 0, wrap: false, align: "left", valign: "middle",
          fontFace: ff, fontSize: fs, bold, color: sg.color || col,
        });
        cx += tw;
      } else {
        const w = this.fracWidth(sg.n, sg.d, ffs);
        this.frac(s, cx + w / 2, cy, sg.n, sg.d, sg.size || ffs, sg.color || col);
        cx += w + 0.03;
      }
    });
    return cx;
  }
  seg(s, x1, y1, x2, y2, o = {}) {
    const x = Math.min(x1, x2), y = Math.min(y1, y2);
    const w = Math.abs(x2 - x1) || 0.01, h = Math.abs(y2 - y1) || 0.01;
    s.addShape(this.p.ShapeType.line, {
      x, y, w, h,
      line: { color: o.color || color.ink.primary, width: o.width || 1.5 },
      flipV: (x2 - x1) * (y2 - y1) < 0,
    });
  }

  // =====================================================================
  // 圖表（方向 3）—— 依 dataviz 規範手繪，不用 pptx 內建圖表
  //   · 細筆觸、資料端 4px 圓角、相鄰填色留 2px 表面間隙
  //   · 文字永遠穿文字色，不穿系列色
  //   · 直接標籤：色彩永不單獨承載語意
  //   · 網格線退居背景
  // =====================================================================
  barChart(s, x, y, w, h, data, o = {}) {
    const c = comp.chart;
    if (data.length > c.maxSeries && !o.allowExtended) {
      this._flag(`長條圖 ${data.length} 類，超過建議上限 ${c.maxSeries} — 應合併「其他」或改小倍數圖`);
    }
    const pal = o.allowExtended ? c.seriesExtended : c.series;
    const max = o.max || Math.max(...data.map((d) => d.value));
    const labelH = 0.42;          // 底部類別標籤
    const plotH = h - labelH;
    const gap = space.md;
    const bw = (w - gap * (data.length - 1)) / data.length;

    // 基線
    this.seg(s, x, y + plotH, x + w, y + plotH, { color: c.axis, width: 1 });

    data.forEach((d, i) => {
      const bx = x + i * (bw + gap);
      const bh = Math.max(0.06, (d.value / max) * (plotH - 0.5));
      const by = y + plotH - bh;
      s.addShape(this.p.ShapeType.roundRect, {
        x: bx, y: by, w: bw, h: bh, rectRadius: c.barRadius,
        fill: { color: d.color || pal[i % pal.length] }, line: { type: "none" },
      });
      // 直接標值（文字色，非系列色）
      s.addText(d.display || String(d.value), {
        x: bx, y: by - 0.44, w: bw, h: 0.4, align: "center", valign: "bottom",
        fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, bold: true, color: c.value,
      });
      // 類別標籤
      s.addText(d.label, {
        x: bx, y: y + plotH + 0.06, w: bw, h: labelH, align: "center", valign: "top",
        fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, color: c.label,
      });
    });
  }

  // 大數字磚（dataviz：有時答案不是圖，是一個數）
  statTile(s, x, y, w, h, { value, label, note }) {
    this.card(s, x, y, w, h);
    s.addText(value, {
      x, y: y + 0.12, w, h: h * 0.5, align: "center", valign: "middle",
      fontFace: type.display.fontFace, fontSize: type.display.fontSize, bold: true,
      color: color.ink.primary,
    });
    s.addText(label, {
      x, y: y + h * 0.55, w, h: 0.4, align: "center", valign: "middle",
      fontFace: type.bodySm.fontFace, fontSize: type.bodySm.fontSize, bold: true,
      color: color.ink.secondary,
    });
    if (note) s.addText(note, {
      x, y: y + h * 0.55 + 0.36, w, h: 0.36, align: "center", valign: "middle",
      fontFace: type.caption.fontFace, fontSize: type.caption.fontSize, color: color.ink.muted,
    });
  }

  // ---- 輸出 ----
  async save(file) {
    if (this.issues.length) {
      console.warn(`\n[版面守衛] 累積 ${this.issues.length} 項問題：`);
      this.issues.forEach((i) => console.warn("  · " + i));
    }
    if (this.advisories.length) {
      console.warn(`\n[版面建議] ${this.advisories.length} 項：`);
      this.advisories.forEach((i) => console.warn("  · " + i));
    }
    await this.p.writeFile({ fileName: file });
    return { file, slides: this.n, issues: this.issues };
  }
}

module.exports = { Deck, estimateLines, textWidthIn, maxCJKCharsPerLine, findSlashFraction, T };
