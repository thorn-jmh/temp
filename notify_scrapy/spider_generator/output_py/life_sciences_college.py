# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class LifeSciencesCollegePage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'life_sciences_college_page0'
    source = '25'
    publisher = '生命科学学院'
    column = ['本科生教育', '本科通知']
    start_urls = ['http://www.cls.office.zju.edu.cn/25871/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/25871/list%d.htm'
    initial_page = 0
    list_xpath = '//ul[@class="cg-news-list"]/li'
    title_xpath = './/a/@title'
    url_xpath = './/a/@href'
    publish_time_xpath = './/span[@class="art-date"]/text()'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '专业院系'


class LifeSciencesCollegePage1Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page1'
    source = '25'
    publisher = '生命科学学院'
    column = ['本科生教育', '专业培养']
    start_urls = ['http://www.cls.office.zju.edu.cn/25872/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/25872/list%d.htm'


class LifeSciencesCollegePage2Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page2'
    source = '25'
    publisher = '生命科学学院'
    column = ['本科生教育', '教学动态']
    start_urls = ['http://www.cls.office.zju.edu.cn/25873/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/25873/list%d.htm'


class LifeSciencesCollegePage3Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page3'
    source = '25'
    publisher = '生命科学学院'
    column = ['本科生教育', '服务信息']
    start_urls = ['http://www.cls.office.zju.edu.cn/25874/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/25874/list%d.htm'


class LifeSciencesCollegePage4Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page4'
    source = '25'
    publisher = '生命科学学院'
    column = ['本科生教育', '海外交流']
    start_urls = ['http://www.cls.office.zju.edu.cn/25875/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/25875/list%d.htm'


class LifeSciencesCollegePage5Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page5'
    source = '25'
    publisher = '生命科学学院'
    column = ['学院动态']
    start_urls = ['http://www.cls.office.zju.edu.cn/25819/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/25819/list%d.htm'


class LifeSciencesCollegePage6Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page6'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '队伍风采']
    start_urls = ['http://www.cls.office.zju.edu.cn/dwfc/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/dwfc/list%d.htm'


class LifeSciencesCollegePage7Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page7'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '学生党建', '政策文件']
    start_urls = ['http://www.cls.office.zju.edu.cn/zcwj_44494/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/zcwj_44494/list%d.htm'


class LifeSciencesCollegePage8Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page8'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '学生党建', '组织设置']
    start_urls = ['http://www.cls.office.zju.edu.cn/zzsz_44495/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/zzsz_44495/list%d.htm'


class LifeSciencesCollegePage9Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page9'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '学生党建', '公示公告']
    start_urls = ['http://www.cls.office.zju.edu.cn/gsgg/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/gsgg/list%d.htm'


class LifeSciencesCollegePage10Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page10'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '学生党建', '支部动态']
    start_urls = ['http://www.cls.office.zju.edu.cn/zbdt/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/zbdt/list%d.htm'


class LifeSciencesCollegePage11Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page11'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '青春团学', '组织设置']
    start_urls = ['http://www.cls.office.zju.edu.cn/zzsz_44498/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/zzsz_44498/list%d.htm'


class LifeSciencesCollegePage12Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page12'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '青春团学', '青春动态']
    start_urls = ['http://www.cls.office.zju.edu.cn/qcdt/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/qcdt/list%d.htm'


class LifeSciencesCollegePage13Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page13'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '青春团学', '实践服务']
    start_urls = ['http://www.cls.office.zju.edu.cn/sjfw/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/sjfw/list%d.htm'


class LifeSciencesCollegePage14Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page14'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '青春团学', '创新创业']
    start_urls = ['http://www.cls.office.zju.edu.cn/cxcy/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/cxcy/list%d.htm'


class LifeSciencesCollegePage15Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page15'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '青春团学', '文艺体育']
    start_urls = ['http://www.cls.office.zju.edu.cn/wyty/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/wyty/list%d.htm'


class LifeSciencesCollegePage16Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page16'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '学生事务', '文件汇编']
    start_urls = ['http://www.cls.office.zju.edu.cn/wjhb/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/wjhb/list%d.htm'


class LifeSciencesCollegePage17Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page17'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '学生事务', '评奖评优']
    start_urls = ['http://www.cls.office.zju.edu.cn/pjpy/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/pjpy/list%d.htm'


class LifeSciencesCollegePage18Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page18'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '学生事务', '勤工助贷']
    start_urls = ['http://www.cls.office.zju.edu.cn/qgzd/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/qgzd/list%d.htm'


class LifeSciencesCollegePage19Spider(LifeSciencesCollegePage0Spider):
    name = 'life_sciences_college_page19'
    source = '25'
    publisher = '生命科学学院'
    column = ['学生思政', '学生事务', '心理健康']
    start_urls = ['http://www.cls.office.zju.edu.cn/xljk/list.htm']
    page_url = 'http://www.cls.office.zju.edu.cn/xljk/list%d.htm'