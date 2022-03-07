# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from urllib.parse import urljoin

from lxml.html.clean import Cleaner
from scrapy import Request
from scrapy.exceptions import DropItem

from notify_scrapy.items import HTMLContentItem, NoticeItem
from notify_scrapy.parser_selector import select_parser

url_regex = re.compile(r"<(.*?)(src|href)=\"(?!http)(.*?)\"(.*?)>")


class FetchHTMLContentPipeline:
    """
    The pipeline that fetches HTML content to support read mode.
    """

    def __init__(self, crawler):
        self.crawler = crawler

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_item(self, item, spider):
        if not isinstance(item, NoticeItem) or item['type'] != 'HTML':
            return item
        url = item['url']
        parser = select_parser(url)
        if parser:
            request = Request(url, callback=parser)
            request.meta['origin_url'] = url
            self.crawler.engine.crawl(request, spider)
        return item


class HTMLContentCheckPipeline:
    """
    The pipeline that checks if HTML content item is correct.
    """

    def process_item(self, item, spider):
        if not isinstance(item, HTMLContentItem):
            return item
        for key in ['content', 'url']:
            if not item.get(key):
                raise DropItem('%s of HTMLContentItem can not be empty.' % key)
        return item


class HTMLContentCleanerPipeline:
    """
    The pipeline that cleans HTML content in following steps:
    * Removes any <meta> tags
    * Removes any embedded objects (flash, iframes)
    * Removes any <link> tags
    * Removes any style tags
    * Removes any processing instructions
    * Removes any style attributes. Defaults to the value of the style option
    * Removes any Javascript, like an onclick attribute. Also removes stylesheets as they could contain Javascript
    * Removes any comments
    * Removes any frame-related tags
    * Removes any form tags
    * Tags that aren't wrong, but are annoying. <blink> and <marquee>
    * Remove any tags that aren't standard parts of HTML
    * Keep src, color, href, title, name attrs only
    * Remove span, font, div tags. Their content will get pulled up into the parent tag
    """

    def process_item(self, item, spider):
        if not isinstance(item, HTMLContentItem):
            return item
        cleaner = Cleaner(page_structure=False,
                          meta=True,
                          embedded=True,
                          links=True,
                          style=True,
                          processing_instructions=True,
                          inline_style=True,
                          scripts=True,
                          javascript=True,
                          comments=True,
                          frames=True,
                          forms=True,
                          annoying_tags=True,
                          remove_unknown_tags=True,
                          safe_attrs_only=True,
                          safe_attrs=frozenset(['src', 'color', 'href', 'title', 'name']),
                          remove_tags=('span', 'font', 'div')
                          )

        item['content'] = cleaner.clean_html(item['content'])
        return item


class RelativeURLHandlerPipeline:
    """
    The pipeline that converts all relative URL in HTML content to absolute URL.
    """

    def process_item(self, item, spider):
        if not isinstance(item, HTMLContentItem):
            return item

        def url_repl(match):
            return '<%s%s="%s"%s>' % (
                match.group(1), match.group(2), urljoin(item['url'], match.group(3)), match.group(4))

        item['content'] = url_regex.sub(url_repl, item['content'])
        return item
