# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class MarxismSchoolPage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'marxism_school_page0'
    source = '27'
    publisher = '马克思主义学院'
    column = ['学院通知']
    start_urls = ['http://marx.zju.edu.cn/23482/list.htm']
    page_url = 'http://marx.zju.edu.cn/23482/list%d.htm'
    initial_page = 1
    list_xpath = '//ul[@class="cg-news-list"]/li'
    title_xpath = './/a/text()'
    url_xpath = './/a/@href'
    publish_time_xpath = './span/text()'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '专业院系'


class MarxismSchoolPage1Spider(MarxismSchoolPage0Spider):
    name = 'marxism_school_page1'
    source = '27'
    publisher = '马克思主义学院'
    column = ['图片新闻']
    start_urls = ['http://marx.zju.edu.cn/23485/list.htm']
    page_url = 'http://marx.zju.edu.cn/23485/list%d.htm'


class MarxismSchoolPage2Spider(MarxismSchoolPage0Spider):
    name = 'marxism_school_page2'
    source = '27'
    publisher = '马克思主义学院'
    column = ['学院动态']
    start_urls = ['http://marx.zju.edu.cn/23481/list.htm']
    page_url = 'http://marx.zju.edu.cn/23481/list%d.htm'


class MarxismSchoolPage3Spider(MarxismSchoolPage0Spider):
    name = 'marxism_school_page3'
    source = '27'
    publisher = '马克思主义学院'
    column = ['学术学科', '国际交流']
    start_urls = ['http://marx.zju.edu.cn/23464/list.htm']
    page_url = 'http://marx.zju.edu.cn/23464/list%d.htm'
