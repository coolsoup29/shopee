#表格设计
import traceback

from setting import *
import pymysql
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from my_timeout import DIR_NAME,DATA_TIME
import time
import sys
import random as R

import multiprocessing
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from timeout_decorator import timeout





# first_url_msg
# 页数  url 类别
MAX_FIRST_URL = 0

@timeout(30)
def get_html(page,rankBY):
        # IP_POOL = ["171.15.153.199:42438","119.98.6.253:52831","49.86.18.65:42953","218.73.143.47:40081"]
    # # my_msg = html.split("\n")
    # # my_IP = my_msg[R.randint(0, len(my_msg))]
    # the_ip = R.choice(IP_POOL)
    # print(the_ip)
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

        # ---- for proxy IP-----
        # req = requests.get(
        #     "https://proxy.horocn.com/api/proxies?order_id=LCUM1618813436539550&num=3&format=text&line_separator=win&loc_name=%E5%B9%BF%E5%B7%9E%2C%E6%B7%B1%E5%9C%B3%2C%E9%A6%99%E6%B8%AF")
        # req.encoding = 'utf-8'
        # IP_html = req.text
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--proxy-server=http://%s'%IP_html)

        # chrome_options.add_argument(
        #     '--user-agent=%s'%R.choice(user_agent))
        # profile = webdriver.FirefoxOptions()
        # profile.add_argument("--headless")
        # profile.add_experimental_option("prefs", prefs)

        # ran = R.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 8, 10])
        # if ran % 2 == 1:
        #     print("using CHrome")
        #     driver = webdriver.Chrome('/home/yice/Desktop/set_driver/chromedriver', chrome_options=chrome_options)
        #     # driver.set_window_size(6000, 6000)
        # else:
        #     print("using Firefox")
        #     driver = webdriver.Firefox(options=profile)
        #     # driver.set_window_size(6000, 6000)
        # # driver.maximize_window()
        # # driver.get(url)
        # print("缓冲中,缓冲时间%s秒" % STOPTIME, )





        driver = webdriver.Chrome('/home/yice/Desktop/set_driver/chromedriver',options=chrome_options)    # chrome_options=chrome_options
        driver.set_window_size(6000,6000)     # chang the window size for loading page
        # driver.maximize_window(5000*5000)   # where chrome use --headless,maxmize_window make nothing
        driver.get("https://shopee.co.id/search?keyword=jam%20tangan&page="+str(page)+"&sortBy="+rankBY)
        print("https://shopee.co.id/search?keyword=jam%20tangan&page="+str(page)+"&sortBy="+rankBY)
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
        driver.quit()
        return html

    except TimeoutError as e:
        print("\033[0;31;40m\tsomething wrongs beacuse of sql>>%s\033[0m"%e)
        driver.quit()
        get_html(page,rankBY)

    except Exception as e:
        print(e)
        driver.quit()
        get_html(page,rankBY)

def connect_to_mysql():
    db = pymysql.connect(h_line,user,pwd,db_name,charset='utf8')
    # cur = db.cursor()

    return db

def insert_bug(msg):
    with open("bug.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")



