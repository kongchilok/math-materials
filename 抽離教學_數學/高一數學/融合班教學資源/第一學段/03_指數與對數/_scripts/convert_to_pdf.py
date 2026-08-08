#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
from pathlib import Path

# 要轉換的檔案清單
base_path = r"C:\Users\KongChiLok\notebookLM\高一講義\4.1-4.4 指數與對數（含指數對數方程）融合班教學資源_高一數學_第一學段\融合班講義"
files_to_convert = [
    "講義_4.2指數函數_融合版.docx",
    "練習_4.2指數函數_融合版.docx",
    "講義_4.3反函數_融合版.docx",
    "練習_4.3反函數_融合版.docx",
    "講義_4.4對數函數_融合版.docx",
    "練習_4.4對數函數_融合版.docx",
]

# 使用 PowerShell + Word COM 轉換
for filename in files_to_convert:
    docx_path = os.path.join(base_path, filename)
    pdf_filename = filename.replace('.docx', '.pdf')
    pdf_path = os.path.join(base_path, pdf_filename)

    if not os.path.exists(docx_path):
        print(f"跳過：{filename}（檔案不存在）")
        continue

    # 用 PowerShell 呼叫 Word COM
    ps_script = f'''
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$d = $w.Documents.Open('{docx_path}')
$d.SaveAs2('{pdf_path}', 17)
$d.Close()
$w.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($w) | Out-Null
"已轉換：{pdf_filename}"
'''

    try:
        result = subprocess.run(
            ['powershell', '-NoProfile', '-Command', ps_script],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0:
            print(f"✓ {pdf_filename} 轉換成功")
        else:
            print(f"✗ {pdf_filename} 轉換失敗：{result.stderr}")
    except subprocess.TimeoutExpired:
        print(f"✗ {pdf_filename} 轉換逾時")
    except Exception as e:
        print(f"✗ {pdf_filename} 轉換錯誤：{e}")

print("\n所有 docx → PDF 轉換完成")
