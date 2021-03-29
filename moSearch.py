# coding = utf-8
# momo 爬蟲
from selenium import webdriver
import requests
import json
import urllib.parse
from bs4 import BeautifulSoup
import csv
import datetime

keyword = str(input("請輸入搜尋關鍵字: "))
n = int(input("請問要搜尋多少頁的內容? "))
print('爬蟲中...')
parse_word = urllib.parse.quote(keyword)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}
source = requests.get(
    'https://m.momoshop.com.tw/search.momo?searchKeyword=' + parse_word + '&couponSeq=&cpName=&searchType=1&cateLevel=-1&curPage=' + str(n) +
    '&cateCode=-1&ent=k&_imgSH=fourCardStyle', headers=headers)
soup = BeautifulSoup(source.content, 'html.parser')
raw_data = soup.find_all('li', class_='goodsItemLi')
for data in raw_data:
    for title in data.find_all('h3', class_='prdName'):
        prod_name = title.text.strip()  # 產品名
    for url in data.find_all('a'):
        url = url['href']  # 產品網址
        price_url = requests.get(
            'https://m.momoshop.com.tw' + url, headers=headers)
        prod_url = 'https://m.momoshop.com.tw' + url
        url_soup = BeautifulSoup(price_url.content, 'html.parser')
        try:
            current_price = url_soup.find(
                'td', class_='priceArea').text.strip()
            current_price = str(current_price.strip('元'))
            today = str(datetime.date.today())
            with open(today + '_' + keyword + '_momo.csv', 'a') as f:
                file = csv.writer(f)
                file.writerow(['名稱', '促銷價', '網址'])
                file.writerow([prod_name, current_price, prod_url])
                print('爬蟲結果在csv檔了！')
        except Exception as err:
            print(str(err))