# main function in here! data_tuple is a tuple from mysql
# here we can get the price,offset,rank,title,appraisl...from the page
# last change the function on Dec_27;   REASON:shopee change the page
def get_url(data_tuple):
    try:
        base_url = "https://shopee.co.id"
        db = connect_to_mysql()

        html = get_html((data_tuple[2]-1),data_tuple[0])
        soup = BeautifulSoup(html,"html.parser")
        # tags = soup.find_all("div","shopee-item-card shopee-item-card--full shopee-item-card--shadow shopee-item-card--with-similar")
        tags = soup.find_all("div","_1gkBDw _2O43P5")

        if len(tags)<MAX_GOODS_ONEPAGE:
            print("商品加载未完成，重新加载当前网页(%s/50)"%len(tags))
            get_url(data_tuple)
            return "gg"

        cur = db.cursor()
        i = 0
        dz_sum = soup.find_all("div", "_2tl_fc")
        pl_sum = soup.find_all("span", "_113dbk")
        # off = soup.find_all("span", "percent")
        pf = soup.find_all("div", "shopee-rating-stars__stars")
        # titles = soup.find_all("div","_1NoI8_ KQFWxC")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!pinfen long>>>%s"%len(pf))
        sell = soup.find_all("div","_2-i6yP")
        all_load_tags = soup.find_all("button","shopee-icon-button shopee-icon-button--right ")
        # try:
        #     print(all_load_tags[0])
        #
        # except Exception as e:
        #     ex_type, ex_val, ex_stack = sys.exc_info()
        #     print(ex_type)
        #     print(ex_val)
        #     for stack in traceback.extract_tb(ex_stack):
        #         print(stack)
        #
        #     print(e,"fial to load >>")
        #     get_url(data_tuple)
        # print("test")
        for tag in tags:

            full_url = base_url + tag.parent.attrs['href']
            print("test")
            print(i, full_url)

            title = tag.contents[1].contents[0].contents[0].string
            if title == None:
                # for the pic "MALL"
                title = tag.contents[1].contents[0].contents[1].string
                print(title)

            else:
                pass
            print(title)
            try:
                # price_tag = tag.contents[1].contents[2].contents[1].string
                price_tag = tag.contents[1].contents[1].contents[1].contents[1].text
                # price = int(price_tag.split(" - ")[0][2:].replace(".", ""))
                price = int(price_tag.split(" - ")[0].replace(".", ""))
            except Exception as e:
                # price_tag = tag.contents[1].contents[2].contents[0].string
                price_tag = tag.contents[1].contents[1].contents[0].contents[1].text
                print(tag.contents[1].contents[2].contents)
                # price = int(price_tag.split(" - ")[0][2:].replace(".", ""))
                price = int(price_tag.split(" - ")[0].replace(".", ""))
            print(price)
            # price = int(price_tag.split(" - ")[0][2:].replace(".",""))
            try:

                price_max =  int(price_tag.split(" - ")[1][2:].replace(".",""))
            except Exception as e :

                price_max = 0
                print("some wrong about price_max>>",price_max)
            try:
                dz = int(dz_sum[i].string)
            except Exception as e:
                dz = 0

            try:
                pl = int(pl_sum[i].string[1:-1])
            except Exception:
                pl = 0


#-------------------------------------------------------------------------------------------
            try:
                off_set = int(tag.contents[0].contents[0].next_sibling.next_sibling.contents[0].contents[0].contents[0].string[:-1])    # .string[:-1]
                # print("None",tag.contents[0].contents[0].next_sibling.next_sibling.contents[0].contents[0].contents)

            # except TypeError:
            #     try:
            #         print("off_set",tag.contents[0].contents[0].next_sibling.next_sibling.next_sibling.contents[0].contents[0].contents[0])
            #         off_set=tag.contents[0].contents[0].next_sibling.next_sibling.next_sibling.contents[0].contents[0].contents[0].string[:-1]
            #         print("off_set",tag.contents[0].contents[0].next_sibling.next_sibling.next_sibling.contents[0].contents[0].contents[0].string[:-1])
            #     except Exception as e:
            #         off_set=0
            except Exception as e:
                # print("off_set", 0)
                # print("start",tag.contents[0].contents[0].next_sibling.contents[0].contents[0].contents[0].string[:-1])
                off_set =0
            print("折扣",off_set)

            if off_set == "habis":
                off_set =tag.contents[0].contents[0].next_sibling.next_sibling.next_sibling.contents[1].contents[0].contents[0].string[:-1]
