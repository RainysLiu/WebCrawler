# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    #爬虫的名字
    name = 'qiubai'
    #允许的域名，域名限制
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    #重写父类的函数,自动被调回
    def parse(self, response):
        print('*'*50)
        divList = response.xpath('//*[@id="content-left"]/div')
        print(len(divList))
        items = []
        for odiv in divList:
            userImgeUrl = odiv.xpath('./div//img/@src').extract()[0]
            userName = odiv.xpath('./div//h2/text()')[0].extract().strip('\n\t\r')
            item ={
                '用户头像链接':userImgeUrl,
                '用户名':userName
            }
            items.append(item)
            print(item)
        print('*' * 50)
        return items



