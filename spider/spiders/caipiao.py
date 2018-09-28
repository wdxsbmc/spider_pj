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

        #data and number

        resultinfo_haomalist = str(resultinfo_haoma).replace('<em class="rr">','').replace('</em>','').replace('<em>','').replace('[','').replace(']','').split(',')

        #print(len(resultinfo_qishu))
        #print(resultinfo_haoma)
        #print(resultinfo_haomalist)

        for i in range(0,len(resultinfo_qishu)-1,7):
            for j in range(0,2):
                if j == 0:
                    print('date：' + str(resultinfo_qishu[i+j]).replace('<td align="center">','').replace('</td>',''))
                    cp_date = str(resultinfo_qishu[i+j]).replace('<td align="center">','').replace('</td>',''))

                else:
                    print('number：' + str(resultinfo_qishu[i+j]).replace('<td align="center">','').replace('</td>',''))
                    cp_num = str(resultinfo_qishu[i+j]).replace('<td align="center">','').replace('</td>',''))
            x = []
            for n in range(0,7):
                x.append(resultinfo_haomalist[i+n])

            print('red：%s,%s,%s,%s,%s,%s;blue：%s' % (x[0],x[1],x[2],x[3],x[4],x[5],x[6]))

            caipiao_item = CaiPiaoInfoItem()
            caipiao_item['cp_date'] = cp_date
            caipiao_item['cp_num'] = cp_num
            caipiao_item['cp_red_1'] = x[0]
            caipiao_item['cp_red_2'] = x[1]
            caipiao_item['cp_red_3'] = x[2]
            caipiao_item['cp_red_4'] = x[3]
            caipiao_item['cp_red_5'] = x[4]
            caipiao_item['cp_red_6'] = x[5]
            caipiao_item['cp_red_7'] = x[6]

            caipiao_item.save()

        init_urls = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_'
        for n in range(2,5):
            url=init_urls + str(n) + '.html'
            print url
            yield Request(url,callback=self.parse)
        pass
