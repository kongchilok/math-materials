# 一課重出：python make_lesson.py <build模組名> <單元名>  （出 docx＋html＋pdf，並在 _tmp_prev_*.png 留預覽圖，看完請刪）
import sys, glob, importlib, fitz, os
sys.stdout.reconfigure(encoding='utf-8')
import cx_common as C
mod = sys.argv[1]; short = sys.argv[2]
m = importlib.import_module(mod)
for x in C.build(m.Hd, m.Pr, m.UNIT, short): print(x)
for f in glob.glob('_tmp_prev_*.png'): os.remove(f)
for k in ['講義', '練習']:
    stem = f'{k}_{short}_抽離小班共用版'
    C.html_to_pdf(stem + '.html', stem + '.pdf')
    d = fitz.open(stem + '.pdf'); print(k, 'pages', d.page_count)
    for i, pg in enumerate(d): pg.get_pixmap(dpi=75).save(f'_tmp_prev_{k}_{i+1}.png')
    d.close()
