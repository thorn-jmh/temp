# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class LawSchoolPage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'law_school_page0'
    source = '23'
    publisher = '光华法学院'
    column = ['首页', '信息公告']
    start_urls = ['https://webplus.zju.edu.cn/_s331/15348/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/15348/list.psplist%d.htm'
    initial_page = 1
    list_xpath = '//ul[@class="list_ul"]/li'
    title_xpath = './/a/@title'
    url_xpath = './/a/@href'
    publish_time_xpath = './/span/text()'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '专业院系'


class LawSchoolPage1Spider(LawSchoolPage0Spider):
    name = 'law_school_page1'
    source = '23'
    publisher = '光华法学院'
    column = ['教育教学', '本科生教育', '学籍管理']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16322/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16322/list.psplist%d.htm'


class LawSchoolPage2Spider(LawSchoolPage0Spider):
    name = 'law_school_page2'
    source = '23'
    publisher = '光华法学院'
    column = ['教育教学', '本科生教育', '培养过程']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16323/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16323/list.psplist%d.htm'


class LawSchoolPage3Spider(LawSchoolPage0Spider):
    name = 'law_school_page3'
    source = '23'
    publisher = '光华法学院'
    column = ['教育教学', '本科生教育', '实践环节']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16324/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16324/list.psplist%d.htm'


class LawSchoolPage4Spider(LawSchoolPage0Spider):
    name = 'law_school_page4'
    source = '23'
    publisher = '光华法学院'
    column = ['国际交流', '相关通知']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16349/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16349/list.psplist%d.htm'


class LawSchoolPage5Spider(LawSchoolPage0Spider):
    name = 'law_school_page5'
    source = '23'
    publisher = '光华法学院'
    column = ['国际交流', '遴选规则']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16350/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16350/list.psplist%d.htm'


class LawSchoolPage6Spider(LawSchoolPage0Spider):
    name = 'law_school_page6'
    source = '23'
    publisher = '光华法学院'
    column = ['国际交流', '院级项目']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16351/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16351/list.psplist%d.htm'


class LawSchoolPage7Spider(LawSchoolPage0Spider):
    name = 'law_school_page7'
    source = '23'
    publisher = '光华法学院'
    column = ['国际交流', '成果展示']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16352/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16352/list.psplist%d.htm'


class LawSchoolPage8Spider(LawSchoolPage0Spider):
    name = 'law_school_page8'
    source = '23'
    publisher = '光华法学院'
    column = ['国际交流', '院设奖学金', '相关通知']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16311/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16311/list.psplist%d.htm'


class LawSchoolPage9Spider(LawSchoolPage0Spider):
    name = 'law_school_page9'
    source = '23'
    publisher = '光华法学院'
    column = ['国际交流', '院设奖学金', '遴选规则']
    start_urls = ['https://webplus.zju.edu.cn/_s331/16312/list.psp']
    page_url = 'https://webplus.zju.edu.cn/_s331/16312/list.psplist%d.htm'
