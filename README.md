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

![image](https://user-images.githubusercontent.com/122861933/215395833-8f29c825-08c7-4935-99ee-3e5ba504e051.png)

변수 간 다중공선성을 고려하지 않았던 것은 아니나, 기업 내 Fundamental 변수를 통해 회귀분석을 진행하는 방식의 논문 수 건을 참조한 결과, 다중공선성 보다도 설명력을 강화할 수 있다는 점을 근거로 본 실험과 유사한 변수들을 다수 사용했음. 

## 3. Macro
19개의 FRED 거시경제 데이터에 금 가격, 중국 GDP 분기별 성장률 데이터를 기간에 맞게 불러와 Merge

![image](https://user-images.githubusercontent.com/122861933/215394684-dfa46bf7-1e6b-465a-8035-f78610722722.png)

6. 기준금리가 아니라 실효 연방기금금리를 사용한 이유는 실효 연방기금금리가 보다 당시의 상황을 면밀히 반영한다고 보았기 때문.

7. 근원 CPI는 프록시로 Sticky Price CPI (비탄력적 CPI)를 사용했음. Sticky Price CPI 사용 결과 가격변동이 잦은 상품들(e.g. 중고차)이 제외되었음. 

7, 8, 17. 명목이 아니라 근원 수치를 사용한 이유는 변수 간 다중공선성을 고려하였기 때문.

## 4. Regression
OLS.py & OLS_BW.py
워렌버핏과 레이달리오의 포트폴리오에 대해 주식별 변화량(이번기 - 전기)에 대해 regression (OLS) 진행하고 이에 대한 2022 4Q에 대한 예상치를 반환하는 파일

