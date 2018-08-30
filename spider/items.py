# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CaipiaoItems(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    idx = scrapy.Field()
    date = scrapy.Field()
    n1 = scrapy.Field()
    n2 = scrapy.Field()
    n3 = scrapy.Field()
    n4 = scrapy.Field()
    n5 = scrapy.Field()
    n6 = scrapy.Field()
    n7 = scrapy.Field()

    pass
