// =====================================================================
// 投影可讀性計算器
// ---------------------------------------------------------------------
// 回答：「這套字級，在 <N> 吋螢幕、最遠 <D> 米的座位，看不看得清？」
//
// 兩套業界判準：
//  ① AVIXA/ANSI V202.01 DISCAS —— 基本決策用途（BDM，教學內容屬此類）：
//     最遠觀看距離 ≤ 150 × 文字高度。反推：文字高度 ≥ 距離 / 150。
//  ② 傳統 4/6/8 法則 —— 最遠座位 ≤ 4／6／8 倍「畫面高度」
//     （4＝細節判讀、6＝一般教學、8＝被動觀看）。
//
// 另計角分（arcminute）：拉丁字母約需 16–20 弧分才好讀，
// 中文筆畫密度高得多，實務上要 25–30 弧分才不會糊成一團 —— 本檔採 25 為門檻。
// =====================================================================
const T = require("./deck-tokens.js");
const { type, RULES } = T;

const SLIDE_H_IN = T.layout.H; // 7.5 in（LAYOUT_WIDE 邏輯高度）
const CJK_ARCMIN_MIN = 25;     // 中文可讀角分門檻
const LATIN_ARCMIN_MIN = 16;

// 16:9 螢幕：由對角線吋數求實際高度（公分）
function screenHeightCm(diagIn) {
  return diagIn * (9 / Math.hypot(16, 9)) * 2.54;
}
// N pt 文字在畫面上的實際高度（公分）
function glyphHeightCm(pt, diagIn) {
  return (pt / 72) / SLIDE_H_IN * screenHeightCm(diagIn);
}
// 角分
function arcmin(heightCm, distM) {
  return (heightCm / 100) / distM * 3438;
}
// DISCAS BDM：該距離所需的最小文字高度（公分）
function discasMinCm(distM) { return distM / 150 * 100; }
// 反推所需 pt
function requiredPt(distM, diagIn) {
  return Math.ceil(discasMinCm(distM) / screenHeightCm(diagIn) * SLIDE_H_IN * 72);
}

function reportRoom(diagIn, distances) {
  const hCm = screenHeightCm(diagIn);
  console.log(`\n${"=".repeat(72)}`);
  console.log(`螢幕 ${diagIn}"（16:9）→ 畫面高 ${hCm.toFixed(1)} cm、寬 ${(hCm * 16 / 9).toFixed(1)} cm`);
  console.log(`4/6/8 法則可服務距離：細節 ${(hCm * 4 / 100).toFixed(1)} m ／ 一般教學 ${(hCm * 6 / 100).toFixed(1)} m ／ 被動觀看 ${(hCm * 8 / 100).toFixed(1)} m`);
  console.log("=".repeat(72));

  // 各字級的實際高度
  const roles = [
    ["內文下限 bodySm", type.bodySm.fontSize],
    ["內文 body", type.body.fontSize],
    ["小標 headline", type.headline.fontSize],
    ["頁標題 title", type.title.fontSize],
    ["頁尾 caption", type.caption.fontSize],
  ];
  console.log("\n字級 → 螢幕實際字高");
  console.log("角色".padEnd(20) + "pt".padStart(5) + "字高cm".padStart(9));
  roles.forEach(([n, pt]) => {
    console.log(n.padEnd(18) + String(pt).padStart(5) + glyphHeightCm(pt, diagIn).toFixed(2).padStart(9));
  });

  console.log(`\n各距離的判定（以現行內文下限 ${type.bodySm.fontSize}pt 計）`);
  console.log("距離".padEnd(8) + "角分".padStart(7) + "DISCAS需要".padStart(12) + "實際".padStart(8) + "  判定");
  console.log("-".repeat(56));
  distances.forEach((dm) => {
    const g = glyphHeightCm(type.bodySm.fontSize, diagIn);
    const am = arcmin(g, dm);
    const need = discasMinCm(dm);
    const ok = g >= need && am >= CJK_ARCMIN_MIN;
    const marginal = !ok && am >= LATIN_ARCMIN_MIN;
    console.log(
      `${dm} m`.padEnd(8) +
      am.toFixed(1).padStart(7) +
      `${need.toFixed(2)}cm`.padStart(12) +
      `${g.toFixed(2)}cm`.padStart(8) +
      "  " + (ok ? "足夠" : marginal ? "勉強（中文會糊）" : "**不足**")
    );
  });

  console.log("\n若要在該距離讀得舒服，內文最少需要：");
  distances.forEach((dm) => {
    console.log(`  ${dm} m → ${requiredPt(dm, diagIn)} pt`);
  });
}

// ---- 使用者的課室：50 m² 近正方形 ≈ 7.1 × 7.1 m ----
const ROOM_SIDE = Math.sqrt(50);
console.log(`課室：50 m² 近正方形 → 邊長約 ${ROOM_SIDE.toFixed(1)} m、對角線約 ${(ROOM_SIDE * Math.SQRT2).toFixed(1)} m`);
console.log("最遠座位：正對螢幕約 6.5 m（扣去講台）／坐對角最遠約 9 m");

reportRoom(65, [3, 4.5, 5, 6.5, 9]);
reportRoom(75, [3, 4.5, 5, 6.5, 9]);

// ---- 20 m 需要多大螢幕？----
console.log(`\n${"=".repeat(72)}`);
console.log("若真的要在 20 m 外讀 20pt 內文，需要多大螢幕？");
const needCm = discasMinCm(20);
const needScreenH = needCm / ((RULES.minBodyPt / 72) / SLIDE_H_IN);
const needDiag = needScreenH / 2.54 / (9 / Math.hypot(16, 9));
console.log(`  文字需高 ${needCm.toFixed(1)} cm → 畫面高需 ${(needScreenH / 100).toFixed(2)} m → 螢幕約 ${Math.round(needDiag)}"（${(needDiag * 2.54 / 100).toFixed(1)} m 對角）`);
console.log("  → 已屬戲院級規格，一般課室不可行；20 m 應為口誤。");
