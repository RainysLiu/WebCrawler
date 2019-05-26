# -*- coding: utf-8 -*-
import scrapy



from day9.imagepro.imagepro.items import ImageproItem


class ImageSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['699pic.com']
    start_urls = ['http://699pic.com/nature.html']

    page = 1
    url = 'http://699pic.com/photo-0-11-{}-0-0-0.html'

    def parse(self, response):
        href_list = response.xpath('//div[@class="list"]/a/@href').extract()
        for imghref in href_list:
            yield scrapy.Request(url=imghref,callback=self.parse_detail)
        if self.page<2:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url,callback=self.parse)
    def parse_detail(self,response):
        item = ImageproItem()
        item['name'] = response.xpath('//div[@class="photo-view"]/h1/text()').extract_first()
        # 提取发布时间
        item['publish_time'] = response.xpath('//div[@class="photo-view"]/div/span[@class="publicityt"]/text()').extract_first().rstrip(' 发布')
        # 提取浏览量
        item['click'] = response.xpath('//div[@class="photo-view"]/div/span[@class="look"]/read/text()').extract_first()
        # 提取收藏量
        item['collect'] = response.xpath('//div[@class="photo-view"]/div/span[@class="collect"]/text()').extract_first().rstrip('收藏')
        # 提取下载量
        item['download'] = response.xpath('//div[@class="photo-view"]/div/span[@class="download"]/text()')[
            1].extract().rstrip(' 下载\t\n')
        # 提取图片的url
        item['image_src'] = response.xpath('//img[@id="photo"]/@src').extract_first()
        yield item
        # yield scrapy.Request(url=item['image_src'], callback=self.download)