#--------------------------------------------------------------------------------------------------------------

            # try:
            #     # print(111)
            #     off_set = tag.contents[0].contents[0].next_sibling.contents[0].contents[0].contents[0].string[:-1]
            #     # if off_set==None:
            #     #     print(off_set)
            #     #     off_set = int(
            #     #         tag.contents[0].contents[0].next_sibling.next_sibling.contents[0].contents[0].contents[0].string[
            #     #         :-1])  # .string[:-1]
            #     # elif off_set =="habi":
            #     #     off_set=0
            # except TypeError:
            #     # print(111)
            #     try:
            #         off_set = int(
            #             tag.contents[0].contents[0].next_sibling.next_sibling.contents[0].contents[0].contents[
            #                 0].string[:-1])
            #     except Exception as e:
            #         off_set = 0
            #
            #
            #
            # except Exception as e:
            #     # print(e)
            #     # print("off_set", 0)
            #     # print("start",tag.contents[0].contents[0].next_sibling.contents[0].contents[0].contents[0].string[:-1])
            #     # print(333)
            #     off_set = 0
            #
            # if off_set == 'habi':
            #     off_set = tag.contents[0].contents[0].next_sibling.contents[1].contents[0].contents[0].string[:-1]

            try:
                # my_sell = sell
                sell_sum = int(sell[i].contents[0].string[:-7])
            except Exception as e:
                print("sell !!!!!!!!!!!!!!!!!!!!!")
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
                print("pinfen",e)
            try:
                print("price",price,type(price))
            except Exception as e:
                print(e,"for price")
            print("pinfen>>",nu_pf)
            print("price_max",price_max)
            print("dianzan",dz, type(dz))
            print("pinlun",pl, type(pl))
            print('off_set',off_set, type(off_set))

            # 类型 页内排名 链接 页数 状态码 排名 标题 价格 最高价 折扣 评分 点赞数 评论数  （区别：畅销类没有点赞数，销量数取代了取代）
            msg = (DIR_NAME, data_tuple[0], i+1, full_url.replace("'", "++"), data_tuple[2],title,price,price_max,int(off_set),nu_pf,dz,pl,sell_sum)
            print(DIR_NAME, data_tuple[0], i+1, full_url.replace("'", "++"), data_tuple[2],title,price,price_max,int(off_set),nu_pf,dz,pl,sell_sum)
            try:
                # 有些　标题和链接　内　含有单引号，用*替换处理写入数据库
                insert_sql = "insert into second_url_Season%s values('%s',%d,'%s',%d,0,0,'%s',%d,%d,%d,%s,%d,%d,%d,0,'%s');"%(DIR_NAME, data_tuple[0], i+1, full_url.replace("'", "++"), data_tuple[2],title.replace("'", "++"),price,price_max,int(off_set),nu_pf,dz,pl,sell_sum,DATA_TIME)
            # print(nu_pf)
            except Exception as e:
                print(e)
            try:
                cur.execute(insert_sql)
                db.commit()
                print("%s第二层写入成功"%data_tuple[1])
                updata_sql = "update first_url_Season%s set url_status=1 where first_url='%s' and time='%s';"%(DIR_NAME,data_tuple[1],DATA_TIME)
                print(updata_sql)
                cur.execute(updata_sql)#爬取成功之后，父链接的my_status改为1
                print("父链接修改成功")
                db.commit()
            except Exception as e:
                db.close()
                with open("bug.txt", "a", encoding='utf-8') as f:
                    f.write("last:>>>https://shopee.co.id/search?keyword=jam%20tangan&page=" + str(data_tuple[2]-1) + "&sortBy=" + data_tuple[0]+"     %s"%str(msg)+'\n')
                print("\033[0;31;40m\tsomething wrongs beacuse of sql>>%s\033[0m"%e)
                # return "gg"


            i += 1
        db.close()
        return "gg"
    except Exception as e:
        print(11111111, e)
        ex_type, ex_val, ex_stack = sys.exc_info()
        print(ex_type)
        print(ex_val)
        for stack in traceback.extract_tb(ex_stack):
            print(stack)



        updata_sql = "update first_url_%s set url_status=0 where first_url='%s' and time='%s'" % (DIR_NAME, data_tuple[1],DATA_TIME)
        print(updata_sql)
        cur.execute(updata_sql)
        db.commit()
        db.close()
        insert_bug("last:>>>https://shopee.co.id/search?keyword=jam%20tangan&page="+str(data_tuple[2]-1)+"&sortBy="+data_tuple[0]+"      %s"%e++'\n')
        print("\033[0;31;40m\tsomething wrongs beacuse of >>%s\033[0m"%e)
        return "gg"
    finally:
        db.close()
        driver.quit()

# @timeout(10)
def get_max_page(rankBY):
    soup=BeautifulSoup(get_html(0,rankBY),"html.parser")
    global MAX_FIRST_URL
    try:
        max_page_tags = soup.find_all("span","shopee-mini-page-controller__total")
        max_page = max_page_tags[0].string   # 商品展示页的最大页数
        MAX_FIRST_URL += int(max_page)
        print("-----------------------%s maxpage:"%rankBY,max_page)
        return max_page
    except Exception as e:
        print("max_page>>>",e)
        get_max_page(rankBY)



