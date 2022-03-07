# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from datetime import datetime
from platform import release
from unicodedata import category

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
# from scrapy.loader.processors import TakeFirst, MapCompose

types = ('PlainText', 'File', 'HTML', 'Markdown')


def type_check(t, value):
    if type(value) is not t:
        raise TypeError("Type of value must be '%s', not '%s'." % (t.__name__, type(value).__name__))
    else:
        return value


def type_check_str(value):
    return type_check(str, value)


def type_check_datetime(value):
    return type_check(datetime, value)


def notice_type_check(value):
    if value not in types:
        raise ValueError('Notice type must be %s.' % ' or '.join(types))
    else:
        return value


class NoticeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(input_processor=MapCompose(type_check_str, str.strip), output_processor=TakeFirst())
    type = scrapy.Field(input_processor=MapCompose(notice_type_check),
     output_processor=TakeFirst())  # PlainText/File/URL
    publisher = scrapy.Field(input_processor=MapCompose(type_check_str), output_processor=TakeFirst())
    url = scrapy.Field(input_processor=MapCompose(type_check_str), output_processor=TakeFirst())
    content = scrapy.Field(input_processor=MapCompose(type_check_str), output_processor=TakeFirst())
    publish_time = scrapy.Field(input_processor=MapCompose(type_check_datetime), output_processor=TakeFirst())
    tags = scrapy.Field(input_processor=MapCompose(type_check_str))
    column = scrapy.Field(input_peocessor=MapCompose(type_check_str))
    source = scrapy.Field(input_processor=MapCompose(type_check_str), output_processor=TakeFirst())

# This item is used to contain the content of the HTML notices to support Read Mode
class HTMLContentItem(scrapy.Item):
    url = scrapy.Field(input_processor=MapCompose(type_check_str), output_processor=TakeFirst())
    content = scrapy.Field(input_processor=MapCompose(type_check_str), output_processor=TakeFirst())
