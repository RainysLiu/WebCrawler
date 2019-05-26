# -*- coding: utf-8 -*-
import scrapy
from day9.moviepro.moviepro.items import MovieproItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.com/movie']

    page = 1
    url = 'http://www.id97.com/movie/?page={}'

    def parse(self, response):
        # 首先找到包含电影的所有div
        div_list = response.xpath('//div[starts-with(@class,"movie-item-in")]')
        # 遍历，提取一些信息
        for div in div_list:
            item = MovieproItem()
            # 获取电影海报
            item['post'] = div.xpath('./a/img/@data-src').extract_first()
            # 获取电影名字
            item['name'] = div.xpath('./div/h1/a/text()').extract_first()
            # 获取电影评分
            item['score'] =  div.xpath('./div/h1/em/text()').extract_first().strip(' - ').rstrip('分')
            #获取电影类型
            item['type'] = div.xpath('.//div[@class="otherinfo"]//a/text()').extract()
            # 获取电影详情页链接
            item['detail_url'] = div.xpath('./div/h1/a/@href').extract_first()

            yield scrapy.Request(url=item['detail_url'], callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        # 获取到传递过来的item
        item = response.meta['item']
        tbody = response.xpath('//div[@class="col-xs-8"]/table/tbody')
        # 提取导演
        item['director'] = tbody.xpath(".//tr/td/span[contains(text(),'导演')]/../../td[2]/a/text()").extract_first()
        # 提取主演
        item['actors'] = tbody.xpath(".//tr/td/span[contains(text(),'主演')]/../../td[2]/a/text()").extract()
        #地区
        item['region'] = tbody.xpath(".//tr/td/span[contains(text(),'地区')]/../../td[2]/a/text()").extract_first()
        #上映时间
        item['pub_time'] = tbody.xpath("tr/td/span[contains(text(),'上映时间')]/../../td[2]/text()").extract_first()
        #片长
        item['movie_time'] = tbody.xpath("tr/td/span[contains(text(),'片长')]/../../td[2]/text()").extract_first()
        #语言
        item['language'] = tbody.xpath("tr/td/span[contains(text(),'语言')]/../../td[2]/text()").extract_first()
        yield item
        # 接着发送请求，爬取指定页码的内容
        if self.page < 5:
            self.page += 1
            url = self.url.format(self.page)
            yield scrapy.Request(url=url, callback=self.parse)


