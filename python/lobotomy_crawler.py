import requests
from bs4 import BeautifulSoup
import os

url = 'https://lobotomycorp.fandom.com/zh/wiki/%E5%BC%82%E6%83%B3%E4%BD%93'

response = requests.get(url)

html = response.content.decode()

soup = BeautifulSoup(html, 'html.parser')

all_a = soup.find_all('a')

for a_tag in all_a:
    title = a_tag.get('title')

    if title is not None :
        imgs = a_tag.find('img')
        try:
            imgs_url = imgs['src']
            img_resp = requests.get(imgs_url)
            w_img = img_resp.content
            os.makedirs('Abnormality', exist_ok=True)
            with open(f'Abnormality/{title}.png', 'wb') as f:
                f.write(w_img)
        except:
            pass