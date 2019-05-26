# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieproItem(scrapy.Item):
    # define the fields for your item here like:
    post = scrapy.Field()
    name = scrapy.Field()
    score = scrapy.Field()
    type = scrapy.Field()
    detail_url = scrapy.Field()

    director = scrapy.Field()
    actors = scrapy.Field()
    region = scrapy.Field()
    pub_time = scrapy.Field()
    movie_time = scrapy.Field()
    language = scrapy.Field()


