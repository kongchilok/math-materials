// gen.js — 產生某年的「學生版工作紙」與「教師版」HTML
// 用法： node gen.js <年份>      例： node gen.js 2024
// 需要 data/ALL.json（由 extract.js 產生）與 solutions/sol<年>.js（教師版詳解；缺少時只出學生版）
// 輸出： output/四校聯考數學工作紙_<年>.html、output/四校聯考數學教師版_<年>.html
const fs = require("fs");
const path = require("path");

const YEAR = process.argv[2];
if (!YEAR) { console.error("請提供年份，例： node gen.js 2024"); process.exit(1); }

const ALL = JSON.parse(fs.readFileSync(path.join(__dirname, "data", "ALL.json"), "utf8"));
const data = ALL[YEAR];
if (!data) { console.error(`ALL.json 沒有 ${YEAR} 年資料`); process.exit(1); }

let TSOL = null;
const solFile = path.join(__dirname, "solutions", `sol${YEAR}.js`);
if (fs.existsSync(solFile)) TSOL = require(solFile);
else console.warn(`（注意）找不到 ${solFile}，本次只產生學生版；教師版需先撰寫該年詳解。`);

const KEYS = ["A", "B", "C", "D", "E"];

// 圖片覆蓋表（imageoverrides.js）：{ 年: { choice:{n:{file,big}}, solution:{n:{file,big}} } }
let IMG = {};
const ovFile = path.join(__dirname, "imageoverrides.js");
if (fs.existsSync(ovFile)) IMG = require(ovFile);
function mimeOf(f) { f = f.toLowerCase(); if (f.endsWith(".svg")) return "image/svg+xml"; if (f.endsWith(".jpg") || f.endsWith(".jpeg")) return "image/jpeg"; if (f.endsWith(".gif")) return "image/gif"; return "image/png"; }
function imgData(file) { const b = fs.readFileSync(path.join(__dirname, "images", file)).toString("base64"); return `data:${mimeOf(file)};base64,${b}`; }
function overrideFor(kind, n) { const y = IMG[YEAR]; if (!y || !y[kind]) return null; return y[kind][n] || null; }

// 只在數學分隔符 \(...\) 與 \[...\] 內，把 < > & 轉為 HTML 實體（避免瀏覽器把 <字母 當標籤；body 的 <br> 等不受影響）
function protectMath(s) {
  if (s == null) return s;
  return String(s).replace(/\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]/g, m =>
    m.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"));
}

// ---------- helpers ----------
const ruled = n => '<div class="rules">' + '<div class="rule"></div>'.repeat(n) + '</div>';
function imgHtml(kind, q, floatCls) {
  const ov = overrideFor(kind, q.n);
  let src = q.img, big = false;
  if (ov) { src = imgData(ov.file); big = !!ov.big; }
  if (!src) return "";
  if (big) return `<div class="q-img img-big"><img src="${src}" alt="第${q.n}題圖示"></div>`;
  return `<div class="q-img ${floatCls || ""}"><img src="${src}" alt="第${q.n}題圖示"></div>`;
}
const formulaBox = q => (q.formula && q.formula.length)
  ? `<div class="box formula"><span class="lbl">相關公式</span><ul>${q.formula.map(f=>`<li>${protectMath(f)}</li>`).join("")}</ul></div>` : "";
const hintBox = q => q.hint ? `<div class="box hint"><span class="lbl">方向提示</span>${protectMath(q.hint)}</div>` : "";
const optionsHtml = q => (q.options && q.options.length)
  ? '<div class="opts">' + q.options.map((o,i)=>`<span class="opt"><span class="opt-key">(${KEYS[i]})</span><span class="opt-txt">${protectMath(o)}</span></span>`).join("") + '</div>' : "";
function alignedBlock(math) {
  const lines = math.split("\n").map(s=>s.trim()).filter(Boolean);
  return protectMath(`\\[\\begin{aligned}\n${lines.join(" \\\\\n")}\n\\end{aligned}\\]`);
}
function regionsHtml(parts) {
  return parts.map(p => {
    const title = p.title ? `<div class="part">${protectMath(p.title)}</div>` : "";
    const row = '<div class="row">' + p.regions.map(rg =>
      `<div class="region"><span class="region-h">${protectMath(rg.h)}</span><div class="math">${alignedBlock(rg.math)}</div></div>`
    ).join("") + '</div>';
    return title + row;
  }).join("");
}

