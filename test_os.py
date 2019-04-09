import multiprocessing
import os,signal
import sys
import time


out=os.popen("ps aux | grep test_os").read()

a= 0


# 重启程序
def restart_program():
    print("重启。。。。。。。")
    python = sys.executable
    os.execl(python, python, *sys.argv)


def get_goods(num):
    global a
    a += 1
    time.sleep(2)
    print(a)
    if a ==5:
        a =0
        print("restart test_os.py after 5s...")
        time.sleep(5)
        os.kill(out,signal.SIGKILL)

        print("test_os.py was killed!")
        os.system("python3 test_os.py")
        # # sys.exit("123")
        # print("father exited!!")


def mul_test():
    global a
    p = multiprocessing.Pool(processes=4)

    for rankBY in range(50):
        # 三个类别的排序方法的爬虫记录,记录在txt文本中(优化:存入数据库中), 参数设置在setting.py中print("正在爬取[[%s]]分类的数据"%(RANKSTYLE[rankBY]))
        i = 1
        p.apply_async(get_goods, args=(rankBY, ))  # url前三位是排名,最后一位是\n
    print('正在多进程抓取写入第goods层链接')
    p.close()
    p.join()
    print('第goods层链接写入完成!')
    print("line to mysql..")


    print("all Done!!!")

mul_test()