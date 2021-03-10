# coding = utf-8
from selenium import webdriver
import requests
import json
import urllib.parse
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

keyword = str(input("請輸入搜尋關鍵字: "))
parse_word = urllib.parse.quote(keyword)


def Get_Results(parse_word):
    # 這個函式會針對輸入的搜尋關鍵字取出PCHome24hr搜尋結果前5頁資料的標題
    for i in range(0, 1):
        response = requests.get(
            'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=' + parse_word + '&page=' + str(i) + '&sort=sale/dc')
        raw_data = response.content.decode('utf-8')
        data = json.loads(raw_data)
        try:
            products = data['prods']
            for key in products:
                product_name = key['name']
                prod_id = key['Id']
                if product_name != '' or prod_id != '':
                    print(prod_id + '\n' + product_name + '\n' +
                          'current price at: $' + Get_Current_Price(prod_id) + '\n')
                elif product_name == '':
                    print(prod_id + '\n' + 'No Product Name' + '\n' +
                          'current price at: $' + Get_Current_Price(prod_id) + '\n')
                elif prod_id == '':
                    print('No product ID' + '\n' + 'No Product Name' + '\n' +
                          'current price at: $' + Get_Current_Price(prod_id) + '\n')
                    print()
        except Exception as err:
            print(str(err))


def Get_Current_Price(prod_id):
    # 此函式會針對輸入的產品Id給出當前價錢
    driver = webdriver.Chrome('/Users/jc/chromedriver')
    driver.get('https://24h.pchome.com.tw/prod/' + prod_id)
    try:
        element = driver.find_element_by_css_selector('#PriceTotal')
        current_price = element.text
        driver.close()
        return str(current_price)
    except Exception as err:
        print(str(err))


Get_Results(parse_word)
