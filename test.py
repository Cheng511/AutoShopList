from selenium import webdriver
import requests
import json
import urllib.parse
from bs4 import BeautifulSoup
import csv
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}

price_url = requests.get(
    'https://m.momoshop.com.tw/goods.momo?i_code=5619813&mdiv=searchEngine&oid=1_1&kw=SSD', headers=headers)
url_soup = BeautifulSoup(price_url.content, 'html.parser')
original_price = str(url_soup.find('del').text.strip())
current_price = url_soup.find('td', class_='priceArea').text.strip()
current_price = str(current_price.strip('元'))
print(current_price)
