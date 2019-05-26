# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request

import pymysql


class XinpianchangproPipeline(object):
    # 开启爬虫的函数
    def open_spider(self, spider):
        # 打开文件
        self.fp = open('xinpianchang.txt', 'w', encoding='utf8')
        #建立数据库连接
        self.conn = self.database()
    def database(self):
        conn = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='4801',
            db='mydb',
            charset='utf8'
            )
        return conn
        
    def process_item(self, item, spider):
        d = dict(item)
        string = json.dumps(d, ensure_ascii=False)
        self.fp.write(string + '\n')
        self.download(item)
        self.insertMYSQL(item)
        return item
    def insertMYSQL(self,item):
        # 创建游标对象
        cursor = self.conn.cursor()
        try:
            cursor.execute("insert into movie(img_url,name,time,user)values('{}','{}','{}','{}')".format(item['image_url'],
                                                                                                         item['video_name'],item['release_date'], item['video_author']))
        except Exception:
            self.conn.rollback()
        self.conn.commit()
        cursor.close()

    def download(self, item):
        dirname = r'E:\工作区\WebCrawler\xinpianchangpro\xinpianchangpro\spiders\images'
        filename = item['video_name'].replace('|','').replace('/','').replace(':','') + '.jpg'
        filepath = os.path.join(dirname, filename)
        urllib.request.urlretrieve(item['image_url'], filepath)
    def close_spider(self, spider):
        # 关闭文件
        self.fp.close()
        #关闭数据库连接
        self.conn.close()

