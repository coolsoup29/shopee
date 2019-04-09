import pymysql
import csv
import os
import sys
from to_mysql import *
from my_timeout import *
from setting import *
# ['类目',"排名",'标题', '产品链接', '价格  ', '折扣', '  颜色（变体）',
#  '页数', '评分', '评价数', '月销售', '点赞数', '关键词',
#  '店铺链接', '店铺产品数',
#  '聊天百分比回复', '聊天回复', '加入时间', '粉丝']
# 一共19个字段

def in_str(p):
    if str(p)[-1] == "\t":
        p = p[:-1]
    p = str(p).replace(".","")
    return p


# 将处理好的信息存入数据库
# def wrtie_to_mysql(msg_list):
#     db = pymysql.connect("localhost","lin","123456","yice",charset='utf8')
#     cur = db.cursor()
#     sql = 'create table  if not exists last_good_msg_%s (my_type enum("relevancy","ctime","sales"),rank smallint not null unique,title varchar(200) not null,good_url varchar(200) not null,price bigint not null,price_max bigint default 0,off_set tinyint default 0,off_set_NULL tinyint(1) default 0,style text not null,page tinyint not null,pinfen decimal(5,1),sum_pinjia bigint,sum_sell bigint,good_parisal bigint not null,main_words text,shop_url varchar(200) not null,sum_goods smallint not null,chat_back_per varchar(50) not null,chat_back varchar(50) not null,join_time tinyint not null,sum_fans bigint not null)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;'%DIR_NAME
#     cur.execute(sql)
#     # msg_str = ""
#     # for i in  msg_list:
#     #     # print(i)
#     #     msg_str += str(i)+","
#     try:
#         insert_sql = 'insert into last_good_msg_%s values("%s","%s","%s","%s",%s,%s,%s,"%s","%s",%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s",%s)'%(DIR_NAME,msg_list[0],msg_list[1],msg_list[2],msg_list[3],msg_list[4],msg_list[5],msg_list[6],msg_list[7],msg_list[8],msg_list[9],msg_list[10],msg_list[11],msg_list[12],msg_list[13],msg_list[14],msg_list[15],msg_list[16],msg_list[17],msg_list[18],msg_list[19],msg_list[20])
#         # print(insert_sql)
#         cur.execute(insert_sql)
#         print("写入成功",msg_list[1])
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         print(e,">>",insert_sql)




def chang_msg(main_word):#data是列表
    # for main_word in list(data):
    # main_words关键词是 -7
    # print(main_word)
    price = main_word[4].split(" - ")[0]
    # print(main_word[4].split(" - ")[0])
    # 区分单个价格和区间价格
    price_max = 0
    if len(main_word[4].split(" - "))==2:
        price_max = main_word[4].split(" - ")[1][2:]
        # print(price_max)

    title = main_word[2].replace('"""', "***")
    title = main_word[2].replace('""', "*")
    title = main_word[2].replace('"',"*")


    join_time = main_word[17].split(" ")[0]
    if join_time == "label_joined_ago":
        join_time = 0#注意，0代表label_joined_ago


    # 区分有折扣　和无优惠　
    try:
        # print(int(main_word[5][:-1]))
        off_set = int(main_word[5][:-1])

        off_set_NULL = 0# (off_set,0)  则是有优惠
    except Exception :
        off_set = 0
        off_set_NULL =1# (0,1) 则是无优惠

    # print(off_set,off_set_NULL)

    pinfen = main_word[8]
    # try:
    #     print(float(pinfen))
    # except Exception as e:
    #     print(e,pinfen)

    # print(pinfen,main_word[9],main_word[10],main_word[11])
    # print(len(main_word))

    if pinfen == "Belum ada penilaian":
        # print("chang %s to zero"%pinfen,main_word[1])
        pinfen = 0
        # print("ok")
    elif pinfen == "label_no_ratings_yet":
        pinfen = 0.1
        print("label_no_ratings_yet change ok")

    sum_pinjia = main_word[9]
    if sum_pinjia == 'None':
        sum_pinjia = 0

    sum_goods = main_word[11]
    if sum_goods == "N/A":
        sum_goods = 0

    # print(pinfen,main_word[9],main_word[10],main_word[11])
    # print(len(main_word))


    word = main_word[12].replace('""',"*")
    word = main_word[12].replace('"',"*")
    # print(main_word[7])

    typeof_goods = main_word[6].replace('""',"*")
    typeof_goods = main_word[6].replace('"',"*")


    sum_fans = main_word[18]
    if main_word[18] == "N/A":
        sum_fans = 0

