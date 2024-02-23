# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FupinPipeline:
    def process_item(self, item, spider):
        print(item['gys_name'], item['gys_province'], item['gys_city'], item['gys_county'])
        return item
