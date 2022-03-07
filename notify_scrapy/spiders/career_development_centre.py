from datetime import datetime

import scrapy

import re

from notify_scrapy.notice_loader import NoticeLoader


class CareerDevelopmentCentreSpider(scrapy.Spider):
    name = 'career_development_centre'
    source = 7
    publisher = '就业指导与服务中心'
    type = 'HTML'
    column = ['新闻公告', '新闻动态']
    start_urls = ['http://www.career.zju.edu.cn/jyxt/jygz/new/getContent.zf?minCount=0\
                  &maxCount=10&lmjdid=739BEBB72A072B25E0538713470A6C41&sjlmid=undefined&lmtype=2&lx=2&_=1621613604205']
    publisher_group = '学校部门'

    def __init__(self, name=None, **kwargs):
        super(CareerDevelopmentCentreSpider, self).__init__(name, **kwargs)
        self.stop_signal = False
        self.count = 0
        self.data_src = ''
        self.data_xwid = ''
        self.data_lmtype = ''
        self.data_href = ''

    def parse(self, response):
        for node in response.xpath('//ul[@class="com-list"]/li'):
            loader = NoticeLoader(self, selector=node)
            loader.add_xpath('title', './a//span/text()')
            self.data_src = node.xpath('./a/@data-src').extract_first()
            self.data_xwid = node.xpath('./a/@data-xwid').extract_first()
            self.data_lmtype = node.xpath('./a/@data-lmtype').extract_first()
            self.data_href = node.xpath('./a/@href').extract_first()
            if self.data_href == "javascript:void(0)":
                loader.add_value('url', response.urljoin("http://www.career.zju.edu.cn/jyxt" + self.data_src + \
                                                         "xwid=" + self.data_xwid + "&lmtype=" + self.data_lmtype))
            else:
                loader.add_value('url', response.urljoin(self.data_href))
            loader.add_value('publish_time',
                             datetime.strptime(node.xpath('.//span[@class="news-time"]/text()').extract_first(),
                                               '%Y-%m-%d'))
            yield loader.load_item()
            if self.stop_signal:
                return

        self.count += 10

        yield response.follow(re.search("http.+?minCount=", self.start_urls[0]).group(0) + \
                              '%d&maxCount=' % self.count + '%d' % (self.count + 10) + \
                              re.search("&lmjdid.+", self.start_urls[0]).group(0), callback=self.parse)


class CareerDevelopmentCentreSpider1(CareerDevelopmentCentreSpider):
    name = 'career_development_centre1'
    column = ['新闻公告', '活动通知']
    start_urls = ['http://www.career.zju.edu.cn/jyxt/jygz/new/getContent.zf?minCount=0\
                  &maxCount=10&lmjdid=739BEBB72A0B2B25E0538713470A6C41&sjlmid=undefined&lmtype=2&lx=2&_=1621613604232']


class CareerDevelopmentCentreSpider2(CareerDevelopmentCentreSpider):
    name = 'career_development_centre2'
    column = ['新闻公告', '学院动态']
    start_urls = ['http://www.career.zju.edu.cn/jyxt/jygz/new/getContent.zf?minCount=0\
    &maxCount=10&lmjdid=739BEBB72A0C2B25E0538713470A6C41&sjlmid=undefined&lmtype=2&lx=2&_=1621613604233']


class CareerDevelopmentCentreSpider3(CareerDevelopmentCentreSpider):
    name = 'career_development_centre3'
    column = ['新闻公告', '公示公告']
    start_urls = ['http://www.career.zju.edu.cn/jyxt/jygz/new/getContent.zf?minCount=0\
    &maxCount=10&lmjdid=739BEBB72A252B25E0538713470A6C41&sjlmid=undefined&lmtype=2&lx=2&_=1621613604243']
