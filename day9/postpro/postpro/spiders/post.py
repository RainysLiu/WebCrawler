# -*- coding: utf-8 -*-
import scrapy


class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['cn.bing.com']
    #start_urls = ['http://cn.bing.com/']




    # 爬虫启动就会执行这个方法
    # def start_requests(self):
    # 	for url in start_urls:
    # 		yield scrapy.Request(url=url, callback=self.parse)
    # 如果上来就想直接发送post，需要重写start_requests这个方法

    def start_requests(self):
        post_url = 'https://cn.bing.com/ttranslationlookup?&IG=173800F312B648A9A3172BEF6BAAFF4F&IID=translator.5036.1'
        # 表单数据
        str = input('请输入你想查询的关键字:')
        formdata = {
            'from': 'zh-CHS',
            'to': 'en',
            'text': str,
        }
        # 发送post请求
        yield scrapy.FormRequest(url=post_url, callback=self.parse, formdata=formdata)
    def parse(self,response):
        print('*'*50)
        print(response.text)
        print('*'*50)
