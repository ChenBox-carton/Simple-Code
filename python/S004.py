import requests
from bs4 import BeautifulSoup

path = 'output.txt'
note = open(path, 'w', encoding = 'utf-8')

url = 'https://twcoupon.com/bmenu-%e8%82%af%e5%be%b7%e5%9f%ba-menu%e8%8f%9c%e5%96%ae%e5%83%b9%e6%a0%bc.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.title
print(title.getText())
print(title.getText(), file = note)

select = soup.select('div.wrapper img')

for i in select:
    print(i['src'], i.text)
    print(i['src'], i.text, file = note)

note.close()