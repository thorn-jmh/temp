from datetime import datetime

import scrapy

from notify_scrapy.notice_loader import NoticeLoader

LIBRARY_URL = 'http://libweb.zju.edu.cn/39478/list.htm'


class LibrarySpider(scrapy.Spider):
    name = 'library'
    source = 24
    publisher = '浙江大学图书馆'
    type = 'HTML'
    start_urls = [LIBRARY_URL]
    publisher_group = '学校部门'

    def __init__(self, name=None, **kwargs):
        super(LibrarySpider, self).__init__(name, **kwargs)
        self.stop_signal = False
        self.page = 1

    def parse(self, response):
        for node in response.xpath('//ul[@class="news_list list2"]/li'):
            loader = NoticeLoader(self, selector=node)
            loader.add_xpath('title', './/a/text()')
            loader.add_value('url', response.urljoin(node.xpath('.//a/@href').extract_first()))
            loader.add_value('publish_time',
                             datetime.strptime(node.xpath('.//span[@class="news_meta"]/text()').extract_first(),
                                               '%Y-%m-%d'))
            yield loader.load_item()
            if self.stop_signal:
                return

        self.page += 1
        yield response.follow('http://libweb.zju.edu.cn/39478/list' + '%d.htm' % self.page, callback=self.parse)
