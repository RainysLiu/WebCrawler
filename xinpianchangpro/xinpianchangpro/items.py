# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XinpianchangproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_url = scrapy.Field()
    video_name = scrapy.Field()
    video_author = scrapy.Field()
    release_date = scrapy.Field()
    #video_url = scrapy.Field()