# four months create a new table for msg
def create_table_first_second():
    db = connect_to_mysql()
    cur = db.cursor()
    first_all_url_sql = "create table if not exists first_url_Season%s(type varchar(15) not null,first_url varchar(200),page smallint not null,url_status tinyint(1) default 0,time varchar(10))CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"%DIR_NAME
    cur.execute(first_all_url_sql)
    try:
        # 加入该表的约束条件，防止加入重复数据
        cur.execute(
            "alter table first_url_Season%s add constraint lim_first_url unique (type,first_url,time)" % DIR_NAME)
    except Exception as e:
        # print("stop for >>",e)
        # sys.exit()pass
        pass

    second_all_url_sql = "create table if not exists second_url_Season%s(type VARCHAR(15) not null,rank_page tinyint not null,good_url VARCHAR(300),page tinyint not null,my_status tinyint DEFAULT 0,rank smallint default null,title varchar(200) not null ,price bigint not null,price_max bigint default 0,off_set tinyint default 0,pinfen decimal(5,1)default 0,dianzan bigint not null ,pinlun_sum bigint not null,sell_sum bigint default 0,id int primary key auto_increment ,time varchar(10))CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"%DIR_NAME
    cur.execute(second_all_url_sql)# 类型 页内排名 链接 页数 状态码 排名 标题 价格 最高价 折扣 评分 点赞数 评论数
    try:
        # 加入该表的约束条件，防止加入重复数据
        cur.execute("alter table second_url_Season%s add constraint lim_second_url unique (type,page,rank_page,time)"%DIR_NAME)
    except Exception as e:
        # print("stop for >>",e)
        # sys.exit()pass
        pass
    sql = 'create table  if not exists last_good_msg_Season%s (my_type enum("relevancy","ctime","sales"),rank smallint not null,title varchar(200) not null,good_url varchar(200) not null,price bigint not null,price_max bigint default 0,off_set tinyint default 0,off_set_NULL tinyint(1) default 0,style text not null,page tinyint not null,pinfen decimal(5,1),sum_pinjia bigint,sum_sell bigint,good_parisal bigint not null,main_words text,shop_url varchar(200) not null,sum_goods smallint not null,chat_back_per varchar(50) not null,chat_back varchar(50) not null,join_time tinyint not null,sum_fans bigint not null,id int primary key auto_increment,time varchar(10))CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;' % DIR_NAME
    cur.execute(sql)
    # z增加约束,防止多台机器写入相同消息
    try:
        cur.execute("alter table last_good_msg_Season%s add constraint lim_good_url unique (my_type,rank,time)" % DIR_NAME)
    except Exception:
        pass
    db.close()

def insert_first(rankBY):
    # global  MAX_FIRST_URL

    db = connect_to_mysql()
    max_page = get_max_page(rankBY)
    for page in range(int(max_page)):
        # print(123123)
        # try:
        cur=db.cursor()
        url = "https://shopee.co.id/search?keyword=jam%20tangan&page=" + str(page) + "&sortBy=" + rankBY
        try:
            cur.execute("insert into first_url_Season%s values('%s','%s','%d',0,'%s')" % (DIR_NAME, rankBY, url, (page + 1),DATA_TIME))  # RANKSTYLE[rankBY]
        # print("%s类别一级url写入完成,写入数:%d"%(rankBY,max_page))
            db.commit()
            print("写入完成", ">>%s" % url)
        except Exception as e:
            print(e)

    db.close()
        # except Exception as e:
        #     db.rollback()
        #     print("写入失败 >>",e,url)
    # db = connect_to_mysql()
    # cur = db.cursor()
    # sum_data = "select page from first_url_%s"%DIR_NAME
    # print(sum_data,type(sum_data))
    # db.close()
    # if sum_data < int(max_page):
    #     print("一层链接进入进度(%s/%s)"%(sum_data,int(max_page)))
    #     insert_first(rankBY)



