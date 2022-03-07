from datetime import datetime

import scrapy
from scrapy.loader import ItemLoader

from notify_scrapy.items import NoticeItem


class BaseHTMLSpider(scrapy.Spider):
    name = ''
    source = ''
    publisher = ''
    column = []
    type = 'HTML'
    page_url = ''
    initial_page = 0
    list_xpath = ''
    title_xpath = ''
    url_xpath = ''
    publish_time_xpath = ''
    publish_time_format = ''
    max_sticky = 10     # change it if necessary
    publisher_group = ''
    publish_time_xpath_extra = ''

    def __init__(self, name=None, **kwargs):
        super(BaseHTMLSpider, self).__init__(name, **kwargs)
        self.stop_signal = False
        self.page = self.initial_page

    def parse(self, response):
        nodes = response.xpath(self.list_xpath)
        # if response.status == 302:
        #     return
        # Not sure for it can be save. Try to use it to avoid redirecting while many pages change from
        # .htm to .psp and they will loop forever
        if len(nodes) == 0:
            return

        for node in nodes:
            loader = ItemLoader(item=NoticeItem(), selector=node)
            loader.add_xpath('title', self.title_xpath)
            loader.add_value('url', response.urljoin(node.xpath(self.url_xpath).extract_first()))
            pub_time_text = node.xpath(self.publish_time_xpath).extract_first()
            if len(pub_time_text) >= 6:
                if list(pub_time_text)[3] == '-':
                    pub_time_text = list(pub_time_text)
                    pub_time_text.insert(1, "20")
                    pub_time_text = "".join(pub_time_text)
            # This is only for time like [21-08-09], now it become [2021-08-09]
            if self.publish_time_xpath_extra != '':
                if self.publish_time_xpath_extra == './/div[@class="time fl"]/h3/text()':
                    pub_time_text_extra = node.xpath(self.publish_time_xpath_extra).extract_first()
                    pub_time_text = pub_time_text + '-' + pub_time_text_extra
                    # This is for isee_college
                if self.publish_time_xpath_extra == './/div[@class="date fl"]/p[@class="year"]/text()':
                    pub_time_text_extra = node.xpath(self.publish_time_xpath_extra).extract_first()
                    pub_time_text = "20" + pub_time_text_extra + '-' + pub_time_text
                    # This is for polymer_depart
                if self.publish_time_xpath_extra == './/div[@class="date"]/p[@class="y"]/text()':
                    pub_time_text_extra = node.xpath(self.publish_time_xpath_extra).extract_first()
                    pub_time_text = pub_time_text_extra + '-' + pub_time_text
                    # This is for math_school
            if pub_time_text:
                loader.add_value('publish_time', datetime.strptime(pub_time_text, self.publish_time_format))
            yield loader.load_item()
            if self.stop_signal:
                return
        self.page += 1
        yield response.follow(self.page_url % self.page, callback=self.parse)
