# DBregression
13F and independent variables

## 1. 13F
### 1-1. NumShares
분기 별로 투자자가 담은 주식 수(Amount). 수정 주가로 액면 분할 반영된 수치
### 1-2. loadstocks.ipynb
투자자가 2013 4Q부터 2022 3Q까지 담았던 모든 주식의 중복 없는 list를 구하기 위한 파일
### 1-3. aggregate
1-1의 NumShares를 산출하기 위한 파일

## 2. Fundamentals
### 2-1. Crawling Fundamentals
1-2의 loadstocks를 통해 수집한 티커로 해당 기업의 재무제표를 불러오는 파일. 현재 시점까지 오면서 상장폐지, 합병됐거나 ETF 등 원래 재무제표가 존재하지 않는 증권들 예외처리.
### 2-2. Features
불러온 재무제표 값들을 바탕으로 30 여개의 Financial Ratios를 산출. 섹터별로 재무제표 계정에 차이가 있음에 따라서 예외처리 완료.

## 3. Macro
19개의 FRED 거시경제 데이터에 금 가격, 중국 GDP 분기별 성장률 데이터를 기간에 맞게 불러와 Merge

## 4. Regression
OLS.py & OLS_BW.py
워렌버핏과 레이달리오의 포트폴리오에 대해 주식별 변화량(이번기 - 전기)에 대해 regression (OLS) 진행하고 이에 대한 2022 4Q에 대한 예상치를 반환하는 파일

