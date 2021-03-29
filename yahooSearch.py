# coding = utf-8
# yahoo 爬蟲
import requests
import json
import urllib.parse
from bs4 import BeautifulSoup, SoupStrainer
import csv
import datetime

keyword = str(input("請輸入搜尋關鍵字: "))
parse_word = urllib.parse.quote(keyword)
print('爬蟲中...')
source = requests.get(
    'https://tw.mall.yahoo.com/search/product?p=' + parse_word)
soup = BeautifulSoup(source.content, 'html.parser')
data = soup.find('ul', class_='gridList')
for product in data:
    for title in product.find_all('span', class_='BaseGridItem__title___2HWui'):
        product_name = title.text  # 產品名
    for product_url in product.find_all('a'):
        url = product_url['href']  # 產品連結
        price_info = requests.get(url)  # 找產品連結頁面中的價格們
        price = BeautifulSoup(price_info.content, 'html.parser')
        product_prices = price.find('span', class_='price')
        product_prices = product_prices.text  # 產品價格
        today = today = str(datetime.date.today())
        with open(today + '_' + keyword + '_yahoo.csv', 'a') as f:
            file = csv.writer(f)
            file.writerow(['名稱', '價格', '網址'])
            file.writerow([product_name, product_prices, url])
            print('爬蟲結果在csv檔了！')
