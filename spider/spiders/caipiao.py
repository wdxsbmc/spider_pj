# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request

class CaipiaoSpider(scrapy.Spider):
    name = 'caipiao'
    allowed_domains = ['zhcw.com']
    start_urls = ['http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html']

    def parse(self, response):
        res = response.body
        htmlinfo = BeautifulSoup(res,'html.parser')
        resultinfo_qishu = htmlinfo.select('td')

        resultinfo_haoma = htmlinfo.select('em')

        #包括每一期的期号；开奖日期等信息

        resultinfo_haomalist = str(resultinfo_haoma).replace('<em class="rr">','').replace('</em>','').replace('<em>','').replace('[','').replace(']','').split(',')

        #print(len(resultinfo_qishu))
        #print(resultinfo_haoma)
        #print(resultinfo_haomalist)

        for i in range(0,len(resultinfo_qishu)-1,7):
            for j in range(0,2):
                if j == 0:
                    print('开奖日期：' + str(resultinfo_qishu[i+j]).replace('<td align="center">','').replace('</td>',''))
                else:
                    print('期 号：' + str(resultinfo_qishu[i+j]).replace('<td align="center">','').replace('</td>',''))
            x = []
            for n in range(0,7):
                x.append(resultinfo_haomalist[i+n])

            print('红色球：%s,%s,%s,%s,%s,%s;蓝色球：%s' % (x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

        init_urls = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_'
        for n in range(2,5):
            url=init_urls + str(n) + '.html'
            print url
            yield Request(url,callback=self.parse)
        pass
