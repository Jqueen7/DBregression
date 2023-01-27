import requests

url = 'https://www.sec.gov/files/company_tickers_exchange.json'
headers = {'User-Agent': 'Mozilla'}
res = requests.get(url, headers=headers)
cik_list = res.json()
tickers = dict()
for p in cik_list['data']:
    tickers[p[1]] = p[2]
print(tickers)