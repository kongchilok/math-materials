// inv_draw.js — 初三 13 反比例函數．本單元共用設定
// 只放「呢個單元反覆用到」嘅嘢：雙曲線曲線段、標準坐標範圍。
// 通用底層（Deck／drawEq／eqJudge…）喺高一 01 soil_kit.js；坐標系 axes() 喺高一 02 fn_draw.js。
const KIT  = require('../../../../../高一數學/融合班教學資源/第一學段/01_集合與常用邏輯用語/教學簡報/_scripts/soil_kit.js');
const FN   = require('../../../../../高一數學/融合班教學資源/第一學段/02_函數的概念與性質/教學簡報/_scripts/fn_draw.js');

const RANGE = 7;                    // 標準視窗 [-7,7]×[-7,7]
const TICKS = [-6, -4, -2, 2, 4, 6];

// y = k/x 嘅兩支。|y| ≤ RANGE ⟹ |x| ≥ |k|/RANGE，所以由 xMin 起畫，唔會衝出頂。
function branches(k, { color, dash, width } = {}) {
  const xMin = Math.abs(k) / RANGE;
  const f = (x) => k / x;
  const o = { f, color, dash, width: width || 2.6, n: 40 };
  return [
    { ...o, from: xMin, to: RANGE },
    { ...o, from: -RANGE, to: -xMin },
  ];
}

// 本單元標準坐標圖：傳 k 就畫好兩支，其餘照 axes() 參數
function hyperbola(k, opts = {}) {
  const { extraCurves = [], ...rest } = opts;
  return FN.axes({
    xr: [-RANGE, RANGE], yr: [-RANGE, RANGE],
    xticks: TICKS, yticks: TICKS,
    curves: [...branches(k), ...extraCurves],
    ...rest,
  });
}

// 淨係坐標系＋點（描點頁用，未連線）
function plotOnly(opts = {}) {
  return FN.axes({
    xr: [-RANGE, RANGE], yr: [-RANGE, RANGE],
    xticks: TICKS, yticks: TICKS, curves: [],
    ...opts,
  });
}

module.exports = { KIT, FN, RANGE, TICKS, branches, hyperbola, plotOnly };
