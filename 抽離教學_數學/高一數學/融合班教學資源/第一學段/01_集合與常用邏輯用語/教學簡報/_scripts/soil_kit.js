// soil_kit.js — 融合班 SOIL 教學 deck 共用工具（Sage Calm 低刺激版）
// 硬規則：微軟正黑體、內文≥20pt、標題≥32pt、每頁≤5行×18字、左對齊、難度只用星星、
//         淺底非純白、無斜體底線、色盲安全（唔靠紅綠）、CRA 序、步驟編號、可預測版型。
//
// 數學符號注意（2026-07-19 實測）：微軟正黑體本身無 ⊆⊊∅∈∉∁∀∃⇒⇔ 等符號，
// 靠 Windows 自動 fallback（Segoe UI Symbol）顯示，正常。但 Unicode 下標字元
// （如 ᵤ）三大字型皆無 → 一定出豆腐。故下標一律用 `_{...}` 標記走真排版下標。
//   例：'∁_{U}A' → ∁ 下標U A ；'2^{n}' → 2 上標n
const pptxgen = require('pptxgenjs');

const C = {
  DARK:  '34493F', LIGHT: 'F1F4F1', INK:   '202A26', HEAD:  '2E4A40',
  BLOCK: 'DCE6DF', EDGE:  'C4D3C8', ACCENT:'5E8574', WHITE: 'FFFFFF',
  MUTED: '6B7A72',   // 頁尾（非關鍵資訊）
  MUTED2:'4E5C55',   // 卡內註解（要夠對比：失讀症友善）
  STAR:  '46564E',
  OKBG:  'DDE7DF', OK:'35604D',    // ✓ 配「啱」字，唔淨靠色
  BADBG: 'ECE0DB', BAD:'8C5748',   // ✗ 配「錯」字，唔淨靠色
};
const F = 'Microsoft JhengHei';
const XL = 12.1, MX = 0.6;

// ── `_{}` / `^{}` 標記 → pptxgenjs run 陣列（同時處理 \n 換行）──────────
function rt(s, base = {}) {
  if (typeof s !== 'string') return s;
  const out = [];
  const lns = s.split('\n');
  lns.forEach((line, li) => {
    const re = /([_^])\{([^}]*)\}/g;
    let last = 0, m; const segs = [];
    while ((m = re.exec(line))) {
      if (m.index > last) segs.push({ text: line.slice(last, m.index), o: {} });
      segs.push({ text: m[2], o: { [m[1] === '_' ? 'subscript' : 'superscript']: true } });
      last = re.lastIndex;
    }
    if (last < line.length) segs.push({ text: line.slice(last), o: {} });
    if (!segs.length) segs.push({ text: '', o: {} });
    segs.forEach((sg, i) => out.push({
      text: sg.text,
      options: { ...base, ...sg.o, ...(i === segs.length - 1 && li < lns.length - 1 ? { breakLine: true } : {}) },
    }));
  });
  return out;
}
// 多行（每個字串一行）→ run 陣列
function rtLines(arr, base = {}) {
  const out = [];
  arr.forEach((l, i) => {
    const r = rt(l, base);
    if (i < arr.length - 1) r[r.length - 1].options.breakLine = true;
    out.push(...r);
  });
  return out;
}

class Deck {
  // course 預設「高一數學」＝原有行為；其他年級（如初三）傳入覆蓋
  constructor(footerLabel, course = '高一數學'){ this.p = new pptxgen(); this.p.layout = 'LAYOUT_WIDE'; this.foot = footerLabel; this.course = course; this.n = 0; }
  save(fileName){ return this.p.writeFile({ fileName }); }

