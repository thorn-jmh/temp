# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class PsychologyDepartPage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'psychology_depart_page0'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['本科生教育', '最新通知']
    start_urls = ['http://www.psych.zju.edu.cn/27653/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27653/list%d.htm'
    initial_page = 1
    list_xpath = '//div[@id="wp_news_w6"]/ul/li'
    title_xpath = './/a/text()'
    url_xpath = './/a/@href'
    publish_time_xpath = './/span/text()'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '专业院系'


class PsychologyDepartPage1Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page1'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['本科生教育', '新闻动态']
    start_urls = ['http://www.psych.zju.edu.cn/27654/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27654/list%d.htm'


class PsychologyDepartPage2Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page2'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['本科生教育', '培养方案']
    start_urls = ['http://www.psych.zju.edu.cn/27655/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27655/list%d.htm'


class PsychologyDepartPage3Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page3'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['本科生教育', '规章制度']
    start_urls = ['http://www.psych.zju.edu.cn/27656/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27656/list%d.htm'


class PsychologyDepartPage4Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page4'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['本科生教育', '学生科研']
    start_urls = ['http://www.psych.zju.edu.cn/27657/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27657/list%d.htm'


class PsychologyDepartPage5Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page5'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['科学研究', '学生活动']
    start_urls = ['http://www.psych.zju.edu.cn/27619/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27619/list%d.htm'


class PsychologyDepartPage6Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page6'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['科学研究', '学术成果']
    start_urls = ['http://www.psych.zju.edu.cn/27620/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27620/list%d.htm'


class PsychologyDepartPage7Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page7'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['科学研究', '学术日历']
    start_urls = ['http://www.psych.zju.edu.cn/xsrl/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/xsrl/list%d.htm'


class PsychologyDepartPage8Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page8'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['学生天地', '新闻动态']
    start_urls = ['http://www.psych.zju.edu.cn/27623/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27623/list%d.htm'


class PsychologyDepartPage9Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page9'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['学生天地', '团建园地']
    start_urls = ['http://www.psych.zju.edu.cn/27624/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27624/list%d.htm'


class PsychologyDepartPage10Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page10'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['学生天地', '评奖评优']
    start_urls = ['http://www.psych.zju.edu.cn/27625/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27625/list%d.htm'


class PsychologyDepartPage11Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page11'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['学生天地', '学生资助']
    start_urls = ['http://www.psych.zju.edu.cn/27626/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27626/list%d.htm'


class PsychologyDepartPage12Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page12'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['学生天地', '学生组织']
    start_urls = ['http://www.psych.zju.edu.cn/27627/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27627/list%d.htm'


class PsychologyDepartPage13Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page13'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['国际交流', '新闻动态']
    start_urls = ['http://www.psych.zju.edu.cn/27641/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27641/list%d.htm'


class PsychologyDepartPage14Spider(PsychologyDepartPage0Spider):
    name = 'psychology_depart_page14'
    source = '37'
    publisher = '心理与行为科学系'
    column = ['国际交流', '最新通知']
    start_urls = ['http://www.psych.zju.edu.cn/27640/list.htm']
    page_url = 'http://www.psych.zju.edu.cn/27640/list%d.htm'