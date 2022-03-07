# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import re
import pdb
from datetime import datetime

import pytz
from scrapy.exceptions import DropItem

from notify_scrapy.items import NoticeItem


# Make sure not both of url and content are None
class ContentCheckPipeline:
    def process_item(self, item, spider):
        if not isinstance(item, NoticeItem):
            return item
        missing = 0
        keys = item.keys()
        for field in ('url', 'content'):
            if field in keys:
                continue
            value = getattr(spider, field, None)
            if value is not None:
                item[field] = value
            else:
                item[field] = ''
                missing += 1
        if missing == 2:
            # spider.stop_signal = True
            raise DropItem('At least a url or a content must be given.')
        return item


class ItemCheckPipeline:
    def process_item(self, item, spider):
        if not isinstance(item, NoticeItem):
            return item
        keys = item.keys()
        for field in NoticeItem.fields.keys() - ['url', 'content', 'tags', 'column']:
            if field in keys:
                continue
            value = getattr(spider, field, None)
            if value is not None:
                item[field] = value
            else:
                # spider.stop_signal = True
                # This is used for test,if it works well, it can be kept
                raise DropItem('Missing field: %s.' % field)
        return item


class TagsHandlerPipeline:
    def process_item(self, item, spider):
        if not isinstance(item, NoticeItem):
            return item
        item['column'] = getattr(spider, 'column', []) + item.get('column', [])
        item['tags'] = getattr(spider, 'tags', []) + item.get('tags', [])
        # Handle auto tags
        auto_tags = getattr(spider, 'auto_tags', [])
        item['tags'].extend([auto_tag for auto_tag in auto_tags if auto_tag in item['title']])
        # Handle detected tags
        detected_tags = re.findall(r'[【\[](.+?)[】\]]', item['title'])
        item['tags'].extend([tag for tag in detected_tags if tag not in item['tags']])
        return item


class TimeLimitCheckPipeline:
    def __init__(self, time_limit):
        self.time_limit = time_limit

    @classmethod
    def from_crawler(cls, crawler):
        tz = pytz.timezone(crawler.settings['TIME_ZONE'])
        # pdb.set_trace()
        return cls(
            time_limit=int(tz.localize(crawler.settings.get('NOTICE_TIME_LIMIT', datetime.now())).timestamp())
        )

    def process_item(self, item, spider):
        if not isinstance(item, NoticeItem):
            return item
        # pdb.set_trace()
        if item['publish_time'] < self.time_limit:
            if getattr(spider, 'max_sticky', 0) > 0:
                logging.getLogger('notify.scrapy').info('A possible sticky notice was found (too old). '
                                                        'Allowed sticky notice(s) left: %d.' % spider.max_sticky)
            else:
                spider.stop_signal = True
                raise DropItem('The notice is beyond the earliest time limit.')
        return item


class DateTimeHandlerPipeline:
    def process_item(self, item, spider):
        if not isinstance(item, NoticeItem):
            return item
        # pdb.set_trace()
        tz = pytz.timezone(spider.settings['TIME_ZONE'])
        item['publish_time'] = int(tz.localize(item['publish_time']).timestamp())
        return item
