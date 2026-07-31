#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""掃描並批量上傳高一高二檔案"""

import subprocess
import os
import sys
from pathlib import Path

# 強制 stdout 使用 UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 單元對應
units = {
    "01_集合與常用邏輯用語": "13564236-e41b-4dc6-aa5c-d618a147233e",
    "02_函數的概念與性質": "1590dc99-ca39-4902-ba42-a28cde9682a3",
    "03_指數與對數": "410544c4-9508-46d2-bd22-b7a600a1676d",
    "01_三角函數": "ed589a78-927a-4910-908e-dc863144ddd2",
    "02_平面向量與正餘弦定理": "f7c75aa4-f2b2-438b-b068-5e34e7746175",
    "03_立體幾何初步": "a88b4200-e742-428e-8f79-3d5fd253216b",
    "04_多項式與因式定理": "cd53c5b6-8104-4746-b949-f6e8d0723035",
    "01_直線的傾斜角與斜率": "a01e782a-5746-4bf5-b72f-fe105e86f301",
    "02_圓的方程與直線圓位置關係": "19ccc58d-09a2-4edf-b21f-a30b9fc45abf",
    "03_圓錐曲線": "690635ab-8504-4583-a3dd-5d043311eef7",
    "01_數列": "6daa6562-75f5-4e02-b922-11a7faf68733",
    "04_不等式的性質與基本不等式": "c3101402-0a44-4d4a-9245-5a051389abbe",
    "02_排列組合與概率": "ba1d8f54-1f99-4941-b17b-f1645c946bfe",
}

base = Path("C:/Users/KongChiLok/notebookLM/抽離教學_數學")
total = 0
uploaded = 0

# 掃描高一高二所有符合的資料夾
for grade_dir in ["高一數學", "高二數學"]:
    grade_path = base / grade_dir / "融合班教學資源"
    if not grade_path.exists():
        continue

    for unit_name, notebook_id in units.items():
        # 找包含該單元名的資料夾
        for segment_dir in grade_path.glob("第*學段"):
            for unit_dir in segment_dir.glob(f"*{unit_name}*"):
                if not unit_dir.is_dir():
                    continue

                # 掃描該資料夾的所有 docx 和 pdf
                files = [
                    f for f in unit_dir.glob("*.*")
                    if f.suffix in [".docx", ".pdf"] and not f.name.startswith("~$")
                ]

                if files:
                    print(f"\n【{unit_dir.name}】 {len(files)} files → {notebook_id}")
                    for f in files:
                        total += 1
                        try:
                            result = subprocess.run(
                                ["nlm", "sources", "add", "--notebook", notebook_id, "--file", str(f)],
                                capture_output=True, text=True, timeout=20
                            )
                            if result.returncode == 0:
                                print(f"  + {f.name}")
                                uploaded += 1
                            else:
                                err = result.stderr[:60] if result.stderr else "unknown error"
                                print(f"  ? {f.name} ({err})")
                        except Exception as e:
                            print(f"  ! {f.name} ({str(e)[:40]})")

print(f"\n=== Summary: {uploaded}/{total} files uploaded ===")
