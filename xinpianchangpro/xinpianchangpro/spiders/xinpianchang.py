# -*- coding: utf-8 -*-
import scrapy

from xinpianchangpro.items import XinpianchangproItem


class XinpianchangSpider(scrapy.Spider):
    name = 'xinpianchang'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/id-0/sort-addtime/type-0/']

    page = 1
    url = 'http://www.xinpianchang.com/channel/index/id-0/sort-addtime/type-0/page-{}/'

    def parse(self, response):
        li_list = response.xpath('//li[@class="enter-filmplay"]')
        for li in li_list:
            item = XinpianchangproItem()
            item['image_url'] = li.xpath('./a/img/@_src').extract_first()
            item['video_name'] = li.xpath('.//div[@class="video-con-top"]/a/p/text()').extract_first()
            item['video_author'] = li.xpath('.//div[@class="user-info"]/a//span[2]/text()').extract_first().strip('\t\n')
            item['release_date'] = li.xpath('.//div[@class="video-hover-con"]/p/text()').extract_first().strip(' 发布')
            yield item
        if self.page<5:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)
