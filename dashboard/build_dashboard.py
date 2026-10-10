"""정제 데이터(data/clean_production.csv)를 대시보드 HTML(docs/index.html)에 넣는다.

실행: python dashboard/build_dashboard.py   (analysis.ipynb를 먼저 실행해 CSV를 만든 뒤)
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
COLS = ['semi_prod', 'nonsemi_prod', 'semi_prod_ma12', 'nonsemi_prod_ma12',
        'semi_prod_yoy', 'nonsemi_prod_yoy', 'semi_inv_yoy']
PHASES = [
    ('① 슈퍼사이클', '2017-01', '2018-12'), ('② 다운사이클', '2019-01', '2019-12'),
    ('③ 코로나', '2020-01', '2020-12'), ('④ 비대면 특수', '2021-01', '2022-06'),
    ('⑤ 불황', '2022-07', '2023-06'), ('⑥ 회복', '2023-07', '2024-12'),
    ('⑦ AI·HBM 호황', '2025-01', '2026-07'),
]

df = pd.read_csv(ROOT / 'data' / 'clean_production.csv', index_col=0)
records = [
    {'month': m, **{c: (None if pd.isna(row[c]) else round(float(row[c]), 2)) for c in COLS}}
    for m, row in df.iterrows()
]
phases = [{'name': n, 's': s, 'e': e} for n, s, e in PHASES]

html = (ROOT / 'dashboard' / 'template.html').read_text(encoding='utf-8')
html = html.replace('__DATA__', json.dumps(records, ensure_ascii=False))
html = html.replace('__PHASES__', json.dumps(phases, ensure_ascii=False))
out = ROOT / 'docs' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding='utf-8')
print(f'대시보드 생성: {out} ({len(records)}개월)')
