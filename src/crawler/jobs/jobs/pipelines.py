# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import mongodb

class LagouPipeline(object):
    def __init__(self):
        # self.file = codecs.open('lagou.json', mode='wb', encoding='utf-8')
        self.db = mongodb.Mongodb('127.0.0.1', 27017, 'job_info', 'jobs')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item)) + '\n'
        # self.file.write(line.decode('unicode_escape'))
        self.db.save(item)
        return item
