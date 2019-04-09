import re

from setting import *
import pymysql
import csv
from my_timeout import DIR_NAME,DATA_TIME
from timeout_decorator import timeout
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from rebuit_str import re_str
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import random as R
from to_mysql import *
import multiprocessing
import requests,signal
import urllib3


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait       #WebDriverWait注意大小写
from selenium.webdriver.common.by import By


# import tomysql
# 最大访问次数
BIG = 3
# 当前访问次数
THIS_I = 0

s = requests.Session()
s.keep_alive = False
num=0
TIME=0


def cnn_mysql():
    try:
        db = pymysql.connect(h_line, user, pwd, db_name, charset='utf8')
    except Exception as e:
        print("lining to mysql",e)
        cnn_mysql()


def get_ip():
    ip_url = "http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=f03aa084696849e6831cff28351d4849&count=5&expiryDate=0&format=2&newLine=2"
    req = requests.get(ip_url)
    pro_ip = req.text.split("\r\n")
    with open("ip.txt", 'w', encoding='utf-8') as f:
        for ip in pro_ip:
            f.write(ip + "\n")
    return pro_ip


def kill():

    lines = os.popen('ps -e|grep get_main_msg.py').readlines()

    pa = re.compile(r'(\d+) ')

    for line in lines:

        result = re.findall(pa,line)

        print(result[0])


