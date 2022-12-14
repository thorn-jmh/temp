# HTML Spider Generator version 3.3
# --------------------------------
# This file is automatically generated by HTML spider generator, a tool used to generate spider.
# Please copy or move this file to notify_scrapy/spiders and test to make sure it can fetch notices
# properly before deploying it.
# It is not recommended to modify this file directly. If the spider does not work properly, please
# check if it is outdated. Current version of spider can be find in Spider's properties.

from notify_scrapy.base_html_spider import BaseHTMLSpider


class CseCollegePage0Spider(BaseHTMLSpider):
    generator_version = '3.3'
    name = 'cse_college_page0'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['党建工作', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055823']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055823&page=%d'
    initial_page = 0
    list_xpath = '//div[@class="con1rm2 mg2"]/ul/li'
    title_xpath = './/a/@title'
    url_xpath = './/a/@href'
    publish_time_xpath = './div[@class="con1rm2l xi20"]/text()'
    publish_time_format = ' \n\r\t\t%Y-%m-%d'
    publisher_group = '专业院系'


class CseCollegePage1Spider(CseCollegePage0Spider):
    name = 'cse_college_page1'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['党建工作', '活动简讯']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055824']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055824&page=%d'


class CseCollegePage2Spider(CseCollegePage0Spider):
    name = 'cse_college_page2'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['党建工作', '学习园地']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055826']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055826&page=%d'


class CseCollegePage3Spider(CseCollegePage0Spider):
    name = 'cse_college_page3'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['党建工作', '党风党纪']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055827']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055827&page=%d'


class CseCollegePage4Spider(CseCollegePage0Spider):
    name = 'cse_college_page4'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['党建工作', '下载专区']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055828']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055828&page=%d'


class CseCollegePage5Spider(CseCollegePage0Spider):
    name = 'cse_college_page5'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['人事工作', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1063014']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1063014&page=%d'


class CseCollegePage6Spider(CseCollegePage0Spider):
    name = 'cse_college_page6'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['人事工作', '人事文件']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1063015']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1063015&page=%d'


class CseCollegePage7Spider(CseCollegePage0Spider):
    name = 'cse_college_page7'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['人事工作', '招聘信息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1063017']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1063017&page=%d'


class CseCollegePage8Spider(CseCollegePage0Spider):
    name = 'cse_college_page8'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['科研学术', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055783']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055783&page=%d'


class CseCollegePage9Spider(CseCollegePage0Spider):
    name = 'cse_college_page9'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['科研学术', '科研政策']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055785']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055785&page=%d'


class CseCollegePage10Spider(CseCollegePage0Spider):
    name = 'cse_college_page10'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['科研学术', '科研项目']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055787']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055787&page=%d'


class CseCollegePage11Spider(CseCollegePage0Spider):
    name = 'cse_college_page11'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['科研学术', '成果奖励']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055786']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055786&page=%d'


class CseCollegePage12Spider(CseCollegePage0Spider):
    name = 'cse_college_page12'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['科研学术', '表格下载']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055788']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055788&page=%d'


class CseCollegePage13Spider(CseCollegePage0Spider):
    name = 'cse_college_page13'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['科研学术', '服务指南']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055789']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055789&page=%d'


class CseCollegePage14Spider(CseCollegePage0Spider):
    name = 'cse_college_page14'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['科研学术', '科技创新论坛']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055790']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055790&page=%d'


class CseCollegePage15Spider(CseCollegePage0Spider):
    name = 'cse_college_page15'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['科研学术', '视频论坛']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1115104']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1115104&page=%d'


class CseCollegePage16Spider(CseCollegePage0Spider):
    name = 'cse_college_page16'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055813']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055813&page=%d'


class CseCollegePage17Spider(CseCollegePage0Spider):
    name = 'cse_college_page17'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '招生消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055814']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055814&page=%d'


class CseCollegePage18Spider(CseCollegePage0Spider):
    name = 'cse_college_page18'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '培养方案']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055815']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055815&page=%d'


class CseCollegePage19Spider(CseCollegePage0Spider):
    name = 'cse_college_page19'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '文件汇编']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055816']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055816&page=%d'


class CseCollegePage20Spider(CseCollegePage0Spider):
    name = 'cse_college_page20'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '科研训练']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055817']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055817&page=%d'


class CseCollegePage21Spider(CseCollegePage0Spider):
    name = 'cse_college_page21'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '对外交流']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055818']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055818&page=%d'


class CseCollegePage22Spider(CseCollegePage0Spider):
    name = 'cse_college_page22'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '短学期']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055819']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055819&page=%d'


