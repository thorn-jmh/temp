# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class MechanicalEngineeringSchoolPage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'mechanical_engineering_school_page0'
    source = '30'
    publisher = '机械工程学院'
    column = ['学院新闻']
    start_urls = ['http://me.zju.edu.cn/meoffice/xyxw/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/xyxw/list%d.htm'
    initial_page = 1
    list_xpath = '//div[@id="wp_news_w9"]/ul//li'
    title_xpath = './/a/@title'
    url_xpath = './/a/@href'
    publish_time_xpath = './/span[@class="column-news-date news-date-hide"]/text()'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '专业院系'


class MechanicalEngineeringSchoolPage1Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page1'
    source = '30'
    publisher = '机械工程学院'
    column = ['通知公告']
    start_urls = ['http://me.zju.edu.cn/meoffice/tzgg/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/tzgg/list%d.htm'


class MechanicalEngineeringSchoolPage2Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page2'
    source = '30'
    publisher = '机械工程学院'
    column = ['学术报告']
    start_urls = ['http://me.zju.edu.cn/meoffice/xsbg/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/xsbg/list%d.htm'


class MechanicalEngineeringSchoolPage3Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page3'
    source = '30'
    publisher = '机械工程学院'
    column = ['本科生教育', '重要通知']
    start_urls = ['http://me.zju.edu.cn/meoffice/6427/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/6427/list%d.htm'


class MechanicalEngineeringSchoolPage4Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page4'
    source = '30'
    publisher = '机械工程学院'
    column = ['本科生教育', '规章制度']
    start_urls = ['http://me.zju.edu.cn/meoffice/gzzd/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/gzzd/list%d.htm'


class MechanicalEngineeringSchoolPage5Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page5'
    source = '30'
    publisher = '机械工程学院'
    column = ['本科生教育', '主修专业确认']
    start_urls = ['http://me.zju.edu.cn/meoffice/zyqr/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/zyqr/list%d.htm'


class MechanicalEngineeringSchoolPage6Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page6'
    source = '30'
    publisher = '机械工程学院'
    column = ['本科生教育', '推荐免试研究生']
    start_urls = ['http://me.zju.edu.cn/meoffice/tjmsyjs/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/tjmsyjs/list%d.htm'


class MechanicalEngineeringSchoolPage7Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page7'
    source = '30'
    publisher = '机械工程学院'
    column = ['本科生教育', '毕业生管理']
    start_urls = ['http://me.zju.edu.cn/meoffice/bysgl/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/bysgl/list%d.htm'


class MechanicalEngineeringSchoolPage8Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page8'
    source = '30'
    publisher = '机械工程学院'
    column = ['本科生教育', '实践教学', '科研竞赛']
    start_urls = ['http://me.zju.edu.cn/meoffice/kyjs/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/kyjs/list%d.htm'


class MechanicalEngineeringSchoolPage9Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page9'
    source = '30'
    publisher = '机械工程学院'
    column = ['本科生教育', '实践教学', '实习']
    start_urls = ['http://me.zju.edu.cn/meoffice/sx/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/sx/list%d.htm'


class MechanicalEngineeringSchoolPage10Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page10'
    source = '30'
    publisher = '机械工程学院'
    column = ['本科生教育', '实践教学', '毕业论文(设计']
    start_urls = ['http://me.zju.edu.cn/meoffice/bylwwsjw/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/bylwwsjw/list%d.htm'


class MechanicalEngineeringSchoolPage11Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page11'
    source = '30'
    publisher = '机械工程学院'
    column = ['科学研究', '重要通知']
    start_urls = ['http://me.zju.edu.cn/meoffice/6450/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/6450/list%d.htm'


class MechanicalEngineeringSchoolPage12Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page12'
    source = '30'
    publisher = '机械工程学院'
    column = ['科学研究', '学生工作', '重要通知']
    start_urls = ['http://me.zju.edu.cn/meoffice/6469/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/6469/list%d.htm'


class MechanicalEngineeringSchoolPage13Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page13'
    source = '30'
    publisher = '机械工程学院'
    column = ['科学研究', '学生工作', '学生三会']
    start_urls = ['http://me.zju.edu.cn/meoffice/6472/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/6472/list%d.htm'


class MechanicalEngineeringSchoolPage14Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page14'
    source = '30'
    publisher = '机械工程学院'
    column = ['科学研究', '学生工作', '奖贷三助']
    start_urls = ['http://me.zju.edu.cn/meoffice/6473/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/6473/list%d.htm'


class MechanicalEngineeringSchoolPage15Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page15'
    source = '30'
    publisher = '机械工程学院'
    column = ['科学研究', '学生工作', '思政工作']
    start_urls = ['http://me.zju.edu.cn/meoffice/6474/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/6474/list%d.htm'


class MechanicalEngineeringSchoolPage16Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page16'
    source = '30'
    publisher = '机械工程学院'
    column = ['科学研究', '学生工作', '荣誉成果']
    start_urls = ['http://me.zju.edu.cn/meoffice/rycg/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/rycg/list%d.htm'


class MechanicalEngineeringSchoolPage17Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page17'
    source = '30'
    publisher = '机械工程学院'
    column = ['国际交流', '通知公告']
    start_urls = ['http://me.zju.edu.cn/meoffice/tzgg_42656/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/tzgg_42656/list%d.htm'


class MechanicalEngineeringSchoolPage18Spider(MechanicalEngineeringSchoolPage0Spider):
    name = 'mechanical_engineering_school_page18'
    source = '30'
    publisher = '机械工程学院'
    column = ['国际交流', '最新动态']
    start_urls = ['http://me.zju.edu.cn/meoffice/6477/list.htm']
    page_url = 'http://me.zju.edu.cn/meoffice/6477/list%d.htm'
