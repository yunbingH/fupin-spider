# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FupinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gys_name = scrapy.Field()
    gys_province = scrapy.Field()
    gys_city = scrapy.Field()
    gys_county = scrapy.Field()
