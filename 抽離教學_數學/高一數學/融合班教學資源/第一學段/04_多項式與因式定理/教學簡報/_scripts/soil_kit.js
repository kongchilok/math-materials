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
  constructor(footerLabel){ this.p = new pptxgen(); this.p.layout = 'LAYOUT_WIDE'; this.foot = footerLabel; this.n = 0; }
  save(fileName){ return this.p.writeFile({ fileName }); }

  _content(){ const s = this.p.addSlide(); s.background = { color: C.LIGHT }; this.n++; this._footer(s); return s; }
  _dark(){ const s = this.p.addSlide(); s.background = { color: C.DARK }; this.n++; return s; }
  _footer(s){
    s.addText(`高一數學 · ${this.foot}`, { x:MX, y:7.04, w:9, h:0.3, fontFace:F, fontSize:11, color:C.MUTED, align:'left', margin:0, valign:'middle' });
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

  agenda({ title='今日課堂流程', steps, note }){
    const s = this._content(); this._title(s, title);
    const y0 = 1.65, h = 0.86, gap = 0.16;
    steps.forEach((st, i) => {
      const y = y0 + i*(h+gap);
      s.addShape('ellipse', { x:MX, y:y, w:h, h:h, fill:{ color:C.ACCENT } });
      s.addText(String(i+1), { x:MX, y:y, w:h, h:h, fontFace:F, fontSize:30, bold:true, color:C.WHITE, align:'center', valign:'middle', margin:0 });
      s.addShape('roundRect', { x:MX+h+0.25, y:y, w:XL-h-0.25, h:h, rectRadius:0.08, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
      s.addText(rt(st, { bold:true, color:C.HEAD }), { x:MX+h+0.55, y:y, w:XL-h-0.85, h:h, fontFace:F, fontSize:23, align:'left', valign:'middle', margin:0 });
    });
    if(note) s.addText(rt(note, { color:C.MUTED2 }), { x:MX, y:6.5, w:XL, h:0.5, fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0 });
    return this;
  }

  problem({ title='先想一想', question, sub, caption, star, badge }){
    const s = this._content(); this._title(s, title, star);
    s.addShape('roundRect', { x:MX, y:1.9, w:XL, h:2.4, rectRadius:0.1, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
    s.addText(rt(question, { bold:true, color:C.HEAD }), { x:MX+0.4, y:2.15, w:XL-0.8, h:1.1, fontFace:F, fontSize:30, align:'left', valign:'middle', margin:0 });
    if(sub) s.addText(rt(sub, { color:C.INK }), { x:MX+0.4, y:3.25, w:XL-0.8, h:0.9, fontFace:F, fontSize:23, align:'left', valign:'top', margin:0 });
    if(caption) s.addText(rt(caption, { bold:true, color:C.HEAD }), { x:MX, y:4.7, w:XL, h:0.9, fontFace:F, fontSize:22, align:'left', valign:'middle', margin:0 });
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
      if(r.eg) s.addText(rt(r.eg, { color:C.MUTED2 }), { x:MX+1.35, y:y+0.82, w:XL-1.6, h:0.55, fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0 });
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
      const head = rt((c.ok?'啱　':'錯　')+c.text, { bold:true, color:C.INK, fontSize:24 });
      let runs = head;
      if(c.note){ head[head.length-1].options.breakLine = true; runs = [...head, ...rt(c.note, { color:C.MUTED2, fontSize:20, bold:false })]; }
      s.addText(runs, { x:MX+1.25, y:y, w:XL-1.5, h:h, fontFace:F, align:'left', valign:'middle', margin:0 });
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
      s.addText(rt(st, { color:C.INK }), { x:x+1.05, y:y+0.2, w:cw-1.3, h:ch-0.4, fontFace:F, fontSize:22, align:'left', valign:'middle', margin:0, lineSpacingMultiple:1.2 });
    });
    if(note) s.addText(rt(note, { color:C.MUTED2 }), { x:MX, y:6.45, w: badge?6.9:XL, h:0.5, fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0 });
    if(badge) this._badge(s, badge);
    return this;
  }

  // 大圖 + 右側說明（Venn 圖／示意圖專用）
  figure({ title, draw, image, caption, side, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const fw = 7.0, fh = 4.5, fy = 1.6;
    s.addShape('roundRect', { x:MX, y:fy, w:fw, h:fh, rectRadius:0.1, fill:{ color:C.WHITE }, line:{ color:C.EDGE, width:1 } });
    if(draw) draw(s, MX+0.25, fy+0.25, fw-0.5, fh-(caption?1.05:0.5));
    if(image) s.addImage({ path:image, x:MX+0.4, y:fy+0.3, w:fw-0.8, h:fh-(caption?1.15:0.6), sizing:{ type:'contain', w:fw-0.8, h:fh-(caption?1.15:0.6) } });
    if(caption) s.addText(rt(caption, { bold:true, color:C.HEAD }), { x:MX, y:fy+fh-0.75, w:fw, h:0.6, fontFace:F, fontSize:21, align:'center', valign:'middle', margin:0 });
    if(side) s.addText(rtLines(side, { color:C.INK, fontSize:23 }),
      { x:MX+fw+0.45, y:fy+0.35, w:XL-fw-0.45, h:fh-0.7, fontFace:F, align:'left', valign:'top', margin:0, lineSpacingMultiple:1.35 });
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
      s.addText(rtLines(col.lines, { color:C.INK, fontSize:21 }),
        { x:x+0.3, y:y+1.15, w:cw-0.6, h:ch-1.35, fontFace:F, align:'left', valign:'top', margin:0, lineSpacingMultiple:1.25 });
    });
    // 有徽章時 note 收窄靠左，避免同右下角徽章疊字
    if(note) s.addText(rt(note, { color:C.MUTED2 }), { x:MX, y: badge?6.45:6.15, w: badge?6.9:XL, h:0.5, fontFace:F, fontSize:20, align: badge?'left':'center', valign:'middle', margin:0 });
    if(badge) this._badge(s, badge);
    return this;
  }

  // 綜合除法陣列：係數行 → 乘積行 → 橫線 → 結果行，最右一欄係餘式
  // top/mid/bot 長度要一致；空格用 '' 表示（唔畫格）
  synthDiv({ title, c, top, mid, bot, cLabel='除式常數變號', note, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const n = top.length;
    const cw = Math.min(1.62, (XL - 1.55) / n);
    const rh = 0.74, x0 = MX + 1.55, y0 = 2.55;
    // 左邊 c 格（標籤位要夠闊，唔好迫到兩行又逼爆格）
    s.addShape('roundRect', { x:MX, y:y0+rh*0.5, w:1.30, h:rh, rectRadius:0.06, fill:{ color:C.ACCENT } });
    s.addText(rt(String(c), { bold:true, color:C.WHITE }), { x:MX, y:y0+rh*0.5, w:1.30, h:rh, fontFace:F, fontSize:27, align:'center', valign:'middle', margin:0 });
    s.addText(cLabel, { x:MX-0.35, y:y0-0.56, w:2.0, h:0.46, fontFace:F, fontSize:16, bold:true, color:C.MUTED2, align:'center', valign:'middle', margin:0 });
    // 三行格仔
    [top, mid, bot].forEach((row, ri) => {
      const y = y0 + ri*rh;
      row.forEach((v, ci) => {
        if (v === '' || v === null || v === undefined) return;
        const x = x0 + ci*cw;
        s.addShape('roundRect', { x, y, w:cw-0.08, h:rh-0.08, rectRadius:0.05,
          fill:{ color: ri===2 ? C.BLOCK : C.WHITE }, line:{ color:C.EDGE, width:1 } });
        s.addText(rt(String(v), { bold: ri===2, color:C.INK }),
          { x, y, w:cw-0.08, h:rh-0.08, fontFace:F, fontSize:27, align:'center', valign:'middle', margin:0 });
      });
    });
    // 橫線（乘積行同結果行之間）
    s.addShape('line', { x:x0-0.06, y:y0+2*rh-0.05, w:n*cw, h:0, line:{ color:C.INK, width:2 } });
    // 商式／餘式標籤（唔淨靠一條直線分隔，直接寫字）
    const qw = (n-1)*cw - 0.08;
    s.addText('商式係數', { x:x0, y:y0+3*rh-0.02, w:qw, h:0.46, fontFace:F, fontSize:19, bold:true, color:C.HEAD, align:'center', valign:'middle', margin:0 });
    s.addText('餘式', { x:x0+(n-1)*cw, y:y0+3*rh-0.02, w:cw-0.08, h:0.46, fontFace:F, fontSize:19, bold:true, color:C.HEAD, align:'center', valign:'middle', margin:0 });
    // note 收上嚟就唔會同陣列之間留一大浸吉位；接受字串或多行陣列
    if(note) s.addText(Array.isArray(note) ? rtLines(note, { color:C.MUTED2 }) : rt(note, { color:C.MUTED2 }),
      { x:MX, y:5.72, w: badge?6.9:XL, h:0.86, fontFace:F, fontSize:20, align:'left', valign:'middle', margin:0, lineSpacingMultiple:1.3 });
    if(badge) this._badge(s, badge);
    return this;
  }

  // 三欄圖示（標題自訂，唔似 cra 鎖死「具體／表徵／抽象」）
  threeFig({ title, panels, note, star, badge }){
    const s = this._content(); this._title(s, title, star);
    const cw = 3.83, gap = 0.30, y = 1.6, ph = 4.35;
    const xs = [MX, MX+cw+gap, MX+2*(cw+gap)];
    panels.slice(0,3).forEach((pn, i) => {
      const x = xs[i];
      s.addShape('roundRect', { x, y, w:cw, h:ph, rectRadius:0.08, fill:{ color:C.WHITE }, line:{ color:C.EDGE, width:1 } });
      s.addShape('roundRect', { x, y, w:cw, h:0.62, rectRadius:0.08, fill:{ color:C.ACCENT } });
      s.addText(rt(pn.head, { bold:true, color:C.WHITE }), { x, y, w:cw, h:0.62, fontFace:F, fontSize:21, align:'center', valign:'middle', margin:0 });
      if(pn.draw) pn.draw(s, x+0.15, y+0.75, cw-0.3, 2.55);
      if(pn.text) s.addText(rtLines(pn.text, { color:C.INK, fontSize:20 }),
        { x:x+0.25, y:y+3.35, w:cw-0.5, h:0.85, fontFace:F, align:'center', valign:'middle', margin:0, lineSpacingMultiple:1.2 });
    });
    if(note) s.addText(rt(note, { bold:true, color:C.HEAD }), { x:MX, y:6.15, w:XL, h:0.7, fontFace:F, fontSize:21, align:'center', valign:'middle', margin:0 });
    if(badge) this._badge(s, badge);
    return this;
  }

  summary({ title='今日帶走', takeaway, lines, star }){
    const s = this._content(); this._title(s, title, star);
    s.addShape('roundRect', { x:MX, y:1.75, w:XL, h:1.7, rectRadius:0.1, fill:{ color:C.ACCENT } });
    s.addText(rt(takeaway, { bold:true, color:C.WHITE }), { x:MX+0.4, y:1.75, w:XL-0.8, h:1.7, fontFace:F, fontSize:30, align:'center', valign:'middle', margin:0 });
    s.addText('保底三句', { x:MX, y:3.75, w:XL, h:0.5, fontFace:F, fontSize:20, bold:true, color:C.MUTED2, align:'left', margin:0 });
    s.addShape('roundRect', { x:MX, y:4.25, w:XL, h:2.35, rectRadius:0.1, fill:{ color:C.BLOCK }, line:{ color:C.EDGE, width:1 } });
    s.addText(rtLines(lines, { color:C.INK, fontSize:24, bold:true }),
      { x:MX+0.5, y:4.45, w:XL-1.0, h:1.95, fontFace:F, align:'left', valign:'middle', margin:0, lineSpacingMultiple:1.35 });
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

// 線段（pptxgenjs 嘅 line 預設由左上去右下；斜上就要 flipV）
function seg(s, x1, y1, x2, y2, color = C.INK, width = 2){
  const o = { x:Math.min(x1,x2), y:Math.min(y1,y2), w:Math.abs(x2-x1), h:Math.abs(y2-y1), line:{ color, width } };
  if ((x2-x1)*(y2-y1) < 0) o.flipV = true;
  s.addShape('line', o);
}

// 拋物線（a>0，開口向上）+ x 軸。mode: 'two'（Δ>0）｜'one'（Δ=0）｜'none'（Δ<0）
// 用 24 段折線逼近曲線 —— pptxgenjs 畫唔到真曲線，但夠滑順。
function drawParabola({ mode = 'two', roots = ['x_{1}', 'x_{2}'], caption } = {}){
  return (s, x, y, w, h) => {
    const ah = h * (caption ? 0.80 : 0.94);
    const cx = x + w/2, halfW = w*0.34;
    // 三格用同一條拋物線，郁嘅係 x 軸高度 —— 數學上真係咁（Δ 變 = 條線相對 x 軸上下移），
    // 視覺上又保持一致。頂點固定喺 0.78ah、高度 0.68ah → 曲線頂 = y+0.10ah，唔會切頂。
    const vy = y + ah*0.78, curveH = ah*0.68, dUp = ah*0.16;
    const axY = mode === 'two' ? vy - dUp : (mode === 'one' ? vy : vy + ah*0.08);
    // x 軸（先畫，等曲線壓喺上面）
    s.addShape('line', { x:x+0.06, y:axY, w:w-0.12, h:0, line:{ color:C.INK, width:1.5, endArrowType:'triangle' } });
    s.addText('x', { x:x+w-0.42, y:axY+0.02, w:0.4, h:0.34, fontFace:F, fontSize:16, color:C.INK, align:'center', valign:'middle', margin:0 });
    // 拋物線
    const N = 24, px = t => cx + t*halfW, py = t => vy - curveH*t*t;
    for (let i = 0; i < N; i++){
      const t1 = -1 + 2*i/N, t2 = -1 + 2*(i+1)/N;
      seg(s, px(t1), py(t1), px(t2), py(t2), C.ACCENT, 2.75);
    }
    // 交點
    if (mode === 'two'){
      const t = Math.sqrt(dUp/curveH);
      [-t, t].forEach((tt, i) => {
        const mx = px(tt);
        s.addShape('ellipse', { x:mx-0.085, y:axY-0.085, w:0.17, h:0.17, fill:{ color:C.INK } });
        s.addText(rt(roots[i] || '', { bold:true, color:C.INK }), { x:mx-0.45, y:axY+0.10, w:0.9, h:0.38, fontFace:F, fontSize:17, align:'center', valign:'middle', margin:0 });
      });
    } else if (mode === 'one'){
      s.addShape('ellipse', { x:cx-0.085, y:axY-0.085, w:0.17, h:0.17, fill:{ color:C.INK } });
      s.addText(rt(roots[0] || '', { bold:true, color:C.INK }), { x:cx-0.45, y:axY+0.10, w:0.9, h:0.38, fontFace:F, fontSize:17, align:'center', valign:'middle', margin:0 });
    }
    if (caption) s.addText(rt(caption, { color:C.MUTED2 }), { x, y:y+ah+0.02, w, h:0.4, fontFace:F, fontSize:17, align:'center', valign:'middle', margin:0 });
  };
}

// 數線 + 解集陰影。marks: [{t:0..1, label}]；shade: 'middle'｜'outside'
// 空心圈 = 唔包括該點（嚴格不等號）；陰影用半透明色帶，黑白列印仍見深淺。
function drawNumberLine({ marks = [], shade, caption } = {}){
  return (s, x, y, w, h) => {
    const lh = h * (caption ? 0.78 : 0.92);
    const ly = y + lh*0.52, x0 = x + w*0.16, x1 = x + w*0.84;
    const px = t => x0 + t*(x1 - x0);
    const lo = x + 0.26, hi = x + w - 0.26;   // 色帶要收喺箭嘴以內，唔可以衝出數線
    const bands = [];
    if (shade === 'middle'  && marks.length >= 2) bands.push([px(marks[0].t), px(marks[1].t)]);
    if (shade === 'outside' && marks.length >= 2){ bands.push([lo, px(marks[0].t)]); bands.push([px(marks[1].t), hi]); }
    bands.forEach(([a, b]) => s.addShape('rect', { x:a, y:ly-0.14, w:Math.max(b-a, 0.02), h:0.28, fill:{ color:C.ACCENT, transparency:40 } }));
    s.addShape('line', { x:x+0.08, y:ly, w:w-0.16, h:0, line:{ color:C.INK, width:2, beginArrowType:'triangle', endArrowType:'triangle' } });
    marks.forEach(m => {
      const mx = px(m.t);
      // 實心 = 包括呢點（≥／≤）；空心 = 唔包括（>／<）
      s.addShape('ellipse', { x:mx-0.10, y:ly-0.10, w:0.20, h:0.20, fill:{ color: m.filled ? C.INK : C.WHITE }, line:{ color:C.INK, width:2.25 } });
      s.addText(rt(m.label, { bold:true, color:C.INK }), { x:mx-0.55, y:ly+0.16, w:1.1, h:0.40, fontFace:F, fontSize:20, align:'center', valign:'middle', margin:0 });
    });
    if (caption) s.addText(rt(caption, { color:C.MUTED2 }), { x, y:y+lh+0.02, w, h:0.4, fontFace:F, fontSize:17, align:'center', valign:'middle', margin:0 });
  };
}

module.exports = { Deck, C, F, rt, rtLines, drawGroup, drawVenn, drawComplement, drawSubset,
                   seg, drawParabola, drawNumberLine };