// ---------- 學生版（無詳解時：純書寫格線版） ----------
function stuChoice(q) {
  return `<div class="q">
  <div class="q-head"><span class="q-no">${q.n}.</span><span class="q-tag">${q.type||""}</span></div>
  ${imgHtml("choice",q,"img-float")}
  <div class="q-body">${protectMath(q.body)}</div>
  ${optionsHtml(q)}
  <div class="clear"></div>
  ${formulaBox(q)}
  ${hintBox(q)}
  <div class="work work-mc">${ruled(3)}</div>
  <div class="ans-line">答案：<span class="ans-box"></span></div>
</div>`;
}
function stuSolution(q) {
  return `<div class="q q-long">
  <div class="q-head"><span class="q-no">解答第 ${q.n} 題</span><span class="q-tag">${q.type||""}</span></div>
  ${imgHtml("solution",q,"img-float")}
  <div class="q-body">${protectMath(q.body)}</div>
  <div class="clear"></div>
  ${formulaBox(q)}
  ${hintBox(q)}
  <div class="work work-sol"><span class="work-lbl">解答過程</span>${ruled(40)}</div>
</div>`;
}

// ---------- 學生版（有詳解時：填空骨架版） ----------
// 用教師版工序分區當骨架：保留「工序N·所求」標題，內部依步驟數留純空白框
function blankRegionsHtml(parts) {
  return parts.map(p => {
    const title = p.title ? `<div class="part">${protectMath(p.title)}</div>` : "";
    const row = '<div class="row">' + p.regions.map(rg => {
      const lines = rg.math.split("\n").map(s=>s.trim()).filter(Boolean).length;
      const h = (lines * 0.9 + 0.3).toFixed(2); // 高度依步驟數
      return `<div class="region"><span class="region-h">${protectMath(rg.h)}</span><div class="fill" style="height:${h}cm"></div></div>`;
    }).join("") + '</div>';
    return title + row;
  }).join("");
}
function stuChoiceFill(q, t) {
  return `<div class="q">
  <div class="q-head"><span class="q-no">${q.n}.</span><span class="q-tag">${q.type||""}</span></div>
  ${imgHtml("choice",q,"img-float")}
  <div class="q-body">${protectMath(q.body)}</div>
  ${optionsHtml(q)}
  <div class="clear"></div>
  ${formulaBox(q)}
  ${hintBox(q)}
  ${blankRegionsHtml(t.parts)}
  <div class="ans-line">答案：<span class="ans-box"></span></div>
</div>`;
}
function stuSolutionFill(q, t) {
  return `<div class="q">
  <div class="q-head"><span class="q-no">解答第 ${q.n} 題</span><span class="q-tag">${q.type||""}</span></div>
  ${imgHtml("solution",q,"img-float")}
  <div class="q-body">${protectMath(q.body)}</div>
  <div class="clear"></div>
  ${formulaBox(q)}
  ${hintBox(q)}
  ${blankRegionsHtml(t.parts)}
</div>`;
}

function buildStudent() {
  const useScaffold = !!TSOL;
  const cc = data.choices.map(q => {
    const t = useScaffold ? TSOL.choice[q.n] : null;
    return t ? stuChoiceFill(q, t) : stuChoice(q);
  }).join("\n");

  let solSection;
  if (useScaffold) {
    const ss = data.solutions.map(q => stuSolutionFill(q, TSOL.solution[q.n])).join("\n");
    solSection = `
  <div class="sec-head sec-break">第二部分　解答題<span class="sec-sub">共 ${data.solutions.length} 題</span></div>
  ${ss}`;
  } else {
    const s = data.solutions;
    solSection = `
<div class="sol-fullpage">
  <div class="sec-head">第二部分　解答題<span class="sec-sub">共 ${s.length} 題，須列出完整步驟（每題一頁）</span></div>
  ${stuSolution(s[0])}
</div>
${s.slice(1).map(q=>`<div class="sol-fullpage">${stuSolution(q)}</div>`).join("\n")}`;
  }

  return pageWrap("學生版", `
  <div class="sec-head">第一部分　選擇題<span class="sec-sub">共 ${data.choices.length} 題</span></div>
  ${cc}
  ${solSection}`, false);
}

