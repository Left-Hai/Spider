# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter


class MaitianSpiderPipeline(object):
    def __init__(self, file):
        self.file_name = file

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            file_name=crawler.settings.get('SAVEJSON_FILENAME'),
        )

    def open_spider(self, spider):
        self.file = open(self.file_name, 'wb')
        self.export = JsonItemExporter(self.file)
        self.export.start_exporting()

    def process_item(self, item, spider):
        self.export.export_item(item)
        return item

    def close_spider(self, spider):
        self.file.close()
        self.export.finish_exporting()