# 类目,排名,标题,产品链接,价格   ,折扣,    颜色（变体）,页数,评分,评价数,月销售,点赞数,关键词,店铺链接,店铺产品数,聊天百分比回复,聊天回复,加入时间,粉丝
    # print(main_word[7])
    try:
        msg_list = [
            main_word[0],#类目
            main_word[1],#排名
            title,#标题
            main_word[3],#链接
            int(in_str(price[2:])),#最小值
            float(in_str(price_max)),#最大值(max/0)
            int(off_set),#(优惠,0)
            off_set_NULL,#无优惠(0/1)
            typeof_goods,#变体
            int(main_word[7]),#页数
            float(pinfen),#评分
            int(sum_pinjia),#评价数
            int(main_word[10]),#月销售
            int(sum_goods),#点赞数
            word,#关键词
            main_word[13],#店铺链接
            main_word[14],#店铺产品数
            main_word[15],#聊天回复比
            main_word[16],#聊天回复
            join_time,#加入时间
            int(sum_fans),#粉丝
        ]
        # print(write_list)
        db = pymysql.connect(h_line,user,pwd,db_name,charset='utf8')
        cur = db.cursor()
        # sql = 'create table  if not exists last_good_msg_Season%s (my_type enum("relevancy","ctime","sales"),rank smallint not null,title varchar(200) not null,good_url varchar(200) not null,price bigint not null,price_max bigint default 0,off_set tinyint default 0,off_set_NULL tinyint(1) default 0,style text not null,page tinyint not null,pinfen decimal(5,1),sum_pinjia bigint,sum_sell bigint,good_parisal bigint not null,main_words text,shop_url varchar(200) not null,sum_goods smallint not null,chat_back_per varchar(50) not null,chat_back varchar(50) not null,join_time tinyint not null,sum_fans bigint not null)CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;'%DIR_NAME
        # cur.execute(sql)
        # z增加约束,防止多台机器写入相同消息
        # try:
        #     cur.execute("alter table last_good_msg_Season%s add constraint lim_good_url unique (my_type,rank,time)"%DIR_NAME)
        # except Exception:
        #     pass
        # msg_str = ""
        # for i in  msg_list:
        #     # print(i)
        #     msg_str += str(i)+","
        try:
            insert_sql = 'insert into last_good_msg_Season%s values("%s","%s","%s","%s",%s,%s,%s,"%s","%s",%s,%s,%s,%s,%s,"%s","%s","%s","%s","%s","%s",%s,0,"%s")'%(DIR_NAME,msg_list[0],msg_list[1],msg_list[2],msg_list[3],msg_list[4],msg_list[5],msg_list[6],msg_list[7],msg_list[8],msg_list[9],msg_list[10],msg_list[11],msg_list[12],msg_list[13],msg_list[14],msg_list[15],msg_list[16],msg_list[17],msg_list[18],msg_list[19],msg_list[20],DATA_TIME)
            print(insert_sql)
            cur.execute(insert_sql)
            print("写入成功",msg_list[1])
            db.commit()
            fath_sql = "update second_url_Season%s set my_status=1 where type='%s' and rank=%d and time='%s';"%(DIR_NAME,msg_list[0],msg_list[1],DATA_TIME)
            cur.execute(fath_sql)
            print("father_url status is changed")
            db.commit()


        #!!!!!for exists
        except pymysql.err.IntegrityError:
            print(" exeists!!!!")
            fath_sql = "update second_url_Season%s set my_status=1 where type='%s' and rank=%d and time='%s'" % (
            DIR_NAME, msg_list[0], msg_list[1],DATA_TIME)
            cur.execute(fath_sql)
            print("father_url status is changed")
            db.commit()


        except Exception as e:
            db.rollback()
            print(e,">>")

    except Exception as e:
        print(e,main_word[1])
        sys.exit()
    finally:
        db.close()
