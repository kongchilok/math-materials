// 圖片覆蓋表：補上題庫缺圖的題目，或替換／放大既有圖。
// 結構： { "年": { choice:{ 題號:{file, big} }, solution:{ 題號:{file, big} } } }
// file 對應 images/ 內的檔名；big:true 時圖片不浮動、置中放大、自成一行。
module.exports = {
  "2017": { solution: { 2: { file: "2017_s2.png" } } },
  "2019": { solution: { 2: { file: "2019_s2.svg" } } },
  "2020": {
    choice:   { 12: { file: "2020_c12.png" }, 14: { file: "2020_c14.png" } },
    solution: { 5:  { file: "2020_s5.png" } },
  },
  "2022": { choice: { 9: { file: "2022_c9.png", big: true } } },
  "2026": { solution: { 4: { file: "2026_s4.svg" } } },
};
