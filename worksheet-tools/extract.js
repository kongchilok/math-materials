// extract.js — 從來源 HTML 抽出 const ALL = {...} 存成 data/ALL.json
// 用法： node extract.js ["來源HTML路徑"]
//   省略路徑時，預設用桌面的「四校聯考數學正卷_練習_2017-2026_測試版.html」
const fs = require("fs");
const path = require("path");

const DEFAULT_SRC = "C:/Users/KongChiLok/Desktop/四校聯考數學正卷_練習_2017-2026_測試版.html";
const srcPath = process.argv[2] || DEFAULT_SRC;
const outPath = path.join(__dirname, "data", "ALL.json");

const html = fs.readFileSync(srcPath, "utf8");
const i = html.indexOf("const ALL = ");
if (i < 0) { console.error("找不到 const ALL ="); process.exit(1); }
const start = html.indexOf("{", i);
let depth = 0, inStr = false, esc = false, end = -1;
for (let j = start; j < html.length; j++) {
  const c = html[j];
  if (inStr) {
    if (esc) esc = false;
    else if (c === "\\") esc = true;
    else if (c === '"') inStr = false;
  } else {
    if (c === '"') inStr = true;
    else if (c === "{") depth++;
    else if (c === "}") { depth--; if (depth === 0) { end = j + 1; break; } }
  }
}
const ALL = JSON.parse(html.slice(start, end));
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(ALL), "utf8");
const years = Object.keys(ALL).sort();
console.log("已寫入", outPath);
console.log("年份：", years.join(", "));
years.forEach(y => console.log(`  ${y}: 選擇 ${ALL[y].choices.length} 題、解答 ${ALL[y].solutions.length} 題`));
