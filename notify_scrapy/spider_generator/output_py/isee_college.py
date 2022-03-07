# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class IseeCollegePage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'isee_college_page0'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '本科生教育', '培养方案']
    start_urls = ['http://www.isee.zju.edu.cn/21061/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21061/list%d.htm'
    initial_page = 1
    list_xpath = '//div[@id="wp_news_w10"]/li[@class="list_guild"]'
    title_xpath = './/div[@class="list_content"]//a/@title'
    url_xpath = './/div[@class="list_content"]//a/@href'
    publish_time_xpath = 'custom'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '专业院系'


class IseeCollegePage1Spider(IseeCollegePage0Spider):
    name = 'isee_college_page1'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '本科生教育', '管理文件']
    start_urls = ['http://www.isee.zju.edu.cn/21062/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21062/list%d.htm'


class IseeCollegePage2Spider(IseeCollegePage0Spider):
    name = 'isee_college_page2'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '本科生教育', '表格下载']
    start_urls = ['http://www.isee.zju.edu.cn/21063/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21063/list%d.htm'


class IseeCollegePage3Spider(IseeCollegePage0Spider):
    name = 'isee_college_page3'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '研究生教育', '培养方案']
    start_urls = ['http://www.isee.zju.edu.cn/21064/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21064/list%d.htm'


class IseeCollegePage4Spider(IseeCollegePage0Spider):
    name = 'isee_college_page4'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '研究生教育', '学位申请']
    start_urls = ['http://www.isee.zju.edu.cn/21065/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21065/list%d.htm'


class IseeCollegePage5Spider(IseeCollegePage0Spider):
    name = 'isee_college_page5'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '研究生教育', '学位论文']
    start_urls = ['http://www.isee.zju.edu.cn/21066/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21066/list%d.htm'


class IseeCollegePage6Spider(IseeCollegePage0Spider):
    name = 'isee_college_page6'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '研究生教育', '文件汇编']
    start_urls = ['http://www.isee.zju.edu.cn/21067/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21067/list%d.htm'


class IseeCollegePage7Spider(IseeCollegePage0Spider):
    name = 'isee_college_page7'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '研究生教育', '表格下载']
    start_urls = ['http://www.isee.zju.edu.cn/21068/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21068/list%d.htm'


class IseeCollegePage8Spider(IseeCollegePage0Spider):
    name = 'isee_college_page8'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '学子在线', '本科生']
    start_urls = ['http://www.isee.zju.edu.cn/21081/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21081/list%d.htm'


class IseeCollegePage9Spider(IseeCollegePage0Spider):
    name = 'isee_college_page9'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '学子在线', '研究生', '党团建设']
    start_urls = ['http://www.isee.zju.edu.cn/21082/list.psp']
    page_url = 'http://www.isee.zju.edu.cn/21082/list.psplist%d.htm'


class IseeCollegePage10Spider(IseeCollegePage0Spider):
    name = 'isee_college_page10'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '学子在线', '新闻动态']
    start_urls = ['http://www.isee.zju.edu.cn/xwdt/list.psp']
    page_url = 'http://www.isee.zju.edu.cn/xwdt/list.psplist%d.htm'


class IseeCollegePage11Spider(IseeCollegePage0Spider):
    name = 'isee_college_page11'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['教学思政', '工程硕士']
    start_urls = ['http://www.isee.zju.edu.cn/21070/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21070/list%d.htm'


class IseeCollegePage12Spider(IseeCollegePage0Spider):
    name = 'isee_college_page12'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['招生工作', '本科生招生', '招生信息']
    start_urls = ['http://www.isee.zju.edu.cn/21107/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21107/list%d.htm'


class IseeCollegePage13Spider(IseeCollegePage0Spider):
    name = 'isee_college_page13'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['招生工作', '研究生招生', '招生信息']
    start_urls = ['http://www.isee.zju.edu.cn/21109/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21109/list%d.htm'


class IseeCollegePage14Spider(IseeCollegePage0Spider):
    name = 'isee_college_page14'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['就业工作', '招聘信息']
    start_urls = ['http://www.isee.zju.edu.cn/21110/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21110/list%d.htm'


class IseeCollegePage15Spider(IseeCollegePage0Spider):
    name = 'isee_college_page15'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['就业工作', '就业新闻']
    start_urls = ['http://www.isee.zju.edu.cn/jyxw/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/jyxw/list%d.htm'


class IseeCollegePage16Spider(IseeCollegePage0Spider):
    name = 'isee_college_page16'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['就业工作', '生涯辅导', '经验交流']
    start_urls = ['http://www.isee.zju.edu.cn/jyjl/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/jyjl/list%d.htm'


class IseeCollegePage17Spider(IseeCollegePage0Spider):
    name = 'isee_college_page17'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['就业工作', '生涯辅导', '就业出口']
    start_urls = ['http://www.isee.zju.edu.cn/21112/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21112/list%d.htm'


class IseeCollegePage18Spider(IseeCollegePage0Spider):
    name = 'isee_college_page18'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['就业工作', '生涯辅导', '文件表格']
    start_urls = ['http://www.isee.zju.edu.cn/21113/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21113/list%d.htm'


class IseeCollegePage19Spider(IseeCollegePage0Spider):
    name = 'isee_college_page19'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['国际交流', '交流动态']
    start_urls = ['http://www.isee.zju.edu.cn/50899/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/50899/list%d.htm'


class IseeCollegePage20Spider(IseeCollegePage0Spider):
    name = 'isee_college_page20'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['继续教育', '新闻动态']
    start_urls = ['http://www.isee.zju.edu.cn/50904/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/50904/list%d.htm'


class IseeCollegePage21Spider(IseeCollegePage0Spider):
    name = 'isee_college_page21'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['继续教育', '招生信息']
    start_urls = ['http://www.isee.zju.edu.cn/21069/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21069/list%d.htm'


class IseeCollegePage22Spider(IseeCollegePage0Spider):
    name = 'isee_college_page22'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['继续教育', '工程硕士']
    start_urls = ['http://www.isee.zju.edu.cn/50906/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/50906/list%d.htm'


class IseeCollegePage23Spider(IseeCollegePage0Spider):
    name = 'isee_college_page23'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['继续教育', '培训项目']
    start_urls = ['http://www.isee.zju.edu.cn/21071/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21071/list%d.htm'


class IseeCollegePage24Spider(IseeCollegePage0Spider):
    name = 'isee_college_page24'
    source = '20'
    publisher = '信息与电子工程学院'
    column = ['继续教育', '表格下载']
    start_urls = ['http://www.isee.zju.edu.cn/21072/list.htm']
    page_url = 'http://www.isee.zju.edu.cn/21072/list%d.htm'