def mul_get_page():
    p = multiprocessing.Pool(processes=5)

    for rankBY in rankBY_list:
        # 三个类别的排序方法的爬虫记录,记录在txt文本中(优化:存入数据库中), 参数设置在setting.py中print("正在爬取[[%s]]分类的数据"%(RANKSTYLE[rankBY]))
        i = 1
        p.apply_async(insert_first, args=(rankBY,))  # url前三位是排名,最后一位是\n
    print('正在多进程抓取写入第一层链接')
    p.close()
    p.join()
    print('第一层链接写入完成!')

    db = connect_to_mysql()
    cur = db.cursor()
    select_sql = "select * from first_url_Season%s where  time='%s' order by rand()" % (
    DIR_NAME, DATA_TIME)
    sum_page = cur.execute(select_sql)  # 返回查询结果的数据总数
    if sum_page!=210:
        print("try again for get_page_rank (%s//210"%sum_page)
        mul_get_page()
        db.close
    db.close




def get_first_url():
    db = connect_to_mysql()
    cur = db.cursor()
    select_sql = "select * from first_url_Season%s where url_status =0 and time ='%s' order by rand()"%(DIR_NAME,DATA_TIME)
    sum_page = cur.execute(select_sql)# 返回查询结果的数据总数
    # if sum_page != MAX_FIRST_URL:
    #     os.system("python3 tomysql.py")
    #     print('already exit! ',sum_page,MAX_GOODS_ONEPAGE)
    #     sys.exit()
    #     print("done!")

    print("will get %d个页面没爬去"%sum_page)
    data = cur.fetchall()#　返回查询结果的第一条，fetchall() 返回得到的是元祖组成的元祖，元祖中的元祖[0],类别;[1]链接;[2]页数;[3]状态;0未成功读取
    db.close()
    return data


def mul_main(data):


    p = multiprocessing.Pool(processes=32)

    for rankBY in data:
        # 三个类别的排序方法的爬虫记录,记录在txt文本中(优化:存入数据库中), 参数设置在setting.py中print("正在爬取[[%s]]分类的数据"%(RANKSTYLE[rankBY]))
        i = 1
        p.apply_async(get_url, args=(rankBY,))  # url前三位是排名,最后一位是\n

    print('正zai进程抓取第二层链接...')
    p.close()
    p.join()
    print('All processes done!')
    data = get_first_url()
    # for rankBY in data:
    #     get_url(rankBY)
    if len(get_first_url()) != 0:
        print(data)
        mul_main(data)
    print("over!over!")
    return "ok"


#写入排名方法
def alter_rank():
    db = connect_to_mysql()
    cur = db.cursor()
    # alter_sql =  "alter table second_url_%s add rank SMALLINT;"%(DIR_NAME)
    # cur.execute(alter_sql)
    for my_type in rankBY_list:
        page_list = cur.execute("select distinct page from second_url_Season%s where type='%s' and time='%s'"%(DIR_NAME,my_type,DATA_TIME))
        print(page_list)
        sum_good = 0
        for page in range(1,page_list+1):
            sum_good_this_page = cur.execute("select * from second_url_Season%s where page=%d and type='%s' and time='%s'"%(DIR_NAME,page,my_type,DATA_TIME))
            # print(sum_good_this_page)
            # data = cur.fetchall()
            # for msg in data:
            #     # print("test1")
            #     rank = msg[1]+sum_good
            #     # print(rank)
            rank_sql = "update second_url_Season%s set rank=rank_page+%s where page=%s and type='%s' and time='%s';"%(DIR_NAME,sum_good,page,my_type,DATA_TIME)
            # print("ok?")
            cur.execute(rank_sql)
            # print("test3")
            db.commit()
                # print("okokokokokokokok")
            sum_good += sum_good_this_page
        print("%s排名写入完成"%RANKSTYLE[my_type])
    print("所有排名写入完成")
# 所有商品链接表
# 类别  当前页排名  链接  页数  状态  全级排名
def start_item():
    start = time.time()
    # insert first_url to mysql
    # get_max_page()
    mul_get_page()
    data = get_first_url()
    mul_main(data)
    end = time.time()
    print("use_time>>>", (end - start) // 60, "min", (end - start) % 60, "second")
    alter_rank()  # 写入排名方法



if __name__ == "__main__":

    # create table first
    print(DATA_TIME)
    create_table_first_second()
    start_item()
    import get_main_msg
    #get_main_msg.mul_main()
    os.system("pypy get_main_msg.py")



