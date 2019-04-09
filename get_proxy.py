import time

import requests



def st():
    req=requests.get("http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=e38894b1451d461ebf948a1d54d757f5&count=5&expiryDate=0&format=2&newLine=3")
    req.encoding='utf-8'

    html=req.text
    print(html)
    with open('ip.txt','w',encoding='utf-8') as f:
        f.write(html)




while True:
    print("正在更新proxy")
    st()
    time.sleep(10)
