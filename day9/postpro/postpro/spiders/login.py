# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['so.gushiwen.org']
    start_urls = ['http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx']

    def parse(self, response):
        # 提取你需要的信息即可
        image_src = 'https://so.gushiwen.org' + response.css('#imgCode::attr(src)').extract_first()
        # image_ret = s.get(image_src, headers=headers)
        # 获取那两个参数
        self.viewstat = response.css('#__VIEWSTATE::attr(value)').extract_first()
        self.viewg = response.css('#__VIEWSTATEGENERATOR::attr(value)').extract_first()
        yield scrapy.Request(url=image_src, callback=self.download)
    def download(self,response):
        with open('code.png', 'wb') as fp:
            fp.write(response.body)

        code = input('请输入验证码:')
        # 发送post请求
        formdata = {
            '__VIEWSTATE': self.viewstat,
            '__VIEWSTATEGENERATOR': self.viewg,
            'from': 'http://so.gushiwen.org/user/collect.aspx',
            'email': '1090509990@qq.com',
            'pwd': '123456',
            'code': code,
            'denglu': '登录',
        }
        post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
        yield scrapy.FormRequest(url=post_url, formdata=formdata, callback=self.parse_post)
    def parse_post(self,response):
        with open('loginok.html', 'wb') as fp:
            fp.write(response.body)