// ---------- 教師版 ----------
function teaChoice(q) {
  const t = TSOL.choice[q.n];
  if (!t) throw new Error(`solutions/sol${YEAR}.js 缺少選擇題 ${q.n} 的詳解`);
  return `<div class="tq">
  <div class="q-head"><span class="q-no">${q.n}.</span><span class="q-type">${q.type||""}</span></div>
  ${imgHtml("choice",q,"img-float")}
  <div class="q-body">${protectMath(q.body)}</div>
  <div class="clear"></div>
  ${formulaBox(q)}
  <div class="box ans"><span class="lbl">正確答案</span>${protectMath(t.ans)}</div>
  <div class="sol-title">詳細解題過程（工序分析法）</div>
  ${regionsHtml(t.parts)}
</div>`;
}
function teaSolution(q) {
  const t = TSOL.solution[q.n];
  if (!t) throw new Error(`solutions/sol${YEAR}.js 缺少解答題 ${q.n} 的詳解`);
  return `<div class="tq tq-break">
  <div class="q-head"><span class="q-no">解答第 ${q.n} 題</span><span class="q-type">${q.type||""}</span></div>
  ${imgHtml("solution",q,"img-float")}
  <div class="q-body">${protectMath(q.body)}</div>
  <div class="clear"></div>
  ${formulaBox(q)}
  <div class="box ans"><span class="lbl">參考答案</span>${protectMath(t.ans)}</div>
  <div class="sol-title">詳細解題過程（工序分析法）</div>
  ${regionsHtml(t.parts)}
</div>`;
}
function buildTeacher() {
  const cc = data.choices.map(teaChoice).join("\n");
  const ss = data.solutions.map(teaSolution).join("\n");
  return pageWrap("教師版", `
  <div class="sec-head">第一部分　選擇題<span class="sec-sub">共 ${data.choices.length} 題 · 含正確答案與詳解</span></div>
  ${cc}
  <div class="sec-head sec-break">第二部分　解答題<span class="sec-sub">共 ${data.solutions.length} 題 · 含參考答案與詳解</span></div>
  ${ss}`, true);
}

