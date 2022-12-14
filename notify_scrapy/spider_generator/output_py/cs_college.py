# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class CsCollegePage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'cs_college_page0'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['科学研究', '最新通知']
    start_urls = ['http://cspo.zju.edu.cn/27159/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27159/list%d.htm'
    initial_page = 1
    list_xpath = '//div[@id="wp_news_w7"]//div[@class="a"]'
    title_xpath = './/a/@title'
    url_xpath = './/a/@href'
    publish_time_xpath = './span/text()'
    publish_time_format = '%Y-%m-%d'
    publisher_group = '专业院系'


class CsCollegePage1Spider(CsCollegePage0Spider):
    name = 'cs_college_page1'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['科学研究', '新闻动态']
    start_urls = ['http://cspo.zju.edu.cn/27160/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27160/list%d.htm'


class CsCollegePage2Spider(CsCollegePage0Spider):
    name = 'cs_college_page2'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['科学研究', '公示信息']
    start_urls = ['http://cspo.zju.edu.cn/27161/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27161/list%d.htm'


class CsCollegePage3Spider(CsCollegePage0Spider):
    name = 'cs_college_page3'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['科学研究', '科研政策']
    start_urls = ['http://cspo.zju.edu.cn/27162/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27162/list%d.htm'


class CsCollegePage4Spider(CsCollegePage0Spider):
    name = 'cs_college_page4'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['科学研究', '办事流程']
    start_urls = ['http://cspo.zju.edu.cn/27164/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27164/list%d.htm'


class CsCollegePage5Spider(CsCollegePage0Spider):
    name = 'cs_college_page5'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['科学研究', '文件下载']
    start_urls = ['http://cspo.zju.edu.cn/27165/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27165/list%d.htm'


class CsCollegePage6Spider(CsCollegePage0Spider):
    name = 'cs_college_page6'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['本科生教育', '最新通知']
    start_urls = ['http://cspo.zju.edu.cn/29529/list.htm']
    page_url = 'http://cspo.zju.edu.cn/29529/list%d.htm'


class CsCollegePage7Spider(CsCollegePage0Spider):
    name = 'cs_college_page7'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['研究生教育', '最新通知']
    start_urls = ['http://cspo.zju.edu.cn/27169/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27169/list%d.htm'


class CsCollegePage8Spider(CsCollegePage0Spider):
    name = 'cs_college_page8'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['研究生教育', '新闻动态']
    start_urls = ['http://cspo.zju.edu.cn/27170/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27170/list%d.htm'


class CsCollegePage9Spider(CsCollegePage0Spider):
    name = 'cs_college_page9'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['研究生教育', '招生']
    start_urls = ['http://cspo.zju.edu.cn/27171/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27171/list%d.htm'


class CsCollegePage10Spider(CsCollegePage0Spider):
    name = 'cs_college_page10'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['研究生教育', '学籍与培养']
    start_urls = ['http://cspo.zju.edu.cn/27172/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27172/list%d.htm'


class CsCollegePage11Spider(CsCollegePage0Spider):
    name = 'cs_college_page11'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['研究生教育', '学位']
    start_urls = ['http://cspo.zju.edu.cn/27173/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27173/list%d.htm'


class CsCollegePage12Spider(CsCollegePage0Spider):
    name = 'cs_college_page12'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['研究生教育', '文件下载']
    start_urls = ['http://cspo.zju.edu.cn/27174/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27174/list%d.htm'


class CsCollegePage13Spider(CsCollegePage0Spider):
    name = 'cs_college_page13'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '最新消息']
    start_urls = ['http://cspo.zju.edu.cn/27175/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27175/list%d.htm'


class CsCollegePage14Spider(CsCollegePage0Spider):
    name = 'cs_college_page14'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '新闻动态']
    start_urls = ['http://cspo.zju.edu.cn/27176/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27176/list%d.htm'


class CsCollegePage15Spider(CsCollegePage0Spider):
    name = 'cs_college_page15'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '党建工作']
    start_urls = ['http://cspo.zju.edu.cn/27177/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27177/list%d.htm'


class CsCollegePage16Spider(CsCollegePage0Spider):
    name = 'cs_college_page16'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '团建工作']
    start_urls = ['http://cspo.zju.edu.cn/27178/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27178/list%d.htm'


class CsCollegePage17Spider(CsCollegePage0Spider):
    name = 'cs_college_page17'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '学生事务', '评奖评优']
    start_urls = ['http://cspo.zju.edu.cn/27183/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27183/list%d.htm'


class CsCollegePage18Spider(CsCollegePage0Spider):
    name = 'cs_college_page18'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '学生事务', '学生资助']
    start_urls = ['http://cspo.zju.edu.cn/27184/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27184/list%d.htm'


class CsCollegePage19Spider(CsCollegePage0Spider):
    name = 'cs_college_page19'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '学生事务', '勤工助学']
    start_urls = ['http://cspo.zju.edu.cn/27185/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27185/list%d.htm'


class CsCollegePage20Spider(CsCollegePage0Spider):
    name = 'cs_college_page20'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '学生组织', '本科生学生组织']
    start_urls = ['http://cspo.zju.edu.cn/27186/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27186/list%d.htm'


class CsCollegePage21Spider(CsCollegePage0Spider):
    name = 'cs_college_page21'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '学生组织', '研究生学生组织']
    start_urls = ['http://cspo.zju.edu.cn/27187/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27187/list%d.htm'


class CsCollegePage22Spider(CsCollegePage0Spider):
    name = 'cs_college_page22'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '学生活动']
    start_urls = ['http://cspo.zju.edu.cn/27181/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27181/list%d.htm'


class CsCollegePage23Spider(CsCollegePage0Spider):
    name = 'cs_college_page23'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['学生工作', '文件下载']
    start_urls = ['http://cspo.zju.edu.cn/27182/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27182/list%d.htm'


class CsCollegePage24Spider(CsCollegePage0Spider):
    name = 'cs_college_page24'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '最新通知']
    start_urls = ['http://cspo.zju.edu.cn/27197/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27197/list%d.htm'


class CsCollegePage25Spider(CsCollegePage0Spider):
    name = 'cs_college_page25'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '重点引导']
    start_urls = ['http://cspo.zju.edu.cn/27210/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27210/list%d.htm'


class CsCollegePage26Spider(CsCollegePage0Spider):
    name = 'cs_college_page26'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '新闻动态']
    start_urls = ['http://cspo.zju.edu.cn/27198/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27198/list%d.htm'


class CsCollegePage27Spider(CsCollegePage0Spider):
    name = 'cs_college_page27'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '招聘信息', '央企国企']
    start_urls = ['http://cspo.zju.edu.cn/27199/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27199/list%d.htm'


class CsCollegePage28Spider(CsCollegePage0Spider):
    name = 'cs_college_page28'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '招聘信息', '选调生']
    start_urls = ['http://cspo.zju.edu.cn/27203/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27203/list%d.htm'


class CsCollegePage29Spider(CsCollegePage0Spider):
    name = 'cs_college_page29'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '招聘信息', '事业单位']
    start_urls = ['http://cspo.zju.edu.cn/27204/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27204/list%d.htm'


class CsCollegePage30Spider(CsCollegePage0Spider):
    name = 'cs_college_page30'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '招聘信息', '高校招聘']
    start_urls = ['http://cspo.zju.edu.cn/27205/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27205/list%d.htm'


class CsCollegePage31Spider(CsCollegePage0Spider):
    name = 'cs_college_page31'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '招聘信息', '企业招聘']
    start_urls = ['http://cspo.zju.edu.cn/27206/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27206/list%d.htm'


class CsCollegePage32Spider(CsCollegePage0Spider):
    name = 'cs_college_page32'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '实习招聘', '重点企业']
    start_urls = ['http://cspo.zju.edu.cn/27207/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27207/list%d.htm'


class CsCollegePage33Spider(CsCollegePage0Spider):
    name = 'cs_college_page33'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '实习招聘', '一般企业']
    start_urls = ['http://cspo.zju.edu.cn/27208/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27208/list%d.htm'


class CsCollegePage34Spider(CsCollegePage0Spider):
    name = 'cs_college_page34'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '职业生涯规划', '就业之星推荐']
    start_urls = ['http://cspo.zju.edu.cn/27209/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27209/list%d.htm'


class CsCollegePage35Spider(CsCollegePage0Spider):
    name = 'cs_college_page35'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '职业生涯规划', '职业规划咨询']
    start_urls = ['http://cspo.zju.edu.cn/27211/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27211/list%d.htm'


class CsCollegePage36Spider(CsCollegePage0Spider):
    name = 'cs_college_page36'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '职业生涯规划', '政策法规']
    start_urls = ['http://cspo.zju.edu.cn/27212/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27212/list%d.htm'


class CsCollegePage37Spider(CsCollegePage0Spider):
    name = 'cs_college_page37'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['就业工作', '职业生涯规划', '文件下载']
    start_urls = ['http://cspo.zju.edu.cn/27213/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27213/list%d.htm'


class CsCollegePage38Spider(CsCollegePage0Spider):
    name = 'cs_college_page38'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '学生国际交流', '交流动态']
    start_urls = ['http://cspo.zju.edu.cn/27214/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27214/list%d.htm'


class CsCollegePage39Spider(CsCollegePage0Spider):
    name = 'cs_college_page39'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '学生国际交流', '服务指南']
    start_urls = ['http://cspo.zju.edu.cn/27222/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27222/list%d.htm'


class CsCollegePage40Spider(CsCollegePage0Spider):
    name = 'cs_college_page40'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '学生国际交流', '项目一览']
    start_urls = ['http://cspo.zju.edu.cn/27220/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27220/list%d.htm'


class CsCollegePage41Spider(CsCollegePage0Spider):
    name = 'cs_college_page41'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '教师国际交流', '内部公示']
    start_urls = ['http://cspo.zju.edu.cn/27223/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27223/list%d.htm'


class CsCollegePage42Spider(CsCollegePage0Spider):
    name = 'cs_college_page42'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '教师国际交流', '服务指南']
    start_urls = ['http://cspo.zju.edu.cn/27224/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27224/list%d.htm'


class CsCollegePage43Spider(CsCollegePage0Spider):
    name = 'cs_college_page43'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '合作交流动态']
    start_urls = ['http://cspo.zju.edu.cn/27216/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27216/list%d.htm'


class CsCollegePage44Spider(CsCollegePage0Spider):
    name = 'cs_college_page44'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '学术讲座']
    start_urls = ['http://cspo.zju.edu.cn/27217/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27217/list%d.htm'


class CsCollegePage45Spider(CsCollegePage0Spider):
    name = 'cs_college_page45'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '外国专家']
    start_urls = ['http://cspo.zju.edu.cn/27218/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27218/list%d.htm'


class CsCollegePage46Spider(CsCollegePage0Spider):
    name = 'cs_college_page46'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['国际交流', '国际会议']
    start_urls = ['http://cspo.zju.edu.cn/27219/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27219/list%d.htm'


class CsCollegePage47Spider(CsCollegePage0Spider):
    name = 'cs_college_page47'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['发展中心', '最新通知']
    start_urls = ['http://cspo.zju.edu.cn/27225/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27225/list%d.htm'


class CsCollegePage48Spider(CsCollegePage0Spider):
    name = 'cs_college_page48'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['发展中心', '新闻动态']
    start_urls = ['http://cspo.zju.edu.cn/27226/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27226/list%d.htm'


class CsCollegePage49Spider(CsCollegePage0Spider):
    name = 'cs_college_page49'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['发展中心', '学科竞赛']
    start_urls = ['http://cspo.zju.edu.cn/27228/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27228/list%d.htm'


class CsCollegePage50Spider(CsCollegePage0Spider):
    name = 'cs_college_page50'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['发展中心', '信息公告']
    start_urls = ['http://cspo.zju.edu.cn/27232/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27232/list%d.htm'


class CsCollegePage51Spider(CsCollegePage0Spider):
    name = 'cs_college_page51'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['综合服务', '服务指南', '综合服务']
    start_urls = ['http://cspo.zju.edu.cn/27235/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27235/list%d.htm'


class CsCollegePage52Spider(CsCollegePage0Spider):
    name = 'cs_college_page52'
    source = '10'
    publisher = '计算机科学与技术学院'
    column = ['综合服务', '服务指南', '科学研究']
    start_urls = ['http://cspo.zju.edu.cn/27237/list.htm']
    page_url = 'http://cspo.zju.edu.cn/27237/list%d.htm'