# filename = "all_url_left.txt"
@timeout(30)
def get_goods(data, STOPTIME):
    # global TIME
    s = requests.session()
    s.keep_alive = False
    print("test1111")
    c_time = time.ctime().split(" ")[4].split(":")[1]
    print('test2222',c_time)
    #
    # if int(c_time)==TIME+2:
    #     pass
    # else:
    #     TIME=c_time
    #     ip_url = "http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=f03aa084696849e6831cff28351d4849&count=5&expiryDate=0&format=2&newLine=2"
    #     req = requests.get(ip_url)
    #     pro_ip = req.text.split("\r\n")
    #     with open("ip.txt", 'w', encoding='utf-8') as f:
    #         for ip in pro_ip:
    #             f.write(ip + "\n")
    # restart_time=time.ctime().split(" ")[3].split(":")[1]
    # if str(restart_time) == "06"  :
    #     out = os.popen("ps aux | pgrep chromedriver").read()
    #     os.system("python3 first_second_url.py")
    #     for i in out:
    #         os.system("kill -9 %s" % i)
    # data[0] :类别
    # data[2] :链接
    # data[3] :页数



    if int(c_time)%10==0:
        kill()

    # ip_list = []
    # with open("ip.txt", 'r', encoding='utf-8') as f:
    #
    #    for ip in f.readlines()[:-1]:
    #        ip_list.append(ip)


    print(data[2])
    CSV_COOKIE = []  # for rank

    # ip_url = "http://ged.ip3366.net/api/?key=20190117135632663&getnum=1&filter=1"
    # req =requests.get(ip_url)
    # pro_ip = req.text[:-2]
    # print(pro_ip)
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
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    ]
    #         ['类目', '标题', '产品链接', '价格	', '折扣', '	颜色（变体）', '页数', '评分', '评价数', '月销售', '点赞数', '关键词', '店铺链接', '店铺产品数',
    #          '聊天百分比回复', '聊天回复', '加入时间', '粉丝'])
    try:
        #print(123123)
        chrome_options = Options()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('–single-process')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("–disable-plugins")
        chrome_options.add_argument(
            '--user-agent=%s' % R.choice(user_agent))
        chrome_options.add_argument("–first run")
        #      print("pro_ip>>",pro_ip)
        ran_list=[0,0,0,0,0,0]
        if R.choice(ran_list)==0:

            pass
        else:
            ip_list = []
            with open("ip.txt", 'r', encoding='utf-8') as f:
                for ip in f.readlines()[:-1]:
                    ip_list.append(ip[:-1])
            pro_ip=R.choice(ip_list[:-1])
            print(pro_ip)
            chrome_options.add_argument("--proxy-server=http://%s"%pro_ip)

        profile = webdriver.FirefoxOptions()
        profile.add_argument("--headless")

        # dri_list = [webdriver.Chrome('../set_driver/chromedriver',chrome_options=chrome_options),webdriver.Firefox(options=profile)]
        # #driver = webdriver.Chrome('../set_driver/chromedriver',chrome_options=chrome_options)
        # driver=R.choice(dri_list)
        ran = R.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        if ran % 2 == 1:
            print("using CHrome")
            capa = DesiredCapabilities.CHROME
            capa["pageLoadStrategy"] = "none"
            driver = webdriver.Chrome('/home/yice/Desktop/set_driver/chromedriver', chrome_options=chrome_options,desired_capabilities=capa)
            wait = WebDriverWait(driver, 20)
            driver.get(data[2])
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='_3n5NQx'] | //div[@class='product-not-exist__text']")))
            driver.delete_all_cookies(  )
            driver.set_window_size(6000,6000)
        else:
            print("using Firefox")
            driver = webdriver.Firefox(options=profile)
        # driver.maximize_window()
        driver.delete_all_cookies()
        # driver.set_page_load_timeout(20)
        # driver.set_script_timeout(20)
        # try:
        #     driver.get(data[2])
        # except:
        #     print("加载页面太慢，停止加载，继续下一步操作")
        #     driver.execute_script("window.stop()")
        # # driver.get(data[2])
        # print("缓冲中,缓冲时间%s秒" % STOPTIME, )
        #
        # time.sleep(STOPTIME)
        # js = "var q=document.documentElement.scrollTop=3000"
        # driver.execute_script(js)
        #
        # time.sleep(1)
        # driver.save_screenshot("goods.png")
        html = driver.page_source
        driver.quit()
        # 标题

        soup = BeautifulSoup(html, "html.parser")

        # 考虑商品下架因素
        out_tags = soup.find_all("div", "product-not-exist__text")
        try:
            if out_tags[0].string == "Produk tidak ada":
                print(out_tags[0].string)
                # msg_list = [data[0],data[4],'zero',data[2],str(0),0,str(0),data[3],0,0,0,0,str(0),0,0,0,0,str(0),0,0,0]
                # insert_sql = 'insert into last_good_msg_%s values("%s","%s","%s","%s",%s,%s,%s,"%s","%s",%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s",%s)' % (DIR_NAME, msg_list[0], msg_list[1], msg_list[2], msg_list[3], msg_list[4], msg_list[5], msg_list[6],msg_list[7], msg_list[8], msg_list[9], msg_list[10], msg_list[11], msg_list[12], msg_list[13],msg_list[14], msg_list[15], msg_list[16], msg_list[17], msg_list[18], msg_list[19], msg_list[20])
                db = pymysql.connect(h_line, user, pwd, db_name, charset='utf8')
                cur = db.cursor()
                # cur.execute(insert_sql)
                # chang_msg(my_list)
                print("！！下架商品[!00change成功00!]下架商品[!00change成功00!]")
                # db.commit()
                fath_sql = "update second_url_Season%s set my_status=my_status+3 where type='%s' and rank=%d and time='%s'" % (
                DIR_NAME, data[0], data[5],DATA_TIME)
                try:
                    cur.execute(fath_sql)
                    print("father_url status is changed")
                    db.commit()
                    print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    db.close()
                    return "已下架"
                except Exception as e:
                    db.close()
                    print("!!!!not changed!!!!!!!!!!")
        except Exception as e:
            # driver.quit()
            # try:
            #     db.close()
            # except Exception as e:
            #     pass
            print("last_url>>>>", e)
            # return "gg"
        # finally:
        #     db.close()

        # 价格 ok

        try:
            price_tags = soup.find_all("div", "_3n5NQx")
            # 价格
            print("价格", price_tags[0].string)
        except Exception as e:
            # cookies = driver.get_cookies()
            # print("main: cookies = {cookies}")
            driver.delete_all_cookies()
            print(e, "价格获取失败")
            print(price_tags)
            driver.quit()

            # get_goods(data, STOPTIME)
        title = soup.find_all("title")[0].string

        # print(soup.find_all("div","qaNIZv"))

        # 折扣 ok
        try:
            # 折扣
            off_tags = soup.find_all("div", "MITExd")
            # print("!!!!!!!!!!!!!", off_tags[0].string.split(" ")[0])
            off_set = off_tags[0].string.split(" ")[0]

        except IndexError:
            # 优惠券
            off_tags = soup.find_all("div", "voucher-ticket__promo")
            # print("!!!!!!!!!!!!!!!!!!!!", off_tags[0].string.split(" ")[0])
            try:
                off_set = off_tags[0].string.split(" ")[0]
            except Exception:
                off_set = "无优惠"
        except Exception:
            # 无优惠
            off_set = "无优惠"

        # 种类 ok
        type_tags = soup.find_all("div", "flex items-center crl7WW")
        all_type = []
        try:
            for tag in type_tags[0].contents:
                if tag == None:
                    pass
                if len(tag.attrs['class']) > 1:

                    print(tag.string + "(无库存)")
                    all_type.append(tag.string + "(无库存)")
                else:
                    all_type.append(tag.string)
                    print(tag.string)
        except Exception as e:
            print(e)
            # get_goods(data,STOPTIME)

        finally:
            driver.quit()
            try:
                db.close()
            except Exception as e:
                pass

        # 评分,评价数，销量 ok
        try:
            three_tags = soup.find_all("div", "flex _32fuIU")[0].contents
            pinfen = three_tags[0].contents[0].string
            print("评分", three_tags[0].contents[0].string)
            pinjia = three_tags[1].contents[0].string
            print("评价量", three_tags[1].contents[0].string)
            yuexl = three_tags[2].contents[0].string
            print("月销量", three_tags[2].contents[0].string)
        except IndexError:
            pinfen = three_tags[0].contents[0].string
            print("评分", three_tags[0].contents[0].string)
            yuexl = three_tags[1].contents[0].string
            print("月销量", three_tags[1].contents[0].string)
            pinjia = "None"
            print("评价量", None)
        except Exception as e:
            print(e, ":>>评分评价数销量获取异常")
            driver.delete_all_cookies()
            driver.quit()
            get_goods(data,STOPTIME)

        # 关键词 ok
        main_word_list = []
        word_tags = soup.find_all("div", "_2u0jt9")

        # for tag in word_tags[0].contents[1:]:
        #     if tag.string != " ":
        #         #print(tag.string)   # 获得关键词，若需要链接则获取属性则可
        #         main_word_list.append(tag.string)
        #     else:
        #         pass   # 去除中间存在的span标签
        # main_word_list = []
        # try:
        for tag in word_tags[0].contents[1:]:
            if tag.string != " ":
                # print(tag.string)   # 获得关键词，若需要链接则获取属性则可
                main_word_list.append(tag.string)
            else:
                pass  # 去除中间存在的span标签
        # except Exception:
        #      pass

        # except Exception:
        #     pass
        # 店铺链接
        room_tags = soup.find_all("a", "btn btn-light btn--s btn--inline btn-light--link Ed2lAD")
        href = room_tags[0].attrs["href"]
        print(href)  # 这里需要加上主链接 https://shopee.co.id+ href

        # 点赞数,产品数量，回复比,回复时间,加入时间，粉丝ok
        # dz_tags = soup.find_all("span", "_1rsHot OuQDPE")
        # print("点赞",dz_tags[0].string)
        # print("产品数",dz_tags[1].string)
        # print("回复比",dz_tags[2].string)
        my_tags = soup.find_all("span", "_1rsHot")
        print("点赞", my_tags[0].string)
        print("产品数", my_tags[1].string)
        print("回复比", my_tags[2].string)
        print("聊天时间回复", my_tags[3].string)
        print("加入时间", my_tags[4].string)
        print("粉丝", my_tags[5].string)

        #
        # 获取图片，页数,店铺评分 ！！！

        # 字典数据类型储存调用
        my_msg = {
            "rank": data[5],

            "price": price_tags[0].string,
            "off_": off_set,
            "type": all_type,
            "pingfen": pinfen,
            "num_sell": pinjia,
            "mon_sell": yuexl,
            "word_main": main_word_list,
            "dian_zan_shu": my_tags[0].string,
            "room_href": href,
            "goods_num": my_tags[1].string,
            "chat_back": my_tags[2].string,
            "chat_back_time": my_tags[3].string,
            "join_time": my_tags[4].string,
            "fans_num": my_tags[5].string

        }
        print("*" * 50)
        print(my_msg)
        # print(filename)
        if my_msg["goods_num"] =="N/A":
            my_msg["goods_num"]=0
        print("------------------------------------------------")
        # print(my_msg["off_"],str(my_msg['price']))
        # print(str(my_msg['type']),my_msg['pingfen'])
        in_list = [
            # RANKBY[filename[:-4]],
            data[0],
            data[5],
            title,  # replace the ","
            data[2],
            str(my_msg['price']),
            my_msg["off_"],
            str(my_msg['type']),
            data[3],  # 页数
            my_msg['pingfen'],
            my_msg["num_sell"],
            my_msg["mon_sell"],
            my_msg["dian_zan_shu"],
            str(my_msg["word_main"]),
            my_msg["room_href"],
            my_msg["goods_num"],
            my_msg["chat_back"],
            my_msg["chat_back_time"],
            my_msg["join_time"],
            my_msg["fans_num"]
        ]

        chang_msg(in_list)

    except TimeoutError:
        print("Time out!trying again")
        get_goods(data, STOPTIME)

    # except InterruptedError:
    #     print(" exeists!!!!")
    #     fath_sql = "update second_url_%s set my_status=1 where type='%s' and rank=%d"%(DIR_NAME,msg_list[0],msg_list[1])
    #     cur.execute(fath_sql)
    #     print("father_url status is changed")
    #     db.commit()

    except IOError as e:
        print(e)
        driver.quit()
        get_goods(data, STOPTIME)

    except TimeoutError:
        driver.quit()
        get_good(data,STOPTIME)

    except OSError :
        print("trying to restart...")
        #os.system("python3 get_main_msg.py")
        #with open("bug.txt","a",encoding="utf-8") as f:
        #    f.write("restart in %s"%time.ctime())
        #os._exit()
        driver.quit()
        get_goods(data,STOPTIME)

    except urllib3.exceptions.ProtocolError as e:
        driver.quit()
        with open("bug.txt","a",encoding='utf-8') as f:
            global num
            num +=1
            f.write("can't close the chromedriver %s,time:%s\n"%(num,time.ctime()))


    except Exception as e:
        # drvier.quit()
        print("抓取异常", e)
        global THIS_I
        THIS_I += 1
        if THIS_I > BIG:
            return "gg"
        print("正在进行第%s次访问" % THIS_I)
        print("尝试缓冲时间为%s" % STOPTIME)
        get_goods(data, STOPTIME)

    finally:
        driver.quit()
        # try:
        #     db.close()
        # except Exception as e:
        #     pass