class CseCollegePage23Spider(CseCollegePage0Spider):
    name = 'cse_college_page23'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '毕业设计']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055820']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055820&page=%d'


class CseCollegePage24Spider(CseCollegePage0Spider):
    name = 'cse_college_page24'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['本科生教育', '表格下载']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055821']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055821&page=%d'


class CseCollegePage25Spider(CseCollegePage0Spider):
    name = 'cse_college_page25'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055842']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055842&page=%d'


class CseCollegePage26Spider(CseCollegePage0Spider):
    name = 'cse_college_page26'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '学位管理']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055843']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055843&page=%d'


class CseCollegePage27Spider(CseCollegePage0Spider):
    name = 'cse_college_page27'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '招生信息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055845']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055845&page=%d'


class CseCollegePage28Spider(CseCollegePage0Spider):
    name = 'cse_college_page28'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '文件汇编']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055848']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055848&page=%d'


class CseCollegePage29Spider(CseCollegePage0Spider):
    name = 'cse_college_page29'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '工程硕士', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1076492']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1076492&page=%d'


class CseCollegePage30Spider(CseCollegePage0Spider):
    name = 'cse_college_page30'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '工程硕士', '下载服务']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1076494']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1076494&page=%d'


class CseCollegePage31Spider(CseCollegePage0Spider):
    name = 'cse_college_page31'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '表格下载']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055850']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055850&page=%d'


class CseCollegePage32Spider(CseCollegePage0Spider):
    name = 'cse_college_page32'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '服务指南']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055851']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055851&page=%d'


class CseCollegePage33Spider(CseCollegePage0Spider):
    name = 'cse_college_page33'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['研究生教育', '校企合作']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1134005']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1134005&page=%d'


class CseCollegePage34Spider(CseCollegePage0Spider):
    name = 'cse_college_page34'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['学生思政', '日常通告']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055856']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055856&page=%d'


class CseCollegePage35Spider(CseCollegePage0Spider):
    name = 'cse_college_page35'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['学生思政', '党建相关']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055855']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055855&page=%d'


class CseCollegePage36Spider(CseCollegePage0Spider):
    name = 'cse_college_page36'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['学生思政', '评奖评优']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055857']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055857&page=%d'


class CseCollegePage37Spider(CseCollegePage0Spider):
    name = 'cse_college_page37'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['学生思政', '勤工资助']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055857']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055857&page=%d'


class CseCollegePage38Spider(CseCollegePage0Spider):
    name = 'cse_college_page38'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['学生思政', '消息链接']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055863']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055863&page=%d'


class CseCollegePage39Spider(CseCollegePage0Spider):
    name = 'cse_college_page39'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['学生思政', '表格规范']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055862']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055862&page=%d'


class CseCollegePage40Spider(CseCollegePage0Spider):
    name = 'cse_college_page40'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['学生思政', '文件汇编']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055854']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055854&page=%d'


class CseCollegePage41Spider(CseCollegePage0Spider):
    name = 'cse_college_page41'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['就业指导', '相关通知']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055865']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055865&page=%d'


class CseCollegePage42Spider(CseCollegePage0Spider):
    name = 'cse_college_page42'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['就业指导', '就业信息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055866']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055866&page=%d'


class CseCollegePage43Spider(CseCollegePage0Spider):
    name = 'cse_college_page43'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['对外交流', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055867']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055867&page=%d'


class CseCollegePage44Spider(CseCollegePage0Spider):
    name = 'cse_college_page44'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['对外交流', '外事动态']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055868']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055868&page=%d'


class CseCollegePage45Spider(CseCollegePage0Spider):
    name = 'cse_college_page45'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['对外交流', '表格下载']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1055869']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1055869&page=%d'


class CseCollegePage46Spider(CseCollegePage0Spider):
    name = 'cse_college_page46'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['党政综合', '党政办', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1057225']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1057225&page=%d'


class CseCollegePage47Spider(CseCollegePage0Spider):
    name = 'cse_college_page47'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['党政综合', '实验室安全', '信息公告']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1057653']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1057653&page=%d'


class CseCollegePage48Spider(CseCollegePage0Spider):
    name = 'cse_college_page48'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['党政综合', '实验室安全', '规章制度']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1057654']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1057654&page=%d'


class CseCollegePage49Spider(CseCollegePage0Spider):
    name = 'cse_college_page49'
    source = '11'
    publisher = '控制科学与工程学院'
    column = ['大平台', '最新消息']
    start_urls = ['http://www.cse.zju.edu.cn/redir.php?catalog_id=1135089']
    page_url = 'http://www.cse.zju.edu.cn/redir.php?catalog_id=1135089&page=%d'
