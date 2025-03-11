import requests
import json

name = input("請輸入要查詢的魚貨名稱:")
req = requests.get('https://data.moa.gov.tw/Service/OpenData/FromM/AquaticTransData.aspx')
data = json.loads(req.text)