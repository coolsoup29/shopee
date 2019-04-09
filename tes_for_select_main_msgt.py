#表格设计

from setting import *
import pymysql
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from create_folder import DIR_NAME,timeout
import time
import sys
import random as R
import get_msg
import csv
import multiprocessing
import os
from get_msg import get_goods
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

def get_html(url):
    try:
        user_agent = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        ]

        chrome_options = webdriver.ChromeOptions()
        # req = requests.get(
        #     "https://proxy.horocn.com/api/proxies?order_id=LCUM1618813436539550&num=3&format=text&line_separator=win&loc_name=%E5%B9%BF%E5%B7%9E%2C%E6%B7%B1%E5%9C%B3%2C%E9%A6%99%E6%B8%AF")
        # req.encoding = 'utf-8'
        # IP_html = req.text
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--proxy-server=http://%s'%IP_html)

        chrome_options.add_argument(
            '--user-agent=%s' % R.choice(user_agent))
        driver = webdriver.Chrome('../set_driver/chromedriver',
                                  chrome_options=chrome_options)  # chrome_options=chrome_options
        driver.set_window_size(6000, 6000)
        # driver.maximize_window(5000*5000)
        driver.get(url)
        # print("https://shopee.co.id/search?keyword=jam%20tangan&page=" + str(page) + "&sortBy=" + rankBY)
        # driver.get("https://shopee.co.id/search?keyword=jam%20tangan&page=23&sortBy=sales")
        time.sleep(STOPTIME)
        # 实现滚动条拉到底部的操作("此处滚动加载商品")
        js = "var q=document.documentElement.scrollTop=1000"
        driver.execute_script(js)
        time.sleep(0.5)
        js = "var q=document.documentElement.scrollTop=2000"
        driver.execute_script(js)
        time.sleep(0.5)
        js = "var q=document.documentElement.scrollTop=3000"
        driver.execute_script(js)
        time.sleep(0.5)
        js = "var q=document.documentElement.scrollTop=6000"
        driver.execute_script(js)
        time.sleep(0.5)
        # js = "var q=document.documentElement.scrollTop=5000"
        # driver.execute_script(js)
        # js = "var q=document.documentElement.scrollTop=6000"
        # driver.execute_script(js)
        time.sleep(1)
        html = driver.page_source
        # soup = BeautifulSoup(data,"html.parser")
        driver.quit()
        # driver.save_screenshot("test.png")
        # with open("test.html","a",encoding="utf-8") as f:
        #     f.write(html)
        return html

    except Exception as e:
        print("gg")



# test for second_url what's the rule to get msg:
def get_set(url):
    html = get_html(url)
    soup=BeautifulSoup(html,"html.parser")
    tags = soup.find_all("div", "_1gkBDw _2O43P5")

    base_url = "https://shopee.co.id"
    i = 0
    dz_sum = soup.find_all("div", "_2tl_fc")
    pl_sum = soup.find_all("span", "_113dbk")
    # off = soup.find_all("span", "percent")
    pf = soup.find_all("div", "shopee-rating-stars__stars")
    # titles = soup.find_all("div","_1NoI8_ KQFWxC")
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!pinfen long>>>%s" % len(pf))
    sell = soup.find_all("div", "_2-i6yP")

    for tag in tags:

        full_url = base_url + tag.parent.attrs['href']
        # print("test")
        # print(i, full_url)

        title = tag.contents[1].contents[0].contents[0].string
        if title == None:
            # for the pic "MALL"
            title = tag.contents[1].contents[0].contents[1].string
            print(title)

        else:
            pass
        # print(title)
        try:
            price_tag = tag.contents[1].contents[2].contents[1].string
            price = int(price_tag.split(" - ")[0][2:].replace(".", ""))
        except Exception as e:
            price_tag = tag.contents[1].contents[2].contents[0].string
            # print(tag.contents[1].contents[2].contents)
            price = int(price_tag.split(" - ")[0][2:].replace(".", ""))
        # print(price)
        # price = int(price_tag.split(" - ")[0][2:].replace(".",""))
        try:

            price_max = int(price_tag.split(" - ")[1][2:].replace(".", ""))
        except Exception as e:

            price_max = 0
            # print("some wrong about price_max>>", price_max)
        try:
            dz = int(dz_sum[i].string)
        except Exception as e:
            dz = 0

        try:
            pl = int(pl_sum[i].string[1:-1])
        except Exception:
            pl = 0

        try:
            # print(111)
            off_set = tag.contents[0].contents[0].next_sibling.contents[0].contents[0].contents[0].string[:-1]
            # if off_set==None:
            #     print(off_set)
            #     off_set = int(
            #         tag.contents[0].contents[0].next_sibling.next_sibling.contents[0].contents[0].contents[0].string[
            #         :-1])  # .string[:-1]
            # elif off_set =="habi":
            #     off_set=0
        except TypeError:
            # print(111)
            try:
                off_set = int(tag.contents[0].contents[0].next_sibling.next_sibling.contents[0].contents[0].contents[0].string[:-1])
            except Exception as e:
                off_set=0



        except Exception as e:
            # print(e)
            # print("off_set", 0)
            # print("start",tag.contents[0].contents[0].next_sibling.contents[0].contents[0].contents[0].string[:-1])
            # print(333)
            off_set=0

        if off_set=='habi':
            off_set=tag.contents[0].contents[0].next_sibling.contents[1].contents[0].contents[0].string[:-1]

        try:
            # my_sell = sell
            sell_sum = int(sell[i].contents[0].string[:-7])
        except Exception as e:
            # print("sell !!!!!!!!!!!!!!!!!!!!!")
            sell_sum = 0

        # 评分设置
        try:
            nu_tags = tag.contents[1].contents[3].contents[1].contents[0].contents[0].contents
            nu = 0
            # print(len(nu_tags))
            for msg in nu_tags:
                # print(msg.contents[0].attrs["style"][7:-2])
                per = msg.contents[0].attrs["style"][7:-2]
                # print('---------------1111----------------')
                nu += float(per)
                # print('---------------2222----------------')
            nu_pf = round(nu / 100, 1)
        except Exception as e:
            nu_pf = 0
            # print("pinfen", e)
        # try:
        #     print("price", price, type(price))
        # except Exception as e:
        #     print(e, "for price")
        # print("pinfen>>", nu_pf)
        # print("price_max", price_max)
        # print("dianzan", dz, type(dz))
        # print("pinlun", pl, type(pl))
        # print('off_set', off_set, type(off_set))

        # 类型 页内排名 链接 页数 状态码 排名 标题 价格 最高价 折扣 评分 点赞数 评论数  （区别：畅销类没有点赞数，销量数取代了取代）
        msg = (DIR_NAME, i + 1, full_url.replace("'", "++"), title, price, price_max,(off_set), nu_pf, dz, pl, sell_sum)

        print(i,off_set)
        if off_set == "habi":
            print("""
            *******************************************
            |DIR_NAME:%s,
            |RANK:%d,
            |URL:%s,
            |TITLE:%s,
            |PRICE:%s,
            |MAX_PRICE:%s,
            |OFF_SET:%s,
            |PINFEN:%s,
            |DIANZAN:%s,
            |PINLUN:%s,
            |SELL:%s
            *******************************************
            """%(msg))

        i+=1
        # print(tags.index(tag)+1,off_set)

get_set("https://shopee.co.id/search?keyword=jam%20tangan&page=1&sortBy=sales")
