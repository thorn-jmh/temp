# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class EconomicsSchoolPage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'economics_school_page0'
    source = '14'
    publisher = '经济学院'
    column = ['学院党政', '会议通知']
    start_urls = ['http://www.cec.zju.edu.cn/hytz_36106/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/hytz_36106/list%d.htm'
    initial_page = 1
    list_xpath = '//ul[@class="list-items"]/li'
    title_xpath = './/a/text()'
    url_xpath = './/a/@href'
    publish_time_xpath = './/i/text()'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '专业院系'


class EconomicsSchoolPage1Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page1'
    source = '14'
    publisher = '经济学院'
    column = ['学院党政', '会议纪要']
    start_urls = ['http://www.cec.zju.edu.cn/hyjy/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/hyjy/list%d.htm'


class EconomicsSchoolPage2Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page2'
    source = '14'
    publisher = '经济学院'
    column = ['学院党政', '学院发文']
    start_urls = ['http://www.cec.zju.edu.cn/xyfw/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/xyfw/list%d.htm'


class EconomicsSchoolPage3Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page3'
    source = '14'
    publisher = '经济学院'
    column = ['学院党政', '党务工作']
    start_urls = ['http://www.cec.zju.edu.cn/dwgz/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/dwgz/list%d.htm'


class EconomicsSchoolPage4Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page4'
    source = '14'
    publisher = '经济学院'
    column = ['学院党政', '工会之声']
    start_urls = ['http://www.cec.zju.edu.cn/ghzs/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/ghzs/list%d.htm'


class EconomicsSchoolPage5Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page5'
    source = '14'
    publisher = '经济学院'
    column = ['学院党政', '理论学习']
    start_urls = ['http://www.cec.zju.edu.cn/llxx/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/llxx/list%d.htm'


class EconomicsSchoolPage6Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page6'
    source = '14'
    publisher = '经济学院'
    column = ['学院党政', '平安学院']
    start_urls = ['http://www.cec.zju.edu.cn/paxy/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/paxy/list%d.htm'


class EconomicsSchoolPage7Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page7'
    source = '14'
    publisher = '经济学院'
    column = ['本科生教育', '最新消息']
    start_urls = ['http://www.cec.zju.edu.cn/zxxx/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/zxxx/list%d.htm'


class EconomicsSchoolPage8Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page8'
    source = '14'
    publisher = '经济学院'
    column = ['规章制度', '文件汇编']
    start_urls = ['http://www.cec.zju.edu.cn/wjhb_36403/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/wjhb_36403/list%d.htm'


class EconomicsSchoolPage9Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page9'
    source = '14'
    publisher = '经济学院'
    column = ['规章制度', '会议纪要']
    start_urls = ['http://www.cec.zju.edu.cn/hyjy_36404/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/hyjy_36404/list%d.htm'


class EconomicsSchoolPage10Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page10'
    source = '14'
    publisher = '经济学院'
    column = ['规章制度', '办事流程']
    start_urls = ['http://www.cec.zju.edu.cn/bslc/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/bslc/list%d.htm'


class EconomicsSchoolPage11Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page11'
    source = '14'
    publisher = '经济学院'
    column = ['招生信息']
    start_urls = ['http://www.cec.zju.edu.cn/zsxx/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/zsxx/list%d.htm'


class EconomicsSchoolPage12Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page12'
    source = '14'
    publisher = '经济学院'
    column = ['主修专业确认']
    start_urls = ['http://www.cec.zju.edu.cn/zxzyqr/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/zxzyqr/list%d.htm'


class EconomicsSchoolPage13Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page13'
    source = '14'
    publisher = '经济学院'
    column = ['学籍管理']
    start_urls = ['http://www.cec.zju.edu.cn/xjgl/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/xjgl/list%d.htm'


class EconomicsSchoolPage14Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page14'
    source = '14'
    publisher = '经济学院'
    column = ['教学与教务']
    start_urls = ['http://www.cec.zju.edu.cn/jxyjw/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/jxyjw/list%d.htm'


class EconomicsSchoolPage15Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page15'
    source = '14'
    publisher = '经济学院'
    column = ['毕业论文']
    start_urls = ['http://www.cec.zju.edu.cn/bylw/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/bylw/list%d.htm'


class EconomicsSchoolPage16Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page16'
    source = '14'
    publisher = '经济学院'
    column = ['科研训练']
    start_urls = ['http://www.cec.zju.edu.cn/kyxl/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/kyxl/list%d.htm'


class EconomicsSchoolPage17Spider(EconomicsSchoolPage0Spider):
    name = 'economics_school_page17'
    source = '14'
    publisher = '经济学院'
    column = ['实习实践']
    start_urls = ['http://www.cec.zju.edu.cn/sxsj/list.htm']
    page_url = 'http://www.cec.zju.edu.cn/sxsj/list%d.htm'