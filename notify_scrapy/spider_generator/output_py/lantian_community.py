# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class LantianCommunityPage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'lantian_community_page0'
    source = '22'
    publisher = '蓝田学园'
    column = ['党建园地', '党员素质发展中心']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14397/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14397/list%d.htm'
    initial_page = 1
    list_xpath = '//ul[@class="news_list list2"]/li'
    title_xpath = './/a/@title'
    url_xpath = './/a/@href'
    publish_time_xpath = './/span[@class="news_meta"]/text()'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '学园行政'


class LantianCommunityPage1Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page1'
    source = '22'
    publisher = '蓝田学园'
    column = ['党建园地', '红船快讯']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14399/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14399/list%d.htm'


class LantianCommunityPage2Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page2'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '团委发文']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/twfw/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/twfw/list%d.htm'


class LantianCommunityPage3Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page3'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '一周活动预告']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/yzhdyg/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/yzhdyg/list%d.htm'


class LantianCommunityPage4Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page4'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '分团委学生团队', '组织工作']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/zzgz/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/zzgz/list%d.htm'


class LantianCommunityPage5Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page5'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '分团委学生团队', '志愿服务']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14404/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14404/list%d.htm'


class LantianCommunityPage6Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page6'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '分团委学生团队', '社会实践']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14405/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14405/list%d.htm'


class LantianCommunityPage7Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page7'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '分团委学生团队', '素质拓展']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14406/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14406/list%d.htm'


class LantianCommunityPage8Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page8'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '分团委学生团队', '学生会']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/xsh/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/xsh/list%d.htm'


class LantianCommunityPage9Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page9'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '分团委学生团队', '文体发展中心', '文体发展中心']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/27360/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/27360/list%d.htm'


class LantianCommunityPage10Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page10'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '分团委学生团队', '文体发展中心', '体育发展中心']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/27364/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/27364/list%d.htm'


class LantianCommunityPage11Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page11'
    source = '22'
    publisher = '蓝田学园'
    column = ['团学园地', '分团委学生团队', '班团风采']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14402/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14402/list%d.htm'


class LantianCommunityPage12Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page12'
    source = '22'
    publisher = '蓝田学园'
    column = ['学生事务', '资助工作']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14413/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14413/list%d.htm'


class LantianCommunityPage13Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page13'
    source = '22'
    publisher = '蓝田学园'
    column = ['学生事务', '评奖评优']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14414/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14414/list%d.htm'


class LantianCommunityPage14Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page14'
    source = '22'
    publisher = '蓝田学园'
    column = ['学生事务', '综合事务管理中心']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/27366/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/27366/list%d.htm'


class LantianCommunityPage15Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page15'
    source = '22'
    publisher = '蓝田学园'
    column = ['学生事务', '心理健康教育中心']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/27367/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/27367/list%d.htm'


class LantianCommunityPage16Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page16'
    source = '22'
    publisher = '蓝田学园'
    column = ['学生事务', '学生权益服务中心']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/xsqyfwzx/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/xsqyfwzx/list%d.htm'


class LantianCommunityPage17Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page17'
    source = '22'
    publisher = '蓝田学园'
    column = ['学业园地', '专业引导']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14419/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14419/list%d.htm'


class LantianCommunityPage18Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page18'
    source = '22'
    publisher = '蓝田学园'
    column = ['学业园地', '学务管理']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14417/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14417/list%d.htm'


class LantianCommunityPage19Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page19'
    source = '22'
    publisher = '蓝田学园'
    column = ['学业园地', '学风建设']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14418/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14418/list%d.htm'


class LantianCommunityPage20Spider(LantianCommunityPage0Spider):
    name = 'lantian_community_page20'
    source = '22'
    publisher = '蓝田学园'
    column = ['学业园地', '学业发展中心']
    start_urls = ['http://lantian.zju.edu.cn/ltoffice/14416/list.htm']
    page_url = 'http://lantian.zju.edu.cn/ltoffice/14416/list%d.htm'
