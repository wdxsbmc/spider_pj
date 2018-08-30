# -*- coding: utf-8 -*-
import scrapy


class CaipiaoSpider(scrapy.Spider):
    name = 'caipiao'
    allowed_domains = ['zhcw.com']
    start_urls = ['http://zhcw.com/']

    def parse(self, response):
        pass
