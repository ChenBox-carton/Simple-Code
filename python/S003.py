import requests
import json

name = input('請輸入要查詢的魚貨名稱:')

try:
  req = requests.get('https://data.moa.gov.tw/Service/OpenData/FromM/AquaticTransData.aspx')
except:
  pass

datas = json.loads(req.text)

for data in datas:
  if data is not None and name in data['魚貨名稱']:
    print(f"交易日期: {data['交易日期']}")
    print(f"魚貨名稱: {data['魚貨名稱']}")
    print(f"市場名稱: {data['市場名稱']}")
    print(f"交易量: {data['交易量']}")
    print(f"平均價: {data['平均價']}\n")
  
  
