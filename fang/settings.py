

BOT_NAME = 'fang'
SPIDER_MODULES = ['fang.spiders']
NEWSPIDER_MODULE = 'fang.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1



DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

ITEM_PIPELINES = {
   # 'fang.pipelines.FangPipeline': 300,
   'fang.pipelines.MongoPipeline': 400,
}

DOWNLOADER_MIDDLEWARES = {
    'fang.middlewares.my_useragent': 300,
}


# 1、确保request存储到redis中
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 2、确保所有爬虫共享相同的去重指纹
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 3、在redis中保持scrapy-redis用到的队列，不会清理redis中的队列，从而可以实现暂停和恢复的功能。
SCHEDULER_PERSIST = True

# 设置连接redis信息，mast主机ip，此处为战神k650D本机ip
REDIS_HOST = '192.168.43.68'
REDIS_PORT = 6379
#如果redis数据库有密码，使用如下方法：
# REDIS_URL = 'redis://username:password@192.168.43.68:6379'

MONGO_URI = '192.168.43.68'
MONGO_DB = 'fangtianxia'
#在CentOs下写入数据需要使用账号密码连接
MONGO_USERNAME = 'root'
MONGO_PASSWORD = '123456'

# MONGO_URL = 'mongodb://root:123456@192.168.43.68:27017'