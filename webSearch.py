# coding = utf-8
# PChome24h 爬蟲
from selenium import webdriver
import requests
import json
import urllib.parse
from bs4 import BeautifulSoup
import csv
import datetime

keyword = str(input("請輸入搜尋關鍵字: "))
n = int(input("請問要搜尋多少頁的內容? "))
parse_word = urllib.parse.quote(keyword)
print('搜尋結果如下: ')
print('='*30)


def Get_Results(parse_word):
    # 這個函式會針對輸入的搜尋關鍵字取出PCHome24hr搜尋結果前5頁資料的標題
    for i in range(0, n-1):
        response = requests.get(
            'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=' + parse_word + '&page=' + str(i) + '&sort=sale/dc')
        raw_data = response.content.decode('utf-8')
        data = json.loads(raw_data)
        try:
            products = data['prods']
            for key in products:
                product_name = key['name']
                prod_id = key['Id']
                prod_price = str(key['price'])
                link = 'https://24h.pchome.com.tw/prod/' + prod_id
                print('名稱: ' + product_name + '\n' +
                      '價格: $' + prod_price + '\n' +
                      '網址: https://24h.pchome.com.tw/prod/' + prod_id + '\n')
                print()
                today = str(datetime.date.today())
                with open(today + '_' + keyword + '.csv', 'a') as f:
                    file = csv.writer(f)
                    file.writerow(['名稱', '價格', '網址'])
                    file.writerow([product_name, prod_price, link])
        except Exception as err:
            print(str(err))


Get_Results(parse_word)
