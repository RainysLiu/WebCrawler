# -*- coding: utf-8 -*-
import scrapy

from day9.qiubaipro.qiubaipro.items import QiubaiproItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    page = 1
    url = 'https://www.qiushibaike.com/8hr/page/{}/'

    def parse(self, response):
        # 解析，首先找到所有的段子div
        div_list = response.xpath('//div[starts-with(@id,"qiushi_tag")]')
        # 遍历，依次提取每一个段子信息
        for div in div_list:
            # 创建item对象
            item = QiubaiproItem()
            # 获取头像链接
            item['face_url'] = div.xpath('./div[1]//img/@src').extract_first()
            # 获取用户名
            item['name'] = div.css('.author h2::text').extract_first()
            # 用户年龄
            item['age'] = div.xpath('./div[1]/div/text()').extract_first()
            # 内容
            # 第一种方法
            # content_list = div.xpath('.//div[@class="content"]/span//text()').extract()
            # content = ''.join(content_list).strip('\n\t\r')
            # item['content'] = content
            # 第二种方法
            item['content'] = div.xpath('.//div[@class="content"]/span')[0].xpath('string(.)').extract_first()
            # 好笑个数
            item['haha_count'] = div.css('.number::text').extract()[0]
            # 评论个数
            item['comment_count'] = div.css('.number::text').extract()[1]

            yield item

        # 接着发送请求，爬取指定页码的内容
        if self.page < 5:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)