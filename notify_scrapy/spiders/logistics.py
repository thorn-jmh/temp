from datetime import datetime

import scrapy

from notify_scrapy.notice_loader import NoticeLoader


class LogisticsSpider0(scrapy.Spider):
    name = 'logistics_0'
    source = 26
    publisher = '浙江大学后勤集团'
    type = 'HTML'
    start_urls = ['http://zulg.zju.edu.cn/index.php?c=Index&a=tongzhi_gonggao&catid=172']
    publisher_group = '学校部门'
    column = ['服务大厅', '服务公告']

    def __init__(self, name=None, **kwargs):
        super(LogisticsSpider0, self).__init__(name, **kwargs)
        self.stop_signal = False
        self.page = 1

    def parse(self, response):
        for node in response.xpath('//div[@class="you_news"]/ul/li'):
            loader = NoticeLoader(self, selector=node)
            loader.add_xpath('title', './a/text()')
            loader.add_value('url', response.urljoin(node.xpath('./a/@href').extract_first()))
            loader.add_value('publish_time',
                             datetime.strptime(node.xpath('./span/text()').extract_first(), '%Y-%m-%d'))
            yield loader.load_item()
            if self.stop_signal:
                return

        self.page += 1
        yield response.follow(self.start_urls[0] + '&p=%d' % self.page, callback=self.parse)


class LogisticsSpider1(scrapy.Spider):
    name = 'logistics_1'
    source = 26
    publisher = '浙江大学后勤集团'
    type = 'HTML'
    start_urls = ['http://zulg.zju.edu.cn/index.php?c=Index&a=tlist&model=more&fid=252&pid=254']
    publisher_group = '学校部门'
    column = ['服务大厅', '日常通知']

    def __init__(self, name=None, **kwargs):
        super(LogisticsSpider1, self).__init__(name, **kwargs)
        self.stop_signal = False
        self.page = 1

    def parse(self, response):
        for node in response.xpath('//div[@class="you_news"]/ul/li'):
            loader = NoticeLoader(self, selector=node)
            loader.add_xpath('title', './a/text()')
            loader.add_value('url', response.urljoin(node.xpath('./a/@href').extract_first()))
            loader.add_value('publish_time',
                             datetime.strptime(node.xpath('./span/text()').extract_first(), '%Y-%m-%d'))
            yield loader.load_item()
            if self.stop_signal:
                return

        self.page += 1
        yield response.follow(self.start_urls[0] + '&p=%d' % self.page, callback=self.parse)