# 配置不同参数




rankBY_list = ['ctime','relevancy','sales']  # ,'relevancy''ctime',

# 用于识别当前类别(不够灵活，但相对直观)
RANKSTYLE={
    "relevancy":"有关的",
    "ctime":"最新的",
    "sales":"畅销的",
}

# mysql setting
h_line = "localhost"   # 111.230.10.127
user = "root" # yice
db_name = 'shopee_rank'
pwd = "yice1821"


# 设置缓冲时间
STOPTIME = 5

# 爬取页数
MAX_PAGE=100

# 判断每页商品数（用于判断网页是否加载完成，商品页有时候50个，有时候49个）
# 每页商品低于等于48个 时 重新加载
MAX_GOODS_ONEPAGE=44

# 抓取二层链接的筛选 STATUS码
SECOND_STATUS=0

# 异常的 STATUS码数 !!!下架商品STATUS+3
ERROR_STATUS=3    #暂时不考虑
