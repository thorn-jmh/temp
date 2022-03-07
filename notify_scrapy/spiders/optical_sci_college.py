# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class OpticalSciCollegePage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'optical_sci_college_page0'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '本科生教学', '日常通知']
    start_urls = ['http://office.opt.zju.edu.cn/38204/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38204/list%d.htm'
    initial_page = 1
    list_xpath = '//div[@class="content-middle-list"]//td/div[1]//tr'
    title_xpath = './/a/@title'
    url_xpath = './/a/@href'
    publish_time_xpath = './td[3]/text()'
    publish_time_format = '[%Y-%m-%d]'
    publisher_group = '专业院系'


class OpticalSciCollegePage1Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page1'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '本科生教学', '教学资讯']
    start_urls = ['http://office.opt.zju.edu.cn/38205/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38205/list%d.htm'


class OpticalSciCollegePage2Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page2'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '本科生教学', 'SRTP']
    start_urls = ['http://office.opt.zju.edu.cn/38206/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38206/list%d.htm'


class OpticalSciCollegePage3Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page3'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '本科生教学', '毕业设计']
    start_urls = ['http://office.opt.zju.edu.cn/38207/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38207/list%d.htm'


class OpticalSciCollegePage4Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page4'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '本科生教学', '文件下载']
    start_urls = ['http://office.opt.zju.edu.cn/38208/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38208/list%d.htm'


class OpticalSciCollegePage5Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page5'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '本科生教学', '管理文件']
    start_urls = ['http://office.opt.zju.edu.cn/38209/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38209/list%d.htm'


class OpticalSciCollegePage6Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page6'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '本科生教学', '信息查询']
    start_urls = ['http://office.opt.zju.edu.cn/38210/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38210/list%d.htm'


class OpticalSciCollegePage7Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page7'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '本科生教学', '本科生交流']
    start_urls = ['http://office.opt.zju.edu.cn/38211/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38211/list%d.htm'


class OpticalSciCollegePage8Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page8'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '对外交流', '本科生交流']
    start_urls = ['http://office.opt.zju.edu.cn/38224/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38224/list%d.htm'


class OpticalSciCollegePage9Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page9'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '学生工作', '日常信息']
    start_urls = ['http://office.opt.zju.edu.cn/38230/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38230/list%d.htm'


class OpticalSciCollegePage10Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page10'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '学生工作', '学生党建']
    start_urls = ['http://office.opt.zju.edu.cn/38231/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38231/list%d.htm'


class OpticalSciCollegePage11Spider(OpticalSciCollegePage0Spider):
    name = 'optical_sci_college_page11'
    source = '33'
    publisher = '光电科学与工程学院'
    column = ['首页', '学生工作', '团学联']
    start_urls = ['http://office.opt.zju.edu.cn/38232/list.htm']
    page_url = 'http://office.opt.zju.edu.cn/38232/list%d.htm'
