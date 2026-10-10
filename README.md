# 반도체만 날았나? — 제조업 K자형 시계열 분석

반도체 및 부품(C26A)과 반도체 제외 제조업의 **생산·출하·재고지수(2017.01~2026.07, 월별 115개)**를 비교해,
반도체 호황이 다른 제조업으로 번졌는지 살펴본 시계열 트렌드 분석이다. (코디세이 AI 응용 미션 「데이터 기반 트렌드 분석」)

- 📄 **분석 리포트:** [REPORT.md](REPORT.md)
- 📊 **대시보드 (기간·국면 필터):** https://041211lhs.github.io/semiconductor-kshape-analysis/
- 📓 **분석 코드:** [analysis.ipynb](analysis.ipynb)

![대시보드 화면](images/08_dashboard.png)

## 핵심 결과 한 줄 요약
반도체 생산지수는 2017→2026년에 **2.1배**가 됐지만 나머지 제조업은 **+0.8%로 제자리**였다. 두 산업의 증가율 상관은 **0.08**로, 생산 단계에서 반도체 호황이 다른 제조업으로 번졌다는 신호는 약했다.

## 폴더 구조
```
semiconductor-kshape-analysis/
├─ data/
│  ├─ raw/kosis_production_index_2017_2026.xlsx   KOSIS 원본(수정하지 않음)
│  ├─ clean_production.csv                       정제·파생지표 (노트북이 생성)
│  └─ phase_stats.csv                            국면별 통계 (노트북이 생성)
├─ images/                                       그래프 01~07 + 대시보드 캡처 08
├─ analysis.ipynb                                분석 노트북
├─ dashboard/
│  ├─ template.html                              대시보드 화면 틀
│  └─ build_dashboard.py                         CSV → docs/index.html 생성
├─ docs/index.html                               대시보드(GitHub Pages 배포본)
├─ REPORT.md                                     분석 리포트
├─ PLAN.md                                       분석 계획서
└─ requirements.txt
```

## 실행 방법
```bash
# 1) 라이브러리 설치 (Python 3.10 이상)
pip install -r requirements.txt

# 2) 노트북 실행 → data/clean_production.csv, images/01~07 생성
jupyter nbconvert --to notebook --execute --inplace analysis.ipynb
#    (또는 VS Code / Jupyter에서 analysis.ipynb를 열고 위에서부터 차례로 실행)

# 3) 대시보드 생성 → docs/index.html
python dashboard/build_dashboard.py
```
`docs/index.html`은 더블클릭하면 브라우저에서 바로 열린다. 인터넷 연결이 필요하다(Plotly 라이브러리를 CDN에서 불러옴).

## 대시보드 사용 시나리오
1. **전체 기간**: 반도체 +113%, 비반도체 +0.8%, 상관 0.08 → K자형 격차를 확인한다.
2. **⑤ 불황** 버튼: 반도체 평균 증가율 -20.2%일 때 비반도체는 +0.3% → 같이 떨어지지 않았다.
3. **시작 2022-01 ~ 끝 2023-06**: 세 번째 그래프에서 재고 급증(초록) 뒤 생산 급감(파랑) 순서를 확인한다.
4. **추세 그래프 지표 → 원지수**: 이동평균에 가려진 월별 계절 요동을 확인한다.

## 데이터 출처 및 라이선스
- **출처:** 통계청 KOSIS 국가통계포털, 광업제조업동향조사 「기타분류별 광공업생산지수(2020=100)」 (https://kosis.kr)
- **수집 방법:** KOSIS에서 위 통계표를 조회해 기간 2017.01~2026.07, 항목(산업생산지수·출하지수·재고지수, 원지수)을 선택하고 엑셀로 내려받았다 (조회일 2026-09-28).
- **이용 조건:** KOSIS 이용약관에 따라 출처(통계청, 통계표명, 조회일)를 밝히고 이용했다. 이 저장소의 원본 데이터 파일은 학습 목적으로만 포함했다. 2026.06·07은 잠정치라 이후 수정될 수 있다.
- 분석과 해석은 작성자 개인의 것이며 통계청의 공식 견해가 아니다.