  _content(){ const s = this.p.addSlide(); s.background = { color: C.LIGHT }; this.n++; this._footer(s); return s; }
  _dark(){ const s = this.p.addSlide(); s.background = { color: C.DARK }; this.n++; return s; }
  _footer(s){
    s.addText(`${this.course} · ${this.foot}`, { x:MX, y:7.04, w:9, h:0.3, fontFace:F, fontSize:11, color:C.MUTED, align:'left', margin:0, valign:'middle' });
    s.addText(String(this.n), { x:12.3, y:7.04, w:0.5, h:0.3, fontFace:F, fontSize:11, color:C.MUTED, align:'right', margin:0, valign:'middle' });
  }
  _title(s, t, star){
    s.addShape('ellipse', { x:MX, y:0.52, w:0.30, h:0.30, fill:{ color:C.ACCENT } });
    s.addText([...rt(t, { bold:true, color:C.HEAD }), ...(star?[{ text:'  ★', options:{ color:C.STAR, bold:true } }]:[])],
      { x:1.02, y:0.38, w:XL-0.4, h:0.62, fontFace:F, fontSize:32, align:'left', valign:'middle', margin:0 });
  }
  _badge(s, text){
    s.addShape('roundRect', { x:7.7, y:6.42, w:5.0, h:0.5, rectRadius:0.1, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
    s.addText('▶ 轉換點：'+text, { x:7.7, y:6.42, w:5.0, h:0.5, fontFace:F, fontSize:15, bold:true, color:C.HEAD, align:'center', valign:'middle', margin:0 });
  }

  cover({ title, subtitle, hook }){
    const s = this._dark();
    s.addText('{ }', { x:7.5, y:0.6, w:5.6, h:6.3, fontFace:F, fontSize:180, color:'3E5349', align:'center', valign:'middle', margin:0, wrap:false });
    s.addText(rt(title, { bold:true, color:C.WHITE }), { x:MX, y:2.3, w:8.2, h:1.9, fontFace:F, fontSize:44, align:'left', valign:'middle', margin:0 });
    s.addText(subtitle, { x:MX, y:4.25, w:8.2, h:0.6, fontFace:F, fontSize:22, color:'C9D6CE', align:'left', margin:0 });
    if(hook) s.addText(rt(hook, { color:'9DBAA9' }), { x:MX, y:5.15, w:8.2, h:0.7, fontFace:F, fontSize:20, align:'left', margin:0 });
    return this;
  }

  // val 可以係純文字（rt() 標記照舊，可以摺行）或 { eq:[...] }（drawEq 語法，
  // 畫真分數／根號，單行唔摺行——內容長度要控制喺一行內）。
  _textOrEq(s, val, x, y, w, h, opts = {}) {
    if (val && typeof val === 'object' && val.eq) {
      drawEq(val.eq, { size: opts.size, color: opts.color, align: opts.align || 'left' })(s, x, y, w, h);
    } else {
      s.addText(rt(val, { bold: opts.bold, color: opts.color }),
        { x, y, w, h, fontFace: F, fontSize: opts.size, align: opts.align || 'left', valign: opts.valign || 'middle',
          margin: 0, lineSpacingMultiple: opts.lineSpacingMultiple });
    }
  }

  agenda({ title='今日課堂流程', steps, note }){
    const s = this._content(); this._title(s, title);
    const y0 = 1.65, h = 0.86, gap = 0.16;
    steps.forEach((st, i) => {
      const y = y0 + i*(h+gap);
      s.addShape('ellipse', { x:MX, y:y, w:h, h:h, fill:{ color:C.ACCENT } });
      s.addText(String(i+1), { x:MX, y:y, w:h, h:h, fontFace:F, fontSize:30, bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
      s.addShape('roundRect', { x:MX+h+0.25, y:y, w:XL-h-0.25, h:h, rectRadius:0.08, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
      this._textOrEq(s, st, MX+h+0.55, y, XL-h-0.85, h, { bold:true, color:C.HEAD, size:23 });
    });
    if(note) s.addText(rt(note, { color:C.MUTED2 }), { x:MX, y:6.5, w:XL, h:0.5, fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0 });
    return this;
  }

  // ⚠ sub 最多兩行（區高 0.9"＠23pt）；第三行會被灰框切底，而且唔會超出頁面、機檢捉唔到。
  problem({ title='先想一想', question, sub, caption, star, badge }){
    const s = this._content(); this._title(s, title, star);
    s.addShape('roundRect', { x:MX, y:1.9, w:XL, h:2.4, rectRadius:0.1, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
    this._textOrEq(s, question, MX+0.4, 2.15, XL-0.8, 1.1, { bold:true, color:C.HEAD, size:30 });
    if(sub) this._textOrEq(s, sub, MX+0.4, 3.25, XL-0.8, 0.9, { color:C.INK, size:23, valign:'top' });
    if(caption) this._textOrEq(s, caption, MX, 4.7, XL, 0.9, { bold:true, color:C.HEAD, size:22 });
    if(badge) this._badge(s, badge);
    return this;
  }

  cra({ title, concrete, rep, abstract, takeaway, star }){
    const s = this._content(); this._title(s, title, star);
    const cw = 3.83, gap = 0.30, y = 1.6, ph = 4.35;
    const xs = [MX, MX+cw+gap, MX+2*(cw+gap)];
    [{ head:'具體', ...concrete }, { head:'表徵', ...rep }, { head:'抽象', ...abstract }].forEach((pn, i) => {
      const x = xs[i];
      s.addShape('roundRect', { x, y, w:cw, h:ph, rectRadius:0.08, fill:{ color:C.WHITE }, line:{ color:C.EDGE, width:1 } });
      s.addShape('roundRect', { x, y, w:cw, h:0.62, rectRadius:0.08, fill:{ color:C.ACCENT } });
      s.addText(pn.head, { x, y, w:cw, h:0.62, fontFace:F, fontSize:22, bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
      const hasArt = pn.image || pn.draw;
      if(pn.image) s.addImage({ path:pn.image, x:x+0.35, y:y+0.9, w:cw-0.7, h:2.5, sizing:{ type:'contain', w:cw-0.7, h:2.5 } });
      if(pn.draw)  pn.draw(s, x+0.15, y+0.78, cw-0.3, 2.65);
      if(pn.text)  s.addText(rt(pn.text, { color:C.INK }), { x:x+0.28, y: hasArt ? y+3.52 : y+0.9, w:cw-0.56, h: hasArt ? 0.7 : 3.2, fontFace:F, fontSize:21, align: hasArt?'center':'left', valign: hasArt?'middle':'middle', margin:0 });
    });
    if(takeaway) s.addText(rt('↓ '+takeaway, { bold:true, color:C.HEAD }), { x:MX, y:6.15, w:XL, h:0.7, fontFace:F, fontSize:21, align:'center', valign:'middle', margin:0 });
    return this;
  }

  rows3({ title, rows, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const y0 = 1.6, h = 1.5, gap = 0.24;
    rows.forEach((r, i) => {
      const y = y0 + i*(h+gap);
      s.addShape('roundRect', { x:MX, y:y, w:XL, h:h, rectRadius:0.08, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
      s.addShape('ellipse', { x:MX+0.3, y:y+0.35, w:0.8, h:0.8, fill:{ color:C.ACCENT } });
      s.addText(r.icon || r.term.slice(0,1), { x:MX+0.3, y:y+0.35, w:0.8, h:0.8, fontFace:F, fontSize:28, bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
      s.addText([...rt(r.term+'　', { bold:true, color:C.HEAD, fontSize:24 }), ...rt(r.desc, { color:C.INK, fontSize:22 })],
        { x:MX+1.35, y:y+0.18, w:XL-1.6, h:0.7, fontFace:F, align:'left', valign:'middle', margin:0 });
      if(r.egParts) drawEq(r.egParts, { size:20, color:C.MUTED2, align:'left' })(s, MX+1.35, y+0.82, XL-1.6, 0.55);
      else if(r.eg) s.addText(rt(r.eg, { color:C.MUTED2 }), { x:MX+1.35, y:y+0.82, w:XL-1.6, h:0.55, fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0 });
    });
    if(badge) this._badge(s, badge);
    return this;
  }

  compareCards({ title='呢個寫法啱唔啱？', cards, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const y0 = 1.65, gap = 0.22;
    const h = Math.min(1.4, (4.6 - gap*(cards.length-1)) / cards.length);
    cards.forEach((c, i) => {
      const y = y0 + i*(h+gap);
      s.addShape('roundRect', { x:MX, y:y, w:XL, h:h, rectRadius:0.08, fill:{ color:c.ok?C.OKBG:C.BADBG }, line:{ color:C.EDGE, width:1 } });
      s.addShape('ellipse', { x:MX+0.3, y:y+(h-0.7)/2, w:0.7, h:0.7, fill:{ color:c.ok?C.OK:C.BAD } });
      s.addText(c.ok?'✓':'✗', { x:MX+0.3, y:y+(h-0.7)/2, w:0.7, h:0.7, fontFace:F, fontSize:30, bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
      const label = c.ok ? '啱　' : '錯　';
      if (c.text && typeof c.text === 'object' && c.text.eq) {
        const textY = c.note ? y+0.08 : y, textH = c.note ? h*0.5 : h;
        drawEq([label, ...c.text.eq], { size:24, color:C.INK, align:'left' })(s, MX+1.25, textY, XL-1.5, textH);
        if(c.note) this._textOrEq(s, c.note, MX+1.25, y+h*0.54, XL-1.5, h*0.42, { color:C.MUTED2, size:20 });
      } else {
        const head = rt(label+c.text, { bold:true, color:C.INK, fontSize:24 });
        let runs = head;
        if(c.note){ head[head.length-1].options.breakLine = true; runs = [...head, ...rt(c.note, { color:C.MUTED2, fontSize:20, bold:false })]; }
        s.addText(runs, { x:MX+1.25, y:y, w:XL-1.5, h:h, fontFace:F, align:'left', valign:'middle', margin:0 });
      }
    });
    if(badge) this._badge(s, badge);
    return this;
  }

  symbolTiles({ title, tiles, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const n = tiles.length, gap = 0.3, tw = (XL - gap*(n-1))/n, y = 1.7, th = 4.5;
    tiles.forEach((t, i) => {
      const x = MX + i*(tw+gap);
      s.addShape('roundRect', { x, y, w:tw, h:th, rectRadius:0.1, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
      s.addText(rt(t.sym, { bold:true, color:C.HEAD }), { x:x, y:y+0.35, w:tw, h:1.7, fontFace:F, fontSize: t.symSize || 96, align:'center', valign:'middle', margin:0 });
      s.addText('讀「'+t.read+'」', { x:x+0.2, y:y+2.15, w:tw-0.4, h:0.6, fontFace:F, fontSize:24, bold:true, color:C.HEAD, align:'center', margin:0 });
      s.addText(rt(t.meaning, { color:C.INK }), { x:x+0.2, y:y+2.75, w:tw-0.4, h:0.6, fontFace:F, fontSize:22, align:'center', margin:0 });
      if(t.eg) s.addText(rt(t.eg, { bold:true, color:C.HEAD }), { x:x+0.2, y:y+3.45, w:tw-0.4, h:0.8, fontFace:F, fontSize:22, align:'center', valign:'middle', margin:0 });
    });
    if(badge) this._badge(s, badge);
    return this;
  }

  tableSlide({ title, headers, rows, colW, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const head = headers.map(h => ({ text:h, options:{ fill:{ color:C.ACCENT }, color:C.WHITE, bold:true, fontSize:21, align:'center', valign:'middle' } }));
    const body = rows.map((r, ri) => r.map((cell, ci) => ({ text:rt(cell), options:{ fill:{ color: ri%2?C.LIGHT:C.WHITE }, color:C.INK, fontSize:20, bold: ci===0, align: ci===0?'center':'left', valign:'middle' } })));
    // 上緣 1.62、下緣須守住 6.85（頁尾之上）→ 行高封頂，避免最後一行衝出頁底
    const rowH = Math.min(0.90, 5.15 / (rows.length + 1));
    s.addTable([head, ...body], { x:MX, y:1.62, w:XL, colW, border:{ type:'solid', color:C.EDGE, pt:1 }, rowH, fontFace:F, margin:[2,6,2,6], valign:'middle' });
    if(badge) this._badge(s, badge);
    return this;
  }

  // 同 tableSlide() 睇落一樣（accent 表頭＋斑馬紋），但格仔可以擺 drawEq 真分數／
  // 根號——pptxgenjs 原生 addTable() 嘅 cell 淨係食文字 run，塞唔到分數線／根號嗰啲
  // 獨立 shape，所以呢個方法自己逐格畫 rect＋text／drawEq，唔用 addTable()。
  // cell 可以係字串（跟 tableSlide 舊行為）或 { eq:[...] }（drawEq 語法）。
  eqTable({ title, headers, rows, colW, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const y0 = 1.62;
    const rowH = Math.min(0.90, 5.15 / (rows.length + 1));
    const xs = []; let acc = MX; colW.forEach(w => { xs.push(acc); acc += w; });
    headers.forEach((hd, ci) => {
      s.addShape('rect', { x:xs[ci], y:y0, w:colW[ci], h:rowH, fill:{ color:C.ACCENT }, line:{ color:C.EDGE, width:1 } });
      s.addText(hd, { x:xs[ci], y:y0, w:colW[ci], h:rowH, fontFace:F, fontSize:21, bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
    });
    rows.forEach((row, ri) => {
      const y = y0 + (ri + 1) * rowH;
      row.forEach((cell, ci) => {
        s.addShape('rect', { x:xs[ci], y, w:colW[ci], h:rowH, fill:{ color: ri%2?C.LIGHT:C.WHITE }, line:{ color:C.EDGE, width:1 } });
        if (cell && typeof cell === 'object' && cell.eq) {
          drawEq(cell.eq, { size:22, color:C.INK, align:'center' })(s, xs[ci], y, colW[ci], rowH);
        } else {
          s.addText(rt(String(cell), { color:C.INK, bold: ci===0 }),
            { x:xs[ci], y, w:colW[ci], h:rowH, fontFace:F, fontSize:20, align: ci===0?'center':'left', valign:'middle', margin:0 });
        }
      });
    });
    if(badge) this._badge(s, badge);
    return this;
  }

  compare2({ title, left, right, note, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const cw = 5.85, gap = 0.4, y = 1.65, ch = note?4.0:4.5;
    [[MX,left],[MX+cw+gap,right]].forEach(([x, col]) => {
      s.addShape('roundRect', { x, y, w:cw, h:ch, rectRadius:0.1, fill:{ color:C.WHITE }, line:{ color:C.EDGE, width:1 } });
      s.addShape('roundRect', { x, y, w:cw, h:0.66, rectRadius:0.1, fill:{ color:C.ACCENT } });
      s.addText(rt(col.head, { bold:true, color:C.WHITE }), { x, y, w:cw, h:0.66, fontFace:F, fontSize:23, align:'center', valign:'middle', margin:0 });
      s.addText(rtLines(col.lines, { color:C.INK, fontSize:23 }),
        { x:x+0.35, y:y+0.85, w:cw-0.7, h:ch-1.1, fontFace:F, align:'left', valign:'top', margin:0, lineSpacingMultiple:1.3 });
    });
    if(note) s.addText(rt(note, { bold:true, color:C.HEAD }), { x:MX, y:5.9, w:XL, h:0.6, fontFace:F, fontSize:20, align:'center', valign:'middle', margin:0 });
    if(badge) this._badge(s, badge);
    return this;
  }

  scaffold4({ title, steps, note, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const cw = 5.85, ch = 2.05, gx = 0.4, gy = 0.3, x0 = MX, y0 = 1.6;
    steps.slice(0,4).forEach((st, i) => {
      const x = x0 + (i%2)*(cw+gx), y = y0 + Math.floor(i/2)*(ch+gy);
      s.addShape('roundRect', { x, y, w:cw, h:ch, rectRadius:0.08, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
      const by = y + (ch - 0.62) / 2;   // 編號圓圈同文字垂直置中對齊
      s.addShape('ellipse', { x:x+0.25, y:by, w:0.62, h:0.62, fill:{ color:C.ACCENT } });
      s.addText(String(i+1), { x:x+0.25, y:by, w:0.62, h:0.62, fontFace:F, fontSize:26, bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
      this._textOrEq(s, st, x+1.05, y+0.2, cw-1.3, ch-0.4, { color:C.INK, size: (st && st.eq) ? 21 : 22, lineSpacingMultiple:1.2 });
    });
    if(note) s.addText(rt(note, { color:C.MUTED2 }), { x:MX, y:6.45, w: badge?6.9:XL, h:0.5, fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0 });
    if(badge) this._badge(s, badge);
    return this;
  }

  // 大圖 + 右側說明（Venn 圖／示意圖專用）
  // eq：drawEq 語法陣列，喺標題下面加一條原生數學式橫幅（標題本身唔支援分數／根號，
  // 要展示嘅算式一定要擺呢度，唔好寫入 title 字串）
  figure({ title, eq, draw, image, caption, side, star, badge }){
    const s = this._content(); this._title(s, title, star);
    let fy = 1.6;
    if (eq) {
      s.addShape('roundRect', { x:MX, y:fy, w:XL, h:0.72, rectRadius:0.08, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
      drawEq(eq, { size:28, color:C.HEAD })(s, MX, fy, XL, 0.72);
      fy += 0.90;
    }
    const fw = 7.0, fh = eq ? 3.6 : 4.5;
    s.addShape('roundRect', { x:MX, y:fy, w:fw, h:fh, rectRadius:0.1, fill:{ color:C.WHITE }, line:{ color:C.EDGE, width:1 } });
    if(draw) draw(s, MX+0.25, fy+0.25, fw-0.5, fh-(caption?1.05:0.5));
    if(image) s.addImage({ path:image, x:MX+0.4, y:fy+0.3, w:fw-0.8, h:fh-(caption?1.15:0.6), sizing:{ type:'contain', w:fw-0.8, h:fh-(caption?1.15:0.6) } });
    if(caption) s.addText(rt(caption, { bold:true, color:C.HEAD }), { x:MX, y:fy+fh-0.75, w:fw, h:0.6, fontFace:F, fontSize:21, align:'center', valign:'middle', margin:0 });
    if(side) colLines(s, side, MX+fw+0.45, fy+0.35, XL-fw-0.45, fh-0.7, { color:C.INK, fontSize:23, lineSpacingMultiple:1.35 });
    if(badge) this._badge(s, badge);
    return this;
  }

  layered({ title='揀一層，做做看', cols, note, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const cw = 3.83, gap = 0.30, y = 1.6, ch = 4.35;
    const xs = [MX, MX+cw+gap, MX+2*(cw+gap)];
    cols.forEach((col, i) => {
      const x = xs[i];
      s.addShape('roundRect', { x, y, w:cw, h:ch, rectRadius:0.1, fill:{ color:C.WHITE }, line:{ color:C.EDGE, width:1 } });
      s.addShape('roundRect', { x, y, w:cw, h:0.95, rectRadius:0.1, fill:{ color:C.BLOCK } });
      s.addText(col.stars, { x, y:y+0.12, w:cw, h:0.45, fontFace:F, fontSize:24, color:C.STAR, align:'center', margin:0 });
      s.addText(col.head, { x, y:y+0.5, w:cw, h:0.45, fontFace:F, fontSize:20, bold:true, color:C.HEAD, align:'center', valign:'middle', margin:0 });
      colLines(s, col.lines, x+0.3, y+1.15, cw-0.6, ch-1.35, { fontSize:21 });
    });
    // 有徽章時 note 收窄靠左，避免同右下角徽章疊字
    if(note) s.addText(rt(note, { color:C.MUTED2 }), { x:MX, y: badge?6.45:6.15, w: badge?6.9:XL, h:0.5, fontFace:F, fontSize:20, align: badge?'left':'center', valign:'middle', margin:0 });
    if(badge) this._badge(s, badge);
    return this;
  }

  // 分數式判斷頁：左邊真分數式、中間 ✓/✗＋文字、右邊說明。
  // 辨識類頁面用（教「睇分數線下面係咩」時，式本身一定要有真分數線）。
  // rows: [{ parts:(drawEq 格式), ok:true/false/undefined, note:'…' }]
  eqJudge({ title, rows, note, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const y0 = 1.62, gap = 0.20;
    const h = Math.min(1.25, (4.75 - gap*(rows.length-1)) / rows.length);
    rows.forEach((r, i) => {
      const y = y0 + i*(h+gap);
      s.addShape('roundRect', { x:MX, y, w:XL, h, rectRadius:0.08,
        fill:{ color: r.ok === undefined ? C.BLOCK : (r.ok ? C.OKBG : C.BADBG) },
        line:{ color:C.EDGE, width:1 } });
      drawEq(r.parts, { size:30 })(s, MX+0.15, y, 3.3, h);
      if(r.ok !== undefined){
        const by = y + (h-0.62)/2;
        s.addShape('ellipse', { x:MX+3.70, y:by, w:0.62, h:0.62, fill:{ color: r.ok?C.OK:C.BAD } });
        s.addText(r.ok?'✓':'✗', { x:MX+3.70, y:by, w:0.62, h:0.62, fontFace:F, fontSize:26,
          bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
        s.addText(r.ok?'係':'唔係', { x:MX+4.42, y, w:0.95, h, fontFace:F, fontSize:22,
          bold:true, color:C.INK, align:'left', valign:'middle', margin:0 });
      }
      if(r.note) s.addText(rt(r.note, { color:C.MUTED2 }), { x:MX+5.45, y, w:XL-5.60, h,
        fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0 });
    });
    if(note) s.addText(rt(note, { color:C.MUTED2 }), { x:MX, y:6.5, w: badge?6.9:XL, h:0.5,
      fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0 });
    if(badge) this._badge(s, badge);
    return this;
  }

  summary({ title='今日帶走', takeaway, lines, star }){
    const s = this._content(); this._title(s, title, star);
    s.addShape('roundRect', { x:MX, y:1.75, w:XL, h:1.7, rectRadius:0.1, fill:{ color:C.ACCENT } });
    s.addText(rt(takeaway, { bold:true, color:C.WHITE }), { x:MX+0.4, y:1.75, w:XL-0.8, h:1.7, fontFace:F, fontSize:30, align:'center', valign:'middle', margin:0 });
    s.addText('保底三句', { x:MX, y:3.75, w:XL, h:0.5, fontFace:F, fontSize:20, bold:true, color:C.MUTED2, align:'left', margin:0 });
    s.addShape('roundRect', { x:MX, y:4.25, w:XL, h:2.35, rectRadius:0.1, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
    colLines(s, lines, MX+0.5, 4.45, XL-1.0, 1.95, { color:C.INK, fontSize:24, lineSpacingMultiple:1.35 });
    return this;
  }

  closing({ title, line, iep }){
    const s = this._dark();
    s.addText(rt(title, { bold:true, color:C.WHITE }), { x:MX, y:2.2, w:12.1, h:1.5, fontFace:F, fontSize:40, align:'center', valign:'middle', margin:0 });
    if(line) s.addText(rt(line, { color:'C9D6CE' }), { x:MX, y:3.8, w:12.1, h:0.9, fontFace:F, fontSize:24, align:'center', margin:0 });
    if(iep) s.addText(iep, { x:MX, y:6.5, w:12.1, h:0.7, fontFace:F, fontSize:14, color:'8AA697', align:'center', valign:'middle', margin:0 });
    return this;
  }
}

// ── 示意圖繪製（全部原生圖形：夠清、跟色系、唔靠外部 PNG）─────────────
// 「一個圈圈住幾個對象」
function drawGroup(labels){
  return (s, x, y, w, h) => {
    s.addShape('ellipse', { x:x+0.15, y:y+0.15, w:w-0.3, h:h-0.3, fill:{ color:'FFFFFF' }, line:{ color:C.ACCENT, width:2.5, dashType:'dash' } });
    const cx = x + w/2, cy = y + h/2, r = Math.min(w,h)*0.22;
    labels.slice(0,3).forEach((lb, i) => {
      const ang = -Math.PI/2 + i*(2*Math.PI/labels.length);
      const dx = cx + r*Math.cos(ang) - 0.4, dy = cy + r*Math.sin(ang) - 0.28;
      s.addShape('ellipse', { x:dx, y:dy, w:0.8, h:0.56, fill:{ color:C.BLOCK }, line:{ color:C.ACCENT, width:1 } });
      s.addText(lb, { x:dx, y:dy, w:0.8, h:0.56, fontFace:F, fontSize:16, bold:true, color:C.HEAD, align:'center', valign:'middle', margin:0 });
    });
  };
}

// 兩圓 Venn。mode: 'union' | 'intersection' | 'onlyA'
// 交集用半透明疊色呈現（重疊處自然變深），唔靠紅綠、黑白列印仍可辨深淺。
function drawVenn(mode, { a='A', b='B', u='U', caption } = {}){
  return (s, x, y, w, h) => {
    const uh = h * (caption ? 0.80 : 0.90);
    s.addShape('rect', { x, y, w, h:uh, fill:{ color:C.WHITE }, line:{ color:C.INK, width:1.25 } });
    s.addText(u, { x:x+0.08, y:y+0.05, w:0.5, h:0.35, fontFace:F, fontSize:16, bold:true, color:C.INK, align:'left', valign:'middle', margin:0 });
    const r  = Math.min(w*0.235, uh*0.33);
    const cy = y + uh*0.52, cx1 = x + w/2 - r*0.62, cx2 = x + w/2 + r*0.62;
    const circ = (cx, fill) => s.addShape('ellipse', { x:cx-r, y:cy-r, w:2*r, h:2*r, ...(fill?{fill}:{fill:{ color:'FFFFFF', transparency:100 }}), line:{ color:C.INK, width:1.5 } });
    let aFilled = false, bFilled = false;
    if(mode === 'union'){ circ(cx1, { color:C.ACCENT }); circ(cx2, { color:C.ACCENT }); aFilled = bFilled = true; }
    else if(mode === 'intersection'){ circ(cx1, { color:C.ACCENT, transparency:55 }); circ(cx2, { color:C.ACCENT, transparency:55 }); }
    else if(mode === 'onlyA'){ circ(cx1, { color:C.ACCENT }); circ(cx2, { color:C.WHITE }); circ(cx1, null); circ(cx2, null); aFilled = true; }
    else { circ(cx1, null); circ(cx2, null); }
    // 標籤放喺各自圓形嘅獨佔區內（唔可以放圓外，會壓住全集外框）
    s.addText(a, { x:cx1-r*0.88, y:cy-r*0.80, w:0.6, h:0.4, fontFace:F, fontSize:20, bold:true, color:aFilled?C.WHITE:C.INK, align:'center', valign:'middle', margin:0 });
    s.addText(b, { x:cx2+r*0.28, y:cy-r*0.80, w:0.6, h:0.4, fontFace:F, fontSize:20, bold:true, color:bFilled?C.WHITE:C.INK, align:'center', valign:'middle', margin:0 });
    if(caption) s.addText(rt(caption, { color:C.MUTED2 }), { x, y:y+uh+0.06, w, h:0.4, fontFace:F, fontSize:17, align:'center', valign:'middle', margin:0 });
  };
}

// 補集：全集塗色、A 挖空
function drawComplement({ a='A', u='U', caption } = {}){
  return (s, x, y, w, h) => {
    const uh = h * (caption ? 0.80 : 0.90);
    s.addShape('rect', { x, y, w, h:uh, fill:{ color:C.ACCENT }, line:{ color:C.INK, width:1.25 } });
    s.addText(u, { x:x+0.08, y:y+0.05, w:0.5, h:0.35, fontFace:F, fontSize:16, bold:true, color:C.WHITE, align:'left', valign:'middle', margin:0 });
    const r = Math.min(w*0.22, uh*0.34), cx = x + w/2, cy = y + uh*0.54;
    s.addShape('ellipse', { x:cx-r, y:cy-r, w:2*r, h:2*r, fill:{ color:C.WHITE }, line:{ color:C.INK, width:1.5 } });
    s.addText(a, { x:cx-0.3, y:cy-0.22, w:0.6, h:0.44, fontFace:F, fontSize:22, bold:true, color:C.INK, align:'center', valign:'middle', margin:0 });
    if(caption) s.addText(rt(caption, { color:C.MUTED2 }), { x, y:y+uh+0.06, w, h:0.4, fontFace:F, fontSize:17, align:'center', valign:'middle', margin:0 });
  };
}

// 包含關係：細圈喺大圈入面（子集 / p⇒q 對應 P⊆Q）
function drawSubset({ inner='A', outer='B', caption } = {}){
  return (s, x, y, w, h) => {
    const bh = h * (caption ? 0.80 : 0.92);
    const R = Math.min(w*0.30, bh*0.46), cx = x + w/2, cy = y + bh*0.50;
    s.addShape('ellipse', { x:cx-R, y:cy-R, w:2*R, h:2*R, fill:{ color:C.WHITE }, line:{ color:C.INK, width:1.5 } });
    // 外圈標籤要退入圓內，唔可以貼住圓周（否則同外框線疊住）
    s.addText(outer, { x:cx+R*0.18, y:cy-R*0.78, w:0.6, h:0.4, fontFace:F, fontSize:20, bold:true, color:C.INK, align:'center', valign:'middle', margin:0 });
    const r = R*0.48, icx = cx - R*0.22, icy = cy + R*0.10;
    s.addShape('ellipse', { x:icx-r, y:icy-r, w:2*r, h:2*r, fill:{ color:C.ACCENT }, line:{ color:C.INK, width:1.5 } });
    s.addText(inner, { x:icx-0.3, y:icy-0.22, w:0.6, h:0.44, fontFace:F, fontSize:20, bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
    if(caption) s.addText(rt(caption, { color:C.MUTED2 }), { x, y:y+bh+0.04, w, h:0.4, fontFace:F, fontSize:17, align:'center', valign:'middle', margin:0 });
  };
}

// ── 分數式／根號（原生排版）───────────────────────────────────────────
// 真分數線同真根號係反比例函數／根式嘅視覺識別，inline「12/x」「√(x+5)」
// 呢種純文字寫法頂替唔到——分數線唔一定啱位、根號嘅覆蓋範圍睇唔出（融合生
// 易讀錯做「√x 再 +5」）。2026-08-07 起一律用呢個原生排版，唔准走文字捷徑。
// parts：陣列，每個元素可以係：
//   字串                        → 直接排文字
//   { n:'分子', d:'分母' }       → 分數（n／d 又可以係字串或下面嘅 { sqrt }/{ base,exp }，可以巢狀）
//   { sqrt:'被開方式' }          → 根號（被開方式又可以係字串或 { n, d } 分數，可以巢狀）
//   { sqrt:'a^m', deg:'n' }     → n 次方根（deg 係細字根指數，畫喺 hook 前面，即 ⁿ√(...)；
//                                  唔畀 deg 就係平方根，冇顯示指數，同以前一樣）
//   { base:'a', exp:'2' }       → 指數（exp 抬高、縮細字級，貼喺 base 右上角；exp 本身又可以係
//                                  { n, d } 分數，例如 { base:'a', exp:{n:'2',d:'3'} } → a 嘅 2/3 次方，
//                                  指數入面真係一條分數線疊埋，唔係打斜線）
//   [...]（陣列）                 → 一串橫排子式，可以塞喺 base/exp/n/d/sqrt 任何一欄，用嚟砌
//                                  複合式，例如 (2³)^{2/3}：{ base:['(', {base:'2',exp:'3'}, ')'],
//                                  exp:{n:'2',d:'3'} }
//   例：drawEq(['y = ', { n:'12', d:'x' }], { size:48 })
//   例：drawEq(['f(x) = ', { n:{ sqrt:'x+5' }, d:'x−1' }], { size:28 })
//   例：drawEq([{ sqrt:'a^2', deg:'3' }, ' = ', { base:'a', exp:{n:'2',d:'3'} }], { size:32 })
const _EQ_CJK = /[　-鿿＀-￯]/;
const _eqWOf = (t, fs) => String(t).split('')
  // 空格唔可以當 0.58em 計（會喺 `＝` 同分數之間爆出一大忽留白）
  .reduce((a, ch) => a + (ch === ' ' ? 0.26 : _EQ_CJK.test(ch) ? 1.0 : 0.58), 0) * (fs / 72) + 0.10;

function _eqMeasure(node, fs) {
  if (typeof node === 'string') return { kind: 'text', text: node, fs, w: _eqWOf(node, fs) };
  // 陣列＝一串橫排嘅子式（例如 (2^3) 呢種複合底數：['(', {base:'2',exp:'3'}, ')']），
  // 令 base/exp/n/d/sqrt 呢啲欄位都可以塞多過一個 part 進去，唔限於單一 node。
  if (Array.isArray(node)) {
    const items = node.map((p) => _eqMeasure(p, fs));
    return { kind: 'seq', items, fs, w: items.reduce((a, it) => a + it.w, 0) };
  }
  if (node && node.sqrt !== undefined) {
    const inner = _eqMeasure(node.sqrt, fs);
    const hook = (fs / 72) * 0.46;
    const degFs = fs * 0.6;
    const degW = node.deg !== undefined ? _eqWOf(node.deg, degFs) : 0;
    return { kind: 'sqrt', inner, hook, deg: node.deg, degFs, degW, fs, w: degW * 0.75 + hook + inner.w + 0.10 };
  }
  if (node && node.exp !== undefined) {
    const base = _eqMeasure(node.base, fs);
    const expFs = fs * 0.62;
    const exp = _eqMeasure(node.exp, expFs);
    return { kind: 'exp', base, exp, fs, w: base.w + exp.w * 0.88 };
  }
  const nfs = fs * 0.88;
  const n = _eqMeasure(node.n, nfs), d = _eqMeasure(node.d, nfs);
  return { kind: 'frac', n, d, fs, w: Math.max(n.w, d.w) + 0.16 };
}

// 根號嘅 vinculum（頂線）要企幾高，先夠遮晒被開方式最高嗰忽——普通文字淨係
// cap-height 就夠，但抬高咗嘅指數（exp）／分子（frac）會凸出去，唔企高啲條線
// 會穿過個指數（實測：ⁿ√(aᵐ) 嗰個 m 會凸出條頂線之上）。單位＝吋（絕對值，
// 因為每個 node 自己帶住 fs，唔使再乘一次 em）。
function _eqTopExtent(node) {
  const em = node.fs / 72;
  if (node.kind === 'exp') return Math.max(_eqTopExtent(node.base), em * 0.40 + _eqTopExtent(node.exp));
  if (node.kind === 'frac') return (node.n.fs / 72) * 0.68 + _eqTopExtent(node.n);
  if (node.kind === 'sqrt') return em * 0.60 + (node.deg !== undefined ? em * 0.35 : 0);
  if (node.kind === 'seq') return node.items.reduce((a, it) => Math.max(a, _eqTopExtent(it)), 0);
  return em * 0.60; // 'text'
}

// 鏡像 _eqTopExtent：node 個底伸幾低——分數嘅分母會向下伸（仲會巢埋落去），
// 呢個影響行高：一行入面塞咗分數，成行要留返夠位，唔可以同下一行嘅文字疊埋
// （實測：練習「1/aⁿ = a⁻ⁿ」個分母 aⁿ 疊住埋落面一行「③ 轉咗做指數…」）。
function _eqBottomExtent(node) {
  const em = node.fs / 72;
  if (node.kind === 'frac') {
    const dGap = Math.max((node.d.fs / 72) * 0.68, _eqTopExtent(node.d) + 0.05);
    return dGap + _eqBottomExtent(node.d);
  }
  if (node.kind === 'exp') return _eqBottomExtent(node.base); // exp 抬高，唔加落面嘅伸展
  if (node.kind === 'sqrt') return Math.max(em * 0.28, _eqBottomExtent(node.inner));
  if (node.kind === 'seq') return node.items.reduce((a, it) => Math.max(a, _eqBottomExtent(it)), 0);
  return em * 0.35; // 'text'
}

// parts 陣列（一條 drawEq 算式）喺某個字級之下，實際要幾高先夠企（頂+底，吋）。
// colLines() 用嚟計每行行高——唔可以淨係用固定字級行高，塞咗分數／根號嘅行會更高。
function eqExtent(parts, fontSize) {
  const nodes = parts.map((p) => _eqMeasure(p, fontSize));
  return {
    top: nodes.reduce((a, it) => Math.max(a, _eqTopExtent(it)), 0),
    bottom: nodes.reduce((a, it) => Math.max(a, _eqBottomExtent(it)), 0),
  };
}

function drawEq(parts, { size = 40, color, align = 'center' } = {}) {
  return (s, x, y, w, h) => {
    const cy = y + h / 2;
    const col = color || C.HEAD;
    const nodes = parts.map((p) => _eqMeasure(p, size));
    const tot = nodes.reduce((a, it) => a + it.w, 0);
    let cx = align === 'center' ? x + (w - tot) / 2 : x;

    function put(node, px, centerY) {
      const em = node.fs / 72;
      if (node.kind === 'text') {
        // wrap:false——wOf() 只係粗略估寬，真字寬有落差，唔關就會自動摺行，
        // 摺出嚟嘅孤字會疊住下一個 part（實測：長算式鏈「→ … → x ≥ −5」摺走「−5」）
        s.addText(node.text, { x:px, y:centerY-em*0.75, w:node.w, h:em*1.5, fontFace:F, fontSize:node.fs,
          bold:true, color:col, align:'center', valign:'middle', margin:0, wrap:false });
      } else if (node.kind === 'frac') {
        s.addShape('line', { x:px+0.05, y:centerY, w:node.w-0.10, h:0, line:{ color:col, width:2.25 } });
        put(node.n, px + (node.w - node.n.w) / 2, centerY - (node.n.fs / 72) * 0.68);
        // 分母落幾低唔可以淨係固定 0.68em——分母本身如果係根號（尤其帶 deg），
        // 佢自己嘅 vinculum 會向上凸，落得唔夠深就會同呢條分數線疊埋／打交叉
        // （實測：1/³√(a⁵) 個「3√」嘅頂線同分數線黐埋一齊）。
        const dGap = Math.max((node.d.fs / 72) * 0.68, _eqTopExtent(node.d) + 0.05);
        put(node.d, px + (node.w - node.d.w) / 2, centerY + dGap);
      } else if (node.kind === 'sqrt') {
        // 根指數（deg，得 nth root 先有）：細字，畫喺 hook 前面、貼近 hook 頂——
        // 標準教科書寫法，唔係另外飄一個獨立上標（會讀成「n 乘 √」）。
        // 筆劃粗幼跟 em 縮放（唔可以成粒 hardcode）：巢喺分數分母入面嗰種細字
        // sqrt，2pt 定寬線相對粗幼會顯得同 deg 數字疊埋（實測跑出嚟先發現）。
        const lw = Math.max(1, Math.min(2, em * 3.4)), lwTop = lw * 1.1;
        let px2 = px;
        if (node.deg !== undefined) {
          const degEm = node.degFs / 72;
          s.addText(String(node.deg), { x: px2, y: centerY - em * 0.95, w: node.degW, h: degEm * 1.3,
            fontFace: F, fontSize: node.degFs, bold: true, color: col, align: 'center', valign: 'middle',
            margin: 0, wrap: false });
          px2 += node.degW * 0.95;
        }
        // 鉤（兩段斜線：短下筆＋長上筆）＋頂線（vinculum），覆蓋成個被開方式——
        // 頂線企幾高睇 inner 本身有幾高（例如 aᵐ 嗰個 m 會凸出普通文字嘅 cap-height），
        // 唔可以淨係用固定 em*0.60，否則巢住指數／分數嘅根號頂線會穿過個指數。
        const topY = centerY - Math.max(em * 0.60, _eqTopExtent(node.inner)), botY = centerY + em * 0.28, midY = centerY - em * 0.02;
        const hookMidX = px2 + node.hook * 0.38, hookRightX = px2 + node.hook;
        seg(s, px2, midY, hookMidX, botY, { color: col, width: lw, head: false });
        seg(s, hookMidX, botY, hookRightX, topY, { color: col, width: lw, head: false });
        seg(s, hookRightX, topY, hookRightX + node.inner.w + 0.04, topY, { color: col, width: lwTop, head: false });
        put(node.inner, hookRightX + 0.02, centerY);
      } else if (node.kind === 'exp') {
        // 指數：底數正常畫，指數縮細字級、抬高貼喺右上角——exp 本身可以係
        // { n, d } 分數，遞歸落 put() 就自動用縮細咗嘅字級排返個分數線出嚟。
        put(node.base, px, centerY);
        put(node.exp, px + node.base.w - node.exp.w * 0.14, centerY - em * 0.40);
      } else if (node.kind === 'seq') {
        let px2 = px;
        node.items.forEach((it) => { put(it, px2, centerY); px2 += it.w; });
      }
    }

    nodes.forEach((node) => { put(node, cx, cy); cx += node.w; });
  };
}

// 欄內逐行輸出：line 可以係字串（照舊一次過 rtLines），或 { eq:[...] }（drawEq
// 語法，獨立一行原生分數／根號）。有 eq 先切做逐行手動排版，冇 eq 完全等舊行為。
function colLines(s, lines, x, y, w, h, opts = {}) {
  const fontSize = opts.fontSize || 21;
  const hasEq = lines.some((l) => l && typeof l === 'object' && l.eq);
  if (!hasEq) {
    s.addText(rtLines(lines, { color: opts.color || C.INK, fontSize }),
      { x, y, w, h, fontFace: F, align: 'left', valign: 'top', margin: 0,
        lineSpacingMultiple: opts.lineSpacingMultiple || 1.25 });
    return;
  }
  const lh = (fontSize / 72) * (opts.lineSpacingMultiple || 1.25) * 1.2;
  let cy = y;
  lines.forEach((ln) => {
    if (ln && typeof ln === 'object' && ln.eq) {
      // 塞咗分數／根號嘅行可能比普通文字行高——行高唔可以淨係用固定 lh，
      // 否則個分母／根號會伸落去疊住下一行（實測：1/aⁿ 個分母疊住埋面一行字）。
      const ext = eqExtent(ln.eq, fontSize);
      const rowH = Math.max(lh, ext.top + ext.bottom + 0.06);
      drawEq(ln.eq, { size: fontSize, color: opts.color || C.INK, align: 'left' })(s, x, cy, w, rowH);
      cy += rowH;
    } else {
      if (ln !== '') {
        s.addText(rt(String(ln), { color: opts.color || C.INK }),
          { x, y: cy, w, h: lh, fontFace: F, fontSize, align: 'left', valign: 'middle', margin: 0 });
      }
      cy += lh;
    }
  });
}

// ── 線／箭嘴：pptxgenjs 只食正寬高，向上要靠 flipV ─────────────────────
function seg(s, x1, y1, x2, y2, o = {}) {
  const pr = {
    x: Math.min(x1, x2), y: Math.min(y1, y2),
    w: Math.abs(x2 - x1), h: Math.abs(y2 - y1),
    line: { color: o.color || C.ACCENT, width: o.width || 2,
            ...(o.head === false ? {} : { endArrowType: 'triangle' }),
            ...(o.dash ? { dashType: 'dash' } : {}) },
  };
  // pptxgenjs 嘅 line 預設由 (minX,minY) 畫去 (maxX,maxY)，箭嘴喺後者。
  // 要令終點真係落喺 (x2,y2)：y2 喺上面就 flipV，x2 喺左面就 flipH。
  // （唔可以只睇 (x2-x1)*(y2-y1) 嘅正負——垂直線同向左嘅線個積係 0 或正，會漏。）
  if (y2 < y1) pr.flipV = true;
  if (x2 < x1) pr.flipH = true;
  s.addShape('line', pr);
}

// 對應關係圖（映射圖）：左集合每點射箭到右集合。
// edges = [[左index, 右index], ...]。用嚟教「一個 x 配到幾個 y」。
function drawMapping({ left, right, edges, caption } = {}) {
  return (s, x, y, w, h) => {
    const bh = h * (caption ? 0.82 : 1);
    const ovW = Math.min(1.5, w * 0.30), padY = bh * 0.06;
    const lx = x + w * 0.06, rx = x + w - w * 0.06 - ovW;
    [lx, rx].forEach((ox) =>
      s.addShape('ellipse', { x: ox, y: y + padY, w: ovW, h: bh - 2 * padY,
        fill: { color: 'FFFFFF', transparency: 100 }, line: { color: C.EDGE, width: 1.5 } }));
    const cxL = lx + ovW / 2, cxR = rx + ovW / 2;
    const at = (i, n) => y + padY + (bh - 2 * padY) * (i + 1) / (n + 1);
    const dot = (cx, cy, col) => s.addShape('ellipse',
      { x: cx - 0.085, y: cy - 0.085, w: 0.17, h: 0.17, fill: { color: col }, line: { type: 'none' } });
    left.forEach((lb, i) => {
      const cy = at(i, left.length);
      dot(cxL, cy, C.ACCENT);
      s.addText(lb, { x: cxL - 0.78, y: cy - 0.19, w: 0.55, h: 0.38, fontFace: F, fontSize: 20,
        bold: true, color: C.INK, align: 'right', valign: 'middle', margin: 0 });
    });
    right.forEach((lb, i) => {
      const cy = at(i, right.length);
      dot(cxR, cy, C.HEAD);
      s.addText(lb, { x: cxR + 0.23, y: cy - 0.19, w: 0.55, h: 0.38, fontFace: F, fontSize: 20,
        bold: true, color: C.INK, align: 'left', valign: 'middle', margin: 0 });
    });
    edges.forEach(([a, b]) =>
      seg(s, cxL + 0.13, at(a, left.length), cxR - 0.15, at(b, right.length), { width: 1.75 }));
    if (caption) s.addText(rt(caption, { color: C.MUTED2 }),
      { x, y: y + bh + 0.04, w, h: 0.4, fontFace: F, fontSize: 17, align: 'center', valign: 'middle', margin: 0 });
  };
}

// 函數「機器」示意：x → [ f ] → y
function drawMachine({ inLabel = 'x', box = 'f', outLabel = 'y', caption } = {}) {
  return (s, x, y, w, h) => {
    const bh = h * (caption ? 0.80 : 1);
    const cy = y + bh / 2, bw = w * 0.34, bxH = Math.min(bh * 0.55, 1.2);
    const bx = x + (w - bw) / 2;
    s.addText(inLabel, { x: x, y: cy - 0.28, w: bw * 0.5, h: 0.56, fontFace: F, fontSize: 26,
      bold: true, color: C.INK, align: 'center', valign: 'middle', margin: 0 });
    seg(s, x + bw * 0.5, cy, bx - 0.06, cy);
    s.addShape('roundRect', { x: bx, y: cy - bxH / 2, w: bw, h: bxH, rectRadius: 0.1,
      fill: { color: C.ACCENT }, line: { type: 'none' } });
    s.addText(rt(box, { bold: true, color: C.WHITE }), { x: bx, y: cy - bxH / 2, w: bw, h: bxH,
      fontFace: F, fontSize: 32, align: 'center', valign: 'middle', margin: 0 });
    seg(s, bx + bw + 0.06, cy, x + w - bw * 0.5, cy);
    s.addText(outLabel, { x: x + w - bw * 0.5, y: cy - 0.28, w: bw * 0.5, h: 0.56, fontFace: F,
      fontSize: 26, bold: true, color: C.INK, align: 'center', valign: 'middle', margin: 0 });
    if (caption) s.addText(rt(caption, { color: C.MUTED2 }),
      { x, y: y + bh + 0.04, w, h: 0.4, fontFace: F, fontSize: 17, align: 'center', valign: 'middle', margin: 0 });
  };
}

module.exports = { Deck, C, F, rt, rtLines, seg, drawEq, eqExtent, colLines, drawGroup, drawVenn, drawComplement, drawSubset, drawMapping, drawMachine };