# get_goods(' https://shopee.co.id/-Bayar-Di-Tempat-Tahan-lama-hitam-Wanita-Pria-Unisex-Anak-Quartz-Fashional-Wrist-Watch-Jam-Tangan-i.9501762.65961746',STOPTIME)
# with open("test.csv", "a", newline="", encoding="gb18030") as f:
#     writer = csv.writer(f)
#     writer.writerow(
#         ['类目', "排名",'标题', '产品链接', '价格	', '折扣', '	颜色（变体）', '页数', '评分', '评价数', '月销售', '点赞数', '关键词', '店铺链接', '店铺产品数',
#          '聊天百分比回复', '聊天回复', '加入时间', '粉丝'])
timeout(30)


def mul_main():
    #out = os.popen("ps aux | grep test_os").read()
    #restart_time = time.ctime().split(" ")[3].split(":")[1]
    #if int(restart_time)%20 ==0  :
    #    print("20 min kill the pross!!!")
    #    os.kill(out, signal.SIGKILL)
    print("line to mysql")
    db = pymysql.connect(h_line, user, pwd, db_name, charset='utf8')
    print("success mysql")
    # try:
    cur = db.cursor()
    get_url_sql = "select * from second_url_Season%s where my_status=%d  and time='%s' order by rand() limit 1000;" % (
    DIR_NAME, SECOND_STATUS,DATA_TIME)
    cur.execute(get_url_sql)
    data = cur.fetchall()

    # db.close()
    p = multiprocessing.Pool(processes=32)

    for rankBY in data:
        # 三个类别的排序方法的爬虫记录,记录在txt文本中(优化:存入数据库中), 参数设置在setting.py中print("正在爬取[[%s]]分类的数据"%(RANKSTYLE[rankBY]))
        i = 1
        p.apply_async(get_goods, args=(rankBY, STOPTIME))  # url前三位是排名,最后一位是\n
    print('正在多进程抓取写入第goods层链接')
    p.close()
    p.join()
    print('第goods层链接写入完成!')
    print("line to mysql..")
    cur.execute(get_url_sql)
    data = cur.fetchall()
    db.close()
    if len(data) != 0:
        mul_main()

    print("all Done!!!")


if __name__ == "__main__":
    # get_ip()
    try:
        # tomysql.start_item()
        mul_main()
    except OSError as e:
        print("\033[0;31;40m\twrong>>%s\033[0m" % e)

        with open("bug_%s.txt" % DIR_NAME, 'a', encoding='utf-8') as f:
            f.write(str(time.ctime()) + (e) + "\n")
        mul_main()


    print(time.ctime())