// ---------- 共用頁框 / CSS ----------
function pageWrap(variant, inner, isTeacher) {
  const tag = isTeacher ? `<span class="ws-tag">教師版</span>` : "";
  const meta = isTeacher ? "" : `
    <div class="ws-meta"><div>姓名：<span class="u"></span></div><div>班別：<span class="u"></span></div><div>學號：<span class="u"></span></div></div>
    <div class="ws-note">選擇題請寫出計算過程並於「答案」欄填代號；解答題請在格線內完整列出步驟。</div>`;
  return `<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="UTF-8">
<title>澳門四校聯考 ${YEAR} 數學正卷 ${variant}</title>
<script>
MathJax = { tex:{inlineMath:[['\\\\(','\\\\)']],displayMath:[['\\\\[','\\\\]']]}, svg:{fontCache:'global',displayAlign:'left',displayIndent:'0'} };
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js"></script>
<style>
  @page { size:A4; margin:0.5cm 1cm 1cm 1cm; }
  * { box-sizing:border-box; }
  html { font-size:12pt; }
  body { font-family:"Noto Serif TC","Times New Roman","Songti TC",serif; color:#111; line-height:1.5; margin:0; padding:0; background:#f3f3f3; }
  .sheet { max-width:820px; margin:0 auto; background:#fff; padding:0.5cm 1cm 1cm; }
  .ws-header { border-bottom:2px solid #111; padding-bottom:5px; margin-bottom:8px; }
  .ws-title { font-size:14pt; font-weight:700; letter-spacing:0.04em; }
  .ws-tag { display:inline-block; font-size:10pt; background:#b6532c; color:#fff; padding:1px 10px; border-radius:99px; margin-left:8px; vertical-align:middle; }
  .ws-meta { display:flex; gap:26px; margin-top:5px; font-size:11pt; }
  .ws-meta .u { display:inline-block; min-width:110px; border-bottom:1px solid #111; }
  .ws-note { font-size:9.5pt; color:#555; margin-top:4px; }

  .sec-head { font-size:12pt; font-weight:700; margin:10px 0 8px; padding:3px 10px; background:#1d1c1a; color:#fff; border-radius:3px; break-after:avoid; }
  .sec-head .sec-sub { font-size:9pt; font-weight:400; color:#d8d2c4; margin-left:8px; }
  .sec-break { page-break-before:always; }

  .q-head { display:flex; align-items:baseline; gap:9px; margin-bottom:3px; }
  .q-no { font-weight:700; font-size:12pt; color:#b6532c; }
  .q-tag,.q-type { font-size:8.5pt; color:#888; border:1px solid #ddd; border-radius:99px; padding:0 8px; }
  .q-body { font-size:12pt; }

  .img-float { float:right; margin:0 0 6px 14px; text-align:center; }
  .img-float img { max-width:240px; max-height:180px; height:auto; border:1px solid #e3e1d8; background:#fff; }
  .img-big { clear:both; text-align:center; margin:8px 0; }
  .img-big img { max-width:96%; max-height:320px; height:auto; border:1px solid #e3e1d8; background:#fff; }
  .clear { clear:both; }

  .box { border-radius:4px; padding:5px 11px; margin:6px 0; font-size:10.5pt; }
  .box ul { margin:2px 0 0; padding-left:20px; } .box li { margin:1px 0; }
  .formula { background:#eef3f5; border:1px solid #a9c4cc; } .formula .lbl { font-weight:700; color:#2a5560; margin-right:6px; }
  .hint { background:#f5f0e3; border:1px solid #d6bf86; color:#6a5212; } .hint .lbl { font-weight:700; color:#8a6a1e; margin-right:6px; }
  .ans { background:#e3f0e8; border:1px solid #7fb89a; } .ans .lbl { font-weight:700; color:#2f6b4f; margin-right:6px; }

  .opts { margin:6px 0 2px; display:flex; flex-wrap:wrap; gap:6px 22px; }
  .opt { display:inline-flex; align-items:baseline; gap:5px; font-size:11.5pt; white-space:nowrap; }
  .opt-key { font-weight:700; color:#2a5560; }

  .q { border:1px solid #d8d6cd; border-radius:4px; padding:8px 12px 10px; margin-bottom:9px; page-break-inside:avoid; overflow:hidden; }
  .work { margin-top:10px; border:1px solid #c9c7bd; border-radius:3px; overflow:hidden; display:flex; flex-direction:column; background:#fff; }
  .work-lbl { flex:0 0 auto; font-size:8.5pt; color:#aaa; padding:2px 0 0 8px; }
  .rules { flex:1 1 auto; overflow:hidden; }
  .rule { height:0.82cm; border-bottom:1px solid #d4dadd; } .rule:last-child { border-bottom:none; }
  .work-mc { min-height:2.46cm; }
  .ans-line { margin-top:7px; font-size:11pt; font-weight:600; }
  .ans-box { display:inline-block; min-width:130px; border-bottom:1.5px solid #111; height:1.1em; vertical-align:bottom; }
  .sol-fullpage { height:27.4cm; display:flex; flex-direction:column; page-break-before:always; overflow:hidden; }
  .sol-fullpage .sec-head { flex:0 0 auto; }
  .sol-fullpage .q-long { flex:1 1 auto; }
  .q-long { display:flex; flex-direction:column; page-break-inside:avoid; }
  .q-long .work-sol { flex:1 1 auto; margin-top:8px; }

  .tq { border:1px solid #d8d6cd; border-radius:4px; padding:8px 13px 10px; margin-bottom:10px; }
  .tq-break { page-break-inside:avoid; }
  .sol-title { font-weight:700; font-size:11pt; margin:9px 0 4px; padding-bottom:2px; border-bottom:1.5px solid #1d1c1a; }
  .part { font-weight:700; color:#b6532c; margin:7px 0 4px; font-size:11pt; }
  .row { display:flex; gap:9px; align-items:stretch; flex-wrap:wrap; margin-bottom:3px; }
  .region { flex:1 1 auto; border:1px solid #d8d6cd; border-radius:5px; padding:4px 10px 6px; break-inside:avoid; }
  .region-h { font-size:9.5pt; font-weight:700; color:#fff; background:#2a5560; border-radius:3px; padding:1px 8px; display:inline-block; margin-bottom:3px; }
  .region .math { font-size:10.5pt; }
  .region .math mjx-container { margin:0 !important; }
  .fill { margin-top:3px; border-top:1px dashed #e0ddd2; background:#fcfcfa; }
</style></head><body>
<div class="sheet">
  <div class="ws-header">
    <div class="ws-title">澳門四校聯考　${YEAR} 年試題　數學正卷${tag}</div>${meta}
  </div>
  ${inner}
</div></body></html>`;
}

const outDir = path.join(__dirname, "output");
fs.mkdirSync(outDir, { recursive: true });
const stuPath = path.join(outDir, `四校聯考數學工作紙_${YEAR}.html`);
fs.writeFileSync(stuPath, buildStudent(), "utf8");
console.log("學生版：", stuPath);
if (TSOL) {
  const teaPath = path.join(outDir, `四校聯考數學教師版_${YEAR}.html`);
  fs.writeFileSync(teaPath, buildTeacher(), "utf8");
  console.log("教師版：", teaPath);
}
