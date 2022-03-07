from notify_scrapy.items import NoticeItem
from scrapy.loader import ItemLoader


class NoticeLoader(ItemLoader):
    def __init__(self, spider, selector=None, response=None, parent=None, **context):
        super(NoticeLoader, self).__init__(item=NoticeItem(), selector=selector, response=response, parent=parent,
                                           **context)
