from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import os

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service) 

driver.get("https://uma.komoejoy.com/character.html")
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
imgs = soup.find_all('img')

for img in imgs:
    try:
        url = 'http:' + img['data-src']
        name = img['alt']
        resp = requests.get(url)
        img = resp.content
        os.makedirs('umamusume', exist_ok=True)
        with open(f'umamusume/{name}.png', 'wb') as f:
            f.write(img)
    except:
        pass