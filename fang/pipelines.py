from scrapy.exporters import JsonLinesItemExporter
import pymongo

class FangPipeline(object):
    def __init__(self):
        self.newhouse_fp = open('newhouse.json','wb')
        self.esfhouse_fp = open('esfhouse.json','wb')
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouse_fp,ensure_ascii=False)
        self.esfhouse_exporter = JsonLinesItemExporter(self.esfhouse_fp,ensure_ascii=False)

    def process_item(self, item, spider):
        self.newhouse_exporter.export_item(item)
        self.esfhouse_exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.newhouse_fp.close()
        self.esfhouse_fp.close()



# 保存到mongodb
class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db,mongo_user,mongo_pwd):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_user = mongo_user
        self.mongo_pwd = mongo_pwd

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB'),
            mongo_user = crawler.settings.get('MONGO_USERNAME'),
            mongo_pwd = crawler.settings.get('MONGO_PASSWORD')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri,username=self.mongo_user,password=self.mongo_pwd)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()