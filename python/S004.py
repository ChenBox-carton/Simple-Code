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

select = soup.select('div.wrapper ul')

# 第一組套餐的圖片在 wrapper class 裡面被註解掉了，並不能從select裡搜索到。
# 真實圖片資料在 class="bb690" 的 img 可預先輸出不進入迴圈

first_img = soup.select_one('img.bb690')
img_src = first_img['src'] if first_img else "None"
print(img_src, file = note)

for data in select:
    img = data.find('img')
    text = data.text
    img_src = img['src'] if img else "None"
    # 可從上方的 img_src 的輸出結果看出，第一組套餐的圖片資料被註解掉了，所以會是 None

    print(img_src, text)
    print(img_src, text, file = note)

note.close()